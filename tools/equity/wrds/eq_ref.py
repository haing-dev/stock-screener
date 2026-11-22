"""eq_ref (runs on WRDS Cloud): reference book v1 and Batch 0 on CRSP / Compustat / I/B/E/S (plan v0.4 step 5;
V04_REGISTRATION.md R3, R4, R7 and addendum A8). Seal-exempt job 6 `reference_book` (tools/equity/seal_exempt.json,
SEAL_LOG.md, TRIAL_LOG.md entry T001 written before the first run).

pull(sql, save, load, out, budget=N)   stores ref_* data sets on WRDS (resumable; each table once)
run(load, save, out)                   builds measures, ranks, the book under R4, benchmarks and the published-form
                                       checks; stores monthly series as ref_series / ref_spreads (they stay on WRDS);
                                       prints counts, coverage and summary statistics only (no company, no row)

The engine (universe, measures, sector ranks, tranche book, costs, statistics) is in this one file: seal-exempt
modules may import no lib module. Local LSEG runs import the same functions.
1.0.0 (2026-11-22): first version.
"""
import json
import math
import time

import numpy as np
import pandas as pd

# >>> FROZEN INPUT
CFG = json.loads("{\"y0\": 2007, \"y1\": 2025, \"form0\": 200901, \"form1\": 202511, \"ret0\": 201001, \"ret1\": 202512, \"top_n\": 1500, \"min_price\": 5.0, \"min_dv\": 2000000.0, \"top_frac\": 0.1, \"keep_frac\": 0.2, \"hold\": 12, \"cost_big\": 0.001, \"cost_small\": 0.0025, \"big_n\": 500, \"basket_cost\": 0.001, \"max_missing\": 3, \"stale_days\": 270, \"q_lag_days\": 45, \"ibes_tol_days\": 35, \"cap\": 0.025}")
# <<< FROZEN INPUT

COM = ("securitytype = 'EQTY' and securitysubtype = 'COM' and sharetype = 'NS' and primaryexch in ('N','A','Q')")
MEASURES = ["ey", "bp", "mom", "roe", "acc", "pio", "rev"]
GROUPS = {"value": ["ey", "bp"], "momentum": ["mom"], "quality": ["roe", "acc", "pio"], "expectations": ["rev"]}
HIGH_GOOD = {"ey": 1, "bp": 1, "mom": 1, "roe": 1, "acc": -1, "pio": 1, "rev": 1}
FF_PAIR = {"ey": "hml", "bp": "hml", "mom": "umd", "roe": "rmw", "acc": "cma", "pio": "rmw", "rev": "umd", "book": "hml"}
VERSION = "eq_ref-1.0.0"


# ----------------------------------------------------------------------------------------------------------- pulls
def pull(sql, save, load, out, budget=9000):
    t0 = time.time()
    y0, y1 = CFG["y0"], CFG["y1"]

    def have(name):
        try:
            load(name)
            return True
        except Exception:
            return False

    def step(name, fn):
        if have(name):
            return
        if time.time() - t0 > budget:
            out("budget reached before %s" % name)
            return
        try:
            df = fn()
            save(name, df)
            out("%-14s rows %9d  cols %2d  %5.0f s" % (name, len(df), df.shape[1], time.time() - t0))
        except Exception as e:  # noqa: BLE001
            out("%-14s FAILED: %s" % (name, str(e)[:200]))

    step("ref_msf", lambda: sql(
        "select permno, permco, yyyymm, mthret::float8 as ret, abs(mthprc)::float8 as prc, shrout::float8 as shrout, "
        "mthcumfacpr::float8 as cfpr, usincflg from crsp.msf_v2 where yyyymm between %d01 and %d12 and %s"
        % (y0, y1, COM)))
    for y in range(y0 + 1, y1 + 1):
        step("ref_dv_%d" % y, lambda y=y: sql(
            "select permno, (extract(year from dlycaldt) * 100 + extract(month from dlycaldt))::int as yyyymm, "
            "percentile_cont(0.5) within group (order by abs(dlyprc) * dlyvol)::float8 as mdv, count(*) as nd "
            "from crsp.dsf_v2 where dlycaldt between '%d-01-01' and '%d-12-31' and %s and dlyprc is not null "
            "and dlyvol is not null group by 1, 2" % (y, y, COM)))
    step("ref_link", lambda: sql(
        "select gvkey, lpermno as permno, linkprim, linkdt, linkenddt from crsp.ccmxpf_lnkhist "
        "where linktype in ('LC','LU') and linkprim in ('P','C') and lpermno is not null"))
    step("ref_fq", lambda: sql(
        "select gvkey, datadate, fyearq, fqtr, rdq, saleq, cogsq, oiadpq, niq, oancfy, atq, ceqq, cheq, dlcq, dlttq, "
        "pstkq, mibq, actq, lctq, cshoq, ajexq from comp.fundq where indfmt = 'INDL' and datafmt = 'STD' and "
        "popsrc = 'D' and consol = 'C' and datadate between '%d-01-01' and '%d-12-31'" % (y0 - 3, y1)))

    def gics():
        try:
            g = sql("select gvkey, indfrom, indthru, gsector, ggroup, gind, gsubind from comp.co_hgic")
            g["src"] = "co_hgic"
            return g
        except Exception as e:  # noqa: BLE001
            out("comp.co_hgic not readable (%s); current GICS from comp.company" % str(e)[:80])
            g = sql("select gvkey, gsector, ggroup, gind, gsubind from comp.company")
            g["indfrom"], g["indthru"], g["src"] = None, None, "company"
            return g
    step("ref_gics", gics)

    def ibes():
        cols = list(sql("select * from ibes.statsum_epsus limit 1").columns)
        cur = "curcode" if "curcode" in cols else None
        q = ("select ticker, cusip, statpers, meanest::float8 as meanest, numest%s from ibes.statsum_epsus where "
             "fpi = '1' and measure = 'EPS' and statpers between '%d-06-01' and '%d-12-31' and meanest is not null"
             % ((", " + cur) if cur else "", y0, y1))
        return sql(q)
    step("ref_ibes", ibes)
    step("ref_names", lambda: sql(
        "select distinct permno, cusip, namedt, coalesce(nameenddt, date '2099-12-31') as nend "
        "from crsp.stocknames_v2 where cusip is not null"))
    step("ref_ff", lambda: sql("select date, mktrf, smb, hml, rmw, cma, rf, umd from ff.fivefactors_monthly "
                               "where date between '%d-01-01' and '%d-12-31'" % (y0, y1)))
    left = [n for n in (["ref_msf", "ref_link", "ref_fq", "ref_gics", "ref_ibes", "ref_names", "ref_ff"]
                        + ["ref_dv_%d" % y for y in range(y0 + 1, y1 + 1)]) if not have(n)]
    out("ALL PULLS COMPLETE" if not left else "left for the next run: %s" % ", ".join(left))


# ------------------------------------------------------------------------------------------------------- helpers
def ym_add(ym, k):
    i = (ym // 100) * 12 + (ym % 100 - 1) + k
    return (i // 12) * 100 + i % 12 + 1


def ym_end(ym):
    return pd.Timestamp(year=ym // 100, month=ym % 100, day=1) + pd.offsets.MonthEnd(0)


def months(a, b):
    r, x = [], a
    while x <= b:
        r.append(x)
        x = ym_add(x, 1)
    return r


def nw_t(x, lags=6):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 12:
        return float("nan")
    e = x - x.mean()
    v = (e @ e) / n
    for k in range(1, lags + 1):
        v += 2 * (1 - k / (lags + 1)) * (e[k:] @ e[:-k]) / n
    return float(x.mean() / math.sqrt(v / n)) if v > 0 else float("nan")


def stats(r):
    r = pd.Series(r, dtype=float).dropna()
    if len(r) == 0:
        return dict(n=0)
    w = (1 + r).cumprod()
    dd = (w / w.cummax() - 1).min()
    return dict(n=len(r), ann=float((1 + r).prod() ** (12 / len(r)) - 1), mean=float(r.mean() * 12),
                vol=float(r.std() * math.sqrt(12)), ir=float(r.mean() / r.std() * math.sqrt(12)) if r.std() > 0 else float("nan"),
                t=nw_t(r), worst_fall=float(dd), worst_month=float(r.min()))


# ---------------------------------------------------------------------------------------------- accounts (Compustat)
def quarterly_table(fq):
    """one row per gvkey-quarter with TTM flows, balances, year-ago values; avail = rdq + 1 day else datadate + 45"""
    f = fq.copy()
    f["datadate"] = pd.to_datetime(f.datadate)
    f["rdq"] = pd.to_datetime(f.rdq)
    for c in ("fyearq", "fqtr"):
        f[c] = pd.to_numeric(f[c], errors="coerce")
    f = f.dropna(subset=["fyearq", "fqtr"]).sort_values(["gvkey", "datadate"])
    f = f.drop_duplicates(["gvkey", "fyearq", "fqtr"], keep="last")
    f["qi"] = (f.fyearq * 4 + f.fqtr).astype(int)
    num = ["saleq", "cogsq", "oiadpq", "niq", "oancfy", "atq", "ceqq", "cheq", "dlcq", "dlttq", "pstkq", "mibq",
           "actq", "lctq", "cshoq", "ajexq"]
    for c in num:
        f[c] = pd.to_numeric(f[c], errors="coerce")
    g = f.groupby("gvkey", sort=False)
    prev_ytd = g.oancfy.shift(1)
    prev_same_year = (g.fyearq.shift(1) == f.fyearq) & (g.qi.shift(1) == f.qi - 1)
    f["cfoq"] = np.where(f.fqtr == 1, f.oancfy, np.where(prev_same_year, f.oancfy - prev_ytd, np.nan))
    f["gpq"] = f.saleq - f.cogsq
    g = f.groupby("gvkey", sort=False)

    def lag(col, k):
        v = g[col].shift(k)
        ok = g.qi.shift(k) == f.qi - k
        return v.where(ok)

    for c in ("saleq", "gpq", "oiadpq", "niq", "cfoq"):
        s = f[c].copy()
        for k in (1, 2, 3):
            s = s + lag(c, k)
        f[c[:-1] + "_ttm"] = s
    for c in ("sale_ttm", "gp_ttm", "ni_ttm", "cfo_ttm"):
        f[c + "_l4"] = lag(c, 4)
    for c in ("atq", "ceqq", "dlttq", "actq", "lctq"):
        f[c + "_l4"] = lag(c, 4)
    f["atq_l8"] = lag("atq", 8)
    f["shares_adj"] = f.cshoq * f.ajexq
    f["shares_adj_l4"] = lag("shares_adj", 4)
    f["avail"] = (f.rdq + pd.Timedelta(days=1)).where(f.rdq.notna(), f.datadate + pd.Timedelta(days=CFG["q_lag_days"]))
    return f


def account_measures(q):
    """measures from one quarter row (vectorised); money in Compustat millions"""
    m = pd.DataFrame(index=q.index)
    avg_ceq = (q.ceqq + q.ceqq_l4) / 2
    avg_at = (q.atq + q.atq_l4) / 2
    m["roe"] = (q.ni_ttm / avg_ceq).where(avg_ceq > 0)
    m["acc"] = ((q.ni_ttm - q.cfo_ttm) / avg_at).where(avg_at > 0)
    roa = (q.ni_ttm / q.atq_l4).where(q.atq_l4 > 0)
    roa_l4 = (q.ni_ttm_l4 / q.atq_l8).where(q.atq_l8 > 0)
    cfo_a = (q.cfo_ttm / q.atq_l4).where(q.atq_l4 > 0)
    avg_at_l4 = (q.atq_l4 + q.atq_l8) / 2
    lev = (q.dlttq / avg_at).where(avg_at > 0)
    lev_l4 = (q.dlttq_l4 / avg_at_l4).where(avg_at_l4 > 0)
    cr = (q.actq / q.lctq).where(q.lctq > 0)
    cr_l4 = (q.actq_l4 / q.lctq_l4).where(q.lctq_l4 > 0)
    gm = (q.gp_ttm / q.sale_ttm).where(q.sale_ttm > 0)
    gm_l4 = (q.gp_ttm_l4 / q.sale_ttm_l4).where(q.sale_ttm_l4 > 0)
    tu = (q.sale_ttm / q.atq_l4).where(q.atq_l4 > 0)
    tu_l4 = (q.sale_ttm_l4 / q.atq_l8).where(q.atq_l8 > 0)

    def sig(cond, *inputs):
        ok = pd.concat(inputs, axis=1).notna().all(axis=1)
        return cond.astype(float).where(ok)

    parts = [sig(roa > 0, roa), sig(q.cfo_ttm > 0, q.cfo_ttm), sig(roa > roa_l4, roa, roa_l4),
             sig(cfo_a > roa, cfo_a, roa), sig(lev < lev_l4, lev, lev_l4), sig(cr > cr_l4, cr, cr_l4),
             sig(q.shares_adj <= q.shares_adj_l4, q.shares_adj, q.shares_adj_l4), sig(gm > gm_l4, gm, gm_l4),
             sig(tu > tu_l4, tu, tu_l4)]
    P = pd.concat(parts, axis=1)
    nok = P.notna().sum(axis=1)
    m["pio"] = (P.sum(axis=1) / nok * 9).where(nok >= 7)
    m["ebit_ttm"] = q.oiadp_ttm
    m["ceq"] = q.ceqq
    m["netdebt"] = q.dlcq.fillna(0) + q.dlttq.fillna(0) + q.pstkq.fillna(0) + q.mibq.fillna(0) - q.cheq.fillna(0)
    m["netdebt_ok"] = q[["dlcq", "dlttq", "cheq"]].notna().any(axis=1)
    return m


# --------------------------------------------------------------------------------------------------------- panel
def build_panel(D, out):
    """monthly panel of universe members with measures, sector and next-month return"""
    msf = D["msf"].copy()
    msf["mcap"] = msf.prc * msf.shrout * 1000.0
    msf = msf[msf.usincflg.astype(str).str.upper() == "Y"]
    msf = msf.sort_values(["permno", "yyyymm"]).drop_duplicates(["permno", "yyyymm"], keep="last")
    msf["mi"] = (msf.yyyymm // 100) * 12 + msf.yyyymm % 100 - 1
    co = msf.groupby(["permco", "yyyymm"]).mcap.sum().rename("mcap_co")
    msf = msf.join(co, on=["permco", "yyyymm"])
    # next-month return and momentum
    g = msf.groupby("permno", sort=False)
    nxt_ok = g.mi.shift(-1) == msf.mi + 1
    msf["ret_next"] = g.ret.shift(-1).where(nxt_ok)
    cnt = pd.Series(0.0, index=msf.index)
    acc = pd.Series(0.0, index=msf.index)
    for k in range(1, 12):
        v = g.ret.shift(k)
        ok = (g.mi.shift(k) == msf.mi - k) & v.notna()
        acc = acc + np.log1p(v.clip(lower=-0.9999)).where(ok, 0.0)
        cnt = cnt + ok.astype(float)
    msf["mom"] = np.expm1(acc).where(cnt >= 9)
    # liquidity: median of the last three monthly medians of daily dollar volume
    dv = D["dv"].copy()
    dv = dv.sort_values(["permno", "yyyymm"])
    dv["mi"] = (dv.yyyymm // 100) * 12 + dv.yyyymm % 100 - 1
    gd = dv.groupby("permno", sort=False)
    a = [dv.mdv] + [gd.mdv.shift(k).where(gd.mi.shift(k) == dv.mi - k) for k in (1, 2)]
    dv["mdv3"] = pd.concat(a, axis=1).median(axis=1, skipna=True)
    msf = msf.merge(dv[["permno", "yyyymm", "mdv3"]], on=["permno", "yyyymm"], how="left")
    # universe: 1,500 largest US common lines; then price and liquidity
    msf["size_rank"] = msf.groupby("yyyymm").mcap.rank(ascending=False, method="first")
    u = msf[(msf.size_rank <= CFG["top_n"]) & (msf.yyyymm >= ym_add(CFG["form0"], -3)) & (msf.yyyymm <= CFG["form1"])].copy()
    u["in_univ"] = (u.prc >= CFG["min_price"]) & (u.mdv3 >= CFG["min_dv"])
    u["t_end"] = [ym_end(x) for x in u.yyyymm]
    # link permno -> gvkey at t
    lk = D["link"].copy()
    lk["linkdt"] = pd.to_datetime(lk.linkdt)
    lk["linkenddt"] = pd.to_datetime(lk.linkenddt).fillna(pd.Timestamp("2099-12-31"))
    lk["pri"] = (lk.linkprim == "P").astype(int)
    x = u[["permno", "yyyymm", "t_end"]].merge(lk, on="permno", how="inner")
    x = x[(x.linkdt <= x.t_end) & (x.t_end <= x.linkenddt)].sort_values(["permno", "yyyymm", "pri"])
    x = x.drop_duplicates(["permno", "yyyymm"], keep="last")[["permno", "yyyymm", "gvkey"]]
    u = u.merge(x, on=["permno", "yyyymm"], how="left")
    # GICS at t
    gi = D["gics"].copy()
    src = str(gi.src.iloc[0]) if len(gi) else "none"
    if src == "co_hgic":
        gi["indfrom"] = pd.to_datetime(gi.indfrom)
        gi["indthru"] = pd.to_datetime(gi.indthru).fillna(pd.Timestamp("2099-12-31"))
        y = u[["permno", "yyyymm", "t_end", "gvkey"]].dropna(subset=["gvkey"]).merge(gi, on="gvkey", how="inner")
        y = y[(y.indfrom <= y.t_end) & (y.t_end <= y.indthru)].drop_duplicates(["permno", "yyyymm"], keep="last")
    else:
        y = u[["permno", "yyyymm", "gvkey"]].dropna(subset=["gvkey"]).merge(gi.drop_duplicates("gvkey"), on="gvkey", how="inner")
    u = u.merge(y[["permno", "yyyymm", "gsector", "ggroup", "gind", "gsubind"]], on=["permno", "yyyymm"], how="left")
    for c in ("gsector", "ggroup", "gind", "gsubind"):
        u[c] = u[c].astype(str).str.replace(r"\.0$", "", regex=True).replace({"nan": np.nan, "None": np.nan})
    excl = (u.ggroup.isin(["4010", "4030", "4040"]) | (u.gsector == "60") | (u.gsubind == "35201010"))
    u["excluded"] = excl
    # accounts known at t
    q = quarterly_table(D["fq"])
    am = account_measures(q)
    q = pd.concat([q[["gvkey", "datadate", "avail"]], am], axis=1).dropna(subset=["avail"]).sort_values("avail")
    left = u[["permno", "yyyymm", "t_end", "gvkey"]].dropna(subset=["gvkey"]).sort_values("t_end")
    left = left.rename(columns={"t_end": "avail_key"})
    q = q.rename(columns={"avail": "avail_key"})
    left["gvkey"] = left.gvkey.astype(str)
    q["gvkey"] = q.gvkey.astype(str)
    j = pd.merge_asof(left, q, on="avail_key", by="gvkey", direction="backward")
    j = j[(j.avail_key - j.datadate).dt.days <= CFG["stale_days"]]
    u = u.merge(j.drop(columns=["avail_key", "gvkey"]), on=["permno", "yyyymm"], how="left")
    ev = u.mcap_co + u.netdebt * 1e6
    u["ey"] = (u.ebit_ttm * 1e6 / ev).where((ev > 0) & u.netdebt_ok.fillna(False).astype(bool))
    u["bp"] = (u.ceq * 1e6 / u.mcap_co).where(u.mcap_co > 0)
    # I/B/E/S revision: (FY1 mean at t - at t-3) / price on the I/B/E/S (current) share basis
    u["rev"] = ibes_revision(D, u, msf, out)
    u["t_end"] = u.t_end.astype("datetime64[ns]")
    out("GICS source: %s; universe months %d..%d" % (src, int(u.yyyymm.min()), int(u.yyyymm.max())))
    return u


def ibes_revision(D, u, msf, out):
    ib = D["ibes"].copy()
    if "curcode" in ib:
        ib = ib[ib.curcode.astype(str).str.upper().isin(["USD", "NONE", "NAN"])]
    ib["statpers"] = pd.to_datetime(ib.statpers)
    nm = D["names"].copy()
    nm["namedt"], nm["nend"] = pd.to_datetime(nm.namedt), pd.to_datetime(nm.nend)
    x = ib.merge(nm, on="cusip", how="inner")
    x = x[(x.statpers >= x.namedt) & (x.statpers <= x.nend)].sort_values(["permno", "statpers"])
    x = x.drop_duplicates(["permno", "statpers"], keep="last")[["permno", "statpers", "meanest"]]
    x = x.sort_values("statpers")

    def at(ends):
        k = pd.DataFrame({"permno": u.permno.values, "key": ends, "row": np.arange(len(u))}).sort_values("key")
        r = pd.merge_asof(k, x.rename(columns={"statpers": "key"}), on="key", by="permno", direction="backward",
                          tolerance=pd.Timedelta(days=CFG["ibes_tol_days"]))
        return r.sort_values("row").meanest.to_numpy()

    e_now = at(pd.to_datetime([ym_end(v) for v in u.yyyymm]).values)
    e_l3 = at(pd.to_datetime([ym_end(ym_add(v, -3)) for v in u.yyyymm]).values)
    # CRSP price factor direction (AAPL 4:1 split, 2020-08): +1 if the cumulative factor grows over time
    a = msf[(msf.permno == 14593) & msf.yyyymm.isin([202007, 202009])].set_index("yyyymm").cfpr
    s = 1.0
    if len(a) == 2 and a.loc[202007] > 0:
        s = 1.0 if a.loc[202009] / a.loc[202007] > 1 else -1.0
        out("CRSP price factor 2020-09 / 2020-07 for AAPL: %.3f -> direction %+d" % (a.loc[202009] / a.loc[202007], s))
    else:
        out("AAPL factor check not available; direction +1 assumed")
    last = msf.sort_values("yyyymm").groupby("permno").cfpr.last()
    cf_last = u.permno.map(last).to_numpy(float)
    cf_t = pd.merge(u[["permno", "yyyymm"]], msf[["permno", "yyyymm", "cfpr"]], on=["permno", "yyyymm"], how="left").cfpr.to_numpy(float)
    padj = u.prc.to_numpy(float) * np.power(cf_t / cf_last, s)
    rev = (e_now - e_l3) / padj
    rev[~np.isfinite(rev) | (padj <= 0)] = np.nan
    return rev


# ------------------------------------------------------------------------------------------------------ ranking
def rank_panel(u):
    """sector percentile ranks (higher = better), group and book scores, inside-sector book percentile"""
    r = u[u.in_univ & ~u.excluded & u.gsector.notna()].copy()
    for m in MEASURES:
        v = r[m] * HIGH_GOOD[m]
        r["rk_" + m] = v.groupby([r.yyyymm, r.gsector]).rank(pct=True)
    miss = r[["rk_" + m for m in MEASURES]].isna().sum(axis=1)
    r["n_missing"] = miss
    for m in MEASURES:
        r["rk_" + m] = r["rk_" + m].fillna(0.5)
    for gname, ms in GROUPS.items():
        r["g_" + gname] = r[["rk_" + m for m in ms]].mean(axis=1)
    r["score"] = r[["g_" + gn for gn in GROUPS]].mean(axis=1)
    r = r[r.n_missing <= CFG["max_missing"]].copy()
    r["sec_pct"] = r.groupby(["yyyymm", "gsector"]).score.rank(pct=True)
    r["all_pct"] = r.groupby("yyyymm").score.rank(pct=True)
    r["big"] = r.groupby("yyyymm").mcap.rank(ascending=False, method="first") <= CFG["big_n"]
    return r


# ------------------------------------------------------------------------------------------------------ the book
def simulate(r, ff, costs=True):
    """R4 tranche book on the ranked panel r (one row per permno-month). Returns monthly frame indexed by return
    month: book, sector-matched universe, equal-weight universe, turnover, names, max weight, liquidity breaches."""
    hold, top, keep = CFG["hold"], CFG["top_frac"], 1 - CFG["keep_frac"]
    by_t = {t: d.set_index("permno") for t, d in r.groupby("yyyymm")}
    sec_ret = r.groupby(["yyyymm", "gsector"]).ret_next.mean()
    ew_ret = r.groupby("yyyymm").ret_next.mean()
    rf = {int(d.year * 100 + d.month): float(x) for d, x in zip(pd.to_datetime(ff.date), ff.rf)}
    tranches = []          # list of dict(form=t, pos={permno: value}, bask={sector: value})
    cash = 1.0
    rows = []
    n_form = 0
    for t in months(CFG["form0"], CFG["form1"]):
        cur = by_t.get(t)
        if cur is None:
            continue
        v0 = cash + sum(sum(tr["pos"].values()) + sum(tr["bask"].values()) for tr in tranches)
        traded = 0.0
        cost = 0.0

        def rate(p):
            if not costs:
                return 0.0
            if p in cur.index:
                return CFG["cost_big"] if bool(cur.at[p, "big"]) else CFG["cost_small"]
            return CFG["cost_small"]

        # 1. review: sell holdings no longer in the top two tenths of their sector (or not ranked) into the basket
        for tr in tranches:
            for p in list(tr["pos"]):
                if p in cur.index and cur.at[p, "sec_pct"] >= keep:
                    continue
                val = tr["pos"].pop(p)
                sec = cur.at[p, "gsector"] if p in cur.index else tr["sec"].get(p)
                c = val * (rate(p) + (CFG["basket_cost"] if costs else 0.0))
                cost += c
                traded += 2 * val
                tr["bask"][sec] = tr["bask"].get(sec, 0.0) + val - c
        # 2. maturity
        free = 0.0
        for tr in [x for x in tranches if ym_add(x["form"], hold) <= t]:
            for p, val in tr["pos"].items():
                c = val * rate(p)
                cost += c
                traded += val
                free += val - c
            for sec, val in tr["bask"].items():
                c = val * (CFG["basket_cost"] if costs else 0.0)
                cost += c
                traded += val
                free += val - c
            tranches.remove(tr)
        n_form += 1
        if n_form <= hold:
            free += 1.0 / hold
            cash -= 1.0 / hold
        # 3. new tranche
        sel = cur[cur.all_pct >= 1 - top]
        if len(sel) and free > 0:
            per = free / len(sel)
            agg = {}
            for tr in tranches:
                for p, val in tr["pos"].items():
                    agg[p] = agg.get(p, 0.0) + val
            cap = CFG["cap"] * v0
            pos, secs, bask = {}, {}, {}
            for p in sel.index:
                buy = min(per, max(cap - agg.get(p, 0.0), 0.0))
                sec = sel.at[p, "gsector"]
                if buy < per:                                  # cap: the rest goes to the sector basket
                    c = (per - buy) * (CFG["basket_cost"] if costs else 0.0)
                    cost += c
                    traded += per - buy
                    bask[sec] = bask.get(sec, 0.0) + per - buy - c
                if buy > 0:
                    c = buy * rate(p)
                    cost += c
                    traded += buy
                    pos[p] = buy - c
                    secs[p] = sec
            tranches.append(dict(form=t, pos=pos, bask=bask, sec=secs))
        else:
            cash += free
        # weights at start of month (after trades)
        wsec = {}
        wstock = {}
        for tr in tranches:
            for p, val in tr["pos"].items():
                s_ = tr["sec"].get(p)
                wsec[s_] = wsec.get(s_, 0.0) + val
                wstock[p] = wstock.get(p, 0.0) + val
            for s_, val in tr["bask"].items():
                wsec[s_] = wsec.get(s_, 0.0) + val
        v1 = cash + sum(wsec.values())
        # 4. returns of month t+1
        nt = ym_add(t, 1)
        for tr in tranches:
            for p in list(tr["pos"]):
                rr = cur.at[p, "ret_next"] if p in cur.index else np.nan
                if not np.isfinite(rr):
                    rr = 0.0
                tr["pos"][p] *= 1 + rr
            for s_ in list(tr["bask"]):
                rr = sec_ret.get((t, s_), np.nan)
                tr["bask"][s_] *= 1 + (rr if np.isfinite(rr) else 0.0)
        cash *= 1 + rf.get(nt, 0.0)
        v2 = cash + sum(sum(tr["pos"].values()) + sum(tr["bask"].values()) for tr in tranches)
        invested = sum(wsec.values())
        sm = sum(w * (sec_ret.get((t, s_), 0.0) if np.isfinite(sec_ret.get((t, s_), np.nan)) else 0.0)
                 for s_, w in wsec.items()) / invested if invested > 0 else np.nan
        mx = max(wstock.values()) / v1 if wstock else np.nan
        liq = 0
        if wstock:
            for p, val in wstock.items():
                if p in cur.index and np.isfinite(cur.at[p, "mdv3"]) and val / v1 * 1e7 > 0.05 * cur.at[p, "mdv3"]:
                    liq += 1
        rows.append(dict(ym=nt, book=v2 / v0 - 1, invested=invested / v1 if v1 > 0 else np.nan, secm=sm,
                         ew=ew_ret.get(t, np.nan), turnover=traded / v0, cost=cost / v0,
                         names=len(wstock), maxw=mx, liq=liq))
    return pd.DataFrame(rows).set_index("ym")


def spreads(r):
    """published-form check: top tenth minus bottom tenth inside each sector, equal weight, gross, next month
    (Piotroski: score 8-9 minus score 0-1, as in the 2000 paper)"""
    out = {}
    for m in MEASURES + ["score"]:
        col = "rk_" + m if m != "score" else "sec_pct"
        d = r[[col, "ret_next", "yyyymm", "gsector"]].dropna()
        if m == "pio":                                         # published form: score 8-9 against 0-1
            d = r[["pio", "ret_next", "yyyymm"]].dropna()
            hi = d[d.pio >= 8].groupby("yyyymm").ret_next.mean()
            lo = d[d.pio <= 1].groupby("yyyymm").ret_next.mean()
            out[m] = hi - lo
            continue
        if m != "score":
            d = d[r.loc[d.index, m].notna()]
            d = d.assign(p=d.groupby(["yyyymm", "gsector"])[col].rank(pct=True))
        else:
            d = d.assign(p=d[col])
        hi = d[d.p > 0.9].groupby("yyyymm").ret_next.mean()
        lo = d[d.p <= 0.1].groupby("yyyymm").ret_next.mean()
        out["book" if m == "score" else m] = (hi - lo)
    s = pd.DataFrame(out)
    s.index = [ym_add(t, 1) for t in s.index]
    return s


# ------------------------------------------------------------------------------------------------------------ run
def load_inputs(load):
    D = {"msf": load("ref_msf"), "link": load("ref_link"), "fq": load("ref_fq"), "gics": load("ref_gics"),
         "ibes": load("ref_ibes"), "names": load("ref_names"), "ff": load("ref_ff")}
    parts = []
    for y in range(CFG["y0"] + 1, CFG["y1"] + 1):
        try:
            parts.append(load("ref_dv_%d" % y))
        except Exception:  # noqa: BLE001
            pass
    D["dv"] = pd.concat(parts, ignore_index=True)
    return D


def run(load, save, out):
    t0 = time.time()
    out("%s  config %s" % (VERSION, json.dumps(CFG, sort_keys=True)))
    need = ["ref_msf", "ref_link", "ref_fq", "ref_gics", "ref_ibes", "ref_names", "ref_ff"] + \
        ["ref_dv_%d" % y for y in range(CFG["y0"] + 1, CFG["y1"] + 1)]
    miss = []
    for n in need:
        try:
            load(n)
        except Exception:  # noqa: BLE001
            miss.append(n)
    if miss:
        out("PULLS INCOMPLETE (%s): nothing computed" % ", ".join(miss))
        return
    D = load_inputs(load)
    out("inputs: " + ", ".join("%s %d" % (k, len(v)) for k, v in D.items()))
    u = build_panel(D, out)
    r = rank_panel(u)
    out("panel built %.0f s" % (time.time() - t0))
    # ---------------------------------------------------------------- structure and coverage (Decembers)
    out("\n## 1. Universe and coverage (December of each year)")
    out("year  top1500  in_univ  excluded  no_sector  ranked  " + "  ".join("%5s" % m for m in MEASURES) + "   top10%")
    for y in range(CFG["form0"] // 100, CFG["form1"] // 100 + 1):
        t = y * 100 + 12 if y * 100 + 12 <= CFG["form1"] else CFG["form1"]
        a = u[u.yyyymm == t]
        b = a[a.in_univ]
        rr = r[r.yyyymm == t]
        base = b[~b.excluded & b.gsector.notna()]
        cov = ["%5.0f" % (100 * base[m].notna().mean()) if len(base) else "    -" for m in MEASURES]
        out("%d  %7d  %7d  %8d  %9d  %6d  %s   %6d" % (y, len(a), len(b), int(b.excluded.sum()), int(b.gsector.isna().sum()),
                                                     len(rr), "  ".join(cov), int((rr.all_pct >= 1 - CFG["top_frac"]).sum())))
    out("coverage = %% of non-excluded universe members with the measure (before the sector-median fill)")
    out("rank correlations between measures (mean over months, Spearman inside the month):")
    cm = r.groupby("yyyymm")[["rk_" + m for m in MEASURES]].corr(method="spearman").groupby(level=1).mean()
    cm = cm.loc[["rk_" + m for m in MEASURES], ["rk_" + m for m in MEASURES]]
    out("       " + " ".join("%6s" % m for m in MEASURES))
    for m in MEASURES:
        out("%6s " % m + " ".join("%6.2f" % cm.loc["rk_" + m, "rk_" + k] for k in MEASURES))
    # ---------------------------------------------------------------- published-form checks
    ff = D["ff"].copy()
    ff["ym"] = [int(d.year * 100 + d.month) for d in pd.to_datetime(ff.date)]
    ffi = ff.set_index("ym")
    S = spreads(r)
    S = S[(S.index >= CFG["ret0"]) & (S.index <= CFG["ret1"])]
    save("ref_spreads", S.reset_index().rename(columns={"index": "ym"}))
    out("\n## 2. Published-form checks %d..%d: top minus bottom tenth inside the sector, equal weight, gross" % (CFG["ret0"], CFG["ret1"]))
    out("measure  months  mean%/mo  NW t   sign as published  corr with FF  factor")
    for m in list(S.columns):
        x = S[m].dropna()
        f = FF_PAIR.get(m)
        c = x.corr(ffi.reindex(x.index)[f].astype(float)) if f in ffi else float("nan")
        out("%-7s  %6d  %8.2f  %5.2f  %17s  %12.2f  %s" % (m, len(x), 100 * x.mean(), nw_t(x), "yes" if x.mean() > 0 else "NO", c, f))
    # ---------------------------------------------------------------- the book
    out("\n## 3. Reference book v1, long book under R4 (%d..%d)" % (CFG["ret0"], CFG["ret1"]))
    B = simulate(r, ff, costs=True)
    G = simulate(r, ff, costs=False)
    B["gross"] = G.book
    B = B[(B.index >= CFG["ret0"]) & (B.index <= CFG["ret1"])]
    save("ref_series", B.reset_index())
    rfm = ffi.reindex(B.index).rf.astype(float)
    lines = [("book, net of costs", B.book), ("book, gross", B.gross), ("sector-matched universe", B.secm),
             ("equal-weight universe", B.ew), ("book net - sector-matched", B.book - B.secm),
             ("book gross - sector-matched", B.gross - B.secm), ("book net - equal-weight universe", B.book - B.ew),
             ("book net - cash (excess)", B.book - rfm)]
    out("series                              months   ann.ret  mean/yr   vol/yr    IR    NW t  worst fall  worst month")
    for nm_, s in lines:
        st = stats(s)
        out("%-34s  %6d  %7.2f%%  %6.2f%%  %6.2f%%  %5.2f  %5.2f  %9.1f%%  %10.1f%%" % (
            nm_, st["n"], 100 * st["ann"], 100 * st["mean"], 100 * st["vol"], st["ir"], st["t"], 100 * st["worst_fall"],
            100 * st["worst_month"]))
    out("turnover per year (traded value / book, both sides): %.2f; costs per year: %.2f%%; names held: median %d "
        "(min %d, max %d); share invested: min %.3f; largest stock weight: max %.2f%%; positions above 5%% of median "
        "daily dollar volume at $10m: %d position-months" % (
            B.turnover.mean() * 12, 100 * B.cost.mean() * 12, int(B.names.median()), int(B.names.min()), int(B.names.max()),
            B.invested.min(), 100 * B.maxw.max(), int(B.liq.sum())))
    out("\ncalendar-year returns (%%): year, book net, sector-matched, difference")
    for y in range(CFG["ret0"] // 100, CFG["ret1"] // 100 + 1):
        s = B[(B.index // 100) == y]
        if len(s) == 0:
            continue
        a, b = (1 + s.book).prod() - 1, (1 + s.secm).prod() - 1
        out("%d  %7.1f  %7.1f  %7.1f" % (y, 100 * a, 100 * b, 100 * (a - b)))
    for e0, e1, nm_ in ((201001, 201412, "2010-14"), (201501, 201912, "2015-19"), (202001, 202512, "2020-25")):
        s = (B.book - B.secm)[(B.index >= e0) & (B.index <= e1)]
        st = stats(s)
        out("era %s: book net - sector-matched: mean/yr %.2f%%, NW t %.2f, months %d" % (nm_, 100 * st["mean"], st["t"], st["n"]))
    out("\nseries stored on WRDS: ref_series (book, gross, sector-matched, equal-weight, turnover, costs), ref_spreads")
    out("done %.0f s" % (time.time() - t0))
