"""Style-fidelity test (validation/PROTOCOL.md section 8): do the managers the screens quote actually hold what
'their' screens pick? Their latest 13F holdings are run through the latest formation: the share in PASS or NEAR,
within each screen's universe, against the screen's universe-wide rate. Pass: at least 3x."""
import json
import os
import zipfile

from .backtest_support import OUT
from .config import ROOT
from .holders import (HOLD_DIR, LIST_URL, MAP_PATH, _fetch, choose_filings, guessed_links, map_issuers,
                      positions, scan_values, zip_links)
from .sec import cache_read, cache_write

MANAGERS_PATH = os.path.join(ROOT, "validation", "managers.json")


def latest_zip(client, today, log=print):
    page = _fetch(client, LIST_URL, timeout=60)
    links = zip_links(page.decode("utf-8", "replace")) if page else []
    links = links or guessed_links(today)
    os.makedirs(HOLD_DIR, exist_ok=True)
    for url, _a, _e in links[:3]:
        path = os.path.join(HOLD_DIR, "fidelity_" + url.rsplit("/", 1)[-1])
        if os.path.exists(path) and os.path.getsize(path) > 1e6:
            return path
        blob = _fetch(client, url)
        if blob:
            with open(path, "wb") as f:
                f.write(blob)
            return path
    log("  no 13F data set could be downloaded")
    return None


def run(client, form, today, log=print):
    spec = json.load(open(MANAGERS_PATH, encoding="utf-8"))["managers"]
    path = latest_zip(client, today, log)
    if not path or not form:
        return None
    ctxs = {int(c): {"ticker": x.get("tk"), "name": x.get("nm") or ""} for c, x in form["companies"].items()}
    with zipfile.ZipFile(path) as zf:
        period, accns = choose_filings(zf)
        chosen = {}
        for a, (name, mcik) in accns.items():
            up = (name or "").upper()
            for m in spec:
                if any(p in up for p in m["match"]):
                    chosen[a] = (m["who"], name)
        log(f"  13F period {period}: {len(chosen)} filings matched for {len({v[0] for v in chosen.values()})} managers")
        by_cusip, _by_acc, names = scan_values(zf, set(chosen))
        cache = cache_read(MAP_PATH) or {}
        cusip_cik, remaining = map_issuers(names, by_cusip, ctxs, cache, min_value=0, log=log,
                                           api_key=os.environ.get("OPENFIGI_API_KEY", "").strip())
        cache_write(MAP_PATH, cache)
        pos = positions(zf, set(chosen), cusip_cik)
    holdings = {}
    for cik, accs in pos.items():
        for a in accs:
            holdings.setdefault(chosen[a][0], set()).add(str(cik))
    filers = {}
    for who, name in chosen.values():
        filers.setdefault(who, set()).add(name)
    out = score(spec, holdings, form, filers)
    out.update({"period": str(period), "unmapped_issuers": remaining})
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "fidelity.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    return out


def score(spec, holdings, form, filers=None):
    """holdings: {manager: {cik as str}} -> per manager and screen: PASS-or-NEAR rate of the holdings inside the
    screen's universe, against the screen's universe-wide rate."""
    out = {"formation": form["ym"], "managers": []}
    for m in spec:
        held = holdings.get(m["who"], set())
        row = {"who": m["who"], "filers_matched": sorted((filers or {}).get(m["who"], [])),
               "holdings_mapped": len(held), "screens": {}}
        for sid in m["screens"]:
            res = form["screens"].get(sid) or {}
            uni = set(res)
            good = {c for c, r in res.items() if r[0] in ("PASS", "NEAR")}
            base = len(good) / len(uni) if uni else None
            inu = held & uni
            rate = len(inu & good) / len(inu) if inu else None
            row["screens"][sid] = {"holdings_in_universe": len(inu), "pass_or_near": len(inu & good),
                                   "rate": rate, "universe_rate": base,
                                   "ratio": (rate / base) if (rate is not None and base) else None,
                                   "passes": bool(rate is not None and base and rate >= 3 * base)}
        out["managers"].append(row)
    return out
