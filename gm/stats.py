"""Statistics for design-period evaluation. Nothing here ever reads the holdout: every function takes a period and
callers pass design periods only (1975-89, 1990-2010). HOLDOUT_START guards it."""
import math

import numpy as np
import pandas as pd

HOLDOUT_START = pd.Period("2011-01", "M")
DESIGN = ("1990-01", "2010-12")
EXTRA = ("1975-01", "1989-12")


def cut(r, a, b):
    b = min(pd.Period(b, "M"), HOLDOUT_START - 1)
    return r.loc[pd.Period(a, "M"):b].dropna()


def sharpe(r):
    r = r.dropna()
    return float(r.mean() / r.std() * np.sqrt(12)) if len(r) > 12 and r.std() > 0 else float("nan")


def tstat(r):
    r = r.dropna()
    return float(r.mean() / r.std() * np.sqrt(len(r))) if len(r) > 12 else float("nan")


def maxdd(r):
    c = (1 + r.dropna()).cumprod()
    return float((c / c.cummax() - 1).min()) if len(c) else float("nan")


def summary(r, a=DESIGN[0], b=DESIGN[1]):
    x = cut(r, a, b)
    return {"sr": sharpe(x), "t": tstat(x), "ret": float(x.mean() * 12), "vol": float(x.std() * np.sqrt(12)),
            "maxdd": maxdd(x), "skew": float(x.skew()), "n": len(x)}


def decades(r, edges=("1975", "1985", "1995", "2005", "2011")):
    out = {}
    for a, b in zip(edges[:-1], edges[1:]):
        x = cut(r, a + "-01", str(int(b) - 1) + "-12")
        out["%s-%s" % (a, int(b) - 1)] = round(sharpe(x), 2) if len(x) > 24 else None
    return out


def bootstrap_sr(r, n=2000, block=6, seed=7):
    """Stationary block bootstrap 90% interval of the annual Sharpe ratio."""
    x = r.dropna().values
    if len(x) < 36:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    T, srs = len(x), []
    for _ in range(n):
        idx, i = [], rng.integers(T)
        while len(idx) < T:
            idx.append(i)
            i = rng.integers(T) if rng.random() < 1 / block else (i + 1) % T
        s = x[idx]
        srs.append(s.mean() / s.std() * np.sqrt(12))
    return (float(np.percentile(srs, 5)), float(np.percentile(srs, 95)))


def _norm_ppf(p):
    # Acklam's approximation (no scipy dependency)
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02, 1.383577518672690e+02,
         -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02, 6.680131188771972e+01,
         -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00, -2.549732539343734e+00,
         4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00, 3.754408661907416e+00]
    pl, ph = 0.02425, 1 - 0.02425
    if p < pl:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / \
            ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    if p > ph:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / \
            ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    q = p - 0.5
    r = q * q
    return (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / \
        (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1)


def _norm_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def deflated_sr(r, n_trials, trial_srs_annual):
    """Bailey & Lopez de Prado deflated Sharpe ratio: probability that the true Sharpe exceeds the best Sharpe
    expected from n_trials unskilled trials, given the spread of the trial Sharpe ratios. Monthly returns."""
    x = r.dropna()
    T = len(x)
    sr = x.mean() / x.std()
    g3, g4 = float(x.skew()), float(x.kurt() + 3)
    v = np.var(np.asarray(trial_srs_annual, float) / np.sqrt(12)) if len(trial_srs_annual) > 1 else 0.0
    e = 0.5772156649
    N = max(int(n_trials), 2)
    sr0 = math.sqrt(v) * ((1 - e) * _norm_ppf(1 - 1 / N) + e * _norm_ppf(1 - 1 / (N * math.e)))
    z = (sr - sr0) * math.sqrt(T - 1) / math.sqrt(max(1 - g3 * sr + (g4 - 1) / 4 * sr ** 2, 1e-9))
    return {"dsr": _norm_cdf(z), "sr0_annual": sr0 * math.sqrt(12), "n_trials": N}


def marginal(blocks, fam):
    """Alpha t-stat of one family's book return regressed on the other families (does it add anything?)."""
    y = blocks[fam]
    X = blocks.drop(columns=[fam])
    j = pd.concat([y, X], axis=1).dropna()
    if len(j) < 60:
        return float("nan")
    A = np.column_stack([np.ones(len(j)), j.iloc[:, 1:].values])
    beta, res, *_ = np.linalg.lstsq(A, j.iloc[:, 0].values, rcond=None)
    resid = j.iloc[:, 0].values - A @ beta
    se = np.sqrt(np.sum(resid ** 2) / (len(j) - A.shape[1]) * np.linalg.inv(A.T @ A)[0, 0])
    return float(beta[0] / se)
