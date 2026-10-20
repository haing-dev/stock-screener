"""`python screener.py validate <step>` - the validation run of validation/PROTOCOL.md.

Steps (each resumable; 'all' runs them in order):
  prices    Massive monthly grid (month-end + next trading day), ticker reference incl. delisted, splits, dividends
  prepare   SEC bulk files -> point-in-time facts and filing histories for every company of the price universe
  backtest  company pass, formations (every screen, threshold grid, leave-one-gate-out), returns
  stats     factors (Kenneth French), statistics and verdicts -> validation/out/stats.json; forward record
  audit     reconciliation against SEC's Financial Statement Data Sets, rule and star review sheets
  fidelity  the quoted managers' 13F holdings against 'their' screens
  report    validation/out/report.md
"""
import json
import os
from datetime import date, timedelta

from .backtest import FORM_DIR, RET_DIR, run_company_pass, run_formations, run_returns
from .backtest_support import OUT, WORK, ensure_dirs, read_json, write_json
from .btprices import BTPrices

PREREG_DATE = "2026-10-20"
FRENCH = {"ff5": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip",
          "mom": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip"}
GRID_PATH = os.path.join(WORK, "grid.json.gz")
UNIV_PATH = os.path.join(WORK, "universe.json.gz")


def _ym(s):
    return int(s[:4]), int(s[5:7])


def _months_back(today, years):
    y, m = today.year - years, today.month + 1
    if m > 12:
        y, m = y + 1, 1
    return y, m


def _massive(cfg):
    from .config import CACHE_DIR
    from .massive import Massive
    key = os.environ.get("MASSIVE_API_KEY") or cfg.get("massive_api_key") or ""
    vc = cfg.get("validation") or {}
    return Massive(key, CACHE_DIR, per_minute=int(os.environ.get("MASSIVE_PER_MINUTE", vc.get("massive_per_minute", 5))))


def step_prices(args, cfg, log=print):
    m = _massive(cfg)
    if not m.available():
        raise SystemExit("MASSIVE_API_KEY is not set (GitHub secret).")
    btp = BTPrices(m, log=log)
    today = m.today
    years = int(os.environ.get("MASSIVE_HISTORY_YEARS", "2"))
    start = _ym(args.start) if getattr(args, "start", None) else _months_back(today, years)
    last_full = today.replace(day=1) - timedelta(days=1)
    end = _ym(args.end) if getattr(args, "end", None) else (last_full.year, last_full.month)
    log(f"Price grid {start[0]}-{start[1]:02d} .. {end[0]}-{end[1]:02d} (Massive history: {years} years)")
    grid = btp.grid(start, end)
    log(f"  {len(grid)} months with prices")
    btp.tickers()
    since = date(start[0], start[1], 1) - timedelta(days=800)
    btp.splits(since.isoformat())
    btp.dividends(date(start[0], start[1], 1).isoformat())
    univ, left = {}, {}
    for g in grid:
        univ[g["d"]] = {str(c): u for c, u in btp.universe(g["d"], g["bars_d"], cfg["exchanges"], left).items()}
    log("  left out of the universe (all months): " + ", ".join(f"{k} {v}" for k, v in sorted(left.items())))
    write_json(GRID_PATH, [{k: g[k] for k in ("ym", "d", "e")} for g in grid])
    write_json(UNIV_PATH, univ)
    log(f"  universe: {min(len(u) for u in univ.values()) if univ else 0}-{max(len(u) for u in univ.values()) if univ else 0} "
        "companies per month")
    return grid


def load_grid(btp):
    idx = read_json(GRID_PATH) or []
    out = []
    for g in idx:
        out.append(dict(g, bars_d=btp.bars(g["d"]), bars_e=btp.bars(g["e"])))
    return out


def load_univ():
    raw = read_json(UNIV_PATH) or {}
    return {d: {int(c): u for c, u in us.items()} for d, us in raw.items()}


def step_prepare(args, cfg, client, log=print):
    from .btdata import prepare
    univ = load_univ()
    ciks = sorted({c for us in univ.values() for c in us})
    log(f"Point-in-time SEC data for {len(ciks)} companies")
    # rewritten every run from the newest bulk files: later months need the filings made since the last run
    prepare(client, ciks, log=log, refresh=True)


def step_backtest(args, cfg, log=print):
    from .btdata import load_facts, load_filings
    m = _massive(cfg)
    btp = BTPrices(m, log=log)
    grid = load_grid(btp)
    univ = load_univ()
    if not grid:
        raise SystemExit("No price grid yet - run 'validate prices' first.")
    first = date.fromisoformat(grid[0]["d"])
    splits = btp.splits((first - timedelta(days=800)).isoformat())
    divs = btp.dividends(first.replace(day=1).isoformat())
    run_company_pass(grid, univ, cfg, load_facts, load_filings, log=log)
    run_formations(grid, univ, cfg, splits, log=log)
    # missing exit prices: portfolio members first (any screen's PASS or NEAR)
    pri = {}
    for g in grid:
        f = read_json(os.path.join(FORM_DIR, f"{g['ym']}.json.gz")) or {}
        pri[g["ym"]] = {c for res in (f.get("screens") or {}).values() for c, r in res.items()
                        if r[0] in ("PASS", "NEAR")}
    budget = int(os.environ.get("LAST_CLOSE_BUDGET", (cfg.get("validation") or {}).get("last_close_budget", 300)))
    spent = run_returns(grid, btp, splits, divs, log=log, last_close_budget=budget, priority=pri)
    log(f"  {spent} last-close lookups for companies without a next-month price")


def factors(log=print):
    import requests
    from .btstats import merge_factors, parse_french
    path = os.path.join(WORK, "factors.json.gz")
    hit = read_json(path)
    if hit and hit.get("fetched", "") >= (date.today() - timedelta(days=20)).isoformat():
        return hit["f"]
    raw = {}
    for k, url in FRENCH.items():
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        raw[k] = parse_french(r.content)
    f = merge_factors(raw["ff5"], raw["mom"])
    write_json(path, {"fetched": date.today().isoformat(), "f": f})
    log(f"Factors: {len(f)} months, latest {max(f) if f else None}")
    return f


def load_panel(after=None):
    from .btanalysis import Panel
    months = []
    files = sorted(f for f in os.listdir(FORM_DIR) if f.endswith(".json.gz")) if os.path.isdir(FORM_DIR) else []
    for fn in files:
        ym = fn[:7]
        if after and ym < after:
            continue
        rets = read_json(os.path.join(RET_DIR, fn))
        form = read_json(os.path.join(FORM_DIR, fn))
        if rets is None or form is None:
            continue
        months.append((form, rets))
    return Panel(months)


def forward_panel(panel, history_dir, log=print):
    """The live lists recorded on branch 'history' after pre-registration, put in place of the reconstructed lists
    (same months, same universes, same returns). Also returns the live-vs-reconstruction agreement per screen."""
    from .btanalysis import Panel
    from .listlog import load_all
    snaps = [s for s in load_all(history_dir) if s.get("date", "") >= PREREG_DATE] if history_dir else []
    if not snaps:
        return None, {}
    months, agree = [], {}
    for form, rets in panel.months:
        d = form["d"]
        cand = [s for s in snaps if s["date"] <= d and (date.fromisoformat(d) - date.fromisoformat(s["date"])).days <= 20]
        if not cand:
            continue
        snap = cand[-1]
        f2 = dict(form)
        f2["screens"] = {}
        for sid, res in form["screens"].items():
            live = snap["screens"].get(sid) or {}
            p = {str(r[0]) for r in live.get("pass", [])}
            st = {str(r[0]) for r in live.get("star", [])}
            nr = {str(r[0]) for r in live.get("near", [])}
            new = {}
            for c, r in res.items():
                cls = "PASS" if (c in p or c in st) else ("NEAR" if c in nr else "FAIL")
                new[c] = [cls, c in st, r[2], r[3], r[4]]
            f2["screens"][sid] = new
            rec = {c for c, r in res.items() if r[0] == "PASS"}
            lv = p | st
            j = len(rec & lv) / len(rec | lv) if (rec | lv) else None
            agree.setdefault(sid, []).append(j)
        f2["grid"], f2["loo"] = {}, {}
        months.append((f2, rets))
    log(f"Forward record: {len(months)} months of live lists after {PREREG_DATE}")
    return (Panel(months) if months else None), {k: [x for x in v if x is not None] for k, v in agree.items()}


def step_stats(args, cfg, log=print):
    from .btanalysis import analyse
    from .freeze import compare
    f = factors(log)
    panel = load_panel()
    log(f"Backtest panel: {len(panel.months)} months")
    res = analyse(panel, f)
    res["preregistration"] = compare()
    hist = os.environ.get("HISTORY_DIR")
    fp, agree = forward_panel(panel, hist, log) if hist else (None, {})
    if fp is not None:
        res["forward"] = analyse(fp, f)
    res["live_vs_reconstruction_jaccard"] = {k: (sum(v) / len(v) if v else None) for k, v in agree.items()}
    ensure_dirs(OUT)
    with open(os.path.join(OUT, "stats.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, default=str)
    log("validation/out/stats.json written")
    return res


def step_audit(args, cfg, client, log=print):
    from .audit import run
    summ = run(client, cfg, log=log)
    if summ:
        with open(os.path.join(OUT, "audit_summary.json"), "w", encoding="utf-8") as fh:
            json.dump(summ, fh, indent=1)


def step_fidelity(args, cfg, client, log=print):
    from .audit import latest_formation
    from .fidelity import run
    run(client, latest_formation(), date.today(), log=log)


def export_raw(log=print):
    """The raw outputs anyone can recompute every portfolio from: monthly lists per screen and monthly returns."""
    import csv
    import gzip
    ensure_dirs(OUT)
    files = sorted(f for f in os.listdir(FORM_DIR) if f.endswith(".json.gz")) if os.path.isdir(FORM_DIR) else []
    with gzip.open(os.path.join(OUT, "lists.csv.gz"), "wt", newline="") as fl, \
            gzip.open(os.path.join(OUT, "returns.csv.gz"), "wt", newline="") as fr:
        wl, wr = csv.writer(fl), csv.writer(fr)
        wl.writerow(["formation_month", "formation_day", "screen", "cik", "ticker", "class", "star", "rules_failed",
                     "rules_met", "rules_checked"])
        wr.writerow(["formation_month", "entry_day", "cik", "ticker", "return_next_month", "exit"])
        for fn in files:
            f = read_json(os.path.join(FORM_DIR, fn))
            r = read_json(os.path.join(RET_DIR, fn)) or {}
            if not f:
                continue
            comp = f["companies"]
            for sid, res in f["screens"].items():
                for c, x in res.items():
                    wl.writerow([f["ym"], f["d"], sid, c, comp.get(c, {}).get("tk"), x[0], int(x[1]), x[2], x[3], x[4]])
            for c, (ret, how) in r.items():
                wr.writerow([f["ym"], f["e"], c, comp.get(c, {}).get("tk"), ret, how])
    log(f"raw outputs: {len(files)} months in validation/out/lists.csv.gz and returns.csv.gz")


def step_report(args, cfg, log=print):
    from .valreport import write_report
    export_raw(log)
    path = write_report(cfg)
    log(f"{path} written")


def run(args, cfg):
    from .sec import SECClient
    ua = os.environ.get("SEC_USER_AGENT") or cfg.get("user_agent") or ""
    steps = ["prices", "prepare", "backtest", "stats", "audit", "fidelity", "report"] if args.step == "all" \
        else [args.step]
    client = None
    for st in steps:
        print(f"\n=== validate {st}")
        if st in ("prepare", "audit", "fidelity") and client is None:
            client = SECClient(ua)
        if st == "prices":
            step_prices(args, cfg)
        elif st == "prepare":
            step_prepare(args, cfg, client)
        elif st == "backtest":
            step_backtest(args, cfg)
        elif st == "stats":
            step_stats(args, cfg)
        elif st == "audit":
            step_audit(args, cfg, client)
        elif st == "fidelity":
            step_fidelity(args, cfg, client)
        elif st == "report":
            step_report(args, cfg)
