# P-04 · Anatomy of the sealed prompt (Leo, Pipeline-Presentation, Phase 4)

Source: `Pipeline-Presentation.html` in Leo's share of 2026-09-22, section P-04 (anatomy, the parts
with a fixed shape, and the SHOT 014 worked example). Extracted text, unedited. This is the
structure that says which references a shot carries: block 02 lists one line per @tag present and
nothing else, block 04 pins the first frame, block 17 is where continuity between clips lives.

```
P-04
 Phase 4 · Seedance 2.5
Anatomy of the sealed prompt
Seventeen possible blocks in a fixed order. Context and references first, then space and timing, then action and physics, then descriptive style in its home block, a short technical suffix, and locks last. Use only the blocks the shot needs.
01
Scene context
1–2 sentences: what happens, where, when, who stands where. The prompt opens here.
context
02
Active references
One line per 
@tag
 present: minimal anchor + “100% matches the reference”.
context
03
Location map
Foreground / midground / background, camera position, light origin, movement paths, relative to the anchor object.
space
04
First frame / blocking
Who is where in frame 1: position, orientation, gaze. Composition rule for this shot.
space
05
Format mode
Oner · sequential CUT 1/2/3 · timed HARD CUTs · freestyle b-roll.
timing
06
Optics
Shot size + FOV° per segment + lens character. Multishot: “no drift mid-segment”.
lens character
07
Camera
Operator: height, distance, move in km/h, focus. Body tonal character as a look, never a model name.
tonal character
08
Action
Events at the precision needed. Camera motion and subject motion stated separately.
action
09
Performance
Muscle-level emotion, eye-line, catch-lights, breath, pore detail.
acting · skin
10
Physics
Mass, inertia, contact shadows, fluids, particles.
realism
11
Lighting
Source, direction, exposure, Kelvin. The priority block.
light
12
Color grade
Only for a strong or stylised grade; otherwise fold colour into 03 + 11.
grade
13
Wardrobe
Material + condition, scene-logical.
costume
14
Audio
Only the needed sound. Dialogue with its word count. Exclusions allowed here.
guardrail
15
Style
Technical suffix: overall look in words, photoreal, format, grain. Exclusions allowed here.
suffix · guardrail
16
Output settings
Ratio, resolution, real-time vs slow-mo per segment.
suffix
17
Positive locks
Short hard fixers against likely failures, positive form. Continuity lives here.
locks
Right-hand column: the style aspect each block owns. No style prefix opens the prompt; this supersedes the labelled style header in Higgsfield-Prompt-Formats §2.4.
P-04
 The parts with a fixed shape
Reference lines, timing, locks
Reference line
Copy
@TAG: age + role/build + current state + unique visible features + action-critical details + voice (only if it has a line). 100% matches the reference.
The image carries identity; the text carries what happens. Keep it 
minimal
, because long appearance text fights the image. Still state small text, colour and critical detail in words. Never tag an element that isn't in the shot.
Role-scope each attachment: say what it controls and what to ignore. 
“@video1 controls body motion and timing only; ignore faces, wardrobe, location.”
Format mode phrasing
Copy
Oner
One continuous shot, the camera does not cut on its own.
Sequential
CUT 1 — [description]
CUT 2 — [description]
Timed multishot
0.0s to 4.0s — [description]
4.0s HARD CUT
4.0s to 9.0s — [description]
Whenever cuts are specified
Cuts only at the specified points, the camera does not cut on its own.
Whip pan (under 0.8 s renders as a hard cut)
0.3s — Subject A settled
0.8s — WHIP motion-blur transition
1.4s — Subject B settled
Cut types
HARD CUT
 · 
SMASH CUT
 · 
MATCH CUT
 · 
INSERT CUT
 · 
REVERSE CUT
 · 
WHIP CUT
. Fades only on request.
Extreme FOV stack
At 8° or 107°, all four: one location reference across beats, a LENS LOCK opener and a LENS CHECK closer per beat, colour via material + light.
Observation pattern
Hidden-camera feel needs all three: 20–30 % soft foreground occlusion, haze between camera and subject, an 8°–12° vantage anchored far away.
P-04
 Illustrative · built from the SHOT 014 card with CINEDANCE and the Acting System
A finished sealed prompt
Sixteen of seventeen blocks: COLOR GRADE is dropped and its colour folded into LOCATION MAP and LIGHTING, because the look is naturalistic. No names, FOV in degrees, speeds in km/h, Kelvin, left/right from camera, a word-count lock, and exclusions only in AUDIO and STYLE.
shots/SHOT-014/prompt.md
Copy
SCENE CONTEXT
Night, inside a narrow timber boat-repair workshop that opens onto a harbour slipway in heavy rain. @mara_wet stands alone behind the workbench, camera-left of centre, deciding whether to give up the key she has kept for eleven years.
ACTIVE REFERENCES
@mara_wet: woman, 58, lean shipwright's build, soaked through, grey hair plastered flat to her head, pale scar across the back of her right hand, speaks one line in a low, dry voice. 100% matches the reference.
@harbour_workshop: timber-framed workshop open to the slipway at the back; anchor object is the green enamel pendant lamp hanging over the bench. 100% matches the reference.
@brass_key: heavy brass mortice key, 11 cm long, bow worn smooth, tied to a short loop of faded red cord. 100% matches the reference.
LOCATION MAP
Foreground: the near edge of the bench, chisels laid out in a row, @brass_key on bare pale ash wood directly beneath the pendant lamp. Midground: @mara_wet behind the bench, facing camera. Background: the open slipway doors 6 metres behind her, rain falling through the orange sodium light of the harbour, a hull on trestles camera-right. The camera sits at the short end of the bench, camera-right of the lamp, on her shadow side. The green enamel shade throws a warm pool onto the ash wood; the faded red cord is the only saturated colour in frame.
FIRST FRAME / BLOCKING
The first visible frame already contains @mara_wet in her position, with no delayed reveal. Frame 1: she stands within 0.5 metres of the bench, both palms flat on the wood either side of the key, torso square to camera, head lowered, eyes on the key. Her face sits on the upper-left third; the key sits centred on the lower third.
FORMAT MODE
One continuous shot, 12 seconds, the camera does not cut on its own.
OPTICS
Medium close-up closing to close-up. FOV 29° throughout, no drift. Spherical rectilinear rendering with gentle edge falloff; shallow depth, her eyes and the key held on one plane of focus, the slipway doors dissolving into soft round highlights.
CAMERA
Camera at her chest height, 1.8 metres from her, on a smooth dolly. Continuous push-in along the bench at 0.5 km/h for the full 12 seconds, ending on her face. Focus holds on her eyes. Tonal character: wide latitude, highlights roll off softly around the bulb, the workshop's corners keep detail in the blacks.
ACTION
0–5 s: @mara_wet holds still; only her breath moves her shoulders. 5–8 s: she lifts her right hand and closes it around @brass_key; the red cord swings once. 8–10 s: she raises her eyes to a point just camera-left of the lens and speaks her line. 10–12 s: she sets the key back down a hand's width nearer the camera and draws her hand away.
Camera motion: the single continuous push-in only.
PERFORMANCE
@mara_wet is already mid-decision, weight settled low through both palms, wanting the key out of her hands before she can take it back. Her eyes flick from the key to the open doors and back in small quiet scans, blinks slow and rare; at 7 s two quick blinks and one swallow as she decides, and her eyes reach the point camera-left a beat before her head lifts. Jaw set, lips pressed until the line, delivered low and dry, flatter than she means it. When she sets the key down her fingers stay on it half a second longer than they need to, then open. Rain beads on her skin; pores and fine sun-lines visible across her cheekbones and brow; a single live catch-light from the pendant bulb in each eye; breath faintly visible in the cold air.
PHYSICS
The key has weight: her wrist dips slightly as she lifts it. Water runs from her cuff onto the bench and darkens the wood in a spreading patch. The lamp sways 2 cm on its flex in the draught from the doors, and its pool of light slides with it.
LIGHTING
Key: the single bare bulb inside the green enamel shade, 3200 K, hard and directly overhead, carving deep shadow under her brow. Rim: a thin cold edge of harbour light along her wet hair and shoulders from the doors behind. Her camera-side cheek falls into unfilled shadow. White balance fixed at 3200 K for the whole shot.
WARDROBE
Dark olive oilskin smock, cracked at the elbows and streaming wet; the rolled collar of a grey wool jumper at her neck.
AUDIO
Dialogue (English, audio only, no subtitles): @mara_wet says: "Take it, then." — exactly three words, nothing else spoken. Her lips stay still except for the line.
VOICE: "A 58-year-old harbour shipwright, flat coastal accent. Low, dry alto with a rough edge; short, unhurried sentences; goes quieter, never louder, when it matters."
Ambience: steady rain drumming on a corrugated roof, a gutter overflowing onto the slipway, a halyard ticking against a mast outside. Foreground: the key's scrape on wood at 5 s and at 10 s.
NO MUSIC. SFX ONLY — diegetic sound and live audio throughout.
STYLE
Photoreal live action, fine organic grain, milky filmic black floor. No logos, no readable text.
OUTPUT SETTINGS
2.39:1, 1080p, real-time throughout.
POSITIVE LOCKS
The key stays on the bench or in her right hand at every moment, red cord attached. The scar on the back of her right hand stays visible as she lifts the key. She speaks exactly three words. Her hair stays wet and flat. The pendant lamp is the only light source inside the workshop. The camera moves forward only.
Illustrative example written for this deck. Characters, location and prop are placeholders, not assets from a real production.
```
