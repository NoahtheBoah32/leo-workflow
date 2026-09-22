# img-character-sheet  (14 blocks)


====================================================================================================
## [img-character-sheet #0]  703dd4af  2026-08-24T01:12:53.408Z  len=1568
**USER:** @Image Reference/Test/R1.jpg  create a image prompt of this source image I want a end frame of this image that she was smiling

**PRE:** …xpression. Here's an end-frame prompt that keeps everything else locked and swaps only the expression to a smile — useful as the "end frame" reference in an image-to-video first/last-frame workflow.

**End Frame — R1.jpg (smiling variant)**

```
Photoreal cinematic close-up portrait, young Asian girl in left-facing three-quarter profile,
identical framing, head angle, and camera distance to the reference image. She now wears a
warm, genuine smile — corners of her mouth lifted, eyes crinkled with delight, eyebrows
relaxed — replacing the open-mouthed awe of the original frame. Same wind-tousled long dark
hair with blunt bangs catching the breeze, same pale blue-white top. She stands at the same
elevated wooden-railed walkway at Gardens by the Bay, Supertree Grove's lattice-branched steel
structures rising behind her against a clear blue sky, golden-hour sunlight raking warmly
across her face from camera right, soft rim light on her hair. Lush green canopy and a distant
elevated walkway bridge visible below and behind the railing. Shallow depth of field, subject
tack-sharp, background softly defocused. Natural skin texture, no retouching artifacts, shot on
a cinema camera with a short telephoto lens, warm golden color grade matching the original
frame exactly.

Locks: identity, hairstyle, wardrobe, camera framing/angle, lighting direction and color
temperature, background (Supertree Grove, railing, sky) identical to the reference frame — only
the facial expression changes from open-mouthed wonder to a smile.

Negative: no change in identity/face structure, no change in outfit or hair color/style, no
added text or logos, no extra people, no change in camera angle or framing, no exaggerated or
toothy grin, no warping of background structures, no color-grade shift from the original frame.
```

====================================================================================================
## [img-character-sheet #1]  b7747c58  2026-08-24T01:24:38.834Z  len=856
**USER:** <task-notification>
<task-id>a63a8153089f94dda</task-id>
<tool-use-id>toolu_01Eu6LKjLU9WPPj7CyHCWdmL</tool-use-id>
<output-file>/private/tmp/claude-502/-Users-leo-Desktop-Neutra-DC-Image-to-Video/b7747c58-acd6-4fa0-8efb-602f52078747/tasks/a63a8153089f94dda.output</output-file>
<status>completed</sta

**PRE:** …er the 1500 cap.

**On generation:** attach both frames as start/end references (Stage 5) — role-scope R1_1 as the opening state and R1_2 as the arrival state, both controlling identity/framing only, not literal per-frame timing.

## Prompt

```
Lens slowly zooms in at a constant, unhurried pace, gradually tightening the frame from head-and-shoulders toward a closer view of her face, the three-quarter back angle and warm backlit rim-light on her hair held constant throughout. Her expression shifts from soft, parted-lips wonder into a genuine warm smile, her eyes crinkling as delight breaks across her face. A gentle wind lifts and stirs her dark hair, flyaway strands catching the golden backlight and drifting naturally, never repeating the same shape twice. Shallow depth of field, telephoto compression, the Supertree lattice and canopy behind her held as soft, steady bokeh, warm specular light glinting through the structure and blooming gently out of focus. Cinematic, photoreal, intimate golden-hour warmth, soft rim light haloing her hair, gentle backlight across her cheek and shoulder.
```

====================================================================================================
## [img-character-sheet #2]  0551a088  2026-09-01T07:02:13.455Z  len=1754
**USER:** @Image Reference/Test/F34.jpg use this as base image then replace the face using the face of  @Image Reference/Test/Grandfather.png. Make it photorealistic image. Write an image prompt.

**PRE:** …w, broad nose, deep smile lines, thick white eyebrows, mottled aged skin, full head of white hair combed straight back. Source expression is a big open smile — which needs to be adapted to the base's calm, eyes-closed rest.

## Image prompt

```
Using the first image as the base, replace only the face, head and hair of the
elderly man lying in the CT scanner with the identity of the elderly East Asian
man in the second image.

Preserve his identity exactly: same broad face shape, high cheekbones, wide jaw,
broad flat nose, deep-set eyes, heavy creases around the eyes and mouth, thick
white eyebrows, aged skin with age spots, freckling and fine wrinkles, and a full
head of white hair combed straight back off the forehead.

Adapt his pose and expression to the base image, do not copy the smile: head
resting back on the white pillow, face turned slightly up and toward camera at a
low three-quarter angle, eyes gently closed, brow relaxed, lips lightly together,
a calm and peaceful resting expression. Hair settles naturally against the pillow.

Keep everything else in the base image unchanged: the CT/MRI scanner bore and bed,
the olive-green knit cardigan over the white paper gown, the hands clasped on the
stomach, the floating holographic brain-scan panel reading "Series 2 of 3", the
medical imaging suite, the framing, camera angle, lens and depth of field.

Match the base image's lighting: soft cool clinical light from above with a warm
glow spilling from the scanner bore onto the near cheek, temple and forehead,
gentle shadow under the jaw and in the eye sockets. Blend the new face seamlessly
at the hairline, ears, jaw and neck so skin tone, warmth and shadow direction run
continuously into the neck and body already in the base image.

Photorealistic. Sharp focus on the face, natural aged skin texture with visible
pores, subsurface translucency and soft specular highlights. Match the film grain,
color grade and slight softness of the base photograph. No other changes.
```

====================================================================================================
## [img-character-sheet #3]  55cd0735  2026-09-01T08:39:26.632Z  len=645
**USER:** use the birds eye view angle

**PRE:** …s plaid dress, natural skin texture, fine detail, gentle film grain, soft contrast. No text, letters, numbers, logos, branding, UI or signage anywhere; the robot and the distant towers and dome carry no readable markings.
```

**Negative:**

```
eye-level, ground-level, low angle, horizon in frame, three-quarter or straight-on view; tilted horizon, fisheye or heavy wide-angle distortion; legible text, letters, numbers, logos, branding, watermark, signage, readable UI; extra people, missing people, duplicated family members, extra or fused fingers, distorted hands, extra limbs, warped faces; waxy plastic over-smoothed CGI skin, 3D-render look; oversaturated colour, neon, glowing red light trails or light-network arcs; blown highlights, harsh flash; sharp fully-detailed skyline, recognisable real landmark detail; modern clutter, printed packaging, phones; motion blur on the people
```

====================================================================================================
## [img-character-sheet #4]  cabba732  2026-09-02T01:20:53.475Z  len=1384
**USER:** the should not be an OTS, it should be a two shot. we can see the face of the grandfather and the grandaughter

**PRE:** …d, or toward each other.
  Camera -> fully locked tripod, no micro-drift, no handheld, no push.
  Tears -> may visibly brim and spill (tears of joy); contained - no sobbing, no face contortion.
```

## Stage 2.5 — Director's Brief (updated)

```
Director's Brief — H1_2b · Tripod MCU Two-Shot: The Granddaughter Leans to Her Grandfather (5s)
Dramatic intent: The relief landing between them - the young woman lets the good news break across
  her face and folds toward her grandfather, who takes it in quietly beside her; the viewer should
  feel a shared private exhale, the fear leaving the room. Not a connectivity beat - brand red absent.
Lead motion: The young woman's face releasing - eyes welling with tears of joy and brimming over,
  a soft breath, a trembling smile, a slow blink - then leaning in and lowering her head toward
  his shoulder, face still to camera in three-quarter, eyes closing as she settles.
Supporting motion: The grandfather's contained answer - eyes softening and welling a little, a
  small warm smile, his head tilting toward hers as she settles against him; his hand may come to
  rest over hers. Small, never competing with her.
Ambient motion: Her hair shifting as her head lowers; soft cool daylight from frame right shifting
  minutely; faint dust; slight knit-cardigan cloth movement.
Camera does: Nothing - a locked tripod two-shot that holds both faces and simply witnesses.
  Stillness is the point: it lets her lean and their shared quiet carry the whole beat.
Pace: Held throughout (static frame); her reaction decelerates into the lean and the eyes-closed
  settle, then a brief hold.
```

====================================================================================================
## [img-character-sheet #5]  a851a88d  2026-09-07T01:19:20.377Z  len=2126
**USER:** Base directory for this skill: /Users/leo/Desktop/Neutra DC/Image to Video/.claude/skills/realist-portrait

# Realist Character Portrait — prompt builder

Turns a character idea, a reference photo, or a "I need a consistent character" request into a paste-ready **still-portrait** prompt that reads a

**PRE:** … Heritage: Thai / Isan (Lao-Thai). 4 views, 4:5 vertical. Prompt text only — run these in your generator.

---

## Identity Lock Card — "ISAN FARMER (50)"

Copied verbatim into every view below; only the *framing* sentence changes per view.

```
IDENTITY LOCK — Isan Farmer (50)
- Age:            50 years old; set forehead + nasolabial creases, crow's feet at rest, deep squint lines, slackening jawline — clearly 50, not younger
- Heritage:       Thai, Isan / Lao-Thai (NE Thailand), lifelong rice farmer; dark sun-weathered brown skin; warm golden-brown undertone
- Sex / present.: man; minimal grooming, natural skin shine
- Face geometry:  broad square-round face; wide cheekbones with hollows beneath; low broad nose bridge, rounded tip, wide nostrils; deep-set dark brown monolid eyes, slight epicanthic fold; sparse low level brows; wide softening jaw, short blunt chin; medium-full lips, thinner upper lip; slight resting downturn
- Hairline & hair: mild M-shape recession at the temples; black going salt-and-pepper, grey heaviest at temples + sideburns, scattered white hairs on top; coarse thick straight hair, home-cut short back-and-sides, uneven over the ears, crown cowlick, hat-flattened on top
- Distinguishing: dark raised mole low on the left jaw; faint old scar through the left eyebrow
- Build (face):   lean and wiry; sinewy neck, visible tendons, prominent Adam's apple; hollow cheeks; creased weathered throat
- Facial hair:    sparse black-and-grey stubble, thin on the cheeks, denser at the chin + upper lip, a few long white hairs
- Fixed wardrobe: faded indigo short-sleeve cotton work shirt, soft washed collar, thin at the shoulders, one button missing; plain grey undershirt just visible at the neck
- Lighting:       large soft key just left of the lens axis (~25°), slightly above eye level; small loop nose-shadow; white bounce fill camera-right; low 2:1 ratio, open shadows; neutral 5600K; one catchlight at 10 o'clock  — LOCKED across all views
- Lens/camera:    85mm, camera ~2 m at eye level, f2.8, critical focus on the nearer eye, ears softening, no wide-angle distortion
- Background:     light neutral-grey painted canvas backdrop set back, subtly mottled, gentle edge falloff, faint seam, softly defocused
- Capture:        full-frame digital stills camera, neutral colour science, accurate skin tone, very fine restrained grain
```

====================================================================================================
## [img-character-sheet #6]  a851a88d  2026-09-07T01:19:20.377Z  len=2557
**USER:** Base directory for this skill: /Users/leo/Desktop/Neutra DC/Image to Video/.claude/skills/realist-portrait

# Realist Character Portrait — prompt builder

Turns a character idea, a reference photo, or a "I need a consistent character" request into a paste-ready **still-portrait** prompt that reads a

**PRE:** …t seam, softly defocused. Full-frame digital stills camera, neutral colour science, accurate skin tone, very fine restrained grain. Consistent facial identity in every frame.
```

### View 2 — three-quarter left (~30°), faint closed-lip set

```
Casting-sheet portrait, the same individual across all four frames: a 50-year-old Thai man of Isan / Lao-Thai heritage, northeastern Thailand, a lifelong rice farmer. Dark sun-weathered brown skin, warm golden-brown undertone, slightly leathery over the cheekbones and forehead, sun damage and light freckling, deep squint lines from the outer eyes, set forehead and nasolabial creases, crow's feet at rest, slackening jawline — clearly fifty, not younger. Real skin texture: visible pores, faint shine on forehead, nose and chin, no smoothing, soft translucency at the ear rims and nostrils. Broad square-round face, wide cheekbones with hollows beneath, low broad nose bridge and rounded tip, deep-set dark brown monolid eyes with a slight epicanthic fold, sparse low level brows, a wide softening jaw, short blunt chin, medium-full lips with a thinner upper lip and a slight resting downturn. Natural asymmetry — one eye a little smaller, brows uneven, the mouth pulling slightly to one side. A dark raised mole low on the left jaw; a faint old scar through the left eyebrow. Black hair turning salt-and-pepper, grey heaviest at the temples and sideburns, coarse thick straight hair, home-cut short back-and-sides, uneven over the ears, a crown cowlick, hat-flattened on top, a few flyaways. Sparse black-and-grey stubble, thin on the cheeks, denser at the chin, a few long white hairs. Lean wiry build, sinewy neck, visible tendons, prominent Adam's apple, creased weathered throat. Faded indigo short-sleeve cotton work shirt, soft washed collar, thin at the shoulders, one button missing, a grey undershirt just showing at the neck. This view: face turned about 30 degrees to camera-left with the far eye still fully visible, chin level, relaxed neutral expression with a faint closed-lip set, eyes to the lens. Head-and-shoulders crop, top of frame just above the hair, 4:5 vertical. 85mm lens, camera about 2 m away at eye level, f2.8, critical focus on the nearer eye, ears softening, no wide-angle facial distortion. Large soft key just left of the lens axis about 25 degrees and slightly above eye level, small loop nose-shadow, white bounce fill to camera-right, low 2:1 ratio with open detailed shadows, neutral 5600K, one soft catchlight at 10 o'clock. Light neutral-grey painted canvas backdrop set well back, subtly mottled, gentle darker falloff at the edges, a faint seam, softly defocused. Full-frame digital stills camera, neutral colour science, accurate skin tone, very fine restrained grain. Consistent facial identity in every frame.
```

====================================================================================================
## [img-character-sheet #7]  a851a88d  2026-09-07T01:19:20.377Z  len=2530
**USER:** Base directory for this skill: /Users/leo/Desktop/Neutra DC/Image to Video/.claude/skills/realist-portrait

# Realist Character Portrait — prompt builder

Turns a character idea, a reference photo, or a "I need a consistent character" request into a paste-ready **still-portrait** prompt that reads a

**PRE:** …dges, a faint seam, softly defocused. Full-frame digital stills camera, neutral colour science, accurate skin tone, very fine restrained grain. Consistent facial identity in every frame.
```

### View 3 — three-quarter right (~30°), neutral

```
Casting-sheet portrait, the same individual across all four frames: a 50-year-old Thai man of Isan / Lao-Thai heritage, northeastern Thailand, a lifelong rice farmer. Dark sun-weathered brown skin, warm golden-brown undertone, slightly leathery over the cheekbones and forehead, sun damage and light freckling, deep squint lines from the outer eyes, set forehead and nasolabial creases, crow's feet at rest, slackening jawline — clearly fifty, not younger. Real skin texture: visible pores, faint shine on forehead, nose and chin, no smoothing, soft translucency at the ear rims and nostrils. Broad square-round face, wide cheekbones with hollows beneath, low broad nose bridge and rounded tip, deep-set dark brown monolid eyes with a slight epicanthic fold, sparse low level brows, a wide softening jaw, short blunt chin, medium-full lips with a thinner upper lip and a slight resting downturn. Natural asymmetry — one eye a little smaller, brows uneven, the mouth pulling slightly to one side. A dark raised mole low on the left jaw; a faint old scar through the left eyebrow. Black hair turning salt-and-pepper, grey heaviest at the temples and sideburns, coarse thick straight hair, home-cut short back-and-sides, uneven over the ears, a crown cowlick, hat-flattened on top, a few flyaways. Sparse black-and-grey stubble, thin on the cheeks, denser at the chin, a few long white hairs. Lean wiry build, sinewy neck, visible tendons, prominent Adam's apple, creased weathered throat. Faded indigo short-sleeve cotton work shirt, soft washed collar, thin at the shoulders, one button missing, a grey undershirt just showing at the neck. This view: face turned about 30 degrees to camera-right with the far eye still fully visible, chin level, relaxed neutral expression, eyes to the lens. Head-and-shoulders crop, top of frame just above the hair, 4:5 vertical. 85mm lens, camera about 2 m away at eye level, f2.8, critical focus on the nearer eye, ears softening, no wide-angle facial distortion. Large soft key just left of the lens axis about 25 degrees and slightly above eye level, small loop nose-shadow, white bounce fill to camera-right, low 2:1 ratio with open detailed shadows, neutral 5600K, one soft catchlight at 10 o'clock. Light neutral-grey painted canvas backdrop set well back, subtly mottled, gentle darker falloff at the edges, a faint seam, softly defocused. Full-frame digital stills camera, neutral colour science, accurate skin tone, very fine restrained grain. Consistent facial identity in every frame.
```

====================================================================================================
## [img-character-sheet #8]  a851a88d  2026-09-07T01:25:17.313Z  len=2911
**USER:** can we also have a full body reference?and lock it everytime when I ask for a character sheet?

**PRE:** … dark cotton work trousers, faded and softened, rolled once at the ankle; well-worn rubber sandals, straps stretched
```

Everything else in the card from the previous message is unchanged.

---

### View 5 — full-length, standing reference

```
Casting-sheet full-length reference, the same individual as the head-and-shoulders views: a 50-year-old Thai man of Isan / Lao-Thai heritage, northeastern Thailand, a lifelong rice farmer. Dark sun-weathered brown skin, warm golden-brown undertone, leathery over the face, neck and forearms, sun damage and light freckling, deep squint lines from the outer eyes, set forehead and nasolabial creases, crow's feet at rest, slackening jawline — clearly fifty, not younger. Real skin texture with visible pores, no digital smoothing. Broad square-round face, wide cheekbones with hollows beneath, low broad nose bridge and rounded tip, deep-set dark brown monolid eyes with a slight epicanthic fold, sparse low level brows, a wide softening jaw, short blunt chin, medium-full lips with a thinner upper lip and a slight resting downturn. Natural asymmetry — one eye a little smaller, brows uneven, the mouth pulling slightly to one side. A dark raised mole low on the left jaw; a faint old scar through the left eyebrow. Black hair turning salt-and-pepper, grey heaviest at the temples and sideburns, coarse thick straight hair, home-cut short back-and-sides, uneven over the ears, a crown cowlick, hat-flattened on top, a few flyaways. Sparse black-and-grey stubble, thin on the cheeks, denser at the chin, a few long white hairs. Lean wiry build, narrow shoulders, sinewy forearms with visible tendons and raised veins, knotted knuckles, thin through the chest, a flat hard stomach, a slight forward stoop from decades of field work. Faded indigo short-sleeve cotton work shirt, soft washed collar, thin at the shoulders, one button missing, a grey undershirt just showing at the neck; loose dark cotton work trousers, faded and softened, rolled once at the ankle; well-worn rubber sandals with stretched straps, the feet and toes weathered and calloused. This view: standing square to camera, weight even on both feet, arms relaxed at the sides, hands open with fingers relaxed and fully visible, chin level, relaxed neutral expression, eyes to the lens. Full-length framing, small headroom, feet included with a little floor showing, 4:5 vertical. 50mm lens, camera about 4 m back at chest height, natural true-to-life proportions, f4 with the whole figure sharp and the backdrop softly separated, no wide-angle distortion. Large soft key just left of the lens axis about 25 degrees, raised and feathered to light the figure evenly from head to foot, white bounce fill to camera-right, low 2:1 ratio with open detailed shadows, neutral 5600K. Light neutral-grey painted canvas backdrop running down to a matching floor, subtly mottled, gentle darker falloff at the edges, a faint seam, softly defocused, a soft contact shadow at the feet. Full-frame digital stills camera, neutral colour science, accurate skin tone, very fine restrained grain. Consistent facial identity and body proportions across every frame.
```

====================================================================================================
## [img-character-sheet #9]  a851a88d  2026-09-07T01:25:17.313Z  len=639
**USER:** can we also have a full body reference?and lock it everytime when I ask for a character sheet?

**PRE:** …ital stills camera, neutral colour science, accurate skin tone, very fine restrained grain. Consistent facial identity and body proportions across every frame.
```

### Negative prompt (if the model has a negative field — full-body version)

```
plastic skin, waxy, airbrushed, over-smoothed, poreless, perfectly symmetrical face, generic AI face, stock-photo face, flat HDR lighting, 3d render, CGI, video game character, illustration, digital painting, overprocessed, youthified, de-aged, wide-angle facial distortion, enlarged nose, fisheye, deformed hands, extra fingers, fused fingers, missing fingers, extra limbs, malformed feet, extra toes, floating figure, no contact shadow, malformed ears, brand-new clothing, perfectly pressed, helmet hair, laser-straight hairline, blinding white teeth, heavy beauty retouching, seamless flat background, watermark, text, signature, border
```

====================================================================================================
## [img-character-sheet #10]  a851a88d  2026-09-07T01:29:51.046Z  len=2276
**USER:** The total charcters of the prompt are 10,000 make it that it will not exceeds to 10,000 charcters

**PRE:** …subtly mottled, gentle edge falloff, faint seam, softly defocused. Full-frame digital stills camera, neutral colour, accurate skin tone, very fine grain. Consistent facial identity in every frame.
```

### View 2 — three-quarter left (~30°)

```
Casting-sheet portrait, same individual across all frames: a 50-year-old Thai man, Isan / Lao-Thai heritage, NE Thailand, lifelong rice farmer. Dark sun-weathered brown skin, warm golden-brown undertone, slightly leathery over the cheekbones and forehead, light freckling, deep squint lines at the outer eyes, set forehead and nasolabial creases, crow's feet at rest, slackening jawline — clearly fifty, not younger. Natural skin texture, visible pores, faint shine on forehead and nose, no smoothing, soft translucency at the ear rims. Broad square-round face, wide cheekbones with hollows beneath, low broad nose bridge with a rounded tip, deep-set dark brown monolid eyes with a slight epicanthic fold, sparse low level brows, wide softening jaw, short blunt chin, medium-full lips with a thinner upper lip. Natural asymmetry — one eye smaller, brows uneven, mouth pulling slightly to one side. A dark raised mole low on the left jaw; a faint old scar through the left eyebrow. Black hair going salt-and-pepper, grey heaviest at the temples and sideburns, coarse thick straight home-cut short back-and-sides, crown cowlick, hat-flattened on top, a few flyaways. Sparse black-and-grey stubble, thin on the cheeks, denser at the chin. Lean wiry build, sinewy neck with visible tendons, weathered throat. Faded indigo short-sleeve cotton work shirt, soft washed collar, thin at the shoulders, one button missing, grey undershirt just visible at the neck. This view: face turned about 30 degrees to camera-left, far eye still fully visible, chin level, relaxed neutral with a faint closed-lip set, eyes to the lens. Head-and-shoulders crop, top of frame just above the hair, 4:5 vertical. 85mm lens, camera about 2 m away at eye level, f2.8, focus on the nearer eye, ears softening, no wide-angle distortion. Large soft key just left of the lens axis about 25 degrees and slightly above eye level, small loop nose-shadow, white bounce fill camera-right, low 2:1 ratio, open shadows, neutral 5600K, one catchlight at 10 o'clock. Light neutral-grey painted canvas backdrop set back, subtly mottled, gentle edge falloff, faint seam, softly defocused. Full-frame digital stills camera, neutral colour, accurate skin tone, very fine grain. Consistent facial identity in every frame.
```

====================================================================================================
## [img-character-sheet #11]  a851a88d  2026-09-07T01:29:51.046Z  len=2260
**USER:** The total charcters of the prompt are 10,000 make it that it will not exceeds to 10,000 charcters

**PRE:** …ubtly mottled, gentle edge falloff, faint seam, softly defocused. Full-frame digital stills camera, neutral colour, accurate skin tone, very fine grain. Consistent facial identity in every frame.
```

### View 3 — three-quarter right (~30°)

```
Casting-sheet portrait, same individual across all frames: a 50-year-old Thai man, Isan / Lao-Thai heritage, NE Thailand, lifelong rice farmer. Dark sun-weathered brown skin, warm golden-brown undertone, slightly leathery over the cheekbones and forehead, light freckling, deep squint lines at the outer eyes, set forehead and nasolabial creases, crow's feet at rest, slackening jawline — clearly fifty, not younger. Natural skin texture, visible pores, faint shine on forehead and nose, no smoothing, soft translucency at the ear rims. Broad square-round face, wide cheekbones with hollows beneath, low broad nose bridge with a rounded tip, deep-set dark brown monolid eyes with a slight epicanthic fold, sparse low level brows, wide softening jaw, short blunt chin, medium-full lips with a thinner upper lip. Natural asymmetry — one eye smaller, brows uneven, mouth pulling slightly to one side. A dark raised mole low on the left jaw; a faint old scar through the left eyebrow. Black hair going salt-and-pepper, grey heaviest at the temples and sideburns, coarse thick straight home-cut short back-and-sides, crown cowlick, hat-flattened on top, a few flyaways. Sparse black-and-grey stubble, thin on the cheeks, denser at the chin. Lean wiry build, sinewy neck with visible tendons, weathered throat. Faded indigo short-sleeve cotton work shirt, soft washed collar, thin at the shoulders, one button missing, grey undershirt just visible at the neck. This view: face turned about 30 degrees to camera-right, far eye still fully visible, chin level, relaxed neutral expression, eyes to the lens. Head-and-shoulders crop, top of frame just above the hair, 4:5 vertical. 85mm lens, camera about 2 m away at eye level, f2.8, focus on the nearer eye, ears softening, no wide-angle distortion. Large soft key just left of the lens axis about 25 degrees and slightly above eye level, small loop nose-shadow, white bounce fill camera-right, low 2:1 ratio, open shadows, neutral 5600K, one catchlight at 10 o'clock. Light neutral-grey painted canvas backdrop set back, subtly mottled, gentle edge falloff, faint seam, softly defocused. Full-frame digital stills camera, neutral colour, accurate skin tone, very fine grain. Consistent facial identity in every frame.
```

====================================================================================================
## [img-character-sheet #12]  a851a88d  2026-09-07T01:41:51.536Z  len=3184
**USER:** my problem here if I generate it per block is the inconsistent output of the character. Is possbile the these blocke are generated in generations and layout it as a tile?

**PRE:** …tail. Workflow is: get one consistent sheet → crop each tile → upscale / light img2img each one individually to full res afterward.

Here's the six-view sheet as one prompt (your 4 head views + full-body front + back, 3-wide × 2-tall grid):

```
Character reference sheet of one man, six views in a single image, laid out as a 3-wide by 2-tall grid of equal cells with thin clean white gutters, plain studio character-sheet style, the same individual and the same face in every cell.

Character: a 50-year-old Thai man, Isan / Lao-Thai heritage, NE Thailand, lifelong rice farmer. Dark sun-weathered brown skin, warm golden-brown undertone, slightly leathery over the cheekbones and forehead, light freckling, deep squint lines at the outer eyes, set forehead and nasolabial creases, crow's feet at rest, slackening jawline — clearly fifty, not younger. Natural skin texture, visible pores, faint shine on the forehead and nose, no smoothing. Broad square-round face, wide cheekbones with hollows beneath, low broad nose bridge with a rounded tip, deep-set dark brown monolid eyes with a slight epicanthic fold, sparse low level brows, wide softening jaw, short blunt chin, medium-full lips with a thinner upper lip. Natural asymmetry — one eye smaller, brows uneven, mouth pulling slightly to one side. A dark raised mole low on the left jaw; a faint old scar through the left eyebrow. Black hair going salt-and-pepper, grey heaviest at the temples and sideburns, coarse thick straight home-cut short back-and-sides, crown cowlick, a few flyaways. Sparse black-and-grey stubble, thin on the cheeks, denser at the chin. Lean wiry build, narrow shoulders, sinewy neck and forearms with visible tendons and raised veins, knotted knuckles, thin chest, a slight forward stoop. Faded indigo short-sleeve cotton work shirt, soft washed collar, thin at the shoulders, one button missing, grey undershirt at the neck; loose faded dark cotton work trousers rolled once at the ankle; well-worn rubber sandals, feet weathered.

Cells, left to right then top to bottom:
1 — head and shoulders, face square to camera, chin level, relaxed neutral expression, eyes down the lens.
2 — head and shoulders, face turned about 30 degrees to camera-left, far eye visible, faint closed-lip set, eyes to the lens.
3 — head and shoulders, face turned about 30 degrees to camera-right, far eye visible, relaxed neutral, eyes to the lens.
4 — head and shoulders, full left profile, head turned 90 degrees, gaze level to the far side, ear fully visible.
5 — full-length standing figure, front, weight even on both feet, arms relaxed at the sides, hands open and fully visible, relaxed neutral.
6 — full-length standing figure, back view, arms relaxed at the sides, showing the back of the head, shoulders and posture.

All cells share: soft even frontal key just left of the lens axis, white bounce fill camera-right, low 2:1 ratio, open shadows, neutral 5600K; a plain light neutral-grey seamless studio backdrop, subtly mottled, gentle edge falloff; an 85mm look on the head cells and a 50mm look on the full-length cells, natural facial proportions, no wide-angle distortion; focus on the near eye for head cells, the whole figure sharp for full-length cells. Full-frame digital stills camera, neutral colour, accurate skin tone, very fine grain. Consistent facial identity, hair, marks, wardrobe and body proportions across all six cells. 3:2 landscape.
```

====================================================================================================
## [img-character-sheet #13]  9ce085df  2026-09-07T03:41:38.654Z  len=439
**USER:** Base directory for this skill: /Users/leo/Desktop/Neutra DC/Image to Video/.claude/skills/realist-portrait

# Realist Character Portrait — prompt builder

Turns a character idea, a reference photo, or a "I need a consistent character" request into a paste-ready **still-portrait** prompt that reads a

**PRE:** …exa 35 finished on film, Kodak Portra warm highlight roll-off, fine grain in mid-tones and shadows, soft warm halation, faint haze, 16:9. Genuine candid, unposed, unaware of the camera.
```

**Negative (if the model has a negative field):**

```
plastic or waxy skin, airbrushed, over-smoothed, poreless, generic AI face, symmetrical doll face, 3d render, CGI, illustration, digital painting, overprocessed, deep focus with everything sharp, wide-angle distortion, helmet-smooth hair with no stray strands, brand-new stiff clothing, front view, face fully visible, looking at camera, posed, stiff, staged, flat HDR lighting, cool blue cast, oversaturated, neon, text, watermark, border
```
