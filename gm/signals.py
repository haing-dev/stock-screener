"""Global Macro Book, phase 1: signal families on the free-data panel, each tested alone.

Families (plan section 3):
  trend  price trend: average sign of 1/3/12-month excess return (reference; checked vs AQR TSMOM in plumbing.py)
  econ   economic trend: five themes (growth, inflation, trade, monetary policy, risk appetite), 12-month changes
         scaled by their own 10-year volatility, signed per asset class (AQR "Economic Trend", Exhibit 1); directional
  carry  bonds: yield minus local 3m rate; FX: local minus US 3m rate; commodities: energy curve slope (EIA F1/F2);
         half directional, half cross-sectional; equity carry not built yet (needs index dividend yields)
  value  equities: 5-year reversal (t-60..t-12); bonds: real yield (10y minus trailing 3-year CPI inflation);
         FX: 5-year real depreciation (PPP gap); commodities: 5-year reversal; cross-sectional within asset class

Positions: directional score in [-1, 1] (or rank-demeaned for cross-sectional), times 40% / trailing 36-month vol,
equal weight within an asset class, asset classes at equal risk (full-sample scaling: a test convenience, not a
trading rule). Macro data are lagged by their publication delay (CLI 2 months, CPI 1, BIS FX 1, credit spread 1).
CAVEAT: OECD CLI, CPI and GDP are latest-vintage (revised) data, so econ results here are optimistic; ALFRED vintages
are needed before any result counts. Design period 1990-2010; extra check 1975-89. The 2011-2026 holdout is NOT
reported here (it is run once, after rules are frozen).
"""
import os
import pickle

import numpy as np
import pandas as pd

from . import panel as P

GRID = P.GRID
CLASSES = {"EQ": ("eq_",), "FI": ("bd_", "st_"), "FX": ("fx_",), "CM": ("cm_",)}
ISO3 = {"US": "USA", "DE": "DEU", "GB": "GBR", "FR": "FRA", "JP": "JPN", "CA": "CAN", "AU": "AUS", "CN": "CHN",
        "KR": "KOR", "IN": "IND", "BR": "BRA", "MX": "MEX", "ZA": "ZAF", "CH": "CHE", "SE": "SWE", "NO": "NOR",
        "NZ": "NZL", "IT": "ITA", "ES": "ESP", "NL": "NLD"}
EQ_CC = {"eq_us_spx": "US", "eq_us_ndx": "US", "eq_us_r2k": "US", "eq_eu_stoxx50": "DE", "eq_de_dax": "DE",
         "eq_gb_ftse": "GB", "eq_fr_cac": "FR", "eq_jp_nikkei": "JP", "eq_ca_tsx": "CA", "eq_au_asx": "AU",
         "eq_hk_hsi": "CN", "eq_cn": "CN", "eq_kr_kospi": "KR", "eq_tw": "KR", "eq_in": "IN", "eq_br_ibov": "BR",
         "eq_mx_ipc": "MX", "eq_za": "ZA"}
BD = {"bd_us_2y": ("US", 2), "bd_us_5y": ("US", 5), "bd_us_10y": ("US", 10), "bd_us_30y": ("US", 30),
      "bd_de_10y": ("DE", 10), "bd_gb_10y": ("GB", 10), "bd_jp_10y": ("JP", 10), "bd_ca_10y": ("CA", 10),
      "bd_au_10y": ("AU", 10), "st_us_2y": ("US", 2), "st_de_2y": ("DE", 2), "st_gb_5y": ("GB", 5),
      "st_ca_2y": ("CA", 2), "st_au_2y": ("AU", 2), "st_jp_2y": ("JP", 2)}
FX_CC = {k: (v[0], v[4]) for k, v in P.FXM.items()}
G_EQ_RATE = {k: v[3] for k, v in P.EQUITY.items()}         # equity id -> 3m-rate country       # fx id -> (currency, rate country)
FX_MACRO = {"EZ": "DE"}                                    # euro: German macro data
BIS = {"EZ": "XM"}
GLOBAL = ["US", "DE", "JP", "CN"]                          # commodity demand block (equal weight)


# ------------------------------------------------------------------ data
def lag(s, k):
    return s.shift(k)


def yield_of(cc, n):
    if cc == "US":
        return P.F({2: "DGS2", 5: "DGS5", 10: "DGS10", 30: "DGS30"}[n])
    return P.cb_yield(cc, n)


def rate(cc):
    return P.rate3m("EZ" if cc == "DE" else cc)


_SDMX = {}


def oecd_sdmx(fname, iso3):
    """Series for one country from an OECD SDMX csv download (columns REF_AREA, TIME_PERIOD, OBS_VALUE)."""
    if fname not in _SDMX:
        p = os.path.join(P.RD, fname)
        try:
            x = pd.read_csv(p)
            x = x[[c for c in x.columns if c in ("REF_AREA", "TIME_PERIOD", "OBS_VALUE")]]
            x["m"] = pd.PeriodIndex(x["TIME_PERIOD"].astype(str).str[:7], freq="M")
            _SDMX[fname] = x.pivot_table(index="m", columns="REF_AREA", values="OBS_VALUE", aggfunc="last")
        except Exception:  # noqa: BLE001
            _SDMX[fname] = pd.DataFrame()
    t = _SDMX[fname]
    return t[iso3].reindex(GRID) if iso3 in t else pd.Series(np.nan, index=GRID)


def cpi_yoy(cc):
    c = FX_MACRO.get(cc, cc)
    return P.first(oecd_sdmx("oecd_cpi_yoy.csv", ISO3.get(c, c)), P.F("CPALTT01%sM659N" % c))


def cli(cc):
    c = ISO3.get(FX_MACRO.get(cc, cc), cc)
    return P.first(oecd_sdmx("oecd_cli.csv", c), P.F("%sLOLITONOSTSAM" % c))


def neer(cc):
    return P.F("NB%sBIS" % BIS.get(cc, cc))


def zchg(x, k=12, win=120):
    """12-month change scaled by its trailing 10-year volatility (no mean removal: the sign is the trend), cap 3."""
    c = x - x.shift(k)
    sd = c.rolling(win, min_periods=36).std()
    return (c / sd).clip(-3, 3)


def themes(cc, R):
    """Theme scores for one country (positive = rising growth / inflation / currency weakening / tightening /
    falling risk aversion), each lagged by its publication delay."""
    g = lag(zchg(cli(cc)), 2)
    i = lag(zchg(cpi_yoy(cc)), 1)
    t = lag(zchg(-np.log(neer(cc))), 1)
    y2 = yield_of(cc, 2) if cc in ("US", "DE", "CA", "AU", "JP") else pd.Series(np.nan, index=GRID)
    m = zchg(P.first(y2, rate(cc)))
    eq = [k for k, c in EQ_CC.items() if c == cc and k in R]
    eqr = R[eq[0]].rolling(12, min_periods=12).sum() if eq else pd.Series(np.nan, index=GRID)
    eqz = (eqr / (R[eq[0]].rolling(120, min_periods=36).std() * np.sqrt(12))).clip(-3, 3) if eq else eqr
    cr = lag(zchg(-P.F("BAA10YM")), 1)
    r = pd.concat([eqz, cr], axis=1).mean(axis=1)
    return {"growth": g, "inflation": i, "trade": t, "monetary": m, "risk": r}


SIGNS = {  # AQR Economic Trend, Exhibit 1
    "EQ": {"growth": 1, "inflation": -1, "trade": 1, "monetary": -1, "risk": 1},
    "FI": {"growth": -1, "inflation": -1, "trade": -1, "monetary": -1, "risk": -1},
    "FX": {"growth": 1, "inflation": 1, "trade": -1, "monetary": 1, "risk": 1},
    "CM": {"growth": 1, "inflation": 1, "trade": -1, "monetary": -1, "risk": 1},
}


ECON_THEMES = ("inflation", "trade", "monetary", "risk")   # v1.1: growth (OECD CLI) left out until first-release
                                                            # vintages exist (CLI is heavily revised; v1 used it)


def econ_scores(R):
    """Directional score per market in [-1, 1]: average over themes of sign x tanh(theme z / 2)."""
    cache, out = {}, {}

    def th(cc):
        if cc not in cache:
            cache[cc] = themes(cc, R)
        return cache[cc]

    def combine(ths, sg):
        parts = [np.tanh(ths[k] / 2) * s for k, s in sg.items() if k in ECON_THEMES]
        return pd.concat(parts, axis=1).mean(axis=1, skipna=True).where(pd.concat(parts, axis=1).notna().sum(axis=1) >= 2)

    for k in R.columns:
        if k.startswith("eq_") and k in EQ_CC:
            out[k] = combine(th(EQ_CC[k]), SIGNS["EQ"])
        elif k in BD:
            out[k] = combine(th(BD[k][0]), SIGNS["FI"])
        elif k in FX_CC:
            cur, cc = FX_CC[k]
            loc, us = th(FX_MACRO.get(cc, cc)), th("US")
            rel = {n: loc[n] - us[n] for n in loc}            # local minus US: drives the currency vs the dollar
            out[k] = combine(rel, SIGNS["FX"])
        elif k.startswith("cm_"):
            glob = {n: pd.concat([th(c)[n] for c in GLOBAL], axis=1).mean(axis=1) for n in th("US")}
            out[k] = combine(glob, SIGNS["CM"])
    return pd.DataFrame(out).reindex(GRID)


FRENCH_DY = {"eq_de_dax": "Germany", "eq_gb_ftse": "UK", "eq_fr_cac": "France", "eq_jp_nikkei": "Japan",
             "eq_ca_tsx": "Canada", "eq_au_asx": "Austrlia", "eq_hk_hsi": "HongKong"}


def _french_mkt(fname, name):
    import re
    import zipfile
    p = os.path.join(P.RD, fname)
    if not os.path.exists(p):
        return pd.Series(np.nan, index=GRID)
    z = zipfile.ZipFile(p)
    fn = [n for n in z.namelist() if n.lower() == name.lower() + ".dat"]
    rows, st = [], False
    for ln in z.read(fn[0]).decode("latin-1").splitlines() if fn else []:
        t = ln.split()
        if t and re.fullmatch(r"\d{6}", t[0]):
            st = True
            rows.append((pd.Period(t[0][:4] + "-" + t[0][4:], "M"), float(t[1])))
        elif st and t:
            break
    s = pd.Series(dict(rows), dtype=float)
    return (s.where(s > -99) / 100).reindex(GRID)


def equity_dy():
    """Trailing 12-month dividend yield per equity market: Ken French country market portfolio with minus without
    dividends (1975+, annual update; carried forward up to 12 months); US from SPY total return minus S&P 500 price
    (1993+). Point in time: known at month end."""
    out = {}
    for k, n in FRENCH_DY.items():
        d = _french_mkt("french_intl_countries_ff.zip", n) - _french_mkt("french_intl_countries_ff_xdiv.zip", n)
        out[k] = d.rolling(12, min_periods=12).sum().ffill(limit=12)
    us = (P.ret(P.Y("SPY")) - P.ret(P.Y("^GSPC"))).rolling(12, min_periods=12).sum()
    out["eq_us_spx"] = us.clip(0, 0.1)
    return pd.DataFrame(out).reindex(GRID)


def carry_values(R):
    out = {}
    for k, (cc, n) in BD.items():
        out[k] = (yield_of(cc, n) - rate(cc).shift(1)) / 100   # month-end yield minus last published 3m rate
    r_us = rate("US")
    for k, (cur, cc) in FX_CC.items():
        out[k] = ((P.rate3m(cc) - r_us) / 100).shift(1)      # OECD monthly rates are published after month end
    for k, root in P.EIA_ROOT.items():
        out[k] = P.eia_rolled(root)[1]
    dy = equity_dy()
    for k in dy.columns:
        out[k] = dy[k] - rate(G_EQ_RATE.get(k, "US")).shift(1) / 100     # dividend yield minus local 3m rate
    return pd.DataFrame(out).reindex(GRID)


def value_values(R, eq_measure="dy"):
    """eq_measure 'dy': equities by dividend yield (v1.1); 'rev': 5-year reversal (v1, failed)."""
    out = {}
    for k in R.columns:
        if k.startswith("cm_") and k != "cm_aqr_ew" or (k.startswith("eq_") and eq_measure == "rev"):
            lr = np.log1p(R[k])
            out[k] = -lr.shift(12).rolling(48, min_periods=48).sum()       # return t-60..t-12, reversed
    if eq_measure == "dy":
        dy = equity_dy()
        for k in dy.columns:
            out[k] = dy[k]
    for k, (cc, n) in BD.items():
        if n >= 10:
            infl = cpi_yoy(cc).ffill(limit=18).rolling(36, min_periods=24).mean().shift(1)
            out[k] = (yield_of(cc, n) - infl) / 100
    us_p = cpi_yoy("US").ffill(limit=18).shift(1)
    for k, (cur, cc) in FX_CC.items():
        fxv = P.fx_usd_value(cur)
        lp = cpi_yoy(FX_MACRO.get(cc, cc)).ffill(limit=18).shift(1)
        infl_gap = ((lp - us_p) / 100 / 12).rolling(60, min_periods=60).sum()   # ~5y cumulative inflation gap
        real_chg = np.log(fxv / fxv.shift(60)) + infl_gap                     # real appreciation over 5 years
        out[k] = -real_chg
    return pd.DataFrame(out).reindex(GRID)


# ------------------------------------------------------------------ books
def cs_rank(X, cols):
    """Cross-sectional rank, demeaned, scaled to sum |w| = 1 within the asset class."""
    x = X[cols]
    rk = x.rank(axis=1)
    w = rk.sub(rk.mean(axis=1), axis=0)
    return w.div(w.abs().sum(axis=1), axis=0).where(x.notna().sum(axis=1) >= 3) * x.notna().sum(axis=1).values[:, None]


def book(R, S, kind, target=0.40):
    """kind: 'dir' (score in [-1,1]) or 'cs' (cross-sectional within class) or 'half' (average of the two)."""
    vol = R.rolling(36, min_periods=12).std() * np.sqrt(12)
    res = {}
    for c, pre in CLASSES.items():
        cols = [k for k in S.columns if k.startswith(pre) and k in R]
        if not cols:
            continue
        if kind == "dir":
            w = S[cols].clip(-1, 1)
        elif kind == "cs":
            w = cs_rank(S, cols)
        else:
            d = np.sign(S[cols]) * 0.5
            w = cs_rank(S, cols).fillna(0) * 0.5 + d
            w = w.where(S[cols].notna())
        pos = w * target / vol[cols]
        contrib = pos.shift(1) * R[cols]
        n = contrib.notna().sum(axis=1)
        res[c] = contrib.sum(axis=1, min_count=1) / n.where(n > 0)
    df = pd.DataFrame(res)
    sd = df.std()
    df["ALL"] = (df / sd * sd.mean()).mean(axis=1, skipna=True)
    return df


def century():
    x = pd.read_excel(os.path.join(P.RD, "aqr_century_premia.xlsx"), sheet_name=0, header=18)
    x = x.rename(columns={x.columns[0]: "date"}).dropna(subset=["date"])
    x = x[pd.to_datetime(x["date"], errors="coerce").notna()]
    x.index = pd.to_datetime(x["date"]).dt.to_period("M")
    return x.drop(columns="date").apply(pd.to_numeric, errors="coerce")


REF = {"carry": {"FI": "Fixed income Carry", "FX": "Currencies Carry", "CM": "Commodities Carry"},
       "value": {"EQ": "Equity indices Value", "FI": "Fixed income Value", "FX": "Currencies Value",
                 "CM": "Commodities Value"}}
PERIODS = (("1975-01", "1989-12"), ("1990-01", "2010-12"))


def report(name, df, ref=None, aq=None):
    sr = lambda s: s.mean() / s.std() * np.sqrt(12)
    for a, b in PERIODS:
        line = []
        for c in ["ALL"] + [k for k in ("EQ", "FI", "FX", "CM") if k in df]:
            s = df[c].loc[a:b].dropna()
            if len(s) < 36:
                line.append("%s n/a" % c)
                continue
            t = s.mean() / s.std() * np.sqrt(len(s))
            txt = "%s SR %.2f (t %.1f)" % (c, sr(s), t)
            if ref and aq is not None and c in ref and ref[c] in aq:
                j = pd.concat([s, aq[ref[c]]], axis=1).dropna()
                if len(j) > 36:
                    txt += " corrAQR %.2f" % j.corr().iloc[0, 1]
            line.append(txt)
        print("  %-6s %s..%s  %s" % (name, a[:4], b[:4], " | ".join(line)))


def main():
    D = pickle.load(open(os.path.join(P.OUT, "panel.pkl"), "rb"))
    R = D["R"]
    aq = century()
    print("Signal families alone, gross, monthly; design 1990-2010 and extra check 1975-89 (holdout not shown)")
    from .plumbing import trend_book
    report("trend", trend_book(R))
    E = econ_scores(R)
    report("econ", book(R, E, "dir"))
    C = carry_values(R)
    report("carry", book(R, C, "half"), REF["carry"], aq)
    report("carryD", book(R, np.sign(C), "dir"))
    report("carryX", book(R, C, "cs"), REF["carry"], aq)
    V = value_values(R)
    report("value", book(R, V, "cs"), REF["value"], aq)
    cov = {f: X.loc["1990":"2010"].notna().any().sum() for f, X in (("econ", E), ("carry", C), ("value", V))}
    print("markets with a signal 1990-2010:", cov)
    pickle.dump({"E": E, "C": C, "V": V}, open(os.path.join(P.OUT, "signals.pkl"), "wb"))


if __name__ == "__main__":
    main()
