"""eq_scorecard (runs on WRDS Cloud): the investor scorecard of the equity plan (step E0.4 phase B), as registered in
docs/research/equity/STAGE0_REGISTRATION.md sections 2-9. One of the two seal-exempt jobs (plan v0.3 section 5.4):
it reads US 13F holdings, CRSP stock returns and CRSP fund returns from 2010-06 to the seal end (2025-12) and prints
only the output of registration section 8: statistics and rank shares per library investor, the tier lists, the
best-scored filers and funds the library holds no document for (name and rank shares), persistence tables and counts.
It prints no holding, no stock name, no return series and no average by style, sector or factor.

Build note (functions, the reading taken where the registration left room, run time):
docs/research/equity/SCORECARD_BUILD_NOTE.md. The investor table is the frozen file of phase A2, embedded below by
tools/equity/make_scorecard_job.py; it is the only investor input.

Job steps (tools/wrdsq/jobs/eq_scorecard_v1.json); every pull is resumable (one data set per year, kept on WRDS):
  pull_base(sql, save, out, DATA)        manager names, CUSIP map, factors, book-to-market, fund headers and styles
  pull_crsp(sql, save, out, DATA)        crsp.msf_v2 2009-06..2025-12
  pull_agg(sql, save, out, DATA)         per filer and quarter: matched positions and value (SQL aggregate)
  pull_hold(sql, load, save, out, DATA)  holdings rows of the filers that can be in a rank group, and library filers
  pull_funds(sql, save, out, DATA)       CRSP fund monthly returns and assets
  build(load, save, out)                 the scorecard; the report lines are kept as data set eq_sc_report
  report(load, out, part, parts)         prints one part of the report (each python step stays under 60,000 chars)
"""
import hashlib
import json
import os
import random
import time
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

VERSION = "eq_scorecard-1.0.0"

# >>> FROZEN INPUT (written by tools/equity/make_scorecard_job.py; the only part that may change between runs) >>>
INV = json.loads(r"""[]""")
DOCS = json.loads(r"""[]""")
# <<< FROZEN INPUT <<<

# ------------------------------------------------------------------------------------------- registered settings
H_FROM, H_TO = "2010-06-30", "2025-12-31"          # quarter-ends of 13F holdings read
CRSP_FROM = 200906                                   # first CRSP month (momentum of the June 2010 peer groups)
M_FIRST, M_LAST = 201101, 202512                     # record months computed (seal end 2025-12)
WINDOWS = [("2011-15", 201101, 201512), ("2016-20", 201601, 202012), ("2021-25", 202101, 202512),
           ("2011-25", 201101, 202512)]
BLOCKS = ("2011-15", "2016-20", "2021-25")
MIN_RESULT, MIN_STATS, NW_LAGS = 36, 60, 3
POS_LO, POS_HI, VAL_MIN = 5, 150, 100e6              # rank group of 13F filers (median over the window's filings)
FUND_TNA_MIN = 15.0                                  # $M, mean assets over the window
TIER_RECORD, STYLE_CAP, TIER_EXPLICIT, CONTROL_N, SEED = 30, 8, 10, 10, 20261117
FOUND_N, TOP_FILERS, TOP_FUNDS = 50, 25, 10
FY0, FY1 = 2010, 2025                                # June formation years of the peer groups
PRE_LO, PRE_HI, PRE_VAL, PRE_MONTHS = 3, 200, 75e6, 30   # loose pre-filter of pull_hold (superset of rank groups)
CHUNK = 55000


def _mi(ym):
    return (np.asarray(ym) // 100) * 12 + np.asarray(ym) % 100 - 1


def _ym(mi):
    return (np.asarray(mi) // 12) * 100 + np.asarray(mi) % 12 + 1


MI_FIRST, MI_LAST, MI_CRSP = int(_mi(M_FIRST)), int(_mi(M_LAST)), int(_mi(CRSP_FROM))
WIN = [(w, int(_mi(a)), int(_mi(b))) for w, a, b in WINDOWS]


def _q_of(d):
    d = pd.to_datetime(d)
    return (d.dt.year * 4 + (d.dt.month - 1) // 3).astype("int64").to_numpy()


def _qend_mi(q):
    q = np.asarray(q)
    return (q // 4) * 12 + 3 * (q % 4) + 2


def _entry_mi(q):
    """Month in which the 45-day deadline of quarter q falls (holdings enter at its close)."""
    y, k = divmod(int(q), 4)
    d = pd.Timestamp(y, 3 * k + 3, 1) + pd.offsets.MonthEnd(0) + pd.Timedelta(days=45)
    return d.year * 12 + d.month - 1


def input_sha():
    return hashlib.sha256(json.dumps([INV, DOCS], sort_keys=True).encode()).hexdigest()


# ------------------------------------------------------------------------------------------------------- pulls
def _runner(save, out, data, budget):
    t0 = time.time()
    st = {"left": 0}

    def have(name):
        return bool(data) and os.path.exists(os.path.join(data, name + ".csv.gz"))

    def step(name, fn):
        if have(name):
            return
        if time.time() - t0 > budget:
            st["left"] += 1
            return
        t1 = time.time()
        df = fn()
        save(name, df)
        out("  %-18s %9d rows %6.0f s" % (name, len(df), time.time() - t1))
    return have, step, st, t0


def _done(out, what, st, t0):
    out("%s: %s after %.0f s" % (what, ("%d data sets left for the next run" % st["left"]) if st["left"]
                                else "complete", time.time() - t0))


def pull_base(sql, save, out, data, budget=9000):
    have, step, st, t0 = _runner(save, out, data, budget)
    step("eq_sc_names", lambda: sql("/* eqsc names */ select mgrno, mgrname, rdate2 from tfn.s34names"))
    step("eq_sc_cusip", lambda: sql(
        "/* eqsc cusip */ select distinct cusip, permno, namedt, nameenddt from crsp.stocknames_v2 "
        "where cusip is not null"))
    step("eq_sc_ff", lambda: sql(
        "/* eqsc ff */ select date, mktrf, smb, hml, rmw, cma, umd, rf from ff.fivefactors_monthly "
        "where date between '2009-01-01' and '2025-12-31'"))
    step("eq_sc_bm", lambda: sql(
        "/* eqsc bm */ select permno, public_date, bm from wrdsapps_finratio.firm_ratio where permno is not null "
        "and public_date between '%d-01-01' and '%d-06-30' and extract(month from public_date) <= 6"
        % (FY0, FY1)))
    step("eq_sc_fhdr", lambda: sql(
        "/* eqsc fhdr */ select crsp_fundno, crsp_portno, crsp_cl_grp, fund_name, index_fund_flag, et_flag "
        "from crsp.fund_hdr"))
    step("eq_sc_fsty", lambda: sql(
        "/* eqsc fsty */ select crsp_fundno, begdt, enddt, crsp_obj_cd from crsp.fund_style "
        "where enddt >= '2010-12-01' or enddt is null"))
    _done(out, "pull_base", st, t0)


def pull_crsp(sql, save, out, data, budget=9000):
    have, step, st, t0 = _runner(save, out, data, budget)
    for y in range(CRSP_FROM // 100, M_LAST // 100 + 1):
        lo = "%d-%02d-01" % (y, CRSP_FROM % 100) if y == CRSP_FROM // 100 else "%d-01-01" % y
        step("eq_sc_msf_%d" % y, lambda lo=lo, y=y: sql(
            "/* eqsc msf %s %d-12-31 */ select permno, yyyymm, mthret, mthprc, shrout, primaryexch, securitytype, "
            "securitysubtype, sharetype from crsp.msf_v2 where mthcaldt between '%s' and '%d-12-31'"
            % (lo, y, lo, y)))
    _done(out, "pull_crsp", st, t0)


def _hyears():
    return list(range(int(H_FROM[:4]), int(H_TO[:4]) + 1))


def _hrange(y):
    return (H_FROM if y == int(H_FROM[:4]) else "%d-01-01" % y), (H_TO if y == int(H_TO[:4]) else "%d-12-31" % y)


AGG_SQL = """/* eqsc agg %(lo)s %(hi)s */
with h as (
  select mgrno, rdate, cusip, sum(shares)::float8 as sh, sum(shares * coalesce(prc, 0))::float8 as fv
  from tfn.s34
  where fdate = rdate and shares > 0 and rdate between '%(lo)s' and '%(hi)s'
  group by mgrno, rdate, cusip),
n as (
  select distinct cusip, permno, namedt, coalesce(nameenddt, date '2099-12-31') as ne
  from crsp.stocknames_v2 where cusip is not null),
k as (
  select distinct on (h.mgrno, h.rdate, h.cusip) h.mgrno, h.rdate, h.sh, h.fv, n.permno
  from h left join n on n.cusip = h.cusip and h.rdate between n.namedt and n.ne
  order by h.mgrno, h.rdate, h.cusip, n.permno),
p as (
  select permno, yyyymm, abs(mthprc)::float8 as px from crsp.msf_v2
  where mthcaldt between '%(lo)s' and '%(hi)s' and mthprc is not null and mthprc <> 0)
select k.mgrno, k.rdate, sum(k.fv) as fv_all,
  sum(case when p.px is not null then k.fv else 0 end) as fv_used,
  count(distinct case when p.px is not null then k.permno end) as npos,
  sum(case when p.px is not null then k.sh * p.px else 0 end) as val
from k left join p on p.permno = k.permno
  and p.yyyymm = (extract(year from k.rdate) * 100 + extract(month from k.rdate))::int
group by k.mgrno, k.rdate"""


def pull_agg(sql, save, out, data, budget=9000):
    have, step, st, t0 = _runner(save, out, data, budget)
    for y in _hyears():
        lo, hi = _hrange(y)
        step("eq_sc_agg_%d" % y, lambda lo=lo, hi=hi: sql(AGG_SQL % {"lo": lo, "hi": hi}))
    _done(out, "pull_agg", st, t0)


def _lib_mgrnos():
    return sorted({int(m) for p in INV if p.get("record_kind") == "13f" for m in p.get("mgrnos", [])})


def _lib_fundnos():
    return sorted({int(f) for p in INV if p.get("record_kind") == "fund" for f in p.get("fundnos", [])})


def candidates(load):
    """Filers that can be in a rank group of some window (loose pre-filter on the SQL aggregate) + library filers."""
    a = pd.concat([load("eq_sc_agg_%d" % y) for y in _hyears()], ignore_index=True)
    a = a[(a.npos >= 1) & (a.val > 0)]
    f = pd.DataFrame({"bk": a.mgrno.astype("int64").to_numpy(), "q": _q_of(a.rdate),
                      "npos": a.npos.to_numpy(float), "val": a.val.to_numpy(float)})
    f = f.groupby(["bk", "q"], as_index=False).agg(npos=("npos", "sum"), val=("val", "sum"))
    f = _schedule(f, {})
    keep = set()
    for w, a0, b0 in WIN:
        lo, hi = _win_span(f, a0, b0)
        sub = f[lo <= hi].assign(n=(hi - lo + 1)[lo <= hi])
        g = sub.groupby("bk").agg(npos=("npos", "median"), val=("val", "median"), n=("n", "sum"))
        ok = (g.npos >= PRE_LO) & (g.npos <= PRE_HI) & (g.val >= PRE_VAL) & (g.n >= PRE_MONTHS)
        keep |= set(g.index[ok].tolist())
    return sorted(keep | set(_lib_mgrnos()))


def pull_hold(sql, load, save, out, data, budget=9000):
    have, step, st, t0 = _runner(save, out, data, budget)
    if not all(have("eq_sc_agg_%d" % y) for y in _hyears()):
        out("pull_hold: the per-quarter aggregates are not complete; run pull_agg again")
        return
    step("eq_sc_cand", lambda: pd.DataFrame({"mgrno": candidates(load)}))
    if not have("eq_sc_cand"):
        out("pull_hold: candidate list not written yet; run again")
        return
    ids = load("eq_sc_cand").mgrno.astype("int64").tolist()
    inl = ",".join(str(i) for i in ids) or "-1"
    out("  candidate filers: %d" % len(ids))
    for y in _hyears():
        lo, hi = _hrange(y)
        step("eq_sc_hold_%d" % y, lambda lo=lo, hi=hi: sql(
            "/* eqsc hold %s %s */ select mgrno, rdate, cusip, shares::float8 as shares, prc::float8 as prc "
            "from tfn.s34 where fdate = rdate and shares > 0 and rdate between '%s' and '%s' and mgrno in (%s)"
            % (lo, hi, lo, hi, inl)))
    _done(out, "pull_hold", st, t0)


def pull_funds(sql, save, out, data, budget=9000):
    have, step, st, t0 = _runner(save, out, data, budget)
    lib = ",".join(str(f) for f in _lib_fundnos())
    cond = "crsp_fundno in (select crsp_fundno from crsp.fund_style where crsp_obj_cd like 'ED%')"
    if lib:      # all share classes of the library funds (same class group, else same portfolio)
        cond = ("(%s or crsp_fundno in (%s) or crsp_fundno in (select crsp_fundno from crsp.fund_hdr where "
                "crsp_cl_grp in (select crsp_cl_grp from crsp.fund_hdr where crsp_fundno in (%s)) or "
                "(crsp_cl_grp is null and crsp_portno in (select crsp_portno from crsp.fund_hdr where "
                "crsp_cl_grp is null and crsp_fundno in (%s)))))" % (cond, lib, lib, lib))
    for y in range(M_FIRST // 100 - 1, M_LAST // 100 + 1):
        lo = "%d-12-01" % y if y < M_FIRST // 100 else "%d-01-01" % y
        step("eq_sc_fret_%d" % y, lambda lo=lo, y=y: sql(
            "/* eqsc fret %s %d-12-31 */ select crsp_fundno, caldt, mtna::float8 as mtna, mret::float8 as mret "
            "from crsp.monthly_tna_ret_nav where caldt between '%s' and '%d-12-31' and %s"
            % (lo, y, lo, y, cond)))
    _done(out, "pull_funds", st, t0)


# ----------------------------------------------------------------------------------------------- CRSP panel
class Panel(object):
    """CRSP monthly panel as arrays: rows = permno (sorted), columns = months from 2009-06 to 2025-12."""

    def __init__(self, msf):
        msf = msf.copy()
        msf["j"] = _mi(msf.yyyymm.astype("int64").to_numpy()) - MI_CRSP
        msf = msf[(msf.j >= 0) & (msf.j <= MI_LAST - MI_CRSP)]
        msf = msf.drop_duplicates(["permno", "j"], keep="last")
        self.perm = np.sort(msf.permno.astype("int64").unique())
        self.nm = MI_LAST - MI_CRSP + 1
        ri = np.searchsorted(self.perm, msf.permno.astype("int64").to_numpy())
        j = msf.j.to_numpy()
        shape = (len(self.perm), self.nm)
        self.R = np.full(shape, np.nan)
        self.P = np.full(shape, np.nan)
        self.C = np.full(shape, np.nan)
        self.COM = np.zeros(shape, bool)
        self.NY = np.zeros(shape, bool)
        self.R[ri, j] = pd.to_numeric(msf.mthret, errors="coerce").to_numpy(float)
        p = np.abs(pd.to_numeric(msf.mthprc, errors="coerce").to_numpy(float))
        p[p == 0] = np.nan
        self.P[ri, j] = p
        self.C[ri, j] = p * pd.to_numeric(msf.shrout, errors="coerce").to_numpy(float)
        def txt(c):
            return msf[c].fillna("").astype(str).to_numpy()
        ex = txt("primaryexch")
        self.COM[ri, j] = ((txt("securitytype") == "EQTY") & (txt("securitysubtype") == "COM")
                           & (txt("sharetype") == "NS") & np.isin(ex, ["N", "A", "Q"]))
        self.NY[ri, j] = ex == "N"

    def rows(self, permno):
        permno = np.asarray(permno, dtype="int64")
        i = np.searchsorted(self.perm, permno)
        ic = np.minimum(i, len(self.perm) - 1)
        ok = (i < len(self.perm)) & (self.perm[ic] == permno) if len(self.perm) else np.zeros(len(permno), bool)
        return ic, ok

    def at(self, arr, ri, ok, mi):
        mi = np.broadcast_to(np.asarray(mi), ri.shape)
        j = mi - MI_CRSP
        good = ok & (j >= 0) & (j < self.nm)
        v = np.full(ri.shape, np.nan)
        v[good] = arr[ri[good], j[good]]
        return v


def stock_returns(msf):
    """Monthly total return per CRSP security: crsp.msf_v2 mthret, which includes the delisting return in the
    delisting month. After its last month a security has no row: a position in it earns zero and keeps its weight."""
    return msf


def _bm_table(bm, panel):
    """Book-to-market per permno and formation year: latest firm_ratio row with public_date on or before June 30."""
    b = bm.copy()
    d = pd.to_datetime(b.public_date)
    b = b[d.dt.month <= 6]
    b["fy"] = d[d.dt.month <= 6].dt.year.to_numpy()
    b["d"] = d[d.dt.month <= 6].to_numpy()
    b["bm"] = pd.to_numeric(b.bm, errors="coerce")
    b = b[np.isfinite(b.bm)].sort_values(["permno", "fy", "d"]).drop_duplicates(["permno", "fy"], keep="last")
    out = np.full((len(panel.perm), FY1 - FY0 + 1), np.nan)
    ri, ok = panel.rows(b.permno.to_numpy())
    col = b.fy.to_numpy() - FY0
    good = ok & (col >= 0) & (col <= FY1 - FY0)
    out[ri[good], col[good]] = b.bm.to_numpy()[good]
    return out


def _fifths(v, ids):
    """Fifths 0..4 of v (ties broken by id): floor(5 * rank / n)."""
    order = np.lexsort((ids, v))
    rk = np.empty(len(v), dtype="int64")
    rk[order] = np.arange(len(v))
    return (5 * rk) // max(len(v), 1)


class Peers(object):
    """DGTW peer groups (125) formed each June, held July to June; value-weighted group returns per month."""

    def __init__(self, panel, bmt):
        self.panel = panel
        self.G = np.full((len(panel.perm), FY1 - FY0 + 1), -1, dtype="int16")
        self.B = np.full((125, panel.nm), np.nan)
        for fy in range(FY0, FY1 + 1):
            self._form(fy, bmt)

    def _j(self, mi):
        return int(mi) - MI_CRSP

    def _form(self, fy, bmt):
        p = self.panel
        js = self._j(fy * 12 + 5)       # size at the end of June of the formation year
        jf = self._j(fy * 12 + 5)       # share type and exchange at the end of June
        jm = self._j(fy * 12 + 5)       # momentum: the twelve months June (fy-1) .. May (fy)
        if jm - 12 < 0 or js >= p.nm:
            return
        cap = p.C[:, js]
        mom = np.prod(1.0 + p.R[:, jm - 12:jm], axis=1) - 1.0
        bmv = bmt[:, fy - FY0]
        u = p.COM[:, jf] & np.isfinite(cap) & (cap > 0) & np.isfinite(bmv) & (bmv > 0) & np.isfinite(mom)
        ny = u & p.NY[:, jf]
        if ny.sum() < 5:
            return
        bps = np.percentile(cap[ny], [20, 40, 60, 80])
        idx = np.where(u)[0]
        s = np.searchsorted(bps, cap[idx], side="left")
        g = np.full(len(idx), -1, dtype="int64")
        ids = p.perm[idx]
        for si in range(5):
            a = np.where(s == si)[0]
            if not len(a):
                continue
            b = _fifths(bmv[idx[a]], ids[a])
            for bi in range(5):
                c = a[b == bi]
                if not len(c):
                    continue
                m = _fifths(mom[idx[c]], ids[c])
                g[c] = si * 25 + bi * 5 + m
        self.G[idx, fy - FY0] = g
        # value-weighted group returns July fy .. June fy+1 (weights: previous month-end market value)
        gg = self.G[:, fy - FY0].astype("int64")
        for mi in range(fy * 12 + 6, fy * 12 + 18):
            j = self._j(mi)
            if j <= 0 or j >= p.nm:
                continue
            r, w = p.R[:, j], p.C[:, j - 1]
            v = (gg >= 0) & np.isfinite(r) & np.isfinite(w) & (w > 0)
            sw = np.bincount(gg[v], weights=w[v], minlength=125)
            swr = np.bincount(gg[v], weights=w[v] * r[v], minlength=125)
            with np.errstate(invalid="ignore", divide="ignore"):
                self.B[:, j] = np.where(sw > 0, swr / sw, np.nan)

    def group(self, ri, ok, mi):
        fy = np.where(np.asarray(mi) % 12 >= 6, np.asarray(mi) // 12, np.asarray(mi) // 12 - 1)
        col = np.broadcast_to(fy - FY0, ri.shape)
        good = ok & (col >= 0) & (col <= FY1 - FY0)
        g = np.full(ri.shape, -1, dtype="int64")
        g[good] = self.G[ri[good], col[good]]
        return g

    def bench(self, g, mi):
        j = int(mi) - MI_CRSP
        b = np.full(g.shape, np.nan)
        if 0 <= j < self.panel.nm:
            v = g >= 0
            b[v] = self.B[g[v], j]
        return b


# ------------------------------------------------------------------------------------------- factors, stats
class Factors(object):
    def __init__(self, ff):
        d = pd.to_datetime(ff["date"])
        mi = (d.dt.year * 12 + d.dt.month - 1).to_numpy()
        n = MI_LAST - MI_CRSP + 1
        self.X = np.full((n, 6), np.nan)
        self.RF = np.full(n, np.nan)
        j = mi - MI_CRSP
        v = (j >= 0) & (j < n)
        cols = ["mktrf", "smb", "hml", "rmw", "cma", "umd"]
        self.X[j[v]] = ff[cols].apply(pd.to_numeric, errors="coerce").to_numpy(float)[v]
        self.RF[j[v]] = pd.to_numeric(ff["rf"], errors="coerce").to_numpy(float)[v]
        self.MKT = self.X[:, 0] + self.RF


def ols_nw(y, X, lags):
    """OLS with an intercept and Newey-West standard errors (Bartlett weights, small-sample factor n/(n-k)), the
    form of qs/btstats.ols_nw. Returns (coefficients, t-values)."""
    y = np.asarray(y, float)
    X = np.column_stack([np.ones(len(y)), np.asarray(X, float)])
    n, k = X.shape
    if n <= k + 1:
        return None, None
    XtX_inv = np.linalg.pinv(X.T @ X)
    b = XtX_inv @ X.T @ y
    u = y - X @ b
    Xu = X * u[:, None]
    S = Xu.T @ Xu
    for lag in range(1, lags + 1):
        G = Xu[lag:].T @ Xu[:-lag]
        S += (1 - lag / (lags + 1.0)) * (G + G.T)
    V = XtX_inv @ S @ XtX_inv * n / max(n - k, 1)
    se = np.sqrt(np.maximum(np.diag(V), 1e-30))
    return b, b / se


def _stats(mi, ret, ff, extra=None):
    """Window statistics of a monthly return series (months mi, sorted)."""
    n = len(mi)
    st = {"n": n}
    if n == 0:
        return st
    j = mi - MI_CRSP
    if n >= MIN_RESULT:
        X, ex = ff.X[j], ret - ff.RF[j]
        ok = np.isfinite(ex) & np.all(np.isfinite(X), axis=1)
        b, t = ols_nw(ex[ok], X[ok], NW_LAGS)
        if b is not None:
            st["a"], st["t"] = 1200.0 * b[0], t[0]
    st["r"] = 100.0 * (np.prod(1.0 + ret) ** (12.0 / n) - 1.0)
    mk = ff.MKT[j]
    if np.all(np.isfinite(mk)):
        st["rm"] = st["r"] - 100.0 * (np.prod(1.0 + mk) ** (12.0 / n) - 1.0)
    w = np.cumprod(1.0 + ret)
    peak = np.maximum.accumulate(np.concatenate([[1.0], w]))[1:]
    st["dd"] = 100.0 * float(np.min(w / peak - 1.0))
    yrs = mi // 12
    beat = full = 0
    for y in np.unique(yrs):
        s = yrs == y
        if s.sum() == 12 and np.all(np.isfinite(mk[s])):
            full += 1
            beat += int(np.prod(1.0 + ret[s]) > np.prod(1.0 + mk[s]))
    if full:
        st["yb"] = beat / float(full)
    for key, arr in (extra or {}).items():
        a = np.asarray(arr, float)
        f = np.isfinite(a)
        if key in ("pa", "p10", "pn"):
            if f.sum():
                st[key] = 1200.0 * float(np.mean(a[f]))
        elif f.sum():
            st[key] = float(np.mean(a[f]))
    return st


# ------------------------------------------------------------------------------------------ 13F copy books
def _positions(h, cus, panel):
    """Matched positions per filer and quarter (first versions; CUSIP valid at the quarter-end; CRSP price at the
    quarter-end) and per filing the filed and used value."""
    h = h[h.cusip.notna() & h.mgrno.notna()].copy()
    h["cusip"] = h.cusip.astype(str)
    h["mgrno"] = h.mgrno.astype("int64")
    h["rdate"] = pd.to_datetime(h.rdate)
    h["q"] = _q_of(h.rdate)
    h["fv"] = h.shares.astype(float) * pd.to_numeric(h.prc, errors="coerce").abs().fillna(0.0).to_numpy()
    g = h.groupby(["mgrno", "q", "cusip"], as_index=False).agg(sh=("shares", "sum"), fv=("fv", "sum"),
                                                              rdate=("rdate", "first"))
    fil = g.groupby(["mgrno", "q"], as_index=False).agg(fv_all=("fv", "sum"))
    c = cus[cus.cusip.notna() & cus.permno.notna()].copy()
    c["cusip"] = c.cusip.astype(str)
    c["namedt"] = pd.to_datetime(c.namedt)
    c["nameenddt"] = pd.to_datetime(c.nameenddt).fillna(pd.Timestamp("2099-12-31"))
    m = g.merge(c[["cusip", "permno", "namedt", "nameenddt"]], on="cusip", how="inner")
    m = m[(m.rdate >= m.namedt) & (m.rdate <= m.nameenddt)]
    m = m.sort_values(["mgrno", "q", "cusip", "permno"]).drop_duplicates(["mgrno", "q", "cusip"])
    ri, ok = panel.rows(m.permno.to_numpy())
    px = panel.at(panel.P, ri, ok, _qend_mi(m.q.to_numpy()))
    m = m.assign(px=px)
    m = m[np.isfinite(m.px) & (m.px > 0)]
    m = m.assign(val=m.sh * m.px, permno=m.permno.astype("int64"))
    pos = m.groupby(["mgrno", "q", "permno"], as_index=False).agg(val=("val", "sum"), fv=("fv", "sum"))
    used = pos.groupby(["mgrno", "q"], as_index=False).agg(fv_used=("fv", "sum"))
    fil = fil.merge(used, on=["mgrno", "q"], how="left")
    fil["fv_used"] = fil.fv_used.fillna(0.0)
    return pos[["mgrno", "q", "permno", "val"]], fil


def _schedule(f, cut):
    """Holding months of each filing: from the close of the deadline month, three months, buy and hold; six when
    the filer's next filing is exactly two quarters later (one missed quarter bridged); a longer gap or no later
    filing ends the spell after three months. cut: book -> (first, last) record month index."""
    f = f.sort_values(["bk", "q"]).reset_index(drop=True)
    nxt = f.groupby("bk").q.shift(-1)
    f["H"] = np.where((nxt - f.q) == 2, 6, 3).astype("int64")
    em = {q: _entry_mi(q) for q in f.q.unique()}
    f["em"] = f.q.map(em).astype("int64")
    lo = np.full(len(f), MI_FIRST, dtype="int64")
    hi = np.full(len(f), MI_LAST, dtype="int64")
    for bk, (a, b) in cut.items():
        s = (f.bk == bk).to_numpy()
        lo[s], hi[s] = max(a, MI_FIRST), min(b, MI_LAST)
    f["lo_b"], f["hi_b"] = lo, hi
    return f


def _win_span(f, a, b):
    lo = np.maximum.reduce([f.em.to_numpy() + 1, f.lo_b.to_numpy(), np.full(len(f), a)])
    hi = np.minimum.reduce([f.em.to_numpy() + f.H.to_numpy(), f.hi_b.to_numpy(), np.full(len(f), b)])
    return lo, hi


def _hold(pos, em, panel, peers):
    """Buy and hold of one quarter's positions. pos: bk, permno, w (sums to 1 per book), h (months held).
    Returns per book and record month: return, weight share without a return, peer-adjusted return, weight share
    with a peer group."""
    if not len(pos):
        return []
    ri, ok = panel.rows(pos.permno.to_numpy())
    w0, h = pos.w.to_numpy(float), pos.h.to_numpy()
    codes, books = pd.factorize(pos.bk, sort=True)
    cum = np.ones(len(pos))
    res = []
    for k in range(1, int(h.max()) + 1):
        mi = em + k
        if mi > MI_LAST:
            break
        r = panel.at(panel.R, ri, ok, mi)
        miss = ~np.isfinite(r)
        rr = np.where(miss, 0.0, r)
        if mi >= MI_FIRST:
            act = h >= k
            g = peers.group(ri, ok, mi)
            b = peers.bench(g, mi)
            pm = act & ~miss & np.isfinite(b)
            w = w0 * cum
            nb = len(books)
            sw = np.bincount(codes[act], weights=w[act], minlength=nb)
            swr = np.bincount(codes[act], weights=(w * rr)[act], minlength=nb)
            swm = np.bincount(codes[act], weights=(w * miss)[act], minlength=nb)
            swp = np.bincount(codes[pm], weights=w[pm], minlength=nb)
            swd = np.bincount(codes[pm], weights=(w * (rr - np.where(pm, b, 0.0)))[pm], minlength=nb)
            live = np.bincount(codes[act], minlength=nb) > 0
            with np.errstate(invalid="ignore", divide="ignore"):
                res.append(pd.DataFrame({"bk": np.asarray(books)[live], "mi": mi, "ret": (swr / sw)[live],
                                         "miss": (swm / sw)[live],
                                         "pa": np.where(swp > 0, swd / swp, np.nan)[live],
                                         "pash": np.where(sw > 0, swp / sw, np.nan)[live]}))
        cum = cum * (1.0 + rr)
    return res


def _books(pos, fil, panel, peers):
    """All filers (book = mgrno) and library 13F investors (book = -(n+1), union of their filers): filing table
    and monthly record (copy portfolio, peer-adjusted, top-10 and new-positions variants)."""
    P = [pos.rename(columns={"mgrno": "bk"})]
    F = [fil.rename(columns={"mgrno": "bk"})]
    cut, lib = {}, {}
    for n, p in enumerate(INV):
        if p.get("record_kind") != "13f":
            continue
        bk = -(n + 1)
        mg = sorted({int(m) for m in p.get("mgrnos", [])})
        lib[bk] = (p["id"], mg)
        a = int(_mi(int(p["start_ym"]))) if p.get("start_ym") else MI_FIRST
        b = int(_mi(int(p["end_ym"]))) if p.get("end_ym") else MI_LAST
        cut[bk] = (a, b)
        s = pos[pos.mgrno.isin(mg)]
        v = s.groupby(["q", "mgrno"], as_index=False).val.sum().sort_values(["q", "val", "mgrno"],
                                                                           ascending=[True, False, True])
        pick = v.drop_duplicates("q")[["q", "mgrno"]]   # one filer under several mgrno: the larger filing
        P.append(s.merge(pick, on=["q", "mgrno"])[["q", "permno", "val"]].assign(bk=bk))
        t = fil.merge(pick, on=["q", "mgrno"])
        F.append(t[["q", "fv_all", "fv_used"]].assign(bk=bk))
    P = pd.concat(P, ignore_index=True)[["bk", "q", "permno", "val"]]
    P["w"] = P.val / P.groupby(["bk", "q"]).val.transform("sum")
    st = P.groupby(["bk", "q"], as_index=False).agg(npos=("permno", "count"), val=("val", "sum"))
    top = P.sort_values(["bk", "q", "w", "permno"], ascending=[True, True, False, True])
    top["rk"] = top.groupby(["bk", "q"]).cumcount()
    top = top[top.rk < 10]
    st = st.merge(top.groupby(["bk", "q"], as_index=False).agg(top10=("w", "sum")), on=["bk", "q"])
    Fa = pd.concat(F, ignore_index=True).groupby(["bk", "q"], as_index=False)[["fv_all", "fv_used"]].sum()
    st = st.merge(Fa, on=["bk", "q"], how="left")
    with np.errstate(invalid="ignore", divide="ignore"):
        st["fvsh"] = np.where(st.fv_all > 0, st.fv_used / st.fv_all, np.nan)
    # turnover against the previous quarter's filing, and the new positions
    prev = P[["bk", "q", "permno", "w"]].assign(q=P.q + 1)
    has_prev = set(zip(st.bk, st.q + 1))
    st["hasprev"] = [(b, q) in has_prev for b, q in zip(st.bk, st.q)]
    mm = P[["bk", "q", "permno", "w"]].merge(prev, on=["bk", "q", "permno"], how="outer", suffixes=("", "_p"))
    mm = mm.fillna({"w": 0.0, "w_p": 0.0})
    to = mm.assign(d=(mm.w - mm.w_p).abs()).groupby(["bk", "q"], as_index=False).d.sum()
    st = st.merge(to, on=["bk", "q"], how="left")
    st["to"] = np.where(st.hasprev, 0.5 * st.d, np.nan)
    new = P.merge(prev[["bk", "q", "permno"]].assign(old=1), on=["bk", "q", "permno"], how="left")
    new = new[new.old.isna()].merge(st.loc[st.hasprev, ["bk", "q"]], on=["bk", "q"])
    new = new.assign(w=new.val / new.groupby(["bk", "q"]).val.transform("sum"))
    st = _schedule(st, cut)
    H = st.set_index(["bk", "q"]).H
    res, r10, rnew = [], [], []
    for q in sorted(st.q.unique()):
        em = _entry_mi(q)
        if em + 1 > MI_LAST or em + 6 < MI_FIRST:
            continue
        for src, acc in ((P, res), (top, r10), (new, rnew)):
            s = src[src.q == q]
            if not len(s):
                continue
            s = s.assign(h=H.reindex(pd.MultiIndex.from_arrays([s.bk, s.q])).to_numpy())
            if src is top:
                s = s.assign(w=s.w / s.groupby("bk").w.transform("sum"))
            acc.extend(_hold(s, em, panel, peers))
    M = pd.concat(res, ignore_index=True) if res else pd.DataFrame(columns=["bk", "mi", "ret", "miss", "pa", "pash"])
    for acc, col in ((r10, "p10"), (rnew, "pn")):
        if acc:
            x = pd.concat(acc, ignore_index=True)[["bk", "mi", "pa"]].rename(columns={"pa": col})
            M = M.merge(x, on=["bk", "mi"], how="left")
        else:
            M[col] = np.nan
    lim = st.groupby("bk").agg(lo=("lo_b", "first"), hi=("hi_b", "first"))
    M = M.merge(lim, left_on="bk", right_index=True)
    M = M[(M.mi >= M.lo) & (M.mi <= M.hi) & np.isfinite(M.ret)].drop(columns=["lo", "hi"])
    return st, M.sort_values(["bk", "mi"]).reset_index(drop=True), lib


def _book_windows(st, M, ff):
    """Per book and window: statistics, filing medians, rank-group test (13F)."""
    rows = []
    grp = {bk: g for bk, g in M.groupby("bk")}
    for w, a, b in WIN:
        lo, hi = _win_span(st, a, b)
        sub = st[lo <= hi]
        keys = set(zip(sub.bk, sub.q))
        prev_in = np.array([(bk, q - 1) in keys for bk, q in zip(sub.bk, sub.q)], bool)
        fa = sub.groupby("bk").agg(np_=("npos", "median"), val=("val", "median"), tw=("top10", "median"),
                                   fv=("fvsh", "mean"))
        tov = sub[prev_in & np.isfinite(sub.to)].groupby("bk").to.mean() * 4.0
        for bk in fa.index:
            g = grp.get(bk)
            if g is None:
                s = {"n": 0}
            else:
                g = g[(g.mi >= a) & (g.mi <= b)]
                s = _stats(g.mi.to_numpy(), g.ret.to_numpy(float), ff,
                           {"pa": g.pa, "pv": g.pash, "ms": g.miss, "p10": g.p10, "pn": g.pn})
            s.update({"bk": bk, "w": w, "np": fa.at[bk, "np_"], "valm": fa.at[bk, "val"], "tw": fa.at[bk, "tw"],
                      "fv": fa.at[bk, "fv"], "to": tov.get(bk, np.nan)})
            s["grp"] = bool(bk >= 0 and POS_LO <= s["np"] <= POS_HI and s["valm"] >= VAL_MIN
                            and s["n"] >= MIN_RESULT and "a" in s)
            rows.append(s)
    return pd.DataFrame(rows)


# -------------------------------------------------------------------------------------------------- funds
def _flag(s):
    return s.fillna("").astype(str).str.strip().replace({"nan": "", "None": ""}) != ""


def _fund_classes(hdr):
    h = hdr.drop_duplicates("crsp_fundno")       # one header row per share class
    h = h.assign(crsp_fundno=h.crsp_fundno.astype("int64"))
    cl, pt = h.crsp_cl_grp, h.crsp_portno
    gid = np.where(cl.notna(), "G" + cl.fillna(0).astype("int64").astype(str),
                   np.where(pt.notna(), "P" + pt.fillna(0).astype("int64").astype(str),
                            "C" + h.crsp_fundno.astype(str)))
    return h.assign(gid=gid, idx=_flag(h.index_fund_flag))


def _fund_months(fret, sty):
    """Class-months with return, start-of-month assets (previous month-end TNA) and objective code in force."""
    f = fret.copy()
    f["crsp_fundno"] = f.crsp_fundno.astype("int64")
    d = pd.to_datetime(f.caldt)
    f["mi"] = (d.dt.year * 12 + d.dt.month - 1).to_numpy()
    f = f.drop_duplicates(["crsp_fundno", "mi"]).sort_values(["crsp_fundno", "mi"]).reset_index(drop=True)
    pf, pm = f.crsp_fundno.shift(1), f.mi.shift(1)
    f["w"] = np.where((pf == f.crsp_fundno) & (pm == f.mi - 1), f.mtna.shift(1), np.nan)
    f["dt"] = pd.to_datetime(_ym(f.mi).astype(str), format="%Y%m") + pd.offsets.MonthEnd(0)
    s = sty.copy()
    s["crsp_fundno"] = s.crsp_fundno.astype("int64")
    s["begdt"] = pd.to_datetime(s.begdt)
    s["enddt"] = pd.to_datetime(s.enddt).fillna(pd.Timestamp("2099-12-31"))
    s = s.dropna(subset=["begdt"]).sort_values("begdt")
    f = pd.merge_asof(f.sort_values("dt"), s[["crsp_fundno", "begdt", "enddt", "crsp_obj_cd"]],
                      left_on="dt", right_on="begdt", by="crsp_fundno", direction="backward")
    code = np.where(f.enddt >= f.dt, f.crsp_obj_cd.fillna("").astype(str), "")
    f["ed"] = pd.Series(code).str.startswith("ED").to_numpy()
    return f.drop(columns=["begdt", "enddt", "crsp_obj_cd"])


def _combine(f, key):
    """Share classes combined by assets at the start of the month."""
    v = np.isfinite(f.mret) & np.isfinite(f.w) & (f.w > 0)
    x = f[v].assign(wr=f.w[v] * f.mret[v])
    g = x.groupby([key, "mi"], as_index=False).agg(sw=("w", "sum"), swr=("wr", "sum"), ed=("ed", "max"))
    g["ret"] = g.swr / g.sw
    t = f[np.isfinite(f.mtna)].groupby([key, "mi"], as_index=False).agg(tna=("mtna", "sum"))
    g = g.merge(t, on=[key, "mi"], how="left")
    return g[(g.mi >= MI_FIRST) & (g.mi <= MI_LAST)].sort_values([key, "mi"])


def _fund_windows(rec, key, ff, idx_ids, cut=None):
    rows = []
    for k, g in rec.groupby(key):
        if cut:
            a0, b0 = cut[k]
            g = g[(g.mi >= a0) & (g.mi <= b0)]
        for w, a, b in WIN:
            x = g[(g.mi >= a) & (g.mi <= b)]
            s = _stats(x.mi.to_numpy(), x.ret.to_numpy(float), ff)
            s.update({"bk": k, "w": w, "tna": float(x.tna.mean()) if len(x) else np.nan,
                      "ed": bool(len(x) and x.ed.all())})
            s["grp"] = bool(k not in idx_ids and s["ed"] and s["tna"] >= FUND_TNA_MIN and s["n"] >= MIN_RESULT
                            and "a" in s)
            rows.append(s)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------- ranks, tiers
def _share(pool, x, own):
    """Rank share of x in the pool (0 worst .. 1 best, ties average) after taking out the investor's own entries;
    missing unless one of its own entries is in the pool."""
    if x is None or not np.isfinite(x) or not len(pool) or not pool.index.isin(list(own)).any():
        return np.nan
    v = pool[~pool.index.isin(list(own))].to_numpy(float)
    if len(v) == 0:
        return np.nan
    return (np.sum(v < x) + 0.5 * np.sum(v == x)) / float(len(v))


def _member_shares(pool):
    if len(pool) < 2:
        return pd.Series(np.nan, index=pool.index)
    return (pool.rank(method="average") - 1.0) / (len(pool) - 1.0)


def _blockpos(tab):
    """Share of the blocks with a result in which the six-factor alpha is positive."""
    t = tab[tab.w.isin(BLOCKS) & (tab.n >= MIN_RESULT) & tab.a.notna()]
    return t.groupby("bk").a.apply(lambda s: float((s > 0).mean()))


def _pools(tab):
    pool = {w: tab[(tab.w == w) & tab.grp].set_index("bk").a.astype(float) for w, _, _ in WIN}
    ingrp = set(tab[tab.w.isin(BLOCKS) & tab.grp].bk)
    bp = _blockpos(tab)
    bpool = bp[bp.index.isin(ingrp)]
    return pool, bpool


def _spearman(x, y):
    rx, ry = pd.Series(x).rank().to_numpy(), pd.Series(y).rank().to_numpy()
    if len(rx) < 3 or np.std(rx) == 0 or np.std(ry) == 0:
        return np.nan
    return float(np.corrcoef(rx, ry)[0, 1])


def _quint(s):
    r = s.rank(method="average")
    return np.minimum(5, np.floor(5 * (r - 1) / len(s)).astype(int) + 1)


def _persist(tab, b1, b2):
    t1 = tab[(tab.w == b1) & tab.grp].set_index("bk").a
    t2 = tab[(tab.w == b2) & (tab.n >= MIN_RESULT) & tab.a.notna()].set_index("bk").a
    both = t1.index[t1.index.isin(t2.index)]
    out = {"pop": len(t1), "both": len(both), "rho": _spearman(t1[both], t2[both]) if len(both) else np.nan}
    tbl = np.zeros((5, 6), dtype=int)
    if len(t1):
        q1 = _quint(t1)
        q2 = _quint(t2[both]) if len(both) else pd.Series(dtype=float)
        for k in t1.index:
            col = int(q2[k]) - 1 if k in q2.index else 5
            tbl[int(q1[k]) - 1, col] += 1
    out["tbl"] = tbl
    return out


def _tiers(inv):
    """Registration section 7. inv: list of dicts with id, grade, own_docs, months, score, style, explicit_*."""
    def num(x, d):
        return d if x is None or (isinstance(x, float) and not np.isfinite(x)) else x
    elig = [p for p in inv if p["grade"] in ("A", "B", "F") and p["own_docs"] >= 1 and p["months"] >= MIN_STATS]
    sc = sorted([p for p in elig if np.isfinite(p["score"])], key=lambda p: (-p["score"], -p["own_docs"], p["id"]))
    rec, per = [], {}
    for p in sc:
        if len(rec) >= TIER_RECORD:
            break
        if per.get(p["style"], 0) >= STYLE_CAP:
            continue
        rec.append(p["id"])
        per[p["style"]] = per.get(p["style"], 0) + 1
    ex = [p for p in inv if p.get("ran_money") == "yes" and p.get("role", "investor") == "investor"
          and p["id"] not in rec]
    ex = sorted(ex, key=lambda p: (-num(p.get("explicit_max"), -1e9), -num(p.get("explicit_mean"), -1e9),
                                   -p["own_docs"], p["id"]))
    exp = [p["id"] for p in ex[:TIER_EXPLICIT]]
    a = set(rec) | set(exp)
    pool = sorted(p["id"] for p in elig if p["id"] not in a)
    ctrl = sorted(random.Random(SEED).sample(pool, CONTROL_N)) if len(pool) > CONTROL_N else list(pool)
    b = sorted(p["id"] for p in inv if p["id"] not in a and p["id"] not in set(ctrl))
    return {"record": rec, "explicit": exp, "control": ctrl, "B": b, "eligible": len(elig)}


def _foundation():
    d = sorted(DOCS, key=lambda r: (-r[1], -r[2], -r[3], r[0]))
    return [int(r[0]) for r in d[:FOUND_N]]


# --------------------------------------------------------------------------------------------------- build
def _load_years(load, prefix, years, **kw):
    return pd.concat([load("%s_%d" % (prefix, y), **kw) for y in years], ignore_index=True)


def build(load, save, out, data=None):
    t0 = time.time()
    names = ["eq_sc_names", "eq_sc_cusip", "eq_sc_ff", "eq_sc_bm", "eq_sc_fhdr", "eq_sc_fsty", "eq_sc_cand"]
    names += ["eq_sc_msf_%d" % y for y in range(CRSP_FROM // 100, M_LAST // 100 + 1)]
    names += ["eq_sc_hold_%d" % y for y in _hyears()]
    names += ["eq_sc_fret_%d" % y for y in range(M_FIRST // 100 - 1, M_LAST // 100 + 1)]
    save("eq_sc_report", pd.DataFrame({"line": ["build started but not finished: no scorecard"]}))
    if data:
        miss = [n for n in names if not os.path.exists(os.path.join(data, n + ".csv.gz"))]
        if miss:
            out("build: %d input data sets missing (first: %s); run the pulls again" % (len(miss), miss[0]))
            return None
    panel = Panel(stock_returns(_load_years(load, "eq_sc_msf", range(CRSP_FROM // 100, M_LAST // 100 + 1))))
    peers = Peers(panel, _bm_table(load("eq_sc_bm"), panel))
    ff = Factors(load("eq_sc_ff"))
    out("build: CRSP panel %d securities x %d months, peer groups formed (%.0f s)"
        % (len(panel.perm), panel.nm, time.time() - t0))
    pos, fil = _positions(_load_years(load, "eq_sc_hold", _hyears(), dtype={"cusip": str}),
                          load("eq_sc_cusip", dtype={"cusip": str}), panel)
    st, M, lib = _books(pos, fil, panel, peers)
    tab = _book_windows(st, M, ff)
    out("build: %d filers, %d filings, %d book-months (%.0f s)" % (pos.mgrno.nunique(), len(fil), len(M),
                                                                     time.time() - t0))
    # funds
    hdr = _fund_classes(load("eq_sc_fhdr"))
    fm = _fund_months(_load_years(load, "eq_sc_fret", range(M_FIRST // 100 - 1, M_LAST // 100 + 1)),
                      load("eq_sc_fsty"))
    fm = fm.merge(hdr[["crsp_fundno", "gid"]], on="crsp_fundno", how="inner")
    idx_ids = set(hdr[hdr.idx].gid)
    frec = _combine(fm, "gid")
    ftab = _fund_windows(frec, "gid", ff, idx_ids)
    lrec, lcut, lown = [], {}, {}
    for n, p in enumerate(INV):
        if p.get("record_kind") != "fund":
            continue
        fn = sorted({int(x) for x in p.get("fundnos", [])})
        gids = set(hdr[hdr.crsp_fundno.isin(fn)].gid)      # each listed fundno stands for all its share classes
        x = fm[fm.gid.isin(gids)].assign(inv=p["id"])
        lrec.append(x)
        lcut[p["id"]] = (int(_mi(int(p["start_ym"]))) if p.get("start_ym") else MI_FIRST,
                         int(_mi(int(p["end_ym"]))) if p.get("end_ym") else MI_LAST)
        lown[p["id"]] = gids
    ltab = (_fund_windows(_combine(pd.concat(lrec, ignore_index=True), "inv"), "inv", ff, set(), lcut)
            if lrec else pd.DataFrame(columns=["bk", "w", "n"]))
    out("build: %d fund portfolios with returns (%.0f s)" % (frec.gid.nunique(), time.time() - t0))
    res = _results(tab, ftab, ltab, lib, lown, load, hdr, frec)
    res.update({"st": st, "M": M, "tab": tab, "ftab": ftab, "ltab": ltab, "frec": frec, "panel": panel,
                "peers": peers})
    lines = _report_lines(res)
    save("eq_sc_report", pd.DataFrame({"line": lines}))
    out("build: report %d lines, %d characters (%.0f s)" % (len(lines), sum(len(x) + 1 for x in lines),
                                                         time.time() - t0))
    res["lines"] = lines
    return res


def _results(tab, ftab, ltab, lib, lown, load, hdr, frec):
    pools = {"13f": None, "fund": None}
    pools["13f"], bpf = _pools(tab)
    pools["fund"], bpm = _pools(ftab)
    bpools = {"13f": bpf, "fund": bpm}
    libtab = tab[tab.bk < 0]
    bk_of = {v[0]: k for k, v in lib.items()}
    inv = []
    for n, p in enumerate(INV):
        kind = p.get("record_kind")
        d = {"id": p["id"], "name": p.get("name", ""), "grade": p.get("grade"), "kind": kind,
             "style": p.get("primary_style") or "none", "own_docs": int(p.get("own_docs") or 0),
             "explicit_max": p.get("explicit_max"), "explicit_mean": p.get("explicit_mean"),
             "ran_money": p.get("ran_money"), "role": p.get("role", "investor"), "months": 0, "score": np.nan,
             "win": {}}
        if kind == "13f" and p["id"] in bk_of:
            t, own = libtab[libtab.bk == bk_of[p["id"]]], lib[bk_of[p["id"]]][1]
        elif kind == "fund" and len(ltab) and p["id"] in set(ltab.bk):
            t, own = ltab[ltab.bk == p["id"]], lown.get(p["id"], set())
        else:
            inv.append(d)
            continue
        for _, r in t.iterrows():
            w = r["w"]
            s = r.to_dict()
            pool = pools[kind][w]
            s["rk"] = _share(pool, s.get("a"), own) if s.get("n", 0) >= MIN_RESULT else np.nan
            d["win"][w] = s
        d["months"] = int(d["win"].get("2011-25", {}).get("n", 0))
        bt = t[t.w.isin(BLOCKS) & (t.n >= MIN_RESULT) & t.a.notna()] if "a" in t else t.iloc[0:0]
        bpos = float((bt.a > 0).mean()) if len(bt) else np.nan
        d["bshare"] = _share(bpools[kind], bpos, own)
        comp = [d["win"].get("2011-25", {}).get("rk", np.nan), d["win"].get("2021-25", {}).get("rk", np.nan),
                d["bshare"]]
        comp = [c for c in comp if c is not None and np.isfinite(c)]
        d["comp"] = comp
        d["score"] = float(np.mean(comp)) if comp else np.nan
        inv.append(d)
    tiers = _tiers(inv)
    # best-scored filers and funds without a library document
    libm = set(_lib_mgrnos())
    libg = set().union(*lown.values()) if lown else set()

    def best(tb, kind, exclude, n):
        own_t = tb[~tb.bk.isin(list(exclude))]
        if not len(own_t):
            return []
        sh = {w: _member_shares(pools[kind][w]) for w in ("2011-25", "2021-25")}
        bsh = _member_shares(bpools[kind])
        months = own_t[own_t.w == "2011-25"].set_index("bk").n
        out_ = []
        for bk, m in months.items():
            if (kind == "13f" and bk < 0) or m < MIN_STATS:
                continue
            c = [sh["2011-25"].get(bk, np.nan), sh["2021-25"].get(bk, np.nan), bsh.get(bk, np.nan)]
            cf = [x for x in c if np.isfinite(x)]
            if cf:
                out_.append((float(np.mean(cf)), bk, c))
        out_.sort(key=lambda x: (-x[0], str(x[1])))
        return out_[:n]
    nm = load("eq_sc_names")
    nm = nm.assign(mgrno=nm.mgrno.astype("int64"), d=pd.to_datetime(nm.rdate2, errors="coerce").fillna(
        pd.Timestamp("1900-01-01")), mgrname=nm.mgrname.fillna("").astype(str))
    nm = nm.sort_values(["mgrno", "d"]).drop_duplicates("mgrno", keep="last").set_index("mgrno").mgrname
    tf = [(s, nm.get(bk, str(bk)), c) for s, bk, c in best(tab, "13f", libm, TOP_FILERS)]
    fn = hdr.assign(fund_name=hdr.fund_name.fillna("").astype(str))
    fn = fn.sort_values(["gid", "crsp_fundno"]).drop_duplicates("gid").set_index("gid").fund_name
    tm = [(s, fn.get(bk, bk), c) for s, bk, c in best(ftab, "fund", libg, TOP_FUNDS)]
    pers = {kind: [(b1, b2, _persist(tb, b1, b2)) for b1, b2 in (("2011-15", "2016-20"), ("2016-20", "2021-25"))]
            for kind, tb in (("13f", tab[tab.bk >= 0]), ("fund", ftab))}
    cnt = []
    for w, _, _ in WIN:
        g = tab[(tab.w == w) & tab.grp]
        cnt.append((w, len(g), int(((ftab.w == w) & ftab.grp).sum()) if len(ftab) else 0, g.fv.median(),
                    g.pv.mean() if "pv" in g else np.nan, g.ms.mean() if "ms" in g else np.nan))
    return {"inv": inv, "tiers": tiers, "found": _foundation(), "top_filers": tf, "top_funds": tm,
            "persist": pers, "counts": cnt, "pools": pools}


# -------------------------------------------------------------------------------------------------- report
def _f(x, fmt, sign=False):
    if x is None:
        return "."
    try:
        if not np.isfinite(float(x)):
            return "."
    except (TypeError, ValueError):
        return "."
    s = (("%+" + fmt[1:]) if sign else fmt) % float(x)
    return s.replace("0.", ".", 1) if fmt.startswith("%.") and abs(float(x)) < 1 and not sign else s


def _wline(pid, w, s, full):
    head = "  %-6s %-7s n%-3d" % (pid, w, int(s.get("n", 0)))
    if not full:
        return head + " rk %s" % _f(s.get("rk"), "%.3f")
    return head + (" a %s t %s r %s rm %s pa %s pv %s dd %s yb %s np %s tw %s to %s p10 %s pn %s fv %s ms %s rk %s"
                   % (_f(s.get("a"), "%.2f", True), _f(s.get("t"), "%.2f", True), _f(s.get("r"), "%.1f", True),
                      _f(s.get("rm"), "%.1f", True), _f(s.get("pa"), "%.2f", True), _f(s.get("pv"), "%.2f"),
                      _f(s.get("dd"), "%.1f"), _f(s.get("yb"), "%.2f"), _f(s.get("np"), "%.0f"),
                      _f(s.get("tw"), "%.2f"), _f(s.get("to"), "%.2f"), _f(s.get("p10"), "%.2f", True),
                      _f(s.get("pn"), "%.2f", True), _f(s.get("fv"), "%.2f"), _f(s.get("ms"), "%.3f"),
                      _f(s.get("rk"), "%.3f")))


def _report_lines(res):
    L = []
    kinds = [p.get("record_kind") for p in INV]
    L.append("EQ SCORECARD %s | registration STAGE0_REGISTRATION.md s.8 | input sha256 %s" % (VERSION, input_sha()[:16]))
    L.append("investors %d (13f %d, fund %d, none %d) | record months %d-%02d..%d-%02d | seal-exempt run"
             % (len(INV), kinds.count("13f"), kinds.count("fund"), kinds.count("none"), M_FIRST // 100,
                M_FIRST % 100, M_LAST // 100, M_LAST % 100))
    L.append("")
    L.append("COUNTS window | filers in rank group | funds in rank group | filed value used (median) | "
             "value with a peer group (mean) | weight without a return (mean)")
    for w, nf, nm, fv, pv, ms in res["counts"]:
        L.append("  %-7s %6d %6d %s %s %s" % (w, nf, nm, _f(fv, "%.3f"), _f(pv, "%.3f"), _f(ms, "%.4f")))
    L.append("")
    L.append("LIBRARY INVESTORS (matched). Columns: n months | a six-factor alpha %/yr | t | r return %/yr (geometric) "
             "| rm minus CRSP VW market | pa peer-adjusted %/yr | pv value share with a peer group | dd worst fall % "
             "| yb share of calendar years ahead of the market | np median positions | tw median weight of ten "
             "largest | to turnover/yr | p10, pn peer-adjusted top-10 / new-positions variants | fv filed value used "
             "| ms weight share without a return | rk rank share. Statistics only where the window or the record "
             "has 60 months; '.' = none")
    for d in res["inv"]:
        if d["kind"] not in ("13f", "fund") or not d["win"]:
            continue
        full_rec = d["months"] >= MIN_STATS
        L.append("INV %-6s %-28s | grade %s | %-4s | months %3d | style %s | score %s | components %s"
                 % (d["id"], d["name"][:28], d["grade"], d["kind"], d["months"], d["style"],
                    _f(d["score"], "%.3f"), " ".join(_f(c, "%.3f") for c in d.get("comp", []))))
        for w, _, _ in WIN:
            s = d["win"].get(w)
            if s is None:
                continue
            L.append(_wline(d["id"], w, s, full_rec or s.get("n", 0) >= MIN_STATS))
    nm = {d["id"]: d for d in res["inv"]}
    T = res["tiers"]
    L.append("")
    L.append("TIERS (section 7) | eligible by record %d" % T["eligible"])
    L.append("TIER A by record (%d):" % len(T["record"]))
    for i in T["record"]:
        L.append("  %-6s %-28s %-20s score %s" % (i, nm[i]["name"][:28], nm[i]["style"][:20],
                                                 _f(nm[i]["score"], "%.3f")))
    L.append("TIER A by explicit criteria (%d):" % len(T["explicit"]))
    for i in T["explicit"]:
        L.append("  %-6s %-28s explicit max %s mean %s docs %d" % (i, nm[i]["name"][:28],
                                                                  _f(nm[i]["explicit_max"], "%.0f"),
                                                                  _f(nm[i]["explicit_mean"], "%.2f"),
                                                                  nm[i]["own_docs"]))
    L.append("CONTROL (seed %d, %d): %s" % (SEED, len(T["control"]), " ".join(T["control"])))
    for k in range(0, max(len(T["B"]), 1), 20):
        L.append(("TIER B (%d): " % len(T["B"]) if k == 0 else "  ") + " ".join(T["B"][k:k + 20]))
    for k in range(0, max(len(res["found"]), 1), 25):
        L.append(("FOUNDATION documents (%d): " % len(res["found"]) if k == 0 else "  ")
                 + " ".join(str(x) for x in res["found"][k:k + 25]))
    L.append("")
    L.append("BEST-SCORED FILERS WITHOUT A LIBRARY DOCUMENT (score | rank shares 2011-25, 2021-25, blocks)")
    for n, (s, name, c) in enumerate(res["top_filers"], 1):
        L.append("  %2d %-44s %s | %s" % (n, str(name)[:44], _f(s, "%.3f"), " ".join(_f(x, "%.3f") for x in c)))
    L.append("BEST-SCORED FUNDS WITHOUT A LIBRARY DOCUMENT (score | rank shares 2011-25, 2021-25, blocks)")
    for n, (s, name, c) in enumerate(res["top_funds"], 1):
        L.append("  %2d %-44s %s | %s" % (n, str(name)[:44], _f(s, "%.3f"), " ".join(_f(x, "%.3f") for x in c)))
    L.append("")
    L.append("PERSISTENCE (section 9): rank correlation of the six-factor alpha; rows = first-block fifth (1 worst), "
             "columns = second-block fifth 1..5 and 'stopped filing or under 36 months'")
    for kind, lst in res["persist"].items():
        for b1, b2, p in lst:
            L.append("  %-4s %s -> %s | in rank group %d | with both %d | rho %s" % (kind, b1, b2, p["pop"], p["both"],
                                                                                 _f(p["rho"], "%.3f", True)))
            for i in range(5):
                L.append("     %d: %s" % (i + 1, " ".join("%5d" % v for v in p["tbl"][i])))
    L.append("END OF SCORECARD")
    return L


def report(load, out, part=1, parts=1):
    try:
        lines = load("eq_sc_report", keep_default_na=False).line.astype(str).tolist()
    except (IOError, OSError):
        out("report: not built")
        return
    chunks, cur, size = [], [], 0
    for x in lines:
        if size + len(x) + 1 > CHUNK and cur:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(x)
        size += len(x) + 1
    if cur:
        chunks.append(cur)
    if part > len(chunks):
        out("[report part %d of %d: empty]" % (part, len(chunks)))
        return
    out("[report part %d of %d]" % (part, len(chunks)))
    for x in chunks[part - 1]:
        out(x)
    if part == parts and len(chunks) > parts:
        out("[%d more parts not printed: add report steps]" % (len(chunks) - parts))
