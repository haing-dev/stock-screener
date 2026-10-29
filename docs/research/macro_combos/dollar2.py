import os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "dollar.py")).read().split('log("\\n== dollar as a signal')[0]
exec(compile(src, "d", "exec"))
OUT.clear()
print("\n== squeeze gate neighbourhood (gate = Fed tightening OR score >= x)")
for x in (60, 70, 75, 80, 85, 90):
    print(line2(f"  squeeze >= {x}", run2(exposure(fed | (sq >= x).fillna(False)), base)))
for nm in ("dollar", "oil", "y10_chg", "baa_chg", "dollar_break"):
    if nm in sc:
        print(line2(f"  {nm} score >= 80", run2(exposure(fed | (sc[nm] >= 80).fillna(False)), base)))
print(line2("  squeeze >= 80 alone (no Fed gate)", run2(exposure((sq >= 80).fillna(False)), base)))
g = fed | (sq >= 80).fillna(False)
print(f"gate on: Fed {fed[grid>=Per('1979-01')].mean():.0%} of months; Fed or squeeze {g[grid>=Per('1979-01')].mean():.0%}; squeeze adds {(g & ~fed)[grid>=Per('1979-01')].mean():.0%}")
# placebo: squeeze months shuffled in runs
gv = ((sq >= 80) & ~fed).fillna(False).values
runs, cur, n = [], gv[0], 0
for v in gv:
    if v == cur: n += 1
    else: runs.append((cur, n)); cur, n = v, 1
runs.append((cur, n))
ons = [r for r in runs if r[0]]; offs = [r for r in runs if not r[0]]
rng = np.random.default_rng(11); obs = st(run2(exposure(g), base), "1975-02", "2026-10")[2]; pl = []
for _ in range(500):
    a_on = [ons[i] for i in rng.permutation(len(ons))]; a_off = [offs[i] for i in rng.permutation(len(offs))]
    seq, i, j, on = [], 0, 0, rng.random() < .5
    while i < len(a_on) or j < len(a_off):
        if (on and i < len(a_on)) or j >= len(a_off): seq += [True] * a_on[i][1]; i += 1
        else: seq += [False] * a_off[j][1]; j += 1
        on = not on
    gp = fed | pd.Series(seq[:T], index=grid)
    pl.append(st(run2(exposure(gp), base), "1975-02", "2026-10")[2])
pl = np.array(pl); print(f"placebo (squeeze months shuffled): real Sharpe {obs:.3f}, random median {np.median(pl):.3f}, share >= real {(pl >= obs).mean():.3f}")
# extra cut episodes from the squeeze gate
e3 = exposure(g); r3 = run2(e3, base); r0 = run2(e, base)
d = (e3 < e - 1e-9)
grp = (d != d.shift()).cumsum()
for k, sub in d[d].groupby(grp[d]):
    ix = sub.index; held = grid[(grid > ix[0]) & (grid <= ix[-1] + 1)]
    f = lambda r: (np.prod(1 + r[held].values) - 1) * 100
    print(f"  {ix[0]}..{ix[-1]}: min stocks {e3[ix].min():.0%}; new {f(r3):+.1f}% vs live {f(r0):+.1f}% -> {f(r3)-f(r0):+.1f} pts")
print("today: squeeze score", round(sq.dropna().iloc[-1]), "->", "gate ON" if g.iloc[-1] else "gate off", "; exposure", f"{e3.iloc[-1]:.0%}")
