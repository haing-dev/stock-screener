"""Statistics for the backtest and the forward record (validation/PROTOCOL.md sections 4-6). Pure functions on
the formation and return files, so anyone can recompute every number from the committed raw outputs.
"""
import csv
import io
import math
import zipfile
from itertools import combinations
from statistics import NormalDist

import numpy as np


N01 = NormalDist()
FACTORS = ("Mkt-RF", "SMB", "HML", "RMW", "CMA", "UMD")
MIN_NAMES = 5
MIN_MONTHS = 36
COST_PER_SIDE = 0.005
LISTS = {"P1": "PASS incl. starred, equal-weighted", "P2": "PASS without stars, equal-weighted",
         "P3": "PASS incl. starred, value-weighted", "P4": "near misses, equal-weighted"}
SIC_DIVISIONS = ((1, 9, "A"), (10, 14, "B"), (15, 17, "C"), (20, 39, "D"), (40, 49, "E"), (50, 51, "F"),
                 (52, 59, "G"), (60, 67, "H"), (70, 89, "I"), (90, 99, "J"))


# ------------------------------------------------------------------ factor data (Kenneth French library)
def parse_french(raw_zip_bytes):
    """Monthly rows of a Kenneth French CSV zip -> {'YYYY-MM': {column: decimal}}."""
    z = zipfile.ZipFile(io.BytesIO(raw_zip_bytes))
    text = z.read(z.namelist()[0]).decode("latin-1")
    out, header = {}, None
    for row in csv.reader(io.StringIO(text)):
        cells = [c.strip() for c in row]
        if not cells or not cells[0]:
            if out:
                break           # the monthly block ends at the first blank line after data
            continue
        if cells[0] == "" or not cells[0][0].isdigit():
            if len(cells) > 1 and not out:
                header = cells
            continue
        if len(cells[0]) != 6 or header is None:
            if out:
                break
            continue
        ym = f"{cells[0][:4]}-{cells[0][4:]}"
        rec = {}
        for h, v in zip(header[1:], cells[1:]):
            try:
                rec[h.strip()] = float(v) / 100.0
            except ValueError:
                continue
        out[ym] = rec
    return out


def merge_factors(ff5, mom):
    out = {}
    for ym, r in ff5.items():
        m = mom.get(ym) or {}
        umd = m.get("Mom") if m.get("Mom") is not None else m.get("UMD")
        if umd is None:
            continue
        rr = dict(r)
        rr["UMD"] = umd
        out[ym] = rr
    return out


# ------------------------------------------------------------------ regression with Newey-West errors
def nw_lags(t):
    return int(math.floor(4 * (t / 100.0) ** (2.0 / 9.0)))


def ols_nw(y, X, lags=None):
    """OLS with an intercept; returns (coefs, NW t-stats, n). X: (T, k) array (no constant)."""
    y = np.asarray(y, float)
    X = np.column_stack([np.ones(len(y)), np.asarray(X, float)]) if X is not None and np.size(X) else \
        np.ones((len(y), 1))
    n, k = X.shape
    if n <= k + 1:
        return None, None, n
    XtX_inv = np.linalg.pinv(X.T @ X)
    b = XtX_inv @ X.T @ y
    u = y - X @ b
    L = nw_lags(n) if lags is None else lags
    S = (X * u[:, None]).T @ (X * u[:, None])
    for lag in range(1, L + 1):
        w = 1 - lag / (L + 1)
        G = (X[lag:] * u[lag:, None]).T @ (X[:-lag] * u[:-lag, None])
        S += w * (G + G.T)
    V = XtX_inv @ S @ XtX_inv * n / max(n - k, 1)
    se = np.sqrt(np.maximum(np.diag(V), 1e-30))
    return b, b / se, n


def mean_t(x):
    """Mean and Newey-West t-stat of a series (regression on a constant)."""
    x = np.asarray([v for v in x if v is not None and not math.isnan(v)], float)
    if len(x) < 3:
        return None, None
    b, t, _ = ols_nw(x, None)
    return float(b[0]), float(t[0])


def alpha(series, yms, factors, rf_adjust=True):
    """FF5+UMD alpha of a monthly series. rf_adjust: subtract RF (a long-only portfolio); False for long-short."""
    ys, Xs = [], []
    for r, ym in zip(series, yms):
        f = factors.get(ym)
        if r is None or f is None or any(f.get(k) is None for k in FACTORS):
            continue
        ys.append(r - (f.get("RF", 0.0) if rf_adjust else 0.0))
        Xs.append([f[k] for k in FACTORS])
    if len(ys) < 12:
        return {"alpha": None, "t": None, "n": len(ys)}
    b, t, n = ols_nw(ys, np.array(Xs))
    if b is None:
        return {"alpha": None, "t": None, "n": n}
    return {"alpha": float(b[0]), "t": float(t[0]), "n": n,
            "betas": {k: round(float(v), 3) for k, v in zip(FACTORS, b[1:])}}


# ------------------------------------------------------------------ helpers
def sic_division(sic):
    try:
        s = int(str(sic)[:2])
    except (TypeError, ValueError):
        return "?"
    for lo, hi, lab in SIC_DIVISIONS:
        if lo <= s <= hi:
            return lab
    return "?"


def terciles(vals):
    """{key: 0/1/2} by tercile of value (None -> no key)."""
    items = sorted((v, k) for k, v in vals.items() if v is not None and not math.isnan(v))
    n = len(items)
    return {k: min(2, int(3 * i / n)) for i, (v, k) in enumerate(items)} if n else {}


def spearman(a, b):
    if len(a) < 10:
        return None
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    if ra.std() == 0 or rb.std() == 0:
        return None
    return float(np.corrcoef(ra, rb)[0, 1])


def auc(scores, labels):
    """Mann-Whitney AUC (ties count half); higher score = predicts label 1."""
    pairs = [(s, l) for s, l in zip(scores, labels) if s is not None and not (isinstance(s, float) and math.isnan(s))]
    pos = [s for s, l in pairs if l]
    neg = [s for s, l in pairs if not l]
    if not pos or not neg:
        return None
    allv = sorted(pairs, key=lambda x: x[0])
    i = 0
    vals = [p[0] for p in allv]
    rank_of = []
    while i < len(vals):
        j = i
        while j + 1 < len(vals) and vals[j + 1] == vals[i]:
            j += 1
        r = (i + j) / 2 + 1
        rank_of += [r] * (j - i + 1)
        i = j + 1
    rp = sum(r for r, (s, l) in zip(rank_of, allv) if l)
    return (rp - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))


def sharpe(x):
    x = np.asarray([v for v in x if v is not None], float)
    if len(x) < 3 or x.std(ddof=1) == 0:
        return None
    return float(x.mean() / x.std(ddof=1))


# ------------------------------------------------------------------ deflated Sharpe ratio and PBO
def deflated_sharpe(x, sr_trials):
    """Bailey & Lopez de Prado (2014): probability that the true Sharpe ratio of x exceeds the expected maximum of
    len(sr_trials) unskilled trials. Per-period Sharpe ratios."""
    x = np.asarray([v for v in x if v is not None], float)
    t = len(x)
    srs = [s for s in sr_trials if s is not None]
    if t < 12 or len(srs) < 2 or x.std(ddof=1) == 0:
        return None
    sr = x.mean() / x.std(ddof=1)
    n = len(srs)
    var_sr = float(np.var(srs, ddof=1))
    g = 0.5772156649
    sr0 = math.sqrt(max(var_sr, 1e-12)) * ((1 - g) * N01.inv_cdf(1 - 1.0 / n) + g * N01.inv_cdf(1 - 1.0 / (n * math.e)))
    z = (x - x.mean()) / x.std(ddof=0)
    skew = float((z ** 3).mean())
    kurt = float((z ** 4).mean())
    den = 1 - skew * sr + (kurt - 1) / 4.0 * sr * sr
    if den <= 0:
        return None
    return N01.cdf((sr - sr0) * math.sqrt(t - 1) / math.sqrt(den))


def pbo_cscv(M, blocks=16):
    """Probability of backtest overfitting (Bailey, Borwein, Lopez de Prado & Zhu 2017). M: (T, N) returns of N
    variants. Returns None if too short."""
    M = np.asarray(M, float)
    T, N = M.shape
    if N < 2 or T < blocks * 2:
        return None
    size = T // blocks
    M = M[: size * blocks]
    parts = [M[i * size:(i + 1) * size] for i in range(blocks)]
    lam = []
    for IS in combinations(range(blocks), blocks // 2):
        OS = [i for i in range(blocks) if i not in IS]
        A = np.vstack([parts[i] for i in IS])
        B = np.vstack([parts[i] for i in OS])
        sa = A.mean(0) / np.where(A.std(0, ddof=1) == 0, np.nan, A.std(0, ddof=1))
        sb = B.mean(0) / np.where(B.std(0, ddof=1) == 0, np.nan, B.std(0, ddof=1))
        if np.all(np.isnan(sa)):
            continue
        best = int(np.nanargmax(sa))
        order = np.argsort(np.argsort(np.nan_to_num(sb, nan=-1e9)))
        w = (order[best] + 1) / (N + 1)
        lam.append(math.log(w / (1 - w)))
    return (sum(1 for v in lam if v <= 0) / len(lam)) if lam else None


# ------------------------------------------------------------------ Reality Check / SPA
def stationary_bootstrap_idx(T, B, mean_block, rng):
    p = 1.0 / mean_block
    idx = np.empty((B, T), int)
    start = rng.integers(0, T, B)
    idx[:, 0] = start
    jumps = rng.random((B, T)) < p
    rnd = rng.integers(0, T, (B, T))
    for t in range(1, T):
        idx[:, t] = np.where(jumps[:, t], rnd[:, t], (idx[:, t - 1] + 1) % T)
    return idx


def reality_check(D, B=2000, mean_block=6, seed=7):
    """D: (T, K) excess returns of K strategies over their benchmark. White (2000) Reality Check p-value and
    Hansen (2005) SPA (consistent) p-value for 'no strategy beats its benchmark'."""
    D = np.asarray(D, float)
    T, K = D.shape
    if T < 24 or K < 1:
        return {"rc_p": None, "spa_p": None}
    rng = np.random.default_rng(seed)
    idx = stationary_bootstrap_idx(T, B, mean_block, rng)
    mu = D.mean(0)
    boot = np.stack([D[i].mean(0) for i in idx])          # (B, K)
    rc_stat = math.sqrt(T) * mu.max()
    rc_p = float(np.mean(math.sqrt(T) * (boot - mu).max(1) >= rc_stat))
    sd = np.sqrt(T) * boot.std(0)
    sd = np.where(sd == 0, np.nan, sd)
    thresh = -np.sqrt((sd ** 2) / T * 2 * math.log(math.log(T)))
    mu_c = np.where(mu <= thresh, mu, 0.0)       # only clearly poor strategies keep their (negative) mean
    spa_stat = max(0.0, float(np.nanmax(math.sqrt(T) * mu / sd)))
    # recentred statistic (Hansen's consistent SPA): sqrt(T) * (boot - mu + mu_c) / sd
    spa_boot = np.maximum(0.0, np.nanmax(math.sqrt(T) * (boot - mu + mu_c) / sd, axis=1))
    spa_p = float(np.mean(spa_boot >= spa_stat))
    return {"rc_p": rc_p, "spa_p": spa_p}


# ------------------------------------------------------------------ placebo
def placebo_percentile(months, sims=10000, seed=11):
    """months: [(pick_rets(list), pick_cells(list), cell_members{cell: np.array of returns}, universe_mean)].
    Random portfolios drawing each pick's replacement from the same cell. Returns the percentile (0-1) of the actual
    mean excess return within the simulated distribution."""
    rng = np.random.default_rng(seed)
    sim_sum = np.zeros(sims)
    actual, used = 0.0, 0
    for picks, cells, members, umean in months:
        if not picks:
            continue
        tot = np.zeros(sims)
        for cell in set(cells):
            k = cells.count(cell)
            pool = members.get(cell)
            if pool is None or len(pool) == 0:
                pool = np.array(picks, float)
            draws = rng.integers(0, len(pool), (sims, k))
            tot += pool[draws].sum(1)
        sim_sum += tot / len(picks) - umean
        actual += float(np.mean(picks)) - umean
        used += 1
    if not used:
        return None
    sim = sim_sum / used
    return float(np.mean(sim < actual / used))
