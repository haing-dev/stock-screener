"""eq_conv (runs on WRDS Cloud): conviction holdings of the roster and control investors (plan v0.4 section 6;
V04_REGISTRATION.md R2 and addendum A4). Seal-exempt descriptive job (tools/equity/seal_exempt.json, SEAL_LOG.md):
reads 13F holdings (tfn.s34 first versions), CRSP names and quarter-end prices / share factors (levels; no returns).

Per investor and quarter-end 2009-12 .. 2025-12: weight of each holding (value at the CRSP quarter-end price over the
value of all holdings matched to a CRSP common share), weight rank, new position, addition (split-adjusted shares up
>= 20%), reduction, exit, quarters held; conviction purchase version a (new or addition that ends among the five
largest weights) and version b (new or addition whose bought value, change in shares x quarter-end price, is >= 1% of
the portfolio). The panel stays on WRDS (data set eq_conv_panel). The report prints counts per investor only (no
stock, no weight), plus 13F manager names found by name search for investors without a fixed id (for the next
version's input; they are NOT used in this run).

Job names: eq_conv_v<n>: run(sql, save, out)
1.1.0: quarter filter fixed (v1 kept only quarters of years divisible by 3); 13F ids added from v1's name search.
"""
import json

import numpy as np
import pandas as pd

# >>> FROZEN INPUT
MGR = json.loads("[{\"name\": \"Joel Greenblatt\", \"group\": \"roster\", \"mgrnos\": [\"10969\", \"12775\"]}, {\"name\": \"Terry Smith\", \"group\": \"roster\", \"mgrnos\": [\"13408\"]}, {\"name\": \"Dev Kantesaria\", \"group\": \"roster\", \"mgrnos\": [\"14460\"]}, {\"name\": \"Chris Hohn\", \"group\": \"roster\", \"mgrnos\": [\"11194\"]}, {\"name\": \"Glenn Greenberg\", \"group\": \"roster\", \"mgrnos\": [\"16080\"]}, {\"name\": \"Val Zlatev\", \"group\": \"roster\", \"mgrnos\": [\"7142\"]}, {\"name\": \"Derek Pilecki\", \"group\": \"roster\", \"mgrnos\": [\"8799\"]}, {\"name\": \"Bill Nygren and Alex Fitch\", \"group\": \"roster\", \"mgrnos\": [\"43485\"]}, {\"name\": \"Murray Stahl\", \"group\": \"roster\", \"mgrnos\": [\"44850\", \"49373\"]}, {\"name\": \"Pat Dorsey\", \"group\": \"roster\", \"mgrnos\": [\"14201\"]}, {\"name\": \"Chris Davis\", \"group\": \"roster\", \"mgrnos\": [\"78320\"]}, {\"name\": \"Joseph Shaposhnik\", \"group\": \"roster\", \"mgrnos\": []}, {\"name\": \"Alex Sacerdote\", \"group\": \"roster\", \"mgrnos\": [\"11405\"]}, {\"name\": \"David Einhorn\", \"group\": \"roster\", \"mgrnos\": [\"42315\"]}, {\"name\": \"Stan Druckenmiller\", \"group\": \"roster\", \"mgrnos\": [\"13021\", \"23704\"]}, {\"name\": \"Todd Kantor\", \"group\": \"roster\", \"mgrnos\": [\"13431\"]}, {\"name\": \"Bob Robotti\", \"group\": \"roster\", \"mgrnos\": [\"10247\"]}, {\"name\": \"Fred Martin\", \"group\": \"roster\", \"mgrnos\": [\"23050\"]}, {\"name\": \"Brad Gerstner\", \"group\": \"roster\", \"mgrnos\": [\"13112\"]}, {\"name\": \"Chris Bloomstran\", \"group\": \"roster\", \"mgrnos\": [\"11757\"]}, {\"name\": \"Li Lu\", \"group\": \"roster\", \"mgrnos\": [\"14546\"]}, {\"name\": \"Warren Buffett\", \"group\": \"control\", \"mgrnos\": [\"8350\"]}, {\"name\": \"Henry Ellenbogen\", \"group\": \"control\", \"mgrnos\": [\"9442\"]}, {\"name\": \"Jim Chanos\", \"group\": \"control\", \"mgrnos\": [\"12867\"]}, {\"name\": \"John Lennon\", \"group\": \"control\", \"mgrnos\": [\"9090\"]}, {\"name\": \"Peter Keefe\", \"group\": \"control\", \"mgrnos\": [\"5300\"]}, {\"name\": \"Tobias Carlisle\", \"group\": \"control\", \"mgrnos\": []}, {\"name\": \"Arnold Van Den Berg\", \"group\": \"control\", \"mgrnos\": [\"15095\"]}, {\"name\": \"Eddy Elfenbein\", \"group\": \"control\", \"mgrnos\": []}]")
SEARCH = json.loads("[]")
# <<< FROZEN INPUT

Q0, Q1 = "2009-12-31", "2025-12-31"
COM = "securitytype = 'EQTY' and securitysubtype = 'COM' and sharetype = 'NS' and primaryexch in ('N','A','Q')"


def run(sql, save, out):
    ids = sorted({int(m) for r in MGR for m in r["mgrnos"]})
    out("investors in input: %d (with 13F ids: %d); 13F ids: %d" % (len(MGR), sum(1 for r in MGR if r["mgrnos"]), len(ids)))
    if SEARCH:
        nm = sql("select distinct mgrno, mgrname from tfn.s34names")
        for r in SEARCH:
            hit = nm[nm.mgrname.astype(str).str.upper().str.contains(r["pattern"], regex=False)]
            out("name search '%s' (%s): %s" % (r["pattern"], r["name"], "; ".join(
                "%d %s" % (int(a), str(b)[:40]) for a, b in hit.drop_duplicates("mgrno").head(8).values) or "none"))
    if not ids:
        out("no ids; stop")
        return
    h = sql("select mgrno, rdate, cusip, sum(shares)::float8 as sh from tfn.s34 where fdate = rdate and rdate between "
            "'%s' and '%s' and mgrno in (%s) and shares > 0 group by mgrno, rdate, cusip" % (Q0, Q1, ",".join(map(str, ids))))
    n = sql("select distinct cusip, permno, namedt, coalesce(nameenddt, date '2099-12-31') as nend from crsp.stocknames_v2 "
            "where cusip is not null")
    mcols = list(sql("select * from crsp.msf_v2 limit 1").columns)
    fac = next((c for c in ("mthcumfacshr", "cumfacshr", "cfacshr") if c in mcols), None)
    p = sql("select permno, yyyymm, abs(mthprc)::float8 as px%s from crsp.msf_v2 where mod(yyyymm, 100) in (3, 6, 9, 12) "
            "and yyyymm between 200912 and 202512 and %s" % ((", %s::float8 as fac" % fac) if fac else "", COM))
    out("13F rows %d; share factor column: %s" % (len(h), fac or "NONE (additions not split-adjusted)"))
    h["rdate"] = pd.to_datetime(h.rdate)
    n["namedt"], n["nend"] = pd.to_datetime(n["namedt"]), pd.to_datetime(n["nend"])
    m = h.merge(n, on="cusip", how="left")
    m = m[(m.rdate >= m.namedt) & (m.rdate <= m.nend)].sort_values("permno").drop_duplicates(["mgrno", "rdate", "cusip"])
    m["yyyymm"] = m.rdate.dt.year * 100 + m.rdate.dt.month
    m = m.merge(p, on=["permno", "yyyymm"], how="inner")
    if not fac:
        m["fac"] = 1.0
    m["v"] = m.sh * m.px
    m["shadj"] = m.sh * m.fac.fillna(1.0)
    g = m.groupby(["mgrno", "yyyymm", "permno"], as_index=False).agg(v=("v", "sum"), shadj=("shadj", "sum"), px=("px", "first"),
                                                                     fac=("fac", "first"))
    g["w"] = g.v / g.groupby(["mgrno", "yyyymm"]).v.transform("sum")
    g["rank"] = g.groupby(["mgrno", "yyyymm"]).w.rank(ascending=False, method="first")
    qs = sorted(g.yyyymm.unique())
    prevq = {q: qs[i - 1] for i, q in enumerate(qs) if i}
    g["prevq"] = g.yyyymm.map(prevq)
    prev = g[["mgrno", "yyyymm", "permno", "shadj"]].rename(columns={"yyyymm": "prevq", "shadj": "shadj0"})
    g = g.merge(prev, on=["mgrno", "prevq", "permno"], how="left")
    filed = set(zip(g.mgrno, g.yyyymm))
    havep = pd.Series([(a, b) in filed for a, b in zip(g.mgrno, g.prevq)], index=g.index)  # filed the quarter before
    g["new"] = havep & g.shadj0.isna()
    g["add"] = havep & g.shadj0.notna() & (g.shadj >= 1.2 * g.shadj0)
    g["bought_v"] = np.where(g.new, g.v, np.where(g["add"], (g.shadj - g.shadj0) / g.fac.replace(0, np.nan) * g.px, 0.0))
    tot = g.groupby(["mgrno", "yyyymm"]).v.transform("sum")
    g["conv_a"] = (g.new | g["add"]) & (g["rank"] <= 5)
    g["conv_b"] = (g.new | g["add"]) & (g.bought_v >= 0.01 * tot)
    held = g.sort_values("yyyymm").groupby(["mgrno", "permno"]).cumcount() + 1
    g["q_held"] = held
    save("eq_conv_panel", g[["mgrno", "yyyymm", "permno", "w", "rank", "new", "add", "conv_a", "conv_b", "q_held"]])
    out("panel saved on WRDS: eq_conv_panel (%d rows); quarters %d (%d .. %d)" % (len(g), len(qs), qs[0], qs[-1]))
    out("investor | 13F ids | quarters filed | median holdings | median top-5 weight % | conviction purchases a, b, either | "
        "new positions | additions")
    for r in MGR:
        ms = [int(x) for x in r["mgrnos"]]
        d = g[g.mgrno.isin(ms)]
        if not len(d):
            out("%s | %s | 0" % (r["name"], ",".join(map(str, ms)) or "-"))
            continue
        per = d.groupby("yyyymm")
        top5 = per.apply(lambda x: x.nlargest(5, "w").w.sum())
        out("%s | %s | %d | %d | %.0f | %d, %d, %d | %d | %d" % (
            r["name"], ",".join(map(str, ms)), per.ngroups, int(per.size().median()), 100 * top5.median(),
            int(d.conv_a.sum()), int(d.conv_b.sum()), int((d.conv_a | d.conv_b).sum()), int(d.new.sum()), int(d["add"].sum())))
    out("ALL DONE")
