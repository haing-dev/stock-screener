"""eq_precheck (runs on WRDS Cloud): structure checks before the scorecard runs (not seal-exempt). Every read goes
through eq_reader: rows only from design months (2001-2010, 1990-2010, 2005-2010), and on sealed months only row
counts by year (named checks of eq_reader.count). Prints counts and one maximum; no data rows.
Job: tools/wrdsq/jobs/eq_precheck_v1.json. Build note: docs/research/equity/SCORECARD_BUILD_NOTE.md section 6."""
import numpy as np
import pandas as pd

import eq_reader


def _ym(s):
    d = pd.to_datetime(s, errors="coerce")
    return (d.dt.year * 100 + d.dt.month).fillna(0).astype("int64")


def delist(sql, out):
    """(i) Does crsp.msf_v2 mthret carry the delisting return? Delistings 2001-2010."""
    d = eq_reader.read(sql, "crsp.stkdelists", ["permno", "delret"], "2001-01", "2010-12")
    m = eq_reader.read(sql, "crsp.msf_v2", ["permno", "mthret", "mthdelflg"], "2001-01", "2010-12")
    d["ym"] = _ym(d.delistingdt)
    m["ym"] = _ym(m.mthcaldt)
    m["has"] = pd.to_numeric(m.mthret, errors="coerce").notna()
    fl = m.mthdelflg.fillna("(null)").astype(str)
    out("(i) msf_v2 2001-2010: %d rows" % len(m))
    for v, g in m.groupby(fl):
        out("    mthdelflg %-6s rows %8d | with mthret %8d | without %7d" % (v[:6], len(g), int(g.has.sum()),
                                                                           int((~g.has).sum())))
    last = m.groupby("permno").ym.max()
    dd = d[pd.to_numeric(d.delret, errors="coerce").notna()].copy()
    dd["delret"] = pd.to_numeric(dd.delret)
    x = dd.merge(m[["permno", "ym", "mthret", "has"]], on=["permno", "ym"], how="left")
    present = x.has.notna()
    out("    stkdelists 2001-2010: %d rows, %d with a delret" % (len(d), len(dd)))
    out("    of those: msf row in the delisting month %d (with mthret %d, without %d), no msf row that month %d"
        % (int(present.sum()), int((x.has == True).sum()), int((x.has == False).sum()), int((~present).sum())))  # noqa: E712
    lm = dd.permno.map(last)
    out("    last msf month = delisting month %d, = month before %d, other or none %d"
        % (int((lm == dd.ym).sum()), int((lm == dd.ym - 1).sum() + (lm == dd.ym - 89).sum()),
           int(len(dd) - (lm == dd.ym).sum() - (lm == dd.ym - 1).sum() - (lm == dd.ym - 89).sum())))
    big = x[present & (x.has == True) & (x.delret.abs() >= 0.3)]  # noqa: E712
    r = pd.to_numeric(big.mthret, errors="coerce")
    out("    delret not reflected (no row or no mthret): %d; of %d with |delret| >= 0.3 and a mthret, sign differs: %d"
        % (int((~present).sum() + (x.has == False).sum()), len(big), int((np.sign(r) != np.sign(big.delret)).sum())))  # noqa: E712


def first_versions(sql, out):
    """(ii) Manager-quarters in tfn.s34 with rows but none with fdate = rdate, per year from 2010 (counts only)."""
    tot = eq_reader.count(sql, "s34_manager_quarters", "2010-01", "2025-12")
    no1 = eq_reader.count(sql, "s34_no_first_version", "2010-01", "2025-12")
    t = tot.merge(no1, on="year", how="left", suffixes=("", "_no")).fillna(0)
    out("(ii) tfn.s34 manager-quarters by year: all | without a first version (fdate = rdate)")
    for y, n, k in zip(t.year, t.n, t.n_no):
        out("    %d %8d %7d" % (int(y), int(n), int(k)))


def factors(sql, out):
    """(iii) Are the factors in decimals? Largest absolute value 1990-2010."""
    f = eq_reader.read(sql, "ff.fivefactors_monthly", ["mktrf", "smb", "hml", "rmw", "cma", "umd", "rf"], "1990-01",
                       "2010-12")
    mx = {c: float(pd.to_numeric(f[c], errors="coerce").abs().max()) for c in ["mktrf", "smb", "hml", "rmw", "cma",
                                                                            "umd", "rf"]}
    out("(iii) ff.fivefactors_monthly 1990-2010: %d months; largest |value|: %s; decimals: %s"
        % (len(f), " ".join("%s %.4f" % (k, v) for k, v in mx.items()), "yes" if mx["mktrf"] < 1 else "NO"))


def ratios(sql, out):
    """(iv) firm_ratio: more than one row per permno and public_date, 2005-2010."""
    r = eq_reader.read(sql, "wrdsapps_finratio.firm_ratio", ["permno", "bm"], "2005-01", "2010-12",
                       where="permno is not null")
    g = r.groupby(["permno", "public_date"]).bm.agg(["size", "nunique"])
    out("(iv) firm_ratio 2005-2010: %d rows, %d permno-dates, %d with more than one row, %d with two different bm"
        % (len(r), len(g), int((g["size"] > 1).sum()), int((g["nunique"] > 1).sum())))
