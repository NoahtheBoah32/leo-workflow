# Transition Library

Mister Horse's "Transitions for After Effects / Premiere" pack — 600+ presets across 15 categories, applied editorially (post-generation, in AE or Premiere) rather than as text fed into Seedance/Kling. This complements the generation-side continuity tools already in [Image-to-Video-Pipeline.md](../Image%20to%20Video/Image-to-Video-Pipeline.md) (Stage 5's match-cut workflow) — see [Faking a Continuous Shot](#faking-a-continuous-shot-across-separately-generated-clips) below for how the two combine.

Source: [misterhorse.com/products/transitions-for-after-effects/3266](https://misterhorse.com/products/transitions-for-after-effects/3266) and [.../transitions-for-premiere/3280](https://misterhorse.com/products/transitions-for-premiere/3280). Requires the free Animation Composer plugin + AE or Premiere 2025+.

---

## Categories

| Category | Count | What it is | Reads as |
|---|---|---|---|
| Shapes | 101 | Geometric wipes/masks revealing the next clip | Stylized cut |
| Matte Transitions | 54 | Textured/organic mattes (ink, paper, liquid, etc.) wiping between clips | Stylized cut, can mask a cut point |
| Glitch | 54 | Digital corruption, RGB split, scanlines | Stylized cut, energetic/modern |
| Pan | 48 | Simulated whip pans / directional sweeps | **Can fake continuity** |
| Pan & Rotate | 42 | Combined pan + roll sweep | **Can fake continuity** |
| Zoom | 27 | Push/crash zoom through the frame | **Can fake continuity** |
| Zoom & Twirl | 20 | Zoom combined with a spin | **Can fake continuity** (stylized) |
| Light Leaks | 20 | Overexposed light flares/streaks | Stylized cut only |
| Rotate | 19 | Simulated camera roll | **Can fake continuity** |
| Split | 18 | Frame splits/divides to reveal next clip | Stylized cut |
| Zoom & Rotate | 17 | Zoom combined with roll | **Can fake continuity** (stylized) |
| Creative | 13 | Assorted stylized one-offs | Stylized cut |
| Blurs & Fades | 11 | Motion blur wipes, cross-fades | **Can fake continuity** |
| Roll | 14 | Simulated camera roll/tumble | **Can fake continuity** |
| Shake | 10 | Handheld-style shake punch | Stylized cut, can mask a hard cut |

(Subcategory counts sum to ~470; the product markets "600+," likely counting variants/speeds not broken out on the product page.)

---

## Faking a Continuous Shot Across Separately Generated Clips

Yes — this is a well-established filmmaking technique (the "invisible cut" or "fake oner," as in *1917*, *Birdman*, *Rope*). It works by hiding the cut inside a moment of visual chaos — motion blur, full-frame occlusion, or blown-out light — so the eye can't locate where one shot ends and the next begins. Mister Horse's pack has three category groups actually built for this; the rest are stylized cuts (visible, intentional edits) rather than continuity illusions.

### The three techniques that actually sell continuity

| Technique | MH categories | How it hides the cut | What it needs from generation |
|---|---|---|---|
| **Whip-pan / roll match** | Pan (48), Pan & Rotate (42), Rotate (19), Roll (14) | Camera motion blurs the frame to near-illegible streaks at full speed; cut happens mid-blur | Outgoing clip must end *already whipping* in the transition's direction; incoming clip must start *already moving*, same direction/speed |
| **Occlusion / pass-behind** | Matte Transitions (54), Split (18), Shake (10) | A foreground element (matte shape or a hard shake) briefly fills the entire frame; cut happens during full occlusion | Best paired with actual foreground occlusion in the reference footage/prompt — see `Push Past / Pass-by Shot` and `Pass-Through Objects` in [Camera-Movements-Library.md](Camera-Movements-Library.md) |
| **Crash-zoom match** | Zoom (27), Zoom & Rotate (17), Zoom & Twirl (20) | Camera zooms into a detail until the frame is a blur/blown-out mass; cut happens at max blur | Outgoing clip ends on a `Crash Zoom In` toward a textured/dark detail; incoming clip opens on a matching `Crash Zoom Out`/push-back from a similarly blurred state |

**Not for this purpose:** Light Leaks, Glitch, Shapes, Creative, Blurs & Fades (cross-fade variants) — these read as deliberate, visible edits. Use them when you *want* the audience to notice a cut (montage energy, scene-break punctuation), not when the goal is an unbroken take.

### Why the transition alone isn't enough

The preset masks the join, but it can't invent motion that isn't there. If the outgoing clip is static and you drop a Whip Pan Right on top, it reads as a transition slapped over a cut — not a camera that kept moving. The illusion only holds if **both clips already contain the matching motion before the transition touches them.** The edit-side preset is the last 10%; the generation prompts are the other 90%.

### Combined workflow (extends pipeline Stage 5)

1. **Pick the transition device first**, before generating either clip — e.g. "Whip Pan Right" for a beat where the character turns to face something new.
2. **Write the outgoing shot's per-shot prompt** (Stage 4) so its last ~0.5–1s already shows that exact motion: pull `Whip Pan Right` from [Camera-Movements-Library.md](Camera-Movements-Library.md) and describe it as the shot's terminal beat (use the pipeline's Timecoded mode to pin it to the clip's final second).
3. **Use the outgoing clip's last frame as the incoming clip's reference image** — this is the pipeline's existing Stage 5 match-cut step, unchanged.
4. **Write the incoming shot's prompt to open already in motion**, continuing the same whip/zoom/roll direction and speed for its first ~0.5s, before settling into its own move.
5. **In the edit**, drop the matching Mister Horse preset (same category/direction as step 1) directly over the cut point between the two clips. The preset's built-in motion blur/occlusion covers any residual seam; the pre-matched generation motion is what sells it as one camera.
6. **Squint-test it** (pipeline Stage 9) at speed, not paused — invisible cuts only have to survive real-time playback, not frame-by-frame scrutiny.

### Category → camera-movement pairing cheat sheet

| Want this illusion | Pull this MH category | Pair with this Camera-Movements-Library move |
|---|---|---|
| Character/subject turns to reveal something new | Pan / Pan & Rotate | Whip Pan Right/Left |
| Push into a detail, land somewhere new | Zoom | Crash Zoom In → Crash Zoom Out |
| Camera "spins" through a beat change | Rotate / Roll / Zoom & Rotate | Orbit Clockwise/Counterclockwise, Arc Right/Left |
| Pass behind an object into a new scene | Matte Transitions / Split | Push Past / Pass-by Shot, Pass-Through Objects |
| Hard, punchy beat cut disguised as a stumble | Shake | Handheld Shot |

---

## Usage notes

- This is an editorial (post-generation, AE/Premiere) layer — it doesn't change what you write into a Seedance/Kling prompt except for the terminal-beat motion described above.
- Reserve fake-continuity transitions for the same boundaries the pipeline already flags for match-cut treatment (Stage 5: "reserve this for the exact boundaries chosen as the transition device — not every cut"). Overusing whip-pan/crash-zoom joins reads as a gimmick, not a oner.
- For a boundary where you *want* the cut to be visible (scene break, tonal shift), pick from the "stylized cut" categories (Light Leaks, Glitch, Shapes, Creative) instead — no motion-matching required, since the goal isn't to hide anything.
- Aspect-ratio handling is automatic in both the AE and Premiere versions of the pack (vertical/square/widescreen/4K) — no extra prep needed when mixing with the pipeline's locked aspect ratio from Stage 1.
