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
import operator

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
            if (rng.random() < 0.003 and p not in (A, D, 10010)) or (p == 10010 and mis[t] == mi_of(2012, 7)):
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
    dup = bm[(bm.permno == 10006) & (bm.public_date == "2015-06-30")].copy()
    dup["bm"] = dup.bm * 3                                  # two different values on one date: no value that year
    bm = pd.concat([bm, dup], ignore_index=True)
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
    mid = [int(x) for x in rng.choice(alive_common, 180, replace=False)]
    for d in qends():
        ym = d.year * 100 + d.month
        file(9, d, [(p, 5.5e6 / W["px"][(p, ym)]) for p in mid])          # 180 positions: above the rank group
        file(10, d, [(p, 8e7 / 12 / W["px"][(p, ym)]) for p in mid[:12]])  # $80M: below the value floor
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
    W["s34names"] = pd.DataFrame({"mgrno": [float(m) for m in list(range(100, 160)) + list(range(1, 11))],
                                  "mgrname": ["FILER %03d" % m for m in list(range(100, 160)) + list(range(1, 11))],
                                  "rdate2": "2025-12-31"})


def make_funds(W, rng):
    ff = W["ff"]
    fmis = list(range(mi_of(2010, 12), mi_of(2025, 12) + 1))
    mk = {mi_of(int(d[:4]), int(d[5:7])): (a, r) for d, a, r in zip(ff.date, ff.mktrf, ff.rf)}
    hdr, sty, ret = [], [], []

    def fund(fno, grp, port, alpha, tna0, obj="EDCL", idx=None, sty_from="2000-01-01", fee=0.0, base=None,
             style=True):
        hdr.append((fno, port, grp, "FUND %d" % fno, idx, None))
        if style:
            sty.append((fno, sty_from, None, obj))
        tna = tna0
        rs = {}
        for m in fmis:
            a, r0 = mk[m]
            r = (base[m] - fee) if base else r0 + 1.0 * a + alpha + rng.normal(0, 0.01)
            rs[m] = r
            tna = tna0 * (1 + 0.05 * np.sin(m / 7.0)) + rng.normal(0, 0.2)
            bad = fno == 5002 and mi_of(2015, 1) <= m <= mi_of(2015, 6)     # CRSP missing-value code
            ret.append((fno, mend(m).strftime("%Y-%m-%d"), -99.0 if bad else max(tna, 1.0), r))
        return rs
    b = fund(5001, 900, 9000, 0.015, 100.0)
    fund(5002, 900, 9000, 0.0, 50.0, base=b, fee=0.002)
    for k in range(40):
        fund(6001 + k, 6001 + k, None, 0.0, float(rng.uniform(20, 500)))
    fund(6100, 6100, None, 0.04, 300.0, idx="D")
    fund(6101, 6101, None, 0.04, 5.0)
    fund(6102, 6102, None, 0.04, 300.0, obj="EIEI")
    fund(6103, 6103, None, 0.0, 300.0, sty_from="2018-01-01")
    fund(5011, 901, None, 0.0, 80.0)
    fund(5012, 901, None, 0.0, 40.0, style=False)                    # class of an ED fund without a style row
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

    def add(i, name, kind, grade, style, mg="", fn="", s="", e="", own=1, ran="yes", xm="", xe="", region="us",
            role="investor", km="", kf="", sw=""):
        R.append({"id": i, "name": name, "record_kind": kind, "mgrnos": mg, "fundnos": fn, "start_ym": s,
                  "end_ym": e, "grade": grade, "primary_style": style, "region": region, "explicit_max": xm,
                  "explicit_mean": xe, "own_docs": own, "ran_money": ran, "role": role,
                  "known_mgrnos": km or mg, "known_fundnos": kf or fn, "shares_record_with": sw})
    add("I001", "Alpha One", "13f", "A", "quality_compounders", mg="1", own=3, xm="2", xe="1.5", kf="6005")
    add("I002", "Gap Pair", "13f", "B", "long_short", mg="3 4", own=2)
    add("I003", "Fund Planted", "fund", "F", "deep_value", fn="5002", own=2, km="150")   # one class = the fund
    add("I004", "Stopper", "13f", "A", "growth", mg="2", s="2012-01")
    add("I005", "Writer", "none", "N", "none", ran="no", xm="3", xe="3")
    add("I006", "Explicit Man", "none", "N", "none", own=4, xm="3", xe="2.5")
    add("I007", "Delist Holder", "13f", "A", "deep_value", mg="5")
    add("I008", "Exact Book", "13f", "A", "special_situations", mg="6", e="2024-06")
    for k in range(12):
        add("I%03d" % (10 + k), "Generic %d" % k, "13f", "A", "quality_compounders" if k < 10 else "growth",
            mg=str(100 + k), own=1 + k % 3, xm=str(k % 4), xe="%.2f" % (k % 4 * 0.6))
    add("I022", "Macro Filer", "13f", "C", "macro_multi_asset", mg="120", xm="1", xe="1")
    add("I023", "Two Funds", "fund", "F", "growth", fn="6001 6002")        # two funds: one record
    add("I024", "Shares Filer 100", "13f", "B", "long_short", mg="100", s="2016-01")
    for k in range(20):
        add("I%03d" % (30 + k), "Quality %d" % k, "13f", "A", "quality_compounders", mg=str(112 + k), ran="unclear")
    add("I050", "Tie More Docs", "13f", "A", "special_situations", mg="140", own=3, ran="unclear")
    add("I051", "Tie Fewer Docs", "13f", "A", "special_situations", mg="140", own=1, ran="unclear")
    add("I052", "Fifty Months", "13f", "A", "growth", mg="141", s="2021-01", e="2025-02", ran="unclear")
    add("I053", "Thirty Months", "13f", "A", "growth", mg="142", s="2023-07", ran="unclear")
    add("I054", "Allocator", "none", "N", "none", own=5, xm="3", xe="3", role="allocator")
    add("I055", "Book Owner", "13f", "A", "growth", mg="143", ran="unclear")
    add("I056", "Same Book", "13f", "A", "growth", mg="143", own=2, ran="unclear", sw="I055")
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
            h = W["fhdr"].drop_duplicates("crsp_fundno")
            gid = {int(f): ("G%d" % g if g == g else ("P%d" % pt if pt == pt else "C%d" % f))
                   for f, g, pt in zip(h.crsp_fundno, h.crsp_cl_grp, h.crsp_portno)}
            seed = set(W["fsty"][W["fsty"].crsp_obj_cd.str.startswith("ED")].crsp_fundno)
            lib = args[2].split("=")[1]
            if lib != "-":
                seed |= {int(x) for x in lib.split(",")}
            gs = {gid[f] for f in seed if f in gid}
            keep = {f for f, g in gid.items() if g in gs} | seed
            f = W["fret"]
            return f[(f.caldt >= args[0]) & (f.caldt <= args[1]) & f.crsp_fundno.isin(keep)].copy()
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


def load_module(src, name, path=None):
    m = types.ModuleType(name)
    m.__file__ = path or (name + ".py")
    exec(compile(src, m.__file__, "exec"), m.__dict__)
    return m


def run_pipeline(mod, fk):
    buf = []
    o = lambda *a: buf.append(" ".join(str(x) for x in a))  # noqa: E731
    mod.pull_base(fk.sql, fk.save, o, fk.data)
    mod.pull_crsp(fk.sql, fk.save, o, fk.data)
    mod.pull_agg(fk.sql, fk.save, o, fk.data)
    mod.pull_hold(fk.sql, fk.load, fk.save, o, fk.data)
    mod.pull_funds(fk.sql, fk.load, fk.save, o, fk.data)
    mod.pull_status(fk.load, o, fk.data)
    ret = mod.build(fk.load, fk.save, o, fk.data)
    assert ret is None, "build must return nothing"
    res = dict(mod.LAST) if mod.LAST else None
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
    b = b[b.public_date == b.groupby("permno").public_date.transform("max")]
    nv = b.groupby("permno").bm.nunique()
    b = b[b.permno.isin(nv[nv == 1].index)].groupby("permno").bm.first()
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
        wb = wb if wb > 0 else 0.0                          # -99 = missing assets: the class has no weight
        out[int(d[:4]) * 100 + int(d[5:7])] = (wa * a.mret[d] + wb * b.mret[d]) / (wa + wb)
    return out


def combine_expected(W, fundnos):
    """Classes combined by previous month-end assets (> 0), months 2011-01..2025-12."""
    f = W["fret"][W["fret"].crsp_fundno.isin(fundnos)].copy()
    f["ym"] = f.caldt.str[:4].astype(int) * 100 + f.caldt.str[5:7].astype(int)
    f["mi"] = [mi_of(y // 100, y % 100) for y in f.ym]
    tna = {(a, b): t for a, b, t in zip(f.crsp_fundno, f.mi, f.mtna)}
    out = {}
    for m in range(mi_of(2011, 1), mi_of(2025, 12) + 1):
        num = den = 0.0
        for a, r in zip(f[f.mi == m].crsp_fundno, f[f.mi == m].mret):
            w = tna.get((a, m - 1), 0.0)
            if w > 0:
                num, den = num + w * r, den + w
        if den > 0:
            out[ym_of(m)] = num / den
    return out


def filings_weights(W, mg):
    """Quarter -> {permno: weight} of a filer's first versions, CUSIP at the quarter-end, CRSP quarter-end price."""
    s = W["s34"]
    s = s[(s.mgrno == mg) & (s.fdate == s.rdate)]
    out = {}
    for rd, g in s.groupby("rdate"):
        d = pd.Timestamp(rd)
        ym = d.year * 100 + d.month
        val = {}
        for cu, sh in zip(g.cusip, g.shares):
            c = W["cus"][(W["cus"].cusip == cu) & (pd.to_datetime(W["cus"].namedt) <= d)
                         & (pd.to_datetime(W["cus"].nameenddt) >= d)]
            if len(c) and (int(c.permno.min()), ym) in W["px"]:
                p = int(c.permno.min())
                val[p] = val.get(p, 0.0) + sh * W["px"][(p, ym)]
        t = sum(val.values())
        out[d.year * 4 + (d.month - 1) // 3] = {p: v / t for p, v in val.items()}
    return out


def avg_rank(x):
    """Average ranks 1..n with ties averaged (loop; independent of pandas)."""
    x = list(x)
    out = []
    for v in x:
        out.append(1 + sum(1 for u in x if u < v) + 0.5 * (sum(1 for u in x if u == v) - 1))
    return np.array(out)


def persist_ref(tab, b1, b2):
    t1 = tab[(tab.w == b1) & tab.grp]
    t1 = dict(zip(t1.bk, t1.a))
    t2 = tab[(tab.w == b2) & (tab.n >= 36) & tab.a.notna()]
    t2 = dict(zip(t2.bk, t2.a))
    ids = sorted(t1)
    both = [k for k in ids if k in t2]
    r1 = dict(zip(ids, avg_rank([t1[k] for k in ids])))
    r2 = dict(zip(both, avg_rank([t2[k] for k in both])))
    tbl = np.zeros((5, 6), dtype=int)
    for k in ids:
        q1 = min(5, int(np.floor(5 * (r1[k] - 1) / len(ids))) + 1)
        col = (min(5, int(np.floor(5 * (r2[k] - 1) / len(both))) + 1) - 1) if k in r2 else 5
        tbl[q1 - 1, col] += 1
    return tbl


# ================================================================================================= checks
def checks(res, parts, W, fz):
    C = []

    def ck(name, cond, detail=""):
        C.append((name, bool(cond), detail))

    tab, M, st = res["tab"], res["M"], res["st"]
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
    ck("C03b buy and hold from quarter-end weights; a missing return earns zero and keeps its weight (exact)",
       all(abs(r6.get(m, 9) - v) < 1e-10 for m, v in exp6.items()))
    r5, g5 = book_months(res, 5)
    exp5 = expected_hold(W, 5.0, "2014-03-31", [201406, 201407, 201408])
    ck("C04 delisting return counted (June 2014, D at half weight, -90%)",
       abs(r5.get(201406, 9) - exp5[201406]) < 1e-10, "got %.4f want %.4f" % (r5.get(201406, 9), exp5[201406]))
    ck("C04b after delisting: weight kept, no return (July 2014 weight share without return > 0)",
       float(g5[g5.mi == mi_of(2014, 7)].miss.iloc[0]) > 0.02)
    r2, _ = book_months(res, 2)
    n2 = tab[(tab.bk == 2) & (tab.w == "2016-20")].n
    ck("C05 stopped filer: last portfolio held 3 + 3 months, then out (last 2017-08; 20 months in 2016-20)",
       max(r2) == 201708 and len(n2) and int(n2.iloc[0]) == 20, "last %s n %s" % (max(r2), list(n2)))
    r3, _ = book_months(res, 3)
    ck("C06 one missed quarter: last portfolio held 3 more months (2013-06..2013-11 present, 180 months)",
       all(m in r3 for m in (201306, 201307, 201308, 201309, 201310, 201311)) and len(r3) == 180, len(r3))
    r4, _ = book_months(res, 4)
    gap = [201312, 201401, 201402]
    ck("C07 two missed quarters end the spell after the 3 extra months (2013-12..2014-02 absent, 177 months)",
       all(m not in r4 for m in gap) and len(r4) == 177 and 201311 in r4 and 201403 in r4, len(r4))
    fx = fund_expected(W)
    fr = res["frec"]
    g = fr[fr.gid == "G900"]
    got = dict(zip([ym_of(int(x)) for x in g.mi], g.ret))
    ck("C08 share classes combined by start-of-month assets; CRSP -99 assets = missing (exact, 180 months)",
       len(got) == 180 and all(abs(got[m] - fx[m]) < 1e-10 for m in got))
    ft = res["ftab"]
    out_ = ft[ft.bk.isin(["G6100", "G6101", "G6102"]) & ft.grp]
    i3 = inv["I003"]["win"]["2011-25"]
    ck("C09 fund ranks among funds only: planted fund rank share 1; one class stands for the whole fund",
       i3.get("rk") == 1.0 and inv["I003"]["months"] == 180
       and abs(i3["a"] - float(ft[(ft.bk == "G900") & (ft.w == "2011-25")].a.iloc[0])) < 1e-9, i3.get("rk"))
    ck("C09b index, small and non-domestic funds stay out of the fund rank group; style gap excluded 2011-15",
       len(out_) == 0 and not ft[(ft.bk == "G6103") & (ft.w == "2011-15")].grp.any())
    pe = res["peers"]
    ok = True
    for fy in (2010, 2015, 2024):
        ref = ref_groups(W, fy)
        allg = {int(p): int(x) for p, x in zip(res["panel"].perm, pe.G[:, fy - 2010]) if x >= 0}
        ok &= allg == ref
    ck("C10 peer groups: June size (NYSE breakpoints), June book-to-market (ambiguous dates dropped), momentum "
       "to May (3 formation years exact)", ok)
    rng = np.random.default_rng(3)
    X = rng.normal(0, 1, (80, 6))
    y = X @ rng.normal(0, 1, 6) + 0.3 + rng.standard_t(4, 80)
    b, t = load_module(open(MODULE).read(), "eqsc_ref").ols_nw(y, X, 3)
    b2, t2 = nw_reference(y, X, 3)
    ck("C11 Newey-West regression (3 lags) = loop reference", np.allclose(b, b2) and np.allclose(t, t2))
    cand = set(pd.read_csv(os.path.join(fz.data, "eq_sc_cand.csv.gz")).mgrno)
    ck("C12 holdings pulled only for rank-group candidates and library filers (7, 8 out; 1-6, 9, 10 in)",
       not ({7, 8} & cand) and {1, 2, 3, 4, 5, 6, 9, 10} <= cand)
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
    elig = sorted(d["id"] for d in res["inv"] if d["grade"] in "ABF" and d["own_docs"] >= 1 and d["months"] >= 60
                  and not d.get("shares_with"))
    pool_c = sorted(i for i in elig if i not in set(T["record"]) | set(T["explicit"]))
    ctrl = sorted(random.Random(20261117).sample(pool_c, 10)) if len(pool_c) > 10 else pool_c
    sc = [inv[i]["score"] for i in T["record"]]
    ck("C15 tier rule: at most 8 per style, scores descending, explicit places, control by seed 20261117",
       max(styles.values()) == 8 and sc == sorted(sc, reverse=True) and T["control"] == ctrl
       and len(pool_c) > 10 and T["explicit"][0] == "I006" and "I005" not in T["explicit"]
       and len(T["record"]) == 20, "record %d control pool %d" % (len(T["record"]), len(pool_c)))
    ck("C15b explicit places: only role investor with ran_money yes (allocator I054 left out)",
       "I054" not in T["explicit"] and "I054" not in T["record"])
    ck("C16 two investors on one filer, months cut to the frozen years (I024 120, I010 180, I008 145, I004 68)",
       inv["I024"]["months"] == 120 and inv["I010"]["months"] == 180 and inv["I008"]["months"] == 145
       and inv["I004"]["months"] == 68, [inv[k]["months"] for k in ("I024", "I010", "I008", "I004")])
    r3_, r4_ = book_months(res, 3)[0], book_months(res, 4)[0]
    lb = [d for d in res["lib"] if res["lib"][d][0] == "I002"][0]
    rl, _ = book_months(res, lb)
    v34 = {m: float(st[(st.bk == m) & (st.q == 2011 * 4 + 2)].val.iloc[0]) for m in (3, 4)}
    big_ = 3 if v34[3] >= v34[4] else 4
    ck("C16b one filer under two mgrno: per quarter the larger filing (Jan 2012 = that filer's book; 180 months)",
       abs(rl[201201] - (r3_ if big_ == 3 else r4_)[201201]) < 1e-12 and len(rl) == 180, len(rl))
    ex_ = g6[np.isfinite(g6.pa)]
    ck("C17 variants: top-10 = whole book when 10 or fewer positions; no new positions in a constant book",
       np.allclose(ex_.pa, ex_.p10) and g6.pn.isna().all())
    ck("C18 peer-adjusted return leaves out the ETF and the ADR (value share with a peer group < 1)",
       0.3 < float(g6.pash.mean()) < 0.8)
    found = [r[0] for r in sorted(fz.docs, key=lambda r: (-r[1], -r[2], -r[3], r[0]))[:50]]
    ck("C19 foundation list (technique depth, areas, words, document number)", res["found"] == found)
    ck("C20 counts: filers and funds in each rank group", all(c[1] > 40 and c[2] > 30 for c in res["counts"]))
    # alpha = independent OLS of the planted filer's monthly excess return on the six factors of the same month
    ffd = W["ff"].assign(ym=W["ff"].date.str[:4].astype(int) * 100 + W["ff"].date.str[5:7].astype(int)).set_index("ym")
    r1, _ = book_months(res, 1)
    ms = sorted(r1)
    Xf = ffd.loc[ms, ["mktrf", "smb", "hml", "rmw", "cma", "umd"]].to_numpy()
    yf = np.array([r1[m] for m in ms]) - ffd.loc[ms, "rf"].to_numpy()
    bb = np.linalg.lstsq(np.column_stack([np.ones(len(ms)), Xf]), yf, rcond=None)[0]
    ck("C21 six-factor alpha = OLS on the factors of the same month (exact)", abs(1200 * bb[0] - t1.a) < 1e-8,
       "%.6f vs %.6f" % (1200 * bb[0], t1.a))
    msf = W["msf"]
    cap = {(int(p), int(y)): abs(pr) * sh for p, y, pr, sh in zip(msf.permno, msf.yyyymm, msf.mthprc, msf.shrout)}
    okb = True
    for m in (mi_of(2015, 7), mi_of(2015, 12), mi_of(2016, 6)):
        num, den = np.zeros(125), np.zeros(125)
        for p, gq in zip(res["panel"].perm, pe.G[:, 2015 - 2010]):
            if gq < 0:
                continue
            r = W["ret"].get((int(p), ym_of(m)), np.nan)
            wv = cap.get((int(p), ym_of(m - 1)), np.nan)
            if np.isfinite(r) and np.isfinite(wv) and wv > 0:
                num[gq] += wv * r
                den[gq] += wv
        refb = np.where(den > 0, num / np.where(den > 0, den, 1), np.nan)
        modb = pe.B[:, m - mi_of(2009, 6)]
        okb &= np.allclose(np.nan_to_num(refb, nan=9.0), np.nan_to_num(modb, nan=9.0), atol=1e-12)
    ck("C22 peer-group returns value-weighted by the previous month-end market value (exact, 3 months)", okb)
    fw = filings_weights(W, 101)
    qs_ = [q for q in sorted(fw) if 2010 * 4 + 2 <= q <= 2015 * 4 + 2]
    tv = [0.5 * sum(abs(fw[q].get(p, 0) - fw[q - 1].get(p, 0)) for p in set(fw[q]) | set(fw[q - 1]))
          for q in qs_ if q - 1 in qs_]
    t101 = float(tab[(tab.bk == 101) & (tab.w == "2011-15")].to.iloc[0])
    ck("C23 turnover = half the sum of absolute weight changes between consecutive filings, x 4 (exact)",
       abs(4 * np.mean(tv) - t101) < 1e-10, "%.4f vs %.4f" % (4 * np.mean(tv), t101))
    d1 = inv["I001"]
    ck("C24 score = mean of the three rank shares (2011-25, 2021-25, positive blocks)",
       len(d1["comp"]) == 3 and abs(d1["score"] - np.mean(d1["comp"])) < 1e-12 and np.isfinite(d1["bshare"]))
    ck("C25 tie on score broken by more own-words documents (I050 before I051)",
       "I050" in T["record"] and "I051" in T["record"] and T["record"].index("I050") < T["record"].index("I051"))
    l52 = [x for x in rep.split("\n") if x.startswith("  I052 ")]
    ck("C26 a 50-month record prints rank shares only (no statistics)",
       l52 and all(" a " not in x and " rk " in x for x in l52), l52[:1])
    w53 = inv["I053"]["win"].get("2021-25", {})
    ck("C27 a 30-month window has no result (no alpha, no rank share)",
       w53.get("n") == 30 and not np.isfinite(w53.get("a", np.nan)) and not np.isfinite(w53.get("rk", np.nan)),
       w53.get("n"))
    ck("C28 rank group bounds: 180 positions or $80M value are out (filers 9, 10)",
       not tab[tab.bk.isin([9, 10])].grp.any() and len(tab[tab.bk.isin([9, 10])]))
    names_top = {n for _, n, _ in res["top_filers"]}
    kn = {"FILER %03d" % m for m in list(range(1, 7)) + list(range(100, 132)) + [140, 141, 142, 143, 150]}
    tm = {n for _, n, _ in res["top_funds"]}
    ck("C29 best-scored lists leave out every known filer and fund (incl. known-only filer 150 and fund 6005)",
       not (names_top & kn) and "FUND 6005" not in tm and "FUND 6001" not in tm and len(names_top) == 23,
       (sorted(names_top & kn)[:3], len(names_top), sorted(tm)[:12]))
    t13 = tab[tab.bk >= 0]
    okp = all(np.array_equal(p["tbl"], persist_ref(t13, b1, b2)) for b1, b2, p in res["persist"]["13f"]) and \
        all(np.array_equal(p["tbl"], persist_ref(res["ftab"], b1, b2)) for b1, b2, p in res["persist"]["fund"])
    ck("C30 persistence tables (fifths within each block's own set; stopped column) = independent", okp)
    gq = fr[fr.gid == "G900"]
    tq = dict(zip([ym_of(int(x)) for x in gq.mi], gq.tna))
    f5 = W["fret"][W["fret"].crsp_fundno.isin([5001, 5002])]
    tref = f5[f5.mtna > 0].assign(ym=lambda x: x.caldt.str[:4].astype(int) * 100 + x.caldt.str[5:7].astype(int))
    tref = tref.groupby("ym").mtna.sum()
    ck("C31 fund assets: CRSP -99 left out (assets of 2015-03 = the positive class only)",
       all(abs(tq[m] - tref[m]) < 1e-9 for m in tq))
    i23 = inv["I023"]
    ce = combine_expected(W, [6001, 6002])
    li = res["ltab"]
    ck("C32 an investor's two funds are one record combined by previous month-end assets",
       i23["months"] == 180 and abs(i23["win"]["2011-25"]["r"] - 100 * (np.prod([1 + v for v in ce.values()])
                                                                    ** (12 / 180) - 1)) < 1e-9)
    g9 = fr[fr.gid == "G901"]
    ce9 = combine_expected(W, [5011, 5012])
    ck("C33 a share class without a style row is pulled and combined with its fund",
       len(g9) == 180 and all(abs(r - ce9[ym_of(int(m))]) < 1e-12 for m, r in zip(g9.mi, g9.ret)))
    ck("C34 report header carries the code hash computed at run time and the input hash",
       ("code sha256 %s" % fz.code_hash) in rep and "input sha256" in rep and "peer groups:" in rep)
    tier55 = "record" if "I055" in T["record"] else "control" if "I055" in T["control"] else "B"
    ck("C35 an investor sharing another's record takes no place and joins that investor's tier ('with I055')",
       T["with"].get("I056") == (tier55, "I055") and "I056" not in T["record"] + T["control"] + T["explicit"] + T["B"]
       and re.search(r"I056 .* with I055", rep) is not None, T["with"].get("I056"))
    return C


# ================================================================================================== seal
def seal_tests(tmp, libdir, fk, src, modp):
    C = []
    jobs = {n: os.path.join(tmp, n + ".json") for n in ("eq_sc_pull_v1", "eq_scorecard_v1", "eq_sc_cleanup_v1")}
    for n, p in jobs.items():
        ok, msgs, extra = seal_check.check_job(p, [libdir])
        C.append(("S1 %s passes as seal-exempt" % n, ok, msgs[:2]))
    ok, msgs, _ = seal_check.check_job(os.path.join(ROOT, "tools", "wrdsq", "jobs", "eq_precheck_v1.json"), [libdir])
    C.append(("S1b eq_precheck_v1 passes as a non-exempt job", ok, msgs[:2]))
    bad = os.path.join(tmp, "bad_lib")
    os.makedirs(bad, exist_ok=True)
    shutil.copy(os.path.join(libdir, "eq_reader.py"), bad)
    open(os.path.join(bad, "eq_scorecard.py"), "w").write(src.replace("MIN_RESULT, MIN_STATS, NW_LAGS = 36, 60, 3",
                                                                      "MIN_RESULT, MIN_STATS, NW_LAGS = 24, 60, 3"))
    ok, msgs, _ = seal_check.check_job(jobs["eq_scorecard_v1"], [bad])
    C.append(("S2 changed scorecard code is refused (hash)", not ok, msgs[:1]))
    lines = src.splitlines(True)
    i = next(k for k, x in enumerate(lines) if x.startswith(seal_check.INPUT_BEGIN))
    open(os.path.join(bad, "eq_scorecard.py"), "w").write("".join(lines[:i + 1]) + "import os\n" + "".join(lines[i + 1:]))
    ok, msgs, _ = seal_check.check_job(jobs["eq_scorecard_v1"], [bad])
    C.append(("S3 code smuggled into the frozen input block is refused", not ok, msgs[:1]))

    def jobfile(name, steps):
        p = os.path.join(tmp, name + ".json")
        json.dump({"name": name, "steps": steps}, open(p, "w"))
        return p

    def py(code):
        return [{"do": "python", "code": code}]
    open(os.path.join(libdir, "eq_test_ok.py"), "w").write(
        "import eq_reader\n\ndef run(sql, out):\n    d = eq_reader.read(sql, 'crsp.msf_v2', ['permno'], '1990-01', '2010-12')\n"
        "    out(len(d))\n")
    open(os.path.join(libdir, "eq_test_bad.py"), "w").write(
        "def run(sql, out):\n    d = sql('select * from crsp.msf_v2')\n    out(len(d))\n")
    open(os.path.join(libdir, "eq_helper.py"), "w").write(
        "import eq_reader\ndef get(sql):\n    return eq_reader.read(sql, 'crsp.msf_v2', ['permno', 'mthret'], '2011-01', "
        "'2025-12', None, True)\n")
    shadow = os.path.join(tmp, "shadow_lib")
    os.makedirs(shadow, exist_ok=True)
    for f in os.listdir(libdir):
        shutil.copy(os.path.join(libdir, f), shadow)
    open(os.path.join(shadow, "statistics.py"), "w").write(
        "import sys\ndef run():\n    s = sys._getframe(1).f_globals['sql']\n    return s('select mthret from crsp.msf_v2')\n")
    R = "import eq_reader\n"
    cases = [
        ("S4 metadata-only equity job passes", jobfile("eq_meta_v1", [{"do": "describe", "table": "crsp.msf_v2"},
                                                                     {"do": "datasets"}]), True, [libdir]),
        ("S5 reader-only job passes", jobfile("eq_ok_v1", py("import eq_test_ok\neq_test_ok.run(sql, out)")), True,
         [libdir]),
        ("S6 direct sql in a step", jobfile("eq_x1", py("d = sql('select 1')")), False, [libdir]),
        ("S7 direct sql in a lib module", jobfile("eq_x2", py("import eq_test_bad\neq_test_bad.run(sql, out)")),
         False, [libdir]),
        ("S8 pull step", jobfile("eq_x3", [{"do": "pull", "name": "x", "sql": "select 1"}]), False, [libdir]),
        ("S9 keyword exempt= outside an exempt job", jobfile("eq_x4", py(
            R + "d = eq_reader.read(sql, 'tfn.s34', ['mgrno'], '2011-01', '2012-12', exempt=True)")), False,
         [libdir]),
        ("S10 data set read with load()", jobfile("eq_x5", py("d = load('eq_sc_hold_2015')")), False, [libdir]),
        ("S11 os / open / getattr tricks", jobfile("eq_x6", py(
            "import os\nf = open(os.path.join(DATA, 'x'))\ng = getattr(pd, 'read_' + 'csv')")), False, [libdir]),
        ("S12 A1 exempt passed by position in a step", jobfile("eq_a1", py(
            R + "d = eq_reader.read(sql, 'crsp.msf_v2', ['permno', 'mthret'], '2011-01', '2025-12', None, True)")),
         False, [libdir]),
        ("S13 A2 exempt passed by position in a lib module", jobfile("eq_a2", py(
            "import eq_helper\nd = eq_helper.get(sql)\nout(d.mthret.mean())")), False, [libdir]),
        ("S14 A3 changing eq_reader.SEAL_START", jobfile("eq_a3", py(
            R + "eq_reader.SEAL_START['us'] = 999999\nd = eq_reader.read(sql, 'crsp.msf_v2', ['permno'], '2011-01', "
            "'2025-12')")), False, [libdir]),
        ("S15 A4 eq_reader.TABLES.update", jobfile("eq_a4", py(
            R + "eq_reader.TABLES.update({'crsp.msf_v2': ('mthcaldt', 'nowhere')})")), False, [libdir]),
        ("S16 A5 load_ds with a caller-chosen column (old signature)", jobfile("eq_a5", py(
            R + "d = eq_reader.load_ds(load, 'eq_sc_msf_2015', 'mthret', 'us', '1900-01', '2010-12')")), False,
         [libdir]),
        ("S17 A6 same on fund returns", jobfile("eq_a6", py(
            R + "d = eq_reader.load_ds(load, 'eq_sc_fret_2015', 'mtna', 'us', '1900-01', '2010-12')")), False,
         [libdir]),
        ("S18 A7 a lib file shadowing a standard module", jobfile("eq_a7", py(
            "import statistics\nd = statistics.run()\nout(len(d))")), False, [shadow]),
        ("S19 A7b the scorecard job with a shadowing lib file", jobs["eq_scorecard_v1"], False, [shadow]),
        ("S20 A8 a non-eq job reading a scorecard data set", jobfile("tri_peek", py(
            "d = load('eq_sc_msf_2015')\nout(d.mthret.describe())")), False, [libdir]),
        ("S21 A9 exempt-named job with exempt= in a reader call", jobfile("eq_scorecard_v7", py(
            R + "d = eq_reader.read(sql, 'crsp.msf_v2', ['permno'], '2011-01', '2025-12', exempt=True)")), False,
         [libdir]),
        ("S22 A10 exempt-named job printing a module helper's data", jobfile("eq_scorecard_v8", py(
            "import eq_scorecard\nd = eq_scorecard._load_years(load, 'eq_sc_msf', [2015])\nout(d.to_string())")),
         False, [libdir]),
        ("S23 A11 exempt-named job calling a non-registered function", jobfile("eq_scorecard_v9", py(
            "import eq_scorecard\neq_scorecard.candidates(load)")), False, [libdir]),
        ("S24 A12 exempt-named job printing build's return value", jobfile("eq_scorecard_v10", py(
            "import eq_scorecard\nr = eq_scorecard.build(load, save, out, DATA)\nout(r)")), False, [libdir]),
        ("S25 A13 pull functions under the build job's name", jobfile("eq_scorecard_v11", py(
            "import eq_scorecard\neq_scorecard.pull_base(sql, save, out, DATA)")), False, [libdir]),
        ("S26 A14 delete of a scorecard data set in an eq_ job", jobfile("eq_a14", [
            {"do": "delete", "names": ["eq_sc_hold_2015"]}]), False, [libdir]),
        ("S27 dunder attribute (exempt default via __kwdefaults__)", jobfile("eq_a15", py(
            R + "eq_reader.read.__kwdefaults__['exempt'] = True")), False, [libdir]),
        ("S31 R2.1 swapped helpers: pull_crsp(sql, out, out, 0)", jobfile("eq_sc_pull_v2", py(
            "import eq_scorecard\neq_scorecard.pull_crsp(sql, out, out, 0)")), False, [libdir]),
        ("S32 R2.1 swapped helpers: pull_base(sql, out, out, DATA)", jobfile("eq_sc_pull_v3", py(
            "import eq_scorecard\neq_scorecard.pull_base(sql, out, out, DATA)")), False, [libdir]),
        ("S33 R2.1 permuted arguments: pull_base(save, sql, out, DATA, budget=900)", jobfile("eq_sc_pull_v4", py(
            "import eq_scorecard\neq_scorecard.pull_base(save, sql, out, DATA, budget=900)")), False, [libdir]),
        ("S34 R2.1 build(load, out, out, DATA)", jobfile("eq_scorecard_v12", py(
            "import eq_scorecard\neq_scorecard.build(load, out, out, DATA)")), False, [libdir]),
        ("S35 R2.1 report(load, load, 1, 4)", jobfile("eq_scorecard_v13", py(
            "import eq_scorecard\neq_scorecard.report(load, load, 1, 4)")), False, [libdir]),
        ("S36 R2.1 cleanup(out, out) and a trailing newline", jobfile("eq_sc_cleanup_v2", py(
            "import eq_scorecard\neq_scorecard.cleanup(out, out)") + py(
            "import eq_scorecard\neq_scorecard.cleanup(out, DATA)\n")), False, [libdir]),
        ("S37 R2.1 a registered function under another job name (cleanup in the pull job)", jobfile(
            "eq_sc_pull_v5", py("import eq_scorecard\neq_scorecard.cleanup(out, DATA)")), False, [libdir]),
        ("S38 R2.2 C1 count with a value filter (where=)", jobfile("eq_c1", py(
            R + "n = eq_reader.count(sql, 'crsp.msf_v2', '2015-03', '2015-03', where='permno = 10010 and mthret > 0.05')")),
         False, [libdir]),
        ("S39 R2.2 C2 count with the filter passed by position", jobfile("eq_c2", py(
            R + "n = eq_reader.count(sql, 'crsp.msf_v2', '2015-01', '2015-12', 'mthret > 0.05')")), False, [libdir]),
        ("S40 R2.2 C3 count by a mean (per=, keep=)", jobfile("eq_c3", py(
            R + "n = eq_reader.count(sql, 'crsp.msf_v2', '2015-01', '2015-12', per=['permno'], "
            "keep='avg(mthret) > 0.012')")), False, [libdir]),
        ("S41 R2.2 C4 count recovering one holding", jobfile("eq_c4", py(
            R + "n = eq_reader.count(sql, 'tfn.s34', '2015-01', '2015-03', where=\"mgrno = 1 and shares > 100\")")),
         False, [libdir]),
        ("S42 R2.2 C5 count with a computed check name", jobfile("eq_c5", py(
            R + "c = 's34_' + 'manager_quarters'\nn = eq_reader.count(sql, c, '2015-01', '2015-12')")), False,
         [libdir]),
        ("S43 R2.2 C6 count with **options", jobfile("eq_c6", py(
            R + "o = {'where': 'mthret > 0'}\nn = eq_reader.count(sql, 's34_manager_quarters', '2015-01', '2015-12', **o)")),
         False, [libdir]),
        ("S44 a named structure check passes", jobfile("eq_ok_count", py(
            R + "n = eq_reader.count(sql, 's34_no_first_version', '2010-01', '2025-12')\nout(n.n.sum())")), True,
         [libdir]),
        ("S28 the pull job may delete scorecard data sets to pull again", jobfile("eq_sc_pull_v1b", [
            {"do": "delete", "names": ["eq_sc_cand"]}, {"do": "python", "code":
                                                         "import eq_scorecard\neq_scorecard.pull_status(load, out, DATA)"}]),
         True, [libdir]),
    ]
    for name, p, want, libs in cases:
        ok, msgs, _ = seal_check.check_job(p, libs)
        C.append((name + (" passes" if want else " is refused"), ok == want, msgs[:1]))
    for f in ("eq_test_ok.py", "eq_test_bad.py", "eq_helper.py"):
        os.remove(os.path.join(libdir, f))
    # reader at run time
    calls = []

    def fsql(q):
        calls.append(q)
        if "count(*)" in q:
            return pd.DataFrame({"year": [2015], "n": [7]})
        return pd.DataFrame({"permno": [1], "mthcaldt": ["2005-03-31"]})

    def refused(f, exc=eq_reader.SealError):
        try:
            f()
            return False
        except exc:
            return True
    fl = lambda name: pd.DataFrame({"yyyymm": [200906, 201505], "mthret": [0.1, 0.2]})  # noqa: E731
    flf = lambda name: pd.DataFrame({"yyyymm": [200906.0, 201505.0], "mthret": [0.1, 0.2]})  # noqa: E731
    rr = [refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "2009-01", "2011-01")),
          not refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "1990-01", "2010-12")),
          refused(lambda: eq_reader.read(fsql, "comp.g_funda", ["gvkey"], "1985-01", "1990-01")),
          refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "1990-01", "2000-12", where="1=1) or (1=1")),
          refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "1990-01", "2000-12",
                                         where="permno in (select permno from tfn.s34)")),
          not refused(lambda: eq_reader.read(fsql, "tfn.s34", ["mgrno"], "2026-01", "2026-03")),
          refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "2004-01", "2004-12")),
          not refused(lambda: eq_reader.read(fsql, "tfn.s34", ["mgrno"], "2011-01", "2012-12", exempt=True)),
          refused(lambda: eq_reader.read(fsql, "crsp.msf_v2", ["permno"], "2011-01", "2012-12", None, True), TypeError),
          refused(lambda: operator.setitem(eq_reader.SEAL_START, "us", 999999), TypeError),
          refused(lambda: eq_reader.TABLES.update({}), (TypeError, AttributeError)),
          len(eq_reader.load_ds(fl, "eq_sc_msf_2015", "2009-01", "2010-12")) == 1,
          refused(lambda: eq_reader.load_ds(fl, "eq_sc_msf_2015", "2009-01", "2015-12")),
          refused(lambda: eq_reader.load_ds(fl, "eq_sc_cusip", "2009-01", "2010-12")),
          refused(lambda: eq_reader.load_ds(flf, "eq_sc_msf_2015", "2009-01", "2010-12")),
          list(eq_reader.count(fsql, "s34_no_first_version", "2010-01", "2025-12").columns) == ["year", "n"],
          refused(lambda: eq_reader.count(fsql, "tfn.s34", "2010-01", "2025-12")),
          refused(lambda: eq_reader.count(fsql, "s34_manager_quarters", "2015-01", "2015-12", where="mthret > 0"),
                  TypeError),
          refused(lambda: eq_reader.count(fsql, "s34_manager_quarters", "2015-01", "2015-12", "mthret > 0"),
                  TypeError),
          refused(lambda: operator.setitem(eq_reader.CHECKS, "x", ("crsp.msf_v2", ("permno",), "avg(mthret) > 0")),
                  TypeError)]
    C.append(("S29 reader: sealed months refused (US 2011-01.., non-US 1990-01..), injected clauses and rows outside "
              "the range refused, exempt only by keyword, constants read-only, data sets declared with their own "
              "date column, counts only by year", all(rr), rr))
    # build refuses stale or incomplete pulls
    mod2 = load_module(src, "eqsc_stale", modp)
    mod2.INV = [dict(p, fundnos=p["fundnos"] + [6007]) if p["id"] == "I003" else p for p in mod2.INV]
    buf = []
    mod2.build(fk.load, fk.save, lambda *a: buf.append(" ".join(map(str, a))), fk.data)
    st1 = bool(buf) and buf[-1].startswith("build refused") and not mod2.LAST
    p0 = os.path.join(fk.data, "eq_sc_hold_2017.csv.gz")
    os.rename(p0, p0 + ".x")
    mod3 = load_module(src, "eqsc_miss", modp)
    buf = []
    mod3.build(fk.load, fk.save, lambda *a: buf.append(" ".join(map(str, a))), fk.data)
    mod3.pull_status(fk.load, lambda *a: buf.append(" ".join(map(str, a))), fk.data)
    os.rename(p0 + ".x", p0)
    st2 = buf[0].startswith("build refused") and buf[-1].startswith("PULLS NOT COMPLETE") and not mod3.LAST
    C.append(("S30 build refuses pulls made for another investor input, and incomplete pulls", st1 and st2,
              [st1, st2]))
    mod4 = load_module(src.replace('PULL_VERSION = "pull-1"', 'PULL_VERSION = "pull-2"'), "eqsc_ver", modp)
    buf = []
    mod4.build(fk.load, fk.save, lambda *a: buf.append(" ".join(map(str, a))), fk.data)
    st3 = buf[-1].startswith("build refused") and not mod4.LAST
    fm = os.path.join(fk.data, "eq_sc_fmeta.csv.gz")
    os.rename(fm, fm + ".x")
    mod5 = load_module(src, "eqsc_orph", modp)
    buf = []
    mod5.pull_funds(fk.sql, fk.load, fk.save, lambda *a: buf.append(" ".join(map(str, a))), fk.data)
    st4 = any("orphans" in x for x in buf) and not os.path.exists(fm)
    os.rename(fm + ".x", fm)
    C.append(("S45 pull key: a new PULL_VERSION makes old pulls stale; fund years without eq_sc_fmeta are refused",
              st3 and st4, [st3, st4]))
    return C


def cleanup_test(src, modp, fk):
    mod = load_module(src, "eqsc_clean", modp)
    buf = []
    mod.cleanup(lambda *a: buf.append(" ".join(map(str, a))), fk.data)
    left = sorted(f for f in os.listdir(fk.data) if f.startswith("eq_sc_"))
    return [("S46 cleanup deletes every eq_sc_ data set except the report", left == ["eq_sc_report.csv.gz"], left)]


# ============================================================================================== mutations
MUTATIONS = [
    ("look-ahead of one quarter in the holdings",
     "    return d.year * 12 + d.month - 1\n", "    return d.year * 12 + d.month - 1 - 3\n"),
    ("dropped delisting return",
     "        self.R[ri, j] = r\n",
     "        last = msf.groupby('permno').yyyymm.transform('max').to_numpy()\n"
     "        r[(msf.yyyymm.to_numpy() == last) & (last < 202512)] = np.nan\n        self.R[ri, j] = r\n"),
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
EXTRA = [   # the code check's 14 uncaught mutations (SCORECARD_CODE_CHECK.md finding 17), on the current code
    ("factors one month late in the regression", "    j = mi - MI_CRSP\n    if n >= MIN_RESULT:\n",
     "    j = mi - MI_CRSP - 1\n    if n >= MIN_RESULT:\n"),
    ("peer group returns equal-weighted", "            r, w = p.R[:, j], p.C[:, j - 1]\n",
     "            r, w = p.R[:, j], np.ones(p.C.shape[0])\n"),
    ("peer group weights = same-month value", "            r, w = p.R[:, j], p.C[:, j - 1]\n",
     "            r, w = p.R[:, j], p.C[:, j]\n"),
    ("turnover not halved", "            tov.loc[d.index] = 0.5 * d\n", "            tov.loc[d.index] = d\n"),
    ("score part (iii) dropped", '                d["bshare"]]\n', "                np.nan]\n"),
    ("tier ties broken by fewer documents", 'key=lambda p: (-p["score"], -p["own_docs"], p["id"]))',
     'key=lambda p: (-p["score"], p["own_docs"], p["id"]))'),
    ("statistics printed from 48 months", "MIN_RESULT, MIN_STATS, NW_LAGS = 36, 60, 3",
     "MIN_RESULT, MIN_STATS, NW_LAGS = 36, 48, 3"),
    ("result from 24 months", "MIN_RESULT, MIN_STATS, NW_LAGS = 36, 60, 3",
     "MIN_RESULT, MIN_STATS, NW_LAGS = 24, 60, 3"),
    ("rank group positions 5..250", "POS_LO, POS_HI, VAL_MIN = 5, 150, 100e6", "POS_LO, POS_HI, VAL_MIN = 5, 250, 100e6"),
    ("rank group value floor $50M", "POS_LO, POS_HI, VAL_MIN = 5, 150, 100e6", "POS_LO, POS_HI, VAL_MIN = 5, 150, 50e6"),
    ("top-10 not renormalised (equivalent: every average divides by the weight sum)",
     '                s = s.assign(w=s.w / s.groupby("bk").w.transform("sum"))\n', "                pass\n"),
    ("a missing return counted as -100%", "        rr = np.where(miss, 0.0, r)\n", "        rr = np.where(miss, -1.0, r)\n"),
    ("best-scored lists include library filers", "        own_t = tb[~tb.bk.isin(list(exclude))]\n",
     "        own_t = tb\n"),
    ("persistence fifths of block 2 over all filers",
     "        q2 = _quint(t2[both]) if len(both) else pd.Series(dtype=float)\n",
     "        q2 = _quint(t2) if len(both) else pd.Series(dtype=float)\n"),
]
EQUIVALENT = {"top-10 not renormalised (equivalent: every average divides by the weight sum)"}


def run_mutants(table, src, fk, W, modp):
    caught, rows = 0, []
    for name, a, b in table:
        assert src.count(a) == 1, "mutation anchor not unique: %s" % name
        mm = load_module(src.replace(a, b), "eqsc_mut", modp)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                r2, p2, _ = run_pipeline(mm, fk)
            failed = ["build failed"] if r2 is None else [c[0].split()[0] for c in checks(r2, p2, W, fk) if not c[1]]
        except Exception as e:  # noqa: BLE001
            failed = ["error: %s" % type(e).__name__]
        caught += bool(failed)
        rows.append((name, failed))
        print("%-58s | %-16s | %s" % (name[:58], ",".join(failed)[:16] if failed else "-",
                                       "yes" if failed else ("equivalent" if name in EQUIVALENT else "NO")))
    return caught, rows


def main():
    keep = None
    if "--keep" in sys.argv:
        keep = sys.argv[sys.argv.index("--keep") + 1]
    tmp = tempfile.mkdtemp(prefix="eqsc_")
    try:
        W = make_world()
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
        for f in ("eq_scorecard.py", "eq_reader.py", "eq_precheck.py"):
            shutil.copy(os.path.join(ROOT, "tools", "equity", "wrds", f), libdir)
        modp = os.path.join(libdir, "eq_scorecard.py")
        g = subprocess.run([sys.executable, GEN, "--frozen", fzp, "--inventory", invp, "--module", modp, "--job",
                            os.path.join(tmp, "eq_scorecard_v1.json"), "--pull-job",
                            os.path.join(tmp, "eq_sc_pull_v1.json")], capture_output=True, text=True)
        assert g.returncode == 0, g.stderr
        src = open(modp).read()
        assert seal_check.code_hash(src) == seal_check.code_hash(open(MODULE).read())
        data = os.path.join(tmp, "data")
        os.makedirs(data)
        fk = Fake(W, data)
        fk.docs = docs
        fk.code_hash = seal_check.code_hash(src)
        mod = load_module(src, "eq_scorecard", modp)
        res, parts, log = run_pipeline(mod, fk)
        assert res is not None, "\n".join(log)
        assert any(x.startswith("ALL PULLS COMPLETE") for x in log), log[-3:]
        C = checks(res, parts, W, fk)
        S = seal_tests(tmp, libdir, fk, src, modp)
        bad = [c for c in C + S if not c[1]]
        for name, ok, det in C + S:
            print("%-4s %s%s" % ("ok" if ok else "FAIL", name, "" if ok else "  [%s]" % (det,)))
        if keep:
            os.makedirs(keep, exist_ok=True)
            for p in (fzp, invp, modp):
                shutil.copy(p, keep)
            open(os.path.join(keep, "report_invented.txt"), "w").write("\n".join(parts))
        assert not bad, "%d checks failed" % len(bad)
        print("\nplanted error (registration s.11)                          | checks failed    | caught")
        c1, _ = run_mutants(MUTATIONS, src, fk, W, modp)
        print("\nextra mutation (code check, finding 17)                    | checks failed    | caught")
        c2, r2 = run_mutants(EXTRA, src, fk, W, modp)
        missed = [n for n, f in r2 if not f and n not in EQUIVALENT]
        print("catch rate: registration %d of %d; extra %d of %d (%d equivalent, no effect on any number)"
              % (c1, len(MUTATIONS), c2, len(EXTRA), len(EQUIVALENT)))
        assert c1 == len(MUTATIONS) and not missed, missed
        K = cleanup_test(src, modp, fk)
        for name, ok, det in K:
            print("%-4s %s%s" % ("ok" if ok else "FAIL", name, "" if ok else "  [%s]" % (det,)))
        assert all(k[1] for k in K)
        print("eq_scorecard smoke: PASS")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
