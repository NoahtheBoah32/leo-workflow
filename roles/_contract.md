# _contract.md — rules every subagent follows

You were deployed by the main agent with a spawn prompt that names your role file, a job
folder, a target, and a CONTEXT block. Read this file, then your role file, then work.

## You and the user

- You never talk to the user. The main agent does. Your final report goes to the main agent.
- You never ask questions mid-task. If something you need is missing, stop, report exactly
  what is missing, and let the main agent decide.
- If the main agent sends you a follow-up message (feedback, `GO`, a revision), continue from
  where you were. Your context is intact. Do not start over.

## Files

- Read `FOLDER-PROTOCOL.md` once. Write only inside your target folder
  (`sheets/<target>/` or `scenes/scene-NN/`) plus one appended row per run in `log.csv`.
- Never write an `approved` file. The main agent does that after the user approves.
- Never overwrite a version. The next version is the next number.
- Save the exact prompt you sent as `vN.prompt.txt` (or `still.prompt.txt` / `end.prompt.txt`
  / `video.prompt.txt` for scenes) before you generate, so the file exists even if the
  run fails.
- Append to `report.md` per version: what you checked, what passed, what you would change.

## Generation

- Images: `python tools/gen_image.py`, GPT Image 2 only. The tool loads the key. You never
  see it, print it, or pass it as an argument.
- Video: `python tools/browser_video.py`, the ElevenLabs web workspace through Camoufox.
  Never the video API.
- One generation per `GO`. A `GO` from the main agent covers one version. Feedback that
  arrives later covers the next version. Never run extra variations on your own.
- If a request is rejected before generating (HTTP 4xx), nothing was charged. Fix the
  request, do not retry blindly. Report the rejection text minus any key.
- Log every run, completed or failed, in `log.csv` with the run number continuing from the
  last row.

## Prompt discipline (from `PROMPT-STRUCTURES.md`)

- No director names, film titles, camera bodies, lens models or film stocks in prompt text.
  Named picks live on the scene card only. Describe what the look does instead.
- GPT Image 2 has no negative field. Write every exclusion as a positive state
  ("plain unbranded surfaces", "the sheet carries no lettering").
- State the palette as hex where the ground rules give hex.
- Left and right are from the camera.
- Say each important thing once.

## Your report

Final report to the main agent, in this order, short:

1. Output path(s), as full Windows paths (`C:\...`), so the main agent can relay them unchanged.
2. The prompt you actually sent (the file path is enough if it is unchanged from the plan;
   paste the diff if you changed it, and say why).
3. Three checks you ran on the result and what each found.
4. One line of what you would change next if the user is not happy.

Nothing else. No preamble. No summary of the role file.
