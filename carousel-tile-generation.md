# Carousel Tile Generation — Hybrid Method (AI Photo + HTML Overlay)

A production technique for generating on-brand Instagram carousel/post tiles (PNG, 4:5) that keeps typography pixel-perfect by splitting the work: **AI generates only the photography, real HTML/CSS renders all the text and the logo.**

## Why this exists

The straightforward approach — asking an image model (Nano Banana, GPT Image 2, etc.) to generate the whole tile including headline, pill, caption, price bar, and logo baked into the pixels — usually works, but the model is *drawing* letterforms from a reference image, not typesetting real text. On a `tipos-de-cara-barba`/`manicura-pedicura-hombres` carousel this showed up as:

- A single highlighted word in a headline rendered in a subtly different font weight/texture than the rest of the same line (the model didn't apply the marker-font reference consistently to every word).
- Digits (0/2/8) are unreliable when the model is asked to imitate the hand-cut "Lost in South" marker face, per the known font bug (see `fonts/lost_in_south/` — the real font file is literally missing those glyphs, and the model sometimes reproduces that gap).
- Re-rolling the same prompt sometimes fixes it, sometimes doesn't — it's a silent, inconsistent failure, not a deterministic one.

The hybrid method eliminates all of that for the text layer: nothing on the tile is ever "drawn" by the AI except the photograph itself.

**Trade-off:** more setup per tile than a single AI call (a background-only generation pass + a hand-built HTML layout per tile). Reach for it when a tile carries real typographic weight (multi-line copy, a price bar, several data points) or when a pure-AI slide comes back with visibly inconsistent lettering. For a simple single-headline tile, plain AI generation (see `feedback_ai_image_brand_refs` in memory) is still faster and usually fine.

## Reference implementation

The first working example is `posts/instagram/manicura-pedicura-hombres/05-cita-html-test/` (background: `assets/bg.png`, composition: `index.html`, output: `05-cita-v2.png`). Copy that folder's structure for a new carousel rather than starting from a blank file.

## Workflow

### 1. Generate the background photo only

Prompt the image model for **photography with nothing else** — no headline, no pill, no logo, no watermark. Be explicit about the negative:

> "...duotone grading with a warm golden-yellow rim/key light... [scene description]... Absolutely no text, no letters, no numbers, no logo, no watermark, no graphic overlays, no UI elements anywhere in the image — pure photography only, a clean background plate."

Do **not** pass the logo/character-map reference images for this step — there is nothing in the frame that should reference brand typography or the logo, so those refs only tempt the model to sneak them back in.

```bash
higgsfield generate create nano_banana_flash \
  --prompt "$(cat prompt.txt)" \
  --aspect_ratio 4:5 \
  --resolution 2k \
  --wait --wait-timeout 5m --json > raw/bg.json

URL=$(python3 -c "import json;print(json.load(open('raw/bg.json'))[0]['result_url'])")
curl -sL "$URL" -o assets/bg.png
```

`nano_banana_flash` (Higgsfield's "Nano Banana 2" — mind the display-name-vs-job_type mismatch) is the cheap default (~1.5 credits/image) and supports `aspect_ratio 4:5` natively, matching Instagram's feed spec (1080×1350) exactly.

### 2. Build the text/logo layer in real HTML + CSS

One `index.html` per tile (or one parameterized template reused per slide — see Scaling below), sized to the actual canvas (1080×1350 for a 4:5 feed tile), with:

- The background photo as a full-bleed `<img>`.
- A dark gradient scrim (`linear-gradient` over the lower portion) for legibility, per `design-system.md` §5 "Social post frame".
- The pill/eyebrow tag, headline (with its one highlight word), caption, and any data (prices, stats) as real DOM text — not baked into the photo.
- The actual logo file — `logo-variations/Nordic-BarberShop-logo-white.svg` — as an `<img>`, not a re-drawn approximation.

Load the brand's real font files via `@font-face` (copy them next to the HTML, don't rely on a system font):

```css
@font-face{
  font-family:"Lost in South";
  src:url("assets/fonts/Lost in South.otf") format("opentype");
}
@font-face{
  font-family:"Fira Sans Condensed";
  src:url("assets/fonts/FiraSansCondensed-Regular.ttf") format("truetype");
  font-weight:400;
}
@font-face{
  font-family:"Fira Sans Condensed";
  src:url("assets/fonts/FiraSansCondensed-ExtraBold.ttf") format("truetype");
  font-weight:800;
}
```

Map roles per `design-system.md` §4 — `Lost in South` for the headline/signature (uppercase, tight leading), `Fira Sans Condensed` for the pill, caption, and **any digits/prices** (never set numbers in Lost in South — see the font's known missing-glyph bug). Colors, spacing, and the highlight-word rule are all in `design-system.md` §3/§7; don't eyeball them.

### 3. Render to PNG with headless Chrome

```bash
FILE_URL="file://$(python3 -c "import urllib.parse; print(urllib.parse.quote('$(pwd)/index.html'))")"

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu \
  --screenshot="$(pwd)/tile.png" \
  --window-size=1080,1350 \
  --force-device-scale-factor=2 \
  --hide-scrollbars \
  "$FILE_URL"
```

`--force-device-scale-factor=2` renders at 2160×2700 (2x) for a crisp final asset — downscale on export if a platform needs exactly 1080×1350. `--window-size` must equal the CSS canvas size in `index.html` (`html,body{width:1080px;height:1350px}`), or the screenshot crops/pads incorrectly.

## Scaling this to a full carousel

For a 6-slide carousel on a new topic:

1. Generate all N background photos first (step 1, once per slide — vary the scene description, keep the lighting/grading language identical across slides for visual consistency).
2. Either build N separate `index.html` files (simplest, easiest to hand-tune per slide), or one templated HTML that takes a slide's copy/image path as a small JS data object and is rendered N times with different inputs (less duplication if the layout is identical across every slide, e.g. always pill + headline + caption in the same position).
3. Keep the same `copy.json` + `instagram-preview.html` mock convention already used elsewhere in `posts/instagram/` so the carousel is reviewable as a feed mock before publishing.
4. Only fall back to full pure-AI generation (single prompt, logo + character-map refs, per `feedback_ai_image_brand_refs`) for slides where the text is trivial (a single short pill + headline, no digits) and speed matters more than pixel-perfect typography.

## Known-good outputs referencing this doc

- `posts/instagram/manicura-pedicura-hombres/05-cita.png` — first tile built this way, replacing a pure-AI version that had inconsistent headline lettering.
