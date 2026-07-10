# STORYBOARD — Cómo Agendar Citas (Instagram Story, 9:16, ~52s)

## Big idea

One unbroken camera drifting through a dark Nordic space, where the real booking flow (nordic-barbershop.com/reservar-amelia/) is rebuilt — not screenshotted — as floating charcoal UI panels in the brand's own gold-on-ink language. No slide, no hard cut: every panel arrives, gets used, and dissolves/morphs into the next through the same camera move, the way a single continuous take would. A numbered title card interrupts the flight between each phase like a chapter mark, then the camera pushes back into the scene.

Reference used for content accuracy only (not for creative direction): the 13 screenshots in `../sistema-citas-story/refs/`. Nothing from that folder's pixels appears on screen — every control, label, and price is redrawn in brand type/color.

## Palette & type (from design-system.md — no deviation)

- Canvas: `#101010` ink. Cards: `#1A1A1A` charcoal, hairline border `rgba(247,244,236,0.08)`.
- Accent: `#FFD200` gold / `#C9A400` gold-deep for pressed states. Kept to a highlight role — never a fill larger than a chip or a rule.
- Text: `#F7F4EC` bone (body), bone at reduced opacity for secondary labels.
- Display/title-card headlines + numeral-free accents: **Lost in South**, uppercase, tracking `.07em`.
- **Hard rule carried over from this repo's known asset bug:** Lost in South has no glyphs for digits 0/2/8. Every numeral on screen — prices, dates, times, totals, the "01/02/03…" eyebrow numbers — is set in **Fira Sans Condensed ExtraBold**, gold, never Lost in South. No exceptions.
- Body/UI/labels/buttons: Fira Sans Condensed (400 body, 600–700 UI labels, 800 for numerals per the rule above).
- One signature-typeface use for the whole piece: the closing line "Forged for the close cut." (Lost in South, loose leading, not uppercase-forced).

## Persistent scene rig (present 0–52s, never resets)

- `#stage` — the single framework clip (`data-start="0" data-duration="~52"`), only timed element in the composition.
- `#camera` (`.world`) — one transform wrapper (`translate3d + rotateY + scale`) driven by the master timeline; every phase/title-card div is an untimed child, visibility/position driven by `tl.to(...)` at absolute time. This is what makes the piece read as one shot instead of 8 clips.
- `#ambient-bg` — deterministic gold ember field (index-derived trig placement, no `Math.random`), a small **static** (never rotated, per design-system.md §2) Nordic lockup watermark low in the safe zone, and a soft radial glow that breathes (`sine-wave-loop`, finite repeats, peak opacity ≤0.45). Always on, always behind the stage.
- `#cursor-layer` — a small gold ring "tap" cursor that lives in DOM from t=0 at `opacity:0`, used for every simulated interaction (`cursor-click-ripple`).
- Shared **card shell** (`buildCardShell()`): charcoal panel, 720px wide, header row (label + close-style back chevron matching the real widget), a 5-segment progress-dot rail that fills as phases advance, footer gold pill button. Reused for Phases 1, 2, 3, 5, 6 so `card-morph-anchor` handoffs between them share geometry.

## Scene list

### 0 — Open (0:00.0–0:03.8)
**Concept:** Darkness. Gold embers (`spring-pop-entrance` stagger, deterministic positions) converge and ignite the Nordic helmet mark (`logo-assemble-lockup`, Product_Intro variant). Camera pulls back (`multi-phase-camera`) to reveal the dark stage. Headline wipes on beneath the mark via `discrete-text-sequence`.
**Copy:** "ASÍ RESERVAS TU CITA" (Lost in South, uppercase).
**SFX:** low ignition swell → soft whoosh on the pull-back.
**Transition out:** logo shrinks to a small persistent corner watermark (`scale-swap-transition`) as the camera continues forward into Title Card 01.

### 1 — Title Card 01 (3.8–5.3)
**Concept:** `titlecard-reveal` — gold eyebrow pill "01" + headline "ELIGE TU SERVICIO" slides up once, holds.
**Transition:** camera pushes through the card (`motion-blur-streak` on the push) into the Phase 1 panel arriving via `orbit-3d-entry`.

### 2 — Phase 1: Elige tu servicio (5.3–11.8)
**Concept:** Card shell arrives, header "Selección del servicio", progress dot 1/5 lit. Servicio dropdown opens — category rail (Barbería/Manicura y Pedicura/Tintes/Limpiezas Faciales/Combos) and priced service list cascade in (`grid-card-assemble`). Cursor taps "Cabello y Barba Express" (`cursor-click-ripple`), row highlights gold, dropdown collapses. Artista dropdown opens the same way, cursor selects "Renato López"; a small barber avatar chip spring-pops next to the name. `depth-of-field-blur` racks focus onto whichever list is active.
**Copy:** service rows drawn from the real price list — Corte de cabello Q90, Corte de barba Q90, Cabello y Barba Q150, Cabello y Barba Express Q130, 2 Cortes de cabello Q180 (all prices in Fira Sans Condensed ExtraBold gold).
**SFX:** UI tick per row hover, soft tap chime on each selection.
**Transition:** card shell `card-morph-anchor`s toward Title Card 02.

### 3 — Title Card 02 (11.8–13.2)
"SUMA UN EXTRA" — same `titlecard-reveal` treatment, dot 2/5.

### 4 — Phase 2: Suma un extra (13.2–17.2)
**Concept:** Shell content swaps to "Extras". One extra row, "Mascarilla de Carbón Activado", price Q50. Cursor taps the `+` stepper once; qty proxy counts 0→1 (`counting-dynamic-scale` bump) with `press-release-spring` on the button.
**SFX:** single tactile click + tiny gold sparkle sting on the increment.
**Transition:** `scale-swap-transition` into Title Card 03.

### 5 — Title Card 03 (17.2–18.6)
"FECHA Y HORA" — dot 3/5.

### 6 — Phase 3: Elige fecha y hora (18.6–26.1, peak beat)
**Concept:** Calendar grid for julio 2026 cascades in (`grid-card-assemble`, diagonal wave). Cursor taps day 8 (`cursor-click-ripple`); day glows gold (`ambient-glow-bloom` pulse). Mid-shot, the calendar container **morphs directly into the time-slot grid** — same panel, new content, via `card-morph-anchor` — no cut. Slot chips ("3:30 p.m.–4:30 p.m." … "4:00 p.m.–5:00 p.m." …) sweep in; cursor selects "4:00 p.m. – 5:00 p.m.", chip fills gold.
**Camera:** the longest, most deliberate push of the piece — this is the "hold" the eye rests on.
**SFX:** page-turn-soft on the calendar→slots morph, tap chime on selection.
**Transition:** camera pulls back off the panel toward Title Card 04.

### 7 — Title Card 04 (26.1–27.5)
"HAZLA RECURRENTE" — dot 4/5.

### 8 — Phase 4: Hazla recurrente (27.5–34.0)
**Concept:** Stage dims slightly (scrim) behind a small centered dialog: "¿Quieres repetir esta cita?" / No · Sí. Cursor taps "Sí" (`cursor-click-ripple` + `press-release-spring`); dialog clears and a "Cita recurrente" settings panel `orbit-3d-entry`s in — "Repetir cada: 1 semana", a day-chip rail with "mié" selected gold, "Termina: Después de 1 suceso." Panel `card-morph-anchor`s into "Resumen recurrente": two appointment chips stack in (`grid-card-assemble`) — "1. Julio 8, 2026 · 4:00 p.m." and "2. Julio 15, 2026 · 4:00 p.m."
**SFX:** dialog-open soft thud, confirm chime on "Sí", two light stamps as the chips land.
**Transition:** `scale-swap-transition` into Title Card 05.

### 9 — Title Card 05 (34.0–35.4)
"TUS DATOS" — dot 5/5.

### 10 — Phase 5: Tus datos (35.4–39.4)
**Concept:** Shell swaps to "Tu información" — four fields (Nombre, Apellido, Correo electrónico, Teléfono). Field borders draw on (`svg-path-draw`), then each fills via a typed-caret animation staggered field to field (`typewriter-reveal` / `context-sensitive-cursor`), short generic on-brand placeholder values, not real customer data.
**SFX:** soft keystroke ticks, caret blink is silent.
**Transition:** `card-morph-anchor` into Title Card 06.

### 11 — Title Card 06 (39.4–40.8)
"CONFIRMA Y RESERVA" — dots fully lit (no more segments; this reads as the finishing beat).

### 12 — Phase 6: Confirma y reserva (40.8–46.3, peak beat)
**Concept:** Shell swaps to "Pagos" — line item "Servicios · Subtotal", then "Importe Total" counts up to **Q360.00** (`counting-dynamic-scale`, Fira Sans Condensed ExtraBold gold — never Lost in South; this reflects the Q130 service + Q50 extra × 2 recurring occurrences actually shown in Phases 1-4, not the real screenshot's Q260.00, since that session never added the extra). Cursor taps "Finalizar compra" (`cursor-click-ripple` + `press-release-spring`). The card **collapses into a circular badge** (`card-morph-anchor`, circle case) and a checkmark draws on (`svg-path-draw`) with a gold `ambient-glow-bloom` release burst.
**SFX:** ascending tick per line item, weightier confirm thud on the button press, a bright success chime on the checkmark.
**Transition:** badge holds, breathing (`sine-wave-loop`), camera eases back for the close.

### 13 — Close / CTA (46.3–51.8)
**Concept:** Success badge condenses at the same screen center into a brighter gold "RESERVA AHORA" pill (`cta-morph-press`). The Nordic wordmark reforms above it (small, not the full open-scene lockup). Signature line types on beneath in Lost in South: *"Forged for the close cut."* URL "nordic-barbershop.com/reservar-amelia/" sets in below it (Fira Sans Condensed, small caps). Cursor arrives with a human-aimed decel and lands a click on the pill (`cursor-click-ripple`); scene fades to ink.
**SFX:** the piece's one full-weight whoosh into the pill, tap chime on the click, low fade-out swell.

## Track allocation

- Track 1 — `#stage`, 0–52s, the only visual clip.
- Tracks 90/95/96 — BGM (`assets/bgm/track.wav`), three sequential instances of the same 22s catalog loop crossfaded 1.5s at each seam (20.5s, 41s) via volume tweens, since the retrieved track is shorter than the composition. One track index per instance — same-track overlap is a lint error, and the overlap here is an intentional crossfade, not a conflict.
- Tracks 91/92/93/94 — SFX lanes (taps/presses, whooshes, chime/stamp/keystrokes, second stamp voice), split only so simultaneous one-shots don't trip the same-track-overlap check.

## Audio (committed)

Five BGM candidates were sourced via `/media-use` and auditioned by the user; **`bgm_002` — "energetic trendy barbershop vibe, upbeat modern hip-hop beat"** was picked, saved as `assets/bgm/track.wav`. SFX: `assets/sfx/{tap,whoosh,press,chime,stamp,keystrokes}.mp3`, all from the bundled/HeyGen SFX catalog via `/media-use`, wired at the exact interaction beats baked into the built timeline (dropdown selects, day/slot picks, button presses, chip landings, the success checkmark, and the form-typing texture).
