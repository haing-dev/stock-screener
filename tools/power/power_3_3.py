"""WORKFLOW step 3.3: power check of the test sheet on SYNTHETIC returns only.

python3 power_3_3.py [--reps N] [--part all|calib|validate|cells|batch|hygiene|holdout|robust] [--quick]

Nothing here reads market data. Every series is simulated; the only real-data facts used are the design-era book facts
(1975-2010) quoted in POWER_3.3.md section 2, which fix the generator's parameters. The registered statistics are
imported from the repo (gm/stats.py: _stationary_idx, paired_sr_test, holm, sharpe, maxdd; gm/protocol.py: decide and
its constants; gm/audit.py: holdout_power) and the vectorised versions below are checked against them (part validate).
Deterministic: every random draw comes from a numpy Generator seeded from the cell name and a fixed master seed.
"""
import argparse
import hashlib
import json
import os
import sys
import time

import numpy as np
import pandas as pd

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, REPO)
from gm import audit as AU      # noqa: E402
from gm import protocol as PR   # noqa: E402
from gm import stats as ST      # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(REPO, "docs", "research", "power")   # results folder
RAW = os.path.join(OUT, "csv")
os.makedirs(RAW, exist_ok=True)

MASTER = 3303
VOL = 0.10                                      # book and pod volatility (10% target)
MV = VOL / np.sqrt(12)
NB, BLK, BSEED = 10000, 6, 20261101             # registered bootstrap (TESTING_PROTOCOL test 1; gm/stats.py)
T_FULL, ERA_SPLIT = 432, 180                    # 1975-01..2010-12; era 1 = 1975-89 (180 months)
GEN = dict(df=5, a=0.05, b=0.90, ar=0.10)       # book generator, calibrated in part calib
LAMBDA = 0.5                                    # held size: pod risk = one of four equal independent pods
N_PLACEBO, PL_BLOCK = int(os.environ.get("NPL", 200)), 12                   # placebo shuffles per simulated pod; block length (months)
CHUNK = 250


def rng_for(name):
    h = int(hashlib.sha256(("%d|%s" % (MASTER, name)).encode()).hexdigest()[:12], 16)
    return np.random.default_rng(h)


# ------------------------------------------------------------------------------------------------- generators
def garch_t(rng, shape, T, df=GEN["df"], a=GEN["a"], b=GEN["b"], ar=0.0, burn=100):
    """GARCH(1,1) with Student-t(df) innovations, unconditional variance 1; optional AR(1) filter keeping var 1."""
    if df is None:
        z = rng.standard_normal(shape + (T + burn,))
    else:
        z = rng.standard_t(df, size=shape + (T + burn,)) / np.sqrt(df / (df - 2.0))
    if a == 0 and b == 0:
        out = z[..., burn:]
    else:
        w = 1.0 - a - b
        h = np.ones(shape)
        e_prev = np.zeros(shape)
        out = np.empty(shape + (T + burn,))
        for t in range(T + burn):
            h = w + a * e_prev ** 2 + b * h
            e = np.sqrt(h) * z[..., t]
            out[..., t] = e
            e_prev = e
        out = out[..., burn:]
    if ar:
        y = np.empty_like(out)
        y[..., 0] = out[..., 0]
        k = np.sqrt(1 - ar * ar)
        for t in range(1, T):
            y[..., t] = ar * y[..., t - 1] + k * out[..., t]
        out = y
    return out


def ar1_gauss(rng, shape, T, phi):
    e = rng.standard_normal(shape + (T,))
    s = np.empty_like(e)
    s[..., 0] = e[..., 0]
    k = np.sqrt(1 - phi * phi)
    for t in range(1, T):
        s[..., t] = phi * s[..., t - 1] + k * e[..., t]
    return s


def markov_on(rng, R, T, q, L):
    """0/1 state, stationary share q, mean on-spell length L months."""
    p10 = 1.0 / L
    p01 = q * p10 / (1 - q)
    on = np.empty((R, T))
    st = (rng.random(R) < q).astype(float)
    u = rng.random((R, T))
    for t in range(T):
        on[:, t] = st
        st = np.where(st == 1, (u[:, t] >= p10).astype(float), (u[:, t] < p01).astype(float))
    return on


def sys_moments(m, g, b):
    """Per-market mean and variance of r = s (m + g s + e), s ~ N(b,1), e unit var independent."""
    E2, E3, E4 = 1 + b * b, b ** 3 + 3 * b, b ** 4 + 6 * b * b + 3
    mu = m * b + g * E2
    ex2 = m * m * E2 + 2 * m * g * E3 + g * g * E4 + E2
    return mu, ex2 - mu * mu


def solve_sys(G, K, mode):
    """Parameters (m, gamma, b) giving a K-market pod gross annual Sharpe G."""
    target = G / np.sqrt(12 * K)
    if abs(target) < 1e-12:
        return 0.0, 0.0, (1.0 if mode == "static" else 0.5 if mode == "mixed" else 0.0)
    if mode == "timing":
        return 0.0, target / np.sqrt(1 - 2 * target ** 2), 0.0
    if mode == "static":
        return target * np.sqrt(2 / (1 - target ** 2)), 0.0, 1.0
    b = 0.5                                       # mixed: half of the mean from the standing exposure
    lo, hi = 0.0, 1.0
    for _ in range(80):
        gm = (lo + hi) / 2
        m = gm * (1 + b * b) / b
        mu, v = sys_moments(m, gm, b)
        lo, hi = (gm, hi) if mu / np.sqrt(v) < target else (lo, gm)
    gm = (lo + hi) / 2
    return gm * (1 + b * b) / b, gm, b


def block_perm(rng, T, L=PL_BLOCK, kind="block"):
    """Placebo date map. block: blocks of L months in random order. rot: rotate each 12-month block by a random
    offset (window moved to a random start inside its own year; card 4 proposal)."""
    blocks = [np.arange(i, min(i + L, T)) for i in range(0, T, L)]
    if kind == "rot":
        return np.concatenate([np.roll(bk, rng.integers(len(bk))) for bk in blocks])
    order = rng.permutation(len(blocks))
    return np.concatenate([blocks[i] for i in order])


# ------------------------------------------------------------------------------------------------- pods
def make_pod(spec, R, rng):
    """Returns dict with net, net2x (R x Tw), placebo closure, population mean and sd of the net all-month return,
    and z (standardised gross, for the book's correlation)."""
    kind, Tw = spec["kind"], spec["Tw"]
    c = spec.get("cost", 0.1)
    if kind == "sys":
        K, phi, S, mode = spec.get("K", 8), spec.get("phi", 0.9), spec["S"], spec.get("mode", "timing")
        G = S + c
        m, g, b = solve_sys(G, K, mode)
        s = ar1_gauss(rng, (R, K), Tw, phi) + b
        e = garch_t(rng, (R, K), Tw)
        x = m + g * s + e
        mu1, v1 = sys_moments(m, g, b)
        sd = np.sqrt(v1 / K)
        scale = MV / sd
        gross = (s * x).mean(1) * scale
        cm = c * VOL / 12
        net = gross - cm
        z = (gross - mu1 * scale) / MV
        pop_mu, pop_sd = S * VOL / 12, MV

        def placebo(perms):
            out = np.empty((len(perms), R))
            for i, p in enumerate(perms):
                rr = (s[:, :, p] * x).mean(1) * scale - cm
                out[i] = rr.mean(1) / rr.std(1, ddof=1)
            return out * np.sqrt(12)
        res = dict(net=net, net2x=net - cm, placebo=placebo, pop_mu=pop_mu, pop_sd=pop_sd, z=z)
    else:                                          # rule layer: intermittent, flat when off
        q, L = spec["q"], spec.get("L", 12)
        if kind == "cal":                          # calendar rule: on in the last 2 months of each 12
            on = np.tile((np.arange(Tw) % 12 >= 10).astype(float), (R, 1))
            q = 2 / 12
        else:
            on = markov_on(rng, R, Tw, q, L)
        if "S_on" in spec:
            mu = spec["S_on"] / np.sqrt(12)
        else:
            s_ = spec["S"] / np.sqrt(12)
            mu = s_ / np.sqrt(q - s_ * s_ * (1 - q)) if s_ != 0 else 0.0
        mug = mu + c / np.sqrt(12)
        mode = spec.get("mode", "timing")
        prem = spec.get("prem", None)
        if mode == "timing":
            m, g = 0.0, mug
        elif mode == "premium":
            m, g = mug, 0.0
        else:
            m, g = mug / 2, mug / 2
        if prem is not None:                       # fixed market premium (Sharpe) in the traded direction
            m = prem / np.sqrt(12)
            g = mug - m
        e = garch_t(rng, (R,), Tw)
        x = m + g * on + e
        cm = c * VOL / 12
        gross = on * x * MV
        net = gross - cm * on
        mu_all = q * mu
        var_all = q * (mu * mu + 1) - q * q * mu * mu
        pop_mu, pop_sd = mu_all * MV, np.sqrt(var_all) * MV
        mug_all = q * mug
        z = (gross - mug_all * MV) / pop_sd

        def placebo(perms):
            out = np.empty((len(perms), R))
            for i, p in enumerate(perms):
                o = on[:, p]
                rr = o * x * MV - cm * o
                sd = rr.std(1, ddof=1)
                out[i] = np.where(sd > 0, rr.mean(1) / np.where(sd > 0, sd, 1), -np.inf)
            return out * np.sqrt(12)
        res = dict(net=net, net2x=net - cm * on, placebo=placebo, pop_mu=pop_mu, pop_sd=pop_sd, z=z, on=on)
    hn = spec.get("hidden_n")
    if hn:                                         # P3: loss of n x monthly mean with chance 1/n a month
        L_ = hn * res["pop_mu"]
        hit = rng.random(res["net"].shape) < 1.0 / hn
        res["net"] = res["net"] - L_ * hit
        res["net2x"] = res["net2x"] - L_ * hit
        res["pop_sd_h"] = np.sqrt(res["pop_sd"] ** 2 + L_ * L_ * (1 / hn) * (1 - 1 / hn))
        res["pop_mu"] = 0.0
        res["hit_any"] = hit.any(1)
    return res


def make_book(rng, R, pods, SRb, T=T_FULL, gen=None):
    """Book: mean SRb, vol 10%, GARCH-t AR(1) own part; correlation rho_j with pod j inside pod j's window
    (pods = list of (z, rho, start))."""
    gen = gen or GEN
    e = garch_t(rng, (R,), T, df=gen["df"], a=gen["a"], b=gen["b"], ar=gen["ar"])
    common = np.zeros((R, T))
    used = np.zeros(T)
    for z, rho, t0 in pods:
        common[:, t0:] += rho * z
        used[t0:] += rho * rho
    w = np.sqrt(1 - used)
    return SRb * VOL / 12 + MV * (common + w * e)


# ------------------------------------------------------------------------------------------------- statistics
_CC = {}


def counts(T):
    """Resample count matrix of the registered stationary bootstrap (seed 20261101, 10,000 draws, mean block 6):
    every resample statistic is a linear function of these counts, so one matrix product gives all of them."""
    if T not in _CC:
        idx = ST._stationary_idx(T, NB, BLK, BSEED)
        flat = (idx + np.arange(NB)[:, None] * T).ravel()
        _CC[T] = np.bincount(flat, minlength=NB * T).reshape(NB, T).astype(np.float64)
    return _CC[T]


def boot_alpha(x, y):
    """Least-squares alpha of y on x (rows = reps), one-sided centred stationary-bootstrap p (H0 alpha <= 0),
    regression re-fitted in every resample (1.3c P2)."""
    R, T = x.shape
    mx, my = x.mean(1), y.mean(1)
    beta = ((x - mx[:, None]) * (y - my[:, None])).mean(1) / ((x - mx[:, None]) ** 2).mean(1)
    a = my - beta * mx
    p = np.empty(R)
    C = counts(T)
    for i in range(0, R, CHUNK):
        sl = slice(i, i + CHUNK)
        n = x[sl].shape[0]
        M = np.concatenate([x[sl], x[sl] ** 2, y[sl], x[sl] * y[sl]], 0).T
        S = C @ M / T
        Sx, Sxx, Sy, Sxy = S[:, :n], S[:, n:2 * n], S[:, 2 * n:3 * n], S[:, 3 * n:]
        ab = Sy - (Sxy - Sx * Sy) / (Sxx - Sx * Sx) * Sx
        p[sl] = ((ab - a[sl] >= a[sl]).sum(0) + 1) / (NB + 1)
    return a, beta, p


def _sr(x):
    return x.mean(1) / x.std(1, ddof=1) * np.sqrt(12)


def boot_dsr(b, c):
    """Vectorised gm.stats.paired_sr_test: dSR, p, lb95 (identical rows -> 0, 1, 0)."""
    R, T = b.shape
    d = _sr(c) - _sr(b)
    p, lb = np.ones(R), np.zeros(R)
    ident = np.max(np.abs(b - c), axis=1) < 1e-10
    C = counts(T)
    for i in range(0, R, CHUNK):
        sl = slice(i, i + CHUNK)
        n = b[sl].shape[0]
        M = np.concatenate([b[sl], b[sl] ** 2, c[sl], c[sl] ** 2], 0).T
        S = C @ M
        m1, q1, m2, q2 = S[:, :n] / T, S[:, n:2 * n], S[:, 2 * n:3 * n] / T, S[:, 3 * n:]
        srb = m1 / np.sqrt((q1 - T * m1 * m1) / (T - 1)) * np.sqrt(12)
        src = m2 / np.sqrt((q2 - T * m2 * m2) / (T - 1)) * np.sqrt(12)
        ds = src - srb
        dd = d[sl]
        p[sl] = ((ds - dd >= dd).sum(0) + 1) / (NB + 1)
        lb[sl] = dd - np.percentile(ds - dd, 95, axis=0)
    d = np.where(ident, 0.0, d)
    p = np.where(ident, 1.0, p)
    lb = np.where(ident, 0.0, lb)
    return d, p, lb, ident


def maxdd_rows(r):
    c = np.cumprod(1 + r, axis=1)
    return (c / np.maximum.accumulate(c, axis=1) - 1).min(1)


def holm_rows(P):
    """Holm step-down adjusted p per row (reps x m), same rule as gm.stats.holm."""
    order = np.argsort(P, axis=1, kind="stable")
    Ps = np.take_along_axis(P, order, 1)
    m = P.shape[1]
    adj = np.minimum(1.0, Ps * (m - np.arange(m)))
    adj = np.maximum.accumulate(adj, axis=1)
    out = np.empty_like(P)
    np.put_along_axis(out, order, adj, 1)
    return out


def test_pod(book, pod, t0, rng_pl, pl_kind="block"):
    """All test-sheet statistics for one pod against its book slice (window = pod months)."""
    R, Tw = pod["net"].shape
    b = book[:, t0:]
    p, p2 = pod["net"], pod["net2x"]
    c, c2 = b + LAMBDA * p, b + LAMBDA * p2
    out = {}
    a, beta, pa = boot_alpha(b, p)
    out.update(alpha=a * 12, beta=beta, p_alpha=pa)
    mx, my2 = b.mean(1), p2.mean(1)
    beta2 = ((b - mx[:, None]) * (p2 - my2[:, None])).mean(1) / ((b - mx[:, None]) ** 2).mean(1)
    out["alpha2x"] = (my2 - beta2 * mx) * 12
    d, pd_, lb, _ = boot_dsr(b, c)
    out.update(dsr=d, p_dsr=pd_, lb=lb, dsr2x=_sr(c2) - _sr(b))
    e1 = max(0, ERA_SPLIT - t0)
    era = {}
    for k, (lo, hi) in {"1975": (0, e1), "1990": (e1, Tw)}.items():
        if hi - lo < PR.MIN_ERA:
            era[k] = np.ones(R, bool)
            out["lb_" + k] = np.full(R, np.nan)
            continue
        _, _, lbe, ide = boot_dsr(b[:, lo:hi], c[:, lo:hi])
        era[k] = ide | (lbe > PR.NI_MARGIN)
        out["lb_" + k] = lbe
    out["era1_pass"], out["era2_pass"] = era["1975"], era["1990"]
    out["era_pass"] = era["1975"] & era["1990"]
    cs = c * (b.std(1, ddof=1) / c.std(1, ddof=1))[:, None]
    out["dd_b"], out["dd_c"] = maxdd_rows(b), maxdd_rows(cs)
    out["wm_b"], out["wm_c"] = b.min(1), cs.min(1)
    out["tail"] = (out["dd_c"] >= out["dd_b"] - PR.MAX_DD_WORSE) & (out["wm_c"] >= out["wm_b"] - 0.01)
    sd = p.std(1, ddof=1)
    out["sr_pod"] = np.where(sd > 0, p.mean(1) / np.where(sd > 0, sd, 1), 0) * np.sqrt(12)
    out["mean_pod"] = p.mean(1)
    perms = [block_perm(rng_pl, Tw, kind=pl_kind) for _ in range(N_PLACEBO)]
    pls = pod["placebo"](perms)
    out["p_pl"] = np.where(sd > 0, ((pls >= out["sr_pod"][None, :]).sum(0) + 1) / (N_PLACEBO + 1), 1.0)
    out["pl_point"] = out["sr_pod"] > pls.mean(0)
    if "on" in pod:
        on = pod["on"]
        out["n_on"] = on.sum(1)
        starts = (on[:, 1:] == 1) & (on[:, :-1] == 0)
        out["episodes"] = starts.sum(1) + on[:, 0]
    if "hit_any" in pod:
        out["hit_any"] = pod["hit_any"]
    return out


def truth(spec, SRb, rho, pod):
    """Population alpha (appraisal ratio, annual) and held-size dSR."""
    mu, sd = pod["pop_mu"], pod.get("pop_sd_h", pod["pop_sd"])
    sdz = pod["pop_sd"]                            # the correlation was built on the loss-free part
    mub, sdb = SRb * VOL / 12, MV
    cov = rho * sdz * sdb
    beta = cov / sdb ** 2
    alpha = mu - beta * mub
    res_sd = np.sqrt(max(sd * sd - beta * beta * sdb * sdb, 1e-18))
    ir = alpha / res_sd * np.sqrt(12)
    muc = mub + LAMBDA * mu
    sdc = np.sqrt(sdb ** 2 + LAMBDA ** 2 * sd ** 2 + 2 * LAMBDA * cov)
    dsr = (muc / sdc - mub / sdb) * np.sqrt(12)
    return ir, dsr


# ------------------------------------------------------------------------------------------------- readings
def readings(o, m=1, alpha_wf=0.025, alpha_tp=0.05, pa_holm=None, pd_holm=None):
    """Pass indicators per rep under every reading. pa_holm/pd_holm: Holm-adjusted p (batch) or raw (m = 1)."""
    pa = o["p_alpha"] if pa_holm is None else pa_holm
    pdh = o["p_dsr"] if pd_holm is None else pd_holm
    r = {}
    r["T1_alpha_025"] = pa < 0.025
    r["T1_alpha_05"] = pa < 0.05
    r["T1_dsr_025"] = pdh < 0.025
    r["T1_dsr_05"] = pdh < 0.05
    r["T2_alpha2x"] = o["alpha2x"] > 0
    r["T2_dsr2x"] = o["dsr2x"] > 0
    r["T3_pl05"] = o["p_pl"] < 0.05
    r["T3_pl10"] = o["p_pl"] < 0.10
    r["T3_point"] = o["pl_point"]
    r["T4_tail"] = o["tail"]
    r["T4_tail_3_15"] = (o["dd_c"] >= o["dd_b"] - 0.03) & (o["wm_c"] >= o["wm_b"] - 0.015)
    r["T4_tail_4_2"] = (o["dd_c"] >= o["dd_b"] - 0.04) & (o["wm_c"] >= o["wm_b"] - 0.02)
    r["ERA"] = o["era_pass"]
    r["SIZE"] = o["dsr"] >= PR.MIN_DSR
    base = r["T2_alpha2x"] & r["T3_pl05"] & r["T4_tail"]
    r["WF_025"] = (pa < alpha_wf) & base                       # WORKFLOW s5 + 1.3c P2, Holm 2.5%
    r["WF_05"] = (pa < 0.05) & base                            # same, Holm 5%
    r["WF_025_era"] = r["WF_025"] & r["ERA"]                   # era test decisive
    r["WF_dsr_025"] = (pdh < 0.025) & r["T2_dsr2x"] & r["T3_pl05"] & r["T4_tail"]
    r["WF_025_notail"] = (pa < alpha_wf) & r["T2_alpha2x"] & r["T3_pl05"]
    r["WF_025_tail3"] = (pa < alpha_wf) & r["T2_alpha2x"] & r["T3_pl05"] & r["T4_tail_3_15"]
    r["WF_025_tail4"] = (pa < alpha_wf) & r["T2_alpha2x"] & r["T3_pl05"] & r["T4_tail_4_2"]
    r["WF_025_pl10"] = (pa < alpha_wf) & r["T2_alpha2x"] & r["T3_pl10"] & r["T4_tail"]
    r["TP_05"] = (pdh < alpha_tp) & r["SIZE"] & r["ERA"] & r["T2_dsr2x"] & r["T4_tail"]   # TESTING_PROTOCOL 1-5
    r["TP_025"] = (pdh < 0.025) & r["SIZE"] & r["ERA"] & r["T2_dsr2x"] & r["T4_tail"]
    r["TP_05_pl"] = r["TP_05"] & r["T3_pl05"]
    r["INCUB"] = (o["mean_pod"] > 0) & r["T3_pl05"] & r["T4_tail"]
    return r


# ------------------------------------------------------------------------------------------------- cells
def run_cell(spec, R, SRb, rho, gen=None):
    name = json.dumps(dict(spec, SRb=SRb, rho=rho, R=R, gen=gen), sort_keys=True)
    rng = rng_for(name)
    pod = make_pod(spec, R, rng)
    t0 = T_FULL - spec["Tw"]
    book = make_book(rng, R, [(pod["z"], rho, t0)], SRb, gen=gen)
    o = test_pod(book, pod, t0, rng_for(name + "|pl"), spec.get("pl_kind", "block"))
    ir, tdsr = truth(spec, SRb, rho, pod)
    return o, ir, tdsr


def summarise(o, ir, tdsr):
    r = readings(o)
    row = {k: float(np.mean(v)) for k, v in r.items()}
    row["true_IR"], row["true_dSR_held"] = ir, tdsr
    row["mean_alpha"], row["mean_dsr"] = float(np.mean(o["alpha"])), float(np.mean(o["dsr"]))
    adopted = r["WF_025"]
    row["adopt_share_true_dSR_lt0"] = float(tdsr < 0) if adopted.any() else np.nan
    if "n_on" in o:
        row["n_on_med"], row["episodes_med"] = float(np.median(o["n_on"])), float(np.median(o["episodes"]))
        row["episodes_p10"] = float(np.percentile(o["episodes"], 10))
    if "hit_any" in o:
        row["share_loss_seen"] = float(np.mean(o["hit_any"]))
        row["WF_025_loss_seen"] = float(np.mean(r["WF_025"][o["hit_any"]])) if o["hit_any"].any() else np.nan
        row["WF_025_loss_unseen"] = float(np.mean(r["WF_025"][~o["hit_any"]])) if (~o["hit_any"]).any() else np.nan
    return row


SHAPES = {
    "FULL432": dict(kind="sys", Tw=432, K=8, phi=0.9, cost=0.10),
    "STRIP250": dict(kind="sys", Tw=250, K=8, phi=0.5, cost=0.30),
    "STRIP200": dict(kind="sys", Tw=200, K=8, phi=0.5, cost=0.30),
    "CURVE260": dict(kind="sys", Tw=260, K=8, phi=0.9, cost=0.20),
    "CURVE200": dict(kind="sys", Tw=200, K=8, phi=0.9, cost=0.20),
    "CURVE360": dict(kind="sys", Tw=360, K=8, phi=0.9, cost=0.20),
    "RULE_q10_L12": dict(kind="rule", Tw=432, q=0.10, L=12, cost=0.05),
    "RULE_q25_L12": dict(kind="rule", Tw=432, q=0.25, L=12, cost=0.05),
    "RULE_q50_L12": dict(kind="rule", Tw=432, q=0.50, L=12, cost=0.05),
}


def part_cells(R, quick=False):
    rows = []
    t_start = time.time()
    S_list = (0.0, 0.2, 0.4)
    rhos = (0.0, 0.3, 0.6)
    plan = []
    for sh, sp in SHAPES.items():
        srbs = (1.23, 0.5) if sh in ("FULL432", "STRIP250", "CURVE260", "RULE_q10_L12", "RULE_q25_L12",
                                     "RULE_q50_L12") else (1.23,)
        rr = rhos if len(srbs) == 2 else (0.3,)
        if sp["kind"] == "rule":
            rr = (0.0, 0.3)                       # rho 0.6 is not a realistic layer and distorts the generator
        for SRb in srbs:
            for rho in (rr if SRb == 1.23 else (0.3,)):
                for S in S_list:
                    plan.append((sh, dict(sp, S=S), SRb, rho, "standalone S=%.1f" % S))
                # no skill at all: gross Sharpe 0, net = minus costs
                plan.append((sh, dict(sp, S=-sp["cost"]), SRb, rho, "no skill (gross 0)"))
                # boundary null: alpha exactly zero (S = rho * SRb)
                plan.append((sh, dict(sp, S=rho * SRb), SRb, rho, "null alpha=0"))
                # true appraisal ratio 0.2 / 0.4 in the residual
                for ir in (0.2, 0.4):
                    plan.append((sh, dict(sp, S=rho * SRb + ir * np.sqrt(1 - rho * rho)), SRb, rho, "IR=%.1f" % ir))
    if quick:
        plan = plan[::7]
    for i, (sh, sp, SRb, rho, lab) in enumerate(plan):
        t = time.time()
        o, ir, td = run_cell(sp, R, SRb, rho)
        row = dict(shape=sh, label=lab, S=sp["S"], rho=rho, SRb=SRb, R=R)
        row.update(summarise(o, ir, td))
        rows.append(row)
        print("[%3d/%d] %-14s %-18s rho %.1f SRb %.2f WF %.3f TP %.3f  %.1fs" % (
            i + 1, len(plan), sh, lab, rho, SRb, row["WF_025"], row["TP_05"], time.time() - t), flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RAW, "cells.csv"), index=False)
    print("cells done %.0fs" % (time.time() - t_start))
    return df


def part_special(R):
    """Placebo forms, rule-layer premium, calendar rule, on-month table, hidden-loss row."""
    rows = []
    t_start = time.time()
    # (a) systematic pod: Sharpe from timing / half standing exposure / standing exposure only
    for mode in ("timing", "mixed", "static"):
        for S in (0.0, 0.4):
            sp = dict(SHAPES["FULL432"], S=S, mode=mode)
            o, ir, td = run_cell(sp, R, 1.23, 0.3)
            row = dict(block="placebo_form", shape="FULL432", mode=mode, S=S, rho=0.3, SRb=1.23)
            row.update(summarise(o, ir, td))
            rows.append(row)
            print("placebo", mode, S, row["T3_pl05"], flush=True)
    # (b) rule layer whose return is only the market premium on on-months (no timing) vs timing
    for q in (0.10, 0.25):
        for prem in (0.3,):
            for S_on in (0.3, 0.6):
                for mode in ("premium_only", "timing_plus_premium"):
                    sp = dict(SHAPES["RULE_q25_L12"], q=q, S_on=S_on)
                    if mode == "premium_only":
                        sp.update(mode="premium", S_on=prem)   # all of its on-month Sharpe is the premium
                    else:
                        sp.update(prem=prem)
                    o, ir, td = run_cell(sp, R, 1.23, 0.0)
                    row = dict(block="rule_premium", shape="RULE_q%02d_L12" % (q * 100), mode=mode, S_on=sp["S_on"],
                               prem=prem, rho=0.0, SRb=1.23)
                    row.update(summarise(o, ir, td))
                    rows.append(row)
    # (c) calendar rule: 12-month block shuffle vs within-year rotation
    for S_on in (0.0, 0.8):
        for kind in ("block", "rot"):
            sp = dict(kind="cal", Tw=432, q=2 / 12, cost=0.05, S_on=S_on, pl_kind=kind)
            o, ir, td = run_cell(sp, R, 1.23, 0.0)
            row = dict(block="calendar", shape="CAL_q17", mode=kind, S_on=S_on, rho=0.0, SRb=1.23)
            row.update(summarise(o, ir, td))
            rows.append(row)
    # (d) on-month table: what an intermittent layer can show, by on-share and spell length (rho 0)
    for q in (0.05, 0.10, 0.25, 0.50):
        for L in (3, 12, 24):
            for S_on in (0.0, 0.4, 0.8, 1.2):
                sp = dict(kind="rule", Tw=432, q=q, L=L, cost=0.05, S_on=S_on)
                o, ir, td = run_cell(sp, R, 1.23, 0.0)
                row = dict(block="onmonth", shape="RULE_q%02d_L%d" % (q * 100, L), q=q, L=L, S_on=S_on, rho=0.0,
                           SRb=1.23)
                row.update(summarise(o, ir, td))
                # pass rate by realised on-months
                r = readings(o)
                for lo, hi in ((0, 24), (24, 48), (48, 96), (96, 144), (144, 432)):
                    msk = (o["n_on"] >= lo) & (o["n_on"] < hi)
                    row["WF025_on%d_%d" % (lo, hi)] = float(np.mean(r["WF_025"][msk])) if msk.sum() >= 20 else np.nan
                    row["T1_on%d_%d" % (lo, hi)] = float(np.mean(r["T1_alpha_025"][msk])) if msk.sum() >= 20 else np.nan
                    row["n_on%d_%d" % (lo, hi)] = int(msk.sum())
                for lo, hi in ((0, 3), (3, 6), (6, 10), (10, 1000)):
                    msk = (o["episodes"] >= lo) & (o["episodes"] < hi)
                    row["PL_ep%d_%d" % (lo, hi)] = float(np.mean(r["T3_pl05"][msk])) if msk.sum() >= 20 else np.nan
                    row["n_ep%d_%d" % (lo, hi)] = int(msk.sum())
                rows.append(row)
        print("onmonth q", q, "%.0fs" % (time.time() - t_start), flush=True)
    # (e) hidden loss (1.3c P3): Sharpe-0.4 pod plus a loss of n x monthly mean with chance 1/n
    for rho in (0.0, 0.3):
        base = dict(SHAPES["FULL432"], S=0.4)
        o0, ir0, td0 = run_cell(base, R, 1.23, rho)
        r0 = summarise(o0, ir0, td0)
        for n in (216, 432, 864):
            sp = dict(base, hidden_n=n)
            o, ir, td = run_cell(sp, R, 1.23, rho)
            row = dict(block="hidden_loss", shape="FULL432", hidden_n=n, S=0.4, rho=rho, SRb=1.23,
                       loss_size_pod=n * 0.4 * VOL / 12, WF_025_base04=r0["WF_025"], TP_05_base04=r0["TP_05"],
                       INCUB_base04=r0["INCUB"], identity_bound=(1 - 1 / n) ** T_FULL)
            row.update(summarise(o, ir, td))
            row["ratio_WF"] = row["WF_025"] / r0["WF_025"] if r0["WF_025"] > 0 else np.nan
            row["ratio_T1"] = row["T1_alpha_025"] / r0["T1_alpha_025"] if r0["T1_alpha_025"] > 0 else np.nan
            rows.append(row)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RAW, "special.csv"), index=False)
    print("special done %.0fs" % (time.time() - t_start))
    return df


# ------------------------------------------------------------------------------------------------- batches
B2_PODS = [  # (label, spec, rho)
    ("Strip reversion", dict(SHAPES["STRIP250"]), 0.3),
    ("2nd systematic", dict(SHAPES["FULL432"]), 0.3),
    ("Card 1", dict(kind="rule", Tw=432, q=0.25, L=12, cost=0.05), 0.2),
    ("Card 2", dict(kind="rule", Tw=432, q=0.10, L=12, cost=0.05), 0.2),
    ("Card 3", dict(kind="rule", Tw=432, q=0.50, L=12, cost=0.05), 0.2),
    ("Card 4", dict(kind="rule", Tw=432, q=0.25, L=3, cost=0.05), 0.2),
    ("Card 5", dict(kind="rule", Tw=432, q=0.10, L=24, cost=0.05), 0.2),
]


def run_batch(pods, R, SRb, scen):
    """pods: list of (label, spec with S, rho). One book per rep shared by all pods."""
    name = "batch|%s|%s|%d" % (scen, SRb, R)
    rng = rng_for(name)
    made = [make_pod(sp, R, rng) for _, sp, _ in pods]
    book = make_book(rng, R, [(m["z"], rho, T_FULL - sp["Tw"]) for m, (_, sp, rho) in zip(made, pods)], SRb)
    outs, irs = [], []
    for j, (m, (lab, sp, rho)) in enumerate(zip(made, pods)):
        o = test_pod(book, m, T_FULL - sp["Tw"], rng_for(name + "|pl%d" % j))
        outs.append(o)
        irs.append(truth(sp, SRb, rho, m)[0])
    return outs, np.array(irs)


def part_batch(R):
    rows = []
    t_start = time.time()
    for SRb in (1.23, 0.5):
        scen = {
            "all null (alpha 0)": [(l, dict(sp, S=rho * SRb), rho) for l, sp, rho in B2_PODS],
            "all standalone S 0": [(l, dict(sp, S=0.0), rho) for l, sp, rho in B2_PODS],
            "2 systematic IR 0.4, layers null": [(l, dict(sp, S=rho * SRb + (0.4 * np.sqrt(1 - rho * rho) if j < 2
                                                                             else 0)), rho)
                                                  for j, (l, sp, rho) in enumerate(B2_PODS)],
            "2 systematic S 0.4, layers S 0.2": [(l, dict(sp, S=(0.4 if j < 2 else 0.2)), rho)
                                                 for j, (l, sp, rho) in enumerate(B2_PODS)],
        }
        for sname, pods in scen.items():
            outs, irs = run_batch(pods, R, SRb, sname)
            PA = np.column_stack([o["p_alpha"] for o in outs])
            PD = np.column_stack([o["p_dsr"] for o in outs])
            null = irs <= 1e-9
            for count_name, cols in (("Holm over 7", list(range(7))), ("Holm over 2 (layers outside)", [0, 1])):
                HA = np.ones_like(PA)
                HD = np.ones_like(PD)
                HA[:, cols] = holm_rows(PA[:, cols])
                HD[:, cols] = holm_rows(PD[:, cols])
                reads = []
                for j, o in enumerate(outs):
                    if j in cols:
                        reads.append(readings(o, pa_holm=HA[:, j], pd_holm=HD[:, j]))
                    else:
                        reads.append(None)
                for key in ("T1_alpha_025", "T1_alpha_05", "WF_025", "WF_05", "WF_025_era", "TP_05", "TP_025"):
                    adopt = np.column_stack([reads[j][key] if reads[j] is not None else np.zeros(R, bool)
                                             for j in range(7)])
                    row = dict(SRb=SRb, scenario=sname, count=count_name, reading=key,
                               fwer_false_adoption=float(np.mean((adopt & null[None, :]).any(1))),
                               any_adoption=float(np.mean(adopt.any(1))))
                    for j in range(7):
                        row["pass_" + B2_PODS[j][0]] = float(np.mean(adopt[:, j]))
                    rows.append(row)
            # Incubator (no multiplicity): layers
            inc = np.column_stack([readings(o)["INCUB"] for o in outs])
            row = dict(SRb=SRb, scenario=sname, count="none (Incubator rule)", reading="INCUB",
                       fwer_false_adoption=float(np.mean((inc & null[None, :]).any(1))),
                       any_adoption=float(np.mean(inc.any(1))))
            for j in range(7):
                row["pass_" + B2_PODS[j][0]] = float(np.mean(inc[:, j]))
            rows.append(row)
            print("batch", SRb, sname, "%.0fs" % (time.time() - t_start), flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RAW, "batch.csv"), index=False)
    return df


# ------------------------------------------------------------------------------------------------- hygiene
def part_hygiene(R):
    """Batch A: incumbent book vs a hygiene change with true effect delta on the book Sharpe."""
    rows = []
    for rho_ic, se_lab in ((0.996, "SE~0.015"), (0.971, "SE~0.04"), (0.924, "SE~0.065")):
        for delta in (-0.3, -0.2, -0.1, 0.0, 0.1):
            name = "hyg|%s|%s|%d" % (rho_ic, delta, R)
            rng = rng_for(name)
            b = make_book(rng, R, [], 1.23)
            u = garch_t(rng, (R,), T_FULL)
            tau = np.sqrt(1 - rho_ic ** 2)
            mub = 1.23 * VOL / 12
            c = rho_ic * (b - mub) + tau * MV * u + (1.23 + delta) * VOL / 12
            d, p, lb, _ = boot_dsr(b, c)
            era = []
            for lo, hi in ((0, 180), (180, 432)):
                _, _, lbe, ide = boot_dsr(b[:, lo:hi], c[:, lo:hi])
                era.append(ide | (lbe > PR.NI_MARGIN))
            era = era[0] & era[1]
            cs = c * (b.std(1, ddof=1) / c.std(1, ddof=1))[:, None]
            tail = (maxdd_rows(cs) >= maxdd_rows(b) - PR.MAX_DD_WORSE) & (cs.min(1) >= b.min(1) - 0.01)
            sup = (p < PR.ALPHA) & (d >= PR.MIN_DSR) & era & (d > 0) & tail   # cost difference not modelled
            ni = lb > PR.NI_MARGIN
            row = dict(se_label=se_lab, corr=rho_ic, true_delta=delta, R=R, boot_se_mean=np.nan,
                       superiority_TP=float(np.mean(sup)), superiority_test1_only=float(np.mean(p < PR.ALPHA)),
                       NI_pooled=float(np.mean(ni)), NI_pooled_eras=float(np.mean(ni & era)),
                       NI_pooled_eras_tail=float(np.mean(ni & era & tail)),
                       NI_vs_incumbent_less_023=float(np.mean(lb + 0.23 > PR.NI_MARGIN)),
                       NI_pooled_0p05=float(np.mean(lb > -0.05)),
                       sd_dsr=float(np.std(d)))
            rows.append(row)
            print("hyg", se_lab, delta, row["NI_pooled"], row["superiority_TP"], flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RAW, "hygiene.csv"), index=False)
    return df


# ------------------------------------------------------------------------------------------------- holdout
def part_holdout(R):
    rows = []
    months = 189
    for gen_lab, gen in (("GARCH-t5 (calibrated)", GEN), ("Gaussian iid", dict(df=None, a=0, b=0, ar=0.0))):
        rng = rng_for("holdout|" + gen_lab)
        for s in (0.0, 0.4, 0.8, 1.2):
            e = garch_t(rng, (R,), months, df=gen["df"], a=gen["a"], b=gen["b"], ar=gen["ar"])
            y = e * MV + s * VOL / 12
            sr = _sr(y)
            dd = maxdd_rows(y)
            y22 = np.prod(1 + y[:, 132:144], axis=1) - 1
            out = dict(generator=gen_lab, true_SR=s, months=months, R=R, p_sr=float(np.mean(sr >= 0.3)),
                       p_dd=float(np.mean(dd > -0.25)), p_2022=float(np.mean(y22 > 0)))
            for rs in (0.0, 0.2):
                spx = rs * e + np.sqrt(1 - rs * rs) * rng.standard_normal(e.shape)
                cc = np.array([np.corrcoef(a_, b_)[0, 1] for a_, b_ in zip(y, spx)])
                out["p_corr_true%.1f" % rs] = float(np.mean(cc <= 0.3))
            ok = (sr >= 0.3) & (dd > -0.25) & (y22 > 0)
            out["p_all_corr_met"] = float(np.mean(ok))
            out["p_sr_dd"] = float(np.mean((sr >= 0.3) & (dd > -0.25)))
            rows.append(out)
    # cross-check: the registered gm.audit.holdout_power on synthetic 432-month books (it bootstraps the series given)
    rng = rng_for("holdout|audit")
    acc = {}
    nb = 10
    for i in range(nb):
        x = garch_t(rng, (1,), T_FULL, ar=GEN["ar"])[0] * MV + 1.46 * VOL / 12
        hp = AU.holdout_power(pd.Series(x), sims=4000, seed=11 + i)
        for s_, v in hp.items():
            for k, val in v.items():
                acc.setdefault((s_, k), []).append(val)
    for (s_, k), v in acc.items():
        rows.append(dict(generator="gm.audit.holdout_power on %d synthetic design books" % nb, true_SR=s_,
                         months=189, R=nb * 4000, **{"audit_" + k: float(np.mean(v))}))
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RAW, "holdout.csv"), index=False)
    return df


# ------------------------------------------------------------------------------------------------- calibration
def part_calib(R=4000):
    rng = rng_for("calib")
    rows = []
    from numpy.lib.stride_tricks import sliding_window_view as sw
    for lab, T in (("1975-89 (180 m)", 180), ("1990-2010 (252 m)", 252)):
        x = garch_t(rng, (R,), T, ar=GEN["ar"])
        r = x * MV
        xc = x - x.mean(1, keepdims=True)
        sk = (xc ** 3).mean(1) / x.std(1) ** 3
        ku = (xc ** 4).mean(1) / x.std(1) ** 4
        ac = (xc[:, 1:] * xc[:, :-1]).sum(1) / (xc ** 2).sum(1)
        rv = sw(r, 36, axis=1).std(-1, ddof=1) * np.sqrt(12)
        for k, v in (("skew", sk), ("kurtosis", ku), ("worst month %", r.min(1) * 100), ("AC(1)", ac),
                     ("rolling 36m vol min %", rv.min(1) * 100), ("rolling 36m vol max %", rv.max(1) * 100)):
            rows.append(dict(window=lab, stat=k, p10=np.percentile(v, 10), p50=np.percentile(v, 50),
                             p90=np.percentile(v, 90)))
    x = garch_t(rng, (R,), T_FULL, ar=GEN["ar"])
    for sr in (1.22, 1.46):
        dd = maxdd_rows(x * MV + sr * VOL / 12) * 100
        rows.append(dict(window="1975-2010 (432 m), SR %.2f" % sr, stat="max drawdown %", p10=np.percentile(dd, 10),
                         p50=np.percentile(dd, 50), p90=np.percentile(dd, 90)))
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RAW, "calibration.csv"), index=False)
    print(df.round(2).to_string())
    return df


# ------------------------------------------------------------------------------------------------- validation
def part_validate():
    """The vectorised tests equal the registered code: paired_sr_test, holm, decide; alpha bootstrap vs a loop."""
    rng = rng_for("validate")
    R = 6
    lines = []
    for Tw in (432, 250, 180):
        b = make_book(rng, R, [], 1.23, T=Tw)
        p_ = garch_t(rng, (R,), Tw) * MV + 0.3 * VOL / 12
        c = b + LAMBDA * p_
        d, pv, lb, _ = boot_dsr(b, c)
        for i in range(R):
            ref = ST.paired_sr_test(pd.Series(b[i]), pd.Series(c[i]))
            lines.append("T=%d rep %d: dsr %.6f/%.6f p %.5f/%.5f lb %.6f/%.6f" % (
                Tw, i, d[i], ref["dsr"], pv[i], ref["p"], lb[i], ref["lb95"]))
            assert abs(d[i] - ref["dsr"]) < 1e-9 and abs(pv[i] - ref["p"]) < 1e-12 and abs(lb[i] - ref["lb95"]) < 1e-7
        a, beta, pa = boot_alpha(b, p_)
        idx = ST._stationary_idx(Tw, NB, BLK, BSEED)
        for i in range(2):
            X, Y = b[i][idx], p_[i][idx]
            mx, my = X.mean(1), Y.mean(1)
            bb = ((X - mx[:, None]) * (Y - my[:, None])).mean(1) / ((X - mx[:, None]) ** 2).mean(1)
            ab = my - bb * mx
            A = np.column_stack([np.ones(Tw), b[i]])
            a_ref = np.linalg.lstsq(A, p_[i], rcond=None)[0][0]
            p_ref = ((ab - a_ref >= a_ref).sum() + 1) / (NB + 1)
            lines.append("alpha T=%d rep %d: a %.8f/%.8f p %.5f/%.5f" % (Tw, i, a[i], a_ref, pa[i], p_ref))
            assert abs(a[i] - a_ref) < 1e-12 and abs(pa[i] - p_ref) < 1e-12
    P = rng.random((50, 7))
    H = holm_rows(P)
    for i in range(50):
        ref = ST.holm({j: P[i, j] for j in range(7)})
        assert all(abs(H[i, j] - ref[j]) < 1e-12 for j in range(7))
    lines.append("holm_rows == gm.stats.holm on 50 random 7-vectors")
    # decide(): one-pod batches through gm.protocol.decide vs the vectorised TP_05 reading
    sp = dict(SHAPES["FULL432"], S=0.4)
    o, _, _ = run_cell(sp, 200, 1.23, 0.0)
    r = readings(o)
    agree = 0
    for i in range(200):
        rec = {"name": "x", "p": float(o["p_dsr"][i]), "dsr": float(o["dsr"][i]),
               "eras": {"1975": {"pass": bool(o["era1_pass"][i])}, "1990": {"pass": bool(o["era2_pass"][i])}},
               "dsr_2x": float(o["dsr2x"][i]), "dd_inc": float(o["dd_b"][i]), "dd_cha": float(o["dd_c"][i]),
               "wm_inc": float(o["wm_b"][i]), "wm_cha": float(o["wm_c"][i])}
        agree += PR.decide([rec])[0]["adopt"] == bool(r["TP_05"][i])
    lines.append("gm.protocol.decide agrees with TP_05 on %d of 200 simulated pods" % agree)
    assert agree == 200
    txt = "\n".join(lines)
    open(os.path.join(OUT, "validation.txt"), "w").write(txt + "\nALL VALIDATION CHECKS PASSED\n")
    print(txt + "\nALL VALIDATION CHECKS PASSED")


# ------------------------------------------------------------------------------------------------- robustness
def part_robust(R):
    """Key cells (rho 0.3, SRb 1.23) under other generators: fatter tails, Gaussian iid, negative-skew jumps."""
    gens = {"t4 GARCH(0.08,0.90)": dict(df=4, a=0.08, b=0.90, ar=0.10),
            "Gaussian iid": dict(df=None, a=0, b=0, ar=0.0)}
    rows = []
    for gl, g in gens.items():
        for sh in ("FULL432", "STRIP250", "CURVE260", "RULE_q25_L12"):
            for S in (0.0, 0.2, 0.4):
                o, ir, td = run_cell(dict(SHAPES[sh], S=S), R, 1.23, 0.3, gen=g)
                row = dict(generator=gl, shape=sh, S=S, rho=0.3, SRb=1.23)
                row.update(summarise(o, ir, td))
                rows.append(row)
            o, ir, td = run_cell(dict(SHAPES[sh], S=0.3 * 1.23), R, 1.23, 0.3, gen=g)
            row = dict(generator=gl, shape=sh, S=0.3 * 1.23, rho=0.3, SRb=1.23, label="null alpha=0")
            row.update(summarise(o, ir, td))
            rows.append(row)
            print("robust", gl, sh, flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RAW, "robust.csv"), index=False)
    return df


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=1000)
    ap.add_argument("--part", default="all")
    ap.add_argument("--quick", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    parts = a.part.split(",")
    if "all" in parts or "validate" in parts:
        part_validate()
    if "all" in parts or "calib" in parts:
        part_calib()
    if "all" in parts or "cells" in parts:
        part_cells(a.reps, a.quick)
    if "all" in parts or "special" in parts:
        part_special(a.reps)
    if "all" in parts or "batch" in parts:
        part_batch(a.reps)
    if "all" in parts or "hygiene" in parts:
        part_hygiene(a.reps)
    if "all" in parts or "holdout" in parts:
        part_holdout(max(a.reps, 20000))
    if "all" in parts or "robust" in parts:
        part_robust(a.reps)
    print("total %.0fs" % (time.time() - t0))
