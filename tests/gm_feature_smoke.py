"""Smoke test of the gm-2.1.0 feature version (gm/CHANGES.md 2026-11-24, E6-E11, E14) on SYNTHETIC data only.

No cache, no market data: every series is simulated, so every check has a known answer. No statistic of any path on
real data is computed here.
  E6  k = 1 returns on a constructed series (formula, flags, holding cut at the seal); a k = 1 book has the k = 0
      positions and earns the k = 1 returns
  E7  grid averaging (each version a complete pod, equal-weight mean at the unscaled stage, a missing version = 0);
      Carry v1 / v2 reproduce today's half-and-half; Trend and Economic trend / Value versions by hand
  E8  tranches: NYSE calendar offsets 0 / 5 / 10 / 15 with holidays, last-price rule, markets without daily data,
      tranche 0 = the k = 1 path, seal and holding cut
  E9  Core and shadow masks partition the components; the equal-risk Core book by hand
  E10 alpha bootstrap (known answers; counts agree with tools/power), placebo maps and engine, non-inferiority and
      test 5 (agrees with gm.protocol.decide check 5)
  E11 joint caps keep a spread vector's proportions; a shared leg cap
  E14 card 4 daily excess return sums to the panel's monthly return for a month held in full
  E5  every new path: no output after 2010-12, unchanged when inputs after the seal change

python3 tests/gm_feature_smoke.py      (also run from tests/run_tests.py)
"""
import os
import sys

import numpy as np
import pandas as pd

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, REPO)

from gm import book as B  # noqa: E402
from gm import config as CF  # noqa: E402
from gm import execution as EX  # noqa: E402
from gm import protocol as PR  # noqa: E402
from gm import seal as SL  # noqa: E402
from gm import stats as ST  # noqa: E402
from gm import vol as VM  # noqa: E402

IDX = pd.period_range("1975-01", "2015-12", freq="M")
MK = ["eq_us_spx", "eq_jp_nikkei", "eq_gb_ftse", "eq_de_dax", "bd_us_10y", "bd_de_10y", "bd_gb_10y", "bd_jp_10y",
      "fx_eur", "fx_jpy", "fx_gbp", "fx_aud", "cm_wti", "cm_natgas", "cm_heatoil", "cm_gold"]
DAILY = ["eq_us_spx", "eq_jp_nikkei", "bd_us_10y", "bd_de_10y", "fx_eur", "fx_jpy", "cm_wti"]
SEAL_M = pd.Period("2010-12", "M")
SEAL_D = pd.Timestamp("2010-12-31")


def calendar(a="1980-01-01", b="2015-12-31"):
    """Synthetic NYSE days: weekdays minus 1 January, 4 July, 25 December and the third Monday of each February,
    plus a four-day special closure (as 2001-09-11..14)."""
    d = pd.bdate_range(a, b)
    hol = ((d.month == 1) & (d.day == 1)) | ((d.month == 7) & (d.day == 4)) | ((d.month == 12) & (d.day == 25))
    hol |= (d.month == 2) & (d.dayofweek == 0) & (d.day >= 15) & (d.day <= 21)
    hol |= (d >= "2001-09-11") & (d <= "2001-09-14")
    return d[~hol]


def synth(seed=11):
    rng = np.random.default_rng(seed)
    R = pd.DataFrame(rng.normal(0.003, 0.035, (len(IDX), len(MK))), index=IDX, columns=MK)
    R.loc[:"1979-12", "cm_gold"] = np.nan                    # a market that starts late
    S = {k: pd.DataFrame(rng.normal(0, 1, (len(IDX), len(MK))), index=IDX, columns=MK) for k in ("E", "C", "V")}
    S["E"] = np.tanh(S["E"] / 2)
    S["E_sign"] = np.sign(S["E"])
    S["V2"] = pd.DataFrame(rng.normal(0, 1, (len(IDX), len(MK))), index=IDX, columns=MK)
    S["V2"].loc[:"1990-12", "fx_aud"] = np.nan               # a version missing for one market
    days = pd.bdate_range("1980-01-01", "2015-12-31")
    D = pd.DataFrame(rng.normal(0, 0.008, (len(days), len(DAILY))), index=days, columns=DAILY)
    D.loc[:"1994-12-31", "cm_wti"] = np.nan                  # daily data only from 1995
    hol_jp = (D.index.month == 1) & (D.index.day.isin([2, 3]))
    D.loc[hol_jp, "eq_jp_nikkei"] = np.nan                   # a local holiday (no price that day)
    cal = calendar()
    gspc = pd.Series(np.exp(np.cumsum(rng.normal(0.0003, 0.01, len(cal)))) * 100, index=cal)
    return R, S, D, cal, gspc


def poison(R, S, D, gspc):
    R2, D2, g2 = R.copy(), D.copy(), gspc.copy()
    R2.loc[R2.index > SEAL_M] = R2.loc[R2.index > SEAL_M] * -5 + 0.2
    D2.loc[D2.index > SEAL_D] = 0.1
    g2.loc[g2.index > SEAL_D] = g2.loc[g2.index > SEAL_D] * 3
    S2 = {k: v.copy() for k, v in S.items()}
    for v in S2.values():
        v.loc[v.index > SEAL_M] = -v.loc[v.index > SEAL_M] * 4 + 1
    return R2, S2, D2, g2


def same(a, b, tol=1e-12):
    a, b = a.align(b) if hasattr(a, "align") else (a, b)
    x, y = np.asarray(a, float), np.asarray(b, float)
    return bool(np.array_equal(np.isnan(x), np.isnan(y)) and np.nanmax(np.abs(np.nan_to_num(x - y)), initial=0) <= tol)


def late(x):
    try:
        SL.check_output(x)
        return False
    except SL.SealBreach:
        return True


def run(check):
    R, S, D, cal, gspc = synth()
    cfg = CF.CANDIDATE
    days = EX.nyse_days(gspc=gspc)
    check("E8 calendar: NYSE days from the ^GSPC dates, cut at the seal", days[-1] <= SEAL_D and
          pd.Timestamp("2001-09-12") not in days and pd.Timestamp("2001-09-17") in days)

    # ------------------------------------------------------------------ E6 k = 1
    R1, fl = EX.k1_returns(R, D, days)
    pr = EX.price_returns(D)
    first = EX.month_firsts(days)
    t = pd.Period("1999-06", "M")
    m = "fx_eur"
    want = R.loc[t, m] - pr.loc[first[t], m] + pr.loc[first[t + 1], m]
    check("E6 k = 1 = R(t) - r(first day of t) + r(first day of t+1)", abs(R1.loc[t, m] - want) < 1e-15 and
          not fl.loc[t, m])
    b = "bd_us_10y"
    check("E6 bonds: the daily value is already a price return (no exp)",
          abs(R1.loc[t, b] - (R.loc[t, b] - D.loc[first[t], b] + D.loc[first[t + 1], b])) < 1e-15)
    t2 = pd.Period("2001-01", "M")                      # first NYSE day 2001-01-02: no Nikkei price (local holiday)
    check("E6 no price on a first day -> k = 0 return, flagged",
          fl.loc[t2, "eq_jp_nikkei"] and R1.loc[t2, "eq_jp_nikkei"] == R.loc[t2, "eq_jp_nikkei"])
    check("E6 no daily data at all (cm_gold, cm_natgas) -> k = 0, flagged",
          bool(fl.loc["1990":"2010", "cm_gold"].all()) and same(R1.loc["1990":"2010", "cm_gold"],
                                                                R.loc["1990":"2010", "cm_gold"]))
    dec = pd.Period("2010-12", "M")
    check("E6 holding cut: the holding decided at 2010-11 ends at the 2010-12-31 close (no January day read)",
          abs(R1.loc[dec, m] - (R.loc[dec, m] - pr.loc[first[dec], m])) < 1e-15 and not fl.loc[dec, m])
    check("E5 k = 1: no output after 2010-12", R1.index[-1] == SEAL_M and fl.index[-1] == SEAL_M)
    Rp, Sp, Dp, gp = poison(R, S, D, gspc)
    R1p, flp = EX.k1_returns(Rp, Dp, EX.nyse_days(gspc=gp))
    check("E5 k = 1 unchanged when every input after the seal changes", same(R1, R1p) and flp.equals(fl))
    b0 = B.run(R, cfg=cfg, daily=D, S=S)
    b1 = EX.run_k1(R, cfg, D, S, days)
    check("E6 a k = 1 book holds the k = 0 positions", same(b0["pos"], b1["pos"]))
    g1 = (b1["pos"].shift(1) * R1).sum(axis=1, min_count=1).where(b1["gross"].notna())
    check("E6 a k = 1 book earns the k = 1 returns", same(g1, b1["gross"]))
    check("E6 costs charged as today (same cost series)", same(b0["cost"], b1["cost"]) and
          same(b1["gross"] - b1["net"], b0["gross"] - b0["net"]))
    fs = EX.flag_share_by_year(b1["pos"], fl)
    check("E6 flag report: share of gross position flagged by year, in [0, 1]",
          bool(((fs.dropna() >= 0) & (fs.dropna() <= 1)).all()) and fs.index.max() <= 2010)

    # ------------------------------------------------------------------ E7 grids
    old, _ = B.family_positions(R, cfg, D, S)
    new, _, comp = B.family_positions(R, cfg, D, S, components=True)
    ok = all(same(old["carry"][c], new["carry"][c]) for c in old["carry"])
    check("E7 Carry v1 (sign) and v2 (rank) averaged = today's half-and-half (1e-12)", ok)
    ok = all(same(old[f][c], new[f][c]) for f in ("trend", "econ", "value") for c in old[f])
    check("E7 single-version pods unchanged on the version path", ok)
    g = CF.A2_CHALLENGER
    gp_, vol, gc = B.family_positions(R, g, D, S)
    check("E7 version counts: Trend 16, Economic trend 2, Carry 2, Value 2",
          [len(gc[f]["FX"]) for f in ("trend", "econ", "carry", "value")] == [16, 2, 2, 2])
    ok = True
    for f in ("trend", "econ", "carry", "value"):
        for c, terms in gc[f].items():
            have = sum(tt.notna().astype(int) for tt in terms) > 0
            avg = sum(tt.fillna(0) for tt in terms).where(have)
            ok &= same(avg, gp_[f][c])
    check("E7 pod position = sum of version terms p_v / V, a missing version = 0", ok)
    c, mk = "FX", "fx_aud"
    t3 = pd.Period("1985-06", "M")
    v1, v2 = gc["value"][c][0].loc[t3, mk], gc["value"][c][1].loc[t3, mk]
    check("E7 a missing version adds 0 (Value v2 missing for fx_aud before 1991: pod = v1 / 2)",
          np.isnan(v2) and abs(gp_["value"][c].loc[t3, mk] - v1) < 1e-15)
    # Trend version 2 (h = 3, sign, hybrid) by hand
    vh = VM.estimate(R, CF.variant(CF.CANDIDATE, vol={"model": "hybrid"}), D)
    lvl = (1 + R.fillna(0)).cumprod().where(R.notna().cummax())
    s3 = np.sign(lvl / lvl.shift(3) - 1)
    cols = [k for k in R.columns if k.startswith("eq_")]
    p = s3[cols].clip(-1, 1) * 0.40 / vh[cols]
    p = p.div(p.notna().sum(axis=1).where(p.notna().sum(axis=1) > 0), axis=0) / 16
    check("E7 Trend v2 (3 months, sign, hybrid) = sign x 0.40 / vol / n / 16", same(p, gc["trend"]["EQ"][1][cols]))
    vm = VM.m36(R)
    lr = np.log1p(R)
    sg = (lr.rolling(12, min_periods=12).sum() / (vm * np.sqrt(1.0))).clip(-2, 2) / 2
    p = sg[cols] * 0.40 / vm[cols]
    p = p.div(p.notna().sum(axis=1).where(p.notna().sum(axis=1) > 0), axis=0) / 16
    check("E7 Trend v16 (12 months, graded cap 2, m36) by hand", same(p, gc["trend"]["EQ"][15][cols]))
    try:
        B.family_positions(R, g, D, {k: v for k, v in S.items() if k != "V2"})
        check("E7 a grid run without the Value v2 signal stops", False)
    except KeyError:
        check("E7 a grid run without the Value v2 signal stops", True)
    gb = B.run(R, cfg=g, daily=D, S=S)
    check("E5 grid book: no output after 2010-12", not late(gb) and gb["pos"].index[-1] == SEAL_M)

    # ------------------------------------------------------------------ E9 masks and the equal-risk Core book
    comps = [(f, c, v + 1) for f in ("trend", "econ", "carry", "value") for c, ts in gc[f].items()
             for v in range(len(ts))]

    def held(mask, comp_):
        f, c, v = comp_
        return any(mf == f and (mc == "*" or mc == c) and (mv == "*" or mv == v) for mf, mc, mv in mask)
    core_m = [x for q in CF.CORE_PARTS.values() for x in q]
    sh_m = [x for q in CF.SHADOW_PARTS.values() for x in q]
    part = all(held(core_m, x) + held(sh_m, x) == 1 for x in comps)
    check("E9 Core and shadow masks partition every (pod, class, version) component", part and len(comps) > 60)
    mc, ms = B.mask_components(gc, core_m), B.mask_components(gc, sh_m)
    ok = True
    for f in ("trend", "econ", "carry", "value"):
        for c in gc[f]:
            parts_ = [x[(f, c)] for x in (mc, ms) if (f, c) in x]
            have = sum(x.notna().astype(int) for x in parts_) > 0
            ok &= same(sum(x.fillna(0) for x in parts_).where(have), gp_[f][c])
    check("E9 Core + shadow masked positions = the whole pod position", ok)
    check("E9 Core holds Carry FX v2 only, energy v1 + v2, Value EQ only",
          same(mc[("carry", "FX")], gc["carry"]["FX"][1]) and ("value", "FI") not in mc and ("econ", "EQ") not in mc
          and ("carry", "FI") not in mc)
    big = CF.variant(g, gross_cap=1e9, market_risk_cap=1e9)
    cb = B.run(R, cfg=big, daily=D, S=S, parts=CF.CORE_PARTS)
    # by hand: total = sum_P (1/3) k_P sum_b k_b p_b ; positions = s x total (caps off)
    tot = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    for q, mask in CF.CORE_PARTS.items():
        mb = B.mask_components(gc, mask)
        inner = pd.DataFrame(0.0, index=R.index, columns=R.columns)
        rets = []
        for key, pp in mb.items():
            r = (pp.shift(1) * R[pp.columns]).sum(axis=1, min_count=1)
            k = (1 / (r.rolling(36, min_periods=24).std() * np.sqrt(12))).shift(1).clip(upper=50)
            rets.append(r * k.shift(1))
            inner[pp.columns] = inner[pp.columns].add(pp.mul(k, axis=0).fillna(0), fill_value=0)
        rp = pd.concat(rets, axis=1).sum(axis=1, min_count=1)
        kp = (1 / (rp.rolling(36, min_periods=24).std() * np.sqrt(12))).shift(1).clip(upper=50)
        tot = tot.add(inner.mul(kp, axis=0).fillna(0) / 3, fill_value=0)
        act = (rp * kp).notna() if q == "trend" else act | (rp * kp).notna()
    raw = (tot.shift(1) * R.fillna(0)).sum(axis=1)
    raw = raw.where(act)
    sc = (0.10 / (raw.rolling(36, min_periods=24).std() * np.sqrt(12))).shift(1)
    check("E9 equal-risk Core book = parts at unit volatility x 1/n, then the book scaler (by hand)",
          same(tot.mul(sc, axis=0).loc[:SEAL_M], cb["pos"], 1e-10) and bool(np.isfinite(cb["pos"].fillna(0)).all().all()))
    one = cb["part_ret"].mul(pd.DataFrame({q: B._scaler(cb["part_ret"][q]) for q in cb["part_ret"]}))
    vol_p = one.loc["1990":"2010"].std() * np.sqrt(12)
    check("E9 each Core part rescaled to about unit volatility (three parts, each 0.6-1.6)",
          len(vol_p) == 3 and bool(((vol_p > 0.6) & (vol_p < 1.6)).all()))
    sb = B.run(R, cfg=g, daily=D, S=S, parts=CF.SHADOW_PARTS)
    check("E5 Core and shadow books: no output after 2010-12", not late(cb) and not late(sb))

    # ------------------------------------------------------------------ E8 tranches
    tr = EX.tranches(R, cfg, D, S, days)
    d1, e1 = EX.tranche_days(days, 1, days[-1])
    me = EX.month_ends(days)
    t4 = pd.Period("2003-03", "M")
    i = days.get_loc(me[t4])
    check("E8 offsets: tranche j decides on NYSE day 5j after month-end, trades the next NYSE day",
          d1[t4] == days[i + 5] and e1[t4] == days[i + 6] and EX.tranche_days(days, 3, days[-1])[0][t4] == days[i + 15])
    tf = pd.Period("2001-08", "M")
    iF = days.get_loc(me[tf])
    check("E8 holidays: the special closure is skipped (5 NYSE days after 2001-08-31 = 2001-09-07, 10 = 2001-09-20)",
          d1[tf] == days[iF + 5] == pd.Timestamp("2001-09-07") and
          EX.tranche_days(days, 2, days[-1])[0][tf] == pd.Timestamp("2001-09-20"))
    check("E8 tranche 0 = the monthly k = 1 path", same(tr["tranche"][0]["net"], b1["net"]) and
          same(tr["tranche"][0]["pos"], b1["pos"]))
    X1 = tr["tranche"][1]["X"]
    L = EX.levels(D)

    def lv(mk_, day):
        return L[mk_].loc[:day].iloc[-1]
    want = R.loc[t4, m] - (lv(m, d1[t4 - 1]) / lv(m, me[t4 - 1]) - 1) + (lv(m, d1[t4]) / lv(m, me[t4]) - 1)
    check("E8 tranche panel X_j(t) = R(t) - pr(me(t-1) -> d_j(t-1)) + pr(me(t) -> d_j(t))",
          abs(X1.loc[t4, m] - want) < 1e-12)
    Y1 = tr["tranche"][1]["R_earn"]
    want = R.loc[t4, m] - (lv(m, e1[t4 - 1]) / lv(m, me[t4 - 1]) - 1) + (lv(m, e1[t4]) / lv(m, me[t4]) - 1)
    check("E8 tranche holding return runs from the day after d_j(t-1) to the day after d_j(t)",
          abs(Y1.loc[t4, m] - want) < 1e-12)
    tj = pd.Period("2002-12", "M")                       # d_1(2002-12) spans 2003-01-02/03: no Nikkei price
    jp = "eq_jp_nikkei"
    wantj = R.loc[tj, jp] - (lv(jp, d1[tj - 1]) / lv(jp, me[tj - 1]) - 1) + (lv(jp, d1[tj]) / lv(jp, me[tj]) - 1)
    check("E8 a market without a price that day uses its last price", abs(X1.loc[tj, jp] - wantj) < 1e-12 and
          not tr["flags"][1].loc[tj, jp])
    nod = pd.Period("1990-06", "M")
    pos0, pos1 = tr["tranche"][0]["pos"], tr["tranche"][1]["pos"]
    check("E8 no daily data (cm_wti before 1995): tranche 0's position, tranche 0's k = 1 return, flagged",
          tr["flags"][1].loc[nod, "cm_wti"] and abs(pos1.loc[nod, "cm_wti"] - pos0.loc[nod, "cm_wti"]) < 1e-15 and
          Y1.loc[nod, "cm_wti"] == R1.loc[nod, "cm_wti"] and abs(X1.loc[nod, "cm_wti"] - R.loc[nod, "cm_wti"]) < 1e-15)
    check("E8 a market with daily data has its own tranche position", abs(pos1.loc[t4, m] - pos0.loc[t4, m]) > 0)
    q = pd.concat({j: tr["tranche"][j]["net"] for j in range(4)}, axis=1)
    check("E8 tranche form = one quarter of the four tranche returns",
          same((q.fillna(0).sum(axis=1) / 4).where(q.notna().any(axis=1)), tr["net"]))
    check("E5 tranches: no decision after 2010-12-31 (tranches 1-3 of 2010-12 decide in January 2011)",
          all(tr["tranche"][j]["pos"].loc[SEAL_M].isna().all() for j in (1, 2, 3)) and
          tr["tranche"][0]["pos"].loc[SEAL_M].notna().any())
    want = R.loc[SEAL_M, m] - (lv(m, e1[SEAL_M - 1]) / lv(m, me[SEAL_M - 1]) - 1)
    check("E5 tranches: holdings decided in December 2010 end at the 2010-12-31 close", abs(Y1.loc[SEAL_M, m] - want)
          < 1e-12 and e1[SEAL_M] == days[-1])
    trp = EX.tranches(Rp, cfg, Dp, Sp, EX.nyse_days(gspc=gp))
    check("E5 tranches unchanged when every input after the seal changes", same(tr["net"], trp["net"]) and
          all(same(tr["tranche"][j]["pos"], trp["tranche"][j]["pos"]) for j in range(4)))
    check("E5 tranches: no output after 2010-12", not late({"n": tr["net"], "p": {j: tr["tranche"][j]["pos"]
                                                                                for j in range(4)}}))

    # ------------------------------------------------------------------ E10 alpha bootstrap
    rng = np.random.default_rng(5)
    x = pd.Series(rng.normal(0.008, 0.029, 432), index=pd.period_range("1975-01", periods=432, freq="M"))
    y = 0.004 + 0.3 * x + pd.Series(rng.normal(0, 0.01, 432), index=x.index)
    a = ST.alpha_boot(y, x)
    A = np.column_stack([np.ones(432), x.values])
    ref = np.linalg.lstsq(A, y.values, rcond=None)[0]
    check("E10 alpha = least-squares intercept, beta = slope", abs(a["alpha"] - ref[0]) < 1e-14 and
          abs(a["beta"] - ref[1]) < 1e-12)
    check("E10 a strong true alpha: p = 0", a["p"] == 0.0 and a["count"] == 0)
    a_neg = ST.alpha_boot(-0.004 + 0.3 * x + (y - 0.004 - 0.3 * x), x)
    check("E10 a strong negative alpha: p = 1", a_neg["p"] == 1.0)
    sys.path.insert(0, os.path.join(REPO, "tools", "power"))
    import power_3_3 as PW
    yw = 0.0004 + 0.3 * x + pd.Series(rng.normal(0, 0.02, 432), index=x.index)
    aw = ST.alpha_boot(yw, x)
    ap, bp, pp = PW.boot_alpha(x.values[None, :], yw.values[None, :])
    check("E10 alpha bootstrap agrees with tools/power boot_alpha (same alpha; count = p x 10,001 - 1)",
          abs(ap[0] - aw["alpha"]) < 1e-15 and int(round(pp[0] * 10001)) - 1 == aw["count"] and 0 < aw["p"] < 1)
    z = ST.alpha_boot(yw, x * 0)
    check("E10 a zero Core book: alpha = the pod's own mean", abs(z["alpha"] - yw.mean()) < 1e-15 and z["beta"] == 0)
    h = ST.holm({"a": 0.01, "b": 0.012})
    check("E10 Holm at 2.5% over the batch (two pods at 0.01 / 0.012 -> 0.02 / 0.02 pass)",
          all(v < CF.HOLM_LEVEL for v in h.values()))

    # ------------------------------------------------------------------ E10 placebo
    P_ = ST.placebo_perms(50, n=30)
    blocks_ok = all(sorted(pm) == list(range(50)) for pm in P_)
    seg = all(set(np.diff(pm[k:k + 12])) <= {1} for pm in P_ for k in range(0, 48, 12) if pm[k] % 12 == 0 and
              pm[k] < 48)
    check("E10 placebo maps: permutations of whole 12-month blocks aligned to the window start, last part-block kept",
          blocks_ok and seg and all(sorted(np.flatnonzero(pm >= 48)) == sorted(np.flatnonzero(pm >= 48)) and
                                     len(np.flatnonzero(pm >= 48)) == 2 for pm in P_))
    check("E10 placebo maps are fixed by the registered seed", np.array_equal(ST.placebo_perms(50, 30), P_) and
          not np.array_equal(ST.placebo_perms(50, 30, seed=1), P_))
    w = pd.Period("1985-01", "M"), pd.Period("2010-12", "M")
    Tn = (w[1] - w[0]).n + 1
    fut = np.sign(R.shift(-1))                               # a perfect-foresight score: known answer p = 0

    def pod_net(perm, score):
        sc = score if perm is None else ST.move_rows(score, perm, w[0])
        return (sc.shift(1) * R).mean(axis=1)
    res = ST.placebo_runs(lambda pm: pod_net(pm, fut), w, n=200)
    check("E10 placebo: a pod that times every month beats all its placebos (p = 0, pass)", res["p"] == 0 and res["pass"])
    const = pd.DataFrame(1.0, index=R.index, columns=R.columns)
    res = ST.placebo_runs(lambda pm: pod_net(pm, const), w, n=200)
    check("E10 placebo: a standing long exposure is no better than its placebos (p = 1, fail)",
          res["p"] == 1.0 and not res["pass"])
    f = B.placebo_net_fn(R, cfg, D, S, "1985-01")
    ident = f(None)
    nb = B.run(R, cfg=cfg, daily=D, S=S, score_perm={"start": "1985-01", "perm": np.arange(len(R.loc["1985-01":SEAL_M]))})
    check("E10 placebo engine: the identity map reproduces the pod on the version path", same(ident, nb["net"]))
    pm = ST.placebo_perms(Tn, 3)[0]
    moved = f(pm)
    fp2, _, cp2 = B.family_positions(R, cfg, D, S, score_perm={"start": "1985-01", "perm": pm})
    w0 = cp2["trend"]["EQ"][0]
    sc0 = B.trend_signal(R, cfg, VM.estimate(R, cfg, D), S)
    cols = [k for k in R.columns if k.startswith("eq_")]
    mv = ST.move_rows(sc0[cols].clip(-1, 1), pm, "1985-01")
    vol_c = VM.estimate(R, cfg, D)
    pp_ = mv * 0.40 / vol_c[cols]
    pp_ = pp_.div(pp_.notna().sum(axis=1).where(pp_.notna().sum(axis=1) > 0), axis=0)
    check("E10 placebo engine: scores moved jointly in the window, re-sized with each month's own volatility",
          same(pp_, w0[cols]) and not same(moved, ident) and same(ident.loc[:"1984-12"], moved.loc[:"1984-12"]))
    windows = [(pd.Timestamp("1999-10-29"), 52), (pd.Timestamp("2004-02-20"), 20)]
    mvd = ST.move_windows(windows, days, "year", np.random.default_rng(CF.TEST_SEED))
    mvm = ST.move_windows(windows, days, "month", np.random.default_rng(CF.TEST_SEED))
    ok = all(a_.year == e.year and days.get_loc(b_) - days.get_loc(a_) == n for (a_, b_), (e, n) in zip(mvd, windows))
    ok &= all(a_.year == e.year and a_.month == e.month for (a_, _), (e, _) in zip(mvm, windows))
    late_w = ST.move_windows([(pd.Timestamp("2010-12-15"), 30)], days, "month", np.random.default_rng(1),
                             horizon=SEAL_D)
    check("E10 date-rule mover: same year / month, same length in NYSE days, cut at the seal",
          ok and late_w[0][1] <= SEAL_D)

    # ------------------------------------------------------------------ E10 non-inferiority, test 5, T4
    inc = b0["net"].dropna()
    ni = ST.noninferiority(inc, inc.copy())
    check("E10 H1-H3: identical books pass", ni["pass"] and ni["H1"] and ni["H3"])
    ni = ST.noninferiority(inc, inc - 0.01)
    check("E10 H1: a challenger 12%/yr worse fails non-inferiority", not ni["H1"] and not ni["pass"])
    ni = ST.noninferiority(inc, inc, target_ok=False)
    check("E10 H4: an A3 item that misses its own target fails", not ni["pass"])
    agree = 0
    for k in range(100):
        rr = np.random.default_rng(k)
        bi = pd.Series(rr.normal(0.008, 0.03, 300))
        bc = bi + pd.Series(rr.normal(0, 0.012, 300))
        tt = ST.tail_test(bi, bc)
        rec = {"name": "x", "p": 0.0, "dsr": 1.0, "eras": {"a": {"pass": True}}, "dsr_2x": 1.0,
               "dd_inc": ST.maxdd(bi), "dd_cha": ST.maxdd(bc), "wm_inc": float(bi.min()), "wm_cha": float(bc.min())}
        agree += PR.decide([rec])[0]["checks"]["5 tail: max fall not >2pt, worst month not >1pt worse"] == tt["pass"]
    check("E10 test 5 agrees with gm.protocol.decide check 5 (100 of 100)", agree == 100)
    cmb = ST.combined_book(inc, inc * 0)
    check("E10 T4: Core book + a zero pod, rescaled by the book scaler's convention",
          same(cmb, ST.rescale(inc)))

    # ------------------------------------------------------------------ E11 joint caps
    ix = pd.period_range("2000-01", periods=3, freq="M")
    pos = pd.DataFrame({"a": [3.0, 0.5, np.nan], "b": [-1.0, 0.2, 1.0], "c": [0.5, 0.1, 5.0], "d": [9.0, -9.0, 0.0]},
                       index=ix)
    cap = pd.DataFrame({"a": [1.0] * 3, "b": [2.0] * 3, "c": [2.0] * 3, "d": [2.0] * 3}, index=ix)
    out = B.cap_positions(pos, cap, [{"members": ["a", "b", "c"], "cap_from": None}])
    check("E11 strip vector times the smallest cap_j / |x_j| (proportions kept)",
          np.allclose(out.loc[ix[0], ["a", "b", "c"]].values, [1, -1 / 3, 1 / 6]) and
          np.allclose(out.loc[ix[1], ["a", "b", "c"]].values, [0.5, 0.2, 0.1]) and
          np.allclose(out.loc[ix[2], ["b", "c"]].values, [0.4, 2.0]))
    check("E11 columns outside a group clip alone, as today", list(out["d"]) == [2.0, -2.0, 0.0])
    out2 = B.cap_positions(pos[["b", "c"]], cap[["b", "c"]] * pd.Series({"b": 1.0, "c": 10.0}),
                           [{"members": ["b", "c"], "cap_from": "b"}])
    check("E11 Curve carry legs share the front leg's cap", np.allclose(out2.loc[ix[2]].values, [0.4, 2.0]))
    check("E11 no group = today's clip", same(B.cap_positions(pos, cap), pos.clip(lower=-cap, upper=cap)))
    cfg_g = CF.variant(cfg, gross_weights={"fx_eur": CF.STRIP_GROSS_WEIGHT}, gross_cap=0.5)
    bg = B.run(R, cfg=cfg_g, daily=D, S=S)
    gw = pd.Series(1.0, index=R.columns)
    gw["fx_eur"] = 0.25 / 1.9
    check("E11 gross weight 0.25/1.9 counts in the gross cap", float((bg["pos"].abs() * gw).sum(axis=1).max())
          <= 0.5 + 1e-12)

    # ------------------------------------------------------------------ E14 card 4 daily excess return
    Rs = R.copy()
    e = EX.spx_daily_excess(Rs, gspc)
    sm = e.groupby(e.index.to_period("M")).sum()
    full = sm.index[(sm.index >= pd.Period("1980-02", "M"))]
    check("E14 a month held in full earns exactly the panel's monthly excess return",
          same(sm.loc[full], Rs["eq_us_spx"].reindex(full), 1e-13))
    dd = pd.Timestamp("2005-03-15")
    mo = dd.to_period("M")
    n_m = int((e.index.to_period("M") == mo).sum())
    r_d = gspc.loc[dd] / gspc.loc[:dd].iloc[-2] - 1
    lvm = gspc[gspc.index.to_period("M") == mo]
    prev = gspc[gspc.index < lvm.index[0]].iloc[-1]
    sum_r = (lvm / lvm.shift(1).fillna(prev) - 1).sum()
    check("E14 e(d) = price return of d + (panel - month's summed price returns) / N(m)",
          abs(e.loc[dd] - (r_d + (Rs.loc[mo, "eq_us_spx"] - sum_r) / n_m)) < 1e-15)
    check("E5 card 4 daily excess: no day after 2010-12-31", e.index[-1] <= SEAL_D)
    ep = EX.spx_daily_excess(Rp, gp)
    check("E5 card 4 daily excess unchanged when every input after the seal changes", same(e, ep))


if __name__ == "__main__":
    fails = []

    def check(name, cond, detail=""):
        print(("  ok   " if cond else "  FAIL ") + name + (f"  ({detail})" if detail else ""))
        if not cond:
            fails.append(name)
    run(check)
    print("GM FEATURE SMOKE %s" % ("OK" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
