"""Point-in-time backtest of the frozen screens (validation/PROTOCOL.md sections 2-4).

Three steps, each resumable (results on disk under cache/bt/work):
  1. company pass  - for every company and formation date: its profile and metrics from what had been filed before
                     that date (pit.py). Metrics are recomputed only when a new filing arrived; between filings only
                     'years since the latest fiscal year' moves.
  2. formation pass - per formation date: the live pipeline's context building (make_contexts, industry cycle),
                     prices from that day (valuation.value), and every screen evaluated unchanged; plus the
                     threshold-grid and leave-one-gate-out variants and the baseline scores.
  3. returns       - open of the next trading day to the open of the following month's first trading day, with
                     splits, dividends and delistings.
"""
import copy
import gzip
import os
import pickle
from datetime import date, timedelta

from .backtest_support import WORK, ensure_dirs, read_json, write_json
from .btprices import adjusted_close, holding_return, type_name
from .btscores import all_scores
from .extract import CompanyData
from .industry import CYCLICAL, HEALTHCARE, NEVER, REAL_ASSETS, in_ranges
from .massive import m_symbol
from .pipeline import apply_industry_cycle, detect_events, make_contexts, metrics_for, sic_match
from .pit import facts_as_of, info_as_of, last_filed
from .screens import FAIL, PASS, SCREENS, broad_ok, screen_anyway
from .valuation import primary_ticker, value

GRID_SHIFTS = (-0.3, -0.2, -0.1, 0.1, 0.2, 0.3)       # 0 = the frozen thresholds (base result)
DELIST_HAIRCUT = -0.30                                  # Shumway (1997), when no last price is found
COMP_DIR = os.path.join(WORK, "companies")
FORM_DIR = os.path.join(WORK, "formations")
RET_DIR = os.path.join(WORK, "returns")


def _dd(s):
    return date.fromisoformat(s[:10])


def sec_ticker(sym):
    return str(sym).upper().replace(".", "-")


# ====================================================================== step 1: companies
def company_pass(cik, dates, univ_by_date, cfg, load_facts, load_filings, prev=None):
    """{'dates': {d: [vm, vi]}, 'vm': [metrics version or {'stage': why}], 'vi': [profile version]} for one CIK.
    prev: an earlier result covering the dates before these (a monthly run adds only the new month-ends; facts
    filed later never change an earlier date, so the stored versions stay valid)."""
    fs = load_facts(cik)
    fl = load_filings(cik)
    if prev and prev.get("dates") and "key" in prev and all(d > max(prev["dates"]) for d in dates):
        out = {"dates": dict(prev["dates"]), "vm": list(prev["vm"]), "vi": list(prev["vi"])}
        prev_key, prev_info = prev["key"], (prev["vi"][-1] if prev["vi"] else None)
    else:
        out = {"dates": {}, "vm": [], "vi": []}
        prev_key, prev_info = None, None
    for d in dates:
        dd = _dd(d)
        tickers = [sec_ticker(t) for t in univ_by_date[d][cik]["tickers"]]
        info = info_as_of(fl, d) if fl else {"sic": "", "events": []}
        info["all_tickers"] = tickers
        ev = detect_events(info, cfg, dd) if fl else {}
        info["event_types"] = sorted(ev)
        info["event_detail"] = ev
        if info != prev_info:
            out["vi"].append(info)
            prev_info = info
        vi = len(out["vi"]) - 1
        sic = info.get("sic")
        if not fs or fs.get("_not_found") or not fs.get("facts"):
            key = ("stage", "no XBRL financial data")
        elif in_ranges(sic, NEVER):
            key = ("stage", "not screened: fund / SPAC / REIT / shell")
        else:
            core_ex = None if screen_anyway(info, cfg) else sic_match(cfg["exclude_sic"], sic)
            needed = (not core_ex) or in_ranges(sic, HEALTHCARE) or in_ranges(sic, CYCLICAL) \
                or in_ranges(sic, REAL_ASSETS) or bool(ev) or broad_ok(info, cfg)
            if not needed:
                key = ("stage", f"not screened: {core_ex['label']} (excluded from every screen)")
            else:
                listing = sorted(e["date"] for k, e in ev.items() if k in ("recent IPO", "spin-off / Form 10 listing"))
                key = ("m", last_filed(fs, d), listing[0] if listing else None, sic)
        if key != prev_key:
            if key[0] == "stage":
                out["vm"].append({"stage": key[1]})
            else:
                cd = CompanyData(facts_as_of(fs, d))
                if cd.currency is None:
                    out["vm"].append({"stage": "no monetary XBRL data"})
                else:
                    res, why = metrics_for(cd, sic, ev, cfg, dd)
                    if res is None:
                        out["vm"].append({"stage": why})
                    else:
                        m, rows, compact = res
                        out["vm"].append({"m": m, "compact": compact, "flags": sorted(cd.flags),
                                          "cands": cd.candidates, "scores": all_scores(cd, rows),
                                          "latest_end": m.get("latest_fy_end")})
            prev_key = key
        out["dates"][d] = [len(out["vm"]) - 1, vi]
    out["key"] = prev_key
    return out


def run_company_pass(grid, univ_by_date, cfg, load_facts, load_filings, log=print, refresh=False):
    ensure_dirs(COMP_DIR)
    by_cik = {}
    for g in grid:
        for c in univ_by_date[g["d"]]:
            by_cik.setdefault(c, []).append(g["d"])
    n, done = len(by_cik), 0
    log(f"Company pass: {n} companies")
    for c, dates in sorted(by_cik.items()):
        path = os.path.join(COMP_DIR, f"{c}.pkl.gz")
        old = None
        if os.path.exists(path) and not refresh:
            try:
                with gzip.open(path, "rb") as f:
                    old = pickle.load(f)
                if all(d in old["dates"] for d in dates):
                    done += 1
                    continue
            except (OSError, EOFError, pickle.UnpicklingError):
                old = None
        new_dates = sorted(d for d in dates if not old or d not in old["dates"])
        if old and old.get("dates") and new_dates and new_dates[0] > max(old["dates"]):
            res = company_pass(c, new_dates, univ_by_date, cfg, load_facts, load_filings, prev=old)
        else:
            res = company_pass(c, sorted(dates), univ_by_date, cfg, load_facts, load_filings)
        with gzip.open(path + ".tmp", "wb") as f:
            pickle.dump(res, f, protocol=pickle.HIGHEST_PROTOCOL)
        os.replace(path + ".tmp", path)
        done += 1
        if done % 500 == 0:
            log(f"  {done}/{n} companies")
    return by_cik


class CompanyStore:
    """The version of each company valid on a date, reloading a company's file only when its version changes."""

    def __init__(self):
        self.cur = {}

    def get(self, cik, d):
        hit = self.cur.get(cik)
        if hit is not None and d in hit["dates"]:
            vm, vi = hit["dates"][d]
            if hit.get("loaded") == (vm, vi):
                return hit["m"], hit["i"]
        path = os.path.join(COMP_DIR, f"{cik}.pkl.gz")
        try:
            with gzip.open(path, "rb") as f:
                full = pickle.load(f)
        except (OSError, EOFError, pickle.UnpicklingError):
            return None, None
        if d not in full["dates"]:
            return None, None
        vm, vi = full["dates"][d]
        self.cur[cik] = {"dates": full["dates"], "loaded": (vm, vi), "m": full["vm"][vm], "i": full["vi"][vi]}
        return full["vm"][vm], full["vi"][vi]


# ====================================================================== step 2: formations
class _Shift:
    """A gate with all thresholds moved by s (s > 0 stricter, s < 0 looser)."""

    def __init__(self, g, s):
        self._g, self._s = g, s

    def __getattr__(self, k):
        return getattr(self._g, k)

    def evaluate(self, ctx, cfg, scope, s=0.0):
        return self._g.evaluate(ctx, cfg, scope, self._s + s)


def variant(screen, shift=0.0, drop=None):
    v = copy.copy(screen)
    gates = [g for g in screen.gates if g.gid != drop]
    v.gates = [_Shift(g, shift) for g in gates] if shift else gates
    return v


def _counts(r):
    met = sum(1 for st in r["gates"].values() if st[0] == PASS)
    ev = sum(1 for st in r["gates"].values() if st[0] in (PASS, FAIL))
    return met, ev


def contexts_at(g, univ, store, cfg, splits, fx, hist_closes):
    """Every company's context at formation day g['d'] (point-in-time metrics + that day's prices), as the live
    pipeline builds it: (ctxs, subs, extra). Shared by the frozen-screen formation and the triage panel."""
    d = g["d"]
    dd = _dd(d)
    bars = g["bars_d"]
    uinfo, records, raw, subs, extra = {}, {}, {}, {}, {}
    for c, u in univ.items():
        vm, info = store.get(c, d)
        if vm is None:
            continue
        tickers = [sec_ticker(t) for t in u["tickers"]]
        prim = primary_ticker(tickers) or tickers[0]
        uinfo[c] = {"cik": c, "ticker": prim, "name": u.get("name") or info.get("name") or "",
                    "exchange": "Nasdaq" if u.get("ex") == "XNAS" else "NYSE", "all_tickers": tickers}
        info = dict(info)
        info["sic"] = info.get("sic", "")
        subs[c] = info
        rec = {"cik": c, "ticker": prim, "name": uinfo[c]["name"], "sic": info.get("sic", ""),
               "industry": info.get("sicDescription", ""), "events": info.get("event_detail") or {}}
        if "m" in vm:
            m = dict(vm["m"])
            end = vm.get("latest_end") or m.get("latest_fy_end")
            if end:
                m["years_since_latest_fy"] = round((dd - _dd(end)).days / 365.25, 2)
            raw[c] = (m, vm["compact"], vm["flags"], vm["cands"])
            rec["stage"] = "screened"
            extra[c] = vm.get("scores") or {}
        else:
            rec["stage"] = vm.get("stage") or "?"
        records[c] = rec
        extra.setdefault(c, {})["type"] = u.get("type")
    ctxs = make_contexts(raw, subs, uinfo, records, cfg, fx, dd)
    apply_industry_cycle(ctxs, cfg)

    # as live (Massive.month_end_days): the closes of the previous 12 month-ends, not the formation day itself
    hist_days = sorted(x for x in hist_closes if (dd - _dd(x)).days < 366 and x < d)
    since_split = (dd - timedelta(days=760)).isoformat()
    for c, ctx in ctxs.items():
        if ctx.get("events_only"):
            continue
        sym = m_symbol(ctx["ticker"])
        b = bars.get(sym)
        if not b:
            alt = [m_symbol(t) for t in ctx.get("all_tickers") or [] if m_symbol(t) in bars]
            sym = alt[0] if alt else sym
            b = bars.get(sym)
        sp = splits.get(sym) or []
        ctx["recent_splits"] = [x for x in sp if since_split < x[0] <= d]
        best = None
        for hd in hist_days:
            hb = hist_closes[hd].get(sym)
            if hb and hb[1]:
                cl = adjusted_close(hb[1], sp, hd, d)
                if best is None or cl > best[0]:
                    best = (cl, hd)
        if best:
            ctx["high_12m"], ctx["high_12m_date"], ctx["high_12m_asof"] = best[0], best[1], d
        pfd = ctx.get("public_float_date")
        if pfd:
            near = [x for x in hist_days + [d] if x <= pfd and (_dd(pfd) - _dd(x)).days <= 31]
            pb = (bars if near[-1] == d else hist_closes[near[-1]]).get(sym) if near else None
            if pb and pb[1]:
                ctx["pf_close_raw"] = pb[1]
            else:
                ctx["pf_close_note"] = f"no month-end price near {pfd} (the public float date)"
        if not b or not b[1]:
            quote = {"ok": False, "reason": "no price on the formation day"}
        else:
            vols = [hist_closes[x].get(sym) for x in hist_days[-2:]] + [b]
            vols = [v[2] * v[1] for v in vols if v and v[2] and v[1]]
            adv = (sum(vols) / len(vols) / b[1]) if vols else (b[2] or None)
            quote = {"ok": True, "price": b[1], "price_date": d, "open": b[0], "source": "Massive (backtest)",
                     "avg_volume": adv, "listing_type": type_name(extra.get(c, {}).get("type"))}
        v = value(ctx, {"all_tickers": ctx.get("all_tickers"), "latest_annual": subs[c].get("latest_annual"),
                        "name": ctx.get("name")}, quote, ctx.get("fx_rate"), dd, td=None,
                  listing_type=quote.get("listing_type"))
        ctx.update(v)
        ctx["_sym"] = sym
    return ctxs, subs, extra


def formation(g, grid_index, univ, store, cfg, splits, fx, hist_closes):
    """Evaluate every screen at formation day g['d']. hist_closes: {d: bars} of earlier month-ends (12-month high)."""
    d = g["d"]
    ctxs, subs, extra = contexts_at(g, univ, store, cfg, splits, fx, hist_closes)
    out = {"ym": g["ym"], "d": d, "e": g["e"], "companies": {}, "screens": {}, "grid": {}, "loo": {}, "nodata": {}}
    for c, ctx in ctxs.items():
        x = extra.get(c, {})
        rate = ctx.get("fx_rate") or 0
        be = (x.get("book_equity") or 0) * rate if x.get("book_equity") is not None and rate else None
        ebit = ctx.get("ttm_operating_income")
        ev = ctx.get("ev_usd")
        out["companies"][str(c)] = {
            "tk": ctx.get("ticker"), "nm": ctx.get("name"), "sym": ctx.get("_sym"), "sic": str(ctx.get("sic") or ""),
            "mcap": ctx.get("market_cap_usd"), "be": be, "val_ok": bool(ctx.get("val_ok")),
            "ey": (ebit * rate / ev) if (ebit is not None and rate and ev and ev > 0) else None,
            "roc": x.get("roc_tangible"), "fs": x.get("fscore"), "gp": x.get("gp_assets"), "z2": x.get("z2"),
            "ms": x.get("mscore"), "rf": ctx.get("red_flag_count"), "eo": bool(ctx.get("events_only"))}
    for s in SCREENS:
        res, nod = {}, {}
        for c, ctx in ctxs.items():
            if ctx.get("events_only") and s.sid != "special":
                continue
            ok, _why = s.universe(subs[c], ctx, cfg)
            if not ok:
                continue
            r = s.evaluate(ctx, cfg, priced=True)
            met, ev = _counts(r)
            res[str(c)] = [r["class"], bool(r.get("star")), len(r["failed"]), met, ev]
            for gid in r["no_data"]:
                nod[gid] = nod.get(gid, 0) + 1
            ctx.setdefault("_r", {})[s.sid] = r
        out["screens"][s.sid] = res
        out["nodata"][s.sid] = nod
        grid = {}
        cands = [c for c, ctx in ctxs.items() if s.sid in ctx.get("_r", {}) and len(ctx["_r"][s.sid]["failed"]) <= 3]
        for sh in GRID_SHIFTS:
            vs = variant(s, shift=sh)
            grid[str(sh)] = [str(c) for c in cands if vs.evaluate(ctxs[c], cfg, priced=True)["class"] == PASS]
        out["grid"][s.sid] = grid
        loo = {}
        one = [c for c in cands if len(ctxs[c]["_r"][s.sid]["failed"]) == 1]
        for gt in s.gates:
            vs = variant(s, drop=gt.gid)
            add = [str(c) for c in one if ctxs[c]["_r"][s.sid]["failed"] == [gt.gid]
                   and vs.evaluate(ctxs[c], cfg, priced=True)["class"] == PASS]
            if add:
                loo[gt.gid] = add
        out["loo"][s.sid] = loo
    return out


def run_formations(grid, univ_by_date, cfg, splits, log=print, refresh=False):
    ensure_dirs(FORM_DIR)
    store = CompanyStore()
    fx = {k: (float(v), "config.json fx_to_usd (static)") for k, v in (cfg.get("fx_to_usd") or {}).items()
          if isinstance(v, (int, float))}
    fx["USD"] = (1.0, "USD")
    hist = {}
    for i, g in enumerate(grid):
        hist[g["d"]] = g["bars_d"]
        for old in [k for k in hist if (_dd(g["d"]) - _dd(k)).days > 400]:
            hist.pop(old)
        path = os.path.join(FORM_DIR, f"{g['ym']}.json.gz")
        if os.path.exists(path) and not refresh:
            continue
        f = formation(g, i, univ_by_date[g["d"]], store, cfg, splits, fx, hist)
        write_json(path, f)
        n_pass = sum(1 for res in f["screens"].values() for r in res.values() if r[0] == PASS)
        log(f"  {g['ym']}: {len(f['companies'])} companies, {n_pass} passes across screens")


# ====================================================================== step 3: returns
def run_returns(grid, btp, splits, divs, log=print, last_close_budget=0, priority=None, ret_dir=None,
                companies=None):
    """{ym: {cik: [return, how]}} with how = 'ok' | 'last close' | 'haircut' (no exit price found). Entry: open of g['e'];
    exit: open of the next month's g['e']. priority: CIKs (portfolio members) whose missing exits are looked up
    first within the request budget. companies(ym) -> {cik: {'sym': ...}} (default: the formation file);
    ret_dir: where the monthly files go (default RET_DIR)."""
    ret_dir = ret_dir or RET_DIR
    ensure_dirs(ret_dir)
    spent = 0
    for i in range(len(grid) - 1):
        g, nx = grid[i], grid[i + 1]
        path = os.path.join(ret_dir, f"{g['ym']}.json.gz")
        if os.path.exists(path):
            continue
        if companies is not None:
            comp = companies(g["ym"])
            form = {"companies": comp} if comp else None
        else:
            form = read_json(os.path.join(FORM_DIR, f"{g['ym']}.json.gz"))
        if not form:
            continue
        e0, e1 = g["e"], nx["e"]
        b0, b1 = g["bars_e"], nx["bars_e"]
        cik_syms = {}
        for sym in b1:
            r = btp.resolve(sym, e1)
            if r and r.get("cik"):
                cik_syms.setdefault(r["cik"], []).append(sym)
        out = {}
        pri = (priority or {}).get(g["ym"], set())
        order = sorted(form["companies"].items(), key=lambda kv: kv[0] not in pri)
        for c, x in order:
            sym = x.get("sym")
            if not sym or sym not in b0 or not b0[sym][0]:
                continue
            p0 = b0[sym][0]
            sym1 = sym if (sym in b1 and (btp.resolve(sym, e1) or {}).get("cik") == int(c)) else \
                next(iter(cik_syms.get(int(c), [])), None)
            how, end = "ok", e1
            if sym1 and b1[sym1][0]:
                p1 = b1[sym1][0]
            else:
                lc = None
                if spent < last_close_budget:
                    lc = btp.last_close(sym, e0, e1)
                    spent += 1
                if lc:
                    end, p1, how = lc[0], lc[1], "last close"
                else:
                    p1, how = p0 * (1 + DELIST_HAIRCUT), "haircut"
                    end = e0      # no corporate actions applied
            sp = (splits.get(sym) or []) + ([x for x in splits.get(sym1) or []] if sym1 and sym1 != sym else [])
            r = holding_return(p0, p1, sp, divs.get(sym) or [], e0, end)
            if r is not None:
                out[c] = [round(r, 6), how]
        write_json(path, out)
        log(f"  returns {g['ym']}: {len(out)} companies ({sum(1 for v in out.values() if v[1] != 'ok')} exits "
            "without a next-month price)")
    return spent
