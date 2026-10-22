"""Events, cells, calls and outcomes for the three triages (rules: triage/rules.py).

  detect()    walks the monthly panel once, oldest month first, and finds every event of every triage with only
              what was known at that month-end (backend requirements, the trigger, the 10 most similar stocks).
  outcome     total return from the entry day (open of the first trading day after the month-end) month by month for
              12 months (cache/tri/returns), a company that left the exchange valued at its last close (else -30%)
              and held as cash after; open events to the latest close (daily mark). Same for the similar stocks and
              the index ETF.
  owners      13F conviction owners from the last quarter whose 45-day deadline had passed by the month-end; those
              that first report it for the quarter of the event (filed later, by the deadline) can upgrade a Watch.
              Top performer owners: ranked walk-forward on events whose year had ended.
  insiders    Form 4 open-market trades filed in the 180 days up to the month-end.
  score()     cells, score, call; writes cache/tri/out/<kind>.json.gz.
"""
import os
import statistics as st
from collections import defaultdict, deque
from datetime import date, timedelta

from qs.backtest_support import read_json
from qs.btprices import holding_return

from . import panel as PN
from . import rules as R
from . import paths as P  # noqa: F401  (tests patch the paths)

KINDS = tuple(R.KINDS)
N_SIMILAR = 10
CAP = 5.0                     # any single 12-month return capped at +500% in averages


def plus(d, n):
    return (date.fromisoformat(d) + timedelta(days=n)).isoformat()


# ------------------------------------------------------------------ backend requirements
def leverage(rec, thr):
    """(ok, value, note) - net debt / EBITDA as the screens test it: net cash passes; net debt with no EBITDA fails;
    EBIT stands in when depreciation isn't tagged (stricter)."""
    nd, ebitda, ebit = rec.get("nd"), rec.get("ebitda"), rec.get("ebit")
    if nd is None:
        return False, None, "no balance sheet"
    if not rec.get("debtok") and nd > 0:
        return False, None, "no standard debt tag"
    if nd <= 0:
        return True, None, "net cash"
    if ebitda is None and ebit is not None and ebit > 0:
        return nd / ebit <= thr, nd / ebit, "net debt / EBIT"
    if ebitda is None:
        return False, None, "EBITDA unavailable"
    if ebitda <= 0:
        return False, None, "net debt with no EBITDA"
    return nd / ebitda <= thr, nd / ebitda, ""


def backend(kind, rec):
    """[] when the company is covered by this triage at this month-end, else the reasons it isn't."""
    k = R.KINDS[kind]
    b = k["backend"]
    why = []
    if k["universe"] not in (rec.get("u") or []):
        why.append("industry outside this triage")
    if (rec.get("yrs") or 0) < b["min_years"]:
        why.append(f"fewer than {b['min_years']} years of SEC data")
    if rec.get("ylf") is None or rec["ylf"] > 1.6:
        why.append("latest annual report older than 1.6 years")
    mc = rec.get("mc")
    if mc is None:
        why.append("market cap not verified")
    else:
        if mc < b["min_mcap"]:
            why.append("market cap below the minimum")
        if b["max_mcap"] and mc > b["max_mcap"]:
            why.append("market cap above the maximum")
    if (rec.get("adv") or 0) < b["min_adv"]:
        why.append("trading volume below the minimum")
    if b["min_revenue"] and (rec.get("revfy") or 0) < b["min_revenue"]:
        why.append("revenue below the minimum")
    if not leverage(rec, b["max_lev"])[0]:
        why.append("leverage above the cap or not verifiable")
    return why


# ------------------------------------------------------------------ valuation yields
def yld(kind, rec):
    ev = rec.get("ev")
    if not ev or ev <= 0:
        return None
    if kind == "emerging":
        base = rec.get("ebit") if (rec.get("das") or 0) >= 0.5 else rec.get("ebitda")
        if base is None:
            base = rec.get("ebit")
    else:
        base = rec.get("ebit")
    return None if base is None else base / ev


def pctl(vals, v):
    """Share of vals below v (ties count half)."""
    if not vals:
        return None
    lo = sum(1 for x in vals if x < v)
    eq = sum(1 for x in vals if x == v)
    return (lo + 0.5 * eq) / len(vals)


def peer_groups(comp, kind):
    """{sic prefix: [yields]} for every 4-, 3- and 2-digit industry code (companies of $100M+ with a yield)."""
    g = defaultdict(list)
    for c, r in comp.items():
        if (r.get("mc") or 0) < R.PEER_MIN_MCAP:
            continue
        y = yld(kind, r)
        s = r.get("sic") or ""
        if y is None or len(s) < 2:
            continue
        for n in (4, 3, 2):
            g[s[:n]].append((c, y))
    return g


def peer_pctl(groups, c, rec, y):
    s = rec.get("sic") or ""
    for n in (4, 3, 2):
        mem = [v for cc, v in groups.get(s[:n], []) if cc != c]
        if len(mem) >= R.PEER_MIN:
            return pctl(mem, y), n, len(mem)
    return None, None, 0


# ------------------------------------------------------------------ similar stocks
def _ranks(vals):
    idx = sorted(range(len(vals)), key=lambda k: vals[k])
    r = [0.0] * len(vals)
    for pos, k in enumerate(idx):
        r[k] = pos / max(1, len(vals) - 1)
    return r


def _sub_ranks(vals):
    have = [i for i, v in enumerate(vals) if v is not None]
    out = [None] * len(vals)
    for i, rk in zip(have, _ranks([vals[i] for i in have])):
        out[i] = rk
    return out


def similar_pool(comp):
    """[(cik, rank mc, rank r12, rank ey, mc, r12, ey)] of US companies of $100M+ with a price (12-month change and
    earnings yield may be missing: the first year of the grid has no 12-month change)."""
    rows = [(c, r["mc"], r.get("r12"), (r["ebit"] / r["ev"]) if (r.get("ebit") is not None and r.get("ev")) else None)
            for c, r in comp.items() if (r.get("mc") or 0) >= R.PEER_MIN_MCAP and r.get("px")]
    if len(rows) <= N_SIMILAR:
        return []
    rm, rr, re_ = _ranks([x[1] for x in rows]), _sub_ranks([x[2] for x in rows]), _sub_ranks([x[3] for x in rows])
    return [(rows[i][0], rm[i], rr[i], re_[i], rows[i][1], rows[i][2], rows[i][3]) for i in range(len(rows))]


def nearest(pool, c, rec, busy):
    """The 10 closest companies on market cap, 12-month price change and earnings yield (percentile ranks that day;
    a measure the company lacks is skipped, one a candidate lacks counts as the largest gap), leaving out the company
    itself and companies with an event of the same triage in the last 6 months."""
    if not pool or rec.get("mc") is None:
        return []
    pm = sum(1 for x in pool if x[4] < rec["mc"]) / len(pool)
    r12s = [x[5] for x in pool if x[5] is not None]
    pr = (sum(1 for v in r12s if v < rec["r12"]) / len(r12s)) if (rec.get("r12") is not None and r12s) else None
    ey = (rec["ebit"] / rec["ev"]) if (rec.get("ebit") is not None and rec.get("ev")) else None
    eys = [x[6] for x in pool if x[6] is not None]
    pe = (sum(1 for v in eys if v < ey) / len(eys)) if (ey is not None and eys) else None
    scored = []
    for x in pool:
        if x[0] == c or x[0] in busy:
            continue
        dist = abs(x[1] - pm)
        for mine, theirs in ((pr, x[2]), (pe, x[3])):
            if mine is not None:
                dist += abs(theirs - mine) if theirs is not None else 1.0
        scored.append((dist, x[0]))
    scored.sort()
    return [k for _, k in scored[:N_SIMILAR]]


# ------------------------------------------------------------------ detection (one pass over the panel)
def detect(months, load=PN.load, log=print):
    """{kind: [event, ...]} - events need the previous month's trigger state, so the first month only primes it."""
    out = {k: [] for k in KINDS}
    hist = {k: defaultdict(lambda: deque(maxlen=R.OWN_PAST_MONTHS)) for k in KINDS if k != "hidden"}
    state = {k: {} for k in KINDS}               # cik -> trigger held at the previous month-end (True / False)
    last = {k: {} for k in KINDS}                # cik -> month index of its latest event
    ebit_back = deque(maxlen=13)                 # {cik: TTM EBIT} of the last 13 month-ends (profit trend)
    for i, ym in enumerate(months):
        p = load(ym) or {}
        comp = p.get("companies") or {}
        if not comp:
            ebit_back.append({})
            continue
        pool = similar_pool(comp)
        year_ago = ebit_back[0] if len(ebit_back) == 13 else {}
        new_state = {k: {} for k in KINDS}
        for kind in KINDS:
            groups = peer_groups(comp, kind) if kind != "hidden" else None
            busy = {c for c, j in last[kind].items() if i - j < R.COOLDOWN_MONTHS}
            evs = []
            for c, rec in comp.items():
                if kind == "hidden":
                    trig = None if rec.get("dd") is None else rec["dd"] <= R.HIDDEN_FALL
                    info = {"dd": rec.get("dd")}
                else:
                    y = yld(kind, rec)
                    past = list(hist[kind][c]) if c in hist[kind] else []
                    p_own = pctl(past, y) if (y is not None and len(past) >= R.OWN_PAST_MIN) else None
                    p_peer, lvl, npeer = peer_pctl(groups, c, rec, y) if y is not None else (None, None, 0)
                    trig = None if (p_own is None and p_peer is None) else \
                        ((p_own or 0) >= R.CHEAP_PCTL or (p_peer or 0) >= R.CHEAP_PCTL)
                    info = {"y": y, "p_own": p_own, "n_own": len(past), "p_peer": p_peer, "peer_lvl": lvl,
                            "n_peer": npeer, "y_med": st.median(past) if past else None}
                    if y is not None:
                        hist[kind][c].append(y)
                new_state[kind][c] = trig
                if not trig or state[kind].get(c) is not False or c in busy:
                    continue
                if backend(kind, rec):
                    continue
                evs.append((c, rec, info))
            for c, rec, info in evs:
                last[kind][c] = i
            busy = {c for c, j in last[kind].items() if i - j < R.COOLDOWN_MONTHS}
            for c, rec, info in evs:
                sim = nearest(pool, c, rec, busy)
                out[kind].append({"id": f"{c}_{ym}", "cik": c, "ym": ym, "i": i, "d": p["d"], "e": p["e"],
                                  "rec": rec, "info": info, "ebit_1y": year_ago.get(c), "sim": sim,
                                  "sim_sym": {k: comp[k].get("sym") for k in sim}})
        state = new_state
        ebit_back.append({c: r.get("ebit") for c, r in comp.items()})
        if (i + 1) % 12 == 0 or i == len(months) - 1:
            log(f"  events through {ym}: " + ", ".join(f"{k} {len(v)}" for k, v in out.items()))
    return out


# ------------------------------------------------------------------ returns
class Returns:
    """Month-by-month returns from cache/tri/returns, plus the open month marked to the latest close."""

    def __init__(self, months, grid_e, mark=None, opens=None, splits=None, divs=None):
        self.months = months
        self.e = grid_e                                     # ym -> entry day
        self.r = {ym: read_json(os.path.join(P.RETURNS, f"{ym}.json.gz")) for ym in months}
        self.idx = read_json(os.path.join(P.RETURNS, "index.json.gz")) or {}
        self.mark, self.opens = mark or {}, opens or {}
        self.splits, self.divs = splits or {}, divs or {}

    def _partial(self, sym, ym):
        """Open of the month's entry day to the latest close (None if either is missing)."""
        cl = (self.mark.get("closes") or {}).get(sym)
        op = self.opens.get(sym)
        if not cl or not op or not self.mark.get("day") or self.mark["day"] < self.e.get(ym, "9"):
            return None
        return holding_return(op, cl, self.splits.get(sym) or [], self.divs.get(sym) or [], self.e[ym], self.mark["day"])

    def path(self, key, sym, i0, n=12, index=False):
        """([cumulative return after 0..k months], complete?, last day, stopped?) from the entry of month i0."""
        vals, cum, exited, stopped = [0.0], 1.0, False, None
        last_day = self.e.get(self.months[i0]) if i0 < len(self.months) else None
        for k in range(n):
            i = i0 + k
            if i >= len(self.months):
                return vals, False, last_day, stopped
            ym = self.months[i]
            rets = (self.idx.get(ym) if index else self.r.get(ym))
            if rets is None:
                part = 0.0 if exited else self._partial(sym, ym)
                if part is not None and self.mark.get("day"):
                    vals.append(cum * (1 + part) - 1)
                    last_day = self.mark["day"]
                return vals, False, last_day, stopped
            if exited:
                r = 0.0
            else:
                v = rets.get(str(key)) if not index else rets.get(key)
                if index:
                    r = v if v is not None else 0.0
                elif v is None:
                    if k == 0:
                        return None, False, None, None           # no entry price
                    r, exited, stopped = 0.0, True, ym
                else:
                    r = v[0]
                    if v[1] != "ok":
                        exited, stopped = True, ym
            cum *= 1 + r
            vals.append(cum - 1)
            nxt = self.months[i + 1] if i + 1 < len(self.months) else None
            last_day = self.e.get(nxt) if nxt else last_day
        return vals, True, last_day, stopped

    def series(self, key, sym, i0, ym_set):
        """{ym: monthly return} for the holding months of an event (calendar-time portfolios)."""
        out = {}
        for k in range(12):
            i = i0 + k
            if i >= len(self.months):
                break
            ym = self.months[i]
            rets = self.r.get(ym)
            if rets is None:
                break
            v = rets.get(str(key))
            out[ym] = v[0] if v else 0.0
            if v is None or v[1] != "ok":
                break
        return out


# ------------------------------------------------------------------ 13F owners
def quarter_before(d):
    y = int(d[:4])
    ends = sorted(f"{yy}-{mm:02d}-{dd}" for yy in (y, y - 1) for mm, dd in ((12, 31), (9, 30), (6, 30), (3, 31)))
    return [x for x in ends if plus(x, 45) <= d][-1]


def quarter_of(d):
    y, m = int(d[:4]), int(d[5:7])
    q = (m - 1) // 3
    return f"{y}-{3 * q + 3:02d}-{[31, 30, 30, 31][q]}"


class Owners:
    def __init__(self, rows, through, first_day=None):
        self.by_cik = defaultdict(list)
        self.names = {}
        for r in rows:
            fc, nm, per, fd, cik, w = r
            self.by_cik[str(cik)].append((fc, nm, per, fd, w))
            self.names[fc] = nm
        self.through, self.first = through, first_day

    def funds(self, cik, d):
        """None when the 13F data doesn't cover the date yet, else {'list', 'later', 'before', 'after', 'pending'}."""
        qb, qa = quarter_before(d), quarter_of(d)
        if self.through is None or self.through < plus(qb, 45) or (self.first and self.first > plus(qb, 1)):
            return None
        best, later = {}, {}
        for fc, nm, per, fd, w in self.by_cik.get(str(cik), []):
            if per == qb and fd <= d and (fc not in best or w > best[fc][2]):
                best[fc] = (fc, nm, w, per)
        for fc, nm, per, fd, w in sorted(self.by_cik.get(str(cik), []), key=lambda t: t[3]):
            if per == qa and d < fd <= plus(qa, 45) and fc not in best and fc not in later:
                later[fc] = (fc, nm, w, fd)
        return {"before": qb, "after": qa, "pending": self.through < plus(qa, 45),
                "list": sorted(best.values(), key=lambda t: -t[2]), "later": list(later.values())}


def top_performers(events_all):
    """as_of(day) -> {filer_cik: (rank, score, hits, plays, rate, conc)} from events whose 12 months had ended by
    that day (all three triages). Half quality (conviction-weighted, shrunk hit rate x concentration), half number of
    hits, each a percentile rank among filers with plays in 5+ companies. Hit = beat its similar stocks by 10+ points."""
    done = sorted((x for x in events_all if x.get("y") is not None and x.get("fund") and x.get("end")),
                  key=lambda x: x["end"])
    cache = {}

    def pct_rank(vals):
        order = sorted(vals)
        return [(sum(1 for o in order if o < v) + 0.5 * sum(1 for o in order if o == v)) / len(order) for v in vals]

    def as_of(d):
        if d in cache:
            return cache[d]
        plays = defaultdict(list)
        for x in done:
            if x["end"] > d:
                break
            hit = x["y"] >= R.TOP_HIT
            for fc, _, w, _ in x["fund"]["list"] + x["fund"]["later"]:
                plays[fc].append((w, hit, x["cik"]))
        allp = [p for v in plays.values() for p in v]
        elig = {fc: v for fc, v in plays.items() if len({c for _, _, c in v}) >= R.TOP_MIN_COMPANIES}
        if not elig:
            cache[d] = {}
            return cache[d]
        cap = R.TOP_WEIGHT_CAP
        base = sum(min(w, cap) * h for w, h, _ in allp) / sum(min(w, cap) for w, _, _ in allp)
        wbar = sum(min(w, cap) for w, _, _ in allp) / len(allp)
        med = lambda v: sorted(v)[len(v) // 2]  # noqa: E731
        med_all = med([med([w for w, _, _ in v]) for v in elig.values()])
        stats = []
        for fc, v in elig.items():
            sw = sum(min(w, cap) for w, _, _ in v)
            sh = sum(min(w, cap) * h for w, h, _ in v)
            rate = (sh + R.TOP_PRIOR_PLAYS * wbar * base) / (sw + R.TOP_PRIOR_PLAYS * wbar)
            conc = min(med([w for w, _, _ in v]) / med_all, R.TOP_CONC_CAP) if med_all else 1.0
            stats.append((fc, rate, conc, sum(h for _, h, _ in v), len(v)))
        q = pct_rank([r * c for _, r, c, _, _ in stats])
        n = pct_rank([h for _, _, _, h, _ in stats])
        scored = sorted(((t[0], (qq + nn) / 2, t[1], t[2], t[3], t[4]) for t, qq, nn in zip(stats, q, n)),
                        key=lambda t: (-t[1], t[0]))[:R.TOP_N]
        cache[d] = {fc: (i + 1, sc, hits, k, rate, conc) for i, (fc, sc, rate, conc, hits, k) in enumerate(scored)}
        return cache[d]
    return as_of


# ------------------------------------------------------------------ insiders
def insider_view(trades, d, mcap):
    """Net open-market buying minus discretionary selling filed in the 180 days up to d."""
    lo = plus(d, -R.INSIDER_DAYS)
    win = [t for t in trades if lo < t[1] <= d]
    buy = sum(t[3] for t in win if t[2] == "P")
    sell = sum(t[3] for t in win if t[2] == "S")
    plan = sum(t[3] for t in win if t[2] in ("Splan", "Sex"))
    net = buy - sell
    mat = max(R.INSIDER_MIN_USD, R.INSIDER_MIN_MCAP_SHARE * (mcap or 0))
    big = max((t for t in win if t[2] in ("P", "S")), key=lambda t: t[3], default=None)
    return {"buy": buy, "sell": sell, "plan": plan, "net": net, "material": mat, "n": len(win), "largest": big,
            "colour": "g" if net >= mat else "r" if net <= -mat else "n"}
