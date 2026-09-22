# Cully Hill Boys — prompt samples (verbatim, study only)

Eight prompts pulled verbatim from the published *Cully Hill Boys* project snapshot on Higgsfield
(`@higgsfield.studio/projects/cully-hill-boys`, publication `0efa70c1-07ec-410a-813b-8629502a7de3`),
read 2026-09-22 through the same public endpoints the project page uses, without signing in.

> **Licence and use.** The project is published under Higgsfield's `HOL-RO` licence (rights-owned). The API marks it
> `is_open_source: false` even though the release calls it "open-sourced". These samples are archived **for study only**.
> Do not lift them into a production prompt. They name cameras, lenses, directors and ages, all of which
> our BAN 1 forbids in *our* output. `<<<uuid>>>` tokens are Higgsfield element IDs, several of which point to
> licensed real-person likenesses. See [../Cully-Hill-Boys-Benchmark.md](../Cully-Hill-Boys-Benchmark.md) for the analysis.

## A. Dialogue scene — full sealed video prompt (Scene 83, 15 s, 4 elements)

- Folder: `/2 ACT (50-93)/83/prg_v1`
- model `seedance_2_0` · 2016×864 · 21:9 · 15 s · 1080p · audio on
- Reference elements: `prop_CB_evictionnote_s83v4` (prop), `char_CB_Maggie_s83_v2` (character), `new_lok_CB_koridor_Kel_v3` (environment), `char_CB_Kel_v7` (character)
- Other inputs: —
- Length: 1333 words

````text
SCENE CONTEXT
Scene 83. EXT. Cal's council-block deck-access walkway, cold overcast afternoon, 2011. One generation, internal montage: Cal finds the court eviction order taped to his door, tears it off and reads it aloud — and on the deadline his unseen landlady Meggie, standing directly behind him, says it in exact unison with him; he crushes the paper, rolls his eyes and deadpans back without turning. Gutted man (his daughter is being moved to Germany); comedy played bone-dry.
ACTIVE REFERENCES
<<<dc97b5e1-9440-4379-a4b8-0cf476facafa>>> — Cal: late-20s, thin, exhausted, stubble + moustache; navy zip hoodie, hood UP (plaid lining), grey cargos, worn blue Adidas. Seen in the wide, then a hand, then a frontal medium. Hollow, despairing, then dead-eyed resignation. 100% matches the reference.
<<<59d76766-4704-44e3-af3c-140017ae9096>>> — Meggie: Black Caribbean-London woman, ~50s, stately/voluptuous; a big, brash, larger-than-life Caribbean-London landlady played as a broad CARICATURE — theatrical and broad, teasing and fierce in the same breath, still a photoreal human (NOT a cartoon render). Wardrobe per the reference: grey hair under a dusty-rose do-rag, big gold hoop earrings + gold chain, quilted grey-blue robe over a mint silk slip, blue fuzzy slippers, a lit cigarette in hand. In THIS shot she stands directly BEHIND Cal, OUT OF FRAME / unseen the whole time — heard only. 100% matches the reference.
<<<b85dac3f-c190-4335-b4c8-9316f0191715>>> — the deck-access balcony walkway (controls geometry, materials, layout, landmark placement, cold light only; do not reuse its camera angle). 100% matches the reference.
<<<2b31223f-f889-4da3-8dff-079d837584b5>>> — a single white A4 court order, taped to the door, then torn off, read and crushed in Cal's hands. 100% matches the reference.
LOCATION MAP (LOCATION LOCK — verbatim across all Scene 83 shots; space per <<<b85dac3f-c190-4335-b4c8-9316f0191715>>>)
Covered exterior deck-access walkway of a red-brick council block. Anchors: red-brick wall with teal-green flat doors along screen-RIGHT; the arched concrete stairwell entry mid-walkway toward screen-CENTRE; CAL's teal HERO door the first door immediately screen-RIGHT of the stairwell, white A4 notice taped at chest/eye height; a black wheelie bin + wire shopping trolley + stacked cardboard boxes just screen-LEFT of the stairwell; a folding metal chair against the brick further screen-RIGHT; a low balustrade screen-LEFT with washing on a line and misty tower blocks beyond; the walkway recedes in a long one-point perspective into cold mist. Light: cold overcast blue-green daylight from the open screen-LEFT side, deep shade under the concrete soffit. Wet concrete floor with puddles.
FIRST FRAME AND SPATIAL BLOCKING
First frame is a WIDE GENERAL plate WITH Cal: <<<dc97b5e1-9440-4379-a4b8-0cf476facafa>>> at his teal hero door (mid, screen-right of the arched stairwell), hood up, the white <<<2b31223f-f889-4da3-8dff-079d837584b5>>> taped on the door; bins/trolley/boxes screen-left of the stairwell, folding chair further right, misty perspective screen-left. Locks the real environment and him. (By the frontal medium, <<<59d76766-4704-44e3-af3c-140017ae9096>>> has quietly moved in directly behind Cal, but she is OUT OF FRAME / unseen — established only by her voice.)
FORMAT MODE
ONE single generation, controlled multi-shot montage — hard cuts between three camera set-ups, same location, continuity locked. No fades/dissolves.
OPTICS
Beat 1 (general): 84° wide immersive rectilinear, no fisheye. Beat 2 (notice + tear): 47° standard normal, camera square-on to the door. Beats 3–4 (read aloud + unison + reaction): 47° standard normal frontal medium on Cal (matching the second reference frame). One FOV per beat.
CAMERA
Beat 1: settled wide of the walkway (lock environment + Cal). HARD CUT. Beat 2: camera directly facing the door — a SMALL subtle dolly-in onto the taped notice (~2s), then, ON THE SAME ANGLE (no cut), Cal's hand reaches in from BEHIND the lens into frame and tears the notice off the door. HARD CUT. Beats 3–4: a frontal medium on Cal (like the second reference), calm SETTLE handheld holding him chest-up; it stays ON CAL the whole time — it does NOT turn, reframe, pan or push to reveal Meggie. She is behind him, off-frame, never shown.
ACTION TIMING (≈15s, hard cuts between set-ups)
[~2.0s | 84° WIDE GENERAL] the walkway with Cal at his door and the taped notice — environment locked. HARD CUT.
[2.0–4.0s | 47° head-on to door] small subtle dolly-in onto the white court order taped to the teal door.
[4.0–6.5s | SAME head-on angle, no cut] Cal's hand reaches in from behind the camera and tears the notice off the door — tape resists then gives, paper rips free. HARD CUT.
[6.5–9.5s | 47° frontal medium on Cal, like ref 2] Cal, hood up, holds the paper and reads it aloud, head down, flat and hollow: "...must vacate property within —"
[9.5–11.5s] on the deadline, Cal AND Meggie say it in EXACT UNISON — Cal reading it as Meggie's voice arrives from directly behind him (she is unseen): "Twenty-four hours." (a faint curl of her cigarette smoke may drift into frame from behind him — never her body or face).
[11.5–15.0s | same frontal medium, hold on Cal] with NO pause, Cal crushes the paper in his fist, rolls his eyes and lifts his gaze wearily UP toward the soffit (a spent "give me strength") and deadpans it — WITHOUT turning, without a big jump: "Jesus Meggs!" Meggie is never seen.
PHYSICS
Tape peels with resistance then a crisp release; paper bends, tears, then crushes with real crackle in his fist. A faint curl of cigarette smoke drifts in the cold still air from behind him. Cal's reaction is all in the face — the eye-roll and the slow lift of the gaze — his body barely moving, shoulders staying collapsed. Cold breath faint.
LIGHTING
World of the Boys, cold and submerged, booklight-hard cold end: cold overcast blue-green daylight from the open walkway side, one motivated direction, true negative fill, deep soffit shade — never flat front light. The white paper is the bright note against the cold teal door; on the frontal medium the cold estate daylight reads Cal's face low-key but clear; drifting smoke picks up the cold light. Accent: cold cyan/teal murk.
AUDIO
Dialogue as scripted:
— CAL (reading the notice aloud, flat and hollow, low, London): "...must vacate property within —"
— CAL + MEGGIE (in EXACT UNISON; Meggie OFF-SCREEN directly behind Cal, unseen, her big brash Caribbean-London alto dialled DOWN low and dry, a verdict through cigarette smoke): "Twenty-four hours."
— CAL (immediately, no pause, weary deadpan, eye-roll up, no turn): "Jesus Meggs!"
VOICE LOCK — MEGGIE: female, ~50, Caribbean-London — a loud, rich, chesty alto (~F3–C5), bright and ringing, brash, fierce and scolding by nature; here dialled DOWN to a low, dry, unhurried verdict, smoke on the words, never shouting. CAL: young London man, warm mid-range baritone, here flat, tired and deflated. Ambient: cold wind, distant city hum, the peel and crush of paper. No music, no other voices.
STYLE
Grounded photoreal British social-realist crime-comedy texture; heavy submerged mood, the comedy played bone-dry and low; cold estate palette. 60:30:10 — dominant cold concrete/brick-shadow / secondary teal-green murk / accent the white court letter + pale cigarette smoke.
QUALITY
ARRI Alexa, vintage spherical primes, subtle anamorphic. Sharp clarity, stable picture, readable face, controlled highlights, natural cadence, no grain, no overexposure, no ghosting, no modern tech beyond 2011. British spelling.
POSITIVE LOCKS
ONE generation, hard-cut montage: wide general (locks environment) → dolly onto notice → on the SAME angle Cal's hand enters from behind the camera and tears it off → frontal medium (like ref 2) Cal reads the notice ALOUD ("...must vacate property within —") → on the deadline Cal AND Meggie say "Twenty-four hours" in EXACT UNISON (Meggie unseen, directly behind him) → Cal crushes the paper and deadpans "Jesus Meggs!". Meggie is NOT shown at any point — no body, no face, no reveal, no turn, no pan onto her; only her off-screen voice (and at most a faint curl of cigarette smoke). Meggie does NOT shout — low, dry, a verdict. Cal does NOT jump or spin — eye-roll up, deadpan, WITHOUT turning. Cal keeps hood UP. The flat interior is never seen. Only the scripted lines; no ad-libs, extra voices, subtitles or music.
````

## B. Music-video segment — pre-recorded track fed as a black-screen video carrier, lip sync

- Folder: `/4ACT_Epilogue (121-137)`
- model `seedance_2_0` · 2016×864 · 21:9 · 15 s · 1080p · audio off
- Reference elements: `prop_CB_champagne_bottle` (prop), `char_CB_music_video_girls` (character), `prop_CB_yacht_int` (prop), `prop_CB_capthat` (prop), `char_CB_Cal_MV` (character), `char_CB_Horace_MV` (character), `loc_CB_MV_Thms-cloude_v2` (environment), `char_CB_Oli_MV` (character), `prop_CB_video_yacht` (prop)
- Other inputs: video
- Length: 3105 words

````text
LYRICS

In ENGLISH with a London accent:

"Oli's good wit' dem Knuckles Mane,
Me, I'm good wit' dem buckles boi.
Family names been sullied so -
Came back wit' these Cully boys -
Got no-ting but this Cully noise -
Stompin' into the future Mane -
South side of the River Thames -
But overseas they now know our names, it's like -"

MASTER AUDIO AND LIP SYNC

Use the song from <<<video_1>>> and the characters from the supplied image references to create one segment of the boys’ 2011 hit rap music video. <<<video_1>>> is a black-screen carrier whose audio track is the master.

OLI is the only man who raps. He performs the exact quoted lyrics as precise lip sync to the original vocal in <<<video_1>>>.

The music, voice, timing and mix in the output are taken directly from <<<video_1>>>. The source audio is used whole and untouched from start to finish: identical tempo, pitch, words, vocal performance and mix. Nothing is re-sung, regenerated, remixed, extended or replaced.

Picture and audio begin together at 0:00. Picture cuts never interrupt or restart the track. The audio continues as one uninterrupted master beneath all seven shots.

MEASURED FLOW

The delivery runs at approximately 3.5 words per second, steady, confident and continuous. The densest passage reaches approximately 5.0 words per second around 6.4 seconds. There are no pauses.

THE MOUTH NEVER INVENTS: every visible mouth movement corresponds to a syllable actually sounding in <<<video_1>>> at that instant. Between audible lines, Oli’s mouth rests naturally closed or breathes. Everyone who is not rapping uses their lips only for smiles, laughter and natural reactions.

The quoted words themselves are the primary sync anchors. Each specified gesture lands exactly on its quoted word as that word sounds in <<<video_1>>>. Seedance follows the track’s own rhythm between those anchors.

CONTEXT

A champagne party is in full swing aboard a luxury jacuzzi-yacht cruising along the Thames in London, 2011. The raised steaming tub is the social heart of the boat: champagne glasses everywhere, spray suspended in the air, bodies moving with the track and constant laughter. It feels like the best evening of their lives.

The yacht travels downriver toward Tower Bridge during the final luminous transition from sunset into civil twilight. Tower Bridge stands directly ahead, framed against the warm horizon. The Tower of London occupies the north bank to port: low historic stone battlements, turrets and dark riverside greenery. City Hall and the glass-and-steel More London buildings occupy the south bank to starboard. The distant Canary Wharf towers appear as dark silhouettes beyond Tower Bridge.

The city is close on both banks, but the open river remains broad and expansive around the yacht. The water is deep indigo and charcoal grey, broken by short wind ripples, white boat wakes and elongated orange-peach reflections from the sky.

TIME OF DAY, WEATHER AND SKY

The entire sequence takes place during the exact late-sunset-to-civil-twilight atmosphere of <<<7361586d-3f49-4764-8aed-de6f0fa440fb>>>.

The sun itself has dropped below the distant horizon and never appears as a visible disc. The brightest remaining glow sits low behind and around Tower Bridge. A band of burnt orange, peach and warm amber light spreads above the horizon, then transitions upward into cool violet and deep indigo-blue twilight.

A dramatic mackerel sky fills the upper frame: dense repeating altocumulus cloud patches arranged in natural rippling formations. Their lower edges catch the final orange and peach afterglow while the spaces and upper sky remain cool indigo. The pattern is detailed, rhythmic and expansive, never a flat overcast ceiling.

The weather is dry and clear beneath the high textured cloud layer. There is no fog or low haze obscuring the landmarks. Atmospheric perspective softly separates Tower Bridge, the distant Canary Wharf skyline and the two riverbanks.

The sky structure, time of day, horizon glow, cloud pattern, water colour, bank geography, landmark placement, skyline atmosphere and overall Thames mood remain 100% controlled by <<<7361586d-3f49-4764-8aed-de6f0fa440fb>>> throughout all seven shots. The reference controls the environment and lighting law, but its high panoramic camera composition is never copied.

LOCATION AND RIVER GEOGRAPHY

The yacht follows the central Thames channel toward Tower Bridge.

PORT / NORTH BANK — the Tower of London sits close to the river as a dark historic stone complex with recognisable battlements and turrets. Low riverside greenery and older masonry extend around it.

CENTRE / AHEAD — Tower Bridge remains the dominant directional landmark, with its twin towers and suspended roadway clearly readable against the glowing horizon. The dark Canary Wharf skyline appears much farther away beyond it.

STARBOARD / SOUTH BANK — City Hall’s rounded glass form and the adjoining More London glass offices create the modern bank. Their surfaces retain cool blue reflections from the upper twilight sky and restrained amber reflections from the horizon.

The river bends gently into depth beyond Tower Bridge. Dark indigo-charcoal water carries choppy surface texture, pale wake foam and broken warm reflections along the central channel.

All buildings, boats, infrastructure and skyline details remain period-true to London in 2011.

STYLE

The gold standard of a 2011–2013 hit British rap video. Cinematic texture associated with Cooke S4/i 24mm, 35mm and 85mm primes, plus an Angénieux Optimo zoom character for sudden crash-zoom grabs.

The bright orange-peach horizon or the most luminous section of the patterned twilight sky remains in or just outside the frame whenever geography allows. Bright horizon edges, champagne glass highlights, chrome rails, wet teak and water droplets produce soft creamy Cooke bloom and restrained veiling flare.

Exposure preserves the full colour and texture of the twilight sky. The orange cloud edges never clip into flat white, and the upper indigo sky retains visible tonal depth. The banks, distant skyline and water remain dark and cinematic without becoming empty black shapes.

Shots facing the bow or either bank play in strong contre-jour against the glowing horizon and patterned clouds. Oli’s face remains readable through natural open-sky fill, warm horizon bounce and soft reflection from the yacht’s white surfaces. His lips, eyes and expressions remain clear even when the environment behind him is significantly brighter.

Shots looking astern receive cool violet-blue frontal twilight mixed with warm reflected light from the white deck, honey teak, champagne and skin. The yacht’s wake burns pale silver-white against the deep indigo water.

ARRI Alexa texture, natural highlight roll-off, clean 2011 music-video colour and aggressive operator energy in the Larkin Seiple school. Shaky handheld, steadicam and physically motivated crash-zoom energy are used according to the specified shot. The camera always feels operated by a person and always breathes.

The twilight contrast intensifies the party’s colour. Oli’s purple-pink paisley silk, the mirror-gold champagne bottle, jewellery and individual swimwear colours remain rich and saturated against the indigo water, dark banks and orange-peach sky.

THE RAPPER

OLI is the only rapping mouth.

He wears his purple-pink paisley silk set, large gold-rimmed square shades and gold chain. He is the coolest man aboard and also the most alive: charged, mobile and openly in love with his new life.

He never stops moving. His torso rolls with the beat, his weight dances from foot to foot, and he works the whole boat like a kingdom he has just inherited. The cool comes from how he moves, never from standing still. His sharpest lines live in an eyebrow movement, a collar flick or the rotation of his champagne glass. Between lines, he breaks into the wide grin of a man who cannot believe how good his life has become.

Whenever an active rap line is on camera, Oli’s head remains steady and square to the lens, either frontal or in a slight three-quarter angle, framed MCU or closer. The groove remains in his shoulders, chest and torso so every mouth shape stays crisp and readable.

His mouth is never hidden by hands, champagne glass, spray, shades or another person.

Everyone else remains candid and camera-unaware. Their attention stays on Oli, one another, their drinks or the river. Every body aboard moves to the beat of <<<video_1>>> from the first frame to the last.

A champagne glass is the only handheld object used by the party guests. The mirror-gold bottle appears only where physically motivated.

GEOMETRY

The yacht matches <<<e80e280e-9e58-4d3c-8932-fb1801b5b50f>>> exactly.

<<<261f5961-3cb8-46aa-a119-d63a617d4e4b>>> is the strict deck map. Object placement, scale, circulation paths and interior design match it exactly. Its straight-down reference composition is never reproduced as a generated frame.

The fixed bow-to-stern order is:

Bow lounge → wraparound windshield → cockpit → cockpit U-sofa → two teak platforms → raised round jacuzzi → swim platform.

When facing the bow, the helm sits in the cockpit’s front-right corner. The driver sits facing the bow. The windshield is directly in front of the driver’s face, with the wheel between the driver’s chest and the glass. Nobody and nothing stands between the driver and the windshield.

Directly behind the driver is the cockpit U-sofa. Behind that are two teak platforms: the champagne bucket sits on the port platform and the champagne glasses sit on the starboard platform. Behind the platforms is the raised round eight-person jacuzzi, deep enough for an adult to stand waist-deep. At the stern is the swim platform, with steps on the starboard side and the swim ladder on the port side.

Materials remain white leather, honey-coloured teak, chrome rails and gold trim. These are the exact deck objects and placements throughout all seven shots.

MONTAGE

Exactly seven shots.

Every cut lands on a phrase border or beat in <<<video_1>>>. Seedance follows the master track and places cuts according to its audible rhythm. The source audio remains continuous and never restarts.

Neighbouring shots change by at least two frame sizes or by at least 30 degrees. Each action is answered by a reaction, creating clear Kuleshov pairs. Every frame is off-centre: the principal subject rides a third line with look-room extending into the open side. Dead-centre framing appears only for explicitly marked peak beats.

Speed ramps occur only inside any available windows without vocals. Vocal passages remain real-time so lip sync stays exact.

Inside each shot, the specified camera angle remains consistent. Natural sequencing occurs within the held angle: first one action begins, then the reaction follows, and as one movement resolves the next movement starts.

The clip ends at the peak of Shot 7 at full intended twilight exposure, without dimming or fading, and holds that energy until the final instant of <<<video_1>>>.

SHOT 1 — MS, SHAKY HANDHELD, LEFT THIRD

Oli is seated and flowing toward the lens, but his body is fully alive. His torso rolls with the beat, one heel bounces and his shoulders pop against the hi-hats.

The dark indigo river and a section of orange-edged mackerel clouds sit behind him. Cool open-sky fill and warm reflection from the yacht preserve sharp facial and mouth detail.

On “Knuckles,” Oli cocks his head and smiles knowingly while his thumb rolls the stem of the champagne glass.

On “buckles boi,” he glances down at his own paisley silk set, flicks the collar and laughs at his own luck.

The handheld camera breathes with small physical operator corrections while holding Oli on the left third.

HARD CUT

SHOT 2 — MCU, HANDHELD DRIFT, RIGHT THIRD

At the bow, Oli strolls along the rail line with a bounce in every step. His arms open toward the Thames as though he owns it.

Tower Bridge sits directly ahead against the warm orange-peach horizon. The patterned altocumulus sky expands above it from amber cloud edges into violet and deep indigo. The Tower of London remains on the port side, while the glass buildings around City Hall remain on the starboard side.

On “sullied,” Oli slowly brushes one invisible speck from his shoulder. His face turns serious for exactly one beat.

On “Came back wit’ these Cully boys,” the grin bursts back. He spins on his heel and nods toward Cal and Horace, who bob behind the windshield.

Oli’s head returns square to the lens for each visible lyric. His shoulders and walking rhythm carry the movement without disrupting mouth clarity.

HARD CUT

SHOT 3 — MS, STEADICAM DRIFT, LEFT THIRD

Oli stands at the jacuzzi steps holding a champagne glass. He rocks from side to side, using the glass to conduct the beat.

Warm orange-peach horizon reflections and cool indigo sky reflections travel across the chrome rails, wet teak, champagne glass and white yacht surfaces. The river behind him remains deep charcoal-indigo with broken warm highlights.

On “Cully noise,” he cups one hand to his ear as if asking, “You hear that?” His eyebrows dance while his mouth continues the exact lyric.

Blonde walks directly past him, lightly brushes his shoulder and climbs the steps into the tub. Oli never turns around. He simply grins wider and rocks harder.

HARD CUT

SHOT 4 — TIGHT CU, HANDHELD, RIGHT THIRD

The lower half of Oli’s face fills the right third, carving every syllable with exact lip sync. The edge of his gold-rimmed shades remains visible near the upper frame line.

Behind his shoulder, Blonde’s splash rises into a luminous crown of droplets. One side of the water catches the peach-orange horizon; the other catches the deep indigo upper sky and cool chrome reflections.

A tiny smirk crosses Oli’s mouth mid-word without breaking the lip-sync shape. The splash remains behind his shoulder and never crosses or conceals his mouth.

HARD CUT

SHOT 5 — MCU, HANDHELD, LEFT THIRD

The camera faces from the cockpit toward the tub. Oli drives his whole body forward with the beat. The south bank slides past behind him as a layered mixture of dark glass architecture, cool blue reflections and isolated warm windows.

On “Stompin’ into the future,” he stomps the teak deck on each accented beat. Every stomp has grounded foot contact, visible weight transfer and a natural response through his hips and shoulders.

On “South side of the River Thames,” his head turns briefly toward City Hall and the More London buildings on the south bank. He raises his champagne glass toward them: a toast to the old streets from the new life.

His head and mouth return square to the camera for the continuing vocal.

HARD CUT

SHOT 6 — MCU TO CU, SHAKY PUSH-IN, RIGHT THIRD

This is the fastest vocal passage.

Oli rises from the seat in one clean weighted movement and drives directly toward the lens. The shaky camera pushes closer with him, changing from MCU to CU while keeping his mouth crisp through the final syllable.

On “overseas... our names,” both arms sweep open wide. His face carries triumph and disbelief at how far they have come.

The twilight lighting remains stable and flattering across his face: cool violet-blue open-sky fill from above, warm peach reflection from the horizon and soft neutral bounce from the yacht’s white deck. His lips, skin texture, shades, gold chain and purple-pink paisley remain clearly defined. He never falls into an unreadable silhouette.

HARD CUT

SHOT 7 — CU, 24MM WIDE CHARACTER, HANDHELD, LEFT THIRD

THE AD-LIB POSE.

On the hanging “it’s like—,” Oli performs a double shoulder-brush, lifts his chin and freezes with both arms spread in the rapper’s stance, daring the lens.

Behind him, the entire boat erupts into laughter, raised glasses and beat-driven movement. Cal and Horace react without rapping. The five girls celebrate around the jacuzzi while keeping their individual identities readable.

The camera remains alive and close. Tower Bridge rises behind Oli against the glowing orange-peach horizon. The upper frame is filled by the dramatic rippling pattern of violet and indigo altocumulus clouds. Dark riverbanks and deep indigo water make the yacht party feel bright, expensive and isolated inside the twilight city.

The clip stops on this full-energy pose at full intended exposure. The final image holds without a fade until the exact end of <<<video_1>>>.

CONTINUITY

Everyone remains dry throughout the sequence except for physically separate splash droplets suspended behind Oli in Shot 4. No clothing or hair becomes soaked.

Horace’s hat stays on.

The girls’ champagne glasses remain full.

Oli’s paisley silk set, gold-rimmed square shades, gold chain and champagne glass remain continuous across all seven shots.

The yacht continues travelling in the same direction toward Tower Bridge. The north bank remains port side, the south bank remains starboard, and Tower Bridge stays ahead.

The same late-sunset civil-twilight state remains locked across the complete montage. The sun stays below the horizon. The orange-peach horizon band, violet-indigo upper sky, rippling altocumulus pattern, dark banks, distant Canary Wharf silhouettes and indigo-charcoal water retain exact continuity. The sky does not visibly darken between cuts.

REFERENCES

<<<video_1>>> — the complete track segment and black-screen carrier. Its audio is the master audio and the only sound law. The original music, original voice and original mix remain intact from beginning to end. Location sound is only a faint bed far beneath the unchanged track.

<<<d3ccf0f7-a6f3-446d-b10c-82ff628e744c>>> — OLI, the only rapper in this segment. Purple-pink paisley silk set, large gold-rimmed square shades and gold chain. Face, body, hair, proportions and wardrobe match the reference exactly.

<<<39b100d7-3531-4058-8d8e-c770b795586c>>> — CAL. He never raps here and uses his mouth only for laughter and natural reactions. Pale-blue jacquard denim short-sleeve set, white vest, gold chain, dark hair and light moustache. He matches the reference exactly.

<<<6404dca6-b683-4bb0-8215-608379e7a4d2>>> — HORACE. He never raps here and uses his mouth only for laughter and natural reactions. Orange Hawaiian shirt with white line print, denim shorts, black curls, aviator shades, gold chain and a huge grin. He matches the reference exactly.

<<<15362f4b-e011-4747-83eb-afa798f929dd>>> — five distinct girls identified by hair and appearance: Braids, dark-skinned with high braids; Black-hair, Asian with long straight black hair; Blonde; Red-bob with freckles; and Brunette. Their faces, hairstyles, body proportions and individual swimwear sets match the casting sheet exactly.

<<<33991396-3d42-45e6-86c6-3c82bf186361>>> — the captain’s hat, matching the reference exactly.

<<<05a93286-37d3-44eb-a018-d99a751d5e83>>> — mirror-gold MAISON MARO champagne bottle with a black foil cap and neck, embossed baroque crest featuring two lions, a crown and an “M” shield, plus dark MAISON MARO lettering. It matches the reference exactly.

<<<e80e280e-9e58-4d3c-8932-fb1801b5b50f>>> and <<<261f5961-3cb8-46aa-a119-d63a617d4e4b>>> — strict hull, deck, interior, scale and geometry references as defined in GEOMETRY.

<<<7361586d-3f49-4764-8aed-de6f0fa440fb>>> — the Thames twilight environment reference. It controls the time of day, mackerel-cloud sky, orange-peach horizon glow, violet-indigo upper sky, backlit exposure, dark water, warm reflections, Tower Bridge position, Tower of London on the north bank, City Hall and More London on the south bank, distant Canary Wharf silhouettes and the overall sophisticated twilight atmosphere exactly. Its panoramic camera angle is not inherited; every music-video frame is a new composition built inside its world.

All references are identity, environment and geometry law. Their original compositions are never reproduced as generated frames.
````

## C. World style prefix + b-roll opening (Scene 31)

- Folder: `/1 ACT (1-49)/31 Scene`
- model `seedance_2_0` · 2016×864 · 21:9 · 15 s · 1080p · audio on
- Reference elements: `loc_CB_workshop_interior_back_s31_v2` (environment), `loc_CB_workshop_interior_back_s31_v3` (environment), `char_CB_Tobin` (character), `prop_CB_gunTobin_s26_v1` (prop), `loc_CB_workshop_interior_front_s31_v2` (environment), `prop_CB_gunTEDDI_s26` (prop), `char_CB_Teddy` (character)
- Other inputs: —
- Length: 707 words

````text
STYLE PREFIX — THE CULLY HILL BOYS · world ① BOYS (Lubezki × Edgar Wright × Guy Ritchie). Grounded photoreal British social-realist crime-comedy, cold and submerged, gone kinetic. Cold-concrete grey-teal base field ~85%; booklight wrap at the hard cold end — tight cool wrap, fast falloff into deep shadow, true negative fill, never flat front light. 60:30:10 — dominant cold-concrete grey-teal / secondary wet-steel & brick / accent the one motivated source. ARRI Alexa, vintage spherical primes, subtle anamorphic; sharp clarity, stable picture, no grain, no overexposure, no blur, no ghosting, no modern tech beyond 2011. British spelling. Diegetic SFX only, no music, no subtitles. 2.39:1.

PRODUCTION CONTEXT — A b-roll sequence FOCUSED ONLY on TOBIN and TEDDY — their actions covered from a VARIETY of different angles, ~2 seconds per beat. They are under fire from above (Dmitry off-screen on the roof) and fire back UP at the CEILING SKYLIGHT WINDOW; Teddy hurriedly PUSHES the hinged gates and they swing open, then both just run out into the street — they do NOT fire toward the exit. ~12s total, REAL-TIME, hard cuts.
GEOGRAPHY — the FRONT of the frame/room is <<<0cbe9128-67ac-4d3a-b474-dab946e6e17b>>>; the BACK is <<<cc7b9eab-1527-4103-baed-ad2a111343bc>>> (foreground/background). Roger is NOT the focus here (out of frame / a blur if seen).
ACTIVE REFERENCES — <<<644321a4-b69e-49a5-b0d4-3c4e0dbc523c>>> (black leather coat, his pistol <<<6cfc46bc-31af-41c9-8f68-2b37bfe6da0a>>>), <<<ff31a934-1ecf-4c95-80f2-a7b39a94613d>>> (dark jacket, his pistol <<<ef8309f5-fc0c-4a1b-b261-6c932f4b3c4c>>>),  (firing DOWN from the roof, OFF-SCREEN above — never in frame),  (Dmitry's AK, off above),  (the body in the white boat's cockpit), <<<0cbe9128-67ac-4d3a-b474-dab946e6e17b>>> (FRONT), <<<cc7b9eab-1527-4103-baed-ad2a111343bc>>> (BACK) → <<<0d95446f-7298-49f0-b385-78cd57daa7ae>>> / front_s31_v3 (walls taking bullet damage).
FORMAT MODE — CONTROLLED MULTI-SHOT, ~12s, SIX ~2-second beats, HARD CUTS, each a DIFFERENT angle. Living/kinetic handheld. Real-time.
SEQUENCE (different angle each beat) —
0.0-2.0s — B1 · LOW ANGLE looking up: <<<644321a4-b69e-49a5-b0d4-3c4e0dbc523c>>> fires his pistol (<<<6cfc46bc-31af-41c9-8f68-2b37bfe6da0a>>>) UP at the CEILING SKYLIGHT WINDOW, past the lens, muzzle flash at camera; <<<ff31a934-1ecf-4c95-80f2-a7b39a94613d>>> beside him firing his pistol (<<<ef8309f5-fc0c-4a1b-b261-6c932f4b3c4c>>>) at the same ceiling window. HARD CUT.
2.0-4.0s — B2 · OVER-THE-SHOULDER of <<<ff31a934-1ecf-4c95-80f2-a7b39a94613d>>> firing his pistol UP at the CEILING SKYLIGHT WINDOW (the off-screen threat), rounds pocking the ceiling and wall. HARD CUT.
4.0-6.0s — B3 · DIRTY FOREGROUND CLOSE on <<<644321a4-b69e-49a5-b0d4-3c4e0dbc523c>>>'s pistol (<<<6cfc46bc-31af-41c9-8f68-2b37bfe6da0a>>>), muzzle flash blooming, his hard face behind in shallow focus. HARD CUT.
6.0-8.0s — B4 · WIDE TWO-SHOT: both <<<644321a4-b69e-49a5-b0d4-3c4e0dbc523c>>> and <<<ff31a934-1ecf-4c95-80f2-a7b39a94613d>>> firing UP at the CEILING SKYLIGHT WINDOW and moving toward the big gates, gunsmoke, shells flicking. HARD CUT.
8.0-10.0s — B5 · PROFILE on <<<ff31a934-1ecf-4c95-80f2-a7b39a94613d>>>: in a rush he SHOVES the big HINGED GATES with both hands and they SWING open on their hinges — he does NOT fire toward the exit, just pushes them open and goes; cold night light spilling in. HARD CUT.
10.0-12.0s — B6 · LOW TRACKING from BEHIND: the gates swung open, <<<ff31a934-1ecf-4c95-80f2-a7b39a94613d>>> just RUNS OUT into the street and <<<644321a4-b69e-49a5-b0d4-3c4e0dbc523c>>> follows out through them — neither fires toward the exit, they just run.
CAMERA — Living/kinetic handheld, a fresh angle per beat (low, over-shoulder, dirty-foreground macro, wide two-shot, profile, low rear-track); whip energy on the bursts; never locked.
PHYSICS — Recoil and muzzle kick on the upward pistol fire, shells ejecting and ringing; real running strides; Teddy PUSHES the heavy hinged gates and they SWING open on their hinges; fire from above pocking the walls around them; gunsmoke and breath vapour; the body inert in the boat.
LIGHTING — Cold low-key; their muzzle flashes up + the fire from above; cold night light through the opening gates; faces toward shadow, no flat front light.
POSITIVE LOCKS — FOCUS only on <<<644321a4-b69e-49a5-b0d4-3c4e0dbc523c>>> and <<<ff31a934-1ecf-4c95-80f2-a7b39a94613d>>>, covered from SIX different angles, ~2s each. Both fire UP at the CEILING SKYLIGHT WINDOW with their pistols (<<<6cfc46bc-31af-41c9-8f68-2b37bfe6da0a>>> / <<<ef8309f5-fc0c-4a1b-b261-6c932f4b3c4c>>>). <<<ff31a934-1ecf-4c95-80f2-a7b39a94613d>>> HURRIEDLY PUSHES the big HINGED gates and they SWING open on their hinges, then — once open — just RUNS OUT into the street; <<<644321a4-b69e-49a5-b0d4-3c4e0dbc523c>>> follows. They do NOT fire toward the exit while leaving — they just run.  fires OFF-SCREEN above (never in frame). FRONT = <<<0cbe9128-67ac-4d3a-b474-dab946e6e17b>>>, BACK = <<<cc7b9eab-1527-4103-baed-ad2a111343bc>>>. REAL-TIME, six 2s hard-cut beats.
AUDIO — AK fire from above; Tobin's and Teddy's LOUD PISTOL shots up (sharp loud handgun cracks), shells ringing; rounds smacking the walls; the gates banging open; pounding runs; shouts (no words). Diegetic SFX only.
````

## D. Prop reference sheet — Nano Banana 2, grey #808080, 2×2 turnaround

- Folder: `/PRE  PROD/ASSETS/Vernon's shotgun`
- model `nano_banana_2` · 3168×1344
- Reference elements: —
- Other inputs: —
- Length: 350 words

````text
<<<image_1>>> reference image.

Create a four-panel product reference sheet (a "props sheet" turnaround) of the exact same luxury engraved side-by-side break-action shotgun from the attached reference image. Keep the gun's identity, proportions, engraving pattern, materials and finish perfectly identical to the reference in every panel. Lay it out as a 2x2 grid on one continuous, seamless solid neutral medium-grey background, hex #808080, like a clean photographic studio seamless. Light it with a soft directional key from the upper left and gentle shadow falloff, neutral white balance, even cinematic studio lighting.

Panel layout:

- Top-left — full left-side profile, medium-wide establishing shot. The whole shotgun lies horizontally, buttstock to the left and long blued barrels to the right, exactly as in the reference: gilded, finely floral-scroll-engraved action and lockplates, deep blued side-by-side barrels with a top rib, richly figured walnut stock with the distinctive reddish textured butt, checkered semi-pistol grip and forend, ornate gold trigger guard with twin triggers.

- Top-right — extreme close-up macro of the LEFT lockplate. The engraved cursive surname "Moody" must appear large, sharp and clearly legible, framed by delicate gold floral scrollwork on polished gilded steel. This is the ONLY panel where the name appears.

- Bottom-left — full right-side profile, the opposite (off-side) face of the same gun, medium-wide, buttstock to the right and barrels to the left. The right lockplate shows matching floral scroll engraving only — there must be NO name, NO surname, NO lettering and NO text anywhere on this side. Leave the engraved metal clean of any words.

- Bottom-right — three-quarter rear view of the action and stock from the off-side, medium close-up: gilded action body, gold top lever, double triggers, ornate gold trigger guard, the comb and wrist of the walnut stock and the barrel breech. No text or name is visible from this angle.

The background stays a solid uniform neutral grey #808080 in every panel. Keep lighting, white balance, color palette and surface finish consistent across all four panels. Photorealistic, ultra-detailed rendering of the metal engraving, blued steel and walnut grain. Wide landscape format, single cohesive sheet.
````

## E. Costume-state point edit — Nano Banana 2 on an existing three-panel turnaround

- Folder: `/PRE  PROD/ASSETS/COSTUMES`
- model `nano_banana_2` · 5504×3072
- Reference elements: —
- Other inputs: —
- Length: 115 words

````text
Same man, exact same three-panel turnaround on flat seamless grey, identical poses, stance and camera angles, unchanged. Film costume-continuity reference with practical SFX makeup: keep the dark wine-red stage-blood staining on the collar area and over the right shoulder. Now add stage blood under the beard — wet dark maroon dripping from the underside of the beard onto the chest and collar — plus a few thin blood trickle marks running down the front of the navy coverall. The stage blood reads wet and glossy where fresh and soaks darker into the fabric where it lands, deep maroon, naturalistic prop-blood look. Everything else stays exactly the same — keep his position, framing and angles unchanged.
````

## F. Identity-locked hair edit — Nano Banana 2

- Folder: `/PRE  PROD/ASSETS/Cal`
- model `nano_banana_2` · 2752×1536
- Reference elements: —
- Other inputs: —
- Length: 118 words

````text
Same man, same face, same expression, same pose, same framing, same clothes, same grey background, same muted cool film grade — identity fully preserved. Keep the same short close crop haircut, same length and shape. Change only the hair colour and styling: lighten the hair from dark chestnut to a medium warm brown with soft natural lighter tones through the top, and restyle the top slightly — the short dense fringe now swept casually to one side with loose relaxed texture instead of hanging straight down, a little airier and less flat. Clean soft matte finish, evenly lit with no deep shadows, natural strand detail. The face, hairline, ears, skin and everything below the neck remain exactly untouched.
````

## G. Location plate — Soul Cinematic

- Folder: `/PRE  PROD/ASSETS/LOCATIONS`
- model `soul_cinematic` · 2528×1088
- Reference elements: —
- Other inputs: —
- Length: 384 words

````text
Grounded naturalistic photoreal cinematic film still, private upmarket Thames boat marina, Berkshire upper Thames Valley, 2011, deep autumn, deep dead of night, pitch dark, extremely thick heavy fog, almost total whiteout blackness, visibility cut to a couple of metres. Anamorphic wide angle eye level shot looking straight down the central water channel, slight three quarter angle, rule of thirds, no people, no buildings, no lamps. The scene is overwhelmingly dark, near black, barely lifted by the faintest trace of cold moonlight buried in the fog. Foreground right: a clipped topiary bush gone patchy and a low curved stone bank with browned frosted autumn grass thick with fallen leaves, dry iris reeds at the waterline, all sunk in deep cold blackness. Foreground left: a second low curved bank, bare and leaf strewn. All vegetation low and short, clipped bushes and low scrub only, almost no trees, nothing tall. Centre: a strip of black still water running away into pure darkness. Both banks lined with moored glassfibre motor cruisers and cabin yachts tied up broadside, side on to the channel, lying parallel to the bank, long horizontal hulls running along the frame, packed bow to stern in continuous rows; only the very nearest hulls on left and right barely emerge from the black, wet navy covers, dim cream hulls; the rows just behind swallowed whole into the fog as ghost silhouettes. Beyond a metre or two everything vanishes into a solid black wall of fog and murk, no boats, no bank, no horizon, no houses, no trees, no lights. Materials: composite decking, galvanised steel, glassfibre, wet stone, low hedge. Colour grade: muted desaturated, very low contrast, near monochrome cold slate blue crushed into deep black, milky grey fog, black water, mostly pure darkness, low key, underexposed night. The only light is a barely there trace of cold blue moonlight on the nearest wet hulls, no lamps, no glow sources. Quiet money, discreet, hushed, blind, watched. Nearest foreground clean and sharp, no grain, no overexposure, no modern tech. Shot on ARRI Alexa with 2x anamorphic lens, oval bokeh, slight barrel distortion, cinematic widescreen. --no people, cartoon, render, sailboat, snow, daylight, bright, sunlight, green grass, summer, houses, building, trees, forest, sharp background, lamp, lights --ar 7:3 --raw --stylize 50 --hd --profile 1ygdot2 9odrhhh ib2dn3d --chaos 5 --weird 4
````

## H. Location re-angle from an approved plate — Seedream 4.5

- Folder: `/PRE  PROD/ASSETS/EDITS`
- model `seedream_v4_5` · 6048×2592
- Reference elements: —
- Other inputs: —
- Length: 190 words

````text
Using the attached rooftop image as the reference for this exact location and all its objects, re-create the same scene as a WIDER, HIGHER-ANGLE establishing shot. Move the camera up and back for a more general view, shifted to the RIGHT and looking DOWN on the rooftop at a steeper high angle, so we see much more of the flat roof surface around everything and take in the whole setup from above.

Keep all the SAME objects in the SAME relative positions, just seen from this wider higher viewpoint: the dark blue dome tent with the red sleeping bag, the dirty white plastic chair, the low wooden pallet table covered with empty beer bottles, the tall white vent pipe (top open, no cap), the round metal tub/basin on the right, the low red-brick parapet around the roof, and beyond it the foggy estate — tower block, low-rise brick flats and bare winter trees in haze.

Match the exact same cold desaturated foggy blue-grey grade, flat soft overcast light, wet sheen on the roof and scattered dead leaves, the same gloomy quiet mood. Photoreal, cinematic, anamorphic widescreen, no people. --ar 21:9
````
