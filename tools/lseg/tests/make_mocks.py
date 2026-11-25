"""Mock LSEG pull workbooks with the real layouts and INVENTED numbers (no LSEG data): saved-result form of the four
functions (RHistory newest first with month labels; RDP.Data with an instrument column; DSGRID with Name/Code header rows
and last-weekday dates; HistoricalPricing with or without dates), a synthetic futures market whose continuous series
follow a known roll rule, and the L11 / weekly files filled from the REAL builder templates of code/.
Planted: a copy group (3 codes, identical arrays), a wrong series (CEDCS00), a block without dates (HP without
RH:Timestamp), invalid and empty blocks, a month label after the save day, values after 2010-12 (to be sealed), an
untouched code (TRY=), an economics series (45-day delay), a gap, a stale run, a shared identical run, holiday
month-ends."""
import datetime as dt
import math
import os
import sys

import numpy as np
from openpyxl import Workbook, load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(os.path.dirname(HERE), "code")
sys.path.insert(0, CODE)
import build_lseg_contract_pull as BCP  # noqa: E402
import build_lseg_weekly as BW  # noqa: E402

MONTHS = "FGHJKMNQUVXZ"
PULL = dt.datetime(2026, 11, 12, 12, 0)
L11_SAVED = dt.datetime(2026, 11, 24, 12, 0)
WEEKLY_SAVED = dt.datetime(2026, 11, 20, 18, 0)
VALUES = set()           # every value written, as text with 4 decimals (leak test)


def bdays(a, b):
    out, d = [], a
    while d <= b:
        if d.weekday() < 5:
            out.append(d)
        d += dt.timedelta(days=1)
    return out


def last_bday(y, m):
    d = dt.date(y + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1)
    while d.weekday() >= 5:
        d -= dt.timedelta(days=1)
    return d


def month_end(y, m):
    return dt.date(y + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1)


def add_bdays(d, n):
    step = 1 if n >= 0 else -1
    while n:
        d += dt.timedelta(days=step)
        if d.weekday() < 5:
            n -= step
    return d


def months(a, b):
    y, m = a
    while (y, m) <= b:
        yield y, m
        y, m = (y + (m == 12), m % 12 + 1)


def put(v):
    v = round(float(v), 4)
    VALUES.add("%.4f" % v)
    return v


# ---------------------------------------------------------------------------------------------------- synthetic futures
class Fut:
    """A root with listed months, a last-trade rule, a first-notice rule and a deterministic price per contract."""

    def __init__(self, root, listed, lt_rule, fn_rule, y0, y1, base, seed):
        self.root, self.listed, self.base = root, listed, base
        rng = np.random.default_rng(seed)
        days = bdays(dt.date(y0 - 4, 1, 1), dt.date(2027, 12, 31))
        walk = np.cumsum(rng.normal(0, 0.01, len(days)))
        self.walk = dict(zip(days, walk))
        self.contracts = []
        for y in range(y0 - 1, 2030):
            for m in range(1, 13):
                if MONTHS[m - 1] not in listed:
                    continue
                lt, fnd = lt_rule(y, m), fn_rule(y, m)
                ric = "%s%s%d^%d" % (root, MONTHS[m - 1], y % 10, (y // 10) % 10)
                self.contracts.append({"y": y, "m": m, "lt": lt, "fn": fnd, "ric": ric, "k": len(self.contracts),
                                       "deliv": "%d-%02d" % (y, m)})
        self.contracts.sort(key=lambda c: (c["y"], c["m"]))
        for i, c in enumerate(self.contracts):
            c["k"] = i

    def held(self, n, d):
        live = [c for c in self.contracts if c["lt"] >= d]
        return live[n - 1] if len(live) >= n else None

    def price(self, c, d):
        mtd = (c["y"] - d.year) * 12 + c["m"] - d.month
        lvl = self.base * math.exp(self.walk[d])
        return lvl + 0.37 * mtd + 0.0131 * c["k"] + 0.0001 * ((d.toordinal() * 31 + c["k"] * 17) % 97)

    def c_monthly(self, n, a, b, label="calendar"):
        """[(date, value)]: value at the month's last business day; date = calendar month-end label or that day."""
        out = []
        for y, m in months(a, b):
            ld = last_bday(y, m)
            c = self.held(n, ld)
            if c is None:
                continue
            out.append((month_end(y, m) if label == "calendar" else ld, put(self.price(c, ld))))
        return out

    def c_daily(self, n, a, b):
        out = []
        for d in bdays(a, b):
            c = self.held(n, d)
            if c is not None:
                out.append((d, put(self.price(c, d))))
        return out

    def contract(self, ric):
        return next(c for c in self.contracts if c["ric"] == ric)

    def k_monthly(self, ric, a, b, label="calendar"):
        c, out = self.contract(ric), []
        for y, m in months(a, b):
            ld = min(last_bday(y, m), c["lt"])
            if ld < dt.date(y, m, 1) or (c["y"] - y) * 12 + c["m"] - m > 40:
                continue
            out.append((month_end(y, m) if label == "calendar" else ld, put(self.price(c, ld))))
        return out

    def k_daily(self, ric, a, b):
        c = self.contract(ric)
        return [(d, put(self.price(c, d))) for d in bdays(a, b) if d <= c["lt"]]


def lt_cl(y, m):        # 3 business days before the 25th of the month before delivery
    py, pm = (y - (m == 1), (m - 2) % 12 + 1)
    d = dt.date(py, pm, 25)
    while d.weekday() >= 5:
        d -= dt.timedelta(days=1)
    return add_bdays(d, -3)


def lt_ho(y, m):        # last business day of the month before delivery
    return last_bday(y - (m == 1), (m - 2) % 12 + 1)


def fn_ho(y, m):        # first business day of the delivery month
    d = dt.date(y, m, 1)
    return d if d.weekday() < 5 else add_bdays(d, 1)


def lt_ed(y, m):        # Monday before the third Wednesday of the delivery month
    d = dt.date(y, m, 1)
    d += dt.timedelta(days=(2 - d.weekday()) % 7)
    return d + dt.timedelta(days=14) - dt.timedelta(days=2)


def lt_gc(y, m):
    return add_bdays(last_bday(y, m), -2)


def fn_gc(y, m):
    return last_bday(y - (m == 1), (m - 2) % 12 + 1)


CL = Fut("CL", MONTHS, lt_cl, lambda y, m: add_bdays(lt_cl(y, m), 1), 1983, 2026, 30.0, 1)
HO = Fut("HO", MONTHS, lt_ho, fn_ho, 1979, 2026, 80.0, 2)
GC = Fut("GC", "GJMQVZ", lt_gc, fn_gc, 1975, 2026, 400.0, 3)
ED = Fut("ED", "HMUZ", lt_ed, lambda y, m: None, 1981, 2023, 95.0, 4)
SRA = Fut("SRA", "HMUZ", lt_ed, lambda y, m: None, 2018, 2026, 96.0, 5)
FUTS = {"CL": CL, "HO": HO, "GC": GC, "ED": ED, "SRA": SRA}


# ---------------------------------------------------------------------------------------------------- output shapes
def rh_out(pairs, header="Bid Close"):
    return [["Timestamp", header]] + [[dt.datetime(d.year, d.month, d.day), v] for d, v in sorted(pairs, reverse=True)]


def rd_out(ric, pairs, field="Bid Yield"):
    return [["Updated at 10:08:16"], [None, "Date", field]] + [[ric, dt.datetime(d.year, d.month, d.day), v]
                                                               for d, v in pairs]


def ds_out(codes, series, descs):
    """series: list of [(date, value)] per column, aligned on the union of dates (blank where missing)."""
    dates = sorted({d for s in series for d, _ in s})
    look = [dict(s) for s in series]
    rows = [["Name"] + descs, ["Code"] + codes]
    for d in dates:
        rows.append([dt.datetime(d.year, d.month, d.day)] + [lk.get(d) for lk in look])
    return rows


DS_ERR = [["Name", "#ERROR"], [None, "$$ER: E100,INVALID CODE OR EXPRESSION ENTERED"]]


def hp_out(pairs, dated=True):
    if dated:
        return [["Timestamp", "CLOSE"]] + [[dt.datetime(d.year, d.month, d.day), v] for d, v in pairs]
    return [["CLOSE"]] + [[v] for _, v in pairs]


HP_ERR = [["The universe is not found."]]


class Book:
    def __init__(self, name):
        self.name, self.wb, self.n, self.pos = name, Workbook(), 0, {}
        self.wb.active.title = "Check"
        self.wb.active["A1"] = "mock"

    def block(self, sheet, label, formula, out, w=6):
        if sheet not in self.wb.sheetnames:
            self.wb.create_sheet(sheet)
            self.pos[sheet] = 0
        ws = self.wb[sheet]
        c = 1 + self.pos[sheet] * w
        self.pos[sheet] += 1
        self.n += 1
        ws.cell(2, c, "%s-%03d" % (self.name.split("_")[0], self.n))
        ws.cell(3, c, label)
        ws.cell(4, c, "formula: " + formula.lstrip("="))
        for i, row in enumerate(out):
            for j, v in enumerate(row):
                if v is not None:
                    ws.cell(6 + i, c + j, v)

    def save(self, d, when=PULL):
        p = os.path.join(d, self.name + ".xlsx")
        self.wb.save(p)
        t = when.timestamp()
        os.utime(p, (t, t))
        return p


def rh_f(ric, fam="BID"):
    return '=RHistory("%s","%s.Timestamp;%s.Close","START:01-Jan-1975 INTERVAL:1MO",,"TSREPEAT:NO CH:Fd")' % (ric, fam, fam)


def rd_f(ric, f):
    return '=RDP.Data("%s","%s.date;%s","SDate=1975-01-01 EDate=2026-11-12 Frq=M CH=Fd RH=IN")' % (ric, f, f)


def ds_f(code, dtp="", start="1969-12-31", frq="M"):
    return '=DSGRID("%s","%s","%s","-0D","%s","%s","")' % (code, dtp, start, frq, BCP.DSOPT)


def hp_f(ric, interval="P1M", dated=True, start="01-Jan-1970"):
    f = '=RDP.HistoricalPricing("%s","CLOSE","START:%s END:12-Nov-2026 INTERVAL:%s SOURCE:RFV"' % (ric, start, interval)
    return f + (',,"%s")' % BCP.DATED if dated else ")")


def walk_series(seed, a, b, base, kind="lastwd", step=0.02):
    rng = np.random.default_rng(seed)
    out, lvl = [], base
    for y, m in months(a, b):
        lvl *= math.exp(rng.normal(0, step))
        d = last_bday(y, m) if kind == "lastwd" else (month_end(y, m) if kind == "calendar" else
                                                      add_bdays(last_bday(y, m), -(y % 2)))
        out.append((d, put(lvl)))
    return out


# ---------------------------------------------------------------------------------------------------- the pull files
def make_pull(d):
    os.makedirs(d, exist_ok=True)
    paths = []
    # L1a: RHistory FX spot, newest first, label for November 2026 after the save day (future-dated); TRY untouched
    b = Book("L1a_fx_spot_forwards")
    eur = walk_series(11, (1975, 1), (2026, 11), 1.2, "calendar")
    b.block("Spot", "EUR spot vs USD", rh_f("EUR="), rh_out(eur))
    b.block("Spot", "JPY spot vs USD", rh_f("JPY="), rh_out(walk_series(12, (1975, 1), (2026, 10), 200, "calendar")))
    b.block("Spot", "TRY spot vs USD", rh_f("TRY="), rh_out(walk_series(13, (1990, 1), (2026, 10), 2, "calendar")))
    paths.append(b.save(d))
    # L2a: Datastream benchmark yield + return index (two columns), one invalid code
    b = Book("L2a_rates_datastream")
    ry = walk_series(21, (1979, 12), (2026, 10), 8.0)
    ri = walk_series(22, (1979, 12), (2026, 10), 100.0)
    b.block("DS bench 10y", "United States 10y benchmark: yield, return index", ds_f("BMUS10Y", "RY,RI"),
            ds_out(["BMUS10Y(RY)", "BMUS10Y(RI)"], [ry, ri], ["US BENCHMARK 10 YEAR DS GOVT. INDEX - RED. YIELD",
                                                            "US BENCHMARK 10 YEAR DS GOVT. INDEX - TOT RETURN IND"]))
    b.block("DS bench 30y", "Norway 30y benchmark: yield, return index", ds_f("BMNW30Y", "RY,RI"), DS_ERR)
    paths.append(b.save(d))
    # L2b: RDP.Data yield with an instrument column; actual last trading days
    b = Book("L2b_rates_workspace")
    b.block("Yield 10y", "US 10y government bid yield", rd_f("US10YT=RR", "TR.BIDYIELD"),
            rd_out("US10YT=RR", walk_series(23, (1976, 6), (2026, 10), 7.0, "trading")))
    paths.append(b.save(d))
    # L3: an economics series (45-day delay), a gap and a stale run
    b = Book("L3_equity_markets")
    cpi = walk_series(31, (1970, 1), (2026, 10), 40.0, step=0.003)
    b.block("DS other", "US CPI", ds_f("USCONPRCE"), ds_out(["USCONPRCE"], [cpi], ["US CPI - SA"]), 8)
    gold = walk_series(32, (1975, 1), (2026, 10), 300.0)
    gold = [p for p in gold if not (dt.date(1990, 2, 1) <= p[0] <= dt.date(1990, 7, 31))]       # 6-month gap
    b.block("DS other", "Gold bullion", ds_f("GOLDBLN"), ds_out(["GOLDBLN"], [gold], ["GOLD BULLION LBM"]), 8)
    wti = walk_series(33, (1983, 4), (2026, 10), 30.0)
    for i in range(100, 108):                                                                 # 8 unchanged months
        wti[i] = (wti[i][0], wti[99][1])
    b.block("DS other", "WTI spot", ds_f("CRUDOIL"), ds_out(["CRUDOIL"], [wti], ["CRUDE OIL-WTI SPOT"]), 8)
    paths.append(b.save(d))
    # L4a: energy curves (HistoricalPricing, dated, calendar month-end labels) from the synthetic market
    b = Book("L4a_curves_energy")
    for n in range(1, 7):
        b.block("WTI crude", "WTI crude contract %d" % n, hp_f("CLc%d" % n), hp_out(CL.c_monthly(n, (1983, 4), (2026, 10))))
    for n in range(1, 13):
        b.block("Heating oil", "Heating oil contract %d" % n, hp_f("HOc%d" % n),
                hp_out(HO.c_monthly(n, (1979, 1), (2026, 10))))
    paths.append(b.save(d))
    b = Book("L4b_curves_metals_agri")
    for n in range(1, 5):
        b.block("Metals", "Gold contract %d" % n, hp_f("GCc%d" % n), hp_out(GC.c_monthly(n, (1975, 1), (2026, 10))))
    paths.append(b.save(d))
    # L5: a block without dates (HistoricalPricing without RH:Timestamp)
    b = Book("L5_financial_futures")
    b.block("Rate futures", "Euribor contract 1 (no display option)", hp_f("FEIc1", dated=False),
            hp_out(walk_series(51, (1994, 1), (2026, 10), 95.0, "calendar"), dated=False))
    b.block("Rate futures", "3m SOFR contract 1", hp_f("SRAc1"), hp_out(SRA.c_monthly(1, (2018, 6), (2026, 10))))
    paths.append(b.save(d))
    # L6: a copy group (three codes, identical arrays), a shared identical run, an empty block
    b = Book("L6_indexes_datastream")
    same = walk_series(61, (1983, 1), (2026, 10), 100.0)
    for code in ("GSCLTOT", "GSNGTOT", "GSGCTOT"):
        b.block("GSCI", "GSCI %s" % code, ds_f(code), ds_out([code], [same], ["S&P GSCI ... TOT RETURN"]))
    sb = walk_series(62, (1980, 1), (2026, 10), 50.0)
    kc = walk_series(63, (1980, 1), (2026, 10), 70.0)
    kc = [(dd, v2) if not (dt.date(1990, 1, 1) <= dd <= dt.date(1992, 6, 30)) else (dd, v1)
          for (dd, v2), (_, v1) in zip(kc, sb)]
    b.block("GSCI", "GSCI sugar", ds_f("GSSBTOT"), ds_out(["GSSBTOT"], [sb], ["S&P GSCI SUGAR TOT RETURN"]))
    b.block("GSCI", "GSCI coffee", ds_f("GSKCTOT"), ds_out(["GSKCTOT"], [kc], ["S&P GSCI COFFEE TOT RETURN"]))
    b.block("Other indexes", "Citi surprise China", hp_f(".CESICNY"), [])
    paths.append(b.save(d))
    # L7: deposit rates; economics sheet
    b = Book("L7_rates_swaps_economics")
    b.block("Short rates", "US dollar 3m deposit rate", ds_f("ECUSD3M"),
            ds_out(["ECUSD3M"], [walk_series(71, (1975, 1), (2026, 10), 6.0)], ["US EURO-$ 3 MONTH (LDN:FT) - MIDDLE RATE"]))
    b.block("Short rates", "Japanese yen 3m deposit rate", ds_f("ECJAP3M"),
            ds_out(["ECJAP3M"], [walk_series(72, (1978, 1), (2026, 10), 5.0)], ["JAPANESE YEN 3M DEPOSIT"]))
    paths.append(b.save(d))
    # L8: wrong series, a duplicate of an L10 Eurodollar block, forward EPS
    b = Book("L8_fixes_and_alternatives")
    b.block("Ended rate futures", "Eurodollar continuous (DS guess CED)", ds_f("CEDCS00"),
            ds_out(["CEDCS00"], [walk_series(81, (2007, 11), (2008, 10), 5.0)], ["CME-S&P GRA DESERT WEST CONT. DEAD"]))
    b.block("Ended rate futures", "Eurodollar via Workspace code in Datastream", ds_f("<EDc1>"),
            ds_out(["<EDc1>"], [ED.c_monthly(1, (1981, 12), (2023, 5), "lastwd")], ["CME-3 MTH EURODOLLAR COMP. TRc1 DEAD"]))
    b.block("Indexes", "S&P 500 12m forward EPS (IBES aggregate guess)", ds_f("@:USSP500", "A12FE"),
            ds_out(["@:USSP500(A12FE)"], [walk_series(82, (1985, 1), (2026, 10), 20.0)], ["S&P 500 12M FWD EPS"]))
    paths.append(b.save(d))
    # L9a: daily c1/c2 (weekdays) for CL and HO
    b = Book("L9a_daily_commodities")
    for n in (1, 2):
        b.block("Commodities c%d" % n, "CL contract %d, daily" % n, hp_f("CLc%d" % n, "P1D", start="01-Jan-1990"),
                hp_out(CL.c_daily(n, dt.date(1990, 1, 1), dt.date(2012, 12, 31))))
        b.block("Commodities c%d" % n, "HO contract %d, daily" % n, hp_f("HOc%d" % n, "P1D", start="01-Jan-1990"),
                hp_out(HO.c_daily(n, dt.date(1990, 1, 1), dt.date(2012, 12, 31))))
    paths.append(b.save(d))
    # L10: Eurodollar strip monthly c1-c12 (last weekday), daily c1, c2, c4, c8; BAX c2 invalid
    b = Book("L10_rate_strips_swaps_guesses")
    for n in range(1, 13):
        b.block("Rate futures strips", "Eurodollar contract %d" % n, ds_f("<EDc%d>" % n),
                ds_out(["<EDc%d>" % n], [ED.c_monthly(n, (1981, 12), (2023, 5), "lastwd")],
                       ["CME-3 MTH EURODOLLAR COMP. TRc%d DEAD - SETT. PRICE" % n]))
    b.block("Rate futures strips", "Canada BA contract 2", ds_f("<BAXc2>"), DS_ERR)
    for n in (1, 2, 4, 8):
        b.block("Rate futures daily", "Eurodollar contract %d, daily" % n, ds_f("<EDc%d>" % n, start="1989-12-29", frq="D"),
                ds_out(["<EDc%d>" % n], [ED.c_daily(n, dt.date(1989, 12, 29), dt.date(2012, 12, 31))],
                       ["CME-3 MTH EURODOLLAR COMP. TRc%d DEAD - SETT. PRICE" % n]))
    paths.append(b.save(d))
    # a probe file (must be listed, not read)
    b = Book("P2_probe_futures_indexes_econ")
    b.block("Futures dates", "CLc1", hp_f("CLc1"), hp_out(CL.c_monthly(1, (1983, 4), (2026, 10))))
    paths.append(b.save(d))
    return paths


# ---------------------------------------------------------------------------------------------------- L11 from the template
def _blocks(ws):
    ids = [c.value for c in next(ws.iter_rows(min_row=2, max_row=2))]
    for c, v in enumerate(ids):
        if isinstance(v, str) and v.startswith("L11-"):
            yield c + 1, ws.cell(3, c + 1).value, ws.cell(4, c + 1).value


def _write(ws, c, out):
    for i, row in enumerate(out):
        for j, v in enumerate(row):
            ws.cell(6 + i, c + j, v)


def make_l11(d, template_dir):
    p, rows, contracts = BCP.build(template_dir)
    wb = load_workbook(p)
    clist = {ric: (root, deliv) for root, ric, deliv, form in contracts}
    cal_true = {}
    for f in FUTS.values():
        for c in f.contracts:
            cal_true[c["ric"]] = c
            if (c["y"], c["m"]) >= (2026, 10):                  # live RIC form of the same contract
                cal_true["%s%s%d" % (f.root, MONTHS[c["m"] - 1], c["y"] % 10)] = c
    for sh in wb.sheetnames:
        ws = wb[sh]
        if sh in ("Check", "Contracts", "TestContracts"):
            continue
        for c, label, ftxt in _blocks(ws):
            t = ftxt.replace("formula: ", "")
            if sh == "ED daily":
                n = int(t.split('"<EDc')[1].split(">")[0])
                _write(ws, c, ds_out(["<EDc%d>" % n], [ED.c_daily(n, dt.date(1989, 12, 29), dt.date(2012, 12, 31))],
                                     ["CME-3 MTH EURODOLLAR COMP. TRc%d DEAD - SETT. PRICE" % n]))
            elif sh == "Curve depth":
                ric = t.split('("')[1].split('"')[0]
                if ric.startswith("HO"):
                    n = int(ric[3:])
                    _write(ws, c, hp_out(HO.c_monthly(n, (1979, 1), (2026, 10))))
                else:
                    _write(ws, c, HP_ERR)
            elif sh == "Contract sample":
                code = t.split('("')[1].split('"')[0].strip("<>")
                root = code[:2]
                f = FUTS.get(root)
                if f is None or code not in cal_true:
                    continue                                    # left empty: no result
                if t.startswith("DSGRID"):
                    daily = '"D"' in t
                    a = t.split('","')
                    s0, e0 = dt.date.fromisoformat(a[2]), dt.date.fromisoformat(a[3])
                    pairs = f.k_daily(code, s0, e0) if daily else f.k_monthly(code, (s0.year, s0.month),
                                                                              (e0.year, e0.month), "lastwd")
                    _write(ws, c, ds_out(["<%s>" % code], [pairs], ["CME-3MTH EURODOLLAR %s" % code]))
                else:
                    s0 = dt.datetime.strptime(t.split("START:")[1].split()[0], "%d-%b-%Y").date()
                    e0 = dt.datetime.strptime(t.split("END:")[1].split()[0], "%d-%b-%Y").date()
                    pairs = f.k_daily(code, s0, e0) if "P1D" in t else f.k_monthly(code, (s0.year, s0.month),
                                                                                   (e0.year, e0.month))
                    _write(ws, c, hp_out(pairs))
            elif sh in ("Calendar", "Calendar test"):
                rng = t.split("(")[1].split(",")[0]
                r0, r1 = [int(x.split("$")[-1]) for x in rng.split("!")[1].split(":")]
                src = wb["Contracts" if sh == "Calendar" else "TestContracts"]
                field = t.split(',"')[1].split('"')[0]
                out = [["Instrument", field.replace("TR.", "")]]
                for r in range(r0, r1 + 1):
                    ric = src.cell(r, 2).value
                    tc = cal_true.get(ric)
                    if field in ("TR.LastTradingDate", "TR.ExpirationDate"):
                        val = "The formula is invalid: unknown field %s" % field
                    elif tc is None:
                        val = "Unable to resolve all requested identifiers"
                    elif field == "TR.ExpiryDate" or field == "TR.LastTradeDate":
                        val = tc["lt"]
                    elif field == "TR.FirstNoticeDate":
                        val = tc["fn"] if tc["fn"] else None
                    else:
                        val = None
                    out.append([ric, dt.datetime(val.year, val.month, val.day) if isinstance(val, dt.date) else val])
                _write(ws, c, out)
            elif sh == "Identity probe":
                if "TR.ExpiryDate.date" in t and '"CLc1"' in t:
                    out = [["Updated at 09:00:00"], [None, "Date", "Expiry Date"]]
                    for y, m in months((2004, 12), (2006, 12)):
                        ld = last_bday(y, m)
                        out.append(["CLc1", dt.datetime(ld.year, ld.month, ld.day),
                                    dt.datetime.combine(CL.held(1, ld)["lt"], dt.time())])
                    _write(ws, c, out)
                elif "CLc1,CLc2,CLc12" in t:
                    _write(ws, c, [["Instrument", "Expiry Date"]] + [[r, "No data available"] for r in
                                                                     ("CLc1", "CLc2", "CLc12")])
                else:
                    _write(ws, c, HP_ERR)
    wb.save(os.path.join(d, "L11_contract_identity.xlsx"))
    out = os.path.join(d, "L11_contract_identity.xlsx")
    t = L11_SAVED.timestamp()
    os.utime(out, (t, t))
    return out, clist


# ---------------------------------------------------------------------------------------------------- weekly
def make_weekly(d, template_dir, saved=WEEKLY_SAVED, shift=0.0, stale_code="HOc5"):
    p, rows, plist = BW.build(template_dir)
    wb = load_workbook(p)
    end = saved.date()
    start = end - dt.timedelta(days=70)
    for sh in ("Curves", "Strips", "Monthly", "Identity now"):
        ws = wb[sh]
        ids = [c.value for c in next(ws.iter_rows(min_row=2, max_row=2))]
        for c, v in enumerate(ids, 1):
            if not (isinstance(v, str) and v.startswith("W-")):
                continue
            t = ws.cell(4, c).value
            if sh in ("Curves", "Strips"):
                ric = t.split('("')[1].split('"')[0]
                root, n = ric.split("c")[0], int(ric.split("c")[-1])
                f = FUTS.get(root)
                if f is None:
                    continue
                e = end - dt.timedelta(days=14) if ric == stale_code else end
                pairs = [(dd, put(vv + shift)) for dd, vv in f.c_daily(n, start, e)]
                _write(ws, c, hp_out(pairs))
            elif sh == "Monthly":
                _write(ws, c, ds_out(["@:USSP500(A12FE)"], [walk_series(91, (2025, 10), (2026, 10), 250.0)],
                                     ["S&P 500 12M FWD EPS"]))
            else:
                field = t.split(',"')[1].split('"')[0]
                out = [["Instrument", field]]
                for i, (root, ric, n) in enumerate(plist):
                    f = FUTS.get(root)
                    h = f.held(n, end) if f else None
                    if field == "TR.ExpiryDate" and h is not None:
                        out.append([ric, dt.datetime.combine(h["lt"], dt.time())])
                    else:
                        out.append([ric, "No data available"])
                _write(ws, c, out)
    out = os.path.join(d, "LSEG_weekly_live.xlsx")
    wb.save(out)
    t = saved.timestamp()
    os.utime(out, (t, t))
    return out
