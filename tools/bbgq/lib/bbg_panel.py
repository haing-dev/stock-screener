"""bbg_panel: serve the Bloomberg series that the book engine (gm/) uses from the LOCKED research tables
(bbgdata.Panel(...).asof(T)) instead of the old single-workbook reader gm/bloomberg.py. gm/ is not changed.

How: gm/bloomberg.py reads everything through load(), which returns a cached dict {sheet: {ticker: DataFrame(index =
month Period, columns = fields)}} (gm.bloomberg._CACHE["wb"]). This module builds exactly that dict from bbgdata and puts
it in the cache (install / using), so every gm function (commodity_return, commodity_carry, value_composite, surprise,
short_rate_market, implied_path, breakeven, benchmark_returns) serves Bloomberg data with gm's own conventions:
same sheet names and tickers as file 1 of the first pull (the old single workbook), monthly values indexed by month.

Which copy of a series: the primary series id "TICKER|FIELD" of bbgdata (the copy with the longest history, which may
sit in another file, e.g. a commodity curve point from file 5 or a re-pulled block). Which tickers: the old workbook's
universe, i.e. the tickers bbgdata catalogues under file 1 and the sheet name gm uses (Returns, Curves, EquityValuation,
Economics, RatesFutures, Breakevens, Benchmarks).
Dating: market data (prices, curves, valuations, rates futures, breakevens, benchmarks) by OBSERVATION month, like the
free data (the engine decides at the month-end close); economic releases (Economics) by the month in which they became
KNOWN (release date, bbgdata.AsOf.known) unless econ_dating="obs" (= the old reader's convention).
Everything goes through asof(T) with T <= 2010-12-31: nothing later than what was knowable on T is served (a series with a
one-day live delay therefore ends one month-end before T), held-back (untouched) markets stay invisible, and the sealed
2011+ tables are never opened.

Chosen markets: workbook(markets=[...]) serves only the Returns / Curves / EquityValuation tickers that gm maps to those
markets; every other market stays on free data (gm falls back to its free sources when a Bloomberg series is absent).
"""
import os
import re

import pandas as pd

import bbgdata

VERSION = "bbg_panel-1.0.0"
FILE1 = "1"
SHEETS = ("Returns", "Curves", "EquityValuation", "Economics", "RatesFutures", "Breakevens", "Benchmarks")
MARKET_SHEETS = ("Returns", "Curves", "EquityValuation")       # sheets that belong to one market each
RELEASE_SHEETS = ("Economics",)
VALUATION_FIELDS = ("PE_RATIO", "BEST_PE_RATIO", "PX_TO_BOOK_RATIO", "EQY_DVD_YLD_12M", "BEST_EPS")


def gm_maps():
    """The engine's own maps (gm/bloomberg.py, gm/panel.py, gm/signals.py)."""
    from gm import bloomberg as BBG
    from gm import panel as P
    from gm import signals as G
    return BBG, P, G


def _ticker_markets(BBG):
    """ticker -> set of gm markets that use it (returns, curves, equity valuation)."""
    out = {}
    for m, tks in BBG.COMMOD_ER.items():
        for t in tks:
            out.setdefault(("Returns", t), set()).add(m)
    for m, t in BBG.EQ_INDEX.items():
        out.setdefault(("EquityValuation", t), set()).add(m)
    return out


def _curve_root_of(ticker, roots):
    m = re.match(r"^(.+?)(\d+) Comdty$", ticker)
    return m.group(1) if m and m.group(1) in roots else None


class Source:
    """Bloomberg inputs for gm, as of one date. P: a bbgdata.Panel (or the work dir)."""

    def __init__(self, panel_or_work, asof="2010-12-31", econ_dating="release"):
        self.P = panel_or_work if isinstance(panel_or_work, bbgdata.Panel) else bbgdata.Panel(panel_or_work)
        self.asof_date = pd.Timestamp(asof)
        self.view = self.P.asof(asof)                      # raises HoldoutSealed after 2010-12-31
        self.econ_dating = econ_dating
        cat = self.P.catalog
        self.cat = cat
        prim = cat[(cat["series_id"] != "") & (cat["duplicate_of"] == "") & (cat["per"] == "M")]
        self.primary = {(r.ticker, r.field): r for r in prim.itertuples()}
        f1 = cat[(cat["file"] == FILE1) & (cat["sheet"].isin(SHEETS)) & (cat["per"] == "M")]
        self.universe = {}                                 # sheet -> [(ticker, [fields])] in workbook order
        for r in f1.itertuples():
            lst = self.universe.setdefault(r.sheet, [])
            if not lst or lst[-1][0] != r.ticker:
                lst.append((r.ticker, []))
            if r.field not in lst[-1][1]:
                lst[-1][1].append(r.field)

    # ---- one series
    def sid_for(self, ticker, field):
        """Primary series id for a ticker and field, or None (missing, failed, or held back)."""
        r = self.primary.get((ticker, field))
        return r.series_id if r is not None else None

    def series(self, ticker, field, sheet):
        sid = self.sid_for(ticker, field)
        if sid is None:
            return None
        info = self.P.info(sid, "M")
        if info["kind"] == "date":
            return None
        if sheet in RELEASE_SHEETS and self.econ_dating == "release":
            s = self.view.known(sid, "M")
        else:
            s = self.view.series(sid, "M")
        s = s.dropna()
        if not len(s):
            return None
        s.index = pd.DatetimeIndex(s.index).to_period("M")
        return s[~s.index.duplicated(keep="last")].astype("float64")

    # ---- the gm workbook dict
    def workbook(self, markets=None, sheets=SHEETS):
        """{sheet: {ticker: DataFrame(index=PeriodIndex M, columns=fields)}} in the format of gm.bloomberg.load().
        markets: None = all; else only the market-specific tickers (Returns, Curves, EquityValuation) of those
        markets, and no Economics / RatesFutures / Breakevens / Benchmarks unless named in `sheets`."""
        BBG, _P, _G = gm_maps()
        tm = _ticker_markets(BBG)
        roots = {r: m for m, r in BBG.CURVE_ROOT.items()}
        if markets is not None:
            markets = set(markets)
        out = {}
        for sheet in sheets:
            if sheet not in self.universe:
                continue
            blocks = {}
            for ticker, fields in self.universe[sheet]:
                if markets is not None:
                    if sheet == "Curves":
                        root = _curve_root_of(ticker, roots)
                        if root is None or roots[root] not in markets:
                            continue
                    elif sheet in MARKET_SHEETS:
                        if not (tm.get((sheet, ticker), set()) & markets):
                            continue
                cols = {}
                for f in fields:
                    s = self.series(ticker, f, sheet)
                    if s is not None:
                        cols[f] = s
                if not cols:
                    continue
                # every field of the block as a column (NaN where it has no data), as the old single-file reader did:
                # gm/bloomberg.py value_composite expects all valuation fields to be present
                df = pd.DataFrame(cols).sort_index().reindex(columns=fields)
                df = df.dropna(how="all")
                if len(df):
                    blocks[ticker] = df
            out[sheet] = blocks
        return out


def install(wb):
    """Put the workbook dict into gm.bloomberg's cache. Returns a function that restores the previous state."""
    from gm import bloomberg as BBG
    had, prev = "wb" in BBG._CACHE, BBG._CACHE.get("wb")
    BBG._CACHE["wb"] = wb

    def restore():
        if had:
            BBG._CACHE["wb"] = prev
        else:
            BBG._CACHE.pop("wb", None)
    return restore


class using:
    """with bbg_panel.using(Source(work).workbook(markets=[...])): ... gm runs with Bloomberg inputs ..."""

    def __init__(self, wb):
        self.wb = wb

    def __enter__(self):
        self._restore = install(self.wb)
        return self.wb

    def __exit__(self, *exc):
        self._restore()
        return False


# =====================================================================================================================
# coverage map (metadata only): which Bloomberg series each engine input would use
# =====================================================================================================================
FREE_INPUTS = {
    "eq_": [("return", "free: country ETF / MSCI manual file / Ken French / index + dividend proxy, minus local 3m rate"),
            ("carry", "not used by the book (equity carry dropped)"),
            ("value (without Bloomberg)", "free: dividend yield (Ken French, SPY minus S&P 500)"),
            ("econ themes", "free: OECD CPI, BIS NEER, 2y yields / 3m rates, equity momentum, BAA spread")],
    "bd_": [("return", "free: month-end yields (FRED, central banks, stooq), par-bond pricing, minus 3m rate"),
            ("carry", "free: yield minus 3m rate"), ("value", "free: 10y yield minus 3y average CPI inflation"),
            ("econ themes", "free")],
    "st_": [("return", "free: 2y / 5y month-end yields, par-note pricing"), ("carry", "free: yield minus 3m rate"),
            ("econ themes", "free")],
    "fx_": [("return", "free: FRED H.10 / Yahoo / stooq spot + 3m rate differential"),
            ("carry", "free: 3m rate differential"), ("value", "free: 5-year real exchange-rate change"),
            ("econ themes", "free (local minus US)")],
    "cm_": [("return (without Bloomberg)", "free: EIA contract-2 roll / ETF / Yahoo / stooq front"),
            ("carry (without Bloomberg)", "free: EIA F1/F2 for the four NYMEX energies; none for the rest"),
            ("econ themes", "free (global demand block)")],
    "sp_": [("return", "free: FRED / Bundesbank yields")],
}


def engine_map(P, markets=None, asof="2010-12-31"):
    """Rows (market, input, route, series id, status, first design date, design months, served as of, used by gm)
    for every market of the engine and every input that gm/bloomberg.py can take from Bloomberg; plus what stays free.
    Metadata only: names, statuses, dates, counts."""
    BBG, Pm, G = gm_maps()
    src = Source(P, asof=asof)
    cat = src.cat
    allrows = {(r.ticker, r.field): r for r in cat.itertuples() if r.per == "M"}
    allcat = bbgdata.read_catalog(os.path.dirname(P.root)) if hasattr(P, "root") else cat
    hidden = {(r.ticker, r.field): r for r in allcat.itertuples() if r.per == "M" and int(r.untouched) == 1}
    curves = sorted({r.ticker for r in allcat.itertuples() if r.file == FILE1 and r.sheet == "Curves"})

    def look(ticker, field, sheet, gm_min):
        r = src.primary.get((ticker, field))
        if r is None:
            if (ticker, field) in hidden:
                return {"sid": "%s|%s" % (ticker, field), "status": "held back (untouched market)", "first": "-",
                        "n": 0, "served": 0, "used": False}
            r2 = allrows.get((ticker, field))
            return {"sid": "%s|%s" % (ticker, field), "status": "not in the lock" if r2 is None else r2.status,
                    "first": "-", "n": 0, "served": 0, "used": False}
        s = src.series(ticker, field, sheet)
        served = 0 if s is None else int(s.notna().sum())
        first = "-"
        if r.n_design:
            col = src.P.tables["M"][r.series_id]
            first = col.first_valid_index().strftime("%Y-%m") if col.notna().any() else "-"
        where = "%s|%s" % (r.file, r.sheet)
        return {"sid": r.series_id, "status": "ok (%s, source %s)" % (where, getattr(r, "source", "first") or "first"),
                "first": first, "n": int(r.n_design), "served": served, "used": served > gm_min}

    markets = list(markets) if markets is not None else None
    rows = []
    eq_markets = list(Pm.EQUITY)
    all_markets = (eq_markets + list(Pm.BONDS) + list(Pm.SHORT) + list(Pm.FXM) + list(Pm.COMMOD) + list(Pm.SPREADS)
                   + list(BBG.ALT_COMMOD))
    for m in all_markets:
        if markets is not None and m not in markets:
            continue
        pre = m[:3]
        bb_inputs = []
        if m in BBG.COMMOD_ER:
            alt = m in BBG.ALT_COMMOD
            for t in BBG.COMMOD_ER[m]:
                bb_inputs.append(("return", "Returns", t, "PX_LAST", 36 if alt else 24))
            root = BBG.CURVE_ROOT.get(m)
            if root:
                f1 = root + "1 Comdty"
                far = sorted([t for t in curves if re.match(re.escape(root) + r"(\d+) Comdty$", t) and t != f1],
                             key=lambda t: int(re.findall(r"(\d+) Comdty$", t)[0]))
                bb_inputs.append(("carry (front)", "Curves", f1, "PX_LAST", 24))
                bb_inputs.append(("carry (farthest contract)", "Curves", far[-1] if far else root + "?? Comdty",
                                  "PX_LAST", 24))
        if m in BBG.EQ_INDEX and m.startswith("eq_"):
            t = BBG.EQ_INDEX[m]
            for f in ("BEST_PE_RATIO", "PE_RATIO", "PX_TO_BOOK_RATIO", "EQY_DVD_YLD_12M"):
                bb_inputs.append(("value composite", "EquityValuation", t, f, 0))
        got_return = False
        for inp, sheet, t, f, gm_min in bb_inputs:
            x = look(t, f, sheet, gm_min)
            if inp == "return":                      # gm takes the FIRST index with enough data (GSCI, else BCOM)
                if got_return and x["used"]:
                    x["used"], x["status"] = False, x["status"] + "; fallback, not needed"
                got_return = got_return or x["used"]
            rows.append({"market": m, "input": inp, "route": "Bloomberg", **x})
        if m in BBG.ALT_COMMOD:
            rows.append({"market": m, "input": "all inputs", "route": "no free source: the market exists only with "
                         "Bloomberg data (gm adds it when its return has more than 36 months)", "sid": "-",
                         "status": "-", "first": "-", "n": 0, "served": 0, "used": False})
            continue
        for inp, note in FREE_INPUTS.get(pre, []):
            rows.append({"market": m, "input": inp, "route": note, "sid": "-", "status": "-", "first": "-", "n": 0,
                         "served": 0, "used": False})
    # growth surprises: per country (GROWTH_SOURCE is 'off' in BASE and CANDIDATE)
    for cc, lst in G.SURPRISE_MAP.items():
        for t, _sg in lst:
            for f in ("ACTUAL_RELEASE", "BN_SURVEY_MEDIAN"):
                x = look(t, f, "Economics", 24)
                if G.GROWTH_SOURCE != "surprise":           # BASE and CANDIDATE: growth theme switched off
                    x["used"], x["used_note"] = False, "no (GROWTH_SOURCE %s)" % G.GROWTH_SOURCE
                rows.append({"market": "country %s" % cc, "input": "growth surprise", "route": "Bloomberg", **x})
    return rows, src


def gm_mapping_notes():
    """Observations on gm/bloomberg.py's maps (reported, not changed)."""
    BBG, _P, _G = gm_maps()
    notes = []
    same = [m for m, t in BBG.EQ_INDEX.items() if t == "MXUS Index" and m != "eq_us_spx"]
    if same:
        notes.append("gm/bloomberg.py EQ_INDEX maps %s to MXUS Index as well: in the value composite they carry the "
                     "S&P 500's valuation (MSCI USA), not their own" % ", ".join(same))
    return notes
