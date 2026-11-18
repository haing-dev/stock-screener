#!/usr/bin/env python3
"""Smoke test of the investor scorecard (tools/equity/wrds/eq_scorecard.py), the seal reader and the seal checker,
on INVENTED data only (no WRDS data anywhere). Registration: docs/research/equity/STAGE0_REGISTRATION.md.

    python3 tests/eq_scorecard_smoke.py [--keep DIR]

A generator fabricates small versions of every input table with a planted truth: a filer whose holdings carry a
known positive alpha, a filer that stops filing, a filer with one missed quarter (bridged), one with two missed
quarters (spell ends), a delisted stock with a -90% delisting return, a CUSIP change, an amended filing (ignored),
a fund with two share classes (and a repeated header row), index / small / non-domestic funds that must stay out
of the rank group, and library investors sharing a filer. The real module code runs against fake sql/load/save
helpers (the fake sql recognises each query by its '/* eqsc ... */' tag and applies the same filters to the fake
tables). Then the six planted errors of registration section 11 are patched into copies of the module text; each
must make at least one check fail. --keep DIR keeps the invented frozen file, the generated module, job and report.
Ends with "eq_scorecard smoke: PASS".
"""
import csv
import io
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import types
import contextlib

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "equity"))
sys.path.insert(0, os.path.join(ROOT, "tools", "equity", "wrds"))
import seal_check  # noqa: E402
import eq_reader  # noqa: E402

MODULE = os.path.join(ROOT, "tools", "equity", "wrds", "eq_scorecard.py")
GEN = os.path.join(ROOT, "tools", "equity", "make_scorecard_job.py")
A, D, CHG, ETF, ADR = 10001, 10002, 10004, 10319, 10320


def mi_of(y, m):
    return y * 12 + m - 1


def ym_of(mi):
    return (mi // 12) * 100 + mi % 12 + 1


def mend(mi):
    return pd.Timestamp(mi // 12, mi % 12 + 1, 1) + pd.offsets.MonthEnd(0)


# ============================================================================================= invented world
def make_world(seed=7):
    rng = np.random.default_rng(seed)
    M0, M1 = mi_of(2009, 6), mi_of(2025, 12)
    mis = np.arange(M0, M1 + 1)
    T = len(mis)
    NS = 320
    perms = 10001 + np.arange(NS)
    F = np.column_stack([rng.normal(0.008, 0.045, T), rng.normal(0, 0.03, T), rng.normal(0, 0.03, T),
                         rng.normal(0, 0.02, T), rng.normal(0, 0.02, T), rng.normal(0, 0.04, T)])
    rf = np.full(T, 0.001)
    B = np.column_stack([rng.uniform(0.6, 1.4, NS), rng.normal(0, 0.3, (NS, 5))])
    alpha = np.zeros(NS)
    alpha[0] = 0.03                                         # stock A
    sd = np.full(NS, 0.07)
    sd[0] = 0.01
    R = rf[None, :] + B @ F.T + alpha[:, None] + rng.normal(0, 1, (NS, T)) * sd[:, None]
    R = np.maximum(R, -0.6)
    td = mi_of(2014, 6) - M0
    R[1, td] = -0.9                                         # D: delisting return in its last month
    P = np.empty((NS, T))
    P[:, 0] = rng.uniform(10, 60, NS)
    for t in range(1, T):
        P[:, t] = P[:, t - 1] * (1 + R[:, t])
    shr = rng.uniform(5000, 200000, NS)
    exch = np.where(np.arange(NS) % 5 < 2, "N", np.where(np.arange(NS) % 7 == 0, "A", "Q"))
    rows = []
    for i, p in enumerate(perms):
        for t in range(T):
            if p == D and t > td:
                break
            r = R[i, t]
            if rng.random() < 0.003 and p not in (A, D):
                r = np.nan                                  # a missing return (price kept)
            st, sub, sh = ("FUND", "ETF", "NA") if p == ETF else ("EQTY", "COM", "AD" if p == ADR else "NS")
            rows.append((p, ym_of(mis[t]), mend(mis[t]).strftime("%Y-%m-%d"), r, P[i, t] * (-1 if t % 9 == 0 else 1),
                         shr[i], exch[i], st, sub, sh))
    msf = pd.DataFrame(rows, columns=["permno", "yyyymm", "mthcaldt", "mthret", "mthprc", "shrout", "primaryexch",
                                      "securitytype", "securitysubtype", "sharetype"])
    names = []
    for p in perms:
        cu = "%08d" % p                                     # all-digit CUSIPs with a leading zero (CSV trap)
        if p == CHG:
            names.append((cu, p, "2000-01-01", "2012-12-31"))
            names.append(("00910004", p, "2013-01-01", "2025-12-31"))
        else:
            names.append((cu, p, "2000-01-01", "2014-06-30" if p == D else "2025-12-31"))
    cus = pd.DataFrame(names, columns=["cusip", "permno", "namedt", "nameenddt"])
    ff = pd.DataFrame({"date": [pd.Timestamp(m // 12, m % 12 + 1, 1).strftime("%Y-%m-%d") for m in mis],
                       "mktrf": F[:, 0], "smb": F[:, 1], "hml": F[:, 2], "rmw": F[:, 3], "cma": F[:, 4],
                       "umd": F[:, 5], "rf": rf})
    br = []
    for p in perms:
        if p == 10005:
            continue                                        # no book value
        lvl = rng.normal(0, 0.5)
        for y in range(2010, 2026):
            lvl += rng.normal(0, 0.2)
            for m in range(1, 13):
                v = float(np.exp(lvl + rng.normal(0, 0.05)))
                if rng.random() < 0.02:
                    v = -v
                br.append((p, mend(mi_of(y, m)).strftime("%Y-%m-%d"), v))
    bm = pd.DataFrame(br, columns=["permno", "public_date", "bm"])
    W = {"msf": msf, "cus": cus, "ff": ff, "bm": bm, "P": P, "R": R, "M0": M0, "perms": perms}
    W["px"] = {(int(p), int(ym)): abs(float(pr)) for p, ym, pr in zip(msf.permno, msf.yyyymm, msf.mthprc)}
    W["ret"] = {(int(p), int(ym)): r for p, ym, r in zip(msf.permno, msf.yyyymm, msf.mthret)}
    make_13f(W, rng)
    make_funds(W, rng)
    return W


def qends():
    out = []
    for y in range(2010, 2026):
        for m in (3, 6, 9, 12):
            if (y, m) >= (2010, 6):
                out.append(pd.Timestamp(y, m, 1) + pd.offsets.MonthEnd(0))
    return out


def cusip_at(p, d):
    if p == CHG:
        return "%08d" % p if d <= pd.Timestamp("2012-12-31") else "00910004"
    return "%08d" % p


def make_13f(W, rng):
    rows = []
    alive_common = [int(p) for p in W["perms"] if p not in (A, D, ETF, ADR, 10005)]

    def file(mg, d, hold):
        ym = d.year * 100 + d.month
        for p, sh in hold:
            rows.append((d.strftime("%Y-%m-%d"), float(mg), d.strftime("%Y-%m-%d"), cusip_at(p, d), float(sh),
                         W["px"][(p, ym)]))

    def generic(mg, skip=(), stop=None, extra=None, v=None):
        k = int(rng.integers(8, 40))
        held = list(rng.choice(alive_common, k, replace=False))
        val = v or float(rng.uniform(2e8, 2e9))
        for d in qends():
            if stop is not None and d > stop:
                break
            n_keep = int(len(held) * 0.7)
            held = list(rng.choice(held, n_keep, replace=False))
            while len(held) < k:
                c = int(rng.choice(alive_common))
                if c not in held:
                    held.append(c)
            if d.strftime("%Y-%m-%d") in skip:
                continue
            ym = d.year * 100 + d.month
            w = rng.dirichlet(np.ones(len(held)))
            hold = [(p, val * wi / W["px"][(p, ym)]) for p, wi in zip(held, w)]
            if extra:
                hold = extra(d, hold, ym, val)
            file(mg, d, hold)

    for mg in range(100, 160):
        generic(mg)
    # F1: stock A at 90 percent plus four others
    oth = [int(x) for x in rng.choice(alive_common, 4, replace=False)]
    for d in qends():
        ym = d.year * 100 + d.month
        file(1, d, [(A, 0.9 * 5e8 / W["px"][(A, ym)])] + [(p, 0.025 * 5e8 / W["px"][(p, ym)]) for p in oth])
    generic(2, stop=pd.Timestamp("2016-12-31"))
    generic(3, skip=("2013-06-30",))
    generic(4, skip=("2013-06-30", "2013-09-30"))

    def add_d(d, hold, ym, val):
        if pd.Timestamp("2012-03-31") <= d <= pd.Timestamp("2014-03-31"):
            tot = sum(sh * W["px"][(p, ym)] for p, sh in hold)
            return hold + [(D, tot / W["px"][(D, ym)])]       # D = half of the book
        return hold
    generic(5, extra=add_d)
    ex = [CHG, ETF, ADR, 10010, 10011]
    d0 = pd.Timestamp("2012-03-31")
    sh = {p: 1e8 / W["px"][(p, 201203)] for p in ex}
    for d in qends():
        if d >= d0:
            file(6, d, [(p, sh[p]) for p in ex])
    many = [int(x) for x in rng.choice(alive_common, 250, replace=False)]
    for d in qends():
        ym = d.year * 100 + d.month
        file(7, d, [(p, 2e7 / W["px"][(p, ym)]) for p in many])
        file(8, d, [(p, 2e6 / W["px"][(p, ym)]) for p in many[:10]])
    s34 = pd.DataFrame(rows, columns=["fdate", "mgrno", "rdate", "cusip", "shares", "prc"])
    # an amendment (later file date) of filer 100 for 2015-03: must be ignored
    am = s34[(s34.mgrno == 100) & (s34.rdate == "2015-03-31")].head(3).copy()
    am["fdate"] = "2015-05-15"
    am["shares"] = am.shares * 7
    W["n100_2015q1"] = s34[(s34.mgrno == 100) & (s34.rdate == "2015-03-31")].cusip.nunique()
    W["s34"] = pd.concat([s34, am], ignore_index=True)
    W["s34names"] = pd.DataFrame({"mgrno": [float(m) for m in list(range(100, 160)) + list(range(1, 9))],
                                  "mgrname": ["FILER %03d" % m for m in list(range(100, 160)) + list(range(1, 9))],
                                  "rdate2": "2025-12-31"})


def make_funds(W, rng):
    ff = W["ff"]
    fmis = list(range(mi_of(2010, 12), mi_of(2025, 12) + 1))
    mk = {mi_of(int(d[:4]), int(d[5:7])): (a, r) for d, a, r in zip(ff.date, ff.mktrf, ff.rf)}
    hdr, sty, ret = [], [], []

    def fund(fno, grp, port, alpha, tna0, obj="EDCL", idx=None, sty_from="2000-01-01", fee=0.0, base=None):
        hdr.append((fno, port, grp, "FUND %d" % fno, idx, None))
        sty.append((fno, sty_from, None, obj))
        tna = tna0
        rs = {}
        for m in fmis:
            a, r0 = mk[m]
            r = (base[m] - fee) if base else r0 + 1.0 * a + alpha + rng.normal(0, 0.01)
            rs[m] = r
            tna = tna0 * (1 + 0.05 * np.sin(m / 7.0)) + rng.normal(0, 0.2)
            ret.append((fno, mend(m).strftime("%Y-%m-%d"), max(tna, 1.0), r))
        return rs
    b = fund(5001, 900, 9000, 0.015, 100.0)
    fund(5002, 900, 9000, 0.0, 50.0, base=b, fee=0.002)
    for k in range(40):
        fund(6001 + k, 6001 + k, None, 0.0, float(rng.uniform(20, 500)))
    fund(6100, 6100, None, 0.04, 300.0, idx="D")
    fund(6101, 6101, None, 0.04, 5.0)
    fund(6102, 6102, None, 0.04, 300.0, obj="EIEI")
    fund(6103, 6103, None, 0.0, 300.0, sty_from="2018-01-01")
    fund(6200, None, 77, 0.0, 100.0)
    fund(6201, None, 77, 0.0, 100.0)
    sty = [s for s in sty if s[0] != 6001] + [(6001, "2000-01-01", "2015-12-31", "EDYG"),
                                              (6001, "2016-01-01", None, "EDCL")]
    W["fhdr"] = pd.DataFrame(hdr + [hdr[1]], columns=["crsp_fundno", "crsp_portno", "crsp_cl_grp", "fund_name",
                                                      "index_fund_flag", "et_flag"])   # 5002 header row twice
    W["fsty"] = pd.DataFrame(sty, columns=["crsp_fundno", "begdt", "enddt", "crsp_obj_cd"])
    W["fret"] = pd.DataFrame(ret, columns=["crsp_fundno", "caldt", "mtna", "mret"])


def frozen_rows():
    R = []

    def add(i, name, kind, grade, style, mg="", fn="", s="", e="", own=1, ran="yes", xm="", xe="", region="us"):
        R.append({"id": i, "name": name, "record_kind": kind, "mgrnos": mg, "fundnos": fn, "start_ym": s,
                  "end_ym": e, "grade": grade, "primary_style": style, "region": region, "explicit_max": xm,
                  "explicit_mean": xe, "own_docs": own, "ran_money": ran})
    add("I001", "Alpha One", "13f", "A", "quality_compounders", mg="1", own=3, xm="2", xe="1.5")
    add("I002", "Gap Pair", "13f", "B", "long_short", mg="3 4", own=2)
    add("I003", "Fund Planted", "fund", "F", "deep_value", fn="5001 5002", own=2)
    add("I004", "Stopper", "13f", "A", "growth", mg="2", s="2012-01")
    add("I005", "Writer", "none", "N", "none", ran="no", xm="3", xe="3")
    add("I006", "Explicit Man", "none", "N", "none", own=4, xm="3", xe="2.5")
    add("I007", "Delist Holder", "13f", "A", "deep_value", mg="5")
    add("I008", "Exact Book", "13f", "A", "special_situations", mg="6", e="2024-06")
    for k in range(12):
        add("I%03d" % (10 + k), "Generic %d" % k, "13f", "A", "quality_compounders" if k < 10 else "growth",
            mg=str(100 + k), own=1 + k % 3, xm=str(k % 4), xe="%.2f" % (k % 4 * 0.6))
    add("I022", "Macro Filer", "13f", "C", "macro_multi_asset", mg="120", xm="1", xe="1")
    add("I023", "Generic Fund", "fund", "F", "growth", fn="6001")
    add("I024", "Shares Filer 100", "13f", "B", "long_short", mg="100", s="2016-01")
    for k in range(20):
        add("I%03d" % (30 + k), "Quality %d" % k, "13f", "A", "quality_compounders", mg=str(112 + k), ran="unclear")
    return R


# ======================================================================================= fake WRDS helpers
class Fake(object):
    def __init__(self, W, data):
        self.W, self.data, self.queries = W, data, []

    def save(self, name, df):
        df.to_csv(os.path.join(self.data, re.sub(r"[^A-Za-z0-9_-]", "_", name) + ".csv.gz"), index=False)

    def load(self, name, **kw):
        return pd.read_csv(os.path.join(self.data, name + ".csv.gz"), **kw)

    def sql(self, q):
        self.queries.append(q)
        m = re.match(r"\s*/\* eqsc (\w+)([^*]*)\*/", q)
        assert m, "untagged query"
        kind, args = m.group(1), m.group(2).split()
        W = self.W
        if kind == "names":
            return W["s34names"].copy()
        if kind == "cusip":
            return W["cus"].drop_duplicates().copy()
        if kind == "ff":
            return W["ff"][(W["ff"].date >= "2009-01-01") & (W["ff"].date <= "2025-12-31")].copy()
        if kind == "bm":
            b = W["bm"]
            d = pd.to_datetime(b.public_date)
            return b[(b.public_date >= "2010-01-01") & (b.public_date <= "2025-06-30") & (d.dt.month <= 6)].copy()
        if kind == "fhdr":
            return W["fhdr"].copy()
        if kind == "fsty":
            s = W["fsty"]
            return s[s.enddt.isna() | (s.enddt >= "2010-12-01")].copy()
        if kind == "msf":
            s = W["msf"]
            return s[(s.mthcaldt >= args[0]) & (s.mthcaldt <= args[1])].drop(columns=["mthcaldt"]).copy()
        if kind == "agg":
            return fake_agg(W, args[0], args[1])
        if kind == "hold":
            ids = [float(x) for x in re.search(r"mgrno in \(([^)]*)\)", q).group(1).split(",")]
            s = W["s34"]
            s = s[(s.fdate == s.rdate) & (s.shares > 0) & (s.rdate >= args[0]) & (s.rdate <= args[1])
                  & s.mgrno.isin(ids)]
            return s[["mgrno", "rdate", "cusip", "shares", "prc"]].copy()
        if kind == "fret":
            ed = set(W["fsty"][W["fsty"].crsp_obj_cd.str.startswith("ED")].crsp_fundno)
            lib = re.search(r"or crsp_fundno in \(([\d,]+)\)", q)
            if lib:
                ed |= {int(x) for x in lib.group(1).split(",")}
            f = W["fret"]
            return f[(f.caldt >= args[0]) & (f.caldt <= args[1]) & f.crsp_fundno.isin(ed)].copy()
        raise AssertionError("unknown query " + kind)


def fake_agg(W, lo, hi):
    """Independent version of the SQL aggregate: per filer and quarter, matched positions and value."""
    s = W["s34"]
    s = s[(s.fdate == s.rdate) & (s.shares > 0) & (s.rdate >= lo) & (s.rdate <= hi)].copy()
    s["fv"] = s.shares * s.prc
    h = s.groupby(["mgrno", "rdate", "cusip"], as_index=False).agg(sh=("shares", "sum"), fv=("fv", "sum"))
    k = h.merge(W["cus"], on="cusip", how="left")
    ok = (k.rdate >= k.namedt) & (k.rdate <= k.nameenddt)
    k = k[ok].sort_values("permno").drop_duplicates(["mgrno", "rdate", "cusip"])
    h = h.merge(k[["mgrno", "rdate", "cusip", "permno"]], on=["mgrno", "rdate", "cusip"], how="left")
    ym = h.rdate.str[:4].astype(int) * 100 + h.rdate.str[5:7].astype(int)
    h["px"] = [W["px"].get((int(p), int(y))) if p == p else None for p, y in zip(h.permno, ym)]
    h["px"] = h.px.astype(float)
    m = h.px.notna()
    h["fvu"] = np.where(m, h.fv, 0.0)
    h["val"] = np.where(m, h.sh * h.px.fillna(0), 0.0)
    h["pm"] = np.where(m, h.permno, np.nan)
    out = h.groupby(["mgrno", "rdate"], as_index=False).agg(fv_all=("fv", "sum"), fv_used=("fvu", "sum"),
                                                          npos=("pm", "nunique"), val=("val", "sum"))
    return out


def load_module(src, name):
    m = types.ModuleType(name)
    m.__file__ = name + ".py"
    exec(compile(src, name + ".py", "exec"), m.__dict__)
    return m


def run_pipeline(mod, fk):
    buf = []
    o = lambda *a: buf.append(" ".join(str(x) for x in a))  # noqa: E731
    mod.pull_base(fk.sql, fk.save, o, fk.data)
    mod.pull_crsp(fk.sql, fk.save, o, fk.data)
    mod.pull_agg(fk.sql, fk.save, o, fk.data)
    mod.pull_hold(fk.sql, fk.load, fk.save, o, fk.data)
    mod.pull_funds(fk.sql, fk.save, o, fk.data)
    res = mod.build(fk.load, fk.save, o, fk.data)
    parts = []
    for k in range(1, 5):
        pb = []
        mod.report(fk.load, lambda *a: pb.append(" ".join(str(x) for x in a)), k, 4)
        parts.append("\n".join(pb))
    return res, parts, buf


# ============================================================================================ independent
def nw_reference(y, X, L):
    """Newey-West by explicit loops (independent of the module)."""
    n = len(y)
    Z = np.column_stack([np.ones(n), X])
    k = Z.shape[1]
    b = np.linalg.lstsq(Z, y, rcond=None)[0]
    e = y - Z @ b
    S = np.zeros((k, k))
    for t in range(n):
        S += e[t] ** 2 * np.outer(Z[t], Z[t])
    for l in range(1, L + 1):
        w = 1 - l / (L + 1)
        for t in range(l, n):
            G = e[t] * e[t - l] * np.outer(Z[t], Z[t - l])
            S += w * (G + G.T)
    Q = np.linalg.inv(Z.T @ Z)
    V = Q @ S @ Q * n / (n - k)
    return b, b / np.sqrt(np.diag(V))


def ref_groups(W, fy):
    """DGTW groups of formation year fy computed directly from the fake tables."""
    msf, bm = W["msf"], W["bm"]
    j = msf[msf.yyyymm == fy * 100 + 6]
    com = j[(j.securitytype == "EQTY") & (j.securitysubtype == "COM") & (j.sharetype == "NS")
            & j.primaryexch.isin(["N", "A", "Q"])].copy()
    com["cap"] = com.mthprc.abs() * com.shrout
    b = bm[(bm.public_date >= "%d-01-01" % fy) & (bm.public_date <= "%d-06-30" % fy)]
    b = b.sort_values("public_date").groupby("permno").bm.last()
    com["bm"] = com.permno.map(b)
    yms = [(fy - 1) * 100 + m for m in range(6, 13)] + [fy * 100 + m for m in range(1, 6)]
    rr = msf[msf.yyyymm.isin(yms)].pivot(index="permno", columns="yyyymm", values="mthret").reindex(columns=yms)
    mom = (1 + rr).prod(axis=1, skipna=False) - 1
    com["mom"] = com.permno.map(mom)
    u = com[(com.cap > 0) & (com.bm > 0) & com.mom.notna() & com.bm.notna()].copy()
    bps = np.percentile(u[u.primaryexch == "N"].cap, [20, 40, 60, 80])
    u["s"] = [int(np.sum(bps < c)) for c in u.cap]
    out = {}
    for s, g in u.groupby("s"):
        g = g.sort_values(["bm", "permno"]).reset_index(drop=True)
        g["b"] = (5 * np.arange(len(g))) // len(g)
        for bq, h in g.groupby("b"):
            h = h.sort_values(["mom", "permno"]).reset_index(drop=True)
            for k, p in enumerate(h.permno):
                out[int(p)] = s * 25 + bq * 5 + (5 * k) // len(h)
    return out


def book_months(res, bk):
    M = res["M"]
    g = M[M.bk == bk]
    return dict(zip([ym_of(int(x)) for x in g.mi], g.ret)), g


def expected_hold(W, mg, rdate, months):
    s = W["s34"]
    g = s[(s.mgrno == mg) & (s.rdate == rdate) & (s.fdate == s.rdate)]
    d = pd.Timestamp(rdate)
    ym = d.year * 100 + d.month
    val = {}
    for cu, sh in zip(g.cusip, g.shares):
        c = W["cus"][(W["cus"].cusip == cu) & (pd.to_datetime(W["cus"].namedt) <= d)
                     & (pd.to_datetime(W["cus"].nameenddt) >= d)]
        p = int(c.permno.min())
        val[p] = val.get(p, 0.0) + sh * W["px"][(p, ym)]
    tot = sum(val.values())
    w = {p: v / tot for p, v in val.items()}
    out = {}
    for m in months:
        r = {p: W["ret"].get((p, m), np.nan) for p in w}
        r = {p: (0.0 if (x is None or not np.isfinite(x)) else x) for p, x in r.items()}
        out[m] = sum(w[p] * r[p] for p in w) / sum(w.values())
        w = {p: w[p] * (1 + r[p]) for p in w}
    return out


def fund_expected(W):
    f = W["fret"]
    a = f[f.crsp_fundno == 5001].set_index("caldt")
    b = f[f.crsp_fundno == 5002].set_index("caldt")
    ds = list(a.index)
    out = {}
    for k in range(1, len(ds)):
        d, p = ds[k], ds[k - 1]
        wa, wb = a.mtna[p], b.mtna[p]
        out[int(d[:4]) * 100 + int(d[5:7])] = (wa * a.mret[d] + wb * b.mret[d]) / (wa + wb)
    return out


# ================================================================================================= checks
def checks(res, parts, W, fz):
    C = []

    def ck(name, cond, detail=""):
        C.append((name, bool(cond), detail))

    tab, M = res["tab"], res["M"]
    inv = {d["id"]: d for d in res["inv"]}
    t1 = tab[(tab.bk == 1) & (tab.w == "2011-25")].iloc[0]
    pool = res["pools"]["13f"]["2011-25"]
    ck("C01 planted filer: alpha > 20%/yr, t > 5, best of its rank group",
       t1.a > 20 and t1.t > 5 and pool.idxmax() == 1, "a %.1f t %.1f" % (t1.a, t1.t))
    ck("C02 library investor on that filer: rank share 1", inv["I001"]["win"]["2011-25"]["rk"] == 1.0)
    r6, g6 = book_months(res, 6)
    exp6 = expected_hold(W, 6.0, "2012-03-31", [201206, 201207, 201208])
    ck("C03 point in time: first record month = month after the deadline month (2012-06)",
       min(r6) == 201206, "first %s" % min(r6))
    ck("C03b buy and hold from quarter-end weights (exact)",
       all(abs(r6.get(m, 9) - v) < 1e-10 for m, v in exp6.items()))
    r5, g5 = book_months(res, 5)
    exp5 = expected_hold(W, 5.0, "2014-03-31", [201406, 201407, 201408])
    ck("C04 delisting return counted (June 2014, D at half weight, -90%)",
       abs(r5.get(201406, 9) - exp5[201406]) < 1e-10, "got %.4f want %.4f" % (r5.get(201406, 9), exp5[201406]))
    ck("C04b after delisting: weight kept, no return (July 2014 weight share without return > 0)",
       float(g5[g5.mi == mi_of(2014, 7)].miss.iloc[0]) > 0.02)
    r2, _ = book_months(res, 2)
    n2 = tab[(tab.bk == 2) & (tab.w == "2016-20")].n
    ck("C05 stopped filer leaves the record after its last 3-month hold (last 2017-05; 17 months in 2016-20)",
       max(r2) == 201705 and len(n2) and int(n2.iloc[0]) == 17, "last %s n %s" % (max(r2), list(n2)))
    ck("C05b stopped filer: no result in 2016-20, counted in the persistence 'stopped' column",
       res["persist"]["13f"][0][2]["tbl"][:, 5].sum() >= 1)
    r3, _ = book_months(res, 3)
    ck("C06 one missed quarter bridged (2013-06..2013-11 present, 180 months)",
       all(m in r3 for m in (201306, 201307, 201308, 201309, 201310, 201311)) and len(r3) == 180, len(r3))
    r4, _ = book_months(res, 4)
    gap = [201309, 201310, 201311, 201312, 201401, 201402]
    ck("C07 two missed quarters end the spell (2013-09..2014-02 absent, 174 months)",
       all(m not in r4 for m in gap) and len(r4) == 174 and 201308 in r4 and 201403 in r4, len(r4))
    fx = fund_expected(W)
    fr = res["frec"]
    g = fr[fr.gid == "G900"]
    got = dict(zip([ym_of(int(x)) for x in g.mi], g.ret))
    ck("C08 share classes combined by start-of-month assets (exact, 180 months)",
       len(got) == 180 and all(abs(got[m] - fx[m]) < 1e-10 for m in got))
    ft = res["ftab"]
    out_ = ft[ft.bk.isin(["G6100", "G6101", "G6102"]) & ft.grp]
    ck("C09 fund ranks among funds only: planted fund rank share 1",
       inv["I003"]["win"]["2011-25"]["rk"] == 1.0, inv["I003"]["win"]["2011-25"].get("rk"))
    ck("C09b index, small and non-domestic funds stay out of the fund rank group; style gap excluded 2011-15",
       len(out_) == 0 and not ft[(ft.bk == "G6103") & (ft.w == "2011-15")].grp.any())
    pe = res["peers"]
    ok = True
    for fy in (2010, 2015, 2024):
        ref = ref_groups(W, fy)
        ri, okr = res["panel"].rows(np.array(sorted(ref)))
        mine = pe.G[ri, fy - 2010]
        allg = {int(p): int(x) for p, x in zip(res["panel"].perm, pe.G[:, fy - 2010]) if x >= 0}
        ok &= allg == ref
    ck("C10 peer groups: June size and June book-to-market, momentum to May (3 formation years exact)", ok)
    rng = np.random.default_rng(3)
    X = rng.normal(0, 1, (80, 6))
    y = X @ rng.normal(0, 1, 6) + 0.3 + rng.standard_t(4, 80)
    b, t = load_module(open(MODULE).read(), "eqsc_ref").ols_nw(y, X, 3)
    b2, t2 = nw_reference(y, X, 3)
    ck("C11 Newey-West regression (3 lags) = loop reference", np.allclose(b, b2) and np.allclose(t, t2))
    cand = set(pd.read_csv(os.path.join(fz.data, "eq_sc_cand.csv.gz")).mgrno)
    ck("C12 holdings pulled only for rank-group candidates and library filers (7, 8 out; 1-6 in)",
       not ({7, 8} & cand) and {1, 2, 3, 4, 5, 6} <= cand)
    st = res["st"]
    n100 = st[(st.bk == 100) & (st.q == 2015 * 4)].npos
    ck("C13 amended filing ignored (first version only)", len(n100) and int(n100.iloc[0]) == W["n100_2015q1"])
    big = max(len(p) for p in parts)
    rep = "\n".join(parts)
    leak = [c for c in set(W["s34"].cusip) if c in rep] + \
           [str(p) for p in W["perms"] if re.search(r"\b%d\b" % p, rep)]
    ck("C14 report: every part under 60,000 characters, no CUSIP or permno printed",
       big < 60000 and not leak and "END OF SCORECARD" in rep and "TIER A by record" in rep, "max %d leak %s"
       % (big, leak[:3]))
    T = res["tiers"]
    styles = {}
    for i in T["record"]:
        styles[inv[i]["style"]] = styles.get(inv[i]["style"], 0) + 1
    elig = sorted(d["id"] for d in res["inv"] if d["grade"] in "ABF" and d["own_docs"] >= 1 and d["months"] >= 60)
    pool_c = sorted(i for i in elig if i not in set(T["record"]) | set(T["explicit"]))
    ctrl = sorted(random.Random(20261117).sample(pool_c, 10)) if len(pool_c) > 10 else pool_c
    sc = [inv[i]["score"] for i in T["record"]]
    ck("C15 tier rule: at most 8 per style, scores descending, explicit places, control by seed 20261117",
       max(styles.values()) == 8 and sc == sorted(sc, reverse=True) and T["control"] == ctrl
       and len(pool_c) > 10 and T["explicit"][0] == "I006" and "I005" not in T["explicit"]
       and len(T["record"]) == 17, "record %d control pool %d" % (len(T["record"]), len(pool_c)))
    ck("C16 two investors on one filer, months cut to the frozen years (I024 120, I010 180, I008 to 2024-06)",
       inv["I024"]["months"] == 120 and inv["I010"]["months"] == 180 and inv["I008"]["months"] == 145
       and inv["I004"]["months"] == 65)
    ex_ = g6[np.isfinite(g6.pa)]
    ck("C17 variants: top-10 = whole book when 10 or fewer positions; no new positions in a constant book",
       np.allclose(ex_.pa, ex_.p10) and g6.pn.isna().all())
    ck("C18 peer-adjusted return leaves out the ETF and the ADR (value share with a peer group < 1)",
       0.3 < float(g6.pash.mean()) < 0.8)
    found = [r[0] for r in sorted(fz.docs, key=lambda r: (-r[1], -r[2], -r[3], r[0]))[:50]]
    ck("C19 foundation list (technique depth, areas, words, document number)", res["found"] == found)
    ck("C20 counts: filers and funds in each rank group", all(c[1] > 40 and c[2] > 30 for c in res["counts"]))
    return C


# ================================================================================================== seal
def seal_tests(tmp, libdir):
    C = []
    job = os.path.join(tmp, "eq_scorecard_v1.json")
    ok, msgs, extra = seal_check.check_job(job, [libdir])
    C.append(("S1 scorecard job passes as seal-exempt", ok, msgs[:2]))
    src = open(os.path.join(libdir, "eq_scorecard.py")).read()
    bad = os.path.join(tmp, "bad_lib")
    os.makedirs(bad, exist_ok=True)
    shutil.copy(os.path.join(libdir, "eq_reader.py"), bad)
    open(os.path.join(bad, "eq_scorecard.py"), "w").write(src.replace("MIN_RESULT, MIN_STATS, NW_LAGS = 36, 60, 3",
                                                                      "MIN_RESULT, MIN_STATS, NW_LAGS = 24, 60, 3"))
    ok, msgs, _ = seal_check.check_job(job, [bad])
    C.append(("S2 changed scorecard code is refused (hash)", not ok, msgs[:1]))
    lines = src.splitlines(True)
    i = next(k for k, x in enumerate(lines) if x.startswith(seal_check.INPUT_BEGIN))
    open(os.path.join(bad, "eq_scorecard.py"), "w").write("".join(lines[:i + 1]) + "import os\n" + "".join(lines[i + 1:]))
    ok, msgs, _ = seal_check.check_job(job, [bad])
    C.append(("S3 code smuggled into the frozen input block is refused", not ok, msgs[:1]))

    def jobfile(name, steps):
        p = os.path.join(tmp, name + ".json")
        json.dump({"name": name, "steps": steps}, open(p, "w"))
        return p
    open(os.path.join(libdir, "eq_test_ok.py"), "w").write(
        "import eq_reader\n\ndef run(sql, out):\n    d = eq_reader.read(sql, 'crsp.msf_v2', ['permno'], '1990-01', '2010-12')\n"
        "    out(len(d))\n")
    open(os.path.join(libdir, "eq_test_bad.py"), "w").write(
        "def run(sql, out):\n    d = sql('select * from crsp.msf_v2')\n    out(len(d))\n")
    cases = [
        ("S4 metadata-only equity job passes", jobfile("eq_meta_v1", [{"do": "describe", "table": "crsp.msf_v2"},
                                                                     {"do": "datasets"}]), True),
        ("S5 reader-only job passes", jobfile("eq_ok_v1", [{"do": "python", "code": "import eq_test_ok\n"
                                                            "eq_test_ok.run(sql, out)"}]), False),
        ("S6 direct sql in a step is refused", jobfile("eq_x1", [{"do": "python", "code": "d = sql('select 1')"}]),
         False),
        ("S7 direct sql in a lib module is refused", jobfile("eq_x2", [{"do": "python", "code": "import eq_test_bad\n"
                                                                        "eq_test_bad.run(sql, out)"}]), False),
        ("S8 pull step is refused", jobfile("eq_x3", [{"do": "pull", "name": "x", "sql": "select 1"}]), False),
        ("S9 exempt= flag outside an exempt job is refused", jobfile("eq_x4", [{"do": "python", "code":
            "import eq_reader\nd = eq_reader.read(sql, 'tfn.s34', ['mgrno'], '2011-01', '2012-12', exempt=True)"}]),
         False),
        ("S10 data set read with load() is refused", jobfile("eq_x5", [{"do": "python", "code":
                                                                         "d = load('eq_sc_hold_2015')"}]), False),
        ("S11 os / open / getattr tricks are refused", jobfile("eq_x6", [{"do": "python", "code":
            "import os\nf = open(os.path.join(DATA, 'x'))\ng = getattr(pd, 'read_' + 'csv')"}]), False),
        ("S12 a job named like the exempt one but with a direct read in its step is refused", jobfile(
            "eq_scorecard_v9", [{"do": "python", "code": "import eq_scorecard\nd = sql('select 1')"}]), False),
    ]
    for name, p, _ in cases:
        ok, msgs, _ = seal_check.check_job(p, [libdir])
        want = name.startswith("S4") or name.startswith("S5")
        C.append((name, ok == want, msgs[:1]))
    os.remove(os.path.join(libdir, "eq_test_ok.py"))
    os.remove(os.path.join(libdir, "eq_test_bad.py"))
    # reader at run time
    calls = []

    def fsql(q):
        calls.append(q)
        return pd.DataFrame({"permno": [1], "mthcaldt": ["2005-03-31"]})

    def refused(f):
        try:
            f()
            return False
        except eq_reader.SealError:
            return True
    r1 = refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "2009-01", "2011-01"))
    r2 = not refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "1990-01", "2010-12"))
    r3 = refused(lambda: eq_reader.read(fsql, "comp.g_funda", ["gvkey"], "1985-01", "1990-01"))
    r4 = refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "1990-01", "2000-12",
                                        where="1=1) or (1=1"))
    r5 = refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "1990-01", "2000-12",
                                        where="permno in (select permno from tfn.s34)"))
    r6 = not refused(lambda: eq_reader.read(fsql, "tfn.s34", ["mgrno"], "2026-01", "2026-03"))
    r7 = refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "2004-01", "2004-12"))  # 2005 row back
    r8 = not refused(lambda: eq_reader.read(fsql, "tfn.s34", ["mgrno"], "2011-01", "2012-12", exempt=True))
    C.append(("S13 reader refuses sealed months (US 2011-01.., non-US 1990-01..), injected where clauses and rows "
              "outside the range; allows design months, months after the seal end and exempt reads",
              all([r1, r2, r3, r4, r5, r6, r7, r8]), [r1, r2, r3, r4, r5, r6, r7, r8]))
    return C


# ============================================================================================== mutations
MUTATIONS = [
    ("look-ahead of one quarter in the holdings",
     "    return d.year * 12 + d.month - 1\n", "    return d.year * 12 + d.month - 1 - 3\n"),
    ("dropped delisting return",
     "    return msf\n",
     "    msf = msf.copy()\n    last = msf.groupby('permno').yyyymm.transform('max')\n"
     "    msf.loc[(msf.yyyymm == last) & (last < 202512), 'mthret'] = np.nan\n    return msf\n"),
    ("peer group built with the same month's size",
     "        js = self._j(fy * 12 + 5)       # size at the end of June of the formation year\n",
     "        js = self._j(fy * 12 + 6)       # size at the end of June of the formation year\n"),
    ("filer that stops filing kept with zero returns",
     "                g = g[(g.mi >= a) & (g.mi <= b)]\n",
     "                g = g[(g.mi >= a) & (g.mi <= b)]\n                if len(g):\n"
     "                    g = pd.concat([g, pd.DataFrame({'bk': bk, 'mi': np.arange(g.mi.max() + 1, b + 1), "
     "'ret': 0.0})], ignore_index=True)\n"),
    ("doubled share class",
     '    h = hdr.drop_duplicates("crsp_fundno")       # one header row per share class\n',
     "    h = hdr\n"),
    ("rank computed across record kinds",
     "            pool = pools[kind][w]\n",
     '            pool = pd.concat([pools["13f"][w], pools["fund"][w]])\n'),
]


def main():
    keep = None
    if "--keep" in sys.argv:
        keep = sys.argv[sys.argv.index("--keep") + 1]
    tmp = tempfile.mkdtemp(prefix="eqsc_")
    try:
        W = make_world()
        # frozen file + inventory, generator -> module copy and job
        fzp = os.path.join(tmp, "frozen_investors.csv")
        rows = frozen_rows()
        with open(fzp, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        rng = np.random.default_rng(11)
        docs = [[d, int(rng.integers(0, 4)), int(rng.integers(0, 4)), int(rng.integers(500, 20000))]
                for d in range(1, 81)]
        docs[5][1:] = docs[6][1:]                               # a full tie, broken by document number
        invp = os.path.join(tmp, "inventory.csv")
        with open(invp, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["doc", "technique", "technique_depth", "words"])
            for d, dep, na, wd in docs:
                w.writerow([d, ";".join("t%d" % k for k in range(na)), dep, wd])
        libdir = os.path.join(tmp, "lib")
        os.makedirs(libdir)
        shutil.copy(MODULE, libdir)
        shutil.copy(os.path.join(ROOT, "tools", "equity", "wrds", "eq_reader.py"), libdir)
        modp = os.path.join(libdir, "eq_scorecard.py")
        jobp = os.path.join(tmp, "eq_scorecard_v1.json")
        g = subprocess.run([sys.executable, GEN, "--frozen", fzp, "--inventory", invp, "--module", modp, "--job",
                            jobp], capture_output=True, text=True)
        assert g.returncode == 0, g.stderr
        src = open(modp).read()
        assert seal_check.code_hash(src) == seal_check.code_hash(open(MODULE).read())
        data = os.path.join(tmp, "data")
        os.makedirs(data)
        fk = Fake(W, data)
        fk.docs = docs
        mod = load_module(src, "eq_scorecard")
        res, parts, log = run_pipeline(mod, fk)
        assert res is not None, "\n".join(log)
        C = checks(res, parts, W, fk)
        S = seal_tests(tmp, libdir)
        bad = [c for c in C + S if not c[1]]
        for name, ok, det in C + S:
            print("%-4s %s%s" % ("ok" if ok else "FAIL", name, "" if ok else "  [%s]" % (det,)))
        if keep:
            os.makedirs(keep, exist_ok=True)
            for p in (fzp, invp, modp, jobp):
                shutil.copy(p, keep)
            open(os.path.join(keep, "report_invented.txt"), "w").write("\n".join(parts))
        assert not bad, "%d checks failed" % len(bad)
        # mutations
        print("\nplanted error (registration s.11)              | checks failed | caught")
        caught = 0
        for name, a, b in MUTATIONS:
            assert src.count(a) == 1, "mutation anchor not unique: %s" % name
            mm = load_module(src.replace(a, b), "eqsc_mut")
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    r2, p2, _ = run_pipeline(mm, fk)
                failed = [c[0].split()[0] for c in checks(r2, p2, W, fk) if not c[1]]
            except Exception as e:  # noqa: BLE001
                failed = ["error: %s" % type(e).__name__]
            caught += bool(failed)
            print("%-47s | %-13s | %s" % (name, ",".join(failed)[:13] if failed else "-", "yes" if failed else "NO"))
        print("catch rate %d of %d" % (caught, len(MUTATIONS)))
        assert caught == len(MUTATIONS)
        print("eq_scorecard smoke: PASS")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
