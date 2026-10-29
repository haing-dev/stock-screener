"""Audit 5: AQR commodity alignment check; candidate 5.0 vs live with all mechanical fixes; sensitivity."""
import pickle
import numpy as np
import pandas as pd
from audit_lib import *  # noqa

fx = pickle.load(open(os.path.join(HERE, "audit_fix.pkl"), "rb"))
t30_fix, gu_a = fx["t30_fix"], fx["gu_a"]
RD = "/home/claude/stock-screener/cache/macro/raw/research"


def aqr(fname, hdr_key):          # same parser as rpanel.aqr
    d = pd.read_excel(os.path.join(RD, fname), sheet_name=0, header=None)
    hi = d.index[d.iloc[:, 0].astype(str).str.strip().eq("Date") | d.iloc[:, 1].astype(str).str.contains(hdr_key, na=False)][0]
    cols = d.iloc[hi].astype(str).tolist()
    body = d.iloc[hi + 1:].copy()
    body.columns = cols
    dt = pd.to_datetime(body.iloc[:, 0], errors="coerce")
    body = body[dt.notna()]
    print("   AQR first dates:", list(pd.to_datetime(body.iloc[:3, 0]).dt.date), "header:", cols[:3])
    body.index = pd.to_datetime(body.iloc[:, 0]).dt.to_period("M")
    return body.iloc[:, 1:].apply(pd.to_numeric, errors="coerce").groupby(level=0).last().reindex(grid)


com = aqr("aqr_commodities_long_run.xlsx", "Excess return")
c0 = com.iloc[:, 0]
dbc = R0["commod"].where(grid >= Per("2006-03"))
ov = pd.concat([c0 + rf, dbc], axis=1, keys=["aqr", "dbc"]).dropna()
print(f"== AQR EW commodity (+rf) vs DBC overlap {ov.index[0]}..{ov.index[-1]}: corr same month {ov['aqr'].corr(ov['dbc']):.2f}, "
      f"AQR(t) vs DBC(t+1) {ov['aqr'].corr(ov['dbc'].shift(-1)):.2f}, AQR(t) vs DBC(t-1) {ov['aqr'].corr(ov['dbc'].shift(1)):.2f}; "
      f"vol {ov['aqr'].std()*np.sqrt(12)*100:.1f}% vs {ov['dbc'].std()*np.sqrt(12)*100:.1f}%")
gld = R0["gold"].where(grid >= Per("2005-01"))

# ---------------------------------------------------------------- all mechanical fixes together
Rf = R0.copy()
Rf["t30y"] = t30_fix
print("\n== CAGR / worst / Sharpe: 1975-2000 | 2001-2026 | 1975-2026")
print(line("S&P 500", R0["spx"]))
print(line("live 4.1 as published", live()))
print(line("candidate 5.0 as published", cand()[0]))
lf = live(Rf, cost=0.003)
cf = cand(Rf, gold_up=gu_a, cost=0.003)[0]
print(line("live 4.1, exact T-bond returns, 0.3% cost", lf))
print(line("candidate 5.0, same + gold signal known at t", cf))
print(line("candidate 5.0 fixed, no melt-up (3 episodes, all pre-2000)", cand(Rf, gold_up=gu_a, cost=0.003, use_mu=False)[0]))
print(line("candidate 5.0 fixed, no squeeze (active 1997+ only)", cand(Rf, gold_up=gu_a, cost=0.003, use_sq=False)[0]))
print(line("candidate 5.0 fixed, sleeve + tilt + D7 only", cand(Rf, gold_up=gu_a, cost=0.003, use_sq=False, use_mu=False)[0]))
wf = pickle.load(open(os.path.join(HERE, "audit_wf.pkl"), "rb"))["wf"]
print(line("walk-forward pick among the 300 variants (1985+)", wf, (("1985-01", "2000-12"), ("2001-01", "2026-10"), ("1985-01", "2026-10"))))
print(line("live 4.1 same windows", live(), (("1985-01", "2000-12"), ("2001-01", "2026-10"), ("1985-01", "2026-10"))))

# melt-up neighbourhood: is the gain one event?
print("\n== melt-up cut alone on top of live: months and gain")
spx_l = lvl(R0["spx"])
for mu in ((0.25, 1.5), (0.20, 1.5), (0.30, 1.5), (0.25, 1.0), (0.25, 2.0), (0.20, 1.0)):
    c = (((spx_l / spx_l.shift(12) - 1) > mu[0]) & ((X.gs10 - X.gs10.shift(12)) > mu[1])).fillna(False)
    r = cand(use_sq=False, xs=0, l="L0", d="D0", mu=mu)[0]
    r_ex87 = r.copy(); mm = (grid >= Per("1987-09")) & (grid <= Per("1987-11")); r_ex87[mm] = live()[mm]
    print(f"  {mu}: {int(c[grid >= Per('1975-01')].sum()):2d} months; CAGR {stats(r)['cagr']:.2f}% "
          f"(live {stats(live())['cagr']:.2f}%); with Sep-Nov 1987 set to live: {stats(r_ex87)['cagr']:.2f}%")
