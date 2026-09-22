# Neutra DC — AI Production

Workspace for **narrative work built at scale on Seedance 2.5**: shorts, episodes, features —
anything with a script, a recurring cast and more than a handful of shots. The process is
[Seedance-Feature-Pipeline.md](Seedance-Feature-Pipeline.md) (**Phase 0–9**), which follows
the production order Higgsfield used on *Cully Hill Boys*.

Default output is **prompt text and specs only** — write the prompt, don't call a generator,
don't claim an image/video/audio was produced. The user runs the generation and brings
results back.

**Exception — explicit run command:** when the user explicitly says to generate a specific
shot right now ("run it", "generate this", "submit SHOT-014") — never inferred from being
asked to write or review a prompt — invoke the sibling project's script:
`python3 "../Image to Video/Automation/neutradc.py"` (see
[Automation/README.md](../Image%20to%20Video/Automation/README.md)). It supports
**Seedance, Seedream and GPT-image only** — Kling and Midjourney are not wired in; say so
rather than substituting a model. Never read, print or paste `.env` contents anywhere; the
script loads its own credentials. Prefer `--dry-run` first unless the user has already
reviewed one.

---

## The three bans (binding in this workspace)

1. **No director names, no signature works, no equipment names in prompt text.** No director,
   film title, DP, camera body, lens model or film-stock brand reaches the model. The craft
   libraries are used at **Phase 3 to decide** the look; Phase 4 renders that decision as
   observable description. Named picks live in the shot card, never in the prompt.
2. **No 1500-character prompt cap.** That is a Dreamina constraint and does not apply here —
   working Seedance 2.5 prompts run 2 000+ words. Budget by block necessity: every block
   present must be load-bearing, and never trim a needed block to hit a number.
3. **No model-authored screenplay, no model-generated music.** Claude scaffolds the script;
   a named human authors it. Music is recorded or licensed first, cut into **12-second blocks
   on the vocal's breaths**, and fed in as audio references. Diegetic ambience, foley and
   dialogue *do* come from Seedance in-pass — that is not music.

Full rationale, translation tables and gates: the pipeline's **§The three bans**.

---

## The Cully Hill Boys rule (binding production order)

Every narrative production here follows the order Higgsfield used on *Cully Hill Boys*.
Don't skip a step or start one before the step before it is done. Evidence and numbers:
[Cully-Hill-Boys-Benchmark.md](Cully-Hill-Boys-Benchmark.md).

1. **Human script first.** A named person writes it; it is cut into numbered scenes (BAN 3).
2. **Consent before likeness.** Any real person's face or voice needs a signed agreement
   (pay, scope, script approval, source files deleted within 30 days of wrap) before any
   asset is made. Otherwise, invent the character.
3. **Music before picture.** Recorded or licensed, cut into 12 s blocks on the breaths (BAN 3).
4. **Assets before any video.** Every character, location and prop exists as a saved
   reference on grey — people front, back and 3/4 close-up; locations at 3/4 with one fixed
   anchor object; props from several angles. **Every change of look is its own asset**
   (`_wet`, `_wound`), never a text note. Fix flaws by editing, and inspect before saving.
5. **One look per storyline.** Lock a style "world" per storyline or register once, and
   reuse it verbatim in every prompt for that storyline.
6. **Describe everything, every time.** Each shot prompt is complete on its own: who and
   what is in it, a map of the space, the first frame, lens, camera and cuts, timed action,
   acting and voice, light, physics, sound, and the must-stay-true locks. The model has no memory.
7. **Give the model a corner, not a room.** Exact positions, distances and gaze; a map, not
   guesswork; only the references this shot needs.
8. **Change one thing per attempt, and log every attempt.**
9. **After 10–15 failed attempts, simplify the shot, not the words.** Split it, drop an
   action or change the angle. For hard movement, shoot a real phone reference and attach it.
10. **Repair, don't reroll.** A good clip with one flaw gets a local edit (Phase 6).
11. **Cut to the script.** Every kept clip maps to a scripted beat; grade the whole film once.
12. **Hand over everything.** Script, assets, prompts and the log, together.

Where their production and our rules differ, **our rules win**: their prompts named cameras
and directors, and ours don't (BAN 1).

---

## Request routing

- **Explicit run/generate command on an existing prompt file** → skip prompt-writing, call
  `neutradc.py` per the path above. Seedance/Seedream/GPT-image only.
- **Idea, premise or brief with no script yet** → **Phase 1**. Method is the ten steps in
  [Ideation-and-Script-Library.md](Ideation-and-Script-Library.md);
  the shooting script needs a named human author (BAN 3) and Claude's role is scaffolding.
- **Script exists, no assets yet** → **Phase 2**. Character sheets on neutral **grey**
  (face view + full-body front & back), locations at **3/4 angle**, props isolated and
  unbranded, each saved under its exact `@handle`.
- **Assets exist, writing a shot** → **Phase 3 → 4**. Build the shot card first (motion map,
  director's brief, look picks, lens → FOV step, flattened tag set), then the sealed
  17-block prompt. Read
  [Seedance-Prompt-Architecture.md](Seedance-Prompt-Architecture.md) before writing —
  don't work from memory.
- **A clip came back with one local defect** → **Phase 6**, not a reroll. Region edit /
  Seedream / Nano Banana. Repair the *asset* when the defect traces back to a Phase 2 element.
- **Still image whose subject is a person** (character sheet, casting look, brand face) → run
  the [realist-portrait](.claude/skills/realist-portrait/SKILL.md)
  skill end to end. Mode C for recurring cast.
- **Any generated scene still** → **ask the user for both photography-style axes first, every
  time**: the **Look** and the **Stance**
  ([Photography-Styles-Library.md](Photography-Styles-Library.md) §1).
  No silent default on either. Whatever Look is locked reaches the prompt as **observable
  description, never a named stock or auteur** (BAN 1).
- **Single reference image → one shot**, an ad, product, architecture, FPV, or **any Kling
  work** → wrong workspace. That is the Stage 0–9 process in
  [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md), where the
  1500-char cap *does* apply.
- **Build a person / persona / virtual host** → the `persona-architect` agent in the sibling
  project.

---

## Ground-truth libraries (read what's relevant, don't work from memory)

**In this workspace:**

- [Seedance-Feature-Pipeline.md](Seedance-Feature-Pipeline.md) — the Phase 0–9 process, its
  gates, the three bans, the shot-card template, the old→new stage mapping, folder structure.
- [Seedance-Prompt-Architecture.md](Seedance-Prompt-Architecture.md) — the prompt craft: the
  17-block order, style-distributed rule, `@tag` and context-isolation rules, the cut/timing
  scale, the **FOV anchor table** (degrees, never mm), optical techniques, special protocols,
  the 2.5 capability envelope, and the pre-flight checklist.
- [Sources/higgsfield-seedance-clean-SKILL.md](Sources/higgsfield-seedance-clean-SKILL.md) —
  Higgsfield's shipped production skill, archived verbatim. The primary source; consult it
  when the architecture file is ambiguous.
- `template-project/` — the empty Phase 0–9 folder tree. Copy it to start a production.

**Craft libraries, local to this workspace** (copied from the sibling project — edits here do **not** propagate back):

- [Ideation-and-Script-Library.md](Ideation-and-Script-Library.md) — Phase 1's ten steps
- [Camera-Movements-Library.md](Camera-Movements-Library.md) · [Camera-Framing-Angle-Library.md](Camera-Framing-Angle-Library.md) · [Depth-of-Field-Library.md](Depth-of-Field-Library.md) · [Camera-Look-Library.md](Camera-Look-Library.md) · [Transition-Library.md](Transition-Library.md) · [FPV-Drone-Movements-Library.md](FPV-Drone-Movements-Library.md) · [Film-Director-Library.md](Film-Director-Library.md)
- [Photography-Styles-Library.md](Photography-Styles-Library.md) — the two axes (Look + Stance); carries the mandatory style question
- [SOUL-Image-Generation-Library.md](SOUL-Image-Generation-Library.md) · [Lenses/Zeiss-Supreme-Prime-Lens-Library.md](Lenses/Zeiss-Supreme-Prime-Lens-Library.md)
- [Higgsfield-Prompt-Formats.md](Higgsfield-Prompt-Formats.md) — token/preset/example catalogue. Its §2.4 style-header block is **legacy and not used here**.
- Skills: [realist-portrait](.claude/skills/realist-portrait/SKILL.md) · [elevenlabs-v3-audio-tags](.claude/skills/elevenlabs-v3-audio-tags/SKILL.md) · [multi-speaker-podcast-assembler](.claude/skills/multi-speaker-podcast-assembler/SKILL.md) · agent: [director-dp](.claude/agents/director-dp.md)

**Still in the sibling project, by design:**

- [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md) — the Stage 0–9 pipeline. A *different* process, not a dependency; linked so you can hand a request to the right one.
- [Automation/README.md](../Image%20to%20Video/Automation/README.md) — `neutradc.py` and its credentials live there and are not duplicated.

> This workspace is otherwise **self-contained** — it can be moved, zipped or handed on and
> every library link still resolves. Only the two pointers above need `Image to Video/` to
> sit alongside it.
>
> **Fork warning:** the craft libraries here are copies taken Sep 2026. They will drift from
> the sibling project's originals. If a library needs a real fix, decide which copy is
> canonical and apply it to both.

---

## Output conventions

- Finished prompt ships as its own copyable fenced code block in the chat reply, never buried
  only in a file.
- Negative prompt (if the model has a dedicated field) in a second code block right after —
  and keep exclusions confined to the style line and the audio line; everything else positive.
- **No character cap** (BAN 2). Length comes from block coverage, not repetition — say each
  important thing once.
- Every prompt is a **sealed single-shot document**: no scene numbers, no script headings, no
  summaries of prior shots, no "as above / continues", no unused tags. The model has no memory.
- Never pass a phase gate without its condition met; the gates are listed per phase.
