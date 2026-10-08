"""Stock screener - thirteen screens on SEC filings + Twelve Data prices.

  python screener.py setup-check            check SEC access, your Twelve Data key/plan, and known answers
  python screener.py test                   quick run on ~40 well-known companies (5-10 minutes)
  python screener.py run                    all NYSE + Nasdaq companies, all thirteen screens
  python screener.py run --screens core,fortress      only some screens
  python screener.py run --tickers V,MA     only these tickers
  python screener.py check MCO              every rule of every screen for one company, with the evidence
  python screener.py aipack --screen core --top 30    blind 10-K evidence pack for the AI review
  python screener.py verify-quotes PACK_FOLDER/moat_scores.json PACK_FOLDER

Web portal (run by GitHub Actions - see README 'Web portal'):
  python screener.py portal-screen          full screen, every company priced (Massive), state saved
  python screener.py portal-daily           new end-of-day prices for the saved state, screens re-applied
  python screener.py portal-summaries --max 30    2-3 line company descriptions (Claude)
  python screener.py portal-export          write the encrypted data files for the site (site/data)

Screens: core, emerging, special, fortress, hc_commercial, hc_clinical, cyclicals,
         owners, real_assets, asset_floor, trough_cash, hidden, red_flags
"""
import argparse
import os
import sys

from qs.config import CACHE_DIR, OUTPUT_DIR, ensure_user_agent, load_config
from qs.sec import SECClient

TEST_TICKERS = [
    # core / fortress
    "MSFT", "AAPL", "V", "MA", "MCO", "SPGI", "ADP", "COST", "KO", "ODFL", "FICO", "WM", "RSG", "PG",
    # emerging-type growers
    "AXON", "CELH", "TMDX", "FTAI",
    # special situations (spin-offs / IPOs since 2023)
    "SOLV", "GEV", "VLTO", "SNDK", "RDDT", "ALAB",
    # healthcare
    "LLY", "JNJ", "VRTX", "ISRG", "TMO", "UNH", "SRPT", "ALLO",
    # cyclicals
    "NUE", "STLD", "CAT", "DOW", "LRCX", "XOM", "DHI",
    # second batch: owner-operators, royalties / land, cash-rich, cyclical cash
    "TPL", "RGLD", "BSM", "MLI", "UI", "WSO",
    # controls that must be excluded or fail
    "JPM", "T", "F", "INTC", "TSM", "ASML",
]
SCREEN_IDS = ["core", "emerging", "special", "fortress", "hc_commercial", "hc_clinical", "cyclicals",
              "owners", "real_assets", "asset_floor", "trough_cash", "hidden", "red_flags"]


def make_client(cfg):
    ua = ensure_user_agent(cfg)
    return SECClient(ua, per_sec=cfg.get("requests_per_second", 8),
                     fixtures_dir=os.environ.get("SCREENER_FIXTURES"))


def make_prices(cfg):
    from qs.prices import TwelveData
    fx = os.environ.get("SCREENER_FIXTURES")
    td = TwelveData(cfg.get("twelvedata_api_key", ""), CACHE_DIR, max_age_days=cfg.get("price_max_age_days", 3),
                    fixtures_dir=fx, max_stale_days=cfg.get("price_max_staleness_days", 7))
    if not td.available():
        print("NOTE: no Twelve Data API key in config.json - price-based rules will show 'NO DATA' and those "
              "companies go to the 'Check manually' lists.")
    return td


def make_portal_prices(cfg, daily=False):
    from qs.massive import Massive, PriceSource
    pc = cfg.get("portal") or {}
    key = cfg.get("massive_api_key") or os.environ.get("MASSIVE_API_KEY", "")
    m = Massive(key, CACHE_DIR, fixtures_dir=os.environ.get("SCREENER_FIXTURES"))
    if not m.available():
        print("NOTE: no Massive API key (MASSIVE_API_KEY) - prices come from Twelve Data only, for a few companies.")
    td = make_prices(cfg)
    n = pc.get("twelvedata_backup_quotes_daily" if daily else "twelvedata_backup_quotes_screen_run", 60)
    return PriceSource(m, td, td_fallback_max=n if m.available() else 10 ** 6,
                       max_stale_days=cfg.get("price_max_staleness_days", 7))


def cmd_portal_screen(args):
    from datetime import date
    from qs.pipeline import run_screens
    from qs.portal import save_state
    from qs import history
    from qs.portal import STATE_PATH, write_gz_json
    cfg = load_config()
    client = make_client(cfg)
    prices = make_portal_prices(cfg)
    models = {}
    out, results, ctxs, records = run_screens(client, cfg, prices=prices, price_all=True, models_out=models)
    run_info = {"workbook": os.path.basename(out)}
    state = save_state(results, ctxs, records, run_info, date.today(), models=models)
    print("Price history (52-week ranges, month-end prices for listed companies and peers)")
    history.update(state, prices, cfg, daily=False)
    write_gz_json(STATE_PATH, state)
    print("State saved for the daily price updates.")


def cmd_portal_daily(args):
    from datetime import date
    from qs.portal import STATE_PATH, load_state, reprice, write_gz_json
    state = load_state()
    if not state:
        from qs.portal import SALT_PATH
        if os.path.exists(SALT_PATH):
            # the portal was built before, so a saved screen should exist: say so loudly instead of going stale
            print("ERROR: the saved screen state is missing (GitHub cache and artifact both gone?). "
                  "Run the 'Screen' workflow by hand to rebuild it.")
            sys.exit(1)
        print("No saved screen yet - run the screen workflow first. Nothing to re-price.")
        return
    from qs import history
    cfg = load_config()
    prices = make_portal_prices(cfg, daily=True)
    reprice(state, prices, cfg, date.today())
    print("Price history (52-week ranges, month-end prices for listed companies and peers)")
    history.update(state, prices, cfg, daily=True)
    write_gz_json(STATE_PATH, state)


def cmd_portal_summaries(args):
    from qs.portal import load_state
    from qs.summaries import claude_available, run
    state = load_state()
    if not state:
        print("No saved screen yet - nothing to summarize.")
        return
    if not claude_available():
        print("Claude Code isn't installed or CLAUDE_CODE_OAUTH_TOKEN isn't set - summaries skipped.")
        return
    cfg = load_config()
    client = make_client(cfg)
    model = (cfg.get("portal") or {}).get("summary_model", "haiku")
    run(client, state, args.max, model=model)


def cmd_portal_export(args):
    from qs.portal import evaluate_state, export_site, load_state
    from qs.summaries import load_summaries
    state = load_state()
    if not state:
        print("No saved screen yet - nothing to export.")
        return
    cfg = load_config()
    results = evaluate_state(state, cfg)
    export_site(state, results, cfg, load_summaries(), os.environ.get("PORTAL_PASSWORD", "").strip(),
                allow_plain=args.allow_plain)


def _screens(arg):
    if not arg:
        return None
    out = [s.strip() for s in arg.split(",") if s.strip()]
    bad = [s for s in out if s not in SCREEN_IDS]
    if bad:
        raise SystemExit(f"Unknown screen(s): {', '.join(bad)}. Choose from: {', '.join(SCREEN_IDS)}")
    return out


def cmd_run(args, test=False):
    from qs.pipeline import run_screens
    cfg = load_config()
    client = make_client(cfg)
    tickers = TEST_TICKERS if test else ([t.strip().upper() for t in args.tickers.split(",") if t.strip()]
                                         if getattr(args, "tickers", None) else None)
    name = "test_results.xlsx" if test else None
    run_screens(client, cfg, tickers=tickers, out_name=name, screens=_screens(getattr(args, "screens", None)),
                prices=make_prices(cfg))


def cmd_check(args):
    from qs.pipeline import run_screens
    from qs.report import SHEET, _fmt_val
    from qs.screens import BY_ID
    cfg = load_config()
    client = make_client(cfg)
    t = args.ticker.upper()
    out, results, ctxs, records = run_screens(client, cfg, tickers=[t], out_name=f"check_{t}.xlsx",
                                              prices=make_prices(cfg), detail_all=True)
    if not records:
        return
    c = next(iter(records))
    rec = records[c]
    ctx = ctxs.get(c)
    print(f"\n{rec['ticker']} - {rec['name']}  |  {rec.get('industry')} (SIC {rec.get('sic')})  |  {rec['stage']}")
    if not ctx:
        return
    print(f"Latest FY {ctx.get('latest_fy')} (ends {ctx.get('latest_fy_end')}), TTM to {ctx.get('ttm_end')}, "
          f"balance sheet {ctx.get('bs_date')}, currency {ctx.get('currency')}")
    if ctx.get("price"):
        print(f"Price ${ctx['price']:.2f} ({ctx.get('price_date')}), market cap "
              f"{_fmt_val(ctx.get('market_cap_usd'), 'usd')}, shares: {ctx.get('shares_source')}"
              + (f"  [{ctx['val_issue']}]" if ctx.get("val_issue") else ""))
    for sid, res in results.items():
        r = res.get(c)
        s = BY_ID[sid]
        if not r:
            print(f"\n{SHEET[sid]}: outside this screen's universe")
            continue
        print(f"\n{SHEET[sid]} ({s.title}): {r['class']}" + (f"  - {r['universe_note']}" if r.get("universe_note") else ""))
        for g in s.gates:
            st, val, thr, note = r["gates"][g.gid]
            rule = f"{g.op or ''} {_fmt_val(thr, g.fmt)}" if thr is not None else ""
            print(f"  {g.gid:<4}{g.name:<30}{st:<8}{_fmt_val(val, g.fmt):>14}  {rule:<14} {note}")
        for h in r.get("holds", []):
            print(f"  HOLD: {h}")
    if ctx.get("flags"):
        print("\nFlags:\n  - " + "\n  - ".join(ctx["flags"]))
    print(f"\nEvery input, with a link to its SEC filing: {out.replace('.xlsx', '_evidence.csv')}")


def cmd_setup_check(args):
    from qs.selfcheck import run_selfcheck
    cfg = load_config()
    client = make_client(cfg)
    ok = run_selfcheck(client, make_prices(cfg), cfg)
    sys.exit(0 if ok else 1)


def cmd_aipack(args):
    from qs.aipack import build_pack
    cfg = load_config()
    client = make_client(cfg)
    build_pack(client, screen=args.screen, top=args.top, near=args.watch, blind=not args.not_blind)


def cmd_verify_quotes(args):
    from qs.quotes import verify
    verify(args.scores, args.pack)


def main():
    ap = argparse.ArgumentParser(description="SEC-based multi-strategy stock screener")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("setup-check", help="check SEC + Twelve Data access and known answers")
    sub.add_parser("test", help="quick run on ~40 well-known companies")
    r = sub.add_parser("run", help="full screen")
    r.add_argument("--tickers", help="comma-separated tickers (default: all NYSE + Nasdaq)")
    r.add_argument("--screens", help="comma-separated: " + ",".join(SCREEN_IDS))
    v = sub.add_parser("check", help="every rule of every screen for one company")
    v.add_argument("ticker")
    v2 = sub.add_parser("verify", help="same as check")
    v2.add_argument("ticker")
    a = sub.add_parser("aipack", help="build the 10-K evidence pack for the AI review")
    a.add_argument("--screen", default="core", choices=SCREEN_IDS)
    a.add_argument("--top", type=int, default=30)
    a.add_argument("--watch", type=int, default=0, help="also include this many from the watch list")
    a.add_argument("--not-blind", action="store_true", help="keep company names in the pack")
    q = sub.add_parser("verify-quotes", help="check AI-review quotes against the filings")
    q.add_argument("scores")
    q.add_argument("pack")
    sub.add_parser("portal-screen", help="web portal: full screen with every company priced")
    sub.add_parser("portal-daily", help="web portal: re-price the saved screen")
    ps = sub.add_parser("portal-summaries", help="web portal: company descriptions (Claude)")
    ps.add_argument("--max", type=int, default=30)
    sub.add_parser("portal-report", help="web portal: why companies are on 'check manually' (markdown)")
    pe = sub.add_parser("portal-export", help="web portal: write site/data")
    pe.add_argument("--allow-plain", action="store_true", help="local testing only: write unencrypted data")
    args = ap.parse_args()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if args.cmd == "test":
        cmd_run(args, test=True)
    elif args.cmd == "run":
        cmd_run(args)
    elif args.cmd in ("check", "verify"):
        cmd_check(args)
    elif args.cmd == "setup-check":
        cmd_setup_check(args)
    elif args.cmd == "aipack":
        cmd_aipack(args)
    elif args.cmd == "verify-quotes":
        cmd_verify_quotes(args)
    elif args.cmd == "portal-screen":
        cmd_portal_screen(args)
    elif args.cmd == "portal-daily":
        cmd_portal_daily(args)
    elif args.cmd == "portal-summaries":
        cmd_portal_summaries(args)
    elif args.cmd == "portal-export":
        cmd_portal_export(args)
    elif args.cmd == "portal-report":
        from qs.checkreport import build
        from qs.portal import load_state
        st = load_state()
        if not st:
            raise SystemExit("No saved screen state.")
        os.makedirs("reports", exist_ok=True)
        with open(os.path.join("reports", "check_report.md"), "w", encoding="utf-8") as f:
            f.write(build(st, load_config()))
        print("reports/check_report.md written")
    else:
        ap.print_help()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped. Progress is cached - run the same command again to continue.")
        sys.exit(1)
