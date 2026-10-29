"""Audit 2: where candidate 5.0's gain over live 4.1 comes from; episode concentration; untouched-window check."""
import numpy as np
import pandas as pd
from audit_lib import *  # noqa

W4 = (("1975-02", "2000-12"), ("2001-01", "2026-10"), ("1975-02", "2026-10"))
r5, e5, W5 = cand()
r0 = live()
print("== layer by layer (each added to live 4.1)")
print(line("live 4.1", r0))
print(line("+ squeeze cut only", cand(use_mu=False, xs=0, l="L0", d="D0")[0]))
print(line("+ melt-up cut only", cand(use_sq=False, xs=0, l="L0", d="D0")[0]))
print(line("+ Treasury condition D7 only", cand(use_sq=False, use_mu=False, xs=0, l="L0")[0]))
print(line("+ inflation sleeve only", cand(use_sq=False, use_mu=False, l="L0", d="D0")[0]))
print(line("+ sector tilt only", cand(use_sq=False, use_mu=False, xs=0, d="D0")[0]))
print(line("candidate 5.0", r5))
print(line("candidate 5.0 without melt-up", cand(use_mu=False)[0]))
print(line("candidate 5.0 without squeeze", cand(use_sq=False)[0]))
print(line("candidate 5.0 without sleeve", cand(xs=0)[0]))
print(line("candidate 5.0 without sector tilt", cand(l="L0")[0]))

spx_l = lvl(R0["spx"])
mu = (((spx_l / spx_l.shift(12) - 1) > 0.25) & ((X.gs10 - X.gs10.shift(12)) > 1.5)).fillna(False)
sq = (sc["squeeze"] >= 80).fillna(False)
on = lambda s: [str(p) for p in grid[s.values & (grid >= Per("1966-01")).astype(bool)]]
print("\nmelt-up months (decided at end of):", on(mu))
print("squeeze months:", on(sq))
# which squeeze/melt-up months were NOT already cut by live 4.1
new = (sq | mu) & (X.e41 > 0.999)
print(f"extra cut months not already at 0-stocks by 4.1: {int(new[grid >= Per('1975-01')].sum())}; "
      f"S&P return in the following month (avg) {R0['spx'].shift(-1)[new & (grid >= Per('1975-01'))].mean()*100:.2f}% "
      f"vs all months {R0['spx'][grid >= Per('1975-02')].mean()*100:.2f}%")

# monthly difference candidate - live, concentration
d = (r5 - r0)[grid >= Per("1975-02")]
dd = d.sort_values(ascending=False)
print("\n== top 10 months of candidate minus live (pct pts):")
print((dd.head(10) * 100).round(2).to_string())
lr = np.log1p(r5[grid >= Per("1975-02")]) - np.log1p(r0[grid >= Per("1975-02")])
tot = lr.sum()
top = lr.sort_values(ascending=False)
print(f"total log gain {tot*100:.1f} pts over {len(lr)} months; top 5 months = {top.head(5).sum()/tot:.0%}, top 10 = {top.head(10).sum()/tot:.0%}, top 20 = {top.head(20).sum()/tot:.0%}")
for k in (3, 5, 10):
    idx = top.head(k).index
    rr = r5.copy(); rr[idx] = r0[idx]
    print(f"  replace the {k} best months of the candidate by live's: candidate CAGR {stats(rr)['cagr']:.2f}% (live {stats(r0)['cagr']:.2f}%)")
print("\n== episodes (gain of candidate over live, compounded pct pts)")
for a, b in (("1987-08", "1987-12"), ("1999-12", "2002-12"), ("2021-06", "2023-06"), ("1975-01", "1986-12")):
    m = (grid > Per(a)) & (grid <= Per(b))
    print(f"  {a}..{b}: candidate {(np.prod(1+r5[m].values)-1)*100:6.1f}% live {(np.prod(1+r0[m].values)-1)*100:6.1f}%")

print("\n== 1966-1974 'untouched' window: what is active?")
m = (grid >= Per("1966-01")) & (grid <= Per("1974-12"))
print(f"  squeeze score available: {int(sc['squeeze'][m].notna().sum())} of {int(m.sum())} months")
print(f"  warning share > 0: {int((X.share[m] > 0).sum())}; e41 < 1: {int((X.e41[m] < 1).sum())}; melt-up: {int(mu[m].sum())}")
print(f"  gold sleeve on: {int(((X.cpi_yy > 3) & X.gold_up)[m].sum())}; commodity sleeve on: {int(((X.cpi_yy > 3) & X.com_up)[m].sum())}")
print(f"  sector tilt months (100% invested): {int((e5[m] > 0.999).sum())}")
g_avg_note = "gold price fixed at $35 until 1968 and not legal for US individuals until 1975-01"
print("  note:", g_avg_note)
print(line("  candidate 5.0 1966-74", r5, (("1966-01", "1974-12"),)), "|", line("live", r0, (("1966-01", "1974-12"),)))
print(line("  candidate 5.0 1966-74 without gold sleeve", cand(xs=0)[0], (("1966-01", "1974-12"),)))
