"""gm_engine: run the Global Macro Book engine (the gm/ package, UNCHANGED) on its free-data inputs, in the cloud or on
the user's PC, and measure it on the DESIGN PERIOD ONLY (months up to 2010-12). WORKFLOW v2.1 step 0.5.

What it does not do: change any rule of gm/. It only
  - points gm at the folder that holds the free inputs (path shim: gm.panel.RD / RAW are module variables that every
    loader reads at call time; on the PC the unpacked inputs sit in work\\free\\research and work\\free\\raw),
  - switches the old single-file Bloomberg reader off (gm.bloomberg.PATH -> a file that does not exist), so the free-data
    run is the reference run,
  - and, for the truncation test, wraps the gm LOADER functions so that no observation dated after a cut date T reaches
    the engine (Cut below). The rules themselves run as written.

Holdout rule: gm builds its monthly grid up to today, so the engine computes over 2011+ internally. Nothing computed
from data after 2010-12 leaves this module: fingerprint() and the comparisons slice to DESIGN_END first, and gm's own
console output (panel.build prints a count of big moves over the FULL sample) is captured and discarded unread.

run(free_dir=None, cut=None) -> dict          one engine run (panel -> signals -> daily -> BASE and CANDIDATE books)
fingerprint(res) -> dict                      design-period fingerprint (statistics, per-year sums, per-market sums)
compare(fp, ref) -> list of rows              PASS / FAIL per item with the largest absolute difference
trunc_compare(full, cut_res, T) -> rows       truncation test: per stage, differing market-months up to T
"""
import contextlib
import datetime as dt
import hashlib
import io
import json
import os
import platform
import re
import sys
import time

import numpy as np
import pandas as pd

VERSION = "gm_engine-1.0.0"
DESIGN_END = pd.Period("2010-12", "M")
ERAS = {"1975-2010": ("1975-01", "2010-12"), "1990-2010": ("1990-01", "2010-12")}
CONFIGS = ("BASE", "CANDIDATE")
TOL = {"book": 1e-8, "positions": 1e-6, "stats": 1e-6, "count": 0}
TRUNC_TOL = 1e-12          # truncation: values for months <= T must be the same numbers (rolling / EWMA are prefix-only)


# =====================================================================================================================
# setup: import gm, point it at the inputs
# =====================================================================================================================
def gm_modules():
    from gm import book as B
    from gm import bloomberg as BBG
    from gm import config as CF
    from gm import daily as DL
    from gm import panel as P
    from gm import signals as G
    from gm import stats as ST
    from gm import vol as VM
    return {"B": B, "BBG": BBG, "CF": CF, "DL": DL, "P": P, "G": G, "ST": ST, "VM": VM}


def setup(free_dir=None):
    """Point gm at the free inputs. free_dir: folder with research/ and raw/ (the unpacked zip); None = the repo cache.
    Also switches the old Bloomberg file reader off and clears gm's module caches."""
    M = gm_modules()
    P, BBG, G = M["P"], M["BBG"], M["G"]
    if free_dir:
        P.RD = os.path.join(free_dir, "research")
        P.RAW = os.path.join(free_dir, "raw")
    BBG.PATH = os.path.join(P.RD, "bloomberg", "_free_data_reference_run_no_file_.xlsx")
    BBG._CACHE.clear()
    G._SDMX.clear()
    G._PIT.clear()
    return M


# =====================================================================================================================
# truncation at the loader level
# =====================================================================================================================
class Cut:
    """Context manager: while active, every gm loader returns only observations dated <= T (month T for monthly data,
    day T for daily data). gm's rule code is untouched; the loader functions are wrapped (module attributes) and
    restored on exit. Loaders covered (all file reads of panel / signals / daily, checked with an audit hook):
      panel._csv (Yahoo, stooq, FRED / OECD csv), panel._month_end (central-bank yields, EIA curves), msci_gross_local,
      french_country_usd, french_rf_mkt, eia_curve, _pinksheet; signals.oecd_sdmx, _dallas, _oecd_rev, _french_mkt;
      daily._daily_csv, cb_daily; pandas.read_excel (inline reads: AQR long-run commodities, EIA daily, cb_au history:
      rows whose first column is a date after T are dropped)."""

    def __init__(self, M, T):
        self.M = M
        self.T = pd.Timestamp(T).normalize()
        self.Tp = pd.Period(self.T, "M")
        self.saved = []

    # -- cutters
    def _p(self, x):
        """PeriodIndex series / frame on the gm grid: values after month T -> NaN (same index)."""
        if x is None or not hasattr(x, "index") or not isinstance(x.index, pd.PeriodIndex):
            return x
        y = x.copy()
        y.loc[y.index > self.Tp] = np.nan
        return y

    def _pi(self, x):
        """PeriodIndex series indexed by vintage / edition: drop vintages after month T."""
        if x is None or not hasattr(x, "index") or not len(x):
            return x
        return x[x.index <= self.Tp]

    def _d(self, x):
        """DatetimeIndex series: drop days after T."""
        if x is None or not hasattr(x, "index") or not len(x) or not isinstance(x.index, pd.DatetimeIndex):
            return x
        return x[x.index <= self.T + pd.Timedelta(hours=23, minutes=59)]

    def _wb(self, wb):
        """gm.bloomberg workbook dict {sheet: {ticker: DataFrame(month index)}}: drop months after T."""
        return {sh: {tk: df.loc[df.index <= self.Tp] for tk, df in blocks.items()} for sh, blocks in wb.items()}

    def _wrap(self, mod, name, post):
        orig = getattr(mod, name)

        def w(*a, **k):
            return post(orig(*a, **k))
        w.__wrapped__ = orig
        self.saved.append((mod, name, orig))
        setattr(mod, name, w)

    def _read_excel(self, orig):
        T = self.T

        def w(*a, **k):
            x = orig(*a, **k)
            path = str(a[0] if a else k.get("io", ""))
            if os.path.basename(path).startswith("dallas_") or not isinstance(x, pd.DataFrame) or not len(x):
                return x                                      # dallas: vintages in columns, cut in _dallas
            d = pd.DatetimeIndex([pd.Timestamp(v) if isinstance(v, (dt.datetime, dt.date, np.datetime64)) and
                                  not pd.isna(v) else pd.NaT for v in x.iloc[:, 0]])
            return x[~np.asarray(d > T)]
        return w

    def __enter__(self):
        M = self.M
        P, G, DL = M["P"], M["G"], M["DL"]
        for name in ("_csv", "_month_end", "msci_gross_local", "french_country_usd", "eia_curve", "_pinksheet"):
            self._wrap(P, name, self._p)
        self._wrap(P, "french_rf_mkt", lambda t: tuple(self._p(s) for s in t))
        for name in ("oecd_sdmx", "_french_mkt"):
            self._wrap(G, name, self._p)
        for name in ("_dallas", "_oecd_rev"):
            self._wrap(G, name, self._pi)
        for name in ("_daily_csv", "cb_daily"):
            self._wrap(DL, name, self._d)
        self._wrap(M["BBG"], "load", self._wb)       # Bloomberg inputs (adapter cache or old file): months <= T
        self.saved.append((pd, "read_excel", pd.read_excel))
        pd.read_excel = self._read_excel(pd.read_excel)
        G._SDMX.clear()
        G._PIT.clear()
        return self

    def __exit__(self, *exc):
        for mod, name, orig in reversed(self.saved):
            setattr(mod, name, orig)
        self.saved = []
        self.M["G"]._SDMX.clear()
        self.M["G"]._PIT.clear()
        return False


# =====================================================================================================================
# one engine run
# =====================================================================================================================
def bbg_dict(bbg, asof):
    """bbg: None, a gm.bloomberg workbook dict, or a function asof -> dict (e.g. lambda T: bbg_panel.Source(work,
    asof=T).workbook()). Returns the dict for this date (a dict is used as it is; Cut drops its months after T)."""
    if bbg is None:
        return None
    return bbg(asof) if callable(bbg) else bbg


def run(free_dir=None, cut=None, M=None, bbg=None):
    """panel -> signals (E, C, V as gm.signals.main computes them) -> daily returns -> BASE and CANDIDATE books
    (gm.book.run with daily data and the signals, as gm.protocol does). cut: a date T for the truncation test.
    bbg: optional Bloomberg inputs, a gm.bloomberg workbook dict or a function asof -> dict (see bbg_dict; with a cut
    the function is called with T, so the adapter's as-of guard applies; None = free data only, the reference run)."""
    M = M or setup(free_dir)
    M["BBG"]._CACHE.clear()
    wb = bbg_dict(bbg, cut if cut is not None else "2010-12-31")
    if wb is not None:
        M["BBG"]._CACHE["wb"] = wb
    P, G, DL, B, CF = M["P"], M["G"], M["DL"], M["B"], M["CF"]
    t0 = time.time()
    ctx = Cut(M, cut) if cut is not None else contextlib.nullcontext()
    sink = io.StringIO()
    with ctx:
        with contextlib.redirect_stdout(sink):           # gm prints full-sample counts (incl. 2011+): discarded
            R, SRC, FLAG, rf = P.build()
            E = G.econ_scores(R)
            C = G.carry_values(R)
            V = G.value_values(R)
            D = DL.build()
    S = {"E": E, "C": C, "V": V}
    books = {}
    with contextlib.redirect_stdout(sink):
        for name in CONFIGS:
            books[name] = B.run(R, cfg=getattr(CF, name), daily=D, S=S)
        trend = B.trend_signal(R, CF.BASE, books["BASE"]["vol"], S)
    del sink
    out = {"R": R, "S": S, "D": D, "books": books, "trend": trend, "seconds": time.time() - t0, "cut": cut,
           "bbg_tickers": sum(len(b) for b in wb.values()) if wb else 0}
    if cut is not None:
        Tp = pd.Period(pd.Timestamp(cut), "M")
        out["after_cut_empty"] = bool(R.loc[R.index > Tp].isna().all().all()) and \
            bool(D.loc[D.index > pd.Timestamp(cut)].isna().all().all())
    return out


# =====================================================================================================================
# design-period fingerprint
# =====================================================================================================================
def _design(x):
    return x.loc[x.index <= DESIGN_END]


def _r(v, nd):
    return None if v is None or not np.isfinite(v) else round(float(v), nd)


def _col_sums(df, nd, absval=True):
    d = _design(df)
    d = d.abs() if absval else d
    return {str(k): _r(float(v), nd) for k, v in d.sum(min_count=1).items() if pd.notna(v)}


def era_stats(r, ST, a, b):
    x = ST.cut(r, a, b)                        # gm.stats.cut never goes past 2010-12
    if len(x) < 60:
        return {"n": int(len(x))}
    return {"n": int(len(x)), "sr": _r(ST.sharpe(x), 12), "mean": _r(x.mean() * 12, 12),
            "vol": _r(x.std() * np.sqrt(12), 12), "maxdd": _r(ST.maxdd(x), 12)}


def fingerprint(res, M=None):
    M = M or gm_modules()
    ST = M["ST"]
    R = res["R"]
    fp = {"design_end": str(DESIGN_END), "stats": {}, "book_year_sum": {}, "pos_abs_sum": {}, "vol_sum": {},
          "fam_abs_sum": {}}
    for name, bk in res["books"].items():
        fp["stats"][name] = {era: {"net": era_stats(bk["net"], ST, a, b), "gross": era_stats(bk["gross"], ST, a, b)}
                             for era, (a, b) in ERAS.items()}
        ys = {}
        for part in ("net", "gross"):
            s = _design(bk[part]).dropna()
            ys[part] = {str(y): _r(v, 10) for y, v in s.groupby(s.index.year).sum().items()}
        fp["book_year_sum"][name] = ys
        fp["pos_abs_sum"][name] = _col_sums(bk["pos"], 8)
        fp["vol_sum"][name] = _col_sums(bk["vol"], 8)
        fp["fam_abs_sum"][name] = {f: _col_sums(p, 8) for f, p in bk["fam_pos"].items()}
    fp["market_months"] = {str(k): int(v) for k, v in _design(R).notna().sum().items()}
    fp["signal_abs_sum"] = {k: _col_sums(v, 8) for k, v in res["S"].items()}
    fp["signal_abs_sum"]["trend"] = _col_sums(res["trend"], 8)
    _assert_design_only(fp)
    return fp


def _assert_design_only(fp):
    txt = json.dumps(fp)
    bad = re.findall(r'"(20(?:1[1-9]|[2-9]\d))"', txt)
    if bad:
        raise RuntimeError("fingerprint holds a year after 2010: %s" % bad[:3])


# =====================================================================================================================
# comparison with the reference
# =====================================================================================================================
def _flat(d, pre=()):
    for k, v in d.items():
        if isinstance(v, dict):
            yield from _flat(v, pre + (k,))
        else:
            yield pre + (k,), v


def compare(fp, ref):
    """-> rows (item, kind, n values, n missing / extra, largest abs diff, tolerance, PASS/FAIL).
    Items: statistics per config x era (tol 1e-6); book returns = per-year sums (1e-8); positions, volatility, family
    positions, signals = per-market sums (1e-6); market months = counts (exact)."""
    groups = [("statistics", "stats", "stats"), ("book returns (per-year sums)", "book_year_sum", "book"),
              ("positions (per-market sum of |position|)", "pos_abs_sum", "positions"),
              ("volatility estimate (per-market sum)", "vol_sum", "positions"),
              ("family positions (per-market sum of |position|)", "fam_abs_sum", "positions"),
              ("signals (per-market sum of |signal|)", "signal_abs_sum", "positions"),
              ("market months with a return (count)", "market_months", "count")]
    rows = []
    for label, key, kind in groups:
        a = dict(_flat({key: fp.get(key, {})}))
        b = dict(_flat({key: ref.get(key, {})}))
        sub = {}
        for k in set(a) | set(b):
            top = k[:3] if key in ("stats", "fam_abs_sum") else (k[:1] if key == "market_months" else k[:2])
            sub.setdefault(top, []).append(k)
        for top in sorted(sub, key=str):
            ks = sub[top]
            miss = sum(1 for k in ks if (k in a) != (k in b) or ((a.get(k) is None) != (b.get(k) is None)))
            diffs = [abs(float(a[k]) - float(b[k])) for k in ks if a.get(k) is not None and b.get(k) is not None]
            mx = max(diffs) if diffs else 0.0
            tol = TOL[kind]
            ok = miss == 0 and mx <= tol
            rows.append({"item": "%s | %s" % (label, " / ".join(str(t) for t in top[1:])), "n": len(ks),
                         "missing": miss, "maxdiff": mx, "tol": tol, "pass": ok})
    return rows


# =====================================================================================================================
# truncation test
# =====================================================================================================================
def _frame_diff(a, b, Tp):
    """a: full run, b: cut run; both month-indexed. Compare months <= Tp (and <= 2010-12)."""
    up = min(Tp, DESIGN_END)
    if isinstance(a, pd.Series):
        a, b = a.to_frame("book"), b.to_frame("book")
    a = a.loc[a.index <= up]
    b = b.reindex(index=a.index, columns=a.columns)
    na, nb = a.isna().to_numpy(), b.isna().to_numpy()
    x, y = a.to_numpy(dtype="float64"), b.to_numpy(dtype="float64")
    d = np.where(~na & ~nb, np.abs(x - y), 0.0)
    differ = (d > TRUNC_TOL) | (na != nb)
    cnt = differ.sum(axis=0)
    rows_any = differ.any(axis=1)
    out = {"cells": int((~na | ~nb).sum()), "differ": int(differ.sum()), "maxdiff": float(d.max()) if d.size else 0.0,
           "nan_mismatch": int((na != nb).sum()),
           "markets": [str(c) for c, n in sorted(zip(a.columns, cnt), key=lambda t: -t[1]) if n > 0],
           "first": str(a.index[rows_any][0]) if rows_any.any() else "", "last": str(a.index[rows_any][-1])
           if rows_any.any() else ""}
    return out


def stages(res):
    """Stage name -> month-indexed frame (or series) of one run."""
    st = {"panel returns": res["R"], "signal econ": res["S"]["E"], "signal carry": res["S"]["C"],
          "signal value": res["S"]["V"], "signal trend (sign 1/3/12)": res["trend"]}
    for name, bk in res["books"].items():
        st["volatility %s" % name] = bk["vol"]
        for f, p in bk["fam_pos"].items():
            st["family position %s %s" % (f, name)] = p
        st["positions %s" % name] = bk["pos"]
        st["book net return %s" % name] = bk["net"]
    return st


def _mask(x, T):
    """Copy with every value dated after T set to missing (index kept): month index -> after month T, day -> after T."""
    y = x.copy()
    if isinstance(y.index, pd.PeriodIndex):
        y.loc[y.index > pd.Period(pd.Timestamp(T), "M")] = np.nan
    else:
        y.loc[y.index > pd.Timestamp(T)] = np.nan
    return y


def run_isolated(full, T, M, bbg=None):
    """Each stage ALONE: its inputs come from the full run, cut at T (values after T set to missing), so a failure here
    is the stage's own (its code uses data after T), not one inherited from an earlier stage.
      signals: gm.signals.econ_scores / carry_values / value_values on the cut full-run panel, loaders cut at T
      trend:   gm.book.trend_signal on the cut full-run panel
      books:   gm.book.run on the cut full-run panel, cut full-run signals and cut daily returns (volatility,
               family positions, positions, book returns)"""
    G, B, CF = M["G"], M["B"], M["CF"]
    Rm, Dm = _mask(full["R"], T), _mask(full["D"], T)
    M["BBG"]._CACHE.clear()
    wb = bbg_dict(bbg, T)
    if wb is not None:
        M["BBG"]._CACHE["wb"] = wb
    sink = io.StringIO()
    with Cut(M, T), contextlib.redirect_stdout(sink):
        S = {"E": G.econ_scores(Rm), "C": G.carry_values(Rm), "V": G.value_values(Rm)}
    Sm = {k: _mask(v, T) for k, v in full["S"].items()}
    with contextlib.redirect_stdout(sink):
        books = {name: B.run(Rm, cfg=getattr(CF, name), daily=Dm, S=Sm) for name in CONFIGS}
        trend = B.trend_signal(Rm, CF.BASE, books["BASE"]["vol"], Sm)
    return {"R": Rm, "S": S, "D": Dm, "books": books, "trend": trend, "cut": T}


def trunc_compare(full, cut_res, T):
    Tp = pd.Period(pd.Timestamp(T), "M")
    a, b = stages(full), stages(cut_res)
    rows = []
    for k in a:
        r = _frame_diff(a[k], b[k], Tp)
        r["stage"] = k
        r["pass"] = r["differ"] == 0
        rows.append(r)
    return rows


# =====================================================================================================================
# metadata
# =====================================================================================================================
def lib_versions():
    out = {"python": platform.python_version()}
    for m in ("numpy", "pandas", "scipy", "openpyxl", "xlrd"):
        try:
            out[m] = getattr(__import__(m), "__version__", "ok")
        except Exception:  # noqa: BLE001
            out[m] = "missing"
    return out


def gm_code_hashes(gm_dir=None):
    """sha256 of every .py file of the gm package (the PC compares its copy with the reference)."""
    if gm_dir is None:
        import gm
        gm_dir = os.path.dirname(os.path.abspath(gm.__file__))
    out = {}
    for n in sorted(os.listdir(gm_dir)):
        if n.endswith(".py"):
            with open(os.path.join(gm_dir, n), "rb") as f:
                out[n] = hashlib.sha256(f.read()).hexdigest()
    return out


def gm_data_hashes(gm_dir=None):
    """sha256 of every csv file in gm/data (small manual files that travel inside lib\\gm\\data)."""
    if gm_dir is None:
        import gm
        gm_dir = os.path.dirname(os.path.abspath(gm.__file__))
    d = os.path.join(gm_dir, "data")
    out = {}
    for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if n.lower().endswith(".csv"):
            with open(os.path.join(d, n), "rb") as f:
                out[n] = hashlib.sha256(f.read()).hexdigest()
    return out


def inputs_match(manifest, ref):
    """Shipped inputs vs the reference: same file list and the same original sizes (engine_ref.json keeps no hashes of
    the input files, which hold data after 2010); with an older reference that has a digest, the digest."""
    if "digest" in ref["inputs"]:
        return original_digest(manifest) == ref["inputs"]["digest"], "digest"
    rf = {k: v for k, v in ref["inputs"]["files"].items() if not k.startswith("gm_data/")}
    ok = set(rf) == set(manifest["files"]) and all(
        manifest["files"][k].get("original_bytes", -1) == rf[k]["bytes"] for k in rf)
    return ok, "file list and sizes"


def config_hashes(M=None):
    M = M or gm_modules()
    CF = M["CF"]
    return {n: CF.cfg_hash(getattr(CF, n)) for n in CONFIGS}


def inputs_digest(free_dir_or_files):
    """One sha256 over (relative path, sha256 of content) of every input file, independent of zip timestamps.
    Argument: a folder with research/ and raw/, or a dict {relative path: absolute path}."""
    if isinstance(free_dir_or_files, dict):
        files = free_dir_or_files
    else:
        files = {}
        for sub in ("research", "raw"):
            d = os.path.join(free_dir_or_files, sub)
            if os.path.isdir(d):
                for n in os.listdir(d):
                    files["%s/%s" % (sub, n)] = os.path.join(d, n)
    h = hashlib.sha256()
    for rel in sorted(files):
        with open(files[rel], "rb") as f:
            h.update(("%s\0%s\n" % (rel, hashlib.sha256(f.read()).hexdigest())).encode())
    return h.hexdigest(), len(files)


def py_version_ok():
    return sys.version_info >= (3, 9)


# =====================================================================================================================
# PC: unpack and verify the shipped free inputs
# =====================================================================================================================
def ensure_free_inputs(free_dir, zip_name="gm_free_inputs.zip"):
    """Unpack free_dir/gm_free_inputs.zip into free_dir (research/, raw/) where a file is missing or differs from the
    zip's inputs_manifest.json. -> dict(manifest, ok, extracted, bad, missing_zip)."""
    import zipfile
    zp = os.path.join(free_dir, zip_name)
    out = {"ok": 0, "extracted": 0, "bad": [], "manifest": None, "missing_zip": not os.path.exists(zp)}
    mp = os.path.join(free_dir, "inputs_manifest.json")
    if out["missing_zip"]:
        if os.path.exists(mp):
            out["manifest"] = json.load(open(mp, encoding="utf-8"))
        else:
            return out
    else:
        with zipfile.ZipFile(zp) as z:
            out["manifest"] = json.loads(z.read("inputs_manifest.json").decode("utf-8"))
            for rel, meta in sorted(out["manifest"]["files"].items()):
                p = os.path.join(free_dir, *rel.split("/"))
                if os.path.exists(p) and _sha(p) == meta["sha256"]:
                    out["ok"] += 1
                    continue
                os.makedirs(os.path.dirname(p), exist_ok=True)
                with open(p + ".tmp", "wb") as f:
                    f.write(z.read(rel))
                os.replace(p + ".tmp", p)
                out["extracted"] += 1
            with open(mp, "w", encoding="utf-8") as f:
                json.dump(out["manifest"], f, indent=1, sort_keys=True)
    for rel, meta in sorted(out["manifest"]["files"].items()):
        p = os.path.join(free_dir, *rel.split("/"))
        if not os.path.exists(p) or _sha(p) != meta["sha256"]:
            out["bad"].append(rel)
    return out


def _sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def original_digest(manifest):
    """Digest of the ORIGINAL input files (as in engine_ref.json) from the shipped manifest."""
    h = hashlib.sha256()
    for rel in sorted(manifest["files"]):
        h.update(("%s\0%s\n" % (rel, manifest["files"][rel]["original_sha256"])).encode())
    return h.hexdigest()


# =====================================================================================================================
# truncation report (cloud: tools/bbgq/engine_trunc.py; PC: jobs/gm_trunc_v1.py)
# =====================================================================================================================
CUT_DATES = ("1980-06-30", "1984-12-31", "1989-06-30", "1993-12-31", "1998-06-30", "2002-12-31", "2007-06-30",
             "2010-12-31")
# Causes found by this test (2026-11-11, cloud run on free data). Each: where in gm, why the earlier numbers change,
# and a one-line proposed fix. NOT fixed: gm rules are pre-registered; a fix is a new registered version.
CAUSES = {
    "C1": {"where": "gm/panel.py build(), equity loop: d = mean((tr0 + rl) - r_px) over `both = ... & (GRID <= "
                    "DIV_EST_END)` (DIV_EST_END = 2010-12), gated by tr0.notna().sum() > 60 and both.sum() > 60",
           "why": "the dividend yield added to a price index before the ETF / MSCI / French total-return series starts "
                  "is ONE number estimated from all design months, including months after the decision month",
           "fix": "estimate it on an expanding window (months <= t, with the same 60-month minimum) or register a "
                  "fixed per-market dividend yield"},
    "C2": {"where": "gm/panel.py build(), equity loop: f0 = rl.first_valid_index(); gap = rl.isna() & "
                    "(GRID >= max(f0, 1990-01))",
           "why": "whether the US 3-month rate stands in for a missing local rate depends on whether the local rate "
                  "ever starts later: with the full sample the months before its start stay empty (no return), with a "
                  "cut before its start they get returns",
           "fix": "decide the stand-in month by month: gap = rl.isna() & (GRID >= 1990-01) (or never use the stand-in "
                  "before the local rate exists)"},
    "C3": {"where": "gm/daily.py build(): a daily series is kept only if len(...) > 500 over the WHOLE sample "
                    "(bonds, equities, Yahoo commodities)",
           "why": "a market with fewer than 500 daily observations up to T but more later uses the monthly EWMA in "
                  "the cut run and the daily EWMA in the full run, so the CANDIDATE (hybrid) volatility changes",
           "fix": "drop the length gate (vol.daily_ewma already needs 40 observations) or apply it per date "
                  "(observations up to t)"},
}
CAUSES["C4"] = {
    "where": "gm/panel.py build() (BBG.commodity_return: notna().sum() > 24, alternative markets > 36), "
             "gm/bloomberg.py commodity_return (> 24) and gm/signals.py carry_values (commodity_carry > 24)",
    "why": "with Bloomberg inputs, whether a commodity uses the Bloomberg series at all depends on how many months it "
           "has over the whole sample: a cut before month 25 switches the market back to free data",
    "fix": "decide month by month (use the Bloomberg value from its first month, or require 24 months up to t)"}
STAGE_ORDER = ["panel returns", "daily returns", "signal econ", "signal carry", "signal value",
               "signal trend (sign 1/3/12)", "volatility BASE", "volatility CANDIDATE"]


def _upstream(stage):
    if stage.startswith("signal"):
        return ["panel returns"]
    if stage.startswith("volatility"):
        return ["panel returns", "daily returns"]
    return ["panel returns", "daily returns", "signal econ", "signal carry", "signal value",
            "signal trend (sign 1/3/12)", "volatility BASE" if stage.endswith("BASE") else "volatility CANDIDATE"]


def daily_diff(full_D, cut_D, T):
    """Daily returns up to T: markets present in the full run but dropped in the cut run; value differences."""
    T = pd.Timestamp(T)
    a = full_D.loc[full_D.index <= T]
    b = cut_D.reindex(index=a.index)
    have = [c for c in a.columns if a[c].notna().any()]
    dropped = [c for c in have if c not in cut_D.columns or not b[c].notna().any()]
    common = [c for c in have if c not in dropped]
    x, y = a[common].to_numpy(dtype="float64"), b[common].to_numpy(dtype="float64")
    na, nb = np.isnan(x), np.isnan(y)
    d = np.where(~na & ~nb, np.abs(x - y), 0.0)
    differ = int(((d > TRUNC_TOL) | (na != nb)).sum()) + int(a[dropped].notna().sum().sum())   # + days of dropped
    return {"stage": "daily returns", "dropped": dropped, "differ": differ, "maxdiff": float(d.max()) if d.size else 0.0,
            "pass": not dropped and differ == 0, "markets": dropped, "first": "", "last": "",
            "cells": int((~na | ~nb).sum())}


def panel_causes(full_R, cut_R, T):
    """Per market with a panel difference up to T: which cause (C1 constant shift = dividend proxy, C2 = months that
    have a return only in the cut run, local-rate stand-in) or 'unattributed'."""
    Tp = min(pd.Period(pd.Timestamp(T), "M"), DESIGN_END)
    a, b = full_R.loc[full_R.index <= Tp], cut_R.reindex(index=full_R.index[full_R.index <= Tp])
    out = {}
    for m in a.columns:
        x, y = a[m], b[m]
        only_cut = int((x.isna() & y.notna()).sum())
        only_full = int((x.notna() & y.isna()).sum())
        both = x.notna() & y.notna()
        d = (x - y)[both]
        dv = d[d.abs() > TRUNC_TOL]
        if not (only_cut or only_full or len(dv)):
            continue
        c = []
        if only_cut and m.startswith("eq_"):
            c.append("C2")
        if len(dv) and m.startswith("eq_") and float(dv.max() - dv.min()) < 1e-12:
            c.append("C1")
        if only_full or (len(dv) and "C1" not in c):
            c.append("unattributed")
        out[m] = {"causes": c, "only_cut": only_cut, "only_full": only_full, "value_months": int(len(dv)),
                  "first": str(x.index[(x.isna() != y.isna()) | ((x - y).abs() > TRUNC_TOL)][0])}
    return out


def truncation_report(free_dir, dates, out=print, M=None, bbg=None, bbg_note=""):
    """Full run, then per cut date: end-to-end run cut at T and each stage alone; prints the table and the causes.
    bbg: Bloomberg inputs (see run); a dict is cut at T by Cut like every free loader (observation month <= T)."""
    t0 = time.time()
    M = M or setup(free_dir)
    full = run(M=M, bbg=bbg)
    if full["bbg_tickers"]:
        out("BLOOMBERG INPUTS: YES, %d tickers through gm.bloomberg (%s); cut at T like the free inputs" % (
            full["bbg_tickers"], bbg_note or "adapter"))
    else:
        out("BLOOMBERG INPUTS: NONE (free data only; gm.bloomberg serves nothing, so its paths are not exercised)")
    out("full run %.0fs; cut dates: %s" % (time.time() - t0, ", ".join(dates)))
    out("columns: stage | end-to-end PASS/FAIL, differing market-months / compared, max abs diff, months first..last "
        "| stage alone PASS/FAIL, differing | markets (most differing first)")
    summary, used = [], set()
    for T in dates:
        t1 = time.time()
        if pd.Timestamp(T) > pd.Timestamp("2010-12-31"):
            out("CUT %s skipped: after the design period" % T)
            continue
        c = run(M=M, cut=T, bbg=bbg)
        iso = run_isolated(full, T, M, bbg=bbg)
        e2e = {r["stage"]: r for r in trunc_compare(full, c, T)}
        own = {r["stage"]: r for r in trunc_compare(full, iso, T)}
        e2e["daily returns"] = daily_diff(full["D"], c["D"], T)
        pc = panel_causes(full["R"], c["R"], T)
        if full["bbg_tickers"]:
            for m_, p_ in pc.items():
                if m_.startswith("cm_"):
                    p_["causes"] = ["C4" if x == "unattributed" else x for x in p_["causes"]]
        n_fail = sum(1 for r in e2e.values() if not r["pass"])
        out("CUT %s | inputs after T seen by the engine: %s | stages failing end-to-end %d of %d | %.0fs" % (
            T, "none" if c["after_cut_empty"] else "SOME (cut incomplete)", n_fail, len(e2e), time.time() - t1))
        order = STAGE_ORDER + [k for k in e2e if k not in STAGE_ORDER]
        for k in order:
            r = e2e[k]
            o = own.get(k)
            if k in ("panel returns", "daily returns"):
                os_ = "n/a (loader stage)"
            else:
                os_ = "%s %d" % ("PASS" if o["pass"] else "FAIL", o["differ"])
            out("  %-34s | %s %d/%d max %.1e %s | alone %s | %s" % (
                k, "PASS" if r["pass"] else "FAIL", r["differ"], r["cells"], r["maxdiff"],
                ("%s..%s" % (r["first"], r["last"])) if r["first"] else "", os_,
                ",".join(r["markets"][:8]) + (" +%d" % (len(r["markets"]) - 8) if len(r["markets"]) > 8 else "")))
        # attribution
        for m, p in sorted(pc.items()):
            used.update(x for x in p["causes"] if x in CAUSES)
            out("  cause panel %s: %s (months with a return only in the cut run %d, only in the full run %d, value "
                "differences %d; first %s)" % (m, "+".join(p["causes"]), p["only_cut"], p["only_full"],
                                               p["value_months"], p["first"]))
        if e2e["daily returns"]["dropped"]:
            used.add("C3")
            out("  cause daily returns: C3 (markets with daily data up to T that the cut run drops: %s)" %
                ", ".join(e2e["daily returns"]["dropped"]))
        for k in order:
            r = e2e[k]
            if r["pass"] or k in ("panel returns", "daily returns"):
                continue
            o = own[k]
            if o["pass"]:
                up = [u for u in _upstream(k) if u in e2e and not e2e[u]["pass"]]
                out("  cause %s: inherited (stage alone passes) from %s" % (k, ", ".join(up) or "?"))
            elif full["bbg_tickers"] and k == "signal carry" and all(x.startswith("cm_") for x in o["markets"]):
                used.add("C4")
                out("  cause %s: C4 (stage alone fails on commodity markets only, %d market-months)" % (k, o["differ"]))
            else:
                out("  cause %s: OWN look-ahead (stage alone fails, %d market-months): not attributed" % (k, o["differ"]))
                used.add("own:" + k)
        summary.append((T, n_fail, len(e2e), sum(1 for k, o in own.items() if k not in ("panel returns",)
                                                   and not o["pass"])))
    out("--- causes found")
    for cid in sorted(x for x in used if x in CAUSES):
        cz = CAUSES[cid]
        out("%s | where: %s" % (cid, cz["where"]))
        out("   why: %s" % cz["why"])
        out("   proposed fix (not applied): %s" % cz["fix"])
    for x in sorted(x for x in used if x.startswith("own:")):
        out("OWN %s: a stage uses data after T by itself; not attributed" % x[4:])
    out("--- summary")
    for T, nf, n, no in summary:
        out("TRUNC %s | %s | end-to-end failing stages %d of %d | stages failing alone %d" % (
            T, "PASS" if nf == 0 else "FAIL", nf, n, no))
    allpass = all(nf == 0 for _, nf, _, _ in summary)
    out("TRUNCATION TEST %s | Bloomberg inputs %s" % (
        "PASS" if allpass else "FAIL (honest failures listed above; nothing was fixed)",
        "YES (%d tickers)" % full["bbg_tickers"] if full["bbg_tickers"] else "NONE (free data only)"))
    return summary
