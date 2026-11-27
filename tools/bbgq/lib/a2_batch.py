"""a2_batch: Batch A2 of TESTING_PROTOCOL 7.6 step 3 (version grids, hygiene 7.7 H1-H4), as registered in gm/CHANGES.md
"A2: Batch A2, version grids, hygiene H1-H4" (2026-11-27, before this code). Runs where the A1 panel can be built (the
user's PC: the A1 panel holds Bloomberg values); tested in the cloud on synthetic panels only.

Arms: incumbent = config.A1_INCUMBENT (77374d7bef) as run (old code path, no grid); challenger = config.A2_CHALLENGER
(1faa343535, grids: Trend 16, Economic trend 2, Carry 2, Value 2). Both on the A1 panel (id e7f98d44...), engine
gm-2.2.1, design months only.
Decisive (CHANGES A2 item 3): at k = 1 on the pooled window 1975-01..2010-12, H1 = one-sided 95% lower bound of dSR
(gm.stats.paired_sr_test) > -0.10 and H3 = test 5 (gm.stats.tail_test). PASS = H1 and H3 -> A2-final = challenger;
FAIL -> A2-final = A1_INCUMBENT (no averaging, no cell picked). H2 (double costs) reported; no Holm.
Reported (CHANGES A2 item 4 a-m): see report(). Nothing here prints a data value: summary statistics over at least
60 months, pass / fail, counts and ids only (tools/bbgq/README.md export whitelist).

API
  A1_PANEL_ID, as_run_from_a1(path)       registered id / the incumbent as run, read from the gm_a1_v2 report
  check_panel_id(a1), compare_saved(work, a1)   the A1 panel checks of the job
  selection_inflation(path)                 7.8 item 2 from a trial log
  books(R, D, S, days, cfg)                 one config at k = 1 / k = 0 / one-month delay, single and double costs
  hygiene(inc, cha, a, b)                   H1-H3 on a window (gm.stats.noninferiority)
  trend_split(R, D, S, cfg, bk)             class-average / relative parts of Trend, scaled as held (positions)
  p4(r, m)                                  the P4 specific return
  report(R, D, S, gspc, out, ...)           the registered A2 report; returns the result dict (verdict, trial row data)
  trial_row(res, ...)                       the gm/trials.csv row (family "book") of the challenger
"""
import contextlib
import hashlib
import io
import math
import os

import numpy as np
import pandas as pd

VERSION = "a2_batch-1.1.0"   # 1.1.0 (gm-2.2.1 fix): as-run values read from the gm_a1_v2 report; CM-only cm_aqr_ew
A1_PANEL_ID = "e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43"   # gm/CHANGES.md A1 RUN
LOCK_V2 = "d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9"
INC_HASH, CHA_HASH = "77374d7bef", "1faa343535"     # gm-2.2.1 names (gm/CHANGES.md gm-2.2.1 item 3)
A1_REPORT = "gm_a1_v2.txt"   # the A1 rerun under gm-2.2.1: source of the incumbent's as-run values (gm-2.2.1 item 4c)
TRIALS_SHA = "2b80e2f9b255b05e839f6a6edcafa844aa67c161423d4966d99a141e4e178a36"   # A2 item 4l, with the gm-2.2.1 fix rows
DESIGN_END = pd.Period("2010-12", "M")
WIN = ("1975-01", "2010-12")
ERAS = (("1975-2010", "1975-01", "2010-12"), ("1975-89", "1975-01", "1989-12"), ("1990-2010", "1990-01", "2010-12"))
WEEKLY = ("1990-01", "2010-12")
P4_FROM = "1978-01"
MIN_PRINT = 60
NI_MARGIN = -0.10
FRAG_SHARE = 0.40
KNOBS = ("tuned knobs (7.8 item 4, as registered): Trend 4, Economic trend 3, Carry 3, Value 3 + 1 seen leg (Value "
         "version 2's bond leg = batch-1 V1, 7.8 item 3); book level 3 (pod share vector, no risk scaler, no scenario "
         "limit)")
TIMINGS = (("k1", "k = 1 (decisive)"), ("k0", "k = 0 (reported)"), ("d1", "one-month delay (reported)"))
PODS = ("trend", "econ", "carry", "value")


class AsRunMismatch(RuntimeError):
    pass


# =====================================================================================================================
# checks of the job
# =====================================================================================================================
def check_panel_id(a1, want=A1_PANEL_ID):
    """The rebuilt A1 panel carries the registered id (else the job stops)."""
    return a1["panel_id"] == want


def compare_saved(work, a1):
    """-> ('absent' | 'same' | 'differs: <what>'). The A1 job's saved panel (work/a1/a1_panel_<id12>.pkl) against the
    rebuild: panel id, R and every signal frame equal (values and missing pattern)."""
    import pickle
    p = os.path.join(work, "a1", "a1_panel_%s.pkl" % a1["panel_id"][:12])
    if not os.path.exists(p):
        return "absent"
    with open(p, "rb") as f:
        s = pickle.load(f)
    if s.get("panel_id") != a1["panel_id"]:
        return "differs: panel id"
    if not _same_frame(s["R"], a1["R"]):
        return "differs: R"
    keys = set(s["S"]) | set(a1["S"])
    for k in sorted(keys):
        if k not in s["S"] or k not in a1["S"] or not _same_frame(s["S"][k], a1["S"][k]):
            return "differs: signal %s" % k
    return "same"


def _same_frame(a, b):
    if not isinstance(a, pd.DataFrame) or not isinstance(b, pd.DataFrame):
        return False
    if list(a.columns) != list(b.columns) or not a.index.equals(b.index):
        return False
    x, y = a.values.astype(float), b.values.astype(float)
    return bool(np.array_equal(np.isnan(x), np.isnan(y)) and np.array_equal(x[~np.isnan(x)], y[~np.isnan(y)]))


def as_run_from_a1(path, want_id=A1_PANEL_ID):
    """gm-2.2.1 item 4c: the incumbent's as-run net Sharpe ratios 1975-2010 (k1, k0, d1) from the A1 report (job
    gm_a1_v2), lines "all blocks (A1 panel)... | k1 | 1975-2010 | n | SR | ...". -> (dict or None, reason). None when the
    file is missing, has no "A1 JOB DONE", names another A1 PANEL ID than the registered one, or lacks a line."""
    if not os.path.exists(path):
        return None, "missing (%s)" % os.path.basename(path)
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()
    if not any(x.strip() == "A1 JOB DONE" for x in lines):
        return None, "no 'A1 JOB DONE' line"
    ids = [x.split()[3] for x in lines if x.startswith("A1 PANEL ID ") and len(x.split()) > 3]
    if len(ids) != 1 or ids[0] != want_id:
        return None, "A1 PANEL ID %s, registered %s" % (",".join(i[:16] for i in ids) or "none", want_id[:16])
    out = {}
    for x in lines:
        p = [q.strip() for q in x.split("|")]
        if len(p) >= 5 and p[0].startswith("all blocks (A1 panel)") and p[1] in ("k1", "k0", "d1") and \
                p[2] == "1975-2010":
            out[p[1]] = float(p[4])
    if set(out) != {"k1", "k0", "d1"}:
        return None, "lines missing: %s" % ", ".join(sorted({"k1", "k0", "d1"} - set(out)))
    return out, "ok"


def file_sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def selection_inflation(path):
    """7.8 item 2 by the stats_audit method (gm/audit.py s2): rows of the trial log with family 'book' or 'pod' and a
    numeric 1990-2010 Sharpe; z = (1 - g) Phi^-1(1 - 1/N) + g Phi^-1(1 - 1/(N e)); inflation = z x sd (ddof 1)."""
    from gm import stats as ST
    d = pd.read_csv(path)
    d = d[d["family"].isin(["book", "pod"])]
    srs = pd.to_numeric(d["sr_9010"], errors="coerce").dropna().values
    n = len(srs)
    if n < 2:
        return {"n": n, "mean": float("nan"), "sd": float("nan"), "z": float("nan"), "inflation": float("nan"),
                "by_family": d["family"].value_counts().to_dict()}
    g = 0.5772156649
    z = (1 - g) * ST._norm_ppf(1 - 1 / n) + g * ST._norm_ppf(1 - 1 / (n * math.e))
    sd = float(srs.std(ddof=1))
    return {"n": n, "mean": float(srs.mean()), "sd": sd, "z": float(z), "inflation": float(z * sd),
            "by_family": d["family"].value_counts().to_dict()}


# =====================================================================================================================
# runs
# =====================================================================================================================
def _quiet(fn, *a, **kw):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*a, **kw)


def books(R, D, S, days, cfg):
    """One config: k = 1, k = 0 and the one-month delay (k = 0 path with delay_months = 1), each at cost multiple 1 and
    2. -> {(timing, cost multiple): book}."""
    from gm import book as B
    from gm import execution as EX
    out = {}
    for cm in (1.0, 2.0):
        out[("k1", cm)] = _quiet(EX.run_k1, R, cfg, D, S, days, cost_mult=cm)
        out[("k0", cm)] = _quiet(B.run, R, cost_mult=cm, cfg=cfg, daily=D, S=S)
        out[("d1", cm)] = _quiet(B.run, R, cost_mult=cm, cfg=dict(cfg, delay_months=1), daily=D, S=S)
    return out


def pod_alone(R, D, S, days, cfg, mask):
    """A pod or version as a complete pod alone: one-part equal-risk book (gm-2.1.0 E9) at k = 1."""
    from gm import execution as EX
    return _quiet(EX.run_k1, R, cfg, D, S, days, parts={"alone": mask})["net"]


def versions(cfg):
    """[(pod, v (1-based), label)] of a config's grid (challenger) in the registered order."""
    g = cfg.get("grid") or {}
    out = []
    for i, (h, shape, vm) in enumerate(g.get("trend", ())):
        out.append(("trend", i + 1, "trend v%d (%d m, %s, %s)" % (i + 1, h, shape, vm)))
    for i, sh in enumerate(g.get("econ", ())):
        out.append(("econ", i + 1, "econ v%d (%s)" % (i + 1, "tanh(z/2)" if sh == "tanh" else "sign(z)")))
    for i, k in enumerate(g.get("carry", ())):
        out.append(("carry", i + 1, "carry v%d (%s)" % (i + 1, "sign of carry" if k == "dir" else "rank in class")))
    for i, v in enumerate(g.get("value", ())):
        out.append(("value", i + 1, "value v%d" % v))
    return out


# =====================================================================================================================
# statistics
# =====================================================================================================================
def _cut(r, a, b):
    from gm import stats as ST
    return ST.cut(r, a, b)


def bstats(r, a, b):
    from gm import stats as ST
    x = _cut(r, a, b)
    if len(x) < MIN_PRINT:
        return None
    return {"n": len(x), "sr": ST.sharpe(x), "mean": float(x.mean() * 12), "vol": float(x.std() * np.sqrt(12)),
            "maxdd": ST.maxdd(x), "skew": float(x.skew()), "lo": ST.lo_sharpe(x)}


def hygiene(inc, cha, inc2x, cha2x, a, b):
    """H1-H3 on the months a..b where both books have a net return (gm.stats.noninferiority) plus the bootstrap se."""
    from gm import stats as ST
    i, c = _cut(inc, a, b), _cut(cha, a, b)
    j = pd.concat([i, c], axis=1).dropna()
    out = ST.noninferiority(j.iloc[:, 0], j.iloc[:, 1], _cut(inc2x, a, b), _cut(cha2x, a, b), margin=NI_MARGIN)
    t = ST.paired_sr_test(j.iloc[:, 0], j.iloc[:, 1])
    out["se"] = t.get("se", float("nan"))
    out["identical"] = bool(t.get("identical", False))
    return out


def sr_or(r, a, b):
    from gm import stats as ST
    x = _cut(r, a, b) if r is not None else pd.Series(dtype=float)
    return (ST.sharpe(x), len(x)) if len(x) >= MIN_PRINT else (None, len(x))


def fmt_sr(r, a, b):
    s, n = sr_or(r, a, b)
    return "%.2f (%d)" % (s, n) if s is not None else "n<%d" % MIN_PRINT


def contrib_fam(bk, fam, cols=None):
    """Family contribution at the book's earning returns: held family position x return, before costs, months with a
    held position only."""
    RE = bk["R_earn"] if "R_earn" in bk else None
    pos = bk["fam_pos"][fam]
    if RE is None:
        raise KeyError("contrib_fam needs a k = 1 book")
    cols = [k for k in (cols if cols is not None else pos.columns) if k in RE.columns and k in pos.columns]
    held = pos[cols].shift(1)
    return (held * RE[cols]).sum(axis=1, min_count=1).where(held.abs().sum(axis=1) > 0)


def flag_share(bk, flags, a, b):
    held = bk["pos"].shift(1).abs()
    f = flags.reindex(index=held.index, columns=held.columns).fillna(False).astype(bool)
    sel = (held.index >= pd.Period(a, "M")) & (held.index <= pd.Period(b, "M"))
    tot = float(held[sel].sum().sum())
    return float(held[sel].where(f[sel], 0.0).sum().sum()) / tot if tot > 0 else float("nan")


def p4(r, m, start=WIN[0], first=37):
    """P4 (7.7): w(t) = r(t) - b(t) m(t), b(t) = least-squares slope with intercept of r on m over the common months from
    `start` to t - 1; first value in month `first` (37 = 1978-01 from 1975-01). Point in time: b(t) reads months < t."""
    j = pd.concat([r, m], axis=1)
    j.columns = ["r", "m"]
    j = j.loc[pd.Period(start, "M"):]
    w = pd.Series(np.nan, index=j.index)
    t0 = pd.Period(start, "M") + (first - 1)
    for t in j.index:
        if t < t0 or pd.isna(j.at[t, "r"]) or pd.isna(j.at[t, "m"]):
            continue
        past = j.loc[:t - 1].dropna()
        if len(past) < 3 or past["m"].var() == 0:
            continue
        b = float(np.cov(past["r"], past["m"], ddof=1)[0, 1] / past["m"].var(ddof=1))
        w[t] = j.at[t, "r"] - b * j.at[t, "m"]
    return w


# =====================================================================================================================
# Trend's split (CHANGES A2 item 4e) and carry / price parts (item 4f)
# =====================================================================================================================
def trend_raw_parts(R, cfg, D, S):
    """Per class: (raw Trend pod position p_c = sum over versions of p_v / V, class-average part, relative part), all
    unscaled (book.py family_positions arithmetic). w = clip(score, -1, 1); class mean over the markets of the class
    with a position that month (p_v not missing); part x 0.40 / vol_v / n_v / V."""
    from gm import book as B
    from gm import signals as G
    from gm import vol as VM
    if cfg.get("within_class", "equal") != "equal":
        raise ValueError("trend_split: equal weight in class only (the registered configs)")
    vol = VM.estimate(R, cfg, D)
    vers = B.family_versions(R, cfg, D, S, vol)["trend"]
    V = len(vers)
    out = {}
    for c, pre in G.CLASSES.items():
        raw, avg, rel = [], [], []
        for X, kind, vol_v in vers:
            X = X.reindex(index=R.index)
            cols = [k for k in X.columns if (k.startswith(pre) and k in R and k != "cm_aqr_ew") or
                    (k == "cm_aqr_ew" and c == "CM" and k in X.columns)]        # gm-2.2.1: CM block only
            cols = [k for k in cols if k in R.columns]
            if not cols:
                continue
            w = X[cols].clip(-1, 1)
            a = 0.40 / vol_v[cols]
            p = w * a
            n = p.notna().sum(axis=1)
            nn = n.where(n > 0)
            have = p.notna()
            mw = w.where(have).mean(axis=1)
            wa = pd.DataFrame(np.repeat(mw.values[:, None], len(cols), 1), index=w.index, columns=cols).where(have)
            t_raw = p.div(nn, axis=0) / V
            t_avg = (wa * a).div(nn, axis=0) / V
            raw.append(t_raw)
            avg.append(t_avg)
            rel.append(t_raw - t_avg)
        if not raw:
            continue
        have = sum(t.notna().astype(int) for t in raw) > 0
        out[c] = tuple(sum(t.fillna(0) for t in ts).where(have) for ts in (raw, avg, rel))
    return out


def trend_split(R, D, S, cfg, bk):
    """Scale the unscaled parts as book.run scales Trend: block scaler k_c (36 months, at least 24, lagged, <= 50) x
    family share x m(t), m(t) = |held Trend family position| / |sum_c p_c k_c share| (book scaler x cap shrink), so
    avg + rel = the held Trend family position. -> dict(avg, rel, held, check maxdiff, months without m)."""
    from gm import book as B
    parts = trend_raw_parts(R, cfg, D, S)
    fw = B._fw(cfg, "trend")
    bw = cfg.get("block_vol_months", 36)
    held = bk["fam_pos"]["trend"]
    cols_all = list(held.columns)
    by, av, rl = (pd.DataFrame(0.0, index=R.index, columns=cols_all) for _ in range(3))
    for c, (p, a, r) in parts.items():
        ret = (p.shift(1) * R[p.columns]).sum(axis=1, min_count=1)
        k = (1.0 / (ret.rolling(bw, min_periods=24).std() * np.sqrt(12))).shift(1).clip(upper=50)
        for fr, x in ((by, p), (av, a), (rl, r)):
            sc = x.mul(k, axis=0) * fw
            fr[sc.columns] = fr[sc.columns].add(sc.fillna(0), fill_value=0)
    den = by.abs().sum(axis=1)
    m = (held.reindex(index=R.index).abs().sum(axis=1) / den.where(den > 0))
    no_m = int(((den == 0) & (held.reindex(index=R.index).abs().sum(axis=1) > 0)).sum())
    rec = by.mul(m, axis=0)
    diff = float((rec.fillna(0) - held.reindex(index=R.index).fillna(0)).abs().max().max())
    avg, rel = av.mul(m, axis=0).fillna(0), rl.mul(m, axis=0).fillna(0)
    sdiff = float((avg + rel - held.reindex(index=R.index).fillna(0)).where(m.notna(), 0, axis=0).abs().max().max())
    return {"avg": avg, "rel": rel, "maxdiff_held": diff, "maxdiff_parts": sdiff, "months_no_scale": no_m}


def part_return(pos, RE, cols=None):
    cols = [k for k in (cols if cols is not None else pos.columns) if k in RE.columns and k in pos.columns]
    h = pos[cols].shift(1)
    return (h * RE[cols]).sum(axis=1, min_count=1).where(h.abs().sum(axis=1) > 0)


def carry_price(bk, C):
    """Trend's bond and currency return split into carry (held position x carry / 12 at the prior month end) and price
    (the rest), on the market-months with both a held Trend position and a carry value. -> (total, carry, price,
    covered share of Trend's FX + FI gross position)."""
    pos = bk["fam_pos"]["trend"]
    RE = bk["R_earn"]
    cols = [k for k in pos.columns if k.startswith(("fx_", "bd_", "st_")) and k in RE.columns]
    h = pos[cols].shift(1)
    c12 = C.reindex(index=pos.index, columns=cols).shift(1) / 12
    ok = h.notna() & (h != 0) & c12.notna() & RE[cols].notna()
    tot = (h * RE[cols]).where(ok).sum(axis=1, min_count=1)
    car = (h * c12).where(ok).sum(axis=1, min_count=1)
    allh = h.abs().where(h.notna() & (h != 0) & RE[cols].notna())
    sel = (pos.index >= pd.Period(WIN[0], "M")) & (pos.index <= DESIGN_END)
    cov = float(allh.where(ok)[sel].sum().sum()) / float(allh[sel].sum().sum()) if float(allh[sel].sum().sum()) > 0 \
        else float("nan")
    return tot, car, tot - car, cov


def eq_pos_corr(bk):
    """Economic trend vs Trend held equity positions, pooled over equity market-months 1975-2010, both non-zero."""
    e, t = bk["fam_pos"].get("econ"), bk["fam_pos"].get("trend")
    if e is None or t is None:
        return None, 0
    cols = [k for k in t.columns if k.startswith("eq_") and k in e.columns]
    sel = (t.index >= pd.Period(WIN[0], "M")) & (t.index <= DESIGN_END)
    a, b = e[cols][sel].values.ravel(), t[cols][sel].values.ravel()
    ok = ~np.isnan(a) & ~np.isnan(b) & (a != 0) & (b != 0)
    if ok.sum() < MIN_PRINT:
        return None, int(ok.sum())
    return float(np.corrcoef(a[ok], b[ok])[0, 1]), int(ok.sum())


# =====================================================================================================================
# fragility (CHANGES A2 item 4k)
# =====================================================================================================================
def dsr(inc, cha, a=WIN[0], b=WIN[1], drop=None):
    from gm import stats as ST
    j = pd.concat([_cut(inc, a, b), _cut(cha, a, b)], axis=1).dropna()
    if drop is not None:
        j = j[~drop(j.index)]
    if len(j) < MIN_PRINT:
        return float("nan")
    return ST.sharpe(j.iloc[:, 1]) - ST.sharpe(j.iloc[:, 0])


def fragility(R, D, S, days, inc_cfg, cha_cfg, inc_net, cha_net, markets=None):
    """Largest loss of the pooled k = 1 dSR when one year, one market or one class is removed; year share of the summed
    monthly difference. markets: the markets to try (default every panel column)."""
    from gm import execution as EX
    from gm import signals as G
    full = dsr(inc_net, cha_net)
    j = pd.concat([_cut(inc_net, *WIN), _cut(cha_net, *WIN)], axis=1).dropna()
    years = sorted(set(j.index.year))
    yr = {y: dsr(inc_net, cha_net, drop=lambda ix, y=y: ix.year == y) for y in years}
    diff = (j.iloc[:, 1] - j.iloc[:, 0])
    tot = float(diff.sum())
    by_y = diff.groupby(diff.index.year).sum()
    share = float(by_y.max() / tot) if tot > 0 else float("nan")

    def rerun(cols):
        Rm = R.drop(columns=cols)
        i = _quiet(EX.run_k1, Rm, inc_cfg, D, S, days)["net"]
        c = _quiet(EX.run_k1, Rm, cha_cfg, D, S, days)["net"]
        return dsr(i, c)
    mk = {}
    for m in (markets if markets is not None else list(R.columns)):
        mk[m] = rerun([m])
    cl = {}
    for c, pre in G.CLASSES.items():
        cols = [k for k in R.columns if k.startswith(pre)]
        if cols:
            cl[c] = rerun(cols)

    def worst(d):
        d = {k: v for k, v in d.items() if v == v}
        if not d:
            return None, float("nan")
        k = min(d, key=lambda x: d[x])
        return k, full - d[k]
    return {"full": full, "year": worst(yr), "market": worst(mk), "class": worst(cl), "year_share": share,
            "best_year": int(by_y.idxmax()) if len(by_y) else None, "diff_sum": tot, "n_markets": len(mk)}


# =====================================================================================================================
# the registered report
# =====================================================================================================================
def report(R, D, S, gspc, out=print, inc_cfg=None, cha_cfg=None, as_run=None, trials_path=None,
           frag_markets=None, do_fragility=True):
    """The registered A2 report (CHANGES A2 items 3-6). R, S: the A1 panel; D, gspc: free daily inputs. as_run: the
    incumbent's registered A1-report Sharpe ratios (None = no check, tests). Returns dict(verdict, books, ...)."""
    from gm import config as CF
    from gm import execution as EX
    from gm import seal as SL
    from gm import stats as ST
    inc_cfg = inc_cfg or CF.A1_INCUMBENT
    cha_cfg = cha_cfg or CF.A2_CHALLENGER
    T = SL.resolve(SL.DESIGN)
    R, D, S, gspc = SL.cut_inputs(T, R, D, S, gspc)
    SL.check_output({"R": R, "S": S}, T, "a2_batch.report inputs")
    days = EX.nyse_days(gspc=gspc)
    bi = books(R, D, S, days, inc_cfg)
    # ---- the incumbent as run (A1 report) before any other statistic
    if as_run:
        got = {t: round(ST.sharpe(_cut(bi[(t, 1.0)]["net"], *WIN)), 3) for t in as_run}
        ok = all(abs(got[t] - as_run[t]) < 5e-4 for t in as_run)
        out("%s incumbent as run (A1 report, net Sharpe 1975-2010): %s | registered %s" % (
            "PASS" if ok else "FAIL", ", ".join("%s %.3f" % kv for kv in sorted(got.items())),
            ", ".join("%s %.3f" % kv for kv in sorted(as_run.items()))))
        if not ok:
            raise AsRunMismatch("the incumbent does not reproduce the A1 run")
    bc = books(R, D, S, days, cha_cfg)
    for bb in (bi, bc):
        for v in bb.values():
            SL.check_output(v["net"], T, "a2_batch.report")
    names = (("incumbent", inc_cfg, bi), ("challenger", cha_cfg, bc))
    out("--- A2 (TESTING_PROTOCOL 7.6 step 3; gm/CHANGES.md A2): incumbent %s (%s) as run vs challenger %s (%s), "
        "A1 panel, design months only, net of costs" % (inc_cfg["name"], CF.cfg_hash(inc_cfg), cha_cfg["name"],
                                                        CF.cfg_hash(cha_cfg)))
    # ---- decisive
    hyg = {}
    for tm, _ in TIMINGS:
        hyg[tm] = hygiene(bi[(tm, 1.0)]["net"], bc[(tm, 1.0)]["net"], bi[(tm, 2.0)]["net"], bc[(tm, 2.0)]["net"], *WIN)
    h = hyg["k1"]
    verdict = "PASS" if h["pass"] else "FAIL"
    out("--- DECISIVE (7.7 H1, H3; k = 1; pooled window %s..%s, common months; paired stationary bootstrap 10,000, "
        "block 6, seed 20261101; margin -0.10; no Holm)" % WIN)
    out(_hyg_line("k1", h))
    out("--- reported beside (not decisive): the same lines at k = 0 and at the one-month delay")
    for tm in ("k0", "d1"):
        out(_hyg_line(tm, hyg[tm]))
    out("--- eras (7.1 F2: reported, not decisive): dSR | lb95 | se per era and timing")
    for tm, _ in TIMINGS:
        for era, a, b in ERAS[1:]:
            e = hygiene(bi[(tm, 1.0)]["net"], bc[(tm, 1.0)]["net"], bi[(tm, 2.0)]["net"], bc[(tm, 2.0)]["net"], a, b)
            out("ERA | %s | %s | n %d | dSR %+.3f | lb95 %+.3f | se %.3f | H3 margins %s" % (
                tm, era, e["n"], e["dsr"], e["lb95"], e["se"], _margins(e["tail"])))
    infl = selection_inflation(trials_path) if trials_path else None
    if infl:
        out("selection inflation (7.8 item 2; printed beside, not subtracted, 7.1 F9): %d logged book / pod rows "
            "(%s), mean 1990-2010 Sharpe %.3f, sd %.3f, z %.2f -> expected best Sharpe from luck alone about +%.2f" % (
                infl["n"], ", ".join("%s %d" % kv for kv in sorted(infl["by_family"].items())), infl["mean"],
                infl["sd"], infl["z"], infl["inflation"]))
    out(KNOBS)
    # ---- books
    out("--- books: months | net Sharpe | mean %/yr | vol %/yr | max drawdown % | skew | Lo-adjusted Sharpe")
    for nm, _cfg, bb in names:
        for tm, _ in TIMINGS:
            for cm in (1.0, 2.0):
                for era, a, b in ERAS:
                    s = bstats(bb[(tm, cm)]["net"], a, b)
                    if s is None:
                        out("BOOK | %s | %s | costs x%d | %s | too few months" % (nm, tm, cm, era))
                        continue
                    out("BOOK | %s | %s | costs x%d | %s | %d | %.3f | %.2f | %.2f | %.1f | %.2f | %.2f" % (
                        nm, tm, cm, era, s["n"], s["sr"], s["mean"] * 100, s["vol"] * 100, s["maxdd"] * 100,
                        s["skew"], s["lo"]))
    # ---- by version and pod alone (k = 1)
    out("--- by version (challenger): each version as a complete pod alone (one-part equal-risk book, k = 1, 10%, caps, "
        "costs): net Sharpe (months) 1975-2010 | 1975-89 | 1990-2010")
    pos_share = {}
    for pod, v, label in versions(cha_cfg):
        r = pod_alone(R, D, S, days, cha_cfg, [(pod, "*", v)])
        s = sr_or(r, *WIN)[0]
        pos_share.setdefault(pod, []).append(s)
        out("VERSION | %s | %s" % (label, " | ".join(fmt_sr(r, a, b) for _e, a, b in ERAS)))
    allv = [x for xs in pos_share.values() for x in xs if x is not None]
    out("share of versions with net Sharpe > 0 (1975-2010): %s; all %d of %d" % (
        ", ".join("%s %d of %d" % (p, sum(1 for x in xs if x is not None and x > 0), len(xs))
                  for p, xs in pos_share.items()), sum(1 for x in allv if x > 0), len(allv)))
    out("--- each pod alone (k = 1): net Sharpe (months) 1975-2010 | 1975-89 | 1990-2010")
    for nm, cfg, _bb in names:
        for pod in PODS:
            r = pod_alone(R, D, S, days, cfg, [(pod, "*", "*")])
            out("POD | %s | %s | %s" % (nm, pod, " | ".join(fmt_sr(r, a, b) for _e, a, b in ERAS)))
    for v in (1, 2):
        r = pod_alone(R, D, S, days, inc_cfg, [("carry", "*", v)])
        out("POD | incumbent | carry v%d | %s" % (v, " | ".join(fmt_sr(r, a, b) for _e, a, b in ERAS)))
    # ---- by class and era (contributions, k = 1, before costs)
    import a1_panel as A1
    from gm import signals as G
    out("--- by class and era (k = 1 contributions, held family positions x k = 1 returns, before costs): Sharpe "
        "(months) 1975-2010 | 1975-89 | 1990-2010")
    for nm, _cfg, bb in names:
        bk = bb[("k1", 1.0)]
        cb = A1.contrib_k1(bk)
        for (f, c) in sorted(cb, key=str):
            out("CLASS | %s | %s/%s | %s" % (nm, f, c, " | ".join(fmt_sr(cb[(f, c)], a, b) for _e, a, b in ERAS)))
        for f in sorted(bk["fam_pos"]):
            r = contrib_fam(bk, f)
            out("CLASS | %s | %s/all | %s" % (nm, f, " | ".join(fmt_sr(r, a, b) for _e, a, b in ERAS)))
        for c, pre in G.CLASSES.items():
            rs = [cb[k] for k in cb if k[1] == c]
            if rs:
                r = pd.concat(rs, axis=1).sum(axis=1, min_count=1)
                out("CLASS | %s | all/%s | %s" % (nm, c, " | ".join(fmt_sr(r, a, b) for _e, a, b in ERAS)))
    # ---- weekly check
    out("--- by tranche (weekly check, 7.3 item 6, %s..%s): net Sharpe (months) per tranche and of the tranche form; "
        "flagged share of gross position" % WEEKLY)
    trn = {}
    for nm, cfg, _bb in names:
        tr = _quiet(EX.tranches, R, cfg, D, S, days)
        trn[nm] = tr
        for jj in (0, 1, 2, 3):
            b = tr["tranche"][jj]
            out("TRANCHE | %s | j %d | %s | flagged share %.3f" % (nm, jj, fmt_sr(b["net"], *WEEKLY),
                                                                    flag_share(b, tr["flags"][jj], *WEEKLY)))
        out("TRANCHE | %s | form | %s" % (nm, fmt_sr(tr["net"], *WEEKLY)))
    t = ST.paired_sr_test(_cut(trn["incumbent"]["net"], *WEEKLY), _cut(trn["challenger"]["net"], *WEEKLY))
    out("TRANCHE | tranche form challenger - incumbent | n %d | dSR %+.3f | lb95 %+.3f (reported)" % (
        t["n"], t["dsr"], t["lb95"] if t["lb95"] == t["lb95"] else float("nan")))
    # ---- Trend's split, carry and price
    out("--- Trend split (SPEC_Trend s14; register B12, T12): class-average and relative parts, k = 1, before costs: "
        "Sharpe (months) 1975-2010 | 1975-89 | 1990-2010")
    splits = {}
    for nm, cfg, bb in names:
        bk = bb[("k1", 1.0)]
        sp = trend_split(R, D, S, cfg, bk)
        splits[nm] = sp
        RE = bk["R_earn"]
        out("SPLIT | %s | check: parts add to the held Trend position (max diff %.1e; rebuild of the held position %.1e;"
            " months without a scale %d) %s" % (nm, sp["maxdiff_parts"], sp["maxdiff_held"], sp["months_no_scale"],
                                                "PASS" if sp["maxdiff_parts"] < 1e-9 else "FAIL"))
        for part in ("avg", "rel"):
            r = part_return(sp[part], RE)
            out("SPLIT | %s | %s | all | %s" % (nm, "class-average" if part == "avg" else "relative",
                                               " | ".join(fmt_sr(r, a, b) for _e, a, b in ERAS)))
            for c, pre in G.CLASSES.items():
                cols = [k for k in sp[part].columns if k.startswith(pre)]
                r = part_return(sp[part], RE, cols)
                out("SPLIT | %s | %s | %s | %s" % (nm, "class-average" if part == "avg" else "relative", c,
                                                   " | ".join(fmt_sr(r, a, b) for _e, a, b in ERAS)))
    out("--- Trend carry and price parts (SPEC_Trend s10; bonds and currencies, k = 1, before costs; market-months with "
        "a held position and a carry value): Sharpe (months) | mean %/yr, 1975-2010 | 1975-89 | 1990-2010")
    for nm, _cfg, bb in names:
        tot, car, pri, cov = carry_price(bb[("k1", 1.0)], S["C"])
        out("CARRYPRICE | %s | covered share of Trend's FX + FI gross position %.3f" % (nm, cov))
        for lab, r in (("total", tot), ("carry part", car), ("price part", pri)):
            cells = []
            for _e, a, b in ERAS:
                x = _cut(r, a, b)
                cells.append("%s | %.2f" % (fmt_sr(r, a, b), x.mean() * 1200) if len(x) >= MIN_PRINT else
                             "n<%d" % MIN_PRINT)
            out("CARRYPRICE | %s | %s | %s" % (nm, lab, " | ".join(cells)))
    # ---- Value next to Trend; Economic trend next to Trend
    out("--- Value next to Trend (SPEC_Value s14; k = 1 contributions before costs, 1975-2010): correlation | NW t of "
        "Value's intercept on Trend | correlation with Trend's relative part")
    bik, bck = bi[("k1", 1.0)], bc[("k1", 1.0)]
    vt = {"inc": contrib_fam(bik, "trend"), "cha": contrib_fam(bck, "trend")}
    vrel = {"inc": part_return(splits["incumbent"]["rel"], bik["R_earn"]),
            "cha": part_return(splits["challenger"]["rel"], bck["R_earn"])}
    vv = {"inc": contrib_fam(bik, "value"), "cha": contrib_fam(bck, "value")}
    for lab, v, tr_ in (("incumbent Value (v1) / incumbent Trend (1/3/12)", "inc", "inc"),
                        ("challenger Value (v1 + v2) / incumbent Trend (old grid)", "cha", "inc"),
                        ("challenger Value (v1 + v2) / challenger Trend (16 versions)", "cha", "cha")):
        j = pd.concat([_cut(vv[v], *WIN), _cut(vt[tr_], *WIN), _cut(vrel[tr_], *WIN)], axis=1).dropna()
        if len(j) < MIN_PRINT:
            out("VALUE | %s | n<%d" % (lab, MIN_PRINT))
            continue
        out("VALUE | %s | n %d | corr %.2f | NW t %.2f | corr with relative part %.2f" % (
            lab, len(j), j.iloc[:, 0].corr(j.iloc[:, 1]), ST.nw_alpha_t(j.iloc[:, 0], j.iloc[:, 1]),
            j.iloc[:, 0].corr(j.iloc[:, 2])))
    for nm, _cfg, bb in names:
        c, n = eq_pos_corr(bb[("k1", 1.0)])
        out("ECON-TREND | %s | held equity positions, both non-zero, 1975-2010 | n %d | corr %s" % (
            nm, n, "%.2f" % c if c is not None else "n<%d" % MIN_PRINT))
    # ---- flagged share, P4
    out("--- k = 1 flagged share (7.3 item 2): share of gross position earning the k = 0 return for lack of a daily "
        "price")
    for nm, _cfg, bb in names:
        bk = bb[("k1", 1.0)]
        fs = EX.flag_share_by_year(bk["pos"], bk["k1_flags"]).loc[1975:2010].dropna()
        out("FLAGGED | %s | 1975-2010 %.3f | by year: %s" % (nm, flag_share(bk, bk["k1_flags"], *WIN),
                                                             ", ".join("%d %.2f" % (int(y), v) for y, v in fs.items())))
    out("--- P4 (7.7; S&P alone until M1 has run): Sharpe of the book and of its specific return w = r - b x S&P, "
        "%s..%s, k = 1 net" % (P4_FROM, WIN[1]))
    m = R["eq_us_spx"] if "eq_us_spx" in R.columns else None
    for nm, _cfg, bb in names:
        r = bb[("k1", 1.0)]["net"]
        if m is None:
            out("P4 | %s | no eq_us_spx in the panel" % nm)
            continue
        w = p4(r, m)
        out("P4 | %s | book %s | specific %s" % (nm, fmt_sr(r, P4_FROM, WIN[1]), fmt_sr(w, P4_FROM, WIN[1])))
    # ---- fragility
    fr = None
    if do_fragility:
        fr = fragility(R, D, S, days, inc_cfg, cha_cfg, bi[("k1", 1.0)]["net"], bc[("k1", 1.0)]["net"], frag_markets)
        out("--- fragility (7.7; pooled k = 1 dSR %+.3f): largest loss when one item is removed" % fr["full"])
        for lab in ("year", "market", "class"):
            k, loss = fr[lab]
            out("FRAGILITY | %s | %s | loss of dSR %+.3f" % (lab, k, loss) if k is not None else
                "FRAGILITY | %s | none" % lab)
        out("FRAGILITY | markets tried %d | best year %s gives %s of the summed monthly difference %s | flag %s" % (
            fr["n_markets"], fr["best_year"], "%.2f" % fr["year_share"] if fr["year_share"] == fr["year_share"] else
            "n/a", "(sum %+.2f%%)" % (fr["diff_sum"] * 100), "ON" if fr["year_share"] == fr["year_share"] and
            fr["year_share"] > FRAG_SHARE else ("n/a (sum not positive)" if fr["diff_sum"] <= 0 else "off")))
    # ---- verdict
    final = cha_cfg if h["pass"] else inc_cfg
    out("A2 VERDICT %s | H1 lb95 %+.3f %s -0.10 | H3 %s | A2-final book = %s (%s)%s" % (
        verdict, h["lb95"] if not h["identical"] else 0.0, ">" if h["H1"] else "<=", "pass" if h["H3"] else "fail",
        final["name"], CF.cfg_hash(final), "" if h["pass"] else
        " | the incumbent stays without averaging; no cell of a grid is picked"))
    return {"verdict": verdict, "hyg": hyg, "inc": bi, "cha": bc, "final": final, "fragility": fr,
            "inflation": infl}


def _margins(tl):
    return "max fall %+.1f pts, worst month %+.1f pts" % ((tl["dd_cha"] - tl["dd_inc"]) * 100,
                                                         (tl["wm_cha"] - tl["wm_inc"]) * 100)


def _hyg_line(tm, h):
    lb = 0.0 if h["identical"] else h["lb95"]
    return ("HYGIENE | %s | n %d | dSR %+.3f | lb95 %+.3f | se %.3f | H1 %s | H2 dSR at 2x costs %+.3f (reported) | "
            "H3 %s (%s; max drawdown incumbent %.1f%%, challenger %.1f%%) | %s" % (
                tm, h["n"], h["dsr"], lb, h["se"] if h["se"] == h["se"] else 0.0, "PASS" if h["H1"] else "FAIL",
                h.get("H2_dsr_2x", float("nan")), "PASS" if h["H3"] else "FAIL", _margins(h["tail"]),
                h["tail"]["dd_inc"] * 100, h["tail"]["dd_cha"] * 100,
                "PASS" if h["pass"] else "FAIL"))


def trial_row(res, panel_id_, engine_version, lock_id=LOCK_V2):
    """The gm/trials.csv row of family 'book' for the challenger at k = 1 on the A1 panel (gm/trials.py columns)."""
    from gm import config as CF
    from gm import stats as ST
    cfg = CF.A2_CHALLENGER
    net = res["cha"][("k1", 1.0)]["net"]
    d, e = ST.summary(net), ST.summary(net, *ST.EXTRA)
    h = res["hyg"]["k1"]
    return {"trial": "A2 grids (challenger, k = 1, A1 panel)", "family": "book", "hash": CF.cfg_hash(cfg),
            "sr_9010": round(d["sr"], 3), "t_9010": round(d["t"], 2), "maxdd_9010": round(d["maxdd"], 3),
            "sr_7589": round(e["sr"], 3),
            "turnover": round(float(ST.cut(res["cha"][("k1", 1.0)]["turnover"], *ST.DESIGN).mean() * 12), 1),
            "note": "TESTING_PROTOCOL 7.6 step 3 A2 challenger; engine %s; A1 panel %s; LOCK_v2 %s; incumbent "
                    "A1_INCUMBENT %s as run; verdict %s (H1 lb95 %+.3f, H3 %s)" % (
                        engine_version, panel_id_[:16], lock_id[:16], CF.cfg_hash(CF.A1_INCUMBENT), res["verdict"],
                        h["lb95"], "pass" if h["H3"] else "fail")}
