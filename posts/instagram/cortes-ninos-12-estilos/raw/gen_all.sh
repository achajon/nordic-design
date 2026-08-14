#!/bin/bash
set -e
cd "/Volumes/Alex Stuff/Nordic Design"
OUT="posts/instagram/cortes-ninos-12-estilos/assets"
GEN="python3 scripts/kie_image_gen.py"

STYLE_PREAMBLE="Editorial studio portrait photograph, square framing, of a happy 7-to-9-year-old boy. Head-and-shoulders crop, plain soft charcoal-grey seamless studio backdrop, no props. Duotone photography -- grayscale/charcoal tonal base, NOT sepia or brown -- with a single warm golden-yellow rim/key light striking one side of his hair and face for a subtle dimensional highlight, not an overall color wash. High-contrast, crisp, modern editorial style, tack-sharp focus on the hair detail. Wearing a simple plain crew-neck t-shirt, no logos, no patterns, no barber cape. Genuine warm smile, confident kid energy. Absolutely no text, no letters, no numbers, no logos, no watermarks, no graphic overlays, no UI elements anywhere in the image -- pure photography only, a clean background plate."

$GEN --out "$OUT/bg-00-portada.png" --aspect-ratio 3:4 --resolution 2K --prompt "Dramatic, realistic editorial photograph, vertical portrait orientation. Duotone grading -- grayscale/charcoal base, NOT sepia -- with a single warm golden-yellow rim/key light. High-contrast modern minimalist barbershop interior (matte black fixtures, clean lines, no wood-antique or vintage props). Scene: a happy 7-year-old boy sitting in the barber chair, seen from the front over the barber's shoulder, looking at his own reflection in a large round mirror with a satisfied grin, admiring his freshly finished haircut (short textured crop). An adult barber's hand and comb are visible at the edge of frame giving a final touch. Warm gold key light rakes across the mirror edge and the boy's hair. Leave the upper third of the frame as clean, softly out-of-focus dark negative space for later text overlay. Absolutely no text, no letters, no numbers, no logos, no watermarks, no graphic overlays anywhere in the image -- pure photography only, a clean background plate."

$GEN --out "$OUT/bg-04-cita.png" --aspect-ratio 3:4 --resolution 2K --prompt "Dramatic, realistic editorial photograph, vertical portrait orientation. Duotone grading -- grayscale/charcoal base, NOT sepia -- with a single warm golden-yellow rim/key light. High-contrast modern minimalist barbershop interior (matte black fixtures, clean lines, no wood-antique or vintage props). Scene: a joyful 8-year-old boy standing next to the barber chair giving a confident thumbs-up to the camera, fresh sharp haircut, big genuine smile, barber cape still draped over his shoulders. Warm gold rim light on his hair and shoulder, soft blurred barbershop background behind him. Leave the upper third of the frame as clean, softly out-of-focus dark negative space for later text overlay. Absolutely no text, no letters, no numbers, no logos, no watermarks, no graphic overlays anywhere in the image -- pure photography only, a clean background plate."

$GEN --out "$OUT/bg-01-taper-flequillo.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE Facing the camera straight-on. Haircut: hair grown out on top with a soft natural fringe falling over the forehead, sides tapered short with a subtle gradual fade, tousled natural texture on top -- a low taper with fringe."

$GEN --out "$OUT/bg-02-mohawk-burst.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE Turned slightly to his right, three-quarter view. Haircut: textured spiky mohawk standing up down the center of his head, sides shaved in a curved burst fade that sweeps around the ear."

$GEN --out "$OUT/bg-03-bro-flow.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE Turned slightly to his left, three-quarter view. Haircut: medium-length wavy hair with natural loose flow and movement, no fade, side-swept, effortless relaxed texture, denser and shorter than a full surfer style."

$GEN --out "$OUT/bg-04-ivy-league.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE In profile, side view. Haircut: short classic hair with a crisp side part, neatly combed, slightly longer on top than the sides, preppy polished look."

$GEN --out "$OUT/bg-05-edgar.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE Facing the camera straight-on. Haircut: short hair with a straight, blunt-cut fringe across the forehead in a clean horizontal line, sharp edges around the hairline -- an Edgar cut."

$GEN --out "$OUT/bg-06-cesar.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE Turned slightly to his right, three-quarter view. Haircut: very short hair combed forward with a short straight fringe, minimalist and neat, Roman-emperor-style crop -- a Caesar cut."

$GEN --out "$OUT/bg-07-combover.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE Turned slightly to his left, three-quarter view. Haircut: hair combed sharply to one side with a defined part line, short faded sides, sleek and polished -- a comb-over fade."

$GEN --out "$OUT/bg-08-brushup.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE In profile, side view. Haircut: hair brushed straight up from the forehead in short spiky texture, short tight fade on the sides -- a brush-up fade."

$GEN --out "$OUT/bg-09-miniwolf.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE Facing the camera straight-on. Haircut: shaggy layered haircut with lots of texture and volume, choppy layers throughout, a junior version of the wolf-cut trend."

$GEN --out "$OUT/bg-10-curtains.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE Turned slightly to his right, three-quarter view. Haircut: longer hair parted in the middle and swept to both sides like curtains framing the face, relaxed casual look."

$GEN --out "$OUT/bg-11-quiff.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE Turned slightly to his left, three-quarter view. Haircut: textured voluminous quiff swept upward and slightly back from the forehead, short tapered sides."

$GEN --out "$OUT/bg-12-surferflow.png" --aspect-ratio 1:1 --resolution 2K --prompt "$STYLE_PREAMBLE In profile, side view. Haircut: loose natural beach waves, tousled and wind-swept, medium length, effortless surfer style."

echo "ALL DONE"
