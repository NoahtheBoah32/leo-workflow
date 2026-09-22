# ZEISS Supreme Prime Lens Library

Companion to [Depth-of-Field-Library.md](../Depth-of-Field-Library.md), [Camera-Framing-Angle-Library.md](../Camera-Framing-Angle-Library.md), and [Camera-Look-Library.md](../Camera-Look-Library.md). Those cover focus, framing, and grade; this one is the **glass** — per‑lens focal length, character, and depth‑of‑field behaviour, plus paste‑ready phrasing for the `[lens/perspective language]` slot of the signature card or the `[style/mood]` slot of a per‑shot prompt (see [Image-to-Video-Pipeline.md](../../Image%20to%20Video/Image-to-Video-Pipeline.md)).

Image‑ and video‑models (Seedance, Kling, Seedream, etc.) do **not** simulate a specific lens. They read "50 mm ZEISS Supreme Prime, T1.5" as a *vibe* — full‑frame field of view, shallow plane, gentle sharpness, clean contained flare. Use the numbers to choose the right focal length and DoF, then hand the model the paste‑ready phrase, not the spec sheet.

**Sources.** `manual-depth-of-field-tables-zeiss-supreme-prime-lenses.pdf` (read in full — lens line‑up, T‑stops, focus‑scale engravings, circle‑of‑confusion values, DoF tables for Full Format / ANSI Super 35 / Normal 35 / APS‑H / APS‑C). The companion `brochure-zeiss-supreme-lenses.pdf` in this folder is **corrupted** (every content stream was destroyed by a UTF‑8 re‑encoding pass — ~498k replacement characters; not recoverable), so physical specs, coating, mount, and "look" copy below are filled in from ZEISS's own published data ([Supreme Prime](https://www.zeiss.com/photonics-and-optics/us/cinematography/lenses/supreme-prime-lenses.html), [Supreme Prime Radiance](https://www.zeiss.com/photonics-and-optics/us/cinematography/lenses/supreme-prime-radiance-lenses.html)) and dealer spec sheets. If you can re‑export the brochure as a clean PDF, drop it back in and this file can be tightened.

---

## The family at a glance

- **14 Supreme Prime focal lengths:** 15, 18, 21, 25, 29, 35, 40, 50, 65, 85, 100, 135, 150, 200 mm.
- **11 Supreme Prime Radiance focal lengths:** 18, 21, 25, 29, 35, 40, 50, 65, 85, 100, 135 mm — the middle of the range only (no 15 / 150 / 200).
- **Aperture:** T1.5 across the range **except** 15 mm (T1.8), 150 mm (T1.8), 200 mm (T2.2). Minimum T22.
- **Coverage:** large‑format / full‑frame — **46.3 mm image circle**. Covers VistaVision, Alexa LF / Mini LF / 65 (within the circle), Sony VENICE FF, RED Monstro/Komodo‑X, and every Super 35 sensor.
- **Coating:** ZEISS **T\*** (standard Supreme Prime) / **T\* blue** (Radiance).
- **Iris:** rounded, high‑blade‑count (dealer sheets cite ~16) — circular out‑of‑focus highlights at all stops.
- **Mechanics:** internal focus, **non‑rotating front**, minimal focus breathing; ~300° focus rotation; standard 0.8 MOD / 32‑pitch gears in shared positions across the set; consistent front diameter (95 mm on most, 114 mm on 15 / 18 / 135 / 150 / 200).
- **Mount:** user‑interchangeable (IMS) — ships PL, also LPL and EF; supports ZEISS eXtended Data + Cooke /i metadata.

### One‑line character

> Gentle, "organic" sharpness rather than clinical bite — resolves detail but stays kind to skin. Very smooth in‑focus‑to‑out‑of‑focus transition, elegant round bokeh, and **contained** flare (no big veiling wash). Neutral‑to‑slightly‑warm colour. The Radiance version is a touch warmer still and will throw a deliberate blue streak flare when you point a hard source into it.

---

## Standard Supreme Prime vs. Supreme Prime Radiance

| | **Supreme Prime** | **Supreme Prime Radiance** |
|---|---|---|
| Coating | T\* (maximum flare suppression) | **T\* blue** — reworked formula that *lets* the lens flare in a planned, repeatable way while holding contrast and transmission |
| Flare | Very contained; clean specular highlights, no veiling flare | Consistent, controllable **blue / crystalline streak and halo** flare when a hard source is in or near frame; "classic cinema" flare on demand |
| Colour / contrast | Neutral, high micro‑contrast | Renders **slightly warmer**; contrast held even while flaring; helps a wide range of skin tones |
| Rendering | Gentle sharpness, smooth falloff | Same optical base — "soft but with sharpness," extreme smoothness + high definition |
| Focal lengths | 15–200 mm (14) | 18–135 mm (11) |
| Body / gears / size / weight | — | Mechanically and dimensionally the same as the standard Supreme Prime of the matching focal length |

**Paste‑ready — standard Supreme Prime look:**
`Shot on a ZEISS Supreme Prime, wide-open T1.5 character: gentle organic sharpness, smooth focus falloff, elegant round bokeh, contained flare with no veiling wash, neutral color.`

**Paste-ready — Radiance look (no flare in frame):**
`Shot on a ZEISS Supreme Prime Radiance: gentle sharpness, smooth creamy falloff, slightly warm rendering, elegant round bokeh, high contrast held into the shadows.`

**Paste-ready — Radiance with a flare beat:**
`ZEISS Supreme Prime Radiance flare: a hard light source clips the edge of frame and throws a controlled crystalline blue streak and soft halo across the image, contrast holding, no loss of detail.`

> Use the flare phrase only when there is a **motivated** hard source (sun, practical bulb, headlight, window). Unmotivated, it reads as a render error. Keep it to one shot per sequence unless flare is the signature of the whole treatment.

---

## Per‑lens specification table

Close‑focus values confirmed against the focus‑scale engravings in the supplied DoF manual. Angle of view = horizontal, Full Frame / Super 35.

| Focal | T‑stop | Close focus (MOD) | Front Ø | Length | Weight | HFOV FF / S35 | In the Radiance set? |
|---|---|---|---|---|---|---|---|
| **15 mm** | T1.8–22 | 0.35 m (14") | 114 mm | 149 mm | 2.24 kg | 98.9° / 77.9° | No |
| **18 mm** | T1.5–22 | 0.35 m (14") | 114 mm | 163 mm | 2.27 kg | 88.4° / 67.9° | Yes |
| **21 mm** | T1.5–22 | 0.35 m (14") | 95 mm | 120 mm | 1.61 kg | 79.5° / 59.8° | Yes |
| **25 mm** | T1.5–22 | 0.26 m (10") | 95 mm | 119 mm | 1.42 kg | 70.8° / 52.3° | Yes |
| **29 mm** | T1.5–22 | 0.33 m (13") | 95 mm | 121 mm | 1.61 kg | 64.0° / 46.8° | Yes |
| **35 mm** | T1.5–22 | 0.32 m (13") | 95 mm | 119 mm | 1.40 kg | 55.0° / 39.6° | Yes |
| **40 mm** | T1.5–22 | 0.42 m (17") | 95 mm | 121 mm | 1.49 kg | 47.4° / 33.8° | Yes |
| **50 mm** | T1.5–22 | 0.45 m (18") | 95 mm | 119 mm | 1.22 kg | 39.0° / 27.5° | Yes |
| **65 mm** | T1.5–22 | 0.60 m (2') | 95 mm | 121 mm | 1.63 kg | 30.5° / 21.3° | Yes |
| **85 mm** | T1.5–22 | 0.84 m (2'9") | 95 mm | 119 mm | 1.42 kg | 24.0° / 16.7° | Yes |
| **100 mm** | T1.5–22 | 1.1 m (3'9") | 95 mm | 119 mm | 1.70 kg | 20.4° / 14.2° | Yes |
| **135 mm** | T1.5–22 | 1.4 m (4'6") | 114 mm | 146 mm | 2.27 kg | 15.6° / 10.9° | Yes |
| **150 mm** | T1.8–22 | 1.5 m (5') | 114 mm | 146 mm | 2.27 kg | 13.7° / 9.5° | No |
| **200 mm** | T2.2–22 | 2.0 m (6'6") | 114 mm | 183 mm | 2.87 kg | 10.7° / 7.1° | No |

---

## Per‑lens use guide + paste‑ready phrasing

Each entry: what it's for → how it frames and renders → the phrase to drop in the prompt. "FF" = shot on full‑frame; on Super 35 multiply the effective focal length by ~1.5 (a 35 mm on S35 frames like a ~50 mm on FF).

### Ultra‑wide

**15 mm — T1.8.** Architectural / establishing extreme wide, tight interiors, dramatic foreground‑to‑horizon depth. Near‑rectilinear (very low distortion for the angle). Everything tends to stay sharp; don't ask for shallow DoF here.
`15mm ultra-wide full-frame view, near-rectilinear with minimal distortion, deep foreground-to-horizon depth, everything crisp, gentle ZEISS sharpness.`

**18 mm — T1.5.** Big environmental wide that still lets you go wide‑open for a pool of focus in a dark interior. Strong lead‑room and ceiling/floor in frame.
`18mm wide full-frame view, expansive environment, strong sense of depth and space, clean corners, contained flare.`

**21 mm — T1.5.** Classic "wide master." Walk‑and‑talk, room‑scale coverage, vehicle interiors. Wide enough to feel immersive, controlled enough to avoid a distorted look.
`21mm wide-master full-frame framing, immersive but natural perspective, subject anchored in a legible space.`

### Wide‑normal

**25 mm — T1.5.** Reportage / handheld master, tight spaces, moving with a subject. 0.26 m close focus is the shortest in the set — good for a dramatic wide close‑up with the environment wrapped around the face.
`25mm full-frame, documentary-style wide framing, mild foreground expansion, background kept present and readable.`

**29 mm — T1.5.** The "in the room with them" focal length — group shots, OTS on the wide side, energetic handheld.
`29mm full-frame, natural wide-normal perspective, several subjects held in frame, gentle depth separation at T1.5.`

**35 mm — T1.5.** Everyday storytelling wide. Two‑shots, walking coverage, a wide single that keeps context. The most "invisible" wide — perspective reads as neutral.
`35mm full-frame, neutral storytelling framing, subject and environment balanced, soft background falloff wide open.`

### Normal

**40 mm — T1.5.** Between 35 and 50 — a slightly formal normal. Good default single when 35 feels loose and 50 feels tight. Popular large‑format "hero" focal length.
`40mm full-frame, natural eye-level perspective, subject clearly primary with a soft, legible background.`

**50 mm — T1.5.** The reference normal. Portrait‑friendly single, dialogue OTS, product hero. Perspective matches human vision; shallow but manageable plane at T1.5.
`50mm full-frame normal lens, natural perspective, shallow plane of focus at T1.5, smooth creamy background falloff, round bokeh.`

### Short telephoto / portrait

**65 mm — T1.5.** First "flattering" tele. Clean head‑and‑shoulders, tightening OTS, beginning of background compression. Lightest way to isolate a face from a busy set.
`65mm full-frame short telephoto, mild compression, flattering head-and-shoulders framing, background softened into gentle bokeh.`

**85 mm — T1.5.** Classic portrait / close‑up lens. Strong subject isolation, compressed background, creamy specular bokeh. The go‑to for an emotional single.
`85mm full-frame portrait lens, compressed background rendered as soft round bokeh, tight plane of focus on the eyes, elegant falloff.`

**100 mm — T1.5.** Tele close‑up and detail (hands, objects, macro‑ish inserts at 1.1 m). Noticeable compression; background becomes a wash of tone and shape.
`100mm full-frame telephoto, strong background compression, very shallow focus at T1.5, background dissolved into smooth color and light.`

### Telephoto

**135 mm — T1.5.** Long lens for isolated singles across distance, crowd‑pick‑out, tight inserts. Fast for a 135 — usable wide‑open in low light. Air/haze between camera and subject reads as depth.
`135mm full-frame telephoto, heavily compressed perspective, subject picked cleanly out of a distant soft background, shallow focus.`

**150 mm — T1.8.** Between 135 and 200 — reach with slightly more speed than the 200. Sports‑style singles, wildlife‑style framing, long lens drama.
`150mm full-frame long lens, flattened perspective, isolated subject, distant background compressed into a soft blur.`

**200 mm — T2.2.** Maximum reach. Extreme compression, layers stacked flat, shallow even at T2.2. Long‑lens "watching from afar" or a distant subject against a wall of soft background.
`200mm full-frame super-telephoto, extreme compression, foreground and background layers stacked flat, subject isolated against a fully dissolved background.`

---

## Depth of field — quick reference (from the supplied DoF manual)

The manual publishes tables for five formats. Circle of confusion used:

| Format | Circle of confusion |
|---|---|
| Full Format (full frame) | **0.030 mm** |
| ANSI Super 35 / Normal 35 / APS‑H | **0.025 mm** |
| APS‑C | (tighter — smaller CoC) |

**Focus‑scale engravings (metric).** Every lens is engraved: `INF · 20 · 10 · 7 · 5 · 4 · 3.5 · 3 · 2.5 · 2 · 1.8 · 1.6 · 1.5 · 1.4 · 1.3 · 1.2 · 1.1 · 1.0 …` then, on the wider lenses, finer marks down to close focus (`0.9 · 0.8 · 0.7 · 0.6 · 0.5 · 0.45 · 0.4 · 0.35 …`). Practical takeaway for a rack‑focus prompt: name the *start* and *end* distance in metres and a duration — those are the real marks a focus puller would hit.

**Worked example — 50 mm, Full Frame (CoC 0.030 mm), from the manual:**

| Focus set to | at T1.5 (sharp zone) | at T2.8 (sharp zone) |
|---|---|---|
| 2 m | ≈ 1.93 – 2.07 m (**~14 cm** deep) | ≈ 1.88 – 2.14 m (**~26 cm** deep) |
| 1.5 m | ≈ 1.46 – 1.54 m (~8 cm) | ≈ 1.43 – 1.58 m (~15 cm) |
| ∞ (hyperfocal) | everything from **~55 m** back | everything from **~29 m** back |

So a 50 mm wide‑open on full frame gives you only a hand's width of sharp focus on a subject at 2 m — that is the whole reason a Supreme Prime single looks the way it does. Prompt that as a *result*, not an f‑number:

`Only a few centimeters of the subject's face are in sharp focus; the ears and shoulders already fall into soft blur; the background is fully dissolved.`

### DoF "feel" by focal length (full frame, wide open, subject at a normal working distance)

| Lens | Wide‑open DoF character |
|---|---|
| 15–21 mm | Deep even at T1.5–1.8 — near and far both mostly sharp. Isolation comes from getting *close*, not from the aperture. Don't stack "shallow DoF" language here. |
| 25–35 mm | Moderate — subject sharp, background softened but still readable. Good for "in a place" shots. |
| 40–50 mm | Shallow — clear subject/background separation, background legible as shapes. The balanced default. |
| 65–100 mm | Very shallow — thin plane on the face, background is tone and bokeh only. Portrait / emotional register. |
| 135–200 mm | Extremely shallow + compressed — a sliver of sharpness, everything else a smooth wash. "Observed from a distance." |

Cross‑reference the paste‑ready focus/bokeh phrases in [Depth-of-Field-Library.md](../Depth-of-Field-Library.md); this table just tells you which register each focal length lands in by default.

---

## Selector — which focal length to reach for

| Shot | Default | Notes |
|---|---|---|
| Establishing / landscape / architecture | 18–25 mm | 15 mm only if you need the extreme angle; watch corner subjects |
| Tight interior, room‑scale master | 21–29 mm | 25 mm if you also need very close focus on a foreground face |
| Walk‑and‑talk / handheld coverage | 25–35 mm | 29 mm is the "in the room" sweet spot |
| Neutral single / two‑shot | 35–40 mm | 35 = looser & more context, 40 = more formal |
| Reference normal single, product hero | 50 mm | The default when nothing else is indicated |
| Portrait / emotional close‑up | 85 mm | 65 mm for a slightly wider, less "posed" version |
| Detail / hands / insert | 100 mm | 1.1 m close focus; strong compression |
| Isolated subject across distance, crowd pick‑out | 135 mm | Fast enough to stay wide open in low light |
| Maximum reach / "watched from afar" | 150–200 mm | 200 mm for the flattest, most extreme compression |
| Deliberate blue streak flare beat | any **Radiance** 18–135 mm | Needs a motivated hard source in/near frame |

### Overrides

- **Wide‑angle (15–25 mm) + "shallow depth of field" in the same prompt** → contradictory; the model picks one or blends badly. Drop the shallow‑DoF language and isolate by proximity instead.
- **Multi‑shot sequence** → lock one focal‑length *register* and one Supreme Prime / Radiance choice per treatment, the same way the other libraries lock a movement family and a grade. A cut from "85 mm Supreme Prime, contained flare" to "24 mm Radiance, blue streak" reads as two different cameras.
- **Super 35 reference image** → the field of view is ~1.5× tighter than the numbers above; pick the focal length by the *look you want*, then say "Super 35 framing" so the model doesn't render a full‑frame width.
- **Flare requested but no hard source in the frame** → either add a motivated source to the shot description or drop to the plain Radiance look phrase.

---

## Using this in an image or video prompt

1. **Pick the focal length** from the Selector, using the spec table and DoF "feel" table to sanity‑check framing and separation.
2. **Pick standard vs. Radiance** — Radiance if you want a slightly warmer rendering or a planned flare; standard otherwise.
3. **Drop in one phrase**, in the `[lens/perspective language]` slot of the signature card (if it holds for the whole treatment) or the `[style/mood]` slot of the per‑shot prompt (if it's shot‑specific). Use the per‑lens phrase above, optionally + the matching Radiance look line.
4. **Describe DoF as an observed result**, not an f‑number — see the worked example. The models treat "T1.5" as a mood word; "only the eyes are sharp, the background is fully dissolved" is what actually renders.
5. **Keep it to one lens phrase.** Don't stack "50mm, shallow depth of field, ZEISS, creamy bokeh, cinematic, anamorphic" — pick the focal length phrase + one DoF phrase and stop.

---

## Anti‑patterns

- **Don't quote the spec sheet to the model.** "46.3 mm image circle, 300° focus rotation, 16‑blade iris" means nothing to Seedance/Kling. Translate to look language.
- **Don't put shallow DoF on an ultra‑wide.** Physically contradictory (see overrides).
- **Don't ask for "anamorphic" or "swirly" bokeh** — Supreme Primes are spherical; their bokeh is *round*. Asking for oval bokeh fights the lens character and renders unpredictably.
- **Don't scatter Radiance flare across every shot.** One motivated flare beat per sequence unless flare is the treatment's signature.
- **Don't mix focal‑length registers shot‑to‑shot** in one sequence without a reason — lock the register like a grade.
- **Don't rely on the corrupted brochure PDF in this folder** — it will not open cleanly; use this file or a fresh export.

---

## Sources

- Supplied: `manual-depth-of-field-tables-zeiss-supreme-prime-lenses.pdf` — lens line‑up, T‑stops, focus‑scale engravings, circle‑of‑confusion values, and DoF tables (Full Format / ANSI Super 35 / Normal 35 / APS‑H / APS‑C).
- Supplied but unreadable: `brochure-zeiss-supreme-lenses.pdf` (corrupted content streams).
- [ZEISS — Supreme Prime Lenses](https://www.zeiss.com/photonics-and-optics/us/cinematography/lenses/supreme-prime-lenses.html) — spec table, angle of view, optical‑character copy.
- [ZEISS — Supreme Prime Radiance Lenses](https://www.zeiss.com/photonics-and-optics/us/cinematography/lenses/supreme-prime-radiance-lenses.html) and [ZEISS newsroom — four new Radiance focal lengths (2021)](https://www.zeiss.com/photonics-and-optics/us/home/content/newsroom/news-overview/2021/zeiss-supreme-prime-radiance.html) — T\* blue coating, focal‑length list, flare character.
- [PetaPixel — Supreme Prime Radiance "controlled flares"](https://petapixel.com/2019/11/07/zeiss-new-supreme-prime-radiance-cine-lenses-create-controlled-flares/), [AbelCine — Supreme Prime announcement](https://www.abelcine.com/articles/blog-and-knowledge/tech-news/zeiss-announces-new-supreme-prime-lenses), [B&H Photo spec listings](https://www.bhphotovideo.com/c/product/1411578-REG/zeiss_2202_549_supreme_prime_50mm_t1_5.html) — front diameter, iris blades, focus rotation, mount / metadata, image circle.
