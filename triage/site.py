"""Build the static site: triage/web (page code) + data/data.bin (cache/tri/out/site.json.gz, gzip + AES-256-GCM with
a key derived from PORTAL_PASSWORD, as the archived portal did; the browser decrypts) -> triage_site/.

The workflow force-pushes triage_site/ to branch 'site', which Cloudflare's Worker "stock-screener" serves.
"""
import base64
import json
import os
import shutil
import time

from qs.backtest_support import read_json
from qs.portal import SALT_PATH, Sealer

from . import paths as P

WRANGLER = {"name": "stock-screener", "compatibility_date": "2026-10-01",
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


def build(password, log=print, allow_plain=False, data=None, out_dir=None, salt_path=SALT_PATH):
    out_dir = out_dir or P.SITE
    if not password and not allow_plain:
        raise SystemExit("PORTAL_PASSWORD is not set - refusing to publish unencrypted data.")
    data = data if data is not None else read_json(os.path.join(P.OUT, "site.json.gz"))
    if not data:
        raise SystemExit("Nothing built yet - run 'build' first.")
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    shutil.copytree(P.WEB, out_dir)
    os.makedirs(os.path.join(out_dir, "data"), exist_ok=True)
    sealer = Sealer(password, salt_path)
    with open(os.path.join(out_dir, "data", "data.bin"), "wb") as f:
        f.write(sealer.seal(data))
    info = dict(sealer.info, check=base64.b64encode(sealer.seal({"ok": True})).decode())
    with open(os.path.join(out_dir, "data", "keyinfo.json"), "w", encoding="utf-8") as f:
        json.dump(info, f)
    v = time.strftime("%Y%m%d%H%M", time.gmtime())          # new file names each build: browsers never keep old code
    idx = os.path.join(out_dir, "index.html")
    with open(idx, encoding="utf-8") as f:
        html = f.read()
    with open(idx, "w", encoding="utf-8") as f:
        f.write(html.replace('href="style.css"', f'href="style.css?v={v}"').replace('src="app.js"', f'src="app.js?v={v}"'))
    with open(os.path.join(out_dir, "wrangler.jsonc"), "w", encoding="utf-8") as f:
        f.write("// Cloudflare Worker (static assets) - the triage site, published by .github/workflows/triage.yml\n")
        json.dump(WRANGLER, f, indent=2)
    with open(os.path.join(out_dir, "_headers"), "w", encoding="utf-8") as f:
        f.write(HEADERS)
    with open(os.path.join(out_dir, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nDisallow: /\n")
    n = sum(len(k["items"]) for k in data["kinds"].values())
    log(f"Site: {n} events in {len(data['kinds'])} triages -> {out_dir}" + (" (UNENCRYPTED preview)" if not password else ""))
    return out_dir
