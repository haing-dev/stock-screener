"""X1 diagnostic (TESTING_PROTOCOL 7.5 row X1, order of running item 1; SPEC_Carry s3, s13; THESIS_1.3_xs s5).

Question: is energy carry a calendar pattern? SIGNALS ONLY: no return, no Sharpe, nothing dated after 2010-12.

Signal: the Carry pod's input signal for each energy market, i.e. gm.signals.carry_values for cm_wti, cm_natgas,
cm_heatoil, cm_gasoline = 12 x (F1 / F2 - 1) from the EIA NYMEX contracts 1 and 2 at month end (both Carry versions read
it: v1 its sign, v2 its rank in class). Window: design month-ends 1975-01 .. 2010-12, from the first month the signal
exists. Every loader is cut at 2010-12-31 (gm_engine.Cut), so no observation dated later reaches the computation.

Statistic (registered gate "calendar-month means explain >= 0.25 of a market's carry-signal variance"; closed here,
gm/CHANGES.md "X1 outcome"): share = 1 - SS_within / SS_total, SS_total = sum over the window's months of (c - mean c)^2,
SS_within = sum of (c - mean of c in its calendar month)^2 (the plain, unadjusted share of the twelve calendar-month
means; it equals the R^2 of a regression on 12 month dummies). Gate opens at share >= 0.25 (X1_GATE), computed only
when every calendar month has at least X1_MIN_OBS = 5 observations (else 'insufficient', gate closed).

Output (signals metadata only): first and last signal month, months, smallest calendar-month count, share, open/closed.
python3 -m gm.diag_x1 [OUT.txt]
"""
import datetime as dt
import io
import os
import sys
import contextlib

import numpy as np
import pandas as pd

X1_GATE = 0.25
X1_MIN_OBS = 5
WINDOW = ("1975-01", "2010-12")
ENERGY = ("cm_wti", "cm_natgas", "cm_heatoil", "cm_gasoline")
VERSION = "diag_x1-1.0.0"


def calendar_share(c, min_obs=X1_MIN_OBS):
    """c: monthly signal (PeriodIndex). -> dict(n, min_count, share or None). Share of variance explained by the twelve
    calendar-month means (1 - within / total); None when a calendar month has fewer than min_obs values."""
    c = c.dropna()
    n = int(len(c))
    if n == 0:
        return {"n": 0, "min_count": 0, "share": None}
    m = c.index.month
    cnt = c.groupby(m).count().reindex(range(1, 13), fill_value=0)
    out = {"n": n, "min_count": int(cnt.min())}
    if out["min_count"] < min_obs:
        out["share"] = None
        return out
    tot = float(((c - c.mean()) ** 2).sum())
    within = float(((c - c.groupby(m).transform("mean")) ** 2).sum())
    out["share"] = (1.0 - within / tot) if tot > 0 else 0.0
    return out


def energy_carry(M=None):
    """The engine's energy carry signals on design months only (loaders cut at the seal)."""
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(os.path.dirname(here), "tools", "bbgq", "lib"))
    import gm_engine as GE
    from . import config as CF
    M = M or GE.setup()
    G, P = M["G"], M["P"]
    with GE.Cut(M, CF.SEAL_END), contextlib.redirect_stdout(io.StringIO()):
        C = G.carry_values(pd.DataFrame(index=P.GRID))     # no market columns: the Bloomberg curve part is skipped
        direct = {k: P.eia_rolled(root)[1] for k, root in P.EIA_ROOT.items()}
    a, b = pd.Period(WINDOW[0], "M"), pd.Period(WINDOW[1], "M")
    out = {}
    for k in ENERGY:
        s = C[k]
        d = direct[k].reindex(s.index)
        if not np.allclose(s.fillna(0).values, d.fillna(0).values) or (s.isna() != d.isna()).any():
            raise RuntimeError("carry_values and eia_rolled disagree for %s" % k)
        s = s.loc[(s.index >= a) & (s.index <= b)]
        if len(s) and s.notna().any():
            s = s.loc[s.first_valid_index():]
        out[k] = s
    late = [k for k, s in out.items() if len(s) and s.index.max() > b]
    if late:
        raise RuntimeError("X1 read a month after 2010-12: %s" % late)
    return out


def run(out=print):
    sig = energy_carry()
    out("=== X1 diagnostic (%s, %s UTC) ===" % (VERSION, dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M")))
    out("Question: is energy carry a calendar pattern? (TESTING_PROTOCOL 7.5 X1; SPEC_Carry s3, s13). SIGNALS ONLY.")
    out("Signal: gm.signals.carry_values energy = 12 x (F1 / F2 - 1), EIA NYMEX contracts 1-2, month end (input of both "
        "Carry versions). Window: month-ends %s..%s from the first signal month; loaders cut at 2010-12-31." % WINDOW)
    out("Statistic: share of signal variance explained by the 12 calendar-month means (1 - SS_within / SS_total). "
        "Gate: share >= %.2f, every calendar month >= %d observations." % (X1_GATE, X1_MIN_OBS))
    out("market | first | last | months | smallest calendar-month count | share | gate")
    res = {}
    for k, s in sig.items():
        r = calendar_share(s)
        first = str(s.first_valid_index()) if r["n"] else "-"
        last = str(s.last_valid_index()) if r["n"] else "-"
        if r["share"] is None:
            gate = "CLOSED (insufficient: a calendar month has < %d observations)" % X1_MIN_OBS
            sh = "-"
        else:
            gate = "OPEN" if r["share"] >= X1_GATE else "CLOSED"
            sh = "%.3f" % r["share"]
        out("%s | %s | %s | %d | %d | %s | %s" % (k, first, last, r["n"], r["min_count"], sh, gate))
        res[k] = dict(r, first=first, last=last, open=gate == "OPEN")
    opened = [k for k, r in res.items() if r["open"]]
    out("X1 OUTCOME | gate open for: %s | closed for: %s" % (", ".join(opened) or "none",
                                                            ", ".join(k for k in res if k not in opened) or "none"))
    out("Nothing else computed: no return, no Sharpe, no month after 2010-12.")
    return res


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else None
    lines = []

    def emit(s):
        print(s)
        lines.append(s)
    run(emit)
    if path:
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
