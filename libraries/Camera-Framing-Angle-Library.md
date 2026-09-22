# Camera Framing & Angle Library

Companion to [Camera-Movements-Library.md](Camera-Movements-Library.md) — that library describes motion *over time* (what the camera does during the clip); this one describes a *static camera position/composition* (where the camera sits and what it sees at a given moment). Use it to spec the reference image itself, describe an existing reference precisely, or define the frame a camera move arrives at.

Source: vocabulary adapted from ["A Vocabulary for Camera Position, Angle, Framing, and Perspective for AI Image Generation"](https://idacooper.medium.com/a-vocabulary-for-camera-position-angle-framing-and-perspective-for-ai-image-generation-fcbd78478022) (Ida Cooper).

---

## Height / Vertical Position

| Term | Paste-ready phrase | Notes |
|---|---|---|
| High Angle | `Camera positioned above the subject, looking down.` | Diminishes/surveys the subject |
| Low Angle | `Camera positioned below the subject, looking up, making the subject appear dominant and powerful.` | Adds power/scale |
| Eye Level | `Camera at the subject's eye level, neutral human perspective.` | Default, non-editorializing |
| Chest Level | `Camera slightly below eye level, at chest height, for an intimate mid-shot feel.` | Softer than straight eye-level |
| Ground Level | `Camera positioned at or near ground level, looking across or slightly up.` | Grounded, environmental |
| Ultra Low Angle / Worm's Eye | `Camera at extreme ground level looking almost straight up, exaggerating the subject's height and scale.` | Extreme — use deliberately |
| Overhead / Top-Down | `Camera directly above the subject, looking straight down at a 90-degree angle.` | Flat-lay/map-like read |

## Distance / Framing (Shot Size)

| Term | Paste-ready phrase | Notes |
|---|---|---|
| Extreme Close-Up (ECU) | `Extreme close-up framing, tight on eyes, mouth, or fine surface texture.` | Detail/texture emphasis |
| Close-Up (CU) | `Close-up framing on the head and neck.` | Emotional read |
| Medium Close-Up (MCU) | `Medium close-up framing from the shoulders to the top of the head.` | Standard talking-head |
| Medium Shot (MS) | `Medium shot framing from the waist up.` | General conversational default |
| Medium Wide Shot (MWS) | `Medium wide shot framing from the knees up.` | Body language visible |
| Wide Shot (WS) | `Wide shot framing the subject's full body within the environment.` | Subject + context balanced |
| Long Shot | `Long shot with the subject small within the frame.` | Environment starts to dominate |
| Extreme Long Shot (ELS) | `Extreme long shot dominated by environment, subject tiny in frame.` | Scale/isolation |
| Establishing Shot | `Establishing shot emphasizing context, architecture, and the space itself over the subject.` | Opening/orientation shot |

## Orientation / Angle

| Term | Paste-ready phrase | Notes |
|---|---|---|
| Straight-On | `Camera faces the subject straight-on, neutral orientation.` | Default, confrontational if close |
| Three-Quarter Angle | `Camera angled roughly 45 degrees from the subject's front.` | Most flattering default for portraits/products |
| Profile / Side-View | `Camera positioned at a full 90-degree side profile to the subject.` | Graphic, silhouette-friendly |
| Back-View / Rear Angle | `Camera positioned behind the subject, facing the same direction they are.` | Anonymity, mystery, POV setup |
| Dutch Angle / Tilt | `Camera rotated off the horizon line, tilted for tension and unease.` | Use sparingly — signals disorientation |
| Top-Lit Vertical Perspective | `Camera positioned above the subject with a slight downward tilt.` | Softer than full overhead |
| Low Tilt-Up | `Camera positioned low with the lens pointed upward toward the subject.` | Combine with Low Angle for emphasis |

## Position Relative to Subject

| Term | Paste-ready phrase | Notes |
|---|---|---|
| Over-the-Shoulder (OTS) | `Camera framed from behind one subject's shoulder, looking toward a second subject.` | Dialogue/interaction framing |
| Point-of-View (POV) | `Camera frames the scene as if seen directly through the subject's own eyes.` | Pairs with First-Person View in the movement library |
| Reverse Angle | `Camera positioned on the opposite side of a prior over-the-shoulder framing.` | For shot/reverse-shot sequences |
| Close-Profile | `Tight side-view framing close on the subject's face.` | Intimate + graphic |
| Back-to-Camera | `Subject faces away from the camera, back to the lens.` | Withholds the face; builds anticipation |
| Frontal Symmetrical Shot | `Camera centered directly on the subject with the composition symmetrical, Kubrick-style geometry.` | Formal, deliberate, slightly unsettling |

## Lens / Perspective

| Term | Paste-ready phrase | Notes |
|---|---|---|
| Wide-Angle Perspective | `Wide-angle lens perspective, expanded sense of space with foreground elements slightly exaggerated.` | Environmental/architectural default |
| Ultra-Wide Perspective | `Ultra-wide lens perspective with strong barrel distortion at the edges.` | Stylized — heavy distortion |
| Normal Focal Length | `Normal focal length, natural human perspective with minimal distortion.` | Neutral default |
| Telephoto Compression | `Telephoto lens compression, background pulled visually closer to the subject, shallow depth of field.` | Flattering portraits, isolates subject |
| Macro Perspective | `Macro lens perspective, extreme close detail with a miniature sense of depth.` | Product/texture detail work |
| Anamorphic Perspective | `Anamorphic lens perspective, horizontal stretch with oval-shaped bokeh.` | Cinematic/premium register |
| Fisheye Perspective | `Fisheye lens perspective, strongly curved edges across a near-180-degree field of view.` | Extreme/stylized, use deliberately |

## Position in 3D Space

| Term | Paste-ready phrase | Notes |
|---|---|---|
| Front-Facing | `Camera centered directly in front of the subject.` | Baseline |
| Off-Axis Left | `Camera positioned slightly to the left of the subject's centerline.` | Subtle asymmetry |
| Off-Axis Right | `Camera positioned slightly to the right of the subject's centerline.` | Subtle asymmetry |
| High Vantage Point | `Camera elevated above the scene, overlooking the subject and environment.` | Surveying/establishing |
| Balcony-Level Viewpoint | `Camera at a mid-level high angle, as if viewing from a balcony or mezzanine.` | Between eye-level and full aerial |
| Rooftop Vantage | `Camera at a very high angle, elevated but not directly overhead.` | Pairs well with Helicopter Shot/Crane Up in the movement library |
| Close Foreground Placement | `Camera positioned very near a foreground object, framing it large in front of the subject.` | Depth/parallax setup |
| Distant Observation Point | `Camera positioned far back from the subject, detached and observational.` | Voyeuristic/documentary read |

---

## Combining with the Movement Library

A full camera spec stacks four independent choices — height, framing/distance, angle/lens, and (if the shot moves) a movement from [Camera-Movements-Library.md](Camera-Movements-Library.md):

```
[Height/Position] + [Distance/Framing] + [Orientation or Lens/Perspective] + [Camera movement, if any]
```

**Example — static portrait reference frame:**
```
Camera at the subject's eye level, neutral human perspective. Medium close-up framing
from the shoulders to the top of the head. Camera angled roughly 45 degrees from the
subject's front. Normal focal length, natural human perspective with minimal distortion.
```

**Example — architecture establishing frame that then dollies in:**
```
Camera elevated above the scene, overlooking the subject and environment. Establishing
shot emphasizing context, architecture, and the space itself over the subject.
Wide-angle lens perspective, expanded sense of space with foreground elements slightly
exaggerated. Camera dollies straight forward toward the main subject, smooth and
controlled, tightening the composition.
```

The movement library's own phrases already describe *pace and path* — don't restate framing/lens terms there too; let each library own its layer.

---

## Where this fits in the pipeline

This library describes a **position**, not a change over time, so it plugs into [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md) at different points than the movement library:

- **Stage 2 (Reference Library) — no reference photo exists yet.** If a shot needs a generated (text-to-image) starting frame rather than a real photo, write that generation prompt using this library's vocabulary (height + framing + angle/lens) so the composition is precise instead of left to chance.
- **Stage 3 (Motion Analysis) — describing an existing reference precisely.** Use these terms in the motion-map file to record what the reference image *is* (e.g. "Low angle, wide shot, wide-angle perspective") before classifying what moves within it.
- **Signature card's `[lens/perspective language]` slot** — pull directly from the Lens/Perspective section above so every shot in a treatment shares one lens register (e.g. always Telephoto Compression for a portrait series, always Wide-Angle for real estate).
- **Per-shot prompts — the "arrival" frame.** When a camera move (from the movement library) ends somewhere specific, describe that end state using this library's terms, e.g. "...arriving on a close-up, eye-level, normal focal length."

Don't use this library to *replace* the `[Camera movement]` slot in the per-shot template — a moving shot still needs a movement phrase from [Camera-Movements-Library.md](Camera-Movements-Library.md). This library sets the position; that one sets the motion.

## Selector cross-reference

Extends the Movement Selector's subject table in [Camera-Movements-Library.md](Camera-Movements-Library.md) with a starting angle/framing default:

| Subject | Default height/angle | Default framing | Default lens |
|---|---|---|---|
| Building / real estate | Eye Level or Low Angle | Wide Shot / Establishing Shot | Wide-Angle Perspective |
| Product / still-life | Three-Quarter Angle | Medium Close-Up / Close-Up | Macro or Normal |
| Portrait, close-up face | Eye Level | Close-Up / Medium Close-Up | Telephoto Compression |
| Person, full body | Eye Level or Chest Level | Medium Wide Shot / Wide Shot | Normal Focal Length |
| Vehicle | Low Angle | Wide Shot | Wide-Angle Perspective |
| Landscape / establishing | High Vantage Point | Extreme Long Shot | Wide-Angle or Ultra-Wide |
| Food / tabletop | High Angle or Overhead | Close-Up | Macro Perspective |

As with the movement selector, Stage 3's locked/moving classification of the *specific* reference image overrides these defaults — they're a fast starting point, not a rule.
