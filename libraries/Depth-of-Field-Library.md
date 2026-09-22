# Depth of Field Library

Companion to [Camera-Movements-Library.md](Camera-Movements-Library.md) and [Camera-Framing-Angle-Library.md](Camera-Framing-Angle-Library.md). Those cover motion and position; this one covers *what's sharp and what's not* — the paste-ready phrase for describing focus, blur, and bokeh in the `[style/mood]` or `[lens/perspective language]` slot of the per-shot prompt template (see [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md)). Works across Kling, Seedance, and similar image-to-video tools — depth of field is controlled entirely through prompt language on both, there's no dedicated slider.

Source: synthesized from current AI-video prompting guides on depth of field and bokeh technique, including [Hailuo AI's DoF & bokeh prompting guide](https://hailuoai.video/pages/knowledge/mastering-depth-of-field-cinematic-bokeh-prompting), [Hailuo AI's product-video bokeh guide](https://hailuoai.video/pages/knowledge/soft-focus-bokeh-ai-product-video-guide), [vvsvs.pro's rack focus guide](https://vvsvs.pro/cinematique/rack-focus), [invideo.io's cinematography terms guide](https://invideo.io/faq/what-cinematography-terms-work-best-in-ai-video-prompts/), and [ageofllms.com's DoF techniques overview](https://ageofllms.com/ai-howto-prompts/ai-fun/dof-techniques-ai-image-generation).

---

## Shallow Focus / Subject Isolation

| Technique | Paste-ready phrase | Notes |
|---|---|---|
| Shallow Depth of Field | `Shallow depth of field, subject in sharp focus while the background dissolves into soft blur.` | General-purpose default for subject isolation |
| Extreme Subject Isolation | `Extremely shallow depth of field, only a thin sliver of the subject in focus, everything else dissolving into soft blur.` | Macro/detail work — use deliberately, can read as a flaw if overused |
| Telephoto Compression + Shallow Focus | `Telephoto lens compression with shallow depth of field, background pulled visually closer and rendered as soft blur.` | Pairs with Telephoto Compression in [Camera-Framing-Angle-Library.md](Camera-Framing-Angle-Library.md) |
| Macro Shallow Focus | `Macro lens perspective, extremely shallow depth of field isolating fine texture and detail, background fully dissolved.` | Product/food/detail work |
| Sharp Subject, Soft Foreground Edge | `Soft out-of-focus foreground element at the edge of frame, sharp focus held on the subject behind it.` | Adds depth without moving focus — see Foreground Framing below |

## Deep Focus / Everything Sharp

| Technique | Paste-ready phrase | Notes |
|---|---|---|
| Deep Focus | `Deep focus, sharp detail held from foreground to background across the full depth of the scene.` | Landscapes, establishing shots, architecture — sells scale/detail over intimacy |
| Hyperfocal Landscape | `Hyperfocal distance focus, everything from the middle distance to the horizon rendered in sharp detail.` | Wide establishing/landscape shots |
| Group / Ensemble Focus | `Every subject held in sharp focus from nearest to furthest, no falloff across the group.` | Multi-subject shots where no one should read as secondary |

## Focus Transitions

| Technique | Paste-ready phrase | Notes |
|---|---|---|
| Rack Focus, Foreground → Background | `Focus racks smoothly from the sharp foreground subject to the background over two seconds, the background resolving into detail as the foreground softens.` | Needs a narrative trigger (a glance, sound, revealed object) or it reads as an error, not a choice |
| Rack Focus, Background → Foreground | `Focus racks smoothly from the background to the foreground subject over two seconds, the foreground sharpening into detail as the background dissolves into soft blur.` | Classic reveal — introduces the "real" subject after a decoy |
| Slow Reveal Into Focus | `Shot opens soft and out of focus, gradually resolving into sharp focus on the subject as the shot settles.` | Cold-open/establishing beat — works even on a locked-off camera |
| Focus Breathing Drift | `Focus subtly drifts and breathes across the depth of field as the camera holds, without fully racking to a new subject.` | Adds "shot on real glass" realism — subtle, easy to overdo |

## Bokeh & Background Light Quality

| Technique | Paste-ready phrase | Notes |
|---|---|---|
| Creamy Circular Bokeh | `Soft, creamy circular bokeh in the background, out-of-focus highlights rendered as smooth round discs of light.` | Default premium/commercial background quality |
| City Lights Bokeh | `Background city lights dissolve into soft bokeh, scattered points of warm and cool light blurred into round discs.` | Night/urban backgrounds |
| Dappled Light Bokeh | `Dappled sunlight through foliage breaks into soft out-of-focus bokeh circles across the background.` | Outdoor/natural-light backgrounds |
| Specular Highlight Bokeh | `Specular highlights in the background bloom into soft bokeh as the lens holds a wide aperture.` | Reflective surfaces, water, glass — reinforces the shallow-focus read |

## Lens & Aperture Language

| Technique | Paste-ready phrase | Notes |
|---|---|---|
| Wide-Aperture Prime | `Wide-aperture prime lens look, f/1.4-f/1.8 character, shallow plane of focus with soft falloff.` | Style cue, not a literal slider — models read the f-number as a vibe, not a computed value |
| Standard Aperture | `Standard aperture, f/4-f/5.6 character, moderate depth of field holding the subject and near background both reasonably sharp.` | Balanced default when neither shallow nor deep is called for |
| Small Aperture / Everything Sharp | `Small aperture, f/11-f/16 character, wide depth of field keeping near and far detail both crisp.` | Pairs with Deep Focus above; landscape/architecture |
| Vintage Lens Character | `Vintage lens character, gentle softness at the edges of the focal plane.` | Use with caution — "swirly"/anamorphic bokeh quirks are unpredictable across models; keep it generic |

## Foreground Framing

| Technique | Paste-ready phrase | Notes |
|---|---|---|
| Frame Within a Frame | `Soft out-of-focus foreground framing element — a doorway, branch, or railing — at the edge of the composition, sharp focus held on the subject beyond it.` | Adds depth/context without racking focus; pairs with Close Foreground Placement in [Camera-Framing-Angle-Library.md](Camera-Framing-Angle-Library.md) |
| Depth Layering (FG / MG / BG) | `Three visible depth layers — soft blurred foreground, sharp midground subject, softly blurred background — selling depth without any focus movement.` | Static-shot depth cue, strong for portraits/product |

---

## Selector (which category to reach for)

| Subject | Default category | Lead candidates |
|---|---|---|
| Portrait, close-up face | Shallow Focus | Telephoto Compression + Shallow Focus, Creamy Circular Bokeh |
| Product / still-life | Shallow Focus | Macro Shallow Focus, Wide-Aperture Prime |
| Food / tabletop | Shallow Focus | Macro Shallow Focus, Dappled Light Bokeh |
| Landscape / establishing scene | Deep Focus | Deep Focus, Hyperfocal Landscape |
| Architecture / real estate exterior | Deep Focus (usually) | Deep Focus — switch to Sharp Subject, Soft Foreground Edge if a tree/railing sits in frame |
| Group / ensemble shot | Deep Focus | Group / Ensemble Focus |
| Two-subject dialogue, attention must shift | Focus Transition | Rack Focus Foreground→Background or Background→Foreground, matched to a stated trigger |
| Night / urban background | Shallow Focus | City Lights Bokeh |

### Overrides

- **Wide-angle or ultra-wide lens phrase already in the prompt** → don't stack shallow depth of field on top. The two are physically contradictory; most models will pick one or render an inconsistent blend. Drop to Standard or Small Aperture instead.
- **Busy/cluttered background** → lean into Shallow Focus harder than usual — it doubles as cleanup, same logic as Stage 2's clean-composition rule in the pipeline.
- **Two distinct depth planes with a stated reason for attention to move** (a glance, a sound, a reveal) → use a Focus Transition, not a static category.
- **Multi-shot sequence** → pick one depth-of-field register per treatment (e.g. always shallow + creamy bokeh for an intimate portrait series, always deep focus for a real-estate walkthrough) so the set reads as one camera, same as the movement-family and lens-register rules in the other two libraries.

---

## Anti-patterns

- **Don't stack synonyms.** "Cinematic bokeh, shallow depth of field, creamy blur, soft focus" in one prompt is redundant load, not reinforcement — pick one phrase per category and let it carry the intent.
- **Don't treat f-stop numbers as literal sliders.** "f/1.8" reads as a style cue to these models, not a computed aperture value — useful for vibe, not for precision.
- **Don't pair wide-angle language with shallow depth of field.** They contradict each other physically; see the override above.
- **Avoid vintage-specific bokeh quirks** ("swirly bokeh," "anamorphic oval bokeh") unless tested on the specific model first — unpredictable, may not render at all.
- **A rack focus needs a trigger and a duration.** State what causes the shift and roughly how long it takes ("...over two seconds, as the phone buzzes on the table") — without both, it reads as a focus error rather than a deliberate move.

---

## Model-specific notes

| | Kling | Seedance |
|---|---|---|
| DOF control | Text-only — no dedicated slider (unlike its pan/tilt/zoom/roll % sliders in Pro mode) | Text-only — works best paired with a reference image that already has the depth-of-field baked in |
| Best default | Pair the DOF phrase with Kling's structured shot-description style (subject, action, lens, light, in order) | Keep DOF language to 1-2 words, not stacked adjectives — let the reference image carry most of the optical look |
| Rack focus | Describe as a timed, observed transition rather than the instruction "rack focus" | Same — restate as an observed result, per the pipeline's general diagnose rule below |

---

## Usage notes

- Drop the paste-ready phrase into the `[style/mood]` slot of the per-shot prompt template, or fold it into the signature card's `[lens/perspective language]` slot if it should hold constant across the whole treatment (see [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md)).
- Per the pipeline's diagnose step: if the model ignores a stated focus shift, restate it as an **observed result** rather than an instruction — e.g. instead of "rack focus to the background," describe what the frame shows: *"the background sharpens into detail over two seconds as the foreground softens into blur."*
- Depth of field and camera movement compound — a Dolly In (from [Camera-Movements-Library.md](Camera-Movements-Library.md)) naturally deepens background blur as the subject nears the lens, so a stated "shallow depth of field" plus a push-in reinforce each other rather than fighting.
- For multi-shot sequences, treat the depth-of-field register the same as the camera-language "signature card" line — one register per treatment, not a different DOF choice per shot.
