"""Smoke test of the pre-B diagnostics (tools/bbgq/lib/diag_preb.py, job tools/bbgq/jobs/gm_diag_preb_v1.py;
gm/CHANGES.md "Pre-B diagnostics", 2026-11-27) on SYNTHETIC panels and a MOCK LSEG store only (invented numbers; no
cache, no market data, no real panel, no LSEG value).

Checks:
  R1        strip identity (holding end, eight quarterly contracts, no 2011 date read); a flat-in-index strip has no
            bend above cost (FAIL); planted month-long bends qualify (PASS); one triple-month by an independent brute
            force (gap, normal, cost); a stale contract is left out; values after 2010-12 change nothing
  F0        episodes (12-month gap rule), the 48 / 3 floor
  card 1 R5 trigger (median minus G, at least three currencies), 12-month tail, legs and versions; C1-D1 episodes on
            condition months; C1-D2 same-sign share against a hand-made book
  C2-D1     worst fifth, low / other rate split, pooled gate by hand
  card 3 R4 E - TB3MS bar, versions, C3-D1 share and labels
  card 4    R1 windows (form A / B / C, exact cancellation), R2 window length, R3 gate, R4 sign and window; F0 one
            episode for R1, R2, R4 (entry item 5 F0 g)
  card 5 R1 triggers (new high, 120 earlier values), H-month hold, versions; C5-D1 share; C5-D2 breaks and gate
  1.1.0     card inputs reader (lags, daily means, first release vs latest with flags, planted rebase break, seal,
            the lock on the real git files: hashes only); card 1 R1 / R4, C2-D2, C3-D2, card 3 R1 / R2, fixed size,
            card 4 R5, C4-D2, C4-D1 by hand or by construction
  LsegView  on a mini lsegdata store written here: ED contract parse, monthly Period index, sealed as-of refused;
            lseg_lock_of reads the lock before any table
  report    end to end on a synthetic panel + mock LSEG: every diagnostic line, PRE-B SUMMARY, trial rows; printing
            (no 5+ decimals; values only with >= 60 months); seal (values after 2010-12 change nothing)
  job       in the PC layout: lib checks pass; no reports -> STOP before any store; a non-LOCK_v2 Bloomberg store ->
            STOP before any value; a changed diag_preb.py -> STOP at the hash check
python3 tests/diag_preb_smoke.py      (also run from tests/run_tests.py)
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

import a2_batch_smoke as S2  # noqa: E402
import diag_a2_smoke as DS  # noqa: E402
import diag_preb as PB  # noqa: E402
import lsegdata as LD  # noqa: E402
import lseg_rules as LR  # noqa: E402
from gm import config as CF  # noqa: E402
from gm import execution as EX  # noqa: E402

P = lambda s: pd.Period(s, "M")  # noqa: E731


# --------------------------------------------------------------------------------------------------- synthetic ED
def ed_contracts(seed=3, bend=0.0, slope=0.05, stale=None, late=False):
    """Quarterly ED contracts 1981-2012, daily on weekdays, from about 2.6 years before the last trading day; rate =
    level(t) + slope x years to expiry + bend (per contract and calendar month, constant inside the month)."""
    rng = np.random.default_rng(seed)
    days = pd.bdate_range("1981-01-01", "2012-12-31" if late else "2010-12-31")
    lvl = 5 + 2 * np.sin(np.arange(len(days)) / 900.0)
    lvl = pd.Series(lvl, index=days)
    out = {}
    for y in range(1981, 2013):
        for m in (3, 6, 9, 12):
            ltd = pd.Timestamp(LR.dates("ED", y, m)[0])
            d = days[(days >= ltd - pd.Timedelta(days=950)) & (days <= ltd) & (days >= pd.Timestamp("1981-12-09"))]
            if not len(d):
                continue
            tau = (ltd - d).days / 365.0
            r = lvl.reindex(d).to_numpy() + slope * tau
            if bend:
                months = (d - pd.Timedelta(days=7)).to_period("M")   # a bend runs into the next month's first days
                #                                     one draw per (contract, month): the same before 2011 if late
                u = {p: np.random.default_rng([seed, y, m, int(p.ordinal) + 1000]).normal(0, 1) for p in months.unique()}
                r = r + bend * np.array([u[p] for p in months])
            s = pd.Series(100 - r, index=d)
            if late:
                s[s.index > pd.Timestamp("2010-12-31")] = 1.23456789
            out[(y, m)] = s
    if stale is not None:
        k, a, b = stale
        s = out[k]
        msk = (s.index >= pd.Timestamp(a)) & (s.index <= pd.Timestamp(b))
        s[msk] = s[msk].iloc[0]
    return out


def brute_gap(contracts, days, d, n):
    """Independent R1 gap of K_n at month-end d: strip, rates, normal over earlier month-ends of the same group."""
    days = pd.DatetimeIndex(days)

    def strip(day):
        p = day.to_period("M") + 2
        h = dt.date(p.year, p.month, 1)
        while h.weekday() >= 5 or LD.hol_flag(h) & 1:
            h += dt.timedelta(days=1)
        ks = sorted(k for k in [(y, m) for y in range(1980, 2015) for m in (3, 6, 9, 12)]
                    if LR.dates("ED", *k)[0] > h)
        return ks[:8]

    def K(day, st):
        r = []
        for k in st[:n + 1]:
            s = contracts.get(k)
            if s is None or day not in s.index:
                return None
            r.append((100 - s[day]) * 100)
        r = np.array(r)
        return 2 * r[:n].mean() - r[:n - 1].mean() - r[:n + 1].mean()
    st = strip(d)
    g = st[n - 1][1]
    me = pd.Series(days, index=days).groupby(days.to_period("M")).max()
    vals, first = [], None
    for p, e in me.items():
        if e >= d:
            break
        if p < P("1981-12"):
            continue
        ste = strip(e)
        v = K(e, ste)
        if v is None:
            continue
        first = first or p
        if ste[n - 1][1] == g:
            vals.append(v)
    return K(d, st) - np.mean(vals), first


# --------------------------------------------------------------------------------------------------- synthetic panel
EXTRA = ["bd_us_2y", "fx_chf", "fx_sek", "fx_eur", "bd_jp_10y", "bd_gb_10y", "eq_ca_tsx", "bd_ca_10y", "eq_au_asx", "bd_au_10y"]


def panel(seed=11, late=False):
    R, D, S, gspc = S2.scenario(seed=seed, late=late)
    rng = np.random.default_rng(seed + 1)
    g0 = pd.period_range("1960-01", "2010-12", freq="M")
    for k in EXTRA:
        R[k] = pd.Series(rng.normal(0.003, 0.03, len(g0)), index=g0).reindex(R.index)
        R.loc[R.index < P("1970-01"), k] = np.nan
        if late:
            R.loc[R.index > P("2010-12"), k] = 9.87654321
    return R, D, S, gspc


class MockLseg:
    def __init__(self, contracts, monthly):
        self.c, self.m = contracts, monthly

    def ed_contracts(self):
        return {k: "DS:<ED%s%d^%d>|X" % ("FGHJKMNQUVXZ"[k[1] - 1], k[0] % 10, (k[0] // 10) % 10) for k in self.c}

    def daily(self, sid):
        k = PB.ed_delivery(sid.split(":")[1].split("|")[0])
        return self.c[k]

    def monthly(self, sid):
        return self.m[sid]


def lseg_monthly(seed=5, late=False):
    rng = np.random.default_rng(seed)
    g0 = pd.period_range("1969-12", "2010-12", freq="M")
    g = pd.period_range("1969-12", "2012-12" if late else "2010-12", freq="M")
    out = {}
    for sid, start in [(PB.EPS_SID, "1985-01"), ("HP:HGc1|CLOSE", "1988-07"), ("HP:CLc1|CLOSE", "1983-03"),
                       ("HP:Wc1|CLOSE", "1973-01"), ("HP:Cc1|CLOSE", "1973-01"), ("HP:Sc1|CLOSE", "1973-01"),
                       ]:
        x = pd.Series(np.exp(np.cumsum(rng.normal(0.006, 0.06, len(g0)))) * 100, index=g0).reindex(g)
        if sid == PB.EPS_SID:
            x = x * 0 + 60 + np.arange(len(g)) * 0.1
        x[x.index < P(start)] = np.nan
        if late:
            x[x.index > P("2010-12")] = 9.87654321
        out[sid] = x.dropna()
    return out


def fx_values(R, seed=2, crash=("GBP", "1992-10")):
    rng = np.random.default_rng(seed)
    g = R.index
    f = pd.DataFrame({c: np.exp(np.cumsum(rng.normal(0, 0.01, len(g)))) for c in PB.R5_CUR}, index=g)
    f.loc[f.index < P("1999-01"), "EUR"] = np.nan
    if crash:
        c, m = crash
        f.loc[f.index >= P(m), c] *= 0.7
    return f


def rates_of(R):
    g = R.index
    r = {cc: pd.Series(np.where(np.arange(len(g)) % 97 < 40, 0.5, 5.0), index=g) for cc in ("US", "JP", "DE", "GB", "CA")}
    rng = np.random.default_rng(9)
    g0 = pd.period_range("1960-01", "2010-12", freq="M")
    for cc in ("CH", "SE", "JP", "DE", "GB", "CA"):
        x = pd.Series(5 + np.cumsum(rng.normal(0, 0.2, len(g0))), index=g0).reindex(g)
        r[cc] = x if cc in ("CH", "SE") else r[cc]
    r["CH"][r["CH"].index < P("1972-01")] = np.nan
    r["TB3MS"] = r["US"]
    return r


# --------------------------------------------------------------------------------------------------- card inputs
import card_inputs as CI  # noqa: E402


def _csv(idx, vals):
    return ("date,value\n" + "".join("%s,%.6f\n" % (d.strftime("%Y-%m-%d"), v) for d, v in zip(idx, vals)
                                     if v == v)).encode()


def synth_card_files(late=False, seed=7):
    """Invented FRED-like files with the lock's names (no FRED data); a planted rebase in PCEPILFE's first release."""
    rng = np.random.default_rng(seed)
    end = "2012-12-01" if late else "2010-12-01"
    m = pd.date_range("1946-01-01", "2010-12-01", freq="MS")
    t = np.arange(len(m))
    ext = pd.date_range("2011-01-01", "2012-12-01", freq="MS") if late else pd.DatetimeIndex([])

    def mk(vals, start=None):
        s = pd.Series(vals, index=m)
        if start:
            s[s.index < pd.Timestamp(start)] = np.nan
        if late:
            s = pd.concat([s, pd.Series(9.87654321, index=ext)])
        return s
    ff = np.clip(5 + 4 * np.sin(t / 30.0), 0.1, None)
    gs2 = ff + 0.5 + np.sin(t / 17.0)
    gs10 = gs2 + 1 + np.sin(t / 40.0)
    infl = 4 + 3.5 * np.sin(t / 50.0)
    cpi = np.exp(np.cumsum(infl / 1200.0)) * 30
    pce = np.exp(np.cumsum((infl - 0.5) / 1200.0)) * 15
    m2 = np.exp(np.cumsum((6 + 4 * np.sin(t / 35.0)) / 1200.0)) * 200
    un = 6 + 2.5 * np.sin(t / 45.0)
    f = {}
    f["FEDFUNDS.csv"] = mk(ff, "1954-07-01")
    f["GS1.csv"] = mk(ff + 0.3, "1953-04-01")
    f["GS2.csv"] = mk(gs2, "1976-06-01")
    f["GS5.csv"] = mk(gs2 + 0.4 + 0.6 * np.sin(t / 23.0), "1953-04-01")
    f["GS10.csv"] = mk(gs10, "1953-04-01")
    f["BAA.csv"] = mk(gs10 + 2 + 0.6 * np.sin(t / 11.0))
    f["TWEXMMTH.csv"] = mk(100 * np.exp(np.cumsum(rng.normal(0, 0.02, len(t)))), "1973-01-01")
    f["WTISPLC.csv"] = mk(20 * np.exp(np.cumsum(rng.normal(0.003, 0.06, len(t)))))
    f["research/CPILFESL.csv"] = mk(cpi, "1957-01-01")
    f["research/CPILFESL_FR.csv"] = mk(cpi * (1 + rng.normal(0, 0.0003, len(t))), "1996-12-01")
    f["research/UNRATE.csv"] = mk(un, "1948-01-01")
    f["research/UNRATE_FR.csv"] = mk(un + rng.normal(0, 0.1, len(t)), "1960-03-01")
    f["research/M2SL.csv"] = mk(m2, "1959-01-01")
    f["M2SL.csv"] = mk(m2 * (1 + rng.normal(0, 0.0005, len(t))), "1980-01-01")
    f["research/PCEPILFE.csv"] = mk(pce, "1959-01-01")
    base = np.where(m >= pd.Timestamp("2003-11-01"), 0.93, 1.0)
    f["PCEPILFE.csv"] = mk(pce * base * (1 + rng.normal(0, 0.0003, len(t))), "2000-07-01")
    out = {k: _csv(v.index, v.values) for k, v in f.items()}
    days = pd.bdate_range("1990-01-02", "2012-12-31" if late else "2010-12-31")
    vix = pd.Series(20 + 8 * np.sin(np.arange(len(days)) / 70.0) + rng.normal(0, 1, len(days)), index=days)
    dtw = pd.Series(100 * np.exp(np.cumsum(rng.normal(0, 0.004, len(days)))), index=days)
    if late:
        vix[vix.index > pd.Timestamp("2010-12-31")] = 9.87654321
        dtw[dtw.index > pd.Timestamp("2010-12-31")] = 9.87654321
    dtw = dtw[dtw.index >= pd.Timestamp("2006-01-02")]
    out["VIXCLS.csv"] = _csv(vix.index, vix.values)
    out["DTWEXBGS.csv"] = _csv(dtw.index, dtw.values)
    out["manifest.json"] = b"{}"
    return out


def synth_ci(late=False):
    """An Inputs object on invented files (the lock check is bypassed: its own test uses the real lock)."""
    files = synth_card_files(late=late)
    ci = CI.Inputs.__new__(CI.Inputs)
    ci.lock_id = PB.CARD_LOCK
    ci._raw = {k: CI.parse_csv(v) for k, v in files.items() if k.endswith(".csv")}
    ci._cache = {}
    return ci, files


def run(check):
    tmp = tempfile.mkdtemp(prefix="preb_smoke_")
    try:
        _run(check, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _run(check, tmp):
    # ---------------------------------------------------------------- R1: strip identity
    ltd = PB.quarterly_ltd()
    st = PB.strip_of(P("1990-02"), ltd)
    check("R1 strip: month-end 1990-02 -> holding end 1990-04-02, contract 1 = June 1990, contract 8 = March 1992",
          PB.holding_end(P("1990-02")) == dt.date(1990, 4, 2) and st[0] == (1990, 6) and st[-1] == (1992, 3) and
          len(st) == 8, st)
    st2 = PB.strip_of(P("2010-11"), ltd)
    check("R1 strip: month-end 2010-11 -> holding end in January 2011 by calendar arithmetic, contract 1 = March 2011",
          PB.holding_end(P("2010-11")).year == 2011 and st2[0] == (2011, 3), st2)
    check("R1 ED code parse: <EDH0^9> = 1990-03, <EDZ2^8> = 1982-12, <EDZ0^1> = 2010-12, serial <EDG5^0> -> None",
          PB.ed_delivery("<EDH0^9>") == (1990, 3) and PB.ed_delivery("<EDZ2^8>") == (1982, 12) and
          PB.ed_delivery("<EDZ0^1>") == (2010, 12) and PB.ed_delivery("<EDG5^0>") is None)
    # ---------------------------------------------------------------- R1: no bend / planted bends / brute force
    days = pd.bdate_range("1970-01-02", "2010-12-31")
    flat = ed_contracts(bend=0.0)
    r0 = PB.r1(flat, days)
    check("R1: a strip linear in years to expiry has no curvature gap above cost: 0 qualifying, gate FAIL",
          r0["eligible"] > 1000 and r0["qualifying"] == 0 and not r0["pass"], (r0["eligible"], r0["qualifying"]))
    check("R1: month-ends from 1990-01 to 2010-11; every K_n has a first normal; all eight priced on every weekday",
          r0["start"] == P("1990-01") and r0["end"] == P("2010-11") and len(r0["first_normal"]) == 6 and
          r0["coverage"][0] == r0["coverage"][1], (r0["start"], r0["end"], r0["coverage"]))
    bent = ed_contracts(bend=5.0)
    rb = PB.r1(bent, days)
    check("R1: month-long bends of 5 bp per contract qualify (same sign on d and d1, above cost): share > 0.5, PASS",
          rb["pass"] and rb["share"] > 0.5, rb["share"])
    d = pd.Timestamp("1995-06-30")
    for n in (2, 5, 7):
        g_lib = None
        # recompute the library's gap at one month-end by its own pieces
        st = PB.strip_of(P("1995-06"), ltd)
        r = np.array([(100 - bent[k][d]) * 100 for k in st])
        gb, first = brute_gap(bent, days, d, n)
        # the library: normal over earlier month-ends of the same group
        me = pd.Series(days, index=days).groupby(days.to_period("M")).max()
        vals = []
        for p_, e in me.items():
            if p_ < P("1981-12") or e >= d:
                continue
            ste = PB.strip_of(p_, ltd)
            if all(e in bent.get(k, pd.Series(dtype=float)).index for k in ste[:n + 1]):
                rr = np.array([(100 - bent[k][e]) * 100 for k in ste[:n + 1]] + [np.nan] * (7 - n))
                if ste[n - 1][1] == st[n - 1][1]:
                    vals.append(PB.measures(rr)[("K", n)])
        g_lib = PB.measures(r)[("K", n)] - np.mean(vals)
        check("R1 K%d at 1995-06-30: the library's gap = an independent brute force (strip, rates, normal by group)" % n,
              abs(g_lib - gb) < 1e-9, (g_lib, gb))
    check("R1 cost: 2 x 0.5 x (2n + 4) / (n (n + 1)): K2 1.333, K7 0.321",
          abs(PB.r1_cost(2) - 8 / 6) < 1e-12 and abs(PB.r1_cost(7) - 18 / 56) < 1e-12)
    st_ = PB.strip_of(P("1996-03"), ltd)
    stale = ed_contracts(bend=5.0, stale=(st_[1], "1996-03-01", "1996-03-29"))
    rs = PB.r1(stale, days)
    check("R1: a contract unchanged over the 20 days before a month-end leaves that month's triples out (stale)",
          rs["excluded"]["stale"] >= rb["excluded"]["stale"] + 6, (rs["excluded"], rb["excluded"]))
    late = ed_contracts(bend=5.0, late=True)
    rl = PB.r1({k: v[v.index <= PB.SEAL] for k, v in late.items()}, pd.bdate_range("1970-01-02", "2010-12-31"))
    rl2 = PB.r1(late, pd.bdate_range("1970-01-02", "2012-12-31"))
    check("R1 seal: days and values after 2010-12-31 change nothing",
          (rl["eligible"], rl["qualifying"]) == (rl2["eligible"], rl2["qualifying"]) == (rb["eligible"],
                                                                                         rb["qualifying"]))
    # ---------------------------------------------------------------- F0
    check("F0 episodes: months 0..47 -> 1; gaps of 11 months -> 1; a gap of 12 starts a new one",
          PB.episodes(range(48)) == 1 and PB.episodes([0, 11, 22]) == 1 and PB.episodes([0, 12, 24]) == 3 and
          PB.episodes([]) == 0)
    f = PB.f0([P("1980-01") + i for i in range(48)] + [P("1990-01"), P("2000-01")], "x")
    g = PB.f0([P("1980-01") + i for i in range(47)] + [P("1990-01"), P("2000-01")], "y")
    check("F0: 50 held months in 3 episodes judgeable; 49 held months... 47 + 2 = 49 >= 48 too; 47 alone not",
          f["judgeable"] and g["judgeable"] and not PB.f0([P("1980-01") + i for i in range(47)], "z")["judgeable"])
    # ---------------------------------------------------------------- card 1 R5
    R, D, S, gspc = panel()
    vol = PB.card_vol(R, D)
    fxv = fx_values(R)
    r5 = PB.card1_r5(fxv, vol)
    t = r5["trig"][15]
    check("card 1 R5: a 30% GBP fall triggers GBP at G 15 in its month (6-month change <= median - 15)",
          bool(t.at[P("1992-10"), "GBP"]) and not t.loc[P("1992-04"), "GBP"], None)
    m6 = 100 * (fxv / fxv.shift(6) - 1)
    hand = (m6.loc[P("1992-10"), "GBP"] <= m6.loc[P("1992-10")].median() - 15)
    check("card 1 R5 trigger by hand equals the library", bool(hand) == bool(t.at[P("1992-10"), "GBP"]))
    lp = r5["legs"]["stock"]["eq_gb_ftse"]
    lb = r5["legs"]["bond"]["bd_gb_10y"]
    last_trig = max(p for p, v in r5["trig"][10]["GBP"].items() if v and p <= P("1993-12"))
    check("card 1 R5: the GBP stock leg is held from the trigger to 12 months after the last trigger, then flat; the "
          "bond leg only in the 'stocks and bond' versions (half the versions)",
          lp[P("1992-10")] > 0 and lp[last_trig + 12] > 0 and lp[last_trig + 13] == 0 and lb[P("1992-10")] > 0 and
          abs(lb[P("1992-10")] - 0.40 / vol.at[P("1992-10"), "bd_gb_10y"] / 2 / 2) < 1e-12, (last_trig,))
    cnt = fxv.notna().sum(axis=1)
    check("card 1 R5: no trigger in months with fewer than three currencies with data",
          not r5["trig"][10][cnt.reindex(r5["trig"][10].index) < 3].any().any())
    d1 = PB.c1d1(r5["cond_months"])
    check("C1-D1: episodes of the condition months (G 10, any currency) by the 12-month rule",
          d1["episodes"] == PB.episodes(r5["cond_months"]) and d1["pass"] == (d1["episodes"] >= 6), d1)
    book = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    book["eq_gb_ftse"] = 1.0
    book["bd_gb_10y"] = -1.0
    d2 = PB.c1d2(r5, book)
    held_st = r5["legs"]["stock"][PB.in_dec(r5["legs"]["stock"].index)]
    n_st = int((held_st != 0).to_numpy().sum())
    n_gb = int((held_st["eq_gb_ftse"] != 0).sum())
    check("C1-D2: the stock-leg share = GBP stock-months / all held stock-months (book long FTSE only); bond leg 0",
          d2["stock"]["n"] == n_st and abs(d2["stock"]["share"] - n_gb / n_st) < 1e-12 and d2["bond"]["share"] == 0,
          d2)
    # ---------------------------------------------------------------- C2-D1
    rates = rates_of(R)
    c2 = PB.c2d1(R, rates)
    lo, hi = [], []
    for cc, eq, bd in PB.C2_COUNTRIES:
        x = R.loc[P("1975-01"):P("2010-12"), eq].dropna()
        q = np.percentile(x, 20)
        for p_ in x.index[x <= q]:
            b, rr = R.at[p_, bd], rates[cc].get(p_)
            if b == b and rr == rr:
                (lo if rr < 1.0 else hi).append(b)
    check("C2-D1: pooled low-rate / other worst-fifth bond means by hand",
          c2["pooled"]["n_low"] == len(lo) and abs(c2["pooled"]["mean_low"] - np.mean(lo)) < 1e-15 and
          abs(c2["pooled"]["mean_other"] - np.mean(hi)) < 1e-15, c2["pooled"])
    ok = len(lo) >= 30 and np.mean(hi) > 0 and np.mean(lo) < 0.5 * np.mean(hi)
    check("C2-D1 gate by hand", c2["pooled"]["pass"] == ok)
    R2 = R.copy()
    for cc, eq, bd in PB.C2_COUNTRIES:
        x = R2.loc[P("1975-01"):P("2010-12"), eq]
        w = x.index[x <= np.nanpercentile(x, 20)]
        R2.loc[w, bd] = np.where(rates[cc].reindex(w) < 1.0, -0.01, 0.02)
    check("C2-D1: bonds that lose in low-rate stock falls and gain otherwise -> PASS",
          PB.c2d1(R2, rates)["pooled"]["pass"])
    # ---------------------------------------------------------------- card 3 R4
    lm = lseg_monthly()
    lv = gspc.copy()
    spx_me = lv.groupby(pd.DatetimeIndex(lv.index).to_period("M")).last()
    ey = spx_me * (4.5 + 2.5 * np.sin(np.arange(len(spx_me)) / 20.0)) / 100.0
    lm[PB.EPS_SID] = ey[ey.index >= P("1985-01")]
    r4 = PB.card3_r4(lm[PB.EPS_SID], spx_me, rates["TB3MS"], vol["eq_us_spx"])
    E = 100 * lm[PB.EPS_SID].reindex(vol.index) / spx_me.reindex(vol.index)
    on1 = (E - rates["TB3MS"]) < 1.0
    p_ = next(p for p, v in on1.items() if v and p >= P("1986-01") and vol.at[p, "eq_us_spx"] == vol.at[p, "eq_us_spx"])
    check("card 3 R4: on while E - TB3MS < B; short; starts at the first EPS month",
          r4["pos"][p_] < 0 and r4["start"] == P("1985-01") and (r4["pos"][r4["pos"].index < P("1985-01")] == 0).all())
    bk = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    bk["eq_us_spx"] = -1.0
    c3 = PB.c3d1(r4, bk)
    check("C3-D1: a book always short the S&P -> share 1.0 -> dropped before B2; always long -> 0 -> kept",
          c3["share"] == 1.0 and c3["outcome"] == "dropped before B2" and
          PB.c3d1(r4, -bk)["outcome"] == "kept", c3)
    # ---------------------------------------------------------------- card 4
    days_ny = EX.nyse_days(gspc=gspc)
    c4 = PB.card4_days(gspc, days_ny, vol["eq_us_spx"])
    s1 = c4["card 4 R1"]["sum"]
    E_ = pd.DatetimeIndex(days_ny)
    yrs_above, yrs_below = [], []
    for Y in range(1975, 2010):
        a = PB._on_before(E_, "%d-10-31" % Y)
        bar = gspc[PB._on_before(E_, "%d-12-31" % (Y - 1))]
        c_oct = gspc[E_[E_.get_loc(a) - 1]]
        dec = PB._on_before(E_, "%d-12-15" % Y)
        c_dec = gspc[E_[E_.get_loc(dec) - 1]]
        b = PB._on_before(E_, "%d-01-15" % (Y + 1))
        nov = s1[(s1.index > a) & (s1.index <= dec)]          # only the October entries are active
        if c_oct > bar:
            yrs_above.append(Y)
            ok_y = (nov == 3).all()
        elif c_oct < bar:
            yrs_below.append(Y)
            ok_y = (nov == 0).all()                         # A + B + C = 1 + 0 - 1: exact cancellation
        else:
            ok_y = True
        jan = s1[(s1.index > dec) & (s1.index <= b)]
        want = (3 if c_oct > bar else (0 if c_oct < bar else 1)) + (3 if c_dec > bar else (0 if c_dec < bar else 1))
        if not (ok_y and (jan == want).all()):
            break
    else:
        Y = None
    check("card 4 R1: the six versions sum to 3 per entry above last year's close, 0 below (form A + B + C = 1 + 0 "
          "- 1, an exact cancellation), over (entry, last day <= 15 January]", Y is None and yrs_above and yrs_below,
          Y)
    check("card 4 R1: the direction sum is an exact integer per day (cancellation is exact)",
          s1.dtype.kind == "i")
    check("F0 (entry correction of item 5 F0 g): card 4 R2 and R4 have one episode; R1's episodes follow the years "
          "the averaged rule is non-zero (data-dependent)",
          PB.episodes(c4["card 4 R2"]["months"]) == 1 and PB.episodes(c4["card 4 R4"]["months"]) == 1 and
          PB.episodes(c4["card 4 R1"]["months"]) == PB.episodes(
              [m for m in c4["card 4 R1"]["months"]]) and PB.episodes(c4["card 4 R1"]["months"]) > 1,
          [PB.episodes(c4[k]["months"]) for k in ("card 4 R1", "card 4 R2", "card 4 R4")])
    s2 = c4["card 4 R2"]["sum"]
    X = PB._on_before(pd.DatetimeIndex(days_ny), PB._third_friday(1995, 6))
    wdays = s2[(s2.index <= X) & (s2.index > X - pd.Timedelta(days=30))]
    check("card 4 R2: before the June 1995 expiry the window sum is 4 (all versions) on the last 12 days and the "
          "X+1 day holds 2 (two exit-next-day versions)",
          (wdays.iloc[-12:] == 4).all() and s2[s2.index > X].iloc[0] == 2, wdays.tail(16).tolist())
    s4 = c4["card 4 R4"]["sum"]
    T = PB._on_before(pd.DatetimeIndex(days_ny), "1997-05-31")
    i = E_.get_loc(T)
    prevm = PB._on_before(E_, "1997-04-30")
    sg = np.sign(gspc[E_[i - 4]] / gspc[prevm] - 1)
    check("card 4 R4: d = 3 holds the month-to-date sign from T-3 to day 3 of the next month (by hand)",
          s4[E_[i - 2]] in (sg, sg + np.sign(gspc[E_[i - 6]] / gspc[prevm] - 1)) and s4[E_[i - 3]] != 2 * sg + 7)
    # ---------------------------------------------------------------- card 5 R1
    Pm = {"cm_copper": lm["HP:HGc1|CLOSE"], "cm_wti": lm["HP:CLc1|CLOSE"]}
    trg = PB.triggers(Pm["cm_copper"])
    pc = Pm["cm_copper"]
    hand = [p for i_, (p, v) in enumerate(pc.items()) if i_ >= 120 and v > pc.iloc[:i_].max()]
    check("card 5 R1 triggers: new high over every earlier value, at least 120 earlier values (by hand)",
          [p for p, v in trg.items() if v] == hand, (len(hand),))
    r5c = PB.card5_r1(Pm, vol)
    if hand:
        t0 = hand[-1]
        cu = r5c["pos"]["cm_copper"]
        check("card 5 R1: copper held 36 months after its last trigger (H 36 versions), at half size 25-36 months "
              "after (only the H 36 versions)",
              t0 + 36 > P("2010-12") or (cu.get(t0 + 36, 0) > 0 and (t0 + 37 > P("2010-12") or cu.get(t0 + 37) == 0)))
    avg, nv = PB.trend12_avg_sign(R, D)
    c5 = PB.c5d1(r5c, avg, book)
    rp = r5c["pos"][PB.in_dec(r5c["pos"].index)]
    hm = (rp != 0)
    hand_s = float((hm & (avg.reindex(index=rp.index, columns=rp.columns) > 0)).to_numpy().sum()) / max(1, hm.to_numpy().sum())
    check("C5-D1: share of held market-months with the four 12-month Trend versions long by average sign (by hand)",
          nv == 4 and abs(c5["share"] - hand_s) < 1e-12 and c5["n"] == int(hm.to_numpy().sum()), (c5["share"], hand_s))
    br = PB.breaks(pc)
    tm = [p for p, v in trg.items() if v]
    hand_b = [p for p in tm if p <= P("2008-12") and not any((p - k) in tm for k in range(1, 13))]
    check("C5-D2 breaks: first trigger after 12 months without one, to 2008-12; higher = P(t+24) > P(t)",
          [p for p, _ in br] == hand_b and all(h == (pc[p + 24] > pc[p]) for p, h in br if h is not None))
    rising = pd.Series(np.r_[np.full(130, 100.0), np.linspace(101, 200, 200)],
                       index=pd.period_range("1980-01", periods=330, freq="M"))
    saw = rising.copy()
    for k_ in range(130, 330, 20):
        saw.iloc[k_ + 10:k_ + 20] = saw.iloc[k_] - 50
    c52 = PB.c5d2({"a": saw}, {"c": rising}, {"g": rising})
    check("C5-D2 gate: fewer than 10 breaks in a class -> FAIL whatever the shares", not c52["pass"] and
          c52["grains"]["breaks"] < 10, (c52["slow"], c52["grains"]))
    # ---------------------------------------------------------------- 1.1.0: card inputs reader
    ci, cfiles = synth_ci()
    raw = CI.parse_csv(cfiles["WTISPLC.csv"])
    w = CI.to_month(raw)
    check("card inputs: WTISPLC at lag 1 (the value used at t is month t-1); FEDFUNDS lag 0",
          abs(ci.m("WTISPLC")[P("1990-05")] - w[P("1990-04")]) < 1e-12 and
          abs(ci.m("FEDFUNDS")[P("1990-05")] - CI.to_month(CI.parse_csv(cfiles["FEDFUNDS.csv"]))[P("1990-05")]) < 1e-12)
    dv = CI.parse_csv(cfiles["VIXCLS.csv"])
    check("card inputs: a daily series enters as the mean of the month's daily values (VIXCLS, lag 0)",
          abs(ci.m("VIXCLS")[P("1995-03")] - dv[(dv.index >= "1995-03-01") & (dv.index <= "1995-03-31")].mean()) < 1e-9)
    cl, fl = ci.fr_change("CPILFESL", 12)
    lat = CI.to_month(CI.parse_csv(cfiles["research/CPILFESL.csv"]))
    fr = CI.to_month(CI.parse_csv(cfiles["research/CPILFESL_FR.csv"]))
    check("card inputs: CPILFESL 12-month change from two first-release values at lag 1 (2005-06 uses 2005-05 / 2004-05)",
          abs(cl[P("2005-06")] - 100 * (fr[P("2005-05")] / fr[P("2004-05")] - 1)) < 1e-9 and not fl[P("2005-06")])
    check("card inputs: before the first vintage (1996-12) the change uses latest values, flagged",
          abs(cl[P("1990-06")] - 100 * (lat[P("1990-05")] / lat[P("1989-05")] - 1)) < 1e-9 and bool(fl[P("1990-06")]))
    check("card inputs: the planted PCEPILFE rebase (2003-11) is the only break; changes whose window holds it use latest "
          "values, flagged; later ones are first release again",
          ci.breaks("PCEPILFE") == [P("2003-11")] and bool(ci.fr_change("PCEPILFE", 12)[1][P("2004-06")]) and
          not ci.fr_change("PCEPILFE", 12)[1][P("2005-06")])
    ul, uf = ci.fr_level("UNRATE")
    check("card inputs: UNRATE level at lag 1, first release from 1960-03, latest (flagged) before",
          bool(uf[P("1955-06")]) and not uf[P("1980-06")] and
          abs(ul[P("1980-06")] - CI.to_month(CI.parse_csv(cfiles["research/UNRATE_FR.csv"]))[P("1980-05")]) < 1e-12)
    late_ci, _lf = synth_ci(late=True)
    check("card inputs seal: values dated after 2010-12-31 are dropped on parsing",
          max(late_ci._raw["GS10.csv"].index) <= pd.Timestamp("2010-12-31") and
          late_ci.m("VIXCLS").index.max() <= P("2010-12"))
    try:
        CI.Inputs.from_files(cfiles)
        refused = False
    except CI.CardInputsError:
        refused = True
    check("card inputs lock: files that differ from LOCK_CARD_v1 are refused before any value is parsed", refused)
    try:
        real = {pth: subprocess.check_output(["git", "-C", REPO, "show", "%s:%s" % (CI.COMMIT, pth)],
                                             stderr=subprocess.DEVNULL) for pth in CI.FILES}
    except Exception:  # noqa: BLE001
        real = None
    if real is None:
        check("card inputs lock (real files): commit not fetched here, check skipped", True)
    else:
        okl = CI.Inputs.from_files(real).lock_id == PB.CARD_LOCK == CI.LOCK_ID
        bad = dict(real)
        bad["GS2.csv"] = bad["GS2.csv"] + b"\n"
        try:
            CI.Inputs.from_files(bad)
            r2 = False
        except CI.CardInputsError:
            r2 = True
        check("card inputs lock (real files from git, hashes only, no value used): the registered files pass with lock "
              "id 6c154f7d...; one changed byte is refused", okl and r2)
    # ---------------------------------------------------------------- 1.1.0: card rules by hand
    ix = R.index
    r1c = PB.card1_rules(ci, R, vol, spx_me)
    WTI, TW, FFs, G10 = (ci.m(x).reindex(ix) for x in ("WTISPLC", "TWEXMMTH", "FEDFUNDS", "GS10"))
    t0 = next(p for p in r1c["card 1 R1"]["cond_months"] if p >= P("1980-01"))
    hand = any((WTI[t0] > WTI[t0 - L]) and (TW[t0] > TW[t0 - L]) and (rr[t0] > rr[t0 - L])
               for L in (6, 12) for rr in (FFs, G10))
    check("card 1 R1: a condition month satisfies oil, dollar and rate all above their level L months ago (by hand)",
          hand, t0)
    c45 = PB.r4_state(ci, 4.5)
    cc, _f = ci.fr_change("CPILFESL", 12)
    tt = next(p for p, v in c45.items() if v and p >= P("1975-01"))
    check("card 1 R4: state at 4.5 = core CPI change > 4.5 and FEDFUNDS below it (by hand); R4 legs short bonds, "
          "B adds short S&P and a long basket", cc[tt] > 4.5 and ci.m("FEDFUNDS")[tt] < cc[tt] and
          (r1c["card 1 R4"]["legs"]["10-year"].loc[tt] < 0).all() and
          (r1c["card 1 R4"]["legs"]["basket"].loc[tt].fillna(0) >= 0).all(), tt)
    check("card 1 R4: no tail (held months = state months with a volatility)",
          set(PB.nonzero_months(r1c["card 1 R4"]["legs"]["10-year"])) <= set(r1c["card 1 R4"]["cond_months"]))
    v2c = PB.card2_rules(ci, R, vol, spx_me)
    kp = PB.c2d2(v2c["card 2 R1"], c45.reindex(ix))
    on, _h = v2c["card 2 R1"][("0.0", False)]
    om = PB.months_of(on)
    ins = sum(1 for p in om if bool(c45.reindex(ix).fillna(False)[p])) / max(1, len(om))
    check("C2-D2: on-months, episodes and the share inside card 1 R4's 4.5 state by hand; kept = >= 24, >= 3 and <= 2/3",
          kp[("0.0", False)]["on"] == len(om) and abs(kp[("0.0", False)]["inside"] - ins) < 1e-12 and
          kp[("0.0", False)]["keep"] == (len(om) >= 24 and PB.episodes(om) >= 3 and ins <= 2 / 3))
    rules3, d32, aux = PB.card3_rules(ci, R, vol, rates)
    rngf = FFs.rolling(12, min_periods=12).max() - FFs.rolling(12, min_periods=12).min()
    qh = int(((rngf < 0.5) & rngf.notna())[(ix >= P("1975-01")) & (ix <= P("2010-12"))].sum())
    check("C3-D2: gate-off months (FEDFUNDS 12-month range < 0.50, 1975-2010) by hand; gate kept iff >= 60",
          d32["gate_off_months"] == qh and d32["gate_kept"] == (qh >= 60))
    check("card 3 R1: 16 versions with the gate (8 without); R2 long 2-year / short 10-year at D2 / D10",
          rules3["card 3 R1"]["versions"] == (16 if d32["gate_kept"] else 8) and
          PB.card3_r1(rates, R, vol, FFs, with_gate=False)["versions"] == 8 and
          ((rules3["card 3 R2"]["legs"]["2-year"]["bd_us_2y"] >= 0) &
           (rules3["card 3 R2"]["legs"]["10-year"]["bd_us_10y"] <= 0)).all())
    fr_ = PB.fixed_runs(pd.Series([0, 1, 1, 1, -1, -1, 0, 1]), pd.Series([1., 2., 3., 4., 5., 6., 7., 8.]))
    check("card 3 fixed size: a notional is fixed at the first month of a same-direction run",
          list(fr_) == [0.0, 2.0, 2.0, 2.0, -5.0, -5.0, 0.0, 8.0], list(fr_))
    v45, st45 = PB.card4_r5(ci, R, aux)
    c5v = PB.core_cpi(ci)[0].reindex(ix)
    on1 = v45[1][0]
    tq = next(p for p, v in on1.items() if v and p >= P("1980-01"))
    check("card 4 R5: version 1 on while core CPI's change is below its value 6 months earlier (by hand); version 2 "
          "inside version 1", c5v[tq] < c5v[tq - 6] and bool((v45[2][0] <= v45[1][0]).all()))
    sc = pd.DataFrame({"bd_us_2y": 1.0, "bd_us_10y": -1.0}, index=ix)
    c42 = PB.c4d2(v45, pd.Series(True, index=ix), sc)
    check("C4-D2: card 3 R2 always on and Trend always long 2-year / short 10-year -> both shares 1.0, R5 not "
          "registered; never -> R5 stays", c42["not_registered"] and
          not PB.c4d2(v45, pd.Series(False, index=ix), -sc)["not_registered"])
    c41 = PB.c4d1(ci, gspc)
    check("C4-D1: three windows; gate = all three median ratios >= 1.25",
          len(c41["windows"]) == 3 and c41["pass"] == all(x["ok"] for x in c41["windows"].values()))
    # ---------------------------------------------------------------- LsegView on a mini lsegdata store
    wd = os.path.join(tmp, "work")
    root = os.path.join(wd, "lseg")
    os.makedirs(os.path.join(root, "design"))
    rows = []
    cat = []
    for k_, s in list(flat.items())[:3]:
        code = "<ED%s%d^%d>" % ("FGHJKMNQUVXZ"[k_[1] - 1], k_[0] % 10, (k_[0] // 10) % 10)
        sid = "DS:%s|X" % code
        for d_, v in s.items():
            rows.append((sid, "D", d_, d_, float(v), 0))
        cat.append({"file": "L14x", "code": code, "fn": "DS", "per": "D", "status": "ok", "series_id": sid,
                    "duplicate_of": ""})
    for d_, v in lm["HP:HGc1|CLOSE"].items():
        ts = d_.to_timestamp(how="end").normalize()
        rows.append(("HP:HGc1|CLOSE", "M", ts, ts, float(v), 0))
    cat.append({"file": "L4b", "code": "HGc1", "fn": "HP", "per": "M", "status": "ok", "series_id": "HP:HGc1|CLOSE",
                "duplicate_of": ""})
    for d_, v in lm["HP:HGc1|CLOSE"].items():
        ts = d_.to_timestamp(how="end").normalize()
        rows.append(("HP:LCCc1|CLOSE", "M", ts, ts, float(v), 0))
    cat.append({"file": "L4b", "code": "LCCc1", "fn": "HP", "per": "M", "status": "ok", "series_id": "HP:LCCc1|CLOSE",
                "duplicate_of": "", "untouched": 1})
    cat.append({"file": "L14x", "code": "<EDG5^0>", "fn": "DS", "per": "D", "status": "ok",
                "series_id": "DS:<EDG5^0>|X", "duplicate_of": ""})
    long = pd.DataFrame(rows, columns=["sid", "per", "obs", "key", "value", "hol"])
    long["obs"] = pd.to_datetime(long["obs"]).astype("datetime64[ns]")
    long["key"] = pd.to_datetime(long["key"]).astype("datetime64[ns]")
    long["hol"] = long["hol"].astype("int8")
    long = long.sort_values(["per", "sid", "obs"], kind="mergesort").reset_index(drop=True)
    long.to_pickle(os.path.join(root, "design", "long.pkl"))
    c = pd.DataFrame(cat)
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
    lid = LD.lock_id_of(man)
    open(os.path.join(root, "LOCK"), "w").write(lid)
    got, why = PB.lseg_lock_of(wd)
    check("lseg_lock_of: reads the lock id from the manifest and LOCK before any table", got == lid and why == "ok")
    open(os.path.join(root, "LOCK"), "w").write("0" * 64)
    check("lseg_lock_of: LOCK not matching the manifest -> None", PB.lseg_lock_of(wd)[0] is None)
    open(os.path.join(root, "LOCK"), "w").write(lid)
    lvw = PB.LsegView(LD.Panel(wd))
    ec = lvw.ed_contracts()
    check("LsegView: three quarterly ED contracts parsed (serial G5 dropped); daily series equal the stored values; "
          "monthly on a Period index", len(ec) == 3 and (1982, 3) in ec and
          np.allclose(lvw.daily(ec[(1982, 3)]).to_numpy(), flat[(1982, 3)].to_numpy()) and
          isinstance(lvw.monthly("HP:HGc1|CLOSE").index, pd.PeriodIndex), list(ec))
    try:
        lvw.panel.asof("2011-01-03")
        sealed = False
    except LD.HoldoutSealed:
        sealed = True
    check("LsegView: an as-of date after 2010-12-31 is refused (sealed)", sealed)
    try:
        lvw.monthly("HP:LCCc1|CLOSE")
        hidden = False
    except KeyError:
        hidden = True
    check("LsegView (correction 2): a held-back (untouched) instrument such as London cocoa is hidden", hidden)
    # ---------------------------------------------------------------- report end to end
    mock = MockLseg(bent, lm)
    lines = []
    ci0, _cf = synth_ci()
    res = PB.report(R, D, S, gspc, fxv, rates, mock, ci0, out=lines.append)
    txt = "\n".join(lines)
    need = ["R1 GATE", "C1-D1 |", "C1-D2 | card 1 R5 stock leg", "C2-D1 GATE", "C3-D1 | card 3 R4", "C5-D1 | card 5 R1",
            "C5-D2 GATE", "C5-D2 | reported line not computed", "F0 | card 4 R1", "F0 | card 5 R1", "PRE-B SUMMARY", "CORE BOOK READING"]
    check("report: every registered line is printed and nothing is BLOCKED (1.1.0)", all(x in txt for x in need) and
          "BLOCKED" not in txt,
          [x for x in need if x not in txt])
    check("report: the R1 gate equals r1() on the same inputs",
          res["res"]["R1"]["qualifying"] == PB.r1(bent, EX.nyse_days(gspc=gspc))["qualifying"])
    check("report printing: no number with 5+ decimals", not re.findall(r"\d\.\d{5,}", txt), re.findall(
        r".{30}\d\.\d{5,}", txt)[:3])
    small = [x for x in lines if re.search(r"\| n (\d+), sign", x)]
    check("report printing: values under 60 months appear as count and sign only",
          all(int(m) < 60 for x in small for m in re.findall(r"n (\d+), sign", x)))
    rows_ = PB.trial_rows(res, PB.A1_PANEL_ID, CF.ENGINE_VERSION)
    check("trial rows: 12 diag rows, no Sharpe column, ids R1..F0, LSEG lock in the note",
          len(rows_) == 12 and all(r["family"] == "diag" and "sr_9010" not in r for r in rows_) and
          [json.loads(r["config"])["diag"] for r in rows_] == list(PB.DIAG_IDS) and PB.LSEG_LOCK[:16] in rows_[0]["note"])
    RL, DL_, SL_, gl = panel(late=True)
    lml = lseg_monthly(late=True)
    lml[PB.EPS_SID] = pd.concat([lm[PB.EPS_SID], pd.Series(9.87654321, index=pd.period_range("2011-01", "2012-12",
                                                                                               freq="M"))])
    fxl = fx_values(RL)
    fxl.loc[fxl.index > P("2010-12")] = 9.87654321
    ratl = rates_of(RL)
    for k_ in ratl:
        ratl[k_] = ratl[k_].copy()
        ratl[k_][ratl[k_].index > P("2010-12")] = 9.87654321
    lines2 = []
    PB.report(RL, DL_, SL_, gl, fxl, ratl, MockLseg(ed_contracts(bend=5.0, late=True), lml), synth_ci(late=True)[0],
              out=lines2.append)
    strip_t = lambda L: list(L)  # noqa: E731
    check("report seal: values dated after 2010-12 (panel, FX, rates, LSEG monthly and daily, card inputs) change no "
          "line",
          strip_t(lines) == strip_t(lines2), [(a_, b_) for a_, b_ in zip(lines, lines2) if a_ != b_][:2])
    # ---------------------------------------------------------------- the job in the PC layout
    import a1_panel_smoke as A1S
    loc = os.path.join(tmp, "local")
    lib = os.path.join(loc, "lib")
    os.makedirs(lib)
    shutil.copytree(os.path.join(REPO, "gm"), os.path.join(lib, "gm"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    bq = os.path.join(REPO, "tools", "bbgq")
    for rel in ("lib/gm_engine.py", "lib/bbg_panel.py", "lib/bbgdata.py", "lib/a1_panel.py", "lib/a2_batch.py",
                "lib/diag_a2.py", "lib/diag_preb.py", "lib/card_inputs.py", "live_sources.csv", "untouched_markets.csv",
                "engine_ref.json"):
        shutil.copy(os.path.join(bq, rel), os.path.join(lib, os.path.basename(rel)))
    for f_ in os.listdir(os.path.join(REPO, "tools", "lseg")):
        if f_ in ("lsegdata.py", "lseg_rules.py") or f_.endswith(".csv"):
            shutil.copy(os.path.join(REPO, "tools", "lseg", f_), os.path.join(lib, f_))
    blocks, _free = A1S.scenario()
    A1S.write_store(os.path.join(loc, "work"), blocks)
    env = dict(os.environ, BBG_WORK=os.path.join(loc, "work"), PYTHONPATH="")
    env.pop("PYTHONDONTWRITEBYTECODE", None)
    job_src = open(os.path.join(bq, "jobs", "gm_diag_preb_v1.py"), encoding="utf-8").read()
    pb_sha = hashlib.sha256(open(os.path.join(bq, "lib", "diag_preb.py"), "rb").read()).hexdigest()
    job_src = re.sub(r'"diag_preb.py": "[^"]*"', '"diag_preb.py": "%s"' % pb_sha, job_src)   # the build note pins it
    ci_sha = hashlib.sha256(open(os.path.join(bq, "lib", "card_inputs.py"), "rb").read()).hexdigest()
    job_src = re.sub(r'"card_inputs.py": "[^"]*"', '"card_inputs.py": "%s"' % ci_sha, job_src)
    job = os.path.join(tmp, "gm_diag_preb_v1.py")
    open(job, "w", encoding="utf-8").write(job_src)

    def go():
        q = subprocess.run([sys.executable, job], cwd=loc, env=env, capture_output=True, text=True, timeout=600)
        return q.stdout + q.stderr
    o0 = go()
    check("job (PC layout): gm code, engine_ref, config hashes, 10 lib files and the trial-log digest PASS (12 'PASS lib' lines); no A2 "
          "report -> STOP before any store", "PASS gm code vs reference" in o0 and o0.count("PASS lib ") == 12 and
          "FAIL A2 report gm_a2_v1.txt: missing" in o0 and "lock id" not in o0, o0[-1200:])
    os.makedirs(os.path.join(loc, "results"))
    open(os.path.join(loc, "results", "gm_a2_v1.txt"), "w").write(DS.a2_report_text())
    import core_v1_smoke as CVS
    open(os.path.join(loc, "results", "gm_diag_v1.txt"), "w").write(CVS.diag_text())
    o1 = go()
    check("job: A2 and diagnostics reports PASS, no Core book v1 report -> STOP before any store",
          "PASS A2 report" in o1 and "PASS diagnostics report" in o1 and "FAIL Core book v1 report" in o1 and
          "lock id" not in o1, o1[-900:])
    open(os.path.join(loc, "results", "gm_core_v1.txt"), "w").write(
        "CORE BOOK V1 EMPTY | no Core candidate passed\nCORE V1 JOB DONE\n")
    o2 = go()
    check("job: Core book v1 report PASS; a non-LOCK_v2 Bloomberg store -> STOP before any value is read (LSEG not "
          "opened)", "PASS Core book v1 report" in o2 and "FAIL Bloomberg store lock id" in o2 and
          "STOP: the Bloomberg store is not LOCK_v2 (nothing read)" in o2 and "LSEG store" not in o2, o2[-900:])
    with open(os.path.join(lib, "diag_preb.py"), "a") as f_:
        f_.write("\n# changed\n")
    o3 = go()
    check("job: a changed diag_preb.py stops it at the hash check", "FAIL lib diag_preb.py" in o3 and
          "STOP: lib file differs from the registered build: diag_preb.py" in o3, o3[-600:])
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
    print("PREB SMOKE " + ("PASSED" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
