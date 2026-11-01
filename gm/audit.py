"""Statistical audit of the build (design months only; the holdout is never read).

python -m gm.audit   -> docs/research/global_macro/stats_audit_2026-11-02.md
1. Bootstrap block-length sensitivity (Sharpe interval and the batch-0 paired tests).
2. Selection inflation among logged variants, and the deflated Sharpe under larger trial counts.
3. Probability of backtest overfitting (CSCV, Bailey et al. 2017) over every rebuildable variant.
4. Power of the one-shot holdout test (block bootstrap from design returns, rescaled to a true Sharpe).
5. Emerging-market tradability: the book without EM currencies and equities before 2000.
"""
import itertools
import json
import math
import os

import numpy as np
import pandas as pd

from . import config as CF
from . import protocol as PR
from . import stats as ST
from . import variants as VA

WIN = ("1975-01", "2010-12")
OUT = os.path.join(PR.DOC, "stats_audit_2026-11-02.md")
EM = ("fx_mxn", "fx_brl", "fx_krw", "fx_zar", "eq_cn", "eq_kr_kospi", "eq_tw", "eq_in", "eq_br_ibov", "eq_mx_ipc",
      "eq_za")


def net(cfg, R, S, D):
    return ST.cut(PR.book(cfg, R, S, D)["net"], *WIN)


def variants(R, S, D):
    """Every variant whose result can be rebuilt exactly: logged configs with distinct hashes + batch-1 builders."""
    log = pd.read_csv(os.path.join(os.path.dirname(__file__), "trials.csv"))
    out, seen = {}, set()
    for _, r in log.iterrows():
        if not isinstance(r["config"], str) or r["hash"] in seen or str(r["trial"]).startswith(("batch", "cand2 econ")):
            continue
        seen.add(r["hash"])
        out[r["trial"]] = net(json.loads(r["config"]), R, S, D)
    for name, fn in VA.BATCH1.items():
        c, R2, S2 = fn(CF.CANDIDATE, R, S)
        out[name] = net(c, R2, S2, D)
    return pd.DataFrame(out).dropna()


def cscv(M, S=16):
    """PBO: share of the C(S, S/2) in-sample/out-of-sample splits where the in-sample best variant ranks below the
    median out of sample; also the median out-of-sample Sharpe of the in-sample winner vs its in-sample Sharpe."""
    X = M.values
    T, N = X.shape
    bl = np.array_split(np.arange(T), S)
    s1 = np.array([X[b].sum(0) for b in bl])
    s2 = np.array([(X[b] ** 2).sum(0) for b in bl])
    n = np.array([len(b) for b in bl])
    lam, is_sr, oos_sr = [], [], []
    for comb in itertools.combinations(range(S), S // 2):
        m = np.zeros(S, bool)
        m[list(comb)] = True

        def sr(mask):
            k = n[mask].sum()
            mu = s1[mask].sum(0) / k
            var = s2[mask].sum(0) / k - mu ** 2
            return mu / np.sqrt(var) * np.sqrt(12)
        a, b = sr(m), sr(~m)
        j = int(np.argmax(a))
        w = (np.sum(b < b[j]) + 0.5) / N          # relative out-of-sample rank of the in-sample winner
        lam.append(math.log(w / (1 - w)))
        is_sr.append(a[j])
        oos_sr.append(b[j])
    lam = np.array(lam)
    return {"pbo": float(np.mean(lam <= 0)), "is_sr": float(np.median(is_sr)), "oos_sr": float(np.median(oos_sr)),
            "splits": len(lam), "variants": N}


def holdout_power(r, months=189, sims=20000, block=6, seed=11):
    """Probability of passing the four holdout criteria (corr criterion assumed met) if the true Sharpe is s,
    resampling design-month blocks (keeps fat tails and autocorrelation), rescaled to 10% vol and Sharpe s."""
    x = r.dropna().values
    x = (x - x.mean()) / x.std() * 0.10 / np.sqrt(12)
    idx = ST._stationary_idx(len(x), sims, block, seed)[:, :months] if months <= len(x) else None
    out = {}
    for s in (0.0, 0.3, 0.5, 0.8):
        y = x[idx] + s * 0.10 / 12
        sr = y.mean(1) / y.std(1, ddof=1) * np.sqrt(12)
        c = np.cumprod(1 + y, axis=1)
        dd = (c / np.maximum.accumulate(c, axis=1) - 1).min(1)
        y22 = np.prod(1 + y[:, 132:144], axis=1) - 1            # the 12th calendar year of the holdout = 2022
        ok = (sr >= 0.3) & (dd > -0.25) & (y22 > 0)
        out[s] = {"sr>=0.3": float(np.mean(sr >= 0.3)), "dd": float(np.mean(dd > -0.25)),
                  "2022>0": float(np.mean(y22 > 0)), "all": float(np.mean(ok))}
    return out


def main():
    R, S, D = PR.load()
    L = ["# Statistical audit of the Global Macro Book build (design months 1975-2010 only)", ""]
    cand = net(CF.CANDIDATE, R, S, D)
    base = net(CF.BASE, R, S, D)
    hyb = net(CF.variant(CF.BASE, vol={"model": "hybrid"}), R, S, D)

    L += ["## 1. Bootstrap block length", "", "| Mean block (months) | gm-2.0 SR 90% interval 1975-2010 | "
          "B0.1 hybrid vol dSR p (lb95) | B0.2 shares dSR p (lb95) |", "|---|---|---|---|"]
    for b in (3, 6, 12, 24):
        lo, hi = ST.bootstrap_sr(cand, n=4000, block=b)
        t1 = ST.paired_sr_test(base, hyb, n=4000, block=b)
        t2 = ST.paired_sr_test(hyb, cand, n=4000, block=b)
        L.append("| %d | %.2f - %.2f | %+.3f p %.4f (%+.3f) | %+.3f p %.4f (%+.3f) |" % (
            b, lo, hi, t1["dsr"], t1["p"], t1["lb95"], t2["dsr"], t2["p"], t2["lb95"]))
    sr = ST.sharpe(cand)
    yrs = len(cand) / 12
    L += ["", "Analytic standard error of the 1975-2010 Sharpe (Lo 2002, iid): %.2f (SR %.2f over %.0f years)." % (
        math.sqrt((1 + sr ** 2 / 2) / yrs), sr, yrs), ""]

    log = pd.read_csv(os.path.join(os.path.dirname(__file__), "trials.csv"))
    d = log[~log["trial"].str.startswith("batch")]
    srs = pd.to_numeric(d["sr_9010"], errors="coerce").dropna().values
    L += ["## 2. Selection inflation and trial count", "",
          "Logged 1990-2010 Sharpe ratios of %d book variants: mean %.2f, sd %.2f, best %.2f." % (
              len(srs), srs.mean(), srs.std(ddof=1), srs.max())]
    e = 0.5772156649
    for N in (len(srs), 100, 300):
        z = (1 - e) * ST._norm_ppf(1 - 1 / N) + e * ST._norm_ppf(1 - 1 / (N * math.e))
        L.append("- if %d variants had been tried: expected best Sharpe from luck alone = mean + %.2f x sd = "
                 "selection inflation about %.2f" % (N, z, z * srs.std(ddof=1)))
    c9010 = ST.cut(cand, "1990-01", "2010-12")
    for N in (len(srs), 100, 300):
        L.append("- deflated Sharpe probability at N = %d (trial variance from the log): %.3f" % (
            N, ST.deflated_sr(c9010, N, srs)["dsr"]))
    L.append("")

    M = variants(R, S, D)
    p = cscv(M)
    L += ["## 3. Probability of backtest overfitting (CSCV)", "",
          "%d rebuildable variants, %d months, 16 blocks, %d in/out splits: PBO %.2f; median in-sample Sharpe of the "
          "in-sample winner %.2f, its median out-of-sample Sharpe %.2f." % (
              p["variants"], len(M), p["splits"], p["pbo"], p["is_sr"], p["oos_sr"]),
          "Variants: " + ", ".join(M.columns) + ".", ""]

    hp = holdout_power(cand)
    L += ["## 4. Power of the one-shot holdout (189 months, 2011-01..2026-09)", "",
          "| True Sharpe | P(SR >= 0.3) | P(max fall > -25%) | P(2022 > 0) | P(pass all) |", "|---|---|---|---|---|"]
    for s, v in hp.items():
        L.append("| %.1f | %.2f | %.2f | %.2f | %.2f |" % (s, v["sr>=0.3"], v["dd"], v["2022>0"], v["all"]))
    L.append("")

    R2, S2, D2 = R.copy(), {k: (v.copy() if hasattr(v, "copy") else v) for k, v in S.items()}, D.copy()
    em = [k for k in EM if k in R2.columns]
    R2.loc[:"1999-12", em] = np.nan
    for k in ("E", "C", "V"):
        cols = [c for c in em if c in S2[k].columns]
        S2[k].loc[:"1999-12", cols] = np.nan
    D2.loc[:"1999-12-31", [c for c in em if c in D2.columns]] = np.nan
    noem = net(CF.CANDIDATE, R2, S2, D2)
    L += ["## 5. Emerging markets before 2000", ""]
    for a, b in (("1975-01", "1989-12"), ("1990-01", "2010-12"), WIN):
        L.append("- %s..%s: gm-2.0 SR %.2f; without EM currencies and equities before 2000: %.2f" % (
            a[:4], b[:4], ST.sharpe(ST.cut(cand, a, b)), ST.sharpe(ST.cut(noem, a, b))))
    open(OUT, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
