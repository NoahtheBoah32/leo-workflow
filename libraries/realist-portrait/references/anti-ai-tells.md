# Anti-"AI Portrait" Tells — failure modes + negative-prompt bank

The recurring reasons an AI portrait reads as fake, each with the positive-side fix (say the real thing) and the negative-side guard (name the artefact to suppress). Prefer the positive fix — negatives are a backstop and some models ignore them.

---

## 1. The failure modes

| Tell | Positive-side fix | Negative guard |
|---|---|---|
| **Plastic / waxy skin** — no pores, uniform tone, blurred | skin/texture phrases from [skin-and-face.md](skin-and-face.md) §1–2 | `plastic skin, waxy skin, airbrushed, over-smoothed, poreless` |
| **Over-symmetry** — identical eyes/brows/ears | asymmetry phrases §2 | `perfectly symmetrical face, mirrored features` |
| **Glassy / dead eyes** — glossy irises, double catchlights, drawn lashes | eye detail phrases §5 | `glassy eyes, oversaturated iris, doubled catchlights, painted eyelashes` |
| **Averaged "AI face"** — instantly recognisable model default | demographic specificity + age in years + 1–2 distinguishing marks | `generic face, stock-photo face, instagram face` |
| **HDR / flat lighting** — everything evenly bright, no real key | a named lighting pattern from [face-lighting.md](face-lighting.md) | `flat lighting, HDR, evenly lit, no shadows` |
| **Wide-angle face bulge** — big nose, small ears, domed forehead | 85mm + working distance from [portrait-lenses.md](portrait-lenses.md) | `wide-angle distortion, enlarged nose, fisheye, warped face` |
| **Everything in focus** — no focus plane on a "portrait" | aperture + named focus point §2 | `deep focus, everything sharp, no depth of field` |
| **Mannequin hair** — helmet-smooth, laser parting | hair imperfection from [wardrobe-hair-grooming.md](wardrobe-hair-grooming.md) §3 | `plastic hair, helmet hair, perfect hairstyle, no stray hairs` |
| **Catalogue clothing** — crisp, new, perfectly draped | fabric + fit + condition §1 | `brand-new clothing, perfectly pressed, mannequin drape` |
| **Toothpaste smile** — uniform blinding-white teeth | `natural teeth, not uniformly white, slight overlap` | `perfect white teeth, veneers, gleaming smile` |
| **Melted details** — hands, ears, jewellery, glasses hinges, earbuds | frame so hands are out, or describe them explicitly; give jewellery a hard highlight + cast shadow | `deformed hands, extra fingers, melted jewellery, malformed ears, fused earrings` |
| **CGI sheen** — subject looks 3D-rendered | capture character from [../../../../Camera-Look-Library.md](../../../../Camera-Look-Library.md): grain, halation, film stock | `3d render, CGI, video game character, unreal engine, digital art, illustration` |
| **Uncanny cleanliness** — no dust, no grain, sterile | `fine film grain in the midtones and shadows, faint sensor noise, a little atmospheric haze` | `overly clean, sterile, noiseless` |
| **Backdrop that's too perfect** — seamless studio nothing | give the background a real texture, falloff, and a flaw (a scuff, a seam, uneven light) | `seamless perfect background, flat gradient` |
| **Age mismatch** — "50 years old" rendered at 30 | age corroboration detail from §3 of skin-and-face | `youthified, de-aged` |

## 2. Negative-prompt bank (trim to what's relevant — don't paste the whole thing)

**Core (almost always useful):**
`plastic skin, waxy, airbrushed, over-smoothed skin, poreless, perfectly symmetrical face, generic AI face, stock-photo face, flat HDR lighting, 3d render, CGI, video game character, illustration, digital painting, overprocessed`

**Anatomy / detail:**
`deformed hands, extra fingers, fused fingers, malformed ears, asymmetric eyes misaligned, crooked teeth blur, extra limbs, distorted jewellery, warped glasses`

**Lens / focus:**
`wide-angle facial distortion, fisheye, enlarged nose, deep focus everything sharp, tilt-shift`

**Styling:**
`brand-new clothing, perfectly pressed, helmet hair, laser-straight hairline, blinding white teeth, heavy beauty retouching`

**Quality junk (model-dependent):**
`lowres, jpeg artifacts, oversharpened, chromatic aberration fringing, banding, watermark, text, signature, border, frame`

## 3. Notes

- Flux / Seedream / Dreamina: put this in the negative field if the model exposes one; if not, delete the negatives entirely rather than appending "no X, no Y" into the positive paragraph (it often summons X).
- Midjourney: use `--no plastic skin, symmetrical face, 3d render, deformed hands` — keep the `--no` list short, 4–8 items.
- Don't negate something you also need — e.g. don't put `grain` in negatives if the positive asks for film grain.
- The strongest anti-tell move is always positive: name the real photographic setup (body, lens, light pattern, film stock) so the model has something concrete to render instead of its "portrait" prior.
