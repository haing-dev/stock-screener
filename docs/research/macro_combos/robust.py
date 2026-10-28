"""Robustness of the grid's leading family: macro warnings acted on only while the Fed is tightening (G5) + growth-trend
cut (X1). Neighbourhood of the Fed-gate and growth-trend settings, random-schedule placebo for the Fed gate, decades,
episodes, IEF check, today's reading."""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "combos.py")).read().split("# ---------------------------------------------------------------- engines")[0]
exec(compile(src, "combos_head", "exec"))

import numpy as np    # noqa: E402
import pandas as pd   # noqa: E402

OUT.clear()
cn = corr_neg.shift(1).fillna(False).astype(bool).values
bv = bond.values
ief = P["ief"].values
rfv, mv = rf.values, mkt.values


def sim(e, b="B2", s="S2", bondv=None):
    e = pd.Series(e, index=grid).astype(float).fillna(1.0)
    eh = e.shift(1).values
    fp = (e.shift(1) > 1 - 1e-9).values
    bb = bv if bondv is None else bondv
    alt = rfv if b == "T" else (np.where(cn, bb, rfv) if b == "B2" else bb)
    act = 0.0 if s == "S0" else (ACT.values * fp if s == "S2" else ACT.values)
    return pd.Series(eh * (mv + act) + (1 - eh) * alt, index=grid), pd.Series(eh, index=grid)


def st(r, a="1975-02", b="2026-10"):
    m = (grid >= Per(a)) & (grid <= Per(b))
    x, f = r[m], rf[m]
    if x.isna().any():
        return dict(cagr=np.nan, dd=np.nan, sh=np.nan)
    lv = np.r_[1, (1 + x.values).cumprod()]
    return dict(cagr=(lv[-1] ** (12 / len(x)) - 1) * 100, dd=(lv / np.maximum.accumulate(lv) - 1).min() * 100,
                sh=(x - f).mean() / x.std() * math.sqrt(12))


def row(name, r, eh):
    a, b, f = st(r, "1975-02", "2000-12"), st(r, "2001-01", "2026-10"), st(r)
    return dict(name=name, A_cagr=a["cagr"], A_dd=a["dd"], A_sh=a["sh"], B_cagr=b["cagr"], B_dd=b["dd"], B_sh=b["sh"],
                F_cagr=f["cagr"], F_dd=f["dd"], F_sh=f["sh"], avg_eq=eh[SEL["F"]].mean() * 100)


def engine(gate, xcut, floor=0.0, w="W1"):
    e = 1 - I[w] * (1 - floor) * gate.astype(float)
    if xcut is not None:
        e = np.minimum(e, pd.Series(np.where(xcut, floor, 1.0), index=grid))
    return pd.Series(e, index=grid)


gtt = trend_dn & unr_up
rows = []
for nm, e, b, s in (("S&P 500", pd.Series(1.0, index=grid), "T", "S0"),
                    ("live rule (T-bills)", engine(pd.Series(True, index=grid), None, 0.5), "T", "S0"),
                    ("winner: Fed gate + growth-trend, floor 0, bonds if corr<0, momentum", engine(fed_tight, gtt), "B2", "S2"),
                    ("  same, T-bills, no momentum", engine(fed_tight, gtt), "T", "S0"),
                    ("  same, floor 25%", engine(fed_tight, gtt, 0.25), "B2", "S2"),
                    ("  same, floor 50%", engine(fed_tight, gtt, 0.5), "B2", "S2"),
                    ("  Fed gate only (no growth-trend), T-bills", engine(fed_tight, None), "T", "S0"),
                    ("  growth-trend only, floor 0, T-bills", engine(pd.Series(False, index=grid), gtt), "T", "S0"),
                    ("  live rule + growth-trend, T-bills", engine(pd.Series(True, index=grid), gtt), "T", "S0")):
    r, eh = sim(e, b, s)
    rows.append(row(nm, r, eh))
log("== the winner and its parts")
log(pd.DataFrame(rows).set_index("name").round(2).to_string())

# ---------------- neighbourhood of the Fed gate
log("\n== Fed gate settings (rise above the N-month low, pts) with growth-trend cut, floor 0, bonds if corr<0, momentum; "
    "cells: Sharpe 1975-2000 / 2001-2026, worst fall full")
tab = {}
for lb in (12, 18, 24, 36):
    for th in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0):
        g = (ff - ff.rolling(lb, min_periods=lb // 2).min()) >= th
        r, eh = sim(engine(g, gtt))
        a, b, f = st(r, "1975-02", "2000-12"), st(r, "2001-01", "2026-10"), st(r)
        tab.setdefault(f"{lb}m", {})[th] = f"{a['sh']:.2f}/{b['sh']:.2f} {f['dd']:.0f}%"
log(pd.DataFrame(tab).T.to_string())
alt_g = {"funds rate above 12 months ago": ff > ff.shift(12),
         "funds rate above 6 months ago": ff > ff.shift(6),
         "funds rate 12m change >= +1 pt": (ff - ff.shift(12)) >= 1,
         "2y yield above funds rate (market expects hikes)": F["GS2"] > ff}
for nm, g in alt_g.items():
    r, eh = sim(engine(g.fillna(False), gtt))
    a, b, f = st(r, "1975-02", "2000-12"), st(r, "2001-01", "2026-10"), st(r)
    log(f"  {nm:<48} {a['sh']:.2f}/{b['sh']:.2f}  CAGR {f['cagr']:.1f}%  worst {f['dd']:.0f}%")
log(f"  share of months with the Fed gate on (24m, 1 pt): {fed_tight[SEL['F']].mean():.0%}")

# ---------------- neighbourhood of the growth-trend cut
log("\n== growth-trend settings (with the 24m/1pt Fed gate, floor 0, B2, momentum)")
lvl = E.level(mkt)
for nm, x in {"trend 10m & unemp > 12m avg (base)": gtt,
              "trend 8m & unemp > 12m avg": lvl < lvl.rolling(8).mean(),
              "trend 12m & unemp > 12m avg": lvl < lvl.rolling(12).mean(),
              "trend 10m & unemp 3m avg >= 12m low + 0.3": None,
              "trend 10m & unemp > 6m avg": trend_dn & (unr > unr.rolling(6).mean()),
              "trend 10m & unemp > 24m avg": trend_dn & (unr > unr.rolling(24).mean())}.items():
    if nm.startswith("trend 8m") or nm.startswith("trend 12m"):
        x = x & unr_up
    if x is None:
        x = trend_dn & ((unr.rolling(3).mean() - unr.rolling(12).min()) >= 0.3)
    r, eh = sim(engine(fed_tight, x))
    a, b, f = st(r, "1975-02", "2000-12"), st(r, "2001-01", "2026-10"), st(r)
    log(f"  {nm:<46} {a['sh']:.2f}/{b['sh']:.2f}  CAGR {f['cagr']:.1f}%  worst {f['dd']:.0f}%")

# ---------------- placebo: Fed gate replaced by random schedules with the same on-share and run lengths
log("\n== placebo: the Fed gate replaced by 1000 random on/off schedules (same runs, shuffled in time)")
g = fed_tight.values.astype(bool)
runs, cur, n = [], g[0], 0
for v in g:
    if v == cur:
        n += 1
    else:
        runs.append((cur, n))
        cur, n = v, 1
runs.append((cur, n))
ons = [r_ for r_ in runs if r_[0]]
offs = [r_ for r_ in runs if not r_[0]]
rng = np.random.default_rng(7)
obs_r, _ = sim(engine(fed_tight, gtt))
obs = st(obs_r)["sh"]
pl = []
for _ in range(1000):
    a_on = [ons[i] for i in rng.permutation(len(ons))]
    a_off = [offs[i] for i in rng.permutation(len(offs))]
    seq = []
    start_on = rng.random() < 0.5
    i = j = 0
    while i < len(a_on) or j < len(a_off):
        if (start_on and i < len(a_on)) or j >= len(a_off):
            seq += [True] * a_on[i][1]
            i += 1
        else:
            seq += [False] * a_off[j][1]
            j += 1
        start_on = not start_on
    gp = pd.Series(seq[:T], index=grid)
    r, _ = sim(engine(gp, gtt))
    pl.append(st(r)["sh"])
pl = np.array(pl)
log(f"  real Fed gate Sharpe {obs:.3f}; random schedules median {np.median(pl):.3f}, 95th pct {np.percentile(pl, 95):.3f}; "
    f"share of random >= real: {(pl >= obs).mean():.3f}")

# ---------------- decades
log("\n== by decade: CAGR % (winner / live rule / S&P 500)")
rw, _ = sim(engine(fed_tight, gtt))
rr, _ = sim(engine(pd.Series(True, index=grid), None, 0.5), "T", "S0")
for a, b in (("1975-02", "1979-12"), ("1980-01", "1989-12"), ("1990-01", "1999-12"), ("2000-01", "2009-12"),
             ("2010-01", "2019-12"), ("2020-01", "2026-10")):
    log(f"  {a[:4]}-{b[:4]}: {st(rw, a, b)['cagr']:5.1f} / {st(rr, a, b)['cagr']:5.1f} / {st(mkt, a, b)['cagr']:5.1f}")

# ---------------- episodes
log("\n== sell-offs: total return over the S&P 500's fall (peak to trough, month end): winner / live rule / S&P 500")
lv = E.level(mkt)
for a, b in (("1980-11", "1982-07"), ("1987-08", "1987-11"), ("1990-06", "1990-10"), ("1998-06", "1998-08"),
             ("2000-08", "2002-09"), ("2007-10", "2009-02"), ("2011-04", "2011-09"), ("2015-05", "2016-02"),
             ("2018-09", "2018-12"), ("2020-01", "2020-03"), ("2021-12", "2022-09")):
    m = (grid > Per(a)) & (grid <= Per(b))
    f = lambda x: (np.prod(1 + x[m].values) - 1) * 100
    log(f"  {a} to {b}: {f(rw):6.1f}% / {f(rr):6.1f}% / {f(mkt):6.1f}%")

# ---------------- IEF check (2002-08+)
iefs = pd.Series(ief, index=grid)
r_ief, _ = sim(engine(fed_tight, gtt), bondv=iefs.fillna(pd.Series(bv, index=grid)).values)
log(f"\n== IEF instead of the synthetic bond (2002-08..2026-10): synthetic {st(rw, '2002-08')['cagr']:.1f}%/yr, Sharpe "
    f"{st(rw, '2002-08')['sh']:.2f}; IEF {st(r_ief, '2002-08')['cagr']:.1f}%/yr, Sharpe {st(r_ief, '2002-08')['sh']:.2f}")

# ---------------- costs and turnover
ew_ = engine(fed_tight, gtt)
d = ew_.diff().abs()
log(f"\n== winner trades: {(d[SEL['F']] > 0.005).sum() / (len(grid[SEL['F']]) / 12):.1f} exposure changes/yr; "
    f"avg stocks {ew_.shift(1)[SEL['F']].mean():.0%}; months at 0% stocks: {(ew_[SEL['F']] < 0.01).mean():.0%}")

# ---------------- today
t = grid[-1]
log(f"\n== reading at {t}: Fed funds {ff.iloc[-1]:.2f} (24m low {ff.rolling(24).min().iloc[-1]:.2f}) -> Fed gate "
    f"{'ON' if fed_tight.iloc[-1] else 'off'}; S&P {'below' if trend_dn.iloc[-1] else 'above'} its 10-month average; "
    f"unemployment {unr.iloc[-1]:.1f} vs 12m avg {unr.rolling(12).mean().iloc[-1]:.2f}; warning share {share_w.iloc[-1]:.1%}; "
    f"winner exposure {ew_.iloc[-1]:.0%} stocks; live rule {1 - I['W1'].iloc[-1] * 0.5:.0%}")
log("  last 24 months of the winner's exposure: " + " ".join(f"{p.strftime('%y%m')}:{v:.0%}" for p, v in ew_.iloc[-24:].items()))
open(os.path.join(HERE, "log_robust.txt"), "w").write("\n".join(OUT))
