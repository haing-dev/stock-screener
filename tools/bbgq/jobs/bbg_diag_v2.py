"""bbg_diag_v2: WHAT is in the late-starting blocks of files 1 and 3?
bbg_diag_v1 showed: every block that starts in the cut-off month (file 1: 2009-06, file 3: 2004-04) holds numbers that
match neither the daily pull nor another monthly pull of the same ticker in the same month. This job asks where those
numbers come from. It reads the raw workbooks and prints counts, names, month offsets and year ranges only (no data
value). The numbers tested are the ones in cells dated up to 2010-12-31; they are looked up (equal / not equal only)
in the other pulls of the same workbooks.

A  same ticker, other month: is the late block the right series moved by k months (any k)?
B  same ticker, daily pull: are the numbers daily values of that ticker (any date)? one per month, or a run of
   consecutive days?
C  other ticker, same month: do the numbers belong to another ticker (or another field) of the pull?
D  same ticker, same month: constant ratio to the right value (a unit or currency conversion)?
E  structure: how many numbers a late block has, and whether two late blocks hold the same numbers
"""
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
CUT = {"1": (2009, 6), "3": (2004, 4)}
TK = re.compile(r"(Comdty|Index|Curncy|Govt|Equity|Corp)\s*$")
print("=== bbg_diag_v2 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
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


def key(v):
    return "%.9g" % v                                # equal to 9 significant digits


def ym(d):
    return d.year * 12 + d.month


BL = []     # blocks: file, sheet, daily, pos (block number in the sheet), ticker, field, dates[], vals[] (all dates)


def scan(path):
    digit = os.path.basename(path)[:1]
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
                                    cols[k] = ([], [])
                    continue
                for c, (tk, fields) in starts.items():
                    d = as_date(row[c]) if c < len(row) else None
                    if d is None:
                        continue
                    for k, _f in fields:
                        v = row[k] if k < len(row) else None
                        if num(v):
                            cols[k][0].append(d)
                            cols[k][1].append(float(v))
            daily = name.lower().startswith("daily")
            for pos, c in enumerate(sorted(starts)):
                tk, fields = starts[c]
                for k, f in fields:
                    dd, vv = cols[k]
                    BL.append({"file": digit, "sheet": name, "daily": daily, "pos": pos, "ticker": tk, "field": f,
                               "dates": dd, "vals": vv})
        except Exception as e:                       # one bad sheet must not stop the job
            print("SHEET %s|%s could not be read: %s" % (digit, name, type(e).__name__))
    wb.close()


for p in sorted(glob.glob(os.path.join(D, "*.xlsx"))):
    if os.path.basename(p)[:1].isdigit():
        t = time.time()
        scan(p)
        print("read file %s in %.0fs" % (os.path.basename(p)[:1], time.time() - t))


def is_late(b):
    if b["daily"] or not b["dates"] or b["file"] not in CUT:
        return False
    f = min(b["dates"])
    return (f.year, f.month) == CUT[b["file"]]


LATE = [b for b in BL if is_late(b)]
GOODM = [b for b in BL if not b["daily"] and b["dates"] and not is_late(b)]
DAILY = [b for b in BL if b["daily"] and b["dates"]]
print("blocks: %d | late (start in the cut-off month of file 1 or 3): %d | other monthly with data: %d | daily with data: %d"
      % (len(BL), len(LATE), len(GOODM), len(DAILY)))


def month_last(b):
    m = {}
    for d, v in zip(b["dates"], b["vals"]):
        m[ym(d)] = v
    return m


daily_by = {}
for b in DAILY:
    daily_by.setdefault((b["ticker"], b["field"]), b)
goodm_by = collections.defaultdict(list)
for b in GOODM:
    goodm_by[(b["ticker"], b["field"])].append(b)

# reference month-end value of every ticker and field that has a trustworthy copy (daily pull first, else a monthly
# block that does not start in a cut-off month)
REF = {}
for kf, b in daily_by.items():
    REF[kf] = (month_last(b), "%s|%s" % (b["file"], b["sheet"]))
for kf, bs in goodm_by.items():
    if kf not in REF:
        REF[kf] = (month_last(bs[0]), "%s|%s" % (bs[0]["file"], bs[0]["sheet"]))
POOL = collections.defaultdict(lambda: collections.defaultdict(set))     # month -> value key -> {(ticker, field)}
for kf, (mm, _src) in REF.items():
    for m, v in mm.items():
        POOL[m][key(v)].add(kf)
POS = {}
for b in BL:
    POS.setdefault((b["file"], b["sheet"], b["ticker"]), b["pos"])


def design(b):
    return [(d, v) for d, v in zip(b["dates"], b["vals"]) if d <= SEAL]


def top(c, n=4):
    return ", ".join("%s x%d" % kv for kv in c.most_common(n)) or "-"


def yrs(dates):
    return "%d-%d" % (min(dates).year, max(dates).year) if dates else "-"


print("--- E structure of the late blocks")
cnt = collections.defaultdict(collections.Counter)
lastd = collections.defaultdict(collections.Counter)
same = collections.defaultdict(list)
for b in LATE:
    s = (b["file"], b["sheet"])
    cnt[s][len(b["vals"])] += 1
    lastd[s][max(b["dates"]).strftime("%Y-%m")] += 1
    dv = design(b)
    if len(dv) >= 12:
        same[tuple(key(v) for _d, v in dv)].append(b)
for s in sorted(cnt):
    print("E %s|%s | late blocks %d | numbers per block: %s | last month with a number: %s" % (
        s[0], s[1], sum(cnt[s].values()), top(cnt[s]), top(lastd[s], 2)))
dups = [g for g in same.values() if len(g) > 1]
print("E late blocks that hold exactly the same numbers as another late block: %d groups, %d blocks" % (len(dups), sum(len(g) for g in dups)))
for g in dups[:15]:
    print("E same numbers: " + " = ".join("%s|%s|%s|%s" % (b["file"], b["sheet"], b["ticker"], b["field"]) for b in g[:6]))

agg = collections.defaultdict(lambda: collections.Counter())
kdist = collections.defaultdict(collections.Counter)
runyrs = collections.defaultdict(collections.Counter)
mthyrs = collections.defaultdict(collections.Counter)
other = collections.defaultdict(collections.Counter)
offs = collections.defaultdict(collections.Counter)
examples = collections.defaultdict(list)
OK = 0.8                                                # share of a block's numbers that must fit

for b in LATE:
    s = "%s|%s" % (b["file"], b["sheet"])
    dv = design(b)
    n = len(dv)
    agg[s]["late blocks"] += 1
    if n < 12:
        agg[s]["fewer than 12 numbers up to 2010 (not tested)"] += 1
        continue
    kf = (b["ticker"], b["field"])
    verdict = []

    # A: same ticker moved by k months
    ref = REF.get(kf)
    if ref is None:
        agg[s]["A no other copy of this ticker and field"] += 1
    else:
        mm = ref[0]
        rix = collections.defaultdict(list)
        for m, r in mm.items():
            rix[key(r)].append(m)
        sh, rv = collections.Counter(), collections.Counter()
        for d, v in dv:
            for m in rix.get(key(v), ()):
                sh[m - ym(d)] += 1                      # same order, moved by k months
                rv[m + ym(d)] += 1                      # reversed order (newest first)
        best_k, best = sh.most_common(1)[0] if sh else (0, 0)
        rbest = rv.most_common(1)[0][1] if rv else 0
        if best >= OK * n:
            kdist[s][best_k] += 1
            verdict.append("A")
            agg[s]["A = same ticker, moved by k months%s" % (" (k=0: equal)" if best_k == 0 else "")] += 1
        elif rbest >= OK * n:
            verdict.append("A")
            agg[s]["A = same ticker, month-end values in REVERSED order"] += 1
        else:
            agg[s]["A no month shift fits"] += 1
        # D: constant ratio in the same month
        rat = [v / mm[ym(d)] for d, v in dv if mm.get(ym(d)) not in (None, 0.0)]
        if len(rat) >= 12 and min(rat) > 0 and max(rat) / min(rat) - 1 <= 1e-3 and abs(rat[0] - 1) > 1e-6:
            agg[s]["D constant ratio to the right value (unit or currency)"] += 1
            verdict.append("D")

    # B: numbers found among the daily values of the same ticker
    db = daily_by.get(kf)
    if db is None:
        agg[s]["B no daily pull of this ticker and field"] += 1
    else:
        idx = collections.defaultdict(list)
        for i, v in enumerate(db["vals"]):
            idx[key(v)].append(i)
        found = sum(1 for _d, v in dv if key(v) in idx)
        agg[s]["B numbers tested"] += n
        agg[s]["B numbers found among the daily values (any date)"] += found
        if found >= OK * n:
            run, rrun = collections.Counter(), collections.Counter()
            for i, (_d, v) in enumerate(dv):
                for j in idx.get(key(v), ()):
                    run[j - i] += 1
                    rrun[j + i] += 1
            off, c = run.most_common(1)[0]
            roff, rc = rrun.most_common(1)[0]
            if c >= OK * n and 0 <= off < len(db["dates"]):
                agg[s]["B = a run of CONSECUTIVE DAILY values of the same ticker"] += 1
                d0 = db["dates"][off]
                d1 = db["dates"][min(off + n - 1, len(db["dates"]) - 1)]
                runyrs[s]["%s to %s" % (d0.strftime("%Y-%m"), d1.strftime("%Y-%m"))] += 1
                verdict.append("B")
            elif rc >= OK * n and 0 <= roff < len(db["dates"]):
                agg[s]["B = a run of consecutive daily values, NEWEST FIRST"] += 1
                d0 = db["dates"][max(roff - n + 1, 0)]
                runyrs[s]["%s to %s (reversed)" % (d0.strftime("%Y-%m"), db["dates"][roff].strftime("%Y-%m"))] += 1
                verdict.append("B")
            else:
                agg[s]["B = daily values of the same ticker, one per month or scattered"] += 1
                md = [db["dates"][idx[key(v)][0]] for _d, v in dv if key(v) in idx]
                mthyrs[s][yrs(md)] += 1
                verdict.append("B")

    # C: another ticker (or field) in the same month
    hit = collections.Counter()
    for d, v in dv:
        for o in POOL.get(ym(d), {}).get(key(v), ()):
            if o != kf:
                hit[o] += 1
    if hit:
        o, c = hit.most_common(1)[0]
        if c >= OK * n:
            verdict.append("C")
            agg[s]["C = the numbers of ANOTHER ticker or field, same month"] += 1
            po = POS.get((b["file"], b["sheet"], o[0]))
            if o[0] == b["ticker"]:
                other[s]["same ticker, other field"] += 1
            elif po is not None:
                other[s]["ticker of the same sheet"] += 1
                offs[s][po - b["pos"]] += 1
            else:
                other[s]["ticker of another sheet"] += 1
            if len(examples[s]) < 6:
                examples[s].append("%s|%s holds %s|%s" % (b["ticker"], b["field"], o[0], o[1]))
    if not verdict:
        agg[s]["NOTHING fits (A-D)"] += 1

print("--- A-D per sheet (a block counts when at least 80% of its numbers dated up to 2010-12 fit)")
for s in sorted(agg):
    print("SHEET %s" % s)
    for k, v in sorted(agg[s].items()):
        print("   %-62s %d" % (k, v))
    if kdist[s]:
        print("   A month shift k (months the numbers sit too LATE if negative, too EARLY if positive): %s" % top(kdist[s], 6))
    if runyrs[s]:
        print("   B consecutive daily run covers: %s" % top(runyrs[s], 5))
    if mthyrs[s]:
        print("   B matched daily dates fall in years: %s" % top(mthyrs[s], 5))
    if other[s]:
        print("   C where the other ticker sits: %s | block offset in the sheet: %s" % (top(other[s]), top(offs[s], 6)))
    for e in examples[s]:
        print("   C example: %s" % e)

tot = collections.Counter()
for s in agg:
    for k, v in agg[s].items():
        tot[k] += v
print("--- TOTAL")
for k, v in sorted(tot.items()):
    print("   %-62s %d" % (k, v))
print("=== END === %.0fs" % (time.time() - T0))
