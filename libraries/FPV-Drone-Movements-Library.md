# FPV Drone Movements Library

Extension to [Camera-Movements-Library.md](Camera-Movements-Library.md), covering FPV-freestyle-specific moves that plain "drone push in / pull back" doesn't capture. Same usage: drop the paste-ready phrase into the `[Camera movement]` slot of the per-shot prompt template in [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md).

These describe *piloting maneuvers* rather than simple linear moves, so they carry more risk of the model flattening them into generic motion — pair with the pipeline's "restate as an observed result" diagnose step if the first pass looks too tame.

---

## Freestyle Maneuvers

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Power Loop | `FPV drone pulls into a full vertical loop, climbing hard, cresting inverted, then diving back down through the starting point.` | Big, showy — good for hero reveals over a subject |
| Split-S | `FPV drone rolls to inverted mid-flight, then pulls back to dive downward, exiting in the opposite direction it entered.` | Reads as a sharp direction change, not a full loop |
| Dive / Dive Bomb | `FPV drone drops into a steep dive toward the ground, accelerating, then levels out and recovers just above the surface.` | High energy — pair with a clear ground-plane subject to land the recovery |
| Matty Flip | `FPV drone flies backward over an obstacle, inverts, and completes a full flip before continuing forward.` | Advanced/showy; best over a distinct foreground obstacle |
| Barrel Roll | `FPV drone rolls a full 360 degrees around its forward axis while continuing to fly forward.` | Keeps forward travel readable while adding rotation |
| Immelmann Turn | `FPV drone climbs and half-loops, rolling upright at the top to exit flying in the opposite direction at higher altitude.` | Combines a climb with a direction reversal |
| Juke | `FPV drone snaps sideways in a sudden sharp direction change mid-flight, then continues on the new line.` | Fast, reactive — good for energetic action cuts |

## Wall / Surface Interaction

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Wall Ride | `FPV drone approaches a vertical surface at a shallow angle, pitches up at the last moment to skim along it, then breaks away.` | Needs a clear vertical surface in the reference image (building facade, cliff) |
| Ground Skim | `FPV drone flies low and fast just above the ground, hugging the terrain's contours.` | High-energy, good for landscape/runway-style establishing shots |
| Canopy / Gap Run | `FPV drone weaves fast and low through a tight gap or cluster of obstacles, threading the space without slowing.` | Needs a foreground obstacle cluster (trees, structural gaps) in frame |

## Proximity & Flow

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Proximity Flying | `FPV drone flies close alongside a structure or object, maintaining a tight, consistent distance as it tracks past.` | Reads as confident/skilled piloting; needs a strong linear subject edge (facade, fence line) |
| Rubik's Cube Roll | `FPV drone tumbles forward through a continuous sequence of alternating rolls, tumbling through space while still advancing.` | Disorienting, stylized — use sparingly, best for short energetic inserts |
| Close Orbit Pass | `FPV drone circles tight and fast around the subject at close range, banking into the turn.` | Faster, tighter, more aggressive version of the standard Orbit move |

## Cinematic FPV

| Movement | Paste-ready phrase | Notes |
|---|---|---|
| Cine Glide | `FPV drone moves in a smooth, slow, floating glide through the space, minimal roll or pitch, cinematic and controlled.` | The "cinewhoop" register — for calm establishing/interior moves rather than freestyle energy |
| Rip and Recover | `FPV drone accelerates hard in a straight line, then decelerates and stabilizes smoothly as it approaches the subject.` | Energy building into a calm hold — good for an intro beat before a static hero frame |
| Reveal Climb | `FPV drone climbs steadily while pitching the camera up, transitioning from a close low shot into a wide elevated view.` | Establishing-shot payoff move |

---

## Deep Technical Profiles

Four maneuvers with well-documented flight mechanics — pulled apart into entry conditions, throttle/pitch behavior, and what that translates to visually, so the prompt phrasing can reference *why* the motion looks the way it does instead of a generic verb. Numbers here come from real piloting technique, not arbitrary — useful for pinning Kling's motion sliders or writing a "restate as observed result" retry per the pipeline's diagnose step.

**Power Loop**
- Entry: moderate approach speed (roughly 30–40 km/h) before initiating the climb.
- Throttle/pitch: full throttle (80–100%) held through the climbing arc; the defining moment is a hard cut to zero throttle right at the apex, while inverted — that's what separates a clean loop from a mushy one — then throttle comes back in at a reduced level (~30%) through the dive and full pitch-forward to level out.
- Visual translation: acceleration and motion blur build through the climb, a brief weightless hang at the very top, then a committed dive back to the starting altitude.
- AI-prompt phrase: `FPV drone pitches back into a steep climbing arc, motion blur building through the climb, a brief weightless hang as it crests inverted at the top, then a committed dive back down through the starting altitude.`

**Split-S**
- Entry: needs real altitude margin — at least 15–20m of clearance, since the whole maneuver trades altitude for the direction change.
- Throttle/pitch: throttle cut to roughly 20% while rolling to inverted, pitch pulled back immediately after inverting to start the dive, then throttle smoothly reintroduced as the horizon reappears to arrest the descent.
- Visual translation: a fast roll to upside-down, a diving beat, and a recovery facing the opposite direction from where it started.
- AI-prompt phrase: `FPV drone rolls sharply to inverted, throttle briefly cutting, then dives through the roll and recovers right-side-up now facing the opposite direction from where it started.`

**Wall Ride**
- Entry: a shallow, near-parallel approach angle to the surface — a steep or perpendicular approach reads as a collision, not a ride.
- Behavior: the maneuver is commitment-based rather than throttle-timed — hesitating or pulling back mid-slide causes a visible deflection/bounce off the surface instead of a clean glide.
- Visual translation: the drone grazes into the surface, pitches up right at contact to hold the slide, then peels away at a matching shallow angle.
- AI-prompt phrase: `FPV drone approaches the wall at a shallow, near-parallel angle, pitching up right at contact to hold a smooth slide along the surface, then peeling away at the same shallow angle.`

**Proximity Flying**
- Core relationship: distance and speed are inversely linked — the tighter the gap or the closer to the subject, the slower and more controlled the flight needs to be for it to read as intentional rather than reckless.
- Camera behavior: the more the camera/lens tilts upward relative to the flight vector, the faster the forward motion reads on screen, independent of actual speed.
- What sells it: a fixed reference edge in frame (a wall, fence line, tree line) that the drone tracks parallel to — the parallax against that edge is what makes the proximity register, not the subject alone.
- AI-prompt phrase: `FPV drone flies at close, controlled range alongside the structure's edge, holding a slow, steady pace with the camera tilted slightly upward, the surface sliding past at a consistent, tight distance.`

---

## A note on terminology

"Tic-toc" and "matrix dive" are sometimes used informally by individual FPV pilots/creators but aren't standardized trick names in the sources checked — left out to avoid inventing a definition. If you've seen either used in a specific reference clip, describe the actual motion you want rather than relying on the name; the model won't know the slang either.

---

Sources:
- [A master list of FPV tricks and maneuvers and how to do them](https://wrekd.com/pages/a-master-list-of-fpv-tricks-and-manuevers-and-how-to-do-them)
- [FPV Freestyle Tricktionary – Rotor Riot](https://rotorriot.com/blogs/tutorials-guides/fpv-freestyle-tricktionary)
- [FPV Acro Freestyle (Ultimate Guide) – Droneblog](https://www.droneblog.com/fpv-acro-freestyle/)
- [FPV Freestyle Trick Progression 2026: From Power Loops to Matty Flips – UAVMODEL Insights](https://blog.uavmodel.com/fpv-freestyle-trick-progression-2026-from-power-loops-to-matty-flips/)
