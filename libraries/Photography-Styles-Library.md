# Photography Styles Library

Names the **aesthetic / genre style** of a still — the thing a photographer means by "shoot it like a Helmut Newton" or "make it look like Kodachrome" or "reportage, not posed." Companion to [Camera-Look-Library.md](Camera-Look-Library.md) (which covers *"looks shot on a real camera"* — grain, shutter, lens artifacts) and [Camera-Framing-Angle-Library.md](Camera-Framing-Angle-Library.md) (height / framing / lens). This one sits one level up: it picks the **whole visual register** — lighting philosophy, palette, contrast, subject treatment, era — that those other libraries then execute. It is **two choices, not one**: a *Look* (§2–§7) and a *Stance* (§8) — see §0.

No external source. Compiled from a deep-research pass (Sept 2026) across photography history, practitioner monographs, film-stock references, and AI-prompt style guides; standard photo/cinematography vocabulary translated into paste-ready prompt phrases.

---

## 0. Two axes — pick one from each

A photography style is **two independent choices**, and this library is split accordingly:

| Axis | What it sets | Sections | Rule |
|---|---|---|---|
| **1. The Look** | Lighting philosophy, palette, contrast, grain, era, subject treatment — the visual register | §2–§7 | Pick **one**, hold it across the whole treatment |
| **2. The Stance** | The relationship between photographer, subject and moment — genuine candid / directed candid / posed | §8 | Pick **one**, hold it; default is set by the Look (§8 table) |

They **combine** — "photojournalism look + directed stance" and "e-commerce look + genuine candid" are both valid, and both are things briefs actually ask for. The Look is not a stance and the Stance is not a look; picking only one leaves the other to the model's default (usually stiff, centred, posed).

```
Scene-image generation (SOUL, Stage 2 text-to-image branch)
   → pick ONE Look (§2–§7) + ONE Stance (§8)   ← ASK THE USER, every time (see §1)
   → map Look to a SOUL preset + one aesthetic term; add the Stance term (§9 table)
Stage 4 signature card (video prompt)
   → both carry forward: Look phrase + Stance phrase together fill the [style/mood] slot,
     Look capture notes reconcile with Camera-Look-Library.md in the [finish] slot
```

- **Scene-image generation (SOUL):** the Look becomes a **preset + one term**, the Stance adds **one more term** — SOUL is tuned for short prompts, so do *not* paste the full phrase stacks here (that fights the model — see [SOUL-Image-Generation-Library.md](SOUL-Image-Generation-Library.md) §2, §8). Use the §9 mapping table.
- **Video prompt (Stage 4):** the Look's full paste-ready phrase **plus** the Stance's phrase go in the signature card's `[style/mood]` slot, held constant across the treatment — same discipline as the lens/perspective register and base camera body.
- **One Look + one Stance per treatment.** Mixing "film noir" and "sun-drenched Testino" across shots that cut together breaks the squint test; so does flipping candid↔posed mid-set. Pick once, hold both.

### "Documentary" — which do you mean?

The word is used three ways; disambiguate before locking it:

| If they mean… | It's a… | Use |
|---|---|---|
| Grainy B&W, available light, handheld, 35mm — *the capture look* | **Look** (§4) | "Photojournalism / war" or "Street photography" row |
| Camera observes, subject unaware, nothing staged — *the stance* | **Stance** (§8) | `genuine candid` (or `fly-on-the-wall`) |
| "Real-feeling but we'll direct it" — wedding/event/brand *marketing label* | **Stance** (§8) | `directed candid` — and if the look should also read reportage, that combination has a name: **posed photojournalism** (§8) |

---

## 1. Mandatory style question (scene-image generation)

**Every time** you are about to write a scene-image generation prompt (SOUL text-to-image, or any generated establishing / environment / product / location still), ask the user for **both** axes before writing the prompt. Do not default silently on either.

Ask it like this:

> **1 — Which look should this scene use?** Pick one (or describe your own):
> a named film-stock look (Kodachrome, Portra, CineStill 800T…), a cinematic register (film noir, neo-noir/neon, anamorphic, teal-orange, chiaroscuro/low-key, high-key), a documentary/street *look* (photojournalism, direct-flash snapshot, provoke-era), a studio/portrait register (Old Hollywood glamour, beauty, e-comm, environmental, fine-art, lifestyle), a fashion-editorial auteur (Newton, Avedon, Penn, Bourdin, Lindbergh, Testino, LaChapelle…), a landscape/technical register (Ansel Adams, long-exposure, tilt-shift, aerial, astro, architectural), or an art-movement register (Pictorialism, f/64, New Topographics, Düsseldorf School, New Color, Constructivism).
>
> **2 — What stance: candid, directed, or posed?**
> • **genuine candid** — subject unaware, nothing staged (street, paparazzi, fly-on-the-wall)
> • **directed candid** — subject aware, a natural-looking action is prompted/staged, no held pose (lifestyle, reportage wedding, "authentic" brand). Reportage/photojournalism *look* + this stance = **posed photojournalism**.
> • **posed** — subject arranged and holding, usually to camera (studio portrait, e-comm, beauty, product)
> If they don't say, use the default stance for the chosen look (§8 table) and state which one you applied.

If the brief already names or implies either axis, still state what you're locking for both and confirm — don't skip the confirmation.

Record **both** the locked look and the locked stance in the generation log alongside the SOUL preset, and carry them into the Stage 4 signature card unchanged.

---

## 2. Cinematic looks *(Look — axis 1)*

| Style | Paste-ready phrase (Stage 4 `[style/mood]`) | Practitioners / era | Negative exclusions |
|---|---|---|---|
| **Film noir** | `film noir, low-key chiaroscuro, hard single key light, deep black shadows with no fill, venetian-blind slat shadows, high-contrast black and white, wet reflective street at night, cigarette-smoke haze, Dutch angle, 1940s Hollywood` | John Alton, Nicholas Musuraca, John F. Seitz; 1940–58 | `soft light, flat lighting, low contrast, HDR, color, fill light, bright, cheerful` |
| **Neo-noir (desaturated)** | `neo-noir, washed-out desaturated palette, pre-flashed muted color, overcast melancholy, 1970s crime drama` | Gordon Willis, Robby Müller; 1970s | `saturated, punchy, neon, high-key, warm glow` |
| **Neo-noir (neon)** | `neo-noir, neon-lit rain-slick street, uncorrected colored gels, magenta and cyan light, sodium-vapor amber, moody underexposed, deep shadows with colored highlights, 1980s` | Jordan Cronenweth (*Blade Runner*), Dante Spinotti; 1980s+ | `even exposure, daylight-balanced, natural color, flat, low saturation` |
| **Anamorphic cinematic** | `anamorphic lens, 2.39:1 widescreen, horizontal blue lens flare, oval bokeh, shallow depth of field, subtle lens distortion, soft smeared corners, filmic highlight bloom, 35mm cinema` | Panavision; PT Anderson, Villeneuve, Deakins, van Hoytema | `1:1 aspect ratio, circular bokeh, deep focus, clinical sharpness, no flares` |
| **Teal-and-orange** | `teal and orange color grade, complementary scheme, warm skin tones against cool blue-teal background, crushed blacks, high-contrast digital-intermediate finish, blockbuster grade` | Michael Bay, Tony Scott; Deakins (justified version); mid-2000s+ | `muted palette, monochrome, green cast, pastel, natural color` |
| **Chiaroscuro / low-key** | `chiaroscuro, low-key lighting, single dominant light source, deep shadow over most of frame, Rembrandt triangle, dark near-black background, high lighting ratio 8:1, candlelit, Caravaggio` | Painters → Karsh, still life, noir | `high-key, flat even light, bright background, soft fill, low contrast` |
| **High-key** | `high-key lighting, bright even shadowless illumination, white seamless background, large soft sources plus fill, airy, minimal contrast, luminous, optimistic, overexposed background` | Classical Hollywood comedy; 1980s beauty; Apple lifestyle | `shadows, dark background, moody, high contrast, chiaroscuro, vignette` |
| **Wes Anderson** | `symmetrical centered composition, flat frontal staging, pastel palette, planimetric framing, deadpan, meticulous production design, twee` | Wes Anderson | `asymmetric, handheld, gritty, desaturated, naturalistic clutter` |
| **Deakins naturalism** | `motivated natural light, single justified source, warm backlight against cool key, restrained, silhouettes, no over-lighting, understated cinematic` | Roger Deakins | `over-lit, flat fill, theatrical gels, high-key, busy` |

---

## 3. Film-stock emulations

**Prompt rule:** name the stock, then spell out grain + contrast + colour cast (models don't reliably "know" the emulsion). Optionally add the scan pipeline (`lab-scanned on a Fuji Frontier`, `drum-scanned`) for extra authenticity.

| Stock | Paste-ready phrase | Character / era | Negative exclusions |
|---|---|---|---|
| **Kodachrome 64** | `shot on Kodachrome 64, rich saturated reds, deep dense blacks, fine grain, high-contrast slide film, warm-neutral midtones, 1970s National Geographic, painterly color transparency` | Dense, archival, Americana; 1935–2009 | `washed out, low saturation, cool cast, heavy grain, faded` |
| **Kodak Portra 400** | `Kodak Portra 400, soft natural skin tones, warm rose-amber cast, low contrast, gentle highlight roll-off, fine grain, overexposed half a stop, pastel color, medium format` | The default "pretty film"; weddings, editorial | `high contrast, saturated, punchy, digital clarity, cool blue cast` |
| **Kodak Gold 200** | `Kodak Gold 200, warm golden cast, 1990s drugstore film, nostalgic, moderate grain, slightly soft, amateur family-snapshot color` | Nostalgic consumer | `clinical, neutral white balance, tack sharp, professional studio` |
| **Kodak Ektar 100** | `Kodak Ektar 100, ultra-saturated, vivid blue sky, very fine grain, punchy contrast, cool-leaning, landscape color negative` | Punchy, product/landscape | `muted, grainy, warm pastel, soft` |
| **Kodak Tri-X 400** | `Kodak Tri-X 400, black and white, gritty grain, high contrast, pushed to 1600, deep blacks, photojournalism, grainy reportage, 35mm` | Street / photojournalism classic; 1954 | `smooth tonality, low contrast, color, fine grain, clean` |
| **Ilford HP5 Plus 400** | `Ilford HP5 Plus, black and white, moderate grain, soft highlight contrast, rich shadow detail, classic reportage, 35mm` | Gentler documentary B&W | `harsh contrast, blown highlights, color` |
| **Kodak T-Max 100** | `Kodak T-Max 100, ultra-fine tabular grain, smooth tonal gradation, sharp, fine-art black and white, large format` | Clinical fine-art B&W | `grainy, gritty, contrasty, lo-fi` |
| **Fuji Velvia 50** | `Fujifilm Velvia 50, hyper-saturated, vivid greens and reds, very high contrast, deep shadows, ultra-fine grain, dramatic landscape slide film` | Hyper-real landscape; 1990 | `muted, pastel, low contrast, flat, faded` |
| **Fuji Pro 400H** | `Fuji Pro 400H, cool pastel tones, minty green cast, airy, low contrast, soft highlights, light-and-bright wedding film` | "Light and airy" (vs Portra's warmth) | `warm, saturated, contrasty, moody` |
| **Kodak Ektachrome E100** | `Kodak Ektachrome E100, clean neutral color, slight cool cast, fine grain, crisp editorial transparency, 1990s magazine` | Editorial slide reference | `warm, heavy grain, low contrast, muddy` |
| **CineStill 800T** | `CineStill 800T, tungsten white balance, cool blue cast, red-orange halation glow around bright point lights, neon night, grainy, cinematic street at night, motion-picture stock` | The "neon night city" look; 2012 | `daylight balance, warm, no halation, clean highlights, sharp` |
| **Cross-processed (x-pro)** | `cross-processed film, x-pro, green-yellow color shift, high contrast, crushed cyan shadows, blocked blacks, grainy, unpredictable color cast, 1990s music editorial` | Lomo / '90s music & skate press | `accurate color, neutral white balance, natural skin tones` |
| **Lomography / Holga** | `lomography, toy camera, heavy corner vignette, light leaks, red streak, oversaturated cross-processed color, plastic-lens softness, chromatic aberration, Holga medium format, lo-fi analog` | Lomographic Society, 1992 | `sharp, corrected optics, even exposure, no vignette, clean` |
| **Kodak Aerochrome (colour IR)** | `Kodak Aerochrome, color infrared film, magenta-pink foliage, crimson trees, deep blue sky, waxy pale skin, surreal false color` | Richard Mosse (*Infra*); military origin, disc. ~2009 | `natural green foliage, realistic color` |
| **B&W infrared** | `black-and-white infrared photography, Wood effect, glowing white foliage, near-black sky, milky dreamy haze, soft glow, 720nm filter` | Fine-art IR | `natural tonality, green foliage, normal sky` |

---

## 4. Documentary / street / photojournalism *(Look — axis 1; this is the capture look, not the stance)*

This section is the **capture look** — grain, B&W, available light, handheld, 35mm. It does *not* set the stance: pair it with a §8 stance. Default stance for every row here is **genuine candid**, except where a brief says otherwise (a directed shoot in a photojournalism look = **posed photojournalism**, §8). "Reportage" as a *stance* lives in §8; here it only means the look.

| Style (look) | Paste-ready phrase | Practitioners / era | Negative exclusions |
|---|---|---|---|
| **Street photography** | `candid street photography, 35mm lens, available light, decisive moment, black-and-white Tri-X grain, high contrast, shot from within the crowd, tilted frame, layered composition, mid-century city sidewalk` | Cartier-Bresson (50mm), Winogrand (28mm), Frank, Maier | `posed, studio lighting, shallow bokeh portrait, staged, retouched` |
| **Photojournalism / war** | `war photojournalism, 35mm reportage, grainy black and white, Tri-X pushed to 1600, available light, motion blur, handheld, close to the action, dark printed sky, unstaged, gritty` | Capa, W. Eugene Smith, Don McCullin, Nachtwey; Magnum, *Life* | `clean, staged, studio, color-graded, sharp tripod shot, glamorous` |
| **Direct-flash snapshot** | `direct on-camera flash, harsh frontal flash, hard flash shadow on the wall behind the subject, snapshot aesthetic, red-eye, blown-out foreground falling to black, casual tilted framing, plain wall, 1990s party photo` | Weegee → Nan Goldin, Larry Clark, Martin Parr, Terry Richardson, Juergen Teller | `soft studio lighting, diffused, flattering, cinematic, shallow depth of field, retouched, moody` |
| **Provoke era / are-bure-boke** | `are-bure-boke, Provoke-era Japanese photography, extreme coarse grain, very high-contrast black and white, motion blur, out of focus, blown highlights, crushed blacks, harsh flash, tilted fragmentary framing, raw gritty Tokyo street, 1960s` | Daido Moriyama, Takuma Nakahira; *Provoke* 1968–69 | `sharp, well-composed, balanced exposure, fine grain, clean, color` |
| **British social documentary** | `British social documentary, working-class daily life, flash-lit interior, muted color or black and white, deadpan wit, 1980s` | Martin Parr, Chris Killip, Tish Murtha | `glamorous, staged, warm nostalgic, studio` |
| **Grunge / heroin-chic editorial** | `early-1990s grunge editorial, desaturated green cast, harsh flash or bleak daylight, waifish, squalid apartment, snapshot framing` | Corinne Day, David Sims; *The Face*, early-'90s | `polished, glossy, saturated, glamour lighting, healthy glow` |

---

## 5. Studio & portrait

| Style | Paste-ready phrase | Practitioners / era | Negative exclusions |
|---|---|---|---|
| **Old Hollywood glamour** | `1930s Hollywood glamour portrait, hard Fresnel key light, butterfly lighting, hard rim and hair light, glossy black background, luminous heavily-retouched skin, high-contrast black and white, satin and sequins, cigarette smoke, dramatic diagonal pose` | George Hurrell, Clarence Sinclair Bull; 1930s–40s | `softbox, natural light, candid, color, matte, low contrast, environmental` |
| **Beauty / cosmetics** | `beauty photography, ring light or beauty dish, flawless dewy skin, macro detail on eyes and lips, catchlights top and bottom, 100mm macro, seamless pastel background, symmetrical, cosmetics campaign` | Cosmetics advertising; Sølve Sundsbø, Ben Hassett | `dramatic shadow, environmental, wide shot, gritty texture, low-key` |
| **Fashion e-commerce** | `e-commerce fashion photography, white seamless background, even high-key lighting, full-length, color-accurate garment, neutral white balance, sharp front to back, minimal shadow, catalog` | Catalog / online retail | `moody, colored gels, motion blur, environmental, shallow bokeh, film grain` |
| **Environmental portrait** | `environmental portrait, subject in their own workplace, 35mm lens, natural window light with subtle fill, context-rich background of equal weight, medium depth of field, direct gaze` | Arnold Newman (coined term, 1946), Annie Leibovitz, Dan Winters | `plain seamless backdrop, studio, isolated subject, extreme bokeh` |
| **Fine-art portraiture** | `fine-art portrait, north-window light, medium format, muted restrained palette, formal three-quarter pose, neutral contemplative expression, dark ground, minimal retouching, painterly, per-pore detail` | August Sander, Rineke Dijkstra, Paolo Roversi, Thomas Ruff | `glamour retouching, commercial, saturated, busy background, snapshot` |
| **Boudoir / glamour** | `boudoir photography, soft warm window light, backlit rim light, hazy Pro-Mist filter, shallow depth of field 85mm f/1.4, intimate bedroom, sheer drapery, film grain, low-key warm` | 1920s "French postcard" → David Hamilton; Playboy studio | `hard flash, cool light, wide angle, clinical, deep focus, explicit` |
| **Lifestyle** | `lifestyle photography, natural window light, candid interaction, subjects laughing not looking at camera, warm airy tones, 35mm, shallow depth of field, authentic lived-in moment, art-directed but natural, Kinfolk aesthetic` | 2000s–2010s advertising/stock; Airbnb, *Kinfolk* | `posed to camera, studio seamless, hard flash, high saturation, staged stiffness` |
| **Product / hero pack shot** | `product photography, controlled gradient reflector lighting, defined edge highlights, clean white sweep, focus-stacked front to back, subtle reflection, high-end commercial` | Commercial / advertising | `available light, snapshot, cluttered background, motion blur, film grain` |
| **Old Master still life** | `Old Master still life, single raking window light, dark background, chiaroscuro, Dutch/Flemish arrangement, deep shadow, rich surface texture, oil-painting look` | Caravaggio / Dutch Golden Age reference | `flat even light, bright background, high-key, modern minimal` |

---

## 6. Fashion-editorial auteurs

Naming the photographer is the strongest single cue — pair it with 2–3 descriptors as fallback.

| Auteur | Paste-ready phrase | Era / bodies of work | Negative exclusions |
|---|---|---|---|
| **Helmut Newton** | `Helmut Newton, high-contrast black and white, hard flash on location, poolside Riviera, powerful woman in stilettos, voyeuristic, cinematic staging, cold glamour, 1970s French Vogue` | *White Women* (1976), *Big Nudes*; French *Vogue*, *Stern* | `soft romantic light, candid warmth, natural no-makeup, low contrast` |
| **Richard Avedon** | `Richard Avedon, stark white seamless background, hard even frontal strobe, sharp full-tonal black and white, no props, subject in motion mid-jump, or brutally frontal 8x10 portrait with every pore` | *Harper's Bazaar* 1945–65; *In the American West* (1985) | `environmental background, moody shadow, colored gel, soft focus` |
| **Irving Penn** | `Irving Penn, north-skylight daylight studio, plain grey backdrop, muted neutral palette, meticulous minimal composition, refined tonal range, elegant, form over ornament` | *Vogue* from 1943; *Moments Preserved* (1960) | `dramatic gels, busy set, snapshot, oversaturated, motion` |
| **Guy Bourdin** | `Guy Bourdin, hyper-saturated color, glossy lacquer red, hard graphic lighting, surreal cropped disorienting composition, cinematic unease, mannequin-like pose, 1970s French Vogue advertising` | French *Vogue*, Charles Jourdan campaigns; 1955–80s | `natural color, candid, soft light, documentary, wholesome` |
| **Peter Lindbergh** | `Peter Lindbergh, black and white, soft overcast daylight, minimal retouching, natural visible skin texture and lines, windswept, white shirt, industrial location, emotional, early 1990s` | British *Vogue* Jan 1990 supermodel cover; Pirelli | `heavy retouching, glossy color, studio strobe, glamour, flawless plastic skin` |
| **Mario Testino** | `Mario Testino, warm sun-drenched light, glossy vibrant color, spontaneous laughing pose, glowing healthy skin, luxurious yet approachable, 2000s Vogue` | *Vogue*, *Vanity Fair*, Gucci/D&G; 1990s–2000s | `moody, desaturated, stiff formal pose, hard shadow, film noir` |
| **Steven Meisel** | `Steven Meisel, Vogue Italia editorial, conceptual fashion narrative, impeccable studio lighting craft, cinematic pastiche, controlled color palette` (better: also name the sub-genre he emulates) | *Vogue Italia* covers for decades; *W* | `snapshot, amateur, single flat setup` |
| **David LaChapelle** | `David LaChapelle, hyper-saturated fluorescent color, elaborate built set, theatrical multi-source lighting, glossy surreal tableau, maximalist, kitsch pop, Baroque excess, celebrity spectacle` | *Interview*, *Rolling Stone*, i-D; late-1980s+ | `minimal, muted, natural light, candid, understated, documentary` |
| **Herb Ritts** | `Herb Ritts, black and white, hard California sun, sculptural muscular bodies, clean sky backdrop, sensual graphic form` | 1980s–90s | `soft flat light, busy environment, color, casual snapshot` |
| **Tim Walker** | `Tim Walker, whimsical fantasy, oversized handmade props, painterly pastel sets, storybook staging, English eccentric` | British *Vogue*; 2000s+ | `minimal, gritty, documentary, desaturated, corporate` |
| **Paolo Roversi** | `Paolo Roversi, 8x10 Polaroid, dark backdrop, ethereal soft frontal light, dust-and-shadow romance, faded muted color, painterly` | Studio Luce, Paris | `hard flash, high contrast, saturated, sharp clinical, bright` |

---

## 7. Landscape & technical genres

| Style | Paste-ready phrase | Practitioners / era | Negative exclusions |
|---|---|---|---|
| **Ansel Adams / Zone System** | `Ansel Adams, large-format black-and-white landscape, full tonal range from textured black to luminous detailed white, red-filter dramatic sky, front-to-back sharp focus, f/64, monumental Western wilderness, contact-print clarity` | Adams & Fred Archer; Group f/64 (1932); *Moonrise, Hernandez* (1941) | `color, shallow depth of field, soft focus, low contrast, snapshot, handheld blur` |
| **Long-exposure** | `long exposure, 10-stop ND filter, silky smooth water, blurred streaking clouds, light trails, ghosted figures, tripod-locked sharp static elements, minimalist, ethereal` | Michael Kenna, Hiroshi Sugimoto (*Seascapes*) | `frozen motion, sharp waves, handheld, busy, high shutter speed` |
| **Tilt-shift / miniature** | `tilt-shift lens, miniature-faking, narrow selective focus band, exaggerated blur top and bottom, high vantage angle, boosted saturation and contrast, toy-model effect` | Olivo Barbieri (*site specific_*), Vincent Laforet | `even focus, eye-level, converging verticals` |
| **Aerial / drone** | `aerial drone shot, top-down bird's-eye view, golden-hour raking light, long shadows, strong graphic pattern, tiny figures for scale, wide angle, deep focus, ultra-smooth` | Yann Arthus-Bertrand (*Earth from Above*), Edward Burtynsky | `eye-level, close-up, shallow depth of field, static tripod` |
| **Astrophotography** | `astrophotography, Milky Way core arching over a dark landscape, thousands of stars, deep blue-black sky with faint airglow, 14mm f/2.8, high ISO grain, moonlit silhouetted foreground, nightscape` | — | `daylight, light-pollution glow, blurred stars, low ISO clean` |
| **Architectural** | `architectural photography, corrected parallel verticals, tilt-shift lens, blue-hour dusk shot, warm interior lights against cobalt sky, symmetrical, 17mm, deep focus, clean sky, unpopulated` | Julius Shulman (*Case Study House #22*, 1960), Ezra Stoller, Iwan Baan | `converging verticals, keystone distortion, harsh midday, cluttered, crowds` |
| **Macro** | `macro photography, 1:1 magnification, 100mm macro lens, extreme close-up, razor-thin depth of field, creamy fully-dissolved background, ring-flash catchlights, dewdrop refraction detail, focus-stacked subject` | — | `wide shot, deep focus, environmental context, soft detail` |

---

## 8. The Stance axis — candid / directed / posed

**Axis 2.** Sets the **relationship between photographer, subject, and moment** — orthogonal to the Look (§2–§7). Load-bearing because "candid" is one of the strongest single cues for defeating the stiff, centred, eye-contact "AI portrait" default. Runs: **genuine candid** (subject unaware) → **directed candid** (subject aware, natural-looking action staged) → **posed** (subject arranged and holding).

Pick one. If the brief is silent, apply the **default for the chosen Look**:

| Look (§2–§7) | Default stance | Common override |
|---|---|---|
| Street photography, Photojournalism/war, Provoke, Aerochrome-of-people | **genuine candid** | posed photojournalism (directed) for staged portraits in that look |
| Lifestyle, Kinfolk, "authentic" brand, wedding/event | **directed candid** | genuine candid for true fly-on-the-wall coverage |
| Direct-flash snapshot, grunge/heroin-chic | **directed candid** | genuine candid (Goldin's own work sits here) |
| Beauty, E-commerce, Product, Old Hollywood glamour, Old Master still life | **posed** | — |
| Environmental portrait, Fine-art portrait, most auteur work (Newton, Avedon, Penn, Bourdin, LaChapelle) | **posed** (aware, engaging the lens) | directed candid for Testino/Lindbergh-style "spontaneous" frames |
| Landscape & technical (no people) | n/a — stance doesn't apply | — |

### Primary stances

| Stance | Paste-ready phrase (add to `[style/mood]` after the Look phrase) | Meaning / origin | Negative exclusions |
|---|---|---|---|
| **Genuine candid** | `genuine candid, unposed, caught mid-motion, not looking at camera, unaware of the camera, spontaneous moment, off-center framing, decisive moment` | Subject unaware; photographer changes nothing. Cartier-Bresson's "decisive moment" (*Images à la Sauvette*, 1952). | `posed, looking at camera, direct eye contact, stiff, symmetrical, retouched, staged, holding a pose` |
| **Directed candid** | `candid-style but composed, subject interacting and laughing, walking and talking, mid-gesture, not posed for the camera, gentle natural direction, naturalistic, unscripted feel` | Subject aware; photographer prompts/stages a natural-looking action, then shoots the real reaction. Dominant mode of modern wedding, lifestyle & "authentic" advertising. Synonyms: *prompted candid*, *guided candid*, *semi-posed*, *docu-style*, *storytelling*; film term *blocking*. | `stiff studio pose, holding a pose, formal group lineup, direct eye contact, seamless backdrop, over-retouched` |
| **Posed** | `posed, subject arranged and holding the pose, deliberate composition` (add `direct eye contact` unless the look is away-gaze) | The staged pole — state it explicitly when you want it; it's also the model's default, so naming it mainly buys precision on gaze/composition. | `candid, motion blur, accidental framing, caught unaware, snapshot` |

### Secondary / variant stances

| Variant | Paste-ready phrase | Sits at | Notes |
|---|---|---|---|
| **Paparazzi** | `paparazzi shot, long telephoto lens, compressed perspective, subject unaware or evading, harsh on-camera night flash, imperfect framing, shot through a gap` | genuine candid pole | Long-lens predatory grammar; overrides most Look lighting |
| **Fly-on-the-wall / observational** | `fly-on-the-wall, observational, camera present but non-participating, subjects behaving as if it weren't there, invisible presence` | genuine candid pole | Direct Cinema / cinéma vérité (Maysles, Wiseman). This is the *stance* sense of "documentary" |
| **Posed photojournalism** *(hybrid)* | Look = a §4 photojournalism/reportage row **+** stance phrase `directed, staged to look like reportage, subject aware but acting naturally, no held pose, editorial documentary framing` | between directed candid and posed | The named look+stance combo for wedding/event/editorial "reportage" that is actually lightly directed. Distinct from real §4 photojournalism, which is genuine candid |
| **Environmental portrait** | see §5 — subject aware, often engaging the lens, placed in a meaningful setting of equal weight | posed / directed border | It's a Look (§5) with a built-in aware stance; listed here only as a pointer |

### Key distinction to encode

- **Genuine candid** = *subject unaware, nothing changed.* Reach for `unaware of the camera`, `caught`, `grab shot`, long-lens compression; keep the full anti-pose negative set. Loosen lighting and composition too — it should not look lit.
- **Directed candid** = *subject aware, action staged to look natural.* Reach for `candid-style but composed`, `interacting, not looking at camera`, `gentle natural direction`. Keep `posed / stiff / eye contact / seamless backdrop` negative — but **allow** good light and deliberate framing.
- **Posed** = *subject arranged and holding.* Usually to camera; name the gaze explicitly.
- Shared core negatives for the two candid stances: **`posed, looking at camera, stiff, symmetrical, retouched, holding a pose`**.

---

## 9. Style → SOUL preset mapping (scene-image generation)

For **SOUL text-to-image** (Stage 2 branch), build the prompt tail as: **preset + one Look term + one Stance term** — never the full §2–§8 phrase stacks (that fights SOUL; see [SOUL-Image-Generation-Library.md](SOUL-Image-Generation-Library.md) §2, §8). Set `style_strength` ~1.0 for full commitment, ~0.5 for a hint. Presets are a live in-app list — names below are the common ones; browse for the closest match.

### 9a. Look → preset + Look term

| Locked look | SOUL preset (closest) | One Look term to append | Notes |
|---|---|---|---|
| Film noir / chiaroscuro / low-key | `Theatrical light` | `film noir, hard single key, deep shadow` | Expect partial compliance on pure-black shadows; finish in Stage 4 |
| Neo-noir neon / CineStill 800T / cyberpunk | `Subtle flash` + `Theatrical light` | `neon night, tungsten blue, red halation` | SOUL's flash bias helps here |
| High-key / beauty / e-commerce | `General` / `Realistic` | `soft even studio light, white seamless` | SOUL resists "clean" — accept some grain, or fix at QC |
| Kodachrome / New Color (Eggleston, Shore) | `2000s Cam` or `General` | `saturated 1970s color, dye-transfer` | — |
| Portra / Pro 400H / light-and-airy | `Nature light` / `Warm ambient` | `pastel film, soft roll-off` | — |
| Tri-X / HP5 / photojournalism / street | `General` (mono in post) or a B&W preset | `black and white, grainy Tri-X, 35mm reportage look` | — |
| Direct-flash snapshot / Nan Goldin / Parr | `Subtle flash` or `2000s Cam` | `direct on-camera flash, hard wall shadow` | Strong native match — SOUL is built for this |
| Provoke / are-bure-boke | `2000s Cam` at high strength | `extreme grain, high contrast, motion blur` | — |
| Old Hollywood glamour | `Theatrical light` | `1930s Hollywood glamour, hard rim light, glossy black` | — |
| Lifestyle / Kinfolk | `Nature light` + `Editorial street style` | `lifestyle, warm airy, lived-in` | — |
| Environmental portrait | `Nature light` | `environmental portrait, workplace setting` | — |
| Fashion-editorial auteur (Newton/Testino/etc.) | `Editorial street style` or `Theatrical light` | the auteur's name + one descriptor | Auteur name carries most of the load |
| LaChapelle / Bourdin / maximalist | `Theatrical light` at full strength | `hyper-saturated, elaborate staged set, surreal` | — |
| Ansel Adams / landscape technical | `General` | `large-format black and white, deep tonal range` | Technical genres (tilt-shift, astro, long-exposure) are mostly a Stage-3 concern; SOUL just needs the base register. No people → skip the Stance term |
| Pictorialism / painterly art-movement | `General` low strength | `soft-focus pictorialism, atmospheric haze, sepia` | — |

If no preset fits, use `General` at `style_strength` 1.0 and carry the full look into Stage 4 instead.

### 9b. Stance → Stance term (append after the Look term; skip if no people in frame)

| Locked stance | One Stance term to append | Preset nudge |
|---|---|---|
| **Genuine candid** | `genuine candid, unaware of the camera, caught mid-motion, not looking at camera` | lean `iPhone` / `Old smartphone` — reads unstaged |
| **Paparazzi** (candid variant) | `paparazzi, long lens, subject unaware, harsh night flash` | `Subtle flash` |
| **Directed candid** | `candid interaction, not looking at camera, natural gesture, unscripted feel` | keep the Look's preset |
| **Posed photojournalism** (hybrid) | `directed but reportage-style, subject aware acting naturally, no held pose` | pair with a Tri-X / photojournalism Look row |
| **Posed** | `posed, direct eye contact` (or name the gaze) | keep the Look's preset — this is also SOUL's default |

---

## 10. Selector — which style for which brief

Look and stance are chosen separately. First table picks the Look; second picks the Stance.

**Look:**

| Brief / mood | Reach for (Look) |
|---|---|
| Premium, warm, aspirational | Lifestyle · Testino · Portra 400 · golden-hour |
| Cold, powerful, luxury-with-an-edge | Helmut Newton · neo-noir · high-contrast B&W |
| Nostalgic / memory / warmth | Kodachrome · Kodak Gold · Portra · faded film |
| Gritty, real, unvarnished | Photojournalism (Tri-X) · direct-flash snapshot · British social documentary |
| Night city / neon / genre | CineStill 800T · neo-noir neon · cyberpunk |
| Clean, clinical, catalog | E-commerce · beauty · high-key |
| Dramatic single-subject beat | Chiaroscuro / low-key · Old Hollywood glamour · Theatrical |
| Surreal, loud, maximalist | LaChapelle · Bourdin · Aerochrome |
| Epic / monumental / scale | Ansel Adams · aerial drone · Düsseldorf School (Gursky) |
| Deadpan, banal-on-purpose, conceptual | New Topographics · Düsseldorf School · New Color (Shore) |

**Stance:**

| Brief cue | Reach for (Stance) |
|---|---|
| "Caught in the moment", "they don't know", street, paparazzi | **genuine candid** |
| "Feels real but we'll art-direct it", wedding/event, "authentic" brand, lifestyle | **directed candid** |
| Reportage/documentary *look* but a planned shoot | **posed photojournalism** (photojournalism Look + directed) |
| Catalogue, campaign hero, headshot, product, beauty | **posed** |
| "Documentary" (unqualified) | stop — disambiguate per §0 box before locking |

---

## 11. Anti-patterns

- **Don't stack two Looks.** One Look per treatment. "Film noir meets Testino" is not a style, it's a note that you haven't chosen. (Stacking a Look *and* a Stance is correct — that's the two-axis design, §0.)
- **Don't skip the Stance.** A Look with no stance chosen leaves it to the model, which defaults to stiff and posed-to-camera. If people are in frame, lock a §8 stance even when the answer is "posed".
- **Don't confuse the two senses of "documentary".** It's a Look (§4 grain/handheld) *or* a Stance (§8 fly-on-the-wall) — never assume which; disambiguate per the §0 box.
- **Don't paste the full phrase stacks into SOUL.** Use the §9 preset + one Look term + one Stance term. The stacks are for the Stage 4 video prompt only. (Same rule as [SOUL-Image-Generation-Library.md](SOUL-Image-Generation-Library.md) §8 "don't stack camera/film/lens on top of a preset.")
- **Don't let the style fight the base camera body.** If Stage 4's [Camera-Look-Library.md](Camera-Look-Library.md) choice is "ARRI Alexa 35, clean filmic," don't also ask for "coarse 16mm documentary grain" from the style — pick a style whose capture character is compatible, or switch the base body to match.
- **Don't describe a style as an applied filter.** Say "shot on Kodachrome 64, dense saturated color" not "add a Kodachrome filter" — filter phrasing cues a post-processed look, the opposite of the goal (same note as Camera-Look-Library.md's anti-patterns).
- **Auteur names are a register, not a costume.** "Helmut Newton" sets lighting, palette, power dynamic and staging — don't also over-specify every other layer, or the cue gets diluted.
- **Hold both axes across the treatment.** Same Look phrase *and* same Stance phrase in every shot's signature card, exactly like the lens/perspective register and base camera body. Flipping either mid-treatment breaks the Stage 9 squint test.

---

## 12. Negative-prompt additions

Both the Look row (§2–§7) and the Stance row (§8) list their own exclusions — put **both sets** in the Stage 4 negative field. On top of that, every treatment still gets [Camera-Look-Library.md](Camera-Look-Library.md)'s standing anti-digital list:

```
no CGI look, no 3D render, no video game rendering, no plastic or waxy skin, no oversharpened
digital clarity, no flat lifeless highlights, no clipped blown-out whites, no hyper-clean
noise-free image, no digital sheen, no motion interpolation smoothness
```

Do not fold a style's positive descriptors into the negative by accident (e.g. don't negate "grain" when the style *is* grainy). SOUL has no negative field — fold any hard exclusion into the positive as a plain statement and enforce the rest at the QC gate.

---

## 13. Usage notes

- **Signature-card slots:** the Look phrase **and** the Stance phrase together fill `[style/mood]` (Look first, then stance — e.g. `…grainy Tri-X photojournalism, 35mm reportage · directed but reportage-style, subject aware acting naturally, no held pose`). Any capture character the Look implies (film stock, B&W, halation) reconciles with the base camera choice in `[finish: photoreal / commercial / etc.]` — see [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md) Stage 4. Treatment-level, fixed once.
- **Per-shot:** neither axis changes shot to shot. Only restate a detail per shot if it genuinely varies (rare — e.g. one flashback beat in a different stock).
- **Portraits of people:** [realist-portrait](.claude/skills/realist-portrait/SKILL.md) builds its own Realism Stack (lighting, lens, capture). If a portrait needs one of these named looks, name the Look and the Stance up front and let the stack execute them — this library supplies the vocabulary, the portrait skill supplies the layer-by-layer control.
- **Log it:** record the locked Look and Stance in the generation log next to the SOUL preset and the Stage 4 signature card, so every downstream shot reuses the same pair.
