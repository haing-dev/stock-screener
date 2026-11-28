"""b1_curve: Batch B1 = Curve carry (TESTING_PROTOCOL 7.6 step 8, register T08, SPEC_Curve_carry), as registered in
gm/CHANGES.md "Batch B1: Curve carry" (2026-11-28, before this code). Runs where the LSEG store and the A1 panel exist
(the user's PC); tested in the cloud on mock LSEG tables with invented prices only.

The pod: per commodity, long the contract delivering 12 months after the front leg, short the front leg (the nearest
contract delivering at least three calendar months after the decision month), equal face value; V1 always on, V2 flat
when the front settles above the far contract; the two versions averaged; one block at unit volatility, the pod alone at
the book's 10% target, the E11 joint leg cap from the front leg's volatility, 5x gross cap, costs per leg in contract
space; k = 0 (decision-day settlement). Tested against the EMPTY Core book v1 (alpha = the pod's own mean).

API
  contract_table(cat, long, roots, cut=None)   entry item 4a-c: settlements by (root, delivery), observed expiries
  prepare(tab)                                 legs, states, screens, returns, volatilities, eligibility, start (4e-4j)
  run(prep, cost_mult=1, delay=0, versions=(1, 2), score_perm=None, drop=())    the pod alone (4k-4n)
  truncation(cat, long, roots, dates, out)     entry item 7 (PASS / FAIL and counts only)
  report(prep, spx, blocks, out, ...)          entry items 5-6, 8; returns the result dict
  trial_rows(res)                              entry item 9 (one 'pod' row, one 'diag' row)
  core_facts(path), preb_facts(path), lseg_lock_of(work_dir)                job checks (entry item 10)
"""
import datetime as dt
import json
import os

import numpy as np
import pandas as pd

VERSION = "b1_curve-1.0.0"
LSEG_LOCK = "90322681b9f989cc24393ae7de4fe24bf5af2f32074ffa6400b1cbed09c4074c"          # LOCK_LSEG_v5
A1_PANEL_ID = "e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43"
LOCK_V2 = "d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9"
ENGINE = "gm-2.2.1"
REF_SHA = "cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39"
CFG_HASHES = {"BASE": "f1d682c384", "CANDIDATE": "438a092b53", "A1_INCUMBENT": "77374d7bef",
              "A2_CHALLENGER": "1faa343535"}
FINAL_NAME, FINAL_HASH = "gm-2.0.4-candidate-x1", "77374d7bef"
TRIAL_ROWS_SHA = "f200d02ce574f002753c0d9ad54ae7a082c8e7f3d2ad120a14905fcf498e268a"     # book / pod rows, N = 41
TRIAL_ROWS_N = 41
A2_REPORT, CORE_REPORT, PREB_REPORT = "gm_a2_v1.txt", "gm_core_v1.txt", "gm_diag_preb_v1.txt"
SEAL = pd.Timestamp("2010-12-31")
LAST = pd.Period("2010-12", "M")
GRID0 = pd.Period("1970-01", "M")
WIN = ("1975-01", "2010-12")
ERAS = (("1975-2010", "1975-01", "2010-12"), ("1975-89", "1975-01", "1989-12"), ("1990-2010", "1990-01", "2010-12"))
P4_FROM = "1978-01"
MIN_PRINT = 60
MIN_WINDOW = 120
SEED = 20261101
NBOOT = 10000
NPLACEBO = 1000
FRONT_MIN = 3          # spec s3 step 2: delivery at least three calendar months after month t
FAR_OFF = 12           # spec s3 step 3: the same delivery month one year later
START_N = 8            # spec s7: at least 8 of the 16 markets eligible
POS_SCALE = 0.40       # spec s3 step 9: score x 40% / vol
VOL_CFG = {"vol": {"model": "hybrid", "hl_days": 35, "hl_months": 6, "fast_w": 0.7, "floor": 0.75}}  # CANDIDATE's
BOOK_VOL, RISK_CAP, GROSS_CAP, BLOCK_MONTHS, SCALER_MIN, BLOCK_CAP = 0.10, 0.10, 5.0, 36, 24, 50.0
# spec s4: the 16 panel commodities, in the spec's order; LSEG root -> engine id (tools/lseg/lseg_roots.csv)
ROOTS = (("CL", "cm_wti"), ("LCO", "cm_brent"), ("NG", "cm_natgas"), ("HO", "cm_heatoil"), ("RB", "cm_gasoline"),
         ("GC", "cm_gold"), ("SI", "cm_silver"), ("HG", "cm_copper"), ("PL", "cm_platinum"), ("C", "cm_corn"),
         ("W", "cm_wheat"), ("S", "cm_soybeans"), ("SB", "cm_sugar"), ("KC", "cm_coffee"), ("CT", "cm_cotton"),
         ("LC", "cm_cattle"))
MARKET = dict(ROOTS)
LISTING = ("NG", "HO", "GC", "KC")            # data entry item 2c: continuous positions, registered listing models
OIL = ("cm_wti", "cm_brent", "cm_heatoil", "cm_gasoline")      # entry item 6: crude or oil-product spreads (P3)
OIL_SPIKE = ("1990-08", "1990-10")                             # config.STRESS_WINDOWS "1990 oil spike"
CONFIG = {"name": "curve-carry-b1", "pod": "Curve carry (T08)", "versions": ["V1 always on",
                                                                            "V2 flat in backwardation"],
          "front_min_months": FRONT_MIN, "far_offset_months": FAR_OFF, "start_markets": START_N,
          "markets": [m for _, m in ROOTS], "vol": VOL_CFG["vol"], "block_vol_months": BLOCK_MONTHS,
          "book_vol": BOOK_VOL, "market_risk_cap": RISK_CAP, "gross_cap": GROSS_CAP, "timing": "k0",
          "leg_cap": "joint, from the front leg's hybrid volatility (E11)", "costs": "cost_bp per leg, contract space",
          "lseg_lock": LSEG_LOCK[:16]}


class AsRunMismatch(RuntimeError):
    pass


# =====================================================================================================================
# checks of the job (entry item 10)
# =====================================================================================================================
def _lines(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read().splitlines()


def core_facts(path):
    """gm_core_v1 report -> (ok, reason): 'CORE V1 JOB DONE' and a 'CORE BOOK V1 EMPTY |' line."""
    if not os.path.exists(path):
        return False, "missing (%s)" % os.path.basename(path)
    L = _lines(path)
    if not any(x.strip() == "CORE V1 JOB DONE" for x in L):
        return False, "no 'CORE V1 JOB DONE' line"
    if not any(x.startswith("CORE BOOK V1 EMPTY |") for x in L):
        return False, "no 'CORE BOOK V1 EMPTY' line"
    return True, "ok"


def preb_facts(path):
    """gm_diag_preb_v1 report -> (ok, reason): 'PREB JOB DONE' (7.6 step 7 ended)."""
    if not os.path.exists(path):
        return False, "missing (%s)" % os.path.basename(path)
    if not any(x.strip() == "PREB JOB DONE" for x in _lines(path)):
        return False, "no 'PREB JOB DONE' line"
    return True, "ok"


def lseg_lock_of(work_dir):
    """The LSEG store's lock id from work_dir/lseg/manifest.json and its LOCK file, read BEFORE any table."""
    import lsegdata as LD
    root = os.path.join(work_dir, "lseg")
    try:
        with open(os.path.join(root, "manifest.json"), encoding="utf-8") as f:
            man = json.load(f)
        with open(os.path.join(root, "LOCK"), encoding="utf-8") as f:
            lk = f.read().strip()
    except OSError as e:
        return None, "no LSEG store (%s)" % type(e).__name__
    lid = LD.lock_id_of(man)
    if lid != lk:
        return None, "LOCK does not match manifest.json"
    return lid, "ok"


# =====================================================================================================================
# contract table (entry item 4a-c)
# =====================================================================================================================
def mi(y, m):
    return y * 12 + m - 1


def ym(i):
    return int(i) // 12, int(i) % 12 + 1


def pmi(p):
    return mi(p.year, p.month)


def ymd(v):
    """A TR.ExpiryDate value (YYYYMMDD or an Excel serial) -> date (lseg_ident_v4)."""
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None
    if 19000101 <= v <= 21001231 and float(v).is_integer():
        iv = int(v)
        try:
            return dt.date(iv // 10000, iv // 100 % 100, iv % 100)
        except ValueError:
            return None
    if 20000 < v < 80000:
        return dt.date(1899, 12, 30) + dt.timedelta(days=int(round(v)))
    return None


_RULE = {}


def rule_dates(root, y, m):
    import lseg_rules as LR
    k = (root, y, m)
    if k not in _RULE:
        _RULE[k] = LR.dates(root, y, m)
    return _RULE[k]


def _root_of_ric(code, roots):
    import lsegdata as LD
    m = LD.RIC_RE.match(code)
    if not m or m.group(4) is None:
        return None, None
    root = next((r for r, rc in roots.items() if m.group(1) == str(rc.get("ric_root") or r).upper()), None)
    if root is None or root not in MARKET:
        return None, None
    dec = int(m.group(4))
    year = (1900 if dec >= 5 else 2000) + 10 * dec + int(m.group(3))
    return root, mi(year, LD.MONTH_CODES.index(m.group(2)) + 1)


def _is_price_field(f):
    import lsegdata as LD
    f = str(f or "").strip().upper()
    return f not in LD.ROLE_OF_FIELD and not f.startswith("TR.")


def contract_table(cat, long, roots, cut=None):
    """Entry item 4a-c. cat, long = lsegdata.load_design (design part, held-back hidden); roots = lsegdata.roots_config();
    cut = a date: observations after it are dropped first (truncation). -> {"px": {root: DataFrame (Period months x
    delivery index)}, "src": {root: {delivery: 'DS' | 'HP' | 'LIST'}}, "exp": {root: {delivery: date}}, "conflicts":
    {root: count}}."""
    import lsegdata as LD
    import lseg_rules as LR
    cat = cat[(cat["series_id"].astype(str) != "") & (cat["duplicate_of"].astype(str) == "")]
    cat = cat[cat["status"].astype(str) == "ok"]
    long = long[long["per"] == "M"]
    if cut is not None:
        long = long[long["obs"] <= pd.Timestamp(cut)]
    data = {sid: g for sid, g in long.groupby("sid", sort=False)}

    def series(sid):
        g = data.get(sid)
        if g is None or not len(g):
            return None
        g = g.sort_values("obs", kind="mergesort")
        obs = pd.DatetimeIndex(g["obs"]).normalize()
        s = pd.Series(g["value"].to_numpy(dtype=float), index=obs)
        s = s[obs <= SEAL]
        return s
    # ---- observed expiries (4b): c1 / c2 TR.ExpiryDate, mapped to the delivery whose rule last trading day is nearest
    exp = {r: {} for r, _ in ROOTS}
    for r in cat.itertuples():
        if str(r.field).strip().upper() != "TR.EXPIRYDATE" or r.per != "M":
            continue
        code = str(r.code).strip("<> ").upper()
        root = next((rt for rt in MARKET if code.startswith(str(roots.get(rt, {}).get("ric_root") or rt).upper() + "C")
                     and code[len(str(roots.get(rt, {}).get("ric_root") or rt)) + 1:].isdigit()), None)
        if root is None:
            continue
        n = int(code[len(str(roots.get(root, {}).get("ric_root") or root)) + 1:])
        if n > 2:
            continue
        s = series(r.series_id)
        if s is None:
            continue
        for d, v in s.items():
            e = ymd(v)
            if e is None:
                continue
            best = None
            for k in range(-2, 40):
                y, m = ym(mi(d.year, d.month) + k)
                lt = rule_dates(root, y, m)[0]
                gap = abs((lt - e).days)
                if gap <= 10 and (best is None or gap < best[1]):
                    best = (mi(y, m), gap)
            if best is not None:
                exp[root][best[0]] = e
    # ---- contract-level series (4a): files L14* / L16*, one series per (root, delivery)
    cand = {}
    rx = cat[cat["file"].astype(str).str.match(r"^L1[46][a-z]") & (cat["per"] == "M")]
    for r in rx.itertuples():
        if not _is_price_field(r.field):
            continue
        root, dmi = _root_of_ric(str(r.code).strip("<> ").upper(), roots)
        if root is None or root in LISTING:
            continue
        cand.setdefault((root, dmi), []).append((str(r.fn).upper(), r.series_id))
    px = {}
    src = {r: {} for r, _ in ROOTS}
    conflicts = {r: 0 for r, _ in ROOTS}
    for (root, dmi), lst in sorted(cand.items()):
        pref = ("HP", "DS") if root == "LCO" else ("DS", "HP")
        lst = sorted(lst, key=lambda x: (pref.index(x[0]) if x[0] in pref else 9, x[1]))
        got = None
        for fn, sid in lst:
            s = series(sid)
            if s is not None and s.notna().any():
                got = (fn, s)
                break
        if got is None:
            continue
        s = got[1].dropna()
        s.index = s.index.to_period("M")
        s = s[~s.index.duplicated(keep="last")]
        px.setdefault(root, {})[dmi] = s
        src[root][dmi] = got[0]
    # ---- listing roots (4a): continuous positions identified by lseg_rules.held_contract
    for root in LISTING:
        rc = roots.get(root)
        if not rc:
            continue
        mk = LR.MARKET.get(root, "US")
        obs_y = {(ym(d)[0], ym(d)[1]): e for d, e in exp[root].items()}
        rows = {}
        for n in LD.root_positions(rc, "M"):
            s = series(LD.c_series_id(rc, n, "M"))
            if s is None:
                continue
            for d, v in s.dropna().items():
                day = LD.trading_day(d.date(), mk)
                dl = LR.held_contract(root, n, day, obs_y)
                if dl is None:
                    continue
                key = (pd.Period(d, "M"), mi(*dl))
                rows.setdefault(key, []).append(float(v))
        out = {}
        for (p, dmi), vs in rows.items():
            if len(vs) > 1:
                conflicts[root] += 1
                continue
            out.setdefault(dmi, {})[p] = vs[0]
        for dmi, dd in out.items():
            s = pd.Series(dd).sort_index()
            s.index = pd.PeriodIndex(s.index, freq="M")
            px.setdefault(root, {})[dmi] = s
            src[root][dmi] = "LIST"
    grid = pd.period_range(GRID0, LAST, freq="M")
    tab = {}
    for root, cs in px.items():
        cols = sorted(cs)
        tab[root] = pd.DataFrame({d: cs[d].reindex(grid) for d in cols}, index=grid, columns=cols)
    return {"px": tab, "src": src, "exp": exp, "conflicts": conflicts, "grid": grid}


# =====================================================================================================================
# legs, states, screens, returns, volatilities (entry item 4e-4j)
# =====================================================================================================================
def leg_dates(root, dmi, exp):
    """Item 2b: (last trading day, first notice day) of root's contract delivering in month index dmi."""
    y, m = ym(dmi)
    lt, fn = rule_dates(root, y, m)
    return exp.get(root, {}).get(dmi, lt), fn


def prepare(tab):
    """-> the per-market frames on the grid (columns = engine ids): F, D (delivery index of the legs at decision t),
    pair, B, stale, cal, rs (spread return of month t), rf (front-leg return of month t), rD, rF (leg returns of the
    pair chosen at t-1, only where rs exists), bnext (held front above far at month-end t), mixed (pair mixes forms),
    vol, volF, slow, eligible counts, t0."""
    from gm import vol as VM
    grid = tab["grid"]
    G = len(grid)
    gi = np.array([pmi(p) for p in grid])
    cols = [m for _, m in ROOTS]
    fr = {k: pd.DataFrame(np.nan, index=grid, columns=cols) for k in
          ("F", "D", "B", "rs", "rf", "rD", "rF", "bnext")}
    bl = {k: pd.DataFrame(False, index=grid, columns=cols) for k in ("pair", "stale", "cal", "mixed", "noret")}
    for root, mkt in ROOTS:
        T = tab["px"].get(root)
        if T is None or not T.shape[1]:
            continue
        dl = np.array(T.columns, dtype=np.int64)
        X = T.to_numpy(dtype=float)
        F = np.full(G, -1, dtype=np.int64)
        Dc = np.full(G, -1, dtype=np.int64)
        for i in range(G):
            ok = np.flatnonzero((dl >= gi[i] + FRONT_MIN) & np.isfinite(X[i]))
            if not len(ok):
                continue
            F[i] = dl[ok[0]]
            j = np.flatnonzero(dl == F[i] + FAR_OFF)
            if len(j) and np.isfinite(X[i, j[0]]):
                Dc[i] = dl[j[0]]
        col = {d: k for k, d in enumerate(dl)}

        def p(i, d):
            return X[i, col[d]] if (d >= 0 and 0 <= i < G) else np.nan
        exp = tab["exp"]
        src = tab["src"].get(root, {})
        for i in range(G):
            f, d = F[i], Dc[i]
            if f >= 0:
                fr["F"].iat[i, cols.index(mkt)] = f
            if f >= 0 and d >= 0:
                c = cols.index(mkt)
                fr["D"].iat[i, c] = d
                bl["pair"].iat[i, c] = True
                pf, pd_ = p(i, f), p(i, d)
                fr["B"].iat[i, c] = 1.0 if pf > pd_ else 0.0
                st = (np.isfinite(p(i - 1, f)) and p(i - 1, f) == pf) or (np.isfinite(p(i - 1, d)) and p(i - 1, d) == pd_)
                bl["stale"].iat[i, c] = bool(st)
                hold = gi[i] + 1
                hit = False
                for q in (f, d):
                    lt, fn = leg_dates(root, q, exp)
                    for x in (lt, fn):
                        if x is not None and mi(x.year, x.month) == hold:
                            hit = True
                bl["cal"].iat[i, c] = hit
                bl["mixed"].iat[i, c] = src.get(f) != src.get(d)
            if i == 0:
                continue
            f0, d0 = F[i - 1], Dc[i - 1]
            c = cols.index(mkt)
            if f0 >= 0:
                a, b = p(i - 1, f0), p(i, f0)
                if np.isfinite(a) and np.isfinite(b) and a != 0:
                    fr["rf"].iat[i, c] = b / a - 1
            if f0 >= 0 and d0 >= 0:
                a, b, a2, b2 = p(i - 1, f0), p(i, f0), p(i - 1, d0), p(i, d0)
                if all(np.isfinite(v) for v in (a, b, a2, b2)) and a != 0 and a2 != 0:
                    rF, rD = b / a - 1, b2 / a2 - 1
                    fr["rs"].iat[i, c] = rD - rF
                    fr["rD"].iat[i, c], fr["rF"].iat[i, c] = rD, rF
                    fr["bnext"].iat[i, c] = 1.0 if b > b2 else 0.0
                else:
                    bl["noret"].iat[i, c] = True
    out = dict(fr)
    out.update(bl)
    out["vol"] = VM.estimate(fr["rs"], VOL_CFG, None)
    out["slow"] = VM.slow(fr["rs"])
    out["volF"] = VM.estimate(fr["rf"], VOL_CFG, None)
    elig = out["slow"].notna()
    out["n_elig"] = elig.sum(axis=1)
    hit = out["n_elig"][out["n_elig"] >= START_N]
    out["t0"] = hit.index[0] if len(hit) else None
    out["grid"] = grid
    out["valid"] = valid_mask(out)
    out["tab_meta"] = {"src": tab["src"], "conflicts": tab["conflicts"]}
    return out


def valid_mask(prep, drop=()):
    """Item 4k: where a score is defined (t >= t0, the pair exists, no stale leg, no calendar exclusion)."""
    t0 = prep["t0"]
    v = prep["pair"] & ~prep["stale"] & ~prep["cal"]
    if t0 is None:
        v = v & False
    else:
        v = v.mul(pd.Series(np.asarray(prep["grid"] >= t0), index=prep["grid"]), axis=0).astype(bool)
    for m in drop:
        v[m] = False
    return v


def scores(prep, versions=(1, 2), drop=()):
    """Item 4k: {version: score frame} (V1 = 1, V2 = 1 - B, missing where not valid)."""
    v = valid_mask(prep, drop) if drop else prep["valid"]
    out = {}
    for k in versions:
        s = pd.DataFrame(1.0, index=v.index, columns=v.columns) if k == 1 else 1.0 - prep["B"]
        out[k] = s.where(v)
    return out


# =====================================================================================================================
# the pod alone (entry items 4k-4n)
# =====================================================================================================================
def version_positions(prep, sc):
    """Item 4k: p_v = s_v x 0.40 / v / n_v, only where the market is eligible (4i: slow part of v) and has a cap
    volatility; pod p = mean over versions at the
    unscaled stage (a missing version adds 0; no position where none has one)."""
    pv = {}
    for k, s in sc.items():
        p = (s * POS_SCALE / prep["vol"]).where(prep["slow"].notna() & prep["volF"].notna())   # item 4i
        n = p.notna().sum(axis=1)
        pv[k] = p.div(n.where(n > 0), axis=0)
    V = len(pv)
    have = sum(p.notna().astype(int) for p in pv.values()) > 0
    pod = (sum(p.fillna(0) for p in pv.values()) / V).where(have)
    return pv, pod


def run(prep, cost_mult=1.0, delay=0, versions=(1, 2), score_perm=None, drop=()):
    """The pod alone (entry item 4l-4n). score_perm = {"start": first window month, "perm": date map} moves the score
    arrays of every version jointly (T3); drop = markets removed (fragility). -> dict of frames and series."""
    from gm import book as B
    from gm import seal as SL
    from gm import stats as ST
    sc = scores(prep, versions, drop)
    if score_perm is not None:
        sc = {k: ST.move_rows(s, score_perm["perm"], score_perm["start"]) for k, s in sc.items()}
    pv, p = version_positions(prep, sc)
    rs = prep["rs"]
    rb = (p.shift(1) * rs).sum(axis=1, min_count=1)
    k = (1.0 / (rb.rolling(BLOCK_MONTHS, min_periods=SCALER_MIN).std() * np.sqrt(12))).shift(1).clip(upper=BLOCK_CAP)
    total = p.mul(k, axis=0).fillna(0.0)
    blocks = rb * k
    active = blocks.notna()
    raw = (total.shift(1) * rs.fillna(0)).sum(axis=1).where(active)
    s = (BOOK_VOL / (raw.rolling(36, min_periods=SCALER_MIN).std() * np.sqrt(12))).shift(1)
    pos = total.mul(s, axis=0)
    mk = list(rs.columns)
    dcol, fcol = ["%s|D" % m for m in mk], ["%s|F" % m for m in mk]
    L = pd.concat([pos.set_axis(dcol, axis=1), (-pos).set_axis(fcol, axis=1)], axis=1)
    capF = (RISK_CAP * BOOK_VOL * 3) / prep["volF"]
    cap = pd.concat([capF.set_axis(dcol, axis=1), capF.set_axis(fcol, axis=1)], axis=1)
    groups = [{"members": [a, b], "cap_from": b} for a, b in zip(dcol, fcol)]
    Lc = B.cap_positions(L, cap, groups)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = (Lc[dcol].abs().to_numpy() / L[dcol].abs().to_numpy())
    bind = pd.DataFrame(ratio < 1 - 1e-12, index=L.index, columns=mk) & (L[dcol].abs().to_numpy() > 0)
    g = Lc.abs().sum(axis=1)
    Lg = Lc.mul((GROSS_CAP / g).clip(upper=1), axis=0)
    RE = pd.concat([prep["rD"].set_axis(dcol, axis=1), prep["rF"].set_axis(fcol, axis=1)], axis=1)
    lag = 1 + int(delay)
    gross = (Lg.shift(lag) * RE).sum(axis=1, min_count=1).where(active & s.notna())
    cid = pd.concat([prep["D"].set_axis(dcol, axis=1), prep["F"].set_axis(fcol, axis=1)], axis=1)
    same = (cid == cid.shift(1)) & cid.notna()         # the leg holds the same contract at t-1 and t
    prev = Lg.shift(1)
    trade = (Lg - prev).abs().where(same | (Lg.fillna(0) == 0) | (prev.fillna(0) == 0), Lg.abs() + prev.abs())
    one = pd.Series({c: B.cost_bp(c.split("|")[0])[0] / 1e4 for c in Lg.columns})
    tc = (trade * one).sum(axis=1)
    net = gross - cost_mult * tc.shift(lag)
    out = {"net": net, "gross": gross, "pos": Lg[dcol].set_axis(mk, axis=1), "legs": Lg, "cost": tc,
           "turnover": trade.sum(axis=1), "rb": rb, "k": k, "s": s, "active": active, "p": p, "pv": pv,
           "scores": sc, "bind": bind}
    return SL.check_output(out, SL.DESIGN, "b1_curve.run")


# =====================================================================================================================
# truncation (entry item 7)
# =====================================================================================================================
def _diff(a, b, T):
    """Differing cells of two frames / series on months <= T (missing = missing is equal)."""
    Tp = pd.Period(T, "M")
    a = a.loc[a.index <= Tp]
    b = b.loc[b.index <= Tp]
    if isinstance(a, pd.Series):
        a, b = a.to_frame(), b.to_frame()
    cols = sorted(set(a.columns) | set(b.columns), key=str)
    idx = a.index.union(b.index)
    x = a.reindex(index=idx, columns=cols).astype(float).to_numpy()
    y = b.reindex(index=idx, columns=cols).astype(float).to_numpy()
    eq = (x == y) | (np.isnan(x) & np.isnan(y)) | (np.abs(x - y) <= 1e-12 * np.maximum(1, np.abs(x)))
    return int((~eq).sum())


def stages(tab, prep, res):
    out = {}
    for root, T in tab["px"].items():
        out["px " + root] = T
    for k in ("F", "D", "B", "rs", "rf", "rD", "rF", "bnext", "vol", "volF", "slow"):
        out[k] = prep[k]
    for k in ("pair", "stale", "cal", "valid"):
        out[k] = prep[k].astype(float)
    out["n_elig"] = prep["n_elig"].astype(float)
    for v, s in res["scores"].items():
        out["score V%d" % v] = s
    for v, p in res["pv"].items():
        out["position V%d" % v] = p
    for k in ("p", "rb", "k", "s", "legs", "gross", "net", "cost"):
        out[k] = res[k]
    return out


def truncation(cat, long, roots, dates, out=print, full=None):
    """Entry item 7: the pod rebuilt with every LSEG observation dated after T removed, against the full run, months
    <= T, stage by stage. -> (all pass, {T: (failing stages, n stages)})."""
    if full is None:
        tab = contract_table(cat, long, roots)
        prep = prepare(tab)
        full = (tab, prep, run(prep))
    fs = stages(*full)
    res, ok = {}, True
    for T in dates:
        tab = contract_table(cat, long, roots, cut=T)
        prep = prepare(tab)
        cs = stages(tab, prep, run(prep))
        bad = []
        for k in sorted(set(fs) | set(cs)):
            if k not in fs or k not in cs:
                if k.startswith("px ") and (k in fs and (fs[k].index <= pd.Period(T, "M")).any() and
                                            fs[k].loc[fs[k].index <= pd.Period(T, "M")].notna().any().any()):
                    bad.append((k, -1))
                continue
            n = _diff(fs[k], cs[k], T)
            if n:
                bad.append((k, n))
        res[T] = (bad, len(fs))
        ok = ok and not bad
        out("B1 TRUNC %s | stages %d | differing: %s | %s" % (
            T, len(fs), ", ".join("%s %d" % b for b in bad[:6]) or "none", "PASS" if not bad else "FAIL"))
    return ok, res


# =====================================================================================================================
# statistics (entry items 5-6, 8)
# =====================================================================================================================
def cell(v, n, fmt="%.2f"):
    """Printing rule (entry item 8): the value over >= 60 months, else the count and the sign only."""
    if v is None or v != v:
        return "n %d, n/a" % n
    if n >= MIN_PRINT:
        return (fmt % v) + " (%d)" % n
    return "n %d, sign %s" % (n, "+" if v > 0 else ("-" if v < 0 else "0"))


def _cut(r, a=WIN[0], b=WIN[1]):
    from gm import stats as ST
    return ST.cut(r, a, b)


def window(net):
    return _cut(net)


def alpha_zero(x):
    """T1 against the empty Core book (gm.stats.alpha_boot with a zero book: alpha = mean)."""
    from gm import stats as ST
    x = x.dropna()
    return ST.alpha_boot(x, pd.Series(0.0, index=x.index), n=NBOOT, block=6, seed=SEED)


def alpha_lb(x):
    """Entry item 6: one-sided 95% lower bound of the era alpha (= mean) from the T1 bootstrap draws."""
    from gm import stats as ST
    v = x.dropna().to_numpy(dtype=float)
    if len(v) < 24:
        return float("nan")
    idx = ST._stationary_idx(len(v), NBOOT, 6, SEED)
    a = float(v.mean())
    ab = v[idx].mean(axis=1)
    return float(a - np.percentile(ab - a, 95))


def placebo(prep, win, n=NPLACEBO, seed=SEED, cost_mult=1.0):
    """T3: 1,000 date maps over the window (12-month blocks from its first month), both versions' score arrays moved
    jointly, re-sized with each month's own volatility, scalers, caps and costs."""
    from gm import stats as ST
    a, b = str(win.index[0]), WIN[1]

    def fn(perm):
        if perm is None:
            return run(prep, cost_mult)["net"]
        return run(prep, cost_mult, score_perm={"start": a, "perm": perm})["net"]
    r = ST.placebo_runs(fn, (a, b), n=n, L=12, seed=seed)
    r["window"] = (a, b)
    return r


def falsifiers(prep, win_idx):
    """Spec s10 items 1-3 (entry item 6): V1's equal-risk positions before scaling, gross."""
    sc = scores(prep, (1,))
    pv, _ = version_positions(prep, sc)
    p1 = pv[1]
    rs = prep["rs"]
    contrib = p1.shift(1) * rs
    tot = contrib.sum(axis=1, min_count=1)
    Bp = prep["B"].shift(1)
    con = contrib.where(Bp == 0).sum(axis=1, min_count=1).fillna(0).where(tot.notna())
    bak = contrib.where(Bp == 1).sum(axis=1, min_count=1).fillna(0).where(tot.notna())
    held = p1.shift(1).notna() & (p1.shift(1) != 0)
    move = (held & (Bp == 0) & (prep["bnext"] == 1)).any(axis=1)
    idx = [t for t in win_idx if t in tot.index and pd.notna(tot[t])]
    t_ = tot.reindex(idx)
    worst = list(t_.sort_values(kind="mergesort").index[:10])
    share10 = float(np.mean([bool(move[t]) for t in worst])) if worst else float("nan")
    base = float(move.reindex(idx).mean()) if idx else float("nan")
    return {"n": len(idx), "mean": float(t_.mean()) if idx else float("nan"),
            "contango": float(con.reindex(idx).mean()) if idx else float("nan"),
            "backward": float(bak.reindex(idx).mean()) if idx else float("nan"),
            "worst": worst, "share10": share10, "base": base, "move": move, "n_move": int(move.reindex(idx).sum())}


def fragility(prep, net, win):
    """Entry item 6: largest loss of the annualised net mean (on the pod's window) when one year or one market is
    removed; flag when one year gives more than 40% of the net profit."""
    x = net.reindex(win.index)
    base = float(x.mean() * 12)
    yrs = sorted({p.year for p in x.index})
    by_year = {y: float(x[[p.year != y for p in x.index]].mean() * 12) for y in yrs}
    prof = x.groupby([p.year for p in x.index]).sum()
    tot = float(x.sum())
    top = (prof.idxmax(), float(prof.max() / tot)) if tot > 0 and len(prof) else (None, float("nan"))
    by_mkt = {}
    for m in prep["rs"].columns:
        r = run(prep, drop=(m,))["net"].reindex(win.index)
        by_mkt[m] = float(r.mean() * 12) if r.notna().any() else float("nan")
    wy = min(by_year, key=lambda y: by_year[y] - base) if by_year else None
    wm = min(by_mkt, key=lambda m: (by_mkt[m] if by_mkt[m] == by_mkt[m] else np.inf) - base)
    return {"base": base, "year": (wy, by_year.get(wy, np.nan) - base), "market": (wm, by_mkt[wm] - base),
            "top_year": top, "flag": bool(top[1] == top[1] and top[1] > 0.40)}


def data_lines(prep, out):
    """Counts and months only (entry item 10: the data lines before any statistic)."""
    meta = prep["tab_meta"]
    for root, mkt in ROOTS:
        pr = prep["pair"][mkt]
        pm = pr[pr]
        src = meta["src"].get(root, {})
        kinds = sorted(set(src.values()))
        el = prep["slow"][mkt].dropna()
        out("DATA | %s %s | identity %s | contracts %d | pair months %d (%s .. %s) | stale %d | calendar exclusions %d | "
            "pair at t-1 without a return at t %d | mixed-form pairs %d | eligible from %s | listing conflicts %d" % (
                mkt, root, "/".join(kinds) or "none", len(src), int(pr.sum()),
                pm.index[0] if len(pm) else "-", pm.index[-1] if len(pm) else "-",
                int((prep["stale"][mkt] & pr).sum()), int((prep["cal"][mkt] & pr).sum()), int(prep["noret"][mkt].sum()),
                int((prep["mixed"][mkt] & pr).sum()), el.index[0] if len(el) else "never",
                meta["conflicts"].get(root, 0)))


def report(prep, spx=None, blocks=None, out=print, trials_path=None, n_placebo=NPLACEBO):
    """Entry items 4o-6, 8 on the prepared pod. spx = the A1 panel's eq_us_spx monthly excess return (P4); blocks =
    {"carry": series, "trend": series} = the A2-final book's commodity blocks at k = 0. Returns the result dict."""
    from gm import seal as SL
    from gm import stats as ST
    res = {"cfg": CONFIG}
    out("--- BATCH B1: CURVE CARRY (TESTING_PROTOCOL 7.6 step 8; gm/CHANGES.md \"Batch B1: Curve carry\"): 16 commodity "
        "spreads, far = 12 months after the front (>= 3 months out), V1 always on, V2 flat in backwardation, averaged; "
        "k = 0; LSEG LOCK_LSEG_v5 design part; Core book v1 EMPTY (alpha = the pod's own mean); values over fewer than "
        "60 months are printed as count and sign")
    data_lines(prep, out)
    bk = run(prep)
    SL.check_output(bk, SL.DESIGN, "b1_curve.report")
    net = bk["net"]
    win = window(net)
    t0 = prep["t0"]
    fe = bk["active"][bk["active"]]
    out("WINDOW | start t0 (first decision month with >= %d of 16 markets eligible) %s | eligible markets at t0 %s | "
        "first active block month %s | first scaled test month %s | window %d months to %s | minimum %d | %s" % (
            START_N, t0 or "never", int(prep["n_elig"][t0]) if t0 is not None else 0, fe.index[0] if len(fe) else "-",
            win.index[0] if len(win) else "-", len(win), WIN[1], MIN_WINDOW,
            "TESTED" if len(win) >= MIN_WINDOW else "INSUFFICIENT DATA"))
    res["window"] = len(win)
    if len(win) < MIN_WINDOW:
        res.update({"verdict": "insufficient data", "status": "insufficient data"})
        out("B1 VERDICT | Curve carry | window %d months < %d: insufficient data, not tested" % (len(win), MIN_WINDOW))
        return res
    # ---- T1-T4
    t1 = alpha_zero(win)
    res["T1"] = t1
    out("T1 | alpha against the empty Core book (= mean) %s %%/yr | bootstrap p %s (raw; Holm count 0: B1 has no "
        "Core-eligible pod) | %s" % (cell(t1["alpha"] * 1200, t1["n"]), cell(t1["p"], t1["n"], "%.4f"),
                                     "alpha > 0" if t1["alpha"] > 0 else "alpha <= 0"))
    bk2 = run(prep, cost_mult=2.0)
    w2 = _cut(bk2["net"]).reindex(win.index).dropna()
    t2 = alpha_zero(w2)
    res["T2"] = t2
    out("T2 | alpha at twice the costs %s %%/yr | %s (decisive only for Core; Curve carry is not Core-eligible)" % (
        cell(t2["alpha"] * 1200, t2["n"]), "> 0" if t2["alpha"] > 0 else "<= 0"))
    pl = placebo(prep, win, n=n_placebo)
    res["T3"] = {k: pl[k] for k in ("sr", "p", "pass", "n", "window")}
    out("T3 | placebo window %s..%s | pod net Sharpe %s | placebos %d | share with Sharpe >= the pod's %.3f | %s" % (
        pl["window"][0], pl["window"][1], cell(pl["sr"], len(win)), pl["n"], pl["p"], "PASS" if pl["pass"] else "FAIL"))
    out("T4 | not applicable: Core book v1 is EMPTY (test 5 compares two books at the same volatility target; a zero "
        "book has none; reading of \"Core book v1\" item 4j)")
    inc = bool(t1["alpha"] > 0 and pl["pass"])
    res["status"] = "Incubator" if inc else "Shelved"
    out("B1 VERDICT | Curve carry | not Core-eligible (7.2 not qualified; no registered live source) | T1 alpha %s, T3 "
        "%s, T4 n/a | %s" % ("> 0" if t1["alpha"] > 0 else "<= 0", "PASS" if pl["pass"] else "FAIL",
                             res["status"].upper()))
    # ---- reported lines
    out("--- reported, not decisive (7.7 list; spec s5, s10, s14)")
    eras = []
    for lab, a, b in ERAS:
        x = _cut(net, a, b).reindex([p for p in win.index if a <= str(p) <= b]).dropna()
        eras.append("%s alpha %s %%/yr, lb95 %s, Sharpe %s" % (
            lab, cell(float(x.mean() * 1200) if len(x) else np.nan, len(x)),
            cell(alpha_lb(x) * 1200 if len(x) >= MIN_PRINT else np.nan, len(x)), cell(ST.sharpe(x), len(x))))
    out("ERAS | " + " | ".join(eras))
    s = {"n": len(win), "sr": ST.sharpe(win), "mean": float(win.mean() * 12), "vol": float(win.std() * np.sqrt(12)),
         "maxdd": ST.maxdd(win), "skew": float(win.skew()), "lo": ST.lo_sharpe(win)}
    res["stats"] = s
    out("POD | net, k = 0, costs x1 | months %d | Sharpe %s | mean %s %%/yr | achieved vol %s %%/yr | max drawdown %s %% "
        "| skew %s | Lo-adjusted Sharpe %s" % (s["n"], cell(s["sr"], s["n"]), cell(s["mean"] * 100, s["n"]),
                                               cell(s["vol"] * 100, s["n"]), cell(s["maxdd"] * 100, s["n"], "%.1f"),
                                               cell(s["skew"], s["n"]), cell(s["lo"], s["n"])))
    d1 = window(run(prep, delay=1)["net"])
    out("DELAY | one-month delay (positions applied one month late on the leg columns) | Sharpe %s | mean %s %%/yr" % (
        cell(ST.sharpe(d1), len(d1)), cell(float(d1.mean() * 1200), len(d1))))
    vers = {}
    for v in (1, 2):
        x = run(prep, versions=(v,))["net"].reindex(win.index).dropna()
        vers[v] = float(x.mean()) if len(x) else np.nan
        out("VERSION | V%d alone (the whole pod path) | Sharpe %s | mean %s %%/yr" % (
            v, cell(ST.sharpe(x), len(x)), cell(vers[v] * 1200, len(x))))
    out("VERSIONS POSITIVE | %d of 2" % sum(1 for v in vers.values() if v == v and v > 0))
    gross_c = (bk["p"].shift(1) * prep["rs"])
    cm = []
    for m in prep["rs"].columns:
        x = gross_c[m].reindex(win.index)
        x = x[x.notna() & (x != 0)]
        cm.append("%s %s" % (m, cell(float(x.mean() * 1200) if len(x) else np.nan, len(x))))
    out("BY CLASS | one class (commodities) = the pod | BY MARKET (gross contribution of the unscaled pod position, %/yr "
        "per unit, held months) | " + ", ".join(cm))
    held = bk["pos"].abs().reindex(win.index) > 0
    nb = int((bk["bind"].reindex(win.index) & held).sum().sum())
    nh = int(held.sum().sum())
    out("LEG CAP | held market-months %d | binding %d | share %s" % (nh, nb, cell(nb / nh if nh else np.nan, nh,
                                                                                    "%.3f")))
    fr_ = fragility(prep, net, win)
    res["fragility"] = fr_
    ty = ("top year %s gives %s of the net profit" % (fr_["top_year"][0], cell(fr_["top_year"][1], len(win), "%.2f"))
          if fr_["top_year"][0] is not None else "top year: n/a (net profit <= 0)")
    out("FRAGILITY | largest change of the annual mean (%%/yr points) without one year: %s %s | without one market: %s "
        "%s | %s | %s" % (fr_["year"][0], cell(fr_["year"][1] * 100, len(win)), fr_["market"][0],
                          cell(fr_["market"][1] * 100, len(win)), ty, "FLAG (> 0.40)" if fr_["flag"] else "no flag"))
    if spx is not None:
        import a2_batch as A2
        w = A2.p4(net, spx)
        j = pd.concat([_cut(net, P4_FROM, WIN[1]), _cut(w, P4_FROM, WIN[1])], axis=1).dropna()
        out("P4 | S&P 500 alone (M1) | pod %s | specific %s" % (cell(ST.sharpe(j.iloc[:, 0]), len(j)),
                                                               cell(ST.sharpe(j.iloc[:, 1]), len(j))))
    else:
        out("P4 | not computed (no S&P series given)")
    if blocks:
        for nm in ("carry", "trend"):
            b = blocks.get(nm)
            if b is None:
                continue
            cc = []
            for lab, a, b_ in ERAS:
                j = pd.concat([net.reindex(win.index), b], axis=1).dropna()
                j = j.loc[(j.index >= pd.Period(a, "M")) & (j.index <= pd.Period(b_, "M"))]
                cc.append("%s %s" % (lab, cell(float(j.iloc[:, 0].corr(j.iloc[:, 1])) if len(j) > 2 else np.nan,
                                               len(j))))
            out("OVERLAP | correlation with %s's commodity block (A2-final book, k = 0) | %s" % (
                nm.capitalize(), " | ".join(cc)))
    f = falsifiers(prep, win.index)
    res["falsifiers"] = {k: v for k, v in f.items() if k not in ("move", "worst")}
    out("FALSIFIER 1 | V1 pooled gross mean (equal risk, unscaled) %s | %s" % (
        cell(f["mean"] * 1200, f["n"], "%.3f"), "holds (zero or below)" if f["mean"] <= 0 else "does not hold"))
    f2 = f["contango"] <= 0 and f["mean"] > 0
    out("FALSIFIER 2 | contango market-months %s | backwardation market-months %s | %s" % (
        cell(f["contango"] * 1200, f["n"], "%.3f"), cell(f["backward"] * 1200, f["n"], "%.3f"),
        "holds (profit only from backwardation)" if f2 else "does not hold"))
    f3 = (f["share10"] < 0.5) or not (f["share10"] > f["base"])
    out("FALSIFIER 3 | ten worst V1 months with a held front moving above its far contract: %d of %d | base share over "
        "the window %s | %s" % (int(round(f["share10"] * len(f["worst"]))) if f["worst"] else 0, len(f["worst"]),
                                cell(f["base"], f["n"], "%.2f"),
                                "holds (the loss is something else)" if f3 else "does not hold"))
    out("FALSIFIER 4 | not computed: USREC is in no registered source")
    a_, b_ = pd.Period(OIL_SPIKE[0], "M"), pd.Period(OIL_SPIKE[1], "M")
    oil = [m for m in OIL if m in bk["pos"].columns]
    lag_pos = bk["pos"][oil].shift(1)
    oil_held = bool((lag_pos.loc[(lag_pos.index >= a_) & (lag_pos.index <= b_)].abs() > 0).any().any()) and \
        any(a_ <= t <= b_ for t in win.index)
    n_move = f["n_move"]
    seen = oil_held or n_move > 0
    res["loss_not_seen"] = not seen
    out("FALSIFIER 5 / P3 | oil spread held in 1990-08..1990-10: %s | window months with a held front moving into "
        "backwardation: %d | %s" % ("yes" if oil_held else "no", n_move, "loss seen" if seen else "LOSS NOT SEEN"))
    if trials_path:
        import a2_batch as A2
        si = A2.selection_inflation(trials_path)
        out("selection inflation (7.8 item 2; printed beside, not subtracted): %d logged book / pod rows, mean 1990-2010 "
            "Sharpe %.3f, sd %.3f, z %.2f -> expected best Sharpe from luck alone about %+.2f" % (
                si["n"], si["mean"], si["sd"], si["z"], si["inflation"]))
    out("tuned knobs (7.8 item 4): Curve carry 1 (the hybrid volatility estimator, chosen on the whole book; 7.8 item 3)")
    out("NOT APPLICABLE | Sharpe difference of the Core book with the pod (empty book) | k = 1 flagged share (k = 0 pod) | "
        "weekly-implementation check (no daily far-contract settlements, spec s7) | untouched markets (none held back)")
    s9 = ST.summary(net)
    s7 = ST.summary(net, *ST.EXTRA)
    res["trial"] = {"sr_9010": s9["sr"], "t_9010": s9["t"], "maxdd_9010": s9["maxdd"], "sr_7589": s7["sr"],
                    "turnover": float(ST.cut(bk["turnover"], *ST.DESIGN).mean() * 12)}
    out("B1 SUMMARY | window %d | T1 alpha %s, raw p %s | T2 %s | T3 %s | %s | loss %s" % (
        len(win), "> 0" if t1["alpha"] > 0 else "<= 0", cell(t1["p"], t1["n"], "%.4f"),
        "> 0" if t2["alpha"] > 0 else "<= 0", "PASS" if pl["pass"] else "FAIL", res["status"].upper(),
        "not seen" if res["loss_not_seen"] else "seen"))
    return res


def _r(v, nd):
    return None if v is None or v != v else round(float(v), nd)


def trial_rows(res, engine_version=ENGINE, lseg_lock=LSEG_LOCK):
    """Entry item 9: one 'pod' row (Sharpe columns) and one 'diag' row (the spec s10 falsifier computations)."""
    from gm import config as CF
    st = res.get("status", "?")
    c = dict(CONFIG)
    note = ("TESTING_PROTOCOL 7.6 step 8 Batch B1, register T08; engine %s; %s; LOCK_LSEG_v5 %s; Core book v1 EMPTY "
            "(alpha = mean); window %s; verdict %s" % (engine_version, VERSION, lseg_lock[:16], res.get("window"), st))
    pod = {"trial": "Curve carry B1 (k = 0, LSEG lock v5)", "family": "pod", "hash": CF.cfg_hash(c), "note": note,
           "config": json.dumps(c, sort_keys=True, default=list)}
    t = res.get("trial")
    if t:
        pod.update({"sr_9010": _r(t["sr_9010"], 3), "t_9010": _r(t["t_9010"], 2), "maxdd_9010": _r(t["maxdd_9010"], 3),
                    "sr_7589": _r(t["sr_7589"], 3), "turnover": _r(t["turnover"], 1)})
    cd = dict(c, diag="Curve carry s10 falsifiers")
    diag = {"trial": "Curve carry falsifiers (spec s10, B1)", "family": "diag", "hash": CF.cfg_hash(cd),
            "note": "SPEC_Curve_carry s10 items 1-3, 5 (item 4 not computed); " + note,
            "config": json.dumps(cd, sort_keys=True, default=list)}
    return [pod, diag]
