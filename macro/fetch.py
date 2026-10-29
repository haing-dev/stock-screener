"""Download every raw series the Macro Compass needs into cache/macro/raw/ (one CSV per series: date,value).

Sources (all free): FRED (API with FRED_API_KEY: first-published values for revised series; else the public CSV),
Yahoo Finance monthly adjusted closes (dividends included) with Stooq as fallback, Kenneth French industry and
factor returns, multpl.com Shiller CAPE, monthly gold (datahub.io gold-prices on GitHub),
AQR commodity futures index (excess returns since 1877). Each source fails on its own; manifest.json says what worked.
"""
import csv
import io
import json
import os
import re
import time
import zipfile

import requests

from . import registry as R

RAW = os.path.join("cache", "macro", "raw")
UA = {"User-Agent": "Mozilla/5.0 (macro-compass research; GitHub Actions)"}
FRENCH_URL = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/"


def _get(url, tries=3, **kw):
    last = None
    for i in range(tries):
        try:
            r = requests.get(url, headers=UA, timeout=60, **kw)
            if r.status_code == 200:
                return r
            last = f"HTTP {r.status_code}"
            if r.status_code in (400, 401, 403, 404):
                break
        except requests.RequestException as e:
            last = str(e)[:120]
        time.sleep(2 * (i + 1))
    raise RuntimeError(last or "failed")


def _write(name, rows):
    os.makedirs(RAW, exist_ok=True)
    with open(os.path.join(RAW, f"{name}.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "value"])
        w.writerows(rows)
    return len(rows)


def fred(sid, spec, key):
    """-> rows (date, value). First-published values when a key is set and the series is revised."""
    if key:
        params = {"series_id": sid, "api_key": key, "file_type": "json"}
        if spec.get("fr"):
            params.update(realtime_start="1776-07-04", realtime_end="9999-12-31", output_type=4)
        js = _get("https://api.stlouisfed.org/fred/series/observations", params=params).json()
        rows = [(o["date"], o["value"]) for o in js.get("observations", []) if o.get("value") not in (".", "", None)]
        if rows:
            return rows, "first release" if spec.get("fr") else "api"
    txt = _get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}").text
    rows = []
    for row in list(csv.reader(io.StringIO(txt)))[1:]:
        if len(row) >= 2 and row[1] not in (".", ""):
            rows.append((row[0], row[1]))
    return rows, "latest (public csv)"


def yahoo(sym):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
    js = _get(url, params={"period1": 0, "period2": 9999999999, "interval": "1mo", "events": "div,split",
                           "includeAdjustedClose": "true"}).json()
    res = js["chart"]["result"][0]
    ts = res["timestamp"]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose") or res["indicators"]["quote"][0]["close"]
    rows = []
    for t, v in zip(ts, adj):
        if v is not None:
            rows.append((time.strftime("%Y-%m-%d", time.gmtime(t)), round(float(v), 6)))
    return rows


def stooq(sym):
    s = {"DX-Y.NYB": "dx.f"}.get(sym, sym.lower() + ".us")
    txt = _get(f"https://stooq.com/q/d/l/?s={s}&i=m").text
    rows = []
    for row in list(csv.reader(io.StringIO(txt)))[1:]:
        if len(row) >= 5 and row[4]:
            rows.append((row[0], row[4]))
    if not rows:
        raise RuntimeError("no rows")
    return rows


def french(fname):
    from qs.btstats import parse_french
    data = parse_french(_get(FRENCH_URL + fname).content)
    return data


def cape():
    html = _get("https://www.multpl.com/shiller-pe/table/by-month").text
    rows = []
    for d, v in re.findall(r"<td>\s*([A-Z][a-z]{2} \d{1,2}, \d{4})\s*</td>\s*<td>\s*(?:&#x2002;)?\s*([\d.]+)", html):
        rows.append((time.strftime("%Y-%m-%d", time.strptime(d, "%b %d, %Y")), v))
    if len(rows) < 100:
        raise RuntimeError(f"only {len(rows)} rows parsed")
    return sorted(rows)


AQR_COMMOD_URL = ("https://www.aqr.com/-/media/AQR/Documents/Insights/Data-Sets/"
                  "Commodities-for-the-Long-Run-Index-Level-Data-Monthly.xlsx")


def aqr_commodities(content=None):
    """Equal-weight commodity futures excess return (first data column), month-end dates."""
    import pandas as pd
    content = content if content is not None else _get(AQR_COMMOD_URL).content
    d = pd.read_excel(io.BytesIO(content), sheet_name=0, header=None)
    dt = pd.to_datetime(d.iloc[:, 0], errors="coerce")
    v = pd.to_numeric(d.iloc[:, 1], errors="coerce")
    ok = dt.notna() & v.notna()
    rows = [(x.strftime("%Y-%m-%d"), round(float(y), 8)) for x, y in zip(dt[ok], v[ok])]
    if len(rows) < 500:
        raise RuntimeError(f"only {len(rows)} rows")
    return rows


def run(log=print):
    key = os.environ.get("FRED_API_KEY", "").strip()
    man = {"fetched": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "fred_key": bool(key), "series": {}}
    for sid, spec in R.FRED.items():
        try:
            rows, how = fred(sid, spec, key)
            man["series"][sid] = {"ok": True, "rows": _write(sid, rows), "last": rows[-1][0], "how": how}
        except Exception as e:
            man["series"][sid] = {"ok": False, "error": str(e)[:200]}
        time.sleep(0.6)
    for sid in getattr(R, "EXTRA_FRED", []):
        try:
            rows, how = fred(sid, {}, key)
            man["series"][sid] = {"ok": True, "rows": _write(sid, rows), "first": rows[0][0], "last": rows[-1][0], "how": how}
        except Exception as e:
            man["series"][sid] = {"ok": False, "error": str(e)[:200]}
        time.sleep(0.6)
    syms = R.YAHOO + [i["etf"] for i in R.INDUSTRIES]
    for s in syms:
        name = "Y_" + s.replace("-", "_").replace(".", "_").replace("^", "").replace("=", "_")
        try:
            try:
                rows, how = yahoo(s), "yahoo"
            except Exception as e1:
                rows, how = stooq(s), f"stooq (yahoo: {str(e1)[:60]})"
            man["series"][name] = {"ok": True, "rows": _write(name, rows), "first": rows[0][0], "last": rows[-1][0],
                                   "how": how}
        except Exception as e:
            man["series"][name] = {"ok": False, "error": str(e)[:200]}
        time.sleep(1.0)
    for tag, fname in (("FR_IND", R.FRENCH_IND), ("FR_FF", R.FRENCH_FF)):
        try:
            data = french(fname)
            os.makedirs(RAW, exist_ok=True)
            with open(os.path.join(RAW, f"{tag}.json"), "w") as f:
                json.dump(data, f, separators=(",", ":"))
            ks = sorted(data)
            man["series"][tag] = {"ok": True, "rows": len(ks), "first": ks[0], "last": ks[-1]}
        except Exception as e:
            man["series"][tag] = {"ok": False, "error": str(e)[:200]}
    try:
        rows = cape()
        man["series"]["CAPE"] = {"ok": True, "rows": _write("CAPE", rows), "first": rows[0][0], "last": rows[-1][0]}
    except Exception as e:
        man["series"]["CAPE"] = {"ok": False, "error": str(e)[:200]}
    try:                                     # gold, monthly average London price since 1833 (datahub.io on GitHub)
        txt = _get("https://raw.githubusercontent.com/datasets/gold-prices/main/data/monthly.csv").text
        rows = [(r[0] + "-01", r[1]) for r in list(csv.reader(io.StringIO(txt)))[1:] if len(r) >= 2 and r[1]]
        man["series"]["GOLD"] = {"ok": True, "rows": _write("GOLD", rows), "first": rows[0][0], "last": rows[-1][0]}
    except Exception as e:
        man["series"]["GOLD"] = {"ok": False, "error": str(e)[:200]}
    try:                                     # commodity futures index, monthly excess return since 1877 (AQR data set)
        rows = aqr_commodities()
        man["series"]["AQR_COMMOD"] = {"ok": True, "rows": _write("AQR_COMMOD", rows), "first": rows[0][0], "last": rows[-1][0]}
    except Exception as e:
        man["series"]["AQR_COMMOD"] = {"ok": False, "error": str(e)[:200]}
    os.makedirs(RAW, exist_ok=True)
    with open(os.path.join(RAW, "manifest.json"), "w") as f:
        json.dump(man, f, indent=1)
    bad = [k for k, v in man["series"].items() if not v["ok"]]
    log(f"fetch: {len(man['series']) - len(bad)} ok, {len(bad)} failed {bad}; FRED key {'set' if key else 'NOT set'}")
    return man
