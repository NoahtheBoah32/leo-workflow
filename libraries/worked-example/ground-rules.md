# Phase 0 — Ground Rules — THE WINDOW MAP

Set once, checked at every gate. Never changed mid-flight.

| # | Rule | Value | Status |
|---|---|---|---|
| 1 | **Aspect ratio** | **16:9** | locked by user, 2026-09-22 |
| 2 | **Palette** | Warm storybook — see table | locked by user, 2026-09-22 |
| 3 | **Runtime target** | **120 s** → **11 shots** (8–14 s each; well under the 30 s ceiling) | locked by user, 2026-09-22 |
| 4 | **Forbidden everywhere** | see list | locked by user, 2026-09-22 |
| 5 | **Reroll budget** | **5 per shot** → **55 generations max** across 11 shots | locked by user, 2026-09-22 |
| 6 | **Generation log** | `generation-log.csv` — first entry is run #1, whatever the result | ready |

## Palette (hex)

| Role | Hex |
|---|---|
| Waffles orange (the cat's coat) | `#E07B39` |
| Sill cream (apartment, morning light) | `#F3E3C3` |
| Bus green (`@bus_7`) | `#2F7D5B` |
| Tower red (`@water_tower`) | `#B8322A` |
| Neon gold (`@pretzel_sign`) | `#F2B33D` |
| Raincoat yellow (`@nia`, night) | `#F4C430` |
| Night rain blue (dusk → night scenes) | `#1F3552` |

**Exclusions:** crushed pure-black shadows; neon magenta; a teal-and-orange grade.
Exclusions go only in the style line (BAN 2 house rule: all other blocks stay positive).

## Forbidden everywhere

Each item goes into every prompt as a **positive lock**, not a negative.

1. **No legible text or logos**, with one exception: the numeral **"7"** on `@bus_7`.
   Positive form: *"shop fronts, signage and vehicles carry no readable lettering or brand
   marks; the only legible character in frame is the white numeral 7 on the bus front."*
2. **`@flyers` carry Waffles' photo; the text under it renders as soft unreadable blocks.**
3. **Exactly one cat in the whole film**: `@waffles`. No other cats in the background.
4. **`@waffles` is never anthropomorphic.** He doesn't speak or make human gestures, never
   stands upright except a brief rear-up with front paws on glass, and never shows a
   human facial expression.
5. **No animal is harmed, and no animal is seen in distress beyond comic surprise.** The
   dog never makes contact with the cat; the fall into the cart is a soft landing.
6. **No music in any generation** (BAN 3). Only ambience, foley and dialogue in-pass.

## Photography axes (locked for the whole film — Phase 2 onward)

| Axis | Pick | Reaches prompts as (observable description only, BAN 1) |
|---|---|---|
| **Look** | Warm colour-negative film | soft warm highlights that roll off gently, fine even grain, creamy natural skin, forgiving mid-contrast, slightly lifted blacks |
| **Stance** | Directed candid | staged action that reads natural; no one plays to camera (grey character sheets are posed by nature — the stance governs locations and shots) |

Locked by user, 2026-09-22.

> **Gate 0 — PASSED** 2026-09-22. All six constants locked by the user.
