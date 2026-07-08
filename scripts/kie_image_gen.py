#!/usr/bin/env python3
"""
kie.ai image generator: calls the kie.ai GPT Image 2 text-to-image API
(gpt-image-2-text-to-image) for brand tiles.

Usage:
  python3 scripts/kie_image_gen.py \
    --prompt "..." \
    --out posts/instagram/.../output.png \
    [--aspect-ratio 5:4] [--resolution 1K]

Note: kie.ai does not support 2K/4K with aspect ratios 5:4, 4:5, 3:1, 1:3, or
9:21 -- the task will fail to create. Use 1K with those ratios, or pick a
supported ratio (e.g. 4:3/3:4) for 2K/4K.

Reads KIE_API_KEY from scripts/.env (or the environment, which takes
precedence). Edit scripts/.env and replace the placeholder with your real key
-- that file is gitignored so it won't get committed.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(SCRIPT_DIR, ".env")
MODEL = "gpt-image-2-text-to-image"
CREATE_URL = "https://api.kie.ai/api/v1/jobs/createTask"
RECORD_URL = "https://api.kie.ai/api/v1/jobs/recordInfo"

UNSUPPORTED_HIGH_RES_RATIOS = {"5:4", "4:5", "3:1", "1:3", "9:21"}


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
    key = os.environ.get("KIE_API_KEY", "")
    if not key or key.startswith("REPLACE_WITH_"):
        sys.exit(
            "KIE_API_KEY is not set. Edit scripts/.env and put your real "
            "kie.ai API key in place of the placeholder, then re-run."
        )
    return key


def http_post_json(url, api_key, body):
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        sys.exit(f"kie.ai API error {e.code}: {detail}")


def http_get_json(url, api_key, params):
    query = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
    req = urllib.request.Request(
        f"{url}?{query}",
        headers={"Authorization": f"Bearer {api_key}"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        sys.exit(f"kie.ai API error {e.code}: {detail}")


def create_task(api_key, prompt, aspect_ratio, resolution):
    if resolution in ("2K", "4K") and aspect_ratio in UNSUPPORTED_HIGH_RES_RATIOS:
        sys.exit(
            f"kie.ai does not support {resolution} with aspect_ratio={aspect_ratio} "
            f"(unsupported at 2K/4K: {sorted(UNSUPPORTED_HIGH_RES_RATIOS)}). "
            "Use 1K, or switch to a supported ratio."
        )
    input_params = {"prompt": prompt, "aspect_ratio": aspect_ratio}
    if resolution:
        input_params["resolution"] = resolution
    body = {"model": MODEL, "input": input_params}
    resp = http_post_json(CREATE_URL, api_key, body)
    if resp.get("code") != 200:
        sys.exit(f"createTask failed: {json.dumps(resp)}")
    return resp["data"]["taskId"]


def poll_task(api_key, task_id, interval=3, timeout=300):
    elapsed = 0
    while elapsed < timeout:
        resp = http_get_json(RECORD_URL, api_key, {"taskId": task_id})
        data = resp.get("data", {})
        state = data.get("state")
        if state == "success":
            return data
        if state == "fail":
            sys.exit(f"Task failed: {data.get('failCode')} {data.get('failMsg')}")
        print(f"[state={state}] waiting...", file=sys.stderr)
        time.sleep(interval)
        elapsed += interval
    sys.exit(f"Timed out after {timeout}s waiting for task {task_id}")


def download_image(url, out_path):
    with urllib.request.urlopen(url, timeout=120) as resp:
        with open(out_path, "wb") as f:
            f.write(resp.read())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--aspect-ratio", default="auto")
    ap.add_argument("--resolution", default=None, choices=["1K", "2K", "4K"])
    args = ap.parse_args()

    api_key = get_api_key()
    task_id = create_task(api_key, args.prompt, args.aspect_ratio, args.resolution)
    print(f"Task created: {task_id}", file=sys.stderr)
    data = poll_task(api_key, task_id)
    result = json.loads(data["resultJson"])
    urls = result.get("resultUrls") or []
    if not urls:
        sys.exit(f"No resultUrls in response: {json.dumps(data)[:2000]}")
    download_image(urls[0], args.out)
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
