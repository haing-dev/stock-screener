"""Streaming reader for the LSEG monthly files (build_lseg_monthly.py). Reads block by block with openpyxl read_only,
never holding a whole sheet in memory. Writes one panel (csv.gz: isin, ym, date, close, shares, mcap, volume, ret1m) and
prints a metadata report: blocks, rows, lines with data, months per line, first/last month, text (error) cells,
duplicate-series check, and the volume check block. Never prints values of single companies.
usage: python3 tools/equity/lseg/read_monthly.py OUT.csv.gz FILE1.xlsx [FILE2.xlsx ...]"""
import collections as C
import csv
import datetime as dt
import gzip
import hashlib
import sys

import openpyxl


def blocks_of(ws):
    """yield (block_id, first_col) from row 2 of a data sheet"""
    for r in ws.iter_rows(min_row=2, max_row=2, values_only=True):
        return [(v, k) for k, v in enumerate(r) if isinstance(v, str) and v.startswith("E-")]
    return []


def main(out, files):
    w = csv.writer(gzip.open(out, "wt", newline=""))
    w.writerow(["isin", "ym", "date", "close", "shares", "mcap", "volume", "ret1m"])
    rep = C.Counter()
    lines = {}
    texts = C.Counter()
    hashes = C.defaultdict(list)
    for f in files:
        wb = openpyxl.load_workbook(f, read_only=True, data_only=True)
        for sh in wb.sheetnames:
            if not sh.startswith("M") and sh != "Check2":
                continue
            ws = wb[sh]
            bl = blocks_of(ws)
            if not bl:
                continue
            hdr = None
            cur = {k: None for _, k in bl}
            for i, r in enumerate(ws.iter_rows(min_row=6, values_only=True)):
                if i == 0:
                    hdr = {k: [str(x) for x in r[k:k + 7]] for _, k in bl}
                    continue
                for pid, k in bl:
                    if k + 6 >= len(r):
                        continue
                    inst, d, *vals = r[k:k + 7]
                    if inst is None and d is None:
                        continue
                    if isinstance(inst, str) and inst:
                        cur[k] = inst
                    inst = cur[k]
                    if sh == "Check2":
                        rep["check rows " + pid] += 1
                        continue
                    if not isinstance(d, dt.datetime):
                        if any(isinstance(x, str) for x in (d, *vals)):
                            texts[str(next(x for x in (d, *vals) if isinstance(x, str)))[:50]] += 1
                        continue
                    nums = [x if isinstance(x, (int, float)) else "" for x in vals]
                    rep["rows"] += 1
                    if any(x != "" for x in nums):
                        rep["rows with a number"] += 1
                        L = lines.setdefault(inst, [999999, 0, 0])
                        ym = d.year * 100 + d.month
                        L[0] = min(L[0], ym); L[1] = max(L[1], ym); L[2] += 1
                        hashes[inst].append((ym, nums[0]))
                        w.writerow([inst, ym, d.date().isoformat()] + nums)
            rep["blocks"] += len(bl)
        print("read", f.split("/")[-1])
    print("blocks %d, dated rows %d, rows with a number %d, lines with data %d" % (rep["blocks"], rep["rows"], rep["rows with a number"], len(lines)))
    print("check block rows:", {k: v for k, v in rep.items() if k.startswith("check")})
    print("text cells (first 6 kinds):", texts.most_common(6))
    m = sorted(v[2] for v in lines.values())
    print("months per line: min %d, median %d, max %d" % (m[0], m[len(m) // 2], m[-1]))
    print("first month by year:", sorted(C.Counter(v[0] // 100 for v in lines.values()).items()))
    print("last month by year:", sorted(C.Counter(v[1] // 100 for v in lines.values()).items()))
    sig = C.Counter(hashlib.md5(repr(sorted(v)).encode()).hexdigest() for v in hashes.values() if len(v) > 24)
    print("identical close series shared by more than one line: %d groups" % sum(1 for n in sig.values() if n > 1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
