"""The dollar (and safe-haven currencies) as a holding and as a signal. Written 2026-10-29 before results.
Stock exposure = live 4.0.0; base non-stock rule = live 4.1.0 (growth-trend cut & stock-bond corr < 0 -> long Treasuries,
else T-bills).
Instruments (retail ETF proxies, total return incl. interest):
  dollar = UUP from 2007-03; before: T-bill + carry vs the DXY basket - basket currency returns (DXY weights EUR/DEM 57.6,
           JPY 13.6, GBP 11.9, CAD 9.1, SEK 4.2, CHF 3.6), spot from DXY month-end from 1985 and from month-end
           estimates of monthly-average FX rates (geometric mean of this and next month's average) before.
  yen = FXY from 2007-02, before: yen deposit (FX month-end estimate + Japan 3-month rate; call rate 1985-2002,
        German 3-month rate as proxy before 1985).  franc = FXF from 2006-06, before: franc deposit (Swiss call rate).
  gold (check) = month-end GC=F from 2000-09, before: month-end estimate from monthly averages (not the raw average).
Holdings in cuts: H1 dollar instead of bills always | H2 dollar instead of bills in growth-trend cuts | H3 dollar
  instead of bills when corr >= 0 | H4 yen instead of bills in growth-trend cuts | H5 franc same | H6 half long
  Treasuries / half dollar in growth-trend cuts with corr < 0 | H7 gold instead of bills when inflation hot (re-check).
Signals: D1 extra cut: dollar at a 12-month high AND S&P below its 10-month average -> 0% | D2 warnings acted on while
  the Fed is tightening OR the dollar is up 10%+ in 12 months | D3 ... OR the dollar-oil-rates squeeze score >= 80 |
  D4 replace the Fed gate with the dollar gate (up 10%+).
"""
import math
import os
import pickle
import sys
import warnings

warnings.filterwarnings("ignore")
import numpy as np    # noqa: E402
import pandas as pd   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
exec(compile(open(os.path.join(HERE, "assets.py")).read().split("def run(wdef")[0], "assets_head", "exec"))
OUT.clear()


def raw(name):
    s = E._csv(name)
    if s is None:
        return pd.Series(np.nan, index=grid)
    return pd.Series(s.values, index=s.index.to_period("M")).groupby(level=0).last().reindex(grid).astype(float)


def end_est(avg):                       # month-end level estimate from monthly averages
    return np.sqrt(avg * avg.shift(-1))


def usd_per(name, invert):              # USD per unit of the foreign currency, month-end estimate
    a = raw(name)
    a = 1 / a if invert else a
    return end_est(a)


fx = {"EUR": usd_per("EXUSEU", False), "DEM": usd_per("EXGEUS", True), "JPY": usd_per("EXJPUS", True),
      "GBP": usd_per("EXUSUK", False), "CAD": usd_per("EXCAUS", True), "SEK": usd_per("EXSDUS", True),
      "CHF": usd_per("EXSZUS", True)}
rate = {"EUR": raw("IR3TIB01EZM156N").combine_first(raw("IR3TIB01DEM156N")), "DEM": raw("IR3TIB01DEM156N"),
        "JPY": raw("IR3TIB01JPM156N").combine_first(raw("IRSTCI01JPM156N")).combine_first(raw("IR3TIB01DEM156N")),
        "GBP": raw("IR3TIB01GBM156N"), "CAD": raw("IR3TIB01CAM156N"),
        "SEK": raw("IR3TIB01SEM156N").combine_first(raw("IR3TIB01DEM156N")),
        "CHF": raw("IR3TIB01CHM156N").combine_first(raw("IRSTCI01CHM156N"))}
for k in rate:
    rate[k] = rate[k].ffill(limit=3)


def deposit(c):                         # return of holding currency c deposits, in USD
    return fx[c] / fx[c].shift(1) * (1 + rate[c].shift(1) / 1200) - 1


dep = {c: deposit(c) for c in fx}
dep["EURX"] = dep["EUR"].combine_first(dep["DEM"])
wts = {"EURX": 0.576, "JPY": 0.136, "GBP": 0.119, "CAD": 0.091, "SEK": 0.042, "CHF": 0.036}
basket = sum(w * dep[c] for c, w in wts.items()) / sum(wts.values())
carry_basket = sum(w * rate[c if c != "EURX" else "EUR"].shift(1) / 1200 for c, w in wts.items()) / sum(wts.values())
dxy = raw("Y_DX_Y_NYB")
dxy_r = dxy.pct_change(fill_method=None)
# dollar ETF: T-bill + (US rate - basket rate) + DXY spot change  (spot from DXY month-end when it exists)
spot_syn = -(basket - carry_basket)                                          # minus basket spot moves (approx)
usd_syn = rf + (rf - carry_basket) + dxy_r.combine_first(spot_syn) - 0.011 / 12   # UUP fee + basis (fitted gap vs UUP)
uup = px("Y_UUP")
dollar = uup.combine_first(usd_syn)
yen = px("Y_FXY").combine_first(dep["JPY"])
franc = px("Y_FXF").combine_first(dep["CHF"])
g_end = end_est(raw("GOLD")).pct_change(fill_method=None)
gold_e = px("Y_GC_F").combine_first(g_end)


def st(r, a, b):
    m = (grid >= Per(a)) & (grid <= Per(b))
    x, f = r[m], rf[m]
    lv = np.r_[1, (1 + x.values).cumprod()]
    return (lv[-1] ** (12 / len(x)) - 1) * 100, (lv / np.maximum.accumulate(lv) - 1).min() * 100, (x - f).mean() / x.std() * math.sqrt(12)


def chk(nm, a, b):
    o = a.notna() & b.notna()
    log(f"check {nm} ({o.sum()} months): corr {a[o].corr(b[o]):.2f}, {a[o].mean() * 1200:.1f} vs {b[o].mean() * 1200:.1f}%/yr")


chk("synthetic dollar vs UUP", usd_syn, uup)
chk("synthetic DXY spot (from averages) vs DXY month-end", spot_syn, dxy_r)
chk("yen deposit vs FXY", dep["JPY"], px("Y_FXY"))
chk("franc deposit vs FXF", dep["CHF"], px("Y_FXF"))
chk("gold month-end estimate vs GC=F", g_end, px("Y_GC_F"))
log(f"dollar proxy starts {dollar.first_valid_index()}, yen {yen.first_valid_index()}, franc {franc.first_valid_index()}")

A2 = A.copy()
A2["dollar"], A2["yen"], A2["franc"], A2["gold"] = dollar, yen, franc, gold_e
for c in ("dollar", "yen", "franc"):
    A2[c] = A2[c].fillna(rf)                                              # before the proxy exists: bills


def run2(e_, wdef):
    eh, wd = e_.shift(1), wdef.shift(1)
    alt = (wd * A2.fillna(0)).sum(axis=1)
    return eh * mkt + (1 - eh) * alt


def W2(**k):
    d = pd.DataFrame(0.0, index=grid, columns=A2.columns)
    for c, v in k.items():
        d[c] = v.astype(float) if isinstance(v, pd.Series) else v
    return d


g_l = cneg & cause_g                       # live: long Treasuries
rest = ~g_l
base = W2(long=g_l, bills=rest)
H = {"H0 live 4.1 (long T / bills)": base,
     "H1 dollar instead of bills": W2(long=g_l, dollar=rest),
     "H2 dollar instead of bills, growth cuts": W2(long=g_l, dollar=rest & cause_g, bills=rest & ~cause_g),
     "H3 dollar instead of bills when corr>=0": W2(long=g_l, dollar=~cneg, bills=cneg & ~g_l),
     "H4 yen instead of bills, growth cuts": W2(long=g_l, yen=rest & cause_g, bills=rest & ~cause_g),
     "H5 franc instead of bills, growth cuts": W2(long=g_l, franc=rest & cause_g, bills=rest & ~cause_g),
     "H6 half long T / half dollar (growth, corr<0)": W2(long=0.5 * g_l, dollar=0.5 * g_l, bills=rest),
     "H7 gold (month-end est.) instead of bills when hot": W2(long=g_l, gold=rest & hot, bills=rest & ~hot)}


def line2(nm, r):
    c = [st(r, *w) for w in (("1975-02", "2000-12"), ("2001-01", "2026-10"), ("1975-02", "2026-10"))]
    return f"{nm:<48} " + " | ".join(f"{a:5.1f}% {b:4.0f}% {s:4.2f}" for a, b, s in c)


log("\n== holdings in cuts (stock exposure 4.0.0). CAGR / worst / Sharpe: 1975-2000 | 2001-2026 | 1975-2026")
log(line2("S&P 500", mkt))
for nm, w in H.items():
    log(line2(nm, run2(e, w)))

# ---------------- dollar as a signal
d12 = ind["dollar"]
dbreak = ind["dollar_break"]
sq = sc["squeeze"]
dup = (d12 >= 10).fillna(False)
dhigh = (dbreak >= 0).fillna(False)


def exposure(gate, extra=None):
    ee = 1 - ((share - lo) / (hi - lo)).clip(0, 1) * gate.astype(float)
    ee = np.minimum(ee, pd.Series(np.where(gtt, 0.0, 1.0), index=grid))
    if extra is not None:
        ee = np.minimum(ee, pd.Series(np.where(extra, 0.0, 1.0), index=grid))
    return pd.Series(ee, index=grid).fillna(1.0)


log("\n== dollar as a signal (non-stock share per live 4.1)")
log(f"  (dollar up 10%+ y/y in {dup[grid >= Per('1975-02')].mean():.0%} of months; at a 12-month high in {dhigh[grid >= Per('1975-02')].mean():.0%})")
for nm, ee in (("live 4.0 exposure", e),
               ("D1 + cut when dollar at 12m high & S&P below trend", exposure(fed, dhigh & (ind["spx_trend"] < 0))),
               ("D2 gate: Fed tightening OR dollar up 10%+", exposure(fed | dup)),
               ("D3 gate: Fed tightening OR squeeze >= 80", exposure(fed | (sq >= 80).fillna(False))),
               ("D4 gate: dollar up 10%+ instead of Fed", exposure(dup))):
    log(line2(nm, run2(ee, base)))

# where the dollar helped: average monthly return of each holding in growth-trend cut months, by decade
m = (e.shift(1) < 1 - 1e-9) & cause_g.shift(1).fillna(False)
log("\n== growth-trend cut months: average return per month, % (bills / long T / dollar / yen / franc / gold)")
for a, b in (("1975-02", "1989-12"), ("1990-01", "2004-12"), ("2005-01", "2026-10")):
    mm = m & (grid >= Per(a)) & (grid <= Per(b))
    log(f"  {a[:4]}-{b[:4]} ({int(mm.sum())} months): " + " / ".join(f"{A2[c][mm].mean() * 100:+.2f}" for c in ("bills", "long", "dollar", "yen", "franc", "gold")))
open(os.path.join(HERE, "log_dollar.txt"), "w").write("\n".join(OUT))
