# Camera Movements Library

81 camera movements, organized by category. Each entry gives a paste-ready phrase for the `[Camera movement]` slot in the per-shot prompt template (see [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md)). Works across Kling, Seedance, and similar image-to-video tools — none of the movements below are model-exclusive.

These are moves *over time*. For the static camera position they move away from — height/angle, shot size/framing, lens/perspective — see the companion [Camera-Framing-Angle-Library.md](Camera-Framing-Angle-Library.md).

Source: extracted and organized from [aicameramovements.com](https://aicameramovements.com/) (original 46) and [higgsfield.ai/camera-controls](https://higgsfield.ai/camera-controls) (35 additions — presets not covered by the first source; aliases like Higgsfield's "360 Orbit" or "Dolly Left/Right" for moves already in the library were skipped rather than duplicated).

---

## Pan / Tilt

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Static Shot | `Hold one fixed camera position for the full clip.` | Use when the subject/environment should carry all the motion |
| Pan Right | `Camera pans smoothly right, rotating horizontally while keeping the horizon level.` | Constant speed |
| Pan Left | `Camera pans smoothly left, rotating horizontally while keeping the horizon level.` | Constant speed |
| Whip Pan Right | `Camera whip-pans rapidly to the right toward the new target, with motion blur.` | Fast, use for hard cuts/reveals |
| Whip Pan Left | `Camera whip-pans rapidly to the left toward the new target, with motion blur.` | Fast, use for hard cuts/reveals |
| Tilt Up | `Camera tilts upward from a fixed point, keeping vertical subjects centered as the frame rises.` | Good for reveals of height (buildings, towers) |
| Tilt Down | `Camera tilts downward from a fixed point, keeping vertical subjects centered as the frame descends.` | Good for grounding a reveal |

## Zoom / Lens

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Slow Zoom In | `Lens slowly zooms in, gradually tightening the frame.` | Even, gradual |
| Slow Zoom Out | `Lens slowly zooms out, gradually widening the frame.` | Even, gradual |
| Fast Zoom In | `Lens zooms in quickly toward the main subject.` | Decisive, not punchy |
| Fast Zoom Out | `Lens zooms out quickly away from the main subject.` | Decisive, not punchy |
| Crash Zoom In | `Lens snaps into a rapid crash zoom toward the main subject.` | Very fast, punchy — use sparingly |
| Crash Zoom Out | `Lens snaps into a rapid crash zoom away from the main subject.` | Very fast, punchy — use sparingly |
| Dolly Zoom In | `Camera dollies forward while the lens zooms out at a matched rate, holding the subject's size steady as the background stretches and warps around them.` | Vertigo/Hitchcock effect — disorienting, use sparingly |
| Dolly Zoom Out | `Camera dollies backward while the lens zooms in at a matched rate, holding the subject's size steady as the background compresses toward them.` | Reverse vertigo effect |
| YoYo Zoom | `Lens zooms in and out in a repeating pulse, tightening and loosening the frame rhythmically without the camera moving.` | Stylized, energetic — good for hooks/highlights |

## Dolly / Track

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Dolly In | `Camera dollies straight forward toward the main subject, smooth and controlled, tightening the composition.` | The default "push-in" |
| Dolly Out | `Camera dollies straight backward away from the main subject, smooth and controlled.` | The default "pull-out" |
| Tracking Shot | `Camera tracks alongside the subject, moving through the scene at the subject's pace, keeping them readable as the environment moves past.` | General follow |
| Follow Shot / Over-the-Shoulder | `Camera follows behind the subject at shoulder height, matching their pace along the route.` | Classic follow-cam |
| Reverse Tracking / Walk-and-Talk | `Camera moves backward in front of the walking subject, keeping a stable front-facing composition.` | Interview/dialogue framing |
| Side Tracking | `Camera moves parallel beside the subject along their direction of travel, holding a three-quarter profile.` | Good for walking/running subjects |
| Low Tracking | `Camera tracks at ground or below-waist height alongside the subject's movement.` | Dramatic, dynamic low angle |
| Vehicle Tracking | `Camera tracks alongside the moving vehicle, matching its pace and keeping it stable in frame.` | For car/product-in-motion shots |
| Chase Shot | `Camera chases the moving subject quickly and closely along the action route.` | Fast, reactive, handheld-adjacent |
| Super Dolly In | `Camera dollies forward at a heightened, dramatic speed, pushing hard toward the subject with exaggerated perspective shift.` | Intensified Dolly In — use for high-impact moments |
| Super Dolly Out | `Camera dollies backward at a heightened, dramatic speed, pulling hard away from the subject with exaggerated perspective shift.` | Intensified Dolly Out |
| Double Dolly | `Camera dollies in and then back out (or out then in) in one continuous two-stage move.` | Punctuates a beat — use for a single emphasized moment mid-clip |

## Physical Moves

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Truck Right | `Camera trucks right, moving physically along a straight horizontal path.` | Lateral, no rotation |
| Truck Left | `Camera trucks left, moving physically along a straight horizontal path.` | Lateral, no rotation |
| Pedestal Up | `Camera pedestals straight up, lens level and pointed in the same direction throughout.` | Vertical lift, no tilt |
| Pedestal Down | `Camera pedestals straight down, lens level and pointed in the same direction throughout.` | Vertical descent, no tilt |
| Slider Right | `Camera slides a small distance to the right, slow and controlled, revealing parallax between foreground and background layers.` | Subtle — good for product/still-life |
| Slider Left | `Camera slides a small distance to the left, slow and controlled, revealing parallax between foreground and background layers.` | Subtle — good for product/still-life |
| Push Past / Pass-by Shot | `Camera glides forward past a foreground object or opening, arriving inside or beyond it.` | Great for doorway/archway transitions |
| Arc Right | `Camera arcs smoothly on a shallow curved path around the subject toward the right.` | Softer than a full orbit |
| Arc Left | `Camera arcs smoothly on a shallow curved path around the subject toward the left.` | Softer than a full orbit |
| Orbit Clockwise | `Camera orbits clockwise around the subject at a consistent radius.` | Full 360-capable, product/hero shots |
| Orbit Counterclockwise | `Camera orbits counterclockwise around the subject at a consistent radius.` | Full 360-capable, product/hero shots |
| 3D Rotation | `Camera rotates freely around the subject across multiple axes at once, not just horizontally, for a full dimensional turntable view.` | More complex than a flat Orbit — needs a clean subject with room on all sides |
| Lazy Susan | `Camera holds a fixed distance and glides in a slow, even rotation around the subject, like it's turning on a turntable.` | Gentler, slower cousin of Orbit — good for product/portrait beauty shots |
| Incline Track | `Camera moves along a diagonal path, rising or descending at an angle rather than a straight vertical or horizontal line.` | Use when the scene itself has a diagonal line (stairs, slopes, ramps) to travel along |

## Human Camera

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Handheld Shot | `Handheld camera at human operator height, with natural body movement — subtle sway and micro-adjustments.` | Adds authenticity, anti-generic |
| Body-mounted Camera / Snorricam | `Camera fixed relative to the subject's torso, staying close and centered on their face while the background moves behind them.` | Distinctive, disorienting effect |
| Head Tracking | `Camera locks onto the subject's head, following and keeping their face centered and level as they move.` | Keeps face framed through motion — good for walk-and-talk/vlog style |
| Wiggle | `Handheld camera adds a subtle, rhythmic side-to-side wiggle while holding the subject in frame.` | More stylized/playful than plain Handheld |
| Robo Arm | `Camera moves along a precise, mechanical path with swift, exact sweeps and none of handheld's organic drift.` | Opposite feel from Handheld — precise, robotic |

## Drone / Crane

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Crane Up | `Camera cranes smoothly upward through open space, slow and controlled.` | Vertical reveal, wider than pedestal |
| Crane Down | `Camera cranes smoothly downward through open space, slow and controlled.` | Vertical descent, wider than pedestal |
| Crane Over The Head | `Camera cranes up from eye level and arcs forward over the subject's head, ending in a high overhead vantage.` | Combines a lift with a reveal — dramatic transition move |
| Drone Push In | `Drone flies smoothly forward through open space toward the subject or destination.` | Aerial approach |
| Drone Pull Back | `Drone flies smoothly backward away from the subject or destination.` | Aerial reveal/retreat |
| FPV Drone | `Drone flies fast and low through the scene in tight, racing-style FPV movement, banking and diving around obstacles.` | High-energy aerial, distinct from the smoother Drone Push In |
| Flying Cam Transition | `Camera flies rapidly through the scene as a transition, sweeping from the current subject or location straight into the next.` | Scene-to-scene transition device |
| Helicopter Shot | `Camera moves from high altitude along a broad, gradual flight path, steady and wide.` | Landscape/establishing scale |

## Specials

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| First-Person View | `First-person camera moves forward at human eye height, natural walking pace, with visible hands/body edges as reference.` | POV shots |
| Object POV | `Camera adopts the point of view of an object in the scene, moving as if seen through that object's perspective.` | Distinct from First-Person View, which is human-eye height |
| Tilt-Shift | `High angled glide over the scene with a narrow band of sharp focus and soft blur above and below, creating a miniature look.` | Stylized "toy world" effect |
| Infinite Zoom | `Camera zooms continuously and smoothly inward, accelerating toward the center target until the next visual world fills the frame.` | Needs a matched second image/scene at the zoom target |
| Earth Zoom Out | `Camera pulls rapidly upward from the starting point, expanding out through street, city, landscape, and planet scale.` | Needs multiple layered reference images to sell the scale jump |
| Time-Lapse | `Hold one fixed camera position while time moves rapidly forward.` | Pair with visible time cues (light change, moving clouds, crowds) |
| Hyperlapse | `Camera physically moves through the scene while time advances rapidly, combining a traveling shot with time-lapse acceleration.` | Distinct from Time-Lapse, which holds one fixed position |
| Pass-Through Objects | `Camera glides smoothly forward, centered, toward a visible object or barrier and continues into the space beyond it.` | Portal/transition device |
| Through Object Out | `Camera pulls back from inside or behind an object or barrier, widening to reveal it from the outside.` | Reverse-direction complement to Pass-Through Objects |
| Bullet Time | `Camera orbits rapidly around a frozen or slow-motion subject while time appears to stop.` | Matrix-style VFX beat — use sparingly, needs a clear subject |
| Eyes In | `Lens pushes in tight until only the subject's eyes fill the frame.` | Extreme close-up, isolates the gaze |
| Mouth In | `Lens pushes in tight until only the subject's mouth fills the frame.` | Extreme close-up — food/beauty/dialogue emphasis |
| Overhead | `Camera looks straight down at the subject from directly above.` | Bird's-eye framing — flat lay/top-down product or crowd shots |
| Fisheye | `Lens applies a fisheye distortion, bowing straight lines outward from the center of frame.` | Exaggerated wide-angle, stylized look |
| Dutch Angle | `Camera frame is tilted off the horizontal axis, canting the horizon.` | Disorienting/tense feel — use sparingly |
| Focus Change | `Focus racks from one plane to another while the camera position holds, pulling attention to the new focal point.` | Classic rack focus — needs two distinct depth planes in the reference |
| Low Shutter | `Camera shoots with a slowed shutter speed, adding pronounced motion blur and trails to anything moving in frame.` | Dreamy/gritty motion-blur look |

## Vehicle & Lifestyle Presets

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Car Grip | `Camera is rigged directly to the exterior of the moving car — hood, door, or bumper mount — riding along at car height and speed.` | Rig-mounted, distinct from the smoother Vehicle Tracking |
| Buckle Up | `Camera sits inside the vehicle at passenger POV, framing the interior and the road ahead through the windshield.` | Interior car POV |
| Road Rush | `Camera tracks low and fast alongside or just behind a moving vehicle, emphasizing speed and momentum.` | Faster, lower, more energetic variant of Vehicle Tracking |
| BTS (Behind-the-Scenes) | `Camera holds a documentary, behind-the-scenes feel — informal handheld framing that includes crew, rigs, or set edges alongside the subject.` | Adds a "how it's made" authenticity layer |
| Hero Cam | `Camera holds a low, slightly upward angle on the subject with soft dramatic light, framing them as the hero of the shot.` | Flattering, elevated-status portrait framing |
| Eating Zoom | `Lens pushes in close on the food as the subject eats, timed to each bite.` | Food-content close-up |
| Glam | `Camera holds a flattering close or medium beauty framing with a slow, subtle push or drift.` | Tuned for glamour/portrait content |
| Timelapse Glam | `Time-lapse of a styling or beauty transformation — hair, makeup, or outfit change — compressed into rapid motion while the camera holds on the subject.` | Needs reference stages of the transformation to sell the change |
| Timelapse Human | `Time-lapse centered on a person, compressing their movement or changes over time while the camera holds a steady frame.` | Person-centered variant of Time-Lapse |

---

## Movement Selector (auto-suggest from a reference photo)

Hand a reference photo to Claude in chat and ask it to suggest a movement — it reads the image directly and walks this decision order. No separate tool needed.

### 1. Subject category → default movement family

| What's in the photo | Default family | Lead candidates |
|---|---|---|
| Building / real estate / architecture exterior | Dolly / Track, Drone / Crane | Dolly In, Crane Up, Truck Right/Left, Push Past |
| Product / still-life on a surface | Physical Moves | Orbit CW/CCW, Arc Right/Left, Slider Right/Left |
| Portrait, close-up face | Pan / Tilt, Human Camera | Static Shot, Slow Zoom In, Handheld Shot |
| Person, full body, walking/moving | Dolly / Track | Tracking Shot, Side Tracking, Reverse Tracking, Follow Shot |
| Vehicle | Dolly / Track | Vehicle Tracking, Chase Shot, Side Tracking |
| Landscape / wide establishing scene | Drone / Crane | Helicopter Shot, Drone Push In, Crane Up |
| Food / tabletop | Physical Moves | Orbit CW/CCW, Arc Right/Left, Slow Zoom In |
| Interior with a doorway/archway/threshold in frame | Physical Moves | Push Past / Pass-by Shot |

### 2. Composition cues that override or refine the default

- **Strong foreground/background separation** (something close to lens, something distant) → favor **Slider Right/Left** or **Truck Right/Left** to sell parallax.
- **Leading lines / symmetric vanishing point / corridor** → favor **Dolly In** or **Drone Push In**.
- **Tall vertical subject** (tower, standing figure, waterfall) → favor **Tilt Up/Down**, **Crane Up/Down**, or **Pedestal Up/Down**.
- **Subject centered with clean negative space around it** → favor **Orbit** or **Arc** (needs room to travel without clipping the subject).
- **Busy/cluttered background** → pull back to **Static Shot** or **Slow Zoom In** — per Stage 2 of the pipeline, a busy frame makes any traveling move motion-heavy and messy.
- **High vantage point already in the shot** (aerial/rooftop reference) → **Helicopter Shot** or **Earth Zoom Out**.

### 3. Orientation check

- **Vertical / 9:16** → bias toward **Static Shot, Slow Zoom In/Out, Handheld Shot** — wide lateral moves (orbit, truck, drone flyover) read as cramped or disorienting in a tall frame.
- **Horizontal / 16:9** → full library is in play, including orbit/crane/drone families.

### 4. Mood cross-check (against the signature card)

- Calm / premium / commercial → Slow Zoom, Dolly, Orbit, Crane (smooth, controlled).
- Urgent / action / reveal → Whip Pan, Crash Zoom, Chase Shot (use sparingly, per their Notes column).

**Output format when suggesting:**

```text
Suggested: [movement name] — [paste-ready phrase]
Why: [1-2 visual cues from the photo that drove the pick]
Alternate: [movement name] — if primary reads too aggressive/subtle for the shot
```

This selector is a fast default, not a replacement for judgment — Stage 3's locked/moving classification of the *specific* reference image still overrides it (e.g. don't suggest Orbit around a subject whose background is tagged "locked, must not distort").

For the starting height/angle/framing/lens to pair with the suggested movement, see the equivalent selector table in [Camera-Framing-Angle-Library.md](Camera-Framing-Angle-Library.md#selector-cross-reference).

---

## Usage notes

- Drop the paste-ready phrase straight into the `[Camera movement]` slot of the per-shot prompt template in [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md).
- Per the pipeline's diagnose step: if the model ignores a stated move, restate it as an **observed result** rather than an instruction — e.g. instead of "camera tilts up," describe what the frame shows: *"the horizon drops from center-frame to the bottom edge as the building's full height comes into view."*
- Kling's Pro mode exposes explicit pan/tilt/zoom/roll percentage sliders — use these phrases as the text prompt and let the sliders reinforce the same direction, don't fight them against each other.
- For multi-shot sequences, pick one movement family per treatment (e.g. all dolly/track for an intimate story, all drone/crane for an establishing/epic feel) so the sequence reads as one coherent camera language — this is the "signature card" camera-language line from the main pipeline.
