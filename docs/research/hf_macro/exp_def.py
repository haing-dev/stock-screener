"""Exp 1 (pre-registered 2026-10-29): what to hold outside stocks, and always-on diversifier sleeves.
Stock exposure = live 4.1 (e41). Windows: 1985-2000 | 2001-2026 | 1985-2026 (trend data start 1985).
Regimes known at t: hot = CPI y/y (NSA, lagged 1m) > 3%; corr_pos = 12m stock-bond corr >= 0; curve_ok = 10y >= Fed
funds; growth cut = S&P below 10m avg and unemployment rising; com_up = commodity index above its 10-month average."""
from base import *  # noqa

W85 = WIN_LONG
hot = (cpi_yy > 3).fillna(False)
hot4 = (cpi_yy > 4).fillna(False)
cpos = ~cneg
com_up = above_ma("commod").fillna(False)
gold_up = above_ma("gold").fillna(False)
g_l = gtt & cneg
V = {}
V["D0 live 4.1"] = live_def
V["D1 trend in every cut"] = {"trend_lo": 1.0}
V["D2 live, trend instead of bills"] = {"t30y": g_l, "trend_lo": ~g_l}
V["D3 live, trend instead of bills when hot or corr>=0"] = {"t30y": g_l, "trend_lo": ~g_l & (hot | cpos)}
V["D4 live, gold instead of bills when hot"] = {"t30y": g_l, "gold": ~g_l & hot}
V["D5 live, commodities when hot & commod trend up"] = {"t30y": g_l, "commod": ~g_l & hot & com_up}
V["D6 live, 2y instead of bills"] = {"t30y": g_l, "t2y": ~g_l}
V["D7 long T if growth cut & corr<0 & 10y>=FF"] = {"t30y": g_l & curve_ok}
V["D8 1/2 live + 1/2 trend"] = {"t30y": 0.5 * g_l, "trend_lo": pd.Series(0.5, index=grid)}
V["D9 live, then trend/gold/2y by regime"] = {"t30y": g_l, "trend_lo": ~g_l & cpos, "t2y": ~g_l & cneg}
V["D10 gold if gold trend up, else live"] = {"gold": ~g_l & gold_up, "t30y": g_l}
print("== non-stock share (stock exposure live 4.1); CAGR / worst / Sharpe: 1985-2000 | 2001-2026 | 1985-2026")
print(line("S&P 500", R["spx"], W85))
res = {}
for k, d in V.items():
    res[k] = run(W_from(e41, d))
    print(line(k, res[k], W85))

print("\n== always-on sleeves (on top of live 4.1, scaled so weights sum <= 1)")


def sleeve(W, asset, w):
    W2 = W.mul(1 - (w if isinstance(w, float) else w.astype(float)), axis=0)
    W2[asset] = W2.get(asset, 0.0) + w
    return W2


for nm, a, w in (("S1 20% trend always", "trend_lo", 0.2), ("S2 10% trend always", "trend_lo", 0.1),
                 ("S3 10% gold always", "gold", 0.1), ("S4 20% commodities when hot & commod up", "commod", 0.2 * (hot & com_up)),
                 ("S5 20% trend when hot", "trend_lo", 0.2 * hot), ("S6 30% trend always", "trend_lo", 0.3),
                 ("S7 20% gold when hot & gold up", "gold", 0.2 * (hot & gold_up))):
    print(line(nm, run(sleeve(W41, a, w)), W85))
print("\n== the same, 1975 start where data exist (no trend): 1975-2000 | 2001-2026 | 1975-2026")
for k in ("D0 live 4.1", "D4 live, gold instead of bills when hot", "D5 live, commodities when hot & commod trend up",
          "D6 live, 2y instead of bills", "D7 long T if growth cut & corr<0 & 10y>=FF", "D10 gold if gold trend up, else live"):
    print(line(k, res[k]))
print(line("S4 20% commodities when hot & commod up", run(sleeve(W41, "commod", 0.2 * (hot & com_up)))))
