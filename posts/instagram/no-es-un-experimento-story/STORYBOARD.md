# STORYBOARD — No Es Un Experimento (Instagram Story, 9:16, ~50s)

## Big idea

One unbroken camera drifting through a chain of illustrated worlds, where a short-form contrast script — "barbero que corta en silencio" vs. "Nordic te explica el corte" — plays out as a single continuous shot instead of a cut-based reel. Cold open on a shock beat (no wind-up), a decelerating drift through a silent-barber vignette, a whip-pan into an absurd mechanic-shop analogy, a dark ambient hold for the thesis line, an ember-ignition brand reveal (the turn/payoff — deliberately withheld until the midpoint, unlike a typical logo-first open), then three morphing promise cards and a badge-and-signature close. No hard-cut scene stack: the camera itself is the throughline, same technique as `../como-agendar-citas/`.

Origin: adapted from a chapín-Spanish reel/TikTok script co-developed with the user (11 spoken beats), first explored as a 6-slide carousel, now built as a cinematic HyperFrames piece per the user's request.

## Palette & type

- UI chrome and all on-screen text stay on the strict brand tokens from `../../../design-system.md` — no deviation: `#101010` ink canvas, `#1A1A1A` charcoal panels, hairline border `rgba(247,244,236,0.08)`, `#FFD200` gold / `#C9A400` gold-deep accent (highlight role only, never a fill larger than a chip or rule), `#F7F4EC` bone text (reduced opacity for secondary labels).
- **Deliberate exception for this project (confirmed with user):** the 7 generated background illustrations (`assets/images/*.png`) use an *expanded* palette — not restricted to the 3 brand hues — to give each world (shock/cold/garage/warmth) its own emotional temperature. Every illustration still keeps gold as a recurring accent and dark/moody base tones so it reads as a Nordic property, not a foreign style. The expanded palette lives only inside the PNGs; it never leaks into CSS/text colors.
- Display/title headlines: **Lost in South**, uppercase, tracking `.07em`.
- **Hard rule carried over from this repo's known asset bug:** Lost in South has no glyphs for digits 0/2/8. This piece has no numerals on screen, so the rule is moot here but is kept in mind if any timestamp/number treatment is added later.
- Body/UI/small labels: Fira Sans Condensed (400 body, 600–700 for any UI-style labels).
- One signature-typeface use for the whole piece: the closing line "Forged for the close cut." (Lost in South, loose leading, not uppercase-forced) — the brand's actual positioning line from `design-system.md` line 11, reused verbatim rather than inventing a new tagline.

## Persistent scene rig (present 0–50s, never resets)

- `#stage` — the single framework clip (`data-start="0" data-duration="50"`), only timed element in the composition.
- `#camera` (`.world`) — one transform wrapper (`translate(x,y) scale(s)`) driven by the master timeline via `applyCamera()` on every `tl.to(...,{onUpdate})`; every scene/card div is an untimed child, visibility/position driven by `tl.to(...)` at absolute time. This is what makes the piece read as one shot instead of 10 cuts.
- `#ambient-bg` — deterministic gold ember field (index-derived trig placement, no `Math.random`) and a soft radial glow that breathes (finite-repeat sine loop, peak opacity ≤0.45). Always mounted, only visually dominant during the Analogía→Declaración→Giro stretch (18.0–33.0s) where no illustration is on screen.
- **No persistent logo watermark before the reveal** — this is a deliberate inversion of the `como-agendar-citas` pattern (which shows the lockup from t=0). Here the logo is absent until Scene 6's ignition at 29.0s so the brand reveal lands as an actual turn. After Scene 6's transition-out, the lockup shrinks to a small static corner watermark (never rotated, per design-system.md §2) and stays for the rest of the piece — same shrink mechanic `como-agendar-citas` uses right after its own open, just deployed at the midpoint instead of t=0.
- Shared **card shell** (`.morph-shell`, `card-morph-anchor` driven): charcoal panel with a backdrop illustration crop, used for Scenes 7–9 (the tricolon promise cards) and Scene 10's circular badge collapse — one shell, content/geometry morphs between beats, no cut.

## Scene list

### 0 — Hook (0:00.0–4.5)
**Concept:** Cold open, no establishing pull-back — camera is already tight on `hook-shock.png` at t=0 and pushes closer through 4.5s (`motion-blur-streak` on the punch). Headline slams in word-by-word, each word on its own jittery/off-axis entrance (`spring-pop-entrance` + `discrete-text-sequence`) to read as a shout.
**Copy:** "¿QUÉ ME HICISTE AQUÍ ATRÁS, VOS?!"
**SFX:** hard impact/hit stinger under the first word (0.0–0.3), dramatic riser as the headline completes (~3.5).
**Transition out:** camera begins pulling back into Scene 1 — no cut, continuous move.

### 1 — Reframe (4.5–9.0)
**Concept:** Camera pull-back (`multi-phase-camera`) reveals the hook illustration was sitting inside a wider world — dissolves into `reframe-cold-barber.png`. Drift noticeably decelerates (the pacing contrast is the joke: shout, then quiet). Single calm line, minimal stagger (`discrete-text-sequence`).
**Copy:** "Así te sentís cuando el barbero te corta... y no dice ni pío."
**SFX:** soft whoosh on the pull-back (~4.5–5.0).
**Transition:** drift continues laterally into Scene 2, same world, no cut.

### 2 — Contexto A (9.0–13.5)
**Concept:** Same barbershop world (`contexto-barbershop-wide.png`), lateral drift continues uninterrupted.
**Copy:** "Te sentás. Decís 'así nomás, parejito' — y ya, empieza a cortar."
**SFX:** low ambient scissor-snip texture loop starts here, low volume.
**Transition:** drift continues, beginning to decelerate toward Scene 3.

### 3 — Contexto B (13.5–18.0)
**Concept:** Drift decelerates to near-stop — the silence is visual, a deliberate hold rather than motion.
**Copy:** "Y en todo el corte no te dice nada. Ni qué te está haciendo, ni por qué."
**SFX:** scissor-snip texture fades out at scene end.
**Transition:** whip-pan (`motion-blur-streak`) into Scene 4 — a hard world-swap, the first real "cut-like" move in the piece, justified by the tonal jump into absurdist comparison.

### 4 — Analogía (18.0–24.0)
**Concept:** Whip-pan lands on `analogia-garage.png`, camera pushes in. Two-part comedic reveal: setup clause, then punchline clause, staggered as two `discrete-text-sequence` waves with a held beat between them.
**Copy:** "Es como llevar el carro al taller... y que el mecánico lo desarme sin decirte qué le va a hacer."
**SFX:** whoosh on the whip-pan-in (~18.0), metal wrench/tool clank timed to the punchline clause (~20.5–23).
**Transition:** illustration dissolves to black as camera pushes forward — `#ambient-bg` takes over, no hard cut.

### 5 — Declaración (24.0–29.0)
**Concept:** Near-black `#ambient-bg` only (embers + glow, no illustration) — the thesis line gets a clean stage. Camera almost holds still, slow push-in. Two-part line with a deliberate pause at the dash.
**Copy:** "Tu corte no es un experimento — es tu cara, todos los días."
**SFX:** bass hit/thud under the first clause (~24.0), held silence, second hit under the second clause (~26.5).
**Transition:** embers begin converging (`spring-pop-entrance` stagger) into Scene 6 — no cut, continuous.

### 6 — Giro a la marca / logo reveal (29.0–33.0)
**Concept:** Converging embers ignite the Nordic helmet mark (`logo-assemble-lockup`, Product_Intro variant) — the piece's payoff turn, deployed mid-video instead of as an opener. Camera pulls back (`multi-phase-camera`) to reveal the full lockup. Headline wipes on beneath via `discrete-text-sequence`.
**Copy:** "Por eso en Nordic lo hacemos distinto."
**SFX:** low ignition swell, then a full-weight whoosh on the pull-back.
**Transition out:** lockup shrinks to a small persistent corner watermark (`scale-swap-transition`) as the camera continues forward into the promise cards — the watermark stays mounted for the rest of the piece.

### 7 — Promesa A (33.0–36.7)
**Concept:** `.morph-shell` arrives (`orbit-3d-entry`), backdrop crop of `promesa-card-a-explica.png`, short line lands via `discrete-text-sequence`.
**Copy:** "Te explican qué te están haciendo."
**SFX:** ascending confirmation tick 1.
**Transition:** `card-morph-anchor` — same shell geometry, content swaps, no cut.

### 8 — Promesa B (36.7–40.3)
**Concept:** Shell morphs content again, backdrop crop of `promesa-card-b-forma-cara.png` (more graphic/diagram treatment than the other two cards, deliberately — this is the "expert knowledge" beat).
**Copy:** "Te sugieren según la forma de tu cara."
**SFX:** ascending confirmation tick 2.
**Transition:** `card-morph-anchor` into the third card.

### 9 — Promesa C (40.3–44.0)
**Concept:** Shell morphs a final time, backdrop crop of `promesa-card-c-en-casa.png`.
**Copy:** "Y te enseñan cómo replicarlo en casa."
**SFX:** ascending confirmation tick 3.
**Transition:** card collapses into a circular badge (`card-morph-anchor`, circle case) heading into the close.

### 10 — Close (44.0–50.0)
**Concept:** Badge holds, breathing (`sine-wave-loop`), full lockup reforms above it (matching the persistent watermark's position, scaled up). Two-part punchline with a held pause at the dash, then the signature line sets in beneath in Lost in South. Fade to ink.
**Copy:** "El que sale de Nordic, sale sabiendo por qué se ve bien — no adivinando." → "Forged for the close cut."
**SFX:** confirm thud on the badge collapse + bright success chime as the closing line lands (~44.5), low fade-out swell under the final hold (~48.5).

## Track allocation

- Track 1 — `#stage`, 0–50s, the only visual clip.
- Tracks 90/91 — BGM: Pool A "tensión" (Scenes 0–5, 0–29s) and Pool B "payoff" (Scenes 6–10, 29–50s), crossfaded via volume tweens over ~1.5s centered on the Scene 6 ignition (29.0–30.5s) — a genuine mood-change needle-drop, not a same-track loop seam.
- Tracks 92/93/94/95 — SFX lanes, split only so simultaneous one-shots don't trip the same-track-overlap lint check.

## Audio (committed)

Five BGM candidates were sourced per pool via `/media-use` (HeyGen audio-sounds catalog) and auditioned by the user. **Pool A — "dark ambient, slow minor key, suspenseful thriller tone"** (score 0.885) was picked for 0–29s, saved as `assets/bgm/track-a.mp3`. **Pool B — "uplifting contemporary product demo track, energetic and premium"** (score 0.770) was picked for 27.5–50s, saved as `assets/bgm/track-b.mp3`, crossfaded in over 1.5s at the Scene 6 ignition (29.0–30.5s). All 10 candidates (5 per pool) are recorded in `.media/manifest.jsonl` with full provenance. SFX: `assets/sfx/{hard-impact-hit-stinger-dramatic,dramatic-riser-tension-sting,whoosh-transition-swoosh,scissors-snipping-barber-ambient,metal-wrench-clank-tool,dramatic-bass-hit-thud,ignition-swell-magical-reveal,soft-ui-tap-click-select,button-press-thud-confirm,success-chime-positive-confirmation-brig}.mp3`, all from the HeyGen sound-effects catalog via `/media-use`, wired at the beat-specific cues baked into the built timeline.
