# Ideation & Script Library

The front of [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md). Everything else in that pipeline assumes you already have *a shot* — a reference image and a reason to move the camera. This library covers the step before that: turning an idea into a **shot-sized script** that the rest of the pipeline can consume, one shot at a time.

Method adapted from Higgsfield's published AI-film workflow — the Academy "Santiago" director's course, the open-sourced *Hell Grind* feature archive, and the Seedance pipeline blog breakdowns. The governing principle is theirs: **the script is reverse-engineered from the generator's limits.** A shot is written to be exactly one Seedance/Kling generation, so nothing has to be re-cut later. Full research write-up and source list in [Higgsfield-Script-Workflow-Research/](Higgsfield-Script-Workflow-Research/).

**Division of labor (unchanged):** Claude's output here is **text only** — the premise, the emotional core, the structure, and the shot-numbered script. Claude does not generate video, audio, or images, and does not call any generator. The user takes the script forward into Stage 1 (ground rules) and Stage 2 (reference library), builds the assets, and runs generation.

---

## 0. When this stage runs

- **Runs first**, before [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md) Stage 1. Its output — a shot list with a character/location/prop registry — is the input to Stage 1's ground rules and Stage 2's reference library.
- **Skip it** when the user hands over a single standalone reference image and just wants that one shot moved. Ideation & Script is for pieces built from an idea rather than from an existing frame — shorts, ads, explainers, multi-shot sequences.
- **Partial entry is fine.** If the user already has a premise, start at §3. If they have a finished prose script, start at §7 (segment and shot-break it). Don't re-run steps that are already locked.
- **Ask, don't invent.** Premise, emotional core, structure, runtime, and aspect ratio are the user's calls. If any is missing and can't be inferred from the brief, ask — same discipline as Stage 1's "never invent a palette or aspect ratio."

---

## 1. The ten steps

Steps 1–4 are creative decisions a human makes. Step 5 hands the brief to the model. Steps 6–10 shape the draft into something the pipeline can consume.

### Step 1 — Premise in one sentence, with a wound

Shape: **character + a specific failure or conflict + the present-tense situation that forces them to deal with it.**

> "A footballer who failed to score a goal in the biggest match of his life, and now he's sitting in a psychologist's office trying to work through it." — the *Santiago* premise

- Not a topic ("a film about football") — a person, a concrete obstacle, a room they can't leave.
- One or two sentences. Everything downstream inherits from it.
- **Output:** a 1–2 sentence logline with a clear wound.

### Step 2 — Name the emotional core (the "think like a director" step)

Lock **the one feeling** the film delivers and **the one idea** underneath it.

- *Santiago* — feeling: quiet shame turning to release. Idea: a missed goal is not the end of an identity.
- This is the filter: any scene that doesn't serve it gets cut.
- It is reused verbatim later as the `Dramatic intent` line of the Stage 3.5 Director's Brief for the shots in this piece.
- **Output:** one feeling + one idea, written down.

### Step 3 — Pick a structure

**Story / emotional short** (e.g. *Santiago*) — a simple arc:

1. Setup.
2. Confrontation of the wound.
3. The shift.
4. Resolution that recontextualises the failure (*Santiago* meets a young fan after the session).

**Ad / explainer / brand short** — the four-beat structure:

| Beat | Job | Length |
|---|---|---|
| **Hook** | One strong visual that shows what it's about. No setup, no logos. | 1 shot |
| **Problem** | Concrete tension — a person, a situation, an obstacle. | 1–2 scenes |
| **Solution** | The product / idea / character resolves the tension *on screen*. | 2–3 scenes |
| **CTA** | One clear action, spoken or shown as text. | 1 shot |

- **Output:** a chosen skeleton with a scene count per beat.

### Step 4 — Expand the premise into a four-input brief

Decide these *before* prompting the model. *Santiago*'s values shown:

- **Character background** — 25 years old; has played football 18 years; lifelong championship dream.
- **Central conflict** — missed the decisive goal in the biggest match.
- **Character arc** — self-blame / identity collapse → acceptance.
- **Resolution** — meets a young fan after the session who still idolizes him.
- **Output:** a four-line brief (background · conflict · arc · resolution).

### Step 5 — Prompt the model to write the script, with the generation limits baked in

Higgsfield's literal instruction was: *"Write a 2-minute script with every shot 15 seconds max."*

**Why 15 seconds:** that is one Seedance generation. Writing in 15-second units means one shot = one render, with no re-cutting later. A ~2-minute film lands at **15–25 shots**.

Reusable prompt (reconstructed from the method):

```
Help me write a script for a short film.

PREMISE: [1-2 sentence premise with the wound]
EMOTIONAL CORE: [the one feeling + the one idea underneath]
CHARACTER BACKGROUND: [age, history, what they want]
CENTRAL CONFLICT: [the specific failure / obstacle]
ARC: [start state -> end state]
RESOLUTION: [the final turn]

FORMAT RULES:
- Total runtime ~2 minutes (state your real target).
- Every shot 15 seconds maximum - one shot = one generation.
- Number every shot: [SHOT 1], [SHOT 2]...
- Per shot: shot type (wide / medium / close-up / handheld / broadcast),
  character position + eyeline, numbered action beats (beat 1, beat 2),
  camera movement, lighting / mood.
- Short visual action lines. Show behaviour, not interior feeling.
- One idea per scene.
- Keep the same characters, locations and props throughout - list them at the top.
- Respect the 180 degree rule so eyelines match across cuts.
```

### Step 6 — Apply the formatting rules to the draft

- **Scene headers:** location + time of day.
- **Action lines:** short, visual, external.
- **One idea per scene** — split anything bigger into two scenes.
- **Dialogue pacing:** ~60–80 spoken words per 30 seconds as a starting guess, then read aloud and time it (pauses change the real length). Cross-check against the pipeline's Stage 7 rate of ~2.5 words/sec (~12 words per 5s clip).
- **Show, don't tell:** "she stops mid-step and looks back at the door", not "she feels conflicted." The camera can only film behaviour.
- **Output:** a clean, camera-ready draft.

### Step 7 — Segment into scenes

Cut a new scene at **one of exactly four** boundaries — nothing else counts:

1. A location change.
2. A time jump.
3. A new character entrance.
4. An emotional turn.

- **Output:** an ordered scene list.

### Step 8 — Break each scene into shots

- **One scene → 2–4 shots** (rule of thumb). In storyboard terms, 4–8 frames — a plain dialogue scene needs 4, an action beat needs the full 8.
- Each shot row carries: **scene # · shot # · shot size · camera movement · character(s) present · specific action.** Optionally a lens and numbered sub-beats (① ② ③) for timing inside the 15 seconds.
- **Generation order ≠ script order.** Generate the strongest shots first — opening image, the reveal / emotional peak, the transformation moment, the final frame — approve those, then fill the connective tissue.
- **Output:** a shot list — the reference map for every stage after this one.

### Step 9 — Build the reference registry (the bridge into Stage 2)

The script's real job here is to name exactly which characters, locations, and props exist.

- List every character, location, prop.
- Note which appears in which shot.
- Note what each one *is* — enough that Stage 2 can source or generate a reference sheet for it. Character sheets: keep only the close-up face on the sheet to stop drift; props: split-screen multi-angle; seamless grey background reads better to the model than white or black.
- Give each a fixed handle: `@santiago`, `@office`, `@stadium`, `@map_prop`. These tags carry through every per-shot prompt so faces, props and rooms stay identical shot to shot.
- On *Hell Grind* (95 minutes, made in ~14 days) "character drift" was the number-one problem — solved with locked references plus fixed seeds.

### Step 10 — Write the consistency locks into the script itself

Put rules that are normally a director's job into the text, so they carry into the Stage 4 per-shot prompts as a "Positive Locks" block:

- **180° rule** — "@psychologist always screen-left, @santiago always screen-right."
- **Prop behaviour** — "the drawing on @map_prop stays identical in every frame."
- **Identity locks** — "100% matches the reference; identity locked."
- **No negative prompts — invert them.** Instead of "not crying," specify the positive state: "dry face, anxious eyes, lips tightly pursed." The model renders what you name.

---

## 2. Script output format

Deliver the script as its own copyable fenced code block in the chat reply, same convention as a finished prompt. Structure:

```
TITLE — [runtime target] — [aspect ratio, if locked]

EMOTIONAL CORE: [one feeling + one idea]

REGISTRY
  Characters: @handle — one-line description ...
  Locations:  @handle — one-line description ...
  Props:      @handle — one-line description ...

LOCKS (apply to every shot)
  - [180° / identity / prop-behaviour lines]

--- SCENE 1 — [LOCATION], [TIME] ---
[SHOT 1]  (0-Xs)  [shot size], [camera movement]
  Characters: @a (screen-left), @b (screen-right)
  beat 1: [visual action]
  beat 2: [visual action]
  Lighting/mood: [short phrase]

[SHOT 2] ...
```

Each `[SHOT n]` block is one Stage 4 per-shot prompt's worth of intent — it is deliberately shaped to map straight onto the pipeline's `[Camera movement], [subject action/motion], [environmental motion], [style/mood], [lighting/atmosphere]` template.

---

## 3. How it feeds downstream

| This stage produces | Goes to | As |
|---|---|---|
| Runtime target + aspect ratio | Stage 1 — Ground Rules | the aspect-ratio lock; runtime sets clip count |
| Emotional core | Stage 3.5 — Director's Brief | the `Dramatic intent` line, per shot |
| Character / location / prop registry | Stage 2 — Reference Library | the list of reference sheets to source or generate |
| `@handle` names | Stage 5 generation loop | the reference-attachment tags, role-scoped per shot |
| Shot list (size · move · action) | Stage 3.5 → Stage 4 | one Director's Brief + one per-shot prompt each |
| Per-shot beat timings | Stage 4 timing mode | picks Timecoded when a beat must land on a specific second |
| LOCKS block | Stage 4 positive-locks tail + Stage 1 forbidden list | restated positively per shot |
| Dialogue lines + word counts | Stage 7 — Audio | TTS script, timed at ~2.5 words/sec |
| Transition device (if multi-shot) | Stage 5 — Sequence Design | the one repeated boundary treatment; match-cut points |

**Note:** photography Look + Stance ([Photography-Styles-Library.md](Photography-Styles-Library.md)) is *not* decided here. It's locked at Stage 2 (SOUL branch) or asked at Stage 4. The script may *suggest* a register in its mood lines, but the two-axis style question still gets asked at the normal point — no silent default.

---

## 4. Sample — Higgsfield "Santiago" (shot-by-shot map of a two-scene sequence)

**Scene 1 — Therapy session**

| Shot | Time | Framing |
|---|---|---|
| 1 | 0–6s | high establishing, Dutch angle — both characters in frame |
| 2 | 6–10s | wide canted single on the psychologist, lower-left corner |
| 3 | 10–15s | wide canted single on Santiago, lower-right corner |

**Scene 2 — World Cup penalty**

| Shot | Time | Framing |
|---|---|---|
| 1 | 0–2s | high wide establishing — penalty geometry |
| 2 | 2–5s | close-up of Santiago's face, pinned far-left |
| 3 | 5–8s | low ground-level rack focus to the ball |
| 4 | 8–10.5s | sports-broadcast long lens (super-tele) |
| 5 | 10.5–12.5s | goalkeeper's face, tight close-up |
| 6 | 12.5–15s | frontal close-up, Santiago's run-up and exit |

Every shot is timed to the second and pinned to a screen position — that is what makes each one a single deterministic generation.

**The prompt architecture every Santiago shot follows** (this is the Stage 4 shape, shown here so the script author writes toward it):

1. **Style block** — references ("Emmanuel Lubezki × Roger Deakins"), 8K / 24fps / 180° shutter, pore-level skin, "no 3D render, no game engine."
2. **Context** — narrative beat + emotional intent.
3. **Shot breakdown** — `[SHOT 1]`, `[SHOT 2]`… with timings, subject placement, action beats, camera spec.
4. **Constraints** — identity locks, prop consistency, composition rules, the 180° line: *"exactly two people, both seated in their own chairs throughout"; "the 180° line holds (@psychologist always screen-left, @santiago always screen-right)."*
5. **Audio** — environmental SFX only, no music.

---

## 5. Sample — Higgsfield "case4k": plain description → finished prompt

What the human typed:

> "Eduardo searches his cabin, finds a treasure map, then a crewman bursts through the door with urgent news about an island sighting. He slaps the map down and rushes toward the exit into daylight."

What the Skill produced (verbatim, one shot = one generation):

```
SCENE CONTEXT  Bright day outside, darkness inside a cramped windowless ship cabin. Pirate
captain Eduardo works through stacks of papers on a chart desk, sliding sheet after sheet
aside, and uncovers an old treasure map - a red X on a small island, a dashed course line
running from a drawn ship to that island. The cabin door swings open behind him and a
crewman delivers one hoarse line - Eduardo slaps the map back onto the desk and immediately
heads for the door.

ACTIVE REFERENCES  @eduardo matches the character sheet exactly; @map_prop stays identical
across frames; @loc_cabin controls environment only; @eduardo_crew appears only in the doorway.

LOCATION MAP  Interior of @loc_cabin. The chart desk sits midground-center under the hanging
lantern - the only light source.

CUT 1 - MS, 47 deg:  Eduardo bent over desk working through papers in steady rhythm,
  muttering "You think you're gonna outsmart me?.. Nice try!"
CUT 2 - MCU, 29 deg:  His hands stop. Under loose papers a corner of aged parchment. He pulls
  @map_prop free and lifts it into lantern light, eyes locking onto it - a slow grin spreads.
CUT 3 - OVER-THE-SHOULDER MS, 29 deg:  From behind Eduardo's shoulder, the map held in his
  hands in lantern light. The red X reads clearly. A short 1.5-second hold.
CUT 4 - MS, 47 deg:  Door swings open, hard white daylight BLASTS in. @eduardo_crew stands
  silhouetted. Eduardo startles, slaps the map flat onto the desk, then strides toward the
  doorway into light.

LIGHTING  Handheld 3cm breath. Focus rides Eduardo's hands, then the map. Papers slide with
air resistance; every sheet keeps exact shape and identity.

POSITIVE LOCKS  The drawing on @map_prop stays identical in every frame. The lantern stays
lit. Only two people appear. Eduardo keeps the map in his hands until CUT 4, then slaps it
back onto the desk.
```

Template shape: **scene context → references → location map → shot-by-shot → lighting → positive locks.** "Sequence of cuts, no timecodes — cuts only at the specified points." Maps directly onto the pipeline's Stage 4 Cut-count timing mode + positive-locks tail.

---

## 6. Sample — Higgsfield "Seedance 4K" one-minute film: beat → shot prompt

Film structure (4 scenes): (1) character comes home, sits, turns on TV → (2) fantasy flight playing on the TV → (3) mom calls for dinner, he changes channel → (4) wildlife documentary of a snow leopard.

Plain-language beat handed to the model:

> "A girl flies joyfully on a mystical dragon-bird creature through an impossibly tall jungle, diving down a waterfall, skimming water, weaving past wildlife, threading narrow gaps, and climbing above the canopy for a final awe-inspiring reveal."

Opening of the generated prompt:

```
SCENE CONTEXT  @woman flies on @fantasy-dragon, a large flying creature, through a colossal
jungle of mile-high fantastical trees. Wordless throughout, she steers with her body and pure
joy - laughing and whooping as @fantasy-dragon pulls off daring tricks: a sheer near-vertical
plunge down an immensely tall 90 degree waterfall almost grazing the water, a low skim across
the pool, passing through a cloud of giant butterflies with a single breathtaking slow-motion
moment, gliding between branches and lianas past leaping monkeys, threading a razor-narrow
gap, then climbing straight up the trunks and bursting above the canopy into a vast reveal of
the whole world.
```

---

## 7. Samples — community & open-source

### 7a. Stylised scene, community prompt library (Seedance 2.0)

Same skeleton as the pro films — timed blocks inside 15 seconds, one idea per block, escalation to a hard cut — applied to a 2D anime look:

```
<<<image_1>>> is the character reference AND visual style reference - a young man drawn in a
bold anime/illustration style: clean flat cel-shading, thick confident outlines, watch on his
left hand <<<image_2>>> ... Maintain consistent 2D anime illustration style throughout all frames.

Opening frame (0-4s): The young man jolts awake in his bedroom - he overslept. Warm golden
  light floods his room... His <<<image_2>>> watch buzzes - a holographic notification: a
  dating app, "Anna", "I'll be at the cafe in 10 minutes." ... Handheld shaky pan, fast cuts.
Rushed preparation (4-10s): Fast anime montage - water splash on face, grabs his suit jacket
  and throws it on mid-run... Classic anime speed lines. Dutch angle frames.
Map selection + discovery (10-14s): Watch activates - holographic city map... a third option
  flickers into existence: [ULTRAFAST - NEW]. He freezes... a slow smirk... He taps it.
Teleportation (14-15s): The watch DETONATES... His body vaporizes into flat geometric shards
  of light in a single frame... Smash cut to white.

Style: bold 2D anime illustration, cel-shaded flat coloring, thick confident outlines, warm
amber and muted earth tones with cool electric blue holographic accents, 2.35:1, 24fps.
```

### 7b. Character-anchor block + B/W manga scene (community)

The community's version of the reference registry — a reusable `@char` block pasted at the top of every shot:

```
@char: Young male protagonist, late teens, lean build. Curly dark hair, soft sharp eyes.
Black suit jacket, dark dress shirt, black tie, slim black trousers. Left wrist: geometric
watch - faceted bezel, wood grain geometric dial, segmented bracelet. Expressive manga face -
wide eyes for shock, furrowed brow for focus, sweat drops on fear, gritted teeth on effort.

2D manga animation. 16:9. 15s. Black and white only - zero color. Flat 2D hand-drawn ink.
Hard ink outlines, halftone dots in midtones, scanline grain every frame. Handheld, dynamic cuts.

Ultra-wide downshot - @char falls from a white void into a Japanese courtyard. Lands hard -
squash on impact, jacket billows. Two samurai leap from both sides... [escalation: 4 samurai
-> bamboo forest -> he jabs the watch dial] ECU - finger flat on the dial... The watch
explodes white... Full whiteout. @char gone. Last frame: empty stalk swaying hard.
```

Same three moves as the pro films: **lock the character in a header, lock the render style in a block, write the action as timed escalation ending on a hard cut.**

### 7c. "Zephyr" K-pop AI series (community) — character-first build

Three-stage character build before any footage: (1) face generation — lock bone structure & features; (2) outfit design — every detail specified separately; (3) character sheet — merge face + outfit into the master asset. World elements (city, creatures, mechs) built next. Music + lyrics uploaded into Seedance before any frames.

"Haru Min" face-sheet prompt, verbatim:

```
Young Asian female (age 20), slim, very attractive K-pop idol level beauty, flawless skin,
soft symmetrical features, expressive eyes. Short/mid-length slightly messy stylish hair.
Outfit: futuristic mechanic techwear - shorts, layered fabrics, straps, small details,
slightly worn with stickers/doodles. White studio background, soft cinematic lighting,
realistic, high-end fashion style.
```

Direction principle: describe **camera behaviour and physics**, not just what appears — "the mech's drilling arm swiftly thrusts forward…" rather than "mech punches monster."

### 7d. Open-source corpus to mine

- **Hell Grind** — 95-minute feature, fully open-sourced: ~115,446 generation records across 108 scene folders; each record shows the full prompt, model, parameters, asset link. A shared ~12-line "technical foundation" block every shot inherits; per-scene GEO SPATIAL LAYOUT block; "position-fixing first second"; a ban dictionary; a 10–15 iteration rule. Mirror repo: `github.com/XucroYuri/higgsfield-hell-grind-opensource` — prompts under `folders/<scene>/prompts/`.
- **Community Claude Skill** — `github.com/OSideMedia/higgsfield-ai-prompt-skill`: 32 sub-skills (Seedance 2.0/2.5, Hell Grind pipeline, Soul ID consistency, Kling 3.0); DISCIPLINE framework (9 patterns, 3 tiers: prompt-construction, model-selection, iteration-discipline); 18 templates (10 genre, 5 Seedance technique, 3 text-overlay).

---

## 8. Guardrails

- **Prompt text only.** No generator calls, no claiming a video/image/audio was made. Same as every other stage.
- **Don't lock the palette or aspect ratio here** beyond noting the user's stated target — the numeric locks are Stage 1's job. Carry the aspect-ratio *intent* forward; let Stage 1 formalise it as hex + ratio.
- **Don't pick the photography Look/Stance here.** Suggest a register in mood lines if the brief implies one, but the two-axis question is still asked at Stage 2/4.
- **One idea per shot, ≤15 seconds.** If a shot's action can't be said in one or two beats, it's two shots.
- **The registry is the deliverable.** A script with vivid scenes but no clean character/location/prop list has not finished this stage — Stage 2 can't start without it.
- **Budget awareness.** Each `[SHOT n]` block becomes a Stage 4 prompt that must fit the 1500-char positive+negative cap. Keep beats terse; the style block and locks are added downstream and cost characters too.
