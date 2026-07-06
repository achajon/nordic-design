#!/usr/bin/env python3
"""
Fallback image generator: calls the Gemini API directly (Nano Banana Pro /
gemini-3-pro-image-preview) for brand tiles when Higgsfield is out of credits.

Usage:
  python3 scripts/gemini_image_gen.py \
    --prompt "..." \
    --image refs/logo-white-fixed.png \
    --image "fonts/lost_in_south/Title Character Map.png" \
    --out posts/instagram/.../output.png \
    [--model gemini-3-pro-image-preview]

Reads GEMINI_API_KEY from scripts/.env (or the environment, which takes
precedence). Edit scripts/.env and replace the placeholder with your real key
-- that file is gitignored so it won't get committed.
"""
import argparse
import base64
import json
import mimetypes
import os
import sys
import urllib.request
import urllib.error

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(SCRIPT_DIR, ".env")
DEFAULT_MODEL = "gemini-3-pro-image-preview"
API_URL_TMPL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"


def load_env_file(path):
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def get_api_key():
    load_env_file(ENV_PATH)
    key = os.environ.get("GEMINI_API_KEY", "")
    if not key or key.startswith("REPLACE_WITH_"):
        sys.exit(
            "GEMINI_API_KEY is not set. Edit scripts/.env and put your real "
            "Gemini API key in place of the placeholder, then re-run."
        )
    return key


def build_parts(prompt, image_paths):
    parts = [{"text": prompt}]
    for path in image_paths:
        mime, _ = mimetypes.guess_type(path)
        mime = mime or "image/png"
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode("ascii")
        parts.append({"inline_data": {"mime_type": mime, "data": data}})
    return parts


def call_gemini(model, api_key, prompt, image_paths):
    body = {
        "contents": [{"parts": build_parts(prompt, image_paths)}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]},
    }
    url = API_URL_TMPL.format(model=model, key=api_key)
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        sys.exit(f"Gemini API error {e.code}: {detail}")


def extract_image(response, out_path):
    candidates = response.get("candidates", [])
    if not candidates:
        sys.exit(f"No candidates in response: {json.dumps(response)[:2000]}")
    parts = candidates[0].get("content", {}).get("parts", [])
    for part in parts:
        inline = part.get("inlineData") or part.get("inline_data")
        if inline and inline.get("data"):
            with open(out_path, "wb") as f:
                f.write(base64.b64decode(inline["data"]))
            return True
        if "text" in part:
            print(f"[model text] {part['text']}", file=sys.stderr)
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--image", action="append", default=[], help="Reference image path (repeatable)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    args = ap.parse_args()

    api_key = get_api_key()
    response = call_gemini(args.model, api_key, args.prompt, args.image)
    if not extract_image(response, args.out):
        sys.exit("No image data returned by the model.")
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
