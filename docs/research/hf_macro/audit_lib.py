"""Audit helpers: reproduce candidate 5.0 (robust5.cand) with swappable inputs, without touching the author's files.
Imports exp_combo (prints silenced) to reuse its exact signals, then re-implements run/build/cand with an
explicit returns panel so individual inputs can be replaced."""
import contextlib
import io
import math
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import exp_combo as X   # noqa  (runs the 300-variant grid once; ~12 s)

grid, R0, S, rf, P, T = X.grid, X.R.copy(), X.S, X.rf, X.P, X.T
sc, F, ind = X.sc, X.F, X.ind
Per = X.Per
COST, FEE = X.COST, X.FEE


def run(W, Rm=None, cost=COST, drift_cost=False):
    """Copy of lab.run with an explicit returns panel; optional cost on drift rebalancing."""
    Rm = R0 if Rm is None else Rm
    W = W.reindex(grid).fillna(0.0)
    A = Rm.reindex(columns=[c for c in W.columns if c != "tbill"]).copy()
    for c, f in FEE.items():
        if c in A:
            A[c] = A[c] - f
    Wh = W.shift(1).fillna(0.0)
    miss = A.isna() & (Wh[A.columns] != 0)
    r = (Wh[A.columns] * A.fillna(0)).sum(axis=1) + (1 - Wh.sum(axis=1)) * rf
    r[miss.any(axis=1)] = np.nan
    turn = W.diff().abs().sum(axis=1).shift(1).fillna(0)
    if drift_cost:
        # weights after the month's returns drift away from target; rebalancing back costs too
        gross = Wh[A.columns] * (1 + A.fillna(0))
        cash = (1 - Wh.sum(axis=1)) * (1 + rf)
        tot = gross.sum(axis=1) + cash
        drifted = gross.div(tot, axis=0)
        tgt = W[A.columns]
        turn = (tgt - drifted).abs().sum(axis=1).shift(1).fillna(0)   # trade at end of month t+1 -> charged next
    return r - cost * turn


def stats(r, a="1975-02", b="2026-10"):
    return X.stats(r, a, b)


def line(nm, r, wins=(("1975-02", "2000-12"), ("2001-01", "2026-10"), ("1975-02", "2026-10"))):
    out = []
    for a, b in wins:
        s = stats(r, a, b)
        out.append(f"{s['cagr']:5.1f}% {s['dd']:4.0f}% {s['sh']:4.2f}")
    return f"{nm[:58]:<58} " + " | ".join(out)


def lvl(r):
    return (1 + r.fillna(0)).cumprod()


def above_ma_r(r, n=10):
    lv_ = lvl(r).where(r.notna().cummax())
    return (lv_ > lv_.rolling(n, min_periods=n).mean()).fillna(False)


def build(e, d, x, l="L4", DW=None):
    """Same as exp_combo.build for L0/L4."""
    DW = X.DW if DW is None else DW
    W = pd.DataFrame(0.0, index=grid, columns=["spx"])
    xs = sum((v.astype(float) for v in x.values()), pd.Series(0.0, index=grid)) if x else pd.Series(0.0, index=grid)
    eq = e * (1 - xs)
    rest = (1 - e) * (1 - xs)
    for a, w in d.items():
        W[a] = W.get(a, 0.0) + rest * w.astype(float)
    for a, w in x.items():
        W[a] = W.get(a, 0.0) + w.astype(float)
    W["spx"] = eq
    if l == "L4":
        full = (e > 1 - 1e-9).astype(float) * eq
        for c in DW.columns:
            W["sec_" + c] = DW[c] * full
    return W


def cand(Rm=None, sq=80, mu=(0.25, 1.5), cpi_th=3.0, xs=0.1, l="L4", d="D7", cost=COST, gold_up=None, com_up=None,
         e_base=None, squeeze_sc=None, cpi_yy=None, gs10=None, curve_ok=None, g_l=None, DW=None, drift_cost=False,
         use_sq=True, use_mu=True):
    Rm = R0 if Rm is None else Rm
    gs10 = X.gs10 if gs10 is None else gs10
    e_base = X.e41 if e_base is None else e_base
    ssc = sc["squeeze"] if squeeze_sc is None else squeeze_sc
    sqc = (ssc >= sq).fillna(False) if use_sq else pd.Series(False, index=grid)
    spx_l = lvl(Rm["spx"])
    muc = (((spx_l / spx_l.shift(12) - 1) > mu[0]) & ((gs10 - gs10.shift(12)) > mu[1])).fillna(False) if use_mu \
        else pd.Series(False, index=grid)
    e = np.minimum(e_base, pd.Series(np.where(sqc | muc, 0.0, 1.0), index=grid))
    cy = X.cpi_yy if cpi_yy is None else cpi_yy
    h = (cy > cpi_th).fillna(False)
    gu = X.gold_up if gold_up is None else gold_up
    cu = X.com_up if com_up is None else com_up
    x = {"gold": xs * (h & gu), "commod": xs * (h & cu)} if xs else {}
    gl = X.g_l if g_l is None else g_l
    co = X.curve_ok if curve_ok is None else curve_ok
    D = {"D0": {"t30y": gl}, "D7": {"t30y": gl & co}}[d]
    W = build(e, D, x, l, DW)
    return run(W, Rm, cost, drift_cost), e, W


def live(Rm=None, cost=COST, g_l=None, e_base=None):
    gl = X.g_l if g_l is None else g_l
    e = X.e41 if e_base is None else e_base
    return run(X.W_from(e, {"t30y": gl}), Rm, cost)


# --------------------------------------------------------------- exact par-bond return from month-end yields
def par_bond_ret(y_prev, y_now, n_years):
    """Total return over one month of a par bond bought at end of t-1 (coupon = y_prev, semiannual, maturity n_years),
    priced at end of t at yield y_now with maturity n_years - 1/12. Yields in percent."""
    c = y_prev / 100.0
    yn = y_now / 100.0
    m = n_years - 1.0 / 12
    k = np.floor(m * 2)                      # whole coupon periods left
    frac = m * 2 - k                          # fraction of a period to next coupon
    # dirty price at end of month: PV of remaining coupons + principal
    def pv(yv, cv):
        h = yv / 2
        n = k + 1                             # number of coupons remaining (next one in `frac` periods)
        ann = np.where(np.abs(h) < 1e-12, n, (1 - (1 + h) ** (-n)) / np.where(np.abs(h) < 1e-12, 1, h))
        price = (cv / 2 * ann + (1 + h) ** (-n)) * (1 + h) ** (1 - frac)
        return price
    p1 = pv(yn, c)
    return pd.Series(p1 - 1.0, index=y_prev.index) if isinstance(y_prev, pd.Series) else p1 - 1.0
