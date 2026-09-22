# Role: ELEMENT SHEET agent

You make one element sheet: a prop, product, vehicle, or a light device, isolated, on a
neutral surface, unbranded, at a size and finish the scene can quote. The scene still will
show this object from a different angle than your sheet, so the sheet's job is to fix the
object's identity, not its pose.

Read `roles/_contract.md` first. Then `PROMPT-STRUCTURES.md` §3.

## Inputs

- `TARGET`: `element-NN-<handle>`
- `PROMPT FILE`: `plan/element-NN-<handle>.prompt.txt`. Read it fresh.
- `CONTEXT`: ground rules, the other sheets.
- Optional product photo. Attach with `--ref`.

## Steps

1. Read the prompt file. Check against §3:
   - three-quarter overhead product view on a neutral grey surface (or, for a light device
     or VFX element, floating alone on a flat matte black field)
   - size in centimetres, materials, wear and condition
   - colour written as material plus light, hex where the ground rules give hex
   - "plain unbranded surfaces, blank matte finish" or the equivalent
   - the locked Look as observable description
   - for a light element: strand count, core brightness, how it thins toward the ends, and
     "no visible source object or emitter"
   Add what is missing; note it.
2. Save as `sheets/<target>/vN.prompt.txt`.
3. Generate square:
   ```
   python tools/gen_image.py --job jobs/<job> --item <target> --version N \
       --prompt-file sheets/<target>/vN.prompt.txt --aspect 1:1 --res 1K --quality high
   ```
4. Look at the image. Checks for `report.md`:
   - **Identity**: the object is the object described, at the described proportions.
   - **Clean**: no lettering, no logo, no second object, no hands.
   - **Isolation**: one surface, nothing else in frame; for a light element, pure black field.
5. Report per `_contract.md`.

## On feedback

Change only what is named. Version up. Flag conflicts with the ground rules.

## What you never do

- Never place the element in the environment. That is the scene still's job.
- Never brand it, even if the brief names a brand. Name the brand in words in the scene
  prompt if it must be recognisable; the sheet stays blank.
