"""eq_reader (runs on WRDS Cloud and on the PC): the one way equity jobs read WRDS tables and stored data sets.

The seal (plan v0.3 section 8.2, docs/research/equity/SEAL_LOG.md): US months from 2011-01 to the seal end and
non-US months from 1990-01 to the seal end are sealed until the freeze. Every table and stored data set an equity job
may read is declared below with its date column and region; the caller cannot choose either. A read whose month range
touches a sealed month is refused, unless the keyword exempt=True is passed; tools/equity/seal_check.py lets no job
pass that flag except the registered seal-exempt jobs, and refuses any equity job that reads another way.
count() returns row counts by year only and may run on sealed months (structure checks, plan 8.2).

    import eq_reader
    df = eq_reader.read(sql, "crsp.msf_v2", ["permno", "mthcaldt", "mthret"], "1990-01", "2010-12",
                        where="securitytype = 'EQTY'")
    df = eq_reader.load_ds(load, "eq_sc_msf_2009", "2009-06", "2009-12")
    n = eq_reader.count(sql, "tfn.s34", "2010-01", "2025-12", per=["mgrno", "rdate"],
                        keep="sum(case when fdate = rdate then 1 else 0 end) = 0")
"""
import re
import types

SEAL_END = 202512                      # last CRSP stock month (WRDS table check 2026-11-17)
SEAL_START = types.MappingProxyType({"us": 201101, "nonus": 199001})

# table -> (date column, region). Region "all" = the table holds US and non-US rows: both seals apply.
TABLES = types.MappingProxyType({
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
})

# stored data set (exact name, or prefix ending in '_' followed by a year) -> (date column, region)
DATASETS = types.MappingProxyType({
    "eq_sc_msf_": ("yyyymm", "us"),
    "eq_sc_fret_": ("caldt", "us"),
    "eq_sc_hold_": ("rdate", "us"),
    "eq_sc_agg_": ("rdate", "us"),
    "eq_sc_bm": ("public_date", "us"),
    "eq_sc_ff": ("date", "us"),
})

_IDENT = re.compile(r"^[a-z_][a-z0-9_]*$")
_BAD_SQL = re.compile(r";|--|/\*|\*/|\b(select|from|join|union|with|into|insert|update|delete|drop|alter|"
                      r"create|grant|copy|pg_\w+|lateral|over|window)\b", re.I)


class SealError(Exception):
    pass


def _ym(x):
    """'1990-01', '1990-01-31', 199001 -> 199001."""
    s = re.sub(r"[^0-9]", "", str(x))
    if len(s) < 6:
        raise SealError("bad month %r" % (x,))
    y, m = int(s[:4]), int(s[4:6])
    if not 1 <= m <= 12 or not 1900 <= y <= 2100:
        raise SealError("bad month %r" % (x,))
    return y * 100 + m


def _sealed(region, lo, hi):
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


def _clause(text):
    if text and (_BAD_SQL.search(text) or text.count("(") != text.count(")") or text.count("'") % 2):
        raise SealError("clause refused: plain conditions only")
    return text


def read(sql, table, cols, lo, hi, where=None, *, exempt=False):
    """Rows of a declared table with its date column in the months lo..hi (inclusive)."""
    if table not in TABLES:
        raise SealError("table %s is not declared in eq_reader.TABLES" % table)
    dcol, region = TABLES[table]
    lo_, hi_, d0, d1 = _range(lo, hi)
    if _sealed(region, lo_, hi_) and exempt is not True:
        raise SealError("%s %d..%d touches sealed months (%s)" % (table, lo_, hi_, region))
    cols = list(cols)
    if not cols or any(not isinstance(c, str) or not _IDENT.match(c) for c in cols):
        raise SealError("columns must be plain lower-case names")
    if dcol not in cols:
        cols.append(dcol)
    q = "select %s from %s where %s >= '%s' and %s < '%s'" % (", ".join(cols), table, dcol, d0, dcol, d1)
    if where:
        q += " and (%s)" % _clause(where)
    df = sql(q)
    _check_dates(df[dcol] if dcol in df.columns else None, lo_, hi_)
    return df


def count(sql, table, lo, hi, where=None, per=None, keep=None):
    """Row counts by year of the declared date column (allowed on sealed months). per: count groups of these
    columns instead of rows (a group falls in the year of its date column, which is then part of the group);
    keep: a condition on aggregates that a group must meet. Returns only (year, n)."""
    if table not in TABLES:
        raise SealError("table %s is not declared in eq_reader.TABLES" % table)
    dcol, _ = TABLES[table]
    _, _, d0, d1 = _range(lo, hi)
    per = list(per or [])
    if any(not isinstance(c, str) or not _IDENT.match(c) for c in per):
        raise SealError("per must be plain lower-case names")
    rng = "%s >= '%s' and %s < '%s'" % (dcol, d0, dcol, d1)
    if where:
        rng += " and (%s)" % _clause(where)
    if per:
        g = ", ".join(dict.fromkeys(per + [dcol]))
        inner = "select %s from %s where %s group by %s" % (g, table, rng, g)
        if keep:
            inner += " having %s" % _clause(keep)
        q = "select extract(year from t.%s)::int as year, count(*) as n from (%s) t group by 1 order by 1" % (dcol,
                                                                                                         inner)
    else:
        if keep:
            raise SealError("keep needs per")
        q = "select extract(year from %s)::int as year, count(*) as n from %s where %s group by 1 order by 1" % (
            dcol, table, rng)
    df = sql(q)
    if list(df.columns) != ["year", "n"]:
        raise SealError("count returned other columns")
    return df


def _dataset(name):
    if name in DATASETS:
        return DATASETS[name]
    for k, v in DATASETS.items():
        if k.endswith("_") and name.startswith(k) and re.match(r"^\d{4}$", name[len(k):]):
            return v
    raise SealError("data set %s is not declared in eq_reader.DATASETS" % name)


def load_ds(load, name, lo, hi, *, exempt=False):
    """A stored data set, kept to the months lo..hi of its declared date column."""
    dcol, region = _dataset(name)
    lo_, hi_, _, _ = _range(lo, hi)
    if _sealed(region, lo_, hi_) and exempt is not True:
        raise SealError("data set %s %d..%d touches sealed months (%s)" % (name, lo_, hi_, region))
    df = load(name)
    if dcol not in df.columns:
        raise SealError("data set %s has no column %s" % (name, dcol))
    ym = _ym_col(df[dcol])
    return df[(ym >= lo_) & (ym <= hi_)].reset_index(drop=True)


def _ym_col(s):
    """Month of every row; refuses a column that is not a date (or yyyymm integer) in every row."""
    import pandas as pd
    if pd.api.types.is_integer_dtype(s):
        v = s.astype("int64")
        if len(v) and (v.min() < 190001 or v.max() > 210012 or not ((v % 100 >= 1) & (v % 100 <= 12)).all()):
            raise SealError("date column is not yyyymm")
        return v
    if pd.api.types.is_float_dtype(s) or pd.api.types.is_bool_dtype(s):
        raise SealError("date column is not a date")
    d = pd.to_datetime(s, errors="coerce")
    if d.isna().any():
        raise SealError("date column has values that are not dates")
    ym = d.dt.year * 100 + d.dt.month
    if len(ym) and (ym.min() < 190001 or ym.max() > 210012):
        raise SealError("date column out of range")
    return ym.astype("int64")


def _check_dates(col, lo, hi):
    if col is not None and len(col):
        ym = _ym_col(col)
        if int(ym.min()) < lo or int(ym.max()) > hi:
            raise SealError("rows outside the requested months came back")
