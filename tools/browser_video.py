# -*- coding: utf-8 -*-
"""Drive the ElevenLabs Image & Video web workspace in Camoufox to make one clip.

Setup, once, from the user's own terminal (never from an agent):
    pip install -U "camoufox[geoip]"
    python -m camoufox fetch
    python tools/browser_video.py login          opens a real window; log in by hand (2FA and all),
                                                 come back here and press Enter. The session lives in
                                                 the browser-profile/ folder and is reused from then on.

Map the workspace once (the UI is not documented; selectors are learned, not guessed):
    python tools/browser_video.py inspect        opens the workspace logged in and dumps every button,
                                                 combobox, textbox and file input it can see to
                                                 tools/inspect-<timestamp>.txt. Fill tools/selectors.json
                                                 from that dump (a template is written next to it).

Submit a clip (what the video director runs on GO):
    python tools/browser_video.py submit --job jobs/<job> --item scene-01 --version 1 \
        --model seedance-2.5 --prompt-file scenes/scene-01/video.prompt.txt \
        --ref sheets/character-01-doctor/approved.png --ref sheets/environment-01-clinic/approved.png \
        --aspect 16:9 --duration 6 --resolution 4k --out scenes/scene-01/video-v1.mp4

    No start frame, no end frame. The clip is made from the prompt plus the approved SHEETS attached
    as references (--ref, repeatable, order kept, strongest first). Frames were tested and they make
    the output worse; so does attaching the storyboard.

What submit does, in order, and nothing else:
    1. open the workspace URL in the persistent profile          (exit 3 if a sign-in form shows)
    2. switch to video, pick the model                            (exit 2 if a selector is missing)
    3. set aspect, duration, resolution; nearest lower option if the exact one is absent (printed)
    4. upload the reference sheets, in the order given
    5. paste the prompt, click generate
    6. wait for the result (up to --wait minutes), download to --out, print the generation URL
    7. append a row to <job>/log.csv, with the credits the workspace showed as spent when the
       optional credits_text selector is mapped (otherwise the credits column stays empty)
Every step waits like a person would. One attempt per call. A failure screenshots to
<job>/scenes/<item>/browser-fail-v<version>.png and exits non-zero with the reason.

Exit codes: 0 saved · 1 bad arguments · 2 selector missing (run inspect) · 3 not logged in (run login)
            · 4 workspace refused the request · 5 generation failed in the workspace · 6 timed out.
"""
import argparse, csv, io, json, os, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELECTORS_PATH = os.path.join(ROOT, "tools", "selectors.json")

# Every selector the submit flow needs. Values are Playwright locators (CSS, text=, role=...).
# `inspect` writes this template to tools/selectors.template.json; copy it to selectors.json and fill it.
SELECTOR_TEMPLATE = {
    "_comment": "Playwright locator strings. Fill from an inspect dump. Keys with null are required.",
    "signed_in_marker": None,          # something only visible when logged in, e.g. "button[aria-label='Account']"
    "sign_in_form": "input[type='password'], text=Sign in",
    "video_tab": None,                 # e.g. "role=tab[name='Video']"
    "model_picker": None,              # opens the model list
    "model_option": {                  # one locator per model id used on the command line
        "seedance-2.5": None,          # e.g. "text=Seedance 2.5"
        "kling": None
    },
    "aspect_picker": None,
    "aspect_option_prefix": None,      # e.g. "role=option[name='" -> closed with the value + "']"
    "duration_picker": None,
    "duration_option_prefix": None,
    "resolution_picker": None,
    "resolution_option_prefix": None,
    "reference_input": None,           # input[type=file] that takes the reference images (the sheets)
    "credits_text": None,              # optional: element whose text shows the remaining credits
    "prompt_box": None,                # textarea or contenteditable
    "generate_button": None,
    "result_video": None,              # <video> element of the newest generation
    "download_button": None,
    "failure_marker": None,            # text shown when a generation fails
    "generation_link": None            # optional: anchor that holds the generation URL
}

ASPECT_FALLBACK = {"21:9": ["21:9", "16:9"], "16:9": ["16:9"], "9:16": ["9:16"], "1:1": ["1:1", "4:3", "16:9"],
                   "4:3": ["4:3", "16:9"], "3:4": ["3:4", "9:16"]}
RES_ORDER = ["4k", "2k", "1080p", "720p", "480p"]


def env_value(name, default=None):
    v = os.environ.get(name)
    if v:
        return v
    p = os.path.join(ROOT, ".env")
    if os.path.exists(p):
        for line in io.open(p, encoding="utf-8"):
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip().strip('"').strip("'") or default
    return default


WORKSPACE_URL = env_value("ELEVENLABS_WORKSPACE_URL", "https://elevenlabs.io/app/image-video")
PROFILE_DIR = os.path.join(ROOT, env_value("BROWSER_PROFILE_DIR", "browser-profile"))


def resolve(p):
    return p if os.path.isabs(p) else os.path.normpath(os.path.join(ROOT, p))


def browser(headless=False):
    try:
        from camoufox.sync_api import Camoufox
    except ImportError:
        sys.exit("camoufox is not installed. From your own terminal: pip install -U \"camoufox[geoip]\" && python -m camoufox fetch")
    os.makedirs(PROFILE_DIR, exist_ok=True)
    return Camoufox(headless=headless, persistent_context=True, user_data_dir=PROFILE_DIR, humanize=True)


def load_selectors():
    if not os.path.exists(SELECTORS_PATH):
        return None
    return json.load(io.open(SELECTORS_PATH, encoding="utf-8"))


def need(sel, key, sub=None):
    v = sel.get(key) if sel else None
    if sub is not None and isinstance(v, dict):
        v = v.get(sub)
    if not v:
        print("selector missing: %s%s  -> run: python tools/browser_video.py inspect, then fill tools/selectors.json"
              % (key, ("." + sub) if sub else ""))
        sys.exit(2)
    return v


def pause(lo=0.6, hi=1.4):
    import random
    time.sleep(random.uniform(lo, hi))


def pick_option(page, sel, picker_key, prefix_key, wanted, candidates):
    page.locator(need(sel, picker_key)).first.click()
    pause()
    prefix = need(sel, prefix_key)
    for c in candidates:
        loc = page.locator(prefix + c + "']")
        if loc.count():
            loc.first.click()
            pause()
            if c != wanted:
                print("workspace has no %s; picked %s" % (wanted, c))
            return c
    page.keyboard.press("Escape")
    print("none of %s offered for %s" % (candidates, picker_key))
    sys.exit(4)


def cmd_login(a):
    with browser(headless=False) as ctx:
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(WORKSPACE_URL, wait_until="domcontentloaded")
        print("A browser window is open. Log in there by hand, finish 2FA, wait until the workspace shows.")
        print("Then come back here and press Enter. Nothing is typed or stored by this script.")
        try:
            input()
        except EOFError:
            print("no terminal to wait on; leaving the window open for 10 minutes instead")
            time.sleep(600)
        print("session kept in", PROFILE_DIR)


def cmd_inspect(a):
    stamp = time.strftime("%Y%m%d-%H%M%S")
    dump = os.path.join(ROOT, "tools", "inspect-%s.txt" % stamp)
    tmpl = os.path.join(ROOT, "tools", "selectors.template.json")
    with browser(headless=False) as ctx:
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(WORKSPACE_URL, wait_until="domcontentloaded")
        page.wait_for_timeout(6000)
        lines = ["URL: " + page.url, "TITLE: " + page.title(), ""]
        for role in ("tab", "button", "combobox", "textbox", "option", "link", "menuitem"):
            loc = page.get_by_role(role)
            n = min(loc.count(), 300)
            for i in range(n):
                el = loc.nth(i)
                try:
                    name = (el.get_attribute("aria-label") or el.inner_text(timeout=500) or "").strip().replace("\n", " ")[:80]
                except Exception:
                    name = ""
                lines.append("%-10s %s" % (role, name))
        inputs = page.locator("input[type='file'], textarea, [contenteditable='true'], video")
        for i in range(min(inputs.count(), 100)):
            el = inputs.nth(i)
            try:
                lines.append("element    <%s> id=%s name=%s accept=%s placeholder=%s" % (
                    el.evaluate("e => e.tagName.toLowerCase()"), el.get_attribute("id"), el.get_attribute("name"),
                    el.get_attribute("accept"), el.get_attribute("placeholder")))
            except Exception:
                pass
        io.open(dump, "w", encoding="utf-8").write("\n".join(lines))
        page.screenshot(path=dump[:-4] + ".png", full_page=True)
    if not os.path.exists(tmpl):
        io.open(tmpl, "w", encoding="utf-8").write(json.dumps(SELECTOR_TEMPLATE, indent=2))
    print("dump:", dump)
    print("template:", tmpl, "-> copy to tools/selectors.json and fill in")


def log_row(job, row):
    logp = os.path.join(job, "log.csv")
    run = 1
    if os.path.exists(logp):
        with io.open(logp, encoding="utf-8", newline="") as f:
            nums = [int(r[0]) for r in list(csv.reader(f))[1:] if r and r[0].isdigit()]
        run = (max(nums) + 1) if nums else 1
    row = row + [""] * (14 - len(row))
    with io.open(logp, "a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow([run] + row)
    return run


def cmd_submit(a):
    job = resolve(a.job)
    prompt_path, out = resolve(a.prompt_file), resolve(a.out)
    refs = [resolve(r) for r in a.ref]
    if not refs:
        sys.exit("no --ref given: a clip is made from the prompt plus the approved sheets as references")
    for p in [prompt_path] + refs:
        if not os.path.exists(p):
            sys.exit("missing: " + p)
    if os.path.exists(out):
        sys.exit("refusing to overwrite an existing version: " + out)
    prompt = io.open(prompt_path, encoding="utf-8").read().strip()
    if not prompt:
        sys.exit("prompt file is empty")
    sel = load_selectors()
    if sel is None:
        print("tools/selectors.json is missing. Run: python tools/browser_video.py inspect")
        sys.exit(2)
    fail_shot = os.path.join(os.path.dirname(out), "browser-fail-v%d.png" % a.version)
    rel = lambda p: os.path.relpath(p, job).replace("\\", "/")
    settings = "%s %s %ss %s" % (a.model, a.aspect, a.duration, a.resolution)
    t0 = time.time()
    gen_url = ""
    credits_before = None
    refs_col = ";".join(os.path.relpath(r, job).replace("\\", "/") for r in refs)

    def read_credits(page):
        """Remaining credits as shown in the workspace when credits_text is mapped; else None."""
        if not sel.get("credits_text"):
            return None
        try:
            txt = page.locator(sel["credits_text"]).first.inner_text()
            digits = "".join(ch for ch in txt if ch.isdigit())
            return int(digits) if digits else None
        except Exception:
            return None

    def fail(code, why):
        try:
            page.screenshot(path=fail_shot, full_page=True)
        except Exception:
            pass
        log_row(job, [time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"), a.item, "v%d" % a.version, a.model,
                      rel(prompt_path), refs_col, settings, "", why.split(":")[0], int(time.time() - t0), why[:200], "", ""])
        print(why, "| screenshot:", fail_shot)
        sys.exit(code)

    with browser(headless=a.headless) as ctx:
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(WORKSPACE_URL, wait_until="domcontentloaded")
        page.wait_for_timeout(5000)
        if page.locator(sel.get("sign_in_form") or "input[type='password']").count():
            fail(3, "not logged in: run  python tools/browser_video.py login  from your own terminal")
        if sel.get("signed_in_marker") and not page.locator(sel["signed_in_marker"]).count():
            fail(3, "not logged in (signed_in_marker absent): run login from your own terminal")

        page.locator(need(sel, "video_tab")).first.click(); pause()
        page.locator(need(sel, "model_picker")).first.click(); pause()
        page.locator(need(sel, "model_option", a.model)).first.click(); pause()

        pick_option(page, sel, "aspect_picker", "aspect_option_prefix", a.aspect, ASPECT_FALLBACK.get(a.aspect, [a.aspect]))
        durations = [str(a.duration)] + [str(d) for d in range(a.duration - 1, 3, -1)]
        pick_option(page, sel, "duration_picker", "duration_option_prefix", str(a.duration), durations)
        r = a.resolution.lower()
        res_candidates = RES_ORDER[RES_ORDER.index(r):] if r in RES_ORDER else [r]
        pick_option(page, sel, "resolution_picker", "resolution_option_prefix", r, res_candidates)

        credits_before = read_credits(page)
        page.locator(need(sel, "reference_input")).set_input_files(refs); pause(2, 4)

        box = page.locator(need(sel, "prompt_box")).first
        box.click(); pause()
        box.fill(prompt) if box.evaluate("e => e.tagName.toLowerCase()") == "textarea" else box.type(prompt, delay=2)
        pause(1, 2)
        page.locator(need(sel, "generate_button")).first.click()
        print("submitted; waiting up to %d min" % a.wait)

        deadline = time.time() + a.wait * 60
        video = None
        while time.time() < deadline:
            if sel.get("failure_marker") and page.locator(sel["failure_marker"]).count():
                fail(5, "generation failed in the workspace: " + page.locator(sel["failure_marker"]).first.inner_text()[:160])
            loc = page.locator(need(sel, "result_video"))
            if loc.count():
                src = loc.first.get_attribute("src")
                if src and src != a.ignore_src:
                    video = src
                    break
            time.sleep(10)
        if not video:
            fail(6, "timed out waiting for the clip")
        if sel.get("generation_link"):
            try:
                gen_url = page.locator(sel["generation_link"]).first.get_attribute("href") or ""
            except Exception:
                gen_url = ""
        credits_after = read_credits(page)
        try:
            with page.expect_download(timeout=120000) as dl:
                page.locator(need(sel, "download_button")).first.click()
            dl.value.save_as(out)
        except Exception:
            data = ctx.request.get(video).body()
            with open(out, "wb") as f:
                f.write(data)

    secs = int(time.time() - t0)
    credits, note = "", gen_url
    if credits_before is not None and credits_after is not None:
        credits = credits_before - credits_after
    else:
        note = (gen_url + " credits: not readable in the workspace, fill log.csv by hand").strip()
    run = log_row(job, [time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"), a.item, "v%d" % a.version, a.model,
                        rel(prompt_path), refs_col, settings, rel(out), "completed", secs, note, credits, gen_url])
    print("saved %s  (%d s, run #%d, credits: %s)  %s" % (out, secs, run, credits if credits != "" else "?", gen_url))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("login")
    sub.add_parser("inspect")
    s = sub.add_parser("submit")
    s.add_argument("--job", required=True)
    s.add_argument("--item", required=True, help="scene-NN")
    s.add_argument("--version", type=int, required=True)
    s.add_argument("--model", default="seedance-2.5", help="key of model_option in selectors.json")
    s.add_argument("--prompt-file", required=True)
    s.add_argument("--ref", action="append", default=[], help="reference sheet, repeatable, order kept, strongest first")
    s.add_argument("--aspect", default="16:9")
    s.add_argument("--duration", type=int, default=6)
    s.add_argument("--resolution", default="4k")
    s.add_argument("--out", required=True)
    s.add_argument("--wait", type=int, default=25, help="minutes to wait for the clip")
    s.add_argument("--headless", action="store_true")
    s.add_argument("--ignore-src", default="", help="src of an older result video to ignore")
    a = ap.parse_args()
    if a.cmd == "login":
        cmd_login(a)
    elif a.cmd == "inspect":
        cmd_inspect(a)
    elif a.cmd == "submit":
        cmd_submit(a)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
