"""lseg_rules: contract calendar from exchange rules (lsegdata 1.0.1; TESTING_PROTOCOL 7.10 item 3 step 2).

Why: the L11 refresh (2026-11-24) returned no contract date for any of 12,736 contracts (TR.ExpiryDate NULL /
"unable to collect", TR.LastTradeDate "access to field(s) denied", the rest "no output"), so LSEG cannot supply the
calendar on this licence. The calendar is therefore COMPUTED from each exchange's last-trading-day and first-notice
rules (below, design era 1972-2010 plus the live years) and CHECKED against what LSEG does show: (a) sample contracts
matched by value to the continuous positions (which position held the contract on each date), (b) the last date a
sample contract has a daily price (= its observed last trading day), (c) TR.ExpiryDate as a dated series on
continuation RICs where it returns dates. A root's identity is registered only where the check agrees (>= 99% of
matched observations, lseg_check_v3).

Rules are written from the exchanges' contract specifications as understood here; every one is a hypothesis that the
check confirms or rejects (approximate holiday calendars of lsegdata.holidays: US for US exchanges, UK for London).
Listed months: the months each continuous series steps through. Where an exchange also lists near serial months
(metals, short-rate futures since the 1990s), whether LSEG's cN steps through them is not known: both variants are
built ("base" = the regular cycle only, "serial" = plus the nearest serial months) and the check reports agreement
for each; nothing is assumed."""
import datetime as dt

import pandas as pd

import lsegdata as LD

VERSION = "lseg_rules-1.1.0"
CYCLE = {
    "CL": "FGHJKMNQUVXZ", "LCO": "FGHJKMNQUVXZ", "NG": "FGHJKMNQUVXZ", "HO": "FGHJKMNQUVXZ", "RB": "FGHJKMNQUVXZ",
    "GC": "GJMQVZ", "SI": "HKNUZ", "HG": "HKNUZ", "PL": "FJNV",
    "C": "HKNUZ", "W": "HKNUZ", "S": "FHKNQUX", "SB": "HKNV", "KC": "HKNUZ", "CT": "HKNVZ", "LC": "GJMQVZ",
    "ED": "HMUZ", "FEI": "HMUZ", "FSS": "HMUZ", "FES": "HMUZ", "SRA": "HMUZ", "SON3": "HMUZ",
}
# serial variant: the nearest N calendar months are listed as well (exchange practice; to be confirmed by the check)
SERIAL_NEAR = {"GC": 3, "SI": 3, "HG": 3, "PL": 3, "ED": 4, "FEI": 2, "FSS": 2, "SRA": 4, "SON3": 3}
SERIAL_FROM = {"GC": 1975, "SI": 1975, "HG": 1975, "PL": 1975, "ED": 1995, "FEI": 1999, "FSS": 2004, "SRA": 2018,
               "SON3": 2018}
MARKET = {"LCO": "UK", "FSS": "UK", "FES": "UK", "FEI": "UK", "SON3": "UK"}
FND = {"GC", "SI", "HG", "PL", "C", "W", "S", "KC", "CT", "LC"}


def _bd(d, mk):
    return d.weekday() < 5 and not (LD.hol_flag(d) & (1 if mk == "US" else 2))


def _back(d, n, mk):
    """n business days before d (d itself not counted)."""
    while n:
        d -= dt.timedelta(days=1)
        if _bd(d, mk):
            n -= 1
    return d


def _on_or_before(d, mk):
    while not _bd(d, mk):
        d -= dt.timedelta(days=1)
    return d


def _on_or_after(d, mk):
    while not _bd(d, mk):
        d += dt.timedelta(days=1)
    return d


def _last_bd(y, m, mk):
    return _on_or_before(LD.month_end(dt.date(y, m, 1)), mk)


def _first_bd(y, m, mk):
    return _on_or_after(dt.date(y, m, 1), mk)


def _prev(y, m, k=1):
    i = y * 12 + m - 1 - k
    return i // 12, i % 12 + 1


def _third_wed(y, m):
    return LD._nth_wd(y, m, 2, 3)


def dates(root, y, m):
    """(last_trade, first_notice) of root's contract delivering in y-m, by the exchange rule; first_notice None where
    no delivery notice precedes the last trading day (cash settled, or notices only after it)."""
    mk = MARKET.get(root, "US")
    py, pm = _prev(y, m)
    fn = None
    if root == "CL":      # 3 business days before the 25th of the month before delivery (25th itself if a bd)
        d25 = dt.date(py, pm, 25)      # 25th not a bd: 3 bd before the last bd before it
        lt = _back(d25 if _bd(d25, mk) else _on_or_before(d25, mk), 3, mk)
    elif root == "LCO":   # to 2016-02: bd before the 15th day before the delivery month's 1st; then last bd of M-2
        if (y, m) <= (2016, 2):
            lt = _on_or_before(dt.date(y, m, 1) - dt.timedelta(days=16), mk)
        else:
            qy, qm = _prev(y, m, 2)
            lt = _last_bd(qy, qm, mk)
    elif root == "NG":    # 3 business days before the first calendar day of the delivery month
        lt = _back(dt.date(y, m, 1), 3, mk)
    elif root in ("HO", "RB"):   # last business day of the month before delivery
        lt = _last_bd(py, pm, mk)
    elif root in ("GC", "SI", "HG", "PL"):   # third last business day of the delivery month; FND last bd of M-1
        lt = _back(_last_bd(y, m, mk), 2, mk)
        fn = _last_bd(py, pm, mk)
    elif root in ("C", "W", "S"):            # bd before the 15th of the delivery month; FND last bd of M-1
        lt = _back(dt.date(y, m, 15), 1, mk)
        fn = _last_bd(py, pm, mk)
    elif root == "SB":    # last trading day of the month before delivery
        lt = _last_bd(py, pm, mk)
    elif root == "KC":    # 8 business days before the last bd of the delivery month; FND 7 bd before its first bd
        lt = _back(_last_bd(y, m, mk), 8, mk)
        fn = _back(_first_bd(y, m, mk), 7, mk)
    elif root == "CT":    # 17 business days from the end of the delivery month; FND 5 bd from the end of M-1
        lt = _back(_last_bd(y, m, mk), 16, mk)
        fn = _back(_last_bd(py, pm, mk), 4, mk)
    elif root == "LC":    # last business day of the delivery month; notices from its first business day
        lt = _last_bd(y, m, mk)
        fn = _first_bd(y, m, mk)
    elif root in ("ED", "FEI", "FES"):       # 2 business days before the third Wednesday (London / TARGET ~ UK)
        lt = _back(_third_wed(y, m), 2, "UK")
    elif root == "FSS":   # third Wednesday
        lt = _on_or_before(_third_wed(y, m), mk)
    elif root in ("SRA", "SON3"):            # reference quarter ends at the third Wednesday of M+3: bd before it
        ny, nm = _prev(y, m, -3)
        lt = _back(_third_wed(ny, nm), 1, mk)
    else:
        raise KeyError(root)
    return lt, fn


def listed(root, y, m, variant, asof=None):
    """Is the y-m contract listed (a position of the continuous series) under the variant."""
    code = LD.MONTH_CODES[m - 1]
    if code in CYCLE[root]:
        return True
    return variant == "serial" and root in SERIAL_NEAR and y >= SERIAL_FROM[root]


def rule_calendar(roots, variant="base", y0=1972, y1=2029):
    """Calendar frame (lsegdata.calendar_frame columns) for every root in roots (lseg_roots.csv dict) from the rules.
    variant 'serial' adds every calendar month for roots with near serial months: Calendar.held then counts them
    only while they are among the nearest SERIAL_NEAR months (see serial_mask)."""
    recs = []
    for root, rc in roots.items():
        if root not in CYCLE:
            continue
        rr = rc.get("ric_root") or root
        for y in range(max(y0, int(rc.get("first_year") or y0) - 1), y1 + 1):
            for m in range(1, 13):
                if not listed(root, y, m, variant):
                    continue
                lt, fn = dates(root, y, m)
                recs.append({"root": root, "delivery": "%d-%02d" % (y, m),
                             "ric": "%s%s%d^%d" % (rr, LD.MONTH_CODES[m - 1], y % 10, (y // 10) % 10),
                             "listed": True, "n_fields_ok": 0, "expiry": lt, "last_trade": lt, "first_notice": fn,
                             "last_trade_m1": _back(lt, 1, MARKET.get(root, "US")),
                             "first_delivery": None, "last_delivery": None,
                             "serial": LD.MONTH_CODES[m - 1] not in CYCLE[root]})
    df = pd.DataFrame(recs)
    for c in list(LD.CAL_ROLES) + ["last_trade_m1"]:
        df[c] = pd.to_datetime(df[c])
    return df


class RuleCalendar(LD.Calendar):
    """Calendar with serial months held only while they are among the nearest SERIAL_NEAR calendar months of the day
    (a serial contract is listed only a few months ahead)."""

    def __init__(self, roots, variant="base", near=None, cal=None):
        self.variant = variant
        self.near = near                       # overrides SERIAL_NEAR (number of nearest calendar months listed)
        super().__init__(rule_calendar(roots, variant) if cal is None else cal, roots)

    def _live(self, root, day):
        live, col = super()._live(root, day)
        if col is None or self.variant != "serial" or root not in SERIAL_NEAR or not len(live):
            return live, col
        p = pd.Period(pd.Timestamp(day), "M")
        dm = pd.PeriodIndex(live["delivery"], freq="M")
        ahead = (dm - p).map(lambda x: x.n)
        keep = (~live["serial"]) | (ahead < (self.near or SERIAL_NEAR[root]))
        return live[keep].reset_index(drop=True), col


# =====================================================================================================================
# 1.1.0: registered listing models (fitted by lseg_ident_v4 on 2026-11-25, design evidence; identity facts, not
# performance). Used ONLY for roots whose continuous positions are identified from the continuous series (no
# contract-level pull): NG, HO, GC, KC (agreement 99.5-100% at every observed depth). Each: cycle months listed while
# fewer than H calendar months ahead (999 = always), serial (non-cycle) months while fewer than `serial` months ahead;
# a contract is held through its expiry day; expiry = the observed TR.ExpiryDate of the contract where LSEG shows one
# (c1 / c2 series), else the exchange rule (dates()).
LISTING = {"NG": ("FGHJKMNQUVXZ", 999, 0), "HO": ("FGHJKMNQUVXZ", 999, 0), "GC": ("GJMQVZ", 24, 4),
           "KC": ("HKNUZ", 999, 0)}


def held_contract(root, n, day, observed=None):
    """Delivery (year, month) of continuous position n of root on trading day `day` under the registered listing model;
    observed = {(year, month): expiry date} from the TR.ExpiryDate series (optional). None if root has no model."""
    if root not in LISTING:
        return None
    cyc, H, serial = LISTING[root]
    observed = observed or {}
    if isinstance(day, dt.datetime):
        day = day.date()
    t = day.year * 12 + day.month - 1
    k_found = 0
    for k in range(t - 2, t + 12 * 8):
        y, m0 = divmod(k, 12)
        m = m0 + 1
        exp = observed.get((y, m)) or dates(root, y, m)[0]
        if exp < day:
            continue
        code = LD.MONTH_CODES[m0]
        ahead = k - t
        ok = (ahead < H) if code in cyc else (ahead < serial)
        if ok:
            k_found += 1
            if k_found == n:
                return (y, m)
    return None
