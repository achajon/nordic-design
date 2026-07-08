# Carousel Tile Generation — Two Approaches

Two valid ways to produce an on-brand Instagram carousel/post tile (PNG, 4:5) in this repo. Both are proven; pick per-tile, not per-carousel — a single carousel can mix both (see `posts/instagram/manicura-pedicura-hombres/`, where slides 00-04 are Option A and slide 05 is Option B).

- **Option A — Full AI generation.** One image-model call produces the finished tile: photo, headline, pill, caption, logo, all in one shot. Faster, less setup, the default starting point.
- **Option B — Hybrid HTML overlay.** The image model generates only the background photo; real HTML/CSS (actual brand fonts + logo file) renders everything else, captured to PNG via headless Chrome. Slower to set up, but typography is pixel-perfect every time.

## Decision guide

Start with **Option A** for every new slide. Move to **Option B** only if:

- The slide carries real typographic weight — a price bar, multi-line stats, several data points — where digit/font-drift risk is highest.
- A pure-AI slide comes back with visibly inconsistent lettering (e.g. one highlighted word in a different font weight/texture than the rest of the same headline) and a re-roll doesn't fix it.

Don't default to Option B for a simple single-headline-plus-pill tile — it's strictly more work for no visible benefit there.

---

## Option A — Full AI generation

Ask the image model for the complete, finished tile in one prompt.

### 1. Pick a model

`nano_banana_flash` (Higgsfield's "Nano Banana 2" — mind the display-name-vs-job_type mismatch, confirm with `higgsfield model list --json` if unsure) is the cheap default (~1.5 credits/image) and supports `aspect_ratio 4:5` natively, matching Instagram's feed spec (1080×1350) exactly. `gpt_image_2` is a solid alternative (used on earlier carousels) at higher cost (~7 credits/image) with `aspect_ratio 3:4` as its closest built-in approximation.

### 2. Always pass two brand reference images

Per `feedback_ai_image_brand_refs` in memory — without these the model invents its own logo and improvises the headline letterforms:

1. **The logo, pre-rendered white-on-ink** — not the raw `logo-variations/Nordic-BarberShop-logo-white.svg` directly (transparent-on-white renders blank in a photo). Rasterize once per carousel: `rsvg-convert --background-color '#101010'` the corrected SVG to a flat PNG, save as `posts/instagram/<carousel-name>/refs/logo-white-fixed.png`. Reuse an existing carousel's copy if the source SVG hasn't changed since.
2. **`fonts/lost_in_south/Title Character Map.png`** — the letterform reference sheet for the brand's marker font. Reference it explicitly in the prompt ("reproduce the exact letterform style shown in the character-map reference image").

### 3. Write one detailed prompt per slide

Describe, in order: the scene (duotone B&W photography, warm gold key-light, no straight color), the dark gradient scrim, the pill tag text/color, the headline text with its one highlight word called out by name and color, the caption line, and the exact unaltered placement of the logo reference. Example skeleton (see any `raw/*.json` under `posts/instagram/*/raw/` for a full worked prompt):

> "Vertical portrait brand social tile for a barbershop, exact 4:5 aspect ratio... Scene: [description]... Top-left: a small solid Nordic-yellow (#FFD200) pill... Center-lower area: a large headline reading '[HEADLINE]', set in the hand-cut marker lettering style shown in the second reference image — reproduce that exact letterform style for every single word, all uppercase — where the word [HIGHLIGHT] is solid Nordic yellow and the rest are solid bone-white... Bottom-right corner: place the exact logo lockup shown in the first reference image completely unchanged..."

If a price or stat needs digits, explicitly tell the model to set that one line in "a clean geometric sans, NOT the hand-cut marker font, so every digit renders correctly" — this sidesteps the Lost-in-South missing-glyph bug (0/2/8) even in a pure-AI generation.

```bash
higgsfield generate create nano_banana_flash \
  --prompt "$(cat prompt.txt)" \
  --image-references "refs/logo-white-fixed.png" \
  --image-references "refs/lost-in-south-character-map.png" \
  --aspect_ratio 4:5 \
  --resolution 2k \
  --wait --wait-timeout 5m --json > raw/00-slide.json

URL=$(python3 -c "import json;print(json.load(open('raw/00-slide.json'))[0]['result_url'])")
curl -sL "$URL" -o 00-slide.png
```

### 4. Review before moving on

Read the generated PNG back and check the headline letterforms are consistent across every word (not just present), and any digits render correctly. If not, re-roll once; if the same issue persists, switch that slide to Option B rather than continuing to re-roll.

---

## Option B — Hybrid HTML overlay

### Reference implementation

`posts/instagram/manicura-pedicura-hombres/05-cita-html-test/` (background: `assets/bg.png`, composition: `index.html`, output: `05-cita-v2.png`). Copy that folder's structure rather than starting from a blank file.

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

Map roles per `design-system.md` §4 — `Lost in South` for the headline/signature (uppercase, tight leading, **letter-spacing: .07em** — the font ships with zero tracking, which reads as cramped/illegible at display sizes), `Fira Sans Condensed` for the pill, caption, and **any digits/prices** (never set numbers in Lost in South — see the font's known missing-glyph bug). Colors, spacing, and the highlight-word rule are all in `design-system.md` §3/§7; don't eyeball them.

### 3. Render to PNG with headless Chrome

```bash
FILE_URL="file://$(python3 -c "import urllib.parse; print(urllib.parse.quote('$(pwd)/index.html'))")"

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu \
  --screenshot="$(pwd)/tile.png" \
  --window-size=1080,1350 \
  --force-device-scale-factor=2 \
  --hide-scrollbars \
  --virtual-time-budget=3000 \
  "$FILE_URL"
```

`--force-device-scale-factor=2` renders at 2160×2700 (2x) for a crisp final asset — downscale on export if a platform needs exactly 1080×1350. `--window-size` must equal the CSS canvas size in `index.html` (`html,body{width:1080px;height:1350px}`), or the screenshot crops/pads incorrectly. `--virtual-time-budget=3000` matters whenever the background image (or any content) is set by JS after page load rather than a static `<img src>` in the HTML — without it, the screenshot can race ahead of the image finishing to decode and capture a blank/partial frame.

---

## Scaling either approach to a full carousel

For a 6-slide carousel on a new topic:

1. Decide per-slide which option to use (Option A by default; Option B for anything digit/text-heavy) — don't commit the whole carousel to one option before seeing how Option A's slides come out.
2. If using Option A: generate + review each slide one at a time (see Option A step 4) before moving to the next, so a font-drift issue gets caught and switched to Option B early rather than at final review.
3. If using Option B for a whole carousel (not just one slide): don't hand-build N separate `index.html` files. Build **one** `index.html` with all N slides' data (background path, pill, headline, highlight word, caption) in a JS array, reading a `?slide=N` query-string param to pick which one to render — then invoke headless Chrome N times, once per `?slide=` value, to distinct output filenames. This is the pattern used in `posts/instagram/aceite-balsamo-cera/index.html`; keeps the layout in one place instead of duplicated N times.
4. If using Option B for a single slide, generate its background photo first, then build that one HTML layout (see the `05-cita-html-test/` reference implementation above).
5. Keep the same `copy.json` + `instagram-preview.html` mock convention already used elsewhere in `posts/instagram/` so the carousel is reviewable as a feed mock before publishing, regardless of which option produced each slide.

**Shell gotcha when batch-downloading generated images:** this machine's shell is zsh, where arrays are 1-indexed (not 0-indexed like bash) — a bash-style `for i in 0..N; do n=${names[$i]}; done` loop silently shifts every filename by one. Don't index arrays with a 0-based loop variable; download each generated image with an explicit, hardcoded filename per command instead, and visually spot-check at least one downloaded image against its expected scene before building overlays on top of it.

## Known-good outputs

- `posts/instagram/manicura-pedicura-hombres/00-portada.png` through `04-pies-sin-callos.png` — Option A (pure `nano_banana_flash` generation).
- `posts/instagram/manicura-pedicura-hombres/05-cita.png` — Option B (hybrid), replacing a pure-AI version that had inconsistent headline lettering.
- `posts/instagram/aceite-balsamo-cera/` — full 6-slide carousel built entirely with Option B, using the single-template-plus-query-param scaling pattern.
