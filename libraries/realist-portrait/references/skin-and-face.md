# Skin & Face Rendering — paste-ready phrasing

The single biggest "this is AI" tell in a portrait is skin that's too clean, too even, and too symmetrical. Every portrait prompt from this skill specifies texture, asymmetry, and age-appropriate detail explicitly. Standard photography/retouching vocabulary translated into prompt language — no external source.

---

## 1. Skin texture (pick a base + stack modifiers)

| Register | Paste-ready phrase |
|---|---|
| Default realist skin | `natural skin texture with visible pores, fine vellus hair catching the light, subtle surface shine on the forehead, nose and chin, no digital smoothing` |
| Close / editorial detail | `high-detail skin: individual pores, faint skin flush across the cheeks and ears, tiny imperfections, dry patch texture near the nostrils, unretouched` |
| Softer beauty-lit but still real | `skin lightly luminous under soft light but keeping real texture — pores, peach fuzz, faint uneven tone — beauty lighting, not beauty retouching` |
| Weathered / outdoor | `sun-exposed skin, slightly leathery texture across the cheekbones and forehead, visible sun damage and freckling, chapped lower lip` |

Always add subsurface scattering language for realism at the edges:
`soft subsurface scattering where light passes through the ears, nostrils and lip edges, warm translucency`

## 2. Asymmetry — say it, or the model averages it out

`natural facial asymmetry — one eye slightly smaller, brows set at different heights, a mouth that pulls a little more to one side` 

`slightly uneven hairline, one ear marginally higher than the other`

## 3. Age-appropriate features (match to the age in years, don't blur)

| Age band | Add |
|---|---|
| Child 4–11 | `soft rounded cheeks, smooth skin with a scatter of freckles, a small scab on one knuckle, slightly chapped lips, fine baby-hair wisps at the temples` |
| Teen 12–18 | `some hormonal skin activity — a few blemishes along the jaw and forehead, slightly oily T-zone, uneven brow growth` |
| 20s–30s | `smooth but textured skin, faint expression lines starting at the outer eyes when the face moves, natural under-eye tone variation` |
| 40s–50s | `established forehead and nasolabial lines, crow's feet at rest, slight loss of skin elasticity along the jaw, a few grey hairs at the temple` |
| 60s+ | `deep-set wrinkles, crepey skin texture on the eyelids and neck, age spots on the cheekbones and hairline, thinning brows, visible veins at the temple` |

## 4. Marks & individuality (choose 1–2, don't overload)

`a small mole below the left eye` · `a faint scar through one eyebrow` · `freckles concentrated across the nose and upper cheeks` · `a chipped front tooth visible when smiling` · `slightly bloodshot sclera, natural eye moisture and lower-lid waterline` · `a healed piercing hole in the earlobe`

## 5. Eyes — the second-biggest tell

`eyes with real detail: visible iris fibre pattern, a soft ring of darker limbal edge, natural redness in the inner corner, individual lower lashes, one catchlight only from the key light`

Avoid: two symmetric catchlights, glassy over-saturated irises, pure-white sclera, lashes that look drawn.

## 6. Expression & gaze — be specific, never "smiling"

| Want | Paste-ready phrase |
|---|---|
| Genuine warmth | `a real Duchenne smile — cheeks lifted, lower eyelids crinkled, crow's feet engaged, lips slightly parted` |
| Polite / social | `a closed-lip social smile that doesn't reach the eyes, jaw relaxed` |
| Neutral (hardest to get right) | `relaxed neutral expression, lips together but not pressed, eyes soft and unforced, a trace of asymmetry at the mouth` |
| Contemplative | `gaze directed just off camera to the left, eyes slightly narrowed in thought, brows drawn a few millimetres together` |
| Direct address | `looking straight down the lens, steady eye contact, chin level, micro-tension in the upper lip` |
| Caught mid-motion | `head turning toward camera, eyes arriving a beat before the face settles, hair still moving` |

Always fix **where the eyes look** (into lens / just past it / down / to a named side) and **head tilt** (chin up X°, head tilted toward the near shoulder, dead level).

## 7. Anti-patterns (see also anti-ai-tells.md)

- No "flawless", "perfect", "porcelain", "smooth skin" as positives.
- Don't request full symmetry.
- Don't stack five distinguishing marks — real faces have one or two that read.
- Teeth: `natural teeth, not uniformly white, slight overlap on the lower row` — never "perfect white smile".
