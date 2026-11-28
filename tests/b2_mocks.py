"""Mock inputs for tests/b2_batch_smoke.py (INVENTED data only: synthetic panel, card inputs, Eurodollar and Euribor
settlements, LSEG monthly series; no LSEG, Bloomberg or FRED value). Built on tests/diag_preb_smoke.py's mocks."""
import os
import sys

import numpy as np
import pandas as pd

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [REPO, os.path.join(REPO, "tools", "bbgq", "lib"), os.path.join(REPO, "tools", "lseg"), HERE]

import diag_preb_smoke as PS  # noqa: E402
import lseg_rules as LR  # noqa: E402

P = lambda s: pd.Period(s, "M")  # noqa: E731
MC = "FGHJKMNQUVXZ"


def fei_contracts(seed=4, bend=3.0, slope=0.06, late=False, gap=None):
    """Quarterly Euribor contracts 1999-2012, daily on weekdays from 1998-12-08 (about 2.6 years before expiry); rate =
    level + slope x years to expiry + a per (contract, month) bend. gap = (a, b): every contract unpriced in [a, b]."""
    days = pd.bdate_range("1998-12-08", "2012-12-31" if late else "2010-12-31")
    lvl = pd.Series(3 + 1.5 * np.sin(np.arange(len(days)) / 700.0), index=days)
    out = {}
    for y in range(1999, 2013):
        for m in (3, 6, 9, 12):
            ltd = pd.Timestamp(LR.dates("FEI", y, m)[0])
            d = days[(days >= ltd - pd.Timedelta(days=950)) & (days <= ltd)]
            if not len(d):
                continue
            tau = (ltd - d).days / 365.0
            r = lvl.reindex(d).to_numpy() + slope * tau
            months = (d - pd.Timedelta(days=7)).to_period("M")
            u = {p: np.random.default_rng([seed, y, m, int(p.ordinal) + 2000]).normal(0, 1) for p in months.unique()}
            r = r + bend * np.array([u[p] for p in months])
            s = pd.Series(100 - r, index=d)
            if late:
                s[s.index > pd.Timestamp("2010-12-31")] = 1.23456789
            if gap is not None:
                s = s[(s.index < pd.Timestamp(gap[0])) | (s.index > pd.Timestamp(gap[1]))]
            out[(y, m)] = s
    return out


def code(root, k):
    return "<%s%s%d^%d>" % (root, MC[k[1] - 1], k[0] % 10, (k[0] // 10) % 10)


class View:
    """Mock of diag_preb.LsegView: catalog rows, daily(sid), monthly(sid)."""

    def __init__(self, ed, fei, monthly, extra_rows=()):
        rows, self.d = [], {}
        for root, cons in (("ED", ed), ("FEI", fei)):
            for k, s in cons.items():
                sid = "DS:%s|X" % code(root, k)
                rows.append({"per": "D", "status": "ok", "duplicate_of": "", "series_id": sid, "code": code(root, k)})
                self.d[sid] = s
        for r in extra_rows:
            rows.append(r)
        self.cat = pd.DataFrame(rows)
        self.m = monthly

    def daily(self, sid):
        return self.d[sid]

    def monthly(self, sid):
        return self.m[sid]

    def ed_contracts(self):
        c = self.cat
        return {PS.PB.ed_delivery(r.code): r.series_id for r in c.itertuples()
                if PS.PB.ed_delivery(r.code) is not None}


def inputs(late=False, seed=11, fei_gap=None):
    """-> dict R, D, S, gspc, fxv, rates, ci, view, ed, fei, lm (all invented)."""
    R, D, S, gspc = PS.panel(seed=seed, late=late)
    ci, _files = PS.synth_ci(late=late)
    ed = PS.ed_contracts(bend=4.0, late=late)
    fei = fei_contracts(late=late, gap=fei_gap)
    lm = PS.lseg_monthly(late=late)
    fxv = PS.fx_values(R)
    rates = PS.rates_of(R)
    return {"R": R, "D": D, "S": S, "gspc": gspc, "fxv": fxv, "rates": rates, "ci": ci,
            "view": View(ed, fei, lm), "ed": ed, "fei": fei, "lm": lm}
