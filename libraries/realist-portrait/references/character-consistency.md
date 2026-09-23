# Character Consistency — the Identity Lock Card

Used by **Mode B** (photo-driven) and **Mode C** (character sheet). It's the portrait-side equivalent of the pipeline's Stage 4 signature card: a fixed block of identity language that is written once and reused **verbatim** in every prompt for that character, so the face doesn't drift between views or between the still and the video made from it.

---

## 1. The card — fill every field, then freeze it

```
IDENTITY LOCK — <character name / label>
- Age:            <N years old> + <one corroborating age detail>
- Heritage:       <specific ancestry> ; <skin tone in plain terms> ; <undertone>
- Sex / presentation: <...>
- Face geometry:  <face shape> ; <nose> ; <eyes: shape, colour, set> ; <brow> ; <jaw/chin> ; <lips>
- Hairline & hair: <hairline shape> ; <hair colour incl. greys> ; <texture> ; <length/cut>
- Distinguishing: <1–3 permanent marks: mole / scar / freckle map / heterochromia / gap teeth ...>
- Build (face-level): <double chin on drop / hollow cheeks / full round face / prominent cheekbones ...>
- Fixed wardrobe:  <only if the character wears the same thing across views — else "varies">
- Capture:        <body / sensor> ; <film stock or colour science> ; <grain level>   (must match the signature card if one exists)
```

## 2. Rules

- **Write it once, above the prompts.** Each per-view prompt then opens with the card's identity lines copied in exactly — same words, same order. Don't paraphrase them per view; paraphrase *is* drift.
- **Only the frame layer changes per view:** head angle, gaze direction, expression, crop, and (if needed) which shoulder leads. Lighting, lens, background, and capture stay identical unless the sheet's whole point is a lighting test.
- **Mode B:** derive every field from the supplied photo. State what the photo *doesn't* show (e.g. "profile and hairline crown not visible in reference — inferred, flag for QC"). Never change a field to "improve" the person.
- **Mode C default view set** (adjust to the request): 
  1. front, neutral, head-and-shoulders 
  2. three-quarter left (~30°), faint closed-lip smile 
  3. three-quarter right (~30°), neutral 
  4. full left profile 
  5. looking down / away, contemplative 
  6. direct-to-lens, slight Duchenne smile
- **Feeding the video pipeline:** if this character has a Stage 4 signature card, copy its mood / palette / lighting register / lens / grain into the card's Capture and Lighting lines rather than inventing them here — the portrait must sit inside the same world.

## 3. Consistency aids to put in every prompt

- `the same individual as described, consistent facial identity across all frames`
- Repeat the 1–3 distinguishing marks in every prompt — they're the cheapest identity anchor.
- Keep the exact age phrase every time; "40 years old" one prompt and "middle-aged" the next will drift.
- If the target model supports a reference-image / character-reference feature (Midjourney `--cref`, some Seedream/Kling identity inputs), say so in the model-adaptation note: pass the approved first render as the reference for the rest and keep this card as the text half.

## 4. Anti-patterns

- Re-describing the face "in fresh words" each view — the fastest way to six different people.
- Letting lighting or lens wander between views of a sheet — even with a locked face it stops reading as one shoot.
- "Improving" a photo-driven subject's jaw, skin, age, or teeth — that's a different person, not a portrait of them.
- Forgetting the capture line — a film-grain front view next to a clean digital profile won't cut together.
