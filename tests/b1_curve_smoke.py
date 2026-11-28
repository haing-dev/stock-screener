"""Smoke test of Batch B1 = Curve carry (tools/bbgq/lib/b1_curve.py, job tools/bbgq/jobs/gm_b1_v1.py; gm/CHANGES.md
"Batch B1: Curve carry", 2026-11-28) on a MOCK LSEG store with INVENTED contract prices only (no LSEG value, no cache).

Checks:
  table     contract parse (L14 Datastream and L16 HistoricalPricing codes, decade digit), only L14*/L16* files, only
            ok primary price series; Brent prefers the HistoricalPricing form; a listing root (NG) identified through
            lseg_rules.held_contract from its continuous positions; observed expiries mapped to deliveries
  legs      front = nearest delivery >= t + 3 priced at t, far = front + 12 months (by hand); no far -> no pair; the
            backwardation state; stale screen; the calendar exclusion (LTD in the holding month, with a 2-month front)
  returns   spread return = far minus front return of the pair chosen the month before (by hand)
  sizing    eligibility = slow part of the hybrid volatility (>= 36 spread returns); start t0 = first month with >= 8
            eligible; version positions s x 0.40 / v / n by hand; V2 flat in backwardation; pod = mean of versions
  book      block and book scalers recomputed independently; E11 joint cap (legs equal and opposite, |leg| <= cap from the
            front leg's volatility); 5x gross cap; contract-space costs (same contract |change|, roll |a| + |b|) by hand
  tests     T1 = mean against a zero book; placebo identity map = the pod; truncation at 8 dates PASS; values after
            2010-12 change nothing; load_design on a mini lsegdata store gives the same table
  report    every line, verdict, printing rule (no 5+ decimals; small groups count and sign), two trial rows
  job       PC layout: lib checks pass; no reports -> STOP before any store; a changed b1_curve.py -> STOP at the hash
python3 tests/b1_curve_smoke.py      (also run from tests/run_tests.py)
"""
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

import numpy as np
import pandas as pd

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [REPO, os.path.join(REPO, "tools", "bbgq", "lib"), os.path.join(REPO, "tools", "lseg"), HERE]

import b1_curve as BC  # noqa: E402
import lsegdata as LD  # noqa: E402
import lseg_rules as LR  # noqa: E402

P = lambda s: pd.Period(s, "M")  # noqa: E731
MC = "FGHJKMNQUVXZ"
HORIZON = {"PL": 14, "LC": 14}          # months before delivery a contract is priced (default 24)
CONTRACT_ROOTS = {"C": 1975, "W": 1975, "S": 1975, "SB": 1975, "CT": 1975, "SI": 1975, "PL": 1975, "LC": 1975,
                  "CL": 1983, "LCO": 1988}


def last_wd(y, m):
    return LD.last_weekday(dt.date(y, m, 1))


def ric(root, y, m):
    return "%s%s%d^%d" % (root, MC[m - 1], y % 10, (y // 10) % 10)


def spot_path(seed):
    rng = np.random.default_rng(seed)
    g = pd.period_range("1970-01", "2012-12", freq="M")
    lv = np.exp(np.cumsum(rng.normal(0.003, 0.05, len(g))))
    slope = 0.08 * np.sin(np.arange(len(g)) / 17.0 + seed)          # contango / backwardation by era
    return g, lv, slope


def contract_prices(root, y0, seed, stale_at=None, late=False):
    """{delivery (y, m): {Period: price}}, each contract priced from 24 months before delivery to its rule last-trade
    month (cycle months of lseg_rules.CYCLE)."""
    g, lv, slope = spot_path(seed)
    gi = {p: i for i, p in enumerate(g)}
    rng = np.random.default_rng(seed + 100)
    out = {}
    for y in range(y0, 2013):
        for m in range(1, 13):
            if MC[m - 1] not in LR.CYCLE[root]:
                continue
            lt = LR.dates(root, y, m)[0]
            last = P("%d-%02d" % (lt.year, lt.month))
            first = P("%d-%02d" % (y, m)) - 24
            s = {}
            for p in pd.period_range(max(first, P("%d-01" % (y0 - 1))), last, freq="M"):
                if p not in gi:
                    continue
                h = (P("%d-%02d" % (y, m)) - p).n
                v = float(lv[gi[p]] * np.exp(slope[gi[p]] * h / 12) * np.exp(rng.normal(0, 0.003)))
                if h > HORIZON.get(root, 24) or (p > P("2010-12") and not late):
                    continue                     # not yet listed (far contracts of platinum and cattle) / sealed
                s[p] = v
            out[(y, m)] = s
    if stale_at:
        (y, m), p = stale_at
        out[(y, m)][p] = out[(y, m)][p - 1]
    return out


def ng_contracts(seed=91):
    g, lv, slope = spot_path(seed)
    gi = {p: i for i, p in enumerate(g)}
    out = {}
    for y in range(1990, 2013):
        for m in range(1, 13):
            s = {}
            for p in pd.period_range(P("%d-%02d" % (y, m)) - 30, P("%d-%02d" % (y, m)), freq="M"):
                if p < P("1990-04") or p > P("2010-12"):
                    continue
                h = (P("%d-%02d" % (y, m)) - p).n
                s[p] = float(lv[gi[p]] * np.exp(slope[gi[p]] * h / 12))
            out[(y, m)] = s
    return out


def build_mock(late=False, stale=True):
    """-> (cat, long, roots, truth) of a mock store: 10 contract roots (L14 Datastream; Brent L16 HistoricalPricing and
    an L14 Datastream twin with other numbers), NG by continuous positions 1-24 + TR.ExpiryDate c1 / c2, distractors."""
    cat, rows, truth = [], [], {}

    def add(file, fn, code, field, per, s, obs_of, status="ok", dup="", untouched=0):
        sid = "%s:%s|%s" % (fn, code, field)
        if dup:
            sid += "#" + dup
        cat.append({"file": file, "fn": fn, "code": code, "field": field, "per": per, "status": status,
                    "series_id": sid if status == "ok" else "", "duplicate_of": dup, "untouched": untouched})
        if status == "ok":
            for p, v in s.items():
                d = pd.Timestamp(obs_of(p))
                rows.append((sid, per, d, d, float(v), 0))
    for k, (root, y0) in enumerate(CONTRACT_ROOTS.items()):
        st = ((1990, 3), P("1989-12")) if (root == "C" and stale) else None
        cs = contract_prices(root, y0, 10 + k, stale_at=st, late=late)
        truth[root] = cs
        for (y, m), s in cs.items():
            if root == "LCO":
                add("L16b", "HP", ric(root, y, m), "CLOSE", "M", s, lambda p: p.to_timestamp(how="end").normalize())
                add("L14k", "DS", "<%s>" % ric(root, y, m), "X", "M", {p: v * 1.5 for p, v in s.items()},
                    lambda p: last_wd(p.year, p.month))
            else:
                add("L14a", "DS", "<%s>" % ric(root, y, m), "X", "M", s, lambda p: last_wd(p.year, p.month))
    # distractors: an L4 file with a contract code (ignored), an invalid block, a duplicate, a calendar field
    add("L4b", "DS", "<%s>" % ric("C", 1999, 2), "X", "M", {P("1998-06"): 999.0}, lambda p: last_wd(p.year, p.month))
    add("L14a", "DS", "<%s>" % ric("W", 2001, 3), "X", "M", {}, lambda p: p, status="invalid")
    add("L14a", "DS", "<%s>" % ric("S", 2001, 3), "X", "M", {P("2000-06"): 999.0}, lambda p: last_wd(p.year, p.month),
        dup="L14x.1")
    add("L14a", "RD", "<%s>" % ric("SB", 2001, 2), "TR.EXPIRYDATE", "M", {P("2000-06"): 20010227.0},
        lambda p: last_wd(p.year, p.month))
    # NG: continuous positions 1-24 by the registered listing model, observed expiries on c1 / c2
    ng = ng_contracts()
    truth["NG"] = ng
    cser = {n: {} for n in range(1, 25)}
    exp_s = {1: {}, 2: {}}
    for p in pd.period_range("1990-04", "2010-12", freq="M"):
        d = p.to_timestamp(how="end").normalize()
        day = LD.trading_day(d.date(), "US")
        for n in range(1, 25):
            dl = LR.held_contract("NG", n, day)
            if dl is None or p not in ng.get(dl, {}):
                continue
            cser[n][p] = ng[dl][p]
            if n <= 2:
                lt = LR.dates("NG", *dl)[0]
                exp_s[n][p] = float(lt.year * 10000 + lt.month * 100 + lt.day)
    for n, s in cser.items():
        add("L4a", "HP", "NGc%d" % n, "CLOSE", "M", s, lambda p: p.to_timestamp(how="end").normalize())
    for n, s in exp_s.items():
        add("L12", "RD", "NGc%d" % n, "TR.EXPIRYDATE", "M", s, lambda p: p.to_timestamp(how="end").normalize())
    c = pd.DataFrame(cat)
    long = pd.DataFrame(rows, columns=["sid", "per", "obs", "key", "value", "hol"])
    long["obs"] = pd.to_datetime(long["obs"]).astype("datetime64[ns]")
    long["key"] = pd.to_datetime(long["key"]).astype("datetime64[ns]")
    long["hol"] = long["hol"].astype("int8")
    if not late:
        long = long[long["obs"] <= BC.SEAL]
    return c, long.reset_index(drop=True), LD.roots_config(), truth


def write_store(wd, cat, long):
    root = os.path.join(wd, "lseg")
    os.makedirs(os.path.join(root, "design"), exist_ok=True)
    long = long.sort_values(["per", "sid", "obs"], kind="mergesort").reset_index(drop=True)
    long.to_pickle(os.path.join(root, "design", "long.pkl"))
    c = cat.copy()
    for col in LD.CATALOG_COLUMNS:
        if col not in c:
            c[col] = 0 if col.startswith("n_") or col in ("delay_days", "untouched") else ""
    c["untouched"] = c["untouched"].fillna(0).astype(int)
    c = c[LD.CATALOG_COLUMNS]
    c.to_csv(os.path.join(root, "catalog.csv"), index=False)
    man = {"seal_date": "2010-12-31", "workbooks": {}, "config": {},
           "tables": {"design/long.pkl": {"content_sha256": LD.content_sha256(long)}},
           "catalog": {"sha256": LD.sha256_file(os.path.join(root, "catalog.csv"))}}
    json.dump(man, open(os.path.join(root, "manifest.json"), "w"))
    open(os.path.join(root, "LOCK"), "w").write(LD.lock_id_of(man))


def run(check):
    tmp = tempfile.mkdtemp(prefix="b1_smoke_")
    try:
        _run(check, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _run(check, tmp):
    cat, long, roots, truth = build_mock()
    tab = BC.contract_table(cat, long, roots)
    px = tab["px"]
    # ---------------------------------------------------------------- table
    c = px["C"]
    k = BC.mi(1985, 7)
    ok = all(abs(c.at[p, k] - v) < 1e-12 for p, v in truth["C"][(1985, 7)].items())
    check("table: Datastream L14 contract <CN5^8> parsed (decade digit 8 -> 1985), its month-end values equal the "
          "invented ones", ok and k in c.columns)
    check("table: a contract code in a non-L14/L16 file, an invalid block, a duplicate and a TR. date field are ignored",
          BC.mi(1999, 2) not in c.columns and abs(px["S"].reindex(columns=[BC.mi(2001, 3)]).iloc[:, 0]
                                                    .fillna(0).max() - 999.0) > 1 and BC.mi(2001, 2) not in px["SB"])
    lk = BC.mi(1995, 12)
    check("table: Brent prefers the HistoricalPricing form (L16) over the Datastream twin",
          tab["src"]["LCO"][lk] == "HP" and abs(px["LCO"].at[P("1995-01"), lk] - truth["LCO"][(1995, 12)][P("1995-01")])
          < 1e-12)
    ng = px["NG"]
    nk = BC.mi(1998, 5)
    okng = all(abs(ng.at[p, nk] - v) < 1e-12 for p, v in truth["NG"][(1998, 5)].items() if p >= P("1990-04") and
               p in ng.index and pd.notna(ng.at[p, nk]))
    nn = int(ng[nk].notna().sum())
    check("table: NG contract 1998-05 rebuilt from continuous positions by lseg_rules.held_contract equals the invented "
          "contract wherever identified (%d months)" % nn, okng and nn >= 20)
    e = tab["exp"]["NG"]
    check("table: observed NG expiries mapped to their deliveries (c1 / c2 TR.ExpiryDate = the rule day here)",
          len(e) > 100 and all(LR.dates("NG", *BC.ym(d))[0] == v for d, v in e.items()))
    # ---------------------------------------------------------------- legs
    prep = BC.prepare(tab)
    t = P("1986-01")
    i = list(prep["grid"]).index(t)
    T = px["C"]
    avail = [d for d in T.columns if d >= BC.pmi(t) + 3 and pd.notna(T.at[t, d])]
    F = min(avail)
    D = F + 12 if (F + 12) in T.columns and pd.notna(T.at[t, F + 12]) else None
    check("legs: corn 1986-01 front = nearest delivery >= 1986-04 priced (by hand), far = front + 12",
          prep["F"].at[t, "cm_corn"] == F and (D is None or prep["D"].at[t, "cm_corn"] == D) and F == BC.mi(1986, 5))
    Bh = 1.0 if T.at[t, F] > T.at[t, D] else 0.0
    check("legs: backwardation state B = front settles above far", prep["B"].at[t, "cm_corn"] == Bh)
    nofar = [p for p in prep["grid"] if pd.notna(prep["F"].at[p, "cm_platinum"]) and not prep["pair"].at[p, "cm_platinum"]]
    check("legs: a front without a priced 12-month contract gives no pair (platinum months %d)" % len(nofar),
          len(nofar) > 0 and all(pd.isna(prep["D"].at[p, "cm_platinum"]) for p in nofar))
    stl = prep["stale"]["cm_corn"]
    check("legs: the planted equal month-end settlement (corn front 1990-03, at 1989-12) is stale; no score there",
          bool(stl[P("1989-12")]) and pd.isna(BC.scores(prep)[1].at[P("1989-12"), "cm_corn"]) and int(stl.sum()) >= 1)
    check("legs: with the registered front rule (>= 3 months) no calendar exclusion bites on the mock",
          int(prep["cal"].sum().sum()) == 0)
    BC.FRONT_MIN = 2
    try:
        pr2 = BC.prepare(tab)
    finally:
        BC.FRONT_MIN = 3
    tc_ = P("2001-03")
    f2 = pr2["F"].at[tc_, "cm_wti"]
    lt2 = LR.dates("CL", *BC.ym(f2))[0]
    check("legs: the calendar exclusion bites where a leg's last trading day falls in the holding month (WTI with a "
          "2-month front: delivery %s, LTD %s)" % (BC.ym(f2), lt2),
          bool(pr2["cal"].at[tc_, "cm_wti"]) == ((lt2.year, lt2.month) == (2001, 4)) and int(pr2["cal"]["cm_wti"].sum()) > 50)
    # ---------------------------------------------------------------- returns
    t1 = t + 1
    rF = T.at[t1, F] / T.at[t, F] - 1
    rD = T.at[t1, D] / T.at[t, D] - 1
    check("returns: spread return of 1986-02 = far minus front return of the pair chosen at 1986-01 (by hand)",
          abs(prep["rs"].at[t1, "cm_corn"] - (rD - rF)) < 1e-12 and abs(prep["rf"].at[t1, "cm_corn"] - rF) < 1e-12)
    # ---------------------------------------------------------------- sizing
    rs = prep["rs"]["cm_corn"]
    first = rs.dropna().index[35]
    sl = prep["slow"]["cm_corn"]
    check("sizing: eligible (slow part) from the 36th spread return on", pd.notna(sl[first]) and
          pd.isna(sl[rs.dropna().index[34]]))
    ne = prep["slow"].notna().sum(axis=1)
    t0h = ne[ne >= 8].index[0]
    check("sizing: start t0 = first month with >= 8 of 16 eligible (%s)" % t0h, prep["t0"] == t0h)
    sc = BC.scores(prep)
    pv, p = BC.version_positions(prep, sc)
    tt = P("1995-06")
    pr = {}
    for v in (1, 2):
        raw = (sc[v].loc[tt] * 0.40 / prep["vol"].loc[tt]).where(prep["slow"].loc[tt].notna() &
                                                                  prep["volF"].loc[tt].notna())
        pr[v] = raw / raw.notna().sum()
    check("sizing: version positions s x 0.40 / v / n at 1995-06 by hand; V2 zero where backwardated; pod = mean",
          np.allclose(pv[1].loc[tt].fillna(-9), pr[1].fillna(-9)) and np.allclose(pv[2].loc[tt].fillna(-9),
                                                                                    pr[2].fillna(-9)) and
          all(pv[2].at[tt, m] == 0 for m in pv[2].columns if prep["B"].at[tt, m] == 1 and pd.notna(pv[2].at[tt, m]))
          and np.allclose(p.loc[tt].fillna(-9), ((pr[1].fillna(0) + pr[2].fillna(0)) / 2).where(pr[1].notna())
                          .fillna(-9)))
    # ---------------------------------------------------------------- book
    bk = BC.run(prep)
    rb = (p.shift(1) * prep["rs"]).sum(axis=1, min_count=1)
    kk = (1 / (rb.rolling(36, min_periods=24).std() * np.sqrt(12))).shift(1).clip(upper=50)
    tot = p.mul(kk, axis=0).fillna(0)
    act = (rb * kk).notna()
    raw = (tot.shift(1) * prep["rs"].fillna(0)).sum(axis=1).where(act)
    ss = (0.10 / (raw.rolling(36, min_periods=24).std() * np.sqrt(12))).shift(1)
    check("book: block scaler, active months and book scaler recomputed independently",
          np.allclose(bk["k"].fillna(-1), kk.fillna(-1)) and np.allclose(bk["s"].fillna(-1), ss.fillna(-1)) and
          bool((bk["active"] == act).all()))
    L = bk["legs"]
    dcol = [c_ for c_ in L.columns if c_.endswith("|D")]
    fcol = [c_.replace("|D", "|F") for c_ in dcol]
    cap = 0.10 * 0.10 * 3 / prep["volF"]
    okc = np.allclose(L[dcol].fillna(0).values, -L[fcol].fillna(0).values) and bool(
        ((L[dcol].abs().values <= cap.values * (1 + 1e-9)) | (L[dcol].abs().values == 0) |
         np.isnan(L[dcol].values)).all())
    check("book: E11 joint cap, legs equal and opposite, |leg| <= 0.1 x 0.1 x 3 / front-leg vol; %d binding "
          "market-months" % int(bk["bind"].sum().sum()), okc)
    g = L.abs().sum(axis=1)
    check("book: 5x gross cap holds", bool((g.fillna(0) <= 5.0 + 1e-9).all()))
    # contract-space costs by hand on one leg
    leg = "cm_corn|F"
    cid = prep["F"]["cm_corn"]
    mm = [tq for tq in L.index[1:] if pd.notna(L.at[tq, leg]) and pd.notna(L.at[tq - 1, leg]) and L.at[tq, leg] != 0
          and L.at[tq - 1, leg] != 0]
    rolls = [tq for tq in mm if cid[tq] != cid[tq - 1]]
    keeps = [tq for tq in mm if cid[tq] == cid[tq - 1]]
    tr = bk["turnover"]
    one = {c_: 4e-4 for c_ in L.columns}
    one["cm_natgas|D"] = one["cm_natgas|F"] = 6e-4

    def hand(tq):
        s_ = 0.0
        for c_ in L.columns:
            a_, b_ = L.at[tq, c_], L.at[tq - 1, c_]
            if pd.isna(a_) or pd.isna(b_):
                continue
            cc = prep["D" if c_.endswith("|D") else "F"][c_.split("|")[0]]
            same = pd.notna(cc[tq]) and cc[tq] == cc[tq - 1]
            s_ += one[c_] * (abs(a_ - b_) if (same or a_ == 0 or b_ == 0) else abs(a_) + abs(b_))
        return s_
    okt = all(abs(bk["cost"][tq] - hand(tq)) < 1e-12 for tq in (rolls[:5] + keeps[:5]))
    check("book: contract-space costs by hand (%d roll months and %d same-contract months checked; roll = |a| + |b|)" % (
        min(5, len(rolls)), min(5, len(keeps))), okt and len(rolls) >= 3 and len(keeps) >= 3)
    nt = (L.shift(1) * pd.concat([prep["rD"].set_axis(dcol, axis=1), prep["rF"].set_axis(fcol, axis=1)], axis=1))
    gh = nt.sum(axis=1, min_count=1).where(bk["active"] & bk["s"].notna())
    check("book: gross = legs at t-1 x leg returns at t; net = gross - cost(t-1)",
          np.allclose(bk["gross"].fillna(-7), gh.fillna(-7)) and
          np.allclose(bk["net"].fillna(-7), (gh - bk["cost"].shift(1)).fillna(-7)))
    # ---------------------------------------------------------------- tests
    win = BC.window(bk["net"])
    t1r = BC.alpha_zero(win)
    check("T1: alpha against a zero book = the pod's mean (%d window months)" % len(win),
          abs(t1r["alpha"] - win.mean()) < 1e-15 and t1r["beta"] == 0.0 and 0 <= t1r["p"] <= 1)
    ident = np.arange((BC.LAST - win.index[0]).n + 1)
    pn = BC.run(prep, score_perm={"start": str(win.index[0]), "perm": ident})["net"]
    check("T3: the identity date map reproduces the pod exactly (one code path)",
          np.allclose(pn.fillna(-7), bk["net"].fillna(-7)))
    # 1.0.1 M1: on a mock with intermittent pairs (wheat, corn listed 16 months ahead), no placebo position sits on a
    # market-month the pod cannot hold (no priced far leg, stale leg, calendar exclusion)
    HORIZON.update({"W": 16, "C": 16})
    try:
        catG, longG, _rG, _tG = build_mock()
    finally:
        del HORIZON["W"], HORIZON["C"]
    prG = BC.prepare(BC.contract_table(catG, longG, roots))
    bG = BC.run(prG)
    wG = BC.window(bG["net"])
    gaps = int((~prG["pair"]["cm_wheat"] & prG["F"]["cm_wheat"].notna()).loc[wG.index].sum())
    import gm.stats as GST
    perms = GST.placebo_perms((BC.LAST - wG.index[0]).n + 1, n=5, L=12, seed=BC.SEED)
    leak = 0
    for pm in perms:
        rG = BC.run(prG, score_perm={"start": str(wG.index[0]), "perm": pm})
        leak += int(sum((pv_.notna() & ~prG["valid"]).sum().sum() for pv_ in rG["pv"].values()))
        leak += int((rG["p"].notna() & ~prG["valid"]).sum().sum())
    idG = BC.run(prG, score_perm={"start": str(wG.index[0]), "perm": np.arange(len(perms[0]))})["net"]
    check("T3 (1.0.1 M1): on a mock with gaps (%d wheat window months without a pair) no placebo position lands on a "
          "month the pod cannot hold; the identity map still reproduces the pod" % gaps,
          gaps > 20 and leak == 0 and np.allclose(idG.fillna(-7), bG["net"].fillna(-7)), leak)
    pl = BC.placebo(prep, win, n=12)
    check("T3: placebo runs give 12 Sharpe ratios and a share in [0, 1]", len(pl["placebo_sr"]) == 12 and
          0 <= pl["p"] <= 1)
    ok_tr, trr = BC.truncation(cat, long, roots, ("1980-06-30", "1989-06-30", "1998-06-30", "2010-12-31"),
                               out=lambda *_: None, full=(tab, prep, bk))
    check("truncation: the pod rebuilt with observations after T removed equals the full run for months <= T (4 cut "
          "dates on the mock)", ok_tr, {k_: v[0][:3] for k_, v in trr.items()})
    orig = BC.prepare

    def peek(tab_):
        out_ = orig(tab_)
        out_["vol"] = out_["vol"].shift(-1)          # planted look-ahead: next month's volatility
        return out_
    BC.prepare = peek
    try:
        pk = peek(tab)
        bad_tr, _bt = BC.truncation(cat, long, roots, ("1998-06-30",), out=lambda *_: None, full=(tab, pk, BC.run(pk)))
    finally:
        BC.prepare = orig
    check("truncation control: a planted look-ahead (next month's volatility) FAILS the gate", not bad_tr)
    dmi_ = BC.mi(2001, 5)
    check("calendar: the last trading day is the observed expiry where LSEG shows one, else the rule; first notice by "
          "the rule", BC.leg_dates("CL", dmi_, {"CL": {dmi_: dt.date(2001, 4, 17)}})[0] == dt.date(2001, 4, 17) and
          BC.leg_dates("CL", dmi_, {})[0] == LR.dates("CL", 2001, 5)[0] and
          BC.leg_dates("C", BC.mi(2001, 5), {})[1] == LR.dates("C", 2001, 5)[1] is not None)
    catL, longL, _r, _t = build_mock(late=True)
    tabL = BC.contract_table(catL, longL, roots)
    bL = BC.run(BC.prepare(tabL))
    check("seal: observations dated after 2010-12-31 change nothing", np.allclose(bL["net"].fillna(-7),
                                                                                   bk["net"].fillna(-7)))
    wd = os.path.join(tmp, "work")
    write_store(wd, cat, long)
    lid, why = BC.lseg_lock_of(wd)
    c2, l2, lk2, _c = LD.load_design(wd, allow_untouched=False)
    tab2 = BC.contract_table(c2, l2, roots)
    same = all(np.allclose(tab2["px"][r].fillna(-7).values, tab["px"][r].fillna(-7).values) for r in tab["px"])
    check("store: lseg_lock_of reads the lock first; load_design on a mini lsegdata store gives the same table",
          lid == lk2 and why == "ok" and same)
    # ---------------------------------------------------------------- report
    lines = []
    spx = pd.Series(np.random.default_rng(5).normal(0.005, 0.04, len(prep["grid"])), index=prep["grid"])
    blocks = {"carry": spx * 0.3 + 0.01, "trend": -spx}
    res = BC.report(prep, spx=spx, blocks=blocks, out=lines.append, n_placebo=20)
    txt = "\n".join(lines)
    need = ("WINDOW |", "T1 |", "T2 |", "T3 |", "T4 | not applicable", "B1 VERDICT |", "ERAS |", "POD |", "DELAY |",
            "VERSION | V1", "VERSION | V2", "VERSIONS POSITIVE", "BY CLASS", "LEG CAP |", "FRAGILITY |", "P4 |",
            "OVERLAP | correlation with Carry", "OVERLAP | correlation with Trend", "FALSIFIER 1", "FALSIFIER 2",
            "FALSIFIER 3", "FALSIFIER 4 | not computed", "FALSIFIER 5 / P3", "tuned knobs", "NOT APPLICABLE",
            "B1 SUMMARY", "DATA | cm_corn C")
    miss = [n for n in need if n not in txt]
    check("report: every registered line printed", not miss, miss)
    check("report: verdict is Incubator or Shelved (window >= 120 on the mock)", res["status"] in ("Incubator",
                                                                                                   "Shelved"))
    check("report printing: no number with 5+ decimals", not re.findall(r"\d\.\d{5,}", txt),
          re.findall(r".{30}\d\.\d{5,}", txt)[:3])
    small = [x for x in lines if re.search(r"n (\d+), sign", x)]
    check("report printing: values under 60 months appear as count and sign only",
          all(int(m) < 60 for x in small for m in re.findall(r"n (\d+), sign", x)))
    tr_ = res["trial"]
    check("trial rows (1.0.1 M2): a column over fewer than 60 months is empty (mock: 1975-89 has %d window months)" %
          tr_["n_7589"], (tr_["sr_7589"] is None) == (tr_["n_7589"] < 60) and (tr_["sr_9010"] is None) ==
          (tr_["n_9010"] < 60) and tr_["n_7589"] < 60)
    rows_ = BC.trial_rows(res)
    check("trial rows: one pod row with Sharpe columns, one diag row without; LSEG lock in the note",
          [r["family"] for r in rows_] == ["pod", "diag"] and "sr_9010" in rows_[0] and "sr_9010" not in rows_[1] and
          BC.LSEG_LOCK[:16] in rows_[0]["note"])
    # ---------------------------------------------------------------- the job in the PC layout
    loc = os.path.join(tmp, "local")
    lib = os.path.join(loc, "lib")
    os.makedirs(lib)
    shutil.copytree(os.path.join(REPO, "gm"), os.path.join(lib, "gm"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    # the trial log as shipped to the job (gm/trials.csv grew after the run: the B1 rows, 2d13f47; the job pins 41)
    shutil.copy(os.path.join(REPO, "tests", "data", "trials_b1_shipped.csv"), os.path.join(lib, "gm", "trials.csv"))
    bq = os.path.join(REPO, "tools", "bbgq")
    for rel in ("lib/gm_engine.py", "lib/bbg_panel.py", "lib/bbgdata.py", "lib/a1_panel.py", "lib/a2_batch.py",
                "lib/diag_a2.py", "lib/b1_curve.py", "live_sources.csv", "untouched_markets.csv", "engine_ref.json"):
        shutil.copy(os.path.join(bq, rel), os.path.join(lib, os.path.basename(rel)))
    for f_ in os.listdir(os.path.join(REPO, "tools", "lseg")):
        if f_ in ("lsegdata.py", "lseg_rules.py") or f_.endswith(".csv"):
            shutil.copy(os.path.join(REPO, "tools", "lseg", f_), os.path.join(lib, f_))
    env = dict(os.environ, BBG_WORK=os.path.join(loc, "work"), PYTHONPATH="")
    env.pop("PYTHONDONTWRITEBYTECODE", None)
    job_src = open(os.path.join(bq, "jobs", "gm_b1_v1.py"), encoding="utf-8").read()
    b_sha = hashlib.sha256(open(os.path.join(bq, "lib", "b1_curve.py"), "rb").read()).hexdigest()
    job_src = re.sub(r'"b1_curve.py": "[^"]*"', '"b1_curve.py": "%s"' % b_sha, job_src)   # the build note pins it
    job = os.path.join(tmp, "gm_b1_v1.py")
    open(job, "w", encoding="utf-8").write(job_src)

    def go():
        q = subprocess.run([sys.executable, job], cwd=loc, env=env, capture_output=True, text=True, timeout=600)
        return q.stdout + q.stderr
    o0 = go()
    check("job (PC layout): gm code, engine_ref, config hashes, 9 lib files, 5 LSEG config lists and the trial-log digest "
          "PASS (16 'PASS lib' lines); no A2 report -> STOP before any store", "PASS gm code vs reference" in o0 and
          o0.count("PASS lib ") == 16 and "FAIL A2 report gm_a2_v1.txt: missing" in o0 and "lock id" not in o0,
          o0[-1200:])
    os.makedirs(os.path.join(loc, "results"))
    import diag_a2_smoke as DS
    open(os.path.join(loc, "results", "gm_a2_v1.txt"), "w").write(DS.a2_report_text())
    open(os.path.join(loc, "results", "gm_core_v1.txt"), "w").write(
        "CORE BOOK V1 EMPTY | no Core candidate passed\nCORE V1 JOB DONE\n")
    o1 = go()
    check("job: A2 and Core book v1 reports PASS, no pre-B report -> STOP before any store",
          "PASS A2 report" in o1 and "PASS Core book v1 report" in o1 and "FAIL pre-B report" in o1 and
          "lock id" not in o1, o1[-900:])
    open(os.path.join(loc, "results", "gm_diag_preb_v1.txt"), "w").write("PRE-B SUMMARY | x\nPREB JOB DONE\n")
    o2 = go()
    check("job: pre-B report PASS; no Bloomberg store -> STOP before any value is read (LSEG not opened)",
          "PASS pre-B report" in o2 and "STOP: checks failed" in o2 and "LSEG store" not in o2, o2[-900:])
    with open(os.path.join(lib, "b1_curve.py"), "a") as f_:
        f_.write("\n# changed\n")
    o3 = go()
    check("job: a changed b1_curve.py stops it at the hash check", "FAIL lib b1_curve.py" in o3 and
          "STOP: lib file differs from the registered build: b1_curve.py" in o3, o3[-600:])
    check("job output: no number with 5+ decimals", not re.findall(r"\d\.\d{5,}", o0 + o1 + o2 + o3))
    pyc = [os.path.join(d_, x) for d_, _s, fs in os.walk(lib) for x in fs if x.endswith(".pyc")]
    check("job: no .pyc written under lib\\", not pyc, pyc[:3])


if __name__ == "__main__":
    fails = []

    def check(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)[:600]))
        if not ok:
            fails.append(name)
    run(check)
    print("B1 SMOKE " + ("PASSED" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
