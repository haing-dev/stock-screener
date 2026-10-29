"""Robustness of candidate 5.0 = E3-D7-X3-L4:
 E3 live 4.1 + squeeze score >= 80 -> 0% stocks + melt-up (S&P 12m > 25% and 10y +1.5 pts in 12m) -> 0% stocks
 D7 non-stock share: long Treasuries only in a growth-trend cut with stock-bond corr < 0 and 10y >= Fed funds, else bills
 X3 10% gold when CPI y/y > 3% and gold above its 10m average; 10% commodities when CPI > 3% and commodities above 10m avg
 L4 sector momentum tilt (top/bottom 5 of 20, 1.5x/0.5x) while 100% in stocks."""
import itertools

from exp_combo import *  # noqa


def cand(sq=80, mu=(0.25, 1.5), cpi_th=3.0, xs=0.1, l="L4", d="D7", cost=COST):
    sqc = (sc["squeeze"] >= sq).fillna(False)
    spx_l = lvl(R["spx"])
    muc = (((spx_l / spx_l.shift(12) - 1) > mu[0]) & ((gs10 - gs10.shift(12)) > mu[1])).fillna(False)
    e = np.minimum(e41, pd.Series(np.where(sqc | muc, 0.0, 1.0), index=grid))
    h = (cpi_yy > cpi_th).fillna(False)
    x = {"gold": xs * (h & gold_up), "commod": xs * (h & com_up)} if xs else {}
    return run(build(e, D_[d], x, l), cost=cost), e


W66 = (("1966-01", "1974-12"), ("1975-02", "2000-12"), ("2001-01", "2026-10"), ("1975-02", "2026-10"))
r5, e5 = cand()
print("== CAGR / worst / Sharpe: 1966-1974 (untouched) | 1975-2000 | 2001-2026 | 1975-2026")
print(line("S&P 500", R["spx"], W66))
print(line("live 4.1", run(W41), W66))
print(line("candidate 5.0", r5, W66))
print(line("candidate 5.0 at 0.3% cost per trade", cand(cost=0.003)[0], W66))
print("\n== neighbourhood")
for sq in (70, 75, 85, 90):
    print(line(f"squeeze >= {sq}", cand(sq=sq)[0], W66))
for mu in ((0.20, 1.5), (0.30, 1.5), (0.25, 1.0), (0.25, 2.0), (0.20, 1.0)):
    print(line(f"melt-up {mu}", cand(mu=mu)[0], W66))
for c_ in (2.5, 3.5, 4.0):
    print(line(f"inflation sleeve CPI > {c_}", cand(cpi_th=c_)[0], W66))
for xs in (0.05, 0.15, 0.2):
    print(line(f"sleeve {xs:.0%} each", cand(xs=xs)[0], W66))
print(line("without sector tilt (L0)", cand(l="L0")[0], W66))
print(line("China cycle instead of sector tilt (L1)", cand(l="L1")[0], W66))
print(line("live defensive rule (D0)", cand(d="D0")[0], W66))

# placebo: melt-up + squeeze months shuffled in runs (same counts and lengths)
sqc = (sc["squeeze"] >= 80).fillna(False)
spx_l = lvl(R["spx"])
muc = (((spx_l / spx_l.shift(12) - 1) > 0.25) & ((gs10 - gs10.shift(12)) > 1.5)).fillna(False)
g = (sqc | muc).values
runs, cur, n = [], g[0], 0
for v in g:
    if v == cur:
        n += 1
    else:
        runs.append((cur, n)); cur, n = v, 1
runs.append((cur, n))
ons = [x for x in runs if x[0]]; offs = [x for x in runs if not x[0]]
rng = np.random.default_rng(5)
h = (cpi_yy > 3).fillna(False)
xx = {"gold": 0.1 * (h & gold_up), "commod": 0.1 * (h & com_up)}
obs = stats(r5, "1975-02", "2026-10")["sh"]
pl = []
for _ in range(300):
    a_on = [ons[i] for i in rng.permutation(len(ons))]; a_off = [offs[i] for i in rng.permutation(len(offs))]
    seq, i, j, on = [], 0, 0, rng.random() < .3
    while i < len(a_on) or j < len(a_off):
        if (on and i < len(a_on)) or j >= len(a_off):
            seq += [True] * a_on[i][1]; i += 1
        else:
            seq += [False] * a_off[j][1]; j += 1
        on = not on
    gp = pd.Series(seq[:T], index=grid)
    e = np.minimum(e41, pd.Series(np.where(gp, 0.0, 1.0), index=grid))
    pl.append(stats(run(build(e, D_["D7"], xx, "L4")), "1975-02", "2026-10")["sh"])
pl = np.array(pl)
print(f"\nplacebo (extra cuts shuffled in time, 300 draws): real Sharpe {obs:.3f}; random median {np.median(pl):.3f}; share >= real {(pl >= obs).mean():.3f}")

# bootstrap gain vs live
x5 = r5[(grid >= Per("1975-02"))] - rf[(grid >= Per("1975-02"))]
x0 = run(W41)[(grid >= Per("1975-02"))] - rf[(grid >= Per("1975-02"))]
Tn = len(x5); B = 2000; Lb = 12
idx = np.empty((B, Tn), dtype=np.int64); idx[:, 0] = rng.integers(0, Tn, B)
jump = rng.random((B, Tn)) < 1 / Lb; fresh = rng.integers(0, Tn, (B, Tn))
for t in range(1, Tn):
    idx[:, t] = np.where(jump[:, t], fresh[:, t], (idx[:, t - 1] + 1) % Tn)
a5, a0 = x5.values[idx], x0.values[idx]
d = a5.mean(1) / a5.std(1) - a0.mean(1) / a0.std(1)
print(f"bootstrap: Sharpe gain vs live <= 0 in {(d <= 0).mean():.3f} of draws")

# episodes
print("\n== S&P falls of 15%+ and big rallies: total return over the window (candidate / live / S&P 500)")
r0 = run(W41)
for a, b in (("1973-01", "1974-09"), ("1980-11", "1982-07"), ("1987-08", "1987-11"), ("1990-06", "1990-10"),
             ("1998-06", "1998-08"), ("2000-08", "2002-09"), ("2007-10", "2009-02"), ("2011-04", "2011-09"),
             ("2018-09", "2018-12"), ("2020-01", "2020-03"), ("2020-03", "2020-12"), ("2021-12", "2022-09"),
             ("2023-01", "2023-12"), ("2025-01", "2025-04"), ("2025-04", "2026-10")):
    m = (grid > Per(a)) & (grid <= Per(b))
    f = lambda x: (np.prod(1 + x[m].fillna(0).values) - 1) * 100
    print(f"  {a}..{b}: {f(r5):6.1f}% / {f(r0):6.1f}% / {f(R['spx']):6.1f}%")
print("\n== by decade CAGR (candidate / live / S&P)")
for a, b in (("1966-01", "1974-12"), ("1975-01", "1984-12"), ("1985-01", "1994-12"), ("1995-01", "2004-12"),
             ("2005-01", "2014-12"), ("2015-01", "2026-10")):
    print(f"  {a[:4]}-{b[:4]}: {stats(r5, a, b)['cagr']:5.1f} / {stats(r0, a, b)['cagr']:5.1f} / {stats(R['spx'], a, b)['cagr']:5.1f}")
print(f"\nturnover: exposure changes per year {(e5.diff().abs() > 0.005)[grid >= Per('1975-01')].sum() / 51.8:.1f}; avg stocks {e5.shift(1)[grid >= Per('1975-02')].mean():.0%}")
pickle.dump({"r5": r5, "e5": e5}, open("cand5.pkl", "wb"))
