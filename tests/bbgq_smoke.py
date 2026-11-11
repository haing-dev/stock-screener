"""Smoke test for tools/bbgq (Bloomberg block 2: reader, data check, lock and seal).

Builds mock workbooks from the real templates (docs/data_requests/Bloomberg_macro_UBC.xlsx and
docs/data_requests/bloomberg_v5/*.xlsx: same sheets, blocks, tickers and fields; random-walk values; error blocks;
serial dates in one sheet; release dates in three formats; dates through 2026) under the awkward real file names,
runs both jobs as subprocesses the way the PC runner does (cwd = local, BBG_DIR, BBG_WORK, PYTHONPATH = lib;pylib),
then checks the catalog, the seal, the as-of guard, untouched markets, the lock id and the export whitelist.

python3 tests/bbgq_smoke.py [--keep]     prints "BBGQ SMOKE OK"
"""
import datetime as dt
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

import numpy as np
import openpyxl
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BBGQ = os.path.join(REPO, "tools", "bbgq")
TEMPLATES = {"1": os.path.join(REPO, "docs", "data_requests", "Bloomberg_macro_UBC.xlsx")}
for _p in glob.glob(os.path.join(REPO, "docs", "data_requests", "bloomberg_v5", "*.xlsx")):
    TEMPLATES[os.path.basename(_p)[0]] = _p
REAL_NAMES = {"1": "1_Bloomberg_macro_UBC_6 1.xlsx", "2": "2_Bloomberg_econ_policy_monthly (1).xlsx",
              "3": "3_Bloomberg_rates_credit_fx_monthly_6 1.xlsx", "4": "4_Bloomberg_equity_vol_funds_monthly_5 1.xlsx",
              "5": "5_Bloomberg_commodities_ext_monthly_5 1.xlsx", "6": "6_Bloomberg_daily_A_futures_fx_5 1.xlsx",
              "7": "7_Bloomberg_daily_B_rates_equity_vol_5 1.xlsx"}
SEAL = pd.Timestamp("2010-12-31")
MONTHS = pd.date_range("1969-12-31", "2026-10-31", freq="ME")              # 683 rows, as in the real files
DAYS = pd.bdate_range("1990-01-01", "2026-11-04")                           # weekdays, Days=W
ALLDAYS = pd.date_range("1989-12-31", "2026-11-04")                         # Days=A (file 1 DailyCommodities)
# special blocks: (file, sheet, ticker) -> behaviour
INVALID = {("2", "EconUS", "JLTOTOTL Index"), ("1", "FXBasis", "JYBSV1 Curncy")}
REQUESTING = {("4", "EquityIndexes", "SPW Index"), ("5", "ComFront", "CL1 Comdty")}
EMPTY = {("1", "RatesFutures", "L 6 Comdty")}
SERIAL_SHEET = ("3", "FXSpot")
REL_FORMAT = {("1", "Economics"): "yyyymmdd", ("2", "EconUS"): "datetime", ("2", "EconIntl"): "serial"}
PLANT = {("1", "Yields", "USGG10YR Index"): "gap", ("1", "Yields", "GDBR10 Index"): "stale",
         ("1", "EquityTR", "SPX Index"): "jump", ("1", "Benchmarks", "BTOP50 Index"): "nonpos",
         ("5", "ComCurve", "CL2 Comdty"): "dupdiff"}
EXCEL0 = dt.date(1899, 12, 30)


def seed_of(*parts):
    return int.from_bytes(__import__("hashlib").md5("|".join(parts).encode()).digest()[:4], "little")


def template_sheets(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    out = []
    for ws in wb.worksheets:
        rows = [list(r) for r in ws.iter_rows(min_row=1, max_row=4, values_only=True)]
        if ws.title in ("Read me", "Check"):
            rows = [list(r) for r in ws.iter_rows(values_only=True)]
        out.append((ws.title, rows))
    wb.close()
    return out


def gen_values(per, ticker, field, n, start):
    """Deterministic random walk per (per, ticker, field): duplicates in other sheets agree."""
    rng = np.random.default_rng(seed_of(per, ticker, field))
    lvl = rng.uniform(60, 4000)
    sig = 0.02 if per == "M" else 0.004
    x = lvl * np.exp(np.cumsum(rng.normal(0, sig, n)))
    x = np.round(x, 7)
    st = start if start is not None else int(rng.integers(0, int(n * 0.75)))
    return x, st


def make_mocks(out_dir, truth):
    """Write the seven mock workbooks; record release dates and every written value in `truth`."""
    from openpyxl import Workbook
    os.makedirs(out_dir, exist_ok=True)
    allvals, blocks = [], []
    for digit, tpl in sorted(TEMPLATES.items()):
        wb = Workbook(write_only=True)
        for name, hdr in template_sheets(tpl):
            ws = wb.create_sheet(name)
            if name in ("Read me", "Check"):
                for r in hdr:
                    ws.append([("NAME" if isinstance(v, str) and v.startswith("=") else v) for v in r])
                continue
            per = "D" if name.lower().startswith("daily") else "M"
            dates = (ALLDAYS if (digit, name) == ("1", "DailyCommodities") else DAYS) if per == "D" else MONTHS
            h2, h3, h4 = (hdr + [[], [], [], []])[1:4]
            for r in hdr[:4]:
                ws.append([("" if isinstance(v, str) and v.startswith("=") else v) for v in r])
            cols = []        # per block: (col, list of column arrays of python objects)
            width = len(h4)
            for c, v in enumerate(h4):
                if not (isinstance(v, str) and v.lower() == "date"):
                    continue
                tk = h3[c].strip()
                fields, k = [], c + 1
                while k < len(h4) and isinstance(h4[k], str) and h4[k].strip() and h4[k].lower() != "date":
                    fields.append(h4[k].strip())
                    k += 1
                blocks.append((digit, name, tk, c, tuple(fields)))
                key = (digit, name, tk)
                n = len(dates)
                if key in INVALID or key in REQUESTING:
                    msg = "#N/A Invalid Security" if key in INVALID else "#N/A Requesting Data..."
                    cols.append((c, [[msg]] + [[None] for _ in fields]))
                    continue
                extra = digit == "1" and name == "Economics" and seed_of(tk) % 3 == 0
                dlist = list(dates) + ([pd.Timestamp("2026-11-30")] if extra else [])
                n = len(dlist)
                if SERIAL_SHEET == (digit, name):
                    dcol = [(d.date() - EXCEL0).days for d in dlist]
                else:
                    dcol = [d.to_pydatetime() for d in dlist]
                fcols = []
                planted = tk in {k[2] for k in PLANT}                     # all copies of a planted ticker start early
                late = seed_of("late", tk) % 9 == 0 and not planted         # ~1 block in 9 starts after 2010
                start0 = 0 if planted else None
                if late:
                    start0 = int(np.searchsorted(np.array(dlist, dtype="datetime64[ns]"), np.datetime64("2012-01-31")))
                for f in fields:
                    if f == "ECO_RELEASE_DT":
                        fmt = REL_FORMAT.get((digit, name), "yyyymmdd")
                        rng = np.random.default_rng(seed_of("rel", digit, name, tk))
                        lag = rng.integers(5, 41, n)
                        lag[rng.random(n) < 0.03] = -3              # a few flash releases before the period end
                        col, rel = [], {}
                        for d, L in zip(dlist, lag):
                            if d < pd.Timestamp("1998-01-01"):
                                col.append(None)
                                continue
                            r = (d + pd.Timedelta(days=int(L))).date()
                            rel[d] = pd.Timestamp(r)
                            col.append(r.year * 10000 + r.month * 100 + r.day if fmt == "yyyymmdd" else
                                       dt.datetime(r.year, r.month, r.day) if fmt == "datetime" else (r - EXCEL0).days)
                        truth["release"][(digit, name, tk)] = rel
                        fcols.append(col)
                        continue
                    if key in EMPTY:
                        fcols.append([None] * n)
                        continue
                    x, st = gen_values(per, tk, f, n, start0)
                    x = x.copy()
                    p = PLANT.get(key)
                    di = pd.DatetimeIndex(dlist)
                    if p == "gap":
                        x[(di >= "1995-03-01") & (di <= "1995-05-31")] = np.nan
                    elif p == "stale":
                        m = (di >= "2001-01-01") & (di <= "2001-12-31")
                        x[m] = x[np.argmax(m)]
                    elif p == "jump" and f == "PX_LAST":
                        x[np.argmax(di >= "1999-06-01")] *= 3.0
                    elif p == "nonpos":
                        x[np.argmax(di >= "2003-03-01")] = -abs(x[np.argmax(di >= "2003-03-01")])
                    elif p == "dupdiff":
                        m = (di >= "2000-01-01") & (di <= "2005-12-31")
                        x[m] = np.round(x[m] * 1.01, 7)
                    col = [None] * st + [None if np.isnan(v) else float(v) for v in x[st:]]
                    if seed_of("na", tk, f) % 7 == 0 and n > st + 10:
                        for j in (st + 3, st + 7):
                            col[j] = "#N/A N/A"
                    allvals.append(x[st:][np.isfinite(x[st:])])
                    fcols.append(col)
                cols.append((c, [dcol] + fcols))
            nrows = max(len(cc[0]) for _, cc in cols) if cols else 0
            for i in range(nrows):
                row = [None] * width
                for c, cc in cols:
                    for j, colv in enumerate(cc):
                        if i < len(colv):
                            row[c + j] = colv[i]
                ws.append(row)
        wb.save(os.path.join(out_dir, REAL_NAMES[digit]))
    truth["values"] = np.sort(np.concatenate(allvals))
    truth["blocks"] = blocks


# ---------------------------------------------------------------- whitelist scan
DATE_RE = re.compile(r"\b(19|20)\d{2}-\d{2}-\d{2}\b")
DEC_RE = re.compile(r"(?<![\w.])-?\d+\.\d+(?![\w.])")


def whitelist_scan(text, values):
    bad = []
    for line in text.splitlines():
        decs = DEC_RE.findall(line)
        if DATE_RE.search(line) and decs:
            bad.append("dated row with a decimal number: " + line[:120])
        for tok in decs:
            k = len(tok.split(".")[1])
            v = float(tok)
            i = np.searchsorted(values, v)
            for j in (i - 1, i):
                if 0 <= j < len(values) and abs(values[j] - v) <= 0.5 * 10 ** -k + 1e-12:
                    bad.append("mock value %s printed: %s" % (tok, line[:120]))
                    break
    return bad


def run_job(local, bbg, name):
    env = dict(os.environ, BBG_DIR=bbg, BBG_WORK=os.path.join(local, "work"),
               PYTHONPATH=os.path.join(local, "lib") + os.pathsep + os.path.join(local, "pylib"))
    t = time.time()
    p = subprocess.run([sys.executable, os.path.join("jobs", name + ".py")], cwd=local, env=env,
                       capture_output=True, text=True, timeout=1800)
    os.makedirs(os.path.join(local, "results"), exist_ok=True)
    with open(os.path.join(local, "results", name + ".txt"), "w") as f:
        f.write(p.stdout)
    assert p.returncode == 0, "%s exit %d: %s" % (name, p.returncode, p.stderr[-2000:])
    assert "=== END ===" in p.stdout, "%s did not finish:\n%s\n%s" % (name, p.stdout[-3000:], p.stderr[-2000:])
    assert "FAILED" not in p.stdout, "%s reported a failure:\n%s" % (name, p.stdout[-3000:])
    print("  %s ok in %.0fs (%d lines)" % (name, time.time() - t, p.stdout.count("\n")))
    return p.stdout


def main():
    keep = "--keep" in sys.argv
    tmp = tempfile.mkdtemp(prefix="bbgq_smoke_")
    try:
        local, bbg = os.path.join(tmp, "local"), os.path.join(tmp, "pulled results")
        for d in ("lib", "pylib", "jobs", "work"):
            os.makedirs(os.path.join(local, d))
        for f in ("lib/bbgdata.py", "live_sources.csv", "untouched_markets.csv"):
            shutil.copy(os.path.join(BBGQ, f), os.path.join(local, "lib", os.path.basename(f)))
        for j in ("bbg_build_v1", "bbg_check_v1"):
            shutil.copy(os.path.join(BBGQ, "jobs", j + ".py"), os.path.join(local, "jobs"))
        truth = {"release": {}}
        t = time.time()
        make_mocks(bbg, truth)
        print("  mock workbooks written in %.0fs: %s" % (time.time() - t, ", ".join(sorted(os.listdir(bbg)))))
        out1 = run_job(local, bbg, "bbg_build_v1")
        out2 = run_job(local, bbg, "bbg_check_v1")

        sys.path.insert(0, os.path.join(local, "lib"))
        import bbgdata
        work = os.path.join(local, "work")
        cat = bbgdata.read_catalog(work)

        # 1. every block catalogued, every field of it
        want = {(d, s, c, f) for d, s, tk, c, fs in truth["blocks"] for f in fs}
        got = {(r.file, r.sheet, r.col, r.field) for r in cat.itertuples()}
        assert want == got, "catalog mismatch: missing %s extra %s" % (list(want - got)[:5], list(got - want)[:5])
        st = {(r.file, r.sheet, r.ticker): r.status for r in cat.itertuples()}
        for k in INVALID:
            assert st[k] == "invalid", (k, st[k])
        for k in REQUESTING:
            assert st[k] == "requesting", (k, st[k])
        for k in EMPTY:
            assert st[k] == "empty", (k, st[k])
        cl1 = cat[(cat.ticker == "CL1 Comdty") & (cat.status == "ok") & (cat.per == "M")]      # requesting copy in file 5
        assert cl1["series_id"].tolist() == ["CL1 Comdty|PX_LAST"] and cl1["file"].tolist() == ["1"]
        print("  catalog: %d blocks, %d ticker fields, all present" % (len(truth["blocks"]), len(cat)))

        # 2. design ends <= 2010-12-31, sealed starts after
        for per in ("monthly", "daily"):
            d = pd.read_pickle(os.path.join(work, "bbg", "design", per + ".pkl"))
            s = pd.read_pickle(os.path.join(work, "bbg", "sealed", per + ".pkl"))
            assert len(d) and len(s) and d.index.max() <= SEAL < s.index.min(), per
            assert s.index.max() >= pd.Timestamp("2026-10-30"), per
            if per == "daily":
                assert (d.index.dayofweek < 5).all() and (s.index.dayofweek < 5).all()
            else:
                assert d.index.is_month_end.all()
        # serial dates were read as dates
        fx = cat[(cat.file == "3") & (cat.sheet == "FXSpot") & (cat.status == "ok")]
        assert len(fx) > 40 and (fx["first"] == "1969-12-31").sum() + (fx["first"] > "1970").sum() == len(fx)

        # 3. as-of guard: property test over random dates (incl. the release-date rule)
        P = bbgdata.Panel(work)
        rng = np.random.default_rng(7)
        mids = P.ids(per="M")
        dids = P.ids(per="D")
        eco = [s for s in mids if P.info(s, "M")["release_sid"]]
        assert len(eco) > 100, len(eco)
        n_checked = 0
        for _ in range(250):
            d = pd.Timestamp("1970-01-01") + pd.Timedelta(days=int(rng.integers(0, (SEAL - pd.Timestamp("1970-01-01")).days + 1)))
            v = P.asof(d)
            picks = list(rng.choice(mids, 6)) + list(rng.choice(eco, 6)) + list(rng.choice(dids, 4))
            for sid in picks:
                per = "D" if sid in dids and sid not in mids else "M"
                s, k = v.series(sid, per), v.known(sid, per)
                assert (s.index <= d).all() and (k.index <= d).all(), (sid, d)
                info = P.info(sid, per)
                delay = pd.Timedelta(days=int(info["live_delay_days"]))
                rel = truth["release"].get((info["file"], info["sheet"], info["ticker"])) if info["release_sid"] else None
                for t in s.index:
                    if rel is not None and t in rel and rel[t] >= t - pd.Timedelta(days=31):
                        avail = max(rel[t], t)
                    else:
                        avail = t + delay
                    assert avail <= d, (sid, d, t, avail)
                    n_checked += 1
                # nothing knowable is missing: the next unreturned observation really was not yet known
                full = P.tables[per][sid].dropna()
                rest = full[~full.index.isin(s.index)]
                rest = rest[rest.index <= d]
                for t in rest.index[-3:]:
                    if rel is not None and t in rel and rel[t] >= t - pd.Timedelta(days=31):
                        assert max(rel[t], t) > d, (sid, d, t)
                    else:
                        assert t + delay > d, (sid, d, t)
        # truncation: an earlier view is a prefix of a later one
        for sid in rng.choice(eco, 10):
            a, b = P.asof("1999-06-15").series(sid, "M"), P.asof("2004-02-10").series(sid, "M")
            assert a.equals(b.loc[a.index]), sid
        print("  as-of guard: %d returned observations checked against their release / delay" % n_checked)

        # 4. HoldoutSealed raised and logged
        log = os.path.join(work, "bbg", "sealed_access.log")
        for bad_call in (lambda: P.asof("2011-01-03"), lambda: bbgdata.Panel(work, holdout_key="guess")):
            try:
                bad_call()
                raise AssertionError("HoldoutSealed not raised")
            except bbgdata.HoldoutSealed:
                pass
        txt = open(log).read()
        assert "asof 2011-01-03 refused" in txt and "holdout key attempt" in txt and "refused" in txt

        # 5. untouched hidden by default
        unt = "USDTRY Curncy|PX_LAST"
        assert unt not in P.ids(per="M") and unt not in P.tables["M"].columns
        try:
            P.asof("2005-01-31").series(unt, "M")
            raise AssertionError("untouched series visible")
        except KeyError:
            pass
        PU = bbgdata.Panel(work, allow_untouched=True)
        assert unt in PU.ids(per="M") and len(PU.asof("2005-01-31").series(unt, "M")) > 0
        assert "LA1 Comdty|PX_LAST" not in P.ids(per="D") and "LA1 Comdty|PX_LAST" in PU.ids(per="D")

        # 6. same lock id on an unchanged rebuild; history kept
        out3 = run_job(local, bbg, "bbg_build_v1")
        lid = [re.search(r"LOCK ID ([0-9a-f]{64})", o).group(1) for o in (out1, out3)]
        assert lid[0] == lid[1], lid
        assert P.lock_id == lid[0]
        assert os.listdir(os.path.join(work, "bbg", "history")), "no history kept"

        # 7. the planted problems are flagged by the check
        for tk, code in (("USGG10YR Index", "GAP"), ("GDBR10 Index", "STALE"), ("SPX Index", "JUMP"),
                         ("BTOP50 Index", "NONPOS"), ("CL2 Comdty", "DUPDIFF"), ("SPW Index", "REQ"),
                         ("JLTOTOTL Index", "INV"), ("L 6 Comdty", "EMPTY")):
            assert re.search(re.escape(tk) + r"\|[A-Z_]+ \[[^\]]*" + code, out2), (tk, code)
        assert "MUST SUMMARY" in out2 and "SEALED TABLE" in out2

        # 8. export whitelist on every job output
        for name, out in (("build", out1), ("check", out2), ("rebuild", out3)):
            bad = whitelist_scan(out, truth["values"])
            assert not bad, "%s output breaks the whitelist: %s" % (name, bad[:5])
        print("  lock id stable, holdout sealed and logged, untouched hidden, planted flags found, whitelist clean")
        print("BBGQ SMOKE OK")
    finally:
        if keep:
            print("kept", tmp)
        else:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
