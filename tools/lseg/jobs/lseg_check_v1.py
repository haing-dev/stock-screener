"""lseg_check_v1: data check of the locked LSEG store (TESTING_PROTOCOL 7.10 item 3 step 2), DESIGN part only
(observations <= 2010-12-31; the sealed table is never opened: its structure comes from the catalog).
Sections:
  STATUS    expected series by status and file (from the catalog)
  NEED      start dates and design counts against what the specs need (lseg_spec_needs.csv): OK / LATE / SHORT / MISSING
  GAP       gaps over GAP_MONTHS months (monthly) or GAP_DAYS business days (daily) inside each series' design range
  STALE     runs of an unchanged value (Datastream carries dead or holiday values forward)
  COPY      copy groups (status copy), whole-array identical pairs, identical value RUNS shared by different instruments
            (windows of RUN_M months / RUN_D days, constant windows ignored)
  DSDATE    month-end date convention per function (Datastream = last weekday, RHistory / HistoricalPricing = calendar
            month-end labels, RDP.Data = last trading day) and month-ends on US / UK holidays (Datastream prints a value
            for them: the previous day's, unscreened)
  LABEL     monthly vs daily copy of the same series: is the month's value the daily value on the month's date
  IDENTITY  per futures root of lseg_roots.csv: positions pulled, contract calendar (listed months = serial months?,
            anchor dates), roll-rule check on sample contracts (value matching), depth for the spec's legs, VERDICT
  PROBE     the identity-probe and calendar-test blocks of L11: which guesses returned dates
  ENGINE    series mapped to engine ids (first design month, design count)
  SEALED    structure only (counts of sealed observations per file, from the catalog)
Prints counts, shares, names, codes and dates of structure only (export whitelist): no data value, no per-date series of
values. Untouched instruments: structure only (start dates, counts), no value-based test."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import datetime as dt  # noqa: E402
import hashlib  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402
from collections import Counter, defaultdict  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

# ---------------------------------------------------------------- thresholds (fixed before the first run)
GAP_MONTHS = 2        # brief: gaps over 2 months (monthly)
GAP_DAYS = 10         # brief: gaps over 10 trading days (daily); weekdays used as trading days
STALE_MONTHS = 6      # an unchanged month-end value for 6+ months in a market series = dead or carried forward
STALE_DAYS = 10       # 10+ business days unchanged in a daily market series
RUN_M, RUN_D = 24, 60  # window of an identical value run shared by two different instruments
REL_TOL = 1e-9        # equality of two values (relative)
MIN_MATCH = 10        # matched sample observations before a roll rule counts as checked
AGREE_SHARE = 0.99    # share of matched sample observations that must agree with the rule
FAR_MONTHS = 12       # Curve carry: far leg = same delivery month one year after the front leg
FRONT_MIN = 3         # Curve carry: front leg delivers at least 3 calendar months after month t
STRIP_N = 8           # Strip reversion: first eight quarterly contracts
CASH_SETTLED = {"ED", "FEI", "FSS", "FES", "SRA", "SON3"}
FND_EXPECTED = {"GC", "SI", "HG", "PL", "C", "W", "S", "KC", "CT", "LC"}   # delivery notices start before the last
# trading day (metals, grains, softs, cattle); energy and sugar expire before the delivery month (to be confirmed from
# the exchange specifications, CHECK_3.2_B s4)

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
print("=== lseg_check_v1 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
try:
    import lsegdata as LD
    cat, long, lock, cal = LD.load_design(WORK, allow_untouched=True)
    roots = LD.roots_config()
    needs, needs_path = LD._read_csv("lseg_spec_needs.csv")
except Exception as e:  # noqa: BLE001
    print("LOAD FAILED", type(e).__name__, str(e)[:300])
    print("".join(traceback.format_exc().splitlines(True)[-6:]))
    print("=== END ===")
    sys.exit(0)
print("lsegdata %s | LOCK %s | design rows %d | spec needs %s" % (LD.VERSION, lock, len(long),
                                                                   LD.sha256_file(needs_path)[:16]))
stored = cat[cat["series_id"] != ""]
prim = stored[stored["duplicate_of"] == ""]
untouched = set(stored.loc[stored["untouched"] == 1, "series_id"])
data = {}
for (per, sid), g in long.groupby(["per", "sid"], sort=False):
    data[(per, sid)] = (g["obs"].to_numpy(dtype="datetime64[D]"), g["key"].to_numpy(dtype="datetime64[D]"),
                        g["value"].to_numpy(dtype="float64"), g["hol"].to_numpy())
info = {(r.per, r.series_id): r for r in stored.itertuples()}


def d2s(x):
    return str(np.datetime64(x, "D")) if x is not None else "-"


def mon(x):
    return str(np.datetime64(x, "M"))


def eq(a, b):
    return abs(a - b) <= REL_TOL * max(1.0, abs(a), abs(b))


# =====================================================================================================================
print("--- STATUS")
for f, g in cat.groupby("file", sort=False):
    print("STATUS %s | %s" % (f, " | ".join("%s %d" % (s, (g["status"] == s).sum()) for s in LD.STATUSES)))
print("STATUS all | %s | stored primary series: monthly %d, daily %d" % (
    " | ".join("%s %d" % (s, (cat["status"] == s).sum()) for s in LD.STATUSES),
    (prim["per"] == "M").sum(), (prim["per"] == "D").sum()))

# =====================================================================================================================
print("--- NEED (start dates and design counts against the specs)")


def series_state(sid, per):
    if (per, sid) in data:
        r = info[(per, sid)]
        return "ok", r.first if r.n_design else "", int(r.n_design)
    rows = cat[(cat["fn"] + ":" + cat["code"] + "|" + cat["field"] == sid) & (cat["per"] == per)]
    return ("not pulled" if not len(rows) else ",".join(sorted(set(rows["status"])))), "", 0


need_tally = Counter()
for nd in needs:
    tgt, per = nd["target"].strip(), nd["per"].strip()
    need_first = nd["need_first"].strip()
    mind = int(nd["min_design"] or 0)
    if tgt.startswith("root:"):
        _, root, posr = tgt.split(":")
        rc = roots[root]
        sids = [(n, LD.c_series_id(rc, n, per)) for n in LD.positions(posr)]
    else:
        sids = [(None, tgt)]
    states = [(n, s) + series_state(s, per) for n, s in sids]
    missing = [("c%d" % n if n else s, st) for n, s, st, _, _ in states if st != "ok"]
    firsts = [f for _, _, st, f, _ in states if st == "ok" and f]
    nds = [k for _, _, st, _, k in states if st == "ok"]
    latest = max(firsts) if firsts else ""
    verdict = "OK"
    if missing:
        verdict = "MISSING"
    elif need_first and latest[:7] > need_first:
        verdict = "LATE"
    elif nds and min(nds) < mind:
        verdict = "SHORT"
    need_tally[verdict] += 1
    print("NEED %s | %s | %s %s | latest first design date %s (needed by %s) | min design count %s (needed %d) | %s%s" % (
        verdict, nd["spec"], tgt, per, latest or "-", need_first or "-", min(nds) if nds else 0, mind,
        nd["input"][:70], (" | missing: " + ", ".join("%s (%s)" % m for m in missing[:12])) if missing else ""))
print("NEED summary | " + " | ".join("%s %d" % kv for kv in sorted(need_tally.items())))

# =====================================================================================================================
print("--- GAP (inside each primary series' design range)")
gap_n = Counter()
for r in prim.itertuples():
    k = (r.per, r.series_id)
    if k not in data:
        continue
    obs, key, val, _ = data[k]
    if len(key) < 2:
        continue
    if r.per == "M":
        mi = key.astype("datetime64[M]").astype("int64")
        miss = np.diff(mi) - 1
        lim, unit = GAP_MONTHS, "months"
    else:
        miss = np.busday_count(key[:-1], key[1:]) - 1
        lim, unit = GAP_DAYS, "business days"
    bad = np.where(miss > lim)[0]
    if len(bad):
        gap_n[r.per] += 1
        j = bad[np.argmax(miss[bad])]
        print("GAP %s %s | runs over %d %s: %d | longest %d %s after %s | design range %s .. %s" % (
            r.per, r.series_id, lim, unit, len(bad), int(miss[j]), unit, d2s(key[j]), r.first, r.last_design))
print("GAP summary | monthly series with gaps %d | daily series with gaps %d" % (gap_n["M"], gap_n["D"]))

print("--- STALE (unchanged value runs; untouched instruments skipped)")
stale_n = Counter()
for r in prim.itertuples():
    k = (r.per, r.series_id)
    if k not in data or r.series_id in untouched or r.kind == "economics":
        continue
    val = data[k][2]
    if len(val) < 3:
        continue
    idx = np.flatnonzero(np.r_[True, val[1:] != val[:-1]])
    lens = np.diff(np.r_[idx, len(val)])
    lim = STALE_MONTHS if r.per == "M" else STALE_DAYS
    long_runs = [int(x) for x in lens if x >= lim]
    if long_runs:
        stale_n[r.per] += 1
        print("STALE %s %s | runs of %d+ unchanged values: %d | longest %d" % (r.per, r.series_id, lim, len(long_runs),
                                                                            max(long_runs)))
print("STALE summary | monthly %d | daily %d" % (stale_n["M"], stale_n["D"]))

# =====================================================================================================================
print("--- COPY")
cg = cat[cat["status"] == "copy"]
print("COPY status copy (identical arrays under %d+ instruments): %d series in %d groups" % (
    LD.COPY_MIN_CODES, len(cg), cg["copy_group"].nunique() if len(cg) else 0))
for r in cg.itertuples():
    print("COPY member %s %s %s | %s|%s" % (r.file, r.sheet, r.block, r.code, r.field))


def rnd(v):
    a = np.abs(v)
    mag = np.where(a > 0, np.floor(np.log10(np.where(a > 0, a, 1.0))), 0.0)
    sc = 10.0 ** (8 - mag)
    return np.round(v * sc) / sc


whole = defaultdict(set)
win = defaultdict(set)
inst_of = {}
for r in stored.itertuples():
    k = (r.per, r.series_id)
    if k not in data or r.series_id in untouched:
        continue
    m_ = LD.RIC_RE.match(r.code.strip("<>"))
    if m_ and m_.group(4) is not None:
        continue                    # an individual (sample) contract is SUPPOSED to equal a continuous position
    _, key, val, _ = data[k]
    inst = (LD.norm_code(r.code), r.field)
    inst_of[k] = inst
    rv = rnd(val)
    kd = key.astype("int64")
    if len(rv) >= LD.COPY_MIN_VALUES:
        whole[(r.per, hashlib.sha1(kd.tobytes() + rv.tobytes()).hexdigest())].add((inst, r.series_id))
    w = RUN_M if r.per == "M" else RUN_D
    if len(rv) < w:
        continue
    kb, vb = kd.tobytes(), rv.tobytes()
    for i in range(0, len(rv) - w + 1):
        seg = rv[i:i + w]
        if seg[0] == seg[-1] and np.all(seg == seg[0]):
            continue
        h = hashlib.sha1(kb[8 * i:8 * (i + w)] + vb[8 * i:8 * (i + w)]).digest()
        win[(r.per, h)].add(inst)
n_pairs = 0
for (per, _), members in whole.items():
    insts = {m[0] for m in members}
    if len(insts) >= 2:
        n_pairs += 1
        print("IDENTICAL whole arrays %s | %s" % (per, " = ".join(sorted(m[1] for m in members))))
pairs = Counter()
for (per, _), insts in win.items():
    if len(insts) >= 2:
        s = sorted(insts)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                pairs[(per, s[i], s[j])] += 1
print("COPY identical whole arrays between different instruments: %d groups (legit aliases possible: review)" % n_pairs)
print("COPY identical value runs (%d months / %d days) shared by different instruments: %d pairs" % (
    RUN_M, RUN_D, len(pairs)))
for (per, a, b), n in pairs.most_common(60):
    print("RUN %s | %s|%s = %s|%s | shared windows %d" % (per, a[0], a[1], b[0], b[1], n))

# =====================================================================================================================
print("--- DSDATE (month-end date convention of monthly series, design dates)")
mp = prim[prim["per"] == "M"]
for fn, g in mp.groupby("fn"):
    print("DSDATE %s | %s" % (fn, " | ".join("%s %d" % (k or "no design data", v)
                                             for k, v in sorted(Counter(g["date_rule"]).items()))))
hol_series = Counter()
for r in mp.itertuples():
    k = ("M", r.series_id)
    if k not in data:
        continue
    h = data[k][3]
    if (h > 0).any():
        hol_series[r.fn] += 1
        if r.fn == "DS" and (r.engine_id or "EDc" in r.code or "FSSc" in r.code or "FESc" in r.code or
                             r.code.startswith("EC") or "@:" in r.code):
            print("DSDATE holiday month-ends %s | US %d | UK %d | both %d (value = the previous trading day's, "
                  "unscreened)" % (r.series_id, int((h == 1).sum()), int((h == 2).sum()), int((h == 3).sum())))
print("DSDATE monthly series with at least one month-end on a US or UK holiday | " +
      " | ".join("%s %d" % kv for kv in sorted(hol_series.items())))

print("--- LABEL (monthly value vs the daily copy of the same series, design months)")
n_lab = 0
for r in mp.itertuples():
    if ("D", r.series_id) not in data or ("M", r.series_id) not in data or r.series_id in untouched:
        continue
    mo, _, mv, _ = data[("M", r.series_id)]
    do, _, dv, _ = data[("D", r.series_id)]
    pos = {d: i for i, d in enumerate(do)}
    same_day = eq_day = eq_last = 0
    offs = []
    dmon = do.astype("datetime64[M]")
    for d, v in zip(mo, mv):
        i = pos.get(d)
        if i is not None:
            same_day += 1
            eq_day += eq(v, dv[i])
        j = np.searchsorted(do, d, side="right") - 1
        if j >= 0 and dmon[j] == np.datetime64(d, "M"):
            eq_last += eq(v, dv[j])
            offs.append(int((d - do[j]).astype("int64")))
    if not offs:
        continue
    n_lab += 1
    print("LABEL %s | months %d | month date is a daily date %d | equal on that date %d | equal to the month's last "
          "daily value %d | median days from last daily date to month label %d" % (
              r.series_id, len(offs), same_day, eq_day, eq_last, int(np.median(offs))))
print("LABEL pairs checked %d" % n_lab)

# =====================================================================================================================
print("--- IDENTITY (contract identity per futures root)")
print("IDENTITY rule under test: position cN holds the N-th listed contract (by delivery month) whose roll anchor "
      "(lseg_roots.csv roll_on) is on or after the day; continuous closes alone carry no delivery month, no roll day "
      "and no listed-month information, so identity needs the L11 calendar and the sample check")
C = LD.Calendar(cal, roots)
cal_all = cal if cal is not None else pd.DataFrame(columns=["root"])
samples = defaultdict(list)
for r in stored.itertuples():
    code = r.code.strip("<>")
    m = LD.RIC_RE.match(code)
    if m and m.group(4) is not None:
        for rt, rc in roots.items():
            if m.group(1) in (rc["ric_root"], rc.get("ric_root_alt") or "#"):
                samples[rt].append((r.per, r.series_id, code))
verdicts = Counter()
for root, rc in roots.items():
    missing = []
    pm, pdl = LD.root_positions(rc, "M"), LD.root_positions(rc, "D")
    mh = [n for n in pm if ("M", LD.c_series_id(rc, n, "M")) in data]
    dh = [n for n in pdl if ("D", LD.c_series_id(rc, n, "D")) in data]
    f1 = info[("M", LD.c_series_id(rc, 1, "M"))].first if ("M", LD.c_series_id(rc, 1, "M")) in data else "-"
    print("IDENTITY %s | %s | positions with design data: monthly %d of %d (%s), daily %d of %d (%s) | c1 monthly from %s" % (
        root, rc["name"], len(mh), len(pm), ",".join(map(str, mh)) or "-", len(dh), len(pdl),
        ",".join(map(str, dh)) or "-", f1))
    missing_pos = [n for n in pm if n not in mh]
    if missing_pos:
        missing.append("monthly positions without design data: %s" % ",".join(map(str, missing_pos)))
    g_all = cal_all[cal_all["root"] == root] if len(cal_all) else cal_all
    g = C.contracts(root)
    design_c = g[g["delivery"] <= "2012-12"] if len(g) else g
    if not len(g_all):
        missing.append("contract calendar (delivery month, last trade, first notice per contract: L11 Calendar)")
        missing.append("listed months (are serial months positions?)")
        print("IDENTITY %s | calendar: none" % root)
    else:
        by_year = Counter(d[:4] for d in design_c["delivery"]) if len(design_c) else Counter()
        print("IDENTITY %s | calendar: %d contracts asked, %d listed (delivery %s .. %s) | listed months %s | contracts "
              "per design year: typical %s, min %s, max %s | anchor %s present for %d of %d design-era contracts | "
              "first notice %d | expiry %d" % (
                  root, len(g_all), len(g), g["delivery"].min() if len(g) else "-", g["delivery"].max() if len(g) else "-",
                  C.listed_months(root) or "-", Counter(by_year.values()).most_common(1)[0][0] if by_year else "-",
                  min(by_year.values()) if by_year else "-", max(by_year.values()) if by_year else "-",
                  C.anchor_col(root), int(design_c[C.anchor_col(root)].notna().sum()) if len(design_c) else 0,
                  len(design_c), int(design_c["first_notice"].notna().sum()) if len(design_c) else 0,
                  int(design_c["expiry"].notna().sum()) if len(design_c) else 0))
        if not len(g):
            missing.append("calendar rows returned no date (field names wrong or contracts not found)")
        elif design_c[C.anchor_col(root)].isna().any():
            missing.append("anchor dates for %d design-era contracts" % int(design_c[C.anchor_col(root)].isna().sum()))
        nfn = int(design_c["first_notice"].isna().sum()) if len(design_c) else 0
        if root in FND_EXPECTED and nfn:
            missing.append("first notice days for %d design-era contracts" % nfn)
        elif root not in CASH_SETTLED and nfn == len(design_c) and len(design_c):
            print("IDENTITY %s | note: no first notice day returned for any contract (none expected for this root; "
                  "confirm from the exchange rules)" % root)
    # roll rule on sample contracts (a month-end value is placed on its trading day: label or holiday -> the close
    # of the last trading day before it)
    mkt = "UK" if rc["exchange"].startswith(("LIFFE", "ICE Futures Europe")) else "US"
    agree = dis = amb = unm = unp = 0
    roll_offsets = []
    for per, sid, code in samples.get(root, []):
        obs, _, val, _ = data[(per, sid)]
        cser = {}
        for n in (pm if per == "M" else pdl):
            k = (per, LD.c_series_id(rc, n, per))
            if k in data:
                o, _, v, _ = data[k]
                cser[n] = dict(zip(o.tolist(), v.tolist()))
        last_c1 = None
        for d, v in zip(obs.tolist(), val.tolist()):
            hits = [n for n, mp_ in cser.items() if d in mp_ and eq(mp_[d], v)]
            if per == "D" and hits == [1]:
                last_c1 = d
            pred = C.position_of(root, code, LD.trading_day(d, mkt)) if len(g) else None
            if not hits:
                unm += 1
            elif len(hits) > 1:
                amb += 1
            elif pred is None:
                unp += 1
            elif hits[0] == pred:
                agree += 1
            else:
                dis += 1
        if per == "D" and last_c1 is not None and len(g):
            row = g[g["ric"] == code]
            if len(row):
                for col in ("last_trade", "first_notice", "expiry"):
                    a = row.iloc[0][col]
                    if pd.notna(a):
                        roll_offsets.append("%s %s%+d bd" % (code, col, int(np.busday_count(
                            np.datetime64(a.date(), "D"), np.datetime64(last_c1, "D")))))
    ns = len(samples.get(root, []))
    print("IDENTITY %s | sample contracts stored %d | observations: agree %d, disagree %d, ambiguous %d, not matched to "
          "any position %d, rule cannot say %d%s" % (root, ns, agree, dis, amb, unm, unp,
                                                     (" | last day as c1 vs anchor: " + "; ".join(roll_offsets))
                                                     if roll_offsets else ""))
    if ns == 0:
        missing.append("roll rule check (sample contracts matched to the continuous series: L11 Contract sample)")
    elif agree + dis < MIN_MATCH or agree < AGREE_SHARE * (agree + dis):
        missing.append("roll rule not confirmed (agree %d of %d matched)" % (agree, agree + dis))
    # depth for the spec's legs
    need = rc.get("need") or ""
    c1k = ("M", LD.c_series_id(rc, 1, "M"))
    if "curve12" in need and c1k in data and len(g):
        okm = beyond = nolist = unk = 0
        first_ok = None
        mmax = max(mh) if mh else 0
        dset = set(g["delivery"])
        for d in data[c1k][0].tolist():
            t = pd.Period(d, "M")
            d = LD.trading_day(d, mkt)
            fr = g[pd.PeriodIndex(g["delivery"], freq="M") >= t + FRONT_MIN]
            if not len(fr):
                unk += 1
                continue
            far = str(pd.Period(fr.iloc[0]["delivery"], "M") + FAR_MONTHS)
            if far not in dset:
                nolist += 1
                continue
            p = C.position_of(root, g[g["delivery"] == far].iloc[0]["ric"], d)
            if p is None:
                unk += 1
            elif p <= mmax and ("M", LD.c_series_id(rc, p, "M")) in data:
                okm += 1
                first_ok = first_ok or d
            else:
                beyond += 1
        print("IDENTITY %s | curve12 depth: design months with the far leg inside the pulled positions %d | beyond "
              "the pulled depth %d | far contract not listed %d | unknown %d | first covered month %s" % (
                  root, okm, beyond, nolist, unk, mon(first_ok) if first_ok else "-"))
        if beyond:
            missing.append("depth: %d design months need a position beyond %d" % (beyond, mmax))
    if "strip8" in need and c1k in data and len(g):
        q = g[g["delivery"].str[5:7].isin(["03", "06", "09", "12"])]
        okm = okd = beyond = unk = 0
        dmax = set(dh)
        for d in data[c1k][0].tolist():
            d = LD.trading_day(d, mkt)
            ql = q[q[C.anchor_col(root)] >= pd.Timestamp(d)]
            if len(ql) < STRIP_N:
                unk += 1
                continue
            ps = [C.position_of(root, x, d) for x in ql["ric"].iloc[:STRIP_N]]
            if any(p is None for p in ps):
                unk += 1
                continue
            if max(ps) <= (max(mh) if mh else 0):
                okm += 1
            else:
                beyond += 1
            if set(ps) <= dmax:
                okd += 1
        print("IDENTITY %s | strip8: design month-ends where the first %d quarterly contracts sit inside the monthly "
              "positions %d (beyond %d, unknown %d); inside the DAILY positions pulled %d" % (
                  root, STRIP_N, okm, beyond, unk, okd))
        if beyond:
            missing.append("depth: %d month-ends need a monthly position beyond %d" % (beyond, max(mh) if mh else 0))
    if not missing:
        verdict = "COMPLETE"
    elif any("calendar" in m for m in missing) and ns == 0:
        verdict = "NONE"
    else:
        verdict = "PARTIAL"
    verdicts[verdict] += 1
    print("IDENTITY VERDICT %s | %s | missing: %s" % (root, verdict, "; ".join(missing) or "nothing"))
print("IDENTITY summary | " + " | ".join("%s %d" % kv for kv in sorted(verdicts.items())))

# =====================================================================================================================
print("--- PROBE (L11 identity probe and calendar test: which guesses returned dates)")
rawp = os.path.join(WORK, "lseg", "calendar_raw.pkl")
raw = pd.read_pickle(rawp) if os.path.exists(rawp) else pd.DataFrame(columns=["sheet"])
pr = raw[raw["sheet"].isin(["Identity probe", "Calendar test", "Calendar"])].copy() if len(raw) else raw
if len(pr):
    pr.loc[pr["sheet"] == "Calendar", "block"] = "all blocks"        # the full calendar: one line per field
for (sh, blk, fld), g in (pr.groupby(["sheet", "block", "field"], sort=False) if len(pr) else []):
    errs = g.loc[g["date"].isna() & (g["error"] != ""), "error"]
    print("PROBE %s %s %s | contracts %d | with a date %d | first error %s" % (
        sh, blk, fld, len(g), int(g["date"].notna().sum()), errs.iloc[0][:60] if len(errs) else "-"))
ip = cat[cat["sheet"] == "Identity probe"]
for r in ip.itertuples():
    print("PROBE series %s %s | %s|%s | %s | design count %d | %s" % (r.file, r.block, r.code, r.field, r.status,
                                                                      r.n_design, (r.error or r.header)[:60]))
if not len(pr) and not len(ip):
    print("PROBE none (L11 not read yet)")

# =====================================================================================================================
print("--- ENGINE (series mapped to engine ids)")
for r in prim[prim["engine_id"] != ""].sort_values(["engine_id", "per"]).itertuples():
    print("ENGINE %s | %s %s | %s | first design %s | design count %d | %s" % (
        r.engine_id, r.per, r.series_id, r.engine_role[:50], r.first if r.n_design else "-", r.n_design, r.date_rule))
print("--- SEALED (structure only, from the catalog; no sealed value is opened)")
for f, g in stored.groupby("file", sort=False):
    print("SEALED %s | series with observations after 2010 %d | sealed observations %d" % (
        f, int((g["n_sealed"] > 0).sum()), int(g["n_sealed"].sum())))
print("=== END === %.0fs" % (time.time() - T0))
