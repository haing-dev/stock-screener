"""eq_rec (runs on WRDS Cloud): record check of roster rule v3 (V04_REGISTRATION.md addendum A12). Seal-exempt job 8
`record_check` (tools/equity/seal_exempt.json; SEAL_LOG.md).

For every 13F filer and quarter-end 2010-12 .. 2025-09 one SQL aggregate: the value-weighted total return (CRSP
msf_v2 mthret, delisting returns included) over the NEXT quarter of all CRSP-matched holdings at that quarter-end, the
same for the 20 largest, the number of holdings and the 13F value. Plus SPY (permno 84398) monthly total return and the
CRSP fund returns of the investors whose registered record is a fund.

Prints per listed investor only: long-record rank share (chained return over the investor's window against every
filer with a full record over the same quarters), recent 5-year return against SPY, calendar-year returns against
SPY, and the rule result. No holding, no stock, no other filer's name or return.

Job names (template steps only):
  eq_rec_pull_v<n>: pull(sql, save, out, DATA, budget=N)   resumable; re-run until ALL PULLS COMPLETE
  eq_rec_v<n>:      report(load, out)
  eq_rec_scan_v<n>: scan(load, out)                          every filer; lists those that pass (A12 item 8)
1.0.0 (2026-11-22): first version.
1.0.1 (2026-11-22, after the v1 output; A12 item 7): the investor's own quarters need >= 1 CRSP holding (not 5); peers unchanged.
1.1.0 (2026-11-23, A12 item 8): scan() over all filers with the 1-point margin; report() unchanged.
"""
import json
import os
import time

import numpy as np
import pandas as pd

# >>> FROZEN INPUT
INV = json.loads("[{\"name\": \"Joel Greenblatt\", \"group\": \"roster\", \"record\": \"fund\", \"fundnos\": [56165, 58470, 59064], \"mgrnos\": []}, {\"name\": \"Joel Greenblatt (13F view, reported only)\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [10969, 12775]}, {\"name\": \"Dev Kantesaria\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [14460]}, {\"name\": \"Chris Hohn\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [11194]}, {\"name\": \"Glenn Greenberg\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [16080]}, {\"name\": \"Val Zlatev\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [7142]}, {\"name\": \"Derek Pilecki\", \"group\": \"roster\", \"record\": \"fund\", \"fundnos\": [6972], \"mgrnos\": []}, {\"name\": \"Derek Pilecki (13F view, reported only)\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [8799]}, {\"name\": \"Bill Nygren and Alex Fitch\", \"group\": \"roster\", \"record\": \"fund\", \"fundnos\": [14612, 14617], \"mgrnos\": []}, {\"name\": \"Bill Nygren and Alex Fitch (13F view, reported only)\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [43485]}, {\"name\": \"Murray Stahl\", \"group\": \"roster\", \"record\": \"fund\", \"fundnos\": [17878], \"mgrnos\": []}, {\"name\": \"Murray Stahl (13F view, reported only)\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [44850, 49373]}, {\"name\": \"Pat Dorsey\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [14201]}, {\"name\": \"Chris Davis\", \"group\": \"roster\", \"record\": \"fund\", \"fundnos\": [7317, 8750, 28357], \"mgrnos\": []}, {\"name\": \"Chris Davis (13F view, reported only)\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [78320]}, {\"name\": \"Joseph Shaposhnik\", \"group\": \"roster\", \"record\": \"fund\", \"fundnos\": [86781], \"mgrnos\": []}, {\"name\": \"Alex Sacerdote\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [11405]}, {\"name\": \"David Einhorn\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [42315]}, {\"name\": \"Stan Druckenmiller\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [13021, 23704]}, {\"name\": \"Todd Kantor\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [13431]}, {\"name\": \"Bob Robotti\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [10247]}, {\"name\": \"Fred Martin\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [23050]}, {\"name\": \"Brad Gerstner\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [13112]}, {\"name\": \"Chris Bloomstran\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [11757]}, {\"name\": \"Li Lu\", \"group\": \"roster\", \"record\": \"13f\", \"mgrnos\": [14546]}, {\"name\": \"Terry Smith (removed, reference)\", \"group\": \"removed\", \"record\": \"13f\", \"mgrnos\": [13408]}, {\"name\": \"William Harnisch\", \"group\": \"candidate\", \"record\": \"13f\", \"mgrnos\": [], \"patterns\": [\"PECONIC PARTNERS\"]}, {\"name\": \"Paul Singer\", \"group\": \"candidate\", \"record\": \"13f\", \"mgrnos\": [78988]}, {\"name\": \"Cliff Sosin\", \"group\": \"candidate\", \"record\": \"13f\", \"mgrnos\": [21801]}, {\"name\": \"Nathaniel August\", \"group\": \"candidate\", \"record\": \"13f\", \"mgrnos\": [13534], \"patterns\": []}, {\"name\": \"John Hussman\", \"group\": \"candidate\", \"record\": \"13f\", \"mgrnos\": [], \"patterns\": [\"HUSSMAN\"]}]")
# <<< FROZEN INPUT

VERSION = "eq_rec-1.1.0"
QW = ["%d-%s" % (y, d) for y in range(2010, 2026) for d in ("03-31", "06-30", "09-30", "12-31")][3:-1]  # 2010-12..2025-09
SPY_PERMNO = 84398
MIN_POS, MIN_VAL, MIN_Q = 5, 1e8, 20
RECENT = [q for q in QW if q >= "2020-12-31"]          # weights 2020-12..2025-09 = returns 2021-01..2025-12


def _ym(d):
    return int(d[:4]) * 100 + int(d[5:7])


def _next3(d):
    y, m = int(d[:4]), int(d[5:7])
    return [(y + (m + k - 1) // 12) * 100 + (m + k - 1) % 12 + 1 for k in (1, 2, 3)]


Q_SQL = """/* eqrec q %(d)s */
with h as (
  select mgrno, cusip, sum(shares)::float8 as sh, sum(shares * coalesce(prc, 0))::float8 as v13
  from tfn.s34 where fdate = rdate and rdate = '%(d)s' and shares > 0 group by mgrno, cusip),
tot as (select mgrno, count(*) as nall, sum(v13) as vall from h group by mgrno),
n as (select distinct cusip, permno, namedt, coalesce(nameenddt, date '2099-12-31') as ne
      from crsp.stocknames_v2 where cusip is not null),
k as (select distinct on (h.mgrno, h.cusip) h.mgrno, h.cusip, h.sh, n.permno
      from h join n on n.cusip = h.cusip and date '%(d)s' between n.namedt and n.ne
      order by h.mgrno, h.cusip, n.permno),
p as (select permno, abs(mthprc)::float8 as px from crsp.msf_v2
      where yyyymm = %(ym)d and mthprc is not null and mthprc <> 0),
kv as (select k.mgrno, k.permno, sum(k.sh * p.px) as v from k join p on p.permno = k.permno group by k.mgrno, k.permno),
r as (select mgrno, permno, v, row_number() over (partition by mgrno order by v desc, permno) as rk from kv),
x as (select permno, exp(sum(ln(greatest(1 + mthret, 1e-9)))) - 1 as ret from crsp.msf_v2
      where yyyymm in (%(nx)s) and mthret is not null group by permno)
select r.mgrno, max(tot.nall) as nall, max(tot.vall) as vall, count(*) as ncrsp, sum(r.v) as vcrsp,
  sum(case when x.ret is not null then r.v * x.ret end) / nullif(sum(case when x.ret is not null then r.v end), 0) as mw,
  sum(case when x.ret is not null then r.v end) / nullif(sum(r.v), 0) as cov,
  sum(case when r.rk <= 20 and x.ret is not null then r.v * x.ret end)
    / nullif(sum(case when r.rk <= 20 and x.ret is not null then r.v end), 0) as mw20
from r join tot on tot.mgrno = r.mgrno left join x on x.permno = r.permno
group by r.mgrno"""


def _clean(e):
    s = str(e).split("[SQL")[0].strip().splitlines()
    return "%s: %s" % (type(e).__name__, (s[0] if s else "")[:200])


def pull(sql, save, out, data, budget=7200):
    t0, left = time.time(), 0

    def have(name):
        return bool(data) and os.path.exists(os.path.join(data, name + ".csv.gz"))

    def step(name, fn):
        nonlocal left
        if have(name):
            return
        if time.time() - t0 > budget:
            left += 1
            return
        t1 = time.time()
        try:
            df = fn()
        except Exception as e:  # noqa: BLE001
            raise RuntimeError("%s not pulled: %s" % (name, _clean(e))) from None
        if data:
            save(name + "_part", df)
            os.replace(os.path.join(data, name + "_part.csv.gz"), os.path.join(data, name + ".csv.gz"))
        else:
            save(name, df)
        out("  %-18s %8d rows %6.0f s" % (name, len(df), time.time() - t1))

    out(VERSION + " pull")
    step("eq_rec_names", lambda: sql("/* eqrec names */ select mgrno, mgrname, rdate2 from tfn.s34names"))
    step("eq_rec_spy", lambda: sql("/* eqrec spy */ select yyyymm, mthret from crsp.msf_v2 where permno = %d and "
                                   "yyyymm between 201012 and 202512" % SPY_PERMNO))
    fnos = sorted({int(f) for r in INV for f in r.get("fundnos", [])})
    if fnos:
        step("eq_rec_fund", lambda: sql(
            "/* eqrec fund */ select crsp_fundno, caldt, mtna::float8 as mtna, mret::float8 as mret from "
            "crsp.monthly_tna_ret_nav where caldt between '2010-12-01' and '2025-12-31' and crsp_fundno in (%s)"
            % ",".join(str(f) for f in fnos)))
    for d in QW:
        step("eq_rec_q_%s" % d[:7].replace("-", ""), lambda d=d: sql(Q_SQL % {
            "d": d, "ym": _ym(d), "nx": ",".join(str(x) for x in _next3(d))}))
    out("pull: %s after %.0f s" % (("%d data sets left for the next run" % left) if left else "ALL PULLS COMPLETE",
                                    time.time() - t0))


# ------------------------------------------------------------------------------------------------------ report
def _chain(r):
    r = np.asarray(r, float)
    return float(np.prod(1 + r) - 1) if len(r) and np.all(np.isfinite(r)) else float("nan")


def _ann(c, nq):
    return (1 + c) ** (4.0 / nq) - 1 if np.isfinite(c) and c > -1 and nq else float("nan")


def _p(x):
    return "%.1f" % (100 * x) if x is not None and np.isfinite(x) else "na"


def _year_of(q):
    """weights at quarter-end q earn the next quarter: 2020-12 -> 2021, 2021-03/06/09 -> 2021"""
    y = int(q[:4])
    return y + 1 if q[5:7] == "12" else y


def _spy_q(load):
    s = load("eq_rec_spy")
    s = pd.to_numeric(s.set_index("yyyymm").mthret, errors="coerce")
    return {q: _chain([s.get(m, np.nan) for m in _next3(q)]) for q in QW}


def _fund_q(load, fundnos):
    f = load("eq_rec_fund")
    f = f[f.crsp_fundno.astype(int).isin([int(x) for x in fundnos])].copy()
    f["ym"] = pd.to_datetime(f.caldt).dt.year * 100 + pd.to_datetime(f.caldt).dt.month
    f = f.sort_values(["crsp_fundno", "ym"])
    f["w"] = f.groupby("crsp_fundno").mtna.shift(1)
    f["mret"] = pd.to_numeric(f.mret, errors="coerce")
    f = f.dropna(subset=["mret", "w"])
    m = f.groupby("ym").apply(lambda g: float(np.average(g.mret, weights=g.w)) if g.w.sum() > 0 else float(g.mret.mean()))
    return {q: _chain([m.get(x, np.nan) for x in _next3(q)]) for q in QW}


def report(load, out):
    out("%s  record check, roster rule v3 (V04_REGISTRATION A12)" % VERSION)
    names = load("eq_rec_names")
    names["mgrno"] = names.mgrno.astype("int64")
    q = []
    for d in QW:
        f = load("eq_rec_q_%s" % d[:7].replace("-", ""))
        f["q"] = d
        q.append(f)
    q = pd.concat(q, ignore_index=True)
    q["mgrno"] = q.mgrno.astype("int64")
    mw = q.pivot(index="mgrno", columns="q", values="mw").reindex(columns=QW)
    mw20 = q.pivot(index="mgrno", columns="q", values="mw20").reindex(columns=QW)
    npos = q.pivot(index="mgrno", columns="q", values="ncrsp").reindex(columns=QW)
    vall = q.pivot(index="mgrno", columns="q", values="vall").reindex(columns=QW)
    elig = (npos >= MIN_POS) & (vall >= MIN_VAL) & mw.notna()
    own = (npos >= 1) & (vall >= MIN_VAL) & mw.notna()          # 1.0.1: the investor's own quarters
    spy = _spy_q(load)
    out("filers: %d; eligible (>= %d CRSP holdings, 13F value >= $%.0fm, return) per quarter: median %d"
        % (len(mw), MIN_POS, MIN_VAL / 1e6, int(elig.sum().median())))
    out("SPY total return 2011-25 %s%%/yr; 2021-25 %s%%/yr" % (
        _p(_ann(_chain([spy[x] for x in QW]), len(QW))), _p(_ann(_chain([spy[x] for x in RECENT]), len(RECENT)))))
    out("")
    out("Rule v3: (a) long rank share >= 0.60 over 2011-25 or since the first eligible quarter (>= %d quarters); "
        "(b) 2021-25 annualised above SPY and ahead of SPY in >= 3 of 5 calendar years" % MIN_Q)
    out("columns: investor | group | record (13F filers or fund) | window | quarters | long ann % | SPY same % | "
        "rank share | 2021-25 ann % | SPY % | ahead | years ahead | 2021 2022 2023 2024 2025 minus SPY (points) | "
        "top-20 2021-25 ann % | (a) | (b) | RESULT")
    years = [2021, 2022, 2023, 2024, 2025]
    for r in INV:
        ids = [int(x) for x in r.get("mgrnos", [])]
        for pat in r.get("patterns", []):
            hit = names[names.mgrname.astype(str).str.upper().str.contains(pat, regex=False)].mgrno.unique().tolist()
            ids += [int(h) for h in hit if int(h) not in ids]
        use_fund = r.get("record") == "fund" and r.get("fundnos")
        if use_fund:
            ser = pd.Series(_fund_q(load, r["fundnos"]))
            ok = ser.notna()
            ser20 = pd.Series({x: np.nan for x in QW})
            what = "fund %s" % "/".join(str(x) for x in r["fundnos"])
        else:
            ids = [i for i in ids if i in mw.index]
            if not ids:
                out("%s | %s | no 13F filer found (patterns %s)" % (r["name"], r["group"], r.get("patterns", [])))
                continue
            v = vall.loc[ids].fillna(0)
            num = (mw.loc[ids] * v).sum()
            den = (v * mw.loc[ids].notna()).sum()
            ser = (num / den.replace(0, np.nan)).where(own.loc[ids].any())
            ok = own.loc[ids].any() & ser.notna()
            ser20 = ((mw20.loc[ids] * v).sum() / den.replace(0, np.nan)).where(ok)
            what = "13F " + "/".join(str(i) for i in ids)
        okq = [x for x in QW if bool(ok.get(x, False))]
        if not okq:
            out("%s | %s | %s | no eligible quarter" % (r["name"], r["group"], what))
            continue
        gaps = [x for x in QW if x >= okq[0] and not bool(ok.get(x, False))]
        start = okq[0] if not gaps else next((x for x in QW if x > gaps[-1]), QW[-1])   # last unbroken run
        win = [x for x in QW if x >= start]
        nq = len(win)
        long_c = _chain([ser[x] for x in win]) if all(bool(ok.get(x, False)) for x in win) else float("nan")
        peers = elig[win].all(axis=1)
        pc = (1 + mw.loc[peers, win]).prod(axis=1) - 1
        rank = float((pc < long_c).mean()) if np.isfinite(long_c) and len(pc) else float("nan")
        spy_long = _chain([spy[x] for x in win])
        rec_ok = all(bool(ok.get(x, False)) for x in RECENT)
        rc = _chain([ser[x] for x in RECENT]) if rec_ok else float("nan")
        sr = _chain([spy[x] for x in RECENT])
        diffs, ahead = [], 0
        for y in years:
            qs = [x for x in RECENT if _year_of(x) == y]
            a, b = _chain([ser[x] for x in qs]), _chain([spy[x] for x in qs])
            d = a - b if np.isfinite(a) else float("nan")
            diffs.append(d)
            ahead += int(np.isfinite(d) and d > 0)
        r20 = _chain([ser20[x] for x in RECENT]) if rec_ok else float("nan")
        a_ok = np.isfinite(rank) and rank >= 0.60 and nq >= MIN_Q
        b_ok = np.isfinite(rc) and _ann(rc, 20) > _ann(sr, 20) and ahead >= 3
        flag = "" if nq >= 40 else " (short record)"
        out("%s | %s | %s | %s..2025-12 | %d%s | %s | %s | %s | %s | %s | %s | %d of 5 | %s | %s | %s | %s | %s" % (
            r["name"], r["group"], what, "%d-%02d" % (int(start[:4]) + (1 if start[5:7] == "12" else 0),
                                                      1 if start[5:7] == "12" else int(start[5:7]) + 1),
            nq, flag, _p(_ann(long_c, nq)), _p(_ann(spy_long, nq)), ("%.2f" % rank) if np.isfinite(rank) else "na",
            _p(_ann(rc, 20)), _p(_ann(sr, 20)), _p(_ann(rc, 20) - _ann(sr, 20)) if np.isfinite(rc) else "na", ahead,
            " ".join(_p(d) for d in diffs), _p(_ann(r20, 20)), "yes" if a_ok else "no", "yes" if b_ok else "no",
            "PASS" if (a_ok and b_ok) else "FAIL"))
        if gaps:
            out("    %d quarters missing since the first eligible one (last %s): window starts after the last gap"
                % (len(gaps), gaps[-1][:7]))
    out("ALL DONE")


# ------------------------------------------------------------------------------------------------------ scan (1.1.0)
MARGIN = 0.01                       # A12 item 8: 2021-25 annualised may trail SPY by up to 1 point a year
LIST_MIN_VAL, LIST_POS = 5e8, (5, 200)   # listed: latest 13F value >= $500m and 5..200 CRSP holdings (stock pickers)
MAX_LINES = 300


def scan(load, out):
    out("%s  scan of all 13F filers, roster rule v3 with the 1-point margin (A12 item 8)" % VERSION)
    names = load("eq_rec_names")
    names["mgrno"] = names.mgrno.astype("int64")
    names = names.sort_values("rdate2").drop_duplicates("mgrno", keep="last").set_index("mgrno").mgrname
    q = []
    for d in QW:
        f = load("eq_rec_q_%s" % d[:7].replace("-", ""))
        f["q"] = d
        q.append(f)
    q = pd.concat(q, ignore_index=True)
    q["mgrno"] = q.mgrno.astype("int64")
    mw = q.pivot(index="mgrno", columns="q", values="mw").reindex(columns=QW)
    mw20 = q.pivot(index="mgrno", columns="q", values="mw20").reindex(columns=QW)
    npos = q.pivot(index="mgrno", columns="q", values="ncrsp").reindex(columns=QW)
    vall = q.pivot(index="mgrno", columns="q", values="vall").reindex(columns=QW)
    elig = (npos >= MIN_POS) & (vall >= MIN_VAL) & mw.notna()
    own = (npos >= 1) & (vall >= MIN_VAL) & mw.notna()
    spy = _spy_q(load)
    spy_r = _ann(_chain([spy[x] for x in RECENT]), 20)
    years = [2021, 2022, 2023, 2024, 2025]
    spy_y = {y: _chain([spy[x] for x in RECENT if _year_of(x) == y]) for y in years}
    # last unbroken own run ending 2025-09
    o = own.to_numpy()
    run = np.zeros(len(own), int)
    for i in range(len(own)):
        k = 0
        for j in range(len(QW) - 1, -1, -1):
            if o[i, j]:
                k += 1
            else:
                break
        run[i] = k
    cand = own.index[run >= MIN_Q]
    out("filers with an unbroken own record of >= %d quarters ending 2025-09: %d" % (MIN_Q, len(cand)))
    rows = []
    starts = {}
    for m, k in zip(own.index, run):
        if k >= MIN_Q:
            starts.setdefault(len(QW) - k, []).append(m)
    for s, ms in starts.items():
        win = QW[s:]
        peers = elig[win].all(axis=1)
        pc = np.sort(((1 + mw.loc[peers, win]).prod(axis=1) - 1).to_numpy())
        lc = (1 + mw.loc[ms, win]).prod(axis=1) - 1
        for m in ms:
            c = lc[m]
            rank = float(np.searchsorted(pc, c, side="left")) / len(pc) if len(pc) else np.nan
            rows.append((m, win[0], len(win), _ann(c, len(win)), _ann(_chain([spy[x] for x in win]), len(win)), rank))
    r = pd.DataFrame(rows, columns=["mgrno", "start", "nq", "long", "spy_long", "rank"]).set_index("mgrno")
    rec = (1 + mw.loc[r.index, RECENT]).prod(axis=1) - 1
    r["recent"] = [(_ann(x, 20)) for x in rec]
    r["top20"] = [_ann(x, 20) for x in ((1 + mw20.loc[r.index, RECENT]).prod(axis=1) - 1)]
    for y in years:
        qs = [x for x in RECENT if _year_of(x) == y]
        r["d%d" % y] = ((1 + mw.loc[r.index, qs]).prod(axis=1) - 1) - spy_y[y]
    r["ahead"] = (r[["d%d" % y for y in years]] > 0).sum(axis=1)
    r["a"] = (r["rank"] >= 0.60)
    r["b"] = (r.recent >= spy_r - MARGIN) & (r.ahead >= 3)
    r["val"] = vall.loc[r.index, QW[-1]]
    r["pos"] = npos.loc[r.index, QW[-1]]
    r["name"] = [str(names.get(m, "?")) for m in r.index]
    p = r[r.a & r.b]
    out("pass (a) %d, (b) %d, both %d" % (int(r.a.sum()), int(r.b.sum()), len(p)))
    lst = p[(p.val >= LIST_MIN_VAL) & p.pos.between(*LIST_POS)].copy()
    out("listed (13F value 2025-09 >= $%.0fm, %d-%d CRSP holdings): %d" % (LIST_MIN_VAL / 1e6, LIST_POS[0], LIST_POS[1], len(lst)))
    lst["ex"] = lst.recent - spy_r
    lst = lst.sort_values("ex", ascending=False)
    out("SPY 2021-25 %s%%/yr; margin %.0f point" % (_p(spy_r), 100 * MARGIN))
    out("columns: mgrno | filer name | 13F value 2025-09 $bn | holdings | window | quarters | long ann % | rank | "
        "2021-25 ann % | vs SPY | years ahead | 2021..2025 minus SPY | top-20 2021-25 %")
    for m, x in lst.head(MAX_LINES).iterrows():
        out("%d | %s | %.1f | %d | %s..2025-12 | %d%s | %s | %.2f | %s | %s | %d of 5 | %s | %s" % (
            m, x["name"][:40], x.val / 1e9, int(x.pos), "%d-%02d" % (int(x.start[:4]) + (1 if x.start[5:7] == "12" else 0), 1 if x.start[5:7] == "12" else int(x.start[5:7]) + 1), int(x.nq), "" if x.nq >= 40 else " (short)",
            _p(x.long), x["rank"], _p(x.recent), _p(x.ex), int(x.ahead),
            " ".join(_p(x["d%d" % y]) for y in years), _p(x.top20)))
    if len(lst) > MAX_LINES:
        out("(%d more not printed)" % (len(lst) - MAX_LINES))
    out("ALL DONE")
