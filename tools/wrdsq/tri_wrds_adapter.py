# ===================================================================== WRDS adapter (hand-written)
# Everything above this line is copied unchanged from triage/rules.py, episodes.py, score.py, stats.py and
# qs/btstats.py by tools/wrdsq/build_tri.py. Below: the WRDS data (CRSP CIZ, Compustat, CCM, LSEG 13F, Fama-French)
# turned into the same panel records, returns and 13F rows the live triage uses, then the live detect / evaluate /
# statistics run unchanged.
#
# WRDS policy: data stays on WRDS. The report prints statistics only (counts, medians, means, regressions).
#
# Differences from the live triage (data, not rules):
#   prices      CRSP daily (dsf_v2, CIZ). Entry = CLOSE of the first trading day after the scan (live: its open).
#               Returns compound CRSP daily returns (dividends and delisting returns included); a stock that
#               delists is held as cash after its delisting return.
#   12-month    close vs the highest of the previous 24 scan closes and the change over 24 scans, from CRSP price
#               returns (split-proof).
#   fundamentals Compustat quarterly (TTM, latest balance sheet; known from the earnings date rdq, else quarter end
#               + 90 days) and annual (known from fiscal year end + 120 days). Compustat restates some figures.
#   US filter   CRSP common stock (EQTY/COM/NS) on NYSE, NYSE American or Nasdaq; US-incorporated or US-located
#               (Compustat loc); USD reporting. Industry = CRSP SIC that day (Compustat SIC when missing).
#   13F         LSEG s34: each manager's first vintage per quarter; filing date taken as the 45-day deadline.
#   insiders    no WRDS access (tr_insiders) -> the Insider Buy/Sell cell is N/A (neutral) for every event.
#   volume      average daily dollar volume over the last 6 scan periods (~3 months).
import time as _time

import numpy as _np
import pandas as _pd



def write(kind, items):                    # score.write: nothing to write on WRDS
    return None


PRICE_START, EVENT_START, END = "2006-01-01", "2008-01-01", "2025-12-31"
F13_START = "2007-06-30"
AAPL = 14593
MC_UNIT = 1000.0                           # CRSP shrout is in thousands
EXCH = ("N", "A", "Q")


def _in(sic, ranges):
    return sic is not None and any(a <= sic <= b for a, b in ranges)


def universes(sic, ticker):
    """Same industry rules as qs/screens.u_broad / u_core / u_emerging (ranges copied by build_tri.py)."""
    if sic is None or _in(sic, NEVER_SIC):
        return []
    anyway = ticker in SCREEN_ANYWAY
    u = []
    if not (_in(sic, STRUCT_EXCL) and not _in(sic, STRUCT_KEEP) and not anyway):
        u.append("broad")
    if anyway or not _in(sic, CORE_EXCL):
        u.append("core")
        if not _in(sic, EMERGING_EXTRA):
            u.append("emerging")
    return u


def holder_excluded(name, val, npos):
    if is_match(name, HOLDERS_PASSIVE) or is_match(name, HOLDERS_EXCLUDE):
        return True
    return npos > HOLDERS_MAX_POS or (val > HOLDERS_HUGE_AUM and npos > HOLDERS_HUGE_POS)


def is_match(name, patterns):
    import re
    n = " " + re.sub(r"[^A-Z0-9]+", " ", (name or "").upper()) + " "
    return any(" " + re.sub(r"[^A-Z0-9]+", " ", p.upper()).strip() + " " in n for p in patterns if p.strip())


# --------------------------------------------------------------------------------------------- calendar
def scan_days(days):
    """[(d, e)]: last trading day on or before the 15th and on or before month-end; e = next trading day."""
    days = sorted(_pd.to_datetime(days))
    s = _pd.Series(days)
    out = []
    for p in _pd.period_range(days[0], days[-1], freq="M"):
        for nominal in (_pd.Timestamp(p.year, p.month, 15), p.end_time.normalize()):
            i = s.searchsorted(nominal, side="right") - 1
            if i < 0 or i + 1 >= len(s):
                continue
            d, e = s.iat[i], s.iat[i + 1]
            if out and d <= out[-1][0]:
                continue
            out.append((d, e))
    return out


def _arr(ds):
    return "ARRAY[" + ",".join("'%s'" % x.strftime("%Y-%m-%d") for x in ds) + "]::date[]"


# --------------------------------------------------------------------------------------------- pull (SQL)
YEARS = list(range(int(PRICE_START[:4]), int(END[:4]) + 1))
F13_YEARS = list(range(int(F13_START[:4]), 2027))


def pull(sql, save, out, data=None, part="all", budget=9000):
    """Resumable pulls: each table (CRSP and 13F one per year) is saved as soon as it is read and skipped when it is
    already in ~/wrdsq/data, so a job stopped by the 3-hour limit continues where it left off when it is run again.
    part: 'crsp' | 'comp' | 'f13' | 'all'. Stops starting new tables after `budget` seconds."""
    import os
    t0 = _time.time()
    state = {"left": 0}

    def have(name):
        return bool(data) and os.path.exists(os.path.join(data, name + ".csv.gz"))

    def step(name, fn):
        if have(name):
            return None
        if _time.time() - t0 > budget:
            state["left"] += 1
            return None
        t1 = _time.time()
        df = fn()
        save(name, df)
        out("  %-14s %9d rows  %5.0f s" % (name, len(df), _time.time() - t1))
        return df

    if part in ("crsp", "all"):
        def calendar():
            cal = sql("select distinct dlycaldt as d from crsp.dsf_v2 where permno = %d and dlycaldt between '%s' "
                      "and '%s'" % (AAPL, PRICE_START, END))
            days = sorted(_pd.to_datetime(cal.d))
            assert len(days) > 4000, "trading calendar too short: %d days" % len(days)
            sc_ = scan_days(days)
            return _pd.DataFrame({"d": [d for d, _ in sc_], "e": [e for _, e in sc_]})
        step("tri_cal", calendar)
        step("tri_etf", lambda: sql(
            "select distinct permno, ticker from crsp.stksecurityinfohist where ticker in ('SPY','IWM') "
            "and securitytype = 'FUND' and secinfoenddt >= '%s'" % PRICE_START))
        assert data, "pull needs the data folder (DATA in a wrdsq python step)"
        if not (have("tri_cal") and have("tri_etf")):
            out("pull %s: calendar not read yet; run again" % part)
            return
        cal = _pd.read_csv(os.path.join(data, "tri_cal.csv.gz"), parse_dates=["d", "e"])
        etf = _pd.read_csv(os.path.join(data, "tri_etf.csv.gz"))
        sc = list(zip(cal.d, cal.e))
        etf_ids = ",".join(str(int(p)) for p in etf.permno)
        thr_e = _arr([e + _pd.Timedelta(days=1) for _, e in sc])
        thr_s = _arr([d + _pd.Timedelta(days=1) for d, _ in sc])
        for y in YEARS:
            ds = [d for d, _ in sc if d.year == y]
            if ds:
                step("tri_px_%d" % y, lambda ds=ds, y=y: sql(
                    "select permno, dlycaldt as d, abs(dlyprc)::float8 as prc, shrout::float8 as shrout, siccd, "
                    "usincflg, ticker from crsp.dsf_v2 where dlycaldt between '%d-01-01' and '%d-12-31' and "
                    "dlycaldt = any(%s) and securitytype = 'EQTY' and securitysubtype = 'COM' and sharetype = 'NS' "
                    "and primaryexch in ('N','A','Q') and dlyprc is not null and dlyprc <> 0" % (y, y, _arr(ds))))
            # period pieces: be = entry bucket (close of entry day k-1 .. close of entry day k), bs = scan bucket
            step("tri_bk_%d" % y, lambda y=y: sql(
                "select permno, width_bucket(dlycaldt, %s) as be, width_bucket(dlycaldt, %s) as bs, "
                "sum(case when dlyret is null then 0 else ln(greatest(1 + dlyret, 0.0001)) end)::float8 as lr, "
                "sum(case when coalesce(dlyretx, dlyret) is null then 0 else ln(greatest(1 + coalesce(dlyretx, dlyret), 0.0001)) end)::float8 as lrx, "
                "sum(abs(dlyprc) * coalesce(dlyvol, 0))::float8 as dv, count(*) as nd, "
                "max(case when dlydelflg = 'Y' then 1 else 0 end) as del "
                "from crsp.dsf_v2 where dlycaldt between '%d-01-01' and '%d-12-31' and "
                "((securitytype = 'EQTY' and securitysubtype = 'COM' and sharetype = 'NS') or permno in (%s)) "
                "group by 1, 2, 3" % (thr_e, thr_s, y, y, etf_ids)))
    if part in ("comp", "all"):
        step("tri_link", lambda: sql(
            "select gvkey, lpermno as permno, linkprim, linkdt, linkenddt from crsp.ccmxpf_lnkhist "
            "where linktype in ('LC','LU') and linkprim in ('P','C') and lpermno is not null"))
        step("tri_co", lambda: sql("select gvkey, sic, loc, fic from comp.company"))
        step("tri_fq", lambda: sql(
            "select gvkey, datadate, fyearq, fqtr, rdq, saleq, cogsq, xsgaq, oiadpq, oibdpq, dpq, niq, oancfy, "
            "capxy, cheq, ivltq, dlttq, dlcq, curcdq from comp.fundq where indfmt = 'INDL' and datafmt = 'STD' "
            "and popsrc = 'D' and consol = 'C' and datadate >= '2003-01-01'"))
        step("tri_fa", lambda: sql(
            "select gvkey, datadate, fyear, sale, cogs, xsga, oiadp, oibdp, dp, ni, oancf, capx, stkco, che, ivao, "
            "at, lct, dlc, dltt, ceq, txt, pi, csho, ajex, curcd from comp.funda where indfmt = 'INDL' and "
            "datafmt = 'STD' and popsrc = 'D' and consol = 'C' and datadate >= '1994-01-01'"))
        step("tri_ff", lambda: sql(
            "select date, mktrf, smb, hml, rmw, cma, rf, umd from ff.fivefactors_monthly where date >= '%s'"
            % PRICE_START))
        step("tri_cusip", lambda: sql(
            "select distinct permno, cusip, namedt, nameenddt from crsp.stocknames_v2 where cusip is not null"))
    if part in ("f13", "all"):
        for y in F13_YEARS:
            lo, hi = ("%d-01-01" % y, "%d-12-31" % y) if y > int(F13_START[:4]) else (F13_START, "%d-12-31" % y)
            step("tri_13t_%d" % y, lambda lo=lo, hi=hi: sql(
                "select mgrno, rdate, fdate, sum(shares * prc)::float8 as val, count(distinct cusip) as npos "
                "from tfn.s34 where rdate between '%s' and '%s' and shares > 0 and prc > 0 group by 1, 2, 3"
                % (lo, hi)))
            step("tri_13p_%d" % y, lambda lo=lo, hi=hi: sql(
                "with t as (select mgrno, rdate, fdate, sum(shares * prc) as val, count(distinct cusip) as npos "
                "from tfn.s34 where rdate between '%s' and '%s' and shares > 0 and prc > 0 group by 1, 2, 3) "
                "select s.mgrno, s.rdate, s.fdate, s.cusip, max(s.mgrname) as mgrname, "
                "(sum(s.shares * s.prc) / max(t.val))::float8 as w "
                "from tfn.s34 s join t on s.mgrno = t.mgrno and s.rdate = t.rdate and s.fdate = t.fdate "
                "where s.rdate between '%s' and '%s' and s.shares > 0 and s.prc > 0 and t.val >= %g and t.npos <= %d "
                "group by 1, 2, 3, 4 having sum(s.shares * s.prc) >= %g * max(t.val)"
                % (lo, hi, lo, hi, R.FUND_MIN_AUM, R.FUND_MAX_POSITIONS, R.FUND_MIN_WEIGHT)))
    out("pull %s: %s after %.0f s" % (part, ("%d tables left for the next run" % state["left"]) if state["left"]
                                       else "complete", _time.time() - t0))


def load_years(load, base, years, **kw):
    parts = []
    for y in years:
        try:
            parts.append(load("%s_%d" % (base, y), **kw))
        except FileNotFoundError:
            continue
    return _pd.concat(parts, ignore_index=True)


def load_bk(load):
    bk = load_years(load, "tri_bk", YEARS)
    return bk.groupby(["permno", "be", "bs"], as_index=False).agg(
        lr=("lr", "sum"), lrx=("lrx", "sum"), dv=("dv", "sum"), nd=("nd", "sum"), dl=("del", "max"))


# --------------------------------------------------------------------------------------------- fundamentals
def _cagr(first, last, years):
    if first is None or last is None or years <= 0 or first <= 0 or last <= 0:
        return None
    return (last / first) ** (1.0 / years) - 1


def _num(v):
    return None if v is None or v != v else float(v)


def quarterly(fq):
    """One row per company-quarter with what the panel needs as of that quarter's earnings date."""
    q = fq.sort_values(["gvkey", "datadate"]).drop_duplicates(["gvkey", "datadate"], keep="last").copy()
    q["avail"] = q.rdq.where(q.rdq.notna() & (q.rdq >= q.datadate), q.datadate + _pd.Timedelta(days=90))
    g = q.groupby(["gvkey", "fyearq"])
    for c in ("oancfy", "capxy"):
        prev = g[c].shift(1)
        q[c[:-1] + "q"] = _np.where(q.fqtr == 1, q[c], q[c] - prev)
    q["ebitdaq"] = q.oibdpq.where(q.oibdpq.notna(), q.oiadpq + q.dpq)
    q["fcfq"] = q.oancfq - q.capxq
    gk = q.groupby("gvkey")
    span = (q.datadate - gk.datadate.shift(3)).dt.days
    ok4 = span.between(250, 300)
    for c, nm in (("oiadpq", "ebit"), ("ebitdaq", "ebitda"), ("fcfq", "fcf"), ("saleq", "rev"), ("niq", "ni"),
                  ("cogsq", "cogs4")):
        s = gk[c].rolling(4, min_periods=4).sum().reset_index(level=0, drop=True)
        q[nm] = s.where(ok4)
    q["gprep"] = q.cogsq.notna()
    q["gm"] = _np.where((q.rev > 0) & q.cogs4.notna(), (q.rev - q.cogs4) / q.rev, _np.nan)
    q["ytd"] = q.groupby(["gvkey", "fyearq"]).saleq.cumsum()
    prev = q[["gvkey", "fyearq", "fqtr", "ytd"]].dropna(subset=["fyearq", "fqtr"]).drop_duplicates(["gvkey", "fyearq", "fqtr"]).copy()
    prev["fyearq"] = prev.fyearq + 1
    q = q.merge(prev.rename(columns={"ytd": "ytd0"}), on=["gvkey", "fyearq", "fqtr"], how="left")
    q["ytdg"] = _np.where((q.fqtr < 4) & (q.ytd0 > 0), q.ytd / q.ytd0 - 1, _np.nan)
    has = q[["dlttq", "dlcq", "cheq"]].notna().any(axis=1)
    q["nd"] = (q.dlttq.fillna(0) + q.dlcq.fillna(0) - q.cheq.fillna(0) - q.ivltq.fillna(0)).where(has)
    q["debtok"] = q[["dlttq", "dlcq"]].notna().any(axis=1)
    for c in ("ebit", "ebitda", "fcf", "rev", "ni", "nd"):          # Compustat reports $ millions
        q[c] = q[c] * 1e6
    keep = ["gvkey", "avail", "ebit", "ebitda", "fcf", "rev", "ni", "gm", "gprep", "ytdg", "nd", "debtok", "curcdq"]
    return q[keep].sort_values("avail").reset_index(drop=True)


def _median_nm(vals, n_nm):
    n = len(vals) + n_nm
    if not n or n_nm * 2 >= n:
        return None
    xs = sorted(vals) + [float("inf")] * n_nm
    k = n // 2
    return xs[k] if n % 2 else (xs[k - 1] + xs[k]) / 2


def annual(fa, keep_gvkeys):
    """One row per company-fiscal year: the 10-year metrics as of that annual report (fiscal year end + 120 days)."""
    a = fa[fa.gvkey.isin(keep_gvkeys)].sort_values(["gvkey", "fyear", "datadate"])
    a = a[a.fyear.notna()].drop_duplicates(["gvkey", "fyear"], keep="last")
    rows = []
    cols = ["fyear", "datadate", "sale", "xsga", "oiadp", "oibdp", "dp", "ni", "oancf", "capx", "stkco", "che",
            "ivao", "at", "lct", "dlc", "dltt", "ceq", "txt", "pi", "csho", "ajex", "curcd"]
    for gv, g in a.groupby("gvkey", sort=False):
        recs = g[cols].to_dict("records")
        yr = {}
        ic = {}
        for r in recs:
            r = {k: (_num(v) if k not in ("datadate", "curcd") else v) for k, v in r.items()}
            y = int(r["fyear"])
            rev, op, da = r["sale"], r["oiadp"], r["dp"]
            ebitda = r["oibdp"] if r["oibdp"] is not None else ((op + da) if (op is not None and da is not None) else None)
            ocf, cap = r["oancf"], r["capx"]
            fcf = (ocf - cap) if (ocf is not None and cap is not None) else None
            t = 0.25
            if r["pi"] and r["pi"] > 0 and r["txt"] is not None and r["txt"] >= 0:
                t = min(max(r["txt"] / r["pi"], 0.0), 0.40)
            nopat = op * (1 - t) if op is not None else None
            che, ivao, dlc = r["che"] or 0, r["ivao"] or 0, r["dlc"] or 0
            if r["at"] is not None and r["lct"] is not None:
                ic[y] = r["at"] - che - ivao - (r["lct"] - dlc)
            elif r["ceq"] is not None and r["ceq"] != 0:
                ic[y] = r["ceq"] + (r["dltt"] or 0) + dlc - che
            icav = [x for x in (ic.get(y), ic.get(y - 1)) if x is not None] if ic.get(y) is not None else []
            ic_avg = sum(icav) / len(icav) if icav else None
            roic, neg = None, False
            if nopat is not None and ic_avg is not None:
                light = not (ic_avg > 0.02 * (rev or 0) and ic_avg > 0)
                if not light:
                    roic = max(nopat / ic_avg, -5.0)
                elif nopat > 0:
                    neg = True
            sh = (r["csho"] * r["ajex"]) if (r["csho"] and r["ajex"]) else None
            ratio = (lambda a_, b_: a_ / b_ if (a_ is not None and b_) else None)
            yr[y] = {"rev": rev, "op": op, "da": da, "ebitda": ebitda, "ni": r["ni"], "fcf": fcf, "sbc": r["stkco"],
                     "roic": roic, "neg": neg, "sh": sh, "om": ratio(op, rev), "em": ratio(ebitda, rev),
                     "sga": ratio(r["xsga"], rev)}
            if rev is None or op is None:
                continue
            full = [z for z in sorted(yr) if yr[z]["rev"] is not None and yr[z]["op"] is not None]
            L = y
            W = [z for z in full if L - 10 < z <= L]
            lr = yr[L]
            m = {"gvkey": gv, "fy": L, "fyend": r["datadate"], "acur": r["curcd"], "yrs": len(W), "ytot": len(full),
                 "revfy": rev, "fyebit": op, "fyebitda": ebitda,
                 "das": (abs(da) / ebitda) if (da is not None and ebitda and ebitda > 0) else None,
                 "lossy": sum(1 for z in W if yr[z]["op"] <= 0)}
            roics = [yr[z]["roic"] for z in W if yr[z]["roic"] is not None]
            n_nm = sum(1 for z in W if yr[z]["neg"])
            m["roic"] = _median_nm(roics, n_nm)
            m["roics"] = ((sum(1 for x in roics if x >= 0.10) + n_nm) / (len(roics) + n_nm)) if (roics or n_nm) else None
            span = W[-1] - W[0]
            m["rc"] = _cagr(yr[W[0]]["rev"], rev, span) if span >= 5 else None
            m["rc3"] = _cagr(yr[L - 3]["rev"], rev, 3) if (L - 3) in yr else None
            p1 = yr.get(L - 1)
            m["fyg"] = (rev / p1["rev"] - 1) if (p1 and p1["rev"] and p1["rev"] > 0) else None
            p3 = yr.get(L - 3)
            for k_, src in (("em3", "em"), ("om3", "om"), ("sga3", "sga")):
                m[k_] = (lr[src] - p3[src]) if (p3 and lr[src] is not None and p3[src] is not None) else None
            rts = []
            for z in range(L - 2, L + 1):
                a_, b_ = yr.get(z, {}).get("sh"), yr.get(z - 1, {}).get("sh")
                if a_ and b_:
                    rts.append(a_ / b_)
            m["sh3"] = (float(_np.prod(rts)) ** (1.0 / len(rts)) - 1) if len(rts) >= 3 else None
            pairs = [(yr[z]["fcf"] - abs(yr[z]["sbc"] or 0), yr[z]["ni"]) for z in W
                     if yr[z]["fcf"] is not None and yr[z]["ni"] is not None]
            sni = sum(p[1] for p in pairs)
            m["fcfc"] = (sum(p[0] for p in pairs) / sni) if (len(pairs) >= 5 and sni > 0) else None
            rows.append(m)
    A = _pd.DataFrame(rows)
    for c in ("revfy", "fyebit", "fyebitda"):                       # Compustat reports $ millions
        A[c] = A[c] * 1e6
    A["avail"] = _pd.to_datetime(A.fyend) + _pd.Timedelta(days=120)
    return A.sort_values("avail").reset_index(drop=True)


# --------------------------------------------------------------------------------------------- panel
class Panel:
    def __init__(self, load, out):
        cal = load("tri_cal", parse_dates=["d", "e"])
        self.d = list(cal.d)
        self.e = list(cal.e)
        self.ids = [x.strftime("%Y-%m-%d") for x in self.d]
        n = len(self.d)
        px = load_years(load, "tri_px", YEARS, parse_dates=["d"])
        px = px[px.d.isin(set(self.d))]
        k_of = {d: i for i, d in enumerate(self.d)}
        px["k"] = px.d.map(k_of)
        px["mc"] = px.prc * px.shrout * MC_UNIT
        perms = _np.sort(px.permno.unique())
        self.col = {p: j for j, p in enumerate(perms)}
        bk = load_bk(load)
        self.etf = load("tri_etf")
        # scan buckets: bs = i covers (d[i-1], d[i]] -> price change into scan i; dollar volume over that period
        b = bk[bk.permno.isin(self.col) & (bk.bs >= 1) & (bk.bs <= n - 1)]
        sb = b.groupby(["permno", "bs"], as_index=False).agg(lrx=("lrx", "sum"), dv=("dv", "sum"), nd=("nd", "sum"))
        ci = sb.permno.map(self.col).to_numpy()
        LRX = _np.zeros((n, len(perms)))
        DV = _np.zeros((n, len(perms)))
        ND = _np.zeros((n, len(perms)))
        LRX[sb.bs.to_numpy(), ci] = sb.lrx.to_numpy()
        DV[sb.bs.to_numpy(), ci] = sb.dv.to_numpy()
        ND[sb.bs.to_numpy(), ci] = sb.nd.to_numpy()
        self.L = _np.cumsum(LRX, axis=0)                        # log price index at each scan close
        self.PRES = _np.zeros((n, len(perms)), bool)
        self.PRES[px.k.to_numpy(), px.permno.map(self.col).to_numpy()] = True
        self.DVc, self.NDc = _np.cumsum(DV, axis=0), _np.cumsum(ND, axis=0)
        self.px = {k: g for k, g in px.groupby("k")}
        # links and fundamentals
        link = load("tri_link", parse_dates=["linkdt", "linkenddt"])
        link["linkenddt"] = link.linkenddt.fillna(_pd.Timestamp("2099-12-31"))
        link["gvkey"] = link.gvkey.astype(str).str.zfill(6)
        link["permno"] = link.permno.astype(int)
        link = link[link.permno.isin(self.col)]
        link["pri"] = (link.linkprim == "P").astype(int)
        self.link = link
        co = load("tri_co", dtype={"gvkey": str, "sic": str, "loc": str})
        co["gvkey"] = co.gvkey.str.zfill(6)
        self.co = co.set_index("gvkey")
        fq = load("tri_fq", parse_dates=["datadate", "rdq"], dtype={"gvkey": str})
        fq["gvkey"] = fq.gvkey.str.zfill(6)
        fq = fq[fq.gvkey.isin(set(link.gvkey))]
        self.Q = quarterly(fq)
        fa = load("tri_fa", parse_dates=["datadate"], dtype={"gvkey": str})
        fa["gvkey"] = fa.gvkey.str.zfill(6)
        t0 = _time.time()
        self.A = annual(fa, set(link.gvkey))
        out("panel inputs: %d scans, %d stocks, %d company-quarters, %d company-years (%.0f s)"
            % (n, len(perms), len(self.Q), len(self.A), _time.time() - t0))
        self.sizes, self.mcs = [], []

    def load(self, ym):
        k = self.ids.index(ym) if ym in self.ids else None
        if k is None or k not in self.px:
            return None
        d = self.d[k]
        g = self.px[k].copy()
        lk = g[["permno"]].merge(self.link, on="permno")
        lk = lk[(lk.linkdt <= d) & (lk.linkenddt >= d)].sort_values(["permno", "pri"], ascending=[True, False])
        lk = lk.drop_duplicates("permno")
        g = g.merge(lk[["permno", "gvkey"]], on="permno")
        g = g.join(self.co[["sic", "loc"]], on="gvkey")
        g["avail"] = d
        g = g.sort_values("avail")
        g = _pd.merge_asof(g, self.Q, on="avail", by="gvkey", direction="backward")
        g = _pd.merge_asof(g, self.A.drop(columns=["fy"]), on="avail", by="gvkey", direction="backward")
        us = (g.usincflg == "Y") | (g["loc"] == "USA")
        g = g[us & (g.curcdq == "USD") & (g.acur == "USD")]
        cols = g.permno.map(self.col).to_numpy()
        lo = max(0, k - R.PER_YEAR)
        win = _np.where(self.PRES[lo:k][:, cols], self.L[lo:k][:, cols], -_np.inf) if k > lo else None
        Lk = self.L[k, cols]
        if win is not None:
            mx = win.max(axis=0)
            g["dd"] = _np.where(_np.isfinite(mx), _np.exp(Lk - mx) - 1, _np.nan)
        else:
            g["dd"] = _np.nan
        if k >= R.PER_YEAR:
            j = k - R.PER_YEAR
            g["r12"] = _np.where(self.PRES[j, cols], _np.exp(Lk - self.L[j, cols]) - 1, _np.nan)
        else:
            g["r12"] = _np.nan
        j0 = max(0, k - 6)
        dv = self.DVc[k, cols] - self.DVc[j0, cols]
        nd = self.NDc[k, cols] - self.NDc[j0, cols]
        g["adv"] = _np.where(nd > 0, dv / _np.maximum(nd, 1), _np.nan)
        g["ev"] = g.mc + g.nd
        g["ylf"] = (d - _pd.to_datetime(g.fyend)).dt.days / 365.25
        sic = g.siccd.where(g.siccd.fillna(0) > 0, _pd.to_numeric(g.sic, errors="coerce"))
        g["sicn"] = sic
        recs = {}
        fields = ["px", "mc", "ev", "adv", "dd", "r12", "ebit", "ebitda", "fcf", "rev", "ni", "fyebit", "fyebitda",
                  "das", "nd", "yrs", "ytot", "ylf", "rc3", "rc", "ytdg", "fyg", "roic", "roics", "gm", "em3", "om3",
                  "sga3", "sh3", "fcfc", "lossy", "revfy"]
        g = g.rename(columns={"prc": "px"})
        for r in g[fields + ["permno", "ticker", "sicn", "gprep", "debtok"]].to_dict("records"):
            rec = {f: (None if (r[f] is None or r[f] != r[f]) else float(r[f])) for f in fields}
            for f in ("yrs", "ytot", "lossy"):
                if rec[f] is not None:
                    rec[f] = int(rec[f])
            s = r["sicn"]
            s = None if s is None or s != s else int(s)
            tk = r["ticker"] if isinstance(r["ticker"], str) else ""
            rec.update({"tk": tk, "nm": "", "sym": None, "sic": ("%04d" % s) if s is not None else "",
                        "gprep": bool(r["gprep"]) if r["gprep"] == r["gprep"] else False,
                        "debtok": bool(r["debtok"]) if r["debtok"] == r["debtok"] else False,
                        "u": universes(s, tk)})
            recs[str(int(r["permno"]))] = rec
        self.sizes.append(len(recs))
        self.mcs.append(float(g.mc.median()) if len(g) else _np.nan)
        return {"ym": ym, "d": ym, "e": self.e[k].strftime("%Y-%m-%d"), "companies": recs}

    def returns(self, bk):
        """r[scan id] = {permno: [return from this scan's entry close to the next one's, 'ok' | 'exit']} for stocks
        that traded on the entry day; idx[scan id] = {'SPY': r, 'IWM': r}."""
        n = len(self.d)
        on_e = bk[(bk.bs == bk.be + 1)]                     # the piece holding entry day k alone: (d_k, e_k]
        on_e = on_e[on_e.nd > 0][["permno", "be", "dl"]].rename(columns={"dl": "dl_e"})
        per = bk[(bk.be >= 1) & (bk.be <= n - 1)].groupby(["permno", "be"], as_index=False).agg(
            lr=("lr", "sum"), dl=("dl", "max"))
        per["k"] = per.be - 1                               # entry bucket k+1 = (e_k, e_{k+1}] -> period of scan k
        on_e = on_e.assign(k=on_e.be)
        m = on_e[on_e.dl_e == 0][["permno", "k"]].merge(per[["permno", "k", "lr", "dl"]], on=["permno", "k"],
                                                         how="left")
        r = {}
        for k, g in m.groupby("k"):
            if k > n - 2:
                continue
            vals = g.lr.fillna(0).to_numpy()
            r[self.ids[k]] = {str(int(p)): [float(_np.exp(v) - 1), "exit" if dl == 1 else "ok"]
                              for p, v, dl in zip(g.permno, vals, g.dl.fillna(0))}
        for k in range(n - 1):
            r.setdefault(self.ids[k], {})
        idx = {self.ids[k]: {} for k in range(n - 1)}
        for p, t in zip(self.etf.permno, self.etf.ticker):
            e = per[per.permno == p]
            for k, v in zip(e.k, e.lr):
                if 0 <= k <= n - 2:
                    idx[self.ids[k]][t] = float(_np.exp(v) - 1)
        return r, idx


class WReturns(Returns):
    def __init__(self, months, grid_e, r, idx):
        self.months, self.e, self.r, self.idx = months, grid_e, r, idx
        self.mark, self.opens, self.splits, self.divs = {}, {}, {}, {}


def owners_rows(load, out):
    tot = load_years(load, "tri_13t", F13_YEARS, parse_dates=["rdate", "fdate"])
    first = tot.sort_values("fdate").drop_duplicates(["mgrno", "rdate"])
    pos = load_years(load, "tri_13p", F13_YEARS, parse_dates=["rdate", "fdate"])
    pos = pos.merge(first[["mgrno", "rdate", "fdate", "val", "npos"]], on=["mgrno", "rdate", "fdate"])
    cus = load("tri_cusip", parse_dates=["namedt", "nameenddt"])
    cus["nameenddt"] = cus.nameenddt.fillna(_pd.Timestamp("2099-12-31"))
    pos = pos.merge(cus, on="cusip")
    pos = pos[(pos.rdate >= pos.namedt - _pd.Timedelta(days=92)) & (pos.rdate <= pos.nameenddt + _pd.Timedelta(days=92))]
    pos = pos.sort_values("w", ascending=False).drop_duplicates(["mgrno", "rdate", "permno"])
    excl = {}
    rows = []
    for mg, nm, rd, w, p, val, npos in zip(pos.mgrno, pos.mgrname, pos.rdate, pos.w, pos.permno, pos.val, pos.npos):
        key = (mg, nm, val > HOLDERS_HUGE_AUM, npos)
        if key not in excl:
            excl[key] = holder_excluded(nm if isinstance(nm, str) else "", val, npos)
        if excl[key]:
            continue
        per = rd.strftime("%Y-%m-%d")
        fd = (rd + _pd.Timedelta(days=45)).strftime("%Y-%m-%d")
        rows.append([str(int(mg)), nm if isinstance(nm, str) else str(int(mg)), per, fd, str(int(p)), round(float(w), 4)])
    first_day = pos.rdate.min().strftime("%Y-%m-%d") if len(pos) else None
    through = (pos.rdate.max() + _pd.Timedelta(days=45)).strftime("%Y-%m-%d") if len(pos) else None
    out("13F: %d conviction positions (3%%+, $100M+ filers, passive / fund-house / quant names left out: %d manager "
        "names), %s .. %s" % (len(rows), sum(excl.values()), first_day, through))
    return rows, through, first_day


def factors_of(load):
    ff = load("tri_ff", parse_dates=["date"])
    out = {}
    for r in ff.itertuples():
        if any(_pd.isna(getattr(r, c)) for c in ("mktrf", "smb", "hml", "rmw", "cma", "rf", "umd")):
            continue
        out[r.date.strftime("%Y-%m")] = {"Mkt-RF": float(r.mktrf), "SMB": float(r.smb), "HML": float(r.hml),
                                         "RMW": float(r.rmw), "CMA": float(r.cma), "UMD": float(r.umd),
                                         "RF": float(r.rf)}
    return out


# --------------------------------------------------------------------------------------------- run
def run(load, save, out):
    t0 = _time.time()
    pnl = Panel(load, out)
    months = list(pnl.ids)
    e_of = {pnl.ids[k]: pnl.e[k].strftime("%Y-%m-%d") for k in range(len(months))}
    quiet = []
    events = detect(months, load=pnl.load, log=quiet.append)
    out("panel: median %d US companies per scan (min %d, max %d), median market cap $%.0fM; detection %.0f s"
        % (int(_np.median(pnl.sizes)), min(pnl.sizes), max(pnl.sizes), _np.nanmedian(pnl.mcs) / 1e6,
           _time.time() - t0))
    r, idx = pnl.returns(load_bk(load))
    rets = WReturns(months, e_of, r, idx)
    rows, through, first_day = owners_rows(load, out)
    owners = Owners(rows, through, first_day)
    names = owners.names
    allev = []
    for kind in KIND_IDS:
        events[kind] = [ev for ev in events[kind] if ev["d"] >= EVENT_START]
        for ev in events[kind]:
            ev["kind"] = kind
            ev["fund"] = owners.funds(str(ev["cik"]), ev["d"])
            ev["ins"] = {"n": 0, "net": None}                  # no insider data on WRDS: cell set to N/A below
            ev["learn"] = _event_learning(ev, rets)
            if ev["learn"] and ev["fund"]:
                allev.append({"y": ev["learn"]["y"], "end": ev["learn"]["end"], "fund": ev["fund"], "cik": ev["cik"]})
    as_of = top_performers(allev)
    factors = factors_of(load)
    months_d = list(months)
    res, flat = {}, []
    for kind in KIND_IDS:
        items, series = [], {}
        for ev in events[kind]:
            f = ev.get("fund")
            if f:
                tops = as_of(ev["d"][:7] + "-01")
                ev["top"] = [(names.get(fc, fc), tops[fc][0], tops[fc][2], tops[fc][3]) for fc, *_ in f["list"] if fc in tops]
                ev["top_later"] = []
                for fc, nm, _w, fd in f["later"]:
                    t = as_of(fd[:7] + "-01").get(fc)
                    if t:
                        ev["top_later"].append((names.get(fc, nm), t[0], t[2], t[3], fd))
                ev["top_later"].sort(key=lambda t: t[4])
            item, _ = evaluate(kind, ev, through, months_d, rets, R.INDEX[kind][0])
            if item.get("no_entry"):
                continue
            item["factors"]["insider"] = list(NA)
            ci = months_d.index(item["call_date"]) if item["call_date"] in months_d else ev["i"]
            if item["upgraded"]:
                ci = next((j for j, dd in enumerate(months_d) if dd >= item["call_date"]), ev["i"])
            series[item["id"]] = rets.series(ev["cik"], None, ci, None)
            items.append(item)
            flat.append({"kind": kind, "permno": ev["cik"], "scan": ev["d"], "call_date": item["call_date"],
                         "call": {"overdone": "Buy", "close": "Watch", "justified": "Avoid"}.get(item["verdict"], item["verdict"]),
                         "upgraded": bool(item["upgraded"]), "score": item["score"], "ret": item.get("ret"),
                         "ctrl_ret": item.get("ctrl_ret"), "idx_ret": item.get("idx_ret"), "played": item.get("played"),
                         "stopped": item.get("stopped"), "p_own": item.get("p_own"), "p_peer": item.get("p_peer"),
                         **{"c_" + k: c[0] if c[1] != "N/A" else "" for k, c in item["factors"].items()}})
        res[kind] = (items, series, summary(kind, items, series, factors))
    save("tri_events", _pd.DataFrame(flat))
    report(res, out)
    out("\nrun done in %.0f s" % (_time.time() - t0))


# --------------------------------------------------------------------------------------------- report (stats only)
LAB = {"overdone": "Buy", "close": "Watch", "justified": "Avoid", "tbu": "TBU"}


def _calls_lines(out, ct, pre="  "):
    out(pre + "%-6s %6s %8s %8s %9s %8s %6s %6s %7s" % ("call", "n", "median%", "mean%", "similar%", "index%",
                                                         "beat%", "up20%", "down50%"))
    for v in ("overdone", "close", "justified"):
        c = ct.get(v)
        if c:
            out(pre + "%-6s %6d %8s %8s %9s %8s %6s %6s %7s" % (LAB[v], c["n"], c["median"], c["mean"], c["ctrl_mean"],
                                                                 c["idx_mean"], c["beat"], c["up20"], c["down50"]))


def report(res, out):
    for kind, (items, series, summ) in res.items():
        k = R.KINDS[kind]
        out("\n" + "=" * 100 + "\n%s (%s)" % (k["label"], kind))
        byv = {v: sum(1 for x in items if x["verdict"] == v) for v in ("overdone", "close", "justified", "tbu")}
        out("events %d: %s; upgraded Watch->Buy %d; with a full year %d"
            % (len(items), ", ".join("%s %d" % (LAB[v], n) for v, n in byv.items()),
               sum(1 for x in items if x.get("upgraded")), sum(1 for x in items if x.get("played"))))
        yrs = {}
        for x in items:
            yrs.setdefault(x["date"][:4], [0, 0])
            yrs[x["date"][:4]][0] += 1
            yrs[x["date"][:4]][1] += x["verdict"] == "overdone"
        out("events by year (all / Buy): " + "  ".join("%s %d/%d" % (y, a, b) for y, (a, b) in sorted(yrs.items())))
        out("\none-year results by call (each return capped at +500%% in means; similar = 10 most similar stocks; "
            "index = %s):" % R.INDEX[kind][1])
        _calls_lines(out, summ["calls"])
        for lab, lo, hi in (("2008-2012", "2008", "2012-12-31"), ("2013-2018", "2013", "2018-12-31"),
                            ("2019-2024", "2019", "2024-12-31")):
            sub = [x for x in items if lo <= x["call_date"] <= hi]
            out("  -- %s" % lab)
            _calls_lines(out, calls_table(sub), "     ")
        y = summ.get("years") or {}
        out("\n$10,000 split over each year's Buy candidates (own / similar / index; n):")
        out("  " + "  ".join("%s %s/%s/%s (%d)" % (yy, v["own"], v["ctrl"], v["idx"], v["n"]) for yy, v in sorted(y.items())))
        reg = summ.get("regression") or {}
        out("\ncalendar-time portfolios, Fama-French 5 + momentum, Newey-West t (alpha per year, %):")
        for v in ("overdone", "close", "justified", "long_short"):
            g = reg.get(v)
            if not g or g.get("alpha_y") is None:
                continue
            b = g.get("betas") or {}
            out("  %-10s n=%3d alpha %+6.1f%%/yr (t %5.2f) R2 %s | %s" % (
                LAB.get(v, "Buy-Avoid"), g["n"], g["alpha_y"], g["t"], g.get("r2"),
                " ".join("%s %+.2f(%.1f)" % (kk, bb[0], bb[1]) for kk, bb in b.items())))
        out("\nper cell: one-year return minus similar stocks (median / mean %, beat %, n) green | neutral | red:")
        for key, e in (summ.get("evidence") or {}).items():
            cells = []
            for col in ("g", "n", "r"):
                c = e["cols"].get(col)
                cells.append("%s %s/%s %s%% n%d" % (col, c["median"], c["mean"], c["beat"], c["n"]) if c else "%s -" % col)
            out("  %-24s w%-3d %s  (N/A %d)" % (e["label"], e["weight"], " | ".join(cells), e["na"]))
