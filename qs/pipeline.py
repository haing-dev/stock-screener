"""End-to-end run: universe -> SEC profiles & events -> XBRL facts -> metrics -> screens (financial rules)
-> prices for candidates only -> screens (price rules) -> scores -> workbook."""
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta

import pandas as pd

from . import __version__
from .config import CACHE_DIR, OUTPUT_DIR
from .extract import SUBSET_VERSION, CompanyData, _d, facts_subset, submissions_subset
from .industry import CLINICAL_STAGE, CYCLICAL, HEALTHCARE, NEVER, REAL_ASSETS, in_ranges
from .metrics import compute, model_years, post_event_dilution
from .rules import concentration, flags_for
from .screens import BY_ID, SCREENS, broad_ok, data_holds, screen_anyway
from .sec import FACTS_URL, SUBMISSIONS_URL, TICKERS_URL, NotFound, cache_read, cache_write, filing_index_url


def sic_match(ranges, sic):
    try:
        s = int(str(sic)[:4])
    except (TypeError, ValueError):
        return None
    for r in ranges:
        if r["from"] <= s <= r["to"]:
            return r
    return None


# ------------------------------------------------------------------ fetching
def load_universe(client, cfg, tickers=None):
    path = os.path.join(CACHE_DIR, "universe.json.gz")
    data = cache_read(path, cfg["cache_days_universe"])
    if data is None:
        print("Downloading the SEC list of listed companies...")
        data = client.get_json(TICKERS_URL)
        cache_write(path, data)
    fields = data["fields"]
    rows = [dict(zip(fields, r)) for r in data["data"]]
    wanted = {t.upper() for t in tickers} if tickers else None
    by_cik = {}
    for r in rows:
        if wanted is not None:
            if str(r["ticker"]).upper() not in wanted:
                continue
        elif r["exchange"] not in cfg["exchanges"]:
            continue
        c = int(r["cik"])
        if c not in by_cik:
            by_cik[c] = {"cik": c, "ticker": r["ticker"], "name": r["name"], "exchange": r["exchange"],
                         "all_tickers": [r["ticker"]]}
        else:
            by_cik[c]["all_tickers"].append(r["ticker"])
    from .valuation import primary_ticker
    for u in by_cik.values():
        u["ticker"] = primary_ticker(u["all_tickers"]) or u["ticker"]
    if wanted:
        missing = wanted - {t.upper() for u in by_cik.values() for t in u["all_tickers"]}
        if missing:
            print("  Not found in SEC ticker list: " + ", ".join(sorted(missing)))
    return list(by_cik.values())


FETCH_STATS = {"reused": 0, "downloaded": 0}


def _cached_fetch(client, url, path, max_age, transform, newer_than=None):
    d = cache_read(path, max_age)
    stale = False
    if d is not None and newer_than:
        # a 10-Q/10-K was filed after this cache file was written: fetch again
        try:
            stale = datetime.fromtimestamp(os.path.getmtime(path)).date().isoformat() <= newer_than
        except OSError:
            stale = False
    if d is not None and d.get("subset_version") == SUBSET_VERSION and not stale:
        FETCH_STATS["reused"] += 1
        return d
    if d is not None and d.get("_not_found"):
        FETCH_STATS["reused"] += 1
        return d
    FETCH_STATS["downloaded"] += 1
    try:
        raw = client.get_json(url)
        d = transform(raw)
    except NotFound:
        d = {"_not_found": True, "subset_version": SUBSET_VERSION}
    cache_write(path, d)
    return d


def get_submissions(client, cik, cfg, newer_than=None, max_age=None):
    """newer_than: date of the company's latest filing in SEC's daily index (refetch if the cache predates it)."""
    return _cached_fetch(client, SUBMISSIONS_URL.format(cik=cik),
                         os.path.join(CACHE_DIR, "submissions", f"{cik}.json.gz"),
                         max_age if max_age is not None else cfg["cache_days_submissions"], submissions_subset,
                         newer_than)


def get_facts(client, cik, cfg, newer_than=None, max_age=None):
    return _cached_fetch(client, FACTS_URL.format(cik=cik),
                         os.path.join(CACHE_DIR, "facts", f"{cik}.json.gz"),
                         max_age if max_age is not None else cfg["cache_days_facts"], facts_subset, newer_than)


def load_cached_facts(cik):
    return cache_read(os.path.join(CACHE_DIR, "facts", f"{cik}.json.gz"))


def fetch_all(ciks, fn, workers, label, on_result=None):
    """Download in parallel (rate-limited). If on_result is given, each result is handed to it as soon as
    it arrives and NOT kept in memory."""
    results, errors = {}, {}
    n = len(ciks)
    if not n:
        return results, errors
    t0 = time.time()
    done = 0
    print(f"{label}: {n} companies")
    with ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
        futs = {ex.submit(fn, c): c for c in ciks}
        for fut in as_completed(futs):
            c = futs[fut]
            try:
                r = fut.result()
                if on_result is None:
                    results[c] = r
                else:
                    on_result(c, r)
            except Exception as e:  # noqa: BLE001 - report and continue
                errors[c] = str(e)
            done += 1
            if done % 250 == 0 or done == n:
                el = time.time() - t0
                eta = el / done * (n - done)
                print(f"  {done}/{n} done, {len(errors)} errors, ~{eta / 60:.0f} min left")
    if errors:
        sample = next(iter(errors.values()))
        print(f"  WARNING: {len(errors)} downloads failed (first error: {sample[:200]})")
    return results, errors


# ------------------------------------------------------------------ successor registrants
# filing agents whose CIK prefixes many companies' accession numbers (never a predecessor company)
FILING_AGENTS = {1193125, 1628280, 1104659, 950170, 950103, 1213900, 1477932, 1640334, 1493152, 1564590, 1558370,
                 1437749, 1615774, 1171843, 1140361, 1079973, 1062993, 1144204, 1185185, 1567619, 1683168, 1654954,
                 1829126, 1096906, 1580642, 1013762, 950123, 1047469, 1206774, 1214659, 940180, 950134, 1157523,
                 1199835, 1209191, 1225208, 1127602, 1179110, 1181431, 1145443, 1069157, 1010412, 1017386}


def no_data_hint(info, fs=None):
    """Why a listed company has no usable financial statements - so the user knows where to look instead."""
    la, forms = info.get("latest_annual") or {}, {e.get("form") for e in info.get("events") or []}
    if not la and (forms & {"S-4", "S-4/A", "8-K12B", "8-K12G3", "F-4", "F-4/A"}):
        return (" - new registrant after a merger/reorganization (S-4): its history is filed under the old "
                "company's CIK; check by hand")
    if (la.get("form") or "").startswith("40-F"):
        return " - Canadian 40-F filer whose financial statements aren't in SEC XBRL; check by hand"
    if not la:
        return " - no annual report yet (recent listing)"
    return ""


def find_predecessor(client, cfg, cik, fs, info, rec):
    """A listed company whose CIK has no annual report yet but whose filings were submitted under another
    company's CIK with the same name (e.g. ExxonMobil Holdings Corp, filed by Exxon Mobil Corp after a
    holding-company reorganization): returns (predecessor_cik, its facts, its profile) so the history isn't lost."""
    if info.get("latest_annual") or "recent IPO" in (rec.get("events") or {}):
        return None
    facts = fs.get("facts") or {}
    if any(e.get("form") in ("10-K", "20-F", "40-F") for t in facts.values() for u in t.values()
           for ents in u.values() for e in ents):
        return None
    counts = {}
    for t in facts.values():
        for u in t.values():
            for ents in u.values():
                for e in ents:
                    a = str(e.get("accn") or "")
                    if a[:10].isdigit():
                        p = int(a[:10])
                        counts[p] = counts.get(p, 0) + 1
    from .valuation import names_match
    for p, _ in sorted(counts.items(), key=lambda kv: -kv[1])[:3]:
        if p == cik or p in FILING_AGENTS:
            continue
        try:
            pfs = get_facts(client, p, cfg)
        except Exception:  # noqa: BLE001
            continue
        if not pfs or pfs.get("_not_found") or not pfs.get("facts"):
            continue
        if names_match(pfs.get("entityName"), fs.get("entityName") or info.get("name")):
            try:
                pinfo = get_submissions(client, p, cfg) or {}
            except Exception:  # noqa: BLE001
                pinfo = {}
            return p, pfs, pinfo
    return None


def merge_facts(old, new):
    """Predecessor facts + successor facts (successor entries listed last, so they win ties)."""
    out = {k: v for k, v in new.items() if k != "facts"}
    merged = {}
    for src in (old, new):
        for tax, tags in (src.get("facts") or {}).items():
            for tag, units in tags.items():
                for unit, ents in units.items():
                    merged.setdefault(tax, {}).setdefault(tag, {}).setdefault(unit, []).extend(ents)
    out["facts"] = merged
    out["candidates"] = new.get("candidates") or old.get("candidates") or {}
    return out


# ------------------------------------------------------------------ events (Special Situations)
def detect_events(info, cfg, today):
    """Spin-offs (Form 10 registration), bankruptcy (8-K item 1.03) and recent IPOs, from SEC filings."""
    window = int(cfg.get("event_window_months", 36)) * 30.44
    out = {}
    for e in info.get("events") or []:
        try:
            age = (today - _d(e["date"])).days
        except (KeyError, ValueError, TypeError):
            continue
        if age > window:
            continue
        f = e["form"]
        if f.startswith("10-12"):
            kind = "spin-off / Form 10 listing"
        elif f.startswith("8-K") and "1.03" in (e.get("items") or []):
            kind = "bankruptcy / reorganization (8-K 1.03)"
        elif f in ("S-1", "S-1/A", "F-1", "F-1/A", "424B4"):
            fa = info.get("first_annual_in_recent")
            young = (not info.get("has_older_filing_pages")) and (fa is None or (today - _d(fa)).days <= window + 400)
            if not young:
                continue
            kind = "recent IPO"
        else:
            continue
        cur = out.get(kind)
        if cur is None or e["date"] < cur["date"]:
            out[kind] = e
    return out


# ------------------------------------------------------------------ context for the screens
def build_ctx(u, info, m, rows, cd, cfg, fx, today):
    ctx = dict(m)
    ctx.update({"cik": u["cik"], "ticker": u["ticker"], "other_tickers": ", ".join(u["all_tickers"][1:]),
                "name": info.get("name") or u["name"], "exchange": u["exchange"], "sic": info.get("sic", ""),
                "industry": info.get("sicDescription", ""), "entity_type": info.get("entityType"),
                "all_tickers": u["all_tickers"]})
    # public during the 2008-09 recession? XBRL figures from 2010 or earlier (smaller filers started XBRL in 2011
    # with one comparative year), or a first annual report before mid-2009 in a complete filing list
    # public during the 2008-09 recession? (conservative: when unsure, the 2009 test asks for a manual check rather
    # than being skipped) - XBRL figures from 2010 or earlier, a first annual report before mid-2009, or a filing
    # history so long that SEC splits it into older pages
    fa = info.get("first_annual_in_recent")
    ctx["listed_before_2009"] = bool((m.get("first_fy_available") and m["first_fy_available"] <= 2010)
                                     or (fa and fa < "2009-07-01") or info.get("has_older_filing_pages"))
    rate = fx.get(m.get("currency"), (None, None))[0] if m.get("currency") else None
    ctx["fx_rate"] = rate
    ctx["fx_source"] = fx.get(m.get("currency"), (None, None))[1]
    ctx["latest_revenue_usd"] = m["latest_revenue"] * rate if (rate and m.get("latest_revenue") is not None) else None
    ctx["ttm_revenue_usd"] = m["ttm_revenue"] * rate if (rate and m.get("ttm_revenue") is not None) else None
    last = rows[-1] if rows else {}
    ctx["latest_fy_ebitda"] = last.get("ebitda")
    ctx["latest_fy_operating_income"] = last.get("operating_income")
    ctx["roic_latest"] = last.get("roic")
    bd = m.get("bs_date")
    ctx["bs_age_days"] = (today - _d(bd)).days if bd else None
    liquid = m.get("liquid_assets")
    ctx["debt_to_liquid_assets"] = ((m.get("bs_debt") or 0) / liquid) if liquid else None
    ctx["liquid_assets_usd"] = liquid * rate if (liquid is not None and rate) else None
    ne = m.get("normalized_ebitda")
    nd = m.get("bs_net_debt")
    ctx["net_debt_to_norm_ebitda"] = (nd / ne) if (nd is not None and ne and ne > 0) else None
    hc = in_ranges(info.get("sic"), HEALTHCARE)
    ctx["hc_segment"] = hc[2] if hc else None
    pre = cfg["screens"]["hc_clinical"]["pre_revenue_below_usd"]
    ctx["hc_stage"] = ("pre-revenue" if (ctx["ttm_revenue_usd"] or 0) < pre else "early commercial") if hc else None
    cy = in_ranges(info.get("sic"), CYCLICAL)
    ctx["cycle_group"] = cy[2] if cy else None
    la = info.get("latest_annual") or {}
    rd, fe = la.get("reportDate"), m.get("latest_fy_end")
    if rd and fe and (_d(rd) - _d(fe)).days > 60:
        ctx["xbrl_lags_annual_report"] = rd
        cd.flags.add(f"latest annual report (period ending {rd}, filed {la.get('filingDate')}) isn't in SEC's XBRL "
                     f"data yet - figures are from the year ending {fe}")
    flags = sorted(cd.flags)
    ctx["hold_reasons"] = data_holds(flags)
    sic_flag = sic_match(cfg.get("flag_sic", []), info.get("sic"))
    ctx["flags"] = flags_for(m, set(flags), sic_flag, info, cfg)
    if m.get("over_earning_short_history") and ctx.get("cycle_group"):
        ctx["over_earning"] = m["over_earning"] = True
    if m.get("over_earning"):
        ctx["flags"].append(f"peak margins? operating margin {m['operating_margin_latest']:.0%} vs its median "
                            f"{m['operating_margin_median']:.0%} after revenue +{m['revenue_growth_2y']:.0%} in 2 "
                            "years - structural or cyclical? (Druckenmiller)")
    if m.get("buybacks_debt_funded"):
        ctx["flags"].append("share count falling while net debt rose by more than a year of cash flow - "
                            "per-share growth partly debt-funded (Druckenmiller)")
    if m.get("capex_to_ocf_3y") is not None and m["capex_to_ocf_3y"] > 1.0:
        ctx["flags"].append(f"capex = {m['capex_to_ocf_3y']:.0%} of operating cash flow (3y) - externally funded "
                            "build-out? (Maverick)")
    if m.get("maturities_covered") is False:
        ctx["flags"].append("debt due within 2 years exceeds cash + 2 years of free cash flow (refinancing risk)")
    from .screens import red_flag_signals
    sig = red_flag_signals(ctx, cfg) if "red_flags" in cfg.get("screens", {}) else []
    ctx["red_flag_count"], ctx["red_flag_notes"] = len(sig), "; ".join(sig)
    ctx["data_gap_candidates"] = cd.candidates
    ctx["latest_annual_form"] = la.get("form")
    ctx["latest_annual_filed"] = la.get("filingDate")
    ctx["latest_annual_accn"] = la.get("accn")
    ctx["latest_annual_doc"] = la.get("primaryDocument")
    ctx["latest_annual_url"] = filing_index_url(u["cik"], la["accn"]) if la.get("accn") else None
    return ctx


def industry_cycle(ctxs, series, cfg):
    """Aggregate operating margin and capex/D&A for each cyclical group; where is the latest year in its
    10-year range? series: {cik: {fy: (rev, op, capex, da)}} for cyclical companies."""
    groups = {}
    for cik, c in ctxs.items():
        g = c.get("cycle_group")
        if g and cik in series:
            groups.setdefault(g, []).append(cik)
    out = {}
    for g, ciks in groups.items():
        years = {}
        for cik in ciks:
            for fy, (rev, op, capex, da, *rest) in series[cik].items():
                if rev and op is not None and rev > 0:
                    y = years.setdefault(fy, {"rev": 0.0, "op": 0.0, "n": 0, "capex": 0.0, "da": 0.0, "n_cd": 0,
                                              "ret": 0.0, "capex_r": 0.0})
                    rate = ctxs[cik].get("fx_rate") or 0
                    if not rate:
                        continue
                    y["rev"] += rev * rate
                    y["op"] += op * rate
                    y["n"] += 1
                    if capex is not None and da:
                        y["capex"] += capex * rate
                        y["da"] += abs(da) * rate
                        y["n_cd"] += 1
                    if capex is not None and rest:
                        # buybacks + dividends vs capex (Einhorn: "higher prices aren't fueling new capacity
                        # instead they're fueling buybacks")
                        y["ret"] += rest[0] * rate
                        y["capex_r"] += capex * rate
        if not years:
            continue
        max_n = max(v["n"] for v in years.values())
        good = sorted(fy for fy, v in years.items() if v["n"] >= max(3, 0.6 * max_n))
        if len(good) < 5:
            out[g] = {"group": g, "companies": len(ciks), "note": "too few companies/years for an industry signal"}
            continue
        good = good[-10:]
        margins = [years[fy]["op"] / years[fy]["rev"] for fy in good]
        last = margins[-1]
        pct = (sum(1 for x in margins[:-1] if x < last) + 0.5 * sum(1 for x in margins[:-1] if x == last)) / (len(margins) - 1)
        l3 = good[-3:]
        cap = sum(years[fy]["capex"] for fy in l3)
        da = sum(years[fy]["da"] for fy in l3)
        out[g] = {"group": g, "companies": len(ciks), "latest_fy": good[-1],
                  "industry_margin_latest": last, "industry_margin_median_10y": sorted(margins)[len(margins) // 2],
                  "industry_margin_percentile": pct, "industry_capex_to_da": (cap / da) if da else None,
                  "industry_trough_zone": pct <= cfg["screens"]["cyclicals"]["industry_trough_percentile"],
                  "industry_returns_to_capex": (sum(years[fy]["ret"] for fy in l3) / sum(years[fy]["capex_r"] for fy in l3)
                                                if sum(years[fy]["capex_r"] for fy in l3) > 0 else None),
                  "years_used": f"{good[0]}-{good[-1]}"}
    return out


# ------------------------------------------------------------------ past prices (Owner-Operators, Hidden Earnings)
def enrich_price_history(ctxs, results, prices, cfg, today, log=print):
    """Inputs that need past prices or split history:
      * recent_splits: every split of the last ~13 months (Massive's split list). value() uses it to put a share
        count reported before a split on today's basis, and the 12-month high is split-adjusted with it.
      * high_12m: highest month-end close of the last 12 months (Massive: 12 all-stocks requests). Without Massive
        (or its split list) Twelve Data's 52-week high is used instead.
      * pf_close_raw / pf_close: the close on the date of the public float each company reports (last day of its
        second fiscal quarter), to turn the float in dollars into shares and so insider ownership. Massive gives the
        close as printed that day (matched with the cover-page share count from the same time, so a later split
        can't distort it); Twelve Data (local runs, capped) gives a split-adjusted close, matched with today's
        share count. Only for companies the Owner-Operators screen hasn't already ruled out."""
    if prices is None or not prices.available():
        return
    from .prices import td_symbol
    pc = cfg.get("price_history") or {}
    massive = hasattr(prices, "m") and prices.m.available()
    splits = prices.splits((today - timedelta(days=760)).isoformat()) if massive else None
    for ctx in ctxs.values():
        for k in ("high_12m", "high_12m_date", "high_12m_asof", "recent_splits", "splits_unknown"):
            ctx.pop(k, None)
        if massive:
            if splits is None:
                ctx["splits_unknown"] = True
            else:
                from .massive import m_symbol
                ctx["recent_splits"] = splits.get(m_symbol(ctx["ticker"])) or []
    if massive and splits is not None:
        tick = [ctx["ticker"] for ctx in ctxs.values() if not ctx.get("events_only")]
        highs = prices.month_end_highs(tick, months=int(pc.get("months_for_high", 12)), splits=splits)
        for ctx in ctxs.values():
            h = highs.get(ctx["ticker"])
            if h:
                ctx["high_12m"], ctx["high_12m_date"] = h
                ctx["high_12m_asof"] = today.isoformat()
    elif massive:
        log("  WARNING: Massive's split list is unavailable - 12-month highs skipped (a split could look like a fall)")
    own = results.get("owners") or {}
    # companies failing at most one financial rule: the rest fail the screen whatever their insider stake, and a
    # 'missed 1 rule' entry must have its insider share measured. Companies failing nothing come first.
    cands = [c for c, r in own.items() if len(r.get("failed") or []) <= 1 and ctxs[c].get("public_float")
             and ctxs[c].get("public_float_date")]
    if not cands:
        return
    cap = None if massive else int(pc.get("float_price_lookups_without_massive", 120))
    cands.sort(key=lambda c: (len(own[c].get("failed") or []), ctxs[c]["public_float_date"],
                              -(ctxs[c].get("latest_revenue_usd") or 0)))
    got = tried = 0
    for c in cands:
        ctx = ctxs[c]
        for k in ("pf_close", "pf_close_raw", "pf_close_note"):
            ctx.pop(k, None)
        if cap is not None and tried >= cap:
            ctx["pf_close_note"] = f"price on the float date not looked up (limit of {cap} without Massive)"
            continue
        tried += 1
        sym = td_symbol(ctx["ticker"])
        if massive:
            close = prices.close_on(sym, ctx["public_float_date"], adjusted=False)
            if close:
                ctx["pf_close_raw"] = close
        else:
            close = prices.close_on(sym, ctx["public_float_date"])
            if close:
                ctx["pf_close"] = close
        if close:
            got += 1
        else:
            ctx["pf_close_note"] = f"no price found for {ctx['public_float_date']} (the public float date)"
    log(f"  Price on the public-float date found for {got} of {len(cands)} Owner-Operator candidates")


# ------------------------------------------------------------------ main
def run_screens(client, cfg, tickers=None, out_name=None, today=None, screens=None, prices=None,
                detail_all=False, price_all=False, models_out=None):
    """models_out: a dict to fill with {cik: per-year statement lines} (Excel model, historical multiples)."""
    today = today or date.today()
    started = datetime.now()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    wanted = [BY_ID[s] for s in (screens or [s.sid for s in SCREENS])]

    universe = load_universe(client, cfg, tickers)
    print(f"Universe: {len(universe)} companies ({'your tickers' if tickers else ', '.join(cfg['exchanges'])})")
    ciks = [u["cik"] for u in universe]
    workers = int(cfg.get("parallel_downloads", 4))
    # only companies that filed since the last run are downloaded again (SEC daily index); a new data format or an
    # empty cache is filled from SEC's nightly bulk files instead of ~11,000 single requests
    from .secsync import BULK_FACTS_URL, BULK_SUBS_URL, bulk_load, mark_bulk_done, needs_bulk, sync_index
    full_universe = not tickers and not getattr(client, "fixtures_dir", None)
    idx = sync_index(client, today) if full_universe else None
    age_subs = cfg.get("cache_days_submissions_indexed", 120) if idx is not None else None
    age_facts = cfg.get("cache_days_facts_indexed", 365) if idx is not None else None
    sub_dir = os.path.join(CACHE_DIR, "submissions")
    n_cached = len(os.listdir(sub_dir)) if os.path.isdir(sub_dir) else 0
    bulk = full_universe and needs_bulk(SUBSET_VERSION, len(ciks), n_cached)
    if bulk:
        print("Full refresh from SEC bulk files (new data format or empty cache)")
        bulk_load(client, BULK_SUBS_URL, ciks, sub_dir, submissions_subset)
    FETCH_STATS.update(reused=0, downloaded=0)
    subs, sub_err = fetch_all(ciks, lambda c: get_submissions(client, c, cfg, (idx or {}).get(str(c), {}).get("any"),
                                                              age_subs), workers,
                              "Step 1/4 - company profiles and filing events")
    print(f"  profiles: {FETCH_STATS['reused']} reused from the cache, {FETCH_STATS['downloaded']} downloaded")

    records, to_fetch = {}, []
    for u in universe:
        c = u["cik"]
        info = subs.get(c) or {}
        info["all_tickers"] = u["all_tickers"]
        rec = {"cik": c, "ticker": u["ticker"], "other_tickers": ", ".join(u["all_tickers"][1:]),
               "name": info.get("name") or u["name"], "exchange": u["exchange"], "sic": info.get("sic", ""),
               "industry": info.get("sicDescription", "")}
        ev = detect_events(info, cfg, today) if info else {}
        info["event_types"] = sorted(ev)
        info["event_detail"] = ev
        rec["events"] = ev
        if c in sub_err:
            rec["stage"] = "download error (profile): " + sub_err[c][:120]
        elif not info or info.get("_not_found"):
            rec["stage"] = "no SEC profile"
        elif in_ranges(info.get("sic"), NEVER):
            rec["stage"] = "not screened: fund / SPAC / REIT / shell"
        else:
            core_ex = None if screen_anyway(info, cfg) else sic_match(cfg["exclude_sic"], info.get("sic"))
            needed = (not core_ex) or in_ranges(info.get("sic"), HEALTHCARE) or in_ranges(info.get("sic"), CYCLICAL) \
                or in_ranges(info.get("sic"), REAL_ASSETS) or bool(ev) or broad_ok(info, cfg)
            if needed:
                rec["stage"] = "pending"
                to_fetch.append(c)
            else:
                rec["stage"] = f"not screened: {core_ex['label']} (excluded from every screen)"
        records[c] = rec
    uinfo = {u["cik"]: u for u in universe}

    raw = {}    # cik -> (m, compact rows)

    def handle(c, fs):
        rec = records[c]
        try:
            if not fs or fs.get("_not_found") or not fs.get("facts"):
                rec["stage"] = "no XBRL financial data" + no_data_hint(subs.get(c) or {})
                return
            pred = find_predecessor(client, cfg, c, fs, subs.get(c) or {}, rec)
            if pred:
                p, pfs, pinfo = pred
                fs = merge_facts(pfs, fs)
                if pinfo.get("latest_annual") and not (subs.get(c) or {}).get("latest_annual"):
                    subs[c]["latest_annual"] = pinfo["latest_annual"]
            cd = CompanyData(fs)
            if cd.currency is None and not pred:
                rec["stage"] = "no monetary XBRL data" + no_data_hint(subs.get(c) or {}, fs)
                return
            if pred:
                cd.flags.add(f"new SEC registrant (holding-company reorganization?): history taken from predecessor "
                             f"CIK {pred[0]} ({pred[1].get('entityName')}) - confirm the share exchange was 1:1")
            if cd.currency is None:
                rec["stage"] = "no monetary XBRL data"
                return
            res, why = compute(cd, cfg, today,
                               allow_no_revenue=bool(in_ranges((subs.get(c) or {}).get("sic"), CLINICAL_STAGE)))
            if res is None:
                rec["stage"] = why
                rec["candidates"] = cd.candidates      # shown on Data_Gaps so the company isn't lost
                return
            m, rows = res
            listing = [e for k, e in (rec.get("events") or {}).items() if k in ("recent IPO", "spin-off / Form 10 listing")]
            if listing and m.get("share_count_cagr_3y") is not None:
                first = min(listing, key=lambda e: e["date"])
                raw3 = m["share_count_cagr_3y"]
                m["share_count_cagr_3y"], basis = post_event_dilution(cd, m, first["date"], today)
                m["share_count_cagr_3y_basis"] = f"measured after the {first['date']} listing: {basis}"
                if raw3 is not None and (m["share_count_cagr_3y"] is None or abs(raw3 - m["share_count_cagr_3y"]) > 0.02):
                    cd.flags.add(f"share count {raw3:+.0%}/yr including pre-listing years (preferred converting at the "
                                 f"IPO / spin) - dilution measured after the listing instead")
            compact = [{k: r[k] for k in ("fy", "revenue", "operating_income", "capex", "da", "ebitda", "roic",
                                          "buybacks", "dividends")}
                       for r in rows]
            raw[c] = (m, compact, sorted(cd.flags), cd.candidates)
            if models_out is not None:
                mdl = model_years(cd, rows)
                if mdl:
                    models_out[c] = mdl
            rec["stage"] = "screened"
        except Exception as e:  # noqa: BLE001 - unusual filings should not stop the run
            rec["stage"] = f"processing error: {type(e).__name__}: {str(e)[:100]}"

    if bulk:
        bulk_load(client, BULK_FACTS_URL, to_fetch, os.path.join(CACHE_DIR, "facts"), facts_subset)

    def _periodic(c):
        a_ = (subs.get(c) or {}).get("latest_periodic_filing") or ""
        b_ = ((idx or {}).get(str(c)) or {}).get("periodic") or ""
        return max(a_, b_) or None
    FETCH_STATS.update(reused=0, downloaded=0)
    _, fact_err = fetch_all(to_fetch, lambda c: get_facts(client, c, cfg, _periodic(c), age_facts), workers,
                            "Step 2/4 - financial statements (XBRL, 10-K and 10-Q)", on_result=handle)
    print(f"  financial statements: {FETCH_STATS['reused']} reused from the cache, {FETCH_STATS['downloaded']} "
          "downloaded")
    if bulk and not fact_err:
        mark_bulk_done(SUBSET_VERSION)
    for c, err in fact_err.items():
        records[c]["stage"] = "download error (financials): " + err[:120]

    # ---- FX (live where possible)
    currencies = {m["currency"] for (m, *_r) in raw.values() if m.get("currency")}
    static = {k: v for k, v in (cfg.get("fx_to_usd") or {}).items() if isinstance(v, (int, float))}
    if prices is not None and prices.available():
        fx = prices.fx_rates(currencies, static)
    else:
        fx = {c: (static[c], "config.json fx_to_usd (static)") for c in currencies if c in static}
        fx["USD"] = (1.0, "USD")

    # ---- contexts
    ctxs, series = {}, {}

    class _CD:  # lightweight stand-in so build_ctx can read flags/candidates
        def __init__(self, flags, cands):
            self.flags, self.candidates = set(flags), cands

    for c, (m, compact, flags, cands) in raw.items():
        info = subs.get(c) or {}
        ctx = build_ctx(uinfo[c], info, m, compact, _CD(flags, cands), cfg, fx, today)
        ev = info.get("event_detail") or {}
        if ev:
            first = min(ev.values(), key=lambda e: e["date"])
            ctx["event_types"] = ", ".join(sorted(ev))
            ctx["event_date"] = first["date"]
            ctx["months_since_event"] = round((today - _d(first["date"])).days / 30.44, 1)
            ctx["event_filing_url"] = filing_index_url(c, first["accn"]) if first.get("accn") else None
        ctxs[c] = ctx
        if ctx.get("cycle_group"):
            series[c] = {r["fy"]: (r["revenue"], r["operating_income"], r["capex"], r["da"],
                                   abs(r.get("buybacks") or 0) + abs(r.get("dividends") or 0)) for r in compact}

    # event companies without usable financials yet (new spin-offs / IPOs): keep them so the Special
    # Situations screen lists them as CHECK ('no annual report yet') instead of silently dropping them
    for c, rec in records.items():
        ev = rec.get("events")
        if c in ctxs or not ev or rec["stage"].startswith("not screened"):
            continue
        if not set(ev) & {"spin-off / Form 10 listing", "bankruptcy / reorganization (8-K 1.03)"}:
            continue   # an IPO with no financial statements yet: listed on the Events sheet only
        u = uinfo[c]
        first = min(ev.values(), key=lambda e: e["date"])
        ctxs[c] = {"cik": c, "ticker": u["ticker"], "other_tickers": ", ".join(u["all_tickers"][1:]),
                   "name": rec["name"], "exchange": u["exchange"], "sic": rec["sic"], "industry": rec["industry"],
                   "all_tickers": u["all_tickers"], "flags": [f"financial data: {rec['stage']}"], "hold_reasons": [],
                   "event_types": ", ".join(sorted(ev)), "event_date": first["date"],
                   "months_since_event": round((today - _d(first["date"])).days / 30.44, 1),
                   "event_filing_url": filing_index_url(c, first["accn"]) if first.get("accn") else None,
                   "currency": "USD", "fx_rate": 1.0, "events_only": True}

    cyc = industry_cycle(ctxs, series, cfg)
    for c, ctx in ctxs.items():
        g = ctx.get("cycle_group")
        if g and g in cyc:
            for k in ("industry_margin_percentile", "industry_capex_to_da", "industry_trough_zone",
                      "industry_margin_latest", "industry_returns_to_capex"):
                ctx[k] = cyc[g].get(k)

    # ---- financial-statement rules first; collect who needs a price
    results = {s.sid: {} for s in wanted}
    to_price = {}
    for c, ctx in ctxs.items():
        info = subs.get(c) or {}
        info["sic"] = info.get("sic", "")
        for s in wanted:
            if ctx.get("events_only") and s.sid != "special":
                continue
            ok, why = s.universe(info, ctx, cfg)
            if not ok:
                continue
            r = s.evaluate(ctx, cfg, priced=False)
            r["universe_note"] = why
            results[s.sid][c] = r
            pending = any(v[0] == "PENDING" for v in r["gates"].values())
            # strict screens (second batch) also price their one-rule misses: without a price their defining rules
            # stay unchecked and a near miss couldn't be shown
            if pending and (not r["failed"] or (s.strict and len(r["failed"]) <= 1)):
                to_price[c] = min(to_price.get(c, 9), 0)   # a price decides the result: fetch first
            pa = cfg.get("price_also") or {}
            if not s.needs_price and r["class"] in ("PASS", "CHECK") and pa.get(f"{s.sid}_pass"):
                to_price[c] = min(to_price.get(c, 9), 1)   # price shown for information

    if price_all:
        # end-of-day prices for everyone (Massive): every company gets valuation columns and peer medians
        for c in ctxs:
            to_price.setdefault(c, 2)
    quotes = {}
    order = sorted(to_price, key=lambda c: (to_price[c], -(ctxs[c].get("latest_revenue_usd") or 0)))
    if to_price:
        items = [(ctxs[c]["ticker"], ctxs[c]["exchange"]) for c in order]
        if prices is not None:
            print(f"Step 3/4 - prices for {len(items)} companies" +
                  ("" if price_all else " (only companies that passed the financial rules)"))
            quotes = prices.quotes(items)
        else:
            quotes = {t: {"ok": False, "reason": "prices not requested"} for t, _ in items}
    enrich_price_history(ctxs, results, prices, cfg, today)
    from .valuation import value
    from .prices import td_symbol
    foreign = [c for c in order if ((subs.get(c) or {}).get("latest_annual") or {}).get("form", "").startswith("20-F")]
    types = prices.instrument_types() if (prices is not None and foreign and prices.available()) else {}
    for c in order:
        ctx = ctxs[c]
        q = quotes.get(ctx["ticker"])
        rate = ctx.get("fx_rate")
        v = value(ctx, {"all_tickers": ctx["all_tickers"], "latest_annual": (subs.get(c) or {}).get("latest_annual"),
                        "name": ctx.get("name")}, q, rate, today, td=prices,
                  listing_type=types.get(td_symbol(ctx["ticker"])))
        ctx.update(v)

    # ---- final evaluation with price rules
    print("Step 4/4 - applying the screens")
    for s in wanted:
        for c in list(results[s.sid]):
            ctx = ctxs[c]
            r = s.evaluate(ctx, cfg, priced=True)
            r["universe_note"] = results[s.sid][c]["universe_note"]
            results[s.sid][c] = r

    # industry concentration (duopoly hint) among all screened companies
    comp_df = pd.DataFrame([{"cik": c, "sic": x.get("sic"), "latest_revenue_usd": x.get("latest_revenue_usd")}
                            for c, x in ctxs.items()]).set_index("cik") if ctxs else pd.DataFrame()
    if len(comp_df):
        conc = concentration(comp_df)
        for c in conc.index:
            for col in conc.columns:
                ctxs[c][col] = conc.at[c, col]

    run_info = {
        "run_started": started.isoformat(timespec="seconds"),
        "run_finished": datetime.now().isoformat(timespec="seconds"),
        "screener_version": __version__,
        "data_source": "SEC EDGAR XBRL companyfacts + submissions (data.sec.gov); prices: " +
                       ("Massive end-of-day (Twelve Data backup); FX: Twelve Data" if price_all else "Twelve Data"),
        "universe": "tickers: " + ", ".join(tickers) if tickers else "exchanges: " + ", ".join(cfg["exchanges"]),
        "screens": ", ".join(s.title for s in wanted),
        "prices_fetched": sum(1 for q in quotes.values() if q.get("ok")),
        "prices_requested": len(quotes),
        "fx": "; ".join(f"{k}={v[0]:.5g} ({v[1]})" for k, v in sorted(fx.items())),
    }
    if os.environ.get("SCREEN_WORKBOOK", "1") == "0":
        print("\nExcel results workbook skipped (SCREEN_WORKBOOK=0)")
        return None, results, ctxs, records
    from .report import write_outputs
    stamp = today.isoformat()
    out_name = out_name or f"screen_results_{stamp}.xlsx"
    out_path = os.path.join(OUTPUT_DIR, out_name)
    write_outputs(out_path, cfg, run_info, wanted, results, ctxs, records, cyc, today,
                  write_latest=not tickers or detail_all is False)
    print(f"\nResults saved to: {out_path}")
    return out_path, results, ctxs, records
