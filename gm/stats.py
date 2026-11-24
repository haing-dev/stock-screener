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


# ------------------------------------------------------------------ gm-2.1.0 test code (E10; TESTING_PROTOCOL 7.7)
SEED = 20261101


def alpha_boot(pod, book, n=10000, block=6, seed=SEED):
    """7.7 T1: intercept of the least-squares regression of the pod's monthly net return on the Core book's monthly net
    return over the common months; one-sided p for H0 alpha <= 0 from the centred stationary bootstrap (whole months,
    mean block 6, 10,000 resamples, seed 20261101, the regression re-fitted in every resample):
    p = share of resamples with (alpha_b - alpha_hat) >= alpha_hat (count / n, as registered).
    A zero Core book (7.6 step 6: "alpha against a zero book (the pod's own mean)"): beta 0, alpha = mean."""
    j = pd.concat([pd.Series(pod), pd.Series(book)], axis=1).dropna()
    T = len(j)
    if T < 24:
        return {"alpha": float("nan"), "beta": float("nan"), "p": 1.0, "count": None, "n": T}
    y, x = j.iloc[:, 0].values.astype(float), j.iloc[:, 1].values.astype(float)
    zero = float(np.var(x)) == 0.0
    idx = _stationary_idx(T, n, block, seed)
    Y = y[idx]
    if zero:
        a, b = float(y.mean()), 0.0
        ab = Y.mean(axis=1)
    else:
        b = float(((x - x.mean()) * (y - y.mean())).mean() / ((x - x.mean()) ** 2).mean())
        a = float(y.mean() - b * x.mean())
        X = x[idx]
        mx, my = X.mean(axis=1), Y.mean(axis=1)
        vx = ((X - mx[:, None]) ** 2).mean(axis=1)
        bb = ((X - mx[:, None]) * (Y - my[:, None])).mean(axis=1) / np.where(vx > 0, vx, np.nan)
        ab = np.where(vx > 0, my - bb * mx, my)
    count = int(np.sum(ab - a >= a))
    return {"alpha": a, "beta": b, "p": count / n, "count": count, "n": T, "resamples": n}


def placebo_perms(T, n=1000, L=12, seed=SEED):
    """7.7 T3 date maps: the T window months cut into L-month blocks from the window's first month (the last
    part-block kept), the blocks in random order; n maps drawn in sequence from numpy default_rng(seed)."""
    rng = np.random.default_rng(seed)
    blocks = [np.arange(i, min(i + L, T)) for i in range(0, T, L)]
    out = np.empty((n, T), dtype=np.int64)
    for i in range(n):
        order = rng.permutation(len(blocks))
        out[i] = np.concatenate([blocks[k] for k in order])
    return out


def move_rows(X, perm, start):
    """Rows of X (a month-indexed frame: scores or rule states) inside the window starting at `start` moved by the
    date map perm, all columns jointly; rows outside the window unchanged."""
    i0 = X.index.get_loc(pd.Period(start, "M"))
    perm = np.asarray(perm)
    if i0 + len(perm) > len(X):
        raise ValueError("placebo window runs past the data")
    out = X.copy()
    out.iloc[i0:i0 + len(perm)] = X.iloc[i0:i0 + len(perm)].values[perm]
    return out


def placebo_p(pod_sr, placebo_srs):
    """7.7 T3: share of placebos with net Sharpe >= the pod's; pass if < 0.05."""
    ps = np.asarray(placebo_srs, float)
    share = float(np.mean(ps >= pod_sr)) if len(ps) else 1.0
    return {"p": share, "pass": share < 0.05, "n": len(ps)}


def placebo_runs(net_fn, window, n=1000, L=12, seed=SEED):
    """Placebo engine for monthly pods and rule states: net_fn(perm) -> the pod's net return series for one date map
    (perm = None gives the pod itself); window = (first, last) month of the pod's window. Returns the pod's Sharpe,
    the placebo Sharpe ratios and the p of placebo_p. Sharpe on the window months only."""
    a, b = pd.Period(window[0], "M"), pd.Period(window[1], "M")
    T = (b - a).n + 1
    sr0 = sharpe(net_fn(None).loc[a:b])
    srs = [sharpe(net_fn(pm).loc[a:b]) for pm in placebo_perms(T, n, L, seed)]
    return {"sr": sr0, "placebo_sr": srs, **placebo_p(sr0, srs)}


def move_windows(windows, days, scope, rng, horizon=None):
    """7.7 T3, card 4 R1-R4: each window (entry day, length in NYSE days) moved to a random start drawn uniformly among
    the NYSE days of the same calendar year (scope 'year', R1 and R3) or month ('month', R2 and R4) as its entry, same
    length in trading days; a window that would run past the horizon (seal) ends at the horizon. Returns a list of
    (new entry day, new exit day). The caller re-reads the gates at the new dates."""
    days = pd.DatetimeIndex(days)
    out = []
    for entry, length in windows:
        e = pd.Timestamp(entry)
        key = days.year == e.year if scope == "year" else (days.year == e.year) & (days.month == e.month)
        cand = np.flatnonzero(key)
        i = int(cand[rng.integers(len(cand))])
        j = i + int(length)
        last = len(days) - 1 if horizon is None else int(np.searchsorted(days.values, np.datetime64(pd.Timestamp(horizon)),
                                                                         side="right")) - 1
        out.append((days[i], days[min(j, last)]))
    return out


def rescale(r, target=0.10, window=36, minp=24):
    """The book scaler's convention: r x target / (trailing realised volatility x sqrt(12)), lagged one month."""
    return r * (target / (r.rolling(window, min_periods=minp).std() * np.sqrt(12))).shift(1)


def combined_book(core, pod, lam=0.5, target=0.10):
    """7.7 held size: Core book + pod at lambda x the book's volatility (both series at 10%), rescaled to 10% by its
    trailing 36-month realised volatility, lagged one month."""
    j = pd.concat([core, pod], axis=1).dropna()
    return rescale(j.iloc[:, 0] + lam * j.iloc[:, 1], target)


def tail_test(inc, cha, max_dd_worse=0.02, worst_month_worse=0.01):
    """Test 5 (gm.protocol.decide check 5): on common months, the challenger's maximum fall is not worse by more than 2
    points and its worst month not worse by more than 1 point."""
    j = pd.concat([inc, cha], axis=1).dropna()
    di, dc = maxdd(j.iloc[:, 0]), maxdd(j.iloc[:, 1])
    wi, wc = float(j.iloc[:, 0].min()), float(j.iloc[:, 1].min())
    return {"dd_inc": di, "dd_cha": dc, "wm_inc": wi, "wm_cha": wc, "n": len(j),
            "pass": bool(dc >= di - max_dd_worse and wc >= wi - worst_month_worse)}


def t4_tail(core, pod, lam=0.5):
    """7.7 T4: test 5 on the combined book against the Core book alone (taken as run), common months."""
    c = combined_book(core, pod, lam)
    j = pd.concat([core, c], axis=1).dropna()
    return tail_test(j.iloc[:, 0], j.iloc[:, 1])


def noninferiority(inc, cha, inc2x=None, cha2x=None, target_ok=None, margin=-0.10):
    """7.7 H1-H4 for hygiene items (A2, A3). H1: one-sided 95% lower bound of dSR (paired_sr_test, pooled common
    window) > margin; H2: dSR at twice the costs (reported); H3: test 5 between the two books; H4 (A3 only): the
    item's own target, point estimate, passed in as target_ok. Pass = H1 and H3 (and H4 when given)."""
    j = pd.concat([inc, cha], axis=1).dropna()
    t = paired_sr_test(j.iloc[:, 0], j.iloc[:, 1])
    h1 = bool(t.get("identical", False) or t["lb95"] > margin)
    h3 = tail_test(j.iloc[:, 0], j.iloc[:, 1])
    out = {"dsr": t["dsr"], "lb95": t["lb95"], "H1": h1, "H3": h3["pass"], "tail": h3, "n": len(j)}
    if inc2x is not None and cha2x is not None:
        j2 = pd.concat([inc2x, cha2x], axis=1).dropna()
        out["H2_dsr_2x"] = sharpe(j2.iloc[:, 1]) - sharpe(j2.iloc[:, 0])
    if target_ok is not None:
        out["H4"] = bool(target_ok)
    out["pass"] = h1 and h3["pass"] and (target_ok is None or bool(target_ok))
    return out
