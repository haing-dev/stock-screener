"""Setup check: can we reach the SEC and Twelve Data, and do known numbers come out right?

Known answers are figures printed in the companies' own annual reports, so a mismatch means the data
pipeline is broken, not that the company changed."""
from datetime import date

from .extract import CompanyData, facts_subset
from .metrics import compute
from .sec import FACTS_URL, SUBMISSIONS_URL
from .valuation import value

KNOWN = [
    # (cik, ticker, fiscal-year label, concept, value, source)
    (320193, "AAPL", 2024, "revenue", 391_035_000_000, "Apple 10-K FY2024 (year to 28 Sep 2024): net sales $391,035M"),
    (320193, "AAPL", 2024, "net_income", 93_736_000_000, "Apple 10-K FY2024: net income $93,736M"),
    (789019, "MSFT", 2024, "revenue", 245_122_000_000, "Microsoft 10-K FY2024 (year to 30 Jun 2024): revenue $245,122M"),
    (789019, "MSFT", 2024, "operating_income", 109_433_000_000, "Microsoft 10-K FY2024: operating income $109,433M"),
]


def run_selfcheck(client, prices, cfg, today=None):
    today = today or date.today()
    ok_all = True

    def line(ok, msg):
        nonlocal ok_all
        ok_all &= bool(ok)
        print(("  OK    " if ok else "  FAIL  ") + msg)

    print("1) SEC EDGAR access and known answers")
    cds = {}
    for cik, t in sorted({(k[0], k[1]) for k in KNOWN}):
        try:
            client.get_json(SUBMISSIONS_URL.format(cik=cik))
            cf = client.get_json(FACTS_URL.format(cik=cik))
            cds[cik] = CompanyData(facts_subset(cf, today))
            line(True, f"downloaded {t} filings")
        except Exception as e:  # noqa: BLE001
            line(False, f"could not download {t}: {e}")
    for cik, t, fy, concept, want, src in KNOWN:
        cd = cds.get(cik)
        if not cd:
            continue
        got = cd.get(concept, fy)
        line(got is not None and abs(got - want) / want < 0.001,
             f"{t} FY{fy} {concept}: got {got:,.0f} vs {want:,.0f} ({src})" if got else f"{t} FY{fy} {concept}: missing")
    if 320193 in cds:
        cd = cds[320193]
        p = cd.ttm("revenue")
        if p:
            line(p.val > 3e11, f"AAPL trailing-12-month revenue {p.val / 1e9:,.1f}B to {p.end} ({p.method})")
        res, why = compute(cd, cfg, today)
        if res:
            m, _ = res
            line(m.get("dei_shares") or m.get("diluted_shares_latest"),
                 f"AAPL share count: cover page {m.get('dei_shares')} ({m.get('dei_shares_date')}), "
                 f"diluted {m.get('diluted_shares_latest')}")
    print("\n2) Twelve Data access")
    if not prices.available():
        line(False, "no 'twelvedata_api_key' in config.json")
        return ok_all
    try:
        u = prices.check_plan()
        line(isinstance(u, dict) and u.get("status") != "error",
             f"plan: {u.get('plan_category')}, {prices.per_minute} credits/minute, daily limit "
             f"{prices.daily_limit or 'n/a'}, used today {prices.daily_used}")
        if prices.per_minute <= 8:
            print("        Free/basic plan: a full run prices ~1,000-1,500 candidates, so it spreads over 2 days "
                  "(quotes are cached; just run again). A paid plan finishes in one go.")
    except Exception as e:  # noqa: BLE001
        line(False, f"Twelve Data: {e}")
        return ok_all
    q = prices.quotes([("AAPL", "Nasdaq"), ("BRK-B", "NYSE")], "Setup check")
    a = q.get("AAPL") or {}
    line(a.get("ok"), f"AAPL quote: ${a.get('price')} on {a.get('price_date')} from {a.get('exchange')} "
                      f"in {a.get('currency')}" + (f" - {a.get('reason')}" if a.get("reason") else ""))
    b = q.get("BRK-B") or {}
    line(b.get("ok"), f"BRK-B quote (share-class symbol mapping): ${b.get('price')} {b.get('exchange')}"
                      + (f" - {b.get('reason')}" if b.get("reason") else ""))
    if 320193 in cds and a.get("ok"):
        res, _ = compute(cds[320193], cfg, today)
        if res:
            m, _ = res
            v = value(m, {"all_tickers": ["AAPL"], "latest_annual": {"form": "10-K"}}, a, 1.0, today)
            line(v.get("val_ok"), f"AAPL market cap ${v.get('market_cap_usd', 0) / 1e9:,.0f}B "
                                  f"({v.get('shares_source')}); x public float = {v.get('mcap_to_public_float', 0):.2f}"
                                  + (f" - {v['val_issue']}" if v.get("val_issue") else ""))
    print("\nAll checks passed." if ok_all else "\nSome checks failed - see above. Send this output to Claude.")
    return ok_all
