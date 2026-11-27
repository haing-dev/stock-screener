"""diag_preb: the pre-B diagnostics of TESTING_PROTOCOL 7.5 order item 3 (7.6 step 7), as registered in gm/CHANGES.md
"Pre-B diagnostics" (2026-11-27, before this code). Runs where the A1 panel and the LSEG store exist (the user's PC);
tested in the cloud on synthetic panels and a mock LSEG store only.

Run (entry item 4 and addendum 1.1.0 A1): R1 (Strip reversion's gate, LSEG Eurodollar contracts), C1-D1 / C1-D2 (card 1
R1-R5), C2-D1, C2-D2 (card 2 R1, R2), C3-D2 then C3-D1 (card 3 R1-R4), C4-D1, C4-D2 (card 4 R5), C5-D1, C5-D2 and F0
on every card rule as it would enter B2. Card inputs: card_inputs.Inputs (LOCK_CARD_v1, FRED / ALFRED first release
from the macro-data branch). Nothing is blocked in 1.1.0.
The reference book: the A2-final book config.A1_INCUMBENT (77374d7bef), engine gm-2.2.1, A1 panel e7f98d44..., its
book.run "pos". Card rule positions are minimal signals from the specs (positions only, no returns of the rules).
Printing (entry item 7): shares, means and gaps over at least 60 months only, else count and sign.

API
  core_facts(path)                       gm_core_v1 report: CORE V1 JOB DONE and CORE BOOK V1 EMPTY
  LsegView(panel)                        as-of 2010-12-31 view of lsegdata.Panel: monthly / daily / ed_contracts
  r1(contracts, days)                    R1 (entry item 5 R1 a-k)
  card1_r5(fxv, vol), card3_r4(eps, spx_me, tb3, vol_spx), card4_days(gspc, days, vol_spx),
  card5_r1(P, vol)                       minimal rule positions (entry item 5)
  card1_rules, card2_rules, card3_rules, card3_r1, card4_r5           1.1.0 rule positions (addendum A3-A6)
  c2d2(...), c4d1(...), c4d2(...)        1.1.0 gates
  f0(...), c1d1(...), c1d2(...), c2d1(...), c3d1(...), c5d1(...), c5d2(...)
  report(R, D, S, gspc, fxv, rates, lseg, ci, out, ...)   the registered pass; returns the result dict
  trial_rows(res, panel_id, engine_version)          gm/trials.csv rows of family 'diag'
"""
import datetime as dt
import json
import os
import re

import numpy as np
import pandas as pd

VERSION = "diag_preb-1.1.0"   # 1.1.0 (addendum): every row on the card inputs (card_inputs-1.0.0)
A1_PANEL_ID = "e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43"
LOCK_V2 = "d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9"
LSEG_LOCK = "90322681b9f989cc24393ae7de4fe24bf5af2f32074ffa6400b1cbed09c4074c"          # LOCK_LSEG_v5
ENGINE = "gm-2.2.1"
REF_SHA = "cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39"
CFG_HASHES = {"BASE": "f1d682c384", "CANDIDATE": "438a092b53", "A1_INCUMBENT": "77374d7bef",
              "A2_CHALLENGER": "1faa343535"}
FINAL_NAME, FINAL_HASH = "gm-2.0.4-candidate-x1", "77374d7bef"
TRIAL_ROWS_SHA = "f200d02ce574f002753c0d9ad54ae7a082c8e7f3d2ad120a14905fcf498e268a"     # entry item 9 (40 + Core v1)
TRIAL_ROWS_N = 41
A2_REPORT, DIAG_REPORT, CORE_REPORT = "gm_a2_v1.txt", "gm_diag_v1.txt", "gm_core_v1.txt"
CORE_NEEDS = ("CORE V1 JOB DONE", "CORE BOOK V1 EMPTY")
SEAL = pd.Timestamp("2010-12-31")
DEC = (pd.Period("1975-01", "M"), pd.Period("2010-11", "M"))        # decision months (7.3 item 5)
MIN_PRINT = 60
DIAG_IDS = ("R1", "C1-D1", "C1-D2", "C2-D1", "C2-D2", "C3-D1", "C3-D2", "C4-D1", "C4-D2", "C5-D1", "C5-D2", "F0")
BLOCKED = ()          # 1.1.0: none (data entry "card inputs"; addendum A1)
CARD_LOCK = "6c154f7d736cefd141fac2252a71536811e7440724d8e3cb4d4eacfecb8e3110"           # LOCK_CARD_v1

# --------------------------------------------------------------------------------------------------- card markets
R5_CUR = ("EUR", "JPY", "GBP", "AUD", "CAD")
R5_LEGS = {"EUR": ("eq_de_dax", "bd_de_10y"), "JPY": ("eq_jp_nikkei", "bd_jp_10y"), "GBP": ("eq_gb_ftse", "bd_gb_10y"),
           "AUD": ("eq_au_asx", "bd_au_10y"), "CAD": ("eq_ca_tsx", "bd_ca_10y")}
C2_COUNTRIES = (("US", "eq_us_spx", "bd_us_10y"), ("JP", "eq_jp_nikkei", "bd_jp_10y"), ("DE", "eq_de_dax", "bd_de_10y"),
                ("GB", "eq_gb_ftse", "bd_gb_10y"), ("CA", "eq_ca_tsx", "bd_ca_10y"))
RATE_SERIES = {"US": ("TB3MS",), "JP": ("IR3TIB01JPM156N",), "DE": ("IR3TIB01DEM156N", "IR3TIB01EZM156N"),
               "GB": ("IR3TIB01GBM156N",), "CA": ("IR3TIB01CAM156N",), "CH": ("IR3TIB01CHM156N",),
               "SE": ("IR3TIB01SEM156N",)}
EPS_SID = "DS:@:USSP500|A12FE"
C5_P = {"cm_copper": "HP:HGc1|CLOSE", "cm_wti": "HP:CLc1|CLOSE"}
C5_GRAINS = {"wheat": "HP:Wc1|CLOSE", "corn": "HP:Cc1|CLOSE", "soybeans": "HP:Sc1|CLOSE"}
# C5-D2's reported line (cocoa, LME cash) is NOT computed: those instruments are held back (tools/lseg/lseg_untouched.csv;
# lsegdata hides them unless allow_untouched=True, which no registered entry grants for a design run): correction 2
# under the gm/CHANGES.md "Pre-B diagnostics" entry, before any run.
C5_REPORTED_NOT_RUN = "cocoa (HP:LCCc1, HP:CCc1) and LME cash (DS:L..CASH) are held-back (untouched) instruments"
C5_BREAK_END = pd.Period("2008-12", "M")
ED_CODE = re.compile(r"^<?ED([HMUZ])(\d)\^(\d)>?$", re.I)
MONTHS = "FGHJKMNQUVXZ"


class AsRunMismatch(RuntimeError):
    pass


# =====================================================================================================================
# checks of the job
# =====================================================================================================================
def core_facts(path):
    """The Core book v1 report (job gm_core_v1) -> (ok, reason): 'CORE V1 JOB DONE' and a 'CORE BOOK V1 EMPTY' line."""
    if not os.path.exists(path):
        return False, "missing (%s)" % os.path.basename(path)
    with open(path, encoding="utf-8", errors="replace") as f:
        L = f.read().splitlines()
    if not any(x.strip() == CORE_NEEDS[0] for x in L):
        return False, "no '%s' line" % CORE_NEEDS[0]
    if not any(x.startswith(CORE_NEEDS[1] + " |") for x in L):
        return False, "no '%s' line" % CORE_NEEDS[1]
    return True, "ok"


DIAG_NEEDS = ("D1: candidate half blocked", "D2: closed", "D3: closed")        # A3 empty (as core_v1.diag_facts)


def diag_facts(path):
    """The diagnostics report (job gm_diag_v1) -> (ok, reason): 'DIAG JOB DONE' and one DIAG SUMMARY line holding
    every item of DIAG_NEEDS (7.5 order item 2 done; A3 empty)."""
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


def lseg_lock_of(work_dir):
    """The LSEG store's lock id from work_dir/lseg/manifest.json (lsegdata.lock_id_of) and its LOCK file, read BEFORE
    any table is loaded -> (lock id or None, reason)."""
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
# small helpers
# =====================================================================================================================
def cell(v, n, fmt="%.3f"):
    """Printing rule (entry item 7): the value over >= 60 months, else the count and the sign only."""
    if v is None or v != v:
        return "n %d, n/a" % n
    if n >= MIN_PRINT:
        return (fmt % v) + " (%d)" % n
    return "n %d, sign %s" % (n, "+" if v > 0 else ("-" if v < 0 else "0"))


def per(s):
    """A monthly series / frame on month-end Timestamps (LSEG) -> PeriodIndex."""
    s = s.copy()
    if not isinstance(s.index, pd.PeriodIndex):
        s.index = pd.DatetimeIndex(s.index).to_period("M")
    return s[~s.index.duplicated(keep="last")].sort_index()


def episodes(months):
    """F0 c: number of episodes among held months (a new one starts at a held month whose previous held month is 12
    or more months earlier)."""
    m = sorted({int(p.ordinal) if isinstance(p, pd.Period) else int(p) for p in months})
    if not m:
        return 0
    return 1 + sum(1 for a, b in zip(m[:-1], m[1:]) if b - a >= 12)


def in_dec(idx):
    return (idx >= DEC[0]) & (idx <= DEC[1])


def nonzero_months(pos, start=None):
    """Decision months (DEC, from start) in which a position frame / series is non-zero anywhere."""
    x = pos if isinstance(pos, pd.Series) else pos.abs().sum(axis=1, min_count=1)
    x = x[in_dec(x.index)]
    if start is not None:
        x = x[x.index >= start]
    return [p for p, v in x.items() if v == v and v != 0]


def f0(held, label):
    n, e = len(set(held)), episodes(held)
    ok = n >= 48 and e >= 3
    return {"rule": label, "held": n, "episodes": e, "judgeable": ok,
            "outcome": "judged in B2" if ok else "not judgeable (analyst watch condition)"}


def card_vol(R, D):
    """Card specs s5: the engine hybrid estimate with the CANDIDATE vol config (the A1 panel, free daily returns)."""
    from gm import config as CF
    from gm import vol as VM
    return VM.estimate(R, CF.CANDIDATE, D)


# =====================================================================================================================
# LSEG view (as of 2010-12-31, design part only)
# =====================================================================================================================
def ed_delivery(code):
    """'<EDH0^9>' -> (1990, 3); serial months and other roots -> None. Decade digit >= 5 -> 19xx (lseg_contract_v3)."""
    m = ED_CODE.match(str(code).strip().upper())
    if not m:
        return None
    dec, yd = int(m.group(3)), int(m.group(2))
    return ((1900 if dec >= 5 else 2000) + 10 * dec + yd, MONTHS.index(m.group(1)) + 1)


class LsegView:
    """Entry item 2 / R1 a: lsegdata.Panel as of 2010-12-31. monthly(sid) -> Period-indexed Series; daily(sid) ->
    DatetimeIndex Series (observation days); ed_contracts() -> {(year, month): series id} for the quarterly Datastream
    daily Eurodollar contracts (status ok, primary)."""

    def __init__(self, panel):
        self.panel = panel
        self.a = panel.asof(SEAL)
        self.cat = panel.catalog

    def monthly(self, sid):
        return per(self.a.monthly(sid, "M").astype(float))

    def daily(self, sid):
        s = self.a.series(sid, "D").astype(float)
        s.index = pd.DatetimeIndex(s.index).normalize()
        return s[~s.index.duplicated(keep="last")].sort_index()

    def ed_contracts(self):
        c = self.cat
        c = c[(c["per"] == "D") & (c["status"] == "ok") & (c["duplicate_of"] == "") &
              c["series_id"].astype(str).str.startswith("DS:")]
        out = {}
        for r in c.itertuples():
            d = ed_delivery(r.code)
            if d is not None and d not in out:
                out[d] = r.series_id
        return out


# =====================================================================================================================
# R1 (entry item 5 R1 a-k; SPEC_Strip_reversion s3, s13; 7.5 row R1)
# =====================================================================================================================
def _first_us_bday(y, m):
    import lsegdata as LD
    d = dt.date(y, m, 1)
    while d.weekday() >= 5 or LD.hol_flag(d) & 1:
        d += dt.timedelta(days=1)
    return d


def holding_end(month):
    """R1 d: the first US business day of month + 2 (calendar arithmetic, no NYSE date after the seal)."""
    p = month + 2
    return _first_us_bday(p.year, p.month)


def strip_of(month, ltd):
    """R1 e: the first eight quarterly deliveries whose last trading day is after the holding end of month."""
    h = holding_end(month)
    return [k for k in sorted(ltd) if ltd[k] > h][:8]


def quarterly_ltd(y0=1980, y1=2014):
    import lseg_rules as LR
    return {(y, m): LR.dates("ED", y, m)[0] for y in range(y0, y1 + 1) for m in (3, 6, 9, 12)}


def measures(r):
    """r = contract rates r_1..r_8 (bp, NaN where missing) -> {('K', n): value, ('S', n): value} where computable."""
    out = {}
    for n in range(2, 8):                         # K_n uses contracts 1..n+1
        if np.all(np.isfinite(r[:n + 1])):
            yn, ym, yp = r[:n].mean(), r[:n - 1].mean(), r[:n + 1].mean()
            out[("K", n)] = 2 * yn - ym - yp
    for n in range(2, 9):                         # S_n uses contracts 1..n
        if np.all(np.isfinite(r[:n])):
            out[("S", n)] = r[:n].mean() - r[:n - 1].mean()
    return out


def uses(key):
    return key[1] + 1 if key[0] == "K" else key[1]


def r1_cost(n):
    return 2 * 0.5 * (2 * n + 4) / (n * (n + 1))


def r1(contracts, days, start=pd.Period("1990-01", "M"), end=pd.Period("2010-11", "M"), normal_from="1981-12"):
    """R1. contracts {(y, m): daily settlement Series}, days = NYSE days (<= 2010-12-31). Returns the result dict."""
    days = pd.DatetimeIndex(days).normalize().unique().sort_values()
    days = days[days <= SEAL]
    ltd = quarterly_ltd()
    keys = sorted(ltd)
    px = pd.DataFrame({k: contracts[k].reindex(days) if k in contracts else pd.Series(np.nan, index=days) for k in keys},
                      index=days)
    rate = (100.0 - px) * 100.0
    ch = (px.notna() & px.shift(1).notna() & (px != px.shift(1))).astype(float)
    nchg = ch.shift(1).rolling(20, min_periods=20).sum()          # changes over the 20 NYSE days before each day
    pos = {d: i for i, d in enumerate(days)}
    me = pd.Series(days, index=days).groupby(days.to_period("M")).max()
    me = me[me.index >= pd.Period(normal_from, "M")]
    hist, first = {}, {}                                          # (key, g) -> [(period, value)], key -> first period

    def vals_at(month, day):
        st = strip_of(month, ltd)
        if day not in pos:
            return st, None
        return st, rate.loc[day, st].to_numpy(dtype=float)

    rows, excl = [], {"no normal": 0, "strip missing on d": 0, "strip missing on d1": 0, "stale": 0}
    period_list = list(me.index)
    window = []
    start_found = first_ok = None
    for p in period_list:
        d = me[p]
        st, r = vals_at(p, d)
        meas = measures(r) if r is not None else {}
        # normals as of d (earlier month-ends only), then add d's own values for later months
        normal = {}
        for key in [("K", n) for n in range(2, 8)] + [("S", n) for n in range(2, 9)]:
            g = st[key[1] - 1][1]
            h = hist.get((key, g))
            if key in first and (p.ordinal - first[key].ordinal) >= 60 and h:
                normal[key] = float(np.mean([v for _, v in h]))
        full = r is not None and np.all(np.isfinite(r))
        okK = all(("K", n) in normal for n in range(2, 8))
        okS = all(("S", n) in normal for n in range(2, 9))
        if first_ok is None and full and (okK or okS):
            first_ok = p                                  # spec s7 start condition, first month-end it holds
        if first_ok is not None and max(start, first_ok) <= p <= end:
            if start_found is None:
                start_found = p
            window.append((p, d, st, r, normal))
        for key, v in meas.items():
            g = st[key[1] - 1][1]
            hist.setdefault((key, g), []).append((p, v))
            first.setdefault(key, p)
    n_month = 0
    for p, d, st, r, normal in window:
        n_month += 1
        i = pos[d]
        d1 = days[i + 1] if i + 1 < len(days) else None
        full_d = r is not None and np.all(np.isfinite(r))
        r1v = rate.loc[d1, st].to_numpy(dtype=float) if d1 is not None else None
        full_d1 = r1v is not None and np.all(np.isfinite(r1v))
        for n in range(2, 8):
            key = ("K", n)
            if key not in normal:
                excl["no normal"] += 1
                continue
            if not full_d:
                excl["strip missing on d"] += 1
                continue
            if not full_d1:
                excl["strip missing on d1"] += 1
                continue
            if any(not (nchg.at[d, k] >= 15) for k in st[:n + 1]):
                excl["stale"] += 1
                continue
            g0 = measures(r)[key] - normal[key]
            g1 = measures(r1v)[key] - normal[key]
            c = r1_cost(n)
            q = abs(g0) > c and abs(g1) > c and np.sign(g0) == np.sign(g1)
            rows.append({"month": p, "n": n, "q": bool(q)})
    elig = len(rows)
    qual = sum(1 for x in rows if x["q"])
    share = qual / elig if elig else float("nan")
    by_n = {n: (sum(1 for x in rows if x["n"] == n and x["q"]), sum(1 for x in rows if x["n"] == n))
            for n in range(2, 8)}
    first_normal = {}
    for p, d, st, r, normal in window:
        for n in range(2, 8):
            if ("K", n) in normal and n not in first_normal:
                first_normal[n] = p
    # coverage (lseg_contract_v3 STRIP definition): NYSE days 1990-2010 with the first eight alive contracts priced
    cov_days = days[days >= pd.Timestamp("1990-01-01")]
    full = 0
    for d in cov_days:
        alive = [k for k in keys if ltd[k] >= d.date()][:8]
        if all(np.isfinite(px.at[d, k]) for k in alive) and len(alive) == 8:
            full += 1
    return {"eligible": elig, "qualifying": qual, "share": share, "pass": bool(elig and share >= 0.5),
            "by_n": by_n, "excluded": excl, "months": n_month, "start": start_found,
            "end": window[-1][0] if window else None, "first_normal": first_normal,
            "coverage": (full, len(cov_days)), "contracts": len(contracts)}


# =====================================================================================================================
# card 1 R5 (entry item 5 C1-D1 / C1-D2 / F0 card 1 R5 a-d)
# =====================================================================================================================
def card1_r5(fxv, vol):
    """fxv: Period-indexed frame of panel.fx_usd_value for R5_CUR; vol: the card volatility frame.
    -> dict(trig {G: frame}, pos (averaged rule, per market), legs {leg: frame}, cond_months)."""
    fxv = fxv.reindex(columns=list(R5_CUR))
    m = 100.0 * (fxv / fxv.shift(6) - 1)
    cnt = m.notna().sum(axis=1)
    med = m.median(axis=1, skipna=True)
    trig = {}
    for G in (15, 10):
        t = m.le(med - G, axis=0) & m.notna()
        t = t.mul(cnt >= 3, axis=0).astype(bool)
        trig[G] = t
    versions = [(G, form) for G in (15, 10) for form in ("stocks", "stocks and bond")]
    stock_mk = [R5_LEGS[c][0] for c in R5_CUR]
    bond_mk = [R5_LEGS[c][1] for c in R5_CUR]
    idx = fxv.index
    legs = {"stock": pd.DataFrame(0.0, index=idx, columns=stock_mk), "bond": pd.DataFrame(0.0, index=idx, columns=bond_mk)}
    for G, form in versions:
        held = trig[G].astype(float).rolling(13, min_periods=1).max() > 0      # tail: t - 12 .. t
        k = 2 if form == "stocks and bond" else 1
        for c in R5_CUR:
            eq, bd = R5_LEGS[c]
            v = vol.reindex(index=idx)
            if eq in v:
                p = (0.40 / v[eq] / k).where(held[c] & v[eq].notna(), 0.0).fillna(0.0)
                legs["stock"][eq] += p / len(versions)
            if form == "stocks and bond" and bd in v:
                p = (0.40 / v[bd] / k).where(held[c] & v[bd].notna(), 0.0).fillna(0.0)
                legs["bond"][bd] += p / len(versions)
    pos = pd.concat([legs["stock"], legs["bond"]], axis=1)
    cond = trig[10].any(axis=1)
    cond_months = [p for p, v in cond.items() if v and DEC[0] <= p <= DEC[1]]
    return {"trig": trig, "pos": pos, "legs": legs, "cond_months": cond_months}


def c1d1(cond_months):
    e = episodes(cond_months)
    return {"condition_months": len(cond_months), "episodes": e, "pass": e >= 6,
            "outcome": "rule stays (with F0)" if e >= 6 else "analyst watch condition"}


def same_sign_share(rule_pos, book_pos, start=None):
    """Over the market-months (decision months DEC) where rule_pos is non-zero: the share with the book's position in
    that market of the same sign (zero or missing = not the same). -> (share, n)."""
    rp = rule_pos[in_dec(rule_pos.index)]
    if start is not None:
        rp = rp[rp.index >= start]
    bp = book_pos.reindex(index=rp.index, columns=rp.columns)
    held = rp.ne(0) & rp.notna()
    same = held & (np.sign(rp) == np.sign(bp)) & bp.notna() & bp.ne(0)
    n = int(held.to_numpy().sum())
    return (float(same.to_numpy().sum()) / n if n else float("nan")), n


def c1d2(r5, book_pos):
    out = {}
    for leg in ("stock", "bond"):
        s, n = same_sign_share(r5["legs"][leg], book_pos)
        out[leg] = {"share": s, "n": n, "drop": bool(n and s > 0.80)}
    return out


# =====================================================================================================================
# C2-D1 (entry item 5 C2-D1 a-c)
# =====================================================================================================================
def c2d1(R, rates):
    """rates {country: Period-indexed Series} (DE already DE then EZ). -> dict(pooled, japan, gate)."""
    lo, hi, jp_lo, jp_hi = [], [], [], []
    per_country = {}
    win = (R.index >= pd.Period("1975-01", "M")) & (R.index <= pd.Period("2010-12", "M"))
    for cc, eq, bd in C2_COUNTRIES:
        if eq not in R or bd not in R or cc not in rates:
            per_country[cc] = (0, 0)
            continue
        x = R.loc[win, eq].dropna()
        if not len(x):
            per_country[cc] = (0, 0)
            continue
        q = np.percentile(x.to_numpy(), 20)
        worst = x.index[x.to_numpy() <= q]
        b = R.loc[worst, bd]
        r = rates[cc].reindex(worst)
        ok = b.notna() & r.notna()
        l_ = b[ok & (r < 1.0)].tolist()
        h_ = b[ok & (r >= 1.0)].tolist()
        lo += l_
        hi += h_
        per_country[cc] = (len(l_), len(h_))
        if cc == "JP":
            jp_lo, jp_hi = l_, h_

    def gate(a, b):
        ma = float(np.mean(a)) if a else float("nan")
        mb = float(np.mean(b)) if b else float("nan")
        ok = len(a) >= 30 and mb == mb and mb > 0 and ma == ma and ma < 0.5 * mb
        return {"n_low": len(a), "n_other": len(b), "mean_low": ma, "mean_other": mb, "pass": bool(ok)}
    return {"pooled": gate(lo, hi), "japan": gate(jp_lo, jp_hi), "countries": per_country}


# =====================================================================================================================
# card 3 R4 (entry item 5 C3-D1 card 3 R4 a-b)
# =====================================================================================================================
def card3_r4(eps, spx_me, tb3, vol_spx):
    """-> averaged rule position (Series, eq_us_spx), the on frames per B, the start month."""
    idx = vol_spx.index
    eps, spx_me, tb3 = eps.reindex(idx), spx_me.reindex(idx), tb3.reindex(idx)
    E = 100.0 * eps / spx_me
    vs = np.maximum(vol_spx, vol_spx.expanding(min_periods=1).median())
    vs = vs.where(vol_spx.notna())
    pos = pd.Series(0.0, index=idx)
    on = {}
    for B in (1.0, 0.0):
        o = ((E - tb3) < B) & E.notna() & tb3.notna()
        on[B] = o
        for v in (vol_spx, vs):
            pos += (-0.40 / v).where(o & v.notna(), 0.0).fillna(0.0) / 4
    fe = eps.first_valid_index()
    return {"pos": pos, "on": on, "start": fe}


def c3d1(r4, book_pos):
    rp = r4["pos"].to_frame("eq_us_spx")
    s, n = same_sign_share(rp, book_pos, start=r4["start"])
    lab = "dropped before B2" if (n and s >= 0.80) else ("kept, flagged" if (n and s >= 0.50) else "kept")
    return {"share": s, "n": n, "outcome": lab}


# =====================================================================================================================
# card 4 R1-R4 (daily date rules; entry item 5 F0 a, g; SPEC_Card4 s3)
# =====================================================================================================================
def _ext_days(days):
    """NYSE days (<= 2010-12-31) extended by US business days (lsegdata calendar) to 2011-03-31: calendar arithmetic
    for windows that would run into 2011 (no 2011 price is read)."""
    import lsegdata as LD
    d0 = pd.DatetimeIndex(days).normalize().unique().sort_values()
    d0 = d0[d0 <= SEAL]
    ext, d = [], dt.date(2011, 1, 1)
    while d <= dt.date(2011, 3, 31):
        if d.weekday() < 5 and not (LD.hol_flag(d) & 1):
            ext.append(pd.Timestamp(d))
        d += dt.timedelta(days=1)
    return d0.append(pd.DatetimeIndex(ext))


def _on_before(days, ts):
    """The last day of days on or before ts (None if none)."""
    i = days.searchsorted(pd.Timestamp(ts), side="right") - 1
    return days[i] if i >= 0 else None


def _third_friday(y, m):
    d = dt.date(y, m, 1)
    d += dt.timedelta(days=(4 - d.weekday()) % 7)
    return d + dt.timedelta(days=14)


def card4_days(gspc, days, vol_spx):
    """-> {rule: Series of the averaged rule's direction sum per day (exact integers) over the window days}, the
    months held (non-zero and a volatility at the previous month end), and the number of versions."""
    E = _ext_days(days)
    pos = {d: i for i, d in enumerate(E)}
    lv = gspc.dropna().copy()
    lv.index = pd.DatetimeIndex(lv.index).normalize()
    lv = lv[~lv.index.duplicated(keep="last")]
    lv = lv[lv.index <= SEAL]

    def close(d):
        return float(lv.get(d, np.nan)) if d is not None else np.nan

    def prev(d, k=1):
        i = pos[d] - k
        return E[i] if i >= 0 else None

    def held(series, a, b, val):
        """days in (a, b] get val (assignment)."""
        if a is None or b is None:
            return
        ia, ib = pos[a], pos[b]
        for j in range(ia + 1, ib + 1):
            series[E[j]] = val

    years = range(1974, 2011)
    rules = {}
    # R1: entry (end-October / mid-December) x form A / B / C
    vers = []
    for ent in ("oct", "dec"):
        for form in ("A", "B", "C"):
            s = {}
            for Y in years:
                en = _on_before(E, "%d-10-31" % Y) if ent == "oct" else _on_before(E, "%d-12-15" % Y)
                ex = _on_before(E, "%d-01-15" % (Y + 1))
                bar = close(_on_before(E, "%d-12-31" % (Y - 1)))
                c = close(prev(en))
                if form == "A":
                    v = 1
                elif form == "B":
                    v = 1 if c > bar else 0
                else:
                    v = 1 if c > bar else (-1 if c < bar else 0)
                if v:
                    held(s, en, ex, v)
            vers.append(s)
    rules["card 4 R1"] = vers
    # R2: N 12 / 15 (13 in five-week cycles) x exit at X / next day
    vers = []
    for N in (12, 15):
        for ex_next in (False, True):
            s = {}
            for Y, M in [(y, m) for y in range(1974, 2012) for m in range(1, 13)
                         if (1974, 12) <= (y, m) <= (2011, 1)]:
                if True:
                    tf = _third_friday(Y, M)
                    py, pm = (Y, M - 1) if M > 1 else (Y - 1, 12)
                    weeks = (tf - _third_friday(py, pm)).days // 7
                    X = _on_before(E, tf)
                    n = 13 if weeks == 5 else N
                    if X is None or pos[X] - n < 0:
                        continue
                    en = E[pos[X] - n]
                    ex = E[pos[X] + 1] if ex_next and pos[X] + 1 < len(E) else X
                    held(s, en, ex, 1)
            vers.append(s)
    rules["card 4 R2"] = vers
    # R3: window 1 / window 2, gate: close before entry above the close of the last trading day of the preceding October
    vers = []
    for w in (1, 2):
        s = {}
        for Y in range(1975, 2011):
            octc = close(_on_before(E, "%d-10-31" % (Y - 1)))
            if w == 1:
                en = _on_before(E, "%d-01-15" % Y)
                ex = E[min(pos[en] + 10, len(E) - 1)]
            else:
                en = _on_before(E, _third_friday(Y, 2))
                xm = _on_before(E, _third_friday(Y, 3))
                ex = E[pos[xm] + 1]
            if close(prev(en)) > octc:
                held(s, en, ex, -1)
        vers.append(s)
    rules["card 4 R3"] = vers
    # R4: d 3 / 5; s = sign of the month to date at T-d-1; held from the close of T-d to the close of day d of m+1
    vers = []
    mt = pd.Series(E, index=E).groupby(E.to_period("M"))
    last = mt.max()
    firsts = {p: list(g) for p, g in mt}
    for d_ in (3, 5):
        s = {}
        for p in last.index:
            if p < pd.Period("1974-12", "M") or p > pd.Period("2010-12", "M"):
                continue
            T = last[p]
            pm = p - 1
            if pm not in last.index or (p + 1) not in firsts or len(firsts[p + 1]) < d_:
                continue
            ref = close(last[pm])
            c = close(E[pos[T] - d_ - 1])
            v = int(np.sign(c / ref - 1)) if (c == c and ref == ref) else 0
            if v:
                held(s, E[pos[T] - d_], firsts[p + 1][d_ - 1], v)
        vers.append(s)
    rules["card 4 R4"] = vers
    out = {}
    lo, hi = pd.Timestamp("1975-01-01"), SEAL
    v_prev = vol_spx.shift(1)                     # the volatility at the previous month end, fixed for the month
    for name, vs in rules.items():
        tot = pd.Series(0, index=E, dtype="int64")
        for s in vs:
            if s:
                tot = tot.add(pd.Series(s, dtype="int64").reindex(E).fillna(0).astype("int64"), fill_value=0)
        tot = tot[(tot.index >= lo) & (tot.index <= hi)]
        vm = v_prev.reindex(tot.index.to_period("M")).to_numpy()
        live = (tot.to_numpy() != 0) & np.isfinite(vm)
        months = sorted(set(tot.index[live].to_period("M")))
        out[name] = {"sum": tot, "months": months, "versions": len(vs)}
    return out


# =====================================================================================================================
# card 5 R1 (entry item 5 C5-D1 / C5-D2 / F0 card 5 R1 a-c)
# =====================================================================================================================
def triggers(P):
    """P(t) above every earlier month-end value, with at least 120 earlier values."""
    P = P.dropna()
    prev_max = P.cummax().shift(1)
    n_before = pd.Series(np.arange(len(P)), index=P.index)
    return (P > prev_max) & (n_before >= 120)


def card5_r1(P, vol):
    """P {market: Period Series} for cm_copper, cm_wti. -> averaged position of the four non-ceiling versions per
    market (H 24 / 36 x crude out / in; entry item 5 F0 f) on the vol index, and the trigger series."""
    idx = vol.index
    pos = pd.DataFrame(0.0, index=idx, columns=list(C5_P))
    trig = {}
    for mk in C5_P:
        t = triggers(P[mk]).reindex(idx, fill_value=False).astype(bool) if mk in P else pd.Series(False, index=idx)
        trig[mk] = t
    for H in (24, 36):
        for crude in (False, True):
            for mk in C5_P:
                if mk == "cm_wti" and not crude:
                    continue
                if mk not in vol:
                    continue
                held = trig[mk].astype(float).rolling(H + 1, min_periods=1).max() > 0
                pos[mk] += (0.40 / vol[mk]).where(held & vol[mk].notna(), 0.0).fillna(0.0) / 4
    return {"pos": pos, "trig": trig}


def trend12_avg_sign(R, D):
    """C5-D1 b: mean of the signs of the four 12-month Trend versions (config TREND_GRID h = 12) on R; a missing
    version (no score or no volatility) counts 0."""
    from gm import book as B
    from gm import config as CF
    from gm import vol as VM
    vols = {"hybrid": VM.estimate(R, CF.variant(CF.CANDIDATE, vol={"model": "hybrid"}), D),
            "m36": VM.estimate(R, {"vol": {"model": "m36"}}, D)}
    acc = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    vers = [v for v in CF.TREND_GRID if v[0] == 12]
    for h, shape, vm in vers:
        X = B._trend_version(R, h, shape, vols[vm], CF.CANDIDATE["trend"].get("cap", 2.0)).clip(-1, 1)
        p = (X * 0.40 / vols[vm]).where(vols[vm].notna())
        acc += np.sign(p).fillna(0.0)
    return acc / len(vers), len(vers)


def c5d1(r5, avg, book_pos):
    rp = r5["pos"]
    rp = rp[in_dec(rp.index)]
    held = rp.ne(0) & rp.notna()
    a = avg.reindex(index=rp.index, columns=rp.columns)
    long_ = held & (a > 0)
    n = int(held.to_numpy().sum())
    s = float(long_.to_numpy().sum()) / n if n else float("nan")
    sb, nb = same_sign_share(rp, book_pos)
    by = {mk: int(held[mk].sum()) for mk in rp.columns}
    return {"share": s, "n": n, "not_registered": bool(n and s >= 0.75), "book_share": sb, "book_n": nb, "by_market": by}


def breaks(P, end=C5_BREAK_END):
    """C5-D2: trigger months with no trigger in the 12 months before, up to `end`; -> [(month, higher 24 months on)]."""
    P = P.dropna()
    t = triggers(P)
    tm = [p for p, v in t.items() if v]
    out = []
    for p in tm:
        if p > end:
            continue
        if any((p - k) in set(tm) for k in range(1, 13)):
            continue
        q = p + 24
        hi = bool(q in P.index and P[q] > P[p]) if q in P.index else None
        out.append((p, hi))
    return out


def c5d2(Pslow, Pcrude, Pgrains, Prep=None):
    def pool(d):
        b = [x for s in d.values() for x in breaks(s)]
        n = len(b)
        k = sum(1 for _, h in b if h)
        nn = sum(1 for _, h in b if h is None)
        return {"breaks": n, "higher": k, "no_outcome": nn, "share": (k / n if n else float("nan"))}
    slow, grains = pool(Pslow), pool(Pgrains)
    ok = slow["breaks"] >= 10 and grains["breaks"] >= 10 and slow["share"] >= grains["share"] + 0.15
    return {"slow": slow, "grains": grains, "crude": pool(Pcrude), "reported": pool(Prep) if Prep else None,
            "pass": bool(ok),
            "diff": slow["share"] - grains["share"] if (slow["breaks"] and grains["breaks"]) else float("nan")}


# =====================================================================================================================
# 1.1.0: the card rules on the locked card inputs (gm/CHANGES.md "Pre-B diagnostics" addendum A1-A6)
# =====================================================================================================================
R4B_BASKET = ("cm_wti", "cm_brent", "cm_natgas", "cm_heatoil", "cm_gasoline", "cm_gold", "cm_silver", "cm_copper",
              "cm_platinum", "cm_corn", "cm_wheat", "cm_soybeans", "cm_sugar", "cm_coffee", "cm_cotton", "cm_cattle")
C3_CUR = (("US", None), ("JP", "fx_jpy"), ("CH", "fx_chf"), ("EZ", "fx_eur"), ("GB", "fx_gbp"), ("CA", "fx_cad"),
          ("SE", "fx_sek"))


def tail(cond, n):
    """Held from a condition month to n months after the last one (inclusive); n = 0: the condition months."""
    c = cond.fillna(False).astype(float)
    return (c.rolling(n + 1, min_periods=1).max() > 0) if n else c > 0


def leg(on, vol, sign, k, idx):
    """direction x 0.40 / vol / k where on and a volatility exists, else 0 (no volatility, no position)."""
    if vol is None:                                           # market not in the panel: no position
        return pd.Series(0.0, index=idx)
    v = vol.reindex(idx)
    o = on.reindex(idx).fillna(False).astype(bool)
    return (sign * 0.40 / v / k).where(o & v.notna(), 0.0).fillna(0.0)


def months_of(cond, start=None):
    c = cond.fillna(False).astype(bool)
    c = c[in_dec(c.index)]
    if start is not None:
        c = c[c.index >= start]
    return [p for p, v in c.items() if v]


def rule(legs, cond_months, versions, start=None):
    pos = pd.concat(list(legs.values()), axis=1)
    pos = pos.T.groupby(level=0).sum().T                     # a market in two legs: summed
    return {"pos": pos, "legs": legs, "cond_months": cond_months, "versions": versions, "start": start}


def core_cpi(ci):
    """A3: CPILFESL 12-month change by data entry item 5, lag 1 -> (value, flagged)."""
    return ci.fr_change("CPILFESL", 12)


def r4_state(ci, H):
    c, _ = core_cpi(ci)
    ff = ci.m("FEDFUNDS").reindex(c.index)
    return (c > H) & (ff < c)


def _idx(R):
    return R.index


def card1_rules(ci, R, vol, spx_me):
    """Card 1 R1-R4 (SPEC_Card1 s3; addendum A3). -> {rule: rule dict}."""
    idx = _idx(R)
    g = lambda s: s.reindex(idx)  # noqa: E731
    FF, GS2, GS5, GS10, BAA = (g(ci.m(x)) for x in ("FEDFUNDS", "GS2", "GS5", "GS10", "BAA"))
    WTI, TW, DB = g(ci.m("WTISPLC")), g(ci.m("TWEXMMTH")), g(ci.m("DTWEXBGS"))
    m2 = g(ci.fr_change("M2SL", 12)[0])
    s5 = g(r4_state(ci, 5.0)).fillna(False).astype(bool)
    out = {}
    # R1 Squeeze
    legs = {"2-year": pd.DataFrame(0.0, index=idx, columns=["bd_us_2y"]),
            "10-year": pd.DataFrame(0.0, index=idx, columns=["bd_us_10y"])}
    cond_any = pd.Series(False, index=idx)
    vers = [(L, r, gate) for L in (6, 12) for r in ("FEDFUNDS", "GS10") for gate in (False, True)]
    for L, rn, gate in vers:
        rr = FF if rn == "FEDFUNDS" else GS10
        both_tw = TW.notna() & TW.shift(L).notna()
        dol = (TW > TW.shift(L)).where(both_tw, DB > DB.shift(L))
        cond = (WTI > WTI.shift(L)) & dol.fillna(False).astype(bool) & (rr > rr.shift(L))
        cond_any |= cond
        held = tail(cond, 12) & (~s5 if gate else True)
        for lg, mk in (("2-year", "bd_us_2y"), ("10-year", "bd_us_10y")):
            legs[lg][mk] += leg(held, vol.get(mk), 1, 2, idx) / len(vers)
    out["card 1 R1"] = rule(legs, months_of(cond_any), len(vers))
    # R2 Tightening into warnings
    legs = {"2-year": pd.DataFrame(0.0, index=idx, columns=["bd_us_2y"]),
            "10-year": pd.DataFrame(0.0, index=idx, columns=["bd_us_10y"])}
    cond_any = pd.Series(False, index=idx)
    vers = [(T, k, gate) for T in (6, 12) for k in (2, 3) for gate in (False, True)]
    sp = BAA - GS10
    wa = (GS5 - GS2 < 0).where(GS2.notna(), False).fillna(False).astype(bool)
    wb = (sp > sp.shift(6)).fillna(False)
    wc = (m2 < m2.shift(24)).fillna(False)
    nw = wa.astype(int) + wb.astype(int) + wc.astype(int)
    start2 = GS2.first_valid_index()
    for T, k, gate in vers:
        cond = (FF >= FF.shift(T) + 0.25) & (nw >= k)
        cond = cond & (idx >= start2)
        cond_any |= cond
        held = tail(cond, 12) & (~s5 if gate else True) & (idx >= start2)
        for lg, mk in (("2-year", "bd_us_2y"), ("10-year", "bd_us_10y")):
            legs[lg][mk] += leg(held, vol.get(mk), 1, 2, idx) / len(vers)
    out["card 1 R2"] = rule(legs, months_of(cond_any, start2), len(vers), start2)
    # R3 Easing into strength
    legs = {"10-year": pd.DataFrame(0.0, index=idx, columns=["bd_us_10y"]),
            "S&P": pd.DataFrame(0.0, index=idx, columns=["eq_us_spx"])}
    cond_any = pd.Series(False, index=idx)
    spx = spx_me.reindex(idx)
    spx_ok = spx > spx.rolling(10, min_periods=10).mean()
    spv = sp.dropna()
    med = spv.expanding().quantile(0.5, interpolation="linear").reindex(idx)
    low3 = spv.expanding().quantile(0.333, interpolation="linear").reindex(idx)
    gold = R["cm_gold"] if "cm_gold" in R else pd.Series(np.nan, index=idx)
    lvl = (1 + gold.fillna(0)).cumprod().where(gold.notna().cummax())
    gold_hi = (lvl >= lvl.rolling(12, min_periods=12).max()) & lvl.notna()
    vers = [(sv, gv) for sv in ("median", "third") for gv in (False, True)]
    for sv, gv in vers:
        sc = (sp < med) if sv == "median" else (sp <= low3)
        cond = (FF <= FF.shift(3) - 0.25) & sc.fillna(False) & spx_ok.fillna(False)
        if gv:
            cond = cond & gold_hi.fillna(False)
        cond_any |= cond
        held = tail(cond, 12)
        legs["10-year"]["bd_us_10y"] += leg(held, vol.get("bd_us_10y"), -1, 2, idx) / len(vers)
        legs["S&P"]["eq_us_spx"] += leg(held, vol.get("eq_us_spx"), 1, 2, idx) / len(vers)
    out["card 1 R3"] = rule(legs, months_of(cond_any), len(vers))
    # R4 Behind on inflation (no tail)
    bk = [m for m in R4B_BASKET if m in vol]
    legs = {"2-year": pd.DataFrame(0.0, index=idx, columns=["bd_us_2y"]),
            "10-year": pd.DataFrame(0.0, index=idx, columns=["bd_us_10y"]),
            "S&P": pd.DataFrame(0.0, index=idx, columns=["eq_us_spx"]),
            "basket": pd.DataFrame(0.0, index=idx, columns=bk)}
    cond_any = pd.Series(False, index=idx)
    vers = [(H, a) for H in (5.0, 4.5) for a in ("A", "B")]
    vb = vol.reindex(idx)[bk] if bk else pd.DataFrame(index=idx)
    nb = vb.notna().sum(axis=1).replace(0, np.nan)
    for H, a in vers:
        st = g(r4_state(ci, H)).fillna(False).astype(bool)
        cond_any |= st
        k = 2 if a == "A" else 4
        legs["2-year"]["bd_us_2y"] += leg(st, vol.get("bd_us_2y"), -1, k, idx) / len(vers)
        legs["10-year"]["bd_us_10y"] += leg(st, vol.get("bd_us_10y"), -1, k, idx) / len(vers)
        if a == "B":
            legs["S&P"]["eq_us_spx"] += leg(st, vol.get("eq_us_spx"), -1, k, idx) / len(vers)
            for m in bk:
                legs["basket"][m] += (leg(st, vb[m], 1, k, idx) / nb).fillna(0.0) / len(vers)
    out["card 1 R4"] = rule(legs, months_of(cond_any), len(vers))
    return out


def card2_rules(ci, R, vol, spx_me):
    """Card 2 R1, R2 by version (SPEC_Card2 s3; addendum A4). -> {rule: {version: (cond, held)}}, rule dicts."""
    idx = _idx(R)
    GS10 = ci.m("GS10").reindex(idx)
    c = core_cpi(ci)[0].reindex(idx)
    y = GS10 - c
    yv = y.dropna()
    y3 = yv.expanding(min_periods=120).quantile(0.333, interpolation="linear").reindex(idx)
    hedge = R["eq_us_spx"].rolling(12, min_periods=12).corr(R["bd_us_10y"]) > 0
    vers1 = {}
    for bar in ("0.0", "third"):
        for hg in (False, True):
            on = (y < 0.0) if bar == "0.0" else (y <= y3)
            on = on.fillna(False) & (hedge.fillna(False) if hg else True)
            vers1[(bar, hg)] = (on, on)                       # no tail
    spx = spx_me.reindex(idx)
    d = GS10 - GS10.shift(12)
    chg = 100.0 * (spx / spx.shift(12) - 1)
    un = ci.fr_level("UNRATE")[0].reindex(idx)
    low240 = un.shift(1).rolling(240, min_periods=240).min()
    vers2 = {}
    for X in (1.5, 1.0):
        for lab in (False, True):
            on = (d >= X) & (chg >= -10 * d)
            if lab:
                on = on & (un <= low240)
            on = on.fillna(False)
            vers2[(X, lab)] = (on, tail(on, 12))
    return {"card 2 R1": vers1, "card 2 R2": vers2}


def c2d2(vers, r4_45):
    """Per version: on-months, episodes, share inside card 1 R4's 4.5 state; left out by the registered rule."""
    st = r4_45.fillna(False).astype(bool)
    out = {}
    for v, (on, _held) in vers.items():
        om = months_of(on)
        n = len(om)
        inside = sum(1 for p in om if bool(st.get(p, False)))
        share = inside / n if n else float("nan")
        ep = episodes(om)
        keep = n >= 24 and ep >= 3 and not (n and share > 2.0 / 3.0)
        out[v] = {"on": n, "episodes": ep, "inside": share, "keep": keep}
    return out


def card2_rule(vers, keep, mk, sign, vol, idx):
    kept = [v for v in vers if keep[v]["keep"]]
    lg = pd.DataFrame(0.0, index=idx, columns=[mk])
    for v in kept:
        lg[mk] += leg(vers[v][1], vol.get(mk), sign, 1, idx) / len(kept)
    cond = pd.Series(False, index=idx)
    for v in kept:
        cond |= vers[v][0].reindex(idx).fillna(False)
    return rule({"leg": lg}, months_of(cond), len(kept))


def par_dur(y, n):
    y = y / 100.0
    return (1 - (1 + y / 2) ** (-2 * n)) / y


def pair_vol(R, GS2, GS10):
    """A5: the pair's own monthly return R2y(t) - h(t-1) R10y(t), h = D2 / D10, and its hybrid volatility."""
    from gm import config as CF
    from gm import vol as VM
    h = par_dur(GS2, 2) / par_dur(GS10, 10)
    r = R["bd_us_2y"] - h.shift(1) * R["bd_us_10y"]
    return VM.estimate(pd.DataFrame({"pair": r}), CF.CANDIDATE, None)["pair"], h


def pair_rule(on, vpair, h, idx, nver):
    """Long 2-year at 0.40 / pair vol, short 10-year at that x h; -> (2-year, 10-year) contributions / nver."""
    p2 = leg(on, vpair, 1, 1, idx)
    return p2 / nver, (-p2 * h.reindex(idx)).fillna(0.0) / nver


def fixed_runs(dirn, scale):
    """A5: notional fixed at the first month of a run with the same direction (a change of direction or a zero ends it)."""
    out = pd.Series(0.0, index=dirn.index)
    cur, val = 0, 0.0
    for t in dirn.index:
        d = int(dirn[t]) if dirn[t] == dirn[t] else 0
        s = scale[t]
        if d == 0 or s != s:
            cur, val = 0, 0.0
            continue
        if d != cur:
            cur, val = d, d * s
        out[t] = val
    return out


def card3_r1(rates, R, vol, FF, with_gate=True):
    """Card 3 R1 (A5): versions L x shape x gate x sizing; -> rule dict (averaged positions on the six fx markets)."""
    idx = _idx(R)
    ch = {}
    for cc, _mk in C3_CUR:
        r = rates[{"EZ": "DE", "US": "TB3MS"}.get(cc, cc)].reindex(idx).shift(1)   # mark then euro; lag 1
        ch[cc] = r
    act = (FF.rolling(12, min_periods=12).max() - FF.rolling(12, min_periods=12).min()) >= 0.50
    vsz = np.maximum(vol, vol.expanding(min_periods=1).median()).where(vol.notna())
    mks = [mk for _c, mk in C3_CUR if mk]
    gates = (False, True) if with_gate else (False,)
    vers = [(L, sh, gt, sz) for L in (6, 12) for sh in ("A", "B") for gt in gates for sz in (False, True)]
    pos = pd.DataFrame(0.0, index=idx, columns=mks)
    cond_any = pd.Series(False, index=idx)
    for L, sh, gt, sz in vers:
        V = (vsz if sz else vol).reindex(idx)
        c = pd.DataFrame({cc: ch[cc] - ch[cc].shift(L) for cc, _ in C3_CUR})
        avail = pd.DataFrame({cc: (c[cc].notna() & (R[mk].notna() if mk in R else False) & V[mk].notna()
                                   if mk else c[cc].notna()) for cc, mk in C3_CUR})
        on_g = act.fillna(False) if gt else pd.Series(True, index=idx)
        roles = {}                                            # (market, role) -> (direction frame, scale frame)
        for t in idx:
            if not on_g[t] or not avail.at[t, "US"]:
                continue
            av = [cc for cc, mk in C3_CUR if mk and avail.at[t, cc]]
            if not av:
                continue
            cus = c.at[t, "US"]
            if sh == "A":
                for cc in av:
                    d = np.sign(c.at[t, cc] - cus)
                    if d:
                        mk = dict(C3_CUR)[cc]
                        roles.setdefault((mk, "A"), {})[t] = (d, 0.40 / V.at[t, mk] / 6)
            else:
                order = ["US"] + av
                vals = np.array([c.at[t, x] for x in order])
                hi, lo = order[int(np.argmax(vals))], order[int(np.argmin(vals))]
                if hi == lo:
                    continue
                if hi == "US":
                    for cc in av:
                        mk = dict(C3_CUR)[cc]
                        roles.setdefault((mk, "basket long"), {})[t] = (-1, 0.40 / V.at[t, mk] / 2 / len(av))
                else:
                    mk = dict(C3_CUR)[hi]
                    roles.setdefault((mk, "long"), {})[t] = (1, 0.40 / V.at[t, mk] / 2)
                if lo == "US":
                    for cc in av:
                        mk = dict(C3_CUR)[cc]
                        roles.setdefault((mk, "basket short"), {})[t] = (1, 0.40 / V.at[t, mk] / 2 / len(av))
                else:
                    mk = dict(C3_CUR)[lo]
                    roles.setdefault((mk, "short"), {})[t] = (-1, 0.40 / V.at[t, mk] / 2)
        for (mk, _role), d in roles.items():
            dirn = pd.Series({t: v[0] for t, v in d.items()}).reindex(idx).fillna(0)
            scale = pd.Series({t: v[1] for t, v in d.items()}).reindex(idx)
            pos[mk] += fixed_runs(dirn, scale) / len(vers)
            cond_any |= dirn != 0
    return rule({"fx": pos}, months_of(cond_any), len(vers))


def card3_rules(ci, R, vol, rates):
    """Card 3 R2, R3 (A5) and the C3-D2 count. -> (rules, c3d2 dict)."""
    idx = _idx(R)
    FF, GS1, GS2, GS10 = (ci.m(x).reindex(idx) for x in ("FEDFUNDS", "GS1", "GS2", "GS10"))
    rng = FF.rolling(12, min_periods=12).max() - FF.rolling(12, min_periods=12).min()
    w = (idx >= pd.Period("1975-01", "M")) & (idx <= pd.Period("2010-12", "M"))
    quiet = int(((rng < 0.50) & rng.notna())[w].sum())
    d2 = {"gate_off_months": quiet, "gate_kept": quiet >= 60}
    out = {}
    vpair, h = pair_vol(R, GS2, GS10)
    S = GS10 - GS2
    Smean = S.dropna().expanding(min_periods=120).mean().reindex(idx)
    p2 = pd.DataFrame(0.0, index=idx, columns=["bd_us_2y"])
    p10 = pd.DataFrame(0.0, index=idx, columns=["bd_us_10y"])
    cond_any = pd.Series(False, index=idx)
    vers = [(b, sz) for b in ("1.0", "mean") for sz in (False, True)]
    vps = np.maximum(vpair, vpair.expanding(min_periods=1).median()).where(vpair.notna())
    for b, sz in vers:
        on = ((S < 1.0) if b == "1.0" else (S < Smean)).fillna(False)
        cond_any |= on
        a2, a10 = pair_rule(on, vps if sz else vpair, h, idx, len(vers))
        p2["bd_us_2y"] += a2
        p10["bd_us_10y"] += a10
    out["card 3 R2"] = rule({"2-year": p2, "10-year": p10}, months_of(cond_any, GS2.first_valid_index()), len(vers),
                            GS2.first_valid_index())
    pc = ci.fr_change("PCEPILFE", 12)[0].reindex(idx)
    v2 = vol.get("bd_us_2y")
    v2s = np.maximum(v2, v2.expanding(min_periods=1).median()).where(v2.notna())
    lg = pd.DataFrame(0.0, index=idx, columns=["bd_us_2y"])
    cond_any = pd.Series(False, index=idx)
    vers = [(m, B, sz) for m in (1, 2) for B in (3.0, 4.0) for sz in (False, True)]
    for m, B, sz in vers:
        meas = (FF - GS2) if m == 1 else 2 * (GS1 - GS2)
        on = ((meas >= 0.50) & (pc > B)).fillna(False)
        cond_any |= on
        lg["bd_us_2y"] += leg(on, v2s if sz else v2, -1, 1, idx) / len(vers)
    out["card 3 R3"] = rule({"leg": lg}, months_of(cond_any, GS2.first_valid_index()), len(vers),
                            GS2.first_valid_index())
    out["card 3 R1"] = card3_r1(rates, R, vol, FF, with_gate=d2["gate_kept"])
    return out, d2, {"vpair": vpair, "h": h, "S": S, "Smean": Smean}


def card4_r5(ci, R, aux):
    """Card 4 R5 by version (A6) -> {version: (on, positions frame)}, start."""
    idx = _idx(R)
    FF = ci.m("FEDFUNDS").reindex(idx)
    GS2 = ci.m("GS2").reindex(idx)
    c = core_cpi(ci)[0].reindex(idx)
    start = GS2.first_valid_index()
    vers = {}
    for v in (1, 2):
        on = (c < c.shift(6))
        if v == 2:
            on = on & (FF <= FF.shift(6) - 0.25)
        on = on.fillna(False) & (idx >= start)
        a2, a10 = pair_rule(on, aux["vpair"], aux["h"], idx, 1)
        vers[v] = (on, pd.DataFrame({"bd_us_2y": a2, "bd_us_10y": a10}))
    return vers, start


def c4d2(vers, r2_on, score):
    """Per R5 version: share of on-months with card 3 R2 on, and with Trend long 2-year and short or flat 10-year."""
    out = {}
    for v, (on, _p) in vers.items():
        om = months_of(on)
        n = len(om)
        a = sum(1 for p in om if bool(r2_on.get(p, False)))
        tl = sum(1 for p in om if (score.at[p, "bd_us_2y"] > 0 if p in score.index else False) and
                 (score.at[p, "bd_us_10y"] <= 0 if p in score.index else False))
        out[v] = {"on": n, "r2": a / n if n else float("nan"), "trend": tl / n if n else float("nan")}
    hit = any(all(out[v][k] == out[v][k] and out[v][k] >= 0.80 for v in out) for k in ("r2", "trend"))
    return {"versions": out, "not_registered": bool(hit)}


def c4d1(ci, gspc):
    """C4-D1 (A6): month-ends 1990-01..2010-06."""
    lv = gspc.dropna().copy()
    lv.index = pd.DatetimeIndex(lv.index).normalize()
    lv = lv[~lv.index.duplicated(keep="last")].sort_index()
    lv = lv[lv.index <= SEAL]
    me = lv.groupby(lv.index.to_period("M")).last()
    vix = ci.m("VIXCLS")
    ret = lv.pct_change()
    rows = []
    for t in pd.period_range("1990-01", "2010-06", freq="M"):
        if t not in me.index or (t - 6) not in me.index or t not in vix.index or (t - 6) not in vix.index:
            continue
        up = me[t] > me[t - 6]
        if not up:
            continue
        st = vix[t] > vix[t - 6]
        path = lv[(lv.index.to_period("M") >= t) & (lv.index.to_period("M") <= t + 6)]
        path = path[path.index >= lv[lv.index.to_period("M") == t].index[-1]]
        dd = float((1 - path / path.cummax()).max())
        r3 = ret[(ret.index.to_period("M") >= t - 2) & (ret.index.to_period("M") <= t)].dropna()
        sd = float(r3.std(ddof=1)) * np.sqrt(252)
        if not (sd > 0):
            continue
        rows.append((t, bool(st), dd / sd))
    res = {}
    for lab, a, b in (("1990-01..2010-06", "1990-01", "2010-06"), ("1990-99", "1990-01", "1999-12"),
                      ("2000-01..2010-06", "2000-01", "2010-06")):
        on = [x for t, s, x in rows if s and pd.Period(a, "M") <= t <= pd.Period(b, "M")]
        off = [x for t, s, x in rows if not s and pd.Period(a, "M") <= t <= pd.Period(b, "M")]
        ratio = (np.median(on) / np.median(off)) if (on and off and np.median(off) > 0) else float("nan")
        res[lab] = {"on": len(on), "off": len(off), "ratio": ratio, "ok": bool(ratio == ratio and ratio >= 1.25)}
    return {"windows": res, "pass": all(v["ok"] for v in res.values())}


# =====================================================================================================================
# the registered pass
# =====================================================================================================================
def report(R, D, S, gspc, fxv, rates, lseg, ci, out=print, cfg=None, facts=None):
    """R, S: the A1 panel and signals; D, gspc: free daily inputs; fxv: panel.fx_usd_value frame (R5_CUR); rates
    {country: Series} + 'TB3MS'; lseg: LsegView (or a mock with monthly / daily / ed_contracts); ci: card_inputs.Inputs
    (LOCK_CARD_v1); facts: the A2 report facts (None = no as-run check, tests). Returns dict(gates, results)."""
    import diag_a2 as DG
    from gm import config as CF
    from gm import execution as EX
    from gm import seal as SL
    cfg = cfg or CF.A1_INCUMBENT
    T = SL.resolve(SL.DESIGN)
    R, D, S, gspc, fxv = SL.cut_inputs(T, R, D, S, gspc, fxv)
    rates = {k: SL.cut_inputs(T, v) for k, v in rates.items()}
    SL.check_output({"R": R, "S": S}, T, "diag_preb.report inputs")
    days = EX.nyse_days(gspc=gspc)
    if facts:
        try:
            bk = DG.as_run(R, D, S, days, cfg, facts, out)
        except DG.AsRunMismatch as e:
            raise AsRunMismatch(str(e))
    else:
        bk = DG.book_k1(R, D, S, days, cfg)
    book_pos = bk["pos"]
    SL.check_output({"pos": book_pos}, T, "diag_preb.report book")
    out("--- PRE-B DIAGNOSTICS (TESTING_PROTOCOL 7.6 step 7, 7.5 order item 3; gm/CHANGES.md \"Pre-B diagnostics\"): "
        "registered systematic book %s (%s), A1 panel, positions book.run pos; LSEG design part as of 2010-12-31; zero "
        "slots, nothing adopted; values over fewer than 60 months are printed as count and sign" % (
            cfg["name"], CF.cfg_hash(cfg)))
    if getattr(ci, "lock_id", None) != CARD_LOCK:
        raise RuntimeError("card inputs are not LOCK_CARD_v1")
    out("CORE BOOK READING | C3-D1 'Core book' = the registered systematic book (7.5 fix: content, not trading status); "
        "C1-D2 the same; C4-D2 and C5-D1 name Trend (a pod of that book); the others name no book: the empty Core book "
        "v1 changes no reference here")
    for b in BLOCKED:
        out("BLOCKED | " + b)
    gates, res = {}, {}
    vol = card_vol(R, D)
    # ---- R1
    cons = {k: lseg.daily(sid) for k, sid in lseg.ed_contracts().items()}
    r = r1(cons, days)
    res["R1"] = r
    fc, fn = r["coverage"]
    out("R1 | Eurodollar quarterly contracts (Datastream daily) %d | NYSE days 1990-2010 with the first eight alive "
        "contracts priced %d of %d" % (r["contracts"], fc, fn))
    out("R1 | month-ends %s..%s (%d) | first normal: %s" % (r["start"], r["end"], r["months"], ", ".join(
        "K%d %s" % kv for kv in sorted(r["first_normal"].items()))))
    out("R1 | left out: %s" % ", ".join("%s %d" % kv for kv in r["excluded"].items()))
    for n in range(2, 8):
        q, e = r["by_n"][n]
        out("R1 | K%d (cost %.3f bp) | qualifying %d of %d | share %s" % (
            n, r1_cost(n), q, e, cell(q / e if e else float("nan"), e)))
    out("R1 GATE | triple-months qualifying %d of %d | share %s | %s" % (
        r["qualifying"], r["eligible"], cell(r["share"], r["eligible"]),
        "PASS: Strip reversion enters B2 (both versions)" if r["pass"] else "FAIL: Strip reversion dropped unbuilt"))
    gates["R1"] = "PASS" if r["pass"] else "FAIL"
    # ---- first-published inputs (data entry items 2, 5)
    for sid, k in (("CPILFESL", 12), ("M2SL", 12), ("PCEPILFE", 12), ("UNRATE", None)):
        sh, n = ci.flagged_share(sid, k)
        out("CARD INPUTS | %s %s | first published where a comparable vintage exists, else latest (flagged) | flagged "
            "share 1975-2010 %s | breaks %s" % (sid, "%d-month change" % k if k else "level", cell(sh, n),
                                                 "n/a (level)" if not k else (", ".join(str(x) for x in
                                                                                     ci.breaks(sid)) or "none")))
    lv = gspc.dropna().copy()
    lv.index = pd.DatetimeIndex(lv.index).normalize()
    spx_me = lv.groupby(lv.index.to_period("M")).last()
    F0R = []                                                    # (rule, held months, note)

    def f0line(name, held, note=""):
        x = f0(held, name)
        x["note"] = note
        F0R.append(x)
    # ---- C2-D1
    c2 = c2d1(R, rates)
    res["C2-D1"] = c2
    out("C2-D1 | worst-fifth months by country (low-rate / other): %s" % ", ".join(
        "%s %d / %d" % (k, a_, b_) for k, (a_, b_) in c2["countries"].items()))
    for lab in ("pooled", "japan"):
        g = c2[lab]
        out("C2-D1 | %s | 10-year bond mean excess return: rate < 1.0 %s | rate >= 1.0 %s | %s" % (
            lab, cell(g["mean_low"] * 1200 if g["mean_low"] == g["mean_low"] else g["mean_low"], g["n_low"], "%.2f %%/yr"),
            cell(g["mean_other"] * 1200 if g["mean_other"] == g["mean_other"] else g["mean_other"], g["n_other"],
                 "%.2f %%/yr"),
            ("PASS" if g["pass"] else "FAIL") + (" (gate)" if lab == "pooled" else " (reported)")))
    gates["C2-D1"] = "PASS" if c2["pooled"]["pass"] else "FAIL"
    out("C2-D1 GATE | %s" % ("PASS: floor versions on card 1 R1, R2 and a card 2 stop line (they change no count here, "
                             "addendum A2)" if c2["pooled"]["pass"] else "FAIL: no change"))
    # ---- card 1: C1-D1, C1-D2, F0
    rules1 = card1_rules(ci, R, vol, spx_me)
    r5 = card1_r5(fxv, vol)
    rules1["card 1 R5"] = rule(r5["legs"], r5["cond_months"], 4)
    g11, g12 = [], []
    res["C1-D1"], res["C1-D2"] = {}, {}
    for name in ("card 1 R1", "card 1 R2", "card 1 R3", "card 1 R4", "card 1 R5"):
        ru = rules1[name]
        d1 = c1d1(ru["cond_months"])
        res["C1-D1"][name] = d1
        out("C1-D1 | %s | condition months (any version) %d | episodes %d | gate fewer than 6 | %s" % (
            name, d1["condition_months"], d1["episodes"], ("PASS: " if d1["pass"] else "FAIL: ") + d1["outcome"]))
        g11.append("%s %s" % (name[7:], "PASS" if d1["pass"] else "FAIL"))
        kept, dr = {}, []
        res["C1-D2"][name] = {}
        for lg_, frame in ru["legs"].items():
            sh, n = same_sign_share(frame, book_pos, start=ru["start"])
            drop = bool(n and sh > 0.80)
            res["C1-D2"][name][lg_] = {"share": sh, "n": n, "drop": drop}
            out("C1-D2 | %s %s leg | held market-months %d | same sign as the book %s | gate > 0.80 | %s" % (
                name, lg_, n, cell(sh, n), "leg dropped" if drop else "leg stays"))
            if drop:
                dr.append(lg_)
            else:
                kept[lg_] = frame
        g12.append("%s %s" % (name[7:], ("dropped " + "/".join(dr)) if dr else "all legs stay"))
        pos = pd.concat(list(kept.values()), axis=1) if kept else pd.DataFrame(index=R.index)
        f0line(name, nonzero_months(pos, start=ru["start"]) if kept else [],
               "" if d1["pass"] else "rule not in B2: C1-D1 watch condition")
    gates["C1-D1"] = ", ".join(g11)
    gates["C1-D2"] = ", ".join(g12)
    # ---- card 2: C2-D2, F0
    r45 = r4_state(ci, 4.5).reindex(R.index)
    v2 = card2_rules(ci, R, vol, spx_me)
    res["C2-D2"] = {}
    g22 = []
    for name, mk in (("card 2 R1", "bd_us_10y"), ("card 2 R2", "eq_us_spx")):
        kp = c2d2(v2[name], r45)
        res["C2-D2"][name] = kp
        for v, x in kp.items():
            out("C2-D2 | %s version %s | on-months %d | episodes %d | share inside card 1 R4's 4.5 state %s | %s" % (
                name, "/".join(str(z) for z in v), x["on"], x["episodes"], cell(x["inside"], x["on"]),
                "kept" if x["keep"] else "left out"))
        nk = sum(1 for x in kp.values() if x["keep"])
        g22.append("%s %d of %d versions kept" % (name[7:], nk, len(kp)))
        if nk:
            ru = card2_rule(v2[name], kp, mk, -1, vol, R.index)
            f0line(name, nonzero_months(ru["pos"]))
        else:
            out("C2-D2 | %s | no version left: the rule is not run" % name)
            f0line(name, [], "rule not run: C2-D2 left every version out")
    gates["C2-D2"] = ", ".join(g22)
    # ---- card 3: C3-D2, C3-D1, F0
    rules3, d32, aux = card3_rules(ci, R, vol, rates)
    res["C3-D2"] = d32
    out("C3-D2 | card 3 R1 activity gate | design months with the FEDFUNDS 12-month range below 0.50: %d | gate fewer "
        "than 60 | %s" % (d32["gate_off_months"], "gate kept (R1 16 versions with sizing)" if d32["gate_kept"] else
                          "gate dropped (R1 8 versions with sizing)"))
    gates["C3-D2"] = "gate kept" if d32["gate_kept"] else "gate dropped"
    eps = lseg.monthly(EPS_SID)
    r4 = card3_r4(eps, spx_me, rates["TB3MS"], vol["eq_us_spx"])
    rules3["card 3 R4"] = rule({"leg": r4["pos"].to_frame("eq_us_spx")}, [], 4, r4["start"])
    res["C3-D1"] = {}
    g31 = []
    for name in ("card 3 R1", "card 3 R2", "card 3 R3", "card 3 R4"):
        ru = rules3[name]
        sh, n = same_sign_share(ru["pos"], book_pos, start=ru["start"])
        lab = "dropped before B2" if (n and sh >= 0.80) else ("kept, flagged" if (n and sh >= 0.50) else "kept")
        res["C3-D1"][name] = {"share": sh, "n": n, "outcome": lab}
        out("C3-D1 | %s | versions %d | held market-months %d | same sign as the book %s | gate >= 0.80 dropped, "
            "0.50-0.80 flagged | %s" % (name, ru["versions"], n, cell(sh, n), lab))
        g31.append("%s %s" % (name[7:], lab))
        f0line(name, nonzero_months(ru["pos"], start=ru["start"]),
               "rule not in B2: C3-D1 dropped" if lab.startswith("dropped") else "")
    gates["C3-D1"] = ", ".join(g31)
    out("C3-D1 | reported lines (cards 1 and 2 in shared markets; R1 against Economic trend's monetary theme; R3 against "
        "Carry's directional bonds) are not gates and are not printed in this version")
    # ---- card 4: C4-D1, C4-D2, F0
    c41 = c4d1(ci, gspc)
    res["C4-D1"] = c41
    for lab, x in c41["windows"].items():
        out("C4-D1 | %s | up-months state on %d / other %d | median ratio %s | at least 1.25: %s" % (
            lab, x["on"], x["off"], ("%.2f" % x["ratio"]) if (x["on"] >= MIN_PRINT and x["off"] >= MIN_PRINT and
                                                              x["ratio"] == x["ratio"]) else "count only",
            "yes" if x["ok"] else "no"))
    out("C4-D1 GATE | %s" % ("PASS: half-size sizing version on card 4 R1-R4 (it changes no held month)" if c41["pass"]
                             else "FAIL: analyst question only"))
    gates["C4-D1"] = "PASS" if c41["pass"] else "FAIL"
    v45, st45 = card4_r5(ci, R, aux)
    sp_, spm = aux["S"], aux["Smean"]
    r2on = ((sp_ < 1.0) | (sp_ < spm)).fillna(False)            # card 3 R2 on, either version
    score = DG.trend_parts(R, D, S, cfg)[2]                      # the A2-final book's Trend score (addendum A6)
    c42 = c4d2(v45, r2on, score)
    res["C4-D2"] = c42
    for v, x in c42["versions"].items():
        out("C4-D2 | card 4 R5 version %d | on-months %d | share with card 3 R2 on %s | share with Trend long 2-year and "
            "short or flat 10-year %s" % (v, x["on"], cell(x["r2"], x["on"]), cell(x["trend"], x["on"])))
    out("C4-D2 GATE | either share >= 0.80 in both versions: %s | %s" % (
        "yes" if c42["not_registered"] else "no", "R5 not registered (note to card 3 R2)" if c42["not_registered"] else
        "R5 stays"))
    gates["C4-D2"] = "R5 not registered" if c42["not_registered"] else "R5 stays"
    c4 = card4_days(gspc, days, vol["eq_us_spx"])
    for name in ("card 4 R1", "card 4 R2", "card 4 R3", "card 4 R4"):
        f0line(name, c4[name]["months"])
    p5 = (v45[1][1] + v45[2][1]) / 2
    f0line("card 4 R5", nonzero_months(p5, start=st45), "rule not in B2: C4-D2" if c42["not_registered"] else "")
    # ---- card 5: C5-D1, C5-D2, F0
    P = {mk: lseg.monthly(sid) for mk, sid in C5_P.items()}
    r5c = card5_r1(P, vol)
    avg, nv = trend12_avg_sign(R, D)
    c5 = c5d1(r5c, avg, book_pos)
    res["C5-D1"] = c5
    out("C5-D1 | card 5 R1 | held market-months %d (%s) | 12-month Trend versions (%d) long by average sign %s | gate "
        ">= 0.75 | %s" % (c5["n"], ", ".join("%s %d" % kv for kv in c5["by_market"].items()), nv,
                          cell(c5["share"], c5["n"]), "R1 not registered" if c5["not_registered"] else "R1 stays"))
    out("C5-D1 | reported, not a gate: same sign as the book's net position %s" % cell(c5["book_share"], c5["book_n"]))
    gates["C5-D1"] = "R1 %s" % ("not registered" if c5["not_registered"] else "stays")
    Pg = {k: lseg.monthly(s_) for k, s_ in C5_GRAINS.items()}
    c52 = c5d2({"copper": P["cm_copper"]}, {"crude": P["cm_wti"]}, Pg)
    res["C5-D2"] = c52
    out("C5-D2 | reported line not computed: %s" % C5_REPORTED_NOT_RUN)
    for lab in ("slow", "grains", "crude"):
        x = c52[lab]
        sh = ("share higher 24 months on %.3f" % x["share"]) if x["breaks"] >= MIN_PRINT else \
            "share printed as counts only"
        out("C5-D2 | %s | breaks to 2008-12 %d | higher 24 months on %d | %s%s" % (
            {"slow": "slow class (copper)", "grains": "grains (wheat, corn, soybeans)", "crude": "crude (reported)"}[lab],
            x["breaks"], x["higher"], sh,
            "" if not x["no_outcome"] else " | no 24-month value %d" % x["no_outcome"]))
    out("C5-D2 GATE | slow minus grains %s | at least 10 breaks each: %s | %s" % (
        ("sign " + ("+" if c52["diff"] > 0 else ("-" if c52["diff"] < 0 else "0"))) if c52["diff"] == c52["diff"]
        else "n/a", "yes" if (c52["slow"]["breaks"] >= 10 and c52["grains"]["breaks"] >= 10) else "no",
        "PASS: R1 built" if c52["pass"] else "FAIL: R1 dropped unbuilt"))
    gates["C5-D2"] = "PASS" if c52["pass"] else "FAIL"
    note5 = "; ".join(x for x in ("rule not in B2: C5-D1" if c5["not_registered"] else "",
                                  "rule not in B2: C5-D2" if not c52["pass"] else "") if x)
    f0line("card 5 R1", nonzero_months(r5c["pos"]), note5)
    # ---- F0
    res["F0"] = F0R
    for x in F0R:
        out("F0 | %s | held months %d | episodes %d | at least 48 and 3: %s | %s%s" % (
            x["rule"], x["held"], x["episodes"], "yes" if x["judgeable"] else "no", x["outcome"],
            (" | " + x["note"]) if x["note"] else ""))
    gates["F0"] = "; ".join("%s %s" % (x["rule"], "judged in B2" if x["judgeable"] else "not judgeable") for x in F0R)
    out("PRE-B SUMMARY | " + " | ".join("%s: %s" % (k, gates[k]) for k in DIAG_IDS))
    return {"gates": gates, "res": res}


def trial_rows(res, panel_id_, engine_version, cfg=None):
    """gm/trials.csv rows of family 'diag', one per diagnostic run (entry item 8), no Sharpe columns."""
    from gm import config as CF
    cfg = cfg or CF.A1_INCUMBENT
    rows = []
    for d in DIAG_IDS:
        c = {"diag": d, "version": VERSION, "book": CF.cfg_hash(cfg), "panel": panel_id_[:16], "lseg": LSEG_LOCK[:16]}
        rows.append({"trial": "%s diagnostic (pre-B)" % d, "family": "diag", "hash": CF.cfg_hash(c),
                     "note": "TESTING_PROTOCOL 7.5 %s, 7.6 step 7, gm/CHANGES.md 'Pre-B diagnostics'; engine %s; A1 "
                             "panel %s; LOCK_v2 %s; LSEG %s; book %s (%s); outcome: %s" % (
                                 d, engine_version, panel_id_[:16], LOCK_V2[:16], LSEG_LOCK[:16], cfg["name"],
                                 CF.cfg_hash(cfg), res["gates"][d]),
                     "config": json.dumps(c, sort_keys=True)})
    return rows
