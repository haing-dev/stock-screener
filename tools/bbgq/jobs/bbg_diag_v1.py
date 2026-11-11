"""bbg_diag_v1: why do files 1 and 3 start late and disagree with other copies of the same series?
Reads the raw workbooks. Prints counts, shares, names and date ranges only (no data value), and uses only cells
dated on or before 2010-12-31.

T1  what sits in the value cells before a series starts (blank or an error text)
T2  the same ticker and field in two monthly sheets: equal months, close months, best row shift
T3  monthly sheet against a daily sheet of the same ticker: is the monthly value the last daily value of that
    month, some other day of the month, the month average, the previous / next month end, or nothing at all
"""
import bisect
import collections
import datetime as dt
import glob
import os
import re
import sys
import time

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

T0 = time.time()
D = os.environ.get("BBG_DIR", "")
SEAL = dt.date(2010, 12, 31)
EPOCH = dt.date(1899, 12, 30)
TK = re.compile(r"(Comdty|Index|Curncy|Govt|Equity|Corp)\s*$")
print("=== bbg_diag_v1 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
import openpyxl  # noqa: E402


def as_date(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    if isinstance(v, (int, float)) and not isinstance(v, bool) and 20000 <= v <= 60000:
        return EPOCH + dt.timedelta(days=int(v))
    return None


def num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


BL = []     # blocks: dict(file, sheet, daily, ticker, field, dates[], vals[])  (design period only)
PRE = collections.defaultdict(collections.Counter)   # (file, sheet) -> what is in cells before the first number


def scan(path):
    fn = os.path.basename(path)
    digit = fn[:1]
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    for ws in wb.worksheets:
        name = ws.title
        if name.lower().startswith("read") or name.lower() == "check":
            continue
        try:
            hdr, starts, cols = {}, {}, {}
            for r, row in enumerate(ws.iter_rows(values_only=True), start=1):
                if r <= 4:
                    hdr[r] = list(row)
                    if r == 4:
                        h3, h4 = hdr.get(3, []), hdr.get(4, [])
                        for c, v in enumerate(h3):
                            d4 = h4[c] if c < len(h4) else None
                            if isinstance(v, str) and v.strip() and (TK.search(v) or (isinstance(d4, str) and d4.strip().lower() == "date")):
                                k, fields = c + 1, []
                                while k < len(h4) and isinstance(h4[k], str) and h4[k].strip() and h4[k].strip().lower() != "date":
                                    fields.append((k, h4[k].strip()))
                                    k += 1
                                starts[c] = (v.strip(), fields)
                                for k, _f in fields:
                                    cols[k] = ([], [], collections.Counter(), [False])
                    continue
                for c, (tk, fields) in starts.items():
                    d = as_date(row[c]) if c < len(row) else None
                    if d is None or d > SEAL:
                        continue
                    for k, _f in fields:
                        v = row[k] if k < len(row) else None
                        dd, vv, pre, seen = cols[k]
                        if num(v):
                            seen[0] = True
                            dd.append(d)
                            vv.append(float(v))
                        elif not seen[0]:
                            pre["blank" if v is None or v == "" else str(v)[:30]] += 1
            daily = name.lower().startswith("daily")
            for c, (tk, fields) in starts.items():
                for k, f in fields:
                    dd, vv, pre, _s = cols[k]
                    BL.append({"file": digit, "sheet": name, "daily": daily, "ticker": tk, "field": f, "dates": dd, "vals": vv})
                    if dd:
                        PRE[(digit, name)].update(pre)
        except Exception as e:                       # one bad sheet must not stop the job
            print("SHEET %s|%s could not be read: %s" % (digit, name, type(e).__name__))
    wb.close()


for p in sorted(glob.glob(os.path.join(D, "*.xlsx"))):
    if os.path.basename(p)[:1].isdigit():
        t = time.time()
        scan(p)
        print("read file %s in %.0fs" % (os.path.basename(p)[:1], time.time() - t))
print("blocks with design data:", sum(1 for b in BL if b["dates"]), "of", len(BL))

print("--- T1 cells before the first number of a series (design period), by sheet")
for (f, s), c in sorted(PRE.items()):
    print("T1 %s|%s | %s" % (f, s, ", ".join("%s %d" % kv for kv in c.most_common(4))))


def eq(a, b, tol=1e-6):
    return abs(a - b) <= tol * max(1.0, abs(b))


def ym(d):
    return d.year * 12 + d.month


def month_map(b):
    m = {}
    for d, v in zip(b["dates"], b["vals"]):
        m[ym(d)] = v                                 # last value of the month
    return m


print("--- T2 same ticker and field in two monthly sheets (months up to 2010-12)")
print("    columns: months both have | equal | within 0.1% | within 1% | within 10% | equal after shifting the FIRST copy by k months (k=-3..3)")
by = collections.defaultdict(list)
for b in BL:
    if not b["daily"] and b["dates"]:
        by[(b["ticker"], b["field"])].append(b)
agg = collections.defaultdict(lambda: [0] * 13)
lines = []
for (tk, f), bs in sorted(by.items()):
    for i in range(len(bs)):
        for j in range(i + 1, len(bs)):
            a, b = bs[i], bs[j]
            ma, mb = month_map(a), month_map(b)
            common = sorted(set(ma) & set(mb))
            if not common:
                continue
            row = [len(common)] + [0] * 4 + [0] * 7 + [1]
            for m in common:
                x, y = ma[m], mb[m]
                r = abs(x - y) / max(abs(y), 1e-12)
                row[1] += eq(x, y)
                row[2] += r <= 1e-3
                row[3] += r <= 1e-2
                row[4] += r <= 1e-1
            for q, k in enumerate(range(-3, 4)):
                row[5 + q] = sum(1 for m in mb if (m - k) in ma and eq(ma[m - k], mb[m]))
            key = "%s|%s vs %s|%s" % (a["file"], a["sheet"], b["file"], b["sheet"])
            for q in range(13):
                agg[key][q] += row[q]
            if row[1] < row[0]:
                lines.append("T2 pair %s|%s | %s | %s" % (tk, f, key, " ".join(str(x) for x in row[:12])))
for key, r in sorted(agg.items()):
    print("T2 %s | pairs %d | months %d | equal %d | 0.1%% %d | 1%% %d | 10%% %d | shift -3..3: %s" % (
        key, r[12], r[0], r[1], r[2], r[3], r[4], " ".join(str(x) for x in r[5:12])))
print("T2 pairs that are not fully equal: %d (first 60 below)" % len(lines))
for ln in lines[:60]:
    print(ln)

print("--- T3 monthly value against the daily sheet of the same ticker and field (months 1990-01 to 2010-12)")
print("    columns: months | = last daily value of the month | = another day of the month | = month average (0.1%) |"
      " = last day of previous month | = last day of next month | = first day of the month | within 1% of last | none of these")
daily = {}
for b in BL:
    if b["daily"] and b["dates"]:
        daily.setdefault((b["ticker"], b["field"]), b)
agg3 = collections.defaultdict(lambda: [0] * 10)
lines3 = []
for b in BL:
    if b["daily"] or not b["dates"]:
        continue
    d = daily.get((b["ticker"], b["field"]))
    if d is None:
        continue
    dm = collections.defaultdict(list)
    for dd, v in zip(d["dates"], d["vals"]):
        dm[ym(dd)].append(v)
    row = [0] * 9
    for m, x in month_map(b).items():
        vals = dm.get(m)
        if not vals:
            continue
        row[0] += 1
        last = vals[-1]
        if eq(x, last):
            row[1] += 1
        elif any(eq(x, v) for v in vals):
            row[2] += 1
        elif abs(x - sum(vals) / len(vals)) <= 1e-3 * max(abs(x), 1e-12):
            row[3] += 1
        elif dm.get(m - 1) and eq(x, dm[m - 1][-1]):
            row[4] += 1
        elif dm.get(m + 1) and eq(x, dm[m + 1][-1]):
            row[5] += 1
        else:
            row[8] += 1
        if eq(x, vals[0]):
            row[6] += 1
        if abs(x - last) <= 1e-2 * max(abs(last), 1e-12):
            row[7] += 1
    if not row[0]:
        continue
    first = min(b["dates"])
    late = "starts %d+" % (first.year // 5 * 5) if first.year >= 2000 else "starts before 2000"
    key = "%s|%s vs %s|%s | %s" % (b["file"], b["sheet"], d["file"], d["sheet"], late)
    for q in range(9):
        agg3[key][q] += row[q]
    agg3[key][9] += 1
    if row[1] < row[0] and len(lines3) < 80:
        lines3.append("T3 pair %s|%s | %s | %s" % (b["ticker"], b["field"], key, " ".join(str(x) for x in row)))
for key, r in sorted(agg3.items()):
    print("T3 %s | pairs %d | months %d | last %d | other day %d | average %d | prev month %d | next month %d | first day %d | within 1%% %d | none %d" % (
        key, r[9], r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]))
print("T3 pairs not fully equal to the last daily value (first 80):")
for ln in lines3:
    print(ln)

print("--- T4 first month with a number, per monthly sheet (top 3 with counts) and day-of-month of the dates")
fm = collections.defaultdict(collections.Counter)
dom = collections.defaultdict(collections.Counter)
for b in BL:
    if b["daily"] or not b["dates"]:
        continue
    fm[(b["file"], b["sheet"])][min(b["dates"]).strftime("%Y-%m")] += 1
    for dd in b["dates"][:24]:
        nxt = dd + dt.timedelta(days=1)
        kind = "calendar month end" if nxt.month != dd.month else ("last weekday" if (dd + dt.timedelta(days=3)).month != dd.month and dd.weekday() == 4 else "inside month")
        dom[(b["file"], b["sheet"])][kind] += 1
for k in sorted(fm):
    print("T4 %s|%s | first month: %s | date kind: %s" % (k[0], k[1], ", ".join("%s x%d" % kv for kv in fm[k].most_common(3)),
                                                         ", ".join("%s %d" % kv for kv in dom[k].most_common(3))))
print("=== END === %.0fs" % (time.time() - T0))
