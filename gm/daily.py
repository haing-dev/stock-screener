"""Daily log returns for the markets that have free daily data (used for daily volatility estimates and the
trade-timing test; the book itself still decides monthly).

FX        : Fed H.10 daily (1971+), currency value in USD.
Bonds     : daily yields -> price return ~ -duration x change in yield (FRED US 1962+, MoF Japan 1974+, Bundesbank
            1997+, BoE 1993+, RBA 1995+, Bank of Canada 2001+).
Equities  : Yahoo daily index levels (price only; dividends accrue evenly and do not affect timing comparisons).
Commodities: EIA NYMEX contract 2 for energy (1983+); Yahoo front futures for the rest (2000+, roll days removed by
            the 25% filter only; acceptable for volatility and timing, not for returns).
"""
import os
import re

import numpy as np
import pandas as pd

from . import panel as P
from . import signals as G

EQ_DAILY = {"eq_us_spx": "^GSPC", "eq_us_ndx": "^IXIC", "eq_us_r2k": "^RUT", "eq_eu_stoxx50": "^STOXX50E",
            "eq_de_dax": "^GDAXI", "eq_gb_ftse": "^FTSE", "eq_fr_cac": "^FCHI", "eq_jp_nikkei": "^N225",
            "eq_ca_tsx": "^GSPTSE", "eq_au_asx": "^AXJO", "eq_hk_hsi": "^HSI", "eq_cn": "000001.SS",
            "eq_kr_kospi": "^KS11", "eq_tw": "^TWII", "eq_in": "^BSESN", "eq_br_ibov": "^BVSP", "eq_mx_ipc": "^MXX",
            "eq_za": "EZA"}
CM_DAILY = {"cm_brent": "BZ=F", "cm_gold": "GC=F", "cm_silver": "SI=F", "cm_copper": "HG=F", "cm_platinum": "PL=F",
            "cm_corn": "ZC=F", "cm_wheat": "ZW=F", "cm_soybeans": "ZS=F", "cm_sugar": "SB=F", "cm_coffee": "KC=F",
            "cm_cotton": "CT=F", "cm_cattle": "LE=F"}


def _daily_csv(path):
    if not os.path.exists(path):
        return pd.Series(dtype=float)
    x = pd.read_csv(path)
    if "value" not in x:
        return pd.Series(dtype=float)
    v = pd.to_numeric(x["value"], errors="coerce")
    d = pd.to_datetime(x["date"], errors="coerce")
    s = pd.Series(v.values, index=d).dropna()
    s = s[s.index.notna()]
    s.index = s.index.normalize()
    return s[~s.index.duplicated(keep="last")].sort_index()


def yahoo_daily(sym):
    return _daily_csv(os.path.join(P.RD, "D_" + re.sub(r"[^A-Za-z0-9]", "_", sym) + ".csv"))


def fred_daily(sid):
    for d in (P.RD, P.RAW):
        p = os.path.join(d, sid + ".csv")
        if os.path.exists(p):
            return _daily_csv(p)
    return pd.Series(dtype=float)


def cb_daily(cc, n):
    """Daily yields from the central-bank files (same sources as panel.cb_yield, not reduced to month ends)."""
    try:
        if cc == "DE":
            rows = P._table(P._lines("cb_de_%dy.csv" % n))
            d = [(P._date(r[0]), r[1]) for r in rows if len(r) >= 2 and re.match(r"\d{4}-\d{2}-\d{2}", r[0].strip('"'))]
        elif cc == "JP":
            d = []
            for f in ("cb_jp_jgb_all.csv", "cb_jp_jgb_recent.csv"):
                rows = P._table(P._lines(f))
                hdr = next((r for r in rows if r and r[0].strip().lower() == "date"), None)
                if not hdr:
                    continue
                c = [i for i, h in enumerate(hdr) if h.strip().upper() == "%dY" % n]
                if c:
                    d += [(P._date(r[0]), r[c[0]]) for r in rows if len(r) > c[0] and r[0][:1] in "SHRTM12"]
        elif cc == "GB":
            rows = P._table(P._lines("cb_gb_yields.csv"))
            hdr = [h.strip().upper() for h in rows[0]] if rows else []
            sid = {10: "IUDMNPY", 5: "IUDSNPY"}.get(n)
            if sid not in hdr:
                return pd.Series(dtype=float)
            c = hdr.index(sid)
            d = [(P._date(r[0]), r[c]) for r in rows[1:] if len(r) > c]
        elif cc == "CA":
            rows = P._table(P._lines("cb_ca_yields.csv"))
            i0 = next((i for i, r in enumerate(rows) if r and r[0].strip() == "date"), None)
            sid = {2: "BD.CDN.2YR.DQ.YLD", 10: "BD.CDN.10YR.DQ.YLD"}.get(n)
            if i0 is None or sid not in rows[i0]:
                return pd.Series(dtype=float)
            c = rows[i0].index(sid)
            d = [(P._date(r[0]), r[c]) for r in rows[i0 + 1:] if len(r) > c]
        elif cc == "AU":
            rows = P._table(P._lines("cb_au_f2.csv"))
            frames = [rows]
            p = os.path.join(P.RD, "cb_au_f2_hist.xls")
            if os.path.exists(p):
                frames.insert(0, pd.read_excel(p, header=None).astype(str).values.tolist())
            d = []
            for rows in frames:
                i0 = next((i for i, r in enumerate(rows) if r and str(r[0]).strip() in ("Series ID", "Mnemonic")), None)
                sid = "FCMYGBAG%dD" % n
                if i0 is None or sid not in [str(x).strip() for x in rows[i0]]:
                    continue
                c = [str(x).strip() for x in rows[i0]].index(sid)
                d += [(P._date(str(r[0]).split(" ")[0] if re.match(r"\d{4}-", str(r[0])) else r[0]), r[c])
                      for r in rows[i0 + 1:] if len(r) > c]
        else:
            return pd.Series(dtype=float)
        s = pd.Series(pd.to_numeric(pd.Series([b for _, b in d]).astype(str).str.replace(",", "."), errors="coerce").values,
                      index=pd.DatetimeIndex([a for a, _ in d]))
        s = s[s.index.notna()].dropna()
        return s[~s.index.duplicated(keep="last")].sort_index()
    except Exception:  # noqa: BLE001
        return pd.Series(dtype=float)


def bond_ret(y, n):
    """Daily price return of a par bond from daily yields (percent): -modified duration x change in yield."""
    yy = (y / 100).clip(lower=1e-4)
    dur = (1 - (1 + yy / 2) ** (-2 * n)) / yy
    return -(dur.shift(1) * yy.diff())


def build():
    out = {}
    for k, (cur, cc) in G.FX_CC.items():
        if cur in P.DEX:
            sid, usd_per = P.DEX[cur]
            v = fred_daily(sid)
            if len(v):
                out[k] = np.log(v if usd_per else 1 / v).diff()
    for k, (cc, n) in G.BD.items():
        y = fred_daily({2: "DGS2", 5: "DGS5", 10: "DGS10", 30: "DGS30"}[n]) if cc == "US" else cb_daily(cc, n)
        if len(y) > 500:
            out[k] = bond_ret(y, n)
    for k, sym in EQ_DAILY.items():
        v = yahoo_daily(sym)
        if len(v) > 500:
            out[k] = np.log(v).diff()
    for k, root in P.EIA_ROOT.items():
        p = os.path.join(P.RD, "eia_%s2.xls" % root)
        if os.path.exists(p):
            x = pd.read_excel(p, sheet_name="Data 1", header=2)
            x.columns = ["date", "value"]
            v = pd.Series(pd.to_numeric(x["value"], errors="coerce").values, index=pd.to_datetime(x["date"], errors="coerce"))
            v = v[v.index.notna()].dropna()
            v = v[~v.index.duplicated()].sort_index()
            out[k] = np.log(v.clip(lower=0.01)).diff()
    for k, sym in CM_DAILY.items():
        v = yahoo_daily(sym)
        if len(v) > 500:
            out[k] = np.log(v.clip(lower=0.01)).diff()
    D = pd.DataFrame(out).sort_index()
    D = D[D.index.dayofweek < 5]
    return D.where(D.abs() < 0.25)


def coverage(D):
    return {k: (str(D[k].first_valid_index())[:10], int(D[k].notna().sum())) for k in D.columns}
