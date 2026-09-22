# PROMPT-STRUCTURES.md — the shape of every prompt this pipeline writes

Distilled from the AI Production kit in `libraries/` (Seedance Feature Pipeline Phase 0–9,
Seedance Prompt Architecture, the Higgsfield formats, the Prompt Archive, the realist
portrait skill, and the worked example). Read the library file when a structure here is
not enough. Never work from memory when the library is one file away.

Three rules apply to every prompt below (the kit's three bans, adapted):

1. **No names in prompt text.** No director, film, DP, camera body, lens model, film stock.
   Decide the look with the libraries; write it as something you can see. The translation
   table is in `libraries/Seedance-Feature-Pipeline.md` §BAN 1.
2. **No character-count trimming on Seedance.** Budget by block necessity. Kling keeps the
   1500-character combined cap because that is where it fails.
3. **GPT Image 2 has no negative field.** Every exclusion is written as a positive state.

Handles: `@doctor` in the plan and the card. In a prompt that attaches references, the
handle becomes "Image 1 is the doctor" (GPT Image 2) or stays `@doctor` (Seedance, where
the workspace has an elements panel; if it does not, write the name in words).

---

## 1. Character sheet (GPT Image 2 · 3:2 six-panel, or 16:9 three-panel · 1K high)

Source: `libraries/realist-portrait-SKILL.md` Mode C, `libraries/Prompt-Archive/character-sheet.md`
#12, `libraries/worked-example/canvas/characters/@nia/prompt.md`.

One prose block. Order matters. Every line is load-bearing.

```
Character reference sheet of one [woman/man], photographed in a single continuous studio
session, laid out as a [3:2 sheet of six panels in a 3-wide by 2-tall grid | 16:9 sheet of
three panels side by side] separated by thin clean gaps; the sheet carries no lettering.
The same individual in every panel, consistent facial identity across all frames:

[IDENTITY]  a [age]-year-old [woman/man] of [concrete heritage], [skin tone with undertone],
[age markers: lines, creases, texture]; [face geometry: shape, nose, eyes, brows, chin,
lips]; [distinguishing marks, each with "her own left / his own right"]; [hair: colour,
texture, cut, flyaways]; [build]; [facial hair or makeup]. Visible pores, natural asymmetry
between the eyes and brows, subsurface warmth in the ears.

[WARDROBE, one state]  [garment: fabric, fit, condition] over [garment], [trousers],
[shoes], [carried item on which shoulder or hand]. Fabric reads real: [one wear detail].

[PANELS]  Panel 1: head and shoulders, front, neutral relaxed expression, eyes to lens.
Panel 2: head and shoulders, three-quarter left, [a small expression]. Panel 3: full body
front, arms relaxed, hands open and fully visible. Panel 4: full body back view. [Panel 5
and 6: the same in wardrobe B, only if the plan says the sheet carries two wardrobes.]

[CAMERA AS DESCRIPTION]  Camera at eye height for the portrait panels, chest height for the
full-body panels, 29-degree field of view, focus on the near eye in the portrait panels.

[BACKDROP + LIGHT]  Seamless mid-grey studio backdrop with a soft floor-to-wall falloff and
a faint scuff near the floor line. Large soft key from camera-left, gentle fill, 4:1
key-to-fill ratio, one soft catchlight at ten o'clock, neutral 5200K white balance.

[LOOK]  [the locked Look as observable description, e.g. "Warm colour-negative film
character: soft warm highlights that roll off gently, fine even grain in the midtones and
shadows, forgiving mid-contrast, slightly lifted blacks."]
```

Rules:
- Grey. Grey tested better than white or black for video reference.
- Face view plus full-body front and back in one generation, so the model never guesses.
- One state per sheet. `_wet`, `_wound`, `_coat_off` are separate sheets.
- Family or relational likeness is stated feature by feature, never "looks like her son".
- Name the side as the subject's own left or right, so a mole does not swap panels.

---

## 2. Environment sheet (GPT Image 2 · job aspect · 1K high)

Source: `libraries/worked-example/canvas/locations/@loc_apartment/prompt.md`, the P-02
location plate template in the kit's presentation, `libraries/Prompt-Archive/location-env.md` #19.

```
Wide three-quarter-angle photograph of an empty [place], taken from [the inner corner |
the doorway | the far end] looking diagonally toward [the main wall or feature], camera at
[standing | seated] eye height, camera about 45 degrees to the main wall so two walls and
the floor plane read clearly, [84 | 63]-degree field of view.

[ANCHORS]  [One or two anchor objects, exact, placed left or right from the camera: "a green
enamel pendant lamp over the bench, camera-right", "the double slipway doors, camera-left".]

[LAYERS]  Foreground: [surface, material, one worn detail]. Midground: [furniture or
structures, materials, finish]. Background: [walls, openings, what is seen through them].

[LIGHT]  [Source] from [side], [quality], [Kelvin] white balance, [shadow character].
[Air: dust, haze in %, still or moving.]

[PALETTE]  [60/30/10 line with hex from the ground rules, as material plus light:
"cream plaster #F3E3C3 warmed by the window light, honey-oak floor, one red accent
#B8322A on the water tower through the glass".]

The room is empty: no people, no animals. The place carries no readable lettering or brand
marks. [LOOK as observable description.]
```

Rules:
- Three-quarter, never frontal. Frontal plates break more often when animated.
- Anchor objects make the place read as the same place from every later angle.
- Empty. The scene still adds the people.

---

## 3. Element sheet (GPT Image 2 · 1:1 · 1K high)

Source: the P-02 prop template, `libraries/Prompt-Archive/element-product.md` #1 (light
element), `libraries/worked-example/canvas/props/`.

Prop or product:

```
Photorealistic three-quarter overhead product shot of [the object] on a neutral grey
concrete surface, soft directional lighting from camera-left, isolated subject, nothing
else in frame. [Size in cm]. [Materials, one by one]. [Wear and condition]. [Colour as
material plus light, hex where locked]. Plain unbranded surfaces, blank matte finish where
a label would be. [LOOK as observable description.]
```

Light element or VFX element:

```
Isolated light element, studio asset, floating alone on a flat seamless matte black field:
no environment, no ground, no horizon, pure black behind the light. [Strand count and
material: "many fine red #E4002B filaments braided into one coherent rope"]. [Core: "a
dense smooth white-hot core near the centre"]. [Ends: "looser separated strands studded
with sparse white-hot beads trailing toward each end"]. [Path: "one gentle wave-like bend,
not a tight S"]. No visible source object, vehicle or emitter: pure self-luminous light.
Sharp edges against black, suitable for compositing. Red and white are the only colours
present.
```

Rules:
- Unbranded on the sheet even if the brief names a brand. Name it in words in the scene.
- Name the object in words in every later prompt too; the model drops small detail that
  exists only in the image.

---

## 4. Scene still (GPT Image 2 · job aspect · 2K high · up to 10 references)

Source: `libraries/Prompt-Archive/element-product.md` #2 and #3 (role-scoped references),
`libraries/worked-example/shots/SHOT-001/storyboard.md` (the REFERENCES block), the FIRST
FRAME / BLOCKING and LOCATION MAP blocks of the sealed prompt.

```
[ONE-LINE SCENE CONTEXT]  A photographic film still, [aspect], of one instant: [who, where,
doing what, in one sentence].

REFERENCES
Image 1 is [character]. It controls [face, hair, marks, wardrobe]. Ignore [its grey backdrop
and panel layout].
Image 2 is [environment]. It controls [the room, the anchors, the light direction]. Ignore
[its emptiness].
Image 3 is [element]. It controls [the object's identity and size]. Ignore [its surface].
Image 4 is the last frame of the previous scene. It controls [positions, states such as
wetness, what is held]. Ignore [its framing].            ← cut mode, scene 02+

LOCATION MAP
Foreground: [...]. Midground: [...]. Background: [...]. The camera is [where, relative to
an anchor], at [height]. [Light source] enters from [side].

FIRST FRAME / BLOCKING
[Person A] [where in frame, which third], [facing which way], [distance to the camera in
metres], [gaze], [hands]. [Person B] [...]. [Object] [where]. Left and right are from the
camera.

OPTICS
[Framing term as description: "wide shot easing to medium" is a video term; a still says
"medium shot, waist up"], [FOV]-degree field of view, rectilinear, [focus: which layer is
sharp, which soft].

LIGHT
[Restate the environment sheet's light: source, side, Kelvin, shadow character.] Exposure
set for [the subject].

PALETTE AND LOOK
[Hex line as material plus light.] [LOOK as observable description.]

LOCKS
Exactly [n] people in frame. [Every forbidden-list item as a positive state: "shop fronts
and papers carry no readable lettering", "the only legible character is the numeral 7 on
the bus".] [Identity locks per person: "the doctor keeps the wire glasses and the mole
under his own left eye".]
```

Rules:
- One reference per element that must stay consistent. Attach only the handles in this
  scene's tag set. A cluttered set is less coherent than a small chosen one.
- Role-scope each attachment: what it controls and what to ignore, or the model inherits
  the grey backdrop and the panel gutters.
- The still is an instant, not an action. Write the opening frame.

---

## 5. The scene card (main agent writes; internal; never sent to a model)

Source: `libraries/Seedance-Feature-Pipeline.md` Phase 3, `libraries/director-dp.md`,
`libraries/worked-example/shots/SHOT-001/card.md`.

```
SCENE 01  ·  [place, time]  ·  [oner | sequential | timed]  ·  6 s  ·  [cut | continuation]

TAGS PRESENT      @doctor, @old_lady, @clinic, @xray_film       (nothing else)
MOTION  locked    [rigid elements: walls, desk, window, the monitor image]
        moves     [lead] → [supporting] → [ambient]
        decided   [each ambiguous element and the call made on it]
BRIEF   intent    [what this scene is doing dramatically]
        camera    [what the move accomplishes, or "static, witnesses"]
        pace      [constant | accelerating | decelerating | held-then-moves]
LOOK    movement  [Camera-Movements-Library name — internal only]
        framing   [Camera-Framing-Angle-Library term — internal only]
        lens      [Lens library name] → FOV [one of 180 / 107 / 84 / 63 / 47 / 29 / 18 / 12 / 8]
        focus     [Depth-of-Field-Library term — internal only]
        capture   [Camera-Look-Library term — internal only]
        look+stance  [the locked pair from ground-rules.md]
BLOCKING start    [who is where at frame one, left/right from camera, distances, gaze]
ARRIVAL   end     [who is where at the last frame; this is what the end frame edit changes]
DIALOGUE          @old_lady — "[line]" — exactly [n] words ([from]–[to] s)   or   none, silence intentional
AUDIO             [ambience bed, foreground foley]. No music.
```

FOV table (degrees only in prompts; the mm column is for choosing):

| FOV | ≈ mm | Use |
|---|---|---|
| 180° | fisheye | POV, dream state |
| 107° | 14–16 | huge interiors, epic establish |
| 84° | 20–24 | establish, group blocking |
| 63° | 28–35 | observation, reportage |
| 47° | 40–50 | neutral human perspective |
| 29° | 75–85 | dialogue bust, medium isolate |
| 18° | 100–135 | close portrait, identity-preserving |
| 12° | 180–200 | hands, objects, detail |
| 8° | 300–400 | extreme compression |

"23°" rounds to 18° or 29°. Never an off-table value.

---

## 6. Video prompt

### 6.1 Seedance 2.5 (sealed prompt, both frames attached)

Source: `libraries/Seedance-Prompt-Architecture.md` (§2 block order, §5 optics, §8 rules,
§10 pre-flight), `libraries/worked-example/shots/SHOT-001/prompt.md`,
`libraries/Sources/higgsfield-seedance-clean-SKILL.md`.

Block order. Use only the blocks the scene needs. Opens on SCENE CONTEXT, never a style
header. CAMERA third among the core layers.

```
SCENE CONTEXT
[Time, place, who, what happens across the clip, in three sentences.]

ACTIVE REFERENCES
@doctor: [age + role/build + current state + unique visible features + action-critical
details + voice if he speaks]. 100% matches the reference.
@clinic: controls the room, the window on camera-left and the light direction.
@xray_film: [size, what is on it].

LOCATION MAP
Foreground: [...]. Midground: [...]. Background: [...]. The camera is [where] at [height].
[Light] enters from [side].

FIRST FRAME / BLOCKING
Matches the attached start frame exactly: [restate the blocking in one or two sentences].

FORMAT MODE
One continuous shot; the camera does not cut on its own.    (or the timed multishot form
with FOV per segment and "no drift mid-segment")

OPTICS
[Shot size], [FOV]-degree field of view throughout, rectilinear, no drift in field of view.
[Focus layering.]

CAMERA
[Position relative to an anchor, height, side of the subject]. [The move as an observed
result with a speed in km/h or a distance in metres over the full duration, or "static,
locked"]. No shake. [Tonal character as description.]

ACTION
Camera: [the move above, continuous from 0.0 s to 6.0 s].
0.0–2.0 s — [beat, measured].
2.0–4.0 s — [beat].
4.0–6.0 s — [beat]. The final frame matches the attached end frame exactly.

PERFORMANCE
[Muscle movement, not emotion labels: "jaw tight, eyes fixed on the film, a slow blink".]

PHYSICS
[What cloth, hair, dust, liquids, light do; masses have weight.]

LIGHTING
[Source, side, quality, Kelvin, exposure set for whom, how much brighter the window is.]

AUDIO
[Ambience bed with timed foley.] Between [a] s and [b] s @old_lady speaks exactly [n]
words, clearly, in English: "[line]". Then no more speech. No music, no score, no
narration, no other voices.       (or: The clip is silent by design apart from [ambience];
no speech at all.)

STYLE
Photoreal live-action. [LOOK as observable description.] No readable text or logos
anywhere, no subtitles, [palette exclusions from the ground rules].

OUTPUT SETTINGS
[aspect], [resolution], 24 fps, real-time throughout, [n] seconds.

POSITIVE LOCKS
Exactly [n] people. [Identity locks per person, sides stated.] [Rigid elements stay rigid.]
[Screen direction.] [The forbidden list as positive states.]
```

Pre-flight before saving (from the architecture file §10):
blocks in order · tags only for present objects · no style prefix at the top · everything
positive except STYLE and AUDIO exclusions · speeds in km/h, atmosphere in % and metres ·
emotion as muscle movement · left/right from the camera · FOV in degrees from the table ·
CAMERA third · white balance in Kelvin · colour as material plus light · dialogue word
count stated as a lock · no banned name anywhere · no block cut to hit a number.

### 6.2 Kling (positive + negative, ≤ 1500 characters combined)

Source: `libraries/Prompt-Archive/video-single.md`, the reference-image pipeline's Stage 4.

```
[Camera move as a result the viewer sees, with pace]. [Lead motion, measured]. [Supporting
motion]. [Ambient motion]. [Rigid elements stay rigid: "the walls, desk and window stay
rigid and unwarped, parallax only"]. [Light and palette in one line, hex]. [Look in one
line]. [aspect]. No legible text, logos or signage.

Negative: [only what this shot tends to get wrong: "camera cutting on its own, extra
people, warped hands, lettering resolving on the film, whole-frame red cast, CGI look"]
```

Camera-led shots go to Seedance. Element-led shots are where Kling earns a run.

---

## 7. Where to look when a structure is not enough

| Question | File |
|---|---|
| How to decide the look before writing | `libraries/Photography-Styles-Library.md`, `libraries/Camera-Look-Library.md`, `libraries/Film-Director-Library.md` (names stop on the card) |
| Which camera move | `libraries/Camera-Movements-Library.md`, `libraries/FPV-Drone-Movements-Library.md` |
| Framing and angle terms | `libraries/Camera-Framing-Angle-Library.md` |
| Focus treatment | `libraries/Depth-of-Field-Library.md` |
| Lens character to describe | `libraries/Lenses/` |
| Matching one scene's end to the next scene's start | `libraries/Transition-Library.md` |
| A person's face, consistent | `libraries/realist-portrait-SKILL.md` |
| The director's brief method | `libraries/director-dp.md` |
| Real prompts that shipped, by type | `libraries/Prompt-Archive/*.md`, `libraries/Compiled-Prompts-By-Format.md` |
| A whole worked production | `libraries/worked-example/` |
| The full process the kit was written for | `libraries/Seedance-Feature-Pipeline.md` |
