# FOLDER-PROTOCOL.md — where everything goes and what it is called

The job folder is the passing table. Subagents never hand files to each other; they write
to a fixed place under a fixed name, and whoever needs the file reads it from there. A
combiner never has to guess what a file is, because the name says so.

## The job folder

`jobs/<YYYY-MM-DD>-<slug>/`, made by `python tools/new_job.py <slug>`.

```
jobs/2026-09-22-clinic/
├─ brief.md                         the user's brief, verbatim
├─ ground-rules.md                  aspect · palette hex · look+stance · forbidden · scene length · reroll budget
├─ STATUS.md                        the board. Main agent only. Every gate result lands here.
├─ log.csv                          every run from #1, approved or not
│
├─ plan/                            what the user edits before anything generates
│  ├─ characters.md                 the Persistent Characters registry (@handles)
│  ├─ environments.md
│  ├─ elements.md
│  ├─ scenes.md                     one line per scene: action · tag set · cut | continuation
│  ├─ character-01-doctor.prompt.txt
│  ├─ character-02-old_lady.prompt.txt
│  ├─ environment-01-clinic.prompt.txt
│  ├─ element-01-xray_film.prompt.txt
│  └─ video-settings.txt            Model / Aspect / Length / Resolution, four lines
│
├─ sheets/                          one folder per sheet, named exactly like its prompt file
│  ├─ character-01-doctor/
│  │  ├─ v1.png  v2.png ...         every version, never deleted
│  │  ├─ v1.prompt.txt              the prompt that made v1 (the subagent's final text)
│  │  ├─ approved.png               a copy of the approved version. Only the main agent writes this.
│  │  └─ report.md                  the subagent's checks and notes, appended per version
│  ├─ environment-01-clinic/
│  └─ element-01-xray_film/
│
└─ scenes/                          sequential. scene-02 cannot exist before scene-01 has end-approved.png
   ├─ scene-01/
   │  ├─ card.md                    motion map · brief · look picks (internal) · FOV step · tags · dialogue count
   │  ├─ still.prompt.txt           the scene still prompt (references the approved sheets by role)
   │  ├─ still-v1.png  still-v2.png
   │  ├─ still-approved.png
   │  ├─ end.prompt.txt             an EDIT of the approved still. Never a fresh generation.
   │  ├─ end-v1.png
   │  ├─ end-approved.png
   │  ├─ video.prompt.txt           the sealed video prompt
   │  ├─ video-v1.mp4
   │  ├─ video-approved.mp4
   │  └─ report.md
   └─ scene-02/
```

## Naming law

`<type>-<NN>-<handle>` for sheets. `scene-<NN>` for scenes. `<what>-v<N>` for versions.
`<what>-approved` for the one the user picked.

- `type` is one of `character`, `environment`, `element`.
- `NN` is two digits, assigned in the plan, never reused inside a job.
- `handle` is the `@handle` without the `@`: lowercase, underscores, no spaces.
- A state change is its own sheet: `character-03-old_lady_wet`, not a note on 02.
- Versions count up and are never overwritten. A reroll is `v2`, not a new `v1`.
- `approved` files are copies. Deleting `v3.png` never loses the approved image.

## Who writes where

| Path | Written by | Read by |
|---|---|---|
| `brief.md`, `ground-rules.md`, `plan/*`, `STATUS.md` | main agent (the user edits `plan/*`) | everyone |
| `sheets/<target>/*` except `approved.png` | that sheet's subagent | main agent, scene agent |
| `sheets/<target>/approved.png` | main agent | scene agent |
| `scenes/scene-NN/card.md` | main agent | scene agent, video director |
| `scenes/scene-NN/still*`, `end*`, `report.md` | scene agent (except `*-approved`) | main agent, video director, next scene agent |
| `scenes/scene-NN/video*` | video director (except `video-approved.mp4`) | main agent |
| `*-approved.*` | main agent only | everyone |
| `log.csv` | every agent appends one row per run | main agent |

A subagent that writes outside its own target folder is broken. It should stop and report.

## STATUS.md

The main agent's board. Plain markdown table, rewritten after every gate:

```
# STATUS · 2026-09-22-clinic

| Item | State | Version | Rerolls | Note |
|---|---|---|---|---|
| ground-rules | OKAY | | | |
| plan | OKAY | | | |
| character-01-doctor | APPROVED | v2 | 1 | glasses fixed |
| character-02-old_lady | GATE | v1 | 0 | waiting on user |
| environment-01-clinic | APPROVED | v1 | 0 | |
| element-01-xray_film | RUNNING | | 0 | |
| scene-01 still | — | | | blocked: character-02 not approved |
| scene-01 end | — | | | |
| scene-01 video | — | | | |
| video-settings | OKAY | | | Seedance 2.5 · 16:9 · 6 s · 4k |
```

States: `—` (not started) · `PLANNED` · `RUNNING` · `GATE` · `APPROVED` · `BLOCKED` ·
`SKIPPED (user override)`.

## log.csv

Header, written by `new_job.py`. One row per generation, appended by whichever agent ran it.

```
run,date,time,item,version,model,prompt_file,refs,settings,output,status,seconds,note
1,2026-09-22,14:03:10,character-01-doctor,v1,gpt-image-2,sheets/character-01-doctor/v1.prompt.txt,,3:2 1K high,sheets/character-01-doctor/v1.png,completed,61,
```

Run #1 is logged whatever happened to it. A failed run is a row too.
