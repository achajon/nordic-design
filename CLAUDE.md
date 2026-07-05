# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is not a software project — there is no build, lint, or test tooling, and no package manager. It's the brand/design-system asset store for **Nordic Barber Shop**, used to produce on-brand social content (Instagram/Facebook carousels, story tiles, promo graphics, flyers) and any future web/print collateral. The only "code" here is a single static HTML style guide; everything else is reference docs, fonts, and image/PDF assets.

## Layout

- `design-system.md` — the brand system in reference form: logo rules, color tokens, type scale, spacing, voice. Treat this as the source of truth for any new asset's tokens.
- `design-system.html` — the same system as an interactive, self-contained style guide (open directly in a browser). Logos are inlined as base64; fonts load from Google Fonts. Sections are plain `<section class="block" id="...">` blocks in order: `#logo`, `#color`, `#type`, `#components`, `#imagery`, `#spacing`, `#voice`. CSS custom properties for color and spacing tokens are declared near the top of the `<style>` block (`--ink`, `--charcoal`, `--bone`, `--gold`, `--gold-deep`, `--steel`, `--sp-1`…`--sp-7`) — update tokens there, not by hardcoding hex/px values in components.
- `logo-variations/` — approved logo lockups and color variants (black/white PNG, SVG, the "Nuevo" logo, and the full PDF of approved lockups).
- `fonts/` — the two non-Google typefaces used by the brand: Fira Sans Condensed (with license `OFL.txt`) and the hand-marker face "Lost in South" (used for the signature/accent role), plus its character map image.
- `inspirations/` — loose moodboard/reference imagery, not brand-approved assets.
- `posts/instagram/` — produced content output for the Instagram channel.

## Working in this repo

- Never redraw, recolor, or distort the logo — pull only from the files in `logo-variations/` or the lockups in the approved PDF (see `design-system.md` §2 for usage rules: clear space, minimum sizes, ink-black/bone-white only).
- New content should derive its tokens (color, type, spacing) from `design-system.md` rather than eyeballing prior posts, and reuse the component patterns already defined in `design-system.html` (e.g. the "Social post frame" in `#components` is the base template for all social tiles: 4:5 canvas, gold pill eyebrow, one Anton headline with a single gold highlight word, small caption line).
- Keep photography duotone (grayscale + gold key-light per `design-system.md` §6); no straight color photography in brand contexts. Gold is an accent (~10–15% of a layout at most), not a fill.
- The marker/signature typeface is limited to one short phrase per piece, never body copy.
- If the file structure changes (new asset folders, new logo variants, etc.), update `README.md`'s file table to match.
