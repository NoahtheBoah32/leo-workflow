# START HERE

## Open it

1. VS Code → **Open Folder...** → `C:\Users\User\Documents\AANG V2\NEUTRA AUTOMATION\Leo Workflow`
2. Open the Claude Code panel (the Claude icon in the sidebar, or `Ctrl+Shift+P` → "Claude Code: Open").
3. Claude reads `CLAUDE.md` on its own. It now knows it is the main agent.

## Say this

Type one message. Something like:

```
images only. new job: a doctor shows an old lady her chest x-ray in a small clinic,
warm and hopeful, three scenes.
```

`images only` keeps the video step off, so no Seedance credits are touched. Drop those two
words when you want clips.

## What happens next

1. It asks one question: **6 seconds, 10 seconds, or decide?** Answer.
2. It proposes the ground rules (aspect, palette, look, forbidden list). Say **OKAY** or edit
   the file it names.
3. It writes the PLAN: a Persistent Characters list, environments, elements, scenes, and one
   prompt file per sheet in `jobs\<job>\plan\`. Open any file in Notepad, edit, save. Then
   say **OKAY**, or **REVISED CHARACTER 01** for the ones you changed.
4. Sheets generate in parallel, one subagent each, GPT Image 2, about a minute.
5. Each image stops at a **GATE** in the chat with its path. Open it, then say **approve**
   or say what is wrong. Vague feedback gets three questions before anything regenerates.
6. Scene 01: it writes the card, then the still prompt (OKAY), the still (gate), the end
   frame prompt (OKAY), the end frame (gate). Then scene 02 from scene 01's end frame.
7. With `images only`, it stops there and says so.

## Where things land

```
jobs\<date>-<slug>\
  plan\          the files you edit
  sheets\        character-01-doctor\v1.png, approved.png ...
  scenes\        scene-01\still-v1.png, end-v1.png ...
  STATUS.md      what is approved, what is waiting
  log.csv        every run
```

## Before the first video (later)

From your own terminal, once:

```
pip install -U "camoufox[geoip]"
python -m camoufox fetch
python tools\browser_video.py login       log in by hand, press Enter
python tools\browser_video.py inspect     dumps the workspace buttons to map once
```
