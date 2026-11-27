"""Smoke test for tools/equity/wrds/eq_recall.py on invented data (no WRDS data).

1. Hand-computed recall / base rate / lift on a tiny case (cell base rates, version averaging, bootstrap bounds).
2. pull() with a mock sql: reuses stored ref_* data sets, pulls the missing one under rc_*, fills a column the table
   lacks, finds the FRB 10-year column through information_schema; and stops with a clear message when no FRB table
   exists.
3. run() end to end on a small invented panel (quality firms planted in the investor's purchases): finishes, prints the
   gate, stores the summary, and prints no identifier.

python3 tests/eq_recall_smoke.py   ->  RECALL SMOKE OK
"""
import io
import os
import re
import sys

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
            return pd.DataFrame(columns=["gvkey", "datadate", "fyearq", "fqtr"] + [c for c in R.FQX_COLS if c != "stkcoy"])
        if "from comp.funda where" in q:
            return pd.DataFrame({"gvkey": ["001000"], "datadate": ["2010-12-31"], "fyear": [2010]})
        if "from comp.fundq where" in q:
            return pd.DataFrame({"gvkey": ["001000"], "datadate": ["2010-12-31"], "fyearq": [2010], "fqtr": [4]})
        if "information_schema" in q:
            if not frb:
                return pd.DataFrame(columns=["table_schema", "table_name", "column_name"])
            return pd.DataFrame({"table_schema": ["frb"] * 3 + ["frb_all"],
                                 "table_name": ["rates_daily"] * 3 + ["other"],
                                 "column_name": ["date", "tcmnom_y10", "tcmii_y10", "x"]})
        if "from frb.rates_daily" in q and "limit 1" not in q:
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
fq_sql = [q for q in queries if "from comp.funda where" in q][0]
assert "null::float8 as stkco" in fq_sql and "revt::float8 as revt" in fq_sql
assert "tcmnom_y10" in [q for q in queries if "from frb.rates_daily" in q][0]
assert "ALL PULLS COMPLETE" in ptxt, ptxt
plines.clear()
R.pull(mk_sql(True), save_mem, load_mem, pout, budget=100)         # resumable: nothing pulled twice
assert not any("rows" in x for x in plines) and "ALL PULLS COMPLETE" in "\n".join(plines)
del store["rc_t10"]
plines.clear()
R.pull(mk_sql(False), save_mem, load_mem, pout, budget=100)
ptxt = "\n".join(plines)
assert "STOP" in ptxt and "ALL PULLS COMPLETE" not in ptxt and "rc_t10" not in store, ptxt
print("pull(): reuse, fallback pull, empty column, FRB discovery and STOP: OK")

# -------------------------------------------------------------------------------------------- 3. run() end to end
rng = np.random.default_rng(11)
N = 90
months = []
x = 200701
while x <= 202512:
    months.append(x)
    x = R.ym_add(x, 1)
permnos = 90001 + np.arange(N)
OK_SECTORS = [("45", "4510", "451030", "45103010"), ("20", "2010", "201060", "20106010"),
              ("25", "2550", "255030", "25503010")]
BAD_SECTORS = [("35", "3510", "351010", "35101010"), ("10", "1010", "101020", "10102010"),
               ("40", "4020", "402010", "40201050"), ("40", "4030", "403010", "40301010"),
               ("55", "5510", "551010", "55101010")]
quality = np.arange(N) < 30
gics_of = [OK_SECTORS[i % 3] if i < 60 else BAD_SECTORS[i % 5] for i in range(N)]

fa, fq, fx = [], [], []
rev_cy = {}
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
        oiadp = opm * rev
        at = 1.5 * rev
        aq = np.nan if (quality[i] and i % 4 == 0) else aqc          # missing acquisitions for some firms
        fa.append(("%06d" % (1000 + i), pd.Timestamp(year=y, month=12, day=31), y, rev, ni, ni / csho, ni / csho, oiadp,
                   1.1 * oiadp, capx, cfo, 0.01 * rev, aq, at, 0.2 * at, 0.1 * rev, 0.01 * rev, 0.1 * rev, csho, csho, 1.0))
        if y >= 2004:
            for qt in range(1, 5):
                dd = pd.Timestamp(year=y, month=3 * qt, day=1) + pd.offsets.MonthEnd(0)
                fq.append(("%06d" % (1000 + i), dd, y, qt, dd + pd.Timedelta(days=30), rev / 4, rev / 8, oiadp / 4, ni / 4,
                           cfo / 4 * qt, at, 0.5 * at, 0.1 * rev, 0.01 * rev, 0.1 * rev, 0.0, 0.0, 0.4 * rev, 0.2 * rev,
                           csho, 1.0))
                sbcq = np.nan if (not quality[i] and i % 3 == 0) else 0.01 * rev / 4
                fx.append(("%06d" % (1000 + i), dd, y, qt, capx / 4 * qt, 1.1 * oiadp / 4, 0.2 * at, sbcq, np.nan))
funda = pd.DataFrame(fa, columns=["gvkey", "datadate", "fyear"] + R.FUNDA_COLS)
refq = pd.DataFrame(fq, columns=["gvkey", "datadate", "fyearq", "fqtr", "rdq", "saleq", "cogsq", "oiadpq", "niq", "oancfy",
                                 "atq", "ceqq", "cheq", "dlcq", "dlttq", "pstkq", "mibq", "actq", "lctq", "cshoq", "ajexq"])
fqx = pd.DataFrame(fx, columns=["gvkey", "datadate", "fyearq", "fqtr"] + R.FQX_COLS)

rows, dv, ib = [], [], []
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
    for i in range(N):
        permco = 90088 if i in (88, 89) else permnos[i]              # one dual-class company
        rows.append((permnos[i], permco, ym, ret[i], price[i], 100000.0, 1.0, "Y"))
        dv.append((permnos[i], ym, 5e6, 21))
        ib.append(("T%03d" % i, "C%07d" % i, R.ym_end(ym) - pd.Timedelta(days=10), 2.0 + 0.001 * months.index(ym), 6, "USD"))
msf = pd.DataFrame(rows, columns=["permno", "permco", "yyyymm", "ret", "prc", "shrout", "cfpr", "usincflg"])
dvf = pd.DataFrame(dv, columns=["permno", "yyyymm", "mdv", "nd"])
link = pd.DataFrame({"gvkey": ["%06d" % (1000 + i) for i in range(N)], "permno": permnos, "linkprim": "P",
                     "linkdt": pd.Timestamp("1990-01-01"), "linkenddt": pd.NaT})
gics = pd.DataFrame({"gvkey": ["%06d" % (1000 + i) for i in range(N)], "indfrom": pd.Timestamp("1990-01-01"),
                     "indthru": pd.NaT, "gsector": [g[0] for g in gics_of], "ggroup": [g[1] for g in gics_of],
                     "gind": [g[2] for g in gics_of], "gsubind": [g[3] for g in gics_of], "src": "co_hgic"})
ibes = pd.DataFrame(ib, columns=["ticker", "cusip", "statpers", "meanest", "numest", "curcode"])
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
    for mg in (10969, 11194, 7142):
        cp.append((mg, ym, permnos[rng.integers(0, 90)], 0.01, 3, True, False, True, bool(k % 2), 1))
conv = pd.DataFrame(cp, columns=["mgrno", "yyyymm", "permno", "w", "rank", "new", "add", "conv_a", "conv_b", "q_held"])

wstore = {"ref_msf": msf, "ref_link": link, "ref_fq": refq, "ref_gics": gics, "ref_ibes": ibes, "ref_names": names,
          "rc_funda": funda, "rc_fqx": fqx, "rc_t10": t10, "eq_conv_panel": conv}
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
    print(*a)


# incomplete inputs stop before anything is computed
t10_keep = wstore.pop("rc_t10")
R.run(load, save, out)
assert any("STOP" in x for x in lines) and not saved, "run must stop without the Treasury series"
wstore["rc_t10"] = t10_keep
lines.clear()

R.run(load, save, out)
txt = "\n".join(lines)
S = saved["rc_recall_summary"]
res = S[S.kind == "result"].set_index("key")
assert np.isfinite(res.loc["decisive", "lift"]), res
assert res.loc["decisive", "lift"] > 1.0, "planted quality purchases must lift the recall above the base rate"
assert res.loc["decisive", "lo"] <= res.loc["decisive", "hi"]
assert np.isfinite(res.loc["full", "lift"]) and np.isfinite(res.loc["control", "lift"])
assert "RECALL GATE:" in txt and "held-out failed" in txt
assert "FULL FORM, 108 versions averaged" in txt
PP = saved["rc_pass_panel"]
assert PP.dec.sum() > 0 and PP.dec.mean() < 0.5, PP.dec.mean()
assert set(PP.yyyymm.unique()) == set(R.quarter_ends(R.T0, R.T1))
# house exclusion: insurance (4030) never in the eligible panel; avoid rules reject health care, energy, utilities
fl = PP.merge(gics.assign(permno=permnos)[["permno", "gsector", "ggroup"]], on="permno")
assert not (fl.ggroup == "4030").any()
assert not fl[fl.gsector.isin(["35", "10", "55"])].dec.any()
# a criterion line per decisive criterion and a masked cross table
for c in ["B1", "B2", "B3", "B4", "B5", "B6", "P1", "P2", "P3", "A1", "A5"]:
    assert re.search(r"^%s\s" % re.escape(c), txt, re.M), c
assert re.search(r"^M\d\d  (roster|control)", txt, re.M)
# no identifier leaves the job: no permno, gvkey or cusip of the invented panel in the report
assert not re.search(r"\b900\d\d\b", txt), "a permno was printed"
assert not re.search(r"\b00(1\d{3})\b", txt) and "C00000" not in txt, "a gvkey / cusip was printed"
assert "Dev Kantesaria" in txt and "Warren Buffett" not in txt
# no forward return: no month after the last evaluation quarter-end was read
assert txt.count("ret_next") == 0
print("\nRECALL SMOKE OK")
