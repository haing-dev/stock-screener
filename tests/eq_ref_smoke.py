"""Smoke test for tools/equity/wrds/eq_ref.py on invented data (no WRDS data). Builds fake ref_* tables with the pull
schemas, plants signals with known signs, runs eq_ref.run and checks that it finishes, that coverage is high and that
the planted measures show the planted sign. python3 tests/eq_ref_smoke.py"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools", "equity", "wrds"))
import eq_ref  # noqa: E402

rng = np.random.default_rng(7)
N, Y0, Y1 = 700, 2006, 2025
eq_ref.CFG.update(top_n=600, big_n=200, min_dv=1e5)
months = eq_ref.months(Y0 * 100 + 1, Y1 * 100 + 12)
permnos = np.arange(10001, 10001 + N)
quality = rng.normal(size=N)                    # planted: high quality -> higher returns
sectors = rng.choice(["10", "15", "20", "25", "45", "40", "35"], size=N)
ggroup = np.where(sectors == "40", rng.choice(["4010", "4020"], size=N), sectors + "10")
size0 = np.exp(rng.normal(21, 1.2, size=N))

rows, dv = [], []
price = np.full(N, 30.0)
shares = size0 / 30.0 / 1000.0
cf = np.ones(N)
for k, ym in enumerate(months):
    r = 0.006 + 0.004 * quality + rng.normal(0, 0.08, size=N)
    if ym == 202009:
        cf[permnos == 10001] *= 4                # a split for the factor-direction check (permno mapped below)
    price = price * (1 + r)
    for i in range(N):
        rows.append((permnos[i], permnos[i], ym, r[i], max(price[i], 1.0), shares[i], cf[i], "Y"))
        dv.append((permnos[i], ym, 2e6 * (1 + i % 7), 21))
msf = pd.DataFrame(rows, columns=["permno", "permco", "yyyymm", "ret", "prc", "shrout", "cfpr", "usincflg"])
msf.loc[msf.permno == 10001, "permno"] = 14593
msf.loc[msf.permco == 10001, "permco"] = 14593
dvf = pd.DataFrame(dv, columns=["permno", "yyyymm", "mdv", "nd"])
dvf.loc[dvf.permno == 10001, "permno"] = 14593
pmap = {p: (14593 if p == 10001 else p) for p in permnos}

fq = []
for i, p in enumerate(permnos):
    at = 1000.0
    for y in range(Y0 - 3, Y1 + 1):
        for qtr in range(1, 5):
            dd = pd.Timestamp(year=y, month=3 * qtr, day=1) + pd.offsets.MonthEnd(0)
            sale = 250 * (1 + 0.1 * quality[i])
            ni = 10 + 5 * quality[i] + rng.normal(0, 2)
            cfo_q = ni + 3 + 2 * quality[i]
            ytd = cfo_q * qtr
            fq.append(("g%05d" % i, dd, y, qtr, dd + pd.Timedelta(days=30), sale, sale * 0.6, ni * 1.5, ni, ytd, at,
                       400 + 50 * quality[i], 50, 20, 200, 0, 5, 300, 200, 100, 1.0))
            at *= 1.005
fq = pd.DataFrame(fq, columns=["gvkey", "datadate", "fyearq", "fqtr", "rdq", "saleq", "cogsq", "oiadpq", "niq", "oancfy",
                               "atq", "ceqq", "cheq", "dlcq", "dlttq", "pstkq", "mibq", "actq", "lctq", "cshoq", "ajexq"])
link = pd.DataFrame({"gvkey": ["g%05d" % i for i in range(N)], "permno": [pmap[p] for p in permnos], "linkprim": "P",
                     "linkdt": pd.Timestamp("1990-01-01"), "linkenddt": pd.NaT})
gics = pd.DataFrame({"gvkey": ["g%05d" % i for i in range(N)], "indfrom": pd.Timestamp("1990-01-01"), "indthru": pd.NaT,
                     "gsector": sectors, "ggroup": ggroup, "gind": [g + "10" for g in ggroup],
                     "gsubind": [g + "1010" for g in ggroup], "src": "co_hgic"})
ib = []
for i, p in enumerate(permnos):
    e = 2.0
    for ym in months:
        e = e * (1 + 0.01 * quality[i] + rng.normal(0, 0.01))
        d = eq_ref.ym_end(ym) - pd.Timedelta(days=10)
        ib.append(("T%05d" % i, "C%07d" % i, d, e, 8, "USD"))
ibes = pd.DataFrame(ib, columns=["ticker", "cusip", "statpers", "meanest", "numest", "curcode"])
names = pd.DataFrame({"permno": [pmap[p] for p in permnos], "cusip": ["C%07d" % i for i in range(N)],
                      "namedt": pd.Timestamp("1990-01-01"), "nend": pd.Timestamp("2099-12-31")})
ff = pd.DataFrame({"date": [pd.Timestamp(year=m // 100, month=m % 100, day=1) for m in months]})
for c in ("mktrf", "smb", "hml", "rmw", "cma", "umd"):
    ff[c] = rng.normal(0, 0.03, size=len(ff))
ff["rf"] = 0.001

store = {"ref_msf": msf, "ref_link": link, "ref_fq": fq, "ref_gics": gics, "ref_ibes": ibes, "ref_names": names,
         "ref_ff": ff}
for y in range(eq_ref.CFG["y0"] + 1, eq_ref.CFG["y1"] + 1):
    store["ref_dv_%d" % y] = dvf[dvf.yyyymm // 100 == y]
saved = {}
lines = []


def load(n):
    return store[n].copy()


def save(n, df):
    saved[n] = df


def out(*a):
    lines.append(" ".join(str(x) for x in a))
    print(*a)


eq_ref.run(load, save, out)
txt = "\n".join(lines)
S = saved["ref_spreads"]
assert S["roe"].mean() > 0 and S["book"].mean() > 0, "planted quality sign not recovered"
B = saved["ref_series"]
assert len(B) == 192, len(B)
assert B.invested.min() > 0.95, B.invested.min()
assert "direction +1" in txt, "factor direction check"
print("\nSMOKE OK")
