"""lseg_ident_v2: contract-identity diagnosis (TESTING_PROTOCOL 7.10 item 3 step 2), DESIGN part only.
For each futures root: every sample contract (L11 / L12 Contract sample) is matched by value to the continuous
positions on each date (which position held it), then compared with the rule calendar (lseg_rules) under each
variant: listed months base / serial with the nearest 2, 3 or 4 calendar months; roll anchor last trading day,
the business day before it, or the first notice day (delivery roots). Prints counts per variant and, for the base and
the best variant, each disagreement as (contract, frequency, date, observed position, rule position): dates and
position numbers only, no data value.
v2 adds: (1) the TR.ExpiryDate dated series on continuation RICs (L11 / L12 Identity probe): value format, date
coverage, the contract each implies (the calendar month whose rule last trading day lies within 3 days of the
expiry) and its agreement with the rule's held contract at that position, per variant, with disagreements listed as
(date, implied delivery, rule delivery); (2) per sample file (L11 / L12)."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import datetime as dt  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402
from collections import defaultdict  # noqa: E402

import numpy as np  # noqa: E402

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
print("=== lseg_ident_v2 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
try:
    import lsegdata as LD
    import lseg_rules as LR
    cat, long, lock, cal = LD.load_design(WORK, allow_untouched=True)
    roots = LD.roots_config()
except Exception as e:  # noqa: BLE001
    print("LOAD FAILED", type(e).__name__, str(e)[:300])
    print("".join(traceback.format_exc().splitlines(True)[-6:]))
    print("=== END ===")
    sys.exit(0)
print("lsegdata %s | %s | LOCK %s" % (LD.VERSION, LR.VERSION, lock))
REL_TOL = 1e-9
MAXLINES = 12
stored = cat[cat["series_id"] != ""]
data = {}
for (per, sid), g in long.groupby(["per", "sid"], sort=False):
    data[(per, sid)] = (g["obs"].to_numpy(dtype="datetime64[D]"), g["value"].to_numpy(dtype="float64"))


def eq(a, b):
    return abs(a - b) <= REL_TOL * max(1.0, abs(a), abs(b))


samples = defaultdict(list)
for r in stored.itertuples():
    code = r.code.strip("<>")
    m = LD.RIC_RE.match(code)
    if m and m.group(4) is not None and (r.per, r.series_id) in data:
        for rt, rc in roots.items():
            if m.group(1) in (rc["ric_root"], rc.get("ric_root_alt") or "#"):
                samples[rt].append((r.per, r.series_id, code, r.file))
# observed positions: (root) -> list of (code, per, date, trading day, position)
obsd = defaultdict(list)
for root, lst in samples.items():
    rc = roots[root]
    mk = LR.MARKET.get(root, "US")
    for per, sid, code, f in lst:
        obs, val = data[(per, sid)]
        cser = {}
        for n in LD.root_positions(rc, per):
            k = (per, LD.c_series_id(rc, n, per))
            if k in data:
                o, v = data[k]
                cser[n] = dict(zip(o.tolist(), v.tolist()))
        nh = na = 0
        for d, v in zip(obs.tolist(), val.tolist()):
            hits = [n for n, mp in cser.items() if d in mp and eq(mp[d], v)]
            if len(hits) == 1:
                obsd[root].append((code, per, d, LD.trading_day(d, mk), hits[0]))
            elif not hits:
                nh += 1
            else:
                na += 1
        print("SAMPLE %s %s %s | %s | dates %d | matched to one position %d | none %d | several %d | first %s last %s"
              % (root, code, per, f, len(obs), len(obs) - nh - na, nh, na, obs.min() if len(obs) else "-",
                 obs.max() if len(obs) else "-"))
VARS = [(lst, near, anc) for lst, near in (("base", None), ("serial", 2), ("serial", 3), ("serial", 4))
        for anc in ("last_trade", "last_trade_m1", "first_notice")]
cals = {}
print("--- VARIANTS (agree / disagree / rule cannot say)")
for root in roots:
    if root not in obsd:
        print("IDENT %s | no matched sample observation" % root)
        continue
    res = {}
    for lst, near, anc in VARS:
        if anc == "first_notice" and root not in LR.FND:
            continue
        if lst == "serial" and root not in LR.SERIAL_NEAR:
            continue
        rr = {k: dict(v, roll_on=anc) for k, v in roots.items()}
        key = (lst, near)
        if key not in cals:
            cals[key] = LR.rule_calendar(roots, lst)
        C = LR.RuleCalendar(rr, lst, near=near, cal=cals[key])
        a = d_ = u = 0
        dis = []
        for code, per, d, td, pos in obsd[root]:
            p = C.position_of(root, code, td)
            if p is None:
                u += 1
            elif p == pos:
                a += 1
            else:
                d_ += 1
                dis.append((code, per, d, pos, p))
        res[(lst, near, anc)] = (a, d_, u, dis)
    best = max(res, key=lambda k: (res[k][0] - 5 * res[k][1], -list(res).index(k)))
    print("IDENT %s | %s" % (root, " | ".join("%s%s/%s %d/%d/%d" % (k[0], k[1] or "", k[2], *res[k][:3])
                                             for k in res)))
    a, d_, u, _ = res[best]
    print("IDENT BEST %s | %s%s/%s | agree %d of %d (%.1f%%) | cannot say %d" % (
        root, best[0], best[1] or "", best[2], a, a + d_, 100.0 * a / max(1, a + d_), u))
    for k in dict.fromkeys([("base", None, "last_trade"), best]):
        if k not in res:
            continue
        for code, per, d, pos, p in res[k][3][:MAXLINES]:
            print("DIS %s %s%s/%s | %s %s %s | observed position %d | rule position %d" % (
                root, k[0], k[1] or "", k[2], code, per, d, pos, p))
        if len(res[k][3]) > MAXLINES:
            print("DIS %s %s%s/%s | ... %d more" % (root, k[0], k[1] or "", k[2], len(res[k][3]) - MAXLINES))
# =====================================================================================================================
print("--- EXPIRY SERIES (TR.ExpiryDate on continuation RICs)")
EXCEL0 = dt.date(1899, 12, 30)
ALLM = {}


def all_months(root):
    if root not in ALLM:
        ALLM[root] = {}
        for y in range(1972, 2031):
            for m in range(1, 13):
                ALLM[root][(y, m)] = LR.dates(root, y, m)[0]
    return ALLM[root]


def as_expiry(v):
    if 20000 < v < 80000:
        return EXCEL0 + dt.timedelta(days=int(round(v))), "serial"
    if 19000101 <= v <= 21001231 and float(v).is_integer():
        iv = int(v)
        try:
            return dt.date(iv // 10000, iv // 100 % 100, iv % 100), "yyyymmdd"
        except ValueError:
            return None, "bad"
    return None, "other"


ex = stored[stored["field"].str.upper() == "TR.EXPIRYDATE"]
for r in ex.itertuples():
    k = (r.per, r.series_id)
    if k not in data:
        print("EXPIRY %s %s | %s | no design data (%s)" % (r.file, r.code, r.status, (r.error or "")[:50]))
        continue
    code = r.code.upper()
    root = next((rt for rt, rc in roots.items() if code.startswith(rc["ric_root"].upper() + "C")
                 and code[len(rc["ric_root"]) + 1:].isdigit()), None)
    if root is None:
        continue
    n = int(code[len(roots[root]["ric_root"]) + 1:])
    obs, val = data[k]
    fmt = defaultdict(int)
    implied = []
    for d, v in zip(obs.tolist(), val.tolist()):
        e, f = as_expiry(v)
        fmt[f] += 1
        if e is None:
            continue
        am = all_months(root)
        hit = [ym for ym, lt in am.items() if abs((lt - e).days) <= 3]
        implied.append((d, e, hit[0] if len(hit) == 1 else None, (e - d).days))
    ahead = [x[3] for x in implied]
    print("EXPIRY %s %s | position %d | dates %d (%s .. %s) | formats %s | days from date to expiry min %s max %s | "
          "implied contract found %d of %d" % (r.file, r.code, n, len(obs), obs.min(), obs.max(), dict(fmt),
                                               min(ahead) if ahead else "-", max(ahead) if ahead else "-",
                                               sum(1 for x in implied if x[2]), len(implied)))
    for lst, near in (("base", None), ("serial", 2), ("serial", 3), ("serial", 4)):
        if lst == "serial" and root not in LR.SERIAL_NEAR:
            continue
        key = (lst, near)
        if key not in cals:
            cals[key] = LR.rule_calendar(roots, lst)
        C = LR.RuleCalendar(roots, lst, near=near, cal=cals[key])
        a = d_ = u = 0
        dl = []
        for d, e, ym, _ in implied:
            h = C.held(root, n, LD.trading_day(d, LR.MARKET.get(root, "US")))
            if h is None or ym is None:
                u += 1
                continue
            if h[1] == "%d-%02d" % ym:
                a += 1
            else:
                d_ += 1
                dl.append((d, "%d-%02d" % ym, h[1]))
        print("EXPIRY %s %s | %s%s | agree %d disagree %d cannot say %d" % (r.file, r.code, lst, near or "", a, d_, u))
        if lst == "base" or root in LR.SERIAL_NEAR:
            for d, im, rl in dl[:MAXLINES]:
                print("EXPDIS %s %s%s | %s | implied delivery %s | rule delivery %s" % (r.code, lst, near or "", d, im,
                                                                                     rl))
            if len(dl) > MAXLINES:
                print("EXPDIS %s %s%s | ... %d more (last %s)" % (r.code, lst, near or "", len(dl) - MAXLINES,
                                                                 dl[-1][0]))
print("=== END === %.0fs" % (time.time() - T0))
