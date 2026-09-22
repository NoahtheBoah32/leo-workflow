---
name: realist-portrait
description: Writes a photorealistic character-portrait prompt — model-agnostic natural language — from a written brief, from an attached reference photo (likeness-preserving), or as a multi-angle character reference sheet for this project's Image-to-Video pipeline. Carries its own craft libraries (skin & face, face lighting, portrait lenses, wardrobe/hair/grooming, demographic specificity, anti-"AI plastic" negatives, character consistency). Use whenever the user wants a believable human portrait prompt rather than a moving shot.
---

# Realist Character Portrait — prompt builder

Turns a character idea, a reference photo, or a "I need a consistent character" request into a paste-ready **still-portrait** prompt that reads as a photograph of a real person, not a render.

## Division of labor

Prompt text only. This skill never calls Seedream / Dreamina / Midjourney / Flux / any generator and never claims to have produced an image — same rule as [Image-to-Video-Pipeline.md](../../../Image-to-Video-Pipeline.md). The user runs the generation and brings results back.

## Ground truth — read what you need before writing; don't work from memory of a past turn

- [references/skin-and-face.md](references/skin-and-face.md) — skin texture, pores, asymmetry, age-appropriate features, expression & gaze.
- [references/face-lighting.md](references/face-lighting.md) — portrait lighting patterns (Rembrandt / loop / split / butterfly / broad / short), source quality, ratio, catchlights.
- [references/portrait-lenses.md](references/portrait-lenses.md) — focal length, aperture/DOF, working distance, camera height vs eyeline, perspective compression. Cross-refers to [Lenses/Zeiss-Supreme-Prime-Lens-Library.md](../../../Lenses/Zeiss-Supreme-Prime-Lens-Library.md) and [Depth-of-Field-Library.md](../../../Depth-of-Field-Library.md).
- [references/wardrobe-hair-grooming.md](references/wardrobe-hair-grooming.md) — fabric, fit, period, condition; hairstyle with real-world imperfection; grooming state.
- [references/demographic-specificity.md](references/demographic-specificity.md) — how to specify age, heritage, sex, body type concretely and without caricature.
- [references/anti-ai-tells.md](references/anti-ai-tells.md) — the recurring "looks AI" failure modes and the negative-prompt bank.
- [references/character-consistency.md](references/character-consistency.md) — the Identity Lock Card used by photo-driven and character-sheet modes.
- [Camera-Look-Library.md](../../../Camera-Look-Library.md) — capture character (film/digital, grain, halation, shutter) so the still matches any video made from it.
- [Photography-Styles-Library.md](../../../Photography-Styles-Library.md) — two axes: the **Look** (film-stock looks, Old Hollywood glamour, editorial auteurs, direct-flash snapshot, etc.) and the **Stance** (§8: genuine candid / directed candid / posed). If the brief names or implies either, pull the vocabulary from here and let the Realism Stack below execute it layer by layer; keep both consistent with any signature card the portrait feeds. Default stance for a straight portrait is **posed** unless the brief says candid/reportage.

## Modes — pick one from the request, state which you picked

| Mode | Trigger | Extra inputs it needs |
|---|---|---|
| **A — Brief only** | A written description, no photo attached. | Nothing beyond the brief; ask only for the *purpose* if it's missing (see Stage 1). |
| **B — Photo-driven** | A reference photo of a person is attached, and the ask is a portrait *of that person*. | The photo (file path or attachment); what to keep vs. change (likeness always kept). |
| **C — Character sheet** | "Consistent character", "reference sheet", "same person across shots", or the portrait is explicitly a character for the video pipeline. | Number of views/expressions wanted; whether it feeds a specific signature card. |

## Workflow — run in order

1. **Purpose check.** One line: what is this portrait *for* (casting look, hero brand face, background extra, character-sheet base, editorial cover)? Purpose sets register — crop, wardrobe polish, lighting drama, how much imperfection. If it's not stated and not obvious, ask before building.
2. **Reference read (Mode B/C).** If a photo is attached, describe what's fixed by likeness: face geometry, skin tone, eye colour, hairline, distinguishing marks, apparent age. Build the [Identity Lock Card](references/character-consistency.md) now and state it. If the photo is low-res / harshly lit / heavily filtered, say so — a weak reference caps how faithful the prompt can be.
3. **Fill the Realism Stack.** Every portrait prompt specifies all nine layers below. Pull paste-ready phrasing from the reference files. Don't leave a layer to the model's default — that's where the "AI look" enters.
   1. **Identity & demographics** — age *in years*, heritage specifics, sex, build, distinguishing features. Specific, not generic ([demographic-specificity.md](references/demographic-specificity.md)).
   2. **Skin & face rendering** — visible pores, natural asymmetry, age-appropriate lines/texture, subsurface scattering, unretouched; blemishes/freckles/scars as fitting ([skin-and-face.md](references/skin-and-face.md)).
   3. **Expression & gaze** — specific micro-expression, where the eyes go, genuine vs. social smile, head tilt, muscle engagement ([skin-and-face.md](references/skin-and-face.md)).
   4. **Lighting** — named pattern, source size/quality, direction, key-to-fill ratio, catchlight shape ([face-lighting.md](references/face-lighting.md)).
   5. **Lens & camera** — focal length (portrait band 50–135mm eq.), aperture / DOF depth, working distance, camera height relative to the eyeline, perspective compression ([portrait-lenses.md](references/portrait-lenses.md)).
   6. **Wardrobe, hair, grooming** — fabric and fit named, period/condition, hairstyle *with* flyaways/parting, grooming state ([wardrobe-hair-grooming.md](references/wardrobe-hair-grooming.md)).
   7. **Environment & framing** — background and subject separation, crop (headshot / head-and-shoulders / half / three-quarter / full), aspect ratio.
   8. **Capture character** — film or digital body, grain, white balance, colour response, halation, faint optical imperfection ([Camera-Look-Library.md](../../../Camera-Look-Library.md)).
   9. **Negatives** — the anti-AI-tells bank, trimmed to what's relevant ([anti-ai-tells.md](references/anti-ai-tells.md)).
4. **Mode C expansion.** Repeat the frame/expression layer once per requested view (e.g. front neutral, 3/4 left slight smile, profile right, looking-down). Everything else — the Identity Lock Card, lighting, lens, capture — stays **verbatim** across every view so the character holds. State it once, reference it, don't redrift it.
5. **Assemble.** One flowing natural-language paragraph (not a keyword dump), ordered: subject & demographics → skin/expression → wardrobe/hair → framing & lens → lighting → environment → capture character. Then the negative list.
6. **Model-agnostic note.** Below the prompt, add one short line on adapting it: Midjourney (compress to phrases, add `--ar` / `--style raw` / moderate `--stylize`), Flux / Seedream / Dreamina (use the paragraph as-is; put negatives in the negative field if present, else drop them), and note any single phrase most likely to need tuning.

## Output format

- Positive prompt in its own fenced code block, ready to paste.
- Negative prompt in a second code block immediately after (label it "if the model has a negative field").
- Mode C: one code block **per view**, each preceded by its view label; the shared Identity Lock Card printed once above them.
- The purpose line, chosen mode, and model-adaptation note go **outside** the code blocks.

## Guardrails

- Prompt text only — never call a generator, never claim an image was made.
- Always specify age in years and concrete heritage — "attractive person", "beautiful woman", "ethnically ambiguous" are the defaults that produce the averaged AI face. Reach for specificity even when the brief is vague; ask if you truly can't.
- Photorealism includes imperfection. If the prompt has no pores, no asymmetry, no stray hair, no skin variation, it isn't finished.
- Likeness in Mode B/C is non-negotiable — never "improve" bone structure, skin tone, age, or distinguishing marks unless explicitly asked.
- No prompts sexualising minors, and no photoreal prompts targeting a real, named private individual from a brief alone (Mode B needs the user's own supplied photo).
- A weak reference photo produces a weak likeness — flag it, don't paper over it.
- Keep total prompt length within the target model's limit; for this project's Seedream/Dreamina default, keep positive + negative combined ≤1500 characters (Stage 1 budget).
