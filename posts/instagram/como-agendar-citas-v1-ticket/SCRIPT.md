# Cómo Agendar Citas — Script

Nordic Barber Shop Story video (9:16, ~41.5s). Text-driven — no voiceover. BGM bed + SFX (tap / whoosh / chime / stamp / keystrokes).

Every UI screen is a coded HTML/CSS component in Nordic's own brand language — **no photography, no screenshots** of the real Amelia booking widget. Reference flow lives in `refs/` (13 raw screenshots) for content accuracy only, never rendered directly.

**Known font bug:** `Lost in South.otf` has no glyphs for digits **0, 2, 8**. Every headline below avoids those digits. All prices/dates/times/totals anywhere in the composition render in Fira Sans Condensed ExtraBold (gold), never Lost in South.

```
00:00–00:03.4  HOOK
  Ghost logo wash + logo reveal.
  Headline (kinetic word-build): "ASÍ SE AGENDA / TU CITA" (gold on "TU CITA")

00:03.0–00:07.2  SETUP / PROMISE
  Eyebrow pill: "Guía paso a paso"
  Headline: "6 PASOS. / EN 1 MINUTO." (gold on "EN 1 MINUTO")
  Hint: "Desliza y mira" + bouncing chevron

00:06.6–00:11.6  STEP 1 — Elige tu servicio
  Step label: "1 · Elige tu servicio"
  UI: category chips (Barbería / Manicura y Pedicura / Tintes / Limpiezas Faciales / Combos)
      → service list rows with GTQ prices → "Cabello y Barba Express · GTQ130.00" taps selected
  Ticket stamps: "SERVICIO ✓ Cabello y Barba Express"

00:11.6–00:16.4  STEP 2 — Elige tu barbero
  Step label: "2 · Elige tu barbero"
  UI: barber cards (gold-ring monogram avatars, no photos) — "Renato López" selected, ring pulses
  Ticket stamps: "BARBERO ✓ Renato López"

00:16.4–00:22.0  STEP 3 — Fecha y hora  (peak beat, shader transition in)
  Step label: "3 · Fecha y hora"
  UI: month calendar grid staggers in, "8 jul" cell fills gold → time-slot pills scroll,
      "4:00 p.m. – 5:00 p.m." fills gold with a sweep
  Ticket stamps: "FECHA ✓ 8 jul, 2026 · 4:00 p.m."

00:22.0–00:26.6  STEP 4 — Tus datos
  Step label: "4 · Tus datos"
  UI: two-column form (Nombre / Apellido / Correo / Teléfono), fields type on with a blinking caret
  Ticket stamps: "CLIENTE ✓ Juan Pérez"

00:26.6–00:31.2  STEP 5 — Confirma y paga
  Step label: "5 · Confirma y paga"
  UI: receipt card — service + extra rows, subtotal counts up to "GTQ180.00", gold "Confirmar y pagar" button press

00:31.2–00:37.0  STEP 6 — ¡Cita confirmada!  (peak beat, shader transition in)
  UI: SVG checkmark draws inside a gold ring, gold spark/particle burst, ticket takes its final rune-stamp
  Headline: "CITA CONFIRMADA"
  Sub: "Cabello y Barba Express · Renato López — 8 jul, 2026 · 4:00 p.m."

00:36.4–00:41.5  OUTRO
  Logo reveal
  Signature line (Lost in South): "Nos vemos en la silla."
  CTA pill: "Reserva Ahora"
  URL caption: "nordic-barbershop.com/reservar-amelia"
```

Voice: confident, short, dry (`design-system.md` §9). No exclamation-mark copywriting — the gold accent carries emphasis, not adjectives.
