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


# ------------------------------------------------------------------ adoption protocol (TESTING_PROTOCOL.md)
def _stationary_idx(T, n, block, seed):
    """n x T index matrix of a stationary (Politis-Romano) bootstrap with mean block length `block`."""
    rng = np.random.default_rng(seed)
    idx = np.empty((n, T), dtype=np.int64)
    idx[:, 0] = rng.integers(T, size=n)
    jump = rng.random((n, T)) < 1.0 / block
    fresh = rng.integers(T, size=(n, T))
    for t in range(1, T):
        idx[:, t] = np.where(jump[:, t], fresh[:, t], (idx[:, t - 1] + 1) % T)
    return idx


def _sr_rows(X):
    return X.mean(axis=1) / X.std(axis=1, ddof=1) * np.sqrt(12)


def paired_sr_test(rb, rc, n=10000, block=6, seed=20261101):
    """Sharpe difference challenger minus incumbent on common months, with a paired stationary bootstrap.
    Returns dSR, one-sided p for H0 dSR <= 0 (centred bootstrap), and the one-sided 95% lower bound."""
    j = pd.concat([rb, rc], axis=1).dropna()
    if len(j) < 24:
        return {"dsr": float("nan"), "p": 1.0, "lb95": float("nan"), "n": len(j)}
    b, c = j.iloc[:, 0].values, j.iloc[:, 1].values
    d = sharpe(j.iloc[:, 1]) - sharpe(j.iloc[:, 0])
    if np.max(np.abs(b - c)) < 1e-10:
        return {"dsr": 0.0, "p": 1.0, "lb95": 0.0, "n": len(j), "identical": True}
    idx = _stationary_idx(len(j), n, block, seed)
    ds = _sr_rows(c[idx]) - _sr_rows(b[idx])
    p = float((np.sum(ds - d >= d) + 1) / (n + 1))
    lb = float(d - np.percentile(ds - d, 95))
    return {"dsr": float(d), "p": p, "lb95": lb, "n": len(j), "se": float(ds.std())}


def holm(pvals):
    """Holm step-down adjusted p-values (dict in, dict out)."""
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m, out, run = len(items), {}, 0.0
    for i, (k, p) in enumerate(items):
        run = max(run, min(1.0, (m - i) * p))
        out[k] = run
    return out


def nw_alpha_t(y, x, lags=6):
    """Newey-West t-stat of the intercept of y on x (monthly)."""
    j = pd.concat([y, x], axis=1).dropna()
    if len(j) < 36:
        return float("nan")
    Y = j.iloc[:, 0].values
    X = np.column_stack([np.ones(len(j)), j.iloc[:, 1:].values])
    beta = np.linalg.lstsq(X, Y, rcond=None)[0]
    u = Y - X @ beta
    Xu = X * u[:, None]
    S = Xu.T @ Xu
    for L in range(1, lags + 1):
        w = 1 - L / (lags + 1)
        G = Xu[L:].T @ Xu[:-L]
        S += w * (G + G.T)
    XtXi = np.linalg.inv(X.T @ X)
    V = XtXi @ S @ XtXi
    return float(beta[0] / np.sqrt(V[0, 0]))


def lo_sharpe(r, q=12):
    """Lo (2002) annualised Sharpe corrected for autocorrelation of monthly returns."""
    x = r.dropna()
    if len(x) < 36:
        return float("nan")
    rho = [x.autocorr(k) for k in range(1, q)]
    eta = q / np.sqrt(q + 2 * sum((q - k) * rho[k - 1] for k in range(1, q)))
    return float(x.mean() / x.std() * eta)


def smile(r, mkt, n=5):
    """Mean monthly return (annualised %) of r in n equal-count states of the market return."""
    j = pd.concat([r, mkt], axis=1).dropna()
    q = pd.qcut(j.iloc[:, 1], n, labels=False)
    return {int(k) + 1: round(float(v * 1200), 1) for k, v in j.iloc[:, 0].groupby(q).mean().items()}
