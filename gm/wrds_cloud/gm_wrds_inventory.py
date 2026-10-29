"""Global Macro Book - WRDS inventory. Saves METADATA ONLY (dataset/table names, date ranges, row counts); no data rows.

Run on WRDS Cloud (compute node):   qrsh   then   python3 gm_wrds_inventory.py
Output: ~/gm_inventory.txt  -> download it and send it to Claude.
Works with Python 3.6+ and the wrds module that WRDS Cloud provides."""
import os
import re
import sys
import time

try:
    import wrds
except ImportError:
    sys.exit("The wrds module is missing. Run:  pip install --user wrds   then run this script again.")

OUT = os.path.expanduser("~/gm_inventory.txt")

# libraries whose table lists we want (macro-relevant vendors); everything else is listed by name only
KEY = re.compile(r"crsp|comp|ibes|cboe|optionm|trace|bond|tr_ds|ds|datastream|refinitiv|lseg|tfn|world|indic|wind|"
                 r"spdj|spgi|snp|macro|mfs|^ff|fama|factor|frb|fed|bank|contrib|public|pastor|beta|wrdsapps|fisd|markit|"
                 r"cftc|fx|commod|futur", re.I)

# key tables: (table, date column for min/max/count or None when the table is too large to scan)
PROBES = [
    ("crsp.msi", "date"), ("crsp.dsi", "date"), ("crsp.tfz_mth_rf", "mcaldt"), ("crsp.tfz_mth_ft", "mcaldt"),
    ("crsp.tfz_mth_cm", "mcaldt"), ("crsp.mcti", "caldt"),
    ("comp.g_idx_mth", "datadate"), ("comp.g_idx_daily", None), ("comp.g_idx_index", None),
    ("comp.g_secd", None), ("comp.g_secm", None), ("comp.g_funda", "datadate"), ("comp.g_fundq", None),
    ("comp.idx_mth", "datadate"),
    ("ibes.statsum_epsus", None), ("ibes.statsum_epsint", None), ("ibes.statsumu_epsus", None),
    ("ibes.statsumu_epsint", None), ("ibes.idsum", None),
    ("cboe.cboe", "date"),
    ("optionm.secprd", None), ("optionm.vsurfd", None),
    ("trace.trace_enhanced", None), ("wrdsapps_bondret.bondret", None), ("wrdsapps.bondret", None),
    ("ff.factors_monthly", "date"), ("ff.factors_daily", "date"),
]


def main():
    t0 = time.time()
    db = wrds.Connection(wrds_username=os.environ.get("USER") or None)
    out = open(OUT, "w")

    def w(s=""):
        out.write(s + "\n")
        out.flush()
        print(s)

    def sql(q):
        try:
            return db.raw_sql(q), None
        except Exception as e:  # noqa: BLE001
            try:
                db.connection.rollback()
            except Exception:  # noqa: BLE001
                pass
            return None, " ".join(str(e).split())[:140]

    w("# Global Macro Book - WRDS inventory (metadata only)")
    w("python %s | wrds module %s | %s" % (sys.version.split()[0], getattr(wrds, "__version__", "?"),
                                           time.strftime("%Y-%m-%d %H:%M")))
    libs = sorted(db.list_libraries())
    w("\n## 1. Libraries you can access (%d)" % len(libs))
    w(", ".join(libs))

    w("\n## 2. Tables in macro-relevant libraries")
    for lib in libs:
        if not KEY.search(lib):
            continue
        try:
            tabs = sorted(db.list_tables(library=lib))
        except Exception as e:  # noqa: BLE001
            w("%s: could not list (%s)" % (lib, " ".join(str(e).split())[:100]))
            continue
        w("%s (%d): %s" % (lib, len(tabs), ", ".join(tabs[:400]) + (" ..." if len(tabs) > 400 else "")))

    w("\n## 3. Key tables: access and date range")
    for tab, dcol in PROBES:
        lib = tab.split(".")[0]
        if lib not in libs:
            w("%-28s library not in subscription" % tab)
            continue
        _, err = sql("select * from %s limit 1" % tab)
        if err:
            w("%-28s NO ACCESS / not found: %s" % (tab, err))
            continue
        if not dcol:
            w("%-28s ok (large table, range not scanned)" % tab)
            continue
        r, err = sql("select min(%s) as a, max(%s) as b, count(*) as n from %s" % (dcol, dcol, tab))
        if err or r is None or not len(r):
            w("%-28s ok (range failed: %s)" % (tab, err))
        else:
            w("%-28s ok  %s .. %s  rows %s" % (tab, r["a"].iloc[0], r["b"].iloc[0], r["n"].iloc[0]))

    w("\n## 4. Columns of the main candidate tables")
    for tab in ("comp.g_idx_mth", "comp.g_idx_index", "ibes.statsum_epsint", "cboe.cboe", "crsp.tfz_mth_ft"):
        lib, name = tab.split(".")
        if lib not in libs:
            continue
        try:
            d = db.describe_table(library=lib, table=name)
            w("%s: %s" % (tab, ", ".join(str(c) for c in d["name"])))
        except Exception:  # noqa: BLE001
            pass

    w("\ndone in %.0f s -> %s" % (time.time() - t0, OUT))
    out.close()
    db.close()


if __name__ == "__main__":
    main()
