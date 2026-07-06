# Nordic Barber Shop — Brand & Content Project

This project holds the visual identity for **Nordic Barber Shop** and the design system used to generate carousels, posts, and other media for the brand's social channels and marketing pushes.

## What's in here

| File | Purpose |
|---|---|
| `design-system.html` | Interactive style guide — logo usage, color, type, and ready-to-copy components (buttons, tags, service lists, hours, post cards). Open in any browser. |
| `design-system.md` | The same system in reference/markdown form — hex values, type scale, spacing, voice rules. |
| `business-info.md` | Operational reference (not design tokens) — phone, address, hours, booking link, and full service/pricing catalog. Used by the WhatsApp virtual assistant. |
| `carousel-tile-generation.md` | Two production techniques for generating carousel/post tile PNGs — Option A: one AI call generates the finished tile (photo + text + logo); Option B: AI generates the background photo only, real HTML/CSS (brand fonts + logo file) renders the text layer via headless Chrome. Includes a decision guide for picking per-slide. |
| `NordicBarberShoplogoblack.png` | Primary logo, dark ink — for light backgrounds. |
| `NordicBarberShoplogowhite.png` | Primary logo, light ink — for dark backgrounds. |
| `NordicNuevoLogoVersiones.pdf` | All approved logo lockups and color variants (light/dark, icon-only). |
| `Title_Character_Map.png` | The brand's hand-marker alphabet — source for the signature/accent typeface used sparingly across content. |

## Purpose

This is the working reference for producing outbound content — Instagram/Facebook carousels, story tiles, promo graphics, flyers, and any other media pushed to the shop's channels. Anyone building a new post or carousel should:

1. Start from the tokens in `design-system.md` (colors, type roles, spacing) rather than eyeballing past posts.
2. Reuse the component patterns in `design-system.html` (the "Social post frame" section is the base template for carousel/post tiles: yellow eyebrow tag, one Lost in South headline with a single yellow highlight word, small caption line).
3. Pull the logo only from the approved files/lockups above — never redraw, recolor, or distort it (see the logo section of the design system for do/don't examples).
4. Keep photography duotone (grayscale + yellow key-light) and reserve the marker script for one signature phrase per piece, per the imagery and typography guidelines.
5. Build to the right canvas size: 4:5 (1080×1350) for feed posts, 9:16 (1080×1920) for Stories/Reels — see the "Instagram sizes" section of the design system.

## Status

v1.0 — identity and system established. New media assets (carousels, ad creative, seasonal campaigns, etc.) should be added to this project as they're produced, and this README updated if the file structure changes.
