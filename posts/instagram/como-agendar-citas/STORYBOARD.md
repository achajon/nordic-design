# Cómo Agendar Citas — Storyboard

9:16 · 1080×1920 · ~41.5s · No voiceover — text + BGM/SFX only.

## Big idea

**"The forge, not the form."** Instead of a phone replaying a screen recording, each choice the viewer makes gets **stamped into a boarding-pass-style ticket** that assembles itself next to the phone — service, barber, date/time each land with a rune-stamp hit and a spark. This second depth layer (phone + ticket) is what keeps the piece from reading as a flat slide deck.

**Palette/type:** `design-system.md` tokens only — `--ink #101010` canvas, `--charcoal #1a1a1a` cards, `--gold #ffd200` / `--gold-deep #c9a400` accent (~10-15% of frame max, never a fill), `--bone` text. Fira Sans Condensed for all UI/body text, Lost in South (uppercase, +0.07em tracking) for headlines and the outro signature line only. Every "screenshot" is a coded component — zero photography.

**Rhythm:** quick-quick-**MEDIUM**-quick-quick-**HOLD**. Steps 1/2/4/5 are fast CSS push/slide beats; step 3 (calendar/time) and step 6 (confirmation) are the two peaks — the only two spots with a shader transition, per the "1-2 shader transitions per reel" rule.

---

## Hook (0–3.4s)
- **Concept:** the logo isn't just faded in — it's struck, like a stamp hitting leather.
- **Mood:** cinematic title card, unhurried but deliberate.
- **Choreography:** ghost logo DRIFTS (slow scale/opacity breathing) · real logo SNAPS in on a short overshoot · headline words SLAM in staggered · gold word gets a brief underline-draw.
- **Depth layers:** BG ink + very low-opacity radial gold glow (breathing). MG ghost logo. FG real logo + headline.
- **SFX:** whoosh under the logo snap.
- **Transition out:** velocity-matched blur/slide into Setup (CSS).

## Setup (3.0–7.2s)
- **Concept:** the promise, stated plainly — six steps, one minute, no exclamation points.
- **Choreography:** eyebrow pill FILLS in · headline word-builds, numeral gets a slight scale-punch · hint chevron PULSES on loop.
- **Depth layers:** BG ghost word "Agenda" at ~5% opacity, slow drift. MG pill + headline. FG hint/chevron.
- **SFX:** whoosh on entry.
- **Transition:** CSS push-slide — phone rig "arrives" from below, like it's being placed on a workbench.

## Steps 1–2 — Servicio, Barbero (6.6–16.4s)
- **Concept:** the phone is a workbench tool, not a recording. Every tap is a decision that immediately becomes physical on the ticket.
- **Mood:** crisp, mechanical, satisfying — a well-made hardware keyboard, not a soft consumer app.
- **Choreography:** category chips SNAP across in a stagger · selected service row FILLS gold + check DRAWS · barber cards float in a row, tapped card's ring EXPANDS/pulses gold, others dim. Ticket panel (docked right edge) receives each confirmed line with a rune-stamp: scale-punch + spark burst + a thin gold divider DRAWS underneath.
- **Depth layers:** BG ink + faint corner tick-mark rule pattern (echoes existing Nordic social pieces). MG phone frame, gold rim-light breathing. FG step-label kinetic type (top) + ticket strip (side) + tap-dot/ring per touch.
- **SFX:** `tap.mp3` on each selection; `stamp.mp3` on each ticket line landing.
- **Transition 1→2:** fast CSS push-slide inside the phone screen (content pushes left, like real in-app navigation) — never a hard cut.

## Step 3 — Fecha y hora (16.4–22.0s) — PEAK
- **Concept:** time made tangible. The calendar assembles cell by cell; the chosen date+time lock in with the most weight of any interaction so far.
- **Choreography:** calendar cells ASSEMBLE in a diagonal stagger wave · selected date cell SNAPS gold with a ring pulse · time-slot list auto-scrolls, selected pill FILLS with a left-to-right gold sweep. Camera: subtle phone tilt/parallax intensifies here — this is the "hold" moment.
- **Depth layers:** BG ink + gold glow pulses brighter than other steps (marks the peak). MG calendar/time UI. FG ticket stamp "FECHA ✓" landing.
- **SFX:** rapid soft ticks as cells assemble, heavier chime on date lock, sweep whoosh on time-slot fill.
- **Transition in from step 2:** shader (whip-pan or sdf-iris) — one of only two shader moments.

## Step 4 — Tus datos (22.0–26.6s)
- **Concept:** a hand filling out a form with total confidence — no hesitation, no backspacing.
- **Choreography:** field boxes DRAW (border stroke-in) · text TYPES ON with a visible caret · labels FLOAT up from placeholder position on focus (reused Nordic form pattern from `design-system.html` `#components`).
- **Depth layers:** BG ink. MG form card. FG ticket stamp "CLIENTE ✓".
- **SFX:** `keystrokes.mp3` under the typing beat, one `tap.mp3` on the confirm.
- **Transition:** CSS push-slide.

## Step 5 — Confirma y paga (26.6–31.2s)
- **Concept:** the tally. A receipt card that adds itself up in front of you.
- **Choreography:** service/extra rows STAGGER in · price column COUNTS UP to GTQ180.00 · "Confirmar y pagar" button gets a press-scale + gold ripple on tap.
- **Depth layers:** BG ink. MG receipt card. FG button + ticket panel (now nearly full).
- **SFX:** `chime.mp3` on total lock, `tap.mp3` on button press.
- **Transition:** CSS push-slide into confirmation, hinged on the button press.

## Step 6 — Cita confirmada (31.2–37.0s) — PEAK
- **Concept:** the payoff. Everything the last 30s built collapses into one clean stamp.
- **Choreography:** SVG ring TRACES, checkmark path DRAWS (stroke-dashoffset) · gold spark/particle burst RADIATES outward once on lock · headline "CITA CONFIRMADA" SLAMS in · sub-line FADES up softly beneath it. Ticket panel gets its last stamp + a full gold divider draws its length.
- **Depth layers:** BG ink + strongest gold glow of the piece (emotional peak). MG phone + success card. FG ticket (complete) + headline.
- **SFX:** `chime.mp3` (bright, resolved) + a soft spark texture under the particle burst.
- **Transition in:** shader (ridged-burn or sdf-iris) — second and last shader moment, reserved for the payoff.

## Outro (36.4–41.5s)
- **Concept:** mirrors the hook — the logo returns, calm and resolved, an invitation rather than a promise.
- **Choreography:** logo SNAPS in (same weight as hook) · signature line FADES/DRIFTS up in Lost in South script · CTA pill and URL caption settle beneath a thin gold rule.
- **Depth layers:** BG ink + ghost word "Nordic" drifting. MG logo + signature. FG CTA pill + URL.
- **SFX:** final whoosh + chime tail decaying under the BGM.
- **Transition:** fade to ink hold.
