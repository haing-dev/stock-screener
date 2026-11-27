"""a1_panel: the A1 panel of TESTING_PROTOCOL 7.6 step 2 (Batch A1, data swap) = the free panel plus the Bloomberg
series of LOCK_v2 that the registered A1 data rule admits, as BACKWARD EXTENSIONS only (gm/CHANGES.md "data: A1 data
rule", 2026-11-27; 7.4 E15). Runs where the Bloomberg store is (the user's PC); tested in the cloud on mock stores.

The rule, word for word (7.6 step 2): "it may only extend a market's free history backwards, never replace an
overlapping free month (live runs on the free source, rule 7); it must be the same instrument (same index family or
contract root) with status ok in LOCK_v2 (not a copy, not cut); and its monthly returns must correlate at least 0.95
with the free series over the overlap months up to 2010-12 ... A series failing a condition is not used and is listed."

Candidates (CHANGES entry item 4): block 1 commodity excess-return indexes -> the panel return R of the 16 panel
commodities; block 2 the generic contracts 1 and 2 of CL / NG / HO / XB -> the EIA contract month-end prices that the
Carry signal 12 x (F1 / F2 - 1) reads; block 3 the MSCI 12-month dividend yield of the market's country -> Value's
equity dividend yield (before E4's lag); report line R: 1st bond futures against the yield-built bond returns (never
used). Seal: Bloomberg through bbg_panel.Source(asof="2010-12-31") (bbgdata never opens the sealed tables), free inputs
under gm_engine.Cut at 2010-12-31, every output checked by gm/seal.py; nothing dated after 2010-12 is read or produced.

API
  candidates()                      the registered candidate list (dicts)
  Store(work) / MemoryStore(...)    Bloomberg side: lock id, lookup(ticker, field) (status), series(ticker, field)
  free_inputs(M)                    free side: R, D, S, EIA contracts 1-2, lag-0 dividend yield, ^GSPC days (cut)
  evaluate(store, free)             one row per candidate: conditions, overlap months, correlation, extension months
  build(store, free, blocks)        -> A1 dict {R, S, rows, admitted, panel_id, ...} (blocks = which blocks to apply)
  report(free, arms, cfg, out)      the registered A1 report (PC): k = 1 and k = 0 statistics per arm, differences
Nothing here prints a data value; report() prints the registered summary statistics only (export whitelist).
"""
import contextlib
import hashlib
import io
import json
import os
import re

import numpy as np
import pandas as pd

VERSION = "a1_panel-1.0.0"
LOCK_V2 = "d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9"
SEAL = "2010-12-31"
DESIGN_END = pd.Period("2010-12", "M")
CORR_MIN = 0.95             # 7.6 step 2
MIN_OVERLAP = 24            # closed here (CHANGES A1 item 5d): gm's C4 convention for a Bloomberg series
MIN_PRINT = 60              # export whitelist: a correlation is printed only over at least 60 months
CUT_NAME = re.compile(r"_cut", re.I)
EIA_OF = {"cm_wti": "cl", "cm_natgas": "ng", "cm_heatoil": "ho", "cm_gasoline": "rb"}
PANEL_COMMOD = ("cm_wti", "cm_brent", "cm_natgas", "cm_heatoil", "cm_gasoline", "cm_gold", "cm_silver", "cm_copper",
                "cm_platinum", "cm_corn", "cm_wheat", "cm_soybeans", "cm_sugar", "cm_coffee", "cm_cotton", "cm_cattle")
BOND_FUT = {"bd_us_2y": "TU1 Comdty", "bd_us_5y": "FV1 Comdty", "bd_us_10y": "TY1 Comdty", "bd_us_30y": "US1 Comdty",
            "st_de_2y": "DU1 Comdty", "bd_de_10y": "RX1 Comdty", "bd_gb_10y": "G 1 Comdty", "bd_jp_10y": "JB1 Comdty",
            "bd_ca_10y": "CN1 Comdty", "st_au_2y": "YM1 Comdty", "bd_au_10y": "XM1 Comdty"}
BLOCK_NAMES = {1: "commodity excess-return indexes -> panel return", 2: "energy contracts 1-2 -> Carry signal",
               3: "MSCI 12-month dividend yield -> Value"}


# =====================================================================================================================
# candidates (registered list, gm/CHANGES.md data entry A1 item 4)
# =====================================================================================================================
def candidates():
    from gm import bloomberg as BBG
    from gm import config as CF
    from gm import signals as G
    rows = []

    def pref(tk):
        return next((i for i, p in enumerate(CF.BBG_ER_PREFERENCE) if tk.startswith(p)), len(CF.BBG_ER_PREFERENCE))
    for m in PANEL_COMMOD:
        for tk in sorted(BBG.COMMOD_ER.get(m, ()), key=pref):
            rows.append({"block": 1, "kind": "er", "market": m, "ticker": tk, "field": "PX_LAST", "sheet": "Returns",
                         "target": "panel return %s" % m,
                         "instrument": "excess-return index on the %s futures root (same contract root)" %
                                       BBG.CURVE_ROOT.get(m, "?").strip()})
    for m, eia in EIA_OF.items():
        root = BBG.CURVE_ROOT[m]
        for n in (1, 2):
            rows.append({"block": 2, "kind": "contract", "market": m, "ticker": "%s%d Comdty" % (root, n),
                         "field": "PX_LAST", "sheet": "Curves", "n": n, "eia": eia,
                         "target": "EIA %s%d month-end (Carry signal of %s)" % (eia, n, m),
                         "instrument": "generic contract %d of root %s (same root and position as EIA %s%d)" % (
                             n, root, eia, n)})
    for m, tk in BBG.EQ_INDEX.items():
        rows.append({"block": 3, "kind": "dy", "market": m, "ticker": tk, "field": "EQY_DVD_YLD_12M",
                     "sheet": "EquityValuation", "lag": (0 if m not in G.FRENCH_DY else CF.VALUE_DY_LAG),
                     "target": "12-month dividend yield of %s (Value)" % m,
                     "instrument": "MSCI index of the same country (7.4 E2 mapping)"})
    return rows


def report_lines():
    return [{"block": "R", "kind": "bondfut", "market": m, "ticker": tk, "field": "PX_LAST", "sheet": "BondFutures",
             "target": "yield-built return %s (report only)" % m} for m, tk in BOND_FUT.items()]


# =====================================================================================================================
# Bloomberg side
# =====================================================================================================================
class Store:
    """LOCK_v2 store on the PC (work dir with bbg/), as of 2010-12-31, through bbg_panel.Source (bbgdata)."""

    def __init__(self, work, asof=SEAL):
        import bbg_panel
        self.src = bbg_panel.Source(work, asof=asof)
        self.lock_id = self.src.P.lock_id
        self.cat = self.src.cat

    def lookup(self, ticker, field):
        r = self.src.primary.get((ticker, field))
        if r is not None:
            return {"status": "ok", "sid": r.series_id, "file": r.file, "file_name": r.file_name, "sheet": r.sheet,
                    "first": r.first, "n_design": int(r.n_design), "source": getattr(r, "source", "") or "first"}
        rows = self.cat[(self.cat["ticker"] == ticker) & (self.cat["field"] == field) & (self.cat["per"] == "M")]
        if not len(rows):
            return {"status": "not in the lock (or held back)", "sid": None}
        st = sorted(set(rows["status"]))
        return {"status": "/".join(st) if st != ["ok"] else "ok but duplicate", "sid": None,
                "file_name": ";".join(sorted(set(rows["file_name"])))}

    def series(self, ticker, field, sheet="Returns"):
        return self.src.series(ticker, field, sheet)


class MemoryStore:
    """In-memory store with the same interface (tests). data: {(ticker, field): Series (PeriodIndex)};
    status: {(ticker, field): status}; file_name: {(ticker, field): name}."""

    def __init__(self, lock_id, data, status=None, file_name=None):
        self.lock_id = lock_id
        self.data = data
        self.status = status or {}
        self.file_name = file_name or {}

    def lookup(self, ticker, field):
        k = (ticker, field)
        st = self.status.get(k, "ok" if k in self.data else "not in the lock (or held back)")
        return {"status": st, "sid": "%s|%s" % k if st == "ok" else None, "file_name": self.file_name.get(k, "mock.xlsx"),
                "first": "", "n_design": int(self.data[k].notna().sum()) if k in self.data else 0, "source": "first"}

    def series(self, ticker, field, sheet="Returns"):
        s = self.data.get((ticker, field))
        if s is None:
            return None
        s = s[s.index <= DESIGN_END].dropna()      # the as-of guard of the real store: nothing after the seal
        return s if len(s) else None


# =====================================================================================================================
# free side
# =====================================================================================================================
def free_inputs(M, R=None):
    """Free inputs of the engine, every loader cut at 2010-12-31 (gm_engine.Cut), outputs cut at the seal.
    R: an already built panel (then only the signals are computed from it, under the same cut)."""
    import gm_engine as GE
    from gm import seal as SL
    P, G, DL = M["P"], M["G"], M["DL"]
    M["BBG"]._CACHE.clear()
    T = SL.resolve(SL.DESIGN)
    with GE.Cut(M, SEAL), contextlib.redirect_stdout(io.StringIO()):
        if R is None:
            R, _src, _flag, _rf = P.build()
        D = DL.build()
        S = signals(M, R)
        eia = {root: P.eia_curve(root) for root in EIA_OF.values()}
        dy0 = G.equity_dy(0)
        gspc = DL.yahoo_daily("^GSPC")
    R, D, S, dy0, gspc = SL.cut_inputs(T, R, D, S, dy0, gspc)
    eia = {k: SL.cut_inputs(T, v) for k, v in eia.items()}
    return {"R": R, "D": D, "S": S, "eia": eia, "dy0": dy0, "gspc": gspc}


def signals(M, R):
    """The engine's signals on panel R (as gm_engine.run + feature paths compute them)."""
    G = M["G"]
    return {"E": G.econ_scores(R), "C": G.carry_values(R), "V": G.value_values(R),
            "E_sign": G.econ_versions(R, ("sign",))["sign"], "V2": G.value_v2(R)}


def _design(s):
    if s is None:
        return None
    s = s.copy()
    return s[s.index <= DESIGN_END]


def _bbg_er(market, tickers, store):
    """gm.bloomberg.commodity_return(market) served with only `tickers` (the engine's own route and C4 gate)."""
    from gm import bloomberg as BBG
    wb = {"Returns": {}}
    for tk in tickers:
        s = store.series(tk, "PX_LAST", "Returns")
        if s is not None and len(s):
            wb["Returns"][tk] = pd.DataFrame({"PX_LAST": s.astype(float)})
    had, prev = "wb" in BBG._CACHE, BBG._CACHE.get("wb")
    BBG._CACHE["wb"] = wb
    try:
        return _design(BBG.commodity_return(market))
    finally:
        if had:
            BBG._CACHE["wb"] = prev
        else:
            BBG._CACHE.pop("wb", None)


def _ret(x):
    return x.pct_change(fill_method=None)


def _pair(c, store, free):
    """-> (bloomberg level or return series, bloomberg 'return' for the correlation, free series, free 'return')."""
    k = c["kind"]
    if k == "er":
        bb = _bbg_er(c["market"], [c["ticker"]], store)
        fr = _design(free["R"][c["market"]]) if c["market"] in free["R"] else None
        return bb, bb, fr, fr
    s = store.series(c["ticker"], c["field"], c["sheet"])
    s = _design(s.reindex(free["R"].index)) if s is not None else None
    if k == "contract":
        cv = free["eia"].get(c["eia"])
        fr = _design(cv[c["n"]]) if cv is not None and c["n"] in cv else None
        return s, (_ret(s) if s is not None else None), fr, (_ret(fr) if fr is not None else None)
    if k == "dy":
        fr = _design(free["dy0"][c["market"]]) if c["market"] in free["dy0"] else None
        s = s / 100 if s is not None else None
        return s, (s.diff() if s is not None else None), fr, (fr.diff() if fr is not None else None)
    if k == "bondfut":
        fr = _design(free["R"][c["market"]]) if c["market"] in free["R"] else None
        return s, (_ret(s) if s is not None else None), fr, fr
    raise ValueError(k)


def evaluate_one(c, store, free):
    info = store.lookup(c["ticker"], c["field"])
    row = dict(c, status=info["status"], file_name=info.get("file_name", ""), reasons=[], n_overlap=0, corr=None,
               first_lock="-", n_lock=0, first_bbg="-", first_free="-", ext_first="-", ext_last="-", n_ext=0,
               verdict="rejected")
    ok_status = info["status"] == "ok"
    cut = bool(CUT_NAME.search(str(info.get("file_name", "") or "")))
    if not ok_status:
        row["reasons"].append("status in LOCK_v2: %s" % info["status"])
    if cut:
        row["reasons"].append("cut file (%s)" % info.get("file_name"))
    if not ok_status:
        return row
    raw = store.series(c["ticker"], c["field"], c["sheet"])
    raw = _design(raw) if raw is not None else None
    if raw is not None and raw.notna().any():
        row["first_lock"], row["n_lock"] = str(raw.first_valid_index()), int(raw.notna().sum())
    bb, bbr, fr, frr = _pair(c, store, free)
    if bb is None or not bb.notna().any():
        row["reasons"].append("no design values served as of 2010-12-31")
        return row
    row["first_bbg"] = str(bb.first_valid_index())
    if fr is None or not fr.notna().any():
        row["reasons"].append("no free history to extend (no overlap)")
        return row
    f0 = fr.first_valid_index()
    row["first_free"] = str(f0)
    both = pd.concat([bbr, frr], axis=1).dropna()
    both = both[both.index <= DESIGN_END]
    row["n_overlap"] = int(len(both))
    if len(both) >= MIN_OVERLAP and both.iloc[:, 0].std() > 0 and both.iloc[:, 1].std() > 0:
        row["corr"] = float(np.corrcoef(both.iloc[:, 0], both.iloc[:, 1])[0, 1])
    if c["kind"] == "bondfut":
        row["verdict"] = "report only"
        return row
    if len(both) < MIN_OVERLAP:
        row["reasons"].append("too few overlap months (%d < %d)" % (len(both), MIN_OVERLAP))
    elif row["corr"] is None or not row["corr"] >= CORR_MIN:
        row["reasons"].append("correlation below %.2f" % CORR_MIN)
    ext = bb[(bb.index < f0) & bb.notna()]            # months strictly before the free start (extension only)
    row["n_ext"] = int(len(ext))
    if len(ext):
        row["ext_first"], row["ext_last"] = str(ext.index[0]), str(ext.index[-1])
    if row["reasons"]:
        return row
    if not len(ext):
        row["reasons"].append("nothing to extend (starts at or after the free start %s)" % f0)
        return row
    row["verdict"] = "admitted"
    return row


def evaluate(store, free):
    rows = [evaluate_one(c, store, free) for c in candidates()]
    rep = [evaluate_one(c, store, free) for c in report_lines()]
    return rows, rep


# =====================================================================================================================
# the A1 panel
# =====================================================================================================================
def _before(x, first):
    return x[(x.index < first) & x.notna()]


def panel_id(lock_id, free_digest, admitted, blocks):
    doc = {"version": VERSION, "lock_id": lock_id, "free_inputs": free_digest, "blocks": sorted(blocks),
           "rule": {"corr_min": CORR_MIN, "min_overlap": MIN_OVERLAP, "seal": SEAL},
           "admitted": sorted([[r["block"], r["kind"], r["market"], r["ticker"], r["field"]] for r in admitted])}
    return hashlib.sha256(json.dumps(doc, sort_keys=True).encode()).hexdigest()


def build(store, free, blocks=(1, 2, 3), rows=None, M=None, free_digest="", recompute_signals=True):
    """The A1 panel for the given blocks. rows: evaluate() rows (computed if None). M: gm modules (gm_engine.setup)
    for recomputing the signals on the extended panel (None: the free signals are kept and only the overrides of
    blocks 2 and 3 are applied, the form used by the tests). Returns dict(R, S, rows, admitted, added, panel_id)."""
    from gm import seal as SL
    if rows is None:
        rows, _ = evaluate(store, free)
    adm = [r for r in rows if r["verdict"] == "admitted" and r["block"] in blocks]
    R = free["R"].copy()
    added = {}
    # block 1: panel return before the free first month, month by month in the registered preference order
    for m in sorted({r["market"] for r in adm if r["kind"] == "er"}):
        tks = [r["ticker"] for r in adm if r["kind"] == "er" and r["market"] == m]
        ext = _bbg_er(m, tks, store).reindex(R.index)
        f0 = R[m].first_valid_index()
        fill = _before(ext, f0)
        R.loc[fill.index, m] = fill.values
        added[("R", m)] = fill.index
    if recompute_signals and M is not None and added:
        import gm_engine as GE
        with GE.Cut(M, SEAL), contextlib.redirect_stdout(io.StringIO()):
            S = signals(M, R)
        S = SL.cut_inputs(SL.resolve(SL.DESIGN), S)
    else:
        S = {k: v.copy() for k, v in free["S"].items()}
    # block 2: EIA contracts 1-2 extended backwards, carry where the free carry has not started
    for m in sorted({r["market"] for r in adm if r["kind"] == "contract"}):
        cv = free["eia"][EIA_OF[m]]
        F = {}
        for n in (1, 2):
            base = cv[n].reindex(R.index)
            rr = [r for r in adm if r["kind"] == "contract" and r["market"] == m and r["n"] == n]
            if rr:
                bb = store.series(rr[0]["ticker"], "PX_LAST", "Curves")
                bb = _design(bb.reindex(R.index)) if bb is not None else None
                if bb is not None:
                    base = base.combine_first(_before(bb, base.first_valid_index()).reindex(R.index))
            F[n] = base
        carry = 12 * (F[1] / F[2] - 1)
        c0 = S["C"][m]
        fill = _before(carry, c0.first_valid_index())
        S["C"].loc[fill.index, m] = fill.values
        added[("C", m)] = fill.index
    # block 3: Value's equity dividend yield (both versions), before its free first month, at the lag of E4
    for r in [r for r in adm if r["kind"] == "dy"]:
        m = r["market"]
        bb = store.series(r["ticker"], r["field"], "EquityValuation")
        bb = (_design(bb.reindex(R.index)) / 100).shift(r["lag"]) if bb is not None else None
        if bb is None:
            continue
        for key in ("V", "V2"):
            if m in S[key]:
                fill = _before(bb, S[key][m].first_valid_index())
                S[key].loc[fill.index, m] = fill.values
                added[(key, m)] = fill.index
    out = {"R": R, "S": S, "rows": rows, "admitted": adm, "blocks": tuple(blocks),
           "added": {k: (str(v[0]), str(v[-1]), len(v)) for k, v in added.items() if len(v)},
           "panel_id": panel_id(store.lock_id, free_digest, adm, blocks)}
    T = SL.resolve(SL.DESIGN)
    SL.check_output({"R": R, "S": S}, T, "a1_panel.build")
    return out


def assert_extension_only(free, a1):
    """No month where the free series has a value changed; only months before each series' free start filled."""
    R0, R1 = free["R"], a1["R"]
    for k in R0.columns:
        m0 = R0[k].notna()
        if not np.allclose(R0[k][m0].values, R1[k].reindex(R0.index)[m0].values, rtol=0, atol=0, equal_nan=True):
            raise AssertionError("A1 changed a free month of %s" % k)
        new = R1[k].notna() & ~m0
        f0 = R0[k].first_valid_index()
        if new.any() and (f0 is None or R1.index[new].max() >= f0):
            raise AssertionError("A1 filled a month of %s at or after the free start" % k)
    for key in ("C", "V", "V2"):
        X0, X1 = free["S"][key], a1["S"][key]
        for k in X0.columns:
            m0 = X0[k].notna()
            a, b = X0[k][m0].values, X1[k].reindex(X0.index)[m0].values
            if not np.allclose(a, b, rtol=0, atol=0, equal_nan=True):
                raise AssertionError("A1 changed a free value of signal %s %s" % (key, k))
    return True


# =====================================================================================================================
# printing (metadata only) and the registered report
# =====================================================================================================================
def fmt_row(r):
    corr = "-" if r["corr"] is None else ("%.3f" % r["corr"] if r["n_overlap"] >= MIN_PRINT else
                                          "withheld (<%d months)" % MIN_PRINT)
    return ("%s | block %s | %s | %s %s | status %s | first in lock %s (%d months as of 2010-12-31) | first used %s | "
            "free first %s | overlap months %d | corr %s | extension %s..%s (%d months) | %s%s" % (
                r["verdict"].upper(), r["block"], r["market"], r["ticker"], r["field"], r["status"], r["first_lock"],
                r["n_lock"], r["first_bbg"], r["first_free"], r["n_overlap"], corr, r["ext_first"], r["ext_last"], r["n_ext"], r["instrument"]
                if "instrument" in r else r["target"], (" | reasons: " + "; ".join(r["reasons"])) if r["reasons"]
                else ""))


def _stats(r, a, b):
    from gm import stats as ST
    x = ST.cut(r, a, b)
    if len(x) < MIN_PRINT:
        return None
    return {"n": len(x), "sr": ST.sharpe(x), "mean": float(x.mean() * 12), "vol": float(x.std() * np.sqrt(12)),
            "maxdd": ST.maxdd(x)}


ERAS = (("1975-2010", "1975-01", "2010-12"), ("1975-89", "1975-01", "1989-12"), ("1990-2010", "1990-01", "2010-12"))


def run_arm(R, D, S, days, cfg):
    from gm import book as B
    from gm import execution as EX
    sink = io.StringIO()
    with contextlib.redirect_stdout(sink):
        k1 = EX.run_k1(R, cfg, D, S, days)
        k0 = B.run(R, cfg=cfg, daily=D, S=S)
    return {"k1": k1, "k0": k0}


def report(free, arms, cfg, out=print):
    """arms: [(name, A1 dict or None for the free arm)], the free arm first. Prints the registered summary statistics
    of 7.6 step 2 (gm/CHANGES.md A1 entry item 6). Returns {name: run_arm result}."""
    from gm import execution as EX
    from gm import seal as SL
    from gm import stats as ST
    days = EX.nyse_days(gspc=free["gspc"])
    res = {}
    for name, a1 in arms:
        R = free["R"] if a1 is None else a1["R"]
        S = free["S"] if a1 is None else a1["S"]
        res[name] = run_arm(R, free["D"], S, days, cfg)
        SL.check_output({"k1": res[name]["k1"]["net"], "k0": res[name]["k0"]["net"]}, SL.resolve(SL.DESIGN),
                        "a1_panel.report")
    base = arms[0][0]
    out("--- A1 report (7.6 step 2): %s, k = 1 decisive timing, k = 0 beside; net of costs; design months only" %
        cfg["name"])
    out("arm | timing | era | months | net Sharpe | mean %/yr | vol %/yr | worst drawdown % | dSR vs free | lb95 | se")
    for name, _ in arms:
        for tm in ("k1", "k0"):
            for era, a, b in ERAS:
                s = _stats(res[name][tm]["net"], a, b)
                if s is None:
                    out("%s | %s | %s | too few months" % (name, tm, era))
                    continue
                txt = "%s | %s | %s | %d | %.3f | %.2f | %.2f | %.1f" % (name, tm, era, s["n"], s["sr"],
                                                                      s["mean"] * 100, s["vol"] * 100,
                                                                      s["maxdd"] * 100)
                if name != base:
                    t = ST.paired_sr_test(ST.cut(res[base][tm]["net"], a, b), ST.cut(res[name][tm]["net"], a, b))
                    if t.get("identical"):
                        txt += " | 0.000 (identical) | - | -"
                    else:
                        txt += " | %+.3f | %+.3f | %.3f" % (t["dsr"], t["lb95"], t.get("se", float("nan")))
                out(txt)
    out("--- differences explained: family x class block Sharpe (unit-volatility blocks, k = 0 book's blocks table), "
        "1975-2010, blocks with at least %d months; '=' when identical to the free arm" % MIN_PRINT)
    bl0 = res[base]["k0"]["blocks"]
    for name, a1 in arms[1:]:
        bl = res[name]["k0"]["blocks"]
        parts = []
        for col in sorted(set(bl0.columns) | set(bl.columns), key=str):
            x0 = ST.cut(bl0[col], "1975-01", "2010-12") if col in bl0 else pd.Series(dtype=float)
            x1 = ST.cut(bl[col], "1975-01", "2010-12") if col in bl else pd.Series(dtype=float)
            if len(x0) == len(x1) and np.allclose(x0.values, x1.values, rtol=0, atol=1e-12):
                continue
            s0 = "%.2f (%d)" % (ST.sharpe(x0), len(x0)) if len(x0) >= MIN_PRINT else "n<%d" % MIN_PRINT
            s1 = "%.2f (%d)" % (ST.sharpe(x1), len(x1)) if len(x1) >= MIN_PRINT else "n<%d" % MIN_PRINT
            parts.append("%s/%s %s -> %s" % (col[0], col[1], s0, s1))
        out("%s | blocks that differ: %s" % (name, "; ".join(parts) if parts else "none"))
        out("%s | series extended: %s" % (name, "; ".join("%s %s %s..%s (%d months)" % (k[0], k[1], v[0], v[1], v[2])
                                                             for k, v in sorted(a1["added"].items())) or "none"))
    out("--- k = 1 flagged share (market-months earning the k = 0 return for lack of a daily price), share of gross "
        "position, 1975-2010")
    for name, _ in arms:
        bk = res[name]["k1"]
        fs = EX.flag_share_by_year(bk["pos"], bk["k1_flags"])
        held = bk["pos"].shift(1).abs()
        f = bk["k1_flags"].reindex(index=held.index, columns=held.columns).fillna(False).astype(bool)
        sel = (held.index >= pd.Period("1975-01", "M")) & (held.index <= DESIGN_END)
        tot = float(held[sel].sum().sum())
        share = float(held[sel].where(f[sel], 0.0).sum().sum()) / tot if tot > 0 else float("nan")
        out("%s | flagged share %.3f | years with any flag %d" % (name, share, int((fs.loc[1975:2010] > 0).sum())))
    return res


def trial_row(cfg, res_all, panel_id_, engine_version, lock_id):
    """The gm/trials.csv row of family 'data' for the all-blocks arm (k = 1), as gm/trials.py writes it."""
    from gm import config as CF
    from gm import stats as ST
    net = res_all["k1"]["net"]
    d, e = ST.summary(net), ST.summary(net, *ST.EXTRA)
    return {"trial": "A1 data swap (all blocks, k = 1)", "family": "data", "hash": CF.cfg_hash(cfg),
            "sr_9010": round(d["sr"], 3), "t_9010": round(d["t"], 2), "maxdd_9010": round(d["maxdd"], 3),
            "sr_7589": round(e["sr"], 3),
            "turnover": round(float(ST.cut(res_all["k1"]["turnover"], *ST.DESIGN).mean() * 12), 1),
            "note": "TESTING_PROTOCOL 7.6 step 2 A1 report arm; engine %s; LOCK_v2 %s; A1 panel %s" % (
                engine_version, lock_id[:16], panel_id_[:16])}


def save_panel(work, a1):
    """The A1 panel values -> work/a1/a1_panel_<id12>.pkl (PC only; never printed)."""
    import pickle
    d = os.path.join(work, "a1")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "a1_panel_%s.pkl" % a1["panel_id"][:12])
    with open(p + ".tmp", "wb") as f:
        pickle.dump({"R": a1["R"], "S": a1["S"], "admitted": a1["admitted"], "panel_id": a1["panel_id"],
                     "version": VERSION}, f)
    os.replace(p + ".tmp", p)
    return p
