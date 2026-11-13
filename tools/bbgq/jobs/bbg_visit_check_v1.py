"""Metadata check of the Bloomberg visit files R8-R11 (no values printed): per series status, first/last month, count, copy check."""
import os, glob, hashlib, datetime, warnings
warnings.filterwarnings("ignore")
import openpyxl
D = r"C:\Users\admin\Documents\WRDS results\lseg\pull_2026-11-12\bloomber 13 Nov 2026"
tot = {}
for f in sorted(glob.glob(os.path.join(D, "*.xlsx"))):
    name = os.path.basename(f); print("#####", name, os.path.getsize(f))
    wb = openpyxl.load_workbook(f, data_only=True, read_only=True)
    exp = {}
    if "Check" in wb.sheetnames:
        for row in wb["Check"].iter_rows(min_row=25, values_only=True):
            if row and len(row) > 6 and row[2]: exp[(row[0], row[2])] = row[6]
    seen = {}; rows_out = []
    for ws in wb.worksheets:
        if ws.title == "Check": continue
        rows = list(ws.iter_rows(values_only=True))
        if len(rows) < 5: continue
        r3 = rows[2]; cols = [i for i, v in enumerate(r3) if isinstance(v, str) and v.strip()]
        for k, c in enumerate(cols):
            end = cols[k + 1] if k + 1 < len(cols) else len(r3)
            tick = r3[c].strip(); lab = rows[1][c] if c < len(rows[1]) else ""
            dts = []; vals = []; first = rows[4][c] if c < len(rows[4]) else None
            for r in rows[4:]:
                if c >= len(r): continue
                d = r[c]; v = [x for x in r[c + 1:end] if isinstance(x, (int, float)) and not isinstance(x, bool)]
                if isinstance(d, datetime.datetime) and v: dts.append(d); vals.append(tuple(v))
                elif isinstance(d, (int, float)) and v and 20000 < d < 60000:
                    dts.append(datetime.datetime(1899, 12, 30) + datetime.timedelta(days=int(d))); vals.append(tuple(v))
            if dts:
                h = hashlib.sha1(repr(vals).encode()).hexdigest()[:10]; seen.setdefault(h, []).append(tick)
                e = exp.get((ws.title, tick)); late = ""
                if isinstance(e, datetime.datetime) and min(dts) > e + datetime.timedelta(days=45): late = " LATE (expected %s)" % e.strftime("%Y-%m")
                rows_out.append((ws.title, tick, lab, "ok", "%s..%s n=%d%s" % (min(dts).strftime("%Y-%m"), max(dts).strftime("%Y-%m"), len(dts), late), h))
                st = "ok"
            else:
                st = "NO DATA"; rows_out.append((ws.title, tick, lab, st, "first cell: %s" % (str(first)[:40]), ""))
            tot[(name, st)] = tot.get((name, st), 0) + 1
    for t in rows_out:
        cp = " COPY of " + ",".join(x for x in seen[t[5]] if x != t[1])[:60] if t[5] and len(set(seen[t[5]])) > 1 else ""
        print("%-18s | %-18s | %-36s | %-7s | %s%s" % (t[0][:18], t[1], str(t[2])[:36], t[3], t[4], cp))
print("TOTALS", sorted(tot.items()))
