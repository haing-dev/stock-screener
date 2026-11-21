"""eq_univ 1.1.0 (runs on WRDS Cloud): completeness check of the LSEG company list (plan v0.4 step 3a;
docs/research/equity/LSEG_universe_v1_2026-11-20.md; V04_REGISTRATION.md addenda A1, A2). Seal-exempt descriptive job
(tools/equity/seal_exempt.json, SEAL_LOG.md): reads CRSP listing levels only (names, December prices and shares), never
a return.

Input (frozen block), all from LSEG: CAND = 8-digit CUSIPs (Datastream lists "D", Workspace screens "W"); TICK = ticker
roots of active Workspace instruments; NAMES = normalised company names (norm() below) of every equity row.
1.1.0 (after v1 found the CUSIP key alone misses companies whose CUSIP changed after 2025 and companies not incorporated
in the US): three keys reported in steps (CUSIP; + current ticker for companies still listed at 2025-12; + normalised
name), split by CRSP's US-incorporation flag. Output: counts and shares per year, the column names of the names table,
and the names of at most 10 of the largest companies not found, for three dates and for companies that left.

Job name: eq_univ_check_v<n>: check(sql, out)
"""
import json
import re

import numpy as np
import pandas as pd

# >>> FROZEN INPUT
CAND = json.loads("{}")
TICK = json.loads("[]")
NAMES = json.loads("[]")  # full input (LSEG identifiers and names) only on the PC / WRDS
# <<< FROZEN INPUT

DROP = {"INC", "CORP", "CORPORATION", "CO", "COMPANY", "LTD", "LIMITED", "PLC", "SA", "NV", "AG", "SE", "LP", "LLC",
        "THE", "NEW", "OF", "AND", "HOLDINGS", "HOLDING", "HLDG", "HLDGS", "GROUP", "GP", "TRUST", "CLASS", "CL", "COM",
        "A", "B", "C", "DEL", "N", "S", "DEAD", "ADR", "SHS", "ORD"}
MAP = {"INTL": "INTERNATIONAL", "INTERNATIONAL": "INTERNATIONAL", "FINL": "FINANCIAL", "FIN": "FINANCIAL",
       "BK": "BANK", "BANCORP": "BANCORP", "BANC": "BANCORP", "BANCORPORATION": "BANCORP", "INDS": "INDUSTRIES",
       "IND": "INDUSTRIES", "TECH": "TECHNOLOGIES", "TECHS": "TECHNOLOGIES", "TECHNOLOGY": "TECHNOLOGIES",
       "PHARMS": "PHARMACEUTICALS", "PHARM": "PHARMACEUTICALS", "PHARMA": "PHARMACEUTICALS", "SVS": "SERVICES",
       "SVCS": "SERVICES", "SERVICE": "SERVICES", "SYS": "SYSTEMS", "SYSTEM": "SYSTEMS", "COMMS": "COMMUNICATIONS",
       "COMMUNICATION": "COMMUNICATIONS", "RES": "RESOURCES", "RESOURCE": "RESOURCES", "ENTM": "ENTERTAINMENT",
       "ENT": "ENTERPRISES", "ENTS": "ENTERPRISES", "PROPS": "PROPERTIES", "PROP": "PROPERTIES", "MNFG": "MANUFACTURING",
       "MFG": "MANUFACTURING", "LABS": "LABORATORIES", "LAB": "LABORATORIES", "NAT": "NATIONAL", "NATL": "NATIONAL",
       "AMER": "AMERICAN", "AMERICA": "AMERICAN", "ELEC": "ELECTRIC", "ELECTRONICS": "ELECTRONIC", "ENGR": "ENGINEERING",
       "PTNS": "PARTNERS", "PRTNS": "PARTNERS", "SOLUTION": "SOLUTIONS", "SLTN": "SOLUTIONS", "THERAPEUTIC": "THERAPEUTICS",
       "THERP": "THERAPEUTICS", "CAP": "CAPITAL", "INV": "INVESTMENT", "INVS": "INVESTMENT", "INVESTMENTS": "INVESTMENT",
       "RLTY": "REALTY", "INS": "INSURANCE", "MED": "MEDICAL", "HLTH": "HEALTH", "HEALTHCARE": "HEALTH", "CTL": "CONTROL",
       "PRDS": "PRODUCTS", "PRODUCT": "PRODUCTS", "PRODS": "PRODUCTS", "MTRS": "MOTORS", "ENERGY": "ENERGY", "EN": "ENERGY"}


def norm(s):
    s = str(s).upper()
    s = re.split(r"\s+DEAD\b|\s+SUSP\b|\(", s)[0]
    s = s.replace("&", " ").replace(".", " ")
    toks = [MAP.get(t, t) for t in re.sub(r"[^A-Z0-9 ]", "", s).split()]
    toks = [t for t in toks if t not in DROP]
    return " ".join(toks[:4])


def check(sql, out):
    cols = list(sql("select * from crsp.stocknames_v2 limit 1").columns)
    out("crsp.stocknames_v2 columns: " + ", ".join(cols))
    namecol = next((c for c in ("issuernm", "comnam", "securitynm") if c in cols), None)
    want = ["permno", "cusip"] + [c for c in (namecol, "ticker", "usincflg", "nameenddt") if c and c in cols]
    nm = sql("select %s from crsp.stocknames_v2" % ", ".join(want))
    tick, names = set(TICK), set(NAMES)
    nm["k_c"] = nm.cusip.astype(str).str[:8].isin(set(CAND))
    nm["k_n"] = nm[namecol].map(lambda s: norm(s) in names and norm(s) != "") if namecol else False
    last = nm.sort_values("nameenddt").groupby("permno").tail(1) if "nameenddt" in nm else nm.groupby("permno").tail(1)
    last = last.set_index("permno")
    kt = last.ticker.astype(str).str.upper().isin(tick) if "ticker" in last else pd.Series(False, index=last.index)
    usf = last.usincflg.astype(str).str.upper() if "usincflg" in last else pd.Series("?", index=last.index)
    kc = nm.groupby("permno").k_c.any()
    kn = nm.groupby("permno").k_n.any()
    nmap = last[namecol] if namecol else None
    com = ("securitytype = 'EQTY' and securitysubtype = 'COM' and sharetype = 'NS' and primaryexch in ('N','A','Q')")
    dec = sql("select permno, yyyymm, abs(mthprc)::float8 as px, shrout::float8 as sh from crsp.msf_v2 "
              "where mod(yyyymm, 100) = 12 and yyyymm between 200912 and 202512 and " + com)
    life = sql("select permno, max(yyyymm) as last from crsp.msf_v2 where yyyymm between 201001 and 202512 and "
               + com + " group by permno")
    alive = set(life.permno[life["last"] == 202512])

    def keys(df):
        p = df.permno
        c = p.map(kc).fillna(False).astype(bool)
        t = c | (p.map(kt).fillna(False).astype(bool) & p.isin(alive))
        n = t | p.map(kn).fillna(False).astype(bool)
        return c, t, n

    dec["mv"] = dec.px * dec.sh
    dec["us"] = dec.permno.map(usf).fillna("?")
    dec["c"], dec["t"], dec["n"] = keys(dec)
    out("US-incorporation flag values (securities): " + ", ".join("%s %d" % kv for kv in usf.value_counts().items()))
    out("CRSP common shares (NYSE / American / Nasdaq) each December. Found % by key: C = CUSIP, T = C or current "
        "ticker (still listed 2025-12), N = T or normalised name")
    out("year | all n: C, T, N | 1,500 largest priced >= $5: C, T, N | of those US-incorporated n: C, T, N | "
        "not US-incorporated n: C, T, N")
    tops = {}
    for ym, g in dec.groupby("yyyymm"):
        g = g.sort_values("mv", ascending=False)
        t5 = g[g.px >= 5].head(1500)
        tops[ym] = t5
        u, f = t5[t5.us == "Y"], t5[t5.us != "Y"]

        def s(d):
            return "%.1f, %.1f, %.1f" % (100 * d.c.mean(), 100 * d.t.mean(), 100 * d.n.mean()) if len(d) else "-"
        out("%d | %d: %s | %s | %d: %s | %d: %s" % (ym // 100, len(g), s(g), s(t5), len(u), s(u), len(f), s(f)))
    gone = life[life["last"] < 202512].copy()
    gone["y"] = gone["last"] // 100
    gone["us"] = gone.permno.map(usf).fillna("?")
    gone["c"], gone["t"], gone["n"] = keys(gone)
    big = dec.groupby("permno").mv.max()
    gone["mv"] = gone.permno.map(big)
    out("companies leaving each year | all n: C, N | US-incorporated n: C, N | US-incorporated with a peak December "
        "value in the top 1,500 of that December n: C, N")
    top_ever = set()
    for ym, g in dec.groupby("yyyymm"):
        top_ever |= set(g.sort_values("mv", ascending=False).head(1500).permno)
    for y, g in gone.groupby("y"):
        u = g[g.us == "Y"]
        b = u[u.permno.isin(top_ever)]

        def s2(d):
            return "%d: %.1f, %.1f" % (len(d), 100 * d.c.mean(), 100 * d.n.mean()) if len(d) else "0: -"
        out("%d | %s | %s | %s" % (y, s2(g), s2(u), s2(b)))
    if nmap is not None:
        for ym in (200912, 201712, 202412):
            t5 = tops.get(ym)
            if t5 is None:
                continue
            for lab, d in (("US-incorporated", t5[t5.us == "Y"]), ("not US-incorporated", t5[t5.us != "Y"])):
                miss = d[~d.n].head(10)
                out("largest NOT found by any key at %d, %s (%d missing): %s" % (ym // 100, lab, int((~d.n).sum()),
                    "; ".join(str(nmap.get(p, "?"))[:28] for p in miss.permno)))
        g2 = gone[(~gone.n) & (gone.us == "Y")].sort_values("mv", ascending=False).head(10)
        out("largest US-incorporated NOT found among companies that left: %s" % "; ".join(
            "%s (%d)" % (str(nmap.get(p, "?"))[:28], y) for p, y in zip(g2.permno, g2.y)))
    out("ALL DONE")
