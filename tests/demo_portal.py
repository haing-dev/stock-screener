"""Local preview of the portal with real SEC samples (tests/real_samples) and made-up prices / price history.

    python tests/demo_portal.py [out_dir]      -> a copy of site/ with unencrypted demo data in out_dir
    cd out_dir && python -m http.server 8000   -> open http://localhost:8000

Prices, 52-week ranges and month-end histories are invented (deterministic) - only the layout is real.
"""
import gzip
import json
import math
import os
import random
import shutil
import sys
import tempfile
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import qs.config as qc  # noqa: E402

TMP = tempfile.mkdtemp(prefix="qs_demo_")
qc.CACHE_DIR = os.path.join(TMP, "cache")
import qs.portal as qp  # noqa: E402
qp.CACHE_DIR = qc.CACHE_DIR
from qs.extract import CompanyData  # noqa: E402
from qs.metrics import compute, model_years  # noqa: E402
from qs.pipeline import build_ctx  # noqa: E402
from qs.screens import SCREENS  # noqa: E402
from qs.valuation import value  # noqa: E402
from qs import history  # noqa: E402

TODAY = date(2026, 10, 5)
# ticker: (sic, industry, price)
DEMO = {
    "aapl": ("3571", "Electronic Computers", 255.0), "msft": ("7372", "Services-Prepackaged Software", 520.0),
    "v": ("7389", "Services-Business Services, NEC", 345.0), "ma": ("7389", "Services-Business Services, NEC", 570.0),
    "cost": ("5331", "Retail-Variety Stores", 920.0), "mco": ("7320", "Services-Consumer Credit Reporting", 480.0),
    "adp": ("7374", "Services-Computer Processing & Data Preparation", 290.0),
    "odfl": ("4213", "Trucking (No Local)", 140.0), "spgi": ("7320", "Services-Consumer Credit Reporting", 485.0),
    "ko": ("2086", "Bottled & Canned Soft Drinks", 68.0), "intc": ("3674", "Semiconductors & Related Devices", 37.0),
    "fico": ("7389", "Services-Business Services, NEC", 1550.0), "hsy": ("2060", "Sugar & Confectionery Products", 185.0),
    "jnj": ("2834", "Pharmaceutical Preparations", 190.0), "lrcx": ("3559", "Special Industry Machinery", 140.0),
    "dhi": ("1531", "Operative Builders", 170.0), "tol": ("1531", "Operative Builders", 135.0),
    "pool": ("5090", "Wholesale-Misc Durable Goods", 310.0), "ggg": ("3561", "Pumps & Pumping Equipment", 85.0),
    "fix": ("1711", "Construction-Special Trade Contractors", 950.0),
    "ait": ("5085", "Wholesale-Industrial Supplies", 260.0), "fls": ("3561", "Pumps & Pumping Equipment", 55.0),
    "tjx": ("5651", "Retail-Family Clothing Stores", 140.0), "veev": ("7372", "Services-Prepackaged Software", 290.0),
    "snow": ("7372", "Services-Prepackaged Software", 230.0), "mth": ("1531", "Operative Builders", 75.0),
    "sndk": ("3572", "Computer Storage Devices", 120.0), "alab": ("3674", "Semiconductors & Related Devices", 210.0),
}
SUMMARY = {"msft": "Sells cloud computing (Azure), Office and other business software, Windows, LinkedIn and Xbox. "
                   "Most revenue is recurring subscriptions from businesses.",
           "mco": "Rates corporate and government bonds and sells credit data and analytics to banks and investors."}


def main(out_dir):
    cfg = qc.load_config()
    rnd = random.Random(7)
    ctxs, models, recs, info_by = {}, {}, {}, {}
    fx = {"USD": (1.0, "USD")}
    for i, (name, (sic, ind, px)) in enumerate(DEMO.items()):
        with gzip.open(os.path.join(ROOT, "tests", "real_samples", f"{name}_companyfacts_subset.json.gz"), "rt") as f:
            cd = CompanyData(json.load(f))
        res, why = compute(cd, cfg, TODAY)
        if res is None:
            print("skip", name, why)
            continue
        m, rows = res
        c = 900000 + i
        info = {"sic": sic, "sicDescription": ind, "name": cd.entity_name}
        ctx = build_ctx({"cik": c, "ticker": name.upper(), "all_tickers": [name.upper()], "name": cd.entity_name,
                         "exchange": "Nasdaq"}, info, m, rows, cd, cfg, fx, TODAY)
        q = {"ok": True, "price": px, "open": px * (1 + rnd.uniform(-0.02, 0.02)), "price_date": "2026-10-02",
             "avg_volume": 5e6, "source": "demo", "listing_type": "Common Stock"}
        ctx.update(value(ctx, {"all_tickers": [name.upper()], "name": cd.entity_name, "latest_annual": {}}, q, 1.0,
                         TODAY, listing_type="Common Stock"))
        ctx["hi_52w"], ctx["lo_52w"], ctx["range_days"] = px * rnd.uniform(1.05, 1.4), px * rnd.uniform(0.6, 0.95), 251
        ctxs[str(c)] = ctx
        mdl = model_years(cd, rows)
        if mdl:
            models[str(c)] = mdl
        recs[str(c)] = {"ticker": name.upper(), "name": cd.entity_name, "sic": sic, "industry": ind, "stage": "screened"}
        info_by[str(c)] = info
    results = {}
    for s in SCREENS:
        res = {}
        for c, ctx in ctxs.items():
            ok, why = s.universe(info_by[c], ctx, cfg)
            if ok:
                r = s.evaluate(ctx, cfg, priced=True)
                r["universe_note"] = why
                res[c] = r
        results[s.sid] = res
    state_path = os.path.join(TMP, "state.json.gz")
    state = qp.save_state(results, ctxs, recs, {"demo": True}, TODAY, path=state_path, models=models)
    state["peers10"] = history.closest_peers(ctxs, 10)
    # invented month-end price histories (deterministic random walk ending at today's price)
    hist = {}
    for c, ctx in ctxs.items():
        p, s_ = ctx["price"], {}
        for k in range(132):
            y, mo = 2026, 9 - k
            while mo <= 0:
                y, mo = y - 1, mo + 12
            s_[f"{y:04d}-{mo:02d}"] = round(p, 2)
            p = p / math.exp(rnd.gauss(0.009, 0.06))
        hist[ctx["ticker"]] = {"fetched": TODAY.isoformat(), "s": s_}
    os.makedirs(os.path.join(qc.CACHE_DIR, "prices"), exist_ok=True)
    with gzip.open(os.path.join(qc.CACHE_DIR, "prices", "monthly_history.json.gz"), "wt") as f:
        json.dump(hist, f)
    # invented 13F holders (names made up; one index fund to show it is left out of the column)
    from qs import holders as qh
    qh.OUT_PATH = os.path.join(qc.CACHE_DIR, "prices", "holders", "holders.json.gz")
    os.makedirs(os.path.dirname(qh.OUT_PATH), exist_ok=True)
    pool = ["Vanguard Group", "Northfield Partners", "Harbor Lane Capital", "Greystone Investors", "Kestrel Asset Management",
            "Meridian Value Advisors", "Juniper Hill Capital", "Ostrander Biotech Partners"]
    byc = {}
    for c, ctx in ctxs.items():
        sh = ctx.get("shares_used") or 1e8
        names = pool[:1] + rnd.sample(pool[1:], 6)
        h = [[n, 0, round(sh * w), 0.01] for n, w in zip(names, (0.09, 0.05, 0.04, 0.03, 0.025, 0.02, 0.015))]
        byc[str(c)] = {"h": h, "n": rnd.randint(150, 1900), "sp": ["Ostrander Biotech Partners"] if "Ostrander Biotech Partners" in names else []}
    with gzip.open(qh.OUT_PATH, "wt") as f:
        json.dump({"period": "2026-06-30", "by_cik": byc}, f)
    summaries = {c: {"text": SUMMARY[ctxs[c]["ticker"].lower()]} for c in ctxs if ctxs[c]["ticker"].lower() in SUMMARY}
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    shutil.copytree(os.path.join(ROOT, "site"), out_dir, ignore=shutil.ignore_patterns("data"))
    qp.export_site(state, results, cfg, summaries, "", out_dir=os.path.join(out_dir, "data"), today=TODAY,
                   allow_plain=True, salt_path=os.path.join(TMP, "salt.json"))
    print("Demo portal written to", out_dir)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(tempfile.gettempdir(), "qs_demo_site"))
