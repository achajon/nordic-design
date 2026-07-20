# Nordic Barber Shop — Design System (v1.0)

A reference for anyone building for Nordic Barber Shop — web, social, signage, or print. Pairs with `design-system.html`, the visual style guide.

---

## 1. Brand idea

Nordic Barber Shop is built on the discipline of a Viking edge: precise, angular, unhurried. The identity is deliberately restrained — one accent color, one bold display face, one hand-cut signature detail — so that everything feels sharpened rather than decorated.

**Positioning line:** *Cada corte, forjado con precisión.*

---

## 2. Logo

Source files: `logo-variations/Nordic-BarberShop-logo-black.png` (dark ink, for light backgrounds) and `logo-variations/Nordic-BarberShop-logo-white.svg` (light ink, genuine alpha transparency, for dark backgrounds and social posts).

> **Note on source files:** the earlier "white" logo PNG was flattened onto a solid white canvas and disappeared on white pages. It has been replaced by `Nordic-BarberShop-logo-white.svg`, a vector export with true transparency — use this one for any dark-background or social-post placement going forward.

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
| **Nordic Yellow** | `#FFD200` | The single accent — CTAs, tags, rules, prices, underlines |
| **Yellow, Deep** | `#C9A400` | Hover/pressed states, hairline borders where full yellow is too loud |
| **Bone** | `#F7F4EC` | Primary text on ink; paper tone for print |

Only three hues exist in this system — ink (black), bone (white), and Nordic Yellow. Charcoal and Yellow, Deep are tonal steps of those two, used for elevation and pressed states, not new colors. Secondary/tertiary text is bone at reduced opacity (see `design-system.html`'s `--steel`/`--steel-dim` tokens), never a separate gray.

**Rule of thumb:** yellow is a highlight, not a fill. If more than ~10–15% of a layout is yellow, pull it back — it should read as a struck line or a single tag, the way a barber's razor catches light, not as a background color.

---

## 4. Typography

Three roles, each with one job. Do not blend roles (e.g., never set body copy in the display face).

| Role | Typeface | Use | Notes |
|---|---|---|---|
| **Display** | Lost in South (`fonts/lost_in_south/Lost in South.otf`) | Headlines, section titles, prices | Always uppercase, tight leading (~0.92–1.05), letter-spacing: .07em. The font's own tracking is zero, which reads as cramped/illegible at display sizes — the .07em opens it back up without breaking the hand-cut letterforms. The brand's own hand-cut face, used for structure now rather than a single accent phrase. |
| **Signature** | Lost in South | One accent phrase per layout — a promise, a call-out | Same font file as Display, set at a looser line-height and without the forced uppercase. Same letter-spacing: .07em applies. Never for body copy or long lines. One use per screen/page maximum. |
| **Body / UI** | Fira Sans Condensed (`fonts/Fira Sans Condensed/`) | Paragraphs, navigation, buttons, forms, schedules | Regular (400) for reading; Semibold/Bold (600–700) for labels and UI. Set in bone (white) on ink. |

### Type scale

| Style | Size / Line-height | Weight |
|---|---|---|
| Display XL | 64–108px / 0.92, +0.07em tracking | Lost in South |
| Display L | 40–52px / 1.0, +0.07em tracking | Lost in South |
| Display M | 26–32px / 1.05, +0.07em tracking | Lost in South |
| Signature | 28–48px / 1.3, +0.07em tracking | Lost in South |
| Body | 15–17px / 1.6 | Fira Sans Condensed 400 |
| Label / Eyebrow | 11–12px / 1.3, +0.14em tracking | Fira Sans Condensed 700, uppercase |

The logo's own lettering (the angular "NORDIC" mark and the rounded "Barber Shop" script) is bespoke artwork, not a live font — it's reserved exclusively for the lockup and should never be recreated in body text.

---

## 5. Components

- **Buttons:** primary (solid gold, ink text), secondary (bone outline, transparent fill), ghost (gold outline + gold text). Uppercase label, 13px, +0.06em tracking.
- **Tags / pills:** solid gold or gold-outline, used for status labels (e.g. "New client," "Walk-ins") — echoes the flat color-block accent seen in past social campaigns.
- **Service list:** name + short description on the left, price set in Lost in South/yellow on the right, dashed hairline divider between rows.
- **Hours table:** day in bone/bold uppercase, time range in steel, right-aligned, tabular numerals.
- **Signature callout / quote card:** one line of marker script for a testimonial or promise, small uppercase attribution below.
- **Social post frame:** 4:5 (1080×1350) ink canvas, a yellow pill eyebrow top-left, a Lost in South headline with one yellow highlight word, small caption line at the bottom, and a small white logo mark (`logo-variations/Nordic-BarberShop-logo-white.svg`) watermarked in the corner. This is the template for all social tiles — one message, one highlight word, no more.

---

## 6. Imagery

- Photography runs **high-contrast grayscale with a yellow key-light** — no straight color photography in brand contexts.
- Favor tight, confident crops: chair-side portraits, tool/hand detail, interior atmosphere.
- Yellow appears in imagery only as implied light (rim light, reflection), never as a flat color overlay across a whole frame.

---

## 7. Spacing

8px base unit: **8 · 16 · 24 · 40 · 64 · 96 · 140**. Use the larger steps (64–140) between major sections so the layout keeps room to breathe; use the smaller steps (8–24) inside components.

---

## 8. Instagram sizes

Default to **4:5 for feed posts** and **9:16 for Stories/Reels**. Build the layout to the target ratio — don't stretch or crop the lockup to force a fit.

| Placement | Aspect ratio | Pixel size | Notes |
|---|---|---|---|
| Feed post (default) | 4:5 | 1080 × 1350px | Matches the Social post frame component. Instagram's grid preview crops feed images to 3:4, so keep faces, logo, and copy inside the top 1080×1440. |
| Feed post, square (alt) | 1:1 | 1080 × 1080px | Use only when a piece genuinely needs a centered, symmetrical crop. |
| Story / Reel | 9:16 | 1080 × 1920px | Full-screen vertical — the only ratio with no bars or cropping. Keep logo and copy out of the top and bottom ~250px, reserved for Instagram's own UI (reply bar, captions, profile chip). |

---

## 9. Voice

Confident, short, warm — talk to people the way you'd talk to a regular who just walked in, not a customer filing a complaint. State the hours; don't apologize for them. Lead with the specific — the cut, the hour, the price — and let the yellow accent carry the emphasis instead of extra adjectives. A little friendliness is welcome (a greeting, a "listo para vos", a light touch of humor); stay short and confident, not stiff — but don't swing into slangy or overly casual either.

**Do:** *Fresh fade, guaranteed. Te esperamos.*
**Don't:** *The most amazing haircut experience ever!!*
**Also don't:** cold, notice-board phrasing for things that affect people directly (e.g. announcements, reminders) — say it like you'd tell a friend, not post a memo.

---

## File reference

- `design-system.html` — full interactive style guide (open in any browser from this folder; fonts load locally from `fonts/`, logos load from `logo-variations/` — keep both folders alongside the HTML file)
- `design-system.md` — this document
- `fonts/lost_in_south/` — the Display/Signature typeface, `Lost in South.otf`/`.ttf`
- `fonts/Fira Sans Condensed/` — the Body/UI typeface, weights 400–800
- `logo-variations/Nordic-BarberShop-logo-white.svg` — dark-background and social-post lockup
- `logo-variations/Nordic-BarberShop-logo-black.png` — light-background lockup
