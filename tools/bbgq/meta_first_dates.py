"""meta_first_dates: the metadata listing of TESTING_PROTOCOL 7.6 step 2 for the free inputs and the LSEG lock (cloud).

"A metadata job at each lock (free inputs, LOCK_v2, any LSEG lock) lists the first date of every series a spec reads
(GS2, TWEXMMTH, ^GSPC monthly and daily, IR3TIB01, the ALFRED first vintages of CPILFESL, M2SL, PCEPILFE, UNRATE, every
LSEG series and contract depth); each rule and market starts at the first month every input exists (specs s7)."
METADATA ONLY: first dates and counts, every loader cut at 2010-12-31 (gm_engine.Cut); no value is printed. The LOCK_v2
part is printed on the PC by the A1 job (tools/bbgq/jobs/gm_a1_v1.py), since the Bloomberg catalog stays on the PC.

python3 tools/bbgq/meta_first_dates.py OUT.txt [LSEG_LOCK.json LSEG_OUT.csv]
"""
import contextlib
import csv
import datetime as dt
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path[:0] = [REPO, os.path.join(HERE, "lib")]

import pandas as pd  # noqa: E402

import gm_engine as GE  # noqa: E402

VERSION = "meta_first_dates-1.0.0"
# series the specs name (7.6 step 2 and the card specs' data sections) that the engine's free loaders do not open today
NAMED = ("GS1", "GS2", "GS5", "GS10", "FEDFUNDS", "BAA", "TB3MS", "TWEXMMTH", "DTWEXBGS", "WALCL", "CPILFESL", "M2SL",
         "PCEPILFE", "UNRATE", "T10YIE", "DFII10", "BAA10YM")
ALFRED = ("CPILFESL", "M2SL", "PCEPILFE", "UNRATE")


def _first(s, daily=False):
    """First date and count of values dated <= 2010-12 (a signal row dated after 2010 is never listed)."""
    s = s.dropna() if s is not None else None
    if s is not None and len(s):
        if isinstance(s.index, pd.PeriodIndex):
            s = s[s.index <= pd.Period("2010-12", "M")]
        else:
            s = s[pd.DatetimeIndex(s.index) <= pd.Timestamp("2010-12-31 23:59")]
    if s is None or not len(s):
        return "-", 0
    i = s.index[0]
    return (str(pd.Timestamp(i).date()) if daily else str(i)), int(len(s))


def free_listing(out):
    M = GE.setup()
    P, G, DL = M["P"], M["G"], M["DL"]
    sink = io.StringIO()
    rows = []
    with GE.Cut(M, "2010-12-31"), contextlib.redirect_stdout(sink):
        R, SRC, FLAG, rf = P.build()
        D = DL.build()
        S = {"E (Economic trend v1)": G.econ_scores(R), "E_sign (Economic trend v2)": G.econ_versions(R, ("sign",))["sign"],
             "C (Carry)": G.carry_values(R), "V (Value v1)": G.value_values(R), "V2 (Value v2)": G.value_v2(R)}
        files = sorted(os.listdir(P.RD))
        for fn in files:
            base, ext = os.path.splitext(fn)
            if ext != ".csv":
                continue
            if fn.startswith("D_"):
                rows.append(("file daily (Yahoo)", fn) + _first(DL._daily_csv(os.path.join(P.RD, fn)), True))
            elif fn.startswith("Y_"):
                rows.append(("file monthly (Yahoo)", fn) + _first(P._csv(os.path.join(P.RD, fn), yahoo=True)))
            elif fn.startswith("S_"):
                rows.append(("file monthly (stooq)", fn) + _first(P._csv(os.path.join(P.RD, fn), stooq=True)))
            elif fn.startswith("cb_") or fn.startswith("oecd_") or fn.startswith("msci_"):
                continue                                  # read below through their own loaders
            else:
                rows.append(("file monthly (FRED / OECD csv)", fn) + _first(P.F(base)))
                if base in ("DGS2", "DGS5", "DGS10", "DGS30", "DFII10", "T10YIE") or base.startswith("DEX"):
                    rows.append(("file daily (FRED)", fn) + _first(DL.fred_daily(base), True))
        for root in ("cl", "ng", "ho", "rb"):
            cv = P.eia_curve(root)
            for c in cv.columns:
                rows.append(("EIA NYMEX contract", "%s%d" % (root, c)) + _first(cv[c]))
        for cc, n in (("DE", 2), ("DE", 10), ("GB", 5), ("GB", 10), ("JP", 2), ("JP", 10), ("CA", 2), ("CA", 10),
                      ("AU", 2), ("AU", 10)):
            rows.append(("central-bank month-end yield", "%s %dy" % (cc, n)) + _first(P.cb_yield(cc, n)))
        for k, name in P.MSCI_NAME.items():
            rows.append(("MSCI manual gross local", "%s (%s)" % (name, k)) + _first(P.msci_gross_local(name)))
        dy = G.equity_dy(0)
        for k in dy.columns:
            rows.append(("12-month dividend yield (lag 0)", k) + _first(dy[k]))
        for cc in sorted(set(v[4] for v in P.FXM.values()) | {"US", "EZ", "DE", "GB", "JP", "CA", "AU"}):
            rows.append(("3-month rate (panel.rate3m)", cc) + _first(P.rate3m(cc)))
        for cc in ("US", "DE", "GB", "FR", "JP", "CA", "AU", "CH", "SE", "NO", "NZ", "KR", "MX", "BR", "ZA", "CN",
                   "IN"):
            rows.append(("CPI y/y (signals.cpi_yoy)", cc) + _first(G.cpi_yoy(cc)))
    have = {os.path.splitext(f)[0] for f in files} | {os.path.splitext(f)[0] for f in os.listdir(P.RAW)
                                                     if os.path.isfile(os.path.join(P.RAW, f))}
    for sid in NAMED:
        tag = "ALFRED first vintage (named in 7.6 step 2)" if sid in ALFRED else "named in a spec"
        if sid in have:
            rows.append((tag, sid) + _first(P.F(sid)))
        else:
            rows.append((tag, sid, "NOT IN THE FREE INPUTS", 0))
    rows.append(("named in 7.6 step 2", "^GSPC monthly (Y__GSPC.csv)") + _first(P.Y("^GSPC")))
    eng = []
    for k in R.columns:
        eng.append(("panel return R", k) + _first(R[k]))
    for k in D.columns:
        eng.append(("daily return D", k) + _first(D[k], True))
    for name, X in S.items():
        for k in X.columns:
            f = _first(X[k])
            if f[1]:
                eng.append(("signal " + name, k) + f)
    del sink
    out("=== metadata listing, free inputs (%s, %s UTC) ===" % (VERSION, dt.datetime.now(dt.timezone.utc)
                                                              .strftime("%Y-%m-%d %H:%M")))
    out("TESTING_PROTOCOL 7.6 step 2. First date with a value (month or day) and count of values up to 2010-12-31; "
        "every loader cut at 2010-12-31; inputs = the repo cache (the gm-1.2.3 reference inputs). No values.")
    out("kind | series | first | count")
    for r in rows + eng:
        out(" | ".join(str(x) for x in r))
    missing = [r[1] for r in rows if r[2] == "NOT IN THE FREE INPUTS"]
    out("NOT IN THE FREE INPUTS (%d): %s" % (len(missing), ", ".join(missing)))
    return rows + eng


def lseg_listing(lock_path, csv_path, out):
    L = json.load(open(lock_path, encoding="utf-8"))
    ser = L["series"]
    out("=== metadata listing, LSEG lock %s (%s, lock id %s) ===" % (L.get("version"), os.path.basename(lock_path),
                                                                     L["lock_id"]))
    out("From the lock's own metadata (lock.json 'series': first design date, last design date, design count); "
        "sealed counts are not listed. Full list: %s" % csv_path)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["per", "series_id", "first_design", "last_design", "n_design"])
        for k in sorted(ser):
            per, sid = k.split("|", 1)
            first, last, nd, _ns = ser[k]
            w.writerow([per, sid, first, last, nd])
    cont, contr = {}, {}
    for k, (first, last, nd, _ns) in ser.items():
        per, sid = k.split("|", 1)
        m = re.match(r"^HP:([A-Z]+)c(\d+)\|", sid)
        if m and nd:
            cont.setdefault((per, m.group(1)), {})[int(m.group(2))] = first
        m = re.match(r"^DS:<([A-Z]+?)([FGHJKMNQUVXZ])(\d)\^(\d)>\|", sid)
        if m and nd:
            d = contr.setdefault((per, m.group(1)), {"n": 0, "first": "9999"})
            d["n"] += 1
            d["first"] = min(d["first"], first)
    out("continuous positions (HistoricalPricing c1..cN): per | root | deepest position with design data | first "
        "date of c1 | first date of the deepest")
    for (per, root), pos in sorted(cont.items()):
        mx = max(pos)
        out("%s | %s | c%d | %s | %s" % (per, root, mx, pos.get(1, "-"), pos[mx]))
    out("contract-level series (Datastream <ROOT MONTH YEAR ^ DECADE>): per | root | contracts with design data | "
        "earliest first date")
    for (per, root), d in sorted(contr.items()):
        out("%s | %s | %d | %s" % (per, root, d["n"], d["first"]))
    out("LSEG series with design data: %d of %d" % (sum(1 for v in ser.values() if v[2]), len(ser)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    lines = []

    def emit(s):
        lines.append(s)
    free_listing(emit)
    if len(sys.argv) >= 4:
        emit("")
        lseg_listing(sys.argv[2], sys.argv[3], emit)
    with open(sys.argv[1], "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(l for l in lines if l.startswith(("===", "NOT IN", "LSEG series"))))
    print("lines written: %d -> %s" % (len(lines), sys.argv[1]))
