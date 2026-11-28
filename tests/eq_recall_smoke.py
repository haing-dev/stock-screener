"""Smoke test for tools/equity/wrds/eq_recall.py on invented data (no WRDS data).

1. Hand-computed recall / base rate / lift on a tiny case (cell base rates, version averaging, bootstrap bounds).
2. pull() with a mock sql: reuses stored ref_* data sets, pulls the missing one under rc_*, fills a column the table
   lacks, finds the FRB 10-year column through information_schema; and stops with a clear message when no FRB table
   exists.
3. run() end to end on a small invented panel (quality firms planted in the investor's purchases): finishes, prints the
   gate, stores the summary, and prints no identifier.
4. 1.1.0: every recipe runs on the mock and gives finite numbers; kantesaria_v1 is unchanged (its printed sections and
   stored numbers equal eq_recall 1.0.3's on the same mock, 1.0.3 read from git); Sosin is reported as not measured;
   labels ("decisive minus", revision, firm-wide) are printed; the new pulls are reused on a second pull() call.

python3 tests/eq_recall_smoke.py   ->  RECALL SMOKE OK
"""
import io
import os
import re
import subprocess
import sys
import types

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools", "equity", "wrds"))
import eq_recall as R  # noqa: E402


def close(a, b, tol=1e-9):
    return abs(a - b) < tol


# ------------------------------------------------------------------------------------- 1. hand-computed tiny case
E = pd.DataFrame({
    "permno": [1, 2, 3, 4, 5, 6, 1, 2],
    "yyyymm": [201003] * 6 + [201006] * 2,
    "cell": ["A", "A", "A", "A", "B", "B", "C", "C"],
    "x": [True, False, False, False, True, True, True, False],
})
# cell A: 1 of 4 pass (0.25); cell B: 2 of 2 (1.0); cell C: 1 of 2 (0.5)
X = pd.DataFrame({"t": [201003, 201003, 201003, 201006, 201006], "permno": [1, 2, 5, 1, 9]})   # permno 9 not eligible
Y = R.attach(X, E, ["x"])
assert len(Y) == 4, len(Y)
assert list(Y.sort_values(["t", "permno"]).b_x.round(6)) == [0.25, 0.25, 1.0, 0.5]
res = R.summarize({"a": Y}, ["x"], nboot=0, min_n=1)
# recall = (1 + 0 + 1 + 1) / 4 = 0.75; base = (0.25 + 0.25 + 1.0 + 0.5) / 4 = 0.5; lift = 1.5
assert close(res["recall"], 0.75) and close(res["base"], 0.5) and close(res["lift"], 1.5), res
# two version sets: b = only the quarter-1 purchases of cell A -> recall 0.5, base 0.25, lift 2.0; average lift 1.75
Yb = Y[(Y.t == 201003) & (Y.cell == "A")]
res2 = R.summarize({"a": Y, "b": Yb}, ["x"], nboot=500, seed=1, min_n=1)
assert close(res2["recall"], (0.75 + 0.5) / 2) and close(res2["base"], (0.5 + 0.25) / 2), res2
assert close(res2["lift"], (1.5 + 2.0) / 2), res2
assert res2["lo"] <= res2["lift"] <= res2["hi"] + 1e-9 or res2["lo"] <= res2["hi"], res2
# a draw of only quarter 201003 gives a: (1+0+1)/(0.25+0.25+1) = 1.333, b: 2.0; only 201006 gives a 2.0, b undefined
assert res2["quarters"] == 2
# measurability: a set below min_n is left out
res3 = R.summarize({"a": Y}, ["x"], nboot=0, min_n=20)
assert not res3["measurable"]
# bootstrap reproducibility (fixed seed)
r4 = R.summarize({"a": Y, "b": Yb}, ["x"], nboot=500, seed=1, min_n=1)
assert r4["lo"] == res2["lo"] and r4["hi"] == res2["hi"]
print("hand-computed recall / base / lift: OK")

# --------------------------------------------------------------------------------------------------- 2. pull()
store = {}
queries = []


def mk_sql(frb=True):
    def sql(q):
        queries.append(q)
        if "limit 1" in q and "comp.funda " in q + " ":
            return pd.DataFrame(columns=["gvkey", "datadate", "fyear"] + [c for c in R.FUNDA_COLS if c != "stkco"])
        if "limit 1" in q and "comp.fundq" in q:
            return pd.DataFrame(columns=["gvkey", "datadate", "fyearq", "fqtr"] + [c for c in R.FQX_COLS if c != "stkcoy"]
                                + [c for c in R.FQX2_COLS if c != "dvpsxq"])
        if "ibes.statsumu_epsus" in q:   # 1.1.1: unadjusted summary
            if not frb:
                raise RuntimeError("permission denied for table statsumu_epsus")
            if "limit 1" in q:
                return pd.DataFrame(columns=["ticker", "cusip", "statpers", "fpi", "fpedats", "meanest", "numest"])
            assert "fpi in ('1', '2')" in q and "curcode" not in q
            return pd.DataFrame({"ticker": ["T"], "cusip": ["X"], "statpers": ["2010-01-15"], "fpi": ["1"],
                                 "fpedats": ["2010-12-31"], "meanest": [2.0], "numest": [3]})
        if "limit 1" in q and "ibes.statsum_epsus" in q:
            return pd.DataFrame(columns=["ticker", "cusip", "statpers", "fpi", "fpedats", "meanest", "numest", "curcode"])
        if "from ibes.statsum_epsus where" in q:
            assert "fpi in ('0', '1', '2')" in q and "fpedats" in q and "curcode" in q
            return pd.DataFrame({"ticker": ["T"], "cusip": ["X"], "statpers": ["2010-01-15"], "fpi": ["1"],
                                 "fpedats": ["2010-12-31"], "meanest": [1.0], "numest": [3], "curcode": ["USD"]})
        if "from tfn.s34names" in q:
            return pd.DataFrame({"mgrno": [1, 2, 3, 4], "mgrname": ["VANGUARD GROUP INC", "BLACKROCK INC.",
                                                                   "STATE STREET CORP", "OTHER FUND LLC"]})
        if "from tfn.s34 where" in q:
            assert "mgrno in (1,2,3)" in q and "fdate = rdate" in q
            return pd.DataFrame({"rdate": ["2009-09-30"], "cusip": ["X"], "sh": [1e6], "nmgr": [3]})
        if "from comp.funda where" in q:
            return pd.DataFrame({"gvkey": ["001000"], "datadate": ["2010-12-31"], "fyear": [2010]})
        if "from comp.fundq where" in q:
            return pd.DataFrame({"gvkey": ["001000"], "datadate": ["2010-12-31"], "fyearq": [2010], "fqtr": [4]})
        if "information_schema" in q:
            if not frb:
                return pd.DataFrame(columns=["table_schema", "table_name", "column_name"])
            return pd.DataFrame({"table_schema": ["frb"] * 3 + ["frb_all"] + ["frb_all_old"] * 2,
                                 "table_name": ["rates_daily"] * 3 + ["other"] + ["rates_daily"] * 2,
                                 "column_name": ["date", "tcmnom_y10", "tcmii_y10", "x", "date", "tcmnom_y10"]})
        if "from frb_all_old." in q:  # 1.0.2: a listed but unreadable schema (as on WRDS, 2026-11-27)
            raise RuntimeError("permission denied for schema frb_all_old")
        if "from frb.rates_daily" in q and "limit 1" not in q:
            if not frb:
                raise RuntimeError("relation does not exist")
            return pd.DataFrame({"date": ["2009-12-31"], "y10": [3.85]})
        if "frb." in q and "limit 1" in q:
            raise RuntimeError("relation does not exist")
        if "stocknames_v2" in q:
            return pd.DataFrame({"permno": [1], "cusip": ["X"], "namedt": ["2000-01-01"], "nend": ["2099-12-31"]})
        raise AssertionError("unexpected query: " + q[:80])
    return sql


def load_mem(n):
    if n not in store:
        raise KeyError(n)
    return store[n]


def save_mem(n, df):
    store[n] = df


plines = []


def pout(*a):
    plines.append(" ".join(str(x) for x in a))


for b in ["msf", "link", "fq", "gics", "ibes"] + ["dv_%d" % y for y in range(R.CFG["y0"] + 1, R.CFG["y1"] + 1)]:
    store["ref_" + b] = pd.DataFrame({"x": [1]})
R.pull(mk_sql(True), save_mem, load_mem, pout, budget=100)
ptxt = "\n".join(plines)
assert "rc_names" in store and "ref_names" not in store, "missing ref_ data set pulled under rc_"
assert "rc_msf" not in store, "stored ref_msf must be reused"
assert "rc_funda" in store and "rc_fqx" in store and "rc_t10" in store
assert all(n in store for n in R.NEW_SETS), [n for n in R.NEW_SETS if n not in store]
fq_sql = [q for q in queries if "from comp.funda where" in q][0]
assert "null::float8 as stkco" in fq_sql and "revt::float8 as revt" in fq_sql
fx2_sql = [q for q in queries if "from comp.fundq where" in q and "cshfdq" in q][0]
assert "null::float8 as dvpsxq" in fx2_sql and "ppentq::float8 as ppentq" in fx2_sql
assert "index managers 'VANGUARD GROUP': 1 13F ids" in "\n".join(plines)
assert "tcmnom_y10" in [q for q in queries if "from frb.rates_daily" in q][0]
assert "ALL PULLS COMPLETE" in ptxt, ptxt
plines.clear()
nq = len(queries)
R.pull(mk_sql(True), save_mem, load_mem, pout, budget=100)         # resumable: nothing pulled twice (new sets too)
assert not any("rows" in x for x in plines) and "ALL PULLS COMPLETE" in "\n".join(plines)
assert len(queries) == nq, queries[nq:]
del store["rc_t10"]
del store["rc_ibes2u"]                                           # 1.1.1: unreadable -> marker, no stop
plines.clear()
R.pull(mk_sql(False), save_mem, load_mem, pout, budget=100)
ptxt = "\n".join(plines)
assert "public H.15" in ptxt and "ALL PULLS COMPLETE" in ptxt and "rc_t10" in store, ptxt  # 1.0.3: public fallback
pt = store["rc_t10"]
assert pt.src.iloc[0] == "public.fred.dgs10" and len(pt) == 211 and pt.date.iloc[0] == "2008-06-30"
assert pt.date.iloc[-1] == "2025-12-31" and abs(pt.y10.iloc[-1] - 4.18) < 1e-9
assert "FRB table seen" not in ptxt  # no FRB table listed in this mock
assert "statsumu_epsus not readable" in ptxt and "unreadable" in store["rc_ibes2u"].columns, ptxt
print("pull(): reuse, fallback pull, empty column, FRB discovery, public H.15 fallback, 1.1.0 pulls reused: OK")

# -------------------------------------------------------------------------------------------- 3. run() end to end
rng = np.random.default_rng(11)
rng2 = np.random.default_rng(12)            # 1.1.0 inputs (kept apart from the 1.0.x draws)
N = 90
months = []
x = 200701
while x <= 202512:
    months.append(x)
    x = R.ym_add(x, 1)
permnos = 90001 + np.arange(N)
OK_SECTORS = [("45", "4510", "451030", "45103010"), ("20", "2010", "201060", "20106010"),
              ("25", "2550", "255030", "25503010"), ("45", "4530", "453010", "45301020")]
BAD_SECTORS = [("35", "3510", "351010", "35101010"), ("10", "1010", "101020", "10102010"),
               ("40", "4020", "402010", "40201050"), ("40", "4030", "403010", "40301010"),
               ("55", "5510", "551010", "55101010"), ("40", "4010", "401010", "40101010")]
quality = np.arange(N) < 30
gics_of = [OK_SECTORS[i % 4] if i < 60 else BAD_SECTORS[i % 6] for i in range(N)]

fa, fa2, fq, fx, fx2 = [], [], [], [], []
rev_cy, eps_cy = {}, {}
for i in range(N):
    rev = 1000.0
    for y in range(1996, 2026):
        if quality[i]:
            rev = 1000.0 * 1.10 ** (y - 1996) * (1 + rng.normal(0, 0.005))
            ni, opm, capx, cfo, aqc = 0.15 * rev, 0.20 + 0.003 * (y - 1996), 0.01 * rev, 0.22 * rev, 0.0
            csho = 100.0 - 0.5 * (y - 1996)
        else:
            rev = max(50.0, rev * (1 + rng.normal(0.05, 0.2)))
            ni, opm, capx, cfo, aqc = rev * rng.normal(0.03, 0.08), rng.normal(0.08, 0.05), 0.08 * rev, 0.1 * rev, 0.05 * rev
            csho = 100.0
        rev_cy[(i, y)] = rev
        eps_cy[(i, y)] = 0.01 * ni                                   # per share: ni (millions) / 1e8 shares
        oiadp = opm * rev
        at = 1.5 * rev
        aq = np.nan if (quality[i] and i % 4 == 0) else aqc          # missing acquisitions for some firms
        fa.append(("%06d" % (1000 + i), pd.Timestamp(year=y, month=12, day=31), y, rev, ni, ni / csho, ni / csho, oiadp,
                   1.1 * oiadp, capx, cfo, 0.01 * rev, aq, at, 0.2 * at, 0.1 * rev, 0.01 * rev, 0.1 * rev, csho, csho, 1.0))
        fa2.append(("%06d" % (1000 + i), pd.Timestamp(year=y, month=12, day=31), y, 0.6 * rev, 0.0, 0.2 * oiadp,
                    0.9 * oiadp))
        if y >= 2004:
            for qt in range(1, 5):
                dd = pd.Timestamp(year=y, month=3 * qt, day=1) + pd.offsets.MonthEnd(0)
                fq.append(("%06d" % (1000 + i), dd, y, qt, dd + pd.Timedelta(days=30), rev / 4, rev / 8, oiadp / 4, ni / 4,
                           cfo / 4 * qt, at, 0.5 * at, 0.1 * rev, 0.01 * rev, 0.1 * rev, 0.0, 0.0, 0.4 * rev, 0.2 * rev,
                           csho, 1.0))
                sbcq = np.nan if (not quality[i] and i % 3 == 0) else 0.01 * rev / 4
                fx.append(("%06d" % (1000 + i), dd, y, qt, capx / 4 * qt, 1.1 * oiadp / 4, 0.2 * at, sbcq, np.nan))
                fx2.append(("%06d" % (1000 + i), dd, y, qt, csho * (1 + rng2.normal(0, 0.002)), 0.3 * rev,
                            np.nan if i % 2 else 0.0005 * rev / csho))
funda = pd.DataFrame(fa, columns=["gvkey", "datadate", "fyear"] + R.FUNDA_COLS)
funda2 = pd.DataFrame(fa2, columns=["gvkey", "datadate", "fyear"] + R.FUNDA2_COLS)
refq = pd.DataFrame(fq, columns=["gvkey", "datadate", "fyearq", "fqtr", "rdq", "saleq", "cogsq", "oiadpq", "niq", "oancfy",
                                 "atq", "ceqq", "cheq", "dlcq", "dlttq", "pstkq", "mibq", "actq", "lctq", "cshoq", "ajexq"])
fqx = pd.DataFrame(fx, columns=["gvkey", "datadate", "fyearq", "fqtr"] + R.FQX_COLS)
fqx2 = pd.DataFrame(fx2, columns=["gvkey", "datadate", "fyearq", "fqtr"] + R.FQX2_COLS)

rows, dv, ib, ib2, idx = [], [], [], [], []
z = np.zeros(N)
price = np.full(N, 30.0)
prev = None
for ym in months:
    z = z + rng.normal(0, 0.05, size=N)
    yr = ym // 100
    newp = np.where(quality, np.array([0.015 * rev_cy[(i, yr)] for i in range(N)]) * np.exp(z),
                    np.maximum(6.0, price * (1 + rng.normal(0.005, 0.08, size=N))))
    ret = newp / price - 1 if prev is not None else np.zeros(N)
    price = newp
    prev = ym
    st = R.ym_end(ym) - pd.Timedelta(days=10)
    for i in range(N):
        permco = 90088 if i in (88, 89) else permnos[i]              # one dual-class company
        rows.append((permnos[i], permco, ym, ret[i], price[i], 100000.0, 1.0, "Y"))
        dv.append((permnos[i], ym, 5e6, 21))
        ib.append(("T%03d" % i, "C%07d" % i, st, 2.0 + 0.001 * months.index(ym), 6, "USD"))
        e = eps_cy[(i, yr)] * (1 + rng2.normal(0, 0.05))
        fpe = pd.Timestamp(year=yr, month=12, day=31)
        ib2.append(("T%03d" % i, "C%07d" % i, st, "1", fpe, e, int(rng2.integers(1, 15)), "USD"))
        ib2.append(("T%03d" % i, "C%07d" % i, st, "2", fpe + pd.offsets.YearEnd(1), 1.1 * e, 5, "USD"))
        ib2.append(("T%03d" % i, "C%07d" % i, st, "0", pd.NaT, 6.0 + 6 * rng2.random(), 4, "USD"))
        if ym % 100 in (3, 6, 9, 12) and R.IDX0 <= R.ym_end(ym).strftime("%Y-%m-%d") <= R.IDX1:
            idx.append((R.ym_end(ym), "C%07d" % i, 1e8 * (0.05 + 0.2 * rng2.random()), 3))
msf = pd.DataFrame(rows, columns=["permno", "permco", "yyyymm", "ret", "prc", "shrout", "cfpr", "usincflg"])
dvf = pd.DataFrame(dv, columns=["permno", "yyyymm", "mdv", "nd"])
link = pd.DataFrame({"gvkey": ["%06d" % (1000 + i) for i in range(N)], "permno": permnos, "linkprim": "P",
                     "linkdt": pd.Timestamp("1990-01-01"), "linkenddt": pd.NaT})
gics = pd.DataFrame({"gvkey": ["%06d" % (1000 + i) for i in range(N)], "indfrom": pd.Timestamp("1990-01-01"),
                     "indthru": pd.NaT, "gsector": [g[0] for g in gics_of], "ggroup": [g[1] for g in gics_of],
                     "gind": [g[2] for g in gics_of], "gsubind": [g[3] for g in gics_of], "src": "co_hgic"})
ibes = pd.DataFrame(ib, columns=["ticker", "cusip", "statpers", "meanest", "numest", "curcode"])
ibes2 = pd.DataFrame(ib2, columns=["ticker", "cusip", "statpers", "fpi", "fpedats", "meanest", "numest", "curcode"])
idxf = pd.DataFrame(idx, columns=["rdate", "cusip", "sh", "nmgr"])
names = pd.DataFrame({"permno": permnos, "cusip": ["C%07d" % i for i in range(N)], "namedt": pd.Timestamp("1990-01-01"),
                      "nend": pd.Timestamp("2099-12-31")})
t10 = pd.DataFrame({"date": [R.ym_end(m) for m in months if m >= 200806], "y10": 3.0, "src": "frb.rates_daily.tcmnom_y10"})

cp = []
qends = [m for m in months if m % 100 in (3, 6, 9, 12) and m >= 200912]
for k, ym in enumerate(qends):
    cp.append((14460, ym, permnos[(k * 7) % 30], 0.1, 1, True, False, True, True, 1))             # quality: a and b
    cp.append((14460, ym, permnos[30 + (k * 5) % 30], 0.02, 8, True, False, False, True, 1))      # noisy: b only
    for mg in (8350, 9442):
        for j in range(3):
            p = permnos[rng.integers(0, 60)]
            cp.append((mg, ym, p, 0.03, j + 1, True, False, bool(j < 2), True, 1))
    cp.append((10969, ym, permnos[rng.integers(0, 90)], 0.01, 3, True, False, True, bool(k % 2), 1))
CPCOLS = ["mgrno", "yyyymm", "permno", "w", "rank", "new", "add", "conv_a", "conv_b", "q_held"]

wstore = {"ref_msf": msf, "ref_link": link, "ref_fq": refq, "ref_gics": gics, "ref_ibes": ibes, "ref_names": names,
          "rc_funda": funda, "rc_fqx": fqx, "rc_t10": t10, "rc_fqx2": fqx2, "rc_funda2": funda2, "rc_ibes2": ibes2,
          "rc_idx": idxf, "rc_ibes2u": ibes2[ibes2.fpi != "0"].drop(columns=["curcode"]),
          "eq_conv_panel": pd.DataFrame(cp, columns=CPCOLS)}
for y in range(R.CFG["y0"] + 1, R.CFG["y1"] + 1):
    wstore["ref_dv_%d" % y] = dvf[dvf.yyyymm // 100 == y]
saved = {}
lines = []


def load(n):
    """as on WRDS: data sets are stored as CSV and read back (keys and dates come back as numbers / text)"""
    buf = io.StringIO()
    wstore[n].to_csv(buf, index=False)
    buf.seek(0)
    return pd.read_csv(buf)


def save(n, df):
    saved[n] = df


def out(*a):
    lines.append(" ".join(str(v) for v in a))


def quiet(*a):
    pass


# purchases of the other targets: passers of their own decisive recipe (so every lift is defined) plus eligible
# stocks drawn at random
Dm = R.load_inputs(load)
um, msfm, sm, _ = R.build_panel(Dm, quiet)
Em = R.recall_panel(Dm, um, msfm, sm, quiet)
for tg in R.TARGETS[2:]:
    rec = R.RECIPES[tg["recipe"]]
    if not rec.get("measured", True):
        continue
    P = R.recipe_set(Em, rec)
    d = rec["entry"](rec["flags"](P))
    assert d.sum() > 0, "no passer of %s on the mock" % tg["recipe"]
    pas = P[d].drop_duplicates("yyyymm").sample(frac=1.0, random_state=1).head(25)
    oth = P[~d].sample(n=25, random_state=2)
    for j, (_, rw) in enumerate(pd.concat([pas, oth]).iterrows()):
        cp.append((int(tg["mgrnos"][0]), R.ym_add(int(rw.yyyymm), 3), int(rw.permno), 0.05, 1, True, False, True,
                   True, 1))
wstore["eq_conv_panel"] = pd.DataFrame(cp, columns=CPCOLS)

# incomplete inputs stop before anything is computed
t10_keep = wstore.pop("rc_t10")
R.run(load, save, out)
assert any("STOP" in x for x in lines) and not saved, "run must stop without the Treasury series"
wstore["rc_t10"] = t10_keep
idx_keep = wstore.pop("rc_idx")
lines.clear()
R.run(load, save, out)
assert any("PULLS INCOMPLETE (rc_idx)" in x for x in lines) and not saved, "run must stop without a 1.1.0 pull"
wstore["rc_idx"] = idx_keep
lines.clear()

R.run(load, save, out)
txt = "\n".join(lines)
print(txt[txt.index("# Summary"):])
S = saved["rc_recall_summary_v11"]
res = S[(S.kind == "result") & (S.recipe == "kantesaria_v1")].set_index("key")
assert np.isfinite(res.loc["decisive", "lift"]), res
assert res.loc["decisive", "lift"] > 1.0, "planted quality purchases must lift the recall above the base rate"
assert res.loc["decisive", "lo"] <= res.loc["decisive", "hi"]
assert np.isfinite(res.loc["full", "lift"]) and np.isfinite(res.loc["control", "lift"])
assert "RECALL GATE:" in txt and "held-out failed" in txt
assert "FULL FORM, 108 versions averaged" in txt and "FULL FORM, 1296 versions averaged" in txt
PP = saved["rc_pass_kantesaria_v1"]
assert PP.dec.sum() > 0 and PP.dec.mean() < 0.5, PP.dec.mean()
assert set(PP.yyyymm.unique()) == set(R.quarter_ends(R.T0, R.T1))
# house exclusion: insurance (4030) never in the house panel; avoid rules reject health care, energy, utilities
fl = PP.merge(gics.assign(permno=permnos)[["permno", "gsector", "ggroup"]], on="permno")
assert not (fl.ggroup == "4030").any()
assert not fl[fl.gsector.isin(["35", "10", "55"])].dec.any()
# recipes with house exclusions off see the excluded industries (Pilecki: banks and insurers)
PL = saved["rc_pass_pilecki_v1"].merge(gics.assign(permno=permnos)[["permno", "ggroup"]], on="permno")
assert (PL.ggroup == "4030").any() and (PL.ggroup == "4010").any()
assert PL[~PL.ggroup.isin(["4010", "4020", "4030"])].dec.sum() == 0, "Pilecki A1: financials only"
# every measured recipe gives finite numbers
for tg in R.TARGETS:
    rr = S[(S.kind == "result") & (S.recipe == tg["recipe"]) & (S.key == "decisive")]
    if not R.RECIPES[tg["recipe"]].get("measured", True):
        assert not len(rr)
        continue
    assert len(rr) == 1, tg["recipe"]
    for c in ("recall", "base", "lift", "lo", "hi"):
        assert np.isfinite(rr[c].iloc[0]), (tg["recipe"], c, rr)
    assert ("# %s: recipe %s" % (tg["name"], tg["recipe"])) in txt
    for c, _, _ in R.RECIPES[tg["recipe"]]["criteria"]:
        assert re.search(r"^%s\s" % re.escape(c), txt, re.M), (tg["recipe"], c)
assert "Sosin: not in eq_conv_panel (13F filer to be added by an eq_conv input change); not measured" in txt
assert "21801" not in txt, "no filer number printed (1.1.1, S4)"
# labels on the blocks
blk = {}
for tg in R.TARGETS:
    a = txt.index("# %s: recipe %s" % (tg["name"], tg["recipe"]))
    b = txt.find("\n# ", a + 3)
    blk[tg["recipe"]] = txt[a:b if b > 0 else None]
assert blk["pilecki_v1"].count("decisive minus B4") >= 7, "label on every section of the Pilecki block"
assert blk["kantesaria_v2"].count("revision after seeing recall v1: same 29 purchases, not independent evidence") >= 7
assert "13F = equity longs only" in blk["druckenmiller_v1"] and "financials only" in blk["pilecki_v1"]
assert "long/short, longs only tested" in blk["zlatev_v1"]
assert "firm-wide" in blk["stahl_v1"] and "firm-wide" in blk["nygren_v1"]
assert "no PRICE criterion in the decisive form" in blk["stahl_v1"] and "no PRICE criterion" in blk["druckenmiller_v1"]
assert "FULL FORM: not implemented" in blk["druckenmiller_v1"]
# 1.1.1: S1 basis line, S2 reference share line, S3 fallback count, N1 house-set line, N5 managers line
assert "I/B/E/S basis of price / estimate criteria (ZLA P1, NYG P4): unadjusted" in txt
assert "provisional (split basis)" not in txt
for k_ in ("pilecki_v1", "nygren_v1", "lilu_v1", "hohn_v1"):
    assert "counted purchases without a reference-book score:" in blk[k_], k_
assert "counted purchases without a reference-book score" not in blk["kantesaria_v1"]
assert re.search(r"comparison-group fallback .*: \d+ of \d+ financial stock-quarters", blk["pilecki_v1"])
assert "decisive on the house set (reported)" in blk["lilu_v1"] and "decisive on the house set" not in blk["hohn_v1"]
assert "index managers found per 13F quarter-end: median 3" in txt
PR = saved["rc_pass_pilecki_v1"].merge(gics.assign(permno=permnos)[["permno", "ggroup"]], on="permno")
assert PR.ref[PR.ggroup.isin(["4010", "4030"])].any(), "S2: banks / insurers get a reference score on the own set"
LL = saved["rc_pass_lilu_v1"].merge(gics.assign(permno=permnos)[["permno", "ggroup"]], on="permno")
assert (LL.ggroup == "4030").any(), "N1: Li Lu on his own set"
assert not re.search(r"^labels: ", blk["kantesaria_v1"].split("## 1.")[1], re.M), "kantesaria_v1 keeps the v1 layout"
assert re.search(r"^Li Lu\s+lilu_v1", txt, re.M) and re.search(r"^Cliff Sosin\s+sosin_v1 .*NOT MEASURED", txt, re.M)
# a masked cross table
assert re.search(r"^M\d\d  (roster|control)", txt, re.M)
# no identifier leaves the job: no permno, gvkey or cusip of the invented panel in the report
assert not re.search(r"\b900\d\d\b", txt), "a permno was printed"
assert not re.search(r"\b00(1\d{3})\b", txt) and "C00000" not in txt, "a gvkey / cusip was printed"
assert "Dev Kantesaria" in txt and "Warren Buffett" not in txt
# no forward return: no month after the last evaluation quarter-end was read
assert txt.count("ret_next") == 0
print("1.1.0 recipes on the mock: finite numbers, labels, Sosin skipped: OK")

# ---------------------------------------------------------------- 4. kantesaria_v1 unchanged against eq_recall 1.0.3
OLD_COMMIT = "b51b62377a7d8527ca2b228b382c59b9d6118e18"      # last commit of eq_recall 1.0.3
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
try:
    src = subprocess.run(["git", "-C", root, "show", OLD_COMMIT + ":tools/equity/wrds/eq_recall.py"], check=True,
                         capture_output=True, text=True).stdout
except Exception as e:  # noqa: BLE001
    src = None
    print("WARNING: eq_recall 1.0.3 not readable from git (%s): identity check against 1.0.3 skipped" % str(e)[:80])
if src is not None:
    assert 'VERSION = "eq_recall-1.0.3"' in src
    old = types.ModuleType("eq_recall_103")
    exec(compile(src, "eq_recall_103", "exec"), old.__dict__)
    saved_old, lines_old = {}, []
    old.run(load, lambda n, df: saved_old.__setitem__(n, df), lambda *a: lines_old.append(" ".join(str(v) for v in a)))
    to = "\n".join(lines_old)

    def sections(s, start, stop):
        a = s.index(start)
        return s[a:s.index(stop, a) + len(stop)]
    so = sections(to, "## 1. Eligible universe", "CONTROL pooled")
    sn = sections(blk["kantesaria_v1"], "## 1. Eligible universe", "CONTROL pooled")
    assert so == sn, "kantesaria_v1 printed sections differ from 1.0.3"
    A = saved_old["rc_recall_summary"].reset_index(drop=True)
    B = S[S.recipe == "kantesaria_v1"].drop(columns=["recipe"]).reset_index(drop=True)[list(A.columns)]
    assert A.shape == B.shape, (A.shape, B.shape)
    for c in A.columns:
        if not pd.api.types.is_numeric_dtype(A[c]):
            assert (A[c].astype(object).fillna("").astype(str) == B[c].astype(object).fillna("").astype(str)).all(), c
        else:
            assert np.array_equal(A[c].to_numpy(float), B[c].to_numpy(float), equal_nan=True), c
    po, pn = saved_old["rc_pass_panel"].reset_index(drop=True), saved["rc_pass_kantesaria_v1"].reset_index(drop=True)
    assert po.equals(pn[list(po.columns)]), "pass panel differs from 1.0.3"
    print("kantesaria_v1 identical to eq_recall 1.0.3 on the mock (%d section lines, %d summary rows, pass panel %d rows): OK"
          % (so.count("\n") + 1, len(A), len(po)))
# ---------------------------------------------------------------- 5. 1.1.1: unadjusted I/B/E/S unreadable -> provisional
keep_u = wstore["rc_ibes2u"]
wstore["rc_ibes2u"] = pd.DataFrame({"unreadable": [1]})
lines.clear()
saved.clear()
R.run(load, save, out)
txt2 = "\n".join(lines)
wstore["rc_ibes2u"] = keep_u
assert "RECALL GATE" in txt2 and "I/B/E/S basis of price / estimate criteria (ZLA P1, NYG P4): provisional" in txt2
for rc_, lab_ in (("zlatev_v1", "P1 provisional (split basis)"), ("nygren_v1", "P4 provisional (split basis)")):
    a = txt2.index("recipe %s" % rc_)
    b = txt2.find("\n# ", a)
    assert txt2[a:b].count(lab_) >= 7, rc_
assert txt2.count("provisional (split basis)") == txt2[txt2.index("recipe zlatev_v1"):].count("provisional (split basis)")
print("1.1.1: unreadable unadjusted I/B/E/S -> labelled provisional, no stop: OK")
print("\nRECALL SMOKE OK")
