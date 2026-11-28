"""b2_batch: Batch B2 = Strip reversion and the ten card rule layers judged in B2 (TESTING_PROTOCOL 7.6 step 9, 7.7,
7.8), as registered in gm/CHANGES.md "Batch B2" (2026-11-28, before this code). Runs where the LSEG store and the A1
panel exist (the user's PC); tested in the cloud on synthetic panels and a mock LSEG store with invented settlements.

Strip reversion (SPEC_Strip_reversion; entry item 4): per currency (Eurodollar, Euribor), the first eight quarterly
3-month rate contracts, local bends (S_n adjacent spreads, version A; K_n adjacent curvatures, version B) against their
expanding normals by expiry month, cost gate, stale screen, sign-only level-neutral contract weights, hybrid volatility
of today's contract vector on the strip history, versions averaged, one block, the pod alone at the book's 10% target,
the strip-vector cap (E11), 5x gross cap at 0.25 / 1.9, contract-level costs, native k = 1 (trade at the next
settlement). Card rule layers (entry item 5): the diag_preb 1.1.1 rule states per version, entry E3, fixed sizes, k = 1
monthly or card 4's daily windows on E14, held size 0.10 / 0.40, book.run costs. Every item is tested against the EMPTY
Core book v1 (alpha = the item's own mean) and labelled on its own.

API
  strip_contracts(view)                     entry 4a: {root: {(y, m): series id}} (Datastream daily, quarterly)
  strip_prepare(contracts, days)            entry 4b-4i: strip, measures, normals, gaps, stale screen, returns, vols
  strip_scores(sp), strip_run(sp, ...)      entry 4f-4p: scores, positions, the pod alone
  strip_r1_counts(sp)                       entry 9a: R1's counts from b2's own tables
  card_inputs_view(R, D, gspc, ci, fxv, tb3, eps)        entry 5a
  card_rules(inp)                           entry 5b-5e: the ten rules, their versions and units
  rule_positions(rule, inp, ...), rule_run(rule, inp, ...)   positions, k = 1 returns, costs (5f-5i)
  identity(inp, rules, sp, DP inputs)       entry 9
  truncation(...)                           entry 10
  report(...)                               entry items 6-8, 11; returns the result dict
  trial_rows(res)                           entry item 12
"""
import datetime as dt
import json
import os
import re

import numpy as np
import pandas as pd

import diag_preb as DP

VERSION = "b2_batch-1.0.1"   # 1.0.1 (CHECK_B2): M1 flat strip months hold 0, T3 over the span; M2 card 4 falsifier n
LSEG_LOCK = "90322681b9f989cc24393ae7de4fe24bf5af2f32074ffa6400b1cbed09c4074c"          # LOCK_LSEG_v5
CARD_LOCK = "6c154f7d736cefd141fac2252a71536811e7440724d8e3cb4d4eacfecb8e3110"          # LOCK_CARD_v1
A1_PANEL_ID = "e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43"
LOCK_V2 = "d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9"
ENGINE = "gm-2.2.1"
REF_SHA = "cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39"
CFG_HASHES = {"BASE": "f1d682c384", "CANDIDATE": "438a092b53", "A1_INCUMBENT": "77374d7bef",
              "A2_CHALLENGER": "1faa343535"}
FINAL_NAME, FINAL_HASH = "gm-2.0.4-candidate-x1", "77374d7bef"
TRIAL_ROWS_SHA = "4fd1775ecdbf4bf073d2cce984fb5b3fe07919d3659502fcb8f783a4b2a53a09"     # book / pod rows, N = 42
TRIAL_ROWS_N = 42
A2_REPORT, CORE_REPORT, PREB_REPORT, B1_REPORT = "gm_a2_v1.txt", "gm_core_v1.txt", "gm_diag_preb_v1.txt", "gm_b1_v1.txt"
SEAL = pd.Timestamp("2010-12-31")
LAST = pd.Period("2010-12", "M")
DEC_LAST = pd.Period("2010-11", "M")          # 7.3 item 5: the decision at month-end 2010-12 is never traded
STRIP_DEC_LAST = pd.Period("2010-10", "M")    # spec s7: last return month 2010-11
ERAS = (("1975-89", "1975-01", "1989-12"), ("1990-2010", "1990-01", "2010-12"))
P4_FROM = "1978-01"
MIN_PRINT = 60
MIN_WINDOW = 120
SEED = 20261101
NBOOT = 10000
NPLACEBO = 1000
HELD = 0.10 / 0.40            # 7.7 held size of a rule layer
BOOK_VOL, RISK_CAP, GROSS_CAP, BLOCK_MONTHS, SCALER_MIN, BLOCK_CAP = 0.10, 0.10, 5.0, 36, 24, 50.0
VOL_CFG = {"vol": {"model": "hybrid", "hl_days": 35, "hl_months": 6, "fast_w": 0.7, "floor": 0.75}}  # CANDIDATE's

# ------------------------------------------------------------------------------------------------- Strip constants
STRIP = (("ED", "sr_usd"), ("FEI", "sr_eur"))
STRIP_CODE = re.compile(r"^<?(ED|FEI)([HMUZ])(\d)\^(\d)>?$", re.I)
MONTHS = "FGHJKMNQUVXZ"
STRIP_START = pd.Period("1990-01", "M")
GATE_C = 0.5                  # bp of rate per contract per side (spec s9)
PTS = 0.25 / 100.0            # return per unit notional per price point (spec s3 step 11)
COST_NOTIONAL = 0.125e-4      # 0.5 bp of rate x 0.25 = 0.125 bp of notional one way (spec s9)
GROSS_W = 0.25 / 1.9          # 2-year equivalent (gm/variants.py st_us_3m; E11)
KEYS_A = tuple(("S", n) for n in range(2, 9))
KEYS_B = tuple(("K", n) for n in range(2, 8))
KEYS = KEYS_A + KEYS_B
STRESS = (("1998-08", "1998-10"), ("2007-07", "2007-08"), ("2008-09", "2008-12"))    # spec s10 item 5

RULES = ("card 1 R1", "card 1 R2", "card 1 R5", "card 2 R1", "card 2 R2", "card 3 R2", "card 3 R4", "card 4 R1",
         "card 4 R3", "card 4 R5")
C2_KEPT = {"card 2 R1": [("third", False), ("third", True)], "card 2 R2": [(1.5, False), (1.0, False)]}
PREB_NEEDS = ("R1: PASS", "C2-D1: FAIL", "C2-D2: R1 2 of 4 versions kept, R2 2 of 4 versions kept",
              "C4-D1: FAIL", "C4-D2: R5 stays", "C5-D2: FAIL") + tuple("%s judged in B2" % r for r in RULES)
KNOBS = {"Strip reversion": "1 (the hybrid volatility estimator, 7.8 item 3)",
         "card 1 R1": "2 (hybrid estimator; the R4 gate version chosen with post-2010 sight)",
         "card 1 R2": "2 (hybrid estimator; the R4 gate version chosen with post-2010 sight)",
         "card 1 R5": "1 (hybrid estimator)",
         "card 2 R1": "2 (hybrid estimator; the hedge gate seen in a related rule, Macro Compass)",
         "card 2 R2": "1 (hybrid estimator)",
         "card 3 R2": "2 (hybrid estimator; the 1.0 bar chosen with post-2010 sight)",
         "card 3 R4": "1 (hybrid estimator)", "card 4 R1": "1 (hybrid estimator)", "card 4 R3": "1 (hybrid estimator)",
         "card 4 R5": "1 (hybrid estimator)"}


class AsRunMismatch(RuntimeError):
    pass


class IdentityFail(RuntimeError):
    pass


class WindowGap(RuntimeError):
    """1.0.1 M1: the Strip window has an interior gap (the job STOPs)."""


# =====================================================================================================================
# job checks
# =====================================================================================================================
def _lines(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read().splitlines()


def core_facts(path):
    return DP.core_facts(path)


def preb_facts(path):
    """gm_diag_preb_v1 report: 'PREB JOB DONE' and the PREB SUMMARY line with the outcomes of entry item 2 (9d)."""
    if not os.path.exists(path):
        return False, "missing (%s)" % os.path.basename(path)
    L = _lines(path)
    if not any(x.strip() == "PREB JOB DONE" for x in L):
        return False, "no 'PREB JOB DONE' line"
    s = [x for x in L if x.startswith("PRE-B SUMMARY |")]
    if len(s) != 1:
        return False, "not exactly one PRE-B SUMMARY line"
    miss = [n for n in PREB_NEEDS if n not in s[0]]
    if miss:
        return False, "PRE-B SUMMARY lacks: %s" % "; ".join(miss)
    return True, "ok"


def b1_facts(path):
    """gm_b1_v1 report: 'B1 JOB DONE' and the B1 VERDICT line ending SHELVED (Curve carry not moved to B2)."""
    if not os.path.exists(path):
        return False, "missing (%s)" % os.path.basename(path)
    L = _lines(path)
    if not any(x.strip() == "B1 JOB DONE" for x in L):
        return False, "no 'B1 JOB DONE' line"
    v = [x for x in L if x.startswith("B1 VERDICT | Curve carry")]
    if len(v) != 1 or not v[0].rstrip().endswith("SHELVED"):
        return False, "no B1 VERDICT line ending SHELVED"
    return True, "ok"


def lseg_lock_of(work_dir):
    return DP.lseg_lock_of(work_dir)


def preb_f0(path):
    """1.0.1 C3: {rule: (held months, episodes)} from the pre-B report's 'F0 | <rule> | held months N | episodes E'."""
    out = {}
    for x in _lines(path):
        m = re.match(r"^F0 \| (card \d R\d) \| held months (\d+) \| episodes (\d+) \|", x)
        if m:
            out[m.group(1)] = (int(m.group(2)), int(m.group(3)))
    return out


def strip_catalog_counts(view):
    """1.0.1 C4: catalog rows (daily, ok, primary, Datastream) whose code starts with ED / FEI (any month letter)."""
    c = view.cat
    c = c[(c["per"] == "D") & (c["status"] == "ok") & (c["duplicate_of"] == "") &
          c["series_id"].astype(str).str.startswith("DS:")]
    code = c["code"].astype(str).str.strip().str.lstrip("<").str.upper()
    return {"ED": int(code.str.match(r"^ED[FGHJKMNQUVXZ]\d").sum()), "FEI": int(code.str.startswith("FEI").sum())}


# =====================================================================================================================
# small helpers
# =====================================================================================================================
def cell(v, n, fmt="%.2f"):
    """Printing rule (entry item 11): the value over >= 60 months, else the count and the sign only."""
    if v is None or v != v:
        return "n %d, n/a" % n
    if n >= MIN_PRINT:
        return (fmt % v) + " (%d)" % n
    return "n %d, sign %s" % (n, "+" if v > 0 else ("-" if v < 0 else "0"))


def _di(y, m):
    return y * 12 + m - 1


def _diff(a, b, T):
    """Differing cells of two frames / series on months (or days) <= T (missing = missing is equal)."""
    if isinstance(a, pd.Series):
        a, b = a.to_frame(), b.to_frame()
    if isinstance(a.index, pd.PeriodIndex):
        Tp = pd.Period(T, "M") if not isinstance(T, pd.Period) else T
        a, b = a.loc[a.index <= Tp], b.loc[b.index <= Tp]
    else:
        a, b = a.loc[a.index <= pd.Timestamp(T)], b.loc[b.index <= pd.Timestamp(T)]
    cols = sorted(set(a.columns) | set(b.columns), key=str)
    idx = a.index.union(b.index)
    x = a.reindex(index=idx, columns=cols).astype(float).to_numpy()
    y = b.reindex(index=idx, columns=cols).astype(float).to_numpy()
    eq = (x == y) | (np.isnan(x) & np.isnan(y)) | (np.abs(x - y) <= 1e-10 * np.maximum(1, np.abs(x)))
    return int((~eq).sum())


# =====================================================================================================================
# Strip reversion (entry item 4)
# =====================================================================================================================
def strip_delivery(code):
    """'<EDH0^9>' -> ('ED', (1990, 3)); serial months and other roots -> None (decade digit >= 5 -> 19xx)."""
    m = STRIP_CODE.match(str(code).strip().upper())
    if not m:
        return None
    dec, yd = int(m.group(4)), int(m.group(3))
    return m.group(1).upper(), ((1900 if dec >= 5 else 2000) + 10 * dec + yd, MONTHS.index(m.group(2)) + 1)


def strip_contracts(view):
    """Entry 4a: catalog rows per D, status ok, duplicate_of empty, function DS, quarterly ED / FEI codes."""
    c = view.cat
    c = c[(c["per"] == "D") & (c["status"] == "ok") & (c["duplicate_of"] == "") &
          c["series_id"].astype(str).str.startswith("DS:")]
    out = {r: {} for r, _ in STRIP}
    for r in c.itertuples():
        d = strip_delivery(r.code)
        if d is not None and d[1] not in out[d[0]]:
            out[d[0]][d[1]] = r.series_id
    return out


def quarterly_ltd(root, y0=1980, y1=2014):
    import lseg_rules as LR
    return {(y, m): LR.dates(root, y, m)[0] for y in range(y0, y1 + 1) for m in (3, 6, 9, 12)}


def weights(key):
    """Spec s3 step 7: contract weights (on rates) of a measure, contracts 1..8."""
    kind, n = key
    w = np.zeros(8)
    if kind == "S":
        w[n - 1] = 1.0 / n
        w[:n - 1] = -1.0 / (n * (n - 1))
    else:
        w[n] = -1.0 / (n + 1)
        w[n - 1] = (n + 2.0) / (n * (n + 1))
        w[:n - 1] = -2.0 / ((n - 1) * n * (n + 1))
    return w


def gate_level(key):
    kind, n = key
    A = 2.0 / n if kind == "S" else (2.0 * n + 4) / (n * (n + 1))
    return 2 * GATE_C * A


W = np.array([weights(k) for k in KEYS])          # (13, 8)
GATES = np.array([gate_level(k) for k in KEYS])


def _first_day(month, days_by_m):
    return days_by_m.get(month)


def strip_prepare(contracts, days, plant=None):
    """Entry 4b-4i. contracts {root: {(y, m): daily settlement Series}}; days = NYSE days (<= 2010-12-31).
    plant: None, or 'normal_next' (the truncation control: each normal also holds the NEXT month-end's value)."""
    days = pd.DatetimeIndex(days).normalize().unique().sort_values()
    days = days[days <= SEAL]
    first_of = pd.Series(days, index=days).groupby(days.to_period("M")).min()
    out = {"roots": {}, "days": days}
    for root, mk in STRIP:
        cons = contracts.get(root) or {}
        if not cons:
            continue
        ltd = quarterly_ltd(root)
        keys = sorted(ltd)
        px = pd.DataFrame({k: cons[k].reindex(days) if k in cons else pd.Series(np.nan, index=days) for k in keys},
                          index=days)
        have = px.notna().any(axis=1)
        if not have.any():
            continue
        d0 = px.index[have.to_numpy()][0]
        rate = (100.0 - px) * 100.0
        ch = (px.notna() & px.shift(1).notna() & (px != px.shift(1))).astype(float)
        nchg = ch.shift(1).rolling(20, min_periods=20).sum()
        pos = {d: i for i, d in enumerate(days)}
        me = pd.Series(days, index=days).groupby(days.to_period("M")).max()
        me = me[me.index >= d0.to_period("M")]
        grid = pd.period_range(me.index[0], LAST, freq="M")
        T = len(grid)
        hist, first = {}, {}
        M = {k: np.full(T, np.nan) for k in KEYS}         # measures at d
        NRM = {k: np.full(T, np.nan) for k in KEYS}       # normals at d
        M1 = {k: np.full(T, np.nan) for k in KEYS}        # measures at d1 on d's strip (R1 identity)
        STL = {k: np.zeros(T, bool) for k in KEYS}        # a contract of the measure fails the stale screen at d
        full = np.zeros(T, bool)
        full1 = np.zeros(T, bool)
        strip = [None] * T
        dd, d1d = [None] * T, [None] * T
        rvec = np.full((T, 8), np.nan)
        vals_next = {}
        if plant == "normal_next":                       # control only: next month-end values (dated after d)
            for i, p in enumerate(grid):
                if p in me.index:
                    st_ = DP.strip_of(p, ltd)
                    r_ = rate.loc[me[p], st_].to_numpy(dtype=float)
                    vals_next[i] = (st_, DP.measures(r_))
        for i, p in enumerate(grid):
            if p not in me.index:
                continue
            d = me[p]
            st = DP.strip_of(p, ltd)
            strip[i] = st
            dd[i] = d
            r = rate.loc[d, st].to_numpy(dtype=float)
            rvec[i] = r
            meas = DP.measures(r)
            full[i] = bool(np.all(np.isfinite(r)))
            j = pos[d]
            d1 = days[j + 1] if j + 1 < len(days) else None
            d1d[i] = d1
            r1v = rate.loc[d1, st].to_numpy(dtype=float) if d1 is not None else None
            full1[i] = r1v is not None and bool(np.all(np.isfinite(r1v)))
            m1 = DP.measures(r1v) if full1[i] else {}
            for key in KEYS:
                g = st[key[1] - 1][1]
                h = hist.get((key, g))
                if key in first and (p.ordinal - first[key].ordinal) >= 60 and h:
                    vals = [v for _, v in h]
                    if plant == "normal_next" and (i + 1) in vals_next:
                        stn, mn = vals_next[i + 1]
                        if key in mn and stn[key[1] - 1][1] == g:
                            vals = vals + [mn[key]]
                    NRM[key][i] = float(np.mean(vals))
                if key in meas:
                    M[key][i] = meas[key]
                if key in m1:
                    M1[key][i] = m1[key]
                STL[key][i] = any(not (nchg.at[d, k] >= 15) for k in st[:DP.uses(key)])
            for key, v in meas.items():
                g = st[key[1] - 1][1]
                hist.setdefault((key, g), []).append((p, v))
                first.setdefault(key, p)
        # start (spec s7; R1 j): first month >= 1990-01 with the strip and every measure of one version normalised
        start = None
        for i, p in enumerate(grid):
            if p < STRIP_START or not full[i]:
                continue
            okA = all(np.isfinite(NRM[k][i]) for k in KEYS_A)
            okB = all(np.isfinite(NRM[k][i]) for k in KEYS_B)
            if okA or okB:
                start = p
                break
        # returns per slot (entry 4k) and the decision-day form (falsifier 2) and the delay form
        RE = np.full((T, 8), np.nan)       # return month t: contract in slot j at decision t-1
        RE0 = np.full((T, 8), np.nan)      # return month t: decision-day settlement t-1 to decision-day settlement t
        RE2 = np.full((T, 8), np.nan)      # return month t: contract in slot j at decision t-2 (one-month delay)
        miss = 0
        for i in range(1, T):
            p = grid[i]
            st = strip[i - 1]
            if st is None:
                continue
            en, ex = _first_day(p, first_of), _first_day(p + 1, first_of)
            if en is not None and ex is not None:
                a = px.loc[en, st].to_numpy(dtype=float)
                b = px.loc[ex, st].to_numpy(dtype=float)
                RE[i] = (b - a) * PTS
                if full[i - 1]:
                    miss += int(np.sum(~np.isfinite(RE[i])))
            if dd[i] is not None and dd[i - 1] is not None:
                RE0[i] = (px.loc[dd[i], st].to_numpy(dtype=float) - px.loc[dd[i - 1], st].to_numpy(dtype=float)) * PTS
            if i >= 2 and strip[i - 2] is not None and en is not None and ex is not None:
                st2 = strip[i - 2]
                RE2[i] = (px.loc[ex, st2].to_numpy(dtype=float) - px.loc[en, st2].to_numpy(dtype=float)) * PTS
        # volatility histories (entry 4i): slots = first eight quarterly contracts with LTD on or after the day
        dsub = days[days >= d0]
        ltd_arr = np.array([ltd[k] for k in keys], dtype="datetime64[D]")
        P = px.loc[dsub].to_numpy(dtype=float)
        X = np.full((len(dsub), 8), np.nan)
        for t in range(1, len(dsub)):
            tau = np.datetime64(dsub[t].date(), "D")
            alive = np.flatnonzero(ltd_arr >= tau)[:8]
            if len(alive) < 8:
                continue
            X[t] = (P[t, alive] - P[t - 1, alive]) * PTS
        comp = np.all(np.isfinite(X), axis=1)
        X[~comp] = np.nan
        Xf = pd.DataFrame(X, index=dsub, columns=range(8))
        Mf = Xf[comp].groupby(dsub[comp].to_period("M")).sum().reindex(grid)
        mats = vol_matrices(Xf, Mf, grid)
        from gm import config as CF
        from gm import vol as VM
        legv = VM.estimate(Mf, CF.CANDIDATE, Xf)
        out["roots"][root] = {
            "market": mk, "grid": grid, "strip": strip, "d": dd, "d1": d1d, "full": full, "full1": full1,
            "M": M, "N": NRM, "M1": M1, "stale": STL, "start": start, "RE": RE, "RE0": RE0, "RE2": RE2, "r": rvec,
            "ltd": ltd, "X": Xf, "Mret": Mf, "mats": mats, "legvol": legv, "contracts": len(cons),
            "miss_ret": miss, "complete_days": (int(comp[1:].sum()), int(len(dsub) - 1)), "first": me.index[0]}
    return out


def vol_matrices(Xf, Mf, grid):
    """Entry 4i: per month of grid the EWMA (daily, half-life 35, >= 40 days) and monthly EWMA (half-life 6, >= 12)
    second-moment matrices and the 120-month (>= 36) and 36-month (>= 12) sample covariances of the slot returns, so
    that sigma(q) = gm.vol.estimate's hybrid form on the series q . X exactly."""
    T = len(grid)
    gi = {p: i for i, p in enumerate(grid)}
    E = np.full((T, 8, 8), np.nan)
    a = 1 - np.exp(-np.log(2) / 35.0)
    num, den, cnt = np.zeros((8, 8)), 0.0, 0
    X = Xf.to_numpy()
    per = Xf.index.to_period("M")
    last_i = {}
    for t in range(len(X)):
        num *= (1 - a)
        den *= (1 - a)
        if np.isfinite(X[t, 0]):
            num += np.outer(X[t], X[t])
            den += 1.0
            cnt += 1
        last_i[per[t]] = (num.copy() / den if (cnt >= 40 and den > 0) else None)
    for p, v in last_i.items():
        if p in gi and v is not None:
            E[gi[p]] = v
    Mv = Mf.reindex(grid).to_numpy()
    EM = np.full((T, 8, 8), np.nan)
    am = 1 - np.exp(-np.log(2) / 6.0)
    num, den, cnt = np.zeros((8, 8)), 0.0, 0
    for t in range(T):
        num *= (1 - am)
        den *= (1 - am)
        if np.isfinite(Mv[t, 0]):
            num += np.outer(Mv[t], Mv[t])
            den += 1.0
            cnt += 1
        if cnt >= 12 and den > 0:
            EM[t] = num / den
    C120 = np.full((T, 8, 8), np.nan)
    C36 = np.full((T, 8, 8), np.nan)
    ok = np.isfinite(Mv[:, 0])
    for t in range(T):
        for C, w, mp in ((C120, 120, 36), (C36, 36, 12)):
            lo = max(0, t - w + 1)
            rows = Mv[lo:t + 1][ok[lo:t + 1]]
            if len(rows) >= mp:
                C[t] = np.cov(rows, rowvar=False, ddof=1)
    return {"E": E, "EM": EM, "C120": C120, "C36": C36}


def sigma(mats, Q):
    """gm.vol.estimate's hybrid form for the return series of the vectors Q (T x 8, one per month) on the histories:
    fast = daily EWMA (else monthly EWMA), slow = 120 months, blend 0.7 / 0.3, floor 0.75 x slow, else 36 months."""
    def qf(Mx, s):
        v = np.einsum("ti,tij,tj->t", Q, np.nan_to_num(Mx), Q)
        ok = np.isfinite(Mx[:, 0, 0])
        return np.where(ok, np.sqrt(np.maximum(v, 0) * s), np.nan)
    fd, fm = qf(mats["E"], 252.0), qf(mats["EM"], 12.0)
    lt, m36 = qf(mats["C120"], 12.0), qf(mats["C36"], 12.0)
    fast = np.where(np.isfinite(fd), fd, fm)
    blend = np.where(np.isfinite(lt) & np.isfinite(fast), 0.7 * fast + 0.3 * lt, fast)
    out = np.where(np.isfinite(blend), np.maximum(blend, np.where(np.isfinite(lt), 0.75 * lt, 0.0)), np.nan)
    return np.where(np.isfinite(out), out, m36)


def col(root, key):
    """Score column name: 'ED|S2', 'FEI|K5' (flat strings: frames align by label)."""
    return "%s|%s%d" % (root, key[0], key[1])


def strip_valid(sp):
    """Destination validity per (root, key) and month: started, strip at d, normal exists, no stale contract."""
    out = {}
    grid = _grid(sp) if sp["roots"] else None
    for root, R in sp["roots"].items():
        g = R["grid"]
        st = np.array([R["start"] is not None and p >= R["start"] for p in g])
        for key in KEYS:
            out[col(root, key)] = pd.Series(st & R["full"] & np.isfinite(R["N"][key]) & ~R["stale"][key], index=g)
    return pd.DataFrame(out).reindex(grid).fillna(False).astype(bool) if out else pd.DataFrame()


def strip_scores(sp):
    """Entry 4f: sign(G) where |G| >= the gate, 0 where it fails, missing where not valid."""
    v = strip_valid(sp)
    out = {}
    for root, R in sp["roots"].items():
        for i, key in enumerate(KEYS):
            G = R["M"][key] - R["N"][key]
            s = np.where(np.abs(G) >= GATES[i], np.sign(G), 0.0)
            out[col(root, key)] = pd.Series(s, index=R["grid"]).reindex(v.index).where(v[col(root, key)])
    return pd.DataFrame(out, index=v.index), v


def _grid(sp):
    gs = [R["grid"] for R in sp["roots"].values()]
    return pd.period_range(min(g[0] for g in gs), LAST, freq="M")


def strip_positions(sp, sc, versions=("A", "B"), drop=()):
    """Entry 4g-4j: q per version and currency, sigma, x = 0.40 / sigma x q / n; pod = mean of versions."""
    grid = _grid(sp)
    roots = [r for r in sp["roots"] if r not in drop]
    avail = {}
    for root in roots:
        R = sp["roots"][root]
        a = pd.Series([R["start"] is not None and p >= R["start"] for p in R["grid"]], index=R["grid"]) & \
            pd.Series(R["full"], index=R["grid"])
        avail[root] = a.reindex(grid).fillna(False).astype(bool)
    n = sum(avail[r].astype(int) for r in roots) if roots else pd.Series(0, index=grid)
    cols = ["%s|%d" % (r, j) for r in roots for j in range(1, 9)]
    pv, qv, sg = {}, {}, {}
    for v in versions:
        keys = KEYS_A if v == "A" else KEYS_B
        ki = [KEYS.index(k) for k in keys]
        X = pd.DataFrame(np.nan, index=grid, columns=cols)
        for root in roots:
            R = sp["roots"][root]
            S = sc[[col(root, k) for k in keys]].reindex(R["grid"]).to_numpy(dtype=float)
            has = np.isfinite(S).any(axis=1)
            q = np.nan_to_num(S) @ W[ki]
            s = sigma(R["mats"], q)
            with np.errstate(divide="ignore", invalid="ignore"):
                x = np.where((s > 0)[:, None], 0.40 / s[:, None] * q, 0.0)
            nn = n.reindex(R["grid"]).to_numpy(dtype=float)
            with np.errstate(divide="ignore", invalid="ignore"):
                x = x / np.where(nn > 0, nn, np.nan)[:, None]
            ok = has & np.isfinite(s) & (nn > 0)
            x[~ok] = np.nan
            started = np.array([R["start"] is not None and p_ >= R["start"] for p_ in R["grid"]])
            x[started & ~ok] = 0.0          # 1.0.1 M1: a started currency without a position holds 0, not missing
            X.loc[R["grid"], ["%s|%d" % (root, j) for j in range(1, 9)]] = x
            qv[(v, root)] = pd.DataFrame(np.where(has[:, None], q, np.nan), index=R["grid"])
            sg[(v, root)] = pd.Series(s, index=R["grid"])
        pv[v] = X
    V = len(pv)
    have = sum(p.notna().astype(int) for p in pv.values()) > 0          # cell by cell (E7; B1 4k)
    pod = (sum(p.fillna(0) for p in pv.values()) / V).where(have)
    return pv, pod, qv, sg


def _slot_frames(sp, grid, cols, what):
    out = pd.DataFrame(np.nan, index=grid, columns=cols)
    for root, R in sp["roots"].items():
        c = [x for x in cols if x.startswith(root + "|")]
        if c:
            out.loc[R["grid"], c] = R[what]
    return out


def _cid(sp, grid, cols):
    """Contract id (delivery index) per slot column and decision month."""
    out = pd.DataFrame(np.nan, index=grid, columns=cols)
    for root, R in sp["roots"].items():
        c = [x for x in cols if x.startswith(root + "|")]
        if not c:
            continue
        a = np.full((len(R["grid"]), 8), np.nan)
        for i, st in enumerate(R["strip"]):
            if st is not None:
                a[i] = [_di(y, m) for (y, m) in st]
        out.loc[R["grid"], c] = a
    return out


def contract_trades(L, cid):
    """Entry 4m: per decision month sum over identified contracts of |x_c(t) - x_c(t-1)| (absent = 0)."""
    x = np.nan_to_num(L.to_numpy(dtype=float))
    c = cid.to_numpy(dtype=float)
    roots = sorted({col.split("|")[0] for col in L.columns})
    T = len(L)
    tr = np.zeros(T)
    for root in roots:
        ci = [i for i, col in enumerate(L.columns) if col.startswith(root + "|")]
        ids = c[:, ci]
        u = np.unique(ids[np.isfinite(ids)])
        if not len(u):
            continue
        A = np.zeros((T, len(u)))
        loc = {v: k for k, v in enumerate(u)}
        for t in range(T):
            for jj, i in enumerate(ci):
                cc = ids[t, jj]
                if cc == cc and x[t, i] != 0:
                    A[t, loc[cc]] += x[t, i]
        dA = np.abs(np.diff(np.vstack([np.zeros((1, len(u))), A]), axis=0))
        tr += dA.sum(axis=1)
    return pd.Series(tr, index=L.index)


def strip_run(sp, cost_mult=1.0, versions=("A", "B"), score_perm=None, drop=(), returns="RE", delay=0, sc=None):
    """The pod alone (entry 4j-4p). score_perm = {"start": first moved decision month, "perm": map}: the score arrays
    of every root and key moved jointly, then masked by the destination month's validity (T3)."""
    from gm import book as B
    from gm import seal as SL
    from gm import stats as ST
    if sc is None:
        sc, valid = strip_scores(sp)
    else:
        valid = strip_valid(sp)
    grid = _grid(sp)
    sc = sc.reindex(grid)
    valid = valid.reindex(grid).fillna(False).astype(bool)
    if score_perm is not None:
        sc = ST.move_rows(sc, score_perm["perm"], score_perm["start"]).where(valid)
    pv, p, qv, sg = strip_positions(sp, sc, versions, drop)
    cols = list(p.columns)
    RE = _slot_frames(sp, grid, cols, "RE")             # the traded returns: scalers always read these
    p1 = p.shift(1)
    rb = (p1 * RE).mask(p1 == 0, 0.0).sum(axis=1, min_count=1)      # 1.0.1 M1: a slot holding 0 earns 0
    k = (1.0 / (rb.rolling(BLOCK_MONTHS, min_periods=SCALER_MIN).std() * np.sqrt(12))).shift(1).clip(upper=BLOCK_CAP)
    total = p.mul(k, axis=0).fillna(0.0)
    blocks = rb * k
    active = blocks.notna()
    raw = (total.shift(1) * RE.fillna(0)).sum(axis=1).where(active)
    s = (BOOK_VOL / (raw.rolling(36, min_periods=SCALER_MIN).std() * np.sqrt(12))).shift(1)
    pos = p.mul(k, axis=0).mul(s, axis=0)               # missing where the pod holds no position in that contract slot
    legv = pd.DataFrame(np.nan, index=grid, columns=cols)
    for root, R in sp["roots"].items():
        c = [x for x in cols if x.startswith(root + "|")]
        if c:
            legv.loc[R["grid"], c] = R["legvol"].to_numpy()
    cap = (RISK_CAP * BOOK_VOL * 3) / legv
    groups = [{"members": [c for c in cols if c.startswith(r + "|")], "cap_from": None}
              for r in sorted({c.split("|")[0] for c in cols})]
    Lc = B.cap_positions(pos, cap, groups)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = Lc.abs().to_numpy() / pos.abs().to_numpy()
    bind = pd.DataFrame((ratio < 1 - 1e-12) & (pos.abs().to_numpy() > 0), index=grid, columns=cols)
    g = (Lc.abs() * GROSS_W).sum(axis=1)
    Lg = Lc.mul((GROSS_CAP / g).clip(upper=1), axis=0)
    if delay:
        RE = _slot_frames(sp, grid, cols, "RE2")       # notionals one month later (entry 4p)
    elif returns != "RE":
        RE = _slot_frames(sp, grid, cols, returns)     # falsifier 2: decision-day settlements, same positions
    lag = 1 + int(delay)
    Lp = Lg.shift(lag)
    gross = (Lp * RE).mask(Lp == 0, 0.0).sum(axis=1, min_count=1).where(active & s.notna())
    cid = _cid(sp, grid, cols)
    trade = contract_trades(Lg, cid)
    tc = trade * COST_NOTIONAL
    net = gross - cost_mult * tc.shift(lag)
    out = {"net": net, "gross": gross, "pos": Lg, "cost": tc, "turnover": trade, "rb": rb, "k": k, "s": s,
           "active": active, "p": p, "pv": pv, "q": qv, "sigma": sg, "scores": sc, "bind": bind, "cid": cid}
    return SL.check_output(out, SL.DESIGN, "b2_batch.strip_run")


def strip_window(net):
    from gm import stats as ST
    x = ST.cut(net, "1975-01", str(STRIP_DEC_LAST + 1))
    return x


def strip_r1_counts(sp):
    """Entry 9a: R1's counts (diag_preb.r1) from b2's own strip, normals, stale screen and next-day measures (ED)."""
    R = sp["roots"]["ED"]
    g = R["grid"]
    excl = {"no normal": 0, "strip missing on d": 0, "strip missing on d1": 0, "stale": 0}
    rows = []
    first_ok = None
    for i, p in enumerate(g):
        okK = all(np.isfinite(R["N"][k][i]) for k in KEYS_B)
        okS = all(np.isfinite(R["N"][k][i]) for k in KEYS_A)
        if first_ok is None and R["full"][i] and (okK or okS):
            first_ok = p
    win = [i for i, p in enumerate(g) if first_ok is not None and max(STRIP_START, first_ok) <= p <= DEC_LAST]
    first_normal = {}
    for i in win:
        for n in range(2, 8):
            key = ("K", n)
            if np.isfinite(R["N"][key][i]) and n not in first_normal:
                first_normal[n] = g[i]
    for i in win:
        for n in range(2, 8):
            key = ("K", n)
            if not np.isfinite(R["N"][key][i]):
                excl["no normal"] += 1
                continue
            if not R["full"][i]:
                excl["strip missing on d"] += 1
                continue
            if not R["full1"][i]:
                excl["strip missing on d1"] += 1
                continue
            if R["stale"][key][i]:
                excl["stale"] += 1
                continue
            g0 = R["M"][key][i] - R["N"][key][i]
            g1 = R["M1"][key][i] - R["N"][key][i]
            c = DP.r1_cost(n)
            rows.append((n, bool(abs(g0) > c and abs(g1) > c and np.sign(g0) == np.sign(g1))))
    elig = len(rows)
    qual = sum(1 for _, q in rows if q)
    return {"eligible": elig, "qualifying": qual, "by_n": {n: (sum(1 for m, q in rows if m == n and q),
                                                               sum(1 for m, _ in rows if m == n)) for n in range(2, 8)},
            "excluded": excl, "months": len(win), "start": g[win[0]] if win else None,
            "end": g[win[-1]] if win else None, "first_normal": first_normal}


def strip_identity(sp, r1):
    """Entry 9a: compare with diag_preb.r1's result dict -> list of differing fields."""
    mine = strip_r1_counts(sp)
    bad = []
    for k in ("eligible", "qualifying", "by_n", "excluded", "months", "start", "end", "first_normal"):
        if mine[k] != r1.get(k):
            bad.append(k)
    return bad, mine


# =====================================================================================================================
# card rule layers (entry item 5)
# =====================================================================================================================
def card_inputs_view(R, D, gspc, ci, fxv, tb3, eps, days=None):
    """Entry 5a: the inputs of every rule, cut at 2010-12-31; the card volatility; NYSE days; S&P month-ends."""
    from gm import execution as EX
    from gm import seal as SL
    Tz = SL.resolve(SL.DESIGN)
    R, D, gspc, fxv, tb3, eps = SL.cut_inputs(Tz, R, D, gspc, fxv, tb3, eps)
    days = EX.nyse_days(gspc=gspc) if days is None else days
    lv = gspc.dropna().copy()
    lv.index = pd.DatetimeIndex(lv.index).normalize()
    lv = lv[~lv.index.duplicated(keep="last")].sort_index()
    spx_me = lv.groupby(lv.index.to_period("M")).last()
    vol = DP.card_vol(R, D)
    R1, flags = EX.k1_returns(R, D, days)
    return {"R": R, "D": D, "gspc": gspc, "ci": ci, "fxv": fxv, "tb3": tb3, "eps": eps, "days": days,
            "spx_me": spx_me, "vol": vol, "R1": R1, "flags": flags, "idx": R.index}


def _unit(version, market, dirn, k=1.0, V=None, sizing="monthly", entry="E1", h=None, partner=None):
    return {"version": version, "market": market, "dir": dirn.fillna(0).astype(float), "k": float(k), "V": V,
            "sizing": sizing, "entry": entry, "h": h, "partner": partner}


def _held_int(b):
    return b.fillna(False).astype(bool).astype(float)


def card_rules(inp, plant=None):
    """Entry 5b-5e: {rule: dict(kind, units, versions, base, start)}; units carry the direction arrays (moved by T3).
    plant: None or 'vol_next' (the truncation control: next month's volatility in card 1 R1)."""
    R, ci, vol, idx = inp["R"], inp["ci"], inp["vol"], inp["idx"]
    if plant == "vol_next":
        vol = vol.shift(-1)
    g = lambda s: s.reindex(idx)  # noqa: E731
    rules = {}
    FF, GS2, GS10 = g(ci.m("FEDFUNDS")), g(ci.m("GS2")), g(ci.m("GS10"))
    s5 = g(DP.r4_state(ci, 5.0)).fillna(False).astype(bool)
    start2 = GS2.first_valid_index()
    # ---- card 1 R1 (diag_preb.card1_rules R1 per version) x E1 / E3
    GS5, BAA = g(ci.m("GS5")), g(ci.m("BAA"))
    WTI, TW, DB = g(ci.m("WTISPLC")), g(ci.m("TWEXMMTH")), g(ci.m("DTWEXBGS"))
    units, vers, base = [], [], []
    for L, rn, gate in [(L, r, gt) for L in (6, 12) for r in ("FEDFUNDS", "GS10") for gt in (False, True)]:
        rr = FF if rn == "FEDFUNDS" else GS10
        both_tw = TW.notna() & TW.shift(L).notna()
        dol = (TW > TW.shift(L)).where(both_tw, DB > DB.shift(L))
        cond = (WTI > WTI.shift(L)) & dol.fillna(False).astype(bool) & (rr > rr.shift(L))
        held = DP.tail(cond, 12) & (~s5 if gate else True)
        for e in ("E1", "E3"):
            v = "L%d/%s/gate %s/%s" % (L, rn, "on" if gate else "off", e)
            vers.append(v)
            if e == "E1":
                base.append(v)
            for mk in ("bd_us_2y", "bd_us_10y"):
                units.append(_unit(v, mk, _held_int(held), 2, vol.get(mk), "monthly", e))
    rules["card 1 R1"] = {"kind": "monthly", "units": units, "versions": vers, "base": base, "start": idx[idx >= pd.Period(
        "1975-01", "M")][0]}
    # ---- card 1 R2
    units, vers, base = [], [], []
    m2 = g(ci.fr_change("M2SL", 12)[0])
    sp = BAA - GS10
    wa = (GS5 - GS2 < 0).where(GS2.notna(), False).fillna(False).astype(bool)
    wb = (sp > sp.shift(6)).fillna(False)
    wc = (m2 < m2.shift(24)).fillna(False)
    nw = wa.astype(int) + wb.astype(int) + wc.astype(int)
    for T_, k_, gate in [(T_, k_, gt) for T_ in (6, 12) for k_ in (2, 3) for gt in (False, True)]:
        cond = (FF >= FF.shift(T_) + 0.25) & (nw >= k_)
        cond = cond & (idx >= start2)
        held = DP.tail(cond, 12) & (~s5 if gate else True) & (idx >= start2)
        for e in ("E1", "E3"):
            v = "T%d/k%d/gate %s/%s" % (T_, k_, "on" if gate else "off", e)
            vers.append(v)
            if e == "E1":
                base.append(v)
            for mk in ("bd_us_2y", "bd_us_10y"):
                units.append(_unit(v, mk, _held_int(pd.Series(held, index=idx)), 2, vol.get(mk), "monthly", e))
    rules["card 1 R2"] = {"kind": "monthly", "units": units, "versions": vers, "base": base, "start": start2}
    # ---- card 1 R5 (diag_preb.card1_r5 per version) x E1 / E3
    fxv = inp["fxv"].reindex(columns=list(DP.R5_CUR)).reindex(idx)
    mm = 100.0 * (fxv / fxv.shift(6) - 1)
    cnt = mm.notna().sum(axis=1)
    med = mm.median(axis=1, skipna=True)
    units, vers, base = [], [], []
    for G in (15, 10):
        t = mm.le(med - G, axis=0) & mm.notna()
        t = t.mul(cnt >= 3, axis=0).astype(bool)
        heldG = t.astype(float).rolling(13, min_periods=1).max() > 0
        for form in ("stocks", "stocks and bond"):
            k = 2 if form == "stocks and bond" else 1
            for e in ("E1", "E3"):
                v = "G%d/%s/%s" % (G, form, e)
                vers.append(v)
                if e == "E1":
                    base.append(v)
                for c in DP.R5_CUR:
                    eq, bd = DP.R5_LEGS[c]
                    if eq in vol:
                        units.append(_unit(v, eq, _held_int(heldG[c]), k, vol.get(eq), "monthly", e))
                    if form == "stocks and bond" and bd in vol:
                        units.append(_unit(v, bd, _held_int(heldG[c]), k, vol.get(bd), "monthly", e))
    rules["card 1 R5"] = {"kind": "monthly", "units": units, "versions": vers, "base": base,
                          "start": idx[idx >= pd.Period("1975-01", "M")][0]}
    # ---- card 2 R1, R2 (diag_preb.card2_rules; kept versions of C2-D2)
    v2 = DP.card2_rules(ci, R, vol, inp["spx_me"])
    r45 = DP.r4_state(ci, 4.5).reindex(idx)
    keep = {}
    for name, mk in (("card 2 R1", "bd_us_10y"), ("card 2 R2", "eq_us_spx")):
        kp = DP.c2d2(v2[name], r45)
        keep[name] = sorted([v for v in kp if kp[v]["keep"]], key=str)
        units, vers = [], []
        for v in C2_KEPT[name]:
            if v not in v2[name]:
                continue
            vn = "/".join(str(z) for z in v)
            vers.append(vn)
            units.append(_unit(vn, mk, -_held_int(v2[name][v][1].reindex(idx)), 1, vol.get(mk), "monthly", "E1"))
        rules[name] = {"kind": "monthly", "units": units, "versions": vers, "base": list(vers),
                       "start": idx[idx >= pd.Period("1975-01", "M")][0], "c2d2_keep": keep[name],
                       "on": {"/".join(str(z) for z in v): v2[name][v][0].reindex(idx).fillna(False) for v in C2_KEPT[name]}}
    # ---- card 3 R2 (diag_preb.card3_rules R2) and card 4 R5 (diag_preb.card4_r5): fixed-size pairs
    vpair, h = DP.pair_vol(R, GS2, GS10)
    vpair, h = vpair.reindex(idx), h.reindex(idx)
    S = GS10 - GS2
    Smean = S.dropna().expanding(min_periods=120).mean().reindex(idx)
    vps = np.maximum(vpair, vpair.expanding(min_periods=1).median()).where(vpair.notna())
    units, vers = [], []
    ons = {}
    for b, sz in [(b, sz) for b in ("1.0", "mean") for sz in (False, True)]:
        on = ((S < 1.0) if b == "1.0" else (S < Smean)).fillna(False)
        vn = "bar %s/sizing %s" % (b, "on" if sz else "off")
        vers.append(vn)
        ons[vn] = on
        units.append(_unit(vn, "bd_us_2y", _held_int(on), 1, vps if sz else vpair, "fixed", "E1", h=h,
                           partner="bd_us_10y"))
    rules["card 3 R2"] = {"kind": "monthly", "units": units, "versions": vers, "base": list(vers), "start": start2,
                          "on": ons}
    aux = {"vpair": vpair, "h": h, "S": S, "Smean": Smean}
    v45, st45 = DP.card4_r5(ci, R, aux)
    units, vers, ons = [], [], {}
    for v in (1, 2):
        on = v45[v][0].reindex(idx).fillna(False)
        vn = "version %d" % v
        vers.append(vn)
        ons[vn] = on
        units.append(_unit(vn, "bd_us_2y", _held_int(on), 1, vpair, "fixed", "E1", h=h, partner="bd_us_10y"))
    rules["card 4 R5"] = {"kind": "monthly", "units": units, "versions": vers, "base": list(vers), "start": st45,
                          "on": ons}
    # ---- card 3 R4 (diag_preb.card3_r4 per version), fixed size
    vs_ = vol["eq_us_spx"]
    eps, spx_me, tb3 = inp["eps"].reindex(idx), inp["spx_me"].reindex(idx), inp["tb3"].reindex(idx)
    E = 100.0 * eps / spx_me
    vsz = np.maximum(vs_, vs_.expanding(min_periods=1).median()).where(vs_.notna())
    units, vers, ons = [], [], {}
    for B_ in (1.0, 0.0):
        o = ((E - tb3) < B_) & E.notna() & tb3.notna()
        for sz in (False, True):
            vn = "B %.1f/sizing %s" % (B_, "on" if sz else "off")
            vers.append(vn)
            ons[vn] = o
            units.append(_unit(vn, "eq_us_spx", -_held_int(o), 1, vsz if sz else vs_, "fixed", "E1"))
    rules["card 3 R4"] = {"kind": "monthly", "units": units, "versions": vers, "base": list(vers),
                          "start": inp["eps"].dropna().index[0] if inp["eps"].notna().any() else None, "on": ons,
                          "E": E}
    # ---- card 4 R1, R3 (daily windows)
    W4 = card4_windows(inp["gspc"], inp["days"])
    for name in ("card 4 R1", "card 4 R3"):
        rules[name] = {"kind": "daily", "windows": W4[name], "versions": W4["versions"][name],
                       "base": list(W4["versions"][name]), "start": pd.Period("1975-01", "M"), "E": W4["E"],
                       "lv": W4["lv"], "vol": vol["eq_us_spx"]}
    return rules


# ---------------------------------------------------------------------------------------------- monthly positions
def e3_factor(d, r):
    """Entry 5c: 1/3 at the run's first month, full from the first month s of the run at which
    prod_{t0+1..s}(1 + r) - 1 times the direction is above zero; 0 off the run."""
    dv = d.to_numpy(dtype=float)
    rv = np.nan_to_num(r.reindex(d.index).to_numpy(dtype=float))
    f = np.zeros(len(dv))
    i = 0
    T = len(dv)
    while i < T:
        if dv[i] == 0:
            i += 1
            continue
        j = i
        while j + 1 < T and dv[j + 1] == dv[i]:
            j += 1
        f[i:j + 1] = 1.0 / 3.0
        cum = 1.0
        for s in range(i + 1, j + 1):
            cum *= (1.0 + rv[s])
            if (cum - 1.0) * dv[i] > 0:
                f[s:j + 1] = 1.0
                break
        i = j + 1
    return pd.Series(f, index=d.index)


def fixed_pair(dirn, V, h):
    """Entry 5d: notional a = 0.40 / V and hedge ratio h fixed at the first month of an on-run (same direction); a
    zero direction or a missing V / h ends the run (diag_preb fixed_runs semantics)."""
    a = np.zeros(len(dirn))
    hh = np.zeros(len(dirn))
    cur, va, vh = 0, 0.0, 0.0
    dv, Vv, hv = dirn.to_numpy(dtype=float), V.to_numpy(dtype=float), h.to_numpy(dtype=float)
    for t in range(len(dv)):
        d = int(dv[t]) if dv[t] == dv[t] else 0
        if d == 0 or not np.isfinite(Vv[t]) or not np.isfinite(hv[t]):
            cur, va, vh = 0, 0.0, 0.0
            continue
        if d != cur:
            cur, va, vh = d, d * 0.40 / Vv[t], hv[t]
        a[t], hh[t] = va, vh
    return pd.Series(a, index=dirn.index), pd.Series(hh, index=dirn.index)


def unit_positions(u, dirn, R, mode="full"):
    """One unit's positions {market: Series} at rule units (0.40 / vol); mode 'base' = without E3 and fixed size."""
    idx = dirn.index
    V = u["V"].reindex(idx) if u["V"] is not None else None
    if V is None:
        return {}
    if u["partner"] is None:
        if u["sizing"] == "fixed" and mode == "full":
            p = DP.fixed_runs(dirn, (0.40 / V / u["k"]).where(V.notna()))
        else:
            p = (dirn * 0.40 / V / u["k"]).where(V.notna() & (dirn != 0), 0.0).fillna(0.0)
        if u["entry"] == "E3" and mode == "full":
            p = p * e3_factor(dirn, R[u["market"]] if u["market"] in R else pd.Series(0.0, index=idx))
        return {u["market"]: p}
    h = u["h"].reindex(idx)
    if u["sizing"] == "fixed" and mode == "full":
        a, hh = fixed_pair(dirn, V, h)
        return {u["market"]: a, u["partner"]: -a * hh}
    p2 = (dirn * 0.40 / V).where(V.notna() & (dirn != 0), 0.0).fillna(0.0)
    return {u["market"]: p2, u["partner"]: (-p2 * h).fillna(0.0)}


def rule_positions(rule, inp, dirs=None, mode="full", versions=None, drop=()):
    """Entry 5e: rule position = mean over versions (an off version counts 0). dirs: {unit index: direction Series}
    (the placebo's moved arrays); versions: subset (version alone); drop: markets removed (fragility)."""
    R, idx = inp["R"], inp["idx"]
    vs = versions if versions is not None else (rule["base"] if mode == "base" else rule["versions"])
    acc = {}
    for i, u in enumerate(rule["units"]):
        if u["version"] not in vs:
            continue
        d = dirs[i] if dirs is not None else u["dir"]
        for mk, p in unit_positions(u, d.reindex(idx).fillna(0.0), R, mode).items():
            if mk in drop:
                continue
            acc[mk] = acc.get(mk, 0.0) + p.reindex(idx).fillna(0.0)
    pos = pd.DataFrame(acc, index=idx) if acc else pd.DataFrame(index=idx)
    return pos / len(vs)


def costs(pos, cost_mult=1.0):
    """Entry 5h (book.run conventions): cost(t) = sum |delta pos| x one-way + |pos| x one-way x 2 x rolls / 12."""
    from gm import book as B
    one = pd.Series({k: B.cost_bp(k)[0] / 1e4 for k in pos.columns})
    rolls = pd.Series({k: B.cost_bp(k)[1] for k in pos.columns})
    trade = pos.diff().abs()
    tc = (trade * one).sum(axis=1) + (pos.abs() * one * 2 * rolls / 12).sum(axis=1)
    return tc, trade.sum(axis=1)


def monthly_returns(pos, RE, cost_mult=1.0, lag=1):
    """Entry 5f-5h: test return = HELD x (sum pos(t-lag) x RE(t) - c x cost(t-lag)); a market without a return
    contributes 0."""
    P = pos.shift(lag)
    RE = RE.reindex(index=pos.index, columns=pos.columns)
    gross = (P * RE).fillna(0.0).sum(axis=1)
    miss = int(((P.fillna(0) != 0) & RE.isna()).to_numpy().sum())
    tc, turn = costs(pos)
    net = gross - cost_mult * tc.shift(lag).fillna(0.0)
    return HELD * net, HELD * gross, miss, HELD * turn


def window_of(rule, series):
    """Entry 5i: return months from the rule's first decision month + 1 (card 4 R1, R3: 1975-01) to 2010-12."""
    s0 = rule["start"]
    if s0 is None:
        return series.iloc[0:0]
    a = s0 if rule["kind"] == "daily" else s0 + 1
    return series.loc[(series.index >= a) & (series.index <= LAST)]


def rule_run(rule, inp, cost_mult=1.0, dirs=None, versions=None, drop=(), timing="k1", windows=None, mode="full"):
    """A rule's net test return (entry 5f-5i). timing 'k1' (decisive), 'k0' (panel), 'delay' (book.py delay 1 on k0)."""
    if rule["kind"] == "daily":
        return card4_run(rule, inp, cost_mult, versions=versions, windows=windows)
    pos = rule_positions(rule, inp, dirs, mode, versions, drop)
    if timing == "k1":
        RE, lag = inp["R1"], 1
    elif timing == "k0":
        RE, lag = inp["R"], 1
    else:
        RE, lag = inp["R"], 2
    net, gross, miss, turn = monthly_returns(pos, RE, cost_mult, lag)
    held = pos.ne(0).any(axis=1)
    return {"net": window_of(rule, net), "gross": window_of(rule, gross), "pos": pos, "miss": miss,
            "turnover": turn, "held": held, "net_all": net}


# ---------------------------------------------------------------------------------------------- card 4 R1, R3
def card4_windows(gspc, days):
    """Entry 5b: the windows of card 4 R1 and R3 (diag_preb.card4_days's dates and gates), with their gate refs."""
    E = DP._ext_days(days)
    posd = {d: i for i, d in enumerate(E)}
    lv = gspc.dropna().copy()
    lv.index = pd.DatetimeIndex(lv.index).normalize()
    lv = lv[~lv.index.duplicated(keep="last")]
    lv = lv[lv.index <= SEAL]

    def close(d):
        return float(lv.get(d, np.nan)) if d is not None else np.nan

    def prev(d, k=1):
        i = posd[d] - k
        return E[i] if i >= 0 else None
    out = {"card 4 R1": [], "card 4 R3": [], "E": E, "lv": lv,
           "versions": {"card 4 R1": ["%s/form %s" % (e, f) for e in ("oct", "dec") for f in ("A", "B", "C")],
                        "card 4 R3": ["window 1", "window 2"]}}
    for ent in ("oct", "dec"):
        for Y in range(1974, 2011):
            en = DP._on_before(E, "%d-10-31" % Y) if ent == "oct" else DP._on_before(E, "%d-12-15" % Y)
            ex = DP._on_before(E, "%d-01-15" % (Y + 1))
            bar = close(DP._on_before(E, "%d-12-31" % (Y - 1)))
            c = close(prev(en))
            dirs = {}
            for form in ("A", "B", "C"):
                if form == "A":
                    v = 1
                elif form == "B":
                    v = 1 if c > bar else 0
                else:
                    v = 1 if c > bar else (-1 if c < bar else 0)
                dirs["%s/form %s" % (ent, form)] = v
            out["card 4 R1"].append({"entry": en, "exit": ex, "ref": bar, "kind": "R1", "dirs": dirs, "year": Y,
                                     "ent": ent})
    for w in (1, 2):
        for Y in range(1975, 2011):
            octc = close(DP._on_before(E, "%d-10-31" % (Y - 1)))
            if w == 1:
                en = DP._on_before(E, "%d-01-15" % Y)
                ex = E[min(posd[en] + 10, len(E) - 1)]
            else:
                en = DP._on_before(E, DP._third_friday(Y, 2))
                xm = DP._on_before(E, DP._third_friday(Y, 3))
                ex = E[posd[xm] + 1]
            c = close(prev(en))
            out["card 4 R3"].append({"entry": en, "exit": ex, "ref": octc, "kind": "R3", "year": Y,
                                     "dirs": {"window %d" % w: -1 if c > octc else 0}})
    return out


def _regate(w, entry, E, lv):
    """T3: re-read a window's gates at a new entry day (entry 6, card 4)."""
    i = int(E.searchsorted(entry))
    pr = E[i - 1] if i - 1 >= 0 else None
    c = float(lv.get(pr, np.nan)) if pr is not None else np.nan
    bar = w["ref"]
    if w["kind"] == "R1":
        out = {}
        for vn in w["dirs"]:
            f = vn[-1]
            out[vn] = 1 if f == "A" else ((1 if c > bar else 0) if f == "B" else (1 if c > bar else (-1 if c < bar
                                                                                                    else 0)))
        return out
    return {vn: (-1 if c > bar else 0) for vn in w["dirs"]}


def card4_daily(rule, versions=None, windows=None):
    """Daily positions (rule units, averaged over versions) on NYSE days <= 2010-12-31 and the direction sum per day.
    windows: [(window dict, entry, exit, dirs)] (placebo) or None (the rule's own)."""
    E, vol = rule["E"], rule["vol"]
    days = E[E <= SEAL]
    if "posd" not in rule:
        rule["posd"] = {d: i for i, d in enumerate(E)}
    pos = rule["posd"]
    vs = versions if versions is not None else rule["versions"]
    P = np.zeros(len(days))
    dsum = np.zeros(len(E), dtype=np.int64)
    items = windows if windows is not None else [(w, w["entry"], w["exit"], w["dirs"]) for w in rule["windows"]]
    for w, en, ex, dirs in items:
        if en is None or ex is None:
            continue
        a, b = pos[en] + 1, pos[ex]
        if b < a:
            continue
        first = E[a]
        vm = vol.get(pd.Period(first, "M") - 1, np.nan) if hasattr(vol, "get") else np.nan
        for vn in vs:
            d_ = dirs.get(vn, 0)
            if not d_:
                continue
            dsum[a:b + 1] += d_
            if vm == vm:
                bb = min(b, len(days) - 1)
                if a <= bb:
                    P[a:bb + 1] += d_ * 0.40 / vm
    return pd.Series(P / len(vs), index=days), pd.Series(dsum, index=E)


def card4_run(rule, inp, cost_mult=1.0, versions=None, windows=None):
    """Entry 5f-5h for card 4 R1, R3: month return = sum over days of position x e(d); one-way cost at each entry and
    exit close, roll pro rata per held day; x HELD."""
    from gm import book as B
    from gm import execution as EX
    P, _ = card4_daily(rule, versions, windows)
    if "e" not in inp:
        inp["e"] = EX.spx_daily_excess(inp["R"], inp["gspc"])
    e = inp["e"].reindex(P.index)
    ow, rolls = B.cost_bp("eq_us_spx")
    ow /= 1e4
    nxt = P.shift(-1).fillna(0.0)
    trade = (nxt - P).abs()
    trade.iloc[0] = trade.iloc[0] + abs(P.iloc[0])
    m = P.index.to_period("M")
    N = pd.Series(1, index=P.index).groupby(m).transform("sum")
    roll = P.abs() * ow * 2 * rolls / 12.0 / N
    gross_d = (P * e).fillna(0.0)
    cost_d = trade * ow + roll
    gross = gross_d.groupby(m).sum()
    cost = cost_d.groupby(m).sum()
    net = gross - cost_mult * cost
    grid = pd.period_range("1974-01", LAST, freq="M")
    net = net.reindex(grid).fillna(0.0)
    gross = gross.reindex(grid).fillna(0.0)
    held = P.ne(0).groupby(m).any().reindex(grid).fillna(False)
    mpos = P.groupby(m).mean().reindex(grid).fillna(0.0)
    return {"net": window_of(rule, HELD * net), "gross": window_of(rule, HELD * gross),
            "pos": mpos.to_frame("eq_us_spx"), "daily": P, "miss": 0, "turnover": HELD * trade.groupby(m).sum(),
            "held": held, "net_all": HELD * net}


def moved_windows(rule, rng):
    """T3 for card 4 R1, R3 (entry 6): one random start per distinct window in the same calendar year as its entry,
    length in NYSE days kept, cut at the last NYSE day of 2010; the gates re-read at the new dates."""
    from gm import stats as ST
    E, lv = rule["E"], rule["lv"]
    days = E[E <= SEAL]
    if "posd" not in rule:
        rule["posd"] = {d: i for i, d in enumerate(E)}
    pos = rule["posd"]
    ws = sorted(rule["windows"], key=lambda w: (w["entry"], w["exit"]))
    moved = ST.move_windows([(w["entry"], pos[w["exit"]] - pos[w["entry"]]) for w in ws], days, "year", rng,
                            horizon=SEAL)
    return [(w, ne, nx, _regate(w, ne, E, lv)) for w, (ne, nx) in zip(ws, moved)]


# ---------------------------------------------------------------------------------------------- placebo, tests
def alpha_zero(x):
    from gm import stats as ST
    x = x.dropna()
    return ST.alpha_boot(x, pd.Series(0.0, index=x.index), n=NBOOT, block=6, seed=SEED)


def alpha_lb(x):
    from gm import stats as ST
    v = x.dropna().to_numpy(dtype=float)
    if len(v) < 24:
        return float("nan")
    idx = ST._stationary_idx(len(v), NBOOT, 6, SEED)
    a = float(v.mean())
    ab = v[idx].mean(axis=1)
    return float(a - np.percentile(ab - a, 95))


def rule_placebo(rule, inp, win, n=NPLACEBO, seed=SEED):
    """T3 (entry 6). Monthly rules: every unit's direction array of the decision months whose holdings earn the window
    moved jointly; card 4 R1, R3: moved windows. -> dict(sr, p, pass, n)."""
    from gm import stats as ST
    sr0 = ST.sharpe(win)
    srs = []
    if rule["kind"] == "daily":
        rng = np.random.default_rng(seed)
        for _ in range(n):
            ws = moved_windows(rule, rng)
            x = card4_run(rule, inp, windows=ws)["net"].reindex(win.index)
            srs.append(ST.sharpe(x))
    else:
        a = win.index[0] - 1
        T = len(win)
        D = pd.DataFrame({i: u["dir"].reindex(inp["idx"]).fillna(0.0) for i, u in enumerate(rule["units"])})
        for pm in ST.placebo_perms(T, n, 12, seed):
            Dm = ST.move_rows(D, pm, str(a))
            x = rule_run(rule, inp, dirs={i: Dm[i] for i in D.columns})["net"].reindex(win.index)
            srs.append(ST.sharpe(x))
    return {"sr": sr0, **ST.placebo_p(sr0, srs)}


def strip_placebo(sp, win, n=NPLACEBO, seed=SEED, sc=None):
    """T3 for Strip reversion (entry 6): score arrays moved, masked by destination validity, re-sized."""
    from gm import stats as ST
    if sc is None:
        sc, _ = strip_scores(sp)
    grid = _grid(sp)
    sc = sc.reindex(grid)
    a = win.index[0] - 1
    T = (win.index[-1] - win.index[0]).n + 1        # 1.0.1 M1: the window's span (= len(win) once contiguous)
    sr0 = ST.sharpe(win)
    srs = []
    for pm in ST.placebo_perms(T, n, 12, seed):
        x = strip_run(sp, score_perm={"start": str(a), "perm": pm}, sc=sc)["net"].reindex(win.index)
        srs.append(ST.sharpe(x))
    return {"sr": sr0, **ST.placebo_p(sr0, srs), "window": (str(win.index[0]), str(win.index[-1]))}


def f0_b2(rule, res):
    """Entry 6 F0 on the B2 positions: held decision months start..2010-11 (card 4 R1, R3: held months 1975-2010)."""
    held = res["held"]
    if rule["kind"] == "daily":
        months = [p for p, v in held.items() if v and pd.Period("1975-01", "M") <= p <= LAST]
    else:
        months = [p for p, v in held.items() if v and rule["start"] <= p <= DEC_LAST]
    return DP.f0(months, ""), months


# =====================================================================================================================
# identity with diag_preb (entry item 9)
# =====================================================================================================================
def _close(a, b):
    cols = sorted(set(a.columns) | set(b.columns))
    x = a.reindex(columns=cols).fillna(0.0).to_numpy(dtype=float)
    y = b.reindex(index=a.index, columns=cols).fillna(0.0).to_numpy(dtype=float)
    return float(np.max(np.abs(x - y) / np.maximum(1.0, np.abs(x)))) if x.size else 0.0


def identity(inp, rules, rates):
    """Entry 9b-9c: -> {rule: (ok, detail)}."""
    R, ci, vol, idx = inp["R"], inp["ci"], inp["vol"], inp["idx"]
    out = {}
    r1 = DP.card1_rules(ci, R, vol, inp["spx_me"])
    r5 = DP.card1_r5(inp["fxv"], vol)
    ref = {"card 1 R1": r1["card 1 R1"]["pos"], "card 1 R2": r1["card 1 R2"]["pos"],
           "card 1 R5": pd.concat([r5["legs"]["stock"], r5["legs"]["bond"]], axis=1)}
    v2 = DP.card2_rules(ci, R, vol, inp["spx_me"])
    r45 = DP.r4_state(ci, 4.5).reindex(idx)
    for name, mk in (("card 2 R1", "bd_us_10y"), ("card 2 R2", "eq_us_spx")):
        kp = DP.c2d2(v2[name], r45)
        ref[name] = DP.card2_rule(v2[name], kp, mk, -1, vol, idx)["pos"]
    rules3, _d32, aux = DP.card3_rules(ci, R, vol, rates)
    ref["card 3 R2"] = rules3["card 3 R2"]["pos"]
    ref["card 3 R4"] = DP.card3_r4(inp["eps"], inp["spx_me"], inp["tb3"], vol["eq_us_spx"])["pos"].to_frame("eq_us_spx")
    v45, _st = DP.card4_r5(ci, R, aux)
    ref["card 4 R5"] = (v45[1][1] + v45[2][1]) / 2
    c4 = DP.card4_days(inp["gspc"], inp["days"], vol["eq_us_spx"])
    for name in RULES:
        ru = rules[name]
        det = []
        if ru["kind"] == "daily":
            _P, ds = card4_daily(ru, ru["base"])
            want = c4[name]["sum"]
            mine = ds.reindex(want.index).fillna(0).astype("int64")
            ok1 = bool((mine.to_numpy() == want.to_numpy()).all())
            res = card4_run(ru, inp)
            f, months = f0_b2(ru, res)
            ok2 = sorted(months) == sorted(c4[name]["months"])
            det.append("direction sums per day %s" % ("equal" if ok1 else "DIFFER"))
            det.append("held months %d vs %d %s" % (len(months), len(c4[name]["months"]), "equal" if ok2 else "DIFFER"))
            out[name] = (ok1 and ok2, "; ".join(det))
            continue
        base = rule_positions(ru, inp, mode="base")
        full = rule_positions(ru, inp, mode="full")
        rf = ref[name].reindex(idx)
        d = _close(base, rf)
        ok1 = d <= 1e-12
        sb = np.sign(base.reindex(columns=sorted(base.columns)).fillna(0.0))
        sf = np.sign(full.reindex(columns=sorted(base.columns)).fillna(0.0))
        ok2 = bool((sb.to_numpy() == sf.to_numpy()).all())
        det.append("base vs diag_preb max rel diff %.1e" % d)
        det.append("full positions same signs and held months as the base layer: %s" % ("yes" if ok2 else "NO"))
        if name in C2_KEPT:
            ok3 = ru["c2d2_keep"] == sorted(C2_KEPT[name], key=str)
            det.append("C2-D2 keeps %s" % ("the registered versions" if ok3 else "OTHER versions"))
        else:
            ok3 = True
        out[name] = (ok1 and ok2 and ok3, "; ".join(det))
    return out


# =====================================================================================================================
# truncation (entry item 10)
# =====================================================================================================================
class CutInputs:
    """card_inputs.Inputs with every raw observation dated after T removed (same lock id, fresh cache)."""

    def __init__(self, ci, T):
        import card_inputs as CIN
        self._ci = CIN.Inputs.__new__(CIN.Inputs)
        self._ci.lock_id = ci.lock_id
        self._ci._raw = {k: v[v.index <= pd.Timestamp(T)] for k, v in ci._raw.items()}
        self._ci._cache = {}
        self.lock_id = ci.lock_id

    def __getattr__(self, k):
        return getattr(self._ci, k)


def _cut_contracts(contracts, T):
    return {r: {k: s[s.index <= pd.Timestamp(T)] for k, s in c.items()} for r, c in contracts.items()}


def _cut(x, T):
    if x is None:
        return None
    if isinstance(x.index, pd.PeriodIndex):
        return x.loc[x.index <= pd.Period(T, "M")]
    return x.loc[x.index <= pd.Timestamp(T)]


def strip_stages(sp, res):
    out = {}
    for root, R in sp["roots"].items():
        g = R["grid"]
        for k in KEYS:
            out["%s %s%d measure" % (root, k[0], k[1])] = pd.Series(R["M"][k], index=g)
            out["%s %s%d normal" % (root, k[0], k[1])] = pd.Series(R["N"][k], index=g)
            out["%s %s%d stale" % (root, k[0], k[1])] = pd.Series(R["stale"][k].astype(float), index=g)
        out["%s full" % root] = pd.Series(R["full"].astype(float), index=g)
        out["%s legvol" % root] = R["legvol"]
        out["%s returns T-1" % root] = pd.DataFrame(R["RE"], index=g)
    out["scores"] = res["scores"]
    for v, p in res["pv"].items():
        out["position %s" % v] = p
    for (v, root), s in res["sigma"].items():
        out["sigma %s %s" % (v, root)] = s
    for k in ("p", "pos", "cost"):
        out[k] = res[k]
    out["k T-1"] = res["k"]
    out["s T-1"] = res["s"]
    out["gross T-1"] = res["gross"]
    out["net T-1"] = res["net"]
    return out


def rule_stages(rules, inp):
    out = {}
    for name in RULES:
        ru = rules[name]
        r = rule_run(ru, inp)
        if ru["kind"] == "monthly":
            for i, u in enumerate(ru["units"]):
                out["%s unit %d dir" % (name, i)] = u["dir"]
            out["%s pos" % name] = r["pos"]
            out["%s net T-1" % name] = r["net_all"]
        else:
            out["%s daily pos" % name] = r["daily"]
            out["%s net T-1" % name] = r["net_all"]
    out["vol"] = inp["vol"]
    out["k1 returns T-1"] = inp["R1"]
    return out


def truncation(build, dates, out=print, label="B2 TRUNC"):
    """Entry 10: build(T or None) -> {stage: frame}; compare months / days <= T ('T-1' stages <= T - 1 month)."""
    full = build(None)
    res, ok = {}, True
    for T in dates:
        cs = build(T)
        bad = []
        Tp = pd.Period(T, "M")
        for k in sorted(set(full) | set(cs)):
            one = full.get(k, cs.get(k))
            lim = Tp - 1 if k.endswith("T-1") else Tp
            if not isinstance(one.index, pd.PeriodIndex):
                lim = pd.Timestamp(T) if not k.endswith("T-1") else (Tp - 1).end_time.normalize()
            if k not in full or k not in cs:          # a stage present in one run only: values <= T must not exist
                x = _cut(one, lim)
                if x.notna().to_numpy().any():
                    bad.append((k, -1))
                continue
            a, b = full[k], cs[k]
            n = _diff(a, b, lim)
            if n:
                bad.append((k, n))
        res[T] = (bad, len(full))
        ok = ok and not bad
        out("%s %s | stages %d | differing: %s | %s" % (label, T, len(full), ", ".join(
            "%s %d" % b for b in bad[:6]) or "none", "PASS" if not bad else "FAIL"))
    return ok, res


def build_cut(T, R, D, gspc, ci, fxv, tb3, eps, contracts, plant=None):
    """One truncated rebuild of every B2 path (entry 10): inputs dated after T removed."""
    from gm import execution as EX
    if T is not None:
        R, D, gspc, fxv, tb3, eps = (_cut(x, T) for x in (R, D, gspc, fxv, tb3, eps))
        ci = CutInputs(ci, T)
        contracts = _cut_contracts(contracts, T)
    days = EX.nyse_days(gspc=gspc)
    inp = card_inputs_view(R, D, gspc, ci, fxv, tb3, eps, days)
    rules = card_rules(inp, plant=plant if plant == "vol_next" else None)
    st = rule_stages(rules, inp)
    sp = strip_prepare(contracts, days, plant=plant if plant == "normal_next" else None)
    if sp["roots"]:                                     # no strip contract before the cut: no Strip stage exists
        st.update(strip_stages(sp, strip_run(sp)))
    return st


# =====================================================================================================================
# falsifiers, netting, fragility (entry items 7-8)
# =====================================================================================================================
def episodes_of(months):
    m = sorted(int(p.ordinal) for p in months)
    if not m:
        return []
    eps, cur = [], [m[0]]
    for a, b in zip(m[:-1], m[1:]):
        if b - a >= 12:
            eps.append(cur)
            cur = [b]
        else:
            cur.append(b)
    eps.append(cur)
    return [[pd.Period(ordinal=x, freq="M") for x in e] for e in eps]


def fragility(net, win, rerun=None, markets=()):
    x = net.reindex(win.index)
    base = float(x.mean() * 12)
    yrs = sorted({p.year for p in x.index})
    by_year = {y: float(x[[p.year != y for p in x.index]].mean() * 12) for y in yrs}
    prof = x.groupby([p.year for p in x.index]).sum()
    tot = float(x.sum())
    top = (prof.idxmax(), float(prof.max() / tot)) if tot > 0 and len(prof) else (None, float("nan"))
    wy = min(by_year, key=lambda y: by_year[y] - base) if by_year else None
    out = {"base": base, "year": (wy, by_year.get(wy, np.nan) - base), "top_year": top,
           "flag": bool(top[1] == top[1] and top[1] > 0.40), "market": (None, float("nan"))}
    if rerun is not None and len(markets) > 1:
        bm = {}
        for m in markets:
            r = rerun(m).reindex(win.index)
            bm[m] = float(r.mean() * 12) if r.notna().any() else float("nan")
        wm = min(bm, key=lambda m: (bm[m] if bm[m] == bm[m] else np.inf) - base)
        out["market"] = (wm, bm[wm] - base)
    return out


def netting(items, labels, out):
    """Entry 8: per market, months with a non-zero net, share of the 431 decision months, share long, months with
    opposite-sign rules, ratio of mean |net| to mean sum of |rule positions|. items {rule: monthly position frame}."""
    dm = pd.period_range("1975-01", DEC_LAST, freq="M")
    mk = sorted({c for p in items.values() for c in p.columns})
    if not items:
        out("NETTING | %s | no rule in it" % labels)
        return {}
    res = {}
    for m in mk:
        cols = [HELD * p[m].reindex(dm).fillna(0.0) for p in items.values() if m in p.columns]
        X = pd.concat(cols, axis=1)
        net = X.sum(axis=1)
        gross = X.abs().sum(axis=1)
        nz = net[net.abs() > 0]
        opp = int(((X > 0).any(axis=1) & (X < 0).any(axis=1)).sum())
        ratio = float(net.abs().mean() / gross.mean()) if gross.mean() > 0 else float("nan")
        res[m] = {"months": len(nz), "share": len(nz) / len(dm), "long": float((nz > 0).mean()) if len(nz) else np.nan,
                  "opposite": opp, "ratio": ratio}
        out("NETTING | %s | %s | net non-zero months %d | share of %d decision months %s | long share %s | months with "
            "opposite rules %d | mean |net| / mean sum |rule| %s" % (
                labels, m, len(nz), len(dm), cell(len(nz) / len(dm), len(dm), "%.3f"),
                cell(res[m]["long"], len(nz), "%.3f"), opp, cell(ratio, len(dm), "%.3f")))
    return res


# =====================================================================================================================
# the registered report (entry items 6-8, 11)
# =====================================================================================================================
def _stat_line(lab, x, out):
    from gm import stats as ST
    s = {"n": len(x), "sr": ST.sharpe(x), "mean": float(x.mean() * 12) if len(x) else np.nan,
         "vol": float(x.std() * np.sqrt(12)) if len(x) > 1 else np.nan, "maxdd": ST.maxdd(x),
         "skew": float(x.skew()) if len(x) > 2 else np.nan, "lo": ST.lo_sharpe(x)}
    out("%s | months %d | Sharpe %s | mean %s %%/yr | achieved vol %s %%/yr | max drawdown %s %% | skew %s | "
        "Lo-adjusted Sharpe %s" % (lab, s["n"], cell(s["sr"], s["n"]), cell(s["mean"] * 100, s["n"]),
                                   cell(s["vol"] * 100, s["n"]), cell(s["maxdd"] * 100, s["n"], "%.1f"),
                                   cell(s["skew"], s["n"]), cell(s["lo"], s["n"])))
    return s


def _eras(x, out, lab, strip=False):
    from gm import stats as ST
    parts = []
    for e, a, b in ERAS:
        y = x[(x.index >= pd.Period(a, "M")) & (x.index <= pd.Period(b, "M"))].dropna()
        if strip and e == "1975-89":
            parts.append("1975-89 no data (passes by construction, tests nothing)")
            continue
        parts.append("%s alpha %s %%/yr, lb95 %s, Sharpe %s" % (
            e, cell(float(y.mean() * 1200) if len(y) else np.nan, len(y)),
            cell(alpha_lb(y) * 1200 if len(y) >= MIN_PRINT else np.nan, len(y)), cell(ST.sharpe(y), len(y))))
    out("ERAS | %s | %s" % (lab, " | ".join(parts)))


def _p4(net, spx, out, lab):
    from gm import stats as ST
    import a2_batch as A2
    if spx is None:
        out("P4 | %s | not computed (no S&P series given)" % lab)
        return
    ix = spx.index.union(net.index).sort_values()          # one sorted month index (a2_batch.p4 slices by label)
    net, spx = net.reindex(ix), spx.reindex(ix)
    w = A2.p4(net, spx)
    j = pd.concat([ST.cut(net, P4_FROM, "2010-12"), ST.cut(w, P4_FROM, "2010-12")], axis=1).dropna()
    out("P4 | %s | S&P 500 alone (M1) | item %s | specific %s" % (lab, cell(ST.sharpe(j.iloc[:, 0]), len(j)),
                                                                  cell(ST.sharpe(j.iloc[:, 1]), len(j))))


def _mean_cond(x, cond):
    y = x[cond.reindex(x.index).fillna(False).astype(bool)]
    return (float(y.mean()) if len(y) else np.nan), len(y)


def report_strip(sp, spx, out, n_placebo=NPLACEBO):
    from gm import seal as SL
    from gm import stats as ST
    res = {"name": "Strip reversion"}
    for root, R in sp["roots"].items():
        nst = int(np.sum(R["full"]))
        nstale = int(sum(int(np.sum(R["stale"][k] & R["full"])) for k in KEYS))
        cd = R["complete_days"]
        out("DATA | Strip %s %s | quarterly contracts %d | first month-end %s | start %s | month-ends with the strip %d | "
            "measure-months failing the stale screen %d | held contracts without an entry or exit settlement %d | "
            "complete days %d of %d" % (R["market"], root, R["contracts"], R["first"], R["start"] or "never", nst,
                                        nstale, R["miss_ret"], cd[0], cd[1]))
    bk = strip_run(sp)
    SL.check_output(bk, SL.DESIGN, "b2_batch.report_strip")
    net = bk["net"]
    win = strip_window(net)
    st = sp["roots"].get("ED", {}).get("start")
    out("WINDOW | Strip reversion | start %s | first active block month %s | first scaled test month %s | window %d "
        "months to %s | minimum %d | %s" % (
            st or "never", bk["active"][bk["active"]].index[0] if bk["active"].any() else "-",
            win.index[0] if len(win) else "-", len(win), STRIP_DEC_LAST + 1, MIN_WINDOW,
            "TESTED" if len(win) >= MIN_WINDOW else "INSUFFICIENT DATA"))
    res["window"] = len(win)
    span = pd.period_range(win.index[0], win.index[-1], freq="M") if len(win) else []
    gaps = [q for q in span if q not in win.index]
    flat = int(((bk["gross"].reindex(win.index) == 0)).sum())
    res["flat_months"], res["gaps"] = flat, len(gaps)
    out("DATA | Strip reversion window | months %d | span %d | flat months (no contract held, gross 0) %d | interior "
        "gaps %d | %s" % (len(win), len(span), flat, len(gaps), "contiguous" if not gaps else "GAPS"))
    if gaps:
        raise WindowGap("the Strip window has %d interior gap months" % len(gaps))
    if len(win) < MIN_WINDOW:
        res["status"] = "insufficient data"
        out("B2 VERDICT | Strip reversion | window %d months < %d: insufficient data, not tested" % (len(win),
                                                                                                   MIN_WINDOW))
        return res, bk
    t1 = alpha_zero(win)
    res["T1"] = t1
    out("T1 | Strip reversion | alpha against the empty Core book (= mean) %s %%/yr | bootstrap p %s (raw; Holm count 0: "
        "no Core-eligible pod in B2) | %s" % (cell(t1["alpha"] * 1200, t1["n"]), cell(t1["p"], t1["n"], "%.4f"),
                                             "alpha > 0" if t1["alpha"] > 0 else "alpha <= 0"))
    w2 = strip_run(sp, cost_mult=2.0)["net"].reindex(win.index).dropna()
    t2 = alpha_zero(w2)
    res["T2"] = t2
    out("T2 | Strip reversion | alpha at twice the costs (1 bp of rate per side) %s %%/yr | %s (decisive only for Core)" % (
        cell(t2["alpha"] * 1200, t2["n"]), "> 0" if t2["alpha"] > 0 else "<= 0"))
    pl = strip_placebo(sp, win, n=n_placebo, sc=bk["scores"])
    res["T3"] = {k: pl[k] for k in ("sr", "p", "pass", "n")}
    out("T3 | Strip reversion | placebo window %s..%s | net Sharpe %s | placebos %d | share with Sharpe >= the pod's "
        "%.3f | %s" % (pl["window"][0], pl["window"][1], cell(pl["sr"], len(win)), pl["n"], pl["p"],
                       "PASS" if pl["pass"] else "FAIL"))
    out("T4 | Strip reversion | not applicable: Core book v1 is EMPTY")
    inc = bool(t1["alpha"] > 0 and pl["pass"])
    res["status"] = "Incubator" if inc else "Shelved"
    out("B2 VERDICT | Strip reversion | not Core-eligible (7.2 qualified, no registered live source) | T1 alpha %s, T3 "
        "%s, T4 n/a | %s" % ("> 0" if t1["alpha"] > 0 else "<= 0", "PASS" if pl["pass"] else "FAIL",
                             res["status"].upper()))
    # ---- reported
    _eras(win, out, "Strip reversion", strip=True)
    res["stats"] = _stat_line("POD | Strip reversion | net, k = 1, costs x1", win, out)
    d1 = strip_run(sp, delay=1)["net"].reindex(win.index).dropna()
    out("DELAY | Strip reversion | one-month delay (notionals per contract one month later) | Sharpe %s | mean %s %%/yr"
        % (cell(ST.sharpe(d1), len(d1)), cell(float(d1.mean() * 1200), len(d1))))
    vp = 0
    for v in ("A", "B"):
        x = strip_run(sp, versions=(v,))["net"].reindex(win.index).dropna()
        vp += int(len(x) and x.mean() > 0)
        out("VERSION | Strip reversion %s alone | Sharpe %s | mean %s %%/yr" % (
            v, cell(ST.sharpe(x), len(x)), cell(float(x.mean() * 1200) if len(x) else np.nan, len(x))))
    out("VERSIONS POSITIVE | Strip reversion | %d of 2" % vp)
    by = []
    for root in sp["roots"]:
        x = strip_run(sp, drop=tuple(r for r in sp["roots"] if r != root))["gross"].reindex(win.index).dropna()
        by.append("%s %s" % (sp["roots"][root]["market"], cell(float(x.mean() * 1200) if len(x) else np.nan, len(x))))
    out("BY MARKET | Strip reversion | gross mean %%/yr of each currency alone (one class: short-rate strips) | %s" %
        ", ".join(by))
    held = bk["pos"].abs().reindex(win.index - 1).fillna(0) > 0
    nb = int((bk["bind"].reindex(win.index - 1).fillna(False) & held).to_numpy().sum())
    nh = int(held.to_numpy().sum())
    out("LEG CAP | Strip reversion | held contract-months %d | strip vector scaled by a binding cap %d | share %s" % (
        nh, nb, cell(nb / nh if nh else np.nan, nh, "%.3f")))
    fr = fragility(net, win, (lambda m: strip_run(sp, drop=(m,))["net"]), list(sp["roots"]))
    out("FRAGILITY | Strip reversion | largest change of the annual mean (%%/yr points) without one year: %s %s | "
        "without one currency: %s %s | %s | %s" % (
            fr["year"][0], cell(fr["year"][1] * 100, len(win)), fr["market"][0],
            cell(fr["market"][1] * 100, len(win)),
            ("top year %s gives %s of the net profit" % (fr["top_year"][0], cell(fr["top_year"][1], len(win))))
            if fr["top_year"][0] is not None else "top year: n/a (net profit <= 0)",
            "FLAG (> 0.40)" if fr["flag"] else "no flag"))
    _p4(net, spx, out, "Strip reversion")
    # mean |G| by months to expiry of contract n (spec s15)
    bins = [(0, 3), (4, 6), (7, 9), (10, 12), (13, 15), (16, 18), (19, 21), (22, 27)]
    acc = {b: [] for b in bins}
    for root, R in sp["roots"].items():
        for i, p in enumerate(R["grid"]):
            if not (win.index[0] - 1 <= p <= STRIP_DEC_LAST) or R["strip"][i] is None:
                continue
            for k in KEYS:
                G = R["M"][k][i] - R["N"][k][i]
                if not np.isfinite(G):
                    continue
                y, m = R["strip"][i][k[1] - 1]
                mo = (y - p.year) * 12 + (m - p.month)
                for b in bins:
                    if b[0] <= mo <= b[1]:
                        acc[b].append(abs(G))
    out("GAPS | Strip reversion | mean |G| (bp) by months to expiry of contract n | " + ", ".join(
        "%d-%d %s" % (b[0], b[1], cell(float(np.mean(v)) if v else np.nan, len(v))) for b, v in acc.items()))
    res["falsifiers"] = strip_falsifiers(sp, bk, win, out)
    res["fragility"] = fr
    res["trial"] = _trial(net, bk["turnover"])
    return res, bk


def strip_falsifiers(sp, bk, win, out):
    """Spec s10 items 1-5 (entry item 7)."""
    from gm import stats as ST
    g = bk["gross"].reindex(win.index)
    f = {"gross_mean": float(g.mean())}
    vm = []
    for v in ("A", "B"):
        x = strip_run(sp, versions=(v,))["gross"].reindex(win.index)
        vm.append(float(x.mean()))
    f1 = f["gross_mean"] <= 0 or any(m <= 0 for m in vm)
    out("FALSIFIER 1 | Strip reversion | pod gross mean %s %%/yr | A %s | B %s | %s" % (
        cell(f["gross_mean"] * 1200, len(g), "%.3f"), cell(vm[0] * 1200, len(g), "%.3f"),
        cell(vm[1] * 1200, len(g), "%.3f"), "holds (zero or below)" if f1 else "does not hold"))
    g0 = strip_run(sp, returns="RE0")["gross"].reindex(win.index)
    f2 = float(g0.mean()) > 0 and f["gross_mean"] <= 0
    out("FALSIFIER 2 | Strip reversion | entered at the decision-day settlement (not tradeable) gross mean %s %%/yr | "
        "traded %s | %s" % (cell(float(g0.mean()) * 1200, len(g0), "%.3f"), cell(f["gross_mean"] * 1200, len(g), "%.3f"),
                            "holds (signal-price artefact)" if f2 else "does not hold"))
    sc = bk["scores"]
    G = {}
    for root, R in sp["roots"].items():
        for k in KEYS:
            G[col(root, k)] = pd.Series(np.abs(R["M"][k] - R["N"][k]), index=R["grid"])
    Gf = pd.DataFrame(G).reindex(sc.index)
    sg = Gf.where(sc.reindex(columns=Gf.columns).fillna(0) != 0).sum(axis=1, min_count=1).fillna(0.0)
    j = pd.concat([g, sg.shift(1).reindex(win.index)], axis=1).dropna()
    c3 = float(j.iloc[:, 0].corr(j.iloc[:, 1])) if len(j) > 2 else np.nan
    out("FALSIFIER 3 | Strip reversion | correlation of the gross return with the sum of |G| held %s | %s" % (
        cell(c3, len(j), "%.3f"), "holds (zero or below)" if (c3 == c3 and c3 <= 0) else "does not hold"))
    roll = strip_roll(sp, bk).reindex(win.index)
    f4 = float(roll.mean()) >= f["gross_mean"]
    out("FALSIFIER 4 | Strip reversion | roll part mean %s %%/yr | gross mean %s | %s" % (
        cell(float(roll.mean()) * 1200, len(roll), "%.3f"), cell(f["gross_mean"] * 1200, len(g), "%.3f"),
        "holds (the profit is roll: Carry)" if f4 else "does not hold"))
    hs = []
    for a, b in STRESS:
        pm = bk["pos"].shift(1).loc[pd.Period(a, "M"):pd.Period(b, "M")]
        hs.append("%s..%s %s" % (a, b, "held" if (pm.abs().fillna(0) > 0).any().any() else "not held"))
    out("FALSIFIER 5 / P3 | Strip reversion | funding-stress months: %s | loss flag: not flagged (spec s10 names window "
        "months)" % ", ".join(hs))
    return {"f1": f1, "f2": f2, "c3": c3, "f4": f4}


def strip_roll(sp, bk):
    """Falsifier 4: ex-ante roll part of the held positions (rates aged by the holding period on the decision-day
    strip, linear in days to expiry; below contract 1 extrapolated from contracts 1 and 2)."""
    L = bk["pos"]
    out = pd.Series(np.nan, index=L.index)
    days = sp["days"]
    first_of = pd.Series(days, index=days).groupby(days.to_period("M")).min()
    for t in range(1, len(L.index)):
        p = L.index[t - 1]
        tot, any_ = 0.0, False
        for root, R in sp["roots"].items():
            if p not in R["grid"]:
                continue
            i = R["grid"].get_loc(p)
            st, d = R["strip"][i], R["d"][i]
            if st is None or d is None:
                continue
            x = L.loc[p, ["%s|%d" % (root, j) for j in range(1, 9)]].to_numpy(dtype=float)
            if not np.any(np.nan_to_num(x)):
                continue
            en, ex = first_of.get(p + 1), first_of.get(p + 2)
            if en is None or ex is None:
                continue
            H = (ex - en).days
            tau = np.array([(R["ltd"][k] - d.date()).days for k in st], dtype=float)
            r = R["r"][i]
            if not np.all(np.isfinite(r)):
                continue
            aged = tau - H
            ri = np.interp(aged, tau, r)
            lo = aged < tau[0]
            if lo.any():
                sl = (r[1] - r[0]) / (tau[1] - tau[0])
                ri[lo] = r[0] + sl * (aged[lo] - tau[0])
            dr = ri - r
            tot += float(np.nansum(x * PTS * (-dr / 100.0)))
            any_ = True
        if any_:
            out.iloc[t] = tot
    return out.where(bk["gross"].notna())


def _trial(net, turnover):
    from gm import stats as ST
    s9 = ST.summary(net)
    s7 = ST.summary(net, *ST.EXTRA)
    ok9, ok7 = s9["n"] >= MIN_PRINT, s7["n"] >= MIN_PRINT
    return {"sr_9010": s9["sr"] if ok9 else None, "t_9010": s9["t"] if ok9 else None,
            "maxdd_9010": s9["maxdd"] if ok9 else None, "sr_7589": s7["sr"] if ok7 else None,
            "turnover": float(ST.cut(turnover, *ST.DESIGN).mean() * 12) if len(ST.cut(turnover, *ST.DESIGN)) else None,
            "n_9010": s9["n"], "n_7589": s7["n"]}


def report_rule(name, ru, inp, spx, out, n_placebo=NPLACEBO):
    from gm import seal as SL
    from gm import stats as ST
    res = {"name": name}
    r = rule_run(ru, inp)
    SL.check_output({k: v for k, v in r.items() if isinstance(v, (pd.Series, pd.DataFrame))}, SL.DESIGN,
                    "b2_batch.report_rule")
    win = r["net"]
    f, months = f0_b2(ru, r)
    res["F0"] = f
    out("WINDOW | %s | versions %d | first decision month %s | window %s..%s, %d months | held months %d | episodes %d | "
        "F0 %s | market-months without a return %d" % (
            name, len(ru["versions"]), ru["start"], win.index[0] if len(win) else "-",
            win.index[-1] if len(win) else "-", len(win), f["held"], f["episodes"],
            "met" if f["judgeable"] else "NOT MET", r["miss"]))
    res["window"] = len(win)
    if not f["judgeable"]:
        res["status"] = "not judgeable"
        out("B2 VERDICT | %s | F0 not met: not judgeable (analyst watch condition)" % name)
        return res, r
    if len(win) < MIN_WINDOW:
        res["status"] = "insufficient data"
        out("B2 VERDICT | %s | window %d months < %d: insufficient data" % (name, len(win), MIN_WINDOW))
        return res, r
    t1 = alpha_zero(win)
    res["T1"] = t1
    out("T1 | %s | alpha against the empty Core book (= mean) %s %%/yr | bootstrap p %s (raw; rule layers are outside "
        "the Holm count) | %s" % (name, cell(t1["alpha"] * 1200, t1["n"]), cell(t1["p"], t1["n"], "%.4f"),
                                 "alpha > 0" if t1["alpha"] > 0 else "alpha <= 0"))
    t2 = alpha_zero(rule_run(ru, inp, cost_mult=2.0)["net"].reindex(win.index).dropna())
    res["T2"] = t2
    out("T2 | %s | alpha at twice the costs %s %%/yr | %s (decisive only for Core; a rule layer is never Core)" % (
        name, cell(t2["alpha"] * 1200, t2["n"]), "> 0" if t2["alpha"] > 0 else "<= 0"))
    pl = rule_placebo(ru, inp, win, n=n_placebo)
    res["T3"] = {k: pl[k] for k in ("sr", "p", "pass", "n")}
    out("T3 | %s | placebo (%s) | net Sharpe %s | placebos %d | share with Sharpe >= the rule's %.3f | %s" % (
        name, "windows moved within their year" if ru["kind"] == "daily" else "12-month blocks of the direction arrays",
        cell(pl["sr"], len(win)), pl["n"], pl["p"], "PASS" if pl["pass"] else "FAIL"))
    out("T4 | %s | not applicable: Core book v1 is EMPTY" % name)
    inc = bool(t1["alpha"] > 0 and pl["pass"])
    res["status"] = "Incubator" if inc else "Shelved"
    out("B2 VERDICT | %s | rule layer (hindsight-flagged, never Core) | F0 met, T1 alpha %s, T3 %s, T4 n/a | %s" % (
        name, "> 0" if t1["alpha"] > 0 else "<= 0", "PASS" if pl["pass"] else "FAIL", res["status"].upper()))
    # ---- reported
    _eras(win, out, name)
    res["stats"] = _stat_line("POD | %s | net, %s, costs x1, held size 0.10 / 0.40" % (
        name, "daily windows (E14)" if ru["kind"] == "daily" else "k = 1"), win, out)
    if ru["kind"] == "monthly":
        k0 = rule_run(ru, inp, timing="k0")["net"]
        dl = rule_run(ru, inp, timing="delay")["net"]
        out("TIMING | %s | k = 0 Sharpe %s | one-month delay Sharpe %s | k = 1 held market-months flagged (k = 0 "
            "return used) %s" % (name, cell(ST.sharpe(k0), len(k0)), cell(ST.sharpe(dl), len(dl)),
                                 _flag_share(r["pos"], inp)))
    else:
        out("TIMING | %s | k = 0 and the one-month delay: not applicable (the dates are the signal, 7.3 item 3)" % name)
    vp = 0
    for v in ru["versions"]:
        x = rule_run(ru, inp, versions=[v])["net"].reindex(win.index)
        vp += int(x.mean() > 0)
    out("VERSIONS POSITIVE | %s | %d of %d (each version alone as the whole rule)" % (name, vp, len(ru["versions"])))
    pos = r["pos"]
    mk = [c for c in pos.columns if pos[c].abs().sum() > 0]
    if ru["kind"] == "monthly":
        cm = []
        for m in mk:
            x = (HELD * pos[m].shift(1) * inp["R1"][m].reindex(pos.index)).reindex(win.index)
            x = x[pos[m].shift(1).reindex(win.index).fillna(0) != 0]
            cm.append("%s %s" % (m, cell(float(x.mean() * 1200) if len(x) else np.nan, len(x))))
        out("BY MARKET | %s | gross contribution %%/yr over its held months | %s" % (name, ", ".join(cm) or "none"))
        pairs = ("bd_us_2y" in mk and "bd_us_10y" in mk and ru["units"][0]["partner"] is not None)
        mkts = [] if pairs else mk
        fr = fragility(win, win, (lambda m: rule_run(ru, inp, drop=(m,))["net"]), mkts)
    else:
        out("BY MARKET | %s | one market (eq_us_spx)" % name)
        fr = fragility(win, win)
    res["fragility"] = fr
    out("FRAGILITY | %s | largest change of the annual mean (%%/yr points) without one year: %s %s | without one "
        "market: %s %s | %s | %s" % (
            name, fr["year"][0], cell(fr["year"][1] * 100, len(win)), fr["market"][0] or "n/a (one market or a pair)",
            cell(fr["market"][1] * 100, len(win)) if fr["market"][0] else "",
            ("top year %s gives %s of the net profit" % (fr["top_year"][0], cell(fr["top_year"][1], len(win))))
            if fr["top_year"][0] is not None else "top year: n/a (net profit <= 0)",
            "FLAG (> 0.40)" if fr["flag"] else "no flag"))
    _p4(win, spx, out, name)
    out("TUNED KNOBS | %s | %s; hindsight-flagged (7.2 item 3)" % (name, KNOBS[name]))
    res["falsifiers"] = rule_falsifiers(name, ru, inp, r, win, out)
    res["trial"] = _trial(win, r["turnover"])
    return res, r


def _flag_share(pos, inp):
    held = pos.shift(1).abs()
    f = inp["flags"].reindex(index=held.index, columns=held.columns).fillna(False).astype(bool)
    tot = float(held.sum().sum())
    fl = float(held.where(f, 0.0).sum().sum())
    n = int((held > 0).to_numpy().sum())
    return cell(fl / tot if tot > 0 else np.nan, n, "%.3f")


def rule_falsifiers(name, ru, inp, r, win, out):
    """Specs s10 (entry item 7)."""
    R1, R, ci, idx = inp["R1"], inp["R"], inp["ci"], inp["idx"]
    g = r["gross"].reindex(win.index)
    pos = r["pos"]
    heldp = pos.ne(0).any(axis=1).shift(1).reindex(win.index).fillna(False).astype(bool)
    f = {}
    if name in ("card 1 R1", "card 1 R2"):
        m, n = _mean_cond(g, heldp)
        GS2 = ci.m("GS2").reindex(idx)
        cm = card1_condition_months(name, inp)
        eps = [e for e in episodes_of(cm) if e[-1] <= pd.Period("2009-12", "M")]
        hi = sum(1 for e in eps if GS2.get(e[-1] + 12, np.nan) > GS2.get(e[-1], np.nan))
        f = {"mean": m, "episodes": len(eps), "gs2_higher": hi}
        out("FALSIFIER | %s | gross mean over held months %s %%/yr | episodes ending by 2009-12 %d, GS2 higher 12 months "
            "after the last condition month in %d | %s" % (
                name, cell(m * 1200 if m == m else m, n, "%.3f"), len(eps), hi,
                "holds" if ((m == m and m <= 0) or (eps and hi > len(eps) / 2)) else "does not hold"))
    elif name == "card 1 R5":
        stocks = [c for c in pos.columns if c.startswith("eq_")]
        x = (HELD * pos[stocks].shift(1) * R1[stocks].reindex(pos.index)).sum(axis=1).reindex(win.index)
        hs = pos[stocks].ne(0).any(axis=1).shift(1).reindex(win.index).fillna(False).astype(bool)
        m, n = _mean_cond(x, hs)
        f = {"stock_mean": m}
        out("FALSIFIER | %s | stock leg gross mean over its held months %s %%/yr | %s | Economic trend trade-theme part: "
            "not computed (no gate)" % (name, cell(m * 1200 if m == m else m, n, "%.3f"),
                                        "holds" if (m == m and m <= 0) else "does not hold"))
    elif name == "card 2 R1":
        on = pd.concat(list(ru["on"].values()), axis=1).any(axis=1)
        y = R1["bd_us_10y"].reindex(idx)
        onm = on.shift(1).reindex(win.index).fillna(False).astype(bool)
        a, na = _mean_cond(y.reindex(win.index), onm)
        b, nb = _mean_cond(y.reindex(win.index), ~onm)
        f = {"on": a, "off": b}
        out("FALSIFIER | %s | bd_us_10y mean return after on-months %s | after off-months %s %%/yr | %s" % (
            name, cell(a * 1200 if a == a else a, na, "%.3f"), cell(b * 1200 if b == b else b, nb, "%.3f"),
            "holds (no worse)" if (a == a and b == b and a >= b) else "does not hold"))
    elif name == "card 2 R2":
        on = pd.concat(list(ru["on"].values()), axis=1).any(axis=1)
        x = R["eq_us_spx"].reindex(idx)
        fwd = (1 + x).rolling(12).apply(np.prod, raw=True).shift(-12) - 1
        d = (idx >= ru["start"]) & (idx <= pd.Period("2009-12", "M"))
        a, na = _mean_cond(fwd[d], on[d])
        b, nb = _mean_cond(fwd[d], ~on[d])
        GS10 = ci.m("GS10").reindex(idx)
        eps = [e for e in episodes_of([p for p, v in on.items() if v and ru["start"] <= p <= DEC_LAST])
               if e[-1] <= pd.Period("2009-12", "M")]
        up = sum(1 for e in eps if GS10.get(e[-1] + 12, np.nan) - GS10.get(e[-1], np.nan) >= 1.0)
        f = {"on": a, "off": b, "mech": (up, len(eps))}
        out("FALSIFIER | %s | S&P 12-month forward excess return after on-months %s | after other months %s | %s | "
            "mechanism: GS10 up a further 1.0+ in %d of %d episodes" % (
                name, cell(a, na, "%.3f"), cell(b, nb, "%.3f"),
                "holds (no lower)" if (a == a and b == b and a >= b) else "does not hold", up, len(eps)))
    elif name in ("card 3 R2", "card 4 R5"):
        FF = ci.m("FEDFUNDS").reindex(idx)
        down = (FF < FF.shift(6)).shift(1).reindex(win.index).fillna(False).astype(bool)
        net = win
        tot = float(net.sum())
        sh = float(net[down].sum() / tot) if tot > 0 else np.nan
        m, n = _mean_cond(g, heldp)
        f = {"share_easing": sh, "mean": m}
        extra = ""
        if name == "card 4 R5":
            on1 = ru["on"]["version 1"]
            dm = on1[(on1.index >= ru["start"]) & (on1.index <= DEC_LAST)]
            extra = " | version 1 on in %s of months" % cell(float(dm.mean()), len(dm), "%.3f")
        out("FALSIFIER | %s | pair gross mean over held months %s %%/yr | share of net P&L after FEDFUNDS fell over 6 "
            "months %s | %s%s" % (name, cell(m * 1200 if m == m else m, n, "%.3f"), cell(sh, len(net), "%.3f"),
                                  "holds" if ((name == "card 3 R2" and m == m and m <= 0) or (sh == sh and sh > 0.80))
                                  else "does not hold", extra))
    elif name == "card 3 R4":
        on = pd.concat(list(ru["on"].values()), axis=1).any(axis=1)
        y = R1["eq_us_spx"].reindex(idx)
        onm = on.shift(1).reindex(win.index).fillna(False).astype(bool)
        a, na = _mean_cond(y.reindex(win.index), onm)
        b, nb = _mean_cond(y.reindex(win.index), ~onm)
        f = {"on": a, "off": b}
        out("FALSIFIER | %s | S&P mean return after on-months %s | after off-months %s %%/yr | %s" % (
            name, cell(a * 1200 if a == a else a, na, "%.3f"), cell(b * 1200 if b == b else b, nb, "%.3f"),
            "holds (no lower)" if (a == a and b == b and a >= b) else "does not hold"))
    elif name == "card 4 R1":
        e = inp["e"]
        lines = []
        for ent in ("oct", "dec"):
            big, oth, bm, om = [], [], set(), set()
            for w in ru["windows"]:
                if w["ent"] != ent:
                    continue
                c = float(ru["lv"].get(_prev_day(ru["E"], w["entry"]), np.nan))
                big_y = c / w["ref"] - 1 >= 0.15 if (c == c and w["ref"] == w["ref"]) else False
                dd = e[(e.index > w["entry"]) & (e.index <= min(w["exit"], SEAL))]
                dd = dd[dd.index >= pd.Timestamp("1975-01-01")]
                dd = dd.dropna()
                (big if big_y else oth).extend(dd.tolist())
                (bm if big_y else om).update(dd.index.to_period("M"))
            a, b = (float(np.mean(big)) if big else np.nan), (float(np.mean(oth)) if oth else np.nan)
            # 1.0.1 M2: n of the printing rule = calendar months spanned by the held days
            lines.append("%s entry: big years %s (%d days) vs other years %s (%d days) %%/yr %s" % (
                ent, cell(a * 25200 if a == a else a, len(bm)), len(big), cell(b * 25200 if b == b else b, len(om)),
                len(oth), "holds" if (a == a and b == b and a <= b) else "does not hold"))
            f[ent] = (a, b)
        out("FALSIFIER | %s | mean e(d) over form A's held days | %s" % (name, " | ".join(lines)))
    elif name == "card 4 R3":
        e = inp["e"]
        vals, vm = [], set()
        for w in ru["windows"]:
            if not any(w["dirs"].values()):
                continue
            dd = e[(e.index > w["entry"]) & (e.index <= min(w["exit"], SEAL))].dropna()
            vals.extend(dd.tolist())
            vm.update(dd.index.to_period("M"))
        a = float(np.mean(vals)) if vals else np.nan
        f = {"mean": a}
        out("FALSIFIER | %s | mean e(d) over held days of gated windows %s %%/yr (%d days) | %s" % (
            name, cell(a * 25200 if a == a else a, len(vm)), len(vals),
            "holds (zero or more)" if (a == a and a >= 0) else "does not hold"))
    if name.startswith("card 3"):
        x = R1["eq_us_spx"].reindex(win.index)
        q = x.quantile(0.10)
        m, n = _mean_cond(win, x <= q)
        f["worst_tenth"] = m
        out("FALSIFIER (c) | %s | mean return in the worst tenth of eq_us_spx months %s %%/yr | %s" % (
            name, cell(m * 1200 if m == m else m, n, "%.3f"), "holds (loses)" if (m == m and m < 0) else
            "does not hold"))
    out("LOSS FLAG | %s | not flagged (spec s10 names window months)" % name)
    return f


def _prev_day(E, d):
    i = E.searchsorted(d)
    return E[i - 1] if i - 1 >= 0 else None


def card1_condition_months(name, inp):
    """Card 1 R1 / R2 condition months, any version (as diag_preb card1_rules cond_any), decision months to 2010-11."""
    ci, R, vol, idx = inp["ci"], inp["R"], inp["vol"], inp["idx"]
    r = DP.card1_rules(ci, R, vol, inp["spx_me"])[name]
    return [p for p in r["cond_months"] if p <= DEC_LAST]


def report(sp, rules, inp, spx, out=print, trials_path=None, n_placebo=NPLACEBO):
    """Entry items 6-8, 11 on the prepared items. Returns the result dict."""
    res = {"items": {}}
    out("--- BATCH B2 (TESTING_PROTOCOL 7.6 step 9; gm/CHANGES.md \"Batch B2\"): Strip reversion (Eurodollar, Euribor; "
        "versions A spread, B curvature; native k = 1) and ten card rule layers (62 versions; k = 1 or card 4 daily "
        "windows; held size 0.10 / 0.40); Core book v1 EMPTY (alpha = the item's own mean); no Core-eligible pod "
        "(Holm count 0); values over fewer than 60 months are printed as count and sign")
    r, _bk = report_strip(sp, spx, out, n_placebo)
    res["items"]["Strip reversion"] = r
    positions = {}
    for name in RULES:
        out("--- %s" % name)
        rr, run_ = report_rule(name, rules[name], inp, spx, out, n_placebo)
        res["items"][name] = rr
        positions[name] = run_["pos"]
    out("--- NETTING REPORT (7.6 step 9, register B19 / C7; reported, no threshold)")
    inc = {n: positions[n] for n in RULES if res["items"][n].get("status") == "Incubator"}
    res["netting_shadow"] = netting(inc, "shadow book (Incubator rules)", out)
    res["netting_all"] = netting(positions, "all ten judged rules (context)", out)
    if trials_path:
        import a2_batch as A2
        si = A2.selection_inflation(trials_path)
        out("selection inflation (7.8 item 2; printed beside, not subtracted): %d logged book / pod rows, mean 1990-2010 "
            "Sharpe %.3f, sd %.3f, z %.2f -> expected best Sharpe from luck alone about %+.2f" % (
                si["n"], si["mean"], si["sd"], si["z"], si["inflation"]))
    out("NOT APPLICABLE | Sharpe difference of the Core book with an item (empty book) | untouched markets (none held "
        "back) | NOT COMPUTED in %s: the weekly-implementation checks (entry item 4q)" % VERSION)
    summ = []
    for k, v in res["items"].items():
        summ.append("%s %s" % (k, str(v.get("status", "?")).upper()))
    out("B2 SUMMARY | " + " | ".join(summ))
    return res


def _r(v, nd):
    return None if v is None or v != v else round(float(v), nd)


def trial_rows(res, engine_version=ENGINE):
    """Entry item 12: 11 'pod' rows and 2 'diag' rows."""
    from gm import config as CF
    rows = []
    base = {"version": VERSION, "lseg": LSEG_LOCK[:16], "card": CARD_LOCK[:16], "panel": A1_PANEL_ID[:16]}
    for name, it in res["items"].items():
        c = dict(base, item=name)
        note = ("TESTING_PROTOCOL 7.6 step 9 Batch B2; engine %s; %s; LOCK_LSEG_v5 %s; LOCK_CARD_v1 %s; A1 panel %s; Core "
                "book v1 EMPTY (alpha = mean); window %s; verdict %s" % (
                    engine_version, VERSION, LSEG_LOCK[:16], CARD_LOCK[:16], A1_PANEL_ID[:16], it.get("window"),
                    it.get("status")))
        row = {"trial": "%s B2 (k = 1)" % name, "family": "pod", "hash": CF.cfg_hash(c), "note": note,
               "config": json.dumps(c, sort_keys=True)}
        t = it.get("trial")
        if t:
            row.update({"sr_9010": _r(t["sr_9010"], 3), "t_9010": _r(t["t_9010"], 2),
                        "maxdd_9010": _r(t["maxdd_9010"], 3), "sr_7589": _r(t["sr_7589"], 3),
                        "turnover": _r(t["turnover"], 1)})
        rows.append(row)
    for nm, what in (("Strip reversion falsifiers (spec s10, incl. the non-tradeable variant)", "strip s10"),
                     ("Card rule falsifiers (specs s10) and netting report (B2)", "cards s10 + netting")):
        c = dict(base, diag=what)
        rows.append({"trial": nm, "family": "diag", "hash": CF.cfg_hash(c),
                     "note": "TESTING_PROTOCOL 7.6 step 9 Batch B2; %s; engine %s" % (VERSION, engine_version),
                     "config": json.dumps(c, sort_keys=True)})
    return rows
