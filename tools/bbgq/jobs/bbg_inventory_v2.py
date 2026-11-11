"""bbg_inventory_v2: structure check of the pulled Bloomberg workbooks (WORKFLOW step 0.1).
Prints metadata only: file, sheet, ticker and field names, counts, date ranges, fill shares, error strings.
No price or other data value is printed."""
import collections
import datetime as dt
import glob
import os
import re
import statistics
import sys
import time

sys.path.insert(0, os.path.join(os.getcwd(), "pylib"))   # libraries installed by env_setup into local\pylib

T0 = time.time()
D = os.environ.get("BBG_DIR", "")
print("=== bbg_inventory_v2 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
print("python", sys.version.split()[0])
for m in ("numpy", "pandas", "openpyxl", "scipy", "pyarrow"):
    try:
        mod = __import__(m)
        print("module", m, getattr(mod, "__version__", "ok"))
    except Exception:
        print("module", m, "MISSING")
files = sorted(glob.glob(os.path.join(D, "*.xlsx")))
print("folder", "ok" if os.path.isdir(D) else "NOT FOUND", "| xlsx files:", len(files))
for f in files:
    print(" file", os.path.basename(f), os.path.getsize(f) // 1024, "KB")
try:
    import openpyxl
except Exception:
    print("=== END (openpyxl missing) ===")
    sys.exit(0)

EPOCH = dt.date(1899, 12, 30)
TK = re.compile(r"(Comdty|Index|Curncy|Govt|Equity|Corp)\s*$")
BLOCKS = []


def as_date(v, start_col):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    if start_col and isinstance(v, (int, float)) and not isinstance(v, bool) and 20000 <= v <= 60000:
        return EPOCH + dt.timedelta(days=int(v))        # Excel serial date (format lost when values were pasted)
    return None


def scan(path):
    fn = os.path.basename(path)
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    for ws in wb.worksheets:
        name = ws.title
        if name.lower().startswith("read"):
            continue
        t1 = time.time()
        hdr, cols, starts, nrow = {}, {}, {}, 0
        for r, row in enumerate(ws.iter_rows(values_only=True), start=1):
            if r <= 4:
                hdr[r] = list(row)
                if r == 4:
                    h3, h4 = hdr.get(3, []), hdr.get(4, [])
                    for c, v in enumerate(h3):
                        d4 = h4[c] if c < len(h4) else None
                        if isinstance(v, str) and v.strip() and (TK.search(v) or (isinstance(d4, str) and d4.strip().lower() == "date")):
                            starts[c] = v.strip()
                continue
            nrow = r
            for c, v in enumerate(row):
                if v is None or v == "":
                    continue
                s = cols.get(c)
                if s is None:
                    s = cols[c] = [0, None, None, 0, 0, collections.Counter()]
                d = as_date(v, c in starts)
                if d is not None:
                    s[0] += 1
                    if s[1] is None or d < s[1]:
                        s[1] = d
                    if s[2] is None or d > s[2]:
                        s[2] = d
                elif isinstance(v, (int, float)) and not isinstance(v, bool):
                    s[3] += 1
                else:
                    s[4] += 1
                    k = str(v)[:40]
                    if k in s[5] or len(s[5]) < 20:
                        s[5][k] += 1
        if not starts:
            print("SHEET %s | %s | rows %d | no ticker blocks (skipped)" % (fn[:28], name, nrow))
            continue
        daily = name.lower().startswith("daily")
        need = 250 if daily else 24
        h4 = hdr.get(4, [])
        ok, bad, firsts, lasts, rows = [], [], [], [], []
        fill = collections.defaultdict(lambda: [0, 0])
        for c, tk in sorted(starts.items()):
            fields, k = [], c + 1
            while k < len(h4) and isinstance(h4[k], str) and h4[k].strip() and h4[k].strip().lower() != "date" and k not in starts:
                fields.append(h4[k].strip())
                k += 1
            s = cols.get(c, [0, None, None, 0, 0, collections.Counter()])
            nd = s[0]
            best = max([cols.get(c + 1 + i, [0, 0, 0, 0])[3] for i in range(len(fields))] or [0])
            if nd >= need and best >= need:
                ok.append(tk)
                firsts.append(s[1]); lasts.append(s[2]); rows.append(nd)
                fl = []
                for i, f in enumerate(fields):
                    nn = cols.get(c + 1 + i, [0, 0, 0, 0])[3]
                    fill[f][0] += nn; fill[f][1] += nd
                    fl.append("%s=%d" % (f, round(100.0 * nn / nd)))
                BLOCKS.append("%s|%s|%s|%d|%s|%s|%s" % (fn[:2], name, tk, nd, s[1], s[2], ",".join(fl)))
            else:
                why = (s[5].most_common(1)[0][0] if s[5] else ("only %d dated rows, %d values" % (nd, best)))
                bad.append("%s [%s]" % (tk, why))
                BLOCKS.append("%s|%s|%s|%d|%s|%s|FAILED" % (fn[:2], name, tk, nd, s[1], s[2]))
        print("SHEET %s | %s | %s | rows %d | blocks %d | ok %d | failed %d | %.0fs" % (
            fn[:28], name, "daily" if daily else "monthly", nrow, len(starts), len(ok), len(bad), time.time() - t1))
        if ok:
            fs = sorted(firsts)
            print("   first date: earliest %s, median %s, latest %s | last date: min %s, max %s | rows per ticker: median %d" % (
                fs[0], fs[len(fs) // 2], fs[-1], min(lasts), max(lasts), statistics.median(rows)))
            print("   fill by field (%% of dated rows with a number): %s" % ", ".join(
                "%s %d%%" % (f, round(100.0 * a / b)) for f, (a, b) in fill.items() if b))
        if bad:
            print("   failed: " + "; ".join(bad))
    wb.close()


def formulas(path):
    """Row 5 holds the BDH formula in the template. After 'paste values' it should hold a value."""
    wb = openpyxl.load_workbook(path, read_only=True, data_only=False)
    out = []
    for ws in wb.worksheets:
        if ws.title.lower().startswith("read"):
            continue
        n = f = 0
        for row in ws.iter_rows(min_row=5, max_row=5, values_only=True):
            for v in row:
                if v is None or v == "":
                    continue
                n += 1
                if isinstance(v, str) and v.startswith("="):
                    f += 1
        out.append("%s %d/%d" % (ws.title, f, n))
    wb.close()
    return out


for f in files:
    try:
        scan(f)
    except Exception as e:
        print("ERROR scanning", os.path.basename(f), type(e).__name__, str(e)[:200])
    try:
        print("   row-5 formula cells (formulas/non-empty) in %s: %s" % (os.path.basename(f)[:28], "; ".join(formulas(f))))
    except Exception as e:
        print("ERROR formulas", os.path.basename(f), type(e).__name__, str(e)[:200])
    print("   elapsed %.0fs" % (time.time() - T0))
print("=== BLOCKS (file|sheet|ticker|dated rows|first|last|fill %) ===")
for b in BLOCKS:
    print(b)
print("=== END === %.0fs" % (time.time() - T0))
