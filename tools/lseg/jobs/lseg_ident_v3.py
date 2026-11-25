"""lseg_ident_v3: fit the contract-listing rule per futures root and era (identity facts, not performance), DESIGN
part only. Evidence: (a) sample contracts matched by value to one continuous position (L11 / L12 Contract sample);
(b) TR.ExpiryDate dated series on continuation RICs (L11 / L12 Identity probe): the expiry names the contract the
position held. Prints:
  LT    per root and era: observed expiry (c1/c2 series) minus the rule last trading day, in business days
  FIT   per root and era: the listing model with the most agreement (agree - 5 x disagree) from a fixed grid:
        cycle months listed while fewer than H months ahead, plus 'far' months listed at any distance, plus serial
        (non-cycle) months while fewer than N months ahead; anchor = observed expiry where known, else the rule
  DIS   up to 8 disagreements of the fitted model: (contract, date, observed position, model position)
Dates, month counts and position numbers only: no data value."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import datetime as dt  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402
from collections import Counter, defaultdict  # noqa: E402

import numpy as np  # noqa: E402

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
print("=== lseg_ident_v3 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
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
ERAS = [(1972, 1984), (1985, 1994), (1995, 2004), (2005, 2010)]
H_GRID = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 36, 48, 60, 999]
FAR_GRID = ["", "Z", "MZ", "NZ", "HNZ", "FNX", "NX", "HNUZ", "GJMQVZ"]
NEAR_GRID = [0, 1, 2, 3, 4]
stored = cat[cat["series_id"] != ""]
data = {}
for (per, sid), g in long.groupby(["per", "sid"], sort=False):
    data[(per, sid)] = (g["obs"].to_numpy(dtype="datetime64[D]"), g["value"].to_numpy(dtype="float64"))


def eq(a, b):
    return abs(a - b) <= REL_TOL * max(1.0, abs(a), abs(b))


def era_of(d):
    for a, b in ERAS:
        if a <= d.year <= b:
            return "%d-%d" % (a, b)
    return None


def mi(y, m):
    return y * 12 + m - 1


def ymd(v):
    if 19000101 <= v <= 21001231 and float(v).is_integer():
        iv = int(v)
        try:
            return dt.date(iv // 10000, iv // 100 % 100, iv % 100)
        except ValueError:
            return None
    if 20000 < v < 80000:
        return dt.date(1899, 12, 30) + dt.timedelta(days=int(round(v)))
    return None


RULE = {}


def rule_lt(root, y, m):
    k = (root, y, m)
    if k not in RULE:
        RULE[k] = LR.dates(root, y, m)[0]
    return RULE[k]


# ------------------------------------------------------------------ evidence
ev = defaultdict(list)            # root -> [(delivery month index, day, observed position, source)]
obs_lt = defaultdict(dict)        # root -> {delivery month index: observed expiry}
for r in stored.itertuples():
    if (r.per, r.series_id) not in data:
        continue
    code = r.code.strip("<>").upper()
    if r.field.upper() == "TR.EXPIRYDATE":
        root = next((rt for rt, rc in roots.items() if code.startswith(rc["ric_root"].upper() + "C")
                     and code[len(rc["ric_root"]) + 1:].isdigit()), None)
        if root is None:
            continue
        n = int(code[len(roots[root]["ric_root"]) + 1:])
        obs, val = data[(r.per, r.series_id)]
        for d, v in zip(obs.tolist(), val.tolist()):
            e = ymd(v)
            if e is None:
                continue
            best = None
            for k in range(-2, 40):
                y, m = divmod(mi(d.year, d.month) + k, 12)
                lt = rule_lt(root, y, m + 1)
                if abs((lt - e).days) <= 10 and (best is None or abs((lt - e).days) < best[1]):
                    best = (mi(y, m + 1), abs((lt - e).days))
            if best is None:
                continue
            ev[root].append((best[0], LD.trading_day(d, LR.MARKET.get(root, "US")), n, "X"))
            if n <= 2:
                obs_lt[root][best[0]] = e
        continue
    m_ = LD.RIC_RE.match(code)
    if not m_ or m_.group(4) is None:
        continue
    root = next((rt for rt, rc in roots.items() if m_.group(1) in (rc["ric_root"], rc.get("ric_root_alt") or "#")),
                None)
    if root is None:
        continue
    dec = int(m_.group(4))
    year = (1900 if dec >= 5 else 2000) + 10 * dec + int(m_.group(3))
    dmi = mi(year, LD.MONTH_CODES.index(m_.group(2)) + 1)
    rc = roots[root]
    obs, val = data[(r.per, r.series_id)]
    cser = {}
    for n in LD.root_positions(rc, r.per):
        k = (r.per, LD.c_series_id(rc, n, r.per))
        if k in data:
            o, v = data[k]
            cser[n] = dict(zip(o.tolist(), v.tolist()))
    for d, v in zip(obs.tolist(), val.tolist()):
        hits = [n for n, mp in cser.items() if d in mp and eq(mp[d], v)]
        if len(hits) == 1:
            ev[root].append((dmi, LD.trading_day(d, LR.MARKET.get(root, "US")), hits[0], "S"))

# ------------------------------------------------------------------ last trading day check
print("--- LT (observed expiry of contracts held at c1/c2 minus the rule last trading day, business days)")
for root in roots:
    if root not in obs_lt:
        continue
    mk = LR.MARKET.get(root, "US")
    by = defaultdict(Counter)
    for dmi, e in obs_lt[root].items():
        y, m = divmod(dmi, 12)
        lt = rule_lt(root, y, m + 1)
        a, b = sorted([lt, e])
        nbd = int(np.busday_count(np.datetime64(a, "D"), np.datetime64(b, "D")))
        by[era_of(dt.date(y, m + 1, 1)) or "other"][nbd if e >= lt else -nbd] += 1
    print("LT %s | %s" % (root, " | ".join("%s: %s" % (k, ", ".join("%+d x%d" % kv for kv in sorted(c.items())))
                                          for k, c in sorted(by.items()))))


# ------------------------------------------------------------------ listing fit
def anchor(root, dmi):
    e = obs_lt[root].get(dmi)
    if e is not None:
        return e
    y, m = divmod(dmi, 12)
    return rule_lt(root, y, m + 1)


def _unused_predict(root, dmi, day, H, far, near):
    cyc = LR.CYCLE[root]
    t = mi(day.year, day.month)
    p = 1
    for k in range(t - 2, dmi):
        code = LD.MONTH_CODES[k % 12]
        ahead = k - t
        if anchor(root, k) < day:
            continue
        if code in cyc:
            ok = ahead < H or code in far
        else:
            ok = ahead < near
        if ok:
            p += 1
    return p


def expand(root, E):
    """Concatenated arrays over all evidence items: item index, months ahead, is-cycle, month code (alive months
    before the observed contract)."""
    cyc = LR.CYCLE[root]
    idx, ah, cy, cd = [], [], [], []
    for i, (dmi, day, p, s) in enumerate(E):
        t = mi(day.year, day.month)
        for k in range(t - 2, dmi):
            if anchor(root, k) < day:
                continue
            code = LD.MONTH_CODES[k % 12]
            idx.append(i)
            ah.append(k - t)
            cy.append(code in cyc)
            cd.append(code)
    return (np.array(idx, dtype=np.int64), np.array(ah, dtype=np.int64), np.array(cy, dtype=bool),
            np.array(cd, dtype="<U1"))


def counts(X, nE, H, far, near):
    idx, ah, cy, cd = X
    infar = np.isin(cd, list(far)) if far else np.zeros(len(cd), dtype=bool)
    ok = (cy & ((ah < H) | infar)) | (~cy & (ah < near))
    return 1 + np.bincount(idx[ok], minlength=nE)


def band(p):
    return "1-2" if p <= 2 else "3-6" if p <= 6 else "7-12" if p <= 12 else "13-18" if p <= 18 else "19+"


print("--- FIT (per root and era; grid H %s, far %s, serial %s)" % (H_GRID, FAR_GRID, NEAR_GRID))
for root in roots:
    if root not in ev or root not in LR.CYCLE:
        print("FIT %s | no evidence" % root)
        continue
    nears = NEAR_GRID if root in LR.SERIAL_NEAR else [0]
    for era in [None] + ["%d-%d" % e for e in ERAS]:
        E = [x for x in ev[root] if era is None or era_of(x[1]) == era]
        E = [x for x in E if anchor(root, x[0]) >= x[1]]          # contract still alive on the day
        if not E:
            continue
        X = expand(root, E)
        P = np.array([x[2] for x in E])
        res = []
        for H in H_GRID:
            for far in FAR_GRID:
                if far and (not set(far) <= set(LR.CYCLE[root]) or H == 999):
                    continue
                for near in nears:
                    a = int((counts(X, len(E), H, far, near) == P).sum())
                    res.append((a - 5 * (len(E) - a), a, H, far, near))
        res.sort(key=lambda x: (-x[0], -x[2], len(x[3]), x[4]))   # ties: the least restrictive model
        sc, a, H, far, near = res[0]
        tie = sum(1 for x in res if x[1] == a)
        print("FIT %s %s | evidence %d (samples %d, expiry %d; positions up to %d) | best H=%s far=%s serial=%d | agree "
              "%d of %d (%.1f%%) | models tied %d | next H=%s far=%s serial=%d agree %d" % (
                  root, era or "all", len(E), sum(1 for x in E if x[3] == "S"), sum(1 for x in E if x[3] == "X"),
                  int(P.max()), H, far or "-", near, a, len(E), 100.0 * a / len(E), tie,
                  res[1][2] if len(res) > 1 else "-", (res[1][3] or "-") if len(res) > 1 else "-",
                  res[1][4] if len(res) > 1 else 0, res[1][1] if len(res) > 1 else 0))
        if era is None:
            Q = counts(X, len(E), H, far, near)
            dis = [(E[i], int(Q[i])) for i in range(len(E)) if Q[i] != P[i]]
            for (dmi, day, p, s), q in dis[:8]:
                y, m = divmod(dmi, 12)
                print("DIS %s | %s delivery %d-%02d | %s | observed %d | model %d" % (root, s, y, m + 1, day, p, q))
            byp, tot = Counter(), Counter()
            for i, x in enumerate(E):
                tot[band(x[2])] += 1
                byp[band(x[2])] += int(Q[i] == P[i])
            print("BYPOS %s | %s" % (root, " | ".join("%s %d/%d" % (k, byp[k], tot[k]) for k in
                                                      ("1-2", "3-6", "7-12", "13-18", "19+") if tot[k])))
print("=== END === %.0fs" % (time.time() - T0))
