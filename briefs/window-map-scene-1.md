# TEST BRIEF · The Window Map · Scene 1 only · images only

This is a comparison run. The story, the ground rules and every prompt already exist in
`libraries/worked-example/` (The Window Map, authored 2026-09-22). Use them **verbatim**
wherever this brief says so, so that our GPT Image 2 outputs can be compared against the
images the kit's author generated from the same prompts. Do not improve his prompts.

## Mode

images only. Video is OFF for this job.

## Scene length

6 seconds. (The original shot is 14 s. We are not making video here, so the length only
sets the card. Do not ask the scene-length question; it is answered.)

## Ground rules (already locked, copy them, do not re-propose)

Take every value from `libraries/worked-example/ground-rules.md`:
16:9 · the warm storybook palette table (seven hex values) · Look = warm colour-negative film
· Stance = directed candid · the six forbidden items · reroll budget 3 per item.

## Scope

Scene 1 of the script (`libraries/worked-example/script.md`, SHOT 1): morning, the
apartment, Waffles on the sill, Nia says goodbye. Tag set for this scene and nothing else:

| Sheet | Handle | Prompt to use, verbatim (first fenced block of the file) |
|---|---|---|
| character-01 | @waffles | `libraries/worked-example/canvas/characters/@waffles/prompt.md` |
| character-02 | @nia | `libraries/worked-example/canvas/characters/@nia/prompt.md` (the second fenced block, the sheet prompt; the Identity Lock Card above it is internal) |
| environment-01 | @loc_apartment | `libraries/worked-example/canvas/locations/@loc_apartment/prompt.md` |
| element-01 | @water_tower | `libraries/worked-example/canvas/props/@water_tower/prompt.md` |
| element-02 | @pretzel_sign | `libraries/worked-example/canvas/props/@pretzel_sign/prompt.md` |
| element-03 | @bus_7 | `libraries/worked-example/canvas/props/@bus_7/prompt.md` |

Copy each prompt into its `plan/<type>-NN-<handle>.prompt.txt` unchanged. The Persistent
Characters registry is the REGISTRY block of `script.md`; copy it, do not rewrite it.

**Negative prompts.** Each of his files has a second fenced block: the negative. GPT Image 2
has no negative field. Do not paste it into the prompt. Instead append one sentence to the
end of the prompt that turns only the items that are not already covered into positive
states, and record in `report.md` exactly which items you folded. This is the one known
difference between his run and ours; keep it small and visible.

**Aspect and resolution.** His sheets are written as 16:9 sheets. Use `--aspect 16:9`,
`--res 1K`, `--quality high` for all six. His storyboard and stills were 1536 × 1024, so the
scene still runs at `--aspect 3:2`, `--res 2K`.

## Scene 1 still and end frame

- Card: build it from `libraries/worked-example/shots/SHOT-001/card.md`. Copy the motion
  map, the brief and the look picks as they are. Duration 6 s. Arrival state: the end of
  beat 2 (Nia has kissed his head, the sash is up a hand's width, she is turning to leave
  frame-left).
- Still prompt: derive from `libraries/worked-example/shots/SHOT-001/storyboard.md`. Use its
  REFERENCES block as the role-scoped reference lines (six images, same order), and its
  top-left panel description as the first frame. Attach the six approved sheets in the
  order the storyboard numbers them.
- End frame: an edit of the approved still per `roles/scene-sheet.md`. Change only the
  arrival state above.

## Comparison

When the author's images arrive, they go in `jobs/<job>/compare/leo/` under the same names
(`character-01-waffles.png`, `environment-01-loc_apartment.png`, and so on). Then, per
sheet, write `compare/<sheet>.md` with three lines: what matches, what differs, and which
you would attach to a video model and why. Nothing is regenerated for the comparison.
