"""Smoke test of Batch B2 (tools/bbgq/lib/b2_batch.py, job tools/bbgq/jobs/gm_b2_v1.py; gm/CHANGES.md "Batch B2",
2026-11-28) on synthetic panels, invented card inputs and a MOCK LSEG store with INVENTED settlements only (no LSEG,
Bloomberg or FRED value; mocks in tests/b2_mocks.py).

Checks:
  strip     code parse and catalog filter (DS, daily, ok, primary, quarterly ED / FEI only); weights level-neutral and
            equal to the measure's gradient; gate levels; R1 identity with diag_preb.r1; the volatility identity with
            gm.vol.estimate (and the 0.25 screen cannot bind); version positions by hand; the strip-vector cap keeps
            the vector's shape; contract-level costs by hand; returns by hand; the Euribor start after its normals
  cards     E3 by hand; fixed sizes (legs and pairs) by hand; card 4 window costs (entry / exit one-way, roll pro rata
            sums to book.run's monthly charge); held size 0.10 / 0.40; the diag_preb identity for all ten rules
  placebo   identity map = the item; moved Strip scores never land on a month without a strip or a normal (mock with an
            Euribor gap); moved rule directions never hold a market without volatility; card 4 windows stay in their
            year with their length
  seal      values after 2010-12 change nothing; truncation PASS at 2 dates, and FAILS with each planted look-ahead
  report    every line, verdicts, printing rule (no 5+ decimals; small groups count and sign), 13 trial rows
  job       PC layout: 16 lib pins + engine_ref + trial log pass; missing reports -> STOP before any store; a changed b2_batch.py -> STOP
python3 tests/b2_batch_smoke.py      (also run from tests/run_tests.py)
"""
import hashlib
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

import b2_batch as B2  # noqa: E402
import b2_mocks as M  # noqa: E402
import diag_preb as DP  # noqa: E402
from gm import book as BK  # noqa: E402
from gm import config as CF  # noqa: E402
from gm import execution as EX  # noqa: E402
from gm import seal as SL  # noqa: E402
from gm import stats as ST  # noqa: E402
from gm import vol as VM  # noqa: E402

P = lambda s: pd.Period(s, "M")  # noqa: E731


def build(m):
    days = EX.nyse_days(gspc=m["gspc"])
    con = B2.strip_contracts(m["view"])
    contracts = {r: {k: m["view"].daily(s) for k, s in c.items()} for r, c in con.items()}
    T = SL.resolve(SL.DESIGN)
    R, D, gspc, fxv = SL.cut_inputs(T, m["R"], m["D"], m["gspc"], m["fxv"])
    contracts = B2._cut_contracts(contracts, "2010-12-31")
    eps, tb3 = SL.cut_inputs(T, m["lm"][DP.EPS_SID], m["rates"]["TB3MS"])
    sp = B2.strip_prepare(contracts, days)
    inp = B2.card_inputs_view(R, D, gspc, m["ci"], fxv, tb3, eps, days)
    rules = B2.card_rules(inp)
    return {"days": days, "con": con, "contracts": contracts, "sp": sp, "inp": inp, "rules": rules, "R": R, "D": D,
            "gspc": gspc, "fxv": fxv, "eps": eps, "tb3": tb3}


def run(check):
    tmp = tempfile.mkdtemp(prefix="b2_smoke_")
    try:
        _run(check, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _run(check, tmp):
    m = M.inputs()
    b = build(m)
    sp, inp, rules = b["sp"], b["inp"], b["rules"]
    # ------------------------------------------------------------------------------------------------ strip: parse
    check("strip code parse: ED / FEI quarterly with the decade digit; serial and other roots refused",
          B2.strip_delivery("<EDH0^9>") == ("ED", (1990, 3)) and B2.strip_delivery("<FEIZ9^9>") == ("FEI", (1999, 12))
          and B2.strip_delivery("<EDF0^9>") is None and B2.strip_delivery("<FSSH0^9>") is None and
          B2.strip_delivery("<EDM2^0>") == ("ED", (2002, 6)))
    extra = [{"per": "D", "status": "ok", "duplicate_of": "", "series_id": "HP:EDH0^9|CLOSE", "code": "EDH0^9"},
             {"per": "D", "status": "invalid", "duplicate_of": "", "series_id": "DS:<EDH1^9>|Y", "code": "<EDH1^9>"},
             {"per": "M", "status": "ok", "duplicate_of": "", "series_id": "DS:<EDU1^9>|M", "code": "<EDU1^9>"},
             {"per": "D", "status": "ok", "duplicate_of": "x", "series_id": "DS:<EDU2^9>|Z", "code": "<EDU2^9>"}]
    v2 = M.View(m["ed"], m["fei"], m["lm"], extra)
    c2 = B2.strip_contracts(v2)
    check("strip catalog filter: only DS daily ok primary quarterly codes (HP form, invalid, monthly, duplicate refused)",
          c2["ED"] == b["con"]["ED"] and c2["FEI"] == b["con"]["FEI"] and len(b["con"]["ED"]) > 100 and
          len(b["con"]["FEI"]) > 40)
    # ------------------------------------------------------------------------------------------------ weights
    rng = np.random.default_rng(3)
    okw, okg = True, True
    for key in B2.KEYS:
        w = B2.weights(key)
        okw &= abs(w.sum()) < 1e-12
        r = rng.normal(500, 50, 8)
        mm = DP.measures(r)
        okg &= abs(float(w @ r) - mm[key]) < 1e-9
    check("weights: level-neutral (sum 0) and w . r = the measure (S_n, K_n) on random strips", okw and okg)
    check("gate levels: 2 x 0.5 x A (K_n = diag_preb.r1_cost, S_n = 2 / n)",
          all(abs(B2.gate_level(("K", n)) - DP.r1_cost(n)) < 1e-12 for n in range(2, 8)) and
          abs(B2.gate_level(("S", 4)) - 0.5) < 1e-12)
    # ------------------------------------------------------------------------------------------------ R1 identity
    r1 = DP.r1(b["contracts"]["ED"], b["days"])
    badi, mine = B2.strip_identity(sp, r1)
    check("identity (entry 9a): b2's own strip, normals, stale screen and next-day measures give diag_preb.r1's counts",
          not badi and mine["eligible"] == r1["eligible"] > 1000, (badi, mine["eligible"], r1["eligible"]))
    # ------------------------------------------------------------------------------------------------ volatility
    Rd = sp["roots"]["ED"]
    okv, mx = True, 0.0
    for seed in (1, 2, 3):
        q = np.random.default_rng(seed).normal(0, 1, 8)
        Q = np.tile(q, (len(Rd["grid"]), 1))
        s1 = B2.sigma(Rd["mats"], Q)
        xd = (Rd["X"] * q).sum(axis=1, min_count=8)
        xm = (Rd["Mret"] * q).sum(axis=1, min_count=8)
        s2 = VM.estimate(xm.to_frame("q"), CF.CANDIDATE, xd.to_frame("q"))["q"].to_numpy()
        both = np.isfinite(s1) & np.isfinite(s2)
        okv &= bool((np.isfinite(s1) == np.isfinite(s2)).all())
        mx = max(mx, float(np.nanmax(np.abs(s1[both] - s2[both]) / s2[both])))
        okv &= float(np.nanmax(np.abs(xd))) < 0.25
    check("volatility identity (entry 4i): quadratic forms = gm.vol.estimate on the q series (rel diff %.1e); the 0.25 "
          "screen cannot bind" % mx, okv and mx < 1e-9)
    legv = VM.estimate(Rd["Mret"], CF.CANDIDATE, Rd["X"])
    e0 = B2.sigma(Rd["mats"], np.tile(np.eye(8)[2], (len(Rd["grid"]), 1)))
    check("leg-cap volatility of slot 3 = the unit-vector quadratic form", np.nanmax(np.abs(
        legv[2].to_numpy() - e0) / np.where(np.isfinite(e0), e0, 1)) < 1e-9)
    # ------------------------------------------------------------------------------------------------ strip run
    bk = B2.strip_run(sp)
    win = B2.strip_window(bk["net"])
    ed, fei = sp["roots"]["ED"], sp["roots"]["FEI"]
    check("starts: ED 1990-01 (normals from 1981-12 + 60 months), FEI after its 60-month normals (>= 2003-12)",
          ed["start"] == P("1990-01") and fei["start"] is not None and fei["start"] >= P("2003-12"),
          (ed["start"], fei["start"]))
    check("window: first scaled test month about 48 months after 1990-01, last 2010-11, >= 120 months",
          P("1993-06") <= win.index[0] <= P("1994-06") and win.index[-1] == P("2010-11") and len(win) >= 120,
          (win.index[0], win.index[-1], len(win)))
    t = P("2006-06")
    sc = bk["scores"]
    i = fei["grid"].get_loc(t)
    q = {}
    for v, keys in (("A", B2.KEYS_A), ("B", B2.KEYS_B)):
        q[v] = sum(np.nan_to_num(sc.at[t, B2.col("FEI", k)]) * B2.weights(k) for k in keys)
    sA = B2.sigma({k_: v_[i:i + 1] for k_, v_ in fei["mats"].items()}, q["A"][None, :])[0]
    x = 0.40 / sA * q["A"] / 2
    got = bk["pv"]["A"].loc[t, ["FEI|%d" % j for j in range(1, 9)]].to_numpy(dtype=float)
    check("version position by hand (FEI, version A, 2006-06): 0.40 / sigma(q) x q / n_c, n_c = 2",
          np.allclose(got, x, rtol=1e-10, atol=1e-14), (got, x))
    pod = bk["p"].loc[t, ["FEI|%d" % j for j in range(1, 9)]].to_numpy(dtype=float)
    xb = bk["pv"]["B"].loc[t, ["FEI|%d" % j for j in range(1, 9)]].to_numpy(dtype=float)
    check("pod = mean of the two versions", np.allclose(pod, (got + xb) / 2, rtol=1e-12))
    # cap keeps the vector's shape; gross weight
    cols = ["ED|%d" % j for j in range(1, 9)]
    raw = bk["p"][cols].mul(bk["k"], axis=0).mul(bk["s"], axis=0)
    capd = bk["pos"][cols]
    okc = True
    for tt in raw.index[(raw.abs().sum(axis=1) > 0) & capd.notna().all(axis=1)][:200]:
        a, c = raw.loc[tt].to_numpy(dtype=float), capd.loc[tt].to_numpy(dtype=float)
        nz = np.abs(a) > 0
        rat = c[nz] / a[nz]
        okc &= bool(np.allclose(rat, rat[0], rtol=1e-9)) and rat[0] <= 1 + 1e-12
    check("strip-vector cap (E11): one factor for the whole currency vector (level neutrality kept)", okc)
    g = (bk["pos"].abs() * B2.GROSS_W).sum(axis=1)
    check("gross cap 5x at 0.25 / 1.9 per contract never exceeded", float(g.max()) <= 5.0 + 1e-9)
    # costs by hand
    L = pd.DataFrame({"ED|1": [1.0, 1.0, 0.0], "ED|2": [2.0, 3.0, 1.0]}, index=pd.period_range("2000-01", periods=3,
                                                                                               freq="M"))
    cid = pd.DataFrame({"ED|1": [10, 11, 11], "ED|2": [11, 12, 12]}, index=L.index)
    tr = B2.contract_trades(L, cid)
    # t0: c10 +1, c11 +2 -> 3; t1: c10 1->0, c11 2->1, c12 0->3 -> 1 + 1 + 3 = 5; t2: c11 1->0, c12 3->1 -> 1 + 2 = 3
    check("contract-level trades by hand (a strip roll moves notional between contracts)", list(tr) == [3.0, 5.0, 3.0],
          list(tr))
    check("cost per unit 0.125 bp of notional (0.5 bp of rate x 0.25); net = gross - c x cost(t-1)",
          abs(B2.COST_NOTIONAL - 0.125e-4) < 1e-15 and
          np.allclose((bk["gross"] - bk["cost"].shift(1)).dropna(), bk["net"].dropna()))
    # returns by hand
    t = P("1995-03")
    i = ed["grid"].get_loc(t)
    st = ed["strip"][i - 1]
    fd = EX.month_firsts(b["days"])
    hand = (m["ed"][st[2]][fd[t + 1]] - m["ed"][st[2]][fd[t]]) * 0.25 / 100
    check("slot return by hand: contract 3 of the 1995-02 strip from the first NYSE day of 1995-03 to that of 1995-04",
          abs(ed["RE"][i, 2] - hand) < 1e-15)
    # ------------------------------------------------------------------------------------------------ placebo (Strip)
    pl = B2.strip_placebo(sp, win, n=3, sc=bk["scores"])
    ident = B2.strip_run(sp, score_perm={"start": str(win.index[0] - 1), "perm": np.arange(len(win))},
                         sc=bk["scores"])["net"]
    check("Strip placebo: the identity map reproduces the pod", np.allclose(ident.reindex(win.index), win))
    mg = M.inputs(fei_gap=("2006-01-01", "2006-12-31"))
    bg = build(mg)
    spg = bg["sp"]
    bkg = B2.strip_run(spg)
    wg = B2.strip_window(bkg["net"])
    leak = 0
    gap = [P("2006-%02d" % k) for k in range(1, 13)]
    valid = B2.strip_valid(spg)
    for pm in ST.placebo_perms(len(wg), 8, 12, 7):
        rr = B2.strip_run(spg, score_perm={"start": str(wg.index[0] - 1), "perm": pm}, sc=bkg["scores"])
        x = rr["pos"][["FEI|%d" % j for j in range(1, 9)]].reindex(gap)
        leak += int((x.abs().fillna(0) > 0).to_numpy().sum())
        sc_ = rr["scores"]
        leak += int((sc_.notna() & ~valid.reindex(sc_.index).fillna(False)).to_numpy().sum())
    check("Strip placebo mask (CHECK_B1 M1 lesson): moved scores never hold Euribor in a month without its strip, nor "
          "any score on an invalid (root, measure, month)", leak == 0, leak)
    # ------------------------------------------------------------------------------------------------ 1.0.1 M1
    ms = M.inputs()
    for k_, s_ in ms["ed"].items():                 # every ED contract flat 1995-02..1996-02 (stale screen fails)
        msk = (s_.index >= pd.Timestamp("1995-02-01")) & (s_.index <= pd.Timestamp("1996-02-29"))
        if msk.any():
            s_[msk] = s_[msk].iloc[0]
    bs = build(ms)
    sps = bs["sp"]
    bks = B2.strip_run(sps)
    ws = B2.strip_window(bks["net"])
    span = pd.period_range(ws.index[0], ws.index[-1], freq="M")
    flat = ws.index[(bks["gross"].reindex(ws.index) == 0).to_numpy()]
    check("M1 (1.0.1): a stale stretch of the dollar strip leaves the window contiguous (%d months = span %d)" % (
        len(ws), len(span)), len(ws) == len(span) and ws.index[-1] == P("2010-11"), (len(ws), len(span)))
    check("M1: flat months (no contract held) earn gross 0 and net = - cost of the month before (%d flat)" % len(flat),
          len(flat) >= 10 and np.allclose(ws.reindex(flat), -bks["cost"].shift(1).reindex(flat)) and
          float(bks["cost"].reindex(flat - 1).max()) > 0)
    ids = B2.strip_run(sps, score_perm={"start": str(ws.index[0] - 1), "perm": np.arange(len(span))},
                       sc=bks["scores"])["net"]
    check("M1: the identity map over the window's span reproduces the pod", np.allclose(ids.reindex(ws.index), ws))
    lines_s = []
    B2.report_strip(sps, None, lines_s.append, n_placebo=2)
    check("M1: the report prints the flat-month DATA line (contiguous, flat months counted)",
          any(x.startswith("DATA | Strip reversion window") and "interior gaps 0 | contiguous" in x and
              "flat months (no contract held, gross 0) %d" % len(flat) in x for x in lines_s))
    net_g = bks["net"].copy()
    net_g[P("2000-06")] = np.nan                     # a planted interior gap
    orig = B2.strip_run
    B2.strip_run = lambda *a_, **k_: dict(orig(*a_, **k_), net=net_g) if not k_ else orig(*a_, **k_)
    raised = False
    try:
        B2.report_strip(sps, None, lambda x: None, n_placebo=0)
    except B2.WindowGap:
        raised = True
    finally:
        B2.strip_run = orig
    check("M1: an interior gap in the window raises WindowGap (the job STOPs)", raised is True, raised)
    # ------------------------------------------------------------------------------------------------ cards: E3, fixed
    idx = pd.period_range("2000-01", periods=8, freq="M")
    d = pd.Series([0, 1, 1, 1, 0, 1, 1, 0], index=idx, dtype=float)
    r = pd.Series([0.0, 0.0, -0.02, 0.03, 0.0, 0.0, 0.01, 0.0], index=idx)
    f = B2.e3_factor(d, r)
    # run 1: t0 = 01; s = 02: cum -0.02 -> no; s = 03: 0.98 x 1.03 - 1 = 0.0094 > 0 -> full from 03; run 2: t0 = 05;
    # s = 06: 0.01 > 0 -> full from 06
    check("E3 by hand: one third at a run's first month, full once the cumulative return times the direction > 0",
          list(np.round(f, 6)) == [0, 1 / 3, 1 / 3, 1, 0, 1 / 3, 1, 0] or list(f) == [0, 1 / 3, 1 / 3, 1, 0, 1 / 3, 1, 0],
          list(f))
    V = pd.Series([0.1, 0.2, 0.4, 0.4, 0.1, 0.5, 0.5, 0.5], index=idx)
    h = pd.Series([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], index=idx)
    a, hh = B2.fixed_pair(d, V, h)
    check("fixed size by hand: notional 0.40 / V and h fixed at the run's first month",
          list(a) == [0, 2.0, 2.0, 2.0, 0, 0.8, 0.8, 0] and list(hh) == [0, 0.3, 0.3, 0.3, 0, 0.7, 0.7, 0])
    fl = DP.fixed_runs(d, 0.40 / V)
    check("fixed leg (diag_preb fixed_runs) by hand", list(fl) == [0, 2.0, 2.0, 2.0, 0, 0.8, 0.8, 0], list(fl))
    # held size and the k = 1 return
    ru = rules["card 1 R1"]
    rr = B2.rule_run(ru, inp)
    pos = rr["pos"]
    hand = 0.25 * ((pos.shift(1) * inp["R1"][pos.columns]).fillna(0).sum(axis=1) -
                   B2.costs(pos)[0].shift(1).fillna(0))
    check("rule test return = 0.10 / 0.40 x (k = 1 gross - cost(t-1)), book.run costs",
          np.allclose(rr["net"], hand.reindex(rr["net"].index)))
    check("card 1 R1: 16 versions (8 x E1 / E3); card 1 R2 16; R5 8; card 2 2 + 2; card 3 4 + 4; card 4 R1 6, R3 2, "
          "R5 2 (62)", [len(rules[n]["versions"]) for n in B2.RULES] == [16, 16, 8, 2, 2, 4, 4, 6, 2, 2],
          [len(rules[n]["versions"]) for n in B2.RULES])
    # card 4 costs
    r4 = rules["card 4 R1"]
    c4 = B2.card4_run(r4, inp)
    Pd = c4["daily"]
    one = BK.cost_bp("eq_us_spx")[0] / 1e4
    mo = P("1995-11")
    days_m = Pd[Pd.index.to_period("M") == mo]
    full = days_m[days_m != 0]
    if len(full) == len(days_m) and len(days_m):
        roll = float((days_m.abs() * one * 2 * 4 / 12 / len(days_m)).sum())
        check("card 4: a fully held month pays book.run's monthly roll charge pro rata (sum = |pos| x 2 x 4 / 12 x ow)",
              abs(roll - abs(days_m.iloc[0]) * one * 2 * 4 / 12) < 1e-15)
    nxt = Pd.shift(-1).fillna(0)
    tr4 = (nxt - Pd).abs()
    tr4.iloc[0] += abs(Pd.iloc[0])
    mm_ = Pd.index.to_period("M")
    Nm = pd.Series(1, index=Pd.index).groupby(mm_).transform("sum")
    cst = (tr4 * one + Pd.abs() * one * 2 * 4 / 12 / Nm).groupby(mm_).sum()
    diff_ = (c4["net_all"] - B2.window_of(r4, 0.25 * (c4["net_all"] / 0.25)))
    hand4 = 0.25 * cst.reindex(c4["net_all"].index).fillna(0)
    g4 = B2.card4_run(r4, inp, cost_mult=0.0)["net_all"]
    check("card 4 costs by hand: one-way at every entry and exit close, roll pro rata per held day (net = gross - "
          "cost)", np.allclose(g4 - c4["net_all"], hand4) and int(((Pd == 0) & (nxt != 0)).sum()) > 10 and
          abs(float(diff_.abs().sum())) < 1e-12)
    # ------------------------------------------------------------------------------------------------ identity
    idn = B2.identity(inp, rules, m["rates"])
    v2c = DP.card2_rules(inp["ci"], inp["R"], inp["vol"], inp["spx_me"])
    r45 = DP.r4_state(inp["ci"], 4.5).reindex(inp["idx"])
    mock_keep = {nm: sorted([v for v, x in DP.c2d2(v2c[nm], r45).items() if x["keep"]], key=str)
                 for nm in ("card 2 R1", "card 2 R2")}
    check("identity (entry 9b): the eight non-card-2 B2 base layers = diag_preb 1.1.1 positions; full positions keep "
          "signs and held months", all(idn[n][0] for n in B2.RULES if not n.startswith("card 2")),
          {k: v[1] for k, v in idn.items() if not v[0]})
    check("identity: card 2 is flagged exactly when the data's C2-D2 keeps other versions than the registered ones "
          "(mock keeps %s)" % mock_keep, all((not idn[nm][0]) == (mock_keep[nm] != sorted(B2.C2_KEPT[nm], key=str))
                                             for nm in mock_keep))
    keep_saved = {k: list(v) for k, v in B2.C2_KEPT.items()}
    okc2 = True
    for nm, mk in (("card 2 R1", "bd_us_10y"), ("card 2 R2", "eq_us_spx")):
        B2.C2_KEPT[nm] = list(v2c[nm])
        allkeep = {v: {"keep": True} for v in v2c[nm]}
        refp = DP.card2_rule(v2c[nm], allkeep, mk, -1, inp["vol"], inp["idx"])["pos"]
        mine = B2.rule_positions(B2.card_rules(inp)[nm], inp, mode="base")
        okc2 &= B2._close(mine, refp) <= 1e-12
    B2.C2_KEPT.update(keep_saved)
    check("identity, card 2 per version: with all four versions kept, the B2 base = diag_preb.card2_rule", okc2)
    # ------------------------------------------------------------------------------------------------ placebo (rules)
    win1 = rr["net"]
    ru_ = rules["card 1 R1"]
    D_ = pd.DataFrame({i: u["dir"] for i, u in enumerate(ru_["units"])})
    idm = ST.move_rows(D_, np.arange(len(win1)), str(win1.index[0] - 1))
    x = B2.rule_run(ru_, inp, dirs={i: idm[i] for i in D_.columns})["net"]
    check("rule placebo: the identity map reproduces the rule", np.allclose(x, win1))
    # a market whose volatility is missing for a year: moved directions never hold it there
    inp2 = dict(inp)
    vol2 = inp["vol"].copy()
    hole = (vol2.index >= P("1990-01")) & (vol2.index <= P("1990-12"))
    vol2.loc[hole, "bd_us_10y"] = np.nan
    inp2["vol"] = vol2
    rules2 = B2.card_rules(inp2)
    ru2 = rules2["card 1 R1"]
    D2 = pd.DataFrame({i: u["dir"] for i, u in enumerate(ru2["units"])})
    lk = 0
    for pm in ST.placebo_perms(len(win1), 8, 12, 5):
        Dm = ST.move_rows(D2, pm, str(win1.index[0] - 1))
        pp = B2.rule_positions(ru2, inp2, dirs={i: Dm[i] for i in D2.columns})
        lk += int((pp.loc[hole, "bd_us_10y"].abs() > 0).sum())
    check("rule placebo mask: moved directions never hold a market in months without its volatility", lk == 0, lk)
    rng = np.random.default_rng(1)
    mw = B2.moved_windows(r4, rng)
    E = r4["E"]
    posd = {dd: i for i, dd in enumerate(E)}
    okm = all(ne.year == w["entry"].year and (nx <= B2.SEAL) and
              (posd[nx] - posd[ne] == posd[w["exit"]] - posd[w["entry"]] or nx == E[E <= B2.SEAL][-1])
              for w, ne, nx, _d in mw)
    check("card 4 placebo: each window moved inside its entry's calendar year, length in NYSE days kept (cut at the "
          "seal)", okm and len(mw) == len(r4["windows"]))
    # ------------------------------------------------------------------------------------------------ seal, truncation
    ml = M.inputs(late=True)
    bl = build(ml)
    same1 = np.allclose(B2.strip_run(bl["sp"])["net"].dropna(), bk["net"].dropna())
    same2 = all(np.allclose(B2.rule_run(bl["rules"][n], bl["inp"])["net"], B2.rule_run(rules[n], inp)["net"])
                for n in B2.RULES)
    check("seal: values planted after 2010-12 change no Strip or rule return", same1 and same2)

    def bc(plant):
        return lambda T: B2.build_cut(T, b["R"], b["D"], b["gspc"], m["ci"], b["fxv"], b["tb3"], b["eps"],
                                      b["contracts"], plant=plant)
    sink = []
    ok, _r = B2.truncation(bc(None), ["1993-12-31", "2007-06-30"], sink.append)
    check("truncation (entry 10): every B2 path at 2 cut dates, 0 differing cells", ok, sink)
    ok1, _r = B2.truncation(bc("vol_next"), ["2007-06-30"], lambda s: None)
    ok2, _r = B2.truncation(bc("normal_next"), ["2007-06-30"], lambda s: None)
    check("truncation controls: next month's volatility (card 1 R1) and a normal with the next month-end (Strip) FAIL",
          not ok1 and not ok2)
    # ------------------------------------------------------------------------------------------------ report
    lines = []
    res = B2.report(sp, rules, inp, b["R"]["eq_us_spx"], out=lines.append, n_placebo=5)
    txt = "\n".join(lines)
    need = ["DATA | Strip sr_usd ED", "DATA | Strip sr_eur FEI", "WINDOW | Strip reversion", "T1 | Strip reversion",
            "T2 | Strip reversion", "T3 | Strip reversion", "T4 | Strip reversion | not applicable",
            "B2 VERDICT | Strip reversion", "ERAS | Strip reversion", "POD | Strip reversion", "DELAY | Strip reversion",
            "VERSIONS POSITIVE | Strip reversion", "LEG CAP | Strip reversion", "FRAGILITY | Strip reversion",
            "P4 | Strip reversion", "GAPS | Strip reversion", "FALSIFIER 1 |", "FALSIFIER 2 |", "FALSIFIER 3 |",
            "FALSIFIER 4 |", "FALSIFIER 5 / P3 |", "NETTING | shadow book", "NETTING | all ten judged rules",
            "NOT APPLICABLE |", "B2 SUMMARY |"] + ["WINDOW | %s |" % n for n in B2.RULES] + \
           ["B2 VERDICT | %s |" % n for n in B2.RULES]
    miss = [x for x in need if x not in txt]
    check("report: every registered line present", not miss, miss)
    judged = [n for n in B2.RULES if res["items"][n]["status"] in ("Incubator", "Shelved")]
    okj = all(("T1 | %s" % n in txt and "T3 | %s" % n in txt and "FALSIFIER" in txt and "LOSS FLAG | %s" % n in txt)
              for n in judged)
    check("report: every judged rule has T1, T3, falsifier and loss-flag lines (%d judged on the mock)" % len(judged),
          okj and len(judged) >= 3)
    check("report: verdict words only Incubator / Shelved / not judgeable / insufficient data",
          all(v.get("status") in ("Incubator", "Shelved", "not judgeable", "insufficient data")
              for v in res["items"].values()))
    c41 = [x for x in lines if x.startswith("FALSIFIER | card 4 R1")]
    nums = re.findall(r"(?:big|other) years (n (\d+), sign [+-0]|[-\d.]+ \((\d+)\)) \((\d+) days\)", c41[0] if c41
                      else "")
    check("M2 (1.0.1): card 4 R1 falsifier n = calendar months spanned by the held days (value only over >= 60 months; "
          "days printed as a count)", len(nums) == 4 and all(
              (int(g[1]) < 60 if g[1] else int(g[2]) >= 60) for g in nums) and
          all(int(g[1] or g[2]) < int(g[3]) for g in nums), c41)
    c43 = [x for x in lines if x.startswith("FALSIFIER | card 4 R3")]
    check("M2: card 4 R3 falsifier n = months spanned", bool(c43) and re.search(r"\((\d+) days\)", c43[0]) is not None
          and "(%s)" % re.search(r"\((\d+) days\)", c43[0]).group(1) not in c43[0].split("%/yr")[0], c43)
    check("report printing: no number with 5+ decimals", not re.findall(r"\d\.\d{5,}", txt),
          re.findall(r".{40}\d\.\d{5,}.{10}", txt)[:3])
    small = re.findall(r"n (\d+), sign", txt)
    check("report printing: values under 60 months appear as count and sign only", all(int(z) < 60 for z in small))
    rows = B2.trial_rows(res)
    check("trial rows: 13 (11 pod with Sharpe columns where judged, 2 diag); locks in the note",
          len(rows) == 13 and [r_["family"] for r_ in rows].count("pod") == 11 and
          [r_["family"] for r_ in rows].count("diag") == 2 and all(B2.LSEG_LOCK[:16] in r_["note"]
                                                                   for r_ in rows if r_["family"] == "pod"))
    # ------------------------------------------------------------------------------------------------ job
    loc = os.path.join(tmp, "local")
    lib = os.path.join(loc, "lib")
    os.makedirs(lib)
    shutil.copytree(os.path.join(REPO, "gm"), os.path.join(lib, "gm"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    # 1.0.1 C1: the trial log as shipped to the job (42 book / pod rows); gm/trials.csv grows after the run
    shutil.copy(os.path.join(REPO, "tests", "data", "trials_b2_shipped.csv"), os.path.join(lib, "gm", "trials.csv"))
    bq = os.path.join(REPO, "tools", "bbgq")
    for rel in ("lib/gm_engine.py", "lib/bbg_panel.py", "lib/bbgdata.py", "lib/a1_panel.py", "lib/a2_batch.py",
                "lib/diag_a2.py", "lib/diag_preb.py", "lib/card_inputs.py", "lib/b2_batch.py", "live_sources.csv",
                "untouched_markets.csv", "engine_ref.json"):
        shutil.copy(os.path.join(bq, rel), os.path.join(lib, os.path.basename(rel)))
    for f_ in os.listdir(os.path.join(REPO, "tools", "lseg")):
        if f_ in ("lsegdata.py", "lseg_rules.py") or f_.endswith(".csv"):
            shutil.copy(os.path.join(REPO, "tools", "lseg", f_), os.path.join(lib, f_))
    env = dict(os.environ, BBG_WORK=os.path.join(loc, "work"), PYTHONPATH="")
    env.pop("PYTHONDONTWRITEBYTECODE", None)
    job_src = open(os.path.join(bq, "jobs", "gm_b2_v1.py"), encoding="utf-8").read()
    b_sha = hashlib.sha256(open(os.path.join(bq, "lib", "b2_batch.py"), "rb").read()).hexdigest()
    job_src = re.sub(r'"b2_batch.py": "[^"]*"', '"b2_batch.py": "%s"' % b_sha, job_src)   # the build note pins it
    job = os.path.join(tmp, "gm_b2_v1.py")
    open(job, "w", encoding="utf-8").write(job_src)

    def go():
        q_ = subprocess.run([sys.executable, job], cwd=loc, env=env, capture_output=True, text=True, timeout=600)
        return q_.stdout + q_.stderr
    o0 = go()
    check("job (PC layout): gm code, engine_ref, config hashes, 11 lib files, 5 LSEG config lists and the trial-log "
          "digest PASS (18 'PASS lib' lines); no A2 report -> STOP before any store",
          "PASS gm code vs reference" in o0 and o0.count("PASS lib ") == 18 and
          "FAIL A2 report gm_a2_v1.txt: missing" in o0 and "lock id" not in o0, o0[-1500:])
    os.makedirs(os.path.join(loc, "results"))
    import diag_a2_smoke as DS
    open(os.path.join(loc, "results", "gm_a2_v1.txt"), "w").write(DS.a2_report_text())
    open(os.path.join(loc, "results", "gm_core_v1.txt"), "w").write(
        "CORE BOOK V1 EMPTY | no Core candidate passed\nCORE V1 JOB DONE\n")
    o1 = go()
    check("job: A2 and Core reports PASS, no pre-B report -> STOP before any store",
          "PASS A2 report" in o1 and "PASS report gm_core_v1.txt" in o1 and "FAIL report gm_diag_preb_v1.txt" in o1
          and "lock id" not in o1, o1[-900:])
    open(os.path.join(loc, "results", "gm_diag_preb_v1.txt"), "w").write("PRE-B SUMMARY | R1: PASS\nPREB JOB DONE\n")
    o2 = go()
    check("job: a pre-B report without the registered outcomes -> STOP", "FAIL report gm_diag_preb_v1.txt: PRE-B "
          "SUMMARY lacks" in o2 and "lock id" not in o2, o2[-900:])
    preb = open(os.path.join(REPO, "tools", "bbgq", "results", "gm_diag_preb_v1.txt"), encoding="utf-8").read()
    open(os.path.join(loc, "results", "gm_diag_preb_v1.txt"), "w").write(preb)
    o3 = go()
    check("job: the real pre-B report PASSES (entry 9d); no B1 report -> STOP", "PASS report gm_diag_preb_v1.txt" in o3
          and "FAIL report gm_b1_v1.txt: missing" in o3 and "lock id" not in o3, o3[-900:])
    b1 = open(os.path.join(REPO, "tools", "bbgq", "results", "gm_b1_v1.txt"), encoding="utf-8").read()
    open(os.path.join(loc, "results", "gm_b1_v1.txt"), "w").write(b1)
    o4 = go()
    check("job: the real B1 report PASSES (Curve carry SHELVED); no Bloomberg store -> STOP before any value is read",
          "PASS report gm_b1_v1.txt" in o4 and "STOP: checks failed" in o4 and "LSEG store" not in o4, o4[-900:])
    with open(os.path.join(lib, "b2_batch.py"), "a") as f_:
        f_.write("\n# changed\n")
    o5 = go()
    check("job: a changed b2_batch.py stops it at the hash check", "FAIL lib b2_batch.py" in o5 and
          "STOP: lib file differs from the registered build: b2_batch.py" in o5, o5[-600:])
    check("job output: no number with 5+ decimals", not re.findall(r"\d\.\d{5,}", o0 + o1 + o2 + o3 + o4 + o5))
    pyc = [os.path.join(d_, x_) for d_, _s, fs in os.walk(lib) for x_ in fs if x_.endswith(".pyc")]
    check("job: no .pyc written under lib\\", not pyc, pyc[:3])


if __name__ == "__main__":
    fails = []

    def check(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)[:900]))
        if not ok:
            fails.append(name)
    run(check)
    print("B2 SMOKE " + ("PASSED" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
