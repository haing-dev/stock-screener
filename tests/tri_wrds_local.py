"""Local dry run of tools/wrdsq/lib/tri_wrds.py on an invented world (no WRDS data): a fake sql() answers each pull
with synthetic CRSP / Compustat / 13F / Fama-French tables of the same shape, then run() goes end to end.

    python3 tests/tri_wrds_local.py [N_STOCKS]
"""
import os
import re
import sys
import tempfile
import time

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools", "wrdsq", "lib"))
import tri_wrds as T  # noqa: E402

N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
rng = np.random.default_rng(7)
DAYS = pd.bdate_range("2006-01-02", "2025-12-31")
SPY, IWM = 84398, 88222
PERMS = np.arange(10001, 10001 + N)
ALL = np.r_[PERMS, SPY, IWM]
# daily returns: market + idiosyncratic; a few stocks list late or delist
mkt = rng.normal(0.0003, 0.011, len(DAYS))
R = mkt[:, None] * rng.uniform(0.6, 1.5, len(ALL)) + rng.normal(0, 0.02, (len(DAYS), len(ALL)))
R[:, -2:] = mkt[:, None]
R = np.clip(R, -0.6, 1.0)
start = np.where(rng.random(len(ALL)) < 0.2, rng.integers(0, len(DAYS) // 2, len(ALL)), 0)
stop = np.where(rng.random(len(ALL)) < 0.15, rng.integers(len(DAYS) // 3, len(DAYS), len(ALL)), len(DAYS) - 1)
start[-2:], stop[-2:] = 0, len(DAYS) - 1
stop = np.maximum(stop, start + 300)
PRICE = 20 * np.exp(np.cumsum(np.log1p(R), axis=0))
SHR = rng.uniform(10_000, 300_000, len(ALL))          # thousands
SIC = rng.choice([2834, 3674, 7372, 5812, 3711, 2080, 4911, 6022, 7370, 3841, 5961, 2836], len(ALL))
DAILY = None


def daily():
    global DAILY
    if DAILY is None:
        rows = []
        for j, p in enumerate(ALL):
            idx = np.arange(start[j], stop[j] + 1)
            df = pd.DataFrame({"permno": p, "dlycaldt": DAYS[idx], "dlyprc": PRICE[idx, j], "dlyret": R[idx, j],
                               "dlyretx": R[idx, j], "dlyvol": rng.uniform(5e4, 2e6, len(idx)),
                               "dlydelflg": "N"})
            df.loc[df.index[0], ["dlyret", "dlyretx"]] = np.nan
            if stop[j] < len(DAYS) - 1:
                df.loc[df.index[-1], "dlydelflg"] = "Y"
                df.loc[df.index[-1], "dlyret"] = -0.3
            rows.append(df)
        DAILY = pd.concat(rows, ignore_index=True)
    return DAILY


def arrays(q):
    return [pd.to_datetime(re.findall(r"'(\d{4}-\d{2}-\d{2})'", a)) for a in re.findall(r"ARRAY\[(.*?)\]", q)]


def gvkey(p):
    return "%06d" % (p - 9000)


def fake_sql(q):
    if "distinct dlycaldt" in q:
        return pd.DataFrame({"d": DAYS})
    if "stksecurityinfohist" in q:
        return pd.DataFrame({"permno": [SPY, IWM], "ticker": ["SPY", "IWM"]})
    if "as prc, shrout" in q:
        ds = arrays(q)[0]
        d = daily()
        d = d[d.dlycaldt.isin(ds) & d.permno.isin(PERMS)]
        j = d.permno - 10001
        return pd.DataFrame({"permno": d.permno, "d": d.dlycaldt, "prc": d.dlyprc, "shrout": SHR[j],
                             "siccd": SIC[j], "usincflg": np.where(j % 17 == 0, "N", "Y"), "ticker": "T" + j.astype(str)})
    if "width_bucket" in q:
        te, ts = arrays(q)
        y = int(re.search(r"between '(\d{4})-01-01'", q).group(1))
        d = daily()
        d = d[d.dlycaldt.dt.year == y].copy()
        d["be"] = np.searchsorted(te.values, d.dlycaldt.values, side="right")
        d["bs"] = np.searchsorted(ts.values, d.dlycaldt.values, side="right")
        d["lr"] = np.log(np.maximum(1 + d.dlyret, 1e-4)).fillna(0)
        d["lrx"] = np.log(np.maximum(1 + d.dlyretx, 1e-4)).fillna(0)
        d["dv"] = d.dlyprc * d.dlyvol
        d["dl"] = (d.dlydelflg == "Y").astype(int)
        return d.groupby(["permno", "be", "bs"], as_index=False).agg(
            lr=("lr", "sum"), lrx=("lrx", "sum"), dv=("dv", "sum"), nd=("dv", "size"), **{"del": ("dl", "max")})
    if "ccmxpf_lnkhist" in q:
        return pd.DataFrame({"gvkey": [gvkey(p) for p in PERMS], "permno": PERMS, "linkprim": "P",
                             "linkdt": pd.Timestamp("1990-01-01"), "linkenddt": pd.NaT})
    if "comp.company" in q:
        return pd.DataFrame({"gvkey": [gvkey(p) for p in PERMS], "sic": SIC[:N].astype(str), "loc": "USA", "fic": "USA"})
    if "comp.fundq" in q:
        rows = []
        for p in PERMS:
            base = rng.uniform(50, 3000)
            g = rng.uniform(-0.02, 0.06)
            margin = rng.uniform(-0.05, 0.3)
            for k, dd in enumerate(pd.date_range("2003-03-31", "2025-12-31", freq="QE")):
                s = base * (1 + g) ** k * rng.uniform(0.9, 1.1)
                fq = (dd.month - 1) // 3 + 1
                rows.append({"gvkey": gvkey(p), "datadate": dd, "fyearq": dd.year, "fqtr": fq,
                             "rdq": dd + pd.Timedelta(days=int(rng.integers(20, 60))) if rng.random() > 0.05 else pd.NaT,
                             "saleq": s, "cogsq": s * 0.55, "xsgaq": s * 0.2, "oiadpq": s * margin, "oibdpq": s * (margin + 0.05),
                             "dpq": s * 0.05, "niq": s * margin * 0.7, "oancfy": s * (margin + 0.06) * fq,
                             "capxy": s * 0.04 * fq, "cheq": s * 0.8, "ivltq": np.nan, "dlttq": s * rng.uniform(0, 2),
                             "dlcq": s * 0.1, "curcdq": "USD"})
        return pd.DataFrame(rows)
    if "comp.funda" in q:
        rows = []
        for p in PERMS:
            base = rng.uniform(200, 12000)
            g = rng.uniform(-0.02, 0.15)
            margin = rng.uniform(-0.05, 0.3)
            for k, y in enumerate(range(1994, 2026)):
                s = base * (1 + g) ** k
                rows.append({"gvkey": gvkey(p), "datadate": pd.Timestamp(y, 12, 31), "fyear": y, "sale": s,
                             "cogs": s * 0.55, "xsga": s * 0.2, "oiadp": s * margin, "oibdp": s * (margin + 0.05),
                             "dp": s * 0.05, "ni": s * margin * 0.7, "oancf": s * (margin + 0.06), "capx": s * 0.04,
                             "stkco": s * 0.01, "che": s * 0.3, "ivao": np.nan, "at": s * 1.2, "lct": s * 0.3,
                             "dlc": s * 0.05, "dltt": s * 0.4, "ceq": s * 0.6, "txt": s * margin * 0.2,
                             "pi": s * margin * 0.9, "csho": 100 * (1.01 ** k), "ajex": 1.0, "curcd": "USD"})
        return pd.DataFrame(rows)
    if "with t as" in q:
        rows = []
        for m in range(60):
            held = rng.choice(PERMS, 25, replace=False)
            for rd in pd.date_range("2007-06-30", "2026-03-31", freq="QE"):
                for p in held[:rng.integers(5, 25)]:
                    rows.append({"mgrno": 1000 + m, "rdate": rd, "fdate": rd, "cusip": "C%07d" % p,
                                 "mgrname": ["VANGUARD GROUP INC", "ACME CAPITAL LLC", "BLUE OWL PARTNERS"][m % 3] + str(m),
                                 "w": rng.uniform(0.03, 0.12)})
        return pd.DataFrame(rows)
    if "tfn.s34" in q:
        rows = []
        for m in range(60):
            for rd in pd.date_range("2007-06-30", "2026-03-31", freq="QE"):
                rows.append({"mgrno": 1000 + m, "rdate": rd, "fdate": rd, "val": 5e8 * (1 + m), "npos": 40})
        return pd.DataFrame(rows)
    if "stocknames_v2" in q:
        return pd.DataFrame({"permno": PERMS, "cusip": ["C%07d" % p for p in PERMS],
                             "namedt": pd.Timestamp("1990-01-01"), "nameenddt": pd.Timestamp("2025-12-31")})
    if "fivefactors_monthly" in q:
        ms = pd.date_range("2006-01-01", "2025-12-01", freq="MS")
        f = lambda: rng.normal(0.005, 0.03, len(ms))  # noqa: E731
        return pd.DataFrame({"date": ms, "mktrf": f(), "smb": f(), "hml": f(), "rmw": f(), "cma": f(),
                             "rf": 0.001, "umd": f()})
    raise AssertionError("unexpected SQL: " + q[:200])


def main():
    tmp = tempfile.mkdtemp()

    def save(name, df):
        df.to_csv(os.path.join(tmp, name + ".csv.gz"), index=False)

    def load(name, **kw):
        return pd.read_csv(os.path.join(tmp, name + ".csv.gz"), **kw)

    buf = []

    def out(*a):
        s = " ".join(str(x) for x in a)
        buf.append(s)
        print(s)

    t0 = time.time()
    T.pull(fake_sql, save, out)
    t1 = time.time()
    T.run(load, save, out)
    ev = load("tri_events")
    print("\nLOCAL: pull %.0f s, run %.0f s, %d events saved, calls %s" % (t1 - t0, time.time() - t1, len(ev),
                                                                          ev.call.value_counts().to_dict()))
    assert len(ev) > 0 and set(ev.call) <= {"Buy", "Watch", "Avoid", "TBU"}
    assert ev.c_insider.isna().all() or (ev.c_insider.fillna("") == "").all()
    print("TRI_WRDS LOCAL OK")


if __name__ == "__main__":
    main()
