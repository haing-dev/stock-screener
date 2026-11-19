"""eq_hf (runs on WRDS Cloud): the hedge fund leaderboard of docs/research/equity/HF_LEADERBOARD_REGISTRATION.md,
computed the way hedgefollow.com computes its table, over 5 years (Q1 2021 - Q4 2025). Seal-exempt job (registered
in tools/equity/seal_exempt.json; the opening is logged in SEAL_LOG.md).

Prints only per-filer statistics (name, country, 13F value, holdings count, top-20 weight, chained returns) and, for
the named validation funds, their quarterly top-20 returns (to check against the website). No holding, no stock.

Job names (template steps only):
  eq_hf_pull_v1 (re-run as v1b ... until pull prints ALL PULLS COMPLETE): pull(sql, save, out, DATA, budget=N)
      one SQL aggregate per quarter-end 2020-12 .. 2025-12 (per filer: top 20 by value, value-weighted and equal
      returns of those 20 over the quarter ending there and over the next quarter), names, 13F value at 2026-03,
      SPY quarterly price return.
  eq_hf_v1: report(load, out, PART, PARTS)
"""
import math
import os
import time

import numpy as np
import pandas as pd

QENDS = ["%d-%s" % (y, d) for y in range(2020, 2026) for d in ("03-31", "06-30", "09-30", "12-31")][3:]  # 2020-12..2025-12
LAST13F = "2026-03-31"
SPY_PERMNO = 84398
EUROPE = {"UNITED KINGDOM", "IRELAND", "FRANCE", "GERMANY", "SWITZERLAND", "NETHERLANDS", "SWEDEN", "NORWAY",
          "DENMARK", "FINLAND", "ITALY", "SPAIN", "BELGIUM", "LUXEMBOURG", "AUSTRIA", "PORTUGAL", "GUERNSEY",
          "JERSEY", "ISLE OF MAN", "MONACO", "LIECHTENSTEIN", "ICELAND", "GREECE", "POLAND", "CZECH REPUBLIC",
          "GIBRALTAR", "MALTA", "CYPRUS", "ENGLAND", "SCOTLAND", "CHANNEL ISLANDS", "HUNGARY"}
US = {"UNITED STATES", "USA", "US", "UNITED STATES OF AMERICA"}
MIN_VAL = 1e9
MIN_POS = 5
TOP = 20
VALID = ["TONTINE", "GENDELL", "ATREIDES", "WHALE ROCK", "DUQUESNE", "RENAISSANCE TECH", "SLATE PATH", "SPRUCE HOUSE",
         "CAS INVESTMENT", "FAIRMOUNT FUNDS", "CALIGAN", "GREENOAKS", "HELIKON"]


def _ym(d):
    return int(d[:4]) * 100 + int(d[5:7])


def _months(d, after):
    y, m = int(d[:4]), int(d[5:7])
    out = []
    for k in ((1, 2, 3) if after else (-2, -1, 0)):
        mm = m + k
        yy = y + (mm - 1) // 12
        mm = (mm - 1) % 12 + 1
        out.append(yy * 100 + mm)
    return out


def _qret(months):
    return ("select permno, exp(sum(ln(greatest(1 + coalesce(mthretx, mthret), 1e-9)))) - 1 as ret "
            "from crsp.msf_v2 where yyyymm in (%s) and coalesce(mthretx, mthret) is not null group by permno"
            % ",".join(str(x) for x in months))


Q_SQL = """/* eqhf q %(d)s */
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
cnt as (select mgrno, count(*) as ncrsp, sum(v) as vcrsp from kv group by mgrno),
r as (select mgrno, permno, v, row_number() over (partition by mgrno order by v desc, permno) as rk from kv),
t as (select mgrno, permno, v from r where rk <= %(top)d),
e as (%(qe)s),
x as (%(qx)s)
select t.mgrno, max(tot.nall) as nall, max(tot.vall) as vall, max(cnt.ncrsp) as ncrsp, max(cnt.vcrsp) as vcrsp,
  count(*) as n20, sum(t.v) as v20,
  sum(case when e.ret is not null then t.v * e.ret end) / nullif(sum(case when e.ret is not null then t.v end), 0) as mw_end,
  avg(e.ret) as ew_end, count(e.ret) as n_end,
  sum(case when x.ret is not null then t.v * x.ret end) / nullif(sum(case when x.ret is not null then t.v end), 0) as mw_next,
  avg(x.ret) as ew_next, count(x.ret) as n_next
from t join tot on tot.mgrno = t.mgrno join cnt on cnt.mgrno = t.mgrno
left join e on e.permno = t.permno left join x on x.permno = t.permno
group by t.mgrno"""


def _clean(e):
    s = str(e).split("[SQL")[0].strip().splitlines()
    return "%s: %s" % (type(e).__name__, (s[0] if s else "")[:200])


def pull(sql, save, out, data, budget=7200):
    t0 = time.time()
    left = 0

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

    step("eq_hf_names", lambda: sql("/* eqhf names */ select mgrno, mgrname, country, rdate1, rdate2 from tfn.s34names"))
    step("eq_hf_spy", lambda: sql("/* eqhf spy */ select permno, yyyymm, mthretx, mthret from crsp.msf_v2 "
                                  "where permno = %d and yyyymm between 202010 and 202512" % SPY_PERMNO))
    step("eq_hf_spyname", lambda: sql("/* eqhf spyname */ select distinct ticker from crsp.stocknames_v2 "
                                      "where permno = %d" % SPY_PERMNO))
    step("eq_hf_last", lambda: sql("/* eqhf last */ select mgrno, count(distinct cusip) as nall, "
                                   "sum(shares * coalesce(prc, 0))::float8 as vall from tfn.s34 where fdate = rdate "
                                   "and rdate = '%s' and shares > 0 group by mgrno" % LAST13F))
    for d in QENDS:
        step("eq_hf_q_%s" % d[:7].replace("-", ""), lambda d=d: sql(Q_SQL % {
            "d": d, "ym": _ym(d), "top": TOP, "qe": _qret(_months(d, False)), "qx": _qret(_months(d, True))}))
    out("pull: %s after %.0f s" % (("%d data sets left for the next run" % left) if left else "ALL PULLS COMPLETE",
                                    time.time() - t0))


# ----------------------------------------------------------------------------------------------------- report
def _chain(r):
    r = np.asarray(r, float)
    return float(np.prod(1 + r) - 1) if len(r) and np.all(np.isfinite(r)) else float("nan")


def _ann(c, years):
    return (1 + c) ** (1.0 / years) - 1 if np.isfinite(c) and c > -1 else float("nan")


def _p(x, w=7):
    return ("%*.1f" % (w, 100 * x)) if x is not None and np.isfinite(x) else " " * (w - 2) + "na"


def _region(c):
    c = (c or "").strip().upper()
    if c in US:
        return "US"
    if c in EUROPE:
        return "EU"
    return "other" if c else "blank"


def _table(load):
    names = load("eq_hf_names")
    names["rdate2"] = pd.to_datetime(names.rdate2, errors="coerce")
    names = names.sort_values(["mgrno", "rdate2"]).groupby("mgrno").tail(1).set_index("mgrno")
    q = []
    for d in QENDS:
        f = load("eq_hf_q_%s" % d[:7].replace("-", ""))
        f["q"] = d
        q.append(f)
    q = pd.concat(q, ignore_index=True)
    q["mgrno"] = q.mgrno.astype("int64")
    last = load("eq_hf_last").set_index("mgrno")
    return names, q, last


def _spy(load):
    s = load("eq_hf_spy")
    s["r"] = pd.to_numeric(s.mthretx, errors="coerce").fillna(pd.to_numeric(s.mthret, errors="coerce"))
    s = s.set_index("yyyymm").r
    out = {}
    for d in QENDS[1:]:
        out[d] = _chain([s.get(m, np.nan) for m in _months(d, False)])
    return out


def _stats(q):
    """Per filer: HF version (weights at q end, return over the quarter ending at q; q = 2021-03..2025-12) and START
    version (weights at q end, return over the next quarter; q = 2020-12..2025-09)."""
    hf_q, st_q = QENDS[1:], QENDS[:-1]
    piv = {c: q.pivot(index="mgrno", columns="q", values=c) for c in
           ("mw_end", "ew_end", "mw_next", "ew_next", "ncrsp", "vall", "nall", "v20")}
    full = piv["ncrsp"].reindex(columns=QENDS)
    ok = full.notna().all(axis=1) & (full.fillna(0) >= MIN_POS).all(axis=1)
    rows = []
    for m in full.index[ok]:
        hm, he = piv["mw_end"].loc[m, hf_q].to_numpy(float), piv["ew_end"].loc[m, hf_q].to_numpy(float)
        sm, se = piv["mw_next"].loc[m, st_q].to_numpy(float), piv["ew_next"].loc[m, st_q].to_numpy(float)
        rows.append({"mgrno": m, "hf5_mw": _chain(hm), "hf5_ew": _chain(he), "hf3_mw": _chain(hm[-12:]),
                     "hf3_ew": _chain(he[-12:]), "st5_mw": _chain(sm), "st5_ew": _chain(se),
                     "st3_mw": _chain(sm[-12:]), "st3_ew": _chain(se[-12:]), "q4_mw": hm[-1], "q4_st": sm[-1], "val25": piv["vall"].loc[m, QENDS[-1]],
                     "nall25": piv["nall"].loc[m, QENDS[-1]], "top20w": piv["v20"].loc[m, QENDS[-1]] /
                     piv["vall"].loc[m, QENDS[-1]] if piv["vall"].loc[m, QENDS[-1]] else float("nan")})
    return pd.DataFrame(rows), piv, int(ok.sum()), len(full)


def report(load, out, part=1, parts=3):
    names, q, last = _table(load)
    st, piv, nfull, nall = _stats(q)
    st["name"] = st.mgrno.map(names.mgrname).fillna("?").astype(str).str.strip()
    st["country"] = st.mgrno.map(names.country).fillna("").astype(str).str.strip()
    st["region"] = st.country.map(_region)
    st["val26"] = st.mgrno.map(last.vall)
    for c in ("hf5_mw", "hf5_ew", "st5_mw", "st5_ew"):
        st[c + "_a"] = st[c].map(lambda x: _ann(x, 5))
    for c in ("hf3_mw", "hf3_ew", "st3_mw", "st3_ew"):
        st[c + "_a"] = st[c].map(lambda x: _ann(x, 3))
    big = st[st.val25 >= MIN_VAL]
    uni = big[big.region.isin(["US", "EU"])].sort_values("st5_mw_a", ascending=False).reset_index(drop=True)
    uni["rank_st"] = np.arange(1, len(uni) + 1)
    uni["rank_hf"] = uni.hf5_mw_a.rank(ascending=False, method="min").astype(int)
    spy = _spy(load)
    if part == 1:
        out("eq_hf report part 1 of %d: universe, SPY, validation" % parts)
        out("filers with a 13F at all 21 quarter-ends 2020-12..2025-12 and >= %d CRSP holdings each: %d of %d"
            % (MIN_POS, nfull, nall))
        out("  of those with 13F value >= $1bn at 2025-12: %d; by region %s" % (
            len(big), ", ".join("%s %d" % (k, v) for k, v in big.region.value_counts().items())))
        out("  regions blank or other among >= $1bn (left out): top 15 by 5y HF MW:")
        rest = big[~big.region.isin(["US", "EU"])].sort_values("hf5_mw_a", ascending=False).head(15)
        for _, r in rest.iterrows():
            out("    %-8d %-34s %-14s %s" % (r.mgrno, r["name"][:34], r.country[:14], _p(r.hf5_mw_a)))
        sp = [spy[d] for d in QENDS[1:]]
        out("SPY (permno %d, tickers %s) price return: 5y %s%% (%s%%/yr), 3y %s%% (%s%%/yr)" % (
            SPY_PERMNO, "/".join(load("eq_hf_spyname").ticker.astype(str)), _p(_chain(sp)), _p(_ann(_chain(sp), 5)),
            _p(_chain(sp[-12:])), _p(_ann(_chain(sp[-12:]), 3))))
        out("SPY quarters 2023-12..2025-12: " + " ".join("%s %s" % (d[:7], _p(spy[d], 6)) for d in QENDS[-9:]))
        out("share of top-20 value with a quarter return (median over filer-quarters of the universe): %s"
            % _p(np.nanmedian((q.n_end / q.n20).to_numpy(float))))
        out("")
        out("VALIDATION: quarterly top-20 returns, % (HF = weights at the quarter end, return over that quarter; "
            "ST = weights at the previous quarter end)")
        hdr = " ".join("%7s" % d[:7] for d in QENDS[-9:])
        for pat in VALID:
            hit = names[names.mgrname.astype(str).str.upper().str.contains(pat, regex=False)]
            if not len(hit):
                out("  %s: no filer name matches" % pat)
                continue
            for m, r in hit.iterrows():
                if m not in piv["mw_end"].index:
                    out("  %-8d %s (%s): no 13F in 2020-12..2025-12" % (m, str(r.mgrname).strip(), r.country))
                    continue
                inu = m in set(uni.mgrno)
                out("  %-8d %s (%s)%s" % (m, str(r.mgrname).strip(), str(r.country).strip(),
                                          "  rank %d" % int(uni.loc[uni.mgrno == m, "rank_st"].iloc[0]) if inu else
                                          "  not in the universe"))
                out("      quarter  " + hdr)
                mw = piv["mw_end"].reindex(columns=QENDS).loc[m]
                ew = piv["ew_end"].reindex(columns=QENDS).loc[m]
                mn = piv["mw_next"].reindex(columns=QENDS).loc[m]
                out("      HF MW    " + " ".join(_p(mw.get(d)) for d in QENDS[-9:]))
                out("      HF EW    " + " ".join(_p(ew.get(d)) for d in QENDS[-9:]))
                prev = {QENDS[i + 1]: mn.get(QENDS[i]) for i in range(len(QENDS) - 1)}
                out("      ST MW    " + " ".join(_p(prev.get(d)) for d in QENDS[-9:]))
                en = piv["ew_next"].reindex(columns=QENDS).loc[m]
                preve = {QENDS[i + 1]: en.get(QENDS[i]) for i in range(len(QENDS) - 1)}
                out("      ST EW    " + " ".join(_p(preve.get(d)) for d in QENDS[-9:]))
        return
    per = int(math.ceil(250.0 / (parts - 1)))
    lo = (part - 2) * per
    sub = uni.iloc[lo:lo + per]
    out("eq_hf report part %d of %d: ranks %d-%d of %d (US + UK/Europe, 13F >= $1bn at 2025-12; ranked on 5y START "
        "MW annualised = weights at the previous quarter end, the website's method; returns %%; value $bn)"
        % (part, parts, lo + 1, lo + len(sub), len(uni)))
    out("rank hfR mgrno    name                              ctry  val25  val26  n25 top20 | 5y MW cum    ann | "
        "5y EW cum    ann | 3y MW cum    ann | 3y EW cum    ann | Q4'25 MW | 5y endW MW ann")
    for _, r in sub.iterrows():
        out("%4d %4d %-8d %-34s %-4s %6.1f %6s %4d %5s | %9s %6s | %9s %6s | %9s %6s | %9s %6s | %8s | %14s" % (
            r.rank_st, r.rank_hf, r.mgrno, r["name"][:34], r.region, r.val25 / 1e9,
            ("%6.1f" % (r.val26 / 1e9)) if np.isfinite(r.val26) else "    na", int(r.nall25), _p(r.top20w, 5),
            _p(r.st5_mw, 9), _p(r.st5_mw_a, 6), _p(r.st5_ew, 9), _p(r.st5_ew_a, 6), _p(r.st3_mw, 9),
            _p(r.st3_mw_a, 6), _p(r.st3_ew, 9), _p(r.st3_ew_a, 6), _p(r.q4_st, 8), _p(r.hf5_mw_a, 14)))
