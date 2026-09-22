# -*- coding: utf-8 -*-
"""Create a job folder skeleton per FOLDER-PROTOCOL.md.

    python tools/new_job.py clinic            ->  jobs/2026-09-22-clinic/
    python tools/new_job.py clinic --date 2026-10-01
"""
import argparse, csv, io, os, re, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATUS = """# STATUS · {name}

| Item | State | Version | Rerolls | Note |
|---|---|---|---|---|
| ground-rules | — | | | |
| plan | — | | | |
| video-settings | — | | | |
"""

GROUND_RULES = """# Ground rules · {name}

Set once, checked at every gate. The main agent proposes, the user locks with OKAY.

| Rule | Value | Status |
|---|---|---|
| Aspect ratio | 16:9 | PROVISIONAL |
| Palette (hex) | | PROVISIONAL |
| Look | | PROVISIONAL |
| Stance | | PROVISIONAL |
| Forbidden everywhere | legible text, logos, brand marks | PROVISIONAL |
| Scene length | | from the first question |
| Reroll budget | 3 per item | PROVISIONAL |
"""

VIDEO_SETTINGS = """Model: Seedance 2.5
Aspect: 16:9
Length: 6 seconds
Resolution: 4k
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--date", default=time.strftime("%Y-%m-%d"))
    a = ap.parse_args()
    slug = re.sub(r"[^a-z0-9]+", "-", a.slug.lower()).strip("-")
    if not slug:
        sys.exit("slug must contain letters or digits")
    name = "%s-%s" % (a.date, slug)
    job = os.path.join(ROOT, "jobs", name)
    if os.path.exists(job):
        sys.exit("job exists: " + job)
    for d in ("plan", "sheets", "scenes"):
        os.makedirs(os.path.join(job, d))
    io.open(os.path.join(job, "brief.md"), "w", encoding="utf-8").write("# Brief · %s\n\n(paste the user's brief here, verbatim)\n" % name)
    io.open(os.path.join(job, "ground-rules.md"), "w", encoding="utf-8").write(GROUND_RULES.format(name=name))
    io.open(os.path.join(job, "STATUS.md"), "w", encoding="utf-8").write(STATUS.format(name=name))
    io.open(os.path.join(job, "plan", "video-settings.txt"), "w", encoding="utf-8").write(VIDEO_SETTINGS)
    for f in ("characters.md", "environments.md", "elements.md", "scenes.md"):
        io.open(os.path.join(job, "plan", f), "w", encoding="utf-8").write("# %s · %s\n\n" % (f[:-3], name))
    with io.open(os.path.join(job, "log.csv"), "w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow(["run", "date", "time", "item", "version", "model", "prompt_file", "refs",
                                "settings", "output", "status", "seconds", "note"])
    print("created", job.replace("\\", "/"))


if __name__ == "__main__":
    main()
