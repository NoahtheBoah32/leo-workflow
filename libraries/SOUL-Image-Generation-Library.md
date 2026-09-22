# SOUL — Image Generation Library

Upstream companion to [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md). The pipeline starts at a reference still; this library covers **how to generate that still in SOUL** when no usable photo exists (Stage 2's "has to be generated instead of sourced" branch). SOUL output then enters the pipeline normally — Stage 3 motion analysis, Stage 3.5 director's pass, Stage 4 signature card — like any other reference image.

SOUL is a hyper-realistic, fashion/editorial-grade AI photo model (text-to-image and image-reference). It deliberately produces *candid, imperfect, "shot on a real camera"* frames rather than clean renders — which is the same fight [Camera-Look-Library.md](Camera-Look-Library.md) picks downstream, so a SOUL reference tends to carry grain/texture into Seedance better than a clean render does.

**Division of labor (unchanged):** Claude's output here is **prompt text only** — the SOUL prompt string, preset choice, aspect ratio, and resolution. The user runs the actual generation in SOUL, QCs the result against the gate below, and brings the chosen still back into Stage 3.

Source: compiled from the SOUL product docs (higgsfield.ai/soul-intro, docs.higgsfield.ai), the SDK repo, and third-party provider pages (eachlabs, Segmind), Sept 2026. The vendor does not publish the base model; parameter names below are from the public API surface and may drift.

---

## 1. Where SOUL sits in the pipeline

```
Stage 1 (ground rules: aspect ratio, palette hex, forbidden list)
   → Stage 2: no usable photo?  → ASK: which Look + which Stance?  (Photography-Styles-Library.md §1)
                                    → SOUL (this doc): prompt + preset + Look term + Stance term (§3 / Styles §9) + ratio + resolution
                                    → QC gate (§7) → reference still
   → Stage 3 motion analysis → Stage 3.5 director's pass → Stage 4 signature card (same Look + Stance) → Seedance/Kling
```

- Run SOUL **after Stage 1 is locked** — aspect ratio and any palette/subject-matter constraints are inputs to the SOUL prompt, not afterthoughts.
- **Ask the user for both photography-style axes this scene uses — every time, before writing the prompt.** The **Look** (§2–§7) and the **Stance** (§8: genuine candid / directed candid / posed). See [Photography-Styles-Library.md](Photography-Styles-Library.md) §1 for the exact question and §9 for how the two answers map to a SOUL preset + one Look term + one Stance term. Never pick silently; if the brief implies either, still name and confirm. "Documentary" is ambiguous — disambiguate per §0 before locking. Record both in the generation log and carry them unchanged into the Stage 4 signature card.
- Generate the still, pass the QC gate, then **write the motion map** (`reference - subject/[name]-motion-map.md`) against the SOUL frame exactly as you would against a sourced photo.
- One SOUL frame per named element still applies — if a shot needs a specific building/material/landscape, either photograph it or generate it deliberately here; don't fake a reference.

---

## 2. Prompt structure — short, subject-first

SOUL is the opposite of the Seedance/Kling 1500-character discipline. It is tuned for **plain, compact prompts** and does its own prompt expansion. Long stacked camera/lens/film-stock paragraphs fight it.

**Template:**

```
[subject: age / build / defining features], [wardrobe / styling], [setting],
[optional: one camera or light note], [optional: aesthetic/subculture term]
--ar [ratio from Stage 1]
```

- **Subject first, wardrobe second, environment third.** Then stop. Add a camera/light note only if it's load-bearing for the shot.
- **Lean on a preset for the "camera look"** (§3) instead of describing it. Pick `2000s Cam` rather than writing "shot on a point-and-shoot, direct flash, slight overexposure, 2000s color."
- **Use subculture / fashion vocabulary directly** — SOUL renders these as real aesthetics, not costume: `gorpcore`, `quiet luxury`, `Y2K`, `coquette`, `blokecore`, `mob wife`, `Amalfi summer`, `0.5 selfie`. One term does more work than a sentence of description.
- **The locked Look + Stance fill the `[aesthetic term]` slot** — from [Photography-Styles-Library.md](Photography-Styles-Library.md) §9, append *only* the one short Look term (§9a, e.g. `direct on-camera flash, hard wall shadow`) plus the one short Stance term (§9b, e.g. `candid interaction, not looking at camera`), on top of the preset. Skip the Stance term if there are no people in frame. Do **not** paste the full Stage-3 phrase stacks here — that muddies SOUL the same way stacking camera/film/lens language does (§8).
- **Don't prompt for "clean studio perfection."** SOUL injects dust, flash blow-out, grain, and motion blur on purpose. Asking for pristine output fights the model; if you genuinely need clean, say `soft even studio light, minimal grain` and expect it to only partly comply.
- **`enhance_prompt` rewrites your text.** If you need the frame reproducible (re-running with a fixed seed), turn prompt enhancement off; otherwise leave it on for richer results and accept variance.

**No negative-prompt field.** SOUL exposes no negative prompt and no CFG/steps control. Fold avoidances into the positive prompt as plain statements (`no visible logos or text`, `bare walls`) and enforce the rest at the QC gate.

---

## 3. Preset selection ("Visual Styles")

A preset is a named style layer (`style_id` + `style_strength` 0–1, default 1). It encodes the camera/film/lighting character so the prompt doesn't have to. Set `style_strength` ~0.5 for a hint, ~1.0 for full commitment. Catalog size is quoted inconsistently by the vendor (20 → 50 → 80 → 100+); treat the list as live and browse it in-app.

**Drive the preset choice from the locked Look** — [Photography-Styles-Library.md](Photography-Styles-Library.md) §9a maps each Look (film-stock, cinematic register, auteur, documentary look, etc.) to its closest SOUL preset plus the one Look term to append; §9b adds the one Stance term. Use those tables first; the generic list below is the fallback when the Look doesn't map cleanly. Common presets useful for this pipeline:

| Preset | Gives you | Reach for it when |
|---|---|---|
| `General` / `Realistic` | Neutral photoreal base, minimal stylization | The shot needs to read straight; you'll do the look in Stage 4 |
| `iPhone` / `Old smartphone` | Casual phone-camera capture, mild HDR, handheld feel | UGC, candid, "someone just took this" |
| `2000s Cam` / `Digital Camera` | Point-and-shoot, direct flash, era color | Nostalgic / consumer / editorial-casual |
| `Subtle flash` | On-camera flash falloff, slight blow-out | Night, indoor, party, fashion-candid |
| `Nature light` / `Warm ambient` | Soft daylight, warm practical interiors | Calm, premium, lifestyle |
| `Theatrical light` | Hard directional key, deep shadow | Dramatic portrait, high-contrast beat |
| `Editorial street style` | Magazine street-fashion framing | Wardrobe-forward, styled subject in environment |
| `Fisheye` | Wide distortion | Only when the distortion is the point |

Keep the preset choice consistent across frames meant to cut together — same discipline as holding one camera body across a treatment in [Camera-Look-Library.md](Camera-Look-Library.md).

---

## 4. Aspect ratio & resolution — match Stage 1

- **Aspect ratio:** set it to the Stage 1 lock. SOUL supports `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `5:4`, `4:5`, `16:9`, `9:16`, `21:9`. Your usual `16:9` / `9:16` / `1:1` are all native — no cropping needed.
- **Resolution:** generate at the **highest tier available** — `2K` (or `4K`) on the standard text-to-image path, `1080p` on the SOUL ID / reference paths. All clear the pipeline's Stage 2 minimum (1080×1080 / 1280×720 / 720×1280) with margin. Never bring a 720p frame into Stage 3 if 1080p+ is available — both video models animate off edge detail.
- **Batch:** SOUL returns up to 4 per run. Generate the batch, pick the one frame that passes §7, discard the rest.
- **Save immediately.** API-hosted outputs expire after ~7 days; download and file the chosen frame into `Image Reference/` the same day.

---

## 5. SOUL ID — character consistency

When the same person must recur across multiple shots (or carry into a Seedance "Element"), train a **SOUL ID** instead of re-rolling a face each time.

- **Input:** 20–80 photos of one person — varied angles, several expressions, at least one full-height frame for body proportions, even lighting, no sunglasses / heavy shadow / cropped faces.
- **Training:** a few minutes, black-box. Produces a reusable identity referenced by an opaque ID — not an exportable file, lives inside the SOUL platform.
- **Use:** apply the SOUL ID to any generation with an adherence strength 0–1 (default 1). It combines with any preset and/or reference image — identity and style are separate inputs.
- **Expectation:** "clearly the same person," not pixel-identical; drift increases under extreme style or angle changes. QC each frame for likeness before it enters Stage 3.
- **Consent:** only train on yourself or someone who has given permission to use their likeness. Log which SOUL ID maps to which person alongside the generation log.

---

## 6. Reference-image mode vs. text mode

| Mode | Input | Use for |
|---|---|---|
| Text-to-image | Prompt only | Casting from scratch — no subject or location photo exists |
| Reference image | Prompt + **one** image URL + style strength | Carrying a location, wardrobe, or composition from an existing frame into SOUL's aesthetic |
| SOUL ID | Prompt + trained identity (+ optional preset / reference) | Recurring person (§5) |

Only **one** reference image per generation — there is no multi-image reference array. Multi-image inputs exist only for SOUL ID training and the in-app Moodboard/HEX tools (no API), so for this pipeline treat "reference" as single-image.

---

## 7. QC gate — before the frame enters Stage 3

A SOUL frame is only done when it passes every check. Fail any → re-prompt or re-roll, don't proceed.

- **Stage 1 compliance** — aspect ratio exact; no legible text/logos in frame; no violated subject-matter fact from the forbidden list; palette in range (SOUL has no hex lock, so eyeball it against the Stage 1 hex).
- **Subject / background separation** — the subject reads as clearly detached from background clutter. Both video models animate off depth and edges; a busy or flat frame = messy motion in Stage 4. This is the single most important check.
- **Structural integrity on anything that must stay locked later** — hands, faces, architecture, product geometry not warped or melting. SOUL's candid-imperfection bias is fine on skin and fabric; it is not fine on things Stage 3 will mark "locked."
- **Exposure** — even and readable; not so blown-out or crushed that Stage 3 can't classify elements in that region.
- **Likeness** (SOUL ID only) — recognizably the intended person at this angle and style strength.
- **Resolution** — 1080p minimum, ideally 2K, native (not upscaled).

Passing frame → file it in `Image Reference/`, log the prompt + preset + seed in the generation log, then write its motion map.

---

## 8. Anti-patterns

- **Don't carry the 1500-character habit over.** A Seedance-length prompt makes SOUL worse. Write three lines, pick a preset, stop.
- **Don't stack camera/film/lens description on top of a preset.** The preset already encodes it; adding "shot on Portra 400, 35mm, harsh flash, halation, grain" on top of `2000s Cam` muddies the result. That vocabulary belongs in Stage 4, on the video prompt — not here.
- **Don't fight the imperfection bias frame-wide.** Grain and candid flash are why the reference survives into Seedance looking captured rather than rendered. Only push back where it breaks a locked element (hands, signage), and do that at QC by re-rolling, not by prompting "ultra clean, no grain, sharp."
- **Don't rely on a negative prompt** — there isn't one. Anything that must be absent is a positive-prompt statement plus a QC rejection criterion.
- **Don't assume reproducibility.** Seed exists, but with no CFG/step control and prompt-enhancement rewriting your text, "same inputs → same image" is loose. For a frame you must be able to regenerate, record seed **and** the exact prompt **and** turn `enhance_prompt` off.
- **Don't switch presets mid-sequence** for frames meant to cut together.

---

## 9. Handoff notes

- **Generation log:** record per SOUL frame — locked Look + Stance (Photography-Styles-Library.md), prompt string, preset + strength, aspect ratio, resolution, seed, `enhance_prompt` on/off, SOUL ID (if any). Same log discipline as the rest of the pipeline; it's the deliverable.
- **Into Stage 3:** the SOUL frame is treated identically to a sourced photo. Note its position/framing first (Camera-Framing-Angle-Library terms), then classify locked vs. moving.
- **Synergy with [Camera-Look-Library.md](Camera-Look-Library.md):** a SOUL reference already carries film-like texture, so in Stage 4 you can lean slightly less on positive grain language and slightly more on holding that texture ("preserve the grain and flash character of the reference"). The anti-digital negative list still goes in every video prompt.
- **What SOUL does *not* do here:** no dedicated negative prompt, no CFG/steps, no multi-image reference, no in-pipeline color-hex lock, and the Inpaint / HEX / Moodboard tools are in-app only (no API) — if a shot needs those, it's a manual in-app pass, not part of the scripted flow.
