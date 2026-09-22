# Film Director Library

Companion to [Camera-Movements-Library.md](Camera-Movements-Library.md), [Camera-Framing-Angle-Library.md](Camera-Framing-Angle-Library.md), and [Depth-of-Field-Library.md](Depth-of-Field-Library.md). Those answer *what movement/framing/focus is available*. This one answers *what is this shot trying to do, and which of those choices actually serves it* — the reasoning layer that sits between Stage 3's motion classification and Stage 4's prompt template in [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md), formalized as **Stage 3.5 — Director's Pass**.

No external source — unlike the other three libraries, this isn't phrases extracted from a reference site. It's a decision framework for reasoning through a shot before writing it. Nothing here is paste-ready on its own; it produces the Director's Brief, which then tells you *which* paste-ready phrases from the other libraries to reach for and *how to order them*.

---

## Shot Intent (what is this shot for?)

Every shot should be doing exactly one dramatic/emotional job. If you can't name it in one sentence, the shot doesn't have an intent yet — it just has a subject.

| Intent | Reads as | Camera family that serves it | Anti-pattern |
|---|---|---|---|
| Reveal | "Now you see it" | Tilt Up, Crane Up, Rack Focus (Background→Foreground), Pull Past | Revealing too early — burying the reveal under other motion |
| Approach / Intimacy | Closing distance, personal | Dolly In, Slow Zoom In, Push Past | Approaching without a reason the reveal is arbitrary, not personal |
| Scale / Awe | Smallness against vastness | Drone Pull Back, Crane Up, Helicopter Shot, Dolly Out | Pulling back so far the subject stops reading at all |
| Departure / Loss | Distance growing, something left behind | Dolly Out, Reverse Tracking, Drone Pull Back | Confusing this with generic "Dolly Out" — the subject should visibly recede, not just the frame widen |
| Tension / Threat | Unease, instability | Handheld Shot, Slow Zoom In (tight), Low Tracking | Overused — handheld on every shot reads as stylistic tic, not tension |
| Curiosity / Possession | Circling, appraising | Orbit CW/CCW, Arc Right/Left | Orbiting a subject with nothing worth circling — reads as decoration |
| Contemplation / Stillness | Held, unhurried | Static Shot, Slow Zoom In (very slow) | Static shot with nothing changing in-frame reads as a mistake, not a choice |
| Arrival | Settling into place | Dolly In arriving on a framing, Crane Down | No clear end-state — arrival needs a defined stopping point |
| Transformation / Passage | Crossing a threshold | Push Past / Pass-by Shot, Pass-Through Objects, Infinite Zoom | Using a portal move without a matched second image/scene on the other side |
| Urgency / Chaos | Disorientation, speed | Whip Pan, Crash Zoom, Chase Shot | Sparingly only — per the movement library's own notes, these read as errors if overused |

---

## Motion Hierarchy (ranking what Stage 3 found)

Stage 3's motion classification gives you a flat **Moves** list — everything that's allowed to move. The director's job is to rank that list by narrative weight, not physical position in the frame:

- **Lead motion** — the one element/action the viewer's eye should follow first. Usually the subject's own action, or the single motivated environmental event the shot is built around (the Hilltop Reveal example's light network is a lead motion, not ambient decoration).
- **Supporting motion** — reinforces the lead without competing for attention (hair/fabric moving with the same wind that's bending the foreground grass).
- **Ambient motion** — background texture that sells "this world is alive" but should never outcompete the lead (drifting clouds, distant haze, background traffic).

**Rule: one lead motion per shot.** If two elements are both fighting to be what the eye follows, the shot is carrying two ideas — split it into two shots, or explicitly subordinate one to supporting/ambient.

This ranking is what determines prompt order in Stage 4 — "whatever leads the prompt wins the frame" is a *director* rule wearing prompt-engineering clothing.

---

## Pacing & Rhythm

| Pace | Feels like | Pairs with |
|---|---|---|
| Constant | Steady, controlled, premium | Dolly In/Out, Orbit, Slow Zoom, Tracking Shot |
| Accelerating | Building, mounting | Crash Zoom, Whip Pan, a push-in that speeds up toward arrival |
| Decelerating | Settling, arriving, resolving | Orbit or dolly that slows into a held final frame |
| Held-then-moves (punctuated) | A beat of stillness before the point lands | Static Shot holding, then a single deliberate move (Tilt Up, Rack Focus) |

State the pace explicitly in the brief — "slowly" vs. "rapidly" is the only lever Seedance gets (no motion slider), and Kling's motion-strength slider should be set to match, not contradict, whatever pace the brief calls for.

---

## Camera Intent Vocabulary (movement family → dramatic verb)

The Movement Selector in [Camera-Movements-Library.md](Camera-Movements-Library.md#movement-selector-auto-suggest-from-a-reference-photo) picks a movement from *what's in the photo*. This table is the check that comes after — does the mechanically-correct pick also do the dramatic job the brief calls for?

| Movement family | What it accomplishes dramatically | Mismatch warning |
|---|---|---|
| Dolly / Push In | Closes distance — intimacy, focus, arrival | Don't use just because "push-in" is the default — state what closing distance means here |
| Dolly / Pull Out | Opens distance — scale, isolation, departure | Pulling back on a subject the shot is supposed to feel close to undercuts the intent |
| Orbit / Arc | Possession, appraisal, curiosity — showcases an object from every side | Orbiting because it "looks cinematic" with no reason to circle reads as decoration |
| Static | Contemplation, held tension, lets the subject/world carry all the motion | Needs *something* moving in-frame (Stage 3's Moves list) or it reads as an accident |
| Handheld | Urgency, rawness, subjectivity — puts the viewer in a body | Overuse flattens it into a stylistic tic instead of a deliberate choice |
| Crane / Drone | Omniscience, grandeur, establishing scale | Grand moves on an intimate/small-scale subject fight the intent |
| Tilt / Pedestal | Reveals height or grounds a reveal | Weak if the vertical subject isn't actually tall enough to justify it |
| Whip Pan / Crash Zoom | Shock, disorientation, hard punctuation | Sparingly — see the movement library's own notes; these are exclamation points, not periods |

---

## Director's Brief (per-shot template)

```
Director's Brief — [shot name]
Dramatic intent: [one sentence — what this shot is doing / what the viewer should feel or notice]
Lead motion: [the one element/action the eye follows first]
Supporting motion: [reinforces the lead without competing]
Ambient motion: [background texture/atmosphere]
Camera does: [what the movement accomplishes dramatically — not just its name]
Pace: [constant / accelerating / decelerating / held-then-moves]
```

**Fill this out per shot, not per reference image.** Stage 3's locked/moving classification is a fixed physical fact about a reference photo — record it once per image. Dramatic intent, motion priority, and pace are shot-level decisions — the same reference image can produce two shots with different Director's Briefs (an intimate approach vs. a scale-establishing pull-out), each with its own brief.

---

## Director Selector — decision order

1. **Name the one thing this shot needs the viewer to notice or feel.** If it's a multi-clip project, this comes from the beat assigned in Stage 5; if standalone, decide it now.
2. **Cross-reference the Shot Intent table** above for camera-family candidates, then run the Movement Selector in [Camera-Movements-Library.md](Camera-Movements-Library.md) to pick the specific paste-ready phrase within that family.
3. **Rank Stage 3's Moves list** into lead / supporting / ambient. Don't re-derive what moves — that's already decided; only decide the *order of importance*.
4. **Sanity-check against the signature card's mood** — same cross-check discipline as the Movement Selector's step 4.
5. **State the camera's dramatic job in one sentence.** If you can't, the pick was chosen because it fit the subject-category default, not because it serves this shot — reconsider it.

**Output format when suggesting (Claude, given a reference photo + Stage 3 motion map):**

```text
Dramatic intent: [one sentence]
Lead motion: [element] — Supporting: [element] — Ambient: [element]
Suggested movement: [name] — [paste-ready phrase from Camera-Movements-Library.md]
Camera does: [what the move accomplishes dramatically]
Pace: [constant/accelerating/decelerating/held-then-moves]
```

---

## Anti-patterns

- **Competing leads.** Two motions both fighting for primary attention — the shot has two ideas, not one. Split it or subordinate one.
- **Camera move chosen for its name, not its job.** Orbiting because it "looks cool" instead of because there's something worth circling.
- **Overriding Stage 3 to serve drama.** The locked/moving classification is a hard boundary, not a suggestion — the director's job is to choose emphasis and pacing *within* it, never to unlock something Stage 3 tagged locked.
- **Pace mismatched to mood.** A crash zoom in a contemplative brief, or a static held shot in an urgent one.
- **Flattening every shot in a sequence to the same intent.** Varying intent shot-to-shot is what makes a sequence a story — see Stage 5. What should stay constant across a sequence is camera-*language* family and pacing register, not dramatic intent itself.

---

## Cross-reference

- Movement phrases: [Camera-Movements-Library.md](Camera-Movements-Library.md)
- Starting framing/angle/lens: [Camera-Framing-Angle-Library.md](Camera-Framing-Angle-Library.md)
- Focus/bokeh: [Depth-of-Field-Library.md](Depth-of-Field-Library.md)
- FPV/drone specialty moves: [FPV-Drone-Movements-Library.md](FPV-Drone-Movements-Library.md)

---

## Usage notes

- This library doesn't produce a paste-ready phrase for the prompt itself — its output is the Director's Brief, which determines *which* paste-ready phrases from the other libraries to use and *what order* to write them in.
- Run it after Stage 3 (you need the Moves list to rank) and before writing the Stage 4 per-shot prompt.
- The brief's `Lead motion` becomes what leads the per-shot prompt sentence; `Camera does` becomes the justification you'd give if someone asked why this movement and not another — it doesn't need to appear in the prompt text itself, but if you can't fill it in, don't lock the movement choice yet.
- For multi-shot sequences: vary Dramatic Intent shot-to-shot (that's the story), but keep the movement-family and pacing register consistent per treatment — same discipline as the signature card in Stage 4.
