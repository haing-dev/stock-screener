"""Untouched extra check: 1966-1974 (never used in any fit; data exists from 1960) + where the winner lost vs S&P."""
import os, math
HERE = os.path.dirname(os.path.abspath(__file__))
exec(compile(open(os.path.join(HERE, "robust.py")).read().split("gtt = trend_dn & unr_up")[0], "rb", "exec"))
OUT.clear()
gtt = trend_dn & unr_up
print("months with >=10 core indicators scored, first:", av.sum(axis=1)[av.sum(axis=1) >= 10].index[0])
for a, b in (("1966-01", "1974-12"), ("1969-01", "1970-06"), ("1973-01", "1974-09")):
    print(f"== {a}..{b}")
    for nm, e, bb, s in (("S&P 500", pd.Series(1.0, index=grid), "T", "S0"),
                         ("live rule", engine(pd.Series(True, index=grid), None, 0.5), "T", "S0"),
                         ("winner (weighted)", engine(fed_tight, gtt), "B2", "S2"),
                         ("winner (equal-wt)", engine(fed_tight, gtt, w="W2"), "B2", "S2"),
                         ("winner T-bills no tilt", engine(fed_tight, gtt), "T", "S0"),
                         ("winner floor 25%", engine(fed_tight, gtt, 0.25), "B2", "S2")):
        r, eh = sim(e, bb, s)
        x = st(r, a, b)
        print(f"  {nm:<24} CAGR {x['cagr']:6.1f}%  worst {x['dd']:6.1f}%  Sharpe {x['sh']:5.2f}  avg stocks {eh[(grid>=Per(a))&(grid<=Per(b))].mean():.0%}")
# where the winner lagged: months at <=25% stocks, S&P return in them
rw, eh = sim(engine(fed_tight, gtt))
m = SEL["F"] & (eh.values <= 0.25)
mk = mkt[m]
print(f"\n== months with the winner at <=25% stocks: {m.sum()}; S&P in them avg {mk.mean()*100:+.2f}%/mo vs all months {mkt[SEL['F']].mean()*100:+.2f}")
ex = pd.Series(eh.values, index=grid)
blk = (ex <= 0.25) & SEL["F"]
g = (blk != blk.shift()).cumsum()
for k, sub in ex[blk].groupby(g[blk]):
    idx = sub.index
    sp = (np.prod(1 + mkt[idx].values) - 1) * 100
    wv = (np.prod(1 + rw[idx].values) - 1) * 100
    print(f"  {idx[0]}..{idx[-1]} ({len(idx)}m): S&P {sp:+6.1f}%  winner {wv:+6.1f}%  -> {wv-sp:+6.1f} pts  {'FED' if fed_tight.shift(1)[idx].any() else 'gtt'}")
