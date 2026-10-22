"""python -m triage.run <step>

Steps (each resumable; work kept under cache/tri and cache/bt):
  prices    Massive scan grid (mid-month and month-end + next trading day) for MASSIVE_HISTORY_YEARS, tickers incl. delisted,
            splits, dividends; the US universe of each month (NYSE, Nasdaq, NYSE American)
  prepare   SEC bulk files -> point-in-time facts and filing histories of every company in the universe
  panel     point-in-time metrics per company and month (qs/backtest company pass) -> cache/tri/panel
  returns   month-to-month returns of every panel company and the index ETFs
  owners    13F conviction holdings and Form 4 insider trades from SEC's data sets
  mark      the latest trading day's closes (one Massive request)
  build     events, calls, outcomes, statistics -> cache/tri/out/site.json.gz
  site      the static site (triage_site/), data encrypted with PORTAL_PASSWORD
  monthly   everything above, in order (a full scan: after each mid-month and month-end)
  daily     mark, build, site
  auto      a full scan when a new scan date (15th or month-end) has settled, else daily
"""
import argparse
import os
import sys
from datetime import date, timedelta

from qs.backtest_support import read_json

from . import panel as PN
from . import paths as P


def _cfg():
    from qs.config import load_config
    return load_config()


def _massive(cfg):
    from qs.config import CACHE_DIR
    from qs.massive import Massive
    key = os.environ.get("MASSIVE_API_KEY") or cfg.get("massive_api_key") or ""
    return Massive(key, CACHE_DIR, per_minute=int(os.environ.get("MASSIVE_PER_MINUTE", "5")))


def _client(cfg):
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from screener import make_client
    return make_client(cfg)


def _months_back(today, years):
    y, m = today.year - years, today.month + 1
    if m > 12:
        y, m = y + 1, 1
    return y, m


def step_prices(cfg, log=print):
    from qs.btprices import BTPrices
    m = _massive(cfg)
    if not m.available():
        raise SystemExit("MASSIVE_API_KEY is not set (GitHub secret).")
    btp = BTPrices(m, log=log)
    today = m.today
    years = int(os.environ.get("MASSIVE_HISTORY_YEARS", "2"))
    start = _months_back(today, years)
    log(f"Scan grid (mid-month and month-end) from {start[0]}-{start[1]:02d} (Massive history: {years} years)")
    grid = PN.scan_grid(btp, start, today)
    btp.tickers()
    since = date(start[0], start[1], 1) - timedelta(days=800)
    btp.splits(since.isoformat())
    btp.dividends(date(start[0], start[1], 1).isoformat())
    univ, left = {}, {}
    for g in grid:
        univ[g["d"]] = {str(c): u for c, u in btp.universe(g["d"], g["bars_d"], PN.EXCHANGES, left).items()}
    PN.save_grid(grid, univ)
    log(f"  {len(grid)} scans; left out (all scans): " + ", ".join(f"{k} {v}" for k, v in sorted(left.items())))
    return grid


def _grid_and_actions(cfg, log=print):
    from qs.btprices import BTPrices
    m = _massive(cfg)
    btp = BTPrices(m, log=log)
    grid = PN.load_grid(btp)
    if not grid:
        raise SystemExit("No price grid yet - run 'prices' first.")
    first = date.fromisoformat(grid[0]["d"])
    splits = btp.splits((first - timedelta(days=800)).isoformat())
    divs = btp.dividends(first.replace(day=1).isoformat())
    return m, btp, grid, splits, divs


def step_prepare(cfg, log=print):
    from qs.btdata import prepare
    univ = PN.load_univ()
    ciks = sorted({c for us in univ.values() for c in us})
    log(f"Point-in-time SEC data for {len(ciks)} companies")
    prepare(_client(cfg), ciks, log=log, refresh=True)


def step_panel(cfg, log=print):
    from qs.backtest import run_company_pass
    from qs.btdata import load_facts, load_filings
    _m, _btp, grid, splits, _divs = _grid_and_actions(cfg, log)
    univ = PN.load_univ()
    run_company_pass(grid, univ, cfg, load_facts, load_filings, log=log)
    PN.build(grid, univ, cfg, splits, log=log)


def step_returns(cfg, log=print):
    from . import returns as RT
    _m, btp, grid, splits, divs = _grid_and_actions(cfg, log)
    RT.build(grid, btp, splits, divs, log=log, budget=int(os.environ.get("LAST_CLOSE_BUDGET", "300")))


def _name_map():
    """{cik: {'ticker', 'name', 'other_tickers'}} over every panel month (13F CUSIP mapping)."""
    out = {}
    for ym in PN.months():
        for c, r in ((PN.load(ym) or {}).get("companies") or {}).items():
            out[int(c)] = {"ticker": r.get("tk"), "name": r.get("nm"), "other_tickers": ",".join(r.get("tks") or [])}
    return out


def step_owners(cfg, log=print):
    from . import owners as OW
    months = PN.months()
    if not months:
        raise SystemExit("No panel yet - run 'panel' first.")
    y, m = int(months[0][:4]), int(months[0][5:7])
    since = date(y - 1, m, 1).isoformat()
    client = _client(cfg)
    today = date.today()
    nm = _name_map()
    OW.update_13f(client, nm, cfg, since, today, log=log, max_sets=int(os.environ.get("TRIAGE_13F_SETS", "12")))
    OW.update_insiders(client, set(nm), since, today, log=log)


def step_mark(cfg, log=print):
    return PN.mark(_massive(cfg), log=log)


def step_build(cfg, log=print):
    from qs.validate import factors
    from . import build as B
    m, btp, grid, splits, divs = _grid_and_actions(cfg, log)
    mark = PN.load_mark()
    last = grid[-1]
    opens = {s: b[0] for s, b in (last.get("bars_e") or {}).items() if b and b[0]}
    try:
        fac = factors(log=log)
    except Exception as e:  # noqa: BLE001 - the regression is left out, everything else still builds
        log(f"  factor data unavailable ({e}); regressions left out")
        fac = {}
    client = None
    try:
        client = _client(cfg)
    except SystemExit:
        log("  no SEC user agent: recent insider trades stay TBU")
    B.build(grid=[{k: g[k] for k in ("ym", "d", "e")} for g in grid], mark=mark, opens=opens, splits=splits,
            divs=divs, factors=fac, client=client, record_dir=os.environ.get("TRIAGE_RECORD_DIR"), log=log)


def step_site(cfg, log=print):
    from . import site as S
    S.build(os.environ.get("PORTAL_PASSWORD", ""), log=log, allow_plain=os.environ.get("TRIAGE_ALLOW_PLAIN") == "1")


STEPS = {"prices": step_prices, "prepare": step_prepare, "panel": step_panel, "returns": step_returns,
         "owners": step_owners, "mark": step_mark, "build": step_build, "site": step_site}
MONTHLY = ["prices", "prepare", "panel", "returns", "owners", "mark", "build", "site"]
DAILY = ["mark", "build", "site"]


def _done_path():
    return os.path.join(P.TRI, "scan_done.json.gz")


def needs_monthly():
    """True until a full run has finished for the latest scan date (mid-month or month-end; an interrupted run
    resumes)."""
    return ((read_json(_done_path()) or {}).get("scan") or "") < PN.latest_scan(date.today()).isoformat()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=list(STEPS) + ["monthly", "daily", "auto"])
    a = ap.parse_args(argv)
    P.ensure(P.TRI)
    cfg = _cfg()
    steps = MONTHLY if a.step == "monthly" else DAILY if a.step == "daily" else \
        (MONTHLY if needs_monthly() else DAILY) if a.step == "auto" else [a.step]
    print(f"Triage steps: {', '.join(steps)}", flush=True)
    for s in steps:
        print(f"== {s}", flush=True)
        STEPS[s](cfg)
    if steps == MONTHLY:
        from qs.backtest_support import write_json
        write_json(_done_path(), {"scan": PN.latest_scan(date.today()).isoformat(), "at": date.today().isoformat()})


if __name__ == "__main__":
    main()
