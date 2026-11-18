"""lseg_eq_probe_v1: read the saved LSEG Workspace EQUITY probe workbook (built by docs/data_requests/build_lseg_equity_probe.py)
and report, per test formula: whether it returned data, number of numeric cells, number of text value cells, date range
of dated rows, error text; for lists the number of items; for first-reported vs restated pairs the number of periods
where the two series differ (counts only). METADATA ONLY: no data value, no company-level number, no name from a data
row is printed. Header labels (field names, series titles) and LSEG error messages are printed.
Workbook: newest LSEG_equity_probe*.xlsx in env LSEG_DIR, else <Documents>\\WRDS results\\lseg\\ (also one folder down).
Runs on the PC runner: cwd = the runner's local folder; openpyxl from pylib."""
import datetime as dt
import glob
import hashlib
import os
import re
import statistics
import sys
import time

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]
T0 = time.time()
print("=== lseg_eq_probe_v1 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
import openpyxl  # noqa: E402

D = os.environ.get("LSEG_DIR") or os.path.join(os.path.dirname(os.getcwd()), "lseg")
files = glob.glob(os.path.join(D, "LSEG_equity_probe*.xlsx")) + glob.glob(os.path.join(D, "*", "LSEG_equity_probe*.xlsx"))
files = sorted((f for f in files if not os.path.basename(f).startswith("~$")), key=os.path.getmtime)
if not files:
    print("no LSEG_equity_probe*.xlsx in", D, "or its subfolders")
    print("=== END ===")
    sys.exit(0)
path = files[-1]
print("file:", os.path.relpath(path, D), "| saved", dt.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M"),
      "| %d bytes" % os.path.getsize(path), "| other probe files: %d" % (len(files) - 1))

ROW0 = 6
META = {"Check", "Index", "Sources", "TestSet", "README"}
PID = re.compile(r"^E-\d+$")
EPOCH = dt.date(1899, 12, 30)
ISO = re.compile(r"^\s*(\d{4})-(\d{2})-(\d{2})")
DMY = re.compile(r"^\s*(\d{1,2})[-/ ]([A-Za-z]{3}|\d{1,2})[-/ ](\d{4})")
MON = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}
NA = {"", "NULL", "NA", "N/A", "#N/A", "NAN", "NONE", "-"}
LOADING = re.compile(r"^\s*(retrieving|updating|requesting|#getting_data|loading)", re.I)
ERRISH = re.compile(r"\berror\b|\binvalid\b|access denied|\bpermission\b|unable to|not found|not available|not entitled|"
                    r"no data|\$\$er|#n/a|\bfailed\b|time ?out|exceeded|too many|not supported|bad request|no record|"
                    r"cannot|could not|not valid|unrecognized", re.I)
HDR = {"instrument", "name", "date", "dates", "code", "type", "series", "calc date", "period end date", "instruments"}


def as_date(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    if isinstance(v, str):
        m = ISO.match(v)
        if m:
            try:
                return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            except ValueError:
                return None
        m = DMY.match(v)
        if m:
            mo = MON.get(m.group(2).lower()) if not m.group(2).isdigit() else int(m.group(2))
            try:
                return dt.date(int(m.group(3)), mo, int(m.group(1))) if mo else None
            except ValueError:
                return None
    return None


def num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def is_na(v):
    return v is None or (isinstance(v, str) and v.strip().upper() in NA)


def text_class(s):
    s = s.strip()
    if as_date(s):
        return "date-like"
    if re.fullmatch(r"[A-Z]{2}[A-Z0-9]{9}\d", s):
        return "ISIN-like"
    if re.fullmatch(r"[0-9]{3}[0-9A-Z]{5}\d", s):
        return "CUSIP-like"
    if re.fullmatch(r"[0-9B-DF-HJ-NP-TV-Z]{6}\d", s):
        return "SEDOL-like"
    if re.fullmatch(r"\d+", s):
        return "digits"
    if re.fullmatch(r"[A-Z0-9.^=@:<>]+", s) and len(s) <= 20:
        return "code-like"
    return "other"


# ---------------------------------------------------------------- Index sheet (meta per formula)
wbv = openpyxl.load_workbook(path, read_only=True, data_only=True)
INFO = {}
if "Index" in wbv.sheetnames:
    rows = list(wbv["Index"].iter_rows(values_only=True))
    head = [str(h or "") for h in rows[0]]
    for r in rows[1:]:
        if r and r[0]:
            INFO[r[0]] = dict(zip(head, r))
else:
    print("WARNING: no Index sheet; groups, pairs and cited/guess unknown")
print("formulas listed in Index:", len(INFO))

RES = {}          # pid -> dict(status, ...)
SERIES = {}       # pid -> {date: value} for pair checks
HASH = {}


def read_block(sheet, pid, cols):
    info = INFO.get(pid, {})
    nrow = max((len(c) for c in cols), default=0)
    rowv = [[(c[i] if i < len(c) else None) for c in cols] for i in range(nrow)]
    while rowv and all(is_na(v) for v in rowv[-1]):
        rowv.pop()
    first = rowv[0][0] if rowv and rowv[0] else None
    # header rows (searched in the first 4 output rows): 'Updated at ...' line or a row with a header token
    hdr_last = -1
    for i, r in enumerate(rowv[:4]):
        cells = [str(v).strip().lower() for v in r if isinstance(v, str)]
        if any(c.startswith("updated at") for c in cells) or any(c in HDR for c in cells):
            hdr_last = i
    headers = []
    for r in rowv[:hdr_last + 1]:
        for v in r:
            if isinstance(v, str) and v.strip() and not v.lower().startswith("updated at") and len(headers) < 6:
                headers.append(v.strip()[:45])
    data = rowv[hdr_last + 1:]
    # the 'Instrument' column repeats our own inputs: never counted as returned text
    instcol = 0 if any(isinstance(r[0], str) and r[0].strip().lower() in ("instrument", "instruments") for r in rowv[:hdr_last + 1] if r) else None
    loading = any(isinstance(v, str) and LOADING.match(v) for r in rowv[:60] for v in r)
    errors = []
    for r in rowv[:5]:      # messages sit at the top of a block; deeper rows are data and are never printed
        for v in r:
            if isinstance(v, str) and (ERRISH.search(v) or v.startswith("#")) and not LOADING.match(v):
                t = v.strip()[:100]
                if t not in errors and len(errors) < 3:
                    errors.append(t)
    # date column: the column with the most date-like cells among data rows (as in lseg_read_v1)
    ncolb = len(cols)
    best = (0, None)
    for j in range(ncolb):
        colv = [r[j] for r in data]
        filled = [v for v in colv if not is_na(v)]
        if len(filled) < 1:
            continue
        nd = sum(1 for v in filled if as_date(v))
        if nd and nd >= 0.8 * len(filled) and nd > best[0]:
            best = (nd, j)
            continue
        serial = [v for v in filled if num(v) and 15000 <= v <= 60000]
        if len(serial) >= 0.8 * len(filled) and len(serial) >= 12 and len(serial) > best[0]:
            steps = [y - x for x, y in zip(serial, serial[1:])]
            if steps and (all(x >= 0 for x in steps) or all(x <= 0 for x in steps)) and any(steps):
                best = (len(serial), j)
    dcol = best[1]

    def rdate(r):
        if dcol is None:
            return None
        v = r[dcol]
        d = as_date(v)
        if d is None and num(v) and 15000 <= v <= 60000:
            d = EPOCH + dt.timedelta(days=int(v))
        return d

    nnum, ntext, nna, alldates, numdates, classes, items = 0, 0, 0, [], [], {}, 0
    ser = {}
    h = hashlib.sha1()
    for r in data:
        rd_ = rdate(r)
        rownum, any_val = None, False
        for j, v in enumerate(r):
            if is_na(v):
                if v is not None:
                    nna += 1
                continue
            any_val = True
            if j == dcol:
                continue
            if num(v):
                nnum += 1
                h.update(("%.9g|" % v).encode())
                if rownum is None:
                    rownum = v
            elif as_date(v):
                alldates.append(as_date(v))
            elif isinstance(v, str):
                if j == instcol:
                    continue
                if ERRISH.search(v) or LOADING.match(v) or v.startswith("#"):
                    continue
                ntext += 1
                k = text_class(v)
                classes[k] = classes.get(k, 0) + 1
        if any_val:
            items += 1
        if rd_ is not None:
            alldates.append(rd_)
            if rownum is not None:
                numdates.append(rd_)
                ser.setdefault(rd_, rownum)
    if nnum >= 24:
        HASH.setdefault(h.hexdigest(), []).append(pid)
    if isinstance(first, str) and first.startswith("#") and not nnum and not ntext:
        status = "EXCEL ERROR"
    elif loading:
        status = "STILL LOADING"
    elif nnum > 0:
        status = "DATA"
    elif ntext > 0 or alldates:
        status = "VALUES (text/dates only)"
    elif errors or headers:
        status = "NO DATA (message)"
    elif any(not is_na(v) for r in rowv for v in r):
        status = "NO DATA (other text)"
    else:
        status = "EMPTY"
    RES[pid] = dict(status=status, info=info)
    if info.get("pair"):
        SERIES[pid] = ser
    line = "%s | %s | %s | %s" % (pid, status, info.get("name cited or guess", "?"), str(info.get("what it tests", ""))[:90])
    parts = []
    if nnum or ntext:
        parts.append("numbers %d | text values %d" % (nnum, ntext))
    if nna:
        parts.append("NA cells %d" % nna)
    if (info.get("kind") in ("list", "static")) or (not nnum and items):
        parts.append("items (rows with a value) %d" % items)
    if numdates:
        gaps = [abs((b - a).days) for a, b in zip(numdates, numdates[1:])]
        parts.append("dated rows with numbers %d: %s to %s (typical gap %s days)" % (
            len(numdates), min(numdates), max(numdates), int(statistics.median(gaps)) if gaps else "-"))
    elif alldates:
        parts.append("date cells %d: %s to %s" % (len(alldates), min(alldates), max(alldates)))
    if classes:
        parts.append("text kinds " + ", ".join("%s %d" % kv for kv in sorted(classes.items())))
    if headers:
        parts.append("headers: " + "; ".join(headers))
    if errors and status != "DATA":
        parts.append("message: " + " / ".join(errors))
    elif errors:
        parts.append("also message: " + errors[0])
    if parts:
        line += " | " + " | ".join(parts)
    print(line)


for ws in wbv.worksheets:
    if ws.title in META:
        continue
    grid = [list(r) for r in ws.iter_rows(values_only=True)]
    ncol = max((len(r) for r in grid), default=0)
    print("--- sheet %s | rows read %d" % (ws.title, len(grid)))
    if len(grid) < 2:
        continue
    starts = [c for c in range(ncol) if c < len(grid[1]) and isinstance(grid[1][c], str) and PID.match(grid[1][c])]
    for q, c in enumerate(starts):
        W = (starts[q + 1] - c) if q + 1 < len(starts) else max(6, ncol - c + 1)
        cols = [[grid[r][k] if k < len(grid[r]) else None for r in range(ROW0 - 1, len(grid))] for k in range(c, min(c + W - 1, ncol))]
        try:
            read_block(ws.title, grid[1][c], cols)
        except Exception as e:  # one broken block must not stop the report
            print("%s | READ FAILED | %s %s" % (grid[1][c], type(e).__name__, str(e)[:100]))
            RES[grid[1][c]] = dict(status="READ FAILED", info=INFO.get(grid[1][c], {}))

# ---------------------------------------------------------------- first reported vs restated
print("--- FIRST REPORTED (Orig) vs RESTATED (Rsdt): counts of fiscal periods, no values")
pairs = {}
for pid, r in RES.items():
    p = str(r["info"].get("pair") or "")
    if "-" in p:
        k, state = p.rsplit("-", 1)
        pairs.setdefault(k, {})[state] = pid
for k in sorted(pairs):
    o, s = pairs[k].get("Orig"), pairs[k].get("Rsdt")
    what = str(RES[o or s]["info"].get("what it tests", ""))[:70].replace(", ReportingState=Orig", "").replace(", ReportingState=Rsdt", "")
    if not (o and s):
        print("PAIR %s | incomplete pair" % k)
        continue
    a, b = SERIES.get(o, {}), SERIES.get(s, {})
    both = set(a) & set(b)
    diff = sum(1 for d in both if abs(a[d] - b[d]) > 1e-6 * max(1.0, abs(a[d]), abs(b[d])))
    print("PAIR %s | %s | %s=%s, %s=%s | periods Orig %d, Rsdt %d, in both %d, DIFFER %d, only Orig %d, only Rsdt %d" % (
        k, what, o, RES[o]["status"], s, RES[s]["status"], len(a), len(b), len(both), diff, len(set(a) - set(b)), len(set(b) - set(a))))

# ---------------------------------------------------------------- copy check + summary
dup = [v for v in HASH.values() if len(v) > 1]
print("COPY CHECK | blocks holding exactly the same numbers as another block: %d groups" % len(dup))
for g in dup[:30]:
    print("COPY | " + " = ".join(g[:8]))
OK = {"DATA", "VALUES (text/dates only)"}
print("--- SUMMARY")
groups = {}
for pid, r in RES.items():
    g = str(r["info"].get("group", "?"))
    c = str(r["info"].get("name cited or guess", "?"))
    s = groups.setdefault(g, {"n": 0, "ok": 0, "load": 0, "xl": 0, "cited": [0, 0], "guess": [0, 0]})
    s["n"] += 1
    s["ok"] += r["status"] in OK
    s["load"] += r["status"] == "STILL LOADING"
    s["xl"] += r["status"] == "EXCEL ERROR"
    if c in ("cited", "guess"):
        s[c][0] += 1
        s[c][1] += r["status"] in OK
for g in sorted(groups):
    s = groups[g]
    print("GROUP %-14s | %3d formulas | returned %3d | still loading %d | Excel error %d | cited %d/%d returned | guess %d/%d returned" % (
        g, s["n"], s["ok"], s["load"], s["xl"], s["cited"][1], s["cited"][0], s["guess"][1], s["guess"][0]))
tot = {}
for r in RES.values():
    tot[r["status"]] = tot.get(r["status"], 0) + 1
print("TOTAL | " + " | ".join("%s %d" % kv for kv in sorted(tot.items())))
missing = sorted(set(INFO) - set(RES))
if missing:
    print("formulas in Index but no block found: %d (%s)" % (len(missing), ", ".join(missing[:10])))
if tot.get("STILL LOADING"):
    print("NOTE: %d blocks were still loading when the file was saved: open it again, wait, save again." % tot["STILL LOADING"])
print("=== END === %.0fs" % (time.time() - T0))
