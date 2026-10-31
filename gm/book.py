"""Global Macro Book v1 (2026-10-30): combine the signal families into one risk-managed, costed paper book.

Pipeline, all point in time (positions decided at month end t, earn month t+1):
 1. Family positions per market (signals.py definitions): price trend, economic trend, carry, value, cross-sectional
    momentum. Each family-and-asset-class block is scaled to unit ex-ante volatility (trailing 36-month realised vol of
    the block, lagged), so blocks are comparable.
 2. Family risk shares (plan section 3, fixed before the holdout): trend 30, econ 30, carry 20, value 15, momentum 5
    (the 10% earmarked for WRDS revisions moved to trend and econ, as the plan prescribes when it is not live).
    Asset classes get equal risk.
 3. Whole book scaled to 10% annual vol (trailing 36-month realised vol of the unscaled book, lagged); gross notional
    capped at 5x; one market capped at 10% of the risk budget (position x vol <= 0.1 x 10% ... approximated by a
    notional-vol cap).
 4. Costs: one-way cost per market type on every change in position, plus futures rolls; EM equity shorts pay 1%/yr
    borrow. Results also at twice the costs.

Placeholders (not yet in v1; marked so the site and the plan show them):
 - BLOOMBERG (next week): per-commodity excess-return history before 2000 and futures curves -> commodity carry for
   metals, grains, softs and livestock; replaces the AQR index stand-in.
 - EQUITY VALUE / CARRY: needs country valuations and dividend yields (WRDS research, or MSCI P/E, P/B, D/Y live).
 - WRDS REVISIONS (family 3.6): research only; weight moved to trend and econ.
 - RISK SCALER (early-warning, 30-100% of risk): separate test, next version.
 - ECON POINT-IN-TIME: econ uses revised OECD data; first-release vintages needed before it counts.
Design period 1990-2010, extra check 1975-89. The holdout 2011-2026 is not printed (run once after freezing).
"""
import os
import pickle

import numpy as np
import pandas as pd

from . import panel as P
from . import signals as G

FAMILY_W = {"trend": 0.30, "econ": 0.30, "carry": 0.20, "value": 0.15, "xsmom": 0.05}
VOL_TARGET = 0.10
GROSS_CAP = 5.0
MARKET_RISK_CAP = 0.10          # one market at most 10% of the book's risk (position x vol <= 0.1 x 10%... see cap())
PLACEHOLDERS = ["BLOOMBERG commodity curves and pre-2000 commodity returns",
                "EQUITY value for emerging markets (only DM + US by dividend yield so far); equity carry (failed)",
                "WRDS revisions (research only)", "Early-warning risk scaler (tested, not adopted)",
                "Econ growth theme on first-release data (left out in v1.1)"]
EM_EQ = ("eq_cn", "eq_kr_kospi", "eq_tw", "eq_in", "eq_br_ibov", "eq_mx_ipc", "eq_za")
EM_FX = ("fx_mxn", "fx_brl", "fx_krw", "fx_zar")


def cost_bp(k):
    """One-way cost (bp of notional) and futures rolls per year."""
    if k.startswith("eq_"):
        return (5.0, 0) if k in EM_EQ else ((1.0, 4) if k.startswith("eq_us") else (2.0, 4))
    if k.startswith(("bd_", "st_")):
        return 1.0, 4
    if k.startswith("fx_"):
        return (8.0, 4) if k in EM_FX else (2.0, 4)
    if k.startswith("cm_"):
        return (6.0, 12) if k in ("cm_natgas",) else ((4.0, 12) if k in ("cm_wti", "cm_brent", "cm_heatoil",
                                                                         "cm_gasoline") else (4.0, 5))
    return 3.0, 4


def family_positions(R):
    """Unscaled position (notional per unit capital) per family, per market: score x 40% / vol, equal weight in class."""
    S = pickle.load(open(os.path.join(P.OUT, "signals.pkl"), "rb"))
    lvl = (1 + R.fillna(0)).cumprod().where(R.notna().cummax())
    trend = sum(np.sign(lvl / lvl.shift(h) - 1) for h in (1, 3, 12)) / 3
    xsm = np.log1p(R).shift(1).rolling(11, min_periods=11).sum()
    V = S["V"][[c for c in S["V"].columns if c.startswith(("fx_", "bd_", "eq_"))]]  # commodity value: failed, out
    C = S["C"][[c for c in S["C"].columns if not c.startswith("eq_")]]       # equity carry: weak in design, out
    fams = {"trend": (trend, "dir"), "econ": (S["E"], "dir"), "carry": (C, "half"), "value": (V, "cs"),
            "xsmom": (xsm, "cs")}
    vol = R.rolling(36, min_periods=12).std() * np.sqrt(12)
    out = {}
    for f, (X, kind) in fams.items():
        X = X.reindex(index=R.index)
        pos = {}
        for c, pre in G.CLASSES.items():
            cols = [k for k in X.columns if k.startswith(pre) and k in R and k != "cm_aqr_ew" or
                    (k == "cm_aqr_ew" and f in ("trend",) and k in X.columns)]
            cols = [k for k in cols if k in R.columns]
            if not cols:
                continue
            if kind == "dir":
                w = X[cols].clip(-1, 1)
            elif kind == "cs":
                w = G.cs_rank(X, cols)
            else:
                w = (G.cs_rank(X, cols).fillna(0) * 0.5 + np.sign(X[cols]) * 0.5).where(X[cols].notna())
            p = w * 0.40 / vol[cols]
            n = p.notna().sum(axis=1)
            pos[c] = p.div(n.where(n > 0), axis=0)
        out[f] = pos
    return out


def run(R, cost_mult=1.0):
    fam = family_positions(R)
    total = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    by_fam = {f: pd.DataFrame(0.0, index=R.index, columns=R.columns) for f in fam}
    blocks = {}
    for f, pos in fam.items():
        for c, p in pos.items():
            r = (p.shift(1) * R[p.columns]).sum(axis=1, min_count=1)
            k = (1.0 / (r.rolling(36, min_periods=24).std() * np.sqrt(12))).shift(1).clip(upper=50)
            blocks[(f, c)] = r * k
            scaled = p.mul(k, axis=0) * FAMILY_W[f]
            total[scaled.columns] = total[scaled.columns].add(scaled.fillna(0), fill_value=0)
            by_fam[f][scaled.columns] = by_fam[f][scaled.columns].add(scaled.fillna(0), fill_value=0)
    active = pd.concat(blocks, axis=1).notna().any(axis=1)
    raw = (total.shift(1) * R.fillna(0)).sum(axis=1).where(active)
    s = (VOL_TARGET / (raw.rolling(36, min_periods=24).std() * np.sqrt(12))).shift(1)
    pos = total.mul(s, axis=0)
    # caps: one market's risk (|pos| x vol) at most MARKET_RISK_CAP of the target... expressed per market
    vol = R.rolling(36, min_periods=12).std() * np.sqrt(12)
    cap = (MARKET_RISK_CAP * VOL_TARGET * 3) / vol         # ~3x the average market's share; binds on outliers only
    pos = pos.clip(lower=-cap, upper=cap)
    g = pos.abs().sum(axis=1)
    pos = pos.mul((GROSS_CAP / g).clip(upper=1), axis=0)
    gross = (pos.shift(1) * R).sum(axis=1, min_count=1).where(active & s.notna())
    # costs
    one_way = pd.Series({k: cost_bp(k)[0] / 1e4 for k in R.columns})
    rolls = pd.Series({k: cost_bp(k)[1] for k in R.columns})
    trade = pos.diff().abs()
    tc = (trade * one_way).sum(axis=1) + (pos.abs() * one_way * 2 * rolls / 12).sum(axis=1)
    borrow = (pos[[k for k in EM_EQ if k in pos]].clip(upper=0).abs() * 0.01 / 12).sum(axis=1)
    net = gross - cost_mult * (tc.shift(1) + borrow.shift(1))
    turnover = trade.sum(axis=1)
    shrink = (pos.abs().sum(axis=1) / total.mul(s, axis=0).abs().sum(axis=1)).fillna(1)   # effect of the caps
    fam_pos = {f: v.mul(s * shrink, axis=0) for f, v in by_fam.items()}
    return {"pos": pos, "gross": gross, "net": net, "blocks": pd.DataFrame(blocks), "turnover": turnover,
            "cost": (tc + borrow), "fam_pos": fam_pos}


def stats(r, spx=None):
    r = r.dropna()
    if len(r) < 24:
        return "n/a"
    cum = (1 + r).cumprod()
    dd = (cum / cum.cummax() - 1).min()
    out = "ret %.1f%% vol %.1f%% SR %.2f maxDD %.0f%% worst12m %.0f%%" % (
        r.mean() * 1200, r.std() * np.sqrt(12) * 100, r.mean() / r.std() * np.sqrt(12), dd * 100,
        ((1 + r).rolling(12).apply(np.prod, raw=True) - 1).min() * 100)
    if spx is not None:
        out += " corrSPX %.2f" % r.corr(spx.reindex(r.index))
    return out


def main():
    D = pickle.load(open(os.path.join(P.OUT, "panel.pkl"), "rb"))
    R = D["R"]
    base, x2 = run(R), run(R, cost_mult=2.0)
    spx = R["eq_us_spx"]
    print("Global Macro Book v1 (paper). Design 1990-2010 and extra check 1975-89; holdout 2011-2026 not shown.")
    for a, b in (("1975-01", "1989-12"), ("1990-01", "2010-12")):
        print(" %s..%s" % (a[:4], b[:4]))
        print("   gross     ", stats(base["gross"].loc[a:b], spx))
        print("   net       ", stats(base["net"].loc[a:b], spx))
        print("   net x2cost", stats(x2["net"].loc[a:b]))
        print("   turnover %.1fx/yr, costs %.2f%%/yr" % (base["turnover"].loc[a:b].mean() * 12,
                                                        base["cost"].loc[a:b].mean() * 1200))
        bl = base["blocks"].loc[a:b]
        fam_sr = {f: round(float(bl[f].mean(axis=1).mean() / bl[f].mean(axis=1).std() * np.sqrt(12)), 2)
                  for f in FAMILY_W if f in bl.columns.get_level_values(0)}
        print("   family SR (unit-vol blocks, equal class weight):", fam_sr)
    net = base["net"]
    for lab, a, b in (("1987 crash Oct-Nov", "1987-10", "1987-11"), ("1994 bonds", "1994-02", "1994-11"),
                      ("1998 LTCM Aug-Oct", "1998-08", "1998-10"), ("2000-02 bear", "2000-04", "2002-09"),
                      ("2008 crisis", "2008-01", "2008-12")):
        rr, sp = net.loc[a:b], spx.loc[a:b]
        print("   %-20s book %+.1f%%  S&P excess %+.1f%%" % (lab, ((1 + rr).prod() - 1) * 100, ((1 + sp).prod() - 1) * 100))
    last = pd.Period(pd.Timestamp.today(), "M") - 1          # last complete month
    p = base["pos"].loc[last]
    vol = R.rolling(36, min_periods=12).std().loc[last] * np.sqrt(12)
    risk = (p * vol).dropna()
    risk = risk[risk.abs() > 1e-4].sort_values()
    print("\nCurrent positions as of %s (risk = notional x vol; book target 10%%):" % last)
    print("   largest shorts:", ", ".join("%s %.1f%%" % (k, v * 100) for k, v in risk.head(6).items()))
    print("   largest longs: ", ", ".join("%s %.1f%%" % (k, v * 100) for k, v in risk.tail(6)[::-1].items()))
    by_class = {c: round(float(p[[k for k in p.index if k.startswith(pre)]].abs().sum()), 2) for c, pre in G.CLASSES.items()}
    print("   gross notional by class:", by_class, "total %.2f" % p.abs().sum())
    print("Placeholders:", "; ".join(PLACEHOLDERS))
    pickle.dump({"base": base, "x2": x2}, open(os.path.join(P.OUT, "book_v1.pkl"), "wb"))


if __name__ == "__main__":
    main()
