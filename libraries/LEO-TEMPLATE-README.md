# Neutra DC — AI Production

Workspace for **scripted, multi-shot narrative work on Seedance 2.5**. Phase 0–9 process,
derived from Higgsfield's *Cully Hill Boys* production order and their shipped
`seedance-clean` prompt-writing skill.

## Start here

| Want to | Read |
|---|---|
| Understand the process end to end | [Seedance-Feature-Pipeline.md](Seedance-Feature-Pipeline.md) |
| Write an actual shot prompt | [Seedance-Prompt-Architecture.md](Seedance-Prompt-Architecture.md) |
| Check a rule against the source | [Sources/higgsfield-seedance-clean-SKILL.md](Sources/higgsfield-seedance-clean-SKILL.md) |
| Start a production | copy `template-project/` |

## The three bans

1. **No director / film / DP / camera / lens / film-stock names in prompt text.** Decide the
   look with the craft libraries at Phase 3; render it as observable description at Phase 4.
2. **No 1500-character cap.** That is a Dreamina limit. Budget by block necessity instead.
3. **No model-authored screenplay, no model-generated music.** A named human authors the
   script. Music is recorded first and fed in as 12-second breath-split blocks.

## Phases

```
0 Ground Rules → 1 Script (human) → 2 Canvas/Assets → 3 Breakdown+Look → 4 Prompt
              → 5 Generate → 6 Repair → 7 Audio → 8 Assemble → 9 Handoff
```

Each phase has a gate. Don't pass one until its condition is met.

## Self-contained

This workspace carries its own copy of every craft library and skill the pipeline calls —
camera, framing, DOF, transitions, directors, photography styles, SOUL, lenses, the ideation
library, `realist-portrait`, `elevenlabs-v3-audio-tags`, `multi-speaker-podcast-assembler`
and the `director-dp` agent. It can be moved, zipped or handed on and every link still resolves.

Two links deliberately point back at `../Image to Video/`: the Stage 0–9 pipeline (a different
process, not a dependency) and `Automation/` (where `neutradc.py` and its credentials live).

> **Fork warning.** Those libraries are copies taken Sep 2026 and will drift from the
> originals in `Image to Video/`. If one needs a real fix, decide which copy is canonical and
> apply it to both.

Use `../Image to Video/` (Stage 0–9) instead of this pipeline for single-shot work: ads,
product, architecture, FPV, and anything on Kling or Dreamina.

## Layout

```
CLAUDE.md                        routing + the three bans, for Claude Code in this workspace
README.md                        this file
Seedance-Feature-Pipeline.md     Phase 0-9 process, gates, shot card, old->new mapping
Seedance-Prompt-Architecture.md  prompt craft: 17 blocks, FOV table, protocols, checklist
Sources/                         Higgsfield's production skill, archived verbatim
template-project/                empty Phase 0-9 folder tree — copy to start a production

*-Library.md                     craft libraries (camera, DOF, directors, styles, ideation...)
Lenses/                          Zeiss Supreme Prime library + DOF tables
.claude/skills/                  realist-portrait, elevenlabs-v3-audio-tags, podcast-assembler
.claude/agents/                  director-dp
```
