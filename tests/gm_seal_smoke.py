"""Smoke test of the gm-1.2.3 fix version (gm/CHANGES.md 2026-11-24, E1-E5) on SYNTHETIC data (no cache needed).

E5 seal and holding cut: a design run (gm.book.run default, gm.timing.delayed_pnl default) has no output dated after
2010-12, does not change when any input dated after the seal changes, and gives the same numbers up to 2010-12 as the
unsealed engine (k = 0 is prefix-only); the guard gm.seal.check_output fails on a late value. E1 Bloomberg switches
default OFF (value composite, curve carry, growth surprise ignored unless switched on). E2 EQ_INDEX without the three
wrong mappings. E3 OECD csv: quarterly rows enter at the quarter's last month (+ the callers' 1-month lag), unparseable
files raise. E4 Value's non-US dividend yield = the 12 months ending at t-12; US unchanged; lag-0 form kept.

python3 tests/gm_seal_smoke.py      (also run from tests/run_tests.py)
"""
import os
import shutil
import sys
import tempfile

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from gm import bloomberg as BBG  # noqa: E402
from gm import book as B  # noqa: E402
from gm import config as CF  # noqa: E402
from gm import panel as P  # noqa: E402
from gm import seal as SL  # noqa: E402
from gm import signals as G  # noqa: E402
from gm import timing as TM  # noqa: E402

IDX = pd.period_range("1975-01", "2015-12", freq="M")
MK = ["eq_us_spx", "eq_jp_nikkei", "eq_gb_ftse", "eq_de_dax", "bd_us_10y", "bd_de_10y", "bd_gb_10y", "bd_jp_10y",
      "fx_eur", "fx_jpy", "fx_gbp", "fx_aud", "cm_wti", "cm_gold", "cm_corn", "cm_copper"]
SEAL_M = pd.Period("2010-12", "M")


def synth(seed=3):
    rng = np.random.default_rng(seed)
    R = pd.DataFrame(rng.normal(0.004, 0.04, (len(IDX), len(MK))), index=IDX, columns=MK)
    S = {k: pd.DataFrame(rng.normal(0, 1, (len(IDX), len(MK))), index=IDX, columns=MK) for k in ("E", "C", "V")}
    S["E"] = S["E"].clip(-1, 1)
    days = pd.bdate_range("1985-01-01", "2015-12-31")
    D = pd.DataFrame(rng.normal(0, 0.01, (len(days), 6)), index=days, columns=MK[:2] + MK[4:6] + MK[8:10])
    return R, S, D


def poison(R, S, D):
    """Change every input dated after the seal (values that would move the result if read)."""
    R2, D2 = R.copy(), D.copy()
    R2.loc[R2.index > SEAL_M] = R2.loc[R2.index > SEAL_M] * -7 + 0.3
    D2.loc[D2.index > pd.Timestamp("2010-12-31")] = 0.2
    S2 = {k: v.copy() for k, v in S.items()}
    for v in S2.values():
        v.loc[v.index > SEAL_M] = -v.loc[v.index > SEAL_M] * 3
    return R2, S2, D2


def frames(res):
    return {k: v for k, v in res.items() if isinstance(v, (pd.Series, pd.DataFrame))} | {
        "fam_" + f: v for f, v in res["fam_pos"].items()}


class Patch:
    def __init__(self, *items):
        self.items, self.saved = items, []

    def __enter__(self):
        for mod, name, val in self.items:
            self.saved.append((mod, name, getattr(mod, name)))
            setattr(mod, name, val)
        return self

    def __exit__(self, *a):
        for mod, name, val in reversed(self.saved):
            setattr(mod, name, val)
        return False


def run(check):
    R, S, D = synth()
    cfg = CF.CANDIDATE
    # ---------------------------------------------------------------- E5
    res = B.run(R, cfg=cfg, daily=D, S=S)
    late = {k: str(v.index.max()) for k, v in frames(res).items() if len(v.index) and v.index.max() > SEAL_M}
    check("E5 seal: no design output of gm.book.run is dated after 2010-12", not late, str(late)[:300])
    check("E5 holding cut: last return month 2010-12 (held from month-end 2010-11), nothing earned later",
          res["net"].index.max() == SEAL_M and np.isfinite(res["net"].loc[SEAL_M]), str(res["net"].tail(2)))
    R2, S2, D2 = poison(R, S, D)
    res2 = B.run(R2, cfg=cfg, daily=D2, S=S2)
    same = all(frames(res)[k].equals(frames(res2)[k]) for k in frames(res))
    check("E5 seal: changing every input dated after the seal leaves every design output unchanged", same)
    un = B.run(R, cfg=cfg, daily=D, S=S, seal=None)
    check("E5 seal: the unsealed engine (live / holdout only) does run past 2010 (test not vacuous)",
          un["net"].index.max() > SEAL_M and un["net"].loc["2011-01":].notna().any())
    eq = all(np.allclose(un[k].loc[:SEAL_M].to_numpy(dtype=float), res[k].to_numpy(dtype=float), equal_nan=True,
                         rtol=0, atol=1e-14) for k in ("net", "gross", "pos", "vol"))
    check("E5 seal: k = 0 design numbers up to 2010-12 equal the unsealed engine's", eq)
    try:
        SL.check_output({"x": pd.Series([1.0, 2.0], index=pd.period_range("2010-12", "2011-01", freq="M"))})
        breach = False
    except SL.SealBreach:
        breach = True
    quiet = SL.check_output({"x": pd.Series([1.0, np.nan], index=pd.period_range("2010-12", "2011-01", freq="M"))})
    check("E5 guard: a value dated 2011-01 in a design output raises SealBreach (an empty late row does not)",
          breach and quiet is not None)
    pnl = TM.delayed_pnl(res["pos"], D, 3)
    pnl2 = TM.delayed_pnl(res2["pos"], D2, 3)
    days = D.index
    m_end = pd.Series(days, index=days).groupby(days.to_period("M")).max()
    i0, i1 = days.get_loc(m_end[pd.Period("2010-11", "M")]) + 3, days.get_loc(pd.Timestamp("2010-12-31"))
    cols = [c for c in res["pos"].columns if c in D.columns]
    want = float((res["pos"].loc[pd.Period("2010-11", "M"), cols].fillna(0) *
                  (D[cols].fillna(0).cumsum().iloc[i1] - D[cols].fillna(0).cumsum().iloc[i0])).sum())
    pnl_un = TM.delayed_pnl(un["pos"], D, 3, seal=None)
    check("E5 delay diagnostic: no month after 2010-12, the 2010-11 holding ends at the 2010-12-31 close, later days "
          "unread", pnl.index.max() == SEAL_M and abs(pnl.loc[SEAL_M] - want) < 1e-12 and pnl.equals(pnl2)
          and abs(pnl_un.loc[SEAL_M] - pnl.loc[SEAL_M]) > 1e-12, "%s %s" % (pnl.tail(1).to_dict(), want))
    # ---------------------------------------------------------------- E2
    check("E2 EQ_INDEX: no eq_eu_stoxx50 / eq_us_ndx / eq_us_r2k mapping; same-country MSCI mappings kept",
          not {"eq_eu_stoxx50", "eq_us_ndx", "eq_us_r2k"} & set(BBG.EQ_INDEX) and BBG.EQ_INDEX["eq_de_dax"] ==
          "MXDE Index" and BBG.EQ_INDEX["eq_us_spx"] == "MXUS Index")
    # ---------------------------------------------------------------- E1
    check("E1 Bloomberg switches: all four OFF by default", CF.BBG_SWITCHES == {
        "value_composite": False, "curve_carry": False, "alt_commodities": False, "growth_surprise": False})
    grid = G.GRID
    one = pd.Series(1.0, index=grid)
    fake_vc = pd.DataFrame(0.123, index=grid, columns=["eq_us_spx", "eq_jp_nikkei", "eq_gb_ftse"])
    fake_dy = pd.DataFrame({"eq_us_spx": 0.02, "eq_jp_nikkei": 0.01, "eq_gb_ftse": 0.03}, index=grid)
    Rg = R.reindex(grid)
    stubs = Patch((G, "yield_of", lambda cc, n: one * 5), (G, "rate", lambda cc: one * 3),
                  (G, "cpi_yoy", lambda cc: one * 2), (G, "equity_dy", lambda lag=0: fake_dy),
                  (P, "rate3m", lambda cc: one * 3), (P, "eia_rolled", lambda root: (one * 0, one * 0.05)),
                  (P, "fx_usd_value", lambda cur: one), (BBG, "value_composite", lambda m: fake_vc),
                  (BBG, "commodity_carry", lambda k: one * 0.777), (BBG, "surprise", lambda tk, sg=1: one * 0.5))
    sw = dict(CF.BBG_SWITCHES)
    try:
        with stubs:
            v_off, c_off, g_off = G.value_values(Rg), G.carry_values(Rg), G.growth_surprise("US")
            for k in CF.BBG_SWITCHES:
                CF.BBG_SWITCHES[k] = True
            v_on, c_on, g_on = G.value_values(Rg), G.carry_values(Rg), G.growth_surprise("US")
    finally:
        CF.BBG_SWITCHES.clear()
        CF.BBG_SWITCHES.update(sw)
    check("E1 switches off: Value ignores the Bloomberg composite, Carry the Bloomberg curves, growth the surprises",
          v_off["eq_us_spx"].dropna().eq(0.02).all() and "cm_corn" not in c_off and c_off["cm_wti"].dropna().eq(0.05).all()
          and g_off.isna().all())
    check("E1 switches on: each Bloomberg input is used (the flags are live)",
          v_on["eq_us_spx"].dropna().eq(0.123).all() and c_on["cm_corn"].dropna().eq(0.777).all()
          and c_on["cm_wti"].dropna().iloc[-1] == 0.777 and g_on.dropna().eq(0.5).all() and g_on.notna().any(),
          "%s %s %s" % (v_on["eq_us_spx"].dropna().unique()[:3], c_on.get("cm_corn", pd.Series()).dropna().unique()[:3],
                        g_on.dropna().unique()[:3]))
    # ---------------------------------------------------------------- E3 and E4
    tmp = tempfile.mkdtemp(prefix="gm_seal_")
    old_rd = P.RD
    try:
        P.RD = tmp
        G._SDMX.clear()
        pd.DataFrame({"REF_AREA": ["AAA", "AAA", "BBB", "BBB", "CCC", "CCC"], "FREQ": ["M", "M", "Q", "Q", "M", "Q"],
                      "TIME_PERIOD": ["2009-01", "2009-02", "2009-Q1", "2009-Q2", "2009-03", "2009-Q1"],
                      "OBS_VALUE": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]}).to_csv(os.path.join(tmp, "t.csv"), index=False)
        b = G.oecd_sdmx("t.csv", "BBB")
        c = G.oecd_sdmx("t.csv", "CCC")
        a = G.oecd_sdmx("t.csv", "AAA")
        m = lambda s: pd.Period(s, "M")  # noqa: E731
        ok_q = (b.loc[m("2009-02")] != b.loc[m("2009-02")] and b.loc[m("2009-03")] == 3.0 and b.loc[m("2009-05")] == 3.0
                and b.loc[m("2009-06")] == 4.0 and b.loc[m("2009-08")] == 4.0 and np.isnan(b.loc[m("2009-09")]))
        check("E3 quarterly CPI: Q1 sits on March (+ the callers' 1-month lag = end of April), carried to May; "
              "monthly rows unchanged; monthly wins over quarterly",
              ok_q and a.loc[m("2009-01")] == 1.0 and c.loc[m("2009-03")] == 5.0 and c.loc[m("2009-04")] == 6.0,
              str(b.dropna().to_dict()))
        lagged = G.lag(b, 1)
        check("E3 as-of: with the 1-month lag a quarter enters at the end of the month after it ends",
              np.isnan(lagged.loc[m("2009-03")]) and lagged.loc[m("2009-04")] == 3.0 and lagged.loc[m("2009-07")] == 4.0)
        pd.DataFrame({"REF_AREA": ["AAA"], "TIME_PERIOD": ["2009"], "OBS_VALUE": [1.0]}).to_csv(
            os.path.join(tmp, "bad.csv"), index=False)
        try:
            G.oecd_sdmx("bad.csv", "AAA")
            raised = False
        except G.OECDParseError:
            raised = True
        check("E3 oecd_sdmx raises on an unparseable csv (no silent fallback); a missing file stays empty",
              raised and G.oecd_sdmx("missing.csv", "AAA").isna().all())
        meta = {r["country"]: r for r in G.sdmx_meta("t.csv")}
        check("E3 metadata listing: frequency per country and first design date",
              meta["AAA"]["frequency"] == "monthly" and meta["BBB"]["frequency"] == "quarterly" and
              meta["CCC"]["frequency"] == "both" and meta["BBB"]["first"] == "2009-03", str(meta))
        rng = np.random.default_rng(5)
        fr = {n: pd.Series(rng.normal(0.008, 0.04, len(grid)), index=grid).where(grid >= m("1975-01"))
              for n in G.FRENCH_DY.values()}
        xd = {n: v - 0.002 for n, v in fr.items()}
        spy = pd.Series(np.exp(np.cumsum(rng.normal(0, 0.03, len(grid)))), index=grid)
        with Patch((G, "_french_mkt", lambda f, n: (xd if "xdiv" in f else fr)[n]),
                   (P, "Y", lambda sym: spy * (1.0 if sym == "SPY" else 0.999 ** np.arange(len(grid))))):
            d0, d12 = G.equity_dy(0), G.equity_dy(12)
            d_reg = G.equity_dy(CF.VALUE_DY_LAG)
        non_us = list(G.FRENCH_DY)
        check("E4 Value dividend yield: non-US = the 12 months ending at t-12 (no carry-forward); US unchanged; "
              "registered lag is 12",
              CF.VALUE_DY_LAG == 12 and d12[non_us].equals(d0[non_us].shift(12).where(d0[non_us].shift(12).notna()))
              and d_reg.equals(d12) and d12["eq_us_spx"].equals(d0["eq_us_spx"]) and len(non_us) == 7
              and abs(d12["eq_de_dax"].loc[m("2000-06")] - 0.024) < 1e-12)
    finally:
        P.RD = old_rd
        G._SDMX.clear()
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    fails = []

    def check(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)[:300]))
        if not ok:
            fails.append(name)
    run(check)
    print("GM SEAL SMOKE " + ("PASSED" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
