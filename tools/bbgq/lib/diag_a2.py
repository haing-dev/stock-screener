"""diag_a2: the zero-slot diagnostics of TESTING_PROTOCOL 7.5 order item 2 on the A2-final book (7.6 step 4), as
registered in gm/CHANGES.md "Diagnostics after A2" (2026-11-27, before this code). Runs where the A1 panel can be built
(the user's PC: the A1 panel holds Bloomberg values); tested in the cloud on synthetic panels only.

Book: the A2 verdict was FAIL, so the A2-final book = config.A1_INCUMBENT (77374d7bef), old path, no grid, on the A1
panel (e7f98d44...), engine gm-2.2.1, design months only. Every return read is the k = 1 return (7.3 item 1).
Diagnostics (entry item 4): D1 structural half, D2, D3, D4 with the crisis table, S1 (five-state tables), D5, D6, X2,
M1, and the specs' falsifier lines (A2 item 5). Nothing is adopted. Printing (entry item 5): statistics over at least
60 months only; a smaller state, window or group is printed as its month count and the sign of its value.

API
  a2_facts(path), trial_rows_digest(path)    the A2 report facts / the book + pod rows pin of the trial log (C7)
  as_run(R, D, S, days, cfg, facts)          the A2-final book against the A2 report (raises AsRunMismatch)
  trend_pnl(R, D, S, cfg, R1)                D1 / D6 Trend P&L per market at equal risk
  d1(...), d2(...), d3(...), d4(...), d5(...), d6(...), x2(...), m1(...), falsifiers(...)
  report(R, D, S, gspc, out, ...)            the registered pass; returns the result dict (gates, trial rows)
"""
import contextlib
import csv
import hashlib
import io
import os

import numpy as np
import pandas as pd

VERSION = "diag_a2-1.0.0"
A1_PANEL_ID = "e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43"
LOCK_V2 = "d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9"
ENGINE = "gm-2.2.1"
REF_SHA = "cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39"       # engine_ref.json of gm-2.2.1
CFG_HASHES = {"BASE": "f1d682c384", "CANDIDATE": "438a092b53", "A1_INCUMBENT": "77374d7bef",
              "A2_CHALLENGER": "1faa343535"}
FINAL_NAME, FINAL_HASH = "gm-2.0.4-candidate-x1", "77374d7bef"
TRIAL_ROWS_SHA = "676b7b0f157cc6cc3e14f4e82754d5ad4c80bc61e3e9e5aa7c26596c6403e5ed"   # entry item 10 C7
TRIAL_ROWS_N = 40
A2_REPORT = "gm_a2_v1.txt"
WIN = ("1975-01", "2010-12")
ERAS = (("1975-89", "1975-01", "1989-12"), ("1990-2010", "1990-01", "2010-12"))
M1_ERAS = (("1978-89", "1978-01", "1989-12"), ("1990-2010", "1990-01", "2010-12"))
P4_FROM = "1978-01"
D3_END = "2009-12"
MIN_PRINT = 60
MIN_CELL = 6
SEED = 20261101
NBOOT = 10000
PODS = ("trend", "econ", "carry", "value")
STATES = ("<5%", "5-15% young", "5-15% old", ">15% young", ">15% old")
FOUR = ("eq_us_spx", "eq_eu_stoxx50", "eq_jp_nikkei", "eq_gb_ftse")      # protocol.py:200
DELAYS = (0, 1, 3, 6, 12)
DIAG_IDS = ("D1", "D2", "D3", "D4", "S1", "D5", "D6", "X2", "M1", "FALSIFIERS")
BLOCKED = ("D1 candidate half: not run (blocked, entry item 6a): T09 no registered data entry names a candidate series "
           "and none has a registered live source; T10 admission needs a registered live source (LSEG LIVE_START not "
           "set) and eight locked contracts (ED excluded as the dollar, FEI only); no A3 breadth item is opened by this "
           "pass",
           "S1 Fung-Hsieh part: not run (blocked, entry item 6b): factor file not obtained and locked")


class AsRunMismatch(RuntimeError):
    pass


# =====================================================================================================================
# checks of the job
# =====================================================================================================================
def trial_rows_digest(path):
    """C7: sha256 of the sorted lines 'trial|family|hash|sr_9010' (raw CSV text) of the rows with family book or pod;
    -> (sha, n, rows). Appended diag / data / fix rows do not change it."""
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r.get("family") in ("book", "pod")]
    lines = sorted("|".join([r["trial"], r["family"], r["hash"], r["sr_9010"]]) for r in rows)
    return hashlib.sha256("\n".join(lines).encode()).hexdigest(), len(rows), lines


def a2_facts(path):
    """The A2 report (job gm_a2_v1) -> (facts or None, reason). facts: book {k1, k0, d1} (1975-2010, costs x1, 3
    decimals), pods {pod: (SR, months)} (incumbent, 2 decimals), p4 (book, specific, months). None when the file is
    missing, lacks 'A2 JOB DONE', the registered A1 PANEL ID PASS line, the 'A2 VERDICT FAIL' line naming the A2-final
    book, or one of the values."""
    if not os.path.exists(path):
        return None, "missing (%s)" % os.path.basename(path)
    with open(path, encoding="utf-8", errors="replace") as f:
        L = f.read().splitlines()
    if not any(x.strip() == "A2 JOB DONE" for x in L):
        return None, "no 'A2 JOB DONE' line"
    if not any(x.startswith("PASS A1 PANEL ID %s" % A1_PANEL_ID) for x in L):
        return None, "no 'PASS A1 PANEL ID' line with the registered id"
    v = [x for x in L if x.startswith("A2 VERDICT ")]
    if len(v) != 1 or not v[0].startswith("A2 VERDICT FAIL") or \
            "A2-final book = %s (%s)" % (FINAL_NAME, FINAL_HASH) not in v[0]:
        return None, "the A2 VERDICT line is not 'FAIL ... A2-final book = %s (%s)'" % (FINAL_NAME, FINAL_HASH)
    book, pods, p4 = {}, {}, None
    for x in L:
        p = [q.strip() for q in x.split("|")]
        if len(p) >= 7 and p[0] == "BOOK" and p[1] == "incumbent" and p[3] == "costs x1" and p[4] == "1975-2010":
            book[p[2]] = float(p[6])
        if len(p) >= 4 and p[0] == "POD" and p[1] == "incumbent" and p[2] in PODS:
            a = p[3].replace("(", " ").replace(")", " ").split()
            pods[p[2]] = (float(a[0]), int(a[1]))
        if len(p) >= 4 and p[0] == "P4" and p[1] == "incumbent":
            b = p[2].replace("book", "").replace("(", " ").replace(")", " ").split()
            s = p[3].replace("specific", "").replace("(", " ").replace(")", " ").split()
            p4 = (float(b[0]), float(s[0]), int(b[1]))
    miss = [k for k in ("k1", "k0", "d1") if k not in book] + [k for k in PODS if k not in pods] + \
        ([] if p4 else ["P4"])
    if miss:
        return None, "values missing: %s" % ", ".join(miss)
    return {"book": book, "pods": pods, "p4": p4}, "ok"


# =====================================================================================================================
# runs and small statistics
# =====================================================================================================================
def _quiet(fn, *a, **kw):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*a, **kw)


def _cut(r, a, b):
    from gm import stats as ST
    return ST.cut(r, a, b)


def _sr(x):
    from gm import stats as ST
    return ST.sharpe(x)


def book_k1(R, D, S, days, cfg, cost_mult=1.0, **kw):
    from gm import execution as EX
    return _quiet(EX.run_k1, R, cfg, D, S, days, cost_mult=cost_mult, **kw)


def pod_book(R, D, S, days, cfg, mask, timing="k1", delay=0):
    """A pod or leg alone: one-part equal-risk book (gm-2.1.0 E9) at k = 1 (or the k = 0 path), delay_months = delay."""
    from gm import book as B
    c = dict(cfg, delay_months=delay) if delay else cfg
    if timing == "k1":
        return book_k1(R, D, S, days, c, parts={"alone": mask})
    return _quiet(B.run, R, cfg=c, daily=D, S=S, parts={"alone": mask})


def cell(v, n, fmt="%.2f"):
    """Printing rule (entry item 5): the value over >= 60 months, else the count and the sign only."""
    if v is None or v != v:
        return "n %d, n/a" % n
    if n >= MIN_PRINT:
        return (fmt % v) + " (%d)" % n
    return "n %d, sign %s" % (n, "+" if v > 0 else ("-" if v < 0 else "0"))


def era_sr(r, eras=ERAS):
    out = {}
    for lab, a, b in ((("1975-2010",) + WIN),) + tuple(eras):
        x = _cut(r, a, b)
        out[lab] = (_sr(x) if len(x) > 12 else float("nan"), len(x))
    return out


def fmt_eras(d):
    return " | ".join("%s %s" % (k, cell(v, n)) for k, (v, n) in d.items())


def boot_idx(T, block, n=NBOOT, seed=SEED):
    from gm import stats as ST
    return ST._stationary_idx(T, n, block, seed)


def nw_ols(y, x, lags=2):
    """OLS y = a + b x; Newey-West (Bartlett, `lags`) standard error of b, as gm.stats.nw_alpha_t's sandwich."""
    y, x = np.asarray(y, float), np.asarray(x, float)
    X = np.column_stack([np.ones(len(y)), x])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    u = y - X @ beta
    Xu = X * u[:, None]
    Sm = Xu.T @ Xu
    for L in range(1, lags + 1):
        if L >= len(y):
            break
        w = 1 - L / (lags + 1)
        G = Xu[L:].T @ Xu[:-L]
        Sm += w * (G + G.T)
    XtXi = np.linalg.inv(X.T @ X)
    V = XtXi @ Sm @ XtXi
    return float(beta[1]), float(np.sqrt(V[1, 1])), float(beta[0]), float(np.sqrt(V[0, 0]))


# =====================================================================================================================
# as-run check against the A2 report
# =====================================================================================================================
def as_run(R, D, S, days, cfg, facts, out=print):
    """The A2-final book as run (entry item 9): net Sharpe 1975-2010 at k1 / k0 / d1 (3 decimals), each pod alone at
    k = 1 (2 decimals), P4 book / specific (2 decimals) against the A2 report. Raises AsRunMismatch on a difference
    (one FAIL line, nothing else). Returns the k = 1 book."""
    import a2_batch as A2
    from gm import book as B
    bk = book_k1(R, D, S, days, cfg)
    got = {"k1": bk["net"]}
    got["k0"] = _quiet(B.run, R, cfg=cfg, daily=D, S=S)["net"]
    got["d1"] = _quiet(B.run, R, cfg=dict(cfg, delay_months=1), daily=D, S=S)["net"]
    gb = {t: round(_sr(_cut(v, *WIN)), 3) for t, v in got.items()}
    ok = all(abs(gb[t] - facts["book"][t]) < 5e-4 for t in ("k1", "k0", "d1"))
    gp = {}
    for p in PODS:
        r = _cut(pod_book(R, D, S, days, cfg, [(p, "*", "*")])["net"], *WIN)
        gp[p] = (round(_sr(r), 2), len(r))
        ok = ok and abs(gp[p][0] - facts["pods"][p][0]) < 5e-3 and gp[p][1] == facts["pods"][p][1]
    w = A2.p4(bk["net"], R["eq_us_spx"])
    pb, ps = _cut(bk["net"], P4_FROM, WIN[1]), _cut(w, P4_FROM, WIN[1])
    g4 = (round(_sr(pb), 2), round(_sr(ps), 2), len(pb))
    ok = ok and abs(g4[0] - facts["p4"][0]) < 5e-3 and abs(g4[1] - facts["p4"][1]) < 5e-3 and g4[2] == facts["p4"][2]
    line = ("%s A2-final book as run (A2 report): book %s | pods %s | P4 book %.2f specific %.2f (%d) | registered book "
            "%s | pods %s | P4 %.2f / %.2f (%d)" % (
                "PASS" if ok else "FAIL", ", ".join("%s %.3f" % kv for kv in sorted(gb.items())),
                ", ".join("%s %.2f (%d)" % (p, gp[p][0], gp[p][1]) for p in PODS), g4[0], g4[1], g4[2],
                ", ".join("%s %.3f" % kv for kv in sorted(facts["book"].items())),
                ", ".join("%s %.2f (%d)" % (p, facts["pods"][p][0], facts["pods"][p][1]) for p in PODS),
                facts["p4"][0], facts["p4"][1], facts["p4"][2]))
    out(line)
    if not ok:
        raise AsRunMismatch("the A2-final book does not reproduce the A2 report")
    return bk


# =====================================================================================================================
# D1 / D6: Trend P&L per market at equal risk
# =====================================================================================================================
def trend_markets(fam):
    """Trend's class-block markets of the book (old path family_positions) -> (all, without cm_aqr_ew)."""
    cols = []
    for c, p in fam["trend"].items():
        cols += [k for k in p.columns if k not in cols]
    return cols, [k for k in cols if k != "cm_aqr_ew"]


def trend_parts(R, D, S, cfg):
    """(family positions, vol, trend score) of the book's old path."""
    from gm import book as B
    fam, vol = B.family_positions(R, cfg, D, S)
    score = B.trend_signal(R, cfg, vol, S)
    return fam, vol, score


def trend_pnl(score, vol, R1, markets):
    """Entry item 4 D1 a: clip(score(t-1), -1, 1) x 0.40 / vol(t-1) x R1(t), before costs."""
    p = score[markets].clip(-1, 1) * 0.40 / vol[markets]
    return (p.shift(1) * R1[markets]).where(p.shift(1).notna() & R1[markets].notna())


def d1(pnl, pod_gross, classes=None):
    """D1 structural half: trailing 60-month windows ending 1979-12..2010-12, correlation PCA."""
    from gm import signals as G
    classes = classes or G.CLASSES
    ends = pd.period_range(pd.Period(WIN[0], "M") + 59, WIN[1], freq="M")
    shares, nmk, ratio = [], [], []
    cls = {c: [] for c in classes}
    skipped = 0
    for e in ends:
        w = pnl.loc[e - 59:e]
        if len(w) < 60:
            continue
        ok = [k for k in w.columns if w[k].notna().all() and w[k].std() > 0]
        if len(ok) < 3:
            continue
        X = w[ok].values
        C = np.corrcoef(X.T)
        lam, vec = np.linalg.eigh(C)
        l1, v1 = lam[-1], vec[:, -1]
        load = v1 * np.sqrt(max(l1, 0.0))
        if load.sum() < 0:
            load = -load
        shares.append(l1 / len(ok))
        nmk.append(len(ok))
        for c, pre in classes.items():
            idx = [i for i, k in enumerate(ok) if k.startswith(pre)]
            if idx:
                cls[c].append(float(load[idx].mean()))
        msr = np.mean([X[:, i].mean() / X[:, i].std(ddof=1) * np.sqrt(12) for i in range(X.shape[1])])
        pg = pod_gross.reindex(w.index)
        if msr <= 0 or pg.isna().any() or pg.std() == 0:
            skipped += 1
            continue
        ratio.append((pg.mean() / pg.std() * np.sqrt(12)) / msr)
    return {"windows": len(shares), "share": float(np.mean(shares)) if shares else float("nan"),
            "markets_mean": float(np.mean(nmk)) if nmk else float("nan"), "markets_min": min(nmk) if nmk else 0,
            "markets_max": max(nmk) if nmk else 0,
            "class_loading": {c: (float(np.mean(v)) if v else float("nan"), len(v)) for c, v in cls.items()},
            "ratio": float(np.mean(ratio)) if ratio else float("nan"), "ratio_windows": len(ratio),
            "ratio_skipped": skipped, "n_markets": pnl.shape[1]}


# =====================================================================================================================
# D2: non-signal trading
# =====================================================================================================================
def rebuild(R, D, S, cfg):
    """book.run's old path (run / _finish), position part only, keeping its intermediates."""
    from gm import book as B
    if cfg.get("grid") or cfg.get("scenario_limit") or cfg.get("cap_groups") or \
            cfg.get("within_class", "equal") != "equal":
        raise ValueError("diag_a2.rebuild: the A2-final book's form only (no grid, scenario limit, cap groups)")
    fam, vol = B.family_positions(R, cfg, D, S)
    bw = cfg.get("block_vol_months", 36)
    terms, blocks = [], {}
    total = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    for f, pos in fam.items():
        fw = B._fw(cfg, f)
        for c, p in pos.items():
            r = (p.shift(1) * R[p.columns]).sum(axis=1, min_count=1)
            k = (1.0 / (r.rolling(bw, min_periods=24).std() * np.sqrt(12))).shift(1).clip(upper=50)
            blocks[(f, c)] = r * k
            sc = p.mul(k, axis=0) * fw
            total[sc.columns] = total[sc.columns].add(sc.fillna(0), fill_value=0)
            terms.append((f, c, p, k, fw))
    active = pd.concat(blocks, axis=1).notna().any(axis=1)
    raw = (total.shift(1) * R.fillna(0)).sum(axis=1).where(active)
    s = (cfg.get("book_vol", B.VOL_TARGET) / (raw.rolling(36, min_periods=24).std() * np.sqrt(12))).shift(1)
    cap = (cfg.get("market_risk_cap", B.MARKET_RISK_CAP) * cfg.get("book_vol", B.VOL_TARGET) * 3) / vol
    gw = pd.Series({k: cfg.get("gross_weights", {}).get(k, 1.0) for k in R.columns})

    def finish(tot, s_, cap_):
        p = B.cap_positions(tot.mul(s_, axis=0), cap_, None)
        g = (p.abs() * gw).sum(axis=1)
        return p.mul((cfg.get("gross_cap", B.GROSS_CAP) / g).clip(upper=1), axis=0)
    return {"pos": finish(total, s, cap), "terms": terms, "vol": vol, "s": s, "cap": cap, "finish": finish,
            "R": R}


def held_positions(rb, hold):
    """hold = 'vol_scalers': scores at t with vol(t-1), k(t-1), s(t-1), cap from vol(t-1); 'scores': scores at t-1 with
    vol, k, s, cap at t. -> (position, invalid market-months: a held input missing where a term exists)."""
    R, vol = rb["R"], rb["vol"]
    total = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    bad = pd.DataFrame(False, index=R.index, columns=R.columns)
    for _f, _c, p, k, fw in rb["terms"]:
        cols = list(p.columns)
        q = p * vol[cols]                                   # w x 0.40 / n: the volatility-free part
        if hold == "vol_scalers":
            qq, vv, kk = q, vol[cols].shift(1), k.shift(1)
        else:
            qq, vv, kk = q.shift(1), vol[cols], k
        term = qq.div(vv).mul(kk, axis=0) * fw
        bad[cols] = bad[cols] | (qq.notna() & term.isna())
        total[cols] = total[cols].add(term.fillna(0), fill_value=0)
    if hold == "vol_scalers":
        pos = rb["finish"](total, rb["s"].shift(1), rb["cap"].shift(1))
    else:
        pos = rb["finish"](total, rb["s"], rb["cap"])
    return pos, bad


def d2(rb, book_pos):
    """D2: rebuild identity, non-signal shares by era (gate) and scores-held shares (reported)."""
    pos = rb["pos"]
    a = pos.reindex(index=book_pos.index, columns=book_pos.columns)
    diff = float((a - book_pos).abs().max().max()) if a.notna().any().any() else float("nan")
    miss = int((a.isna() != book_pos.isna()).sum().sum())
    prev = pos.shift(1)
    to = (pos - prev).abs()
    out = {"rebuild_diff": diff, "rebuild_missing": miss, "eras": {}}
    ph, bh = held_positions(rb, "vol_scalers")
    ps, bs = held_positions(rb, "scores")
    for lab, a_, b_ in ERAS:
        sel = (pos.index >= pd.Period(a_, "M")) & (pos.index <= pd.Period(b_, "M"))
        vh = (~bh & ph.notna() & pos.notna() & prev.notna())[sel]
        vs = (~bs & ps.notna() & pos.notna() & prev.notna())[sel]
        den_h = float(to[sel].where(vh).sum().sum())
        den_s = float(to[sel].where(vs).sum().sum())
        num_h = float((ph - prev).abs()[sel].where(vh).sum().sum())
        num_s = float((ps - prev).abs()[sel].where(vs).sum().sum())
        months = int(vh.any(axis=1).sum())
        out["eras"][lab] = {"share": 1 - num_h / den_h if den_h > 0 else float("nan"),
                            "scores_share": num_s / den_s if den_s > 0 else float("nan"), "months": months,
                            "left_out": int((~vh & pos[sel].notna() & prev[sel].notna() & (to[sel] > 0)).sum().sum())}
    out["open"] = all(v["share"] >= 0.20 for v in out["eras"].values())
    return out


def cost_drag(bk):
    """Per market: mean yearly cost (bp of capital) over the design months with a position (book.py costs, x1)."""
    from gm import book as B
    pos = bk["pos"]
    one = pd.Series({k: B.cost_bp(k)[0] / 1e4 for k in pos.columns})
    rolls = pd.Series({k: B.cost_bp(k)[1] for k in pos.columns})
    c = (pos.diff().abs() * one).fillna(0) + (pos.abs() * one * 2 * rolls / 12).fillna(0)   # book.py: sums skip NaN
    em = [k for k in B.EM_EQ if k in pos.columns]
    c[em] = c[em] + (pos[em].clip(upper=0).abs() * 0.01 / 12).fillna(0)
    tot_diff = float((c.sum(axis=1) - bk["cost"]).abs().max())
    sel = (pos.index >= pd.Period(WIN[0], "M")) & (pos.index <= pd.Period(WIN[1], "M"))
    held = (pos.abs() > 0) & pos.notna()
    out = {}
    for k in pos.columns:
        x = c[k][sel & held[k].values]
        if len(x):
            out[k] = (float(x.mean() * 12 * 1e4), len(x))
    return out, tot_diff


# =====================================================================================================================
# D3: book risk by state
# =====================================================================================================================
def forward_vol(r):
    x = r.copy()
    v = pd.Series(np.nan, index=x.index)
    vals = x.values
    for i in range(len(x) - 12):
        w = vals[i + 1:i + 13]
        if not np.isnan(w).any():
            v.iloc[i] = float(np.std(w, ddof=1) * np.sqrt(12))
    return v


def d3_split(fv, state):
    """Difference of mean forward volatility (named state minus other) and its one-sided 90% bootstrap lower bound."""
    j = pd.concat([fv, state.astype(float)], axis=1).dropna()
    f, s = j.iloc[:, 0].values, j.iloc[:, 1].values.astype(bool)
    if s.sum() == 0 or (~s).sum() == 0:
        return {"n": len(j), "n_state": int(s.sum()), "diff": float("nan"), "lb90": float("nan"), "open": False}
    d = float(f[s].mean() - f[~s].mean())
    idx = boot_idx(len(j), 12)
    F, Sx = f[idx], s[idx]
    ns, no = Sx.sum(axis=1), (~Sx).sum(axis=1)
    ms = np.where(ns > 0, (F * Sx).sum(axis=1) / np.where(ns > 0, ns, 1), np.nan)
    mo = np.where(no > 0, (F * ~Sx).sum(axis=1) / np.where(no > 0, no, 1), np.nan)
    db = ms - mo
    db = db[~np.isnan(db)]
    lb = float(d - np.percentile(db - d, 90))
    return {"n": len(j), "n_state": int(s.sum()), "mean_state": float(f[s].mean()), "mean_other": float(f[~s].mean()),
            "diff": d, "lb90": lb, "open": bool(d >= 0.02 and lb > 0)}


def d3(r, R, score_abs):
    fv = forward_vol(r)
    fv = fv.loc[pd.Period(WIN[0], "M"):pd.Period(D3_END, "M")]
    c12 = R["eq_us_spx"].rolling(12, min_periods=12).corr(R["bd_us_10y"])
    a = (c12 > 0).where(c12.notna())
    sa = score_abs.reindex(fv.index)
    ok = fv.notna() & sa.notna()
    thr = float(np.percentile(sa[ok].values, 90)) if ok.any() else float("nan")
    b = (sa >= thr).where(sa.notna())
    out = {"corr": d3_split(fv, a.reindex(fv.index)), "trend": d3_split(fv, b), "first": None, "last": None}
    v = fv.dropna()
    if len(v):
        out["first"], out["last"] = str(v.index[0]), str(v.index[-1])
    out["open"] = out["corr"]["open"] or out["trend"]["open"]
    return out


# =====================================================================================================================
# D4 / S1: equity-fall states, the crisis table
# =====================================================================================================================
def fall_states(x):
    """Compounded index of monthly returns x; fall from its 24-month high (t-23..t) and age (months since that high,
    the latest month at the maximum); -> DataFrame(fall, age, state)."""
    lvl = (1 + x.fillna(0)).cumprod().where(x.notna().cummax())
    v = lvl.values
    fall = np.full(len(v), np.nan)
    age = np.full(len(v), np.nan)
    for i in range(23, len(v)):
        w = v[i - 23:i + 1]
        if np.isnan(w).any():
            continue
        j = int(np.flatnonzero(w == w.max())[-1])
        fall[i] = 1 - w[-1] / w[j]
        age[i] = 23 - j
    st = pd.Series(None, index=x.index, dtype=object)
    f, a = pd.Series(fall, index=x.index), pd.Series(age, index=x.index)
    st[f < 0.05] = STATES[0]
    mid = (f >= 0.05) & (f <= 0.15)
    st[mid & (a <= 2)] = STATES[1]
    st[mid & (a > 2)] = STATES[2]
    st[(f > 0.15) & (a <= 2)] = STATES[3]
    st[(f > 0.15) & (a > 2)] = STATES[4]
    return pd.DataFrame({"fall": f, "age": a, "state": st})


def pod_contribs(bk):
    """Each pod's family contribution at k = 1 before costs, and Carry's legs (A2 convention, contrib_fam)."""
    import a2_batch as A2
    from gm import signals as G
    out = {p: A2.contrib_fam(bk, p) for p in PODS if p in bk["fam_pos"]}
    pos = bk["fam_pos"].get("carry")
    if pos is not None:
        for c, pre in G.CLASSES.items():
            cols = [k for k in pos.columns if k.startswith(pre)]
            if c != "EQ" and cols:
                out["carry/" + c] = A2.contrib_fam(bk, "carry", cols)
    return out


def state_table(contribs, states):
    sel = (states.index >= pd.Period(WIN[0], "M")) & (states.index <= pd.Period(WIN[1], "M"))
    st = states["state"][sel]
    tab = {}
    for p, r in contribs.items():
        r = r.reindex(st.index)
        tab[p] = {}
        for s in STATES:
            x = r[(st == s).values].dropna()
            tab[p][s] = (float(x.mean()) if len(x) else float("nan"), len(x))
        x = r[st.isin(STATES[3:5]).values].dropna()
        tab[p][">15% pooled"] = (float(x.mean()) if len(x) else float("nan"), len(x))
    return tab


def bad_months(R, windows):
    x = _cut(R["eq_us_spx"], *WIN)
    q = float(np.percentile(x.values, 20))
    bad = pd.Series(False, index=x.index)
    bad[x <= q] = True
    for _k, (a, b) in windows.items():
        bad[(bad.index >= pd.Period(a, "M")) & (bad.index <= pd.Period(b, "M"))] = True
    return bad


def design_windows():
    from gm import config as CF
    return {k: v for k, v in CF.STRESS_WINDOWS.items() if pd.Period(v[1], "M") <= pd.Period(WIN[1], "M")}


def d4(bk, R):
    contribs = pod_contribs(bk)
    sp = fall_states(R["eq_us_spx"])
    four = fall_states(R[[k for k in FOUR if k in R.columns]].mean(axis=1, skipna=True)
                       .where(R[[k for k in FOUR if k in R.columns]].notna().any(axis=1)))
    tab_sp, tab_4 = state_table(contribs, sp), state_table(contribs, four)
    wins = design_windows()
    win_sum = {p: {k: (float(r.loc[pd.Period(a, "M"):pd.Period(b, "M")].sum()),
                       int(r.loc[pd.Period(a, "M"):pd.Period(b, "M")].notna().sum())) for k, (a, b) in wins.items()}
               for p, r in contribs.items()}
    bad = bad_months(R, wins)
    crisis = {}
    for p, r in contribs.items():
        r = r.reindex(bad.index)
        xb, xo = r[bad.values].dropna(), r[~bad.values].dropna()
        crisis[p] = ((float(xb.mean()) if len(xb) else float("nan"), len(xb)),
                     (float(xo.mean()) if len(xo) else float("nan"), len(xo)))
    ty, n_ty = tab_sp["trend"]["5-15% young"]
    td, n_td = tab_sp["trend"][">15% pooled"]
    trend_open = bool(n_ty >= MIN_CELL and n_td >= MIN_CELL and ty < 0 and td > 0)
    c98, c08 = win_sum["carry"]["1998 LTCM"][0], win_sum["carry"]["2008 Lehman"][0]
    carry_open = bool(c98 < 0 and c08 < 0)
    return {"sp": tab_sp, "four": tab_4, "windows": win_sum, "crisis": crisis, "bad_n": int(bad.sum()),
            "n": len(bad), "trend_open": trend_open, "carry_open": carry_open, "contribs": contribs, "bad": bad,
            "wins": wins}


# =====================================================================================================================
# D5: Economic trend by delay
# =====================================================================================================================
def d5(R, D, S, days, cfg):
    out = {}
    for tm in ("k1", "k0"):
        out[tm] = {}
        for d in DELAYS:
            r = _cut(pod_book(R, D, S, days, cfg, [("econ", "*", "*")], timing=tm, delay=d)["net"], *WIN)
            out[tm][d] = (_sr(r), len(r), r)
    s0, s3 = out["k1"][0][0], out["k1"][3][0]
    out["slow"] = bool(s3 < 0.5 * s0)
    return out


# =====================================================================================================================
# D6: trend Sharpe per unit of market move
# =====================================================================================================================
def d6(pnl, R1):
    R1 = R1[pnl.columns]
    years = range(int(WIN[0][:4]), int(WIN[1][:4]) + 1)
    yx = {}
    for y in years:
        sel = pnl.index.year == y
        a, b = pnl[sel], R1[sel]
        ts, ms = [], []
        for k in pnl.columns:
            u, v = a[k], b[k]
            if u.notna().sum() == 12 and v.notna().sum() == 12 and u.std() > 0 and v.std() > 0:
                ts.append(u.mean() / u.std() * np.sqrt(12))
                ms.append(abs(v.mean() / v.std() * np.sqrt(12)))
        if len(ts) >= 3:
            yx[y] = (float(np.mean(ts)), float(np.mean(ms)), len(ts))
    out = {"years": len(yx), "eras": {}}
    for lab, a, b in ERAS:
        ys = [y for y in yx if int(a[:4]) <= y <= int(b[:4])]
        if len(ys) < 4:
            out["eras"][lab] = {"n": len(ys), "slope": float("nan"), "se": float("nan")}
            continue
        sl, se, ic, _se0 = nw_ols([yx[y][0] for y in ys], [yx[y][1] for y in ys], 2)
        out["eras"][lab] = {"n": len(ys), "slope": sl, "se": se, "intercept": ic,
                            "markets": float(np.mean([yx[y][2] for y in ys]))}
    e1, e2 = out["eras"][ERAS[0][0]], out["eras"][ERAS[1][0]]
    z = (e2["slope"] - e1["slope"]) / np.sqrt(e1["se"] ** 2 + e2["se"] ** 2)
    out["z"] = float(z)
    out["open"] = bool(abs(z) < 2)
    return out


# =====================================================================================================================
# X2 and the income / price splits
# =====================================================================================================================
def income_split(pos, cols, C, R1):
    """Held position(t-1) x C(t-1) / 12 = income, x R1(t) = total, price = total - income, over market-months with a
    position, a carry value and a return. -> (total, income, price, covered share of the gross position)."""
    cols = [k for k in cols if k in pos.columns and k in R1.columns]
    h = pos[cols].shift(1)
    c12 = C.reindex(index=pos.index, columns=cols).shift(1) / 12
    r = R1[cols].reindex(pos.index)
    ok = h.notna() & (h != 0) & c12.notna() & r.notna()
    tot = (h * r).where(ok).sum(axis=1, min_count=1)
    inc = (h * c12).where(ok).sum(axis=1, min_count=1)
    allh = h.abs().where(h.notna() & (h != 0) & r.notna())
    sel = (pos.index >= pd.Period(WIN[0], "M")) & (pos.index <= pd.Period(WIN[1], "M"))
    den = float(allh[sel].sum().sum())
    cov = float(allh.where(ok)[sel].sum().sum()) / den if den > 0 else float("nan")
    return tot, inc, tot - inc, cov


def split_stats(tot, inc, pri):
    t, i, p = (_cut(x, *WIN) for x in (tot, inc, pri))
    j = pd.concat([t, i, p], axis=1).dropna()
    out = {"n": len(j), "total": float(j.iloc[:, 0].mean() * 12) if len(j) else float("nan"),
           "income": float(j.iloc[:, 1].mean() * 12) if len(j) else float("nan"),
           "price": float(j.iloc[:, 2].mean() * 12) if len(j) else float("nan")}
    if len(j) >= 24:
        x = j.iloc[:, 2].values
        bm = x[boot_idx(len(x), 6)].mean(axis=1) * 12
        out["ci90"] = (float(np.percentile(bm, 5)), float(np.percentile(bm, 95)))
    else:
        out["ci90"] = (float("nan"), float("nan"))
    return out


def x2(bk, C, R1):
    from gm import signals as G
    pos = bk["fam_pos"]["value"]
    out = {}
    for leg in ("EQ", "FI", "FX"):
        cols = [k for k in pos.columns if k.startswith(G.CLASSES[leg])]
        tot, inc, pri, cov = income_split(pos, cols, C, R1)
        s = split_stats(tot, inc, pri)
        s["covered"] = cov
        s["exact"] = float((inc + pri - tot).abs().max()) if tot.notna().any() else 0.0
        s["paid_by_income"] = bool(s["n"] > 0 and s["price"] <= 0)
        out[leg] = s
    return out


# =====================================================================================================================
# M1: the P4 market set
# =====================================================================================================================
def p4_multi(r, M, start=WIN[0], first=37):
    """P4 with several markets: w(t) = r(t) - b(t)' m(t), b(t) = least-squares slopes with intercept of r on the columns
    of M over the common months from `start` to t - 1; first value in month `first`. Point in time."""
    j = pd.concat([r.rename("r"), M], axis=1).loc[pd.Period(start, "M"):]
    w = pd.Series(np.nan, index=j.index)
    t0 = pd.Period(start, "M") + (first - 1)
    for t in j.index:
        if t < t0 or j.loc[t].isna().any():
            continue
        past = j.loc[:t - 1].dropna()
        if len(past) < M.shape[1] + 2:
            continue
        X = np.column_stack([np.ones(len(past)), past[M.columns].values])
        b = np.linalg.lstsq(X, past["r"].values, rcond=None)[0]
        w[t] = j.at[t, "r"] - float(np.dot(b[1:], j.loc[t, M.columns].values.astype(float)))
    return w


def m1(r, R):
    import a2_batch as A2
    w1 = A2.p4(r, R["eq_us_spx"])
    w2 = p4_multi(r, R[["eq_us_spx", "bd_us_10y"]])
    out = {"eras": {}}
    for lab, a, b in (("1978-2010", P4_FROM, WIN[1]),) + M1_ERAS:
        x = [_cut(s, a, b) for s in (r, w1, w2)]
        out["eras"][lab] = {"n": len(x[1]), "book": _sr(x[0]), "spx": _sr(x[1]), "both": _sr(x[2])}
    out["both"] = any(out["eras"][lab]["both"] <= out["eras"][lab]["spx"] - 0.05 for lab, _a, _b in M1_ERAS)
    return out


# =====================================================================================================================
# falsifier lines (A2 item 5; specs s10)
# =====================================================================================================================
def theme_split(bk, E, ET, R1):
    """Economic trend's held position split into theme parts: held x (theme score / themes present) / E (exact where E is
    the mean of the present parts); E = 0 holds nothing. -> (contribution per theme, max |sum of parts - held|, max |mean
    of the theme scores - E|)."""
    held = bk["fam_pos"]["econ"]
    cols = [k for k in held.columns if k in E.columns and all(k in ET[t].columns for t in ET)]
    E = E.reindex(index=held.index, columns=cols)
    T = {t: ET[t].reindex(index=held.index, columns=cols) for t in ET}
    npres = sum(T[t].notna().astype(int) for t in T)
    mean_t = sum(T[t].fillna(0) for t in T) / npres.where(npres > 0)
    e_diff = float((mean_t - E).abs().where(E.notna()).max().max()) if E.notna().any().any() else float("nan")
    scale = (held[cols] / E).where((E != 0) & E.notna())
    parts = {t: (scale * T[t] / npres.where(npres > 0)).fillna(0) for t in T}
    hc = held[cols].fillna(0)
    sdiff = float((sum(parts.values()) - hc).abs().where(hc != 0, 0).max().max())
    contrib = {t: (p.shift(1) * R1[cols].reindex(held.index)).sum(axis=1, min_count=1)
               .where(p.shift(1).abs().sum(axis=1) > 0) for t, p in parts.items()}
    return contrib, sdiff, e_diff


def falsifiers(R, D, S, days, cfg, bk, d4r, d5r, ET=None):
    from gm import book as B
    from gm import signals as G
    R1 = bk["R_earn"]
    out = {}
    pods = {p: era_sr(pod_book(R, D, S, days, cfg, [(p, "*", "*")])["net"]) for p in ("trend", "carry", "value")}
    pods["econ"] = era_sr(d5r["k1"][0][2])
    legs = {}
    for c in ("FX", "FI", "CM"):
        b = pod_book(R, D, S, days, cfg, [("carry", c, "*")])
        legs[c] = (era_sr(b["net"]), b)

    def both_le0(d):
        return all(d[e][0] <= 0 for e, _a, _b in ERAS)
    out["T1"] = (pods["trend"], both_le0(pods["trend"]))
    td = d4r["sp"]["trend"][">15% pooled"]
    out["T2"] = (td, bool(td[1] >= 1 and td[0] <= 0))
    out["C1"] = ({"pod": pods["carry"], **{c: legs[c][0] for c in legs}},
                 both_le0(pods["carry"]) or any(both_le0(legs[c][0]) for c in legs))
    cr = d4r["crisis"].get("carry/FX")
    out["C2"] = (cr, bool(cr is not None and cr[0][0] >= cr[1][0]))
    pos = bk["fam_pos"]["carry"]
    cm = [k for k in pos.columns if k.startswith("cm_")]
    h = pos[cm].shift(1)
    lg = (h.where(h > 0) * R1[cm]).sum(axis=1, min_count=1).where((h > 0).any(axis=1))
    lgx = _cut(lg, *WIN)
    out["C3"] = ((float(lgx.mean() * 12) if len(lgx) else float("nan"), len(lgx)),
                 bool(len(lgx) > 0 and lgx.mean() <= 0))
    fb = legs["FI"][1]
    fpos = fb["pos"]
    fi = [k for k in fpos.columns if k.startswith(G.CLASSES["FI"]) and (fpos[k].abs() > 0).any()]
    const = pd.DataFrame(0.0, index=fpos.index, columns=fi)
    for k in fi:
        hold = (fpos[k].abs() > 0) & fpos[k].notna()
        sel = hold & (fpos.index >= pd.Period(WIN[0], "M")) & (fpos.index <= pd.Period(WIN[1], "M"))
        const.loc[hold, k] = float(fpos[k][sel].mean()) if sel.any() else 0.0
    one = pd.Series({k: B.cost_bp(k)[0] / 1e4 for k in fi})
    rolls = pd.Series({k: B.cost_bp(k)[1] for k in fi})
    cg = (const.shift(1) * fb["R_earn"][fi]).sum(axis=1, min_count=1)
    cnet = cg - (const.abs() * one * 2 * rolls / 12).sum(axis=1).shift(1)
    j = pd.concat([_cut(fb["net"], *WIN), _cut(cnet, *WIN)], axis=1).dropna()
    out["C4"] = ((float(j.iloc[:, 0].mean() * 12), float(j.iloc[:, 1].mean() * 12), len(j)) if len(j) else
                 (float("nan"), float("nan"), 0), bool(len(j) > 0 and j.iloc[:, 0].mean() <= j.iloc[:, 1].mean()))
    c5 = {}
    for c in ("FX", "FI", "CM"):
        cols = [k for k in pos.columns if k.startswith(G.CLASSES[c])]
        tot, inc, pri, cov = income_split(pos, cols, S["C"], R1)
        s = split_stats(tot, inc, pri)
        s["covered"] = cov
        s["holds"] = bool(s["n"] > 0 and (s["income"] <= 0 or s["price"] > s["income"]))
        c5[c] = s
    out["C5"] = (c5, any(v["holds"] for v in c5.values()))
    out["V1"] = (pods["value"], both_le0(pods["value"]))
    out["E1"] = (pods["econ"], both_le0(pods["econ"]))
    if ET is not None:
        contrib, sdiff, ediff = theme_split(bk, S["E"], ET, R1)
        th = {t: {lab: (float(_cut(r, a, b).mean() * 12) if len(_cut(r, a, b)) else float("nan"),
                        len(_cut(r, a, b))) for lab, a, b in ERAS} for t, r in contrib.items()}
        others = [t for t in th if t != "inflation"]
        oth = {lab: sum(th[t][lab][0] for t in others) for lab, _a, _b in ERAS}
        holds = bool("inflation" in th and all(th["inflation"][lab][0] <= 0 for lab, _a, _b in ERAS) and
                     all(oth[lab] > 0 for lab, _a, _b in ERAS))
        out["E3"] = ({"themes": th, "others": oth, "sum_diff": sdiff, "e_diff": ediff}, holds)
    else:
        out["E3"] = (None, None)
    return out


# =====================================================================================================================
# the registered report
# =====================================================================================================================
def report(R, D, S, gspc, out=print, cfg=None, ET=None, facts=None):
    """The registered pass (entry items 3-8). R, S: the A1 panel; D, gspc: free daily inputs; ET: theme scores of the
    A1 panel (None: the theme split is not computed); facts: the A2 report facts (None = no as-run check, tests).
    Returns dict(gates, trial rows data, results)."""
    from gm import config as CF
    from gm import execution as EX
    from gm import seal as SL
    from gm import signals as G
    cfg = cfg or CF.A1_INCUMBENT
    T = SL.resolve(SL.DESIGN)
    R, D, S, gspc, ET = SL.cut_inputs(T, R, D, S, gspc, ET)
    SL.check_output({"R": R, "S": S}, T, "diag_a2.report inputs")
    days = EX.nyse_days(gspc=gspc)
    if facts:
        bk = as_run(R, D, S, days, cfg, facts, out)
    else:
        bk = book_k1(R, D, S, days, cfg)
    SL.check_output(bk["net"], T, "diag_a2.report")
    R1 = bk["R_earn"]
    out("--- DIAGNOSTICS AFTER A2 (TESTING_PROTOCOL 7.6 step 4, 7.5 order item 2; gm/CHANGES.md \"Diagnostics after "
        "A2\"): A2-final book %s (%s), A1 panel, k = 1, design months %s..%s; zero slots, nothing adopted; values over "
        "fewer than 60 months are printed as count and sign" % (cfg["name"], CF.cfg_hash(cfg), WIN[0], WIN[1]))
    for b in BLOCKED:
        out("BLOCKED | " + b)
    res = {}
    # ---- D1
    fam, vol, score = trend_parts(R, D, S, cfg)
    allm, mk = trend_markets(fam)
    pnl = trend_pnl(score, vol, R1, mk)
    podg = pod_book(R, D, S, days, cfg, [("trend", "*", "*")])["gross"]
    r1 = d1(pnl, podg)
    res["D1"] = r1
    out("D1 | structural half | markets %d (Trend's book markets without cm_aqr_ew) | windows %d (60 months, ending "
        "1979-12..2010-12) | markets per window mean %.1f, min %d, max %d" % (
            r1["n_markets"], r1["windows"], r1["markets_mean"], r1["markets_min"], r1["markets_max"]))
    out("D1 | first-factor share of variance (correlation PCA), averaged over windows | %.3f" % r1["share"])
    out("D1 | class mean loading on the first factor, averaged over windows | %s" % " | ".join(
        "%s %.2f (%d windows)" % (c, v, n) if n else "%s none" % c for c, (v, n) in r1["class_loading"].items()))
    out("D1 | Trend pod alone (gross, k = 1) Sharpe over the mean market P&L Sharpe, averaged over windows | %.2f "
        "(%d windows; %d skipped: mean market Sharpe <= 0 or a pod month missing)" % (
            r1["ratio"], r1["ratio_windows"], r1["ratio_skipped"]))
    out("D1 | candidate half | not run (BLOCKED above) | gate not evaluated; A3 breadth item not opened by this pass")
    # ---- D2
    rb = rebuild(R, D, S, cfg)
    r2 = d2(rb, bk["pos"])
    res["D2"] = r2
    okr = r2["rebuild_diff"] <= 1e-12 and r2["rebuild_missing"] == 0
    out("D2 | rebuild of the book's positions from their intermediates | max abs diff %.1e | missing pattern diff %d | "
        "%s" % (r2["rebuild_diff"], r2["rebuild_missing"], "PASS" if okr else "FAIL"))
    for lab, v in r2["eras"].items():
        out("D2 | %s | trade months %d | non-signal share (1 - turnover with vols and scalers held / actual) %s | "
            "scores-held share %s | market-months left out %d" % (
                lab, v["months"], cell(v["share"], v["months"], "%.3f"), cell(v["scores_share"], v["months"], "%.3f"),
                v["left_out"]))
    r2["open"] = bool(okr and r2["open"])
    out("D2 GATE | non-signal share >= 0.20 in both eras | %s | %s" % (
        "OPEN" if r2["open"] else "closed", "-> A3 no-trade buffer item" if r2["open"] else "-> buffer item dropped"))
    cd, cdd = cost_drag(bk)
    out("D2 | cost drag per market (bp of capital per year, months with a position; costs x1) | check: market costs sum "
        "to the book's cost (max diff %.1e)" % cdd)
    for k in sorted(cd):
        out("COSTDRAG | %s | %s" % (k, cell(cd[k][0], cd[k][1], "%.1f")))
    # ---- D3
    sabs = score[allm].abs().mean(axis=1, skipna=True).where(score[allm].notna().any(axis=1))
    r3 = d3(bk["net"], R, sabs)
    res["D3"] = r3
    out("D3 | state months %s..%s (forward 12-month windows end by 2010-12) | book net k = 1" % (r3["first"], r3["last"]))
    for lab, key in (("(a) stock-bond 12-month correlation > 0", "corr"), ("(b) top tenth of mean |trend score|", "trend")):
        v = r3[key]
        ms = cell(v.get("mean_state", float("nan")) * 100, v["n_state"], "%.1f")
        mo = cell(v.get("mean_other", float("nan")) * 100, v["n"] - v["n_state"], "%.1f")
        out("D3 | %s | months %d, in state %d | forward vol %%/yr: state %s, other %s | difference %+.2f pts | one-sided "
            "90%% bound %+.2f pts | %s" % (lab, v["n"], v["n_state"], ms, mo, v["diff"] * 100, v["lb90"] * 100,
                                           "OPEN" if v["open"] else "closed"))
    out("D3 GATE | difference >= 2 points and bound > 0 in either split | %s | %s" % (
        "OPEN" if r3["open"] else "closed",
        "-> A3 faster book scaler item" if r3["open"] else "-> scaler item dropped"))
    # ---- D4 / S1
    r4 = d4(bk, R)
    res["D4"] = r4
    out("D4 | S&P base (eq_us_spx), fall from the 24-month high and age | mean monthly contribution %, k = 1, before "
        "costs, per state (months)")
    for p in ("trend", "carry"):
        out("D4 | %s | %s | >15%% pooled %s" % (p, " | ".join("%s %s" % (s, cell(r4["sp"][p][s][0] * 100,
                                                                                   r4["sp"][p][s][1]))
                                                              for s in STATES),
                                                 cell(r4["sp"][p][">15% pooled"][0] * 100,
                                                      r4["sp"][p][">15% pooled"][1])))
    for k, (a, b) in r4["wins"].items():
        out("D4 | stress window %s %s..%s | %s" % (k, a, b, " | ".join(
            "%s n %d sign %s" % (p, r4["windows"][p][k][1], "+" if r4["windows"][p][k][0] > 0 else
                                 ("-" if r4["windows"][p][k][0] < 0 else "0")) for p in PODS if p in r4["windows"])))
    out("D4 GATE | Trend: mean < 0 in 5-15%% young and > 0 in >15%% (cells >= 6 months) | %s | %s" % (
        "OPEN" if r4["trend_open"] else "closed",
        "-> SPEC_Trend s10 line 'young, shallow equity fall'" if r4["trend_open"] else "-> no such line"))
    out("D4 GATE | Carry: loses in both 1998 LTCM and 2008 Lehman | %s | %s" % (
        "OPEN" if r4["carry_open"] else "closed",
        "-> SPEC_Carry s11 stop state 'funding break'" if r4["carry_open"] else "-> dropped"))
    out("CRISIS | one shared bad-state set: %d design STRESS_WINDOWS + worst fifth of eq_us_spx months 1975-2010 = %d of "
        "%d months | mean monthly contribution %% in bad | other" % (len(r4["wins"]), r4["bad_n"], r4["n"]))
    for p, (b, o) in r4["crisis"].items():
        out("CRISIS | %s | bad %s | other %s" % (p, cell(b[0] * 100, b[1]), cell(o[0] * 100, o[1])))
    out("S1 | five-state equity tables (mean monthly contribution %, k = 1, before costs; reported only)")
    for base, tab in (("S&P", r4["sp"]), ("four-market average", r4["four"])):
        for p in PODS:
            if p in tab:
                out("S1 | %s | %s | %s" % (base, p, " | ".join("%s %s" % (s, cell(tab[p][s][0] * 100, tab[p][s][1]))
                                                               for s in STATES)))
    # ---- D5
    r5 = d5(R, D, S, days, cfg)
    res["D5"] = r5
    for tm in ("k1", "k0"):
        out("D5 | Economic trend alone, net, %s | %s" % (
            "k = 1 (gate)" if tm == "k1" else "k = 0 path (reported)",
            " | ".join("delay %d: %s" % (d, cell(r5[tm][d][0], r5[tm][d][1])) for d in DELAYS)))
    out("D5 | caution (charter JP8): at 3 months' delay 9 of the 12 months of the 12-month inputs overlap")
    out("D5 GATE | Sharpe at 3 months' delay < half the no-delay Sharpe (k = 1) | %s | claim %s" % (
        "YES" if r5["slow"] else "no", "'slow reaction' (falsifier: no fading with delay)" if r5["slow"] else
        "'a lasting macro state'"))
    # ---- D6
    r6 = d6(pnl, R1)
    res["D6"] = r6
    for lab, v in r6["eras"].items():
        out("D6 | %s | years %d | slope of mean trend Sharpe on mean |market Sharpe| %+.3f | NW se (2 lags) %.3f" % (
            lab, v["n"], v["slope"], v["se"]))
    out("D6 GATE | |slope difference| < 2 standard errors | z %+.2f | %s | %s" % (
        r6["z"], "OPEN" if r6["open"] else "closed",
        "-> Trend breakdown check line registered" if r6["open"] else "-> dropped"))
    # ---- X2
    rx = x2(bk, S["C"], R1)
    res["X2"] = rx
    for leg, v in rx.items():
        out("X2 | Value %s | covered share %.3f | months %d | %%/yr total %s, income %s, price %s | price 90%% interval "
            "%s | income + price = total (max diff %.1e) | %s" % (
                leg, v["covered"], v["n"], cell(v["total"] * 100, v["n"]), cell(v["income"] * 100, v["n"]),
                cell(v["price"] * 100, v["n"]), ("%+.2f..%+.2f" % (v["ci90"][0] * 100, v["ci90"][1] * 100))
                if v["n"] >= MIN_PRINT else "n<60", v["exact"], "PAID BY INCOME" if v["paid_by_income"] else
                "price part > 0"))
    out("X2 GATE | price part <= 0 on the leg's averaged position | %s" % ", ".join(
        "%s %s" % (leg, "'paid by income' entry" if v["paid_by_income"] else "no entry") for leg, v in rx.items()))
    # ---- M1
    rm = m1(bk["net"], R)
    res["M1"] = rm
    for lab, v in rm["eras"].items():
        out("M1 | %s | months %d | Sharpe book %.2f | specific, S&P alone %.2f | specific, S&P and US 10-year %.2f" % (
            lab, v["n"], v["book"], v["spx"], v["both"]))
    out("M1 GATE | two-market Sharpe lower by >= 0.05 in either era (1978-89, 1990-2010) | %s | P4 uses %s" % (
        "YES" if rm["both"] else "no", "the S&P 500 and the US 10-year" if rm["both"] else "the S&P 500 alone"))
    # ---- falsifier lines
    fz = falsifiers(R, D, S, days, cfg, bk, r4, r5, ET)
    res["FALSIFIERS"] = fz

    def hl(x):
        return "n/a" if x is None else ("HOLDS" if x else "does not hold")
    out("--- falsifier lines (specs s10, A2 item 5; reported only): each 'holds' or 'does not hold'")
    out("FALSIFIER | Trend 1 | pod alone net Sharpe <= 0 in both eras | %s | %s" % (fmt_eras(fz["T1"][0]), hl(fz["T1"][1])))
    out("FALSIFIER | Trend 2 | >15%% S&P falls: mean Trend contribution <= 0 | %s %% | %s" % (
        cell(fz["T2"][0][0] * 100, fz["T2"][0][1]), hl(fz["T2"][1])))
    out("FALSIFIER | Trend 3, 4 | carry / price and class-average / relative splits | read at A2 on this book "
        "(gm_a2_v1 CARRYPRICE and SPLIT lines, incumbent); not recomputed")
    out("FALSIFIER | Carry 1 | pod or a leg alone net Sharpe <= 0 in both eras | %s | %s" % (
        " || ".join("%s: %s" % (k, fmt_eras(v)) for k, v in fz["C1"][0].items()), hl(fz["C1"][1])))
    c2 = fz["C2"][0]
    out("FALSIFIER | Carry 2 | FX leg mean contribution in bad months not below other months | %s | %s" % (
        "bad %s %%, other %s %%" % (cell(c2[0][0] * 100, c2[0][1]), cell(c2[1][0] * 100, c2[1][1])) if c2 else "n/a",
        hl(fz["C2"][1])))
    out("FALSIFIER | Carry 3 | CM long side mean contribution <= 0 | %s %%/yr | %s" % (
        cell(fz["C3"][0][0] * 100, fz["C3"][0][1]), hl(fz["C3"][1])))
    c4 = fz["C4"][0]
    out("FALSIFIER | Carry 4 | FI leg alone net mean <= constant-position net mean | leg %s, constant %s %%/yr | %s" % (
        cell(c4[0] * 100, c4[2]), cell(c4[1] * 100, c4[2]), hl(fz["C4"][1])))
    for c, v in fz["C5"][0].items():
        out("FALSIFIER | Carry 5 | %s | covered share %.3f | %%/yr income %s, price %s | income <= 0 or price > income | "
            "%s" % (c, v["covered"], cell(v["income"] * 100, v["n"]), cell(v["price"] * 100, v["n"]), hl(v["holds"])))
    out("FALSIFIER | Value 1 | pod alone net Sharpe <= 0 in both eras | %s | %s" % (fmt_eras(fz["V1"][0]),
                                                                                     hl(fz["V1"][1])))
    out("FALSIFIER | Value 2 | = X2 above | Value 3 | Value against Trend's relative part: read at A2 (VALUE lines)")
    out("FALSIFIER | Economic trend 1 | pod alone net Sharpe <= 0 in both eras | %s | %s" % (fmt_eras(fz["E1"][0]),
                                                                                              hl(fz["E1"][1])))
    e3 = fz["E3"][0]
    if e3 is None:
        out("FALSIFIER | Economic trend 3 | theme split | not computed (no theme scores)")
    else:
        out("FALSIFIER | Economic trend 3 | theme split check: parts sum to the held position (max diff %.1e); theme "
            "scores reproduce the score E (max diff %.1e)" % (e3["sum_diff"], e3["e_diff"]))
        for t, v in e3["themes"].items():
            out("FALSIFIER | Economic trend 3 | %s part %%/yr | %s" % (t, " | ".join(
                "%s %s" % (lab, cell(m * 100, n)) for lab, (m, n) in v.items())))
        out("FALSIFIER | Economic trend 3 | inflation <= 0 in both eras while the other three earn | %s" % hl(fz["E3"][1]))
    out("FALSIFIER | loss-event lines (P3) | text only; nothing computed")
    gates = {"D1": "candidate half blocked; structural half reported", "D2": "OPEN" if r2["open"] else "closed",
             "D3": "OPEN" if r3["open"] else "closed", "D4": "Trend %s, Carry %s" % (
                 "OPEN" if r4["trend_open"] else "closed", "OPEN" if r4["carry_open"] else "closed"),
             "S1": "reported", "D5": "slow reaction" if r5["slow"] else "lasting macro state",
             "D6": "OPEN" if r6["open"] else "closed",
             "X2": ", ".join("%s %s" % (k, "paid by income" if v["paid_by_income"] else "no entry")
                             for k, v in rx.items()),
             "M1": "S&P and US 10-year" if rm["both"] else "S&P alone",
             "FALSIFIERS": ", ".join("%s %s" % (k, hl(v[1])) for k, v in fz.items())}
    out("DIAG SUMMARY | %s" % " | ".join("%s: %s" % (k, gates[k]) for k in DIAG_IDS))
    res["gates"] = gates
    return res


def trial_rows(res, panel_id_, engine_version, cfg=None):
    """gm/trials.csv rows of family 'diag', one per diagnostic run (entry item 8), no Sharpe columns."""
    import json
    from gm import config as CF
    cfg = cfg or CF.A1_INCUMBENT
    rows = []
    for d in DIAG_IDS:
        c = {"diag": d, "version": VERSION, "book": CF.cfg_hash(cfg), "panel": panel_id_[:16], "timing": "k1",
             "window": list(WIN)}
        rows.append({"trial": "%s diagnostic (A2-final book)" % d, "family": "diag", "hash": CF.cfg_hash(c),
                     "note": "TESTING_PROTOCOL 7.5 %s, 7.6 step 4, gm/CHANGES.md 'Diagnostics after A2'; engine %s; A1 "
                             "panel %s; LOCK_v2 %s; book %s (%s); outcome: %s" % (
                                 d, engine_version, panel_id_[:16], LOCK_V2[:16], cfg["name"], CF.cfg_hash(cfg),
                                 res["gates"][d]),
                     "config": json.dumps(c, sort_keys=True)})
    return rows
