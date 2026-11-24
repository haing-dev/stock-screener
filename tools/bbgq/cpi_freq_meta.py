"""cpi_freq_meta: E3 metadata job (gm-1.2.3, gm/CHANGES.md 2026-11-24). METADATA ONLY, design rows only.

python3 tools/bbgq/cpi_freq_meta.py [research_dir]     (default: the repo cache, gm.panel.RD)

Lists, per country of the OECD CPI file the engine reads (oecd_cpi_yoy.csv), whether its series is monthly or
quarterly and its first date (rows dated after 2010-12 are not counted; a first date after 2010-12 is not shown), and
which countries the Economic trend / Value code asks for but the file does not hold (they fall back to FRED
CPALTT01<cc>M659N, whose spacing is listed the same way). No value is printed.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, REPO)

import pandas as pd  # noqa: E402

from gm import panel as P  # noqa: E402
from gm import signals as G  # noqa: E402

END = pd.Period("2010-12", "M")


def fred_meta(cc):
    p = None
    for d in (P.RD, P.RAW, P.MANUAL):
        q = os.path.join(d, "CPALTT01%sM659N.csv" % cc)
        if os.path.exists(q):
            p = q
            break
    if p is None:
        return "no file"
    x = pd.read_csv(p)
    d = pd.to_datetime(x["date"], errors="coerce").dt.to_period("M")
    ok = pd.to_numeric(x["value"], errors="coerce").notna() & d.notna() & (d <= END)
    dd = d[ok].sort_values()
    if not len(dd):
        return "file, no design rows"
    gaps = pd.Series([(b - a).n for a, b in zip(dd.iloc[:-1], dd.iloc[1:])])
    kind = "monthly" if len(gaps) and gaps.median() == 1 else ("quarterly" if len(gaps) and gaps.median() == 3 else
                                                               "other")
    return "%s (median spacing %s months), first %s, design rows %d" % (
        kind, int(gaps.median()) if len(gaps) else "-", dd.iloc[0], len(dd))


def main():
    if len(sys.argv) > 1:
        P.RD = sys.argv[1]
    fname = "oecd_cpi_yoy.csv"
    rows = G.sdmx_meta(fname)
    print("E3 CPI metadata (design rows only, <= 2010-12): %s" % fname)
    print("%-8s %-10s %-12s %-32s %s" % ("country", "frequency", "FREQ column", "first (design)", "design rows"))
    for r in rows:
        print("%-8s %-10s %-12s %-32s %d" % (r["country"], r["frequency"], r["FREQ column"], r["first"],
                                            r["design rows"]))
    n_q = sum(1 for r in rows if r["frequency"] in ("quarterly", "both"))
    print("countries with quarterly rows: %d of %d" % (n_q, len(rows)))
    have = {r["country"] for r in rows if r["design rows"] > 0}
    used = sorted({G.FX_MACRO.get(c, c) for c in list(G.EQ_CC.values()) + [v[0] for v in G.BD.values()] +
                   [v[1] for v in G.FX_CC.values()] + G.GLOBAL})
    print("CPI countries the engine asks for (Economic trend, Value): %s" % ", ".join(used))
    first = {r["country"]: r["first"] for r in rows}
    print("(the engine splices: OECD file first, FRED CPALTT01<cc>M659N fills the months the OECD file lacks)")
    for c in used:
        iso = G.ISO3.get(c, c)
        oecd = ("OECD monthly from %s" % first[iso]) if iso in have else "OECD none"
        print("  %-3s %-4s %-28s | FRED: %s" % (c, iso, oecd, fred_meta(c)))
    print("=== END ===")


if __name__ == "__main__":
    main()
