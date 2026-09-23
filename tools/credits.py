# -*- coding: utf-8 -*-
"""Credit tally for one job, from log.csv. Run at milestones, never per image.

    python tools/credits.py --job jobs/2026-09-23-window-map-scene-1 [--scope sheets | scene-01 | all]

Prints one block the main agent pastes into the chat as it is. "kept" means the run's output is
byte-identical to an approved file (approved.png, storyboard-approved.png, video-approved.mp4).
"thrown away" means completed but not the approved version. "failed" means rejected, failed or
timed out. A run whose credits column is empty (video runs the workspace did not report, or rows
older than credit tracking) is listed so the user can fill it in by hand.
"""
import argparse, csv, io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def resolve(p):
    return p if os.path.isabs(p) else os.path.normpath(os.path.join(ROOT, p))


def same_bytes(a, b):
    try:
        if os.path.getsize(a) != os.path.getsize(b):
            return False
        with open(a, "rb") as fa, open(b, "rb") as fb:
            return fa.read() == fb.read()
    except OSError:
        return False


def approved_path(job, item, output):
    m = re.match(r"^(scene-\d\d)-([a-z]+)$", item)
    if m:
        ext = os.path.splitext(output)[1] or ".png"
        return os.path.join(job, "scenes", m.group(1), "%s-approved%s" % (m.group(2), ext))
    return os.path.join(job, "sheets", item, "approved.png")


def in_scope(item, scope):
    if scope == "all":
        return True
    if scope == "sheets":
        return not item.startswith("scene-")
    return item.startswith(scope + "-")


def num(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--job", required=True)
    ap.add_argument("--scope", default="all", help="sheets | scene-NN | all")
    a = ap.parse_args()
    job = resolve(a.job)
    logp = os.path.join(job, "log.csv")
    if not os.path.exists(logp):
        sys.exit("no log.csv in " + job)
    with io.open(logp, encoding="utf-8", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r.get("run")]
    rows = [r for r in rows if in_scope(r["item"], a.scope)]

    spent = {"image": 0, "video": 0}
    kept = thrown = failed = 0
    kept_n = thrown_n = failed_n = 0
    thrown_list, unknown = [], []
    for r in rows:
        kind = "video" if r["output"].endswith(".mp4") or "seedance" in r["model"] or "kling" in r["model"] else "image"
        c = num(r.get("credits"))
        if c is None:
            unknown.append("run #%s %s %s (%s)" % (r["run"], r["item"], r["version"], r["status"]))
            c = 0
        spent[kind] += c
        if r["status"] != "completed":
            failed += c
            failed_n += 1
            continue
        out = os.path.join(job, r["output"].replace("/", os.sep))
        if same_bytes(out, approved_path(job, r["item"], r["output"])):
            kept += c
            kept_n += 1
        else:
            thrown += c
            thrown_n += 1
            thrown_list.append("%s %s" % (r["item"], r["version"]))

    total = spent["image"] + spent["video"]
    print("CREDITS | %s | %d runs" % (a.scope, len(rows)))
    print("  spent        %8s   images %s | videos %s" % (format(total, ","), format(spent["image"], ","), format(spent["video"], ",")))
    print("  kept         %8s   %d approved versions" % (format(kept, ","), kept_n))
    print("  thrown away  %8s   %d versions not approved%s" % (format(thrown, ","), thrown_n,
          (": " + ", ".join(thrown_list)) if thrown_list else ""))
    print("  failed       %8s   %d rejected, failed or timed-out runs" % (format(failed, ","), failed_n))
    if unknown:
        print("  unknown      %d runs with no credit figure, fill log.csv by hand: %s" % (len(unknown), "; ".join(unknown)))


if __name__ == "__main__":
    main()
