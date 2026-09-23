# -*- coding: utf-8 -*-
"""One GPT Image 2 generation on the ElevenLabs Image & Video API, saved where you say.

    python tools/gen_image.py --job jobs/2026-09-22-clinic --item character-01-doctor --version 1 \
        --prompt-file jobs/2026-09-22-clinic/sheets/character-01-doctor/v1.prompt.txt \
        --aspect 3:2 --res 1K --quality high [--ref photo.jpg ...] [--out path.png] [--dry-run]

Paths are relative to the pipeline root (the folder holding this tools/ directory) or absolute.
If --out is omitted the image lands at <job>/sheets/<item>/v<version>.png, or, for items named
scene-NN-storyboard, at <job>/scenes/scene-NN/storyboard-v<version>.png.

Credits: the tool reads the account's used-credit counter (GET /v1/user/subscription, free) before
the request and again after the image lands, and logs the difference in the `credits` column of
log.csv. If the counter has not moved within ten seconds the row says 0 with the note
"credits: no delta reported" so the tally can flag it. The generation id is logged too.

The key is loaded from, in order: the ELEVENLABS_API_KEY environment variable, a .env file in the
pipeline root, then ../API-KEYS.local.md (a private file outside the repo). It is never printed.
Standard library only. Model is gpt-image-2 and cannot be changed from the command line.

Exit codes: 0 saved · 1 bad arguments or missing file · 4 request rejected (nothing charged) ·
5 generation failed (not charged) · 6 poll timeout.
"""
import argparse, base64, csv, io, json, os, re, sys, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://api.elevenlabs.io/v1"
MODEL = "gpt-image-2"
ASPECTS = ["1:1", "3:2", "2:3", "16:9", "9:16", "4:3", "3:4", "21:9"]
RES = ["1K", "2K", "4K"]
QUALITY = ["low", "medium", "high"]


def load_key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if k:
        return k.strip()
    for path in (os.path.join(ROOT, ".env"), os.path.join(os.path.dirname(ROOT), "API-KEYS.local.md")):
        if os.path.exists(path):
            for line in io.open(path, encoding="utf-8"):
                if line.startswith("ELEVENLABS_API_KEY="):
                    v = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if v:
                        return v
    sys.exit("no key: set ELEVENLABS_API_KEY or fill in .env (copy .env.example)")


def resolve(p):
    return p if os.path.isabs(p) else os.path.normpath(os.path.join(ROOT, p))


def b64ref(path):
    ext = os.path.splitext(path)[1].lower()
    mime = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}.get(ext)
    if not mime:
        sys.exit("reference must be png, jpg or webp: " + path)
    with open(path, "rb") as f:
        return {"type": "inline_base64", "content_base64": base64.b64encode(f.read()).decode(), "mime_type": mime}


def call(key, method, path, body=None, timeout=120):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method,
                                 headers={"xi-api-key": key, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        txt = e.read().decode(errors="replace")
        try:
            txt = json.loads(txt)
        except ValueError:
            pass
        return e.code, txt


def default_out(job, item, version):
    m = re.match(r"^(scene-\d\d)-([a-z]+)$", item)
    if m:
        return os.path.join(job, "scenes", m.group(1), "%s-v%d.png" % (m.group(2), version))
    return os.path.join(job, "sheets", item, "v%d.png" % version)


HEADER = ["run", "date", "time", "item", "version", "model", "prompt_file", "refs",
          "settings", "output", "status", "seconds", "note", "credits", "gen_id"]


def log_row(job, row):
    """Append one row. Upgrades an older log.csv (no credits/gen_id columns) in place."""
    logp = os.path.join(job, "log.csv")
    rows = []
    if os.path.exists(logp):
        with io.open(logp, encoding="utf-8", newline="") as f:
            rows = [r for r in csv.reader(f) if r]
    if rows and rows[0] != HEADER:
        rows = [HEADER] + [r + [""] * (len(HEADER) - len(r)) for r in rows[1:]]
        with io.open(logp, "w", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(rows)
    nums = [int(r[0]) for r in rows[1:] if r[0].isdigit()]
    run = (max(nums) + 1) if nums else 1
    row = row + [""] * (len(HEADER) - 1 - len(row))
    with io.open(logp, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if not rows:
            w.writerow(HEADER)
        w.writerow([run] + row)
    return run


def credits_used(key):
    """The account's used-credit counter, or None if the endpoint did not answer."""
    st, body = call(key, "GET", "/user/subscription", timeout=30)
    if st == 200 and isinstance(body, dict) and isinstance(body.get("character_count"), int):
        return body["character_count"]
    return None


def credits_delta(key, before):
    """Poll the counter for up to ten seconds after a generation; returns (delta, note)."""
    if before is None:
        return "", "credits: counter unavailable"
    for _ in range(5):
        after = credits_used(key)
        if after is not None and after != before:
            return after - before, ""
        time.sleep(2)
    return 0, "credits: no delta reported"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--job", required=True, help="job folder, e.g. jobs/2026-09-22-clinic")
    ap.add_argument("--item", required=True, help="e.g. character-01-doctor or scene-01-still")
    ap.add_argument("--version", type=int, required=True)
    ap.add_argument("--prompt-file", required=True)
    ap.add_argument("--aspect", default="16:9", choices=ASPECTS)
    ap.add_argument("--res", default="1K", choices=RES)
    ap.add_argument("--quality", default="high", choices=QUALITY)
    ap.add_argument("--ref", action="append", default=[], help="reference image, repeatable, order kept (max 10)")
    ap.add_argument("--out", help="output png path; default follows FOLDER-PROTOCOL.md")
    ap.add_argument("--note", default="", help="free text for the log row")
    ap.add_argument("--dry-run", action="store_true", help="print the request (no base64) and send nothing")
    a = ap.parse_args()

    job = resolve(a.job)
    prompt_path = resolve(a.prompt_file)
    if not os.path.isdir(job):
        sys.exit("job folder not found: " + job)
    if not os.path.exists(prompt_path):
        sys.exit("prompt file not found: " + prompt_path)
    prompt = io.open(prompt_path, encoding="utf-8").read().strip()
    if not prompt:
        sys.exit("prompt file is empty: " + prompt_path)
    if len(a.ref) > 10:
        sys.exit("gpt-image-2 takes at most 10 reference images")
    refs = [resolve(r) for r in a.ref]
    for r in refs:
        if not os.path.exists(r):
            sys.exit("reference not found: " + r)
    out = resolve(a.out) if a.out else default_out(job, a.item, a.version)
    if os.path.exists(out):
        sys.exit("refusing to overwrite an existing version: " + out + "  (bump --version)")
    os.makedirs(os.path.dirname(out), exist_ok=True)

    body = {"model_id": MODEL, "prompt": prompt, "aspect_ratio": a.aspect, "resolution": a.res, "quality": a.quality}
    if refs:
        body["images"] = [("file", r) for r in refs]
    settings = "%s %s %s" % (a.aspect, a.res, a.quality)
    rel = lambda p: os.path.relpath(p, job).replace("\\", "/")

    if a.dry_run:
        shown = dict(body)
        shown["prompt"] = prompt[:200] + ("..." if len(prompt) > 200 else "")
        shown["images"] = ["<file %s>" % os.path.basename(r) for r in refs]
        print(json.dumps(shown, indent=2, ensure_ascii=False))
        print("would save:", out)
        return

    key = load_key()
    if refs:
        body["images"] = [b64ref(r) for r in refs]
    before = credits_used(key)
    t0 = time.time()
    status, resp = call(key, "POST", "/flows/image", body)
    if status != 200:
        msg = json.dumps(resp, ensure_ascii=False) if not isinstance(resp, str) else resp
        log_row(job, [time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"), a.item, "v%d" % a.version, MODEL,
                      rel(prompt_path), ";".join(rel(r) for r in refs), settings, "", "rejected %s" % status, 0, msg[:200], 0, ""])
        print("rejected (nothing charged), HTTP %s: %s" % (status, msg[:600]))
        sys.exit(4)
    gen_id = resp["id"]
    interval, deadline = 3, time.time() + 30 * 60
    while True:
        st, body2 = call(key, "GET", "/flows/image/" + gen_id)
        if st != 200:
            sys.exit("poll failed %s" % st)
        s = body2.get("status")
        if s in ("completed", "failed"):
            break
        if time.time() > deadline:
            log_row(job, [time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"), a.item, "v%d" % a.version, MODEL,
                          rel(prompt_path), ";".join(rel(r) for r in refs), settings, "", "timeout", int(time.time() - t0), "", "", gen_id])
            sys.exit(6)
        time.sleep(interval)
        interval = min(interval * 1.5, 20)
    secs = int(time.time() - t0)
    if s != "completed":
        reason = "%s: %s" % (body2.get("failure_reason"), body2.get("error_message"))
        delta, cnote = credits_delta(key, before)
        log_row(job, [time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"), a.item, "v%d" % a.version, MODEL,
                      rel(prompt_path), ";".join(rel(r) for r in refs), settings, "", "failed", secs, reason[:200], delta, gen_id])
        print("generation failed (credits charged: %s):" % delta, reason)
        sys.exit(5)
    data = urllib.request.urlopen(body2["content_url"], timeout=300).read()
    with open(out, "wb") as f:
        f.write(data)
    delta, cnote = credits_delta(key, before)
    note = (a.note + " " + cnote).strip()
    run = log_row(job, [time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"), a.item, "v%d" % a.version, MODEL,
                        rel(prompt_path), ";".join(rel(r) for r in refs), settings, rel(out), "completed", secs, note, delta, gen_id])
    print("saved %s  (%d KB, %d s, run #%d, credits: %s)" % (out, len(data) // 1024, secs, run, delta))


if __name__ == "__main__":
    main()
