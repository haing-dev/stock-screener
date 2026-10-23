"""Build the page: macro/web + data/data.bin (cache/macro/out/compass.json.gz, gzip + AES-256-GCM with a key from
the password; the browser decrypts) -> macro_site/, force-pushed to branch 'macro-site', which its own Cloudflare
Worker "macro-compass" serves. Separate from the stock-screener site."""
import base64
import gzip
import json
import os
import shutil
import time

from qs.portal import Sealer

SALT_PATH = os.path.join("data", "macro_salt.json")          # own salt: its own key, separate from the triage site
WRANGLER = {"name": "macro-compass", "compatibility_date": "2026-10-01",
            "assets": {"directory": "./", "not_found_handling": "single-page-application"}}
HEADERS = """/*
  X-Robots-Tag: noindex, nofollow
  Referrer-Policy: no-referrer
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
/
  Cache-Control: no-cache
/index.html
  Cache-Control: no-cache
/data/*
  Cache-Control: no-cache
"""

WEB = os.path.join(os.path.dirname(__file__), "web")
OUT = os.path.join("cache", "macro", "out", "compass.json.gz")


def build(password, log=print, allow_plain=False, out_dir="macro_site", data=None):
    if not password and not allow_plain:
        raise SystemExit("MACRO_PASSWORD / PORTAL_PASSWORD not set - refusing to publish unencrypted data.")
    if data is None:
        if not os.path.exists(OUT):
            raise SystemExit("Nothing built yet - run 'build' first.")
        data = json.load(gzip.open(OUT, "rt"))
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    shutil.copytree(WEB, out_dir)
    os.makedirs(os.path.join(out_dir, "data"), exist_ok=True)
    sealer = Sealer(password, SALT_PATH)
    with open(os.path.join(out_dir, "data", "data.bin"), "wb") as f:
        f.write(sealer.seal(data))
    info = dict(sealer.info, check=base64.b64encode(sealer.seal({"ok": True})).decode())
    with open(os.path.join(out_dir, "data", "keyinfo.json"), "w", encoding="utf-8") as f:
        json.dump(info, f)
    v = time.strftime("%Y%m%d%H%M", time.gmtime())          # new file names each build: browsers never keep old code
    idx = os.path.join(out_dir, "index.html")
    html = open(idx, encoding="utf-8").read()
    html = html.replace('/style.css"', f'/style.css?v={v}"').replace('/app.js"', f'/app.js?v={v}"')
    open(idx, "w", encoding="utf-8").write(html)
    with open(os.path.join(out_dir, "wrangler.jsonc"), "w", encoding="utf-8") as f:
        f.write("// Cloudflare Worker (static assets) - Macro Compass, published by .github/workflows/macro.yml\n")
        json.dump(WRANGLER, f, indent=2)
    with open(os.path.join(out_dir, ".assetsignore"), "w", encoding="utf-8") as f:
        f.write("wrangler.jsonc\n.assetsignore\n.git\n")
    with open(os.path.join(out_dir, "_headers"), "w", encoding="utf-8") as f:
        f.write(HEADERS)
    with open(os.path.join(out_dir, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nDisallow: /\n")
    log(f"site: {out_dir} ({os.path.getsize(os.path.join(out_dir, 'data', 'data.bin')) // 1024} KB data)"
        + (" UNENCRYPTED preview" if not password else ""))
    return out_dir
