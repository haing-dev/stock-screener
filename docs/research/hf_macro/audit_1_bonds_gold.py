"""Audit 1: reproduce headline; bond returns from monthly-average yields; gold month-end estimate in the signal."""
import os
import numpy as np
import pandas as pd
from audit_lib import *  # noqa
import audit_lib as A

pd.set_option("display.width", 220)
print("== reproduce (CAGR / worst / Sharpe: 1975-2000 | 2001-2026 | 1975-2026)")
r5, e5, W5 = cand()
print(line("S&P 500", R0["spx"]))
print(line("live 4.1", live()))
print(line("candidate 5.0 (reproduced)", r5))

# ------------------------------------------------------------ bonds
RD = "/home/claude/stock-screener/cache/macro/raw/research"


def daily_me(sid):
    s = pd.read_csv(os.path.join(RD, sid + ".csv"))
    s["value"] = pd.to_numeric(s["value"], errors="coerce")
    s = s.dropna()
    d = pd.to_datetime(s["date"])
    return pd.Series(s["value"].values, index=d.dt.to_period("M")).groupby(level=0).last().reindex(grid)


d10, d30 = daily_me("DGS10"), daily_me("DGS30")
g10a = X.F["GS10"]
import macro.engine as E
os.chdir("/home/claude/stock-screener")
g30a = E.fred_monthly("GS30", grid)
syn = lambda yy, d: yy.shift(1) / 1200 - d * (yy - yy.shift(1)) / 100
tlt = R0["t30y"].where(grid >= Per("2002-08"))
ief = (R0["t10y"]).where(grid >= Per("2002-08"))

cmp = pd.DataFrame({"TLT": tlt, "syn30_avg_d15": syn(g30a, 15), "syn30_me_d15": syn(d30, 15),
                    "par30_me": par_bond_ret(d30.shift(1), d30, 30), "par30_avg": par_bond_ret(g30a.shift(1), g30a, 30)})
ok = cmp.dropna().loc["2006-03":]
print("\n== 30y synthetic vs TLT, 2006-03..2026-10 (%d months): corr same month / corr with TLT one month EARLIER" % len(ok))
for c in cmp.columns[1:]:
    print(f"  {c:16s} corr {ok['TLT'].corr(ok[c]):.3f}  corr vs TLT(t-1) {ok[c].corr(ok['TLT'].shift(1).reindex(ok.index)):.3f}  "
          f"vol {ok[c].std()*np.sqrt(12)*100:.1f}% (TLT {ok['TLT'].std()*np.sqrt(12)*100:.1f}%)")
cmp10 = pd.DataFrame({"IEF": ief, "syn10_avg_d7": syn(g10a, 7), "par10_me": par_bond_ret(d10.shift(1), d10, 10)}).dropna()
print("10y synthetic vs IEF 2002-08..: " + ", ".join(f"{c} corr {cmp10['IEF'].corr(cmp10[c]):.3f}" for c in cmp10.columns[1:]))

# Look-ahead: correlation of the avg-yield bond return in month t+1 with the S&P return in month t (already known)
spx = R0["spx"]
m = (grid >= Per("1977-03")) & (grid <= Per("2002-01"))
for nm, s in (("syn30 avg-yield d15", syn(g30a, 15)), ("par30 month-end", par_bond_ret(d30.shift(1), d30, 30))):
    x = pd.DataFrame({"b_next": s.shift(-1), "spx_now": spx, "b_now": s})[m].dropna()
    print(f"  1977-2002 {nm:22s}: corr(bond t+1, S&P t) {x['b_next'].corr(x['spx_now']):+.3f}; autocorr {x['b_next'].corr(x['b_now']):+.3f}")

# fixed bond panel: TLT, else exact par 30y on month-end yields, else par 10y on month-end yields
t30_fix = tlt.combine_first(par_bond_ret(d30.shift(1), d30, 30)).combine_first(par_bond_ret(d10.shift(1), d10, 10))
t30_avg_exact = tlt.combine_first(par_bond_ret(g30a.shift(1), g30a, 30)).combine_first(par_bond_ret(g10a.shift(1), g10a, 10))
t30_me_d15 = tlt.combine_first(syn(d30, 15)).combine_first(syn(d10, 7))
held = W5["t30y"].shift(1).fillna(0) > 0
hm = held & (grid >= Per("1975-02"))
print(f"\nmonths candidate 5.0 holds t30y (1975-2026): {int(hm.sum())}; of which pre-TLT {int((hm & (grid < Per('2002-08'))).sum())}")
for nm, s in (("author (avg yields, fixed duration)", R0["t30y"]), ("month-end yields, author's duration", t30_me_d15),
              ("avg yields, exact par pricing", t30_avg_exact), ("month-end yields, exact par pricing", t30_fix)):
    print(f"  t30y compounded over the held months, {nm:40s}: {(np.prod(1 + s[hm].values) - 1) * 100:7.1f}%")
for nm, s in (("author", R0["t30y"]), ("fixed", t30_fix)):
    for a, b in (("1980-01", "1983-12"), ("1990-06", "1991-06"), ("2000-09", "2003-06"), ("2007-10", "2009-06")):
        mm = hm & (grid >= Per(a)) & (grid <= Per(b))
        print(f"    {nm:7s} {a}..{b}: {int(mm.sum())} held months, {(np.prod(1 + s[mm].values) - 1) * 100:6.1f}%")

Rb = R0.copy()
Rb["t30y"] = t30_fix
print("\n== with exact month-end Treasury returns")
print(line("live 4.1", live(Rb)))
rb5, _, _ = cand(Rb)
print(line("candidate 5.0", rb5))
Rb2 = R0.copy(); Rb2["t30y"] = t30_me_d15
print(line("candidate 5.0 (month-end yields, author duration)", cand(Rb2)[0]))
Rb3 = R0.copy(); Rb3["t30y"] = t30_avg_exact
print(line("candidate 5.0 (avg yields, exact pricing)", cand(Rb3)[0]))

# ------------------------------------------------------------ gold
g_avg = E._csv("GOLD")
g_avg = pd.Series(g_avg.values, index=g_avg.index.to_period("M")).groupby(level=0).last().reindex(grid)
pre = grid < Per("2000-09")
# (a) signal from the monthly average known at t (avg_t vs its own 10-month mean); after 2000-09 the author's
gu_avg = (g_avg > g_avg.rolling(10).mean()).fillna(False)
gu_a = X.gold_up.where(~pre, gu_avg)
# (b) author's estimated level lagged one month (uses avg_t only)
gu_b = X.gold_up.where(~pre, X.gold_up.shift(1).fillna(False))
hot = (X.cpi_yy > 3).fillna(False)
on = lambda g: int((g & hot)[(grid >= Per("1975-01")) & pre].sum())
print(f"\n== gold sleeve months on 1975-2000/08: author {on(X.gold_up)}, avg-based {on(gu_a)}, lagged {on(gu_b)}; "
      f"disagree {int(((X.gold_up != gu_a) & hot)[(grid >= Per('1975-01')) & pre].sum())}")
# predictive content of the leak: next-month gold return when signal on vs off
nxt = R0["gold"].shift(-1)
mm = (grid >= Per("1975-01")) & pre
for nm, gsig in (("author signal", X.gold_up), ("avg-based signal", gu_a)):
    a, b = nxt[mm & gsig].mean() * 1200, nxt[mm & ~gsig].mean() * 1200
    print(f"  {nm:18s}: next-month gold return when on {a:5.1f}%/yr, off {b:5.1f}%/yr")
print(line("candidate 5.0, gold signal from known monthly average", cand(gold_up=gu_a)[0]))
print(line("candidate 5.0, gold signal lagged one month", cand(gold_up=gu_b)[0]))
# Is 1975-2000 gold proxy return itself biased? compare avg-to-avg to end estimate compounded
print(f"  gold 1975-01..2000-08 compounded: end-estimate {(np.prod(1+R0['gold'][mm].values)-1)*100:.0f}%; "
      f"avg-to-avg {(g_avg[Per('2000-08')]/g_avg[Per('1974-12')]-1)*100:.0f}%")

Rf = Rb.copy()
print("\n== bonds fixed + gold signal fixed")
print(line("candidate 5.0", cand(Rf, gold_up=gu_a)[0]))
import pickle
pickle.dump({"t30_fix": t30_fix, "gu_a": gu_a, "d10": d10, "d30": d30}, open(os.path.join(A.HERE, "audit_fix.pkl"), "wb"))
