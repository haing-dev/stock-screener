"""One-shot holdout run (2011-01 .. last complete month) for a FROZEN rule version.

python -m gm.holdout --confirm <VERSION>
Refuses to run unless <VERSION> equals gm.run.VERSION and docs/research/global_macro/holdout_<VERSION>.md does not
exist yet. Writes that file (append-only record of the one run). Pass criteria (plan section 7): net SR >= 0.5,
worst fall no deeper than -20%, correlation with the S&P 500 <= 0.3, no loss in 2022 (2008 and 2020: 2008 is in the
design period; 2020 is in the holdout).
"""
import os
import pickle
import sys

import numpy as np
import pandas as pd

from . import book as B
from . import panel as P
from .run import VERSION

DOC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "research", "global_macro")


def main():
    if len(sys.argv) < 3 or sys.argv[1] != "--confirm" or sys.argv[2] != VERSION:
        sys.exit("usage: python -m gm.holdout --confirm %s   (runs the holdout once for the frozen version)" % VERSION)
    out = os.path.join(DOC, "holdout_%s.md" % VERSION)
    if os.path.exists(out):
        sys.exit("holdout already run for %s: %s" % (VERSION, out))
    R = pickle.load(open(os.path.join(P.OUT, "panel.pkl"), "rb"))["R"]
    res, x2 = B.run(R), B.run(R, cost_mult=2.0)
    end = pd.Period(pd.Timestamp.today(), "M") - 1
    spx = R["eq_us_spx"]
    a, b = "2011-01", str(end)
    n = res["net"].loc[a:b].dropna()
    cum = (1 + n).cumprod()
    dd = (cum / cum.cummax() - 1).min()
    yr = (1 + n).groupby(n.index.year).prod() - 1
    sr = n.mean() / n.std() * np.sqrt(12)
    corr = n.corr(spx.reindex(n.index))
    checks = {"net SR >= 0.5": sr >= 0.5, "worst fall > -20%": dd > -0.20, "corr S&P <= 0.3": corr <= 0.3,
              "2020 >= 0": yr.get(2020, 0) >= 0, "2022 >= 0": yr.get(2022, 0) >= 0}
    L = ["# Holdout run, %s (%s..%s), run once on %s" % (VERSION, a, b, pd.Timestamp.utcnow().strftime("%Y-%m-%d %H:%M UTC")),
         "", "```",
         "gross      " + B.stats(res["gross"].loc[a:b], spx),
         "net        " + B.stats(res["net"].loc[a:b], spx),
         "net 2xcost " + B.stats(x2["net"].loc[a:b]),
         "```", "", "Calendar-year net returns: " + ", ".join("%d %+.1f%%" % (y, v * 100) for y, v in yr.items()),
         "", "| Pass criterion | Result |", "|---|---|"] + ["| %s | %s |" % (k, "PASS" if v else "FAIL")
                                                          for k, v in checks.items()]
    L += ["", "Verdict: %s" % ("GO (all criteria pass)" if all(checks.values()) else "NO-GO on the criteria marked FAIL")]
    os.makedirs(DOC, exist_ok=True)
    open(out, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
