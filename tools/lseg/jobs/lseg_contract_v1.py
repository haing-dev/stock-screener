"""lseg_contract_v1: check of the contract-level files L14a-L14l (DESIGN part only; counts and dates, no value).
  FILES    blocks and contract series per file by status
  ROOT     per root: contracts expected / with data, deliveries covered, design months with data
  LEGS     Curve carry (SPEC_Curve_carry s3): per design month t, front leg F = nearest contract with data delivering
           at least three calendar months after t, far leg D = same delivery month one year later; months where both
           are priced in month t, and months where a leg is stale (same month-end price as the month before)
  VALID    are the contract codes the right instruments? Each month-end value of continuous c1 (and c2) is matched to
           the contract priced equally in the same month; that contract is compared with the one the TR.ExpiryDate
           series of c1 / c2 names (L11 / L12)
  STRIP    Eurodollar / Euribor: trading days 1990-2010 on which the first eight quarterly contracts not yet expired
           (rule last trading day) all have a price"""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import datetime as dt  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402
from collections import Counter, defaultdict  # noqa: E402

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
print("=== lseg_contract_v1 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
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
data = {}
for (per, sid), g in long.groupby(["per", "sid"], sort=False):
    data[(per, sid)] = (g["obs"].to_numpy(dtype="datetime64[D]"), g["value"].to_numpy(dtype="float64"))


def eq(a, b):
    return abs(a - b) <= REL_TOL * max(1.0, abs(a), abs(b))


def mi(y, m):
    return y * 12 + m - 1


def ym(i):
    return "%d-%02d" % (i // 12, i % 12 + 1)


L14 = cat[cat["file"].astype(str).str.match(r"^L14[a-z]")]
print("--- FILES")
for f, g in L14.groupby("file"):
    st = Counter(g["status"])
    print("FILES %s | blocks %d | contract series %d | %s" % (f, g["pid"].nunique(), len(g),
                                                             ", ".join("%s %d" % kv for kv in sorted(st.items()))))
# contract table: (root, per) -> {delivery index: {month index or day: value}}
con = defaultdict(dict)
exp = Counter()
for r in L14.itertuples():
    code = str(r.code).strip("<>").upper()
    m_ = LD.RIC_RE.match(code)
    if not m_ or m_.group(4) is None:
        continue
    root = next((rt for rt, rc in roots.items() if m_.group(1) == rc["ric_root"].upper()), None)
    if root is None:
        continue
    dec = int(m_.group(4))
    year = (1900 if dec >= 5 else 2000) + 10 * dec + int(m_.group(3))
    dmi = mi(year, LD.MONTH_CODES.index(m_.group(2)) + 1)
    exp[(root, r.per)] += 1
    k = (r.per, r.series_id)
    if r.status != "ok" or k not in data:
        continue
    obs, val = data[k]
    if r.per == "M":
        con[(root, "M")][dmi] = {mi(d.year, d.month): v for d, v in zip(obs.tolist(), val.tolist())}
    else:
        con[(root, "D")][dmi] = dict(zip(obs.tolist(), val.tolist()))
print("--- ROOT")
for (root, per), cs in sorted(con.items()):
    months = set()
    for s in cs.values():
        months |= {(d if per == "M" else mi(d.year, d.month)) for d in s}
    dm = sorted(x for x in months if x <= mi(2010, 12))
    print("ROOT %s %s | contracts with data %d of %d | deliveries %s .. %s | design months with data %d (%s .. %s)" % (
        root, per, len(cs), exp[(root, per)], ym(min(cs)), ym(max(cs)), len(dm), ym(dm[0]) if dm else "-",
        ym(dm[-1]) if dm else "-"))
print("--- LEGS (Curve carry, design months)")
for (root, per), cs in sorted(con.items()):
    if per != "M":
        continue
    first = min(min(s) for s in cs.values() if s)
    n = both = stale = 0
    gaps = Counter()
    for t in range(max(first, mi(1975, 1)), mi(2010, 12) + 1):
        n += 1
        F = next((d for d in sorted(cs) if d >= t + 3 and t in cs[d]), None)
        if F is None:
            gaps["no front"] += 1
            continue
        D = F + 12
        if D not in cs or t not in cs[D]:
            gaps["no far (front %s)" % LD.MONTH_CODES[F % 12]] += 1
            continue
        both += 1
        if (t - 1 in cs[F] and cs[F][t - 1] == cs[F][t]) or (t - 1 in cs[D] and cs[D][t - 1] == cs[D][t]):
            stale += 1
    print("LEGS %s | design months from %s: %d | both legs priced %d (%.0f%%) | stale %d | gaps: %s" % (
        root, ym(max(first, mi(1975, 1))), n, both, 100.0 * both / max(1, n), stale,
        ", ".join("%s %d" % kv for kv in gaps.most_common(4)) or "none"))
print("--- VALID (continuous c1/c2 month-ends matched to contracts; vs TR.ExpiryDate identity)")
stored = cat[cat["series_id"] != ""]
expd = {}
for r in stored.itertuples():
    if str(r.field).upper() != "TR.EXPIRYDATE" or (r.per, r.series_id) not in data:
        continue
    code = str(r.code).upper()
    root = next((rt for rt, rc in roots.items() if code.startswith(rc["ric_root"].upper() + "C")
                 and code[len(rc["ric_root"]) + 1:].isdigit()), None)
    if root is None:
        continue
    n = int(code[len(roots[root]["ric_root"]) + 1:])
    obs, val = data[(r.per, r.series_id)]
    for d, v in zip(obs.tolist(), val.tolist()):
        if 19000101 <= v <= 21001231 and float(v).is_integer():
            iv = int(v)
            expd[(root, n, mi(d.year, d.month))] = (iv // 10000, iv // 100 % 100)
for (root, per), cs in sorted(con.items()):
    if per != "M":
        continue
    rc = roots[root]
    for n in (1, 2):
        k = ("M", LD.c_series_id(rc, n, "M"))
        if k not in data:
            continue
        obs, val = data[k]
        uniq = none = sev = agree = dis = noref = 0
        for d, v in zip(obs.tolist(), val.tolist()):
            t = mi(d.year, d.month)
            hits = [dm for dm, s in cs.items() if t in s and eq(s[t], v)]
            if not hits:
                none += 1
                continue
            if len(hits) > 1:
                sev += 1
                continue
            uniq += 1
            ref = expd.get((root, n, t))
            if ref is None:
                noref += 1
                continue
            # the expiry month names the contract: the delivery month whose rule last trading day is in that month
            y, m = ref
            cand = [dm for dm in range(mi(y, m) - 2, mi(y, m) + 3)
                    if (lambda lt: (lt.year, lt.month) == (y, m))(LR.dates(root, dm // 12, dm % 12 + 1)[0])]
            if hits[0] in cand:
                agree += 1
            else:
                dis += 1
        print("VALID %s c%d | month-ends %d | one contract %d | none %d | several %d | vs expiry series: agree %d "
              "disagree %d no expiry %d" % (root, n, len(obs), uniq, none, sev, agree, dis, noref))
print("--- STRIP (first eight quarterly contracts priced, trading days 1990-2010)")
for (root, per), cs in sorted(con.items()):
    if per != "D":
        continue
    days = sorted({d for s in cs.values() for d in s if dt.date(1990, 1, 1) <= d <= dt.date(2010, 12, 31)})
    full = 0
    short = Counter()
    for d in days:
        alive = [dm for dm in sorted(cs) if LR.dates(root, dm // 12, dm % 12 + 1)[0] >= d][:8]
        k = sum(1 for dm in alive if d in cs[dm])
        if k == 8:
            full += 1
        else:
            short[k] += 1
    print("STRIP %s | trading days %d | all eight priced %d (%.0f%%) | fewer: %s" % (
        root, len(days), full, 100.0 * full / max(1, len(days)),
        ", ".join("%d priced x%d" % kv for kv in sorted(short.items())) or "none"))
print("=== END === %.0fs" % (time.time() - T0))
