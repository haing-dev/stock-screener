"""bbgdata: the ONLY code that touches the pulled Bloomberg workbooks and the tables derived from them
(WORKFLOW v2.1 steps 0.2-0.4: reader, lock, seal). Runs on the user's PC; nothing it reads or writes leaves the PC.

build(bbg_dir, work_dir)
    Reads every workbook once (openpyxl, read-only, cached values) and writes, under work_dir/bbg:
      catalog.csv                 one row per file / sheet / ticker / field (metadata only, no data values)
      design/{monthly,daily}.pkl  dates <= 2010-12-31 (month-end index / business-day index)
      sealed/{monthly,daily}.pkl  dates after 2010-12-31 (opened only with the one-time holdout key)
      manifest.json               hashes of raw files, config, tables and catalog; counts; code version; build time
      LOCK                        the lock id = sha256 of the manifest with the build time removed
    Earlier manifests and catalogs move to work_dir/bbg/history/ (a rebuild is a clean, versioned re-run).

Panel(work_dir, allow_untouched=False, holdout_key=None)
    Loads the DESIGN tables only. panel.asof(date) returns a view whose getters return only what was knowable on
    `date`: observations dated <= date and released by then (market data: date + live delay; economic series with a
    release-date field: the actual release date). Asking for a date after 2010-12-31 raises HoldoutSealed.
    Untouched markets are invisible unless allow_untouched=True. The sealed tables open only when
    sha256(holdout_key) == HOLDOUT_KEY_SHA256 (None for now: always refused). Every attempt is logged in
    work_dir/bbg/sealed_access.log.

Workbook layout (all seven files): each data sheet holds blocks side by side; row 2 label, row 3 ticker, row 4 "date"
then field names, row 5+ dates and values; a block is n_fields + 2 columns wide. "Read me" and "Check" sheets are
skipped. Sheets whose name starts with "Daily" are daily, all others monthly.

Re-pull workbooks (1.1.0, 2026-11-11): files named "R<n>_..." (re-pull of 13 Nov 2026). Their data sheets are named
"<original file digit> <original sheet>" (e.g. "1 Curves") and hold blocks that belong to that original sheet. Rule, per
(original file, original sheet, ticker, field): a re-pulled block with status ok REPLACES the first-pull block; a
re-pulled block that is requesting / invalid / empty leaves the first-pull block in place ("kept first"); a block that
exists only in the R file is ADDED. Everything else (series ids, duplicates, live-source tags, untouched flags, periodicity)
comes out as if the block had been in the original sheet: a replaced block takes the original block's column, an added
block gets column R_COL_OFFSET x n + its R column (so it sorts after the original sheet's blocks). The catalog says where
each row came from (column `source`: "first" or "R<n>") and, for replaced rows, the first pull's first date and counts.
The first-pull copies of replaced series are kept (design dates only) in design/replaced_first.pkl for the data check.
Without R files the tables are byte-identical to bbgdata-1.0.0 and the catalog differs only by the new columns.
"""
import csv
import datetime as dt
import glob
import hashlib
import io
import json
import os
import re
import shutil
import time
from array import array
from collections import Counter

import numpy as np
import pandas as pd

VERSION = "bbgdata-1.1.0"
SEAL_DATE = pd.Timestamp("2010-12-31")
HOLDOUT_KEY_SHA256 = None            # set once, when the holdout run is authorised (WORKFLOW 5.3); None = always refuse
LIVE_SOURCES = ("free_daily", "official_release", "bloomberg_only")
MISSING_SHEET_DELAY = 31             # days; a sheet not in live_sources.csv gets bloomberg_only with this delay
RELEASE_FIELD = "ECO_RELEASE_DT"
RELEASE_SLACK_DAYS = 31              # a release date more than this before the observation date is treated as junk
DATE_FIELDS = {RELEASE_FIELD}        # fields whose cells are dates, not numbers
CATALOG_COLUMNS = ["file", "file_name", "sheet", "col", "label", "ticker", "field", "per", "kind", "status",
                   "top_error", "first", "last", "count", "n_design", "n_sealed", "last_design", "series_id",
                   "duplicate_of", "live_source", "live_delay_days", "release_sid", "revised", "untouched",
                   "untouched_reason",
                   # 1.1.0 (re-pull): where the row came from; for a replaced row the first pull's status, first date
                   # and counts; for a first-pull row that a failed re-pull left in place, the re-pull's status
                   "source", "first_pull_status", "first_pull_first", "first_pull_count", "first_pull_n_design",
                   "repull_status"]
R_COL_OFFSET = 100000                # column of an added block = R_COL_OFFSET x R number + its column in the R sheet
REPULL_FILE = re.compile(r"^\s*R(\d+)\D")
REPULL_SHEET = re.compile(r"^\s*([1-7])\s+(\S.*?)\s*$")
_HERE = os.path.dirname(os.path.abspath(__file__))
_ORD0 = dt.date(1970, 1, 1).toordinal()
_EXCEL0 = dt.date(1899, 12, 30).toordinal() - _ORD0       # Excel serial 0 as days since 1970-01-01
_TICKER = re.compile(r"(Comdty|Index|Curncy|Govt|Equity|Corp|Mtge|Muni|Pfd)\s*$")
_ISO = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")
_US = re.compile(r"^(\d{1,2})/(\d{1,2})/(\d{4})$")


class HoldoutSealed(Exception):
    """Raised for any request that would reveal data dated after SEAL_DATE without the holdout key."""


# =====================================================================================================================
# field classification (kind of field: price, rate, date, other)
# =====================================================================================================================
RATE_SHEETS = {"Yields", "YieldsExtra", "SpotRates3m", "Swaps", "Breakevens", "FXForwards", "FXVol", "FXBasis",
               "Volatility", "VolComplex", "Surprise", "DailyRates", "DailyVol"}
OTHER_SHEETS = {"Economics", "EconUS", "EconIntl", "Conditions"}
LEVEL_TICKERS = re.compile(r"^(FARBAST|FARBRSBL|RRPONTSYD|EBBSTOTA|BJACTOTL|UKBSTOTA|SZNBSIGH|M2) Index$")
PRICE_FIELDS = {"TOT_RETURN_INDEX_GROSS_DVDS"}
OTHER_FIELDS = {"PE_RATIO", "BEST_PE_RATIO", "PX_TO_BOOK_RATIO", "EQY_DVD_YLD_12M", "BEST_EPS", "CUR_MKT_CAP",
                "OPEN_INT", "PX_VOLUME", "FUT_AGGTE_OPEN_INT", "FUT_AGGTE_VOL", "FUND_TOTAL_ASSETS", "EQY_SH_OUT",
                "ACTUAL_RELEASE", "BN_SURVEY_MEDIAN"}


def field_kind(sheet, ticker, field):
    """price: positive levels (jumps checked on log changes); rate: yields, spreads, vols, points (differences);
    date: release dates; other: ratios, volumes, economic values (no jump test)."""
    if field in DATE_FIELDS:
        return "date"
    if field in PRICE_FIELDS:
        return "price"
    if field in OTHER_FIELDS:
        return "other"
    if sheet in RATE_SHEETS:
        return "rate"
    if sheet in OTHER_SHEETS:
        return "other"
    if sheet == "PolicyMoney":
        return "other" if LEVEL_TICKERS.match(ticker) else "rate"
    if sheet == "Credit":
        return "rate" if re.search(r"OAS|MOOD|CDS", ticker) and "PRC" not in ticker else "price"
    if sheet == "ComFundamentals":
        return "price" if re.match(r"^(LM|GOLDLNPM|IOE62)", ticker) else "other"
    return "price"


# =====================================================================================================================
# small helpers
# =====================================================================================================================
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def content_sha256(df):
    """Hash of a table's content (column names, index, values), independent of the pickle format."""
    h = hashlib.sha256()
    h.update(json.dumps([str(c) for c in df.columns]).encode())
    h.update(np.asarray(df.index.values, dtype="datetime64[ns]").view("int64").tobytes())
    for c in df.columns:
        a = df[c].to_numpy()
        if np.issubdtype(a.dtype, np.datetime64):
            h.update(np.asarray(a, dtype="datetime64[ns]").view("int64").tobytes())
        else:
            h.update(np.ascontiguousarray(a, dtype="float64").tobytes())
    return h.hexdigest()


def lock_id_of(manifest):
    """The lock identifies the DATA: raw workbook contents, the derived tables, the catalog, the two config lists and
    the seal date. Build time, file modification times and the code version are left out, so copying a workbook or
    editing a comment does not change the lock, while any change to a value does."""
    m = {"seal_date": manifest["seal_date"],
         "workbooks": {d: {"sha256": w["sha256"], "size": w["size"]} for d, w in manifest["workbooks"].items()},
         "config": manifest["config"],
         "tables": {k: v["content_sha256"] for k, v in manifest["tables"].items()},
         "catalog": manifest["catalog"]["sha256"]}
    return hashlib.sha256(json.dumps(m, sort_keys=True).encode()).hexdigest()


def _day(v):
    """Cell in a date column -> (days since 1970-01-01 or None, type tag)."""
    if v is None or v == "":
        return None, "blank"
    if isinstance(v, dt.datetime):
        return v.date().toordinal() - _ORD0, "datetime"
    if isinstance(v, dt.date):
        return v.toordinal() - _ORD0, "datetime"
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        if 20000 <= v <= 80000:                       # Excel serial date (format lost when values were pasted)
            return int(v) + _EXCEL0, "serial"
        return None, "number"
    if isinstance(v, str):
        s = v.strip()
        m = _ISO.match(s)
        if m:
            try:
                return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))).toordinal() - _ORD0, "text date"
            except ValueError:
                pass
        m = _US.match(s)
        if m:
            try:
                return dt.date(int(m.group(3)), int(m.group(1)), int(m.group(2))).toordinal() - _ORD0, "text date"
            except ValueError:
                pass
        return None, "string"
    return None, "other"


def _release_day(x):
    """Numeric release-date cell -> days since 1970 (yyyymmdd number or Excel serial) or None, plus its format."""
    if 19000101 <= x <= 21001231:
        try:
            i = int(x)
            return dt.date(i // 10000, (i // 100) % 100, i % 100).toordinal() - _ORD0, "yyyymmdd"
        except ValueError:
            return None, "bad"
    if 20000 <= x <= 80000:
        return int(x) + _EXCEL0, "serial"
    return None, "bad"


def find_workbooks(bbg_dir):
    """-> ({key: path}, warnings). First-pull files are matched by their leading digit 1-7 (key "1".."7"), re-pull
    files by "R<n>" at the start of the name (key "R<n>"); names carry suffixes (" 1", "(1)", "_CUT", "_VALUES").
    Several candidates for one key: the newest by modification time is used, the others are named in a warning."""
    found, warn = {}, []
    for p in sorted(glob.glob(os.path.join(bbg_dir, "*.xls*"))):
        name = os.path.basename(p)
        if name.startswith("~$"):
            continue
        m = re.match(r"^\s*([1-7])\D", name)
        r = REPULL_FILE.match(name)
        if m:
            found.setdefault(m.group(1), []).append(p)
        elif r:
            found.setdefault("R%d" % int(r.group(1)), []).append(p)
        else:
            warn.append("ignored file without a leading digit 1-7 or R<n>: %s" % name)
    out = {}
    for d, ps in sorted(found.items(), key=lambda kv: _key_order(kv[0])):
        ps = sorted(ps, key=lambda q: (os.path.getmtime(q), q))
        out[d] = ps[-1]
        for q in ps[:-1]:
            warn.append("file %s: two candidates, used the newest %s, ignored %s" % (d, os.path.basename(ps[-1]),
                                                                                   os.path.basename(q)))
    return out, warn


def _key_order(k):
    """First-pull digits first ("1".."7"), then re-pull files by number ("R1", "R2", ..., "R10")."""
    return (1, int(k[1:]), "") if k.startswith("R") else (0, 0, k)


def _config_path(name):
    for d in (_HERE, os.path.dirname(_HERE)):
        p = os.path.join(d, name)
        if os.path.exists(p):
            return p
    raise FileNotFoundError("%s not found next to bbgdata.py or one folder up" % name)


def read_live_sources(path=None):
    path = path or _config_path("live_sources.csv")
    out = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            src = r["live_source"].strip()
            if src not in LIVE_SOURCES:
                raise ValueError("live_sources.csv: unknown live_source %r" % src)
            out[(r["file"].strip(), r["sheet"].strip())] = (src, int(r["live_delay_days"]))
    return out, path


def read_untouched(path=None):
    path = path or _config_path("untouched_markets.csv")
    out = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out.setdefault(r["ticker"].strip(), r["reason"].strip())
    return out, path


# =====================================================================================================================
# reading one sheet
# =====================================================================================================================
def _read_sheet(ws, per, fstats):
    """-> (blocks, info). Each block: dict(col, label, ticker, fields, days array, values {field: array}, counts)."""
    rows = ws.iter_rows(values_only=True)
    hdr = []
    for _ in range(4):
        hdr.append(list(next(rows, ()) or ()))
    h2, h3, h4 = hdr[1], hdr[2], hdr[3]
    starts = []
    for c, v in enumerate(h4):
        tk = h3[c] if c < len(h3) else None
        is_date = isinstance(v, str) and v.strip().lower() == "date"
        if is_date or (v in (None, "") and isinstance(tk, str) and _TICKER.search(tk)):
            starts.append(c)
    blocks, info = [], {"no_ticker": 0, "date_types": Counter(), "rows": 0}
    sset = set(starts)
    for c in starts:
        tk = h3[c] if c < len(h3) else None
        if not isinstance(tk, str) or not tk.strip():
            info["no_ticker"] += 1
            continue
        fields, k = [], c + 1
        while k < len(h4) and isinstance(h4[k], str) and h4[k].strip() and h4[k].strip().lower() != "date" \
                and k not in sset:
            fields.append(h4[k].strip())
            k += 1
        if not fields:
            fields = ["PX_LAST"]
        lab = h2[c] if c < len(h2) else None
        blocks.append({"col": c, "label": str(lab).strip() if lab is not None else "", "ticker": tk.strip(),
                       "fields": fields, "days": array("q"), "vals": [array("d") for _ in fields],
                       "n": [[0, 0, 0] for _ in fields], "errors": Counter(), "rel_fmt": Counter()})
    nan = float("nan")
    for row in rows:
        info["rows"] += 1
        L = len(row)
        for b in blocks:
            c = b["col"]
            d, tag = _day(row[c] if c < L else None)
            info["date_types"][tag] += 1
            if tag in ("string", "other", "number"):
                b["errors"][str(row[c])[:40]] += 1
            b["days"].append(-10 ** 9 if d is None else d)
            for i, f in enumerate(b["fields"]):
                v = row[c + 1 + i] if c + 1 + i < L else None
                arr, n = b["vals"][i], b["n"][i]
                if v is None or v == "":
                    arr.append(nan)
                    continue
                st = fstats.setdefault(f, [0, 0, 0])
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    st[0] += 1
                    n[0] += 1
                    if f in DATE_FIELDS:
                        rd, fmt = _release_day(float(v))
                        b["rel_fmt"][fmt] += 1
                        arr.append(nan if rd is None else float(rd))
                    else:
                        arr.append(float(v))
                elif isinstance(v, (dt.datetime, dt.date)):
                    st[1] += 1
                    n[1] += 1
                    if f in DATE_FIELDS:
                        b["rel_fmt"]["datetime"] += 1
                        dd = v.date() if isinstance(v, dt.datetime) else v
                        arr.append(float(dd.toordinal() - _ORD0))
                    else:
                        arr.append(nan)                # a date where a number belongs: not a value
                else:
                    st[2] += 1
                    n[2] += 1
                    b["errors"][str(v)[:40]] += 1
                    arr.append(nan)
    return blocks, info


def _status(b, i):
    if b["kind"][i] == "date":
        ok = np.isfinite(np.frombuffer(b["vals"][i], dtype="float64")).any()
    else:
        ok = b["n"][i][0] > 0
    if ok:
        return "ok"
    errs = " ".join(b["errors"])
    if "Requesting" in errs:
        return "requesting"
    if "Invalid Security" in errs:
        return "invalid"
    return "empty"


def _collapse(days, vals, per):
    """Block rows -> pandas Series on month-ends (monthly) or weekdays (daily); last valid value per date."""
    d = np.frombuffer(days, dtype="int64")
    v = np.frombuffer(vals, dtype="float64")
    ok = (d > -10 ** 8) & np.isfinite(v)
    d, v = d[ok], v[ok]
    if per == "M":
        dd = d.astype("datetime64[D]")
        key = ((dd.astype("datetime64[M]") + 1).astype("datetime64[D]") - 1)
    else:
        wk = (d + 3) % 7 < 5                          # 1970-01-01 was a Thursday; keep Monday-Friday
        key, v = d[wk].astype("datetime64[D]"), v[wk]
    s = pd.Series(v, index=pd.DatetimeIndex(key.astype("datetime64[ns]")))
    s = s[~s.index.duplicated(keep="last")].sort_index()
    return s


# =====================================================================================================================
# re-pull merge
# =====================================================================================================================
def _first_info(e):
    """First valid date, total count and design count of an entry's collapsed series ('' / 0 when not ok)."""
    s = e.get("_s")
    if s is None or not len(s):
        return "", 0, 0
    return s.index[0].strftime("%Y-%m-%d"), int(len(s)), int((s.index <= SEAL_DATE).sum())


def _median_date(dates):
    """Median of ISO dates (the lower middle one for an even count); '' when empty."""
    if not dates:
        return ""
    s = sorted(dates)
    return s[(len(s) - 1) // 2]


def _merge_repull(entries, r_entries):
    """Apply the re-pull rule in place. Matching key: (original file digit, original sheet, ticker, field); when the
    same key occurs several times in a sheet, the k-th re-pulled occurrence matches the k-th first-pull occurrence.
      re-pull ok                  -> replaces the first-pull entry (which is marked _dropped); takes its column
      re-pull not ok, first exists-> first-pull entry kept, its repull_status says what the re-pull returned
      no first-pull entry         -> added (any status), column R_COL_OFFSET x n + R column
    Returns ({id(R entry): first-pull Series or None}, per-original-sheet merge counts)."""
    by_key = {}
    for e in entries:
        by_key.setdefault((e["file"], e["sheet"], e["ticker"], e["field"]), []).append(e)
    seen = Counter()
    replaced_first, merge = {}, {}
    for e in r_entries:
        k = (e["file"], e["sheet"], e["ticker"], e["field"])
        j = seen[k]
        seen[k] += 1
        cand = by_key.get(k, [])
        m = merge.setdefault("%s|%s" % (e["file"], e["sheet"]), Counter())
        m["repulled"] += 1
        if j < len(cand):
            f = cand[j]
            if e["status"] == "ok":
                f["_dropped"] = True
                e["_merge"] = "replaced"
                e["col"], e["_i"] = f["col"], f["_i"]
                e["first_pull_status"] = f["status"]
                e["first_pull_first"], e["first_pull_count"], e["first_pull_n_design"] = _first_info(f)
                replaced_first[id(e)] = f["_s"]
                m["replaced"] += 1
                if f["status"] != "ok":
                    m["replaced_failed_first"] += 1
            else:
                e["_merge"] = "kept_first"
                f["repull_status"] = "%s:%s" % (e["source"], e["status"])
                m["kept_first"] += 1
        else:
            e["_merge"] = "added"
            e["col"] = R_COL_OFFSET * int(e["source"][1:]) + e["_rcol"]
            m["added"] += 1
    return replaced_first, {k: dict(v) for k, v in merge.items()}


# =====================================================================================================================
# build
# =====================================================================================================================
def build(bbg_dir, work_dir, live_csv=None, untouched_csv=None):
    """Read all workbooks, write catalog, design and sealed tables, manifest and lock. Returns a metadata report."""
    t0 = time.time()
    live, live_path = read_live_sources(live_csv)
    untouched, unt_path = read_untouched(untouched_csv)
    found, warnings = find_workbooks(bbg_dir)
    files = {k: p for k, p in found.items() if not k.startswith("R")}          # first pull, by digit
    rfiles = {k: p for k, p in found.items() if k.startswith("R")}             # re-pull, by "R<n>"
    rep = {"files": [], "sheets": [], "field_types": {}, "release_formats": Counter(), "warnings": warnings}
    fstats = {}
    entries = []          # one per block field (first pull)
    r_entries = []        # one per block field (re-pull), merged below
    sheet_order = {}

    def read_workbook(key, path, out):
        """Read one workbook; append one entry per block field to `out`. key: digit (first pull) or "R<n>"."""
        fname = os.path.basename(path)
        rep["files"].append({"file": key, "name": fname, "kb": os.path.getsize(path) // 1024})
        is_r = key.startswith("R")
        try:
            import openpyxl
            wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        except Exception as e:  # noqa: BLE001
            rep["sheets"].append({"file": key, "sheet": "(workbook)", "error": "%s: %s" % (type(e).__name__,
                                                                                          str(e)[:160])})
            return
        for si, ws in enumerate(wb.worksheets):
            name = ws.title.strip()
            if name.lower().startswith("read") or name.lower() == "check":
                rep["sheets"].append({"file": key, "sheet": name, "skipped": True})
                continue
            if is_r:                                       # "<digit> <sheet>": the block's original place
                m = REPULL_SHEET.match(name)
                if not m:
                    warnings.append("re-pull %s: sheet %r is not named '<file digit> <sheet>': skipped" % (key, name))
                    rep["sheets"].append({"file": key, "sheet": name, "skipped": True})
                    continue
                digit, oname = m.group(1), m.group(2)
                if (digit, oname) not in sheet_order:          # original sheet not read: sort after all others
                    sheet_order[(digit, oname)] = 1000 + len(sheet_order)
            else:
                digit, oname = key, name
                sheet_order[(digit, name)] = si
            per = "D" if oname.lower().startswith("daily") else "M"
            t1 = time.time()
            try:
                blocks, info = _read_sheet(ws, per, fstats)
            except Exception as e:  # noqa: BLE001
                rep["sheets"].append({"file": key, "sheet": name, "error": "%s: %s" % (type(e).__name__,
                                                                                       str(e)[:160])})
                continue
            src, delay = live.get((digit, oname), ("bloomberg_only", MISSING_SHEET_DELAY))
            if (digit, oname) not in live:
                warnings.append("sheet %s|%s not in live_sources.csv: bloomberg_only, %d days" % (digit, oname,
                                                                                                 MISSING_SHEET_DELAY))
            st = Counter()
            for b in blocks:
                b["kind"] = [field_kind(oname, b["ticker"], f) for f in b["fields"]]
                rep["release_formats"].update(b["rel_fmt"])
                has_rel = RELEASE_FIELD in b["fields"]
                for i, f in enumerate(b["fields"]):
                    status = _status(b, i)
                    st[status] += 1
                    s = _collapse(b["days"], b["vals"][i], per) if status == "ok" else None
                    top = b["errors"].most_common(1)[0][0] if b["errors"] else ""
                    e = {"file": digit, "file_name": fname, "sheet": oname, "col": b["col"],
                         "label": b["label"], "ticker": b["ticker"], "field": f, "per": per,
                         "kind": b["kind"][i], "status": status, "top_error": top,
                         "live_source": src, "live_delay_days": delay, "has_rel": has_rel,
                         "revised": int(has_rel and f == "PX_LAST"),
                         "untouched": int(b["ticker"] in untouched),
                         "untouched_reason": untouched.get(b["ticker"], ""), "_s": s, "_i": i,
                         "source": key if is_r else "first"}
                    if is_r:
                        e["_rcol"], e["_rsheet"] = b["col"], name
                    out.append(e)
            sh = {"file": key, "sheet": name, "per": per, "blocks": len(blocks),
                  "fields": sum(len(b["fields"]) for b in blocks), "status": dict(st),
                  "rows": info["rows"], "date_types": dict(info["date_types"]),
                  "no_ticker": info["no_ticker"], "seconds": round(time.time() - t1, 1)}
            if is_r:
                sh["original"] = "%s|%s" % (digit, oname)
            rep["sheets"].append(sh)
            del blocks
        wb.close()

    for digit, path in sorted(files.items()):
        read_workbook(digit, path, entries)
    for key, path in sorted(rfiles.items(), key=lambda kv: _key_order(kv[0])):
        read_workbook(key, path, r_entries)
    rep["field_types"] = {f: {"numeric": a, "date": b, "string": c} for f, (a, b, c) in sorted(fstats.items())}

    # ---- re-pull merge (no R files: nothing happens here)
    replaced_first, merge = _merge_repull(entries, r_entries)
    entries = [e for e in entries if not e.get("_dropped")] + [e for e in r_entries if e.get("_merge") in
                                                               ("replaced", "added")]
    rep["repull"] = merge

    # ---- series ids, duplicates, grids
    entries.sort(key=lambda e: (e["file"], sheet_order.get((e["file"], e["sheet"]), 0), e["col"], e["_i"]))
    groups = {}
    for e in entries:
        e["count"] = 0 if e["_s"] is None else int(len(e["_s"]))
        groups.setdefault((e["per"], e["ticker"], e["field"]), []).append(e)
    used = set()
    for key, es in groups.items():
        oks = [e for e in es if e["status"] == "ok"]
        prim = max(oks, key=lambda e: (e["count"], -int(e["file"]), -sheet_order.get((e["file"], e["sheet"]), 0),
                                       -e["col"])) if oks else None
        psid = "%s|%s" % (key[1], key[2]) if prim else ""
        for e in es:
            e["series_id"], e["duplicate_of"] = "", psid if prim is not None and e is not prim else ""
            if e["status"] != "ok":
                continue
            if e is prim:
                sid = psid
            else:
                sid = "%s#%s.%s" % (psid, e["file"], e["sheet"])
                if (e["per"], sid) in used:
                    sid += ".c%d" % e["col"]
            used.add((e["per"], sid))
            e["series_id"] = sid
    # release-date series id per block
    rel_of = {}
    for e in entries:
        if e["field"] == RELEASE_FIELD and e["series_id"]:
            rel_of[(e["file"], e["sheet"], e["col"])] = e["series_id"]
    tables = {}
    for per in ("M", "D"):
        es = [e for e in entries if e["per"] == per and e["series_id"]]
        if es:
            lo = min(e["_s"].index[0] for e in es)
            hi = max(e["_s"].index[-1] for e in es)
            grid = (pd.date_range(lo, hi, freq="ME") if per == "M" else pd.bdate_range(lo, hi))
        else:
            grid = pd.DatetimeIndex([], dtype="datetime64[ns]")
        cols = {}
        for e in es:
            s = e["_s"].reindex(grid)
            if e["kind"] == "date":
                v = s.to_numpy(dtype="float64")       # days since 1970 -> datetime64 (NaT where blank)
                cols[e["series_id"]] = np.where(np.isfinite(v), (np.nan_to_num(v) * 86400e9).astype("int64"),
                                                np.iinfo("int64").min).view("datetime64[ns]")
            else:
                cols[e["series_id"]] = s.to_numpy(dtype="float64")
        df = pd.DataFrame(cols, index=grid) if cols else pd.DataFrame(index=grid)
        df.index.name = "date"
        tables[per] = df
        for e in es:
            col = df[e["series_id"]]
            idx = col.index[col.notna().to_numpy()]
            e["first"] = idx[0].strftime("%Y-%m-%d") if len(idx) else ""
            e["last"] = idx[-1].strftime("%Y-%m-%d") if len(idx) else ""
            e["count"] = int(len(idx))
            e["n_design"] = int((idx <= SEAL_DATE).sum())
            e["n_sealed"] = int((idx > SEAL_DATE).sum())
            dsg = idx[idx <= SEAL_DATE]
            e["last_design"] = dsg[-1].strftime("%Y-%m-%d") if len(dsg) else ""
    for e in entries:
        for k in ("first", "last", "last_design"):
            e.setdefault(k, "")
        for k in ("n_design", "n_sealed"):
            e.setdefault(k, 0)
        e["release_sid"] = rel_of.get((e["file"], e["sheet"], e["col"]), "") if e["has_rel"] else ""
        for k in ("first_pull_status", "first_pull_first", "first_pull_count", "first_pull_n_design", "repull_status"):
            e.setdefault(k, "")

    # ---- re-pull: first-pull copies of replaced series (design dates only) and history added per original sheet
    rf_cols = {}
    if rfiles:
        for e in entries:
            s0 = replaced_first.get(id(e)) if e.get("_merge") == "replaced" else None
            if s0 is not None and e["series_id"] and e["kind"] != "date" and e["per"] == "M":
                rf_cols[e["series_id"]] = s0[s0.index <= SEAL_DATE]
        for key, m in merge.items():
            d, sh = key.split("|", 1)
            before, after = [], []
            for e in entries:
                if e["file"] != d or e["sheet"] != sh:
                    continue
                if e["first"]:
                    after.append(e["first"])
                b = e["first_pull_first"] if e.get("_merge") == "replaced" else (e["first"] if e["source"] == "first"
                                                                                  else "")
                if b:
                    before.append(b)
            m["median_first_before"] = _median_date(before)
            m["median_first_after"] = _median_date(after)
            m["series_before"], m["series_after"] = len(before), len(after)

    # ---- write (clean, versioned)
    root = os.path.join(work_dir, "bbg")
    os.makedirs(root, exist_ok=True)
    old = os.path.join(root, "manifest.json")
    if os.path.exists(old):
        try:
            om = json.load(open(old, encoding="utf-8"))
            tag = "%s_%s" % (re.sub(r"[^0-9]", "", om.get("build_time", ""))[:14] or "old", lock_id_of(om)[:12])
        except Exception:  # noqa: BLE001
            tag = "unreadable_%d" % int(time.time())
        hd = os.path.join(root, "history", tag)
        os.makedirs(hd, exist_ok=True)
        for n in ("manifest.json", "catalog.csv", "LOCK"):
            if os.path.exists(os.path.join(root, n)):
                shutil.move(os.path.join(root, n), os.path.join(hd, n))
    man_tables = {}
    for part in ("design", "sealed"):
        os.makedirs(os.path.join(root, part), exist_ok=True)
        for per, nm in (("M", "monthly"), ("D", "daily")):
            df = tables[per]
            sub = df.loc[df.index <= SEAL_DATE] if part == "design" else df.loc[df.index > SEAL_DATE]
            p = os.path.join(root, part, nm + ".pkl")
            sub.to_pickle(p + ".tmp")
            os.replace(p + ".tmp", p)
            man_tables["%s/%s.pkl" % (part, nm)] = {
                "content_sha256": content_sha256(sub), "rows": int(sub.shape[0]), "columns": int(sub.shape[1]),
                "first": sub.index[0].strftime("%Y-%m-%d") if len(sub) else "",
                "last": sub.index[-1].strftime("%Y-%m-%d") if len(sub) else ""}
    rf_path = os.path.join(root, "design", "replaced_first.pkl")
    if rfiles:                                         # only with R files, so a build without them is unchanged
        g = tables["M"].index[tables["M"].index <= SEAL_DATE]
        rf = pd.DataFrame({k: v.reindex(g).to_numpy(dtype="float64") for k, v in rf_cols.items()}, index=g)
        rf.index.name = "date"
        rf.to_pickle(rf_path + ".tmp")
        os.replace(rf_path + ".tmp", rf_path)
        man_tables["design/replaced_first.pkl"] = {
            "content_sha256": content_sha256(rf), "rows": int(rf.shape[0]), "columns": int(rf.shape[1]),
            "first": rf.index[0].strftime("%Y-%m-%d") if len(rf) else "",
            "last": rf.index[-1].strftime("%Y-%m-%d") if len(rf) else ""}
    elif os.path.exists(rf_path):
        os.remove(rf_path)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(CATALOG_COLUMNS)
    for e in entries:
        w.writerow([e[k] for k in CATALOG_COLUMNS])
    cat_bytes = buf.getvalue().encode("utf-8")
    with open(os.path.join(root, "catalog.csv"), "wb") as f:
        f.write(cat_bytes)
    cnt = {"blocks": len({(e["file"], e["sheet"], e["col"]) for e in entries}), "fields": len(entries),
           "status": dict(Counter(e["status"] for e in entries)),
           "stored": {"M": int(tables["M"].shape[1]), "D": int(tables["D"].shape[1])},
           "duplicates_stored": sum(1 for e in entries if e["series_id"] and e["duplicate_of"]),
           "kind": dict(Counter(e["kind"] for e in entries if e["series_id"])),
           "live_source": dict(Counter(e["live_source"] for e in entries if e["series_id"])),
           "untouched_series": sum(1 for e in entries if e["series_id"] and e["untouched"]),
           "untouched_tickers": len({e["ticker"] for e in entries if e["untouched"]}),
           "untouched_listed": len(untouched), "release_dated": sum(1 for e in entries if e["release_sid"])}
    if rfiles:
        cnt["repull"] = {"files": sorted(rfiles, key=_key_order),
                         "by_source": dict(Counter(e["source"] for e in entries)),
                         **{k: sum(m.get(k, 0) for m in merge.values())
                            for k in ("repulled", "replaced", "replaced_failed_first", "added", "kept_first")}}
    manifest = {
        "code_version": VERSION, "code_sha256": sha256_file(os.path.abspath(__file__)),
        "build_time": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "seal_date": SEAL_DATE.strftime("%Y-%m-%d"),
        "workbooks": {d: {"name": os.path.basename(p), "sha256": sha256_file(p), "size": os.path.getsize(p),
                          "mtime": dt.datetime.fromtimestamp(int(os.path.getmtime(p)), dt.timezone.utc)
                          .strftime("%Y-%m-%dT%H:%M:%SZ")}
                      for d, p in sorted(list(files.items()) + list(rfiles.items()), key=lambda kv: _key_order(kv[0]))},
        "config": {"live_sources.csv": sha256_file(live_path), "untouched_markets.csv": sha256_file(unt_path)},
        "tables": man_tables,
        "catalog": {"file": "catalog.csv", "sha256": hashlib.sha256(cat_bytes).hexdigest(), "rows": len(entries)},
        "counts": cnt, "warnings": sorted(set(warnings)),
    }
    with open(os.path.join(root, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, sort_keys=True)
    lock = lock_id_of(manifest)
    with open(os.path.join(root, "LOCK"), "w", encoding="utf-8") as f:
        f.write(lock + "\n")
    rep.update({"manifest": manifest, "lock_id": lock, "seconds": round(time.time() - t0, 1),
                "release_formats": dict(rep["release_formats"])})
    return rep


# =====================================================================================================================
# access
# =====================================================================================================================
def _log(root, msg):
    with open(os.path.join(root, "sealed_access.log"), "a", encoding="utf-8") as f:
        f.write("%s\t%s\n" % (dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), msg))


def read_catalog(work_dir):
    cat = pd.read_csv(os.path.join(work_dir, "bbg", "catalog.csv"), dtype=str, keep_default_na=False)
    for c in ("col", "count", "n_design", "n_sealed", "live_delay_days", "revised", "untouched"):
        cat[c] = cat[c].astype(int)
    return cat


class Panel:
    """Design-era access with an as-of guard. See the module docstring."""

    def __init__(self, work_dir, allow_untouched=False, holdout_key=None):
        self.root = os.path.join(work_dir, "bbg")
        with open(os.path.join(self.root, "manifest.json"), encoding="utf-8") as f:
            self.manifest = json.load(f)
        self.lock_id = lock_id_of(self.manifest)
        with open(os.path.join(self.root, "LOCK"), encoding="utf-8") as f:
            if f.read().strip() != self.lock_id:
                raise RuntimeError("LOCK does not match manifest.json: rebuild")
        cat = read_catalog(work_dir)
        with open(os.path.join(self.root, "catalog.csv"), "rb") as f:
            if hashlib.sha256(f.read()).hexdigest() != self.manifest["catalog"]["sha256"]:
                raise RuntimeError("catalog.csv does not match the manifest: rebuild")
        self.holdout = False
        if holdout_key is not None:
            hk = hashlib.sha256(str(holdout_key).encode()).hexdigest()
            if HOLDOUT_KEY_SHA256 is None:
                _log(self.root, "holdout key attempt %s: refused (no key registered)" % hk[:8])
                raise HoldoutSealed("no holdout key is registered: the sealed tables stay closed")
            if hk != HOLDOUT_KEY_SHA256:
                _log(self.root, "holdout key attempt %s: refused (wrong key)" % hk[:8])
                raise HoldoutSealed("wrong holdout key")
            _log(self.root, "holdout key attempt %s: GRANTED, lock %s" % (hk[:8], self.lock_id[:12]))
            self.holdout = True
        self.tables = {}
        for per, nm in (("M", "monthly"), ("D", "daily")):
            parts = ["design"] + (["sealed"] if self.holdout else [])
            dfs = []
            for part in parts:
                df = pd.read_pickle(os.path.join(self.root, part, nm + ".pkl"))
                if content_sha256(df) != self.manifest["tables"]["%s/%s.pkl" % (part, nm)]["content_sha256"]:
                    raise RuntimeError("%s/%s.pkl does not match the manifest: rebuild" % (part, nm))
                dfs.append(df)
            self.tables[per] = pd.concat(dfs) if len(dfs) > 1 else dfs[0]
        self.allow_untouched = allow_untouched
        stored = cat[cat["series_id"] != ""]
        hidden = stored[stored["untouched"] == 1]
        if not allow_untouched:
            for per in ("M", "D"):
                drop = [s for s in hidden.loc[hidden["per"] == per, "series_id"] if s in self.tables[per].columns]
                self.tables[per] = self.tables[per].drop(columns=drop)
            cat = cat[cat["untouched"] == 0]
        self.catalog = cat.reset_index(drop=True)
        self._meta = {(r.per, r.series_id): (int(r.live_delay_days), r.release_sid)
                      for r in self.catalog.itertuples() if r.series_id}
        self._avail = {}

    # ---- discovery
    def ids(self, per=None, sheet=None, ticker=None, field=None, kind=None, duplicates=False):
        c = self.catalog[self.catalog["series_id"] != ""]
        for col, v in (("per", per), ("sheet", sheet), ("ticker", ticker), ("field", field), ("kind", kind)):
            if v is not None:
                c = c[c[col] == v]
        if not duplicates:
            c = c[c["duplicate_of"] == ""]
        return list(c["series_id"])

    def info(self, sid, per=None):
        per = self._per(sid, per)
        r = self.catalog[(self.catalog["series_id"] == sid) & (self.catalog["per"] == per)]
        return r.iloc[0].to_dict()

    def _per(self, sid, per):
        if per is not None:
            if (per, sid) not in self._meta:
                raise KeyError("%s (%s) not found or hidden (untouched)" % (sid, per))
            return per
        have = [p for p in ("M", "D") if (p, sid) in self._meta]
        if not have:
            raise KeyError("%s not found or hidden (untouched)" % sid)
        if len(have) > 1:
            raise ValueError("%s exists monthly and daily: pass per='M' or per='D'" % sid)
        return have[0]

    def availability(self, sid, per=None):
        """Date on which each observation became known (NaT where there is no value)."""
        per = self._per(sid, per)
        key = (per, sid)
        if key not in self._avail:
            delay, rel = self._meta[key]
            df = self.tables[per]
            obs = df.index.values.astype("datetime64[ns]")
            av = obs + np.timedelta64(delay, "D")
            if rel and rel in df.columns:
                r = df[rel].to_numpy().astype("datetime64[ns]")
                good = ~np.isnat(r) & (r >= obs - np.timedelta64(RELEASE_SLACK_DAYS, "D"))
                av = np.where(good, np.maximum(r, obs), av)
            col = df[sid]
            av = np.where(col.notna().to_numpy(), av, np.datetime64("NaT"))
            self._avail[key] = av.astype("datetime64[ns]")
        return self._avail[key]

    def asof(self, date):
        d = pd.Timestamp(date).normalize()
        if d > SEAL_DATE and not self.holdout:
            _log(self.root, "asof %s refused (after seal date %s)" % (d.strftime("%Y-%m-%d"),
                                                                      SEAL_DATE.strftime("%Y-%m-%d")))
            raise HoldoutSealed("asof(%s): dates after %s are sealed" % (d.date(), SEAL_DATE.date()))
        return AsOf(self, d)


class AsOf:
    """What was knowable on one date. Every getter returns observations dated <= date and already released."""

    def __init__(self, panel, date):
        self.panel, self.date = panel, date
        self._d = np.datetime64(date.to_datetime64(), "ns")

    def series(self, sid, per=None):
        """Known observations, indexed by observation date."""
        per = self.panel._per(sid, per)
        av = self.panel.availability(sid, per)
        m = ~np.isnat(av) & (av <= self._d)
        return self.panel.tables[per][sid][m].copy()

    def known(self, sid, per=None):
        """Known observations, indexed by the first grid date on or after the day each became known."""
        per = self.panel._per(sid, per)
        av = self.panel.availability(sid, per)
        m = ~np.isnat(av) & (av <= self._d)
        grid = self.panel.tables[per].index
        pos = grid.searchsorted(pd.DatetimeIndex(av[m]), side="left")
        vals = self.panel.tables[per][sid].to_numpy()[m]
        keep = pos < len(grid)
        s = pd.Series(vals[keep], index=grid[pos[keep]])
        s = s[~s.index.duplicated(keep="last")]
        return s[s.index <= self.date]

    def frame(self, sids, per="M", known=False):
        get = self.known if known else self.series
        return pd.DataFrame({s: get(s, per) for s in sids})

    def last(self, sid, per=None):
        s = self.series(sid, per)
        return (s.index[-1], s.iloc[-1]) if len(s) else (None, np.nan)


def load_design(work_dir, allow_untouched=False):
    """Raw design tables (dates <= 2010-12-31, no as-of shifting) and the catalog, for the data check."""
    p = Panel(work_dir, allow_untouched=allow_untouched)
    return p.catalog, {per: df.copy() for per, df in p.tables.items()}, p.lock_id
