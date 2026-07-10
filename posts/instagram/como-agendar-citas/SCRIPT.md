# SCRIPT — Cómo Agendar Citas

No voiceover. Text-driven, paced by BGM/SFX. All timings are global-timeline seconds inside `#stage`. Every numeral below renders in Fira Sans Condensed ExtraBold (gold) regardless of surrounding typeface — Lost in South is missing glyphs for 0/2/8.

| Time | On-screen copy | Typeface |
|---|---|---|
| 0:00–0:03.8 | NORDIC helmet mark assembles → "ASÍ RESERVAS TU CITA" | Lost in South |
| 3.8–5.3 | Eyebrow "01" · "ELIGE TU SERVICIO" | Fira ExtraBold (num) / Lost in South (headline) |
| 5.3–11.8 | "Selección del servicio" · Servicio: dropdown → Barbería / Manicura y Pedicura / Tintes / Limpiezas Faciales / Combos → Corte de cabello Q90 · Corte de barba Q90 · Cabello y Barba Q150 · **Cabello y Barba Express Q130** (selected) · 2 Cortes de cabello Q180 · Artista: → **Renato López** (selected) | Fira Sans Condensed |
| 11.8–13.2 | Eyebrow "02" · "SUMA UN EXTRA" | Fira ExtraBold (num) / Lost in South |
| 13.2–17.2 | "Extras" · Mascarilla de Carbón Activado — Q50 · stepper 0 → 1 | Fira Sans Condensed |
| 17.2–18.6 | Eyebrow "03" · "FECHA Y HORA" | Fira ExtraBold (num) / Lost in South |
| 18.6–26.1 | "Fecha y Hora" · julio 2026 → día **8** seleccionado → 3:30 p.m.–4:30 p.m. / 3:40–4:40 / 3:50–4:50 / **4:00 p.m.–5:00 p.m.** (selected) / 4:10–5:10 / 4:20–5:20 | Fira Sans Condensed |
| 26.1–27.5 | Eyebrow "04" · "HAZLA RECURRENTE" | Fira ExtraBold (num) / Lost in South |
| 27.5–34.0 | "¿Quieres repetir esta cita?" No / **Sí** → "Cita recurrente" — Repetir cada: 1 semana · Repetir en: **mié** · Termina: Después de 1 suceso → "Resumen recurrente" — 1. Julio 8, 2026 · 4:00 p.m. / 2. Julio 15, 2026 · 4:00 p.m. | Fira Sans Condensed |
| 34.0–35.4 | Eyebrow "05" · "TUS DATOS" | Fira ExtraBold (num) / Lost in South |
| 35.4–39.4 | "Tu Información" · Nombre: **Erik** · Apellido: **Solórzano** · Correo electrónico: **erik@correo.com** · Teléfono: **5555 1234** | Fira Sans Condensed |
| 39.4–40.8 | Eyebrow "06" · "CONFIRMA Y RESERVA" | Fira ExtraBold (num) / Lost in South |
| 40.8–46.3 | "Pagos" · Subtotal Servicios Q360.00 · Importe Total → **Q360.00** (count-up) · botón "Finalizar compra" → checkmark | Fira Sans Condensed |
| 46.3–51.8 | Pill "RESERVA AHORA" · "Forged for the close cut." · nordic-barbershop.com/reservar-amelia/ | Lost in South (signature line only) / Fira Sans Condensed (pill + URL) |

## Notes

- Placeholder identity in Phase 5 ("Erik Solórzano") is generic/on-brand, not a real customer — swap freely if the user prefers a different name.
- Price math is internally consistent with the choices Phases 1-4 actually depict: (Cabello y Barba Express Q130 + Mascarilla extra Q50) × 2 recurring occurrences (julio 8 + julio 15) = **Q360.00**. This differs from the real screenshot's Q260.00 total because that session never actually incremented the extra past 0 — our version shows the extra being added on-screen, so the total must reflect it. Do not silently reuse Q260.00.
- No exclamation points anywhere, per design-system.md §9 voice rules.
