"""Shared signals + the live 4.1 rule, in lab terms."""
import numpy as np
import pandas as pd

from lab import *  # noqa

ind, sc, F = P["ind"], P["sc"], P["F"]
share = P["share"]
lo, hi = 0.15, 0.35
ff = F["FEDFUNDS"]
fed = ((ff - ff.rolling(24, min_periods=12).min()) >= 1.0).fillna(False)
unr = F["UNRATE"]
trend_dn = (ind["spx_trend"] < 0).fillna(False)
unr_up = (unr > unr.rolling(12).mean()).fillna(False)
gtt = (trend_dn & unr_up)
cneg = (ind["stockbond"] < 0).fillna(False)
I = ((share - lo) / (hi - lo)).clip(0, 1)


def exposure(gate=fed, extra=None, floor=0.0):
    e = 1 - (1 - floor) * I * gate.astype(float)
    e = np.minimum(e, pd.Series(np.where(gtt, floor, 1.0), index=grid))
    if extra is not None:
        e = np.minimum(e, pd.Series(np.where(extra, floor, 1.0), index=grid))
    return pd.Series(e, index=grid).fillna(1.0)


e41 = exposure()
cpi = S["fred_CPIAUCNS"]
cpi_yy = (cpi / cpi.shift(12) - 1).shift(1) * 100            # published with a 1-month lag
gs10 = F["GS10"]
curve_ok = (gs10 >= ff).fillna(False)
squeeze = (sc["squeeze"] >= 80).fillna(False)


def W_from(e, defensive):
    """defensive: dict asset -> weight share (Series or float) of the non-stock part; rest = cash."""
    W = pd.DataFrame(0.0, index=grid, columns=["spx"])
    W["spx"] = e
    rest = 1 - e
    for a, w in defensive.items():
        W[a] = rest * (w.astype(float) if isinstance(w, pd.Series) else w)
    return W


live_def = {"t30y": (gtt & cneg)}
W41 = W_from(e41, live_def)


# ---------------- own trend sleeve from tradeable assets (12-month excess-return sign, inverse-vol weights)
_q = R["aqr_equity_indices_market"]
R["intl_eq"] = _q.where(grid <= _q.last_valid_index(), R["eq_eafe"])     # global equity futures, then EFA after its end
TREND_ASSETS = ["spx", "intl_eq", "t10y", "t30y", "gold", "commod"]


def trend_sleeve(assets=TREND_ASSETS, n=12, long_only=True, vol_n=12):
    lv = {a: lvl(R[a]).where(R[a].notna().cummax()) for a in assets}
    ex = pd.DataFrame({a: (R[a] - rf) for a in assets})
    exl = (1 + ex.fillna(0)).cumprod().where(ex.notna().cummax())
    sig = np.sign(exl / exl.shift(n) - 1)
    if long_only:
        sig = sig.clip(lower=0)
    vol = ex.rolling(vol_n, min_periods=6).std()
    w = sig / vol
    w = w.div((1 / vol).where(sig.notna()).sum(axis=1), axis=0)        # weights sum to 1 if all long
    r = (w.shift(1) * pd.DataFrame({a: R[a] for a in assets})).sum(axis=1) + (1 - w.shift(1).sum(axis=1)) * rf
    r[w.shift(1).isna().all(axis=1)] = np.nan
    turn = w.diff().abs().sum(axis=1).shift(1).fillna(0)
    return r - 0.001 * turn


R["trend_lo"] = trend_sleeve()
R["trend_ls"] = trend_sleeve(long_only=False)
