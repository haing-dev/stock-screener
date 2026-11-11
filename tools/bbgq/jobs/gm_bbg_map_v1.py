"""gm_bbg_map_v1: which Bloomberg series the book engine would use, market by market (WORKFLOW v2.1 step 0.5, adapter).
For every market of gm/ and every engine input that gm/bloomberg.py can take from Bloomberg (commodity excess-return
index, commodity curve front and farthest contract for carry, MSCI valuation fields for the equity value composite;
growth surprises are listed but switched off in BASE and CANDIDATE): the series id bbg_panel would serve, whether it is
present and usable in the current lock (status, file|sheet of the copy, first design month, design months, months served
as of 2010-12-31, whether gm's own minimum is met), and what stays on free data. Also a dry run of the adapter: the
gm workbook dict it builds (counts only). METADATA ONLY: names, statuses, months, counts. No data value."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import time  # noqa: E402
import traceback  # noqa: E402
from collections import Counter  # noqa: E402

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
print("=== gm_bbg_map_v1 ===")
try:
    import bbgdata
    import bbg_panel as BP
    P = bbgdata.Panel(WORK)
    print("bbgdata %s | bbg_panel %s | lock id %s" % (bbgdata.VERSION, BP.VERSION, P.lock_id))
except Exception as e:  # noqa: BLE001
    print("LOAD FAILED", type(e).__name__, str(e)[:300])
    print("=== END === %.0fs" % (time.time() - T0))
    sys.exit(0)

try:
    rows, src = BP.engine_map(P)
    print("--- per market and input (route | series id | status and copy | first design month | design months | "
          "months served as of %s | gm uses it)" % src.asof_date.date())
    last = None
    for r in rows:
        if r["market"] != last:
            last = r["market"]
            print("MARKET %s" % last)
        if r["route"] == "Bloomberg":
            print("   %s | Bloomberg | %s | %s | %s | %d | %d | %s" % (
                r["input"], r["sid"], r["status"], r["first"], r["n"], r["served"],
                r.get("used_note") or ("yes" if r["used"] else "no")))
        else:
            print("   %s | %s" % (r["input"], r["route"]))
    # summary per input type
    print("--- summary (Bloomberg inputs)")
    by = {}
    for r in rows:
        if r["route"] != "Bloomberg":
            continue
        st = "used" if r["used"] else r.get("used_note") or ("held back" if r["status"].startswith("held back") else
                                       ("present, too short" if r["status"].startswith("ok") else
                                        "missing or failed (%s)" % r["status"]))
        by.setdefault(r["input"], Counter())[st] += 1
    for inp, c in sorted(by.items()):
        print("SUMMARY %s | %s" % (inp, ", ".join("%s %d" % kv for kv in sorted(c.items()))))
    mk = {}
    for r in rows:
        if r["route"] == "Bloomberg" and not r["market"].startswith("country"):
            mk.setdefault(r["market"], []).append(r["used"])
    ret_used = {r["market"] for r in rows if r["input"] == "return" and r["used"]}
    car_used = {}
    for r in rows:
        if r["route"] == "Bloomberg" and r["input"].startswith("carry"):
            car_used.setdefault(r["market"], []).append(r["used"])
    val_used = {r["market"] for r in rows if r["input"] == "value composite" and r["used"]}
    print("markets whose RETURN would come from Bloomberg: %d (%s)" % (len(ret_used), ", ".join(sorted(ret_used))))
    cu = sorted(m for m, v in car_used.items() if all(v))
    print("markets whose CARRY would come from Bloomberg curves: %d (%s)" % (len(cu), ", ".join(cu)))
    print("equity markets in the Bloomberg VALUE composite: %d (%s)" % (len(val_used), ", ".join(sorted(val_used))))
    free_only = sorted({r["market"] for r in rows if not r["market"].startswith("country")} - set(
        m for m, v in mk.items() if any(v)))
    alt = set(BP.gm_maps()[0].ALT_COMMOD)
    fo = [m for m in free_only if m not in alt]
    ao = [m for m in free_only if m in alt]
    print("markets entirely on free data: %d (%s)" % (len(fo), ", ".join(fo)))
    print("alternative commodities without a usable Bloomberg return (not in the book; held back = untouched): %d (%s)"
          % (len(ao), ", ".join(ao)))
    for n in BP.gm_mapping_notes():
        print("NOTE", n)
except Exception as e:  # noqa: BLE001
    print("MAP FAILED", type(e).__name__, str(e)[:300])
    print("".join(traceback.format_exc().splitlines(True)[-8:]))

# ---- dry run of the adapter: the gm workbook dict (counts only)
try:
    wb = src.workbook()
    print("--- adapter dry run: gm.bloomberg workbook dict as of %s (econ dating: %s)" % (src.asof_date.date(),
                                                                                         src.econ_dating))
    for sheet in BP.SHEETS:
        b = wb.get(sheet, {})
        n_univ = len(src.universe.get(sheet, []))
        months = [len(df) for df in b.values()]
        firsts = sorted(str(df.index[0]) for df in b.values() if len(df))
        lasts = sorted(str(df.index[-1]) for df in b.values() if len(df))
        print("SHEET %s | tickers in file 1 %d | served %d | months per ticker min %s median %s max %s | first month "
              "%s..%s | last month %s..%s" % (
                  sheet, n_univ, len(b), min(months) if months else "-", sorted(months)[len(months) // 2] if months
                  else "-", max(months) if months else "-", firsts[0] if firsts else "-",
                  firsts[-1] if firsts else "-", lasts[0] if lasts else "-", lasts[-1] if lasts else "-"))
except Exception as e:  # noqa: BLE001
    print("DRY RUN FAILED", type(e).__name__, str(e)[:300])
    print("".join(traceback.format_exc().splitlines(True)[-8:]))
print("=== END === %.0fs" % (time.time() - T0))
