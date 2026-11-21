"""eq_univ (runs on WRDS Cloud): completeness check of the LSEG company list (plan v0.4 step 3a;
docs/research/equity/LSEG_universe_v1_2026-11-20.md). Seal-exempt descriptive job (tools/equity/seal_exempt.json,
SEAL_LOG.md): reads CRSP listing levels only (names, December prices and shares), never a return.

Input (frozen block): CAND = 8-digit CUSIPs of US common shares found in LSEG (Datastream dead and research lists = "D",
Workspace screens = "W"). Output: counts and shares per year (all CRSP common shares on NYSE / NYSE American / Nasdaq;
the 1,500 largest; the 1,500 largest priced at $5 or more; companies leaving CRSP in each year), plus the names of at
most 10 of the largest companies NOT found, for three dates (no values).

Job name: eq_univ_check_v<n>: check(sql, out)
"""
import json

import numpy as np
import pandas as pd

# >>> FROZEN INPUT
CAND = json.loads("{}")  # full input (43,678 CUSIPs from LSEG) only on the PC / WRDS; input sha256 6eddb7ede083145f20f78ac9bf74bf6fb3f953eb3fe2d12d513f31e26395807a
# <<< FROZEN INPUT


def check(sql, out):
    cols = list(sql("select * from crsp.stocknames_v2 limit 1").columns)
    namecol = next((c for c in ("comnam", "issuernm", "securitynm") if c in cols), None)
    nm = sql("select permno, cusip%s from crsp.stocknames_v2 where cusip is not null"
             % ((", " + namecol) if namecol else ""))
    nm["cusip"] = nm.cusip.astype(str).str[:8]
    nm["src"] = nm.cusip.map(CAND)
    srcp = nm.dropna(subset=["src"]).groupby("permno").src.apply(lambda s: "".join(sorted(set("".join(s)))))
    names = nm.groupby("permno")[namecol].last() if namecol else None
    com = ("securitytype = 'EQTY' and securitysubtype = 'COM' and sharetype = 'NS' and primaryexch in ('N','A','Q')")
    dec = sql("select permno, yyyymm, abs(mthprc)::float8 as px, shrout::float8 as sh from crsp.msf_v2 "
              "where mod(yyyymm, 100) = 12 and yyyymm between 200912 and 202512 and " + com)
    life = sql("select permno, min(yyyymm) as first, max(yyyymm) as last from crsp.msf_v2 "
               "where yyyymm between 201001 and 202512 and " + com + " group by permno")
    dec["mv"] = dec.px * dec.sh
    dec["src"] = dec.permno.map(srcp).fillna("")
    out("CRSP common shares (NYSE / American / Nasdaq), December of each year; found = any CUSIP the company ever had "
        "is in the LSEG list (D Datastream lists, W Workspace screens)")
    out("year-end | all: n, found % (D only %, W only %) | 1,500 largest: found % | 1,500 largest priced >= $5: found %")
    tot = {}
    for ym, g in dec.groupby("yyyymm"):
        g = g.sort_values("mv", ascending=False)
        f = g.src != ""
        t = g.head(1500)
        t5 = g[g.px >= 5].head(1500)
        tot[ym] = g
        out("%d | %d, %.1f (%.1f, %.1f) | %.1f | %.1f" % (ym // 100, len(g), 100 * f.mean(),
            100 * (g.src == "D").mean(), 100 * (g.src == "W").mean(), 100 * (t.src != "").mean(),
            100 * (t5.src != "").mean()))
    life["src"] = life.permno.map(srcp).fillna("")
    gone = life[life["last"] < 202512].copy()
    gone["y"] = gone["last"] // 100
    out("companies leaving CRSP common shares each year: n, found %")
    for y, g in gone.groupby("y"):
        out("%d | %d, %.1f" % (y, len(g), 100 * (g.src != "").mean()))
    if names is not None:
        for ym in (200912, 201712, 202412):
            g = tot.get(ym)
            if g is None:
                continue
            miss = g[g.src == ""].head(10)
            out("largest NOT found at %d (size rank among all): %s" % (ym // 100, "; ".join(
                "%s (#%d)" % (str(names.get(p, "?"))[:28], int(np.where(g.permno.values == p)[0][0]) + 1)
                for p in miss.permno)))
        big = dec.groupby("permno").mv.max()
        g2 = gone[gone.src == ""].copy()
        g2["mv"] = g2.permno.map(big)
        g2 = g2.sort_values("mv", ascending=False).head(10)
        out("largest NOT found among companies that left: %s" % "; ".join(
            "%s (%d)" % (str(names.get(p, "?"))[:28], y) for p, y in zip(g2.permno, g2.y)))
    out("ALL DONE")
