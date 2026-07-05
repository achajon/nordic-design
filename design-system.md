# Nordic Barber Shop — Design System (v1.0)

A reference for anyone building for Nordic Barber Shop — web, social, signage, or print. Pairs with `design-system.html`, the visual style guide.

---

## 1. Brand idea

Nordic Barber Shop is built on the discipline of a Viking edge: precise, angular, unhurried. The identity is deliberately restrained — one accent color, one bold display face, one hand-cut signature detail — so that everything feels sharpened rather than decorated.

**Positioning line:** *Forged for the close cut.*

---

## 2. Logo

Source files: `NordicBarberShoplogoblack.png` (dark ink, for light backgrounds) and `NordicBarberShoplogowhite.png` (light ink, intended for dark backgrounds).

> **Note on source files:** the "white" logo file as delivered is flattened onto a solid white canvas, so it disappears when viewed on a white page. For any digital use, re-export (or request) a version with genuine alpha transparency — the design system HTML does this automatically by deriving a transparency mask from the black version.

**Anatomy:** a horned Viking helmet profile mark, always paired to the left of the "NORDIC / Barber Shop" wordmark. The helmet mark is the only element approved for standalone use (favicon, stamp, watermark, social avatar).

### Usage rules
- Clear space on all sides ≥ the height of the helmet mark itself.
- Minimum width: 120px for the full lockup, 32px for the helmet mark alone.
- Render in a single flat ink only — **ink black** or **bone white**. Never gold, never gradient, never a photo-fill.
- Never rotate, stretch/distort, recolor, or add glow/drop-shadow/bevel effects.
- The wordmark never appears without the helmet mark; the helmet mark may appear alone.

---

## 3. Color

| Token | Hex | Role |
|---|---|---|
| **Ink** | `#101010` | Primary canvas — nearly every surface starts here |
| **Charcoal** | `#1A1A1A` | Elevated surfaces: cards, panels, inputs |
| **Nordic Gold** | `#E8B324` | The single accent — CTAs, tags, rules, prices, underlines |
| **Gold, Deep** | `#A9760A` | Hover/pressed states, hairline borders where full gold is too loud |
| **Bone** | `#F7F4EC` | Primary text on ink; paper tone for print |

**Rule of thumb:** gold is a highlight, not a fill. If more than ~10–15% of a layout is gold, pull it back — it should read as a struck line or a single tag, the way a barber's razor catches light, not as a background color.

---

## 4. Typography

Three roles, each with one job. Do not blend roles (e.g., never set body copy in the display face).

| Role | Typeface | Use | Notes |
|---|---|---|---|
| **Display** | Anton | Headlines, section titles, prices | Always uppercase, tight leading (~0.92–1.05). Echoes the struck weight of the wordmark without competing with the bespoke logo lettering. |
| **Signature** | Marker script (brand's own hand alphabet, `Title_Character_Map.png`; nearest web equivalent **Permanent Marker**) | One accent phrase per layout — a promise, a call-out | Never for body copy or long lines. One use per screen/page maximum. |
| **Body / UI** | Poppins | Paragraphs, navigation, buttons, forms, schedules | Regular (400) for reading; Semibold/Bold (600–700) for labels and UI. Rounded geometry echoes the "Barber Shop" sub-wordmark. |

### Type scale

| Style | Size / Line-height | Weight |
|---|---|---|
| Display XL | 64–108px / 0.92 | Anton 400 |
| Display L | 40–52px / 1.0 | Anton 400 |
| Display M | 26–32px / 1.05 | Anton 400 |
| Signature | 28–48px / 1.3 | Marker script |
| Body | 15–17px / 1.6 | Poppins 400 |
| Label / Eyebrow | 11–12px / 1.3, +0.14em tracking | Poppins 700, uppercase |

The logo's own lettering (the angular "NORDIC" mark and the rounded "Barber Shop" script) is bespoke artwork, not a live font — it's reserved exclusively for the lockup and should never be recreated in body text.

---

## 5. Components

- **Buttons:** primary (solid gold, ink text), secondary (bone outline, transparent fill), ghost (gold outline + gold text). Uppercase label, 13px, +0.06em tracking.
- **Tags / pills:** solid gold or gold-outline, used for status labels (e.g. "New client," "Walk-ins") — echoes the flat color-block accent seen in past social campaigns.
- **Service list:** name + short description on the left, price set in Anton/gold on the right, dashed hairline divider between rows.
- **Hours table:** day in bone/bold uppercase, time range in steel, right-aligned, tabular numerals.
- **Signature callout / quote card:** one line of marker script for a testimonial or promise, small uppercase attribution below.
- **Social post frame:** 4:5 ink canvas, a gold pill eyebrow top-left, an Anton headline with one gold highlight word, small caption line at the bottom. This is the template for all social tiles — one message, one highlight word, no more.

---

## 6. Imagery

- Photography runs **high-contrast grayscale with a gold key-light** — no straight color photography in brand contexts.
- Favor tight, confident crops: chair-side portraits, tool/hand detail, interior atmosphere.
- Gold appears in imagery only as implied light (rim light, reflection), never as a flat color overlay across a whole frame.

---

## 7. Spacing

8px base unit: **8 · 16 · 24 · 40 · 64 · 96 · 140**. Use the larger steps (64–140) between major sections so the layout keeps room to breathe; use the smaller steps (8–24) inside components.

---

## 8. Voice

Confident, short, a little dry. State the hours; don't apologize for them. Lead with the specific — the cut, the hour, the price — and let the gold accent carry the emphasis instead of extra adjectives.

**Do:** *Fresh fade, guaranteed.*
**Don't:** *The most amazing haircut experience ever!!*

---

## File reference

- `design-system.html` — full interactive style guide (open in any browser; fonts load from Google Fonts, logos are embedded)
- `design-system.md` — this document
