# Portrait Lenses & Camera Geometry — paste-ready

Cross-refers to [../../../../Lenses/Zeiss-Supreme-Prime-Lens-Library.md](../../../../Lenses/Zeiss-Supreme-Prime-Lens-Library.md) and [../../../../Depth-of-Field-Library.md](../../../../Depth-of-Field-Library.md). Focal length drives face *shape* — the wrong one distorts the nose or flattens the face, and that distortion is a strong "AI portrait" tell because generators default to a wide, close, slightly bulged look.

---

## 1. Focal length (35mm-equivalent) → face rendering

| Focal | Character | Paste-ready phrase | Use for |
|---|---|---|---|
| 35mm | Environmental, mild wide distortion if close — nose enlarges, ears recede | `35mm lens, environmental portrait, subject in their space, kept back far enough to avoid facial distortion` | Full/three-quarter body, subject-in-place |
| 50mm | Natural, close to human perspective, honest | `50mm lens, natural perspective, true-to-life facial proportions` | Half-body, casual, documentary |
| **85mm** (default) | Classic portrait compression, flattering, gentle separation | `85mm portrait lens, mild compression flattering the facial proportions, shallow but controlled depth of field` | Head-and-shoulders, the safe default |
| 105–135mm | Stronger compression, flatter facial planes, strong background melt | `135mm lens, strong compression, facial planes rendered flat and even, background dissolved to soft tone` | Tight beauty, editorial, "observed" |
| 200mm | Extreme compression + isolation, very "long-lens paparazzi / observed from distance" | `200mm telephoto, heavy compression, thin plane of focus, background a smooth wash` | Candid-at-distance register only |

Default to **85mm** unless framing (full body → 35–50mm) or register (tight editorial → 135mm) says otherwise. State the working distance: `camera roughly 1.5–2.5 m from the subject`.

## 2. Aperture / depth of field (see Depth-of-Field-Library.md for feel)

| Look | Phrase | Note |
|---|---|---|
| Thin plane (eyes sharp, ears soft) | `wide aperture around T1.5–f2, focus locked on the near eye, the far eye and ears already falling soft` | The editorial default; nail the focus point |
| Balanced portrait | `f2.8, both eyes and the nose sharp, ears softening, background clearly separated` | Safest — most flattering + forgiving |
| Deep / contexty | `f5.6, face and near background both readable, gentle separation only` | Environmental portraits |

Always name the **focus point**: `critical focus on the nearer eye`. A portrait focused on the nose or the front of the hair reads subtly wrong.

## 3. Bokeh quality (if background is defocused)

`background rendered as soft rounded bokeh, specular highlights as gentle circles with faint cat's-eye toward the edges, no harsh outlining` — pull alternates (swirly, anamorphic oval, busy) from [../../../../Depth-of-Field-Library.md](../../../../Depth-of-Field-Library.md) §"Bokeh & Background Light Quality".

## 4. Camera height vs. the eyeline — sets the read of the subject

| Height | Phrase | Reads as |
|---|---|---|
| At eye level (default) | `camera exactly at the subject's eye level, neutral relationship` | Honest, equal, standard |
| Slightly above | `camera just above eye level, subject's chin dropped a few degrees, eyes lifted to the lens` | Flattering, open, slightly vulnerable |
| Slightly below | `camera just below eye level, looking up at the subject a few degrees` | Status, authority, monumentality — subtle amounts only |
| Well above (top-down) | `high angle looking down at the subject` | Diminishing, editorial-quirky — deliberate only |

## 5. Head angle to camera

`face square to camera (symmetric, confrontational)` · `three-quarter view, face turned ~30° with the far eye still fully visible` · `two-thirds / "loose profile", face turned ~60°` · `full profile` · `looking back over the shoulder toward the lens`

## 6. Crop / framing

| Crop | Phrase |
|---|---|
| Tight beauty | `crop from mid-forehead to just below the chin, face fills the frame` |
| Headshot | `head-and-neck crop, a sliver of shoulder` |
| Head and shoulders (default) | `head-and-shoulders crop, top of frame just above the hair` |
| Half | `waist-up framing` |
| Three-quarter | `mid-thigh framing` |
| Full | `full-length, small headroom, feet included` |

State aspect ratio explicitly (`4:5 vertical`, `1:1`, `3:2`, `16:9`) — pull the project's locked ratio from Stage 1 ground rules if this portrait feeds the video pipeline.

## 7. Sensor / body

Match [../../../../Camera-Look-Library.md](../../../../Camera-Look-Library.md) §1 so a still and any video made from it agree:
`shot on an ARRI Alexa 35` / `shot on a full-frame stills camera, Canon colour science` / `medium-format digital back, extreme tonal smoothness and resolution` / `35mm film SLR, Portra 400`.

## 8. Anti-patterns

- Wide lens + very close subject = enlarged nose, tiny ears, domed forehead — the classic AI-selfie distortion. If close framing is required, say `no wide-angle facial distortion, natural nose-to-ear proportion`.
- Don't stack "shallow depth of field" onto a 35mm environmental portrait — it fights the lens (see DOF library §Overrides).
- Everything tack-sharp front to back on a "portrait" reads as a render — give it a focus plane.
