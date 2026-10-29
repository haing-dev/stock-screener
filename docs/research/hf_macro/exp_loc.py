"""Exp 2 (pre-registered 2026-10-29): WHERE to hold the equity part. Fully invested (100% equity) first, to isolate
location skill; the best are then combined with the 4.1 exposure rule. Windows 1997-2011 | 2012-2026 | 1997-2026.
Universe: US (spx), developed ex-US (intl_eq), Korea, Brazil, Japan, China/HK, India, Mexico, Taiwan, Germany, UK,
Canada, Australia (ETF; local index in USD + 2%/yr dividends before the ETF).
L1 US vs ex-US: hold the one with the higher 12-month return (skip last month) | L1b same, 6-month
L2 dollar falling (DXY below its 10-month average) -> 50% ex-US/EM, else 100% US
L3 country momentum: top 3 of the universe by 12-1 month return, only if above own 10-month average, else US
L3b top 5 | L3c top 3 by 6-month return
L4 commodity boom (commodity index 12m > +15% and above its 10m average) -> 50% exporters (Brazil, Canada,
   Australia, Mexico), else US
L5 L3 but no oil importers (Korea, India, Japan, Taiwan) while oil 3m > +30%
L6 China cycle up (Korea exports y/y rising over 3 months and > 0, copper above its 10m average) -> 50% Korea+Taiwan
   +China, else US
L7 EM rebound: average EM country >= 40% below its 3-year high in USD and the Fed not tightening -> 30% EM basket
L8 L3 + L2 dollar filter for EM (EM countries eligible only while the dollar is below its 10m average)
"""
from base import *  # noqa

WS = WIN_SHORT
C = ["spx", "intl_eq", "eq_korea", "eq_brazil", "eq_japan", "eq_hongkong", "eq_india", "eq_mexico", "eq_taiwan",
     "eq_germany", "eq_uk", "eq_canada", "eq_australia"]
EMC = ["eq_korea", "eq_brazil", "eq_hongkong", "eq_india", "eq_mexico", "eq_taiwan"]
IMPORTERS = ["eq_korea", "eq_india", "eq_japan", "eq_taiwan"]
EXPORTERS = ["eq_brazil", "eq_canada", "eq_australia", "eq_mexico"]
M12 = pd.DataFrame({c: mom(c, 12, 1) for c in C})
M6 = pd.DataFrame({c: mom(c, 6, 0) for c in C})
UP = pd.DataFrame({c: above_ma(c) for c in C}).fillna(False)
dxy = S["px_DX-Y.NYB"].combine_first(S.get("fred_TWEXB", pd.Series(np.nan, index=grid)))
usd_dn = (dxy < ma(dxy, 10)).fillna(False)
com_boom = ((mom("commod", 12) > 0.15) & above_ma("commod")).fillna(False)
oil = S["px_CL=F"]
oil_spike = ((oil / oil.shift(3) - 1) > 0.30).fillna(False)
kx = S["fred_XTEXVA01KRM667S"]
kx_yy = (kx / kx.shift(12) - 1).shift(1)
china_up = ((kx_yy > 0) & (kx_yy > kx_yy.shift(3)) & above_ma("copper")).fillna(False)
em_lvl = pd.DataFrame({c: lvl(R[c]).where(R[c].notna().cummax()) for c in EMC})
em_dd = (em_lvl / em_lvl.rolling(36, min_periods=12).max() - 1).mean(axis=1)


def W_top(M, k=3, excl=None, elig=None):
    W = pd.DataFrame(0.0, index=grid, columns=C)
    for t in range(T):
        m = M.iloc[t].dropna()
        ok = [c for c in m.index if UP[c].iloc[t] and R[c].shift(-1).notna().iloc[t] if t + 1 < T]
        if excl is not None:
            ok = [c for c in ok if not (c in excl[0] and excl[1].iloc[t])]
        if elig is not None:
            ok = [c for c in ok if c not in EMC or elig.iloc[t]]
        top = list(m[ok].sort_values(ascending=False).index[:k])
        if not top:
            W.iloc[t, 0] = 1.0
        else:
            for c in top:
                W.loc[grid[t], c] = 1 / len(top)
    return W


def W_mix(cond, basket, w=0.5):
    W = pd.DataFrame(0.0, index=grid, columns=C)
    W["spx"] = 1 - w * cond.astype(float)
    for c in basket:
        W[c] = w * cond.astype(float) / len(basket)
    return W


V = {}
W = pd.DataFrame(0.0, index=grid, columns=C); W["spx"] = 1.0; V["US only (S&P 500)"] = W
W = pd.DataFrame(0.0, index=grid, columns=C); W["spx"] = 0.6; W["intl_eq"] = 0.4; V["static 60 US / 40 ex-US"] = W
W = pd.DataFrame(0.0, index=grid, columns=C); W[C] = 1 / len(C); V["equal weight all 13"] = W
W = pd.DataFrame(0.0, index=grid, columns=C); W["spx"] = (M12["spx"] >= M12["intl_eq"]).astype(float); W["intl_eq"] = 1 - W["spx"]; V["L1 US vs ex-US 12-1m"] = W
W = pd.DataFrame(0.0, index=grid, columns=C); W["spx"] = (M6["spx"] >= M6["intl_eq"]).astype(float); W["intl_eq"] = 1 - W["spx"]; V["L1b US vs ex-US 6m"] = W
V["L2 dollar falling -> 50% ex-US+EM"] = W_mix(usd_dn, ["intl_eq"] + EMC)
V["L3 country momentum top 3"] = W_top(M12, 3)
V["L3b top 5"] = W_top(M12, 5)
V["L3c top 3, 6m"] = W_top(M6, 3)
V["L4 commodity boom -> 50% exporters"] = W_mix(com_boom, EXPORTERS)
V["L5 L3 minus importers on oil spike"] = W_top(M12, 3, excl=(IMPORTERS, oil_spike))
V["L6 China cycle up -> 50% Korea/Taiwan/China"] = W_mix(china_up, ["eq_korea", "eq_taiwan", "eq_hongkong"])
V["L7 EM rebound -> 30% EM"] = W_mix((em_dd <= -0.40) & ~fed, EMC, 0.3)
V["L8 L3 with EM only while dollar falls"] = W_top(M12, 3, elig=usd_dn)
print("== equity location, fully invested. CAGR / worst / Sharpe: 1997-2011 | 2012-2026 | 1997-2026")
LOC = {}
for k, w in V.items():
    LOC[k] = w
    print(line(k, run(w), WS))
print("\n== the same location rules inside the 4.1 exposure (equity part scaled by e41, rest per live defensive rule)")
for k, w in V.items():
    W2 = w.mul(e41, axis=0)
    W2["t30y"] = (1 - e41) * (gtt & cneg).astype(float)
    print(line(k, run(W2), WS))
import pickle
pickle.dump(LOC, open("loc.pkl", "wb"))
