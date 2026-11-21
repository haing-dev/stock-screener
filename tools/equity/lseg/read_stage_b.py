"""Streaming reader for the stage-B LSEG files (build_lseg_company_data.py: accounts Q1-Q6 / A1, estimates E1-E3,
short interest S1, sector + actual EPS S2). Each data sheet holds one block: row 2 = block id, row 4 = the formula text,
row 6 = header, data from row 7. Column names come from the formula's field list (Instrument + fields), not from the
display header. Rows go to OUT_DIR/<kind>_<group>.csv.gz (kind Q, A, E, S, X ...; group = sheet prefix without the chunk
number), instrument filled down. Prints a metadata report only (blocks, rows, rows with a number, text cells, companies
with data, first/last dates); never values of single companies.
usage: python3 tools/equity/lseg/read_stage_b.py OUT_DIR FILE1.xlsx [FILE2.xlsx ...]"""
import collections as C
import csv
import datetime as dt
import gzip
import os
import re
import sys

import openpyxl


def kind_of(fname):
    b = os.path.basename(fname)
    for pat, k in (("accounts_Q", "Q"), ("accounts_A", "A"), ("estimates_E", "E"), ("short_S", "S"), ("sector_actuals", "S2")):
        if pat in b:
            return k
    return "other"


def fields_of(text):
    m = re.search(r'RDP\.Data\([^,]+,\s*"([^"]+)"', text or "")
    return m.group(1).split(";") if m else None


def iso(x):
    return x.date().isoformat() if isinstance(x, dt.datetime) else x


def main(out_dir, files):
    os.makedirs(out_dir, exist_ok=True)
    writers, handles = {}, []
    rep = C.Counter()
    texts = C.Counter()
    comps = C.defaultdict(set)
    dates = C.defaultdict(lambda: ["9999", "0000"])
    for f in files:
        kind = kind_of(f)
        wb = openpyxl.load_workbook(f, read_only=True, data_only=True)
        for sh in wb.sheetnames:
            if sh in ("Check", "Index", "Sources", "TestSet"):
                continue
            ws = wb[sh]
            head = [r for r in ws.iter_rows(min_row=1, max_row=4, max_col=1, values_only=True)]
            bid = head[1][0] if len(head) > 1 else None
            if not (isinstance(bid, str) and bid.startswith("E-")):
                continue
            flds = fields_of(head[3][0] if len(head) > 3 else "")
            if not flds:
                rep["blocks without formula text"] += 1
                continue
            cols = ["instrument"] + flds
            grp = re.sub(r"\d+$", "", sh).rstrip("_") or sh
            key = "%s_%s" % (kind, grp)
            if key not in writers:
                h = gzip.open(os.path.join(out_dir, key + ".csv.gz"), "wt", newline="")
                handles.append(h)
                writers[key] = (csv.writer(h), cols)
                writers[key][0].writerow(cols)
            w, cols0 = writers[key]
            if cols != cols0:
                rep["column mismatch " + key] += 1
                continue
            n = len(cols)
            cur = None
            rep["blocks " + key] += 1
            got = 0
            for r in ws.iter_rows(min_row=7, max_col=n, values_only=True):
                if r is None or all(v is None for v in r):
                    continue
                inst, vals = r[0], list(r[1:n])
                if isinstance(inst, str) and inst:
                    cur = inst
                if cur is None:
                    continue
                strs = [v for v in vals if isinstance(v, str)]
                nums = [v for v in vals if isinstance(v, (int, float)) and not isinstance(v, bool)]
                rep["rows " + key] += 1
                if strs and not nums:
                    texts[strs[0][:60]] += 1
                if nums:
                    rep["rows with a number " + key] += 1
                    comps[key].add(cur)
                    got += 1
                for v in vals:
                    if isinstance(v, dt.datetime):
                        d = v.date().isoformat()
                        dl = dates[key]
                        dl[0], dl[1] = min(dl[0], d), max(dl[1], d)
                        break
                w.writerow([cur] + [iso(v) if v is not None else "" for v in vals])
            if got == 0:
                rep["blocks with no number " + key] += 1
        wb.close()
        print("read", os.path.basename(f), flush=True)
    for h in handles:
        h.close()
    for key in sorted(writers):
        print("%-10s blocks %4d  rows %8d  rows with a number %8d  companies %5d  dates %s .. %s  empty blocks %d" % (
            key, rep["blocks " + key], rep["rows " + key], rep["rows with a number " + key], len(comps[key]),
            dates[key][0], dates[key][1], rep["blocks with no number " + key]))
    other = {k: v for k, v in rep.items() if k.startswith(("column", "blocks without"))}
    if other:
        print("problems:", other)
    print("text cells (first 8 kinds):", texts.most_common(8))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
