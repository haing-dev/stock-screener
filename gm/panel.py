"""Global Macro Book - phase 0 panel: monthly futures-style EXCESS returns for the 64-market universe, from free data.

Reads cache/macro/raw/research (research_fetch downloads: Yahoo, FRED/OECD/BIS, stooq, World Bank, French, AQR).
Writes cache/gm/panel.pkl {grid, R (excess returns), SRC (source by period), FLAG (quality notes), RF (local rates)}.

Conventions (month-end, decided at t, earned over t+1 by the backtest):
  equity   hedged local excess return = local total return - local 3-month rate. Local total return = USD country ETF
           (dividends included) converted to local currency where the ETF exists; before it, the local price index plus
           the dividend yield the ETF era implies (flag 'div proxy').
  bonds    10-year (and US 2/5/30-year) par bond priced from month-end yields where daily data exist, else from the
           OECD monthly AVERAGE yield (flag 'avg yield': smooths returns), minus the local 3-month rate.
  short    3-month rate future: -0.25 x change in the 3-month rate (OECD monthly average; flag).
  FX       long the currency vs USD: change in USD value + (foreign - US 3-month rate)/12.
  commod.  ETF excess return where an ETF exists; before it the front futures price change (roll gaps; flag
           'unadjusted front'); before 2000 the World Bank monthly average spot (flag 'spot avg').
  spreads  US 2s10s steepener (2y minus 10y per unit of duration, scaled to 5 years), US 10-year breakeven
           (TIPS minus nominal, duration 8), German 2s10s (needs a German 2-year yield; missing -> flagged).
"""
import os
import re
import zipfile

import numpy as np
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RD = os.path.join(REPO, "cache", "macro", "raw", "research")
RAW = os.path.join(REPO, "cache", "macro", "raw")
OUT = os.path.join(REPO, "cache", "gm")
GRID = pd.period_range("1960-01", pd.Timestamp.today().strftime("%Y-%m"), freq="M")


# ------------------------------------------------------------------ loaders
def _csv(path, yahoo=False, stooq=False):
    if not os.path.exists(path):
        return pd.Series(np.nan, index=GRID)
    s = pd.read_csv(path)
    if stooq:
        s = s.rename(columns={"Date": "date", "Close": "value"})
    if "value" not in s:
        return pd.Series(np.nan, index=GRID)
    s = s[pd.to_numeric(s["value"], errors="coerce").notna()]
    d = pd.to_datetime(s["date"], errors="coerce")
    per = d.dt.to_period("M")
    if yahoo:      # Yahoo monthly bars stamped at local midnight on the 1st -> day >= 20 belongs to the next month
        per = per.where(d.dt.day < 20, per + 1)
    return pd.Series(s["value"].astype(float).values, index=per).groupby(level=0).last().reindex(GRID)


def Y(sym):
    return _csv(os.path.join(RD, "Y_" + re.sub(r"[^A-Za-z0-9]", "_", sym) + ".csv"), yahoo=True)


def S(sym):
    return _csv(os.path.join(RD, "S_" + re.sub(r"[^A-Za-z0-9]", "_", sym) + ".csv"), stooq=True)


def F(sid):
    p = os.path.join(RD, sid + ".csv")
    return _csv(p if os.path.exists(p) else os.path.join(RAW, sid + ".csv"))


def ret(p):
    return p.pct_change(fill_method=None)


def first(*xs):
    """Splice: the first series wins where it exists, later ones fill earlier gaps."""
    out = xs[0].copy()
    for x in xs[1:]:
        out = out.combine_first(x)
    return out


def par_ret(y, n):
    c, yy = y.shift(1) / 100, y / 100
    k = 2 * (n - 1 / 12)
    pv = (c / 2) * (1 - (1 + yy / 2) ** (-k)) / (yy / 2) + (1 + yy / 2) ** (-k)
    return pv - 1 + c / 12


def french_rf_mkt():
    try:
        z = zipfile.ZipFile(os.path.join(RD, "french_5f.zip"))
        txt = z.read(z.namelist()[0]).decode("latin-1").splitlines()
        rows = []
        for ln in txt:
            p = [x.strip() for x in ln.split(",")]
            if len(p) >= 7 and re.fullmatch(r"\d{6}", p[0]):
                rows.append((pd.Period(p[0][:4] + "-" + p[0][4:], "M"), float(p[1]) / 100, float(p[6]) / 100))
            elif rows and len(p) and re.fullmatch(r"\d{4}", p[0] or ""):
                break                                   # annual section starts
        df = pd.DataFrame(rows, columns=["m", "mkt_rf", "rf"]).set_index("m")
        return df["mkt_rf"].reindex(GRID), df["rf"].reindex(GRID)
    except Exception:  # noqa: BLE001
        return pd.Series(np.nan, index=GRID), pd.Series(np.nan, index=GRID)


# ------------------------------------------------------------------ universe
EQUITY = {  # id: (country ETF in USD, local price index candidates, currency code, 3m-rate country, dividend fallback)
    "eq_us_spx": (None, None, "USD", "US", None),
    "eq_us_ndx": ("QQQ", ["^IXIC"], "USD", "US", 0.01),
    "eq_us_r2k": ("IWM", ["^RUT"], "USD", "US", 0.015),
    "eq_eu_stoxx50": ("EZU", ["^STOXX50E"], "EUR", "EZ", 0.03),
    "eq_de_dax": ("EWG", ["^GDAXI|tr", "^dax|tr"], "EUR", "DE", 0.0),   # DAX is a total-return index
    "eq_gb_ftse": ("EWU", ["^FTSE", "^ukx"], "GBP", "GB", 0.035),
    "eq_fr_cac": ("EWQ", ["^FCHI", "^cac"], "EUR", "FR", 0.03),
    "eq_jp_nikkei": ("EWJ", ["^N225", "^nkx"], "JPY", "JP", 0.015),
    "eq_ca_tsx": ("EWC", ["^GSPTSE", "^tsx"], "CAD", "CA", 0.028),
    "eq_au_asx": ("EWA", ["^AXJO", "^aor"], "AUD", "AU", 0.04),
    "eq_hk_hsi": ("EWH", ["^HSI", "^hsi"], "HKD", "US", 0.035),
    "eq_cn": ("MCHI", ["FXI|etf", "000001.SS"], "CNY", "CN", 0.02),
    "eq_kr_kospi": ("EWY", ["^KS11", "^kospi"], "KRW", "KR", 0.015),
    "eq_tw": ("EWT", ["^TWII", "^twse"], "TWD", "US", 0.03),
    "eq_in": ("INDA", ["^BSESN", "^NSEI"], "INR", "IN", 0.013),
    "eq_br_ibov": ("EWZ", ["^BVSP", "^bvp"], "BRL", "BR", 0.04),
    "eq_mx_ipc": ("EWW", ["^MXX", "^ipc"], "MXN", "MX", 0.025),
    "eq_za": ("EZA", ["^JN0U.JO"], "ZAR", "ZA", 0.035),
}
STQ_Y = {("US", 10): "10usy.b", ("DE", 10): "10dey.b", ("GB", 10): "10uky.b", ("JP", 10): "10jpy.b",
         ("CA", 10): "10cay.b", ("AU", 10): "10auy.b", ("US", 2): "2usy.b", ("DE", 2): "2dey.b", ("GB", 2): "2uky.b",
         ("JP", 2): "2jpy.b", ("CA", 2): "2cay.b", ("AU", 2): "2auy.b"}
BONDS = {  # id: (country code for OECD 10y, daily FRED series for month-end yield, maturity)
    "bd_us_2y": ("US", "DGS2", 2), "bd_us_5y": ("US", "DGS5", 5), "bd_us_10y": ("US", "DGS10", 10),
    "bd_us_30y": ("US", "DGS30", 30), "bd_de_10y": ("DE", None, 10), "bd_gb_10y": ("GB", None, 10),
    "bd_jp_10y": ("JP", None, 10), "bd_ca_10y": ("CA", None, 10), "bd_au_10y": ("AU", None, 10),
}
SHORT = {"st_us_2y": "US", "st_de_2y": "DE", "st_gb_2y": "GB", "st_ca_2y": "CA", "st_au_2y": "AU"}
FXM = {  # id: (currency, FRED monthly, quoted USD per unit?, Yahoo month-end, 3m-rate country)
    "fx_eur": ("EUR", "EXUSEU", True, "EURUSD=X", "EZ"), "fx_jpy": ("JPY", "EXJPUS", False, "JPY=X", "JP"),
    "fx_gbp": ("GBP", "EXUSUK", True, "GBPUSD=X", "GB"), "fx_chf": ("CHF", "EXSZUS", False, "CHF=X", "CH"),
    "fx_aud": ("AUD", "EXUSAL", True, "AUDUSD=X", "AU"), "fx_nzd": ("NZD", "EXUSNZ", True, "NZDUSD=X", "NZ"),
    "fx_cad": ("CAD", "EXCAUS", False, "CAD=X", "CA"), "fx_sek": ("SEK", "EXSDUS", False, "SEKUSD=X|usd", "SE"),
    "fx_nok": ("NOK", "EXNOUS", False, "NOKUSD=X|usd", "NO"), "fx_mxn": ("MXN", "EXMXUS", False, "MXN=X", "MX"),
    "fx_brl": ("BRL", "EXBZUS", False, "BRL=X", "BR"), "fx_krw": ("KRW", "EXKOUS", False, "KRW=X", "KR"),
    "fx_zar": ("ZAR", "EXSFUS", False, "ZAR=X", "ZA"),
}
COMMOD = {  # id: (ETF, Yahoo front future, stooq continuous, World Bank pink-sheet column keyword)
    "cm_wti": ("USO", "CL=F", "cl.f", "Crude oil, WTI"), "cm_brent": ("BNO", "BZ=F", "co.f", "Crude oil, Brent"),
    "cm_natgas": ("UNG", "NG=F", "ng.f", "Natural gas, US"), "cm_heatoil": (None, "HO=F", "ho.f", None),
    "cm_gasoline": (None, "RB=F", "rb.f", None), "cm_gold": ("GLD", "GC=F", "gc.f", "Gold"),
    "cm_silver": ("SLV", "SI=F", "si.f", "Silver"), "cm_copper": ("CPER", "HG=F", "hg.f", "Copper"),
    "cm_platinum": ("PPLT", "PL=F", "pl.f", "Platinum"), "cm_corn": ("CORN", "ZC=F", "zc.f", "Maize"),
    "cm_wheat": ("WEAT", "ZW=F", "zw.f", "Wheat, US HRW"), "cm_soybeans": (None, "ZS=F", "zs.f", "Soybeans"),
    "cm_sugar": (None, "SB=F", "sb.f", "Sugar, world"), "cm_coffee": (None, "KC=F", "kc.f", "Coffee, Arabica"),
    "cm_cotton": (None, "CT=F", "ct.f", "Cotton, A Index"), "cm_cattle": (None, "LE=F", "lc.f", "Beef"),
}
SPREADS = ["sp_us_2s10s", "sp_de_2s10s", "sp_us_breakeven10"]


# ------------------------------------------------------------------ building blocks
def rate3m(cc):
    """Local 3-month rate, % p.a. (OECD interbank; US T-bill; euro area spliced onto Germany)."""
    if cc == "US":
        return first(F("TB3MS"), F("IR3TIB01USM156N"))
    if cc == "EZ":
        return first(F("IR3TIB01EZM156N"), F("IR3TIB01DEM156N"))
    alt = {"BR": ["IRSTCI01BRM156N"], "ZA": ["IR3TIB01ZAM156N", "IRSTCI01ZAM156N"], "KR": ["IR3TIB01KRM156N", "IRSTCI01KRM156N"]}
    return first(*[F(s) for s in (["IR3TIB01%sM156N" % cc] + alt.get(cc, []))])


STQ_FX = {"EUR": ("eurusd", True), "GBP": ("gbpusd", True), "JPY": ("usdjpy", False), "CHF": ("usdchf", False),
          "AUD": ("audusd", True), "NZD": ("nzdusd", True), "CAD": ("usdcad", False), "SEK": ("usdsek", False),
          "NOK": ("usdnok", False), "MXN": ("usdmxn", False), "BRL": ("usdbrl", False), "KRW": ("usdkrw", False),
          "ZAR": ("usdzar", False), "INR": ("usdinr", False), "CNY": ("usdcny", False), "TWD": ("usdtwd", False),
          "HKD": ("usdhkd", False)}
DEX = {"EUR": ("DEXUSEU", True), "JPY": ("DEXJPUS", False), "GBP": ("DEXUSUK", True), "CHF": ("DEXSZUS", False),
       "AUD": ("DEXUSAL", True), "NZD": ("DEXUSNZ", True), "CAD": ("DEXCAUS", False), "SEK": ("DEXSDUS", False),
       "NOK": ("DEXNOUS", False), "MXN": ("DEXMXUS", False), "BRL": ("DEXBZUS", False), "KRW": ("DEXKOUS", False),
       "ZAR": ("DEXSFUS", False), "INR": ("DEXINUS", False), "CNY": ("DEXCHUS", False), "TWD": ("DEXTAUS", False),
       "HKD": ("DEXHKUS", False)}
ALLOW_AVG = False      # monthly-average sources smooth returns and fake trends (phase-0 check); off by default


def fx_usd_value(cur):
    """USD value of one unit of the currency at month end: Yahoo, stooq, FRED H.10 daily; FRED monthly averages only
    when ALLOW_AVG."""
    if cur == "USD":
        return pd.Series(1.0, index=GRID)
    parts = []
    for k, (c, fred, usd_per, yh, _) in FXM.items():
        if c == cur:
            sym, inv = yh.split("|")[0], yh.endswith("|usd")
            y = Y(sym)
            parts.append(y if (usd_per or inv) else 1 / y)
    if cur in {"CNY": 1, "INR": 1}:
        parts.append(1 / Y(cur + "=X"))
    if cur in STQ_FX:
        sym, usd_per = STQ_FX[cur]
        x = S(sym)
        parts.append(x if usd_per else 1 / x)
    if cur in DEX:
        sid, usd_per = DEX[cur]
        x = F(sid)
        parts.append(x if usd_per else 1 / x)
    if ALLOW_AVG:
        for k, (c, fred, usd_per, yh, _) in FXM.items():
            if c == cur:
                m = F(fred)
                parts.append(m if usd_per else 1 / m)
    return first(*parts) if parts else pd.Series(np.nan, index=GRID)


def build():
    R, SRC, FLAG = {}, {}, {}
    mkt_rf, rf_us = french_rf_mkt()
    rf_us = first(rf_us, F("TB3MS") / 1200)

    def note(k, parts, flags=()):
        SRC[k] = parts
        FLAG[k] = list(flags)

    # equities -----------------------------------------------------------------
    for k, (etf, idxs, cur, cc, div) in EQUITY.items():
        rl = rate3m(cc) / 1200
        if k == "eq_us_spx":
            spy = ret(Y("SPY")) - rf_us
            R[k] = first(spy, mkt_rf)
            note(k, ["SPY total return (1993+)", "French US market (1963+)"])
            continue
        fxv = fx_usd_value(cur)
        fx_ch = fxv / fxv.shift(1)                       # USD value change of the currency
        parts, flags, pieces = [], [], []
        if etf:
            r_usd = ret(Y(etf))
            r_loc = (1 + r_usd) / fx_ch - 1               # convert USD total return to local currency
            pieces.append(r_loc - rl)
            parts.append("%s ETF total return in %s" % (etf, cur))
        for ix in idxs or []:
            sym, tag = (ix.split("|") + [""])[:2]
            px = S(sym) if (sym.startswith("^") and sym.lower() == sym) or sym.endswith(".f") else Y(sym)
            r_px = ret(px)
            if tag == "etf":
                r_px = (1 + r_px) / fx_ch - 1
            d = 0.0 if tag in ("tr", "etf") else div
            if etf and r_px.notna().sum() and pieces[0].notna().sum() > 60 and tag != "tr":
                both = pieces[0].notna() & r_px.notna() & rl.notna()
                if both.sum() > 60:                       # dividend yield implied by the ETF era
                    d = float(np.clip(((pieces[0] + rl) - r_px)[both].mean() * 12, 0, 0.06))
            pieces.append(r_px + d / 12 - rl)
            parts.append("%s price index + %.1f%%/yr dividends" % (sym, d * 100) if tag not in ("tr",) else sym + " (total return)")
            if tag not in ("tr",):
                flags.append("div proxy before ETF")
        R[k] = first(*pieces)
        note(k, parts, sorted(set(flags)) + (["local rate missing"] if rl.notna().sum() < 120 else []))

    # bonds ----------------------------------------------------------------------
    for k, (cc, daily, n) in BONDS.items():
        rl = rate3m(cc) / 1200
        pieces, parts, flags = [], [], []
        if daily:
            pieces.append(par_ret(F(daily), n) - rl)
            parts.append("%s month-end yield, %dy par bond" % (daily, n))
        if (cc, n) in STQ_Y:
            pieces.append(par_ret(S(STQ_Y[(cc, n)]), n) - rl)
            parts.append("stooq %s month-end yield" % STQ_Y[(cc, n)])
        if ALLOW_AVG:
            gs = {2: "GS2", 5: "GS5", 10: "GS10", 30: "GS30"}.get(n) if cc == "US" else None
            if gs:
                pieces.append(par_ret(F(gs), n) - rl)
            pieces.append(par_ret(F("IRLTLT01%sM156N" % cc), 10) - rl)
            parts.append("monthly-average yields")
            flags.append("avg yield (smoothed returns)")
        R[k] = first(*pieces) if pieces else pd.Series(np.nan, index=GRID)
        note(k, parts, flags)

    # front end: 2-year government notes from month-end yields (stands in for 3-month rate futures, whose free
    # history exists only as monthly averages)
    for k, cc in SHORT.items():
        y2 = F("DGS2") if cc == "US" else S(STQ_Y[(cc, 2)])
        R[k] = par_ret(y2, 2) - rate3m("EZ" if cc == "DE" else cc) / 1200
        note(k, ["2y month-end yield, par note"], [] if y2.notna().sum() > 120 else ["MISSING month-end 2y yield"])

    # FX -------------------------------------------------------------------------------
    r_us = rate3m("US") / 1200
    for k, (cur, fred, usd_per, yh, cc) in FXM.items():
        v = fx_usd_value(cur)
        R[k] = v / v.shift(1) - 1 + (rate3m(cc) / 1200 - r_us)
        note(k, ["Yahoo / stooq / FRED H.10 month-end", "+ rate differential"], ["avg FX"] if ALLOW_AVG else [])

    # commodities ----------------------------------------------------------------------
    wb = _pinksheet()
    for k, (etf, fut, stq, wbcol) in COMMOD.items():
        pieces, parts, flags = [], [], []
        if etf:
            pieces.append(ret(Y(etf)) - rf_us)
            parts.append(etf + " ETF")
        pieces.append(ret(Y(fut)))
        parts.append(fut + " front future")
        pieces.append(ret(S(stq)))
        parts.append("stooq " + stq)
        flags.append("unadjusted front future (roll gaps)")
        if ALLOW_AVG and wbcol is not None and wb is not None:
            col = [c for c in wb.columns if str(c).lower().startswith(wbcol.lower())]
            if col:
                pieces.append(ret(wb[col[0]]))
                parts.append("World Bank spot " + col[0])
                flags.append("spot monthly average before futures")
        R[k] = first(*pieces)
        note(k, parts, flags)

    # spreads ---------------------------------------------------------------------------
    y2, y10 = F("DGS2"), F("DGS10")
    r2, r10 = par_ret(y2, 2), par_ret(y10, 10)
    R["sp_us_2s10s"] = 5 * (r2 / 1.9 - r10 / 8.0)
    note("sp_us_2s10s", ["DGS2/DGS10 par bonds, duration-neutral, scaled to 5y"], [])
    be = F("T10YIE")
    be = first(be, F("DGS10") - F("DFII10"))
    R["sp_us_breakeven10"] = 8 * (be - be.shift(1)) / 100
    note("sp_us_breakeven10", ["8 x change in 10y breakeven (T10YIE)"], ["no TIPS before 2003"])
    d2, d10 = S("2dey.b"), S("10dey.b")
    R["sp_de_2s10s"] = 5 * (par_ret(d2, 2) / 1.9 - par_ret(d10, 10) / 8.0)
    note("sp_de_2s10s", ["stooq 2dey.b / 10dey.b month-end"], [] if d2.notna().sum() > 120 else
         ["MISSING: German 2-year yield (stooq 2dey.b; alternative Bundesbank SDMX)"])

    R = pd.DataFrame(R).reindex(GRID)
    R = R.where(R.abs() < 0.6)                           # drop impossible monthly moves (data errors)
    return R, SRC, FLAG, rf_us


def _pinksheet():
    p = os.path.join(RD, "wb_pinksheet_monthly.xlsx")
    if not os.path.exists(p):
        return None
    try:
        x = pd.read_excel(p, sheet_name="Monthly Prices", header=4)
        x = x.rename(columns={x.columns[0]: "m"})
        x = x[x["m"].astype(str).str.match(r"^\d{4}M\d{2}$")]
        x.index = pd.PeriodIndex([s.replace("M", "-") for s in x["m"]], freq="M")
        x = x.drop(columns="m").apply(pd.to_numeric, errors="coerce")
        return x.reindex(GRID)
    except Exception:  # noqa: BLE001
        return None


def coverage(R, SRC, FLAG):
    rows = []
    for k in R.columns:
        s = R[k].dropna()
        rows.append({"market": k, "first": str(s.index[0]) if len(s) else "-", "last": str(s.index[-1]) if len(s) else "-",
                     "months": len(s), "vol%": round(s.std() * np.sqrt(12) * 100, 1) if len(s) > 12 else np.nan,
                     "sources": " > ".join(SRC.get(k, [])), "flags": "; ".join(FLAG.get(k, []))})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    import pickle
    R, SRC, FLAG, rf = build()
    os.makedirs(OUT, exist_ok=True)
    pickle.dump({"grid": GRID, "R": R, "SRC": SRC, "FLAG": FLAG, "rf": rf}, open(os.path.join(OUT, "panel.pkl"), "wb"))
    cv = coverage(R, SRC, FLAG)
    pd.set_option("display.width", 250, "display.max_colwidth", 90, "display.max_rows", 100)
    print(cv[["market", "first", "last", "months", "vol%", "flags"]].to_string(index=False))
