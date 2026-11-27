"""card_inputs: reader of the locked card inputs (gm/CHANGES.md data entry "card inputs (FRED / ALFRED first release,
macro-data branch)", 2026-11-27; lock docs/research/card_inputs/LOCK_CARD_v1.json). Stdlib + numpy + pandas.

The zip work\\free\\gm_card_inputs.zip (tools/bbgq/build_card_inputs.py, from git at the registered commit) holds the
raw files whole; Inputs.from_zip checks every file's sha256 against FILES and the lock id before a value is parsed.
Every observation dated after 2010-12-31 is dropped on parsing (entry item 3).

  Inputs.from_zip(path) / Inputs.from_files({path: bytes})     verified inputs (raises CardInputsError)
  ci.m(sid)              monthly Period series at its registered release lag (daily series: monthly mean)
  ci.fr_level(sid)       (values, flagged) first published where a vintage exists, else latest; lagged
  ci.fr_change(sid, k)   (k-month % change, flagged) by entry item 5; lagged
  ci.breaks(sid)         first-release level breaks (months) by entry item 5
"""
import csv
import hashlib
import io
import json
import zipfile

import numpy as np
import pandas as pd

VERSION = "card_inputs-1.0.0"
SOURCE = "origin/macro-data"
COMMIT = "264d0a2cc2f74d02264b30a52d5e8f0950db9cca"
SEAL_DATE = "2010-12-31"
SEAL = pd.Timestamp(SEAL_DATE)
FILES = {
    "GS1.csv": "3ab25da1ce76f092ada31ea7ea83c89b98c7facbb7523049d5c504564c4ee7df",
    "GS2.csv": "c92b08197af1084e93f09a06bd0fd5620e2a9eacb2f9e1956bd71fe250063dc9",
    "GS5.csv": "4097a254739c4a69ae6b564f063ec1800986d40c56b3b5647264fd481ecb89b7",
    "GS10.csv": "14101ef859fbbacf0f0be00bc7a7ad70eea56b640a7a33b41a19982519639c60",
    "FEDFUNDS.csv": "1febfbfd22ef4d1e354d412ab224009f9df4214fd880e60e3b1d3d6f22798573",
    "BAA.csv": "a19a4e7230f5dbf42ad2b056b7b13a8cee53307f1ae893fb073d829a6e0f8f1c",
    "TWEXMMTH.csv": "a5c1ea123197ae46207e489052debaf4cc1309d734a356eeff3900717dc7d33e",
    "DTWEXBGS.csv": "d1c0528a9e337567a70a576a2721829446551d1d6e00a1e7d6197723dfb1e33d",
    "WTISPLC.csv": "0f917359164123db1598402e455c1694e8c639fe58b9cc8e66ba03bcc3d5f4ef",
    "VIXCLS.csv": "1c4696be0611e16d07d696bced9182b5dada3fc0e0850ea7b63bb25941efaaf4",
    "M2SL.csv": "871ca3301a05ad1b462fb26edc408a8eeeb9d14a6e6f3b9a564c0825a80074bf",
    "PCEPILFE.csv": "2580087dc66e991d6e4275d7602ebd3bd8c96963eb87d157ceb9bca4e0590a18",
    "manifest.json": "2d0213bd625eb5b71d8aa8249971b225b002d32e3410defff22cdb1fb4025561",
    "research/CPILFESL_FR.csv": "32f8c0ab27789d3cafac39644cfd239ca62846cb67c440eaf50fb02b7edc75a8",
    "research/UNRATE_FR.csv": "32a5962ede84fe0a42e7b1dac474dc91ba326432881878d7470a3777328295b0",
    "research/CPILFESL.csv": "90d152a56c2be24e3a595308feff963d22c8431dda24cc9f948c12c420a19a50",
    "research/UNRATE.csv": "65fb73bccaa4086aaaf3d19fbae5802daa62401ea3383322c1c5046468757c45",
    "research/M2SL.csv": "c745c8995d819bbee56d32156cd1e3c514db199df23606886ad7aef0cc0b4a9d",
    "research/PCEPILFE.csv": "cdf87be0d6669f8346c08b853b3b78bf669f84f9a6f028208b24587a641271f3",
}
# entry item 2: the file of each input
PLAIN = {"GS1": "GS1.csv", "GS2": "GS2.csv", "GS5": "GS5.csv", "GS10": "GS10.csv", "FEDFUNDS": "FEDFUNDS.csv",
         "BAA": "BAA.csv", "TWEXMMTH": "TWEXMMTH.csv", "DTWEXBGS": "DTWEXBGS.csv", "WTISPLC": "WTISPLC.csv",
         "VIXCLS": "VIXCLS.csv"}
FIRST = {"CPILFESL": "research/CPILFESL_FR.csv", "UNRATE": "research/UNRATE_FR.csv", "M2SL": "M2SL.csv",
         "PCEPILFE": "PCEPILFE.csv"}
LATEST = {"CPILFESL": "research/CPILFESL.csv", "UNRATE": "research/UNRATE.csv", "M2SL": "research/M2SL.csv",
          "PCEPILFE": "research/PCEPILFE.csv"}
DAILY = ("DTWEXBGS", "VIXCLS")
# entry item 4: release lag in months
LAG = {"FEDFUNDS": 0, "GS1": 0, "GS2": 0, "GS5": 0, "GS10": 0, "BAA": 0, "TWEXMMTH": 0, "DTWEXBGS": 0, "VIXCLS": 0,
       "WTISPLC": 1, "CPILFESL": 1, "M2SL": 1, "UNRATE": 1, "PCEPILFE": 2}
BREAK_PP = 0.02          # entry item 5: 2 percentage points


class CardInputsError(RuntimeError):
    pass


def lock_id(files=None):
    files = files or FILES
    return hashlib.sha256(json.dumps({"source": SOURCE, "commit": COMMIT, "seal_date": SEAL_DATE, "files": files},
                                     sort_keys=True).encode()).hexdigest()


LOCK_ID = lock_id()


def parse_csv(raw):
    """date,value csv bytes -> DatetimeIndex Series, observations dated after 2010-12-31 dropped (entry item 3)."""
    txt = raw.decode("utf-8", errors="replace").replace("\r", "")
    d, v = [], []
    for row in list(csv.reader(io.StringIO(txt)))[1:]:
        if len(row) < 2 or row[1].strip() in ("", "."):
            continue
        try:
            t = pd.Timestamp(row[0].strip())
            x = float(row[1])
        except (ValueError, TypeError):
            continue
        if t <= SEAL:
            d.append(t)
            v.append(x)
    s = pd.Series(v, index=pd.DatetimeIndex(d), dtype=float)
    return s[~s.index.duplicated(keep="last")].sort_index()


def to_month(s, daily=False):
    p = s.index.to_period("M")
    g = pd.Series(s.values, index=p).groupby(level=0)
    return (g.mean() if daily else g.last()).sort_index()


class Inputs:
    def __init__(self, files):
        miss = sorted(set(FILES) - set(files))
        extra = sorted(set(files) - set(FILES))
        bad = sorted(k for k in FILES if k in files and hashlib.sha256(files[k]).hexdigest() != FILES[k])
        if miss or extra or bad:
            raise CardInputsError("card inputs differ from LOCK_CARD_v1: missing %s, extra %s, changed %s" % (
                miss or "none", extra or "none", bad or "none"))
        self.lock_id = LOCK_ID
        self._raw = {k: parse_csv(files[k]) for k in FILES if k.endswith(".csv")}
        self._cache = {}

    @classmethod
    def from_zip(cls, path):
        with zipfile.ZipFile(path) as z:
            files = {n: z.read(n) for n in z.namelist() if not n.endswith("/")}
        return cls(files)

    @classmethod
    def from_files(cls, files):
        return cls(files)

    def _month(self, path, sid):
        return to_month(self._raw[path], daily=sid in DAILY)

    def m(self, sid):
        """Monthly series at its release lag (value at t = observation of month t - lag)."""
        if sid in PLAIN:
            s = self._month(PLAIN[sid], sid)
        else:
            s = self.fr_level(sid)[0]
            return s
        s.index = s.index + LAG[sid]
        return s

    def _pair(self, sid):
        f = self._month(FIRST[sid], sid)
        lt = self._month(LATEST[sid], sid)
        idx = f.index.union(lt.index)
        return f.reindex(idx), lt.reindex(idx)

    def breaks(self, sid):
        f, lt = self._pair(sid)
        d = (f / f.shift(1) - 1) - (lt / lt.shift(1) - 1)
        return [p for p, v in d.items() if v == v and abs(v) > BREAK_PP]

    def fr_level(self, sid):
        f, lt = self._pair(sid)
        val = f.combine_first(lt)
        flag = f.isna() & lt.notna()
        val.index = val.index + LAG[sid]
        flag.index = flag.index + LAG[sid]
        return val, flag

    def fr_change(self, sid, k):
        """k-month % change (entry item 5): two comparable first-release values, else the latest values (flagged)."""
        key = (sid, k)
        if key in self._cache:
            return self._cache[key]
        f, lt = self._pair(sid)
        br = pd.Series(0.0, index=f.index)
        for b in self.breaks(sid):
            br[b] = 1.0
        inside = br.rolling(k, min_periods=1).sum() > 0          # a break in m-k+1 .. m
        cf = 100.0 * (f / f.shift(k) - 1)
        cl = 100.0 * (lt / lt.shift(k) - 1)
        use_f = cf.notna() & ~inside
        val = cf.where(use_f, cl)
        flag = ~use_f & cl.notna()
        val.index = val.index + LAG[sid]
        flag.index = flag.index + LAG[sid]
        self._cache[key] = (val, flag)
        return val, flag

    def flagged_share(self, sid, k=None, a="1975-01", b="2010-12"):
        v, fl = self.fr_change(sid, k) if k else self.fr_level(sid)
        w = (v.index >= pd.Period(a, "M")) & (v.index <= pd.Period(b, "M")) & v.notna().to_numpy()
        n = int(w.sum())
        return (float(fl[w].sum()) / n if n else float("nan")), n
