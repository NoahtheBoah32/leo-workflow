# Leo Workflow

Reference-image to AI-video, run by a main agent that deploys subagents from Markdown
role files. The human approves in the chat. The operating path is:

```
brief → PLAN files (edit in Notepad) → OKAY
      → character / environment / element sheets   (GPT Image 2, parallel, ~60 s each)
      → per scene: still → end frame (an edit of the still) → clip
        (Seedance 2.5 in the ElevenLabs web workspace, driven by Camoufox)
      → next scene starts from this scene's end frame
```

There is no ComfyUI in this path. The ComfyUI rig in the parent folder is the spec and
the demo; this folder is the operation.

## What is in here

| Path | What |
|---|---|
| `CLAUDE.md` | tells Claude Code it is the main agent and what to read |
| `MAIN.md` | the main agent's manual: intake, plan, deploy conditions, gates, feedback routing, the scene loop |
| `FOLDER-PROTOCOL.md` | the job folder layout and the naming law |
| `PROMPT-STRUCTURES.md` | the shape of every prompt (sheets, scene still, end frame, scene card, Seedance, Kling) |
| `roles/_contract.md` | rules every subagent follows |
| `roles/character-sheet.md` · `environment-sheet.md` · `element-sheet.md` | the sheet makers |
| `roles/scene-sheet.md` | combines approved sheets into the still and the end frame |
| `roles/video-director.md` | writes the video prompt and drives the browser |
| `tools/gen_image.py` | one GPT Image 2 call, saved and logged (stdlib only) |
| `tools/browser_video.py` | Camoufox: `login` once by hand, `inspect` to map the UI, `submit` a clip |
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
| scene still, end frame | gpt-image-2 | 2K high | about 120 s |
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
