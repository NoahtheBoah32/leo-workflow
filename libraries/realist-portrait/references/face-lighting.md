# Face Lighting — portrait patterns, paste-ready

Companion to [../../../../Camera-Look-Library.md](../../../../Camera-Look-Library.md), which covers capture character; this file covers *how the face is lit*. A named lighting pattern is one of the strongest realism levers — it gives the model a concrete photographic setup instead of "cinematic lighting".

Standard portrait-lighting vocabulary — no external source.

---

## 1. Pattern (pick exactly one)

| Pattern | What it looks like | Paste-ready phrase |
|---|---|---|
| **Loop** (default) | Small nose-shadow loop on the cheek, not touching the smile line. Flattering, natural, works on most faces. | `loop lighting: key light about 45 degrees to camera-left and slightly above eye level, casting a small downward shadow from the nose onto the cheek` |
| **Rembrandt** | Triangle of light on the shadow-side cheek under the eye. Moodier, characterful. | `Rembrandt lighting: key light high and 45 degrees off-axis, a small illuminated triangle on the far cheek, the rest of that side in shadow` |
| **Split** | Half the face lit, half in shadow. Dramatic, tense. | `split lighting: key light 90 degrees to one side, one half of the face fully lit, the other half in deep shadow, thin transition down the centre of the nose` |
| **Butterfly / Paramount** | Symmetric shadow directly under the nose. Glamour, beauty, older-Hollywood. | `butterfly lighting: key light high and directly in front, a small symmetric shadow under the nose, gentle shadows under the cheekbones and jaw` |
| **Broad** | Lit side of the face turned toward camera — widens the face. | `broad lighting: face turned slightly away from the key so the near, camera-facing side is the lit side` |
| **Short** | Lit side turned away from camera — slims, adds depth. Editorial default. | `short lighting: face turned slightly toward the key so the far side is lit and the near side falls into soft shadow` |
| **Rim / edge only** | Subject mostly dark, bright outline. Silhouette-adjacent, dramatic. | `low-key rim lighting: strong backlight raking the edge of the hair and jaw, face held in near-darkness with only a faint fill` |

## 2. Source quality & size

| Quality | Phrase | Reads as |
|---|---|---|
| Large soft | `large soft light source close to the subject, wide gradual wrap, soft-edged shadows` | Overcast window, big softbox — gentle, modern |
| Medium soft | `medium softbox at a moderate distance, shadows with a defined but not hard edge` | Standard studio portrait |
| Hard | `single hard light source, crisp shadow edges, bright specular highlights on the skin` | Direct sun, bare bulb, fashion/noir |
| Diffused ambient | `soft directionless daylight from an overcast sky, very low contrast, shadows barely present` | Documentary, natural, no studio feel |

## 3. Key-to-fill ratio (contrast)

| Ratio | Phrase |
|---|---|
| Low (2:1) | `low lighting ratio, shadows open and full of detail, gentle modelling` |
| Medium (4:1) | `moderate contrast, shadow side clearly darker but still readable` |
| High (8:1+) | `high contrast, shadow side falling to near black, only the key side rendered` |

## 4. Direction & height

Always state both:
`key light [camera-left / camera-right / frontal / behind], [above eye level / at eye level / below eye level (uplight — use sparingly, reads sinister or theatrical)]`

## 5. Catchlights (small detail, big realism payoff)

`a single soft catchlight in each eye at the 10 o'clock position, matching the key light shape` — one key = one catchlight. Add `a faint second catchlight low in the eye from a reflector` only if there's a fill board.

## 6. Colour of light

| Setup | Phrase |
|---|---|
| Neutral studio | `neutral 5600K daylight-balanced light, accurate skin colour` |
| Warm practical | `warm 3200K tungsten key, slight amber cast on the skin, cooler ambient shadow` |
| Window daylight | `cool north-facing window light as key, warm bounce from a wooden interior filling the shadows` |
| Golden hour | `low warm sun as a back-three-quarter key, long soft shadow, orange rim on the hair, cool skylight fill on the shadow side` |
| Mixed / editorial | `warm key with a subtle cyan-tinted fill, controlled colour contrast` |

## 7. Environmental / motivated options

`lit by a single practical lamp just out of frame` · `firelight from below-frame, flickering warm key, deep falloff` · `screen light — cool blue key from a phone or monitor, uneven across the face` · `open shade under a building, soft wrap, bright skylight catchlight`

## 8. Anti-patterns

- "Cinematic lighting", "dramatic lighting", "perfect lighting" alone — no information, model defaults to flat HDR.
- Two equal key lights (flat, dead) unless you specifically want a beauty clamshell: `clamshell lighting: soft key above, reflector directly below, near-shadowless, faint double catchlight`.
- Uplight by default — it almost always reads wrong for a straight portrait.
- Ring-light look (`even flat frontal light, single circular catchlight`) unless the brief is explicitly influencer/vlog.
