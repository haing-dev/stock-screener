"""lsegdata: the ONLY code that touches the saved LSEG pull workbooks (L1a ... L11, the weekly live file) and the tables
derived from them (TESTING_PROTOCOL 7.10 item 3: reader with an as-of function, data check, contract identity, lock with
the 2011+ seal, weekly refresh). Runs on the user's PC (stdlib + numpy + pandas + openpyxl); nothing it reads or writes
leaves the PC. Jobs print metadata only (tools/bbgq/README.md export whitelist).

Workbook layout (docs/data_requests/lseg_pull_helpers.py build()): first sheet "Check" (skipped); every data sheet holds
blocks side by side; row 2 block id (e.g. "L10-049"), row 3 label, row 4 "formula: <formula text>", row 6 the formula,
whose result fills down and right until the next block. Four functions are read:
  RH  =RHistory("EUR=","BID.Timestamp;BID.Close","START:... INTERVAL:1MO",,...)       newest first, month labels
  RD  =RDP.Data("US2YT=RR","TR.BIDYIELD.date;TR.BIDYIELD","SDate=... Frq=M CH=Fd RH=IN")  instrument, date, value
       =RDP.Data(<sheet range of RICs>,"TR.ExpiryDate","CH=Fd RH=IN")                    contract calendar (static)
  DS  =DSGRID("BMUS02Y","RY,RI","1969-12-31","-0D","M",...)   date column + one column per code x datatype
  HP  =RDP.HistoricalPricing("CLc1","CLOSE","START:... INTERVAL:P1M SOURCE:RFV",,"SORT:ASC ... RH:Timestamp")
       (without "RH:Timestamp" in the display argument the values come back WITHOUT dates: status no-dates)
The formula text of row 4 says which codes, fields and frequency a block holds; the reader never guesses them from the
values. Inside a block the date column is the column with the most date-like cells; the value columns are the other
columns holding numbers or error text, mapped in order to the formula's code x field list (an RD instrument column is
skipped). A block with numbers but no date column gets status no-dates.

build(dirs, work_dir)
    Reads every L workbook in dirs once and writes, under work_dir/lseg:
      catalog.csv            one row per block x expected series (metadata only, no data value)
      design/long.pkl        long table (sid, per, obs, key, value, hol) for observations dated <= 2010-12-31
      sealed/long.pkl        observations dated after 2010-12-31 (opened only with the holdout key or the live flag)
      calendar.pkl           contract calendar (root, delivery month, RIC, listed, expiry, last trade, first notice):
                             calendar facts, not prices; not sealed
      manifest.json, LOCK    hashes of workbooks, config, tables, catalog; counts; lock id = sha256 of the manifest's
                             data part (build time and code version left out, as bbgdata)
      lock.json              metadata for the repo (like docs/research/bbg/LOCK_v2.json): lock id, files, counts and,
                             per stored series, first / last design date and design count
    Earlier manifests move to work_dir/lseg/history/<time>_<lock>/ (a rebuild is a clean, versioned re-run).

Statuses per expected series: ok / empty (no number, no error text) / invalid (error text: "$$ER", "universe is not
found", "#N/A", permission ...) / no-dates (numbers without a date column) / copy (identical value arrays under
COPY_MIN_CODES or more different instruments: pasted copies, unusable) / wrong-series (listed in lseg_exclusions.csv:
the code returned a different instrument, e.g. CEDCS00 = a grain contract). Only ok series get a series id and enter
the tables. Rows dated after the file's save day (an RHistory month label for a month not yet ended), weekend rows of
daily series and rows without a date are dropped and counted.

Series id: "<fn>:<code>|<field>", e.g. "DS:BMUS02Y|RI", "HP:CLc1|CLOSE", "RH:EUR=|BID", "DS:<EDc1>|X" (X = Datastream
default datatype). Monthly and daily copies of one id are told apart by per ("M" / "D"). The same id pulled again in
another block or file (e.g. "<EDc1>" in L8 and L10): the longest is the primary, the others get "#<file>.<block>".
Monthly key = calendar month-end of the observation; daily key = the observation day. The observation date itself is
kept (obs): Datastream monthly = last weekday of the month (may be a holiday: flagged in hol), RHistory /
HistoricalPricing monthly = a calendar month-end label, RDP.Data = the actual last trading day.

Panel(work_dir, allow_untouched=False, holdout_key=None, live=False)
    Loads the DESIGN table only. panel.asof(date) returns a view whose getters return only observations whose obs date is
    <= date and whose availability (obs + delay of its file/sheet, lseg_live_sources.csv) is <= date. Asking for a date
    after 2010-12-31 raises HoldoutSealed. The sealed table opens only when sha256(holdout_key) == HOLDOUT_KEY_SHA256
    (None now: always refused). live=True opens design + sealed + the weekly live store, but only for as-of dates on or
    after LIVE_START (None now: refused until the gm/CHANGES.md data entry sets it). Every refused or granted attempt is
    logged in work_dir/lseg/sealed_access.log. Untouched instruments (lseg_untouched.csv) are invisible unless
    allow_untouched=True.

Contract identity: Calendar(work_dir) + lseg_roots.csv. A continuous series cN of a root holds, on day d, the N-th listed
contract (by delivery month) whose roll anchor (last trade, expiry or first notice day, per root) is on or after d; the
day after the anchor it moves on. Calendar.held(root, n, d) -> (ric, delivery, last_trade, first_notice, expiry) or None
when the calendar cannot say (no calendar rows, missing anchor date). Whether that rule is LSEG's rule is checked on
sample contracts by lseg_check (value matching); it is not assumed.

Weekly live store (live_ingest): rows of the saved weekly workbook are appended (append-only) to work_dir/lseg/live/ with
the ingest time; the same file (same hash) is never ingested twice; live/ingests.csv chains the table hash per ingest.
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
from collections import Counter, defaultdict

import numpy as np
import pandas as pd

VERSION = "lsegdata-1.0.0"
SEAL_DATE = pd.Timestamp("2010-12-31")
HOLDOUT_KEY_SHA256 = None            # set once, when the holdout run is authorised; None = always refuse
LIVE_START = None                    # first live as-of date, set by the gm/CHANGES.md LSEG data entry; None = refuse
ROW_ID, ROW_LABEL, ROW_FORMULA, ROW0 = 2, 3, 4, 6     # 1-based rows of the pull layout
COPY_MIN_CODES = 3                   # identical value arrays under this many different instruments = pasted copies
COPY_MIN_VALUES = 12                 # a series needs this many numbers before its array is compared
DEFAULT_DELAY = 1                    # days; a sheet not in lseg_live_sources.csv gets kind "market" with this delay
CONFIG_FILES = ("lseg_live_sources.csv", "lseg_exclusions.csv", "lseg_untouched.csv", "lseg_engine_map.csv",
                "lseg_roots.csv")
STATUSES = ("ok", "empty", "invalid", "no-dates", "copy", "wrong-series")
CATALOG_COLUMNS = ["file", "file_name", "sheet", "block", "label", "fn", "code", "field", "per", "status", "error",
                   "header", "n_numbers", "n_undated", "n_future", "n_weekend", "n_collapsed", "first", "last",
                   "n_design", "n_sealed", "last_design", "series_id", "duplicate_of", "copy_group", "kind",
                   "delay_days", "live", "untouched", "untouched_reason", "wrong_reason", "engine_id", "engine_role",
                   "date_rule", "n_hol_design"]
FILE_KEY = re.compile(r"^\s*(L\d+[a-z]?)[_ \-]", re.I)
WEEKLY_NAME = re.compile(r"^\s*LSEG_weekly", re.I)
PID = re.compile(r"^[A-Z][A-Za-z0-9]*-\d+$")
ERR = re.compile(r"\$\$ER|#ERROR|INVALID|not found|permission|denied|unable to|not available|#N/A|#NAME\?|#VALUE!|"
                 r"#REF!|#NULL!|#DIV/0!|error|no data", re.I)
NA_TEXT = {"", "NULL", "NA", "N/A"}
MONTH_CODES = "FGHJKMNQUVXZ"
RIC_RE = re.compile(r"^([A-Z0-9]+?)([FGHJKMNQUVXZ])(\d)(?:\^(\d))?$")
ROLE_OF_FIELD = {"TR.EXPIRYDATE": "expiry", "TR.EXPIRATIONDATE": "expiry", "EXPIR_DATE": "expiry",
                 "TR.LASTTRADEDATE": "last_trade", "TR.LASTTRADINGDATE": "last_trade", "TR.LASTTRADINGDAY": "last_trade",
                 "TR.FIRSTNOTICEDATE": "first_notice", "TR.FIRSTNOTICEDAY": "first_notice",
                 "TR.FIRSTDELIVERYDATE": "first_delivery", "TR.LASTDELIVERYDATE": "last_delivery"}
CAL_ROLES = ("expiry", "last_trade", "first_notice", "first_delivery", "last_delivery")
_HERE = os.path.dirname(os.path.abspath(__file__))
_EPOCH = dt.date(1970, 1, 1)
_EXCEL0 = dt.date(1899, 12, 30)
_ISO = re.compile(r"^\s*(\d{4})-(\d{2})-(\d{2})")
_DMY = re.compile(r"^\s*(\d{1,2})[-/ ]([A-Za-z]{3})[-/ ](\d{4})")
_MON = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}


class HoldoutSealed(Exception):
    """Raised for any request that would reveal data dated after SEAL_DATE without the holdout key or the live flag."""


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
    """Hash of a long table's content (columns and values in row order; the writer sorts the rows first)."""
    h = hashlib.sha256()
    h.update(json.dumps([str(c) for c in df.columns]).encode())
    for c in df.columns:
        a = df[c].to_numpy()
        if np.issubdtype(a.dtype, np.datetime64):
            h.update(np.asarray(a, dtype="datetime64[ns]").view("int64").tobytes())
        elif np.issubdtype(a.dtype, np.number):
            h.update(np.ascontiguousarray(a, dtype="float64").tobytes())
        else:
            h.update("\x1f".join("" if x is None else str(x) for x in a).encode())
    return h.hexdigest()


def lock_id_of(manifest):
    """The lock identifies the DATA: workbook contents, derived tables, catalog, config lists and the seal date."""
    m = {"seal_date": manifest["seal_date"],
         "workbooks": {k: {"sha256": w["sha256"], "size": w["size"]} for k, w in manifest["workbooks"].items()},
         "config": manifest["config"],
         "tables": {k: v["content_sha256"] for k, v in manifest["tables"].items()},
         "catalog": manifest["catalog"]["sha256"]}
    return hashlib.sha256(json.dumps(m, sort_keys=True).encode()).hexdigest()


def as_date(v):
    """Cell -> datetime.date or None (datetime / date objects, ISO text, '12-Nov-2026' text)."""
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    if isinstance(v, str):
        m = _ISO.match(v)
        if m:
            try:
                return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            except ValueError:
                return None
        m = _DMY.match(v)
        if m and m.group(2).lower() in _MON:
            try:
                return dt.date(int(m.group(3)), _MON[m.group(2).lower()], int(m.group(1)))
            except ValueError:
                return None
    return None


def is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and v == v


def norm_code(code):
    """Instrument key used for copy detection: '<EDc1>' and 'EDc1' are one instrument."""
    return re.sub(r"[<>\s]", "", str(code)).upper()


def month_end(d):
    nxt = dt.date(d.year + (d.month == 12), d.month % 12 + 1, 1)
    return nxt - dt.timedelta(days=1)


def last_weekday(d):
    e = month_end(d)
    while e.weekday() >= 5:
        e -= dt.timedelta(days=1)
    return e


def _config_path(name, cfg_dir=None):
    for d in ([cfg_dir] if cfg_dir else []) + [_HERE, os.path.dirname(_HERE)]:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return p
    raise FileNotFoundError("%s not found next to lsegdata.py or one folder up" % name)


def _read_csv(name, cfg_dir=None):
    p = _config_path(name, cfg_dir)
    with open(p, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if not (r.get(next(iter(r)), "") or "").startswith("#")]
    return rows, p


# ---------------------------------------------------------------- holidays (flags only: month-end on a market holiday)
def _easter(y):
    a, b, c = y % 19, y // 100, y % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l_ = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l_) // 451
    mo = (h + l_ - 7 * m + 114) // 31
    return dt.date(y, mo, (h + l_ - 7 * m + 114) % 31 + 1)


def _nth_wd(y, m, wd, n):
    d = dt.date(y, m, 1)
    d += dt.timedelta(days=(wd - d.weekday()) % 7)
    return d + dt.timedelta(weeks=n - 1)


def _last_wd(y, m, wd):
    d = month_end(dt.date(y, m, 1))
    return d - dt.timedelta(days=(d.weekday() - wd) % 7)


def _observed(d):
    return d + dt.timedelta(days=1) if d.weekday() == 6 else (d - dt.timedelta(days=1) if d.weekday() == 5 else d)


_HOL = {}


def holidays(y):
    """(US exchange holidays, UK bank holidays) of year y: approximate calendars, used only to flag month-ends."""
    if y not in _HOL:
        e = _easter(y)
        us = {_observed(dt.date(y, 1, 1)), e - dt.timedelta(days=2), _observed(dt.date(y, 7, 4)),
              _nth_wd(y, 9, 0, 1), _nth_wd(y, 11, 3, 4), _observed(dt.date(y, 12, 25)), _nth_wd(y, 2, 0, 3)}
        us.add(_last_wd(y, 5, 0) if y >= 1971 else dt.date(y, 5, 30))
        if y >= 1998:
            us.add(_nth_wd(y, 1, 0, 3))
        uk = {e - dt.timedelta(days=2), e + dt.timedelta(days=1)}
        xm, bx = dt.date(y, 12, 25), dt.date(y, 12, 26)
        if xm.weekday() == 5:                       # Saturday: Monday 27 and Tuesday 28
            uk |= {dt.date(y, 12, 27), dt.date(y, 12, 28)}
        elif xm.weekday() == 6:                     # Sunday: Boxing Day Monday 26, Christmas Tuesday 27
            uk |= {bx, dt.date(y, 12, 27)}
        elif xm.weekday() == 4:                     # Friday: Boxing Day Monday 28
            uk |= {xm, dt.date(y, 12, 28)}
        else:
            uk |= {xm, bx}
        if y >= 1974:
            nd = dt.date(y, 1, 1)
            uk.add(nd + dt.timedelta(days=(7 - nd.weekday()) % 7) if nd.weekday() >= 5 else nd)
        if y >= 1971:
            uk.add(_last_wd(y, 5, 0))
            uk.add(_last_wd(y, 8, 0))
        if y >= 1978:
            uk.add(_nth_wd(y, 5, 0, 1))
        _HOL[y] = (us, uk)
    return _HOL[y]


def trading_day(d, market="US"):
    """The trading day a monthly observation's value belongs to: a calendar month-end label (RHistory /
    HistoricalPricing) or a Datastream last weekday that is a holiday carries the close of the last trading day on or
    before it (approximate US or UK calendar). Used by the identity check to place a month-end value on its day."""
    bit = 1 if market == "US" else 2
    while d.weekday() >= 5 or hol_flag(d) & bit:
        d -= dt.timedelta(days=1)
    return d


def hol_flag(d):
    us, uk = holidays(d.year)
    return (1 if d in us else 0) + (2 if d in uk else 0)


# =====================================================================================================================
# formula parsing
# =====================================================================================================================
def _split_args(text, i):
    """Top-level arguments of a call whose '(' is at text[i-1]; raw text of each argument (quotes kept)."""
    args, cur, q, depth = [], [], False, 0
    while i < len(text):
        ch = text[i]
        if q:
            cur.append(ch)
            if ch == '"':
                if i + 1 < len(text) and text[i + 1] == '"':
                    cur.append('"')
                    i += 1
                else:
                    q = False
        elif ch == '"':
            q = True
            cur.append(ch)
        elif ch == "(":
            depth += 1
            cur.append(ch)
        elif ch == ")":
            if depth == 0:
                args.append("".join(cur).strip())
                return args
            depth -= 1
            cur.append(ch)
        elif ch == "," and depth == 0:
            args.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
        i += 1
    args.append("".join(cur).strip())
    return args


def _unq(raw):
    """A plain quoted string -> its content; anything else (range, expression, empty) unchanged."""
    if raw is None:
        return ""
    m = re.fullmatch(r'"((?:[^"]|"")*)"', raw.strip())
    return m.group(1).replace('""', '"') if m else raw.strip()


def _is_quoted(raw):
    return bool(re.fullmatch(r'"((?:[^"]|"")*)"', (raw or "").strip()))


_FN = re.compile(r"([A-Za-z][A-Za-z0-9_.]*)\s*\(")
FN_TAG = {"RHISTORY": "RH", "RDP.DATA": "RD", "TR": "RD", "DSGRID": "DS", "RDP.HISTORICALPRICING": "HP"}


def parse_formula(text):
    """Formula text (row 4 'formula: ...' or a formula) -> dict(fn, codes, fields, expected, per, dated, inst_range)
    or None when the function is not one of the four. per: 'M', 'D' or 'S' (static)."""
    if not isinstance(text, str):
        return None
    t = re.sub(r"^\s*formula:\s*", "", text.strip())
    t = t.lstrip("=").strip()
    m = _FN.match(t)
    if not m or m.group(1).upper() not in FN_TAG:
        return None
    fn = FN_TAG[m.group(1).upper()]
    a = _split_args(t, m.end())
    a += [""] * (6 - len(a))
    up = t.upper()
    out = {"fn": fn, "text": t, "inst_range": None, "dated": True}
    if fn == "RH":
        code = _unq(a[0])
        fl = _unq(a[1])
        fam = fl.split(";")[0].split(".")[0].strip() if fl else ""
        field = fam.upper() if fam else "CLOSE"
        per = "D" if re.search(r"INTERVAL:\s*1D\b", up) else ("M" if re.search(r"INTERVAL:\s*1MO\b", up) else
                                                               ("W" if "INTERVAL:1W" in up.replace(" ", "") else "M"))
        out.update(codes=[code], fields=[field], per=per)
    elif fn == "RD":
        if _is_quoted(a[0]):
            codes = [c.strip() for c in _unq(a[0]).split(",") if c.strip()]
        else:
            codes, out["inst_range"] = [], a[0].strip()
        fl = [f.strip() for f in _unq(a[1]).split(";") if f.strip()]
        vals = [f for f in fl if not f.lower().endswith(".date")]
        fq = re.search(r"FRQ=\s*([A-Z]+)", up)
        per = {"M": "M", "D": "D", "W": "W", "Q": "Q", "FY": "Y", "Y": "Y"}.get(fq.group(1), "M") if fq else "S"
        out.update(codes=codes, fields=[f.upper() for f in vals], per=per,
                   dated=per != "S" and any(f.lower().endswith(".date") for f in fl))
    elif fn == "DS":
        codes = [c.strip() for c in _unq(a[0]).split(",") if c.strip()]
        dts = [d.strip().upper() for d in _unq(a[1]).split(",") if d.strip()] or ["X"]
        start = _unq(a[2])
        frq = _unq(a[4]).upper()
        per = "S" if start.lower().startswith("latest") else ("D" if frq == "D" else ("M" if frq in ("M", "") else frq))
        out.update(codes=codes, fields=dts, per=per, dated=per != "S")
    else:  # HP
        code = _unq(a[0])
        fl = [f.strip().upper() for f in _unq(a[1]).split(";") if f.strip()] or ["CLOSE"]
        fl = [f for f in fl if f not in ("DATE", "TIMESTAMP")] or ["CLOSE"]
        per = "D" if re.search(r"INTERVAL:\s*P1D\b", up) else ("W" if re.search(r"INTERVAL:\s*P1W\b", up) else "M")
        disp = _unq(a[4]) if len(a) > 4 else ""
        out.update(codes=[code], fields=fl, per=per, dated="RH:TIMESTAMP" in disp.upper().replace(" ", ""))
    if fn == "DS":
        out["expected"] = [(c, f) for c in out["codes"] for f in out["fields"]]
    else:
        out["expected"] = [(c, f) for c in out["codes"] for f in out["fields"]] if out["codes"] else []
    return out


# =====================================================================================================================
# reading one workbook
# =====================================================================================================================
def file_key(name):
    """'L10_rate_strips_swaps_guesses.xlsx' -> 'L10'; 'LSEG_weekly_live.xlsx' -> 'W'; else None."""
    m = FILE_KEY.match(name)
    if m:
        k = m.group(1)
        return "L" + k[1:].lower() if not k[1:].isdigit() else "L" + k[1:]
    if WEEKLY_NAME.match(name):
        return "W"
    return None


def key_order(k):
    m = re.match(r"^L(\d+)([a-z]?)$", k)
    return (0, int(m.group(1)), m.group(2)) if m else (1, 0, k)


def find_workbooks(dirs):
    """-> ({key: path}, candidates list, warnings). L files only (P probes and other files are listed, not read).
    Several files for one key: the newest by modification time is used."""
    found, warn, seen = {}, [], set()
    for d in dirs:
        for p in sorted(glob.glob(os.path.join(d, "*.xlsx"))):
            name = os.path.basename(p)
            if name.startswith("~$") or os.path.abspath(p) in seen:
                continue
            seen.add(os.path.abspath(p))
            k = file_key(name)
            if k is None or k == "W":
                warn.append("not read (not an L pull file): %s" % name)
                continue
            found.setdefault(k, []).append(p)
    out, cands = {}, []
    for k in sorted(found, key=key_order):
        ps = sorted(found[k], key=lambda q: (os.path.getmtime(q), q))
        out[k] = ps[-1]
        for q in ps:
            cands.append({"key": k, "name": os.path.basename(q), "dir": os.path.dirname(q), "used": q == ps[-1]})
        for q in ps[:-1]:
            warn.append("file %s: %d candidates, used the newest %s, ignored %s" % (k, len(ps), os.path.basename(ps[-1]),
                                                                                    os.path.basename(q)))
    return out, cands, warn


def _date_column(cols):
    """Index of the column with the most date-like cells (>= 3 and >= 80% of its filled cells), else None; and the
    parsed dates of that column (list aligned with the rows)."""
    best = (0, None, None)
    for j, col in enumerate(cols):
        first = next((i for i, v in enumerate(col) if as_date(v) or (is_num(v) and 15000 <= v <= 80000)), len(col))
        filled = [v for i, v in enumerate(col) if v is not None and not (isinstance(v, str) and
                  (v.strip().upper() in NA_TEXT or i < first))]
        if len(filled) < 3:
            continue
        dd = [as_date(v) for v in col]
        nd = sum(1 for d in dd if d)
        if nd >= 0.8 * len(filled) and nd > best[0]:
            best = (nd, j, dd)
            continue
        serial = [v for v in filled if is_num(v) and 15000 <= v <= 80000]
        if len(serial) >= 0.8 * len(filled) and len(serial) >= 12 and len(serial) > best[0]:
            steps = [y - x for x, y in zip(serial, serial[1:])]
            if steps and (all(x >= 0 for x in steps) or all(x <= 0 for x in steps)) and any(steps):
                best = (len(serial), j, [_EXCEL0 + dt.timedelta(days=int(v)) if is_num(v) and 15000 <= v <= 80000
                                         else None for v in col])
    return best[1], best[2]


def _errors(col):
    """Error texts of a column, the most informative first ('$$ER: E100,INVALID CODE ...' before '#ERROR')."""
    e = [v.strip()[:80] for v in col if isinstance(v, str) and ERR.search(v)]
    return sorted(e, key=lambda x: (not x.startswith("$$ER"), len(x) < 12))


def _strings(col):
    return [v.strip() for v in col if isinstance(v, str) and v.strip() and v.strip().upper() not in NA_TEXT]


def read_block(rows, c0, c1, spec):
    """Rows (from ROW0 on, lists of cell values) of one block, columns c0..c1-1 -> (entries, block info). Each entry:
    code, field, status, error, header, days (list of date), vals (list of float), counts."""
    cols = [[r[k] if k < len(r) else None for r in rows] for k in range(c0, c1)]
    info = {"errors": [], "extra_cols": 0}
    blk_err = []
    for col in cols:
        blk_err += _errors(col)
    info["errors"] = blk_err[:3]
    dj, dates = _date_column(cols)
    numcols = [j for j, col in enumerate(cols) if j != dj and any(is_num(v) for v in col)]
    codes_up = {c.upper() for c in spec["codes"]}
    cand = []
    for j, col in enumerate(cols):
        if j == dj:
            continue
        has_num = any(is_num(v) for v in col) or (dj is not None and any(isinstance(v, (dt.date, dt.datetime))
                                                                         for v in col))
        errs = _errors(col)
        if not has_num and not errs:
            continue
        if spec["fn"] == "RD" and not has_num:
            st = _strings(col)
            if st and sum(1 for s in st if s.upper() in codes_up) >= 0.5 * len(st):
                continue                                  # instrument column
        cand.append(j)
    expected = spec["expected"]
    entries = []

    def entry(code, field, status, error="", header="", days=None, vals=None, nnum=0, nund=0):
        return {"code": code, "field": field, "status": status, "error": error, "header": header,
                "days": days or [], "vals": vals or [], "n_numbers": nnum, "n_undated": nund}
    if not expected:
        return entries, info
    if dj is None:
        nnum = sum(sum(1 for v in cols[j] if is_num(v)) for j in numcols)
        for code, field in expected:
            if nnum:
                entries.append(entry(code, field, "no-dates", nnum=nnum))
            else:
                entries.append(entry(code, field, "invalid" if blk_err else "empty", error=(blk_err or [""])[0]))
        return entries, info
    if len(cand) > len(expected):
        info["extra_cols"] = len(cand) - len(expected)
    for i, (code, field) in enumerate(expected):
        if i >= len(cand):
            entries.append(entry(code, field, "invalid" if blk_err else "empty", error=(blk_err or [""])[0]))
            continue
        col = cols[cand[i]]
        days, vals, nund, hdr = [], [], 0, []
        for r, v in enumerate(col):
            if isinstance(v, (dt.date, dt.datetime)):       # a date-valued field (e.g. an expiry date series):
                v = float(((v.date() if isinstance(v, dt.datetime) else v) - _EXCEL0).days)   # Excel serial
            if is_num(v):
                d = dates[r] if r < len(dates) else None
                if d is None:
                    nund += 1
                    continue
                days.append(d)
                vals.append(float(v))
            elif isinstance(v, str) and not days and len(hdr) < 2 and v.strip() and not ERR.search(v):
                hdr.append(v.strip())
        errs = _errors(col)
        if vals:
            entries.append(entry(code, field, "ok", header=" | ".join(hdr)[:100], days=days, vals=vals,
                                 nnum=len(vals) + nund, nund=nund))
        elif nund:
            entries.append(entry(code, field, "no-dates", header=" | ".join(hdr)[:100], nnum=nund, nund=nund))
        else:
            entries.append(entry(code, field, "invalid" if (errs or blk_err) else "empty",
                                 error=(errs or blk_err or [""])[0], header=" | ".join(hdr)[:100]))
    return entries, info


def read_calendar_block(rows, c0, c1, spec, range_rics):
    """RDP.Data over a range of contract RICs (static fields) -> list of (ric, field, date or None, error text)."""
    cols = [[r[k] if k < len(r) else None for r in rows] for k in range(c0, c1)]
    out = []
    fields = spec["fields"]
    ricset = set(range_rics or [])
    ric_col = None
    for j, col in enumerate(cols):
        st = _strings(col)
        if st and sum(1 for s in st if s in ricset or RIC_RE.match(s)) >= max(1, 0.5 * len(st)):
            ric_col = j
            break
    if ric_col is None:
        errs = []
        for col in cols:
            errs += _errors(col)
        for ric in range_rics or []:
            for f in fields:
                out.append((ric, f, None, (errs or ["no output"])[0]))
        return out
    for r in range(len(rows)):
        ric = cols[ric_col][r]
        if not (isinstance(ric, str) and (ric.strip() in ricset or RIC_RE.match(ric.strip()))):
            continue
        for i, f in enumerate(fields):
            j = ric_col + 1 + i
            v = cols[j][r] if j < len(cols) else None
            d = as_date(v)
            if d is None and is_num(v) and 15000 <= v <= 80000:
                d = _EXCEL0 + dt.timedelta(days=int(v))
            err = v.strip()[:80] if isinstance(v, str) and d is None else ""
            out.append((ric.strip(), f, d, err))
    return out


def _range_values(wb_values, ref):
    """'Contracts!$B$5:$B$404' -> list of the cell values (strings) in that range, read from the saved workbook."""
    m = re.match(r"^'?([^'!]+)'?!\$?([A-Z]+)\$?(\d+):\$?([A-Z]+)\$?(\d+)$", ref.strip())
    if not m or m.group(1) not in wb_values:
        return []
    from openpyxl.utils import column_index_from_string as ci
    grid = wb_values[m.group(1)]
    c, r0, r1 = ci(m.group(2)) - 1, int(m.group(3)) - 1, int(m.group(5)) - 1
    return [str(grid[r][c]).strip() for r in range(r0, min(r1 + 1, len(grid)))
            if c < len(grid[r]) and grid[r][c] not in (None, "")]


def _contract_sheet(grid):
    """Optional 'Contracts' sheet (columns root, RIC, delivery YYYY-MM, form) -> {ric: (root, delivery)}."""
    out = {}
    for r in grid:
        if len(r) >= 3 and isinstance(r[1], str) and isinstance(r[2], str) and re.match(r"^\d{4}-\d{2}$", r[2].strip()):
            out[r[1].strip()] = (str(r[0]).strip(), r[2].strip())
    return out


def read_workbook(path, key, pull_date=None):
    """Read one saved pull workbook -> dict(entries, calendar, sheets, warnings, pull_date). Nothing is written."""
    import openpyxl
    name = os.path.basename(path)
    pull = pull_date or dt.datetime.fromtimestamp(os.path.getmtime(path)).date()
    res = {"key": key, "name": name, "path": path, "entries": [], "calendar": [], "sheets": [], "warnings": [],
           "pull_date": pull, "contracts": {}}
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    grids = {}
    for ws in wb.worksheets:
        grids[ws.title] = [list(r) for r in ws.iter_rows(values_only=True)]
    wb.close()
    if "Contracts" in grids:
        res["contracts"] = _contract_sheet(grids["Contracts"])
    for si, (title, grid) in enumerate(grids.items()):
        if title.strip().lower() in ("check", "contracts", "read me", "readme"):
            continue
        sh = {"sheet": title, "rows": len(grid), "blocks": 0, "status": Counter(), "calendar_rows": 0}
        if len(grid) < ROW_FORMULA:
            res["sheets"].append(sh)
            continue
        ids = grid[ROW_ID - 1]
        starts = [c for c, v in enumerate(ids) if isinstance(v, str) and PID.match(v.strip())]
        ncol = max((len(r) for r in grid), default=0)
        rows = grid[ROW0 - 1:]
        for q, c in enumerate(starts):
            c1 = starts[q + 1] if q + 1 < len(starts) else ncol
            bid = ids[c].strip()
            label = grid[ROW_LABEL - 1][c] if c < len(grid[ROW_LABEL - 1]) else ""
            ftxt = grid[ROW_FORMULA - 1][c] if c < len(grid[ROW_FORMULA - 1]) else None
            spec = parse_formula(ftxt)
            sh["blocks"] += 1
            if spec is None:
                res["warnings"].append("%s %s %s: formula not recognised, block skipped" % (key, title, bid))
                sh["status"]["unparsed"] += 1
                continue
            if spec["per"] == "S":                       # static request: contract dates (calendar rows)
                rics = _range_values(grids, spec["inst_range"]) if spec["inst_range"] else list(spec["codes"])
                for ric, f, d, err in read_calendar_block(rows, c, c1, spec, rics):
                    root, deliv = res["contracts"].get(ric, (None, None))
                    res["calendar"].append({"ric": ric, "root": root, "delivery": deliv, "field": f, "date": d,
                                            "error": err, "file": key, "sheet": title, "block": bid})
                    sh["calendar_rows"] += 1
                continue
            ents, info = read_block(rows, c, c1, spec)
            if info["extra_cols"]:
                res["warnings"].append("%s %s %s: %d more value columns than the formula names (ignored)" % (
                    key, title, bid, info["extra_cols"]))
            for e in ents:
                if e["status"] == "ok" and not spec["dated"]:
                    e["status"], e["n_undated"] = "no-dates", e["n_numbers"]
                    e["days"], e["vals"] = [], []
                e.update({"file": key, "file_name": name, "sheet": title, "block": bid, "label": str(label or "")[:80],
                          "fn": spec["fn"], "per": spec["per"], "_sheet_i": si, "_col": c})
                sh["status"][e["status"]] += 1
                res["entries"].append(e)
        sh["status"] = dict(sh["status"])
        res["sheets"].append(sh)
    return res


def clean_entry(e, pull_date):
    """Sort, drop rows after the pull day, weekend rows of daily series and repeated dates; monthly -> one row per
    month (the latest observation of the month). Sets n_future, n_weekend, n_collapsed and the arrays obs, key."""
    pairs = sorted(zip(e["days"], e["vals"]), key=lambda x: x[0])
    fut = [p for p in pairs if p[0] > pull_date]
    pairs = [p for p in pairs if p[0] <= pull_date]
    e["n_future"] = len(fut)
    wk = 0
    if e["per"] == "D":
        n0 = len(pairs)
        pairs = [p for p in pairs if p[0].weekday() < 5]
        wk = n0 - len(pairs)
    e["n_weekend"] = wk
    dedup = {}
    for d, v in pairs:
        k = month_end(d) if e["per"] == "M" else d
        dedup[k] = (d, v)                              # later observation of the same key wins
    e["n_collapsed"] = len(pairs) - len(dedup)
    keys = sorted(dedup)
    e["key"] = keys
    e["obs"] = [dedup[k][0] for k in keys]
    e["val"] = [dedup[k][1] for k in keys]
    return e


def _value_hash(e):
    v = np.asarray(e["val"], dtype="float64")
    a = np.abs(v)
    mag = np.where(a > 0, np.floor(np.log10(np.where(a > 0, a, 1.0))), 0.0)
    scale = 10.0 ** (8 - mag)
    r = np.round(v * scale) / scale
    h = hashlib.sha1(np.asarray([(k - _EPOCH).days for k in e["key"]], dtype="int64").tobytes())
    h.update(r.tobytes())
    return h.hexdigest()


def date_rule(obs):
    """Monthly observation dates -> 'calendar_me' (calendar month-end labels, weekends included), 'last_weekday'
    (Datastream), 'last_trading_or_other' (actual trading days, e.g. RDP.Data) or 'mixed'."""
    if not obs:
        return ""
    cal = sum(1 for d in obs if d == month_end(d))
    lwd = sum(1 for d in obs if d == last_weekday(d))
    n = len(obs)
    weekend_me = sum(1 for d in obs if d == month_end(d) and d.weekday() >= 5)
    if cal == n and weekend_me:
        return "calendar_me"
    if lwd == n:
        return "last_weekday"
    if cal >= 0.95 * n:
        return "calendar_me"
    if lwd >= 0.95 * n:
        return "last_weekday"
    return "last_trading_or_other"


# =====================================================================================================================
# configuration
# =====================================================================================================================
def load_config(cfg_dir=None):
    cfg, paths = {}, {}
    rows, paths["lseg_live_sources.csv"] = _read_csv("lseg_live_sources.csv", cfg_dir)
    cfg["live"] = {(r["file"].strip(), r["sheet"].strip(), (r.get("code") or "*").strip()):
                   (r["kind"].strip(), int(r["delay_days"]), (r.get("live") or "").strip()) for r in rows}
    rows, paths["lseg_exclusions.csv"] = _read_csv("lseg_exclusions.csv", cfg_dir)
    cfg["excl"] = [((r["fn"] or "*").strip(), r["code"].strip(), (r["field"] or "*").strip(), r["reason"].strip())
                   for r in rows]
    rows, paths["lseg_untouched.csv"] = _read_csv("lseg_untouched.csv", cfg_dir)
    cfg["untouched"] = [(re.compile(r["pattern"].strip()), r["reason"].strip()) for r in rows]
    rows, paths["lseg_engine_map.csv"] = _read_csv("lseg_engine_map.csv", cfg_dir)
    cfg["engine"] = {(r["series_id"].strip(), r["per"].strip()): (r["engine_id"].strip(), r["role"].strip())
                     for r in rows}
    rows, paths["lseg_roots.csv"] = _read_csv("lseg_roots.csv", cfg_dir)
    cfg["roots"] = {r["root"].strip(): r for r in rows}
    return cfg, paths


def _live_of(cfg, e):
    for k in ((e["file"], e["sheet"], e["code"]), (e["file"], e["sheet"], "*"), ("*", e["sheet"], "*"),
              (e["file"], "*", "*")):
        if k in cfg["live"]:
            return cfg["live"][k], True
    return ("market", DEFAULT_DELAY, ""), False


def _excluded(cfg, e):
    for fn, code, field, reason in cfg["excl"]:
        if (fn in ("*", e["fn"])) and norm_code(code) == norm_code(e["code"]) and field in ("*", e["field"]):
            return reason
    return ""


def _untouched(cfg, code):
    for rx, reason in cfg["untouched"]:
        if rx.search(norm_code(code)):
            return reason
    return ""


# =====================================================================================================================
# build
# =====================================================================================================================
def default_dirs():
    """PC default: <Documents>\\WRDS results\\lseg\\pull_2026-11-12 (cwd = ...\\WRDS results\\local) and the contract
    identity folder of the user's project drive. Env LSEG_DIRS (separated by ';') overrides."""
    env = os.environ.get("LSEG_DIRS") or os.environ.get("LSEG_DIR")
    if env:
        return [d for d in env.split(";") if d.strip()]
    return [os.path.join(os.path.dirname(os.getcwd()), "lseg", "pull_2026-11-12"),
            r"G:\My Drive\Screener project\LSEG\09_contract_identity"]


def assemble(reads, cfg):
    """Workbook reads (in key order) -> (entries with ids and statuses, calendar DataFrame, warnings, copy groups)."""
    warnings, entries, cal_rows = [], [], []
    missing_sheets = set()
    for res in reads:
        cal_rows += res["calendar"]
        for e in res["entries"]:
            if e["status"] == "ok":
                clean_entry(e, res["pull_date"])
                if not e["key"]:
                    e["status"] = "empty"
            for k in ("n_future", "n_weekend", "n_collapsed"):
                e.setdefault(k, 0)
            e.setdefault("key", [])
            e.setdefault("obs", [])
            e.setdefault("val", [])
            (kind, delay, live), known = _live_of(cfg, e)
            if not known:
                missing_sheets.add((e["file"], e["sheet"]))
            e["kind"], e["delay_days"], e["live"] = kind, delay, live
            e["wrong_reason"] = _excluded(cfg, e)
            if e["wrong_reason"]:
                e["status"] = "wrong-series"
            e["untouched_reason"] = _untouched(cfg, e["code"])
            e["untouched"] = int(bool(e["untouched_reason"]))
            e["copy_group"] = ""
            entries.append(e)
    for f, s in sorted(missing_sheets):
        warnings.append("sheet %s|%s not in lseg_live_sources.csv: kind market, delay %d day(s)" % (f, s, DEFAULT_DELAY))
    # ---- copies: identical arrays under COPY_MIN_CODES or more different instruments
    groups = defaultdict(list)
    for e in entries:
        if e["status"] == "ok" and len(e["val"]) >= COPY_MIN_VALUES:
            groups[(e["per"], _value_hash(e))].append(e)
    copies = []
    for (per, _), es in groups.items():
        inst = sorted({(norm_code(e["code"]), e["field"]) for e in es})
        if len(inst) >= COPY_MIN_CODES:
            for e in es:
                e["status"], e["copy_group"] = "copy", len(es)
            copies.append({"per": per, "blocks": len(es), "instruments": len(inst),
                           "examples": ["%s %s %s" % (e["file"], e["block"], e["code"]) for e in es[:8]]})
    # ---- series ids and duplicates
    byid = defaultdict(list)
    for e in entries:
        e["series_id"], e["duplicate_of"] = "", ""
        byid[(e["per"], "%s:%s|%s" % (e["fn"], e["code"], e["field"]))].append(e)
    used = set()
    for (per, base), es in byid.items():
        oks = [e for e in es if e["status"] == "ok"]
        if not oks:
            continue
        prim = sorted(oks, key=lambda e: (-len(e["val"]), key_order(e["file"]), e["_sheet_i"], e["_col"]))[0]
        for e in es:
            if e is not prim:
                e["duplicate_of"] = base
            if e["status"] != "ok":
                continue
            sid = base if e is prim else "%s#%s.%s" % (base, e["file"], e["block"])
            if (per, sid) in used:
                sid += ".%d" % e["_col"]
            used.add((per, sid))
            e["series_id"] = sid
    # ---- engine ids, date rule, holidays, design counts
    for e in entries:
        eid, role = cfg["engine"].get((e["series_id"], e["per"]), ("", "")) if e["series_id"] and not \
            e["duplicate_of"] else ("", "")
        e["engine_id"], e["engine_role"] = eid, role
        obs = e["obs"]
        e["hol"] = [hol_flag(d) for d in obs]
        des = [i for i, d in enumerate(obs) if d <= SEAL_DATE.date()]
        e["n_design"], e["n_sealed"] = len(des), len(obs) - len(des)
        e["first"] = obs[0].isoformat() if obs else ""
        e["last"] = obs[-1].isoformat() if obs else ""
        e["last_design"] = obs[des[-1]].isoformat() if des else ""
        e["date_rule"] = date_rule([obs[i] for i in des]) if e["per"] == "M" else ("daily" if obs else "")
        e["n_hol_design"] = sum(1 for i in des if e["hol"][i]) if e["per"] == "M" else 0
    cal = calendar_frame(cal_rows)
    return entries, cal, warnings, copies


def calendar_frame(rows):
    """Calendar rows -> one row per contract: root, delivery, ric, listed, and one date column per role."""
    if not rows:
        return pd.DataFrame(columns=["root", "delivery", "ric", "listed", "n_fields_ok"] + list(CAL_ROLES))
    recs = {}
    for r in rows:
        ric = r["ric"]
        root, deliv = r.get("root"), r.get("delivery")
        if not root or not deliv:
            m = RIC_RE.match(ric)
            if not m or m.group(4) is None:
                continue                              # no Contracts sheet row and not an expired-form RIC
            dec = int(m.group(4))
            year = (1900 if dec >= 5 else 2000) + 10 * dec + int(m.group(3))
            root = root or m.group(1)
            deliv = deliv or "%d-%02d" % (year, MONTH_CODES.index(m.group(2)) + 1)
        k = (root, deliv, ric)
        rec = recs.setdefault(k, {"root": root, "delivery": deliv, "ric": ric, "n_fields_ok": 0,
                                  **{c: None for c in CAL_ROLES}})
        role = ROLE_OF_FIELD.get(r["field"].upper())
        if r["date"] is not None:
            rec["n_fields_ok"] += 1
            if role and rec[role] is None:
                rec[role] = r["date"]
    if not recs:
        return calendar_frame([])
    df = pd.DataFrame(list(recs.values()))
    df["listed"] = df["n_fields_ok"] > 0
    for c in CAL_ROLES:
        df[c] = pd.to_datetime(df[c])
    df = df.dropna(subset=["delivery"])
    # one row per (root, delivery): a listed RIC beats an unlisted alias (expired / live forms of one contract)
    df = df.sort_values(["root", "delivery", "listed", "n_fields_ok", "ric"], ascending=[True, True, False, False, True])
    df = df.drop_duplicates(["root", "delivery"], keep="first").reset_index(drop=True)
    return df[["root", "delivery", "ric", "listed", "n_fields_ok"] + list(CAL_ROLES)]


def calendar_raw(rows):
    """Every static (calendar / identity probe) row as read: file, sheet, block, ric, field, date, error."""
    cols = ["file", "sheet", "block", "ric", "field", "date", "error"]
    df = pd.DataFrame([[r[c] for c in cols] for r in rows], columns=cols) if rows else pd.DataFrame(columns=cols)
    df["date"] = pd.to_datetime(df["date"]).astype("datetime64[ns]")
    for c in ("file", "sheet", "block", "ric", "field", "error"):
        df[c] = df[c].astype(str)
    return df.sort_values(["file", "sheet", "block", "ric", "field"], kind="mergesort").reset_index(drop=True)


def long_frame(entries, part):
    """Stored (ok) entries -> long table of the design (obs <= seal) or sealed (obs > seal) part, sorted."""
    sid, per, obs, key, val, hol = [], [], [], [], [], []
    seal = SEAL_DATE.date()
    for e in entries:
        if not e["series_id"]:
            continue
        for d, k, v, h in zip(e["obs"], e["key"], e["val"], e["hol"]):
            if (d <= seal) == (part == "design"):
                sid.append(e["series_id"])
                per.append(e["per"])
                obs.append(d)
                key.append(k)
                val.append(v)
                hol.append(h)
    df = pd.DataFrame({"sid": pd.Series(sid, dtype="object"), "per": pd.Series(per, dtype="object"),
                       "obs": pd.to_datetime(pd.Series(obs, dtype="object")).astype("datetime64[ns]"),
                       "key": pd.to_datetime(pd.Series(key, dtype="object")).astype("datetime64[ns]"),
                       "value": pd.Series(val, dtype="float64"), "hol": pd.Series(hol, dtype="int8")})
    return df.sort_values(["per", "sid", "obs"], kind="mergesort").reset_index(drop=True)


def _table_meta(df, datecol="obs"):
    return {"content_sha256": content_sha256(df), "rows": int(len(df)),
            "series": int(df["sid"].nunique()) if "sid" in df else 0,
            "first": df[datecol].min().strftime("%Y-%m-%d") if len(df) else "",
            "last": df[datecol].max().strftime("%Y-%m-%d") if len(df) else ""}


def build(dirs, work_dir, cfg_dir=None):
    """Read all L workbooks in dirs, write catalog, design and sealed tables, calendar, manifest, LOCK and lock.json.
    Returns a metadata report (no data value)."""
    t0 = time.time()
    cfg, cpaths = load_config(cfg_dir)
    files, cands, warnings = find_workbooks(dirs)
    reads, rep = [], {"files": [], "sheets": [], "candidates": cands, "dirs": [(d, os.path.isdir(d)) for d in dirs]}
    for k, p in files.items():
        t1 = time.time()
        try:
            r = read_workbook(p, k)
        except Exception as ex:  # noqa: BLE001
            warnings.append("file %s could not be read: %s %s" % (os.path.basename(p), type(ex).__name__, str(ex)[:160]))
            continue
        warnings += r["warnings"]
        reads.append(r)
        rep["files"].append({"key": k, "name": r["name"], "kb": os.path.getsize(p) // 1024,
                             "pull_date": r["pull_date"].isoformat(), "seconds": round(time.time() - t1, 1),
                             "entries": len(r["entries"]), "calendar_rows": len(r["calendar"])})
        for sh in r["sheets"]:
            rep["sheets"].append(dict(sh, file=k))
    entries, cal, w2, copies = assemble(reads, cfg)
    warnings += w2
    rep["copies"] = copies
    design, sealed = long_frame(entries, "design"), long_frame(entries, "sealed")

    root = os.path.join(work_dir, "lseg")
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
        for n in ("manifest.json", "catalog.csv", "LOCK", "lock.json"):
            if os.path.exists(os.path.join(root, n)):
                shutil.move(os.path.join(root, n), os.path.join(hd, n))
    tables = {}
    for part, df in (("design", design), ("sealed", sealed)):
        os.makedirs(os.path.join(root, part), exist_ok=True)
        p = os.path.join(root, part, "long.pkl")
        df.to_pickle(p + ".tmp")
        os.replace(p + ".tmp", p)
        tables["%s/long.pkl" % part] = _table_meta(df)
    calp = os.path.join(root, "calendar.pkl")
    cal.to_pickle(calp + ".tmp")
    os.replace(calp + ".tmp", calp)
    tables["calendar.pkl"] = {"content_sha256": content_sha256(cal), "rows": int(len(cal)),
                              "series": int(cal["root"].nunique()) if len(cal) else 0, "first": "", "last": ""}
    raw = calendar_raw([c for r in reads for c in r["calendar"]])
    rawp = os.path.join(root, "calendar_raw.pkl")
    raw.to_pickle(rawp + ".tmp")
    os.replace(rawp + ".tmp", rawp)
    tables["calendar_raw.pkl"] = {"content_sha256": content_sha256(raw), "rows": int(len(raw)), "series": 0,
                                  "first": "", "last": ""}
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(CATALOG_COLUMNS)
    for e in entries:
        w.writerow([e.get(k, "") for k in CATALOG_COLUMNS])
    cat_bytes = buf.getvalue().encode("utf-8")
    with open(os.path.join(root, "catalog.csv"), "wb") as f:
        f.write(cat_bytes)
    stored = [e for e in entries if e["series_id"]]
    counts = {"expected_series": len(entries), "status": dict(Counter(e["status"] for e in entries)),
              "status_by_file": {r["key"]: dict(Counter(e["status"] for e in entries if e["file"] == r["key"]))
                                 for r in reads},
              "stored": {"M": sum(1 for e in stored if e["per"] == "M"), "D": sum(1 for e in stored if e["per"] == "D")},
              "duplicates_stored": sum(1 for e in stored if e["duplicate_of"]),
              "untouched_series": sum(1 for e in stored if e["untouched"]),
              "engine_mapped": sum(1 for e in stored if e["engine_id"]),
              "rows_dropped": {"future": sum(e["n_future"] for e in entries), "weekend": sum(e["n_weekend"] for e in entries),
                               "undated": sum(e["n_undated"] for e in entries),
                               "collapsed": sum(e["n_collapsed"] for e in entries)},
              "copy_groups": copies, "calendar_contracts": int(len(cal)),
              "calendar_listed": int(cal["listed"].sum()) if len(cal) else 0}
    manifest = {
        "code_version": VERSION, "code_sha256": sha256_file(os.path.abspath(__file__)),
        "build_time": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "seal_date": SEAL_DATE.strftime("%Y-%m-%d"),
        "workbooks": {k: {"name": os.path.basename(p), "sha256": sha256_file(p), "size": os.path.getsize(p),
                          "mtime": dt.datetime.fromtimestamp(int(os.path.getmtime(p)), dt.timezone.utc)
                          .strftime("%Y-%m-%dT%H:%M:%SZ")} for k, p in files.items()},
        "config": {n: sha256_file(p) for n, p in sorted(cpaths.items())},
        "tables": tables,
        "catalog": {"file": "catalog.csv", "sha256": hashlib.sha256(cat_bytes).hexdigest(), "rows": len(entries)},
        "counts": counts, "warnings": sorted(set(warnings)),
    }
    with open(os.path.join(root, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, sort_keys=True)
    lock = lock_id_of(manifest)
    with open(os.path.join(root, "LOCK"), "w", encoding="utf-8") as f:
        f.write(lock + "\n")
    lockdoc = {"version": "lseg-v1", "lock_id": lock, "seal_date": manifest["seal_date"],
               "code": {"version": VERSION, "sha256": manifest["code_sha256"]},
               "built": manifest["build_time"], "workbooks": manifest["workbooks"], "config": manifest["config"],
               "tables": {k: {kk: v[kk] for kk in ("content_sha256", "rows", "series")} for k, v in tables.items()},
               "counts": {k: v for k, v in counts.items() if k != "copy_groups"},
               "series": {"%s|%s" % (e["per"], e["series_id"]): [e["first"] if e["n_design"] else "", e["last_design"],
                                                                 e["n_design"], e["n_sealed"]]
                          for e in stored}}
    with open(os.path.join(root, "lock.json"), "w", encoding="utf-8") as f:
        json.dump(lockdoc, f, indent=1, sort_keys=True)
    rep.update({"manifest": manifest, "lock_id": lock, "seconds": round(time.time() - t0, 1), "entries": entries,
                "calendar": cal, "warnings": sorted(set(warnings))})
    return rep


# =====================================================================================================================
# access
# =====================================================================================================================
def _log(root, msg):
    with open(os.path.join(root, "sealed_access.log"), "a", encoding="utf-8") as f:
        f.write("%s\t%s\n" % (dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), msg))


def read_catalog(work_dir):
    cat = pd.read_csv(os.path.join(work_dir, "lseg", "catalog.csv"), dtype=str, keep_default_na=False)
    for c in ("n_numbers", "n_undated", "n_future", "n_weekend", "n_collapsed", "n_design", "n_sealed", "delay_days",
              "untouched", "n_hol_design"):
        cat[c] = pd.to_numeric(cat[c], errors="coerce").fillna(0).astype(int)
    return cat


class Panel:
    """As-of access to the locked LSEG tables. See the module docstring."""

    def __init__(self, work_dir, allow_untouched=False, holdout_key=None, live=False):
        self.work_dir = work_dir
        self.root = os.path.join(work_dir, "lseg")
        with open(os.path.join(self.root, "manifest.json"), encoding="utf-8") as f:
            self.manifest = json.load(f)
        self.lock_id = lock_id_of(self.manifest)
        with open(os.path.join(self.root, "LOCK"), encoding="utf-8") as f:
            if f.read().strip() != self.lock_id:
                raise RuntimeError("LOCK does not match manifest.json: rebuild")
        with open(os.path.join(self.root, "catalog.csv"), "rb") as f:
            if hashlib.sha256(f.read()).hexdigest() != self.manifest["catalog"]["sha256"]:
                raise RuntimeError("catalog.csv does not match the manifest: rebuild")
        cat = read_catalog(work_dir)
        self.holdout, self.live = False, bool(live)
        if holdout_key is not None:
            hk = hashlib.sha256(str(holdout_key).encode()).hexdigest()
            if HOLDOUT_KEY_SHA256 is None or hk != HOLDOUT_KEY_SHA256:
                _log(self.root, "holdout key attempt %s: refused" % hk[:8])
                raise HoldoutSealed("no holdout key is registered or the key is wrong: the sealed table stays closed")
            _log(self.root, "holdout key attempt %s: GRANTED, lock %s" % (hk[:8], self.lock_id[:12]))
            self.holdout = True
        if self.live:
            if LIVE_START is None:
                _log(self.root, "live mode refused (LIVE_START not registered)")
                raise HoldoutSealed("live mode: LIVE_START is not registered (gm/CHANGES.md LSEG data entry)")
            _log(self.root, "live mode opened, lock %s" % self.lock_id[:12])
        parts = ["design"] + (["sealed"] if (self.holdout or self.live) else [])
        dfs = []
        for part in parts:
            df = pd.read_pickle(os.path.join(self.root, part, "long.pkl"))
            if content_sha256(df) != self.manifest["tables"]["%s/long.pkl" % part]["content_sha256"]:
                raise RuntimeError("%s/long.pkl does not match the manifest: rebuild" % part)
            dfs.append(df)
        if self.live:
            lv = live_table(work_dir)
            if len(lv):
                dfs.append(lv[["sid", "per", "obs", "key", "value", "hol"]])
        long = pd.concat(dfs, ignore_index=True) if len(dfs) > 1 else dfs[0]
        self.allow_untouched = allow_untouched
        if not allow_untouched:
            hidden = set(cat.loc[(cat["untouched"] == 1) & (cat["series_id"] != ""), "series_id"])
            long = long[~long["sid"].isin(hidden)]
            cat = cat[cat["untouched"] == 0]
        self.catalog = cat.reset_index(drop=True)
        delay = {(r.per, r.series_id): int(r.delay_days) for r in self.catalog.itertuples() if r.series_id}
        self._data = {}
        for (per, sid), g in long.groupby(["per", "sid"], sort=False):
            g = g.sort_values("obs", kind="mergesort").drop_duplicates("obs", keep="last")
            obs = g["obs"].to_numpy(dtype="datetime64[ns]")
            d = delay.get((per, sid), DEFAULT_DELAY)          # a live-only series (not in the catalog): default
            self._data[(per, sid)] = (obs, g["key"].to_numpy(dtype="datetime64[ns]"), g["value"].to_numpy(),
                                      obs + np.timedelta64(int(d), "D"))
        cpath = os.path.join(self.root, "calendar.pkl")
        self.calendar = pd.read_pickle(cpath) if os.path.exists(cpath) else None

    def ids(self, per=None, fn=None, code=None, field=None, engine_id=None, duplicates=False):
        c = self.catalog[self.catalog["series_id"] != ""]
        for col, v in (("per", per), ("fn", fn), ("code", code), ("field", field), ("engine_id", engine_id)):
            if v is not None:
                c = c[c[col] == v]
        if not duplicates:
            c = c[c["duplicate_of"] == ""]
        return list(c["series_id"])

    def _per(self, sid, per):
        if per is not None:
            if (per, sid) not in self._data:
                raise KeyError("%s (%s) not found or hidden (untouched)" % (sid, per))
            return per
        have = [p for p in ("M", "D") if (p, sid) in self._data]
        if not have:
            raise KeyError("%s not found or hidden (untouched)" % sid)
        if len(have) > 1:
            raise ValueError("%s exists monthly and daily: pass per='M' or per='D'" % sid)
        return have[0]

    def asof(self, date):
        d = pd.Timestamp(date).normalize()
        if self.live:
            if d < pd.Timestamp(LIVE_START):
                _log(self.root, "live asof %s refused (before LIVE_START)" % d.date())
                raise HoldoutSealed("live mode answers only as-of dates on or after LIVE_START")
        elif d > SEAL_DATE and not self.holdout:
            _log(self.root, "asof %s refused (after seal date %s)" % (d.date(), SEAL_DATE.date()))
            raise HoldoutSealed("asof(%s): dates after %s are sealed" % (d.date(), SEAL_DATE.date()))
        return AsOf(self, d)


class AsOf:
    """What was knowable on one date: observations dated <= date whose availability (obs + delay) is <= date."""

    def __init__(self, panel, date):
        self.panel, self.date = panel, date
        self._d = np.datetime64(date.to_datetime64(), "ns")

    def _mask(self, sid, per):
        per = self.panel._per(sid, per)
        obs, key, val, av = self.panel._data[(per, sid)]
        return per, (obs <= self._d) & (av <= self._d), obs, key, val, av

    def series(self, sid, per=None):
        """Known observations indexed by their observation date (never after the as-of date)."""
        _, m, obs, _, val, _ = self._mask(sid, per)
        return pd.Series(val[m], index=pd.DatetimeIndex(obs[m]), name=sid)

    def monthly(self, sid, per=None):
        """Known observations indexed by month-end label (daily series: the last known observation of each month)."""
        per, m, obs, key, val, _ = self._mask(sid, per)
        s = pd.Series(val[m], index=pd.DatetimeIndex(obs[m]), name=sid)
        if not len(s):
            return s
        lab = s.index.to_period("M").to_timestamp(how="end").normalize()
        s.index = lab
        return s[~s.index.duplicated(keep="last")]

    def known(self, sid, per=None):
        """Known observations indexed by the day each became known."""
        _, m, obs, _, val, av = self._mask(sid, per)
        s = pd.Series(val[m], index=pd.DatetimeIndex(av[m]), name=sid)
        return s[~s.index.duplicated(keep="last")]

    def last(self, sid, per=None):
        s = self.series(sid, per)
        return (s.index[-1], s.iloc[-1]) if len(s) else (None, np.nan)

    def frame(self, sids, per="M", how="monthly"):
        get = {"monthly": self.monthly, "series": self.series, "known": self.known}[how]
        return pd.DataFrame({s: get(s, per) for s in sids})


def load_design(work_dir, allow_untouched=True):
    """Catalog, the raw DESIGN long table (no as-of shifting, lock verified) and the lock id, for the data check."""
    p = Panel(work_dir, allow_untouched=allow_untouched)
    long = pd.read_pickle(os.path.join(p.root, "design", "long.pkl"))
    if not allow_untouched:
        long = long[long["sid"].isin(set(p.catalog["series_id"]))]
    return p.catalog, long, p.lock_id, p.calendar


# =====================================================================================================================
# contract identity
# =====================================================================================================================
def roots_config(cfg_dir=None):
    rows, _ = _read_csv("lseg_roots.csv", cfg_dir)
    return {r["root"].strip(): r for r in rows}


def positions(txt):
    """'1-24;36' -> [1, ..., 24, 36]."""
    out = []
    for part in (txt or "").replace(",", ";").split(";"):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def root_positions(root_cfg, per):
    """Continuous positions of a root held in the pull files (L4/L5/L10 plus L11), monthly or daily."""
    if per == "M":
        return sorted(set(positions(root_cfg.get("depth_m")) + positions(root_cfg.get("depth_m_l11"))))
    return sorted(set(positions(root_cfg.get("positions_d")) + positions(root_cfg.get("positions_d_l11"))))


def c_series_id(root_cfg, n, per):
    """Series id of position n of a root's continuous series in the pull files (monthly or daily template)."""
    tmpl = root_cfg["c_sid_" + ("m" if per == "M" else "d")].strip()
    return tmpl.replace("{n}", str(n)) if tmpl else ""


class Calendar:
    """Contract calendar + roll rule -> which contract a continuous position held on a day."""

    def __init__(self, cal, roots):
        self.cal = cal if cal is not None else pd.DataFrame(columns=["root", "delivery", "ric", "listed"] +
                                                              list(CAL_ROLES))
        self.roots = roots
        self._by = {}
        for r, g in self.cal[self.cal["listed"] == True].groupby("root"):  # noqa: E712
            self._by[r] = g.sort_values("delivery").reset_index(drop=True)

    def anchor_col(self, root):
        return (self.roots.get(root, {}).get("roll_on") or "last_trade").strip()

    def contracts(self, root):
        return self._by.get(root, self.cal.iloc[0:0])

    def listed_months(self, root):
        g = self.contracts(root)
        return "".join(sorted({MONTH_CODES[int(d[5:7]) - 1] for d in g["delivery"]}, key=MONTH_CODES.index))

    def _live(self, root, day):
        """Contracts not yet past their roll anchor on day, by delivery month; contracts without an anchor date are
        kept when they deliver from the month before day on (they may still be held)."""
        g = self.contracts(root)
        if not len(g):
            return g, None
        col = self.anchor_col(root)
        day = pd.Timestamp(day)
        dm = pd.PeriodIndex(g["delivery"], freq="M")
        keep = (g[col] >= day) | (g[col].isna() & (dm >= pd.Period(day, "M") - 1))
        return g[keep].reset_index(drop=True), col

    def held(self, root, n, day):
        """(ric, delivery, last_trade, first_notice, expiry) of the contract position n held on day, or None when the
        calendar cannot say (no rows, too few contracts, or a contract up to position n without its anchor date)."""
        live, col = self._live(root, day)
        if col is None or len(live) < n or live[col].iloc[:n].isna().any():
            return None
        r = live.iloc[n - 1]
        return (r["ric"], r["delivery"], r["last_trade"], r["first_notice"], r["expiry"])

    def position_of(self, root, ric, day):
        """Position n that contract ric occupies on day under the rule (None if not held or unknown)."""
        live, col = self._live(root, day)
        if col is None:
            return None
        hit = live.index[live["ric"] == ric]
        if not len(hit) or live[col].iloc[:hit[0] + 1].isna().any():
            return None
        return int(hit[0]) + 1


# =====================================================================================================================
# weekly live store
# =====================================================================================================================
LIVE_COLUMNS = ["sid", "per", "obs", "key", "value", "hol", "ingest", "ingest_time"]


def live_table(work_dir):
    p = os.path.join(work_dir, "lseg", "live", "live_long.pkl")
    if not os.path.exists(p):
        return pd.DataFrame({c: pd.Series(dtype=t) for c, t in zip(
            LIVE_COLUMNS, ["object", "object", "datetime64[ns]", "datetime64[ns]", "float64", "int8", "int64",
                           "object"])})
    return pd.read_pickle(p)


def live_ingest(path, work_dir, cfg_dir=None, now=None):
    """Append the rows of one saved weekly workbook to the live store. Returns a metadata report."""
    root = os.path.join(work_dir, "lseg", "live")
    os.makedirs(root, exist_ok=True)
    sha = sha256_file(path)
    logp = os.path.join(root, "ingests.csv")
    log = []
    if os.path.exists(logp):
        with open(logp, newline="", encoding="utf-8") as f:
            log = list(csv.DictReader(f))
    rep = {"file": os.path.basename(path), "sha256": sha,
           "saved": dt.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M"),
           "already": any(r["sha256"] == sha for r in log), "warnings": []}
    if rep["already"]:
        return rep
    cfg, _ = load_config(cfg_dir)
    r = read_workbook(path, "W")
    rep["warnings"] += r["warnings"]
    entries, cal, w2, copies = assemble([r], cfg)
    rep["warnings"] += [w for w in w2 if "not in lseg_live_sources" not in w]
    rep["entries"], rep["calendar"], rep["copies"] = entries, cal, copies
    now = now or dt.datetime.now()
    ingest = len(log) + 1
    old = live_table(work_dir)
    seen = {(a, b, c): v for a, b, c, v in zip(old["sid"], old["per"], old["obs"], old["value"])}
    rows, added, revised, refused = [], Counter(), Counter(), 0
    for e in entries:
        if e["status"] != "ok":
            continue
        sid = e["series_id"]
        for d, k, v, h in zip(e["obs"], e["key"], e["val"], e["hol"]):
            if d <= SEAL_DATE.date():
                refused += 1
                continue
            ts = pd.Timestamp(d)
            prev = seen.get((sid, e["per"], ts))
            if prev is not None and prev == v:
                continue
            (revised if prev is not None else added)[(sid, e["per"])] += 1
            rows.append((sid, e["per"], ts, pd.Timestamp(k), v, h, ingest, now.strftime("%Y-%m-%dT%H:%M:%S")))
    new = pd.DataFrame(rows, columns=LIVE_COLUMNS)
    if len(new):
        new["obs"] = new["obs"].astype("datetime64[ns]")
        new["key"] = new["key"].astype("datetime64[ns]")
        new["hol"] = new["hol"].astype("int8")
        new["ingest"] = new["ingest"].astype("int64")
    tab = pd.concat([old, new], ignore_index=True) if len(old) else new
    p = os.path.join(root, "live_long.pkl")
    tab.to_pickle(p + ".tmp")
    os.replace(p + ".tmp", p)
    if r["calendar"]:                                  # identity of the live continuous positions, as LSEG states it
        cp = os.path.join(root, "identity_live.csv")
        new_file = not os.path.exists(cp)
        with open(cp, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new_file:
                w.writerow(["ingest", "saved", "ric", "field", "date", "error"])
            for c in r["calendar"]:
                w.writerow([ingest, rep["saved"], c["ric"], c["field"], c["date"].isoformat() if c["date"] else "",
                            c["error"]])
    rep["identity_rows"] = r["calendar"]
    line = {"ingest": ingest, "time": now.strftime("%Y-%m-%dT%H:%M:%S"), "file": rep["file"], "sha256": sha,
            "saved": rep["saved"], "rows_added": sum(added.values()), "rows_revised": sum(revised.values()),
            "rows_refused_sealed": refused, "table_sha256": content_sha256(tab[LIVE_COLUMNS[:6]]) if len(tab) else ""}
    with open(logp, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(line))
        if not log:
            w.writeheader()
        w.writerow(line)
    rep.update({"ingest": ingest, "added": added, "revised": revised, "refused": refused, "table_rows": len(tab),
                "log": line})
    return rep
