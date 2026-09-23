# Leo Workflow

Reference-image to AI-video, run by a main agent that deploys subagents from Markdown
role files. The human approves in the chat. The operating path is:

```
brief → PLAN files (edit in Notepad) → OKAY
      → character / environment / element sheets   (GPT Image 2, parallel, ~60 s each)
      → per scene: storyboard (client sign-off, optional) → clip
        (prompt + the approved sheets as references; Seedance 2.5 in the ElevenLabs
        web workspace, driven by Camoufox; no start or end frame, no storyboard attached)
      → next scene opens on this scene's arrival state, written into its card
```

There is no ComfyUI in this path. The ComfyUI rig in the parent folder is the spec and
the demo; this folder is the operation.

## What is in here

| Path | What |
|---|---|
| `CLAUDE.md` | tells Claude Code it is the main agent and what to read |
| `MAIN.md` | the main agent's manual: intake, plan, deploy conditions, gates, feedback routing, the scene loop |
| `FOLDER-PROTOCOL.md` | the job folder layout and the naming law |
| `PROMPT-STRUCTURES.md` | the shape of every prompt (sheets with the anti-wax REALISM block, storyboard, scene card, Seedance, Kling) |
| `roles/_contract.md` | rules every subagent follows |
| `roles/character-sheet.md` · `environment-sheet.md` · `element-sheet.md` | the sheet makers |
| `roles/storyboard.md` | combines approved sheets into the client's storyboard sheet (never a video reference) |
| `roles/video-director.md` | picks the sheets the shot needs, writes the video prompt, drives the browser |
| `libraries/realist-portrait/` | Leo's anti-wax skill and its reference banks |
| `tools/gen_image.py` | one GPT Image 2 call, saved and logged (stdlib only) |
| `tools/browser_video.py` | Camoufox: `login` once by hand, `inspect` to map the UI, `submit` a clip with the sheets attached |
| `tools/credits.py` | the credit tally per milestone (sheets, a scene, the whole job): spent, kept, thrown away, failed |
| `tools/new_job.py` | job folder skeleton |
| `libraries/` | the AI Production craft kit: prompt architecture, camera libraries, prompt archive, a worked example |
| `jobs/` | one folder per job (gitignored) |

## Setup

1. Python 3.10 or newer.
2. `copy .env.example .env` and fill in `ELEVENLABS_API_KEY`. The key needs Image & Video
   permission on a Pro plan or above. Never commit `.env`, never paste the key in a chat.
3. For video, from your own terminal:
   ```
   pip install -U "camoufox[geoip]"
   python -m camoufox fetch
   python tools/browser_video.py login
   ```
   A real browser window opens on the ElevenLabs Image & Video workspace. Log in by hand,
   finish 2FA, press Enter in the terminal. The session lives in `browser-profile/`
   (gitignored) and is reused. No script ever sees a password.
4. Map the workspace once: `python tools/browser_video.py inspect`, then copy
   `tools/selectors.template.json` to `tools/selectors.json` and fill in the locators from
   the dump. The workspace UI is not documented, so this is learned once and kept.

## Running a job

Open this folder in Claude Code and say what you want, for example:

> New job: a 30-second clinic scene, a doctor shows an old lady her x-ray, warm, hopeful.

The main agent asks one question (scene length), proposes the ground rules, writes the PLAN
files, and stops. You edit the prompt files in Notepad if you want, say `OKAY`, and the
sheets generate in parallel. Every image stops at a gate in the chat. Then scene by scene.

Things the main agent will do without being asked:

- remind you when a sheet is missing before a scene ("We haven't done the character sheet
  for @old_lady yet");
- ask what exactly is wrong when feedback is vague, before spending a generation;
- send feedback only to the agent whose work you criticised;
- keep `jobs/<job>/STATUS.md` and `log.csv` current.

Things it will never do: use an image model other than GPT Image 2, call the video API,
generate without an OKAY, type a password, or print a key.

## Costs and timing

| Item | Model | Setting | Measured |
|---|---|---|---|
| character / environment / element sheet | gpt-image-2 | 1K high | about 60 s |
| storyboard | gpt-image-2 | 1K high | about 60 s |
| clip | Seedance 2.5 in the workspace | per `video-settings.txt` | workspace dependent |

Sheets run in parallel, so a three-sheet job is one minute of waiting, not three.

## Status of the pieces

| Piece | State |
|---|---|
| Role and manual Markdown | complete |
| `gen_image.py` | complete, tested with `--dry-run`; live calls bill the key holder |
| `new_job.py` | complete |
| `browser_video.py` `login` and `inspect` | complete |
| `browser_video.py` `submit` | scaffold: the flow is written, the locators in `selectors.json` must be mapped once from an `inspect` dump before the first clip |

---

## How it all works, start to finish

This section is the explainer. Read it once and the rest of the repo makes sense.

### The idea in one paragraph

A film is made from a small set of **sheets** (one image per recurring character, place and
prop, generated once and approved once) and a sequence of **scenes**. Every scene's clip is
generated from a written prompt plus the approved sheets attached as references. Nothing
else goes to the video model: no start frame, no end frame, no storyboard. The sheets carry
identity; the prompt carries what happens. A main agent runs the whole thing from Markdown
manuals and deploys one subagent per sheet or scene, and every image or clip stops at a
gate in the chat for the user to approve.

### Who does what

| Piece | Role |
|---|---|
| **Main agent** (the Claude Code session, reads `CLAUDE.md` then `MAIN.md`) | Talks to the user. Runs intake, writes the plan and the prompt files, deploys subagents under fixed conditions, runs the gates, routes feedback, keeps `STATUS.md` and reports credits at milestones. Never generates anything itself. |
| **Sheet agents** (`roles/character-sheet.md`, `environment-sheet.md`, `element-sheet.md`) | One agent per sheet. Reads the prompt file the user may have edited, generates one image with GPT Image 2, checks it, reports. Regenerates only on feedback from the main agent. |
| **Storyboard agent** (`roles/storyboard.md`) | Combines the approved sheets into a grid of keyframes for one scene. This is the client's sign-off image. It is never fed to the video model. |
| **Video director** (`roles/video-director.md`) | Decides which sheets a scene needs, writes the sealed video prompt, drives the ElevenLabs web workspace in a Camoufox browser to submit both, downloads the clip, checks it, and writes the handoff line for the next scene. |

Subagents never talk to the user and never ask questions mid-task. They write only inside
their own folder plus one row in the log. The main agent continues a conversation with a
subagent by message, so feedback goes to the agent that made the thing, with its context
intact.

### The pipeline, step by step

1. **Intake** (`MAIN.md` §1). The user drops a brief. The first question is scene length
   (6 s, 10 s, or decide). Ground rules get locked: aspect, palette in hex, the look, the
   forbidden list, the reroll budget. A brief that already answers these skips the
   questions.
2. **Plan** (§2). The main agent writes a registry of persistent characters, environments
   and elements, breaks the brief into scenes with their tag sets and opening states, and
   writes one prompt file per sheet into `jobs/<job>/plan/`. Human character prompts carry
   the REALISM block (the anti-wax rule). The user edits any file in Notepad and says OKAY.
3. **Sheets** (§3.1 to 3.3). One subagent per sheet, all in parallel, GPT Image 2, about a
   minute each. Each image stops at a gate with its full Windows path. Approval copies it to
   `approved.png`. A sheet is approved against the registry lock by lock: a mark on the wrong
   side fails the sheet, and small marks get their own close-up panel.
4. **Scene card** (§5.1). The main agent writes `card.md` for the scene: motion map,
   director's brief, the lens resolved to a field-of-view step, the tag set, the beats with
   times, the opening and arrival states as positions, the dialogue with its word count.
   Named cameras, lenses, directors and film stocks stop on the card and never reach a
   prompt.
5. **Storyboard** (§5.2, optional, `Storyboard: ON` in the settings). The storyboard agent
   writes the prompt (OKAY), generates the grid (gate). The client signs the scene off on it.
6. **Clip** (§5.3). The video director writes `video.refs.txt` (the sheets this shot needs,
   attach order, strongest first, off-screen handles left out) and `video.prompt.txt` (the
   seventeen-block sealed prompt from Leo's P-04 anatomy). Both stop at an OKAY. On GO the
   browser submits the prompt with the sheets attached, waits, downloads the clip. Gate.
7. **Handoff** (§5.4). The director writes `ARRIVAL OBSERVED`: what the approved clip
   actually ends on, as positions and states. The main agent copies it into the next card
   as the opening state and carries the reference set forward. That is continuity without
   frames: the next prompt opens on the clip that exists, with the same references, and the
   carried states are repeated in the prompt's positive locks.
8. **Close** (§6). Every item approved in `STATUS.md`, every run in `log.csv`, and the
   final credit tally: spent, kept, thrown away, failed.

### The rules that keep it working

- **Fix the sheet, never the frame** (§4.3b). GPT Image 2 obeys the attached reference
  over the prompt text. If a storyboard or clip shows a character, prop or room wrong and
  the sheet shows the same thing, the sheet is redone and re-approved, then the scene is
  regenerated. Two identical failures on a scene is the hard stop. A change of look (wet,
  coat off, orange sweater) is a new sheet, never an edit request.
- **No frames, no storyboard in a video generation.** Tested by Leo: a start or end frame
  pins the model and the motion gets worse; the storyboard shows one angle and the clip
  gets worse. Sheets only.
- **Attach only what is on screen.** A tag for an absent object gets forced in. But every
  object the action touches must have a sheet; an object with no sheet is a reel-back, not
  a sentence in the prompt.
- **Anti-wax.** Human sheets carry the REALISM block from the `realist-portrait` skill,
  written as positive states, because there is no negative field and "no plastic skin"
  summons plastic skin.
- **Positive phrasing, measured values, nothing named.** Speeds in km/h, angles in degrees,
  white balance in Kelvin, colour as material plus light, left and right from the camera.
- **Vague feedback spends nothing.** "Not it" gets up to three questions before anything
  regenerates. Specific feedback goes to one agent, never broadcast.
- **Reel-back.** A scene is never deployed while a sheet in its tag set is unapproved. The
  main agent says what is missing and asks.
- **Credits at milestones only.** Every run logs its credits, but the user hears a figure
  only when all sheets are approved, when a scene is done, and at close, with kept versus
  thrown away versus failed.
- **Every path in the chat is a full Windows path**, pasteable into Explorer.

### Where files land

```
jobs\<date>-<slug>\
  brief.md  ground-rules.md  STATUS.md  log.csv
  plan\        the registry, scenes, one prompt file per sheet, video-settings.txt
  sheets\      <type>-NN-<handle>\v1.png v1.prompt.txt approved.png report.md
  scenes\      scene-NN\card.md storyboard.prompt.txt storyboard-v1.png storyboard-approved.png
                        video.refs.txt video.prompt.txt video-v1.mp4 video-approved.mp4 report.md
```

`FOLDER-PROTOCOL.md` is the naming law. Versions are never deleted, never overwritten, and
only the main agent writes an `approved` file.

### The tools

| Tool | What it does |
|---|---|
| `tools/new_job.py <slug> [--images-only]` | Makes the job skeleton. `--images-only` writes `Video: OFF` so no clip is ever attempted. |
| `tools/gen_image.py` | One GPT Image 2 call on the ElevenLabs Image and Video API. Loads the key itself (env, `.env`, or a private file outside the repo), never prints it. Refuses to overwrite a version. Logs the run with its credits and generation id. |
| `tools/browser_video.py login` | Opens a real Camoufox window once; the user logs in by hand. The session lives in `browser-profile/` and is never read by an agent. |
| `tools/browser_video.py inspect` | Dumps the workspace's buttons and inputs so `tools/selectors.json` can be filled once. |
| `tools/browser_video.py submit` | Picks the model and settings, uploads the reference sheets, pastes the prompt, generates, downloads, logs. One attempt per call. |
| `tools/credits.py --scope sheets \| scene-NN \| all` | The milestone tally from `log.csv`: spent, kept (byte-identical to an approved file), thrown away, failed, and runs with no figure. |

### What is not in the repo

`.env`, the private key file, the browser profile, `tools/selectors.json` and every
`jobs/` folder are ignored. The key never appears in a prompt, a log, a report or the chat.

### Where the method comes from

`libraries/` holds Leo's AI Production kit as ground truth: the camera, lens, look and
movement libraries, the Seedance prompt architecture, the feature pipeline, the CINEDANCE
and Acting skills, the `realist-portrait` skill with its reference banks, the P-04 sealed
prompt anatomy, and The Window Map worked example. `PROMPT-STRUCTURES.md` is the distilled
shape of every prompt this pipeline writes; when a structure is not enough, its last section
says which library to open.
