# Cully Hill Boys — Benchmark

The reference production this workspace measures itself against. Five parts:
**what they did** (numbers), **what their prompts actually look like** (measured),
**the skill behind them**, **what we can adopt**, and **what won't transfer or contradicts
our docs**.

Compiled 2026-09-22 (revised the same day after reading the production data directly).

## How this was measured

- **The production data is public.** The project page loads the published snapshot folder
  from Higgsfield's API without a login. It holds **473,039 generation records** in 1,052
  folders, each with the full prompt, model, duration, aspect, resolution and named
  reference elements.
- **Sample:** one page (up to 20 jobs) from **every** folder, so **19,453 jobs (4.1 %)**
  with 17,130 video prompts and 2,299 image prompts, spread across all 137 scenes and pre-production.
  Percentages below are shares of that sample. Folder counts are exact, not sampled.
- **Not read:** the written **brief** and the **CINEDANCE skill** file. Both need a
  signed-in account. The brief sits behind an authenticated endpoint and was not accessed.
- Eight full prompts are archived for study in
  [Sources/cully-hill-boys-prompt-samples.md](Sources/cully-hill-boys-prompt-samples.md).

Tags: **[MEASURED]** from the production data · **[PRESS]** third-party reporting of
Higgsfield's brief · **[OFFICIAL]** Higgsfield's own posts · **[HG]** Higgsfield Studio's
*Hell Grind* brief, as re-derived in a community skill repo (see §3) · **[DERIVED]** our
arithmetic.

---

## 1. The numbers

| Metric | Value | Tag |
|---|---|---|
| Runtime | 1 h 54 m 49 s (6,889 s); marketed "110 minutes" | MEASURED |
| Delivery | 4096 × 1716 master, 2.39:1; generated at **21:9** | MEASURED |
| Budget | $2 M: ~$1 M compute, ~$1 M people, licensing, script, finishing | PRESS |
| Schedule / crew | ~4 weeks · 25–28 people, 9 directors · 40 % new to AI | PRESS |
| Script | Tim Planagan, human-written (Black List) | PRESS |
| **Generations** | **473,039** in the project (34,388 pre-production = 7 %) | MEASURED |
| Structure | 4 act folders + PRE PROD + Regenerations; scenes numbered 1–137 (the "137-entry log" is most likely the 137 scenes) | MEASURED |
| **Video model** | **Seedance 2.0 on 99.9 % of video jobs.** Seedance 2.5 on 20 sampled jobs, all in the late Regenerations folder | MEASURED |
| Clip length | **15 s on 64 %** (the 2.0 ceiling); rest spread 4–14 s | MEASURED |
| Resolution | 1080p 80 % · 4K 20 % | MEASURED |
| Audio | generated in-pass on 98 % | MEASURED |
| Generation mode | Text + named reference elements. Start frame on **0.2 %**, video input on 4.1 % (continuations, music carriers) | MEASURED |
| Image / asset models | Seedream 4.5 (42 %), Nano Banana 2 (34 %), Soul Cinematic, GPT Image 2, Seedream 5 Pro, Gemini, Recraft | MEASURED |

### Derived rates — the numbers to beat  [DERIVED]

| Rate | Value |
|---|---|
| Generations per finished second | 473,039 ÷ 6,889 ≈ **69** (≈ 4,100 per finished minute) |
| Generations per scene folder | median **~3,000**, max ~34,700 |
| Compute per finished minute | $1 M ÷ 115 ≈ **$8,700** |
| All-in cost per finished minute | ≈ **$17,400** |
| Finished minutes per person-week | ≈ **1.0** |
| Distinct reference elements | **1,000+** in the sample alone (≈ 1,000 assets reported) |

For comparison, *Hell Grind* (same studio, 90 min, 14 days, 15 people) reported **108,859
generations**, **~1.0 % image / ~1.5 % video acceptance**, ~800 generations to lock one lead
character, and 72 generations for a single 10 s establishing shot. [HG] CHB burned ~4× the
generations for a comparable runtime.

---

## 2. What their prompts actually look like  [MEASURED]

### 2.1 Shape

- **Length:** English video prompts run a median **1,750 words** (p10 917 · p90 3,177 · max 8,909).
  Our BAN 2 is right: there is no cap.
- **Language:** 94 % English, **6 % Chinese** (Seedance 2.0's native language). 17 % of image
  edit prompts are **Russian**, the crew's working language.
- **References:** median **5** elements per shot, maximum **9**: characters, environments and props.
  Elements are injected as `<<<uuid>>>` tokens. Each gets a one-line role description ending
  in **"100% matches the reference"** (83 %).
- **Video prompts are hand-authored:** the prompt enhancer was never on for video. It was on for only some image jobs.

### 2.2 Block order as shipped

| Block | Present | Typical position |
|---|---|---|
| `STYLE PREFIX` (a named "world") | 18 % | very top, before everything |
| `SCENE CONTEXT` | 82 % | top |
| `ACTIVE REFERENCES` | 80 % | 2nd |
| `LOCATION MAP` (or GEO / GEOMETRY) | 54–59 % | 3rd |
| `FIRST FRAME AND SPATIAL BLOCKING` | 64 % | 4th |
| `OPTICS` → `FORMAT MODE` → `CAMERA` | 78 / 65 / 84 % | middle |
| `ACTION TIMING` (timecoded beats) | 70 % | middle |
| `CHARACTER ACTING` | 19 % | after action |
| `PHYSICS` · `LIGHTING` | 82 · 86 % | late middle |
| `AUDIO` (with `VOICE` lock) | 86 % | late |
| `STYLE` | 80 % | late |
| **`QUALITY`** | **76 %** | second-to-last |
| `POSITIVE CONSTRAINTS` / `POSITIVE LOCKS` | 48 / 18 % | last |

This is **our 17-block order almost exactly**. The differences: they add a **QUALITY** block
("ARRI Alexa, vintage spherical primes, subtle anamorphic. Sharp clarity, stable picture,
readable face…"), they timecode the action, and they almost never use `COLOR GRADE`,
`WARDROBE` or `OUTPUT SETTINGS` (≤ 1 %).

### 2.3 Conventions and how often they appear

| Convention | Share | Note |
|---|---|---|
| **ARRI / Alexa named** | **72 %** | in QUALITY / STYLE |
| **Director or DP named** | **45 %** | Guy Ritchie, Deakins, Edgar Wright, Scorsese, Lubezki, Gerwig, Balabanov, Larkin Seiple |
| Focal length in **mm** | 50 % | paired with degrees: "18° diagonal field of view (100 mm)" |
| FOV in **degrees** | 72 % | table steps (84°, 47°, 18°, 8°) plus off-table values (40°) |
| Anamorphic · film grain | 65 · 74 % | |
| 60:30:10 colour ratio | 66 % | dominant / secondary / accent, named |
| HARD CUT · timecoded beats | 60 · 56 % | `[2.0–4.0s | 47° head-on to door]` |
| Scene number in the prompt | **31 %** | "Scene 83. EXT. …" |
| "Verbatim / locked across all shots" | 45 % | location map and style prefix pasted unchanged across a scene |
| Explicit age | 30 % | "A 25-year-old English man" in voice specs |
| Height in cm | 34 % | "185 cm … 175 cm" to stop height equalising |
| Accent named | 86 % | "Multicultural London English", "Caribbean-London" |
| `VOICE` / `VOICE LOCK` spec | 23 % | register, pitch range, accent, delivery for this line |
| No music / no score | **81 %** | |
| No subtitles | 57 % | |
| Dialogue lock "only the scripted lines / no ad-libs / nothing else" | 15 % | |
| **Explicit "exactly N words" lock** | **0.5 %** | the thread's "Pull it, Oli" example is not house practice |
| Blinks directed | 52 % | |
| screen-LEFT / screen-RIGHT in caps · 180° rule | 40 · 47 % | |
| British spelling instruction | 72 % | |
| Anti-slop / hand-anatomy lines | 18 · 25 % | |
| Kelvin · km/h | 4 · 5 % | our "measured language" rules are barely used |
| Continuation from previous clip | 14 % | "承接上一镜" / "same as the end of the previous shot" |

### 2.4 Style = per-storyline "worlds"

Instead of one film look, each storyline has a **named world**, compiled once and pasted
verbatim at the top of its prompts:

- `WORLD OF THE BOYS` — "cold and submerged … booklight wrap at the hard cold end … true negative fill"
- `WORLD OF ALISON & MAYA` — "soft daylight" (Deakins × Gerwig)
- `WORLD OF DMITRY` — Balabanov × Scorsese
- `WORLD OF THE GANGSTERS` — "old-money register"
- `WORLD OF CAL & MAYA · ARRIVED` — "settled warm", scene 137 finale

Each world carries variants (NIGHT, SETTLE-on-dialogue, per-location). The look changes when the story changes, never shot by shot.

### 2.5 Music, in practice

A pre-recorded track goes in as a **black-screen video carrier** whose audio is the master:
"The source audio is used whole and untouched … Nothing is re-sung, regenerated, remixed,
extended or replaced." Lyrics are written **phonetically** ("wit' dem", "no-ting"). Flow is
measured ("~3.5 words per second, densest ~5.0 at 6.4 s"). Gestures are anchored to quoted
words, cuts land on phrase borders, and **"the mouth never invents"**: every mouth movement matches
a sounding syllable. Scene 15's performance was built in `block_1 / block_2 / block_3`
folders with audio inputs, consistent with the 12 s breath-split blocks. See sample B.

### 2.6 Asset stage

- **Sheets on grey, specified as hex `#808080`**, laid out as turnarounds (three panels for people, 2×2 for props).
- **States are separate named elements**, never overwrites: `Kel_s84_v2_wet`, `Dmitri_v5+wound`,
  `Dmitri_v1_nogloves`, `Roger_v3_3_noleafs`, `Oli_MV`, `…_FILMLOOK`, `Alison_v2_desloped`.
  Kel alone has 26 variants in the sample.
- **Naming:** `char_CB_<Name>_s<scene>_v<n>`, `loc_CB_…`, `prop_CB_…` (CB = project code).
- **Point edits with an identity lock:** Nano Banana 2 — "Same man, same face, same
  expression, same pose… Change only the hair colour." Nano Banana Flash — "pixel-for-pixel
  identical … The ONLY modification: add a deep dent."
- **New angles of an approved location** come from an image edit of the plate ("re-create
  the same scene as a WIDER, HIGHER-ANGLE establishing shot. Keep all the SAME objects in the SAME relative positions").
- **Prompt versioning by folder:** scenes hold `prg_v1 … prg_vN` folders (prompt versions),
  plus `Assets`, `test`, `team_2`, `Regen`.

---

## 3. The skill: CINEDANCE

- **The file itself is gated.** It sits in the project page sidebar for signed-in users
  ("grab the CINEDANCE skill and open the canvas" [OFFICIAL]). It is not in Higgsfield's public
  [skills repo](https://github.com/higgsfield-ai/skills).
- **What the output tells us:** CINEDANCE writes the block scaffold in §2.2. That scaffold is
  **the same doctrine as our archived `seedance-clean` skill**, plus QUALITY, ACTION
  TIMING, CHARACTER ACTING, VOICE LOCK and the world STYLE PREFIX. Our
  [Seedance-Prompt-Architecture.md](Seedance-Prompt-Architecture.md) is therefore close to
  the real thing. It is not a different system.
- **Best secondary source:** the MIT-licensed community repo
  [OSideMedia/higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill)
  re-derived CINEDANCE and the *Hell Grind* brief (`skills/higgsfield-seedance/HELL-GRIND.md`).
  It records that the CHB and "Zephyr/cinedance" folders are the same CINEDANCE material. CHB's
  five published rules match Hell Grind's five rules word for word, so it is one studio method.
  Techniques from it that we don't have [HG]:
  - **Headless front panel** on character sheets. The model otherwise takes the face from the tiny full-body figure.
  - **An image never goes through a model twice in full.** Point edits are composited back with masks, so the base stays the same pixels.
  - **GEO SPATIAL LAYOUT:** a per-scene floor plan with no people, pasted unchanged into every shot of that scene.
  - **The first second is a wide** that fixes positions, with no action. The "hm" trick makes Seedance treat it as its own shot.
  - **Character-count header:** `EXACT 3 CHARACTERS — NO DUPLICATES: …`, plus counted props.
  - **CHARACTER ACTING fields:** state · want · hiding · body rhythm · habits · what changes.
  - **Dialogue built in a fixed order:** voice + emotion → line → physical action → facial reaction. Lines live only in AUDIO.
  - **A ban dictionary** of words the model punishes ("dark" → "low key").
  - **Two routes to reverse angles:** a generated corner, or a slow walk-through video of the empty location, screenshotted.
  - **Crowd = one asset** with a stated head count; **threshold transitions** with a light contrast; **scale law** that names what a failed shot looks like.

---

## 4. What we can adopt

Ranked by expected reduction in rerolls. The ✅ items are confirmed in the production data.

1. ✅ **State elements, named by state.** One element per condition (`_wet`, `+wound`,
   `_nogloves`, `_MV`), never an overwrite. Registry gets a state column. Phase 3 tags the state handle. → Phase 1 / 2
2. ✅ **Per-storyline "worlds."** Compile a locked style block per storyline and time register
   and paste it verbatim. This fixes whole-film consistency better than distributing style per shot. → Phase 0 / 3
3. ✅ **QUALITY block** as block 16: capture texture, clarity, stability, anti-slop, era lock
   ("no modern tech beyond 2011"), spelling. → Phase 4
4. ✅ **Timecoded ACTION TIMING** with lens per beat, `[2.0–4.0s | 47° head-on]`, plus
   HARD CUT markers. → Phase 4
5. ✅ **Heights in cm and accent named** in every multi-character prompt. **VOICE LOCK** per
   character: register, pitch range, accent, and the delivery adjustment for this line. → Phase 1 registry / Phase 7
6. ✅ **Dialogue lock by exclusivity, not count:** "only the scripted lines, one at a time; no
   ad-libs, no other voices, no subtitles, no music." Keep the word count as a secondary check. → Phase 7
7. ✅ **Role-scoped environment references:** "controls geometry, materials, layout,
   landmark placement, cold light only; do not reuse its camera angle." → Phase 4
8. ✅ **Music as a carrier video** with lyrics written phonetically, a measured words-per-second
   flow, gestures anchored to quoted words, and "the mouth never invents." → Phase 7C
9. ✅ **Grey as a hex value (`#808080`)** and turnaround layouts; **identity-locked point edits**
   ("Same man … change only …"); **location re-angles** by editing the approved plate. → Phase 2 / 6
10. ✅ **Prompt versioning:** `prg_v1…vN` per scene, never overwrite a prompt. Pairs with
    change-one-variable. → Phase 5 / folder template
11. **[HG] GEO layout per scene, first-second wide, character-count header, headless front
    panel, never-two-full-passes** (§3). → Phase 2 / 4
12. **[PRESS] 10–15 attempt ceiling → restructure the shot**; phone stunt footage as a
    motion reference; likeness consent protocol (compensation, scope, script approval,
    deletion within 30 days). → Phase 5 / 0

---

## 5. What won't transfer, or contradicts our docs

### 5.1 Our docs got the model wrong  ⚠️
Our pipeline and architecture file describe CHB as a **Seedance 2.5** production (30 s
clips, 50 references, 2.5 envelope). The data shows **Seedance 2.0 on 99.9 %** of video: 15 s
clips, at most 9 elements per shot. The 2.5 claim came from marketing copy. Our 2.5 capability
section still stands as 2.5 facts, but **CHB proves nothing about 2.5's envelope**, and "what
CHB establishes" in Architecture §0 needs correcting.

### 5.2 BAN 1 is stricter than the benchmark
They name ARRI Alexa in 72 % of prompts, directors or DPs in 45 %, and mm in 50 %, and it worked
across 115 minutes. Their own skill says names "get ignored or break complex moves"; their
production does it anyway. **Our BAN 1 is a house choice, not a replication of what they
did.** It's still defensible, because it makes prompts auditable and lighter on
reroll-sensitive tokens. But the justification "Higgsfield's pipeline avoids names" is false. Reword it.

### 5.3 The "exactly N words" lock is overstated
Our pipeline makes the word count a required Phase 1 and Phase 7 lock on every line. It
appears in **0.5 %** of their prompts. Their real mechanism is exclusivity ("only the scripted
lines, no ad-libs") plus a voice lock plus "no music." Keep the count as a check, and add the exclusivity line as the main lock.

### 5.4 Style prefix and scene numbers
- 15–18 % of their prompts **open with a STYLE PREFIX** (30 % carry one). Our Phase 4 forbids any style prefix.
  The community corpus explains the split: standalone prompts distribute style, while connected
  shot lists paste a verbatim prefix. **A feature is a connected shot list**, so we should allow the world prefix.
- 31 % carry a **scene number** and "verbatim across all Scene 83 shots." Our sealed-document
  rule bans scene numbers. The number is harmless context; what the model must not get is
  *memory* ("as above"). Relax the rule to ban memory references, not labels.

### 5.5 Our automation still can't run this
`neutradc.py video` sends a start frame and an end frame. CHB used start frames on 0.2 % of
jobs and **named reference elements on nearly all**. It also routes through ElevenLabs Flows,
where ByteDance models are gated. Until the script can send 3–9 role-scoped element images,
plus an audio or video carrier, it runs our I2V pipeline, not this method.

### 5.6 Frame-chaining is a minority tool
Continuation from the previous clip shows up in 14 % of prompts and video input in 4.1 %. So it
exists, but as an exception. Our Phase 8 default ("last frame → next shot's reference") should
become the named exception, as they use it.

### 5.7 Study-only material
Their character sheets are licensed real-person likenesses (`HOL-RO`, and the API reports
`is_open_source: false`). **Eyes-only** under our licence tiering. The archived prompts in
`Sources/` are for study and must not be pasted into a production prompt.

### 5.8 Scale
473k generations and $1 M of compute are a different regime. Take their *ratios* (69
generations per finished second, 50:50 compute to people), not their absolute budget.

---

## 6. Corrections owed to our own docs

| File | Says | Should say |
|---|---|---|
| [Seedance-Prompt-Architecture.md](Seedance-Prompt-Architecture.md) §0 | Stack: Seedance 2.5 | Seedance 2.0 on 99.9 % of video; 2.5 only in late regenerations |
| [Seedance-Feature-Pipeline.md](Seedance-Feature-Pipeline.md) intro / Phase 0 | "half of the $2 M was rerolls" | half was compute (kept takes included); 69 generations per finished second |
| Feature-Pipeline BAN 1 rationale | names "get ignored or break complex moves" | their production names cameras and directors constantly; BAN 1 is our house choice |
| Feature-Pipeline Phase 1 / 7 | word count required on every line | exclusivity lock first; word count as a check |
| Feature-Pipeline Phase 4 rule 2 | no style prefix, ever | allow a verbatim per-world prefix in connected sequences |
| Feature-Pipeline Phase 4 rule 1 / CLAUDE.md | no scene numbers | no memory references; labels allowed |
| Feature-Pipeline Phase 8 | last-frame chaining as the match-cut step | named exception, used in ~14 % of their prompts |
| Architecture §9 | "top style line" vs Phase 4 "no prefix" | resolved by the world-prefix rule above |

---

## 7. Sources

- Production data: `fnf-api-gw.higgsfield.ai/fnf/project-publications/higgsfield.studio/cully-hill-boys` and the snapshot folder's `children` / `items/v2` endpoints, read 2026-09-22. Samples: [Sources/cully-hill-boys-prompt-samples.md](Sources/cully-hill-boys-prompt-samples.md)
- [Project page](https://higgsfield.ai/@higgsfield.studio/projects/cully-hill-boys) · [Full film](https://higgsfield.ai/original-series/cully-hill-boys/full-film)
- [Release thread](https://x.com/higgsfield_ai/status/2086868392510963820) · [CINEDANCE post](https://x.com/higgsfield_ai/status/2086868401788731762)
- [AlphaSignal](https://alphasignal.ai/news/higgsfield-made-a-2m-ai-film-with-licensed-celebrity-likenesses) — crew, budget split, state variants, 10–15 rule, voice spec, licensing terms, five rules
- [KuCoin](https://www.kucoin.com/news/flash/higgsfield-produces-110-minute-ai-movie-for-2m-open-sources-entire-production) · [UA.News](https://ua.news/en/technologies/higgsfield-opriliudnila-shi-film-cully-hill-boys-i-prompti-do-nogo) · [AI Directory](https://aidirectory.com/news/higgsfield-posts-ai-movie-cully-hill-boys-and-prompts) · [Screenweaver](https://www.screenweaver.ai/blog/cully-hill-boys-punky-duck-critterz-ai-films)
- [OSideMedia/higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill) (MIT) — `skills/higgsfield-seedance/HELL-GRIND.md`, `SKILL.md` § Official Prompt Architecture, `production-benchmarks.md`, `CHANGELOG.md` v3.33–v3.35
- [higgsfield-ai/skills](https://github.com/higgsfield-ai/skills) — official skills repo (no CINEDANCE)
- [Seedance 2.5 prompting guide](https://higgsfield.ai/blog/seedance-2-5-prompting-guide)
- Variety and Forbes were paywalled and not read.
