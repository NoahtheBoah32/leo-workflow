# Camera Look Library

Companion to [Depth-of-Field-Library.md](Depth-of-Field-Library.md). That one covers *what's sharp and what's not*; this one covers *what makes the image look like it was captured by a physical camera instead of rendered* — grain, texture, lens imperfections, and shutter/motion-blur character. Built for one recurring problem: 4K AI video output that's technically clean but reads as "VFX" or "digital render" rather than "shot on a camera used for ads and films." Works across Kling, Seedance, and similar image-to-video tools — there's no dedicated grain/shutter slider on either, it's all prompt language.

No external source — unlike the movement/framing libraries, this isn't phrases extracted from a reference site. It's standard cinematography/photography vocabulary (real camera bodies, film stocks, shutter-angle convention, lens artifacts) translated into paste-ready prompt phrases.

---

## 1. Base Camera/Sensor Emulation

Pick **one** and hold it constant across the whole treatment — same rule as the lens/perspective register in the signature card. This is the single strongest lever for "looks like it was shot on a real camera used in ads and films," because it gives the model a concrete physical reference instead of an abstract "cinematic" adjective.

| Camera | Paste-ready phrase | Notes |
|---|---|---|
| ARRI Alexa 35 (default) | `Shot on an ARRI Alexa 35, ARRI color science, natural filmic highlight rolloff, true-to-life color, gentle desaturation in shadows.` | The current default body for premium commercials and features — famous for skin tones and highlight handling. Best single default when the brief is just "make it look like an ad/film." |
| ARRI Alexa Mini LF | `Shot on an ARRI Alexa Mini LF large-format sensor, cinematic shallow depth of field falloff, soft creamy background rendering.` | Pair with a shallow-DOF phrase from [Depth-of-Field-Library.md](Depth-of-Field-Library.md); large-format character |
| Sony Venice 2 | `Shot on a Sony Venice 2, full-frame cinema sensor, wide dynamic range, dual-ISO shadow detail, clean but filmic color.` | Alternate to Alexa — slightly cleaner, cooler default color response |
| RED V-Raptor | `Shot on a RED V-Raptor, sharp high-resolution digital cinema image, punchy contrast, modern commercial clarity.` | Crisper, more "digital-premium" — weakest choice if the goal is specifically *less* digital; reach for it only on automotive/tech briefs |
| Film Stock Overlay | `Photochemical film emulation, Kodak Vision3 tungsten-balanced stock characteristics, warm shadow tone, soft halation around highlights.` | Stack on top of any digital camera phrase for a hybrid "shot digital, finished on film" look — the strongest single lever against the "too clean" complaint |

## 2. Shutter Angle & Motion Blur

The single biggest tell that separates "film" from "AI/video-game" motion is whether moving elements carry any motion blur at all.

| Shutter | Paste-ready phrase | Notes |
|---|---|---|
| Standard Cinema (180°) | `180-degree shutter angle, natural cinematic motion blur on moving elements, no stutter or strobing.` | Default — matches the motion-blur character audiences read as "film" |
| Crisp Action (172.8°/90°) | `Slightly narrower shutter angle, crisper motion blur with a touch more definition on fast movement.` | Product/action shots that should still read decisive, not smeary |
| Dreamy Wide (270°–360°) | `Wide shutter angle, heavier trailing motion blur, dreamlike smear on fast-moving elements.` | Sparingly — flashback/slow-emotional beats only |

## 3. Film Grain & Texture

| Grain | Paste-ready phrase | Notes |
|---|---|---|
| Fine Commercial Grain (default) | `Fine, subtle film grain across the image, most visible in the mid-tones and shadows, textured but not noisy.` | Premium ad default — present but not distracting |
| Medium 35mm Grain | `Visible 35mm film grain structure, organic texture breaking up flat digital smoothness, grain shifts slightly frame to frame.` | Stronger, overtly "shot on film" |
| Heavier 16mm/Documentary Grain | `Coarse 16mm film grain, gritty documentary texture, grain most pronounced in shadow detail.` | Editorial/documentary/gritty brief only |
| Halation on Highlights | `Soft halation glow bleeding warmly around bright highlights and light sources, classic film-stock bloom.` | Reads strongly as "film"; pairs with any grain choice |

## 4. Optical Imperfections (Lens Character)

| Imperfection | Paste-ready phrase | Notes |
|---|---|---|
| Subtle Chromatic Aberration | `Faint chromatic aberration fringing at the extreme edges of frame on high-contrast edges, barely visible.` | Keep subtle — overdone, it reads as an Instagram filter, not a lens |
| Natural Vignette | `Gentle natural vignette, subtle darkening toward the corners of frame from the lens itself.` | Draws the eye to center, reads as real glass |
| Lens Flare / Veiling Glare | `Subtle veiling glare and soft lens flare when a light source crosses the frame edge, gentle contrast loss around the flare.` | Only when a light source is in or near frame |
| Lens Breathing | `Subtle focus breathing as the lens holds focus, a faint shift in field of view.` | Very subtle; cross-ref Depth-of-Field-Library's "Focus Breathing Drift" |
| Micro-Imperfections | `Faint dust and micro-scratches barely visible in the image, imperceptible sensor/lens imperfections, not clean digital perfection.` | Use sparingly — too much reads as "damaged film," not "shot on camera" |

## 5. Color Science / Exposure Imperfections

| Trait | Paste-ready phrase | Notes |
|---|---|---|
| Filmic Highlight Rolloff | `Highlights roll off softly and organically instead of clipping hard, gentle compression in the brightest areas.` | Counters AI video's tendency to blow out highlights in a flat, clipped digital way |
| Lifted Shadows | `Shadows are not crushed to pure black, subtle detail and slight warmth retained in the darkest areas.` | Classic filmic trait, avoids the "video game black" look |
| Slight Exposure/Color Imperfection | `A touch of natural exposure imperfection and color variance across the frame, as if captured by a real camera and not digitally rendered.` | General catch-all when nothing else fits |

---

## Selector (which combo for which brief)

| Brief | Base camera | Shutter | Grain | Extras |
|---|---|---|---|---|
| Premium commercial/ad (default) | ARRI Alexa 35 | 180° | Fine Commercial Grain | Halation, natural vignette, filmic highlight rolloff |
| Cinematic drama/narrative | ARRI Alexa Mini LF | 180° | Medium 35mm Grain | Lens breathing, halation, lifted shadows |
| Gritty documentary/editorial | Alexa 35 or Mini LF | 180° | Heavier 16mm Grain | Veiling glare, chromatic aberration |
| Sci-fi/tech/automotive premium | RED V-Raptor | 172.8° | Fine Commercial Grain (light) | Subtle CA only, minimal vignette |

---

## Anti-patterns

- **Don't max out every category at once.** Heavy grain + heavy vignette + heavy CA + heavy flare together reads as an Instagram filter stacked on top of the image, not a camera. Pick one "hero" imperfection per shot and keep the rest subtle — same discipline as the DoF library's "don't stack synonyms" rule.
- **Describe imperfections as native to the capture, not an applied effect.** Say "shot on an ARRI Alexa 35 with fine film grain," not "add a grain filter" or "apply a vignette effect" — phrasing it as a filter/overlay cues the model toward a post-processed look, the opposite of the goal.
- **Keep the camera-body choice constant across a whole treatment.** Same "shot on X" phrase in every shot's signature card, exactly like the lens/perspective register rule elsewhere in the pipeline — switching cameras mid-treatment breaks the squint test.
- **Shutter angle and f-stop numbers are style cues, not literal computed values** — same caveat as the DoF library's f-stop note. Don't expect literal physical accuracy from them.

## Negative prompt additions (do this every time)

Fighting a "too clean/digital" default needs explicit negative-side pressure, not just positive camera language. Add to Kling's dedicated negative field, or fold into the Seedance prompt:

```
no CGI look, no 3D render, no video game rendering, no plastic or waxy skin, no oversharpened
digital clarity, no flat lifeless highlights, no clipped blown-out whites, no hyper-clean
noise-free image, no digital sheen, no motion interpolation smoothness
```

---

## Model-specific notes

| | Kling | Seedance |
|---|---|---|
| Grain/shutter control | Text-only, no dedicated slider | Text-only, no dedicated slider |
| Strongest lever | Combine positive camera/film language with the negative anti-digital list above, every time | Same — and if the reference image itself is a clean digital render, both models tend to preserve that base cleanliness, so a reference that already has grain/texture baked in outperforms text alone |
| If grain doesn't show up | Push the grain phrase earlier in the prompt (near the signature card, not buried at the end) | Same; also try pairing with the Film Stock Overlay phrase, which reads as a stronger instruction than grain alone |

## Usage notes

- **Signature card slot:** fold the base camera/film choice into the `[finish: photoreal / commercial / etc.]` slot of the signature card (see [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md) Stage 4) — e.g. `Shot on ARRI Alexa 35, fine film grain, natural 180-degree motion blur, soft halation, filmic highlight rolloff`. This is treatment-level, fixed once, not rewritten per shot.
- **Per-shot slot:** only restate imperfections that vary shot to shot (e.g. lens flare only when a light source is actually in frame that shot). The base camera/grain/shutter stays in the signature card.
- **Negative prompt:** add the anti-digital list above to every shot's negative field, same as Stage 1's forbidden list — it's a standing addition, not a per-shot decision.
