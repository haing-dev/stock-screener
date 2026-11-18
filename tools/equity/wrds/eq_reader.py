"""eq_reader (runs on WRDS Cloud and on the PC): the one way equity jobs read WRDS tables and stored data sets.

The seal (plan v0.3 section 8.2, docs/research/equity/SEAL_LOG.md): US months from 2011-01 to the seal end and
non-US months from 1990-01 to the seal end are sealed until the freeze. Every table an equity job may read is
declared below with its date column and region. A read whose month range touches a sealed month is refused, unless
the caller passes exempt=True; tools/equity/seal_check.py lets only the registered seal-exempt jobs
(tools/equity/seal_exempt.json) pass that flag, and refuses any equity job that reads a table another way.

    import eq_reader
    df = eq_reader.read(sql, "crsp.msf_v2", ["permno", "mthcaldt", "mthret"], "1990-01", "2010-12",
                        where="securitytype = 'EQTY'")
    df = eq_reader.load_ds(load, "my_set", "mthcaldt", "us", "1990-01", "2010-12")
"""
import re

SEAL_END = 202512                      # last CRSP stock month (WRDS table check 2026-11-17)
SEAL_START = {"us": 201101, "nonus": 199001}

# table -> (date column, region). Region "all" = the table holds US and non-US rows: both seals apply.
TABLES = {
    "crsp.msf_v2": ("mthcaldt", "us"),
    "crsp.dsf_v2": ("dlycaldt", "us"),
    "crsp.stkdelists": ("delistingdt", "us"),
    "crsp.monthly_tna_ret_nav": ("caldt", "us"),
    "crsp.holdings": ("report_dt", "us"),
    "comp.funda": ("datadate", "us"),
    "comp.fundq": ("datadate", "us"),
    "comp.sec_shortint": ("datadate", "us"),
    "comp.g_funda": ("datadate", "nonus"),
    "comp.g_fundq": ("datadate", "nonus"),
    "comp.g_secd": ("datadate", "nonus"),
    "tfn.s34": ("rdate", "us"),
    "tfn.s12": ("rdate", "us"),
    "ibes.statsum_epsus": ("statpers", "us"),
    "ibes.statsum_epsint": ("statpers", "nonus"),
    "wrdsapps_finratio.firm_ratio": ("public_date", "us"),
    "ff.fivefactors_monthly": ("date", "us"),
    "ff.factors_monthly": ("date", "us"),
    "contrib_global_factor.global_factor": ("eom", "all"),
}

_IDENT = re.compile(r"^[a-z_][a-z0-9_]*$")
_BAD_WHERE = re.compile(r";|--|/\*|\*/|\b(select|from|join|union|with|into|insert|update|delete|drop|alter|"
                        r"create|grant|copy|pg_\w+|lateral)\b", re.I)


class SealError(Exception):
    pass


def _ym(x):
    """'1990-01', '1990-01-31', 199001 -> 199001."""
    s = re.sub(r"[^0-9]", "", str(x))
    if len(s) < 6:
        raise SealError("bad month %r" % (x,))
    y, m = int(s[:4]), int(s[4:6])
    if not 1 <= m <= 12:
        raise SealError("bad month %r" % (x,))
    return y * 100 + m


def sealed(region, lo, hi):
    """True if the month range lo..hi touches a sealed month of the region."""
    lo, hi = _ym(lo), _ym(hi)
    regions = ("us", "nonus") if region == "all" else (region,)
    for r in regions:
        if r not in SEAL_START:
            raise SealError("unknown region %r" % (r,))
        if lo <= SEAL_END and hi >= SEAL_START[r]:
            return True
    return False


def _range(lo, hi):
    lo, hi = _ym(lo), _ym(hi)
    if lo > hi:
        raise SealError("empty month range")
    d0 = "%04d-%02d-01" % (lo // 100, lo % 100)
    y, m = (hi // 100, hi % 100 + 1) if hi % 100 < 12 else (hi // 100 + 1, 1)
    return lo, hi, d0, "%04d-%02d-01" % (y, m)


def read(sql, table, cols, lo, hi, where=None, exempt=False):
    """Rows of a declared table with its date column in the months lo..hi (inclusive)."""
    if table not in TABLES:
        raise SealError("table %s is not declared in eq_reader.TABLES" % table)
    dcol, region = TABLES[table]
    lo_, hi_, d0, d1 = _range(lo, hi)
    if sealed(region, lo_, hi_) and not exempt:
        raise SealError("%s %d..%d touches sealed months (%s)" % (table, lo_, hi_, region))
    cols = list(cols)
    if not cols or any(not _IDENT.match(c) for c in cols):
        raise SealError("columns must be plain lower-case names")
    if dcol not in cols:
        cols.append(dcol)
    q = "select %s from %s where %s >= '%s' and %s < '%s'" % (", ".join(cols), table, dcol, d0, dcol, d1)
    if where:
        if _BAD_WHERE.search(where) or where.count("(") != where.count(")"):
            raise SealError("where clause refused: plain conditions only")
        q += " and (%s)" % where
    df = sql(q)
    _check_dates(df, dcol, lo_, hi_)
    return df


def load_ds(load, name, date_col, region, lo, hi, exempt=False):
    """A stored data set, kept to the months lo..hi of its declared date column."""
    lo_, hi_, _, _ = _range(lo, hi)
    if sealed(region, lo_, hi_) and not exempt:
        raise SealError("data set %s %d..%d touches sealed months (%s)" % (name, lo_, hi_, region))
    df = load(name)
    if date_col not in df.columns:
        raise SealError("data set %s has no column %s" % (name, date_col))
    ym = _ym_col(df[date_col])
    return df[(ym >= lo_) & (ym <= hi_)].reset_index(drop=True)


def _ym_col(s):
    import pandas as pd
    if pd.api.types.is_integer_dtype(s) and len(s) and s.max() < 1000000:
        return s.astype("int64")
    d = pd.to_datetime(s, errors="coerce")
    return (d.dt.year * 100 + d.dt.month).fillna(0).astype("int64")


def _check_dates(df, dcol, lo, hi):
    if dcol in df.columns and len(df):
        ym = _ym_col(df[dcol])
        if int(ym.min()) < lo or int(ym.max()) > hi:
            raise SealError("rows outside the requested months came back")
