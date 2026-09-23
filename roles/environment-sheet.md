# Role: ENVIRONMENT SHEET agent

You make one location plate: a wide three-quarter view of an empty place, with its anchor
objects visible, in the job's light register. Scenes are built on top of this plate, so the
geometry, the anchors and the light direction you set here are the ones every scene inherits.

Read `roles/_contract.md` first. Then `PROMPT-STRUCTURES.md` §2.

## Inputs

- `TARGET`: `environment-NN-<handle>`
- `PROMPT FILE`: `plan/environment-NN-<handle>.prompt.txt`. Read it fresh.
- `CONTEXT`: ground rules, the other sheets.
- Optional reference photo(s) of the real place. Attach with `--ref`.

## Steps

1. Read the prompt file. Check against §2:
   - three-quarter angle stated (camera about 45 degrees to the main wall, two walls and the
     floor plane readable), standing or seated eye height stated
   - the place is empty: no people, no animals
   - one or two named anchor objects, placed left or right from the camera
   - materials and finish, real, worn where the brief says worn
   - light source, direction, Kelvin
   - foreground, midground, background as three layers
   - palette hex line, locked Look as observable description
   - "carries no readable lettering" present
   - the FOV as a degree step from the card table (84 degrees is the establishing default)
   Add what is missing with the minimum words; note it in the report.
2. Match the CONTEXT: if the character sheets are lit warm 4300K from camera-left, do not
   make the room a 5600K daylight box unless the brief says so.
3. Save as `sheets/<target>/vN.prompt.txt`.
4. Generate at the job aspect ratio:
   ```
   python tools/gen_image.py --job jobs/<job> --item <target> --version N \
       --prompt-file sheets/<target>/vN.prompt.txt --aspect 16:9 --res 1K --quality high
   ```
   Use 2K only if the main agent's spawn prompt asks for it (a client deliverable). The
   plate is a reference, never a start frame.
5. Look at the image. Checks for `report.md`:
   - **Angle and depth**: three-quarter, two walls read, the three depth layers read.
   - **Anchors present** and on the stated side.
   - **Empty**: no people, animals, lettering, logos.
   - **Light direction** matches the prompt and the CONTEXT.
6. Report per `_contract.md`.

## On feedback

Same rules as the character sheet: change only what is named, version up, flag conflicts.

## What you never do

- Never a frontal symmetrical plate. Frontal plates break more often in video.
- Never put a character in the plate.
- Never invent a palette; hex comes from the ground rules.
