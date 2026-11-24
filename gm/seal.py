"""E5 (gm-1.2.3, registered 2026-11-24): seal and holding cut of TESTING_PROTOCOL 7.3 item 5.

Every holding period of every pod, tranche, rule and diagnostic ends at the close of 2010-12-31 at the latest. No price,
settlement or statistic dated after 2010-12-31 is read, printed or used before the holdout.

A DESIGN run is every run except the live paper run (gm/run.py) and the one-shot holdout run (gm/holdout.py), which
pass seal=None explicitly. In a design run:
  cut_inputs     drops every input row dated after the seal (monthly panel and signals: months after 2010-12; daily
                 returns: days after 2010-12-31), so nothing later can be used and no holding can earn past the seal
                 (under k = 0 the last return month is 2010-12, earned by the holding decided at month-end 2010-11; the
                 decision at month-end 2010-12 earns nothing in a design run);
  check_output   the guard: raises SealBreach if any design output carries a date after the seal (a new path that
                 shifts dates forward, e.g. k = 1 or tranches, fails here instead of leaking);
  last_day       the last daily index position at or before the seal close (delay / daily paths cap a holding there).
The engine runner (tools/bbgq/lib/gm_engine.py) also cuts every loader at the seal (inputs dated later never reach the
rules). tests/gm_seal_smoke.py fails if a design output has a date after 2010-12 or changes when inputs dated later
change.
"""
import numpy as np
import pandas as pd

DESIGN = "design"          # sentinel: the registered seal of gm/config.py (SEAL_END)


class SealBreach(RuntimeError):
    """A design output holds a date after the seal."""


def resolve(seal):
    """'design' -> config.SEAL_END; None -> None (live / holdout); a date -> that date. Returns a Timestamp or None."""
    if seal is None:
        return None
    if isinstance(seal, str) and seal == DESIGN:
        from .config import SEAL_END
        seal = SEAL_END
    return pd.Timestamp(seal).normalize()


def _cut(x, T):
    if x is None:
        return None
    if isinstance(x, dict):
        return {k: _cut(v, T) for k, v in x.items()}
    if not hasattr(x, "index"):
        return x
    idx = x.index
    if isinstance(idx, pd.PeriodIndex):
        return x.loc[idx <= pd.Period(T, "M")]
    if isinstance(idx, pd.DatetimeIndex):
        return x.loc[idx <= T + pd.Timedelta(hours=23, minutes=59, seconds=59)]
    return x


def cut_inputs(T, *xs):
    """Each input (frame, series, dict of them, or None) without the rows dated after the seal T."""
    out = tuple(_cut(x, T) for x in xs)
    return out if len(out) > 1 else out[0]


def _late(x, T):
    """Dates after T that carry at least one value (a missing-only row is not a breach)."""
    idx = x.index
    if isinstance(idx, pd.PeriodIndex):
        late = idx > pd.Period(T, "M")
    elif isinstance(idx, pd.DatetimeIndex):
        late = idx > T + pd.Timedelta(hours=23, minutes=59, seconds=59)
    else:
        return []
    if not late.any():
        return []
    y = x.loc[late]
    has = y.notna().any(axis=1) if isinstance(y, pd.DataFrame) else y.notna()
    return [str(d) for d in y.index[np.asarray(has)]]


def check_output(obj, seal=DESIGN, where="design output"):
    """Guard: raise SealBreach if any frame or series inside obj (dicts walked, also dict keys that are periods or
    dates) has a value dated after the seal."""
    T = resolve(seal)
    if T is None:
        return obj
    bad = []

    def walk(x, path):
        if isinstance(x, dict):
            for k, v in x.items():
                if isinstance(k, (pd.Period, pd.Timestamp)) and (
                        (isinstance(k, pd.Period) and k > pd.Period(T, "M")) or
                        (isinstance(k, pd.Timestamp) and k > T + pd.Timedelta(hours=23, minutes=59, seconds=59))):
                    bad.append("%s[%s]" % (path, k))
                walk(v, "%s.%s" % (path, k))
        elif isinstance(x, (pd.Series, pd.DataFrame)):
            late = _late(x, T)
            if late:
                bad.append("%s: %s" % (path, late[0]))
    walk(obj, where)
    if bad:
        raise SealBreach("seal %s breached: %s" % (T.date(), "; ".join(bad[:5])))
    return obj


def last_day(days, T):
    """Position of the last day in a sorted DatetimeIndex at or before the seal close T (-1 if none)."""
    return int(np.searchsorted(days.values, np.datetime64(T + pd.Timedelta(hours=23, minutes=59, seconds=59)),
                               side="right")) - 1
