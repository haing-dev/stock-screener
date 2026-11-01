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


def daily_ewma(D, hl, grid):
    """D: daily log returns (DatetimeIndex) -> month-end EWMA vol on the monthly grid."""
    if D is None or D.empty:
        return pd.DataFrame(index=grid)
    D = D.where(D.abs() < 0.25)
    e = (D ** 2).ewm(halflife=hl, min_periods=40).mean() ** 0.5 * np.sqrt(252)
    m = e.groupby(e.index.to_period("M")).last()
    return m.reindex(grid)


def estimate(R, cfg, daily=None):
    v = cfg.get("vol", {})
    if v.get("model", "m36") == "m36":
        return m36(R)
    lt = slow(R)
    fast = monthly_ewma(R, v.get("hl_months", 6))
    if daily is not None and not daily.empty:
        dv = daily_ewma(daily, v.get("hl_days", 35), R.index)
        cols = [c for c in dv.columns if c in fast.columns]
        fast[cols] = dv[cols].combine_first(fast[cols])
    w = v.get("fast_w", 0.7)
    blend = (w * fast + (1 - w) * lt).combine_first(fast)
    floor = v.get("floor", 0.75) * lt
    out = np.maximum(blend, floor.fillna(0)).where(blend.notna())
    return out.combine_first(m36(R))
