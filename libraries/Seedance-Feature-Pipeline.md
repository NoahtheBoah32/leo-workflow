# Seedance Feature Pipeline — the Cully Hill Boys method

A **separate, parallel pipeline** for narrative work built at scale on Seedance 2.5:
shorts, episodes, features, anything with a script, a recurring cast and more than a
handful of shots. It follows the production order Higgsfield actually used on
*Cully Hill Boys* (1 h 54 m, $2 M, ~4 weeks) and merges it with everything in
[Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md) that still applies.

> **This does not replace the existing pipeline.** Both stay live:
>
> | Use | When |
> |---|---|
> | **[Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md)** (Stage 0–9) | A reference image → one shot. Ads, product, architecture, FPV, single clips, Kling work, anything Dreamina-bound. |
> | **This file** (Phase 0–9) | A script → a cast → many shots → a cut piece. Seedance 2.5 only. |
>
> Phase numbers deliberately mirror the old Stage numbers so the two read side by side.

**Division of labour — unchanged.** Claude's output here is **prompt text and specs only**:
the Phase 1 script scaffold, the Phase 2 asset prompts, the Phase 4 per-shot prompts, the
Phase 7 audio strings. Claude does not call a generator unless the user gives an explicit
run command (see [CLAUDE.md](CLAUDE.md)).

**Ground truth for prompt construction:** [Seedance-Prompt-Architecture.md](Seedance-Prompt-Architecture.md).
Read it before Phase 4. This file is the *process*; that file is the *prompt craft*.

---

## The three bans

These are the three research findings, enforced as hard rules on this pipeline. They are
the main behavioural difference from the old Stage 0–9 process, so they sit at the top.

### 🚫 BAN 1 — No director names, no signature works, no equipment names in prompt text

Higgsfield's shipped skill is categorical: names "get ignored or break complex moves."
Nothing named reaches the prompt — no director, no film title, no DP, no camera body, no
lens model, no film stock brand.

| ❌ Banned in prompt text | ✅ Write instead |
|---|---|
| "Guy Ritchie coverage" | "snap-in inserts on every named object, whip cut between faces mid-line" |
| "Edgar Wright snap" | "action lands on the cut, each beat 0.4 s, hard cut on impact" |
| "shot on Arri Alexa 65" | "wide tonal latitude, highlight roll-off soft at the top, blacks hold detail" |
| "Master Anamorphic" | "anamorphic optical flares, oval bokeh, slight edge softness" |
| "Kodak Tri-X grain" | "fine organic grain, milky filmic black floor" |
| "Deakins lighting" | "one hard motivated key from a practical, deep unfilled shadow opposite" |

**The libraries stay load-bearing — they just move upstream.**
[Film-Director-Library.md](Film-Director-Library.md),
[Camera-Look-Library.md](Camera-Look-Library.md),
[Photography-Styles-Library.md](Photography-Styles-Library.md) and
[Lenses/Zeiss-Supreme-Prime-Lens-Library.md](Lenses/Zeiss-Supreme-Prime-Lens-Library.md)
are used at **Phase 3 to decide** the look. Phase 4 then renders that decision as
observable description. A name may appear in our internal working docs; it never appears
in the text sent to the model.

*Why this is a ban here and a hedge in the architecture file:* Higgsfield's own published
2.5 examples break this rule constantly and still work. But on a many-shot piece a name is
a lossy instruction competing with the precise line next to it, and reroll cost is the
thing this pipeline exists to control. Named shorthand is a luxury a single ad shot can
afford and a 400-shot cut cannot.

### 🚫 BAN 2 — No 1500-character prompt cap

Stage 1 of the old pipeline caps positive + negative at **1500 characters**. That is a
**Dreamina** limit and it does not apply here. Higgsfield's working Seedance prompts run
**2 000+ words**. Enforcing the cap on this pipeline actively causes failure, because the
blocks it forces you to cut — `LOCATION MAP`, `FIRST FRAME / BLOCKING`, `POSITIVE LOCKS` —
are the exact ones that prevent multi-shot drift.

- **Budget by block necessity, not by character count.** Every block present must be
  load-bearing; drop blocks the shot does not need (§Phase 4), never trim a needed block
  to fit a number.
- Say each important thing **once**. Length comes from coverage, not repetition.
- If a prompt must also run on Dreamina, write the Seedance version first and derive a
  reduced cut — not the reverse.

### 🚫 BAN 3 — No model-authored screenplay, no model-generated music

The $2 M film hired a human screenwriter and recorded its music before generating anything.

- **Script.** The screenplay is **human-authored**. Claude may scaffold — premise pressure,
  structure options, beat gaps, shot segmentation, formatting, registry, locks — and may
  draft passages on request, but the shooting script is not shipped as model output. A
  model-written draft is a **scaffold awaiting an author**, and Phase 1's gate is a named
  human sign-off.
- **Music.** Never generated with the video, and never generated at all on this pipeline.
  The track is **recorded or licensed first**, then cut into **12-second blocks on the
  vocal's breaths**, and each block is fed in as an audio file reference (Phase 7).
  This replaces Stage 7C (Eleven Music) for this pipeline.
- Diegetic ambience, foley and dialogue **do** come from Seedance, in the same pass as
  picture. That is not music.

---

## Pipeline map

```
Phase 1  SCRIPT (human)         → locked shooting script + @handle registry + locks
Phase 2  CANVAS / ASSETS        → every character, location, prop as a saved element
Phase 3  BREAKDOWN + LOOK       → per-shot cards: motion map, director's brief, flattened tags
Phase 4  PROMPT                 → one sealed 17-block prompt per shot
Phase 5  GENERATE               → Seedance 2.5, picture + diegetic audio in one pass
Phase 6  REPAIR                 → region edit / Seedream / Nano Banana, not a reroll
Phase 7  AUDIO                  → dialogue locks, ambience, pre-recorded music in 12 s blocks
Phase 8  ASSEMBLE               → cut, mux, grade
Phase 9  HANDOFF                → squint test, canvas, generation log
         ▲                                    │
         └──────── Phase 0 GROUND RULES ───────┘  (set once, checked at every gate)
```

## Phases at a glance

| # | Phase | Output | Gate — do not pass until |
|---|---|---|---|
| 0 | Ground Rules | `ground-rules.md` | Ratio, palette hex, runtime, forbidden list all locked by the user |
| 1 | Script | `script.md` + registry | A **named human** has signed off the shooting script |
| 2 | Canvas / Assets | element library | Every `@handle` in the registry resolves to a saved element |
| 3 | Breakdown + Look | one card per shot | Every shot has a motion map, a brief, and a flattened tag set |
| 4 | Prompt | one prompt per shot | Pre-flight checklist passes; no banned name present |
| 5 | Generate | raw clips | QC gate passes; run logged either way |
| 6 | Repair | fixed clips | Defect fixed without re-rolling the whole clip |
| 7 | Audio | audio stems | Music exists as pre-recorded 12 s blocks, not a prompt |
| 8 | Assemble | cut | Every clip maps to a scripted beat |
| 9 | Handoff | deliverable + log | Squint test passes at thumbnail size |

---

## Phase 0 — Ground Rules

**Goal:** the constants every later gate checks against. Set once, never mid-flight.

**Do this — ask the user, never invent:**

1. **Aspect ratio.** Seedance 2.5 takes anything from **9:16 to 21:9**. Scope reference
   point: *Cully Hill Boys* delivered **2.39:1** (4096 × 1716).
2. **Palette as hex + exclusions.** A hex code beats "warm and premium." Flag anything provisional.
3. **Runtime target** → shot count. Clip ceiling is **30 s** on 2.5. Budget ~1 shot per generation.
4. **Forbidden everywhere** — legible text, logos, and any subject-matter fact that can
   never be violated. This list becomes a positive lock in every prompt.
5. **Reroll budget.** State it as a number up front. Half of the $2 M reference film was
   rerolls; this is the pipeline's dominant cost and it is decided here, not at Phase 5.
6. **Start the generation log at run #1**, not after the first good result.

**Carried over unchanged from Stage 1:** palette-as-numbers, aspect lock, forbidden list, log-from-run-1.
**Dropped:** the 1500-char cap (BAN 2). **Added:** reroll budget, 30 s ceiling, 9:16–21:9 range.

> **Gate 0** — all six written down and confirmed by the user.

---

## Phase 1 — Script (human-authored)

**Goal:** a shot-sized shooting script the rest of the pipeline consumes one shot at a time.

**Method:** the ten steps in [Ideation-and-Script-Library.md](Ideation-and-Script-Library.md),
unchanged — premise with a wound → emotional core → structure → four-input brief → draft →
formatting rules → scene segmentation → shot breakdown → `@handle` registry → locks in text.

**What changes on this pipeline:**

1. **Claude scaffolds; a human authors.** Claude pressure-tests the premise, offers
   structures, finds beat gaps, segments scenes into shots, formats, builds the registry and
   writes the locks. The shooting script itself carries a human author (BAN 3).
2. **Shot ceiling is 30 s, not 15 s.** One shot = one generation, so a 30 s shot is one
   render. Recount the shot budget against that — it changes the script's shape.
3. **Registry is written to be flattened.** Every character, location and prop gets a fixed
   `@handle` *and* a per-shot presence column, because Phase 3 must be able to produce the
   exact tag set for one shot with nothing else attached (context isolation).
4. **Dialogue gets a word count per line.** Not just the line — the count.
   `"Pull it, Oli." — exactly three words.` Seedance will not tolerate silence and fills it
   with a mumble or a line in another language. See Phase 7.

**Output:** `script.md` — `TITLE / runtime / ratio`, `EMOTIONAL CORE`, `REGISTRY`, `LOCKS`,
then `--- SCENE n ---` blocks of numbered `[SHOT n]` entries.

> **Gate 1** — a named human has signed off the shooting script. Record the name in the file.

---

## Phase 2 — Canvas / Asset build

**Goal:** every character, location and prop exists as a **saved element** before a single
video prompt is written. This is the phase that decides picture quality.

> "Build those as assets first, and the video generation almost takes care of itself."
> "The better the input image, the sharper the final video."

**Do this, per registry entry:**

1. **Characters → sheet on a neutral grey cyclorama.** Grey outperforms white and black;
   this is Higgsfield's tested finding and matches our own default.
   - Minimum **two readable views**: one where the **face** is clearly visible, one
     **full-body** for the outfit — so the model never guesses.
   - Our house default already satisfies this in one generation: a **single-generation
     tiled grid with full-body front *and* back**
     ([realist-portrait](.claude/skills/realist-portrait/SKILL.md)). Keep it.
   - Recurring cast → run the full `realist-portrait` skill, Mode C.
   - **Family / relational likeness** is stated explicitly, feature by feature — inherited
     eye spacing, nose shape, brow, gaze — not left to "looks like his mother."
2. **Locations → 3/4 angle wide.** Shows more of the room, gives the model better depth
   perception, renders without breaking. Frontal plates break more often.
3. **Props → isolated, on grey, unbranded.** Named in words as well as shown, because the
   model drops small detail that exists only in the image.
4. **Ask the two photography axes before any generated still** — the **Look** (§2–§7) and
   the **Stance** (§8) from [Photography-Styles-Library.md](Photography-Styles-Library.md).
   Every time, no silent default. The locked pair carries through every shot.
   ⚠️ Whatever Look is chosen, it reaches Phase 4 as **observable description, never a
   named stock or auteur** (BAN 1).
5. **Save each as an element under its exact `@handle`.** The handle in the registry and the
   handle in the canvas must match character for character.
6. **Inspect before saving.** Examine every detail; regenerate if anything is off. A flaw
   saved here propagates into every shot that references it.

**Carried over from Stage 2:** min resolution, clean composition, one real photo per named
element, licence-tiering every source (attach-freely vs eyes-only), motion references.

> **Gate 2** — every `@handle` in the Phase 1 registry resolves to a saved, inspected element.
> No shot enters Phase 4 with an unresolved tag.

---

## Phase 3 — Breakdown & Look decisions

**Goal:** one working card per shot, holding every decision Phase 4 needs, so no decision
gets made while writing prompt text.

**Do this, per shot:**

1. **Motion map** — walk the frame in regions and tag every element
   **Locked / Moves / Ambiguous-decided**, exactly as Stage 3. Recorded once per reference
   plate and reused by every shot off that plate.
2. **Director's brief** — dramatic intent · lead motion · supporting motion · ambient
   motion · what the camera *accomplishes* · pace. Use the
   [director-dp](.claude/agents/director-dp.md) agent; full framework in
   [Film-Director-Library.md](Film-Director-Library.md).
3. **Look decisions, named internally.** Pick the movement from
   [Camera-Movements-Library.md](Camera-Movements-Library.md), the framing/angle from
   [Camera-Framing-Angle-Library.md](Camera-Framing-Angle-Library.md), the focus treatment
   from [Depth-of-Field-Library.md](Depth-of-Field-Library.md), the capture character from
   [Camera-Look-Library.md](Camera-Look-Library.md), the lens from
   [Lenses/Zeiss-Supreme-Prime-Lens-Library.md](Lenses/Zeiss-Supreme-Prime-Lens-Library.md).
   **Write the names on the card.** They stop here.
4. **Translate to a FOV step.** Convert the chosen lens to one of the nine discrete degree
   steps — 180° / 107° / 84° / 63° / 47° / 29° / 18° / 12° / 8°. Never mm in the prompt,
   never an off-table value. Table in
   [Seedance-Prompt-Architecture.md §5](Seedance-Prompt-Architecture.md).
5. **Flatten the tag set.** List *only* the `@handles` present in this shot. Every
   generation is a blank slate; a tag for an absent object gets forced into frame.
6. **Note the timing mode** — oner / sequential cuts / timed multishot / freestyle b-roll.

**Shot card template:**

```
SHOT [n]  ·  Scene [n]  ·  [oner | sequential | timed | b-roll]  ·  [duration]s

TAGS PRESENT      @handle, @handle          (nothing else — flattened for this shot only)
MOTION  locked    [rigid elements]
        moves     [lead] → [supporting] → [ambient]
BRIEF   intent    [what this shot is doing]
        camera    [what the move accomplishes dramatically]
        pace      [constant | accelerating | decelerating | held-then-moves]
LOOK    movement  [library name — internal only]
        framing   [library term — internal only]
        lens      [library name] → FOV [degree step]
        capture   [library name — internal only]
        look+stance  [locked pair — internal only]
DIALOGUE          "[line]" — exactly [n] words
```

> **Gate 3** — every shot has a card. Lens is resolved to a table FOV step. Tag set is
> flattened. Named library picks are recorded on the card and **nowhere else**.

---

## Phase 4 — Per-shot prompt

**Goal:** one sealed, self-contained prompt per shot. Craft reference:
[Seedance-Prompt-Architecture.md](Seedance-Prompt-Architecture.md) — read it, don't work from memory.

**Rules, in priority order:**

1. **Sealed single-shot document.** No scene numbers, no script headings, no summaries of
   prior shots, no "as above / continues", no unused tags. The model has no memory.
2. **No style prefix at the top.** The prompt opens on `SCENE CONTEXT`. Each style aspect
   lives in the block that governs it; only format/grain sits as a suffix before the locks.
   ⚠️ This supersedes the labelled style-header block of
   [Higgsfield-Prompt-Formats.md §2.4](Higgsfield-Prompt-Formats.md) — do not use it here.
3. **Write the visible.** Every abstraction becomes something seen and measured.
4. **CAMERA in 3rd position** of the core layers. At the end, FOV gets ignored; at the
   front, it fights identity.
5. **Positive phrasing.** State the target, never the prohibition. Confine exclusions to
   the style line and the audio line.
6. **Measured, not adjectival.** Speeds in km/h · atmosphere in % and metres · giant scale
   by human-height comparison · white balance in Kelvin · left/right from the camera.
7. **Colour = material + light beam + role**, never a flat list.
8. **Multishot:** FOV per segment + `"no drift mid-segment"`. Extreme FOV (8°, 107°)
   requires all four consistency mechanisms.
9. **No banned name anywhere** (BAN 1). **No character-count trimming** (BAN 2).

**Block order — use only the blocks the shot needs, drop the rest:**

```
SCENE CONTEXT · ACTIVE REFERENCES · LOCATION MAP · FIRST FRAME / BLOCKING · FORMAT MODE
OPTICS · CAMERA · ACTION · PERFORMANCE · PHYSICS · LIGHTING · COLOR GRADE · WARDROBE
AUDIO · STYLE · OUTPUT SETTINGS · POSITIVE LOCKS
```

**Reference line shape:**

```
@TAG: age + role/build + current state + unique visible features + action-critical details
      + voice (only if it has a line). 100% matches the reference.
```

Keep it **minimal** — long appearance text conflicts with the image and degrades it. But
state critical details in words even when they are on the reference: small text, logos, colour.

**Reference discipline:** one reference per element that must stay consistent. The ceiling
is 50 (30 image / 10 video / 10 audio) — **a ceiling to use deliberately, not to max out.**
A cluttered set is less coherent than a small chosen one. Role-scope each attachment: say
what it controls and what to ignore.

> **Gate 4** — the pre-flight checklist in
> [Seedance-Prompt-Architecture.md §10](Seedance-Prompt-Architecture.md) passes, **plus**:
> no director/film/DP/camera/lens/stock name present · no block cut to hit a character count ·
> tag set matches the shot card · dialogue word count stated.

**Output convention (unchanged):** the finished prompt ships as its own copyable fenced
code block in the reply. Negative prompt, if the model has a dedicated field, in a second
block right after.

---

## Phase 5 — Generation loop

**Goal:** a clip that passes QC, and a log entry either way. Most shots go round more than once.

1. **Attach the flattened reference set**, role-scoped, strongest first.
2. **Generate 2–4 variations** — the model is non-deterministic; small wording changes
   shift results a lot.
3. **Run the QC gate** (below).
4. **Diagnose before touching wording:**
   | Symptom | First move |
   |---|---|
   | Output inherited a reference's flaw | Lower or drop that reference — don't rewrite text |
   | Stated camera motion ignored | Restate as an observed *result* ("the horizon slides to lower-left"), not an intention ("tilt"); check CAMERA is in 3rd position |
   | Identity drifts by cut 3–4 | More reference material per face; at extreme FOV add all four consistency mechanisms |
   | Sequence falls apart between shots | The transition was vague — tighten `FIRST FRAME / BLOCKING`, not the action |
   | Motion static or warped | Pin an exact number — km/h, degrees, % — instead of an adjective |
   | Model invents its own cuts | Add "cuts only at the specified points, the camera does not cut on its own" |
   | Unscripted mumble or a foreign-language line | Dialogue word count missing — state it (Phase 7) |
   | One local defect, rest of the clip good | **Don't reroll — go to Phase 6** |
5. **Log the run either way.** Never re-attach a failed render as a reference.

**QC checklist:**
- [ ] Matches the locked Look + Stance, palette and lighting register
- [ ] Locked palette obeyed — zero excluded colours
- [ ] No legible/gibberish text, no generated logos
- [ ] Motion reads as the *intended* move, not generic drift
- [ ] Phase 3 **locked** elements stayed rigid — no warp, drift or flicker
- [ ] Phase 3 **moves** elements actually move, and plausibly
- [ ] Identity, wardrobe and prop state hold across every internal cut
- [ ] Screen direction and gaze consistent across cuts
- [ ] Cuts landed only where specified
- [ ] Dialogue is exactly the scripted words, no additions
- [ ] Subject-matter facts respected
- [ ] Log entry complete, approved or not

**Generation log:**

| # | date | shot | look+stance | model | prompt file | refs | FOV | output | ★ | reroll cost | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

> **Gate 5** — QC passes and the run is logged. Track cumulative reroll spend against the
> Phase 0 budget; when it runs hot, the fix is almost always a weak Phase 2 asset.

---

## Phase 6 — Repair pass

**Goal:** fix a local defect **without re-rolling the clip**. This is the phase that
protects the reroll budget, and it has no equivalent in the old Stage 0–9 pipeline.

| Tool | Use for |
|---|---|
| **Region edit** (Seedance 2.5) | One wrong spot in an otherwise good clip — fixes it without a full re-render |
| **Seedream** | Image-level repair of a plate or a frame |
| **Nano Banana** | Image/video edit passes |

**Rules:**
1. Try repair **before** any reroll. A reroll discards a good clip and re-rolls every
   other element too.
2. Repair the **asset**, not just the frame, when the defect traces back to a Phase 2
   element — otherwise it returns in every other shot using that element.
3. Log a repair as its own run, with what was fixed and by which tool.
4. If a defect survives two repair attempts, it is a prompt or asset problem. Go back to
   Phase 3/4; don't keep repairing.

> **Gate 6** — defect gone, nothing else in the clip changed.

---

## Phase 7 — Audio

**Goal:** dialogue that says exactly what was written, ambience that belongs to the room,
and music that was never generated.

### A) Dialogue — in-pass, with a word count lock
Seedance 2.5 generates **speech in the same pass as picture**. It does **not** tolerate
silence: given a gap, it invents a mumble or a line in another language.

- State the line **and its exact word count** in the `AUDIO` block:
  `Dialogue (English, audio only, no subtitles): @TAG: "Pull it, Oli." — exactly three words, nothing else spoken.`
- For a silent take, say the silence is intentional and complete — don't leave it unstated.
- Speaker form: `@Name ... says: "…"`, with the delivery as muscle movement, not a label.

### B) Ambience and foley — in-pass, diegetic only
Generated with picture. State the bed, the foreground detail, and the exclusion:
`NO MUSIC. SFX ONLY — diegetic sound and live audio throughout.`

### C) Music — pre-recorded, fed in as blocks  🚫 never generated (BAN 3)
1. **Record or licence the track first**, before generating the picture it scores.
2. **Cut it into 12-second blocks, split on the vocal's breaths** — not on a fixed grid.
3. **Feed each block in as an audio file reference** (10 audio references per generation).
4. Picture is then generated *to* the music, which is why the track has to exist first.

### D) Voiceover — ElevenLabs, where a scene needs narration
Unchanged from Stage 7A: ~2.5 words/sec · tone from the locked signature · stability
40–60 % for narrative, 70 %+ for flat corporate read. Tag scripts with
[elevenlabs-v3-audio-tags](.claude/skills/elevenlabs-v3-audio-tags/SKILL.md).

> **Gate 7** — no line was improvised by the model, and the music existed as audio files
> before the shots it scores were generated.

---

## Phase 8 — Assembly

1. **Cut to the script**, not to the best clips. Every clip maps to a scripted beat; cut
   anything that doesn't, however good it looks.
2. **One transition device**, reused at every boundary. For match cuts: take the prior
   clip's last frame as the next shot's reference and open the new prompt on the *same body
   position* the clip ended on ([Transition-Library.md](Transition-Library.md)).
3. **Grade once, across the whole cut** — not per clip.
4. **Mux:**
   ```
   ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -shortest final.mp4
   ```
   Or Premiere / Resolve for real sync control. Multi-speaker dialogue assembly:
   [multi-speaker-podcast-assembler](.claude/skills/multi-speaker-podcast-assembler/SKILL.md).

> **Gate 8** — every clip in the cut maps to a beat in the Phase 1 script.

---

## Phase 9 — Handoff

1. **Squint test the whole cut at thumbnail size.** Does it read as one piece, or as a
   set of clips? Identity drift and grade breaks show up here that pass shot by shot.
2. **Two tiers:** strongest clip per shot for review, full set underneath for iteration.
3. **Publish the canvas** — script, registry, elements, per-shot prompts and the generation
   log, together. The reference film's prompts are open by default; ours should at minimum
   be *legible to the next production*.
4. **Close the loop:** reroll spend vs the Phase 0 budget, and which phase caused the
   overrun. That number is the only reliable guide to what to fix next time.

> **Gate 9** — squint test passes, log is complete, reroll variance explained.

---

## Old pipeline → new pipeline

| Stage 0–9 | → | Phase 0–9 | Change |
|---|---|---|---|
| 0 Ideation & Script | → | **1 Script** | Human author required; 30 s shots; registry built to flatten; dialogue word counts |
| 1 Ground Rules | → | **0 Ground Rules** | 1500-char cap **removed**; 9:16–21:9; 30 s ceiling; reroll budget added |
| 2 Reference Library | → | **2 Canvas / Assets** | Grey cyclorama; 3/4 locations; saved elements keyed to `@handles` |
| 3 Motion Analysis | → | **3 Breakdown** (part 1) | Unchanged in method |
| 3.5 Director's Pass | → | **3 Breakdown** (part 2) | Merged; now also resolves lens → FOV step and flattens tags |
| 4 Prompt System | → | **4 Prompt** | Signature card + 5-slot line → **17-block sealed prompt**; style distributed, not prefixed |
| 5 Sequence Design | → | **8 Assembly** | Folded in; cut-to-script |
| 6 Generation Loop | → | **5 Generate** | Diagnosis table extended; repair split out |
| — | → | **6 Repair** | **New** — region edit / Seedream / Nano Banana before any reroll |
| 7 Audio | → | **7 Audio** | Dialogue + ambience now in-pass; **Eleven Music removed** (BAN 3) |
| 8 Assembly | → | **8 Assembly** | Grade once across the cut |
| 9 Handoff | → | **9 Handoff** | Canvas publish + reroll post-mortem added |

**Kept wholesale:** ask-don't-invent on ground rules · palette as hex · licence-tiering
references · the Locked/Moves/Ambiguous motion map · the Director's Brief · the two-axis
photography question · role-scoped references · generate 2–4 variations · diagnose before
rewriting · never re-attach a failed render · log from run #1 · the squint test · prompt
ships as a copyable code block.

---

## Folder structure

```
project/
├─ ground-rules.md              # Phase 0 — ratio, palette hex, runtime, forbidden list, reroll budget
├─ script.md                    # Phase 1 — shooting script + @handle registry + LOCKS + human author
├─ canvas/                      # Phase 2 — saved elements, one folder per @handle
│   ├─ characters/@name/        #   sheet on grey: face view + full-body front & back
│   ├─ locations/@loc_name/     #   3/4 angle wide plate
│   └─ props/@prop_name/        #   isolated on grey, unbranded
├─ shots/
│   └─ SHOT-[n]/
│       ├─ card.md              # Phase 3 — motion map + brief + look picks + FOV + flattened tags
│       ├─ prompt.md            # Phase 4 — the sealed 17-block prompt
│       └─ takes/               # Phase 5/6 — renders, repairs, which one is ★
├─ audio/
│   ├─ music/                   # Phase 7C — pre-recorded track + 12 s breath-split blocks
│   ├─ vo/                      # Phase 7D — ElevenLabs outputs
│   └─ stems/
├─ cut/                         # Phase 8
└─ generation-log.csv           # from run #1
```

Named library picks (director, lens, stock, auteur) live in `shots/SHOT-n/card.md` and
**never** in `prompt.md`. The card is the firewall that makes BAN 1 auditable: diff the two
files and any leaked name is obvious.

---

## Quick card

```
BANS      no director/film/DP/camera/lens/stock names in prompt text
          no 1500-char cap — budget by block necessity
          no model-authored screenplay · no model-generated music

ORDER     script → assets → cards → prompts → generate → repair → audio → cut → handoff

PROMPT    opens on SCENE CONTEXT (never a style prefix)
          CAMERA in 3rd position · FOV from the 9-step table · style in its home block
          positive phrasing · km/h · % and metres · Kelvin · left/right from camera
          one reference per element · sealed, no memory of other shots
          multishot: FOV per segment + "no drift mid-segment"

ALWAYS    ask the two photography axes · state dialogue word counts
          repair before reroll · log every run · cut to the script
```
