# Excerpts from tools/equity/wrds/eq_scorecard.py for the independent code check

Module constants used below: M_FIRST, M_LAST = 201101, 202512; MIN_RESULT, MIN_STATS, NW_LAGS = 36, 60, 3; POS_LO, POS_HI, VAL_MIN = 5, 150, 100e6; FUND_TNA_MIN = 15.0; TIER_RECORD, STYLE_CAP, TIER_EXPLICIT, CONTROL_N, SEED = 30, 8, 10, 10, 20261117; FY0, FY1 = 2010, 2025; MI_CRSP = month index of 2009-06. Month index mi = year*12 + month - 1.

## E1. June peer groups (Peers._form)
```python
    def _form(self, fy, bmt):
        p = self.panel
        js = self._j(fy * 12 + 5)       # size at the end of June of the formation year
        jf = self._j(fy * 12 + 5)       # share type and exchange at the end of June
        jm = self._j(fy * 12 + 5)       # momentum: the twelve months June (fy-1) .. May (fy)
        if jm - 12 < 0 or js >= p.nm:
            return
        cap = p.C[:, js]
        mom = np.prod(1.0 + p.R[:, jm - 12:jm], axis=1) - 1.0
        bmv = bmt[:, fy - FY0]
        u = p.COM[:, jf] & np.isfinite(cap) & (cap > 0) & np.isfinite(bmv) & (bmv > 0) & np.isfinite(mom)
        ny = u & p.NY[:, jf]
        if ny.sum() < 5:
            return
        bps = np.percentile(cap[u], [20, 40, 60, 80])
        idx = np.where(u)[0]
        s = np.searchsorted(bps, cap[idx], side="left")
        g = np.full(len(idx), -1, dtype="int64")
        ids = p.perm[idx]
        for si in range(5):
            a = np.where(s == si)[0]
            if not len(a):
                continue
            b = _fifths(bmv[idx[a]], ids[a])
            for bi in range(5):
                c = a[b == bi]
                if not len(c):
                    continue
                m = _fifths(mom[idx[c]], ids[c])
                g[c] = si * 25 + bi * 5 + m
        self.G[idx, fy - FY0] = g
        # value-weighted group returns July fy .. June fy+1 (weights: previous month-end market value)
        gg = self.G[:, fy - FY0].astype("int64")
        for mi in range(fy * 12 + 6, fy * 12 + 18):
            j = self._j(mi)
            if j <= 0 or j >= p.nm:
                continue
            r, w = p.R[:, j], p.C[:, j - 1]
            v = (gg >= 0) & np.isfinite(r) & np.isfinite(w) & (w > 0)
            sw = np.bincount(gg[v], weights=w[v], minlength=125)
            swr = np.bincount(gg[v], weights=w[v] * r[v], minlength=125)
            with np.errstate(invalid="ignore", divide="ignore"):
                self.B[:, j] = np.where(sw > 0, swr / sw, np.nan)
```

## E2. Per-quarter aggregate SQL and its pull
```python
AGG_SQL = """/* eqsc agg %(lo)s %(hi)s */
with h as (
  select mgrno, rdate, cusip, sum(shares)::float8 as sh, sum(shares * coalesce(prc, 0))::float8 as fv
  from tfn.s34
  where fdate = rdate and shares > 0 and rdate between '%(lo)s' and '%(hi)s'
  group by mgrno, rdate, cusip),
n as (
  select distinct cusip, permno, namedt, coalesce(nameenddt, date '2099-12-31') as ne
  from crsp.stocknames_v2 where cusip is not null),
k as (
  select distinct on (h.mgrno, h.rdate, h.cusip) h.mgrno, h.rdate, h.sh, h.fv, n.permno
  from h left join n on n.cusip = h.cusip and h.rdate between n.namedt and n.ne
  order by h.mgrno, h.rdate, h.cusip, n.permno),
p as (
  select permno, yyyymm, abs(mthprc)::float8 as px from crsp.msf_v2
  where mthcaldt between '%(lo)s' and '%(hi)s' and mthprc is not null and mthprc <> 0)
select k.mgrno, k.rdate, sum(k.fv) as fv_all,
  sum(case when p.px is not null then k.fv else 0 end) as fv_used,
  count(distinct case when p.px is not null then k.permno end) as npos,
  sum(case when p.px is not null then k.sh * p.px else 0 end) as val
from k left join p on p.permno = k.permno
  and p.yyyymm = (extract(year from k.rdate) * 100 + extract(month from k.rdate))::int
group by k.mgrno, k.rdate"""


def pull_agg(sql, save, out, data, budget=9000):
    have, step, st, t0 = _runner(save, out, data, budget)
    for y in _hyears():
        lo, hi = _hrange(y)
        step("eq_sc_agg_%d" % y, lambda lo=lo, hi=hi: sql(AGG_SQL % {"lo": lo, "hi": hi}))
    _done(out, "pull_agg", st, t0)
```

## E3. Tier rule (section 7)
```python
def _tiers(inv):
    """Registration section 7. inv: list of dicts with id, grade, own_docs, months, score, style, explicit_*."""
    def num(x, d):
        return d if x is None or (isinstance(x, float) and not np.isfinite(x)) else x
    elig = [p for p in inv if p["grade"] in ("A", "B", "F") and p["own_docs"] >= 1 and p["months"] >= MIN_STATS]
    sc = sorted([p for p in elig if np.isfinite(p["score"])], key=lambda p: (-p["score"], -p["own_docs"], p["id"]))
    rec, per = [], {}
    for p in sc:
        if len(rec) >= TIER_RECORD:
            break
        if per.get(p["style"], 0) > STYLE_CAP:
            continue
        rec.append(p["id"])
        per[p["style"]] = per.get(p["style"], 0) + 1
    ex = [p for p in inv if p.get("ran_money") == "yes" and p.get("role", "investor") == "investor"
          and p["id"] not in rec]
    ex = sorted(ex, key=lambda p: (-num(p.get("explicit_max"), -1e9), -num(p.get("explicit_mean"), -1e9),
                                   -p["own_docs"], p["id"]))
    exp = [p["id"] for p in ex[:TIER_EXPLICIT]]
    a = set(rec) | set(exp)
    pool = sorted(p["id"] for p in elig if p["id"] not in a)
    ctrl = sorted(random.Random(SEED).sample(pool, CONTROL_N)) if len(pool) > CONTROL_N else list(pool)
    b = sorted(p["id"] for p in inv if p["id"] not in a and p["id"] not in set(ctrl))
    return {"record": rec, "explicit": exp, "control": ctrl, "B": b, "eligible": len(elig)}
```

## E4. CUSIP-to-CRSP matching at the quarter-end
```python
def _positions(h, cus, panel):
    """Matched positions per filer and quarter (first versions; CUSIP valid at the quarter-end; CRSP price at the
    quarter-end) and per filing the filed and used value."""
    h = h[h.cusip.notna() & h.mgrno.notna()].copy()
    h["cusip"] = h.cusip.astype(str)
    h["mgrno"] = h.mgrno.astype("int64")
    h["rdate"] = pd.to_datetime(h.rdate)
    h["q"] = _q_of(h.rdate)
    h["fv"] = h.shares.astype(float) * pd.to_numeric(h.prc, errors="coerce").abs().fillna(0.0).to_numpy()
    g = h.groupby(["mgrno", "q", "cusip"], as_index=False).agg(sh=("shares", "sum"), fv=("fv", "sum"),
                                                              rdate=("rdate", "first"))
    fil = g.groupby(["mgrno", "q"], as_index=False).agg(fv_all=("fv", "sum"))
    c = cus[cus.cusip.notna() & cus.permno.notna()].copy()
    c["cusip"] = c.cusip.astype(str)
    c["namedt"] = pd.to_datetime(c.namedt, errors="coerce").fillna(pd.Timestamp("1900-01-01"))
    c["nameenddt"] = pd.to_datetime(c.nameenddt, errors="coerce").fillna(pd.Timestamp("2099-12-31"))
    m = g.merge(c[["cusip", "permno", "namedt", "nameenddt"]], on="cusip", how="inner")
    m = m[(m.rdate >= m.namedt) & (m.rdate <= m.nameenddt)]
    m = m.sort_values(["mgrno", "q", "cusip", "permno"]).drop_duplicates(["mgrno", "q", "cusip"])
    ri, ok = panel.rows(m.permno.to_numpy())
    px = panel.at(panel.P, ri, ok, _qend_mi(m.q.to_numpy()))
    m = m.assign(px=px)
    m = m[np.isfinite(m.px) & (m.px > 0)]
    m = m.assign(val=m.sh * m.px, permno=m.permno.astype("int64"))
    pos = m.groupby(["mgrno", "q", "permno"], as_index=False).agg(val=("val", "sum"), fv=("fv", "sum"))
    used = pos.groupby(["mgrno", "q"], as_index=False).agg(fv_used=("fv", "sum"))
    fil = fil.merge(used, on=["mgrno", "q"], how="left")
    fil["fv_used"] = fil.fv_used.fillna(0.0)
    return pos[["mgrno", "q", "permno", "val"]], fil
```

## E5. Entry month and buy-and-hold months
```python
def _q_of(d):
    d = pd.to_datetime(d)
    return (d.dt.year * 4 + (d.dt.month - 1) // 3).astype("int64").to_numpy()


def _qend_mi(q):
    q = np.asarray(q)
    return (q // 4) * 12 + 3 * (q % 4) + 2


def _entry_mi(q):
    """Month in which the 45-day deadline of quarter q falls (holdings enter at its close)."""
    y, k = divmod(int(q), 4)
    d = pd.Timestamp(y, 3 * k + 3, 1) + pd.offsets.MonthEnd(0) + pd.Timedelta(days=45)
    return d.year * 12 + d.month - 1

def _hold(pos, em, panel, peers):
    """Buy and hold of one quarter's positions. pos: bk, permno, w (sums to 1 per book), h (months held).
    Returns per book and record month: return, weight share without a return, peer-adjusted return, weight share
    with a peer group."""
    if not len(pos):
        return []
    ri, ok = panel.rows(pos.permno.to_numpy())
    w0, h = pos.w.to_numpy(float), pos.h.to_numpy()
    codes, books = pd.factorize(pos.bk, sort=True)
    cum = np.ones(len(pos))
    res = []
    for k in range(int(h.max())):
        mi = em + k
        if mi > MI_LAST:
            break
        r = panel.at(panel.R, ri, ok, mi)
        miss = ~np.isfinite(r)
        rr = np.where(miss, 0.0, r)
        if mi >= MI_FIRST:
            act = h >= k
            g = peers.group(ri, ok, mi)
            b = peers.bench(g, mi)
            pm = act & ~miss & np.isfinite(b)
            w = w0 * cum
            nb = len(books)
            sw = np.bincount(codes[act], weights=w[act], minlength=nb)
            swr = np.bincount(codes[act], weights=(w * rr)[act], minlength=nb)
            swm = np.bincount(codes[act], weights=(w * miss)[act], minlength=nb)
            swp = np.bincount(codes[pm], weights=w[pm], minlength=nb)
            swd = np.bincount(codes[pm], weights=(w * (rr - np.where(pm, b, 0.0)))[pm], minlength=nb)
            live = np.bincount(codes[act], minlength=nb) > 0
            with np.errstate(invalid="ignore", divide="ignore"):
                res.append(pd.DataFrame({"bk": np.asarray(books)[live], "mi": mi, "ret": (swr / sw)[live],
                                         "miss": (swm / sw)[live],
                                         "pa": np.where(swp > 0, swd / swp, np.nan)[live],
                                         "pash": np.where(sw > 0, swp / sw, np.nan)[live]}))
        cum = cum * (1.0 + rr)
    return res
```

## E6. Fund share-class combination
```python
def _fund_months(fret, sty):
    """Class-months with return, start-of-month assets (previous month-end TNA) and objective code in force."""
    f = fret.copy()
    f["crsp_fundno"] = f.crsp_fundno.astype("int64")
    d = pd.to_datetime(f.caldt)
    f["mi"] = (d.dt.year * 12 + d.dt.month - 1).to_numpy()
    f = f.drop_duplicates(["crsp_fundno", "mi"]).sort_values(["crsp_fundno", "mi"]).reset_index(drop=True)
    pf, pm = f.crsp_fundno.shift(1), f.mi.shift(1)
    f["w"] = np.where((pf == f.crsp_fundno) & (pm == f.mi - 1), f.mtna, np.nan)
    f["dt"] = pd.to_datetime(_ym(f.mi).astype(str), format="%Y%m") + pd.offsets.MonthEnd(0)
    s = sty.copy()
    s["crsp_fundno"] = s.crsp_fundno.astype("int64")
    s["begdt"] = pd.to_datetime(s.begdt, errors="coerce")
    s["enddt"] = pd.to_datetime(s.enddt, errors="coerce").fillna(pd.Timestamp("2099-12-31"))
    s = s.dropna(subset=["begdt"]).sort_values("begdt")
    f = pd.merge_asof(f.sort_values("dt"), s[["crsp_fundno", "begdt", "enddt", "crsp_obj_cd"]],
                      left_on="dt", right_on="begdt", by="crsp_fundno", direction="backward")
    code = np.where(f.enddt >= f.dt, f.crsp_obj_cd.fillna("").astype(str), "")
    f["ed"] = pd.Series(code).str.startswith("ED").to_numpy()
    return f.drop(columns=["begdt", "enddt", "crsp_obj_cd"])


def _combine(f, key):
    """Share classes combined by assets at the start of the month."""
    v = np.isfinite(f.mret) & np.isfinite(f.w) & (f.w > 0)
    x = f[v].assign(wr=f.w[v] * f.mret[v])
    g = x.groupby([key, "mi"], as_index=False).agg(sw=("w", "sum"), swr=("wr", "sum"), ed=("ed", "max"))
    g["ret"] = g.swr / g.sw
    t = f[np.isfinite(f.mtna)].groupby([key, "mi"], as_index=False).agg(tna=("mtna", "sum"))
    g = g.merge(t, on=[key, "mi"], how="left")
    return g[(g.mi >= MI_FIRST) & (g.mi <= MI_LAST)].sort_values([key, "mi"])
```

## E7. Newey-West regression
```python
def ols_nw(y, X, lags):
    """OLS with an intercept and Newey-West standard errors (Bartlett weights, small-sample factor n/(n-k)), the
    form of qs/btstats.ols_nw. Returns (coefficients, t-values)."""
    y = np.asarray(y, float)
    X = np.column_stack([np.ones(len(y)), np.asarray(X, float)])
    n, k = X.shape
    if n <= k + 1:
        return None, None
    XtX_inv = np.linalg.pinv(X.T @ X)
    b = XtX_inv @ X.T @ y
    u = y - X @ b
    Xu = X * u[:, None]
    S = Xu.T @ Xu
    for lag in range(1, lags + 1):
        G = Xu[lag:].T @ Xu[:-lag]
        S += (1 - lag / (lags + 1.0)) * (G + G.T)
    V = XtX_inv @ S @ XtX_inv * n / max(n - k, 1)
    se = np.sqrt(np.maximum(np.diag(V), 1e-30))
    return b, b / se
```

## E8. Bridging a missed quarter and stopping
```python
def _schedule(f, cut):
    """Holding months of each filing: from the close of the deadline month, three months, buy and hold; six when
    the filer's next filing is exactly two quarters later (one missed quarter bridged); a longer gap or no later
    filing ends the spell after three months. cut: book -> (first, last) record month index."""
    f = f.sort_values(["bk", "q"]).reset_index(drop=True)
    nxt = f.groupby("bk").q.shift(-1)
    f["H"] = np.where((nxt - f.q) >= 2, 6, 3).astype("int64")
    em = {q: _entry_mi(q) for q in f.q.unique()}
    f["em"] = f.q.map(em).astype("int64")
    lo = np.full(len(f), MI_FIRST, dtype="int64")
    hi = np.full(len(f), MI_LAST, dtype="int64")
    for bk, (a, b) in cut.items():
        s = (f.bk == bk).to_numpy()
        lo[s], hi[s] = max(a, MI_FIRST), min(b, MI_LAST)
    f["lo_b"], f["hi_b"] = lo, hi
    return f


def _win_span(f, a, b):
    lo = np.maximum.reduce([f.em.to_numpy() + 1, f.lo_b.to_numpy(), np.full(len(f), a)])
    hi = np.minimum.reduce([f.em.to_numpy() + f.H.to_numpy(), f.hi_b.to_numpy(), np.full(len(f), b)])
    return lo, hi
```

## E9. Rank shares and pools
```python
def _share(pool, x, own):
    """Rank share of x in the pool (0 worst .. 1 best, ties average) after taking out the investor's own entries;
    missing unless one of its own entries is in the pool."""
    if x is None or not np.isfinite(x) or not len(pool) or not pool.index.isin(list(own)).any():
        return np.nan
    v = pool[~pool.index.isin(list(own))].to_numpy(float)
    if len(v) == 0:
        return np.nan
    return (np.sum(v < x) + 0.5 * np.sum(v == x)) / float(len(v))


def _member_shares(pool):
    if len(pool) < 2:
        return pd.Series(np.nan, index=pool.index)
    return (pool.rank(method="average") - 1.0) / (len(pool) - 1.0)


def _blockpos(tab):
    """Share of the blocks with a result in which the six-factor alpha is positive."""
    t = tab[tab.w.isin(BLOCKS) & (tab.n >= MIN_RESULT) & tab.a.notna()]
    return t.groupby("bk").a.apply(lambda s: float((s > 0).mean()))


def _pools(tab):
    pool = {w: tab[(tab.w == w) & tab.grp].set_index("bk").a.astype(float) for w, _, _ in WIN}
    ingrp = set(tab[tab.w.isin(BLOCKS) & tab.grp].bk)
    bp = _blockpos(tab)
    bpool = bp[bp.index.isin(ingrp)]
    return pool, bpool
```

## E10. What the report prints for an investor
```python
def _f(x, fmt, sign=False):
    if x is None:
        return "."
    try:
        if not np.isfinite(float(x)):
            return "."
    except (TypeError, ValueError):
        return "."
    s = (("%+" + fmt[1:]) if sign else fmt) % float(x)
    return s.replace("0.", ".", 1) if fmt.startswith("%.") and abs(float(x)) < 1 and not sign else s


def _wline(pid, w, s, full):
    head = "  %-6s %-7s n%-3d" % (pid, w, int(s.get("n", 0)))
    if not full:
        return head + " rk %s" % _f(s.get("rk"), "%.3f")
    return head + (" a %s t %s r %s rm %s pa %s pv %s dd %s yb %s np %s tw %s to %s p10 %s pn %s fv %s ms %s rk %s"
                   % (_f(s.get("a"), "%.2f", True), _f(s.get("t"), "%.2f", True), _f(s.get("r"), "%.1f", True),
                      _f(s.get("rm"), "%.1f", True), _f(s.get("pa"), "%.2f", True), _f(s.get("pv"), "%.2f"),
                      _f(s.get("dd"), "%.1f"), _f(s.get("yb"), "%.2f"), _f(s.get("np"), "%.0f"),
                      _f(s.get("tw"), "%.2f"), _f(s.get("to"), "%.2f"), _f(s.get("p10"), "%.2f", True),
                      _f(s.get("pn"), "%.2f", True), _f(s.get("fv"), "%.2f"), _f(s.get("ms"), "%.3f"),
                      _f(s.get("rk"), "%.3f")))

    for d in res["inv"]:
        if d["kind"] not in ("13f", "fund") or not d["win"]:
            continue
        full_rec = d["months"] >= MIN_STATS
        L.append("INV %-6s %-28s | grade %s | %-4s | months %3d | style %s | score %s | components %s"
                 % (d["id"], d["name"][:28], d["grade"], d["kind"], d["months"], d["style"],
                    _f(d["score"], "%.3f"), " ".join(_f(c, "%.3f") for c in d.get("comp", []))))
        for w, _, _ in WIN:
            s = d["win"].get(w)
            if s is None:
                continue
            L.append(_wline(d["id"], w, s, full_rec or s.get("n", 0) >= MIN_RESULT))
```
