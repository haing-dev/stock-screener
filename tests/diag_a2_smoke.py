"""Smoke test of the diagnostics after A2 (tools/bbgq/lib/diag_a2.py, job tools/bbgq/jobs/gm_diag_v1.py; gm/CHANGES.md
"Diagnostics after A2", 2026-11-27) on SYNTHETIC panels and MOCK Bloomberg stores only (no cache, no market data).

Checks:
  D1   PCA first-factor share on streams with a known common factor; 373 windows; the P&L definition
  D2   the rebuild equals book.run's positions; constant volatility and scalers give a non-signal share of 0;
       constant scores give 1 (and a scores-held share of 1); the gate is 'both eras >= 0.20'
  D3   a planted higher forward volatility opens the split, none keeps it closed; state months end at 2009-12
  D4   fall and age equal a hand computation; five states; bad months = 6 windows + worst fifth
  D5   delay 0 equals the pod alone; the gate is the registered inequality
  D6   nw_ols's intercept t equals gm.stats.nw_alpha_t; z and the gate
  X2   income + price = total; the gate sign
  M1   the two-market P4 with one market equals a2_batch.p4; a known two-market beta is removed
  falsifiers  theme parts add to the held Economic trend position exactly
  seal values dated after 2010-12 change nothing; printing: no planted value, no 5+ decimals, every value printed
       with its month count has >= 60 months; facts parser and as-run check; trial-row digest (C7); trial rows
  job  in the PC layout: no A2 report -> STOP before the store; a non-LOCK_v2 store -> STOP before any value; a changed
       diag_a2.py, engine_ref.json or book row of the trial log -> STOP; an appended diag row does not stop it
python3 tests/diag_a2_smoke.py      (also run from tests/run_tests.py)
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

import numpy as np
import pandas as pd

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path[:0] = [REPO, os.path.join(REPO, "tools", "bbgq", "lib"), os.path.dirname(os.path.abspath(__file__))]

import a2_batch as A2  # noqa: E402
import a2_batch_smoke as S2  # noqa: E402
import diag_a2 as DG  # noqa: E402
from gm import book as B  # noqa: E402
from gm import config as CF  # noqa: E402
from gm import execution as EX  # noqa: E402
from gm import stats as ST  # noqa: E402

THEMES = ("inflation", "trade", "monetary", "risk")


def themes_for(S, seed=4):
    """Synthetic theme scores whose mean is the econ score E (E replaced by that mean, as econ_versions defines it)."""
    rng = np.random.default_rng(seed)
    E = S["E"]
    ET = {}
    for t in THEMES[:3]:
        ET[t] = pd.DataFrame(np.tanh(rng.normal(0, 0.5, E.shape)), index=E.index, columns=E.columns).where(E.notna())
    ET["risk"] = (4 * E - ET["inflation"] - ET["trade"] - ET["monetary"]).clip(-1, 1)
    ET["risk"] = ET["risk"].mask(pd.DataFrame(rng.random(E.shape) < 0.1, index=E.index, columns=E.columns))
    n = sum(ET[t].notna().astype(int) for t in THEMES)
    S2_ = dict(S)
    S2_["E"] = (sum(ET[t].fillna(0) for t in THEMES) / n.where(n > 0)).where(n >= 2)
    return S2_, ET


def a2_report_text(book=None, pods=None, p4=None, verdict="FAIL", done=True, pid=DG.A1_PANEL_ID):
    book = book or {"k1": 1.439, "k0": 1.481, "d1": 1.064}
    pods = pods or {"trend": (1.19, 432), "econ": (0.53, 432), "carry": (1.07, 432), "value": (0.15, 345)}
    p4 = p4 or (1.39, 1.34, 396)
    L = ["=== gm_a2_v1 ===", "PASS A1 PANEL ID %s | registered %s" % (pid, pid)]
    for tm in ("k1", "k0", "d1"):
        L.append("BOOK | incumbent | %s | costs x1 | 1975-2010 | 432 | %.3f | 15.07 | 10.47 | -19.0 | -0.42 | 1.37" % (
            tm, book[tm]))
        L.append("BOOK | incumbent | %s | costs x2 | 1975-2010 | 432 | 9.999 | 1 | 1 | -1 | 0 | 1" % tm)
        L.append("BOOK | challenger | %s | costs x1 | 1975-2010 | 432 | 8.888 | 1 | 1 | -1 | 0 | 1" % tm)
    for p in ("trend", "econ", "carry", "value"):
        L.append("POD | incumbent | %s | %.2f (%d) | 1.00 (180) | 1.00 (252)" % (p, pods[p][0], pods[p][1]))
        L.append("POD | challenger | %s | 7.77 (432) | 1.00 (180) | 1.00 (252)" % p)
    L.append("POD | incumbent | carry v1 | 0.88 (432) | 0.76 (180) | 0.96 (252)")
    L.append("P4 | incumbent | book %.2f (%d) | specific %.2f (%d)" % (p4[0], p4[2], p4[1], p4[2]))
    L.append("P4 | challenger | book 6.66 (396) | specific 6.55 (396)")
    L.append("A2 VERDICT %s | H1 lb95 -0.165 <= -0.10 | H3 pass | A2-final book = %s (%s) | the incumbent stays" % (
        verdict, DG.FINAL_NAME if verdict == "FAIL" else CF.A2_CHALLENGER["name"],
        DG.FINAL_HASH if verdict == "FAIL" else DG.CFG_HASHES["A2_CHALLENGER"]))
    if done:
        L.append("A2 JOB DONE")
    return "\n".join(L) + "\n"


def run(check):
    tmp = tempfile.mkdtemp(prefix="diag_smoke_")
    try:
        _run(check, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _run(check, tmp):
    R, D, S0, gspc = S2.scenario()
    S, ET = themes_for(S0)
    lines = []
    res = DG.report(R, D, S, gspc, out=lines.append, ET=ET)
    txt = "\n".join(lines)
    cfg = CF.A1_INCUMBENT
    days = EX.nyse_days(gspc=gspc)
    bk = DG.book_k1(R, D, S, days, cfg)

    # ---- D1
    rng = np.random.default_rng(1)
    idx = pd.period_range("1960-01", "2010-12", freq="M")
    f = rng.normal(0, 1, len(idx))
    streams = pd.DataFrame({"eq_%d" % i if i < 5 else "fx_%d" % i: f + rng.normal(0, 1, len(idx)) for i in range(10)},
                           index=idx)
    pod = streams.mean(axis=1)
    r1 = DG.d1(streams, pod)
    check("D1: 373 windows (60 months ending 1979-12..2010-12); first-factor share on 10 streams with correlation 0.5 "
          "is about (1 + 9 x 0.5) / 10 = 0.55; loadings positive", r1["windows"] == 373 and
          abs(r1["share"] - 0.55) < 0.06 and r1["class_loading"]["EQ"][0] > 0.5 and r1["markets_min"] == 10, r1)
    fam, vol, score = DG.trend_parts(R, D, S, cfg)
    allm, mk = DG.trend_markets(fam)
    pnl = DG.trend_pnl(score, vol, bk["R_earn"], mk)
    k, t = mk[0], pd.Period("1995-06", "M")
    direct = float(np.clip(score.at[t - 1, k], -1, 1) * 0.40 / vol.at[t - 1, k] * bk["R_earn"].at[t, k])
    check("D1: P&L = clip(score(t-1)) x 0.40 / vol(t-1) x R1(t) (one market-month by hand); cm_aqr_ew excluded",
          abs(pnl.at[t, k] - direct) < 1e-15 and "cm_aqr_ew" not in mk, (pnl.at[t, k], direct))

    # ---- D2
    rb = DG.rebuild(R, D, S, cfg)
    r2 = res["D2"]
    check("D2: the rebuild equals book.run's positions (diff 0, same missing pattern) and is printed PASS",
          r2["rebuild_diff"] <= 1e-12 and r2["rebuild_missing"] == 0 and
          any(x.startswith("D2 | rebuild") and x.endswith("PASS") for x in lines), r2["rebuild_diff"])
    rc = dict(rb)
    terms = []
    one = pd.DataFrame(1.0, index=R.index, columns=R.columns)
    for f_, c_, p_, k_, fw_ in rb["terms"]:
        q = p_ * rb["vol"][p_.columns]
        terms.append((f_, c_, q, pd.Series(1.0, index=k_.index).where(k_.notna()), fw_))
    rc["terms"], rc["vol"] = terms, one.where(rb["vol"].notna())
    rc["s"] = pd.Series(1.0, index=rb["s"].index).where(rb["s"].notna())
    rc["cap"] = rb["cap"] * 0 + 1e9
    tot = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    for _f, _c, q, k1, fw_ in terms:
        sc = q.mul(k1, axis=0) * fw_
        tot[sc.columns] = tot[sc.columns].add(sc.fillna(0), fill_value=0)
    rc["pos"] = rc["finish"](tot, rc["s"], rc["cap"])
    c0 = DG.d2(rc, rc["pos"])
    check("D2: constant volatility and scalers -> non-signal share 0 in both eras (all trading is signal trading)",
          all(abs(v["share"]) < 1e-12 for v in c0["eras"].values()), c0["eras"])
    rs = dict(rb)
    terms2 = []
    for f_, c_, p_, k_, fw_ in rb["terms"]:
        q = p_ * rb["vol"][p_.columns]
        qc = pd.DataFrame(np.repeat(q.loc[pd.Period("1980-06", "M")].values[None, :], len(q), 0), index=q.index,
                          columns=q.columns).where(q.notna())
        terms2.append((f_, c_, qc / rb["vol"][p_.columns], k_, fw_))
    rs["terms"] = terms2
    tot = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    for _f, _c, p_, k_, fw_ in terms2:
        sc = p_.mul(k_, axis=0) * fw_
        tot[sc.columns] = tot[sc.columns].add(sc.fillna(0), fill_value=0)
    rs["pos"] = rs["finish"](tot, rs["s"], rs["cap"])
    c1 = DG.d2(rs, rs["pos"])
    e2 = c1["eras"]["1990-2010"]
    check("D2: constant scores -> non-signal share 1 and scores-held share 1 (all trading is from volatilities and "
          "scalers), gate OPEN", abs(e2["share"] - 1) < 1e-9 and abs(e2["scores_share"] - 1) < 1e-9 and c1["open"],
          c1["eras"])
    check("D2 gate: open only if both eras >= 0.20", r2["open"] == all(v["share"] >= 0.20 for v in r2["eras"].values()))
    cd, cdd = DG.cost_drag(bk)
    check("D2 cost drag: per-market costs sum to the book's cost", cdd < 1e-12, cdd)
    k = "fx_jpy"
    pos_ = bk["pos"]
    c_ = (pos_[k].diff().abs() * B.cost_bp(k)[0] / 1e4).fillna(0) + \
        (pos_[k].abs() * B.cost_bp(k)[0] / 1e4 * 2 * B.cost_bp(k)[1] / 12).fillna(0)
    held_ = ((pos_[k].abs() > 0) & pos_[k].notna()).shift(1, fill_value=False)
    xx_ = c_.shift(1)[held_.values].loc["1975-01":"2010-12"]
    check("D2 cost drag (W2): a decision month's cost is charged in the next month, months 1975-01..2010-12 with a held "
          "position", abs(cd[k][0] - xx_.mean() * 12 * 1e4) < 1e-9 and cd[k][1] == len(xx_), (cd[k], len(xx_)))
    p2 = rb["pos"].copy()
    p2.loc[pd.Period("2010-12", "M")] = p2.loc[pd.Period("2010-12", "M")] * 3.0
    rb2 = dict(rb, pos=p2)
    c2_ = DG.d2(rb2, p2)
    check("D2 (W1): the 2010-12 decision is not a trade month (tripling its positions changes no era share)",
          DG.D2_ERAS[-1][2] == "2010-11" and all(abs(c2_["eras"][e]["share"] - r2["eras"][e]["share"]) < 1e-12
                                                 for e in r2["eras"]), (c2_["eras"], r2["eras"]))
    Ralt = R.copy()
    Ralt["cm_cocoa"] = R["cm_gold"]
    try:
        DG.rebuild(Ralt, D, S, cfg)
        refused = False
    except ValueError:
        refused = True
    check("D2 (W5): the rebuild refuses a panel with an alternative-commodity column", refused)
    orig_rebuild = DG.rebuild

    def broken(*a, **kw):
        out = orig_rebuild(*a, **kw)
        out["pos"] = out["pos"] * 1.001
        return out
    DG.rebuild = broken
    try:
        fl = []
        rf = DG.report(R, D, S, gspc, out=fl.append, ET=ET)
    finally:
        DG.rebuild = orig_rebuild
    gl = [x for x in fl if x.startswith("D2 GATE")]
    check("D2 (M2): a failed rebuild prints FAIL and 'not gated', and the recorded outcome is not gated (not closed)",
          any(x.startswith("D2 | rebuild") and x.endswith("FAIL") for x in fl) and
          gl == ["D2 GATE | not gated (rebuild FAIL) | no A3 buffer item decision"] and
          rf["gates"]["D2"] == "not gated (rebuild FAIL)" and "D2: not gated" in fl[-1], (gl, rf["gates"]["D2"]))

    # ---- D3
    rng = np.random.default_rng(3)
    ix = pd.period_range("1975-01", "2009-12", freq="M")
    st = pd.Series(rng.random(len(ix)) < 0.3, index=ix)
    fv = pd.Series(0.10 + rng.normal(0, 0.01, len(ix)), index=ix)
    hi = DG.d3_split(fv + 0.04 * st.astype(float), st)
    lo = DG.d3_split(fv, st)
    check("D3: a planted +4 points in the named state opens the split; no difference keeps it closed",
          hi["open"] and abs(hi["diff"] - 0.04) < 0.005 and not lo["open"], (hi, lo))
    r3 = res["D3"]
    d3l = [x for x in lines if x.startswith("D3 | (")]
    sa_, sb_ = r3["corr"], r3["trend"]
    small_b = min(sb_["n_state"], sb_["n"] - sb_["n_state"]) < 60
    check("D3 (M1): a split with a group under 60 months prints its difference and bound as sign only; a split with "
          "both groups >= 60 prints them in points; empty resamples printed",
          small_b and "difference sign " in d3l[1] and "bound sign " in d3l[1] and "pts" not in d3l[1] and
          min(sa_["n_state"], sa_["n"] - sa_["n_state"]) >= 60 and d3l[0].count(" pts") == 2 and
          all("resamples without a state or other month" in x for x in d3l), d3l)
    tiny = pd.Series(False, index=ix)
    tiny.iloc[::20] = True
    sm = DG.d3_split(fv + 0.04 * tiny.astype(float), tiny)
    check("D3 (W6): a 21-month state is gated on full precision and counts its empty resamples",
          sm["n_state"] == 21 and sm["open"] and sm["empty"] >= 0, sm)
    check("D3: state months end at 2009-12", r3["last"] is not None and r3["last"] <= "2009-12", r3["last"])
    fvb = DG.forward_vol(bk["net"])
    t = pd.Period("1990-03", "M")
    w = bk["net"].loc[t + 1:t + 12].values
    check("D3: forward volatility = std of the next 12 months x sqrt(12)",
          abs(fvb[t] - np.std(w, ddof=1) * np.sqrt(12)) < 1e-15)

    # ---- D4
    x = pd.Series([0.0] * 30 + [-0.03, -0.03, 0.01, -0.15, 0.02], index=pd.period_range("1980-01", periods=35,
                                                                                       freq="M"))
    fs = DG.fall_states(x)
    lv = (1 + x).cumprod()
    tt = x.index[-1]
    hi_ = lv.loc[tt - 23:tt].max()
    check("D4: fall from the 24-month high and age by hand; states", abs(fs["fall"].iloc[-1] - (1 - lv.iloc[-1] / hi_))
          < 1e-15 and fs["age"].iloc[-1] == 5 and fs["state"].iloc[-1] == ">15% old" and
          fs["state"].iloc[31] == "5-15% young" and fs["state"].iloc[29] == "<5%", str(fs.tail(6)))
    r4 = res["D4"]
    wins = DG.design_windows()
    sp = ST.cut(R["eq_us_spx"], *DG.WIN)
    bad = sp <= np.percentile(sp.values, 20)
    for a, b in wins.values():
        bad[(bad.index >= pd.Period(a, "M")) & (bad.index <= pd.Period(b, "M"))] = True
    check("D4 crisis set: the six design stress windows + the worst fifth of eq_us_spx months", len(wins) == 6 and
          r4["bad_n"] == int(bad.sum()), (len(wins), r4["bad_n"], int(bad.sum())))
    ty, nty = r4["sp"]["trend"]["5-15% young"]
    td, ntd = r4["sp"]["trend"][">15% pooled"]
    check("D4 Trend gate = (young 5-15% mean < 0 and >15% mean > 0, cells >= 6 months)",
          r4["trend_open"] == (nty >= 6 and ntd >= 6 and ty < 0 and td > 0))
    c = r4["contribs"]["trend"]
    sel = r4["sp"]["trend"]["<5%"]
    stt = DG.fall_states(R["eq_us_spx"])["state"]
    xx = c.reindex(stt.index)[(stt == "<5%").values].loc["1975-01":"2010-12"].dropna()
    check("D4: the <5% Trend cell mean is a direct computation", abs(sel[0] - xx.mean()) < 1e-15 and sel[1] == len(xx))

    # ---- D5
    r5 = res["D5"]
    pe = ST.cut(DG.pod_book(R, D, S, days, cfg, [("econ", "*", "*")])["net"], *DG.WIN)
    check("D5: delay 0 at k = 1 equals the pod alone (A2's convention); gate = Sharpe(3) < 0.5 x Sharpe(0)",
          abs(r5["k1"][0][0] - ST.sharpe(pe)) < 1e-12 and r5["slow"] == (r5["k1"][3][0] < 0.5 * r5["k1"][0][0]))
    p3 = DG.pod_book(R, D, S, days, cfg, [("econ", "*", "*")], delay=3)
    p0 = DG.pod_book(R, D, S, days, cfg, [("econ", "*", "*")])
    gr = (p0["pos"].shift(4) * p0["R_earn"]).sum(axis=1, min_count=1)
    tt = pd.Period("1999-05", "M")
    check("D5: delay d = positions earn 1 + d months after the decision (gross, one month by hand)",
          abs(p3["gross"][tt] - gr[tt]) < 1e-12, (p3["gross"][tt], gr[tt]))

    # ---- D6
    rng = np.random.default_rng(6)
    xv, yv = rng.normal(1, 0.3, 21), None
    yv = 0.7 * xv + rng.normal(0, 0.1, 21)
    sl, se, b0, se0 = DG.nw_ols(yv, xv, 2)
    nwt = ST.nw_alpha_t(pd.Series(yv), pd.Series(xv), lags=2) if len(yv) >= 36 else None
    yy = np.tile(yv, 2)
    xxx = np.tile(xv, 2)
    sl2, se2, b02, se02 = DG.nw_ols(yy, xxx, 2)
    nwt = ST.nw_alpha_t(pd.Series(yy), pd.Series(xxx), lags=2)
    check("D6: nw_ols intercept t equals gm.stats.nw_alpha_t (same sandwich); slope recovered",
          abs(b02 / se02 - nwt) < 1e-9 and abs(sl - 0.7) < 0.15, (b02 / se02, nwt, sl))
    r6 = res["D6"]
    e1, e2_ = r6["eras"]["1975-89"], r6["eras"]["1990-2010"]
    check("D6: z = (slope 1990-2010 - slope 1975-89) / sqrt(se1^2 + se2^2); gate |z| < 2; 15 and 21 years",
          abs(r6["z"] - (e2_["slope"] - e1["slope"]) / np.sqrt(e1["se"] ** 2 + e2_["se"] ** 2)) < 1e-12 and
          r6["open"] == (abs(r6["z"]) < 2) and e1["n"] == 15 and e2_["n"] == 21, r6)

    # ---- X2
    rx = res["X2"]
    check("X2: income + price = total exactly per leg; gate = price part <= 0",
          all(v["exact"] < 1e-15 and v["paid_by_income"] == (v["price"] <= 0) for v in rx.values()), rx)
    pos = bk["fam_pos"]["value"]
    cols = [k for k in pos.columns if k.startswith("fx_")]
    tot, inc, pri, cov = DG.income_split(pos, cols, S["C"], bk["R_earn"])
    tt = pd.Period("2001-03", "M")
    hand = float((pos[cols].loc[tt - 1] * S["C"][cols].loc[tt - 1] / 12).sum())
    check("X2: income = held position(t-1) x carry(t-1) / 12 (one month by hand)", abs(inc[tt] - hand) < 1e-15)

    # ---- M1
    rng = np.random.default_rng(8)
    ixm = pd.period_range("1975-01", "2010-12", freq="M")
    m1_ = pd.Series(rng.normal(0.005, 0.045, len(ixm)), index=ixm)
    m2_ = pd.Series(rng.normal(0.002, 0.02, len(ixm)), index=ixm)
    r = 0.4 * m1_ - 0.8 * m2_ + pd.Series(rng.normal(0.004, 0.01, len(ixm)), index=ixm)
    wa = A2.p4(r, m1_)
    wb = DG.p4_multi(r, pd.DataFrame({"m1": m1_}))
    wc = DG.p4_multi(r, pd.DataFrame({"m1": m1_, "m2": m2_}))
    check("M1: one-market p4_multi equals a2_batch.p4; first value 1978-01",
          float((wa - wb).abs().max()) < 1e-10 and str(wb.first_valid_index()) == "1978-01")
    check("M1: the two-market form removes both betas (correlations near 0)",
          abs(wc.corr(m1_)) < 0.1 and abs(wc.corr(m2_)) < 0.1 and abs(r.corr(m2_)) > 0.3)
    rm = res["M1"]
    wb1 = A2.p4(bk["net"], R["eq_us_spx"])
    wb2 = DG.p4_multi(bk["net"], R[["eq_us_spx", "bd_us_10y"]])
    jm = pd.concat([ST.cut(x_, "1990-01", "2010-12") for x_ in (bk["net"], wb1, wb2)], axis=1).dropna()
    check("M1 (W7): each era's Sharpe ratios are over the common months of the three series (count printed)",
          res["M1"]["eras"]["1990-2010"]["n"] == len(jm) and
          abs(res["M1"]["eras"]["1990-2010"]["both"] - ST.sharpe(jm.iloc[:, 2])) < 1e-12)
    check("M1 gate: both iff in either era Sharpe(both) <= Sharpe(S&P) - 0.05",
          rm["both"] == any(rm["eras"][e]["both"] <= rm["eras"][e]["spx"] - 0.05 for e in ("1978-89", "1990-2010")))

    # ---- falsifiers
    fz = res["FALSIFIERS"]
    e3 = fz["E3"][0]
    check("Falsifier theme split: parts add to the held Economic trend position (< 1e-12) and the theme scores "
          "reproduce E", e3 is not None and e3["sum_diff"] < 1e-12 and e3["e_diff"] < 1e-12, e3 and
          (e3["sum_diff"], e3["e_diff"]))
    check("Falsifiers: every registered line has a verdict", set(fz) == {"T1", "T2", "C1", "C2", "C3", "C4", "C5", "V1",
                                                                          "E1", "E3"})

    # ---- seal
    Rl, Dl, Sl0, gl = S2.scenario(late=True)
    Sl = dict(Sl0, E=S["E"].reindex(Rl.index))
    Sl["E"].loc[Sl["E"].index > pd.Period("2010-12", "M")] = 9.87654321
    ETl = {}
    for t_ in ET:
        ETl[t_] = ET[t_].reindex(Rl.index)
        ETl[t_].loc[ETl[t_].index > pd.Period("2010-12", "M")] = 9.87654321
    late = []
    DG.report(Rl, Dl, Sl, gl, out=late.append, ET=ETl)
    check("seal: values dated after 2010-12 in every input change nothing in the report", late == lines,
          next((a + " || " + b for a, b in zip(late, lines) if a != b), ""))

    # ---- printing
    need = {"BLOCKED | ": 2, "D1 | ": 5, "D2 | ": 4, "D2 GATE": 1, "COSTDRAG | ": 16, "D3 | ": 3, "D3 GATE": 1,
            "D4 | ": 9, "D4 GATE": 2, "CRISIS | ": 8, "S1 | ": 9, "D5 | ": 3, "D5 GATE": 1, "D6 | ": 2, "D6 GATE": 1,
            "X2 | ": 3, "X2 GATE": 1, "M1 | ": 3, "M1 GATE": 1, "FALSIFIER | ": 20, "DIAG SUMMARY": 1}
    cnt = {k: sum(1 for x in lines if x.startswith(k)) for k in need}
    check("report: every registered line type is printed (counts)", cnt == need,
          {k: (cnt[k], need[k]) for k in need if cnt[k] != need[k]})
    planted = set()
    for v in np.concatenate([R.dropna().values.ravel()[::97], S["C"].dropna().values.ravel()[::89]]):
        planted.add("%.6f" % v)
        planted.add("%.5f" % v)
    hits = [p for p in planted if p in txt]
    check("printing: no planted data value appears", not hits, hits[:5])
    long_dec = re.findall(r"\d\.\d{5,}", txt)
    check("printing: no number with 5 or more decimals", not long_dec, long_dec[:5])
    small = [m for m in re.findall(r"-?\d+\.\d+ \((\d+)\)", txt) if int(m) < DG.MIN_PRINT]
    check("printing: every value printed with a month count has >= 60 months (smaller cells: count and sign)",
          not small and "sign" in txt, small[:5])

    # ---- facts, as run, trial rows
    rp = os.path.join(tmp, "gm_a2_v1.txt")
    v, why = DG.a2_facts(rp)
    check("A2 facts: a missing report gives nothing", v is None and why.startswith("missing"), why)
    open(rp, "w").write(a2_report_text())
    v, why = DG.a2_facts(rp)
    check("A2 facts: book k1 / k0 / d1, the incumbent's pods and P4 are read (not the challenger, not costs x2)",
          why == "ok" and v["book"] == {"k1": 1.439, "k0": 1.481, "d1": 1.064} and v["pods"]["value"] == (0.15, 345)
          and v["p4"] == (1.39, 1.34, 396), (v, why))
    for kw, word in (({"verdict": "PASS"}, "VERDICT"), ({"done": False}, "JOB DONE"), ({"pid": "f" * 64}, "PANEL ID")):
        open(rp, "w").write(a2_report_text(**kw))
        v, why = DG.a2_facts(rp)
        check("A2 facts: refused when %s" % word, v is None and word in why, why)
    got = {"book": {}, "pods": {}, "p4": None}
    from gm import book as B_
    got["book"]["k1"] = round(ST.sharpe(ST.cut(bk["net"], *DG.WIN)), 3)
    got["book"]["k0"] = round(ST.sharpe(ST.cut(B_.run(R, cfg=cfg, daily=D, S=S)["net"], *DG.WIN)), 3)
    got["book"]["d1"] = round(ST.sharpe(ST.cut(B_.run(R, cfg=dict(cfg, delay_months=1), daily=D, S=S)["net"],
                                               *DG.WIN)), 3)
    for p in DG.PODS:
        x_ = ST.cut(DG.pod_book(R, D, S, days, cfg, [(p, "*", "*")])["net"], *DG.WIN)
        got["pods"][p] = (round(ST.sharpe(x_), 2), len(x_))
    w4 = A2.p4(bk["net"], R["eq_us_spx"])
    got["p4"] = (round(ST.sharpe(ST.cut(bk["net"], "1978-01", "2010-12")), 2),
                 round(ST.sharpe(ST.cut(w4, "1978-01", "2010-12")), 2), len(ST.cut(bk["net"], "1978-01", "2010-12")))
    ok_lines = []
    DG.as_run(R, D, S, days, cfg, got, ok_lines.append)
    check("as-run: the book's own values pass (one PASS line)", len(ok_lines) == 1 and ok_lines[0].startswith("PASS"),
          ok_lines)
    bad_lines = []
    try:
        DG.report(R, D, S, gspc, out=bad_lines.append, facts=dict(got, book=dict(got["book"], k1=9.999)))
        raised = False
    except DG.AsRunMismatch:
        raised = True
    check("as-run: a mismatch raises before any diagnostic is printed (one FAIL line)",
          raised and len(bad_lines) == 1 and bad_lines[0].startswith("FAIL A2-final book as run"), bad_lines)
    sha_, n_, _l = DG.trial_rows_digest(os.path.join(REPO, "gm", "trials.csv"))
    check("trial log pin (C7): the repo trial log's book / pod rows have the registered digest (N 40)",
          sha_ == DG.TRIAL_ROWS_SHA and n_ == DG.TRIAL_ROWS_N, (sha_, n_))
    tl = os.path.join(tmp, "trials.csv")
    shutil.copy(os.path.join(REPO, "gm", "trials.csv"), tl)
    with open(tl, "a", encoding="utf-8") as f:
        f.write('2026-11-28 10:00,D1 diagnostic (A2-final book),diag,abcdef1234,,,,,,"note","{}"\n')
    check("trial log pin (C7): an appended diag row does not change the digest", DG.trial_rows_digest(tl)[0] == sha_)
    t2 = open(os.path.join(REPO, "gm", "trials.csv"), encoding="utf-8").read().replace("1faa343535,1.526",
                                                                                        "1faa343535,1.527")
    open(tl, "w", encoding="utf-8").write(t2)
    check("trial log pin (C7): a changed book row changes the digest", DG.trial_rows_digest(tl)[0] != sha_)
    tr = DG.trial_rows(res, DG.A1_PANEL_ID, CF.ENGINE_VERSION)
    check("trial rows: 10 rows, family diag, distinct hashes, note names the panel, book and outcome",
          len(tr) == 10 and all(r["family"] == "diag" for r in tr) and len({r["hash"] for r in tr}) == 10 and
          all("e7f98d4439fccf91" in r["note"] and "77374d7bef" in r["note"] and "outcome" in r["note"] for r in tr))
    check("registered constants: config hashes and engine as the gm-2.2.1 entry",
          {k: CF.cfg_hash(getattr(CF, k)) for k in DG.CFG_HASHES} == DG.CFG_HASHES and CF.ENGINE_VERSION == DG.ENGINE)

    # ---- the job in the PC layout
    import a1_panel_smoke as A1S
    loc = os.path.join(tmp, "local")
    lib = os.path.join(loc, "lib")
    os.makedirs(lib)
    shutil.copytree(os.path.join(REPO, "gm"), os.path.join(lib, "gm"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    bq = os.path.join(REPO, "tools", "bbgq")
    for rel in ("lib/gm_engine.py", "lib/bbg_panel.py", "lib/bbgdata.py", "lib/a1_panel.py", "lib/a2_batch.py",
                "lib/diag_a2.py", "live_sources.csv", "untouched_markets.csv", "engine_ref.json"):
        shutil.copy(os.path.join(bq, rel), os.path.join(lib, os.path.basename(rel)))
    blocks, _free = A1S.scenario()
    A1S.write_store(os.path.join(loc, "work"), blocks)
    env = dict(os.environ, BBG_WORK=os.path.join(loc, "work"), PYTHONPATH="")
    job = os.path.join(bq, "jobs", "gm_diag_v1.py")

    def go():
        q = subprocess.run([sys.executable, job], cwd=loc, env=env, capture_output=True, text=True, timeout=600)
        return q.stdout + q.stderr
    o0 = go()
    check("job (PC layout): no gm_a2_v1 report -> STOP before the store is opened", "PASS gm code vs reference" in o0
          and "PASS lib engine_ref.json" in o0 and "PASS engine gm-2.2.1 and config hashes" in o0 and
          o0.count("PASS lib ") == 8 and "PASS lib gm\\trials.csv book / pod rows | 40 rows" in o0 and
          "FAIL A2 report gm_a2_v1.txt: missing" in o0 and "lock id" not in o0, o0[-900:])
    os.makedirs(os.path.join(loc, "results"))
    open(os.path.join(loc, "results", "gm_a2_v1.txt"), "w").write(a2_report_text())
    with open(os.path.join(lib, "gm", "trials.csv"), "a", encoding="utf-8") as f:
        f.write('2026-11-28 10:00,D1 diagnostic (A2-final book),diag,abcdef1234,,,,,,"note","{}"\n')
    o1 = go()
    check("job: A2 report PASS, an appended diag row passes the trial-log pin, a non-LOCK_v2 store -> STOP before any "
          "value is read", "PASS A2 report gm_a2_v1.txt: ok" in o1 and "PASS lib gm\\trials.csv" in o1 and
          "FAIL Bloomberg store lock id" in o1 and "STOP: the Bloomberg store is not LOCK_v2 (nothing read)" in o1,
          o1[-900:])
    with open(os.path.join(lib, "diag_a2.py"), "a") as f:
        f.write("\n# changed\n")
    o2 = go()
    check("job: a changed diag_a2.py stops it at the hash check", "FAIL lib diag_a2.py" in o2 and
          "STOP: lib file differs from the registered build: diag_a2.py" in o2 and "lock id" not in o2, o2[-600:])
    shutil.copy(os.path.join(bq, "lib", "diag_a2.py"), os.path.join(lib, "diag_a2.py"))
    shutil.copy(os.path.join(bq, "engine_ref_gm-2.2.0.json"), os.path.join(lib, "engine_ref.json"))
    o3 = go()
    check("job: an old engine_ref.json stops it (C2)", "STOP" in o3 and "lock id" not in o3 and
          ("FAIL lib engine_ref.json" in o3 or "FAIL gm code vs reference" in o3), o3[-600:])
    shutil.copy(os.path.join(bq, "engine_ref.json"), os.path.join(lib, "engine_ref.json"))
    t3 = open(os.path.join(lib, "gm", "trials.csv"), encoding="utf-8").read().replace("1faa343535,1.526",
                                                                                     "1faa343535,1.527")
    open(os.path.join(lib, "gm", "trials.csv"), "w", encoding="utf-8").write(t3)
    o4 = go()
    check("job: a changed book row of the trial log stops it before the store (C7)",
          "FAIL lib gm\\trials.csv book / pod rows" in o4 and "STOP: the book / pod rows" in o4 and "lock id" not in o4,
          o4[-600:])
    check("job output: no number with 5+ decimals", not re.findall(r"\d\.\d{5,}", o0 + o1 + o2 + o3 + o4))


if __name__ == "__main__":
    fails = []

    def check(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)[:600]))
        if not ok:
            fails.append(name)
    run(check)
    print("DIAG A2 SMOKE " + ("PASSED" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
