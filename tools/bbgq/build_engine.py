"""build_engine: assemble what the PC needs to run the book engine (WORKFLOW v2.1 step 0.5) into
tools/bbgq/engine_pkg/ (git-ignored build output), laid out like Documents\\WRDS results\\local\\ on the PC.

python3 tools/bbgq/build_engine.py        (run tools/bbgq/engine_ref.py first: it names the input files)

engine_pkg/
  lib/gm/                    the gm package, copied unchanged (all .py files, data/, trials.csv; no __pycache__)
  lib/gm_engine.py           engine runner: path shim, fingerprint, comparison, truncation test
  lib/bbg_panel.py           Bloomberg adapter (serves gm.bloomberg from the locked research tables)
  lib/bbgdata.py, live_sources.csv, untouched_markets.csv     the Bloomberg reader (1.2.0) and its two lists
  lib/engine_ref.json        the cloud reference (design period only; gm-2.2.1)
  lib/a1_panel.py            Batch A1 data swap (gm-2.2.1, gm/CHANGES.md data entry A1)
  lib/a2_batch.py            Batch A2 grids / hygiene (gm-2.2.1, gm/CHANGES.md "A2"; 1.1.1)
  lib/diag_a2.py             diagnostics after A2 (gm-2.2.1, gm/CHANGES.md "Diagnostics after A2")
  lib/core_v1.py             Core book v1 (gm-2.2.1, gm/CHANGES.md "Core book v1")
  lib/diag_preb.py           pre-B diagnostics (gm-2.2.1, gm/CHANGES.md "Pre-B diagnostics")
  lib/card_inputs.py         reader of the locked card inputs (gm/CHANGES.md data entry "card inputs")
  lib/lsegdata.py, lseg_rules.py, lseg_*.csv   the LSEG reader (= LOCK_LSEG_v5 code hash), its rules and config lists,
                             copied unchanged from tools/lseg (already on the PC; shipped so the job's pins can be checked)
  lib/rebuild_s4.py          the independent S4 rebuild (separate agent; docs/research/batches/S4_INTERFACE.md), copied
                             unchanged and only if present (OPTIONAL_LIBS); never opened by this script beyond the copy
  jobs/gm_repro_v1.py, gm_trunc_v1.py, gm_bbg_map_v1.py, bbg_build_v2.py, bbg_check_v2.py, gm_a1_v1.py, gm_a1_v2.py,
  gm_a2_v1.py, gm_diag_v1.py, gm_core_v1.py, gm_diag_preb_v1.py
  work/free/gm_free_inputs.zip   the free input files the engine opens (research/..., raw/...) + inputs_manifest.json
  work/free/gm_card_inputs.zip   the card inputs (FRED / ALFRED, macro-data 264d0a2), LOCK_CARD_v1
                                 (tools/bbgq/build_card_inputs.py; not an engine input)

The engine finds its inputs through gm_engine.setup(free_dir): gm.panel.RD and RAW are set to work\\free\\research and
work\\free\\raw (module variables that every gm loader reads at call time; no gm file is edited). The jobs unpack the
zip there on first use.

Compatibility edit of INPUT FILES (not of gm): the PC has no xlrd, which pandas needs for the old binary .xls format.
Every input .xls in binary format (EIA futures, RBA history) is rewritten as an xlsx workbook under the SAME file name;
pandas picks its reader from the file content, so gm's pd.read_excel calls read it with openpyxl. Before it is shipped,
each converted file is read back with every call gm makes on it and must give an identical DataFrame; the
reproduction job then proves the whole run unchanged.
"""
import datetime as dt
import hashlib
import io
import json
import os
import shutil
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
PKG = os.path.join(HERE, "engine_pkg")
REF = os.path.join(HERE, "engine_ref.json")
JOBS = ["gm_repro_v1", "gm_trunc_v1", "gm_bbg_map_v1", "bbg_build_v2", "bbg_check_v2", "gm_a1_v1", "gm_a1_v2", "gm_a2_v1",
        "gm_diag_v1", "gm_core_v1", "gm_diag_preb_v1"]
LIBS = ["lib/gm_engine.py", "lib/bbg_panel.py", "lib/bbgdata.py", "lib/a1_panel.py", "lib/a2_batch.py", "lib/diag_a2.py",
        "lib/core_v1.py", "lib/diag_preb.py", "lib/card_inputs.py", "live_sources.csv",
        "untouched_markets.csv", "engine_ref.json"]
OPTIONAL_LIBS = ["lib/rebuild_s4.py"]       # copied if present (written by a separate agent; not opened here)
SRC_DIRS = {"research": os.path.join(REPO, "cache", "macro", "raw", "research"),
            "raw": os.path.join(REPO, "cache", "macro", "raw")}
# every pd.read_excel call gm makes on an .xls input (file name prefix -> list of keyword sets)
XLS_CALLS = {"eia_": [{"sheet_name": "Data 1", "header": 2}], "cb_au_f2_hist": [{"header": None}],
             "dallas_": [{"header": None}]}


def is_biff(path):
    with open(path, "rb") as f:
        return f.read(8) == b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"


def xls_to_xlsx_bytes(path):
    """Binary .xls -> xlsx bytes with the same sheets, cell values and cell types (numbers, text, dates, booleans)."""
    import xlrd
    from openpyxl import Workbook
    bk = xlrd.open_workbook(path)
    wb = Workbook()
    wb.remove(wb.active)
    for sh in bk.sheets():
        ws = wb.create_sheet(sh.name)
        for r in range(sh.nrows):
            for c in range(sh.ncols):
                cell = sh.cell(r, c)
                t, v = cell.ctype, cell.value
                if t in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK):
                    continue
                if t == xlrd.XL_CELL_DATE:
                    v = xlrd.xldate.xldate_as_datetime(v, bk.datemode)
                elif t == xlrd.XL_CELL_BOOLEAN:
                    v = bool(v)
                elif t == xlrd.XL_CELL_ERROR:
                    v = xlrd.error_text_from_code.get(v, "#N/A")
                ws.cell(r + 1, c + 1, v)
    # openpyxl writes numbers with "%.16g", which loses the last binary digit of about one float in four; write them
    # with repr (shortest exact form) so every value reads back bit for bit
    import openpyxl.cell._writer as W
    orig = W.safe_string
    W.safe_string = lambda v: repr(float(v)) if isinstance(v, float) else orig(v)
    try:
        buf = io.BytesIO()
        wb.save(buf)
    finally:
        W.safe_string = orig
    return buf.getvalue()


def same_reads(orig, conv_bytes, name):
    """Read the original (xlrd) and the converted bytes (openpyxl) with every call gm makes; True if all equal."""
    import pandas as pd
    calls = next((v for k, v in XLS_CALLS.items() if name.startswith(k)), [{"header": None}])
    for kw in calls + [{"header": None, "sheet_name": None}]:
        a = pd.read_excel(orig, **kw)
        b = pd.read_excel(io.BytesIO(conv_bytes), **kw)
        if isinstance(a, dict):
            if set(a) != set(b):
                return False
            pairs = [(a[k], b[k]) for k in a]
        else:
            pairs = [(a, b)]
        for x, y in pairs:
            if not (x.equals(y) and x.astype(str).equals(y.astype(str)) and list(x.columns) == list(y.columns)):
                return False
    return True


def main():
    if not os.path.exists(REF):
        sys.exit("engine_ref.json missing: run python3 tools/bbgq/engine_ref.py first")
    ref = json.load(open(REF, encoding="utf-8"))
    if os.path.isdir(PKG):
        shutil.rmtree(PKG)
    os.makedirs(os.path.join(PKG, "lib"))
    os.makedirs(os.path.join(PKG, "jobs"))
    os.makedirs(os.path.join(PKG, "work", "free"))
    # gm package, unchanged
    gm_src = os.path.join(REPO, "gm")
    shutil.copytree(gm_src, os.path.join(PKG, "lib", "gm"), ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for d, subs, files in os.walk(os.path.join(PKG, "lib", "gm"), topdown=False):
        if not subs and not files:
            os.rmdir(d)
    for rel in LIBS:
        shutil.copy(os.path.join(HERE, rel), os.path.join(PKG, "lib", os.path.basename(rel)))
    for rel in OPTIONAL_LIBS:
        src = os.path.join(HERE, rel)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(PKG, "lib", os.path.basename(rel)))
            print("optional %s: copied" % rel)
        else:
            print("optional %s: absent (not packaged)" % rel)
    import build_card_inputs as BCI                      # the card inputs zip (LOCK_CARD_v1), from git at its commit
    _f, zsha = BCI.build(os.path.join(PKG, "work", "free", "gm_card_inputs.zip"))
    print("card inputs zip: %d files, sha256 %s (lock %s)" % (len(_f), zsha, BCI.CI.LOCK_ID[:16]))
    lseg_dir = os.path.join(REPO, "tools", "lseg")       # the LSEG reader and its lists, copied unchanged
    for f in sorted(os.listdir(lseg_dir)):
        if f in ("lsegdata.py", "lseg_rules.py") or (f.startswith("lseg_") and f.endswith(".csv")):
            shutil.copy(os.path.join(lseg_dir, f), os.path.join(PKG, "lib", f))
    for j in JOBS:
        shutil.copy(os.path.join(HERE, "jobs", j + ".py"), os.path.join(PKG, "jobs", j + ".py"))
    # check: the copied gm files are the ones the reference ran
    import gm_engine as GE
    hashes = GE.gm_code_hashes(os.path.join(PKG, "lib", "gm"))
    if hashes != ref["code"]["gm_files_sha256"]:
        diff = sorted(k for k in set(hashes) | set(ref["code"]["gm_files_sha256"])
                      if hashes.get(k) != ref["code"]["gm_files_sha256"].get(k))
        sys.exit("gm/ differs from the reference run (%s): re-run engine_ref.py" % ", ".join(diff))
    if GE.gm_data_hashes(os.path.join(PKG, "lib", "gm")) != ref["code"].get("gm_data_sha256", {}):
        sys.exit("gm/data differs from the reference run: re-run engine_ref.py")

    # free inputs
    man = {"made": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"), "files": {}}
    zpath = os.path.join(PKG, "work", "free", "gm_free_inputs.zip")
    converted = []
    with zipfile.ZipFile(zpath, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for rel, meta in sorted(ref["inputs"]["files"].items()):
            tag, name = rel.split("/", 1)
            if tag == "gm_data":
                continue                                 # travels inside lib/gm/data
            src = os.path.join(SRC_DIRS[tag], name)
            data = open(src, "rb").read()
            if len(data) != meta["bytes"]:
                sys.exit("input %s changed since the reference run: re-run engine_ref.py" % rel)
            entry = {"original_sha256": hashlib.sha256(data).hexdigest(), "original_bytes": len(data)}
            if name.lower().endswith(".xls") and is_biff(src):
                conv = xls_to_xlsx_bytes(src)
                if not same_reads(src, conv, name):
                    sys.exit("converted %s does not read back identically: stop" % rel)
                data = conv
                entry["converted"] = "binary xls -> xlsx content, same name (PC has no xlrd); read back identically"
                converted.append(rel)
            entry["sha256"] = hashlib.sha256(data).hexdigest()
            entry["bytes"] = len(data)
            man["files"][rel] = entry
            zi = zipfile.ZipInfo(rel, date_time=(2026, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, data)
        man["converted"] = converted
        z.writestr(zipfile.ZipInfo("inputs_manifest.json", date_time=(2026, 1, 1, 0, 0, 0)),
                   json.dumps(man, indent=1, sort_keys=True))

    # list and deployment table
    dest = {"lib": "Documents\\WRDS results\\local\\lib", "jobs": "Documents\\WRDS results\\local\\jobs",
            "work": "Documents\\WRDS results\\local\\work"}
    lines, total = [], 0
    for d, _subs, files in sorted(os.walk(PKG)):
        for n in sorted(files):
            p = os.path.join(d, n)
            rel = os.path.relpath(p, PKG)
            if rel == "DEPLOY.txt":
                continue
            sz = os.path.getsize(p)
            total += sz
            top = rel.split(os.sep)[0]
            lines.append((rel, sz, dest[top] + "\\" + "\\".join(rel.split(os.sep)[1:])))
    with open(os.path.join(PKG, "DEPLOY.txt"), "w", encoding="utf-8") as f:
        f.write("Copy each file to the PC path on the right (folders lib\\gm\\... as they are).\n")
        for rel, sz, to in lines:
            f.write("%-46s %10d  ->  %s\n" % (rel, sz, to))
    gm_files = [x for x in lines if x[0].startswith(os.path.join("lib", "gm") + os.sep)]
    print("engine_pkg built: %d files, %.1f MB" % (len(lines), total / 1e6))
    print("  lib/gm/ (gm package unchanged): %d files, %d KB -> Documents\\WRDS results\\local\\lib\\gm\\" % (
        len(gm_files), sum(x[1] for x in gm_files) // 1024))
    for rel, sz, to in lines:
        if not rel.startswith(os.path.join("lib", "gm") + os.sep):
            print("  %-40s %9d bytes -> %s" % (rel.replace(os.sep, "/"), sz, to))
    print("  free inputs in the zip: %d files, %.1f MB unpacked; %d converted from binary .xls to xlsx content: %s" % (
        len(man["files"]), sum(e["bytes"] for e in man["files"].values()) / 1e6, len(converted),
        ", ".join(c.split("/")[1] for c in converted)))


if __name__ == "__main__":
    sys.path[:0] = [REPO, os.path.join(HERE, "lib")]
    main()
