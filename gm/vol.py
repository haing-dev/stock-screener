"""Volatility estimates per market, known at each month end (annualised).

m36    : 36-month std of monthly returns (gm-1.x).
hybrid : fast_w x fast + (1 - fast_w) x slow, floored at floor x slow.
         fast = EWMA of daily squared returns (half-life hl_days) where free daily data exist (gm/daily.py),
                else EWMA of monthly squared returns (half-life hl_months);
         slow = 10-year estimate (120 months of monthly returns, min 36).
Why: last month's vol predicts next month's far better than a 3-year average (Carver: R2 about 0.35), but a pure
fast estimate over-sizes calm, policy-pinned markets (JGBs) and cuts winners on every spike; the blend and the floor
keep both (Quantica: dynamic sizing = higher Sharpe, static = more convexity).
"""
import numpy as np
import pandas as pd


def m36(R):
    return R.rolling(36, min_periods=12).std() * np.sqrt(12)


def slow(R):
    return R.rolling(120, min_periods=36).std() * np.sqrt(12)


def monthly_ewma(R, hl):
    return (R ** 2).ewm(halflife=hl, min_periods=12).mean() ** 0.5 * np.sqrt(12)


def daily_ewma(D, hl, grid, sample_days=None):
    """D: daily log returns (DatetimeIndex) -> month-end EWMA vol on the monthly grid.
    sample_days (E8, gm-2.1.0, weekly tranches): a Series label -> day; the value at label t is then the EWMA at the
    last daily row at or before that day (no value where the day is missing). None = today's month-end sampling."""
    if D is None or D.empty:
        return pd.DataFrame(index=grid)
    D = D.where(D.abs() < 0.25)
    e = (D ** 2).ewm(halflife=hl, min_periods=40).mean() ** 0.5 * np.sqrt(252)
    if sample_days is not None:
        return sample_at(e, sample_days, grid)
    m = e.groupby(e.index.to_period("M")).last()
    return m.reindex(grid)


def sample_at(e, sample_days, grid):
    """Rows of a daily frame at the last row at or before each label's day (label -> day Series) on the grid."""
    sd = sample_days.reindex(grid)
    out = pd.DataFrame(np.nan, index=grid, columns=e.columns)
    ok = sd.notna().values
    if ok.any() and len(e):
        pos = np.searchsorted(e.index.values, pd.DatetimeIndex(sd[ok]).values, side="right") - 1
        good = pos >= 0
        vals = np.full((ok.sum(), e.shape[1]), np.nan)
        vals[good] = e.values[pos[good]]
        out.loc[sd.index[ok]] = vals
    return out


def estimate(R, cfg, daily=None, sample_days=None):
    """sample_days (E8, gm-2.1.0): see daily_ewma; None = today's month-end form."""
    v = cfg.get("vol", {})
    if v.get("model", "m36") == "m36":
        return m36(R)
    lt = slow(R)
    fast = monthly_ewma(R, v.get("hl_months", 6))
    if daily is not None and not daily.empty:
        dv = daily_ewma(daily, v.get("hl_days", 35), R.index) if sample_days is None else \
            daily_ewma(daily, v.get("hl_days", 35), R.index, sample_days)
        cols = [c for c in dv.columns if c in fast.columns]
        fast[cols] = dv[cols].combine_first(fast[cols])
    w = v.get("fast_w", 0.7)
    blend = (w * fast + (1 - w) * lt).combine_first(fast)
    floor = v.get("floor", 0.75) * lt
    out = np.maximum(blend, floor.fillna(0)).where(blend.notna())
    return out.combine_first(m36(R))
