"""Bloomberg adapter: reads the workbook the user brings back from the UBC terminal (built by
docs/data_requests/build_bloomberg.py, values pasted) and serves its series to the panel and the signals.

Where the file lives: cache/macro/raw/research/bloomberg/Bloomberg_macro_UBC.xlsx (local cache, never committed:
licence). Without the file every function returns empty and the book runs on free data exactly as before.
Role of the data: HISTORY (backtests, 1970s-2026). Live monthly updates keep running on free data (GitHub has no
copy), spliced after the Bloomberg history ends.

Layout of each sheet (one block per ticker): row 2 label, row 3 ticker, row 4 field names, row 5+ date then values;
blocks sit side by side, (number of fields + 2) columns apart.
"""
import os
import re

import numpy as np
import pandas as pd

from . import panel as P

PATH = os.path.join(P.RD, "bloomberg", "Bloomberg_macro_UBC.xlsx")
_CACHE = {}

# panel market -> Bloomberg commodity excess-return index (first choice) and generic futures root (curves)
COMMOD_ER = {"cm_wti": ("SPGSCLP Index", "BCOMCL Index"), "cm_brent": ("SPGSBRP Index", "BCOMCO Index"),
             "cm_natgas": ("SPGSNGP Index", "BCOMNG Index"), "cm_heatoil": ("SPGSHOP Index", "BCOMHO Index"),
             "cm_gasoline": ("SPGSRBP Index", "BCOMRB Index"), "cm_gold": ("SPGSGCP Index", "BCOMGC Index"),
             "cm_silver": ("SPGSSIP Index", "BCOMSI Index"), "cm_copper": ("SPGSICP Index", "BCOMHG Index"),
             "cm_platinum": ("SPGSPLP Index",), "cm_corn": ("SPGSCNP Index", "BCOMCN Index"),
             "cm_wheat": ("SPGSWHP Index", "BCOMWH Index"), "cm_soybeans": ("SPGSSOP Index", "BCOMSY Index"),
             "cm_sugar": ("SPGSSBP Index", "BCOMSB Index"), "cm_coffee": ("SPGSKCP Index", "BCOMKC Index"),
             "cm_cotton": ("SPGSCTP Index", "BCOMCT Index"), "cm_cattle": ("SPGSLCP Index", "BCOMLC Index"),
             # alternative commodities (new markets once the data exist; capped at 30% of commodity risk)
             "cm_cocoa": ("SPGSCCP Index",), "cm_hogs": ("SPGSLHP Index", "BCOMLH Index"),
             "cm_feeder": ("SPGSFCP Index",), "cm_kcwheat": ("SPGSKWP Index", "BCOMKW Index"),
             "cm_soymeal": ("BCOMSM Index",), "cm_soyoil": ("BCOMBO Index",), "cm_alu": ("SPGSIAP Index", "BCOMAL Index"),
             "cm_zinc": ("SPGSIZP Index", "BCOMZS Index"), "cm_nickel": ("SPGSIKP Index", "BCOMNI Index"),
             "cm_lead": ("SPGSILP Index",), "cm_gasoil": ("SPGSGOP Index",)}
ALT_COMMOD = [k for k in COMMOD_ER if k not in ("cm_wti", "cm_brent", "cm_natgas", "cm_heatoil", "cm_gasoline",
                                                "cm_gold", "cm_silver", "cm_copper", "cm_platinum", "cm_corn",
                                                "cm_wheat", "cm_soybeans", "cm_sugar", "cm_coffee", "cm_cotton",
                                                "cm_cattle")]
CURVE_ROOT = {"cm_wti": "CL", "cm_brent": "CO", "cm_natgas": "NG", "cm_heatoil": "HO", "cm_gasoline": "XB",
              "cm_gold": "GC", "cm_silver": "SI", "cm_copper": "HG", "cm_platinum": "PL", "cm_corn": "C ",
              "cm_wheat": "W ", "cm_soybeans": "S ", "cm_sugar": "SB", "cm_coffee": "KC", "cm_cotton": "CT",
              "cm_cattle": "LC", "cm_cocoa": "CC", "cm_hogs": "LH", "cm_feeder": "FC", "cm_kcwheat": "KW",
              "cm_soymeal": "SM", "cm_soyoil": "BO", "cm_alu": "LA", "cm_zinc": "LX", "cm_nickel": "LN",
              "cm_lead": "LL", "cm_gasoil": "QS"}
EQ_INDEX = {"eq_us_spx": "MXUS Index", "eq_jp_nikkei": "MXJP Index", "eq_gb_ftse": "MXGB Index",
            "eq_de_dax": "MXDE Index", "eq_fr_cac": "MXFR Index", "eq_ca_tsx": "MXCA Index",
            "eq_au_asx": "MXAU Index", "eq_hk_hsi": "MXHK Index", "eq_cn": "MXCN Index", "eq_kr_kospi": "MXKR Index",
            "eq_tw": "MXTW Index", "eq_in": "MXIN Index", "eq_br_ibov": "MXBR Index", "eq_mx_ipc": "MXMX Index",
            "eq_za": "MXZA Index", "eq_eu_stoxx50": "MXEM Index", "eq_us_ndx": "MXUS Index", "eq_us_r2k": "MXUS Index"}


def available():
    return os.path.exists(PATH)


def load():
    """-> {sheet: {ticker: DataFrame(index=month Period, columns=fields)}}"""
    if "wb" in _CACHE:
        return _CACHE["wb"]
    out = {}
    if not available():
        _CACHE["wb"] = out
        return out
    book = pd.read_excel(PATH, sheet_name=None, header=None)
    for name, x in book.items():
        if name.lower().startswith("read"):
            continue
        blocks = {}
        if x.shape[0] < 6:
            continue
        for j in range(x.shape[1]):
            tk = x.iat[2, j] if x.shape[0] > 2 else None
            if not isinstance(tk, str) or not re.search(r"(Comdty|Index|Curncy|Govt|Equity)\s*$", tk):
                continue
            fields = []
            k = j + 1
            while k < x.shape[1] and isinstance(x.iat[3, k], str) and x.iat[3, k].strip():
                fields.append(x.iat[3, k].strip())
                k += 1
            if not fields:
                fields = ["PX_LAST"]
            d = pd.to_datetime(x.iloc[4:, j], errors="coerce")
            vals = x.iloc[4:, j + 1:j + 1 + len(fields)].apply(pd.to_numeric, errors="coerce")
            vals.columns = fields
            vals.index = d
            vals = vals[vals.index.notna()].dropna(how="all")
            if vals.empty:
                continue
            per = "D" if name.lower().startswith("daily") else "M"
            if per == "M":
                vals = vals.groupby(vals.index.to_period("M")).last()
            blocks[tk.strip()] = vals
        out[name] = blocks
    _CACHE["wb"] = out
    return out


def series(sheet, ticker, field=None):
    b = load().get(sheet, {}).get(ticker)
    if b is None or b.empty:
        return pd.Series(dtype=float)
    s = b[field] if field and field in b else b.iloc[:, -1] if field is None and b.shape[1] == 1 else b.iloc[:, 0]
    return s.reindex(P.GRID)


# ---------------------------------------------------------------- returns and markets
def commodity_return(market):
    """Monthly excess return from the first available excess-return index (GSCI, else BCOM)."""
    for tk in COMMOD_ER.get(market, ()):
        s = series("Returns", tk, "PX_LAST")
        if s.notna().sum() > 24:
            return s.pct_change(fill_method=None)
    return pd.Series(np.nan, index=P.GRID)


def commodity_carry(market):
    """Annualised carry from the generic curve: ln(F1 / F~12m) (positive = backwardation)."""
    root = CURVE_ROOT.get(market)
    if not root:
        return pd.Series(np.nan, index=P.GRID)
    blocks = load().get("Curves", {})
    f1 = [tk for tk in blocks if tk.startswith(root + "1 ")]
    far = sorted([tk for tk in blocks if tk.startswith(root) and tk != (f1[0] if f1 else "") and
                  re.match(re.escape(root) + r"(\d+) Comdty", tk)], key=lambda t: int(re.findall(r"(\d+) Comdty", t)[0]))
    if not f1 or not far:
        return pd.Series(np.nan, index=P.GRID)
    a, b = series("Curves", f1[0], "PX_LAST"), series("Curves", far[-1], "PX_LAST")
    n = int(re.findall(r"(\d+) Comdty", far[-1])[0])
    years = 1.0 if n >= 6 else max(n - 1, 1) / 12 * 3     # ~12m contract: one year; else rough spacing
    return np.log(a / b) / years


def short_rate_market(ticker="ED4 Comdty", splice="SFR4 Comdty"):
    """Short-rate futures as a market: monthly return of 1 unit notional of the 4th contract (price = 100 - rate):
    change in price / 100 x 0.25 years. Eurodollar spliced into SOFR."""
    p = series("RatesFutures", ticker, "PX_LAST").combine_first(series("RatesFutures", splice, "PX_LAST"))
    return (p.diff() / 100 * 0.25)


def implied_path(front="ED1 Comdty", deferred="ED4 Comdty"):
    """Market-implied change in the policy rate over ~9 months (percentage points): (100-P4) - (100-P1)."""
    a, b = series("RatesFutures", front, "PX_LAST"), series("RatesFutures", deferred, "PX_LAST")
    return (100 - b) - (100 - a)


# ---------------------------------------------------------------- valuation, macro, benchmarks
def equity_valuation(market):
    """Monthly DataFrame: PE_RATIO, BEST_PE_RATIO, PX_TO_BOOK_RATIO, EQY_DVD_YLD_12M, BEST_EPS."""
    b = load().get("EquityValuation", {}).get(EQ_INDEX.get(market, ""))
    return b.reindex(P.GRID) if b is not None else pd.DataFrame(index=P.GRID)


def value_composite(markets):
    """Cross-sectional equity value score: average percentile rank of forward E/P, B/P and D/P (higher = cheaper)."""
    parts = {}
    for k in markets:
        v = equity_valuation(k)
        if v.empty or v.notna().sum().sum() == 0:
            continue
        ep = 1 / v.get("BEST_PE_RATIO", v.get("PE_RATIO"))
        bp = 1 / v.get("PX_TO_BOOK_RATIO")
        dp = v.get("EQY_DVD_YLD_12M") / 100
        parts[k] = pd.concat([ep, bp, dp], axis=1, keys=["ep", "bp", "dp"])
    if not parts:
        return pd.DataFrame(index=P.GRID)
    ranks = []
    for f in ("ep", "bp", "dp"):
        X = pd.DataFrame({k: v[f] for k, v in parts.items()})
        ranks.append(X.rank(axis=1, pct=True))
    return pd.concat(ranks).groupby(level=0).mean().reindex(P.GRID)


def eps_revisions(markets, months=3):
    """Change in consensus forward EPS over `months` (percent): the live stand-in for the WRDS I/B/E/S signal."""
    return pd.DataFrame({k: np.log(equity_valuation(k).get("BEST_EPS")).diff(months)
                         for k in markets if "BEST_EPS" in equity_valuation(k)}).reindex(P.GRID)


def eco(ticker):
    """Economics sheet: release date, first release, consensus median, latest value (monthly)."""
    b = load().get("Economics", {}).get(ticker)
    return b.reindex(P.GRID) if b is not None else pd.DataFrame(index=P.GRID)


def surprise(ticker, sign=1):
    """Data surprise = (first release - consensus) / its own 5-year std, known after the release date."""
    e = eco(ticker)
    if e.empty or "ACTUAL_RELEASE" not in e or "BN_SURVEY_MEDIAN" not in e:
        return pd.Series(np.nan, index=P.GRID)
    s = (e["ACTUAL_RELEASE"] - e["BN_SURVEY_MEDIAN"]) * sign
    return (s / s.rolling(60, min_periods=24).std()).clip(-3, 3)


def breakeven(ticker):
    return series("Breakevens", ticker, "PX_LAST")


def benchmark_returns():
    return pd.DataFrame({tk: series("Benchmarks", tk, "PX_LAST").pct_change(fill_method=None)
                         for tk in load().get("Benchmarks", {})}).reindex(P.GRID)


def report():
    wb = load()
    if not wb:
        return "Bloomberg file not present (%s): free data only." % PATH
    return "; ".join("%s: %d tickers" % (s, len(b)) for s, b in wb.items())
