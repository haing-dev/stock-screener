"""Exp 3 (pre-registered 2026-10-29): transcript signals for HOW MUCH stock to hold. Each candidate enters the live 4.1
rule either as an extra GATE (warnings are acted on while the Fed is tightening OR the candidate is on) or as an
EXTRA CUT (candidate on -> stocks at 50%, or 0%). Non-stock share per live 4.1. Windows 1975-2000 | 2001-2026 | 1975-2026.
Candidates (thresholds from the transcripts; 'p' = proposed):
 squeeze   dollar/oil/rates squeeze score >= 80 (Druckenmiller/Hyman)
 lead3     homebuilders, transports AND retail all >= 20% below their 12-month highs (Druckenmiller; p 20%)
 nofedput  CPI y/y > 4% and Fed funds above its level 12 months ago (Citrone/Druckenmiller)
 realneg5  CPI y/y > 5% and Fed funds < CPI (Druckenmiller)
 meltup    S&P 12m return > 25% and 10y yield up > 1.5 pts in 12 months (Trennert)
 hike300   Fed funds up >= 3 pts within the past 24 months (Druckenmiller/Bessent credit-event window)
 oilshock  oil > 50% above its 12-month average for 3 months in a row (Bessent)
 resteep   10y-2y spread >= 0.5 pt above its 18-month low after an inversion within the past 18 months (Tropin)
 erp1      earnings yield (S&P, Shiller E/P) minus 3-month T-bill < 1 pt (Tropin 'TINA')
 narrow    narrow leadership score >= 80 (Druckenmiller yellow light; AND with any warning >= 15%)
 epu90     economic policy uncertainty in its top 10% (Gerstner) (1985+)
 credit    Baa spread up >= 1 pt in 6 months (credit stress)
 sell6     May-October (Hirsch best six months)  | midterm  May-Sep of a midterm-election year (Hirsch)
"""
from base import *  # noqa

lv = {c: lvl(R[c]) for c in R.columns if c.startswith("sec_")}
dd12 = {c: lv[c] / lv[c].rolling(12).max() - 1 for c in lv}
spx_l = lvl(R["spx"])
gs2 = F["GS2"]
tb = rf * 1200
C = {}
C["squeeze"] = squeeze
C["lead3"] = (dd12["sec_ITB"] <= -0.20) & (dd12["sec_IYT"] <= -0.20) & (dd12["sec_XRT"] <= -0.20)
C["nofedput"] = (cpi_yy > 4) & (ff > ff.shift(12))
C["realneg5"] = (cpi_yy > 5) & (ff < cpi_yy)
C["meltup"] = ((spx_l / spx_l.shift(12) - 1) > 0.25) & ((gs10 - gs10.shift(12)) > 1.5)
C["hike300"] = (ff - ff.rolling(24, min_periods=12).min()) >= 3
oil = F["WTISPLC"]
osh = oil > 1.5 * oil.rolling(12).mean()
C["oilshock"] = osh & osh.shift(1) & osh.shift(2)
cv = gs10 - gs2
inv = (cv < 0).rolling(18, min_periods=1).max().astype(bool)
C["resteep"] = inv & (cv >= cv.rolling(18, min_periods=6).min() + 0.5)
ey = (S["sh_eps"] / S["sh_price"] * 100).shift(3)                 # earnings published with a lag (~3 months)
C["erp1"] = (ey - tb) < 1
C["narrow"] = (sc["leadership"] >= 80) & (share >= 0.15)
epu = S["fred_USEPUINDXM"]
C["epu90"] = pctl(epu, 60) >= 90
C["credit"] = (F["BAA"] - gs10) - (F["BAA"] - gs10).shift(6) >= 1.0
mo = np.array([p.month for p in grid])
yrs = np.array([p.year for p in grid])
C["sell6"] = pd.Series((mo >= 4) & (mo <= 9), index=grid)          # decided end of Apr..Sep -> held May..Oct
C["midterm"] = pd.Series((yrs % 4 == 2) & (mo >= 4) & (mo <= 8), index=grid)
for k in C:
    C[k] = C[k].reindex(grid).fillna(False).astype(bool)

print("share of months on (1975-2026): " + ", ".join(f"{k} {C[k][grid >= Per('1975-01')].mean():.0%}" for k in C))
print("\n== CAGR / worst / Sharpe: 1975-2000 | 2001-2026 | 1975-2026")
print(line("S&P 500", R["spx"]))
print(line("live 4.1", run(W41)))
rows = {}
for k, c in C.items():
    for mode in ("gate", "cut50", "cut0"):
        if mode == "gate":
            e = exposure(gate=fed | c)
        else:
            e = np.minimum(e41, pd.Series(np.where(c, 0.5 if mode == "cut50" else 0.0, 1.0), index=grid))
        r = run(W_from(e, live_def))
        rows[(k, mode)] = r
        print(line(f"{k} as {mode}", r))
import pickle
pickle.dump({"C": C}, open("cands.pkl", "wb"))
