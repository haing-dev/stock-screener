"""core_v1: Core book v1 (TESTING_PROTOCOL 7.6 step 6), as registered in gm/CHANGES.md "Core book v1" (2026-11-27,
before this code). Runs where the A1 panel can be built (the user's PC: it holds Bloomberg values); tested in the cloud
on synthetic panels and mock stores only.

Book: the final Batch A book = the A2-final book config.A1_INCUMBENT (77374d7bef), engine gm-2.2.1, A1 panel
e7f98d44..., design months 1975-01..2010-12, k = 1 (entry items 2-3).
Core candidates (config.CORE_PARTS): trend, carry (FX v2 + energy v1, v2), value (EQ). For each, on its window
(months 1975-01..2010-12 with a net return of the part alone; >= 120): S1 placebo (7.7 T3), S2 net mean at twice the
costs > 0, S3 tail test 5 of the candidate Core book with / without the part (both as run), S4 the independent rebuild
(tools/bbgq/lib/rebuild_s4.py, docs/research/batches/S4_INTERFACE.md) within 15% relative on net Sharpe and mean, and
the free live-source check (entry item 4f). Core = all pass. Core book v1 = the Core parts at equal risk (E9).
Reported: leave-one-out alpha with its bootstrap p. Incubator rule (7.7) for the shadow parts (config.SHADOW_PARTS) and
any candidate that is not Core, against Core book v1. Printing (entry item 5): statistics over >= 60 months only.

API
  diag_facts(path)                              gm_diag_v1 report: DIAG JOB DONE and the A3-empty summary
  raw_from_engine(M, free, a1, store)           interface v2 raw inputs from the engine's loaders (no signal code)
  raw_check(raw, S)                             the raw inputs reproduce the engine's carry / value measures exactly
  rebuild_inputs(R, D, days, raw, meta)         the dict of S4_INTERFACE.md v2 section 2
  forbidden_imports(path)                       rebuild source scan (interface section 3 item 1)
  validate_rebuild(out)                         interface section 3 items 2-3 -> (ok, why)
  report(R, D, S, gspc, free, rb, out, ...)     the registered run; returns the result dict
  trial_row(res, panel_id, engine_version)      the one gm/trials.csv row of family 'book'
"""
import contextlib
import copy
import io
import os
import re

import numpy as np
import pandas as pd

VERSION = "core_v1-1.1.0"   # 1.1.0 (CHECK_CORE): interface v2 raw inputs, raw check; C1
A1_PANEL_ID = "e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43"
LOCK_V2 = "d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9"
ENGINE = "gm-2.2.1"
REF_SHA = "cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39"       # engine_ref.json of gm-2.2.1
CFG_HASHES = {"BASE": "f1d682c384", "CANDIDATE": "438a092b53", "A1_INCUMBENT": "77374d7bef",
              "A2_CHALLENGER": "1faa343535"}
FINAL_NAME, FINAL_HASH = "gm-2.0.4-candidate-x1", "77374d7bef"
TRIAL_ROWS_SHA = "676b7b0f157cc6cc3e14f4e82754d5ad4c80bc61e3e9e5aa7c26596c6403e5ed"   # book / pod rows (entry item 7)
TRIAL_ROWS_N = 40
A2_REPORT = "gm_a2_v1.txt"
DIAG_REPORT = "gm_diag_v1.txt"
DIAG_NEEDS = ("D1: candidate half blocked", "D2: closed", "D3: closed")        # A3 empty (gm/CHANGES.md "A3: empty")
WIN = ("1975-01", "2010-12")
ERAS = (("1975-2010", "1975-01", "2010-12"), ("1975-89", "1975-01", "1989-12"), ("1990-2010", "1990-01", "2010-12"))
P4_FROM = "1978-01"
LAST_DECISION = "2010-12"
MIN_PRINT = 60
MIN_WINDOW = 120
S4_TOL = 0.15
SEED = 20261101
NBOOT = 10000
NPLACEBO = 1000
LAMBDA = 0.5
CORE = ("trend", "carry", "value")
SHADOW = ("econ", "carry_shadow", "value_shadow")
LABEL = {"trend": "Trend (all classes)", "carry": "Carry currencies v2 + energy", "value": "Value equities",
         "econ": "Economic trend", "carry_shadow": "Carry currencies v1 + bonds",
         "value_shadow": "Value bonds + currencies", "carry_fx_v2": "Carry currencies v2 alone",
         "carry_energy": "Carry energy v1 + v2 alone"}
MEASURE = {"trend": None, "carry": "C", "value": "V"}       # entry item 4f: the measure a live run of the part reads
REBUILD_KEY = {"trend": "trend", "carry": "carry", "value": "value_eq"}               # decisive (interface s1)
REBUILD_REPORTED = ("carry_fx_v2", "carry_energy")
FORBIDDEN = ("gm", "gm_engine", "a1_panel", "a2_batch", "diag_a2", "core_v1", "bbgdata", "bbg_panel")


class AsRunMismatch(RuntimeError):
    pass


def masks():
    """Part name -> mask (config.CORE_PARTS / SHADOW_PARTS; entry item 3) and the two reported Carry legs."""
    from gm import config as CF
    m = {"trend": CF.CORE_PARTS["trend"], "carry": CF.CORE_PARTS["carry"], "value": CF.CORE_PARTS["value"],
         "econ": CF.SHADOW_PARTS["econ"], "carry_shadow": CF.SHADOW_PARTS["carry"],
         "value_shadow": CF.SHADOW_PARTS["value"],
         "carry_fx_v2": [("carry", "FX", 2)], "carry_energy": [("carry", "CM", 1), ("carry", "CM", 2)]}
    return {k: [tuple(x) for x in v] for k, v in m.items()}


# =====================================================================================================================
# checks of the job
# =====================================================================================================================
def diag_facts(path):
    """The diagnostics report (job gm_diag_v1) -> (ok, reason): 'DIAG JOB DONE' and a DIAG SUMMARY line holding every
    item of DIAG_NEEDS (A3 empty: D1 candidate half blocked, D2 and D3 closed)."""
    if not os.path.exists(path):
        return False, "missing (%s)" % os.path.basename(path)
    with open(path, encoding="utf-8", errors="replace") as f:
        L = f.read().splitlines()
    if not any(x.strip() == "DIAG JOB DONE" for x in L):
        return False, "no 'DIAG JOB DONE' line"
    s = [x for x in L if x.startswith("DIAG SUMMARY |")]
    if len(s) != 1:
        return False, "not exactly one DIAG SUMMARY line"
    miss = [n for n in DIAG_NEEDS if n not in s[0]]
    if miss:
        return False, "DIAG SUMMARY lacks: %s" % ", ".join(miss)
    return True, "ok"


def forbidden_imports(path):
    """Interface section 3 item 1: module names from FORBIDDEN that the rebuild's source imports (import x / from x
    import / import x.y / from x.y import)."""
    with open(path, encoding="utf-8", errors="replace") as f:
        src = f.read()
    found = set()
    for m in re.finditer(r"^\s*(?:from\s+([A-Za-z_][\w\.]*)\s+import|import\s+([A-Za-z_][\w\., ]*))", src, re.M):
        names = [m.group(1)] if m.group(1) else [x.strip().split(" ")[0] for x in m.group(2).split(",")]
        for n in names:
            top = n.split(".")[0]
            if top in FORBIDDEN:
                found.add(top)
    for m in re.finditer(r"(?:__import__|import_module)\(\s*['\"]([\w\.]+)['\"]", src):
        if m.group(1).split(".")[0] in FORBIDDEN:
            found.add(m.group(1).split(".")[0])
    return sorted(found)


RATE_COLS = ("US", "EZ", "JP", "GB", "CH", "AU", "NZ", "CA", "SE", "NO", "MX", "BR", "KR", "ZA")
ENERGY = ("cm_wti", "cm_natgas", "cm_heatoil", "cm_gasoline")
FRENCH = ("eq_de_dax", "eq_gb_ftse", "eq_fr_cac", "eq_jp_nikkei", "eq_ca_tsx", "eq_au_asx", "eq_hk_hsi")
RAW_KEYS = ("rate3m", "fx_rate_country", "eia", "french_with", "french_without", "us_total", "us_price")
INPUT_KEYS = ("R", "D", "days") + RAW_KEYS + ("cost", "em_borrow", "classes", "meta")


def raw_from_engine(M, free, a1=None, store=None):
    """Interface v2 section 2: the RAW month-end inputs as the engine's loaders return them (gm.panel rate3m,
    eia_curve; gm.signals _french_mkt; SPY / ^GSPC monthly returns), every loader cut at 2010-12-31, outputs cut at the
    seal; the A1 block-2 contract extension applied to the EIA contracts exactly as a1_panel.build applies it (a1 and
    store given). No signal or volatility code is run."""
    import a1_panel as A1
    import gm_engine as GE
    from gm import seal as SL
    P, G = M["P"], M["G"]
    with GE.Cut(M, A1.SEAL), contextlib.redirect_stdout(io.StringIO()):
        rate = pd.DataFrame({c: P.rate3m(c) for c in RATE_COLS}).reindex(P.GRID)
        fw = pd.DataFrame({k: G._french_mkt("french_intl_countries_ff.zip", G.FRENCH_DY[k]) for k in FRENCH})
        fx = pd.DataFrame({k: G._french_mkt("french_intl_countries_ff_xdiv.zip", G.FRENCH_DY[k]) for k in FRENCH})
        ust = P.ret(P.Y("SPY")).reindex(P.GRID)
        usp = P.ret(P.Y("^GSPC")).reindex(P.GRID)
    T = SL.resolve(SL.DESIGN)
    rate, fw, fx, ust, usp = SL.cut_inputs(T, rate, fw, fx, ust, usp)
    idx = free["R"].index
    eia = {m: free["eia"][A1.EIA_OF[m]][[1, 2]].reindex(idx).copy() for m in ENERGY}
    adm = [r for r in (a1 or {}).get("admitted", []) if r["kind"] == "contract"]
    for m in sorted({r["market"] for r in adm}):                 # a1_panel.build block 2, contracts only
        for n in (1, 2):
            base = eia[m][n]
            rr = [r for r in adm if r["market"] == m and r["n"] == n]
            if rr:
                bb = A1._same_from(m, rr[0]["ticker"], store.series(rr[0]["ticker"], "PX_LAST", "Curves"))
                bb = A1._design(bb.reindex(idx)) if bb is not None else None
                if bb is not None:
                    base = base.combine_first(A1._before(bb, base.first_valid_index()).reindex(idx))
            eia[m][n] = base
    from gm import signals as GS
    return {"rate3m": rate.reindex(idx), "fx_rate_country": {k: v[1] for k, v in GS.FX_CC.items()}, "eia": eia,
            "french_with": fw.reindex(idx), "french_without": fx.reindex(idx), "us_total": ust.reindex(idx),
            "us_price": usp.reindex(idx)}


def measures_from_raw(raw, dy_lag=12):
    """The packaging check of interface v2 section 3 item 0 (NOT the rebuild): the spec formulas on the raw inputs ->
    (C: currency and energy carry, before E13; V: the 8 equity dividend yields with E4)."""
    rt = raw["rate3m"]
    C = {}
    for k, cc in raw["fx_rate_country"].items():
        C[k] = ((rt[cc] - rt["US"]) / 100).shift(1)
    for m, F in raw["eia"].items():
        C[m] = 12 * (F[1] / F[2] - 1)
    V = {}
    for k in raw["french_with"].columns:
        d = raw["french_with"][k] - raw["french_without"][k]
        V[k] = d.rolling(12, min_periods=12).sum().shift(dy_lag)
    V["eq_us_spx"] = (raw["us_total"] - raw["us_price"]).rolling(12, min_periods=12).sum().clip(0, 0.1)
    return pd.DataFrame(C), pd.DataFrame(V)


def raw_check(raw, S):
    """-> rows (group, markets, max abs diff, missing-pattern cells, pass): the raw inputs reproduce the engine's
    carry (currencies, energy; before E13) and equity value measures exactly (tolerance 1e-12)."""
    C, V = measures_from_raw(raw)
    rows = []
    for lab, mine, eng in (("carry currencies", C[[k for k in C if k.startswith("fx_")]], S["C"]),
                           ("carry energy (before E13)", C[[k for k in C if k.startswith("cm_")]], S["C"]),
                           ("value equities (E4)", V, S["V"])):
        cols = list(mine.columns)
        miss = [k for k in cols if k not in eng.columns]
        e = eng.reindex(index=mine.index, columns=cols)
        mp = int((mine.isna() != e.isna()).sum().sum())
        d = (mine - e).abs().max().max()
        d = float(d) if d == d else 0.0
        rows.append({"group": lab, "n": len(cols), "maxdiff": d, "missing": mp + len(miss),
                     "pass": not miss and mp == 0 and d <= 1e-12})
    return rows


def rebuild_inputs(R, D, days, raw, meta=None):
    """Interface v2 section 2: deep copies of the A1 panel's returns, the daily returns, the NYSE days and the raw
    inputs (raw_from_engine), plus the cost table, borrow list and classes. No engine signal or volatility."""
    from gm import book as B
    from gm import signals as G
    out = {"R": R.copy(), "D": D.copy(), "days": pd.DatetimeIndex(days).copy()}
    for k in RAW_KEYS:
        v = raw[k]
        out[k] = {m: f.copy() for m, f in v.items()} if k == "eia" else (dict(v) if isinstance(v, dict) else v.copy())
    out.update({"cost": {k: tuple(B.cost_bp(k)) for k in R.columns}, "em_borrow": tuple(B.EM_EQ),
                "classes": copy.deepcopy(dict(G.CLASSES)), "meta": dict(meta or {})})
    return out


def validate_rebuild(out, keys=None, cut="2010-12"):
    """Interface section 3 items 2-3: every key present, a float Series on a monthly PeriodIndex, nothing after the cut
    month, no infinite value, >= 120 non-missing months in 1975-01..2010-12. -> (ok, reason, months by key)."""
    keys = keys or tuple(REBUILD_KEY.values()) + REBUILD_REPORTED
    if not isinstance(out, dict):
        return False, "output is not a dict", {}
    n = {}
    for k in keys:
        if k not in out:
            return False, "key %r missing" % k, n
        s = out[k]
        if not isinstance(s, pd.Series):
            return False, "%s is not a pandas Series" % k, n
        if not isinstance(s.index, pd.PeriodIndex) or s.index.freqstr not in ("M", "ME"):
            return False, "%s index is not a monthly PeriodIndex" % k, n
        try:
            v = s.astype(float)
        except (TypeError, ValueError):
            return False, "%s is not numeric" % k, n
        if len(v) and v.index.max() > pd.Period(cut, "M"):
            return False, "%s has a month after %s" % (k, cut), n
        if np.isinf(v.values).any():
            return False, "%s has an infinite value" % k, n
        n[k] = int(v.loc[pd.Period(WIN[0], "M"):pd.Period(WIN[1], "M")].notna().sum())
        if n[k] < MIN_WINDOW:
            return False, "%s has %d months in 1975-01..2010-12 (< %d)" % (k, n[k], MIN_WINDOW), n
    return True, "ok", n


# =====================================================================================================================
# runs and small statistics
# =====================================================================================================================
def _quiet(fn, *a, **kw):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*a, **kw)


def _cut(r, a=WIN[0], b=WIN[1]):
    from gm import stats as ST
    return ST.cut(r, a, b)


def _sr(x):
    from gm import stats as ST
    return ST.sharpe(x)


def run_parts(R, D, S, days, cfg, parts, cost_mult=1.0, timing="k1"):
    """An equal-risk E9 book of `parts` ({name: mask}) at k = 1 (or k0 / d1: the k = 0 path, d1 = delay_months 1)."""
    from gm import book as B
    from gm import execution as EX
    if timing == "k1":
        return _quiet(EX.run_k1, R, cfg, D, S, days, cost_mult=cost_mult, parts=parts)
    c = dict(cfg, delay_months=1) if timing == "d1" else cfg
    return _quiet(B.run, R, cost_mult=cost_mult, cfg=c, daily=D, S=S, parts=parts)


def alone(R, D, S, days, cfg, mask, cost_mult=1.0):
    """Entry item 4a: the part alone (a one-part equal-risk book) at k = 1 -> the book dict."""
    return run_parts(R, D, S, days, cfg, {"alone": list(mask)}, cost_mult)


def window(net):
    """Entry item 4a: the months 1975-01..2010-12 with a net return."""
    return _cut(net)


def cell(v, n, fmt="%.2f"):
    """Printing rule (entry item 5): the value over >= 60 months, else the count and the sign only."""
    if v is None or v != v:
        return "n %d, n/a" % n
    if n >= MIN_PRINT:
        return (fmt % v) + " (%d)" % n
    return "n %d, sign %s" % (n, "+" if v > 0 else ("-" if v < 0 else "0"))


def era_cells(net, scale=1.0, stat="sr"):
    out = []
    for lab, a, b in ERAS:
        x = _cut(net, a, b)
        v = _sr(x) if stat == "sr" else float(x.mean() * 12 * scale) if len(x) else float("nan")
        out.append("%s %s" % (lab, cell(v, len(x))))
    return " | ".join(out)


def s1(R, D, S, days, cfg, mask, win, n=NPLACEBO, seed=SEED):
    """Entry item 4b (7.7 T3) on the part alone at k = 1: 1,000 date maps over the window in 12-month blocks."""
    from gm import book as B
    from gm import execution as EX
    from gm import stats as ST
    a, b = str(win.index[0]), WIN[1]
    fn = B.placebo_net_fn(R, cfg, D, S, a, runner=EX.run_k1, days=days, parts={"alone": list(mask)})

    def quiet_fn(perm):
        return _quiet(fn, perm)
    res = ST.placebo_runs(quiet_fn, (a, b), n=n, L=12, seed=seed)
    res["window"] = (a, b)
    return res


def s3(with_net, without_net):
    """Entry item 4d: test 5 (gm.stats.tail_test) of the book without the part (incumbent) against the book with it,
    common months 1975-01..2010-12, both as run."""
    from gm import stats as ST
    return ST.tail_test(_cut(without_net), _cut(with_net))


def rel(a, b):
    """|a - b| / |b| (b = the engine figure)."""
    if b is None or b != b or a is None or a != a or b == 0:
        return float("inf")
    return abs(a - b) / abs(b)


def s4_row(eng, rb):
    """Entry item 4e: Sharpe and annualised mean of engine and rebuild, each over its own months in 1975-01..2010-12;
    pass = both within 15% relative. Common months and their correlation reported."""
    e, r = _cut(eng), _cut(rb.astype(float))
    se, sr_ = _sr(e), _sr(r)
    me, mr = float(e.mean() * 12), float(r.mean() * 12)
    j = pd.concat([e, r], axis=1).dropna()
    corr = float(j.iloc[:, 0].corr(j.iloc[:, 1])) if len(j) > 2 else float("nan")
    ds, dm = rel(sr_, se), rel(mr, me)
    return {"eng_sr": se, "rb_sr": sr_, "eng_mean": me, "rb_mean": mr, "n_eng": len(e), "n_rb": len(r),
            "n_common": len(j), "corr": corr, "rel_sr": ds, "rel_mean": dm, "pass": bool(ds <= S4_TOL and dm <= S4_TOL)}


def live_check(pos, part, freeR, freeS):
    """Entry item 4f: markets the part alone holds at month-end 2010-12 (non-zero) need, on the FREE panel, a return
    at 2010-12 and (carry, value) the measure at 2010-12. -> (pass, held, missing [(market, what)])."""
    t = pd.Period(LAST_DECISION, "M")
    if t not in pos.index:
        return False, [], [("(book)", "no position row at %s" % LAST_DECISION)]
    row = pos.loc[t]
    held = [k for k in row.index if pd.notna(row[k]) and row[k] != 0]
    miss = []
    key = MEASURE[part]
    for k in held:
        if k not in freeR.columns or t not in freeR.index or pd.isna(freeR.at[t, k]):
            miss.append((k, "free return at %s" % LAST_DECISION))
        if key is not None:
            M = freeS[key]
            if k not in M.columns or t not in M.index or pd.isna(M.at[t, k]):
                miss.append((k, "free %s measure at %s" % (key, LAST_DECISION)))
    return (len(held) > 0 and not miss), held, miss


def alpha(pod, book, zero=False):
    """T1 / leave-one-out alpha (gm.stats.alpha_boot) on common window months; zero=True: a zero book (the pod's own
    mean, entry item 4j)."""
    from gm import stats as ST
    p = _cut(pod)
    if zero:
        b = pd.Series(0.0, index=p.index)
    else:
        b = _cut(book)
    j = pd.concat([p, b], axis=1).dropna()
    out = ST.alpha_boot(j.iloc[:, 0], j.iloc[:, 1], n=NBOOT, block=6, seed=SEED)
    out["n"] = len(j)
    return out


def bstats(r, a, b):
    from gm import stats as ST
    x = _cut(r, a, b)
    if len(x) < MIN_PRINT:
        return None
    return {"n": len(x), "sr": ST.sharpe(x), "mean": float(x.mean() * 12), "vol": float(x.std() * np.sqrt(12)),
            "maxdd": ST.maxdd(x), "skew": float(x.skew()), "lo": ST.lo_sharpe(x)}


def margins(tl):
    """Test 5 as its two margins in points (book with / candidate minus book without / incumbent): positive = better."""
    return "max fall %+.1f pts, worst month %+.1f pts" % ((tl["dd_cha"] - tl["dd_inc"]) * 100,
                                                          (tl["wm_cha"] - tl["wm_inc"]) * 100)


# =====================================================================================================================
# the registered run
# =====================================================================================================================
def report(R, D, S, gspc, free, rb, out=print, facts=None, cfg=None, trials_path=None, n_placebo=NPLACEBO,
           rb_version="?"):
    """Entry items 4-6 on panel (R, D, S) with the free panel `free` ({"R", "S"}) for the live-source check and the
    validated rebuild output rb (S4_INTERFACE.md). facts: the A2 report facts (diag_a2.a2_facts) for the as-run check
    (None: skipped; tests). Returns the result dict (verdicts, Core book v1, trial row inputs)."""
    import a2_batch as A2
    import diag_a2 as DG
    from gm import config as CF
    from gm import execution as EX
    from gm import seal as SL
    cfg = cfg or CF.A1_INCUMBENT
    T = SL.resolve(SL.DESIGN)
    R, D, S, gspc = SL.cut_inputs(T, R, D, S, gspc)
    days = EX.nyse_days(gspc=gspc)
    if facts:
        try:
            DG.as_run(R, D, S, days, cfg, facts, out)
        except DG.AsRunMismatch as e:
            raise AsRunMismatch(str(e))
    M = masks()
    res = {"parts": {}, "cfg": cfg}
    out("--- CORE BOOK V1 (TESTING_PROTOCOL 7.6 step 6; gm/CHANGES.md \"Core book v1\"): final Batch A book %s (%s), A1 "
        "panel, k = 1, design months %s..%s; values over fewer than 60 months are printed as count and sign" % (
            cfg["name"], CF.cfg_hash(cfg), WIN[0], WIN[1]))
    out("PARTS | Core candidates: %s | shadow parts: %s" % (
        " ; ".join("%s = %s %s" % (p, LABEL[p], M[p]) for p in CORE),
        " ; ".join("%s = %s %s" % (p, LABEL[p], M[p]) for p in SHADOW)))
    # ---- each part alone (k = 1, single and double costs)
    nets, nets2, bks = {}, {}, {}
    for p in CORE + SHADOW + REBUILD_REPORTED:
        bk = alone(R, D, S, days, cfg, M[p])
        SL.check_output(bk["net"], T, "core_v1.alone")
        bks[p], nets[p] = bk, bk["net"]
        if p in CORE + SHADOW:
            nets2[p] = alone(R, D, S, days, cfg, M[p], cost_mult=2.0)["net"]
    out("--- each part alone (one-part equal-risk book, k = 1, 10%, caps, costs x1): net Sharpe (months) and mean %/yr")
    for p in CORE + SHADOW + REBUILD_REPORTED:
        out("PART | %s | %s | Sharpe %s | mean %%/yr %s" % (p, LABEL[p], era_cells(nets[p]),
                                                            era_cells(nets[p], 100, "mean")))
    # ---- the candidate Core book and the books without one part (S3, leave-one-out)
    cand = {p: M[p] for p in CORE}
    with_bk = run_parts(R, D, S, days, cfg, cand)
    without = {p: run_parts(R, D, S, days, cfg, {q: M[q] for q in CORE if q != p})["net"] for p in CORE}
    # ---- S1-S4, live source
    out("--- S1-S4 and the live-source check per Core candidate (decisive); leave-one-out alpha (reported only)")
    placebo = {}
    for p in CORE + SHADOW:
        win = window(nets[p])
        r = {"window": len(win)}
        if len(win) < MIN_WINDOW:
            r["insufficient"] = True
            placebo[p] = None
            res["parts"][p] = r
            continue
        pl = s1(R, D, S, days, cfg, M[p], win, n=n_placebo)
        placebo[p] = pl
        r["insufficient"] = False
        res["parts"][p] = r
    for p in CORE:
        r = res["parts"][p]
        if r["insufficient"]:
            out("S | %s | window %d months < %d: insufficient data, not tested, not Core" % (p, r["window"], MIN_WINDOW))
            r["core"] = False
            r["status"] = "insufficient data"
            continue
        pl = placebo[p]
        r["S1"] = pl["pass"]
        out("S1 | %s | window %s..%s (%d months) | part net Sharpe %.2f | placebos %d | share with Sharpe >= the part's "
            "%.3f | %s" % (p, pl["window"][0], pl["window"][1], r["window"], pl["sr"], pl["n"], pl["p"],
                           "PASS" if pl["pass"] else "FAIL"))
        w2 = window(nets2[p])
        m2 = float(w2.mean() * 12) if len(w2) else float("nan")
        r["S2"] = bool(m2 > 0)
        out("S2 | %s | net mean at twice the costs %s %%/yr | %s" % (p, cell(m2 * 100, len(w2)),
                                                                     "PASS" if r["S2"] else "FAIL"))
        tl = s3(with_bk["net"], without[p])
        r["S3"] = tl["pass"]
        out("S3 | %s | Core book with vs without the part (both as run), n %d | %s | max drawdown without %.1f%%, with "
            "%.1f%% | %s" % (p, tl["n"], margins(tl), tl["dd_inc"] * 100, tl["dd_cha"] * 100,
                             "PASS" if tl["pass"] else "FAIL"))
        k = REBUILD_KEY[p]
        s4 = s4_row(nets[p], rb[k])
        r["S4"] = s4["pass"]
        r["s4"] = s4
        out("S4 | %s (rebuild key %s, %s) | engine Sharpe %s, mean %s %%/yr | rebuild Sharpe %s, mean %s %%/yr | "
            "relative difference Sharpe %.3f, mean %.3f (limit %.2f) | common months %d, correlation %s | %s" % (
                p, k, rb_version, cell(s4["eng_sr"], s4["n_eng"]), cell(s4["eng_mean"] * 100, s4["n_eng"]),
                cell(s4["rb_sr"], s4["n_rb"]), cell(s4["rb_mean"] * 100, s4["n_rb"]), s4["rel_sr"], s4["rel_mean"],
                S4_TOL, s4["n_common"], cell(s4["corr"], s4["n_common"]), "PASS" if s4["pass"] else "FAIL"))
        ok, held, miss = live_check(bks[p]["pos"], p, free["R"], free["S"])
        r["LIVE"] = ok
        out("LIVE | %s | markets held at %s: %d (%s) | missing free inputs: %s | %s" % (
            p, LAST_DECISION, len(held), ", ".join(held) or "none",
            ", ".join("%s (%s)" % m for m in miss) or "none", "PASS" if ok else "FAIL"))
        la = alpha(nets[p], without[p])
        r["loo"] = la
        out("LOO | %s | alpha on the other two candidates' equal-risk book %s %%/yr | beta %s | bootstrap p %s "
            "(reported only, not decisive: 7.6 step 6)" % (p, cell(la["alpha"] * 1200, la["n"]),
                                                           cell(la["beta"], la["n"]), cell(la["p"], la["n"], "%.4f")))
        r["core"] = bool(r["S1"] and r["S2"] and r["S3"] and r["S4"] and r["LIVE"])
        r["status"] = "Core" if r["core"] else "not Core"
        out("VERDICT | %s | S1 %s, S2 %s, S3 %s, S4 %s, live %s | %s" % (
            p, *("PASS" if r[x] else "FAIL" for x in ("S1", "S2", "S3", "S4", "LIVE")), r["status"].upper()))
    for k in REBUILD_REPORTED:
        s4 = s4_row(nets[k], rb[k])
        res["parts"].setdefault(k, {})["s4"] = s4
        out("S4 REPORTED | %s | engine Sharpe %s, mean %s %%/yr | rebuild Sharpe %s, mean %s %%/yr | relative "
            "difference Sharpe %.3f, mean %.3f | common months %d, correlation %s (not decisive)" % (
                k, cell(s4["eng_sr"], s4["n_eng"]), cell(s4["eng_mean"] * 100, s4["n_eng"]),
                cell(s4["rb_sr"], s4["n_rb"]), cell(s4["rb_mean"] * 100, s4["n_rb"]), s4["rel_sr"], s4["rel_mean"],
                s4["n_common"], cell(s4["corr"], s4["n_common"])))
    # ---- Core book v1
    core = [p for p in CORE if res["parts"][p].get("core")]
    res["core"] = core
    empty = not core
    res["empty"] = empty
    if empty:
        out("CORE BOOK V1 EMPTY | no Core candidate passed S1-S4 and the live-source check | B tests read alpha against "
            "a zero book (the pod's own mean); there is no holdout run; BASE continues, labelled \"no Core book\"")
        core_net = None
        res["books"] = {}
    else:
        parts = {p: M[p] for p in core}
        out("CORE BOOK V1 | parts %s at equal risk (E9, n = %d), 10%% target, caps, costs | config hash %s" % (
            ", ".join(core), len(core), core_hash(cfg, core)))
        books = {}
        for tm in ("k1", "k0", "d1"):
            for cm in (1.0, 2.0):
                books[(tm, cm)] = run_parts(R, D, S, days, cfg, parts, cm, tm) if (tm, cm) != ("k1", 1.0) or \
                    set(core) != set(CORE) else with_bk
        res["books"] = books
        core_net = books[("k1", 1.0)]["net"]
        SL.check_output(core_net, T, "core_v1.core_book")
        out("--- Core book v1: months | net Sharpe | mean %/yr | vol %/yr | max drawdown % | skew | Lo-adjusted Sharpe")
        for (tm, cm), bk in books.items():
            for lab, a, b in ERAS:
                s = bstats(bk["net"], a, b)
                if s is None:
                    out("BOOK | core_v1 | %s | costs x%d | %s | n<%d" % (tm, cm, lab, MIN_PRINT))
                    continue
                out("BOOK | core_v1 | %s | costs x%d | %s | %d | %.3f | %.2f | %.2f | %.1f | %.2f | %.2f" % (
                    tm, cm, lab, s["n"], s["sr"], s["mean"] * 100, s["vol"] * 100, s["maxdd"] * 100, s["skew"],
                    s["lo"]))
        bk1 = books[("k1", 1.0)]
        years = sorted({p.year for p in bk1["net"].index if WIN[0] <= str(p) <= WIN[1]})
        fl = [(y, A2.flag_share(bk1, bk1["k1_flags"], "%d-01" % y, "%d-12" % y)) for y in years]
        out("FLAGGED | core_v1 | 1975-2010 %.3f | by year: %s" % (
            A2.flag_share(bk1, bk1["k1_flags"], *WIN), ", ".join("%d %.2f" % (y, v) for y, v in fl if v == v)))
        w = A2.p4(core_net, R["eq_us_spx"])
        pb, ps = _cut(core_net, P4_FROM, WIN[1]), _cut(w, P4_FROM, WIN[1])
        out("P4 | core_v1 | S&P 500 alone (M1) | book %s | specific %s" % (cell(_sr(pb), len(pb)),
                                                                          cell(_sr(ps), len(ps))))
    if trials_path:
        si = A2.selection_inflation(trials_path)
        out("selection inflation (7.8 item 2; printed beside, not subtracted): %d logged book / pod rows, mean 1990-2010 "
            "Sharpe %.3f, sd %.3f, z %.2f -> expected best Sharpe from luck alone about %+.2f" % (
                si["n"], si["mean"], si["sd"], si["z"], si["inflation"]))
    out(A2.KNOBS)
    # ---- Incubator rule
    out("--- Incubator rule (7.7) against Core book v1%s: T1 alpha > 0 at single costs (raw p reported, no Holm), T3 "
        "placebo, T4 tail at lambda %.1f; T2 alpha at twice the costs reported" % (
            " (EMPTY: alpha against a zero book, T4 not applicable)" if empty else "", LAMBDA))
    res["incubator"] = {}
    for p in [q for q in CORE if not res["parts"][q].get("core")] + list(SHADOW):        # C1: every candidate not Core
        r = res["parts"][p]
        if r["insufficient"]:
            out("INCUBATOR | %s | window %d months < %d: insufficient data" % (p, r["window"], MIN_WINDOW))
            res["incubator"][p] = "insufficient data"
            continue
        a1 = alpha(nets[p], core_net, zero=empty)
        a2 = alpha(nets2[p], books[("k1", 2.0)]["net"] if not empty else None, zero=empty)
        pl = placebo[p]
        if a1["n"] < MIN_WINDOW:
            out("INCUBATOR | %s | common months with Core book v1 %d < %d: insufficient data" % (p, a1["n"], MIN_WINDOW))
            res["incubator"][p] = "insufficient data"
            continue
        if empty:
            t4, t4s = True, "T4 not applicable (empty Core book)"
        else:
            from gm import stats as ST
            tl = ST.t4_tail(_cut(core_net), _cut(nets[p]), LAMBDA)
            t4, t4s = tl["pass"], "T4 %s (n %d; %s)" % ("PASS" if tl["pass"] else "FAIL", tl["n"], margins(tl))
        t1 = bool(a1["alpha"] > 0)
        ok = t1 and pl["pass"] and t4
        st = "Incubator" if ok else "Shelved"
        res["incubator"][p] = st
        out("INCUBATOR | %s | %s | T1 alpha %s %%/yr, beta %s, raw p %s -> %s | T2 alpha at 2x costs %s %%/yr | T3 "
            "placebo share %.3f %s | %s | %s" % (
                p, LABEL[p], cell(a1["alpha"] * 1200, a1["n"]), cell(a1["beta"], a1["n"]),
                cell(a1["p"], a1["n"], "%.4f"), "PASS" if t1 else "FAIL", cell(a2["alpha"] * 1200, a2["n"]), pl["p"],
                "PASS" if pl["pass"] else "FAIL", t4s, st.upper()))
    out("CORE V1 VERDICT | Core: %s | not Core: %s | Incubator: %s | Shelved: %s | insufficient data: %s" % (
        ", ".join(core) or "none (EMPTY)", ", ".join(p for p in CORE if p not in core) or "none",
        ", ".join(p for p, s in res["incubator"].items() if s == "Incubator") or "none",
        ", ".join(p for p, s in res["incubator"].items() if s == "Shelved") or "none",
        ", ".join(p for p, s in res["incubator"].items() if s == "insufficient data") or "none"))
    return res


def core_hash(cfg, core):
    from gm import config as CF
    return CF.cfg_hash(dict(cfg, core_parts=sorted(core)))


def trial_row(res, panel_id_, engine_version, lock_id=LOCK_V2):
    """Entry item 6: the one gm/trials.csv row of family 'book' (gm/trials.py columns)."""
    import json
    from gm import config as CF
    from gm import stats as ST
    cfg = res["cfg"]
    core = res["core"]
    c = dict(cfg, core_parts=sorted(core))
    verdicts = ", ".join("%s %s" % (p, res["parts"][p].get("status", "?")) for p in CORE) + "; " + ", ".join(
        "%s %s" % kv for kv in res["incubator"].items())
    row = {"trial": "Core book v1 (k = 1, A1 panel)", "family": "book", "hash": CF.cfg_hash(c),
           "note": "TESTING_PROTOCOL 7.6 step 6 Core book v1; engine %s; A1 panel %s; LOCK_v2 %s; parent %s (%s); %s; "
                   "%s" % (engine_version, panel_id_[:16], lock_id[:16], cfg["name"], CF.cfg_hash(cfg),
                           "parts " + ", ".join(core) if core else "EMPTY", verdicts),
           "config": json.dumps(c, sort_keys=True, default=list)}
    if not res["empty"]:
        bk = res["books"][("k1", 1.0)]
        d, e = ST.summary(bk["net"]), ST.summary(bk["net"], *ST.EXTRA)
        row.update({"sr_9010": round(d["sr"], 3), "t_9010": round(d["t"], 2), "maxdd_9010": round(d["maxdd"], 3),
                    "sr_7589": round(e["sr"], 3),
                    "turnover": round(float(ST.cut(bk["turnover"], *ST.DESIGN).mean() * 12), 1)})
    return row
