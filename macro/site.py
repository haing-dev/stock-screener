"""Build the page: macro/web + data/data.bin (cache/macro/out/compass.json.gz, gzip + AES-256-GCM with the same
PORTAL_PASSWORD key as the triage site; the browser decrypts) -> macro_site/, published as folder macro/ of branch
'site' (Cloudflare Worker "stock-screener", URL /macro/)."""
import base64
import gzip
import json
import os
import shutil
import time

from qs.portal import SALT_PATH, Sealer

WEB = os.path.join(os.path.dirname(__file__), "web")
OUT = os.path.join("cache", "macro", "out", "compass.json.gz")


def build(password, log=print, allow_plain=False, out_dir="macro_site", data=None):
    if not password and not allow_plain:
        raise SystemExit("PORTAL_PASSWORD is not set - refusing to publish unencrypted data.")
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
    html = html.replace('/macro/style.css"', f'/macro/style.css?v={v}"').replace('/macro/app.js"', f'/macro/app.js?v={v}"')
    open(idx, "w", encoding="utf-8").write(html)
    log(f"site: {out_dir} ({os.path.getsize(os.path.join(out_dir, 'data', 'data.bin')) // 1024} KB data)"
        + (" UNENCRYPTED preview" if not password else ""))
    return out_dir
