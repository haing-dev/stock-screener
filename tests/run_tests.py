"""Offline self-test: synthetic companies with known answers for every screen, plus real SEC data samples.

    python tests/run_tests.py
"""
import gzip
import json
import os
import shutil
import sys
import tempfile
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tests"))

import make_fixtures  # noqa: E402

TMP = tempfile.mkdtemp(prefix="qs_test_")
make_fixtures.FX = os.path.join(TMP, "fixtures")
make_fixtures.main()
os.environ["SCREENER_FIXTURES"] = make_fixtures.FX

import qs.config as qc  # noqa: E402
qc.CACHE_DIR = os.path.join(TMP, "cache")
qc.OUTPUT_DIR = os.path.join(TMP, "output")
import qs.aipack as qa  # noqa: E402
import qs.pipeline as qp  # noqa: E402
qp.CACHE_DIR, qp.OUTPUT_DIR = qc.CACHE_DIR, qc.OUTPUT_DIR
qa.CACHE_DIR, qa.OUTPUT_DIR = qc.CACHE_DIR, qc.OUTPUT_DIR
from qs.extract import CompanyData, fy_label  # noqa: E402
from qs.metrics import compute  # noqa: E402
import qs.metrics as qm  # noqa: E402
import qs.screens as qs_screens  # noqa: E402
from qs.prices import TwelveData, td_symbol  # noqa: E402
from qs.quotes import verify  # noqa: E402
from qs.screens import BY_ID  # noqa: E402
from qs.sec import SECClient  # noqa: E402
from qs.valuation import value  # noqa: E402

failures = []


def check(name, cond, detail=""):
    print(("  ok   " if cond else "  FAIL ") + name + (f"  ({detail})" if detail else ""))
    if not cond:
        failures.append(name)


def close(a, b, tol=1e-3):
    return a is not None and b is not None and abs(a - b) <= tol


TODAY = date(2025, 6, 30)
cfg = qc.load_config()
client = SECClient("test test@example.com", fixtures_dir=make_fixtures.FX)
prices = TwelveData("", qc.CACHE_DIR, fixtures_dir=make_fixtures.FX, today=TODAY, log=lambda *a: None)
out, results, ctxs, records = qp.run_screens(client, cfg, today=TODAY, prices=prices)
T = {x["ticker"]: c for c, x in ctxs.items()}
R = {r["ticker"]: r for r in records.values()}


def cls(screen, t):
    r = results[screen].get(T.get(t))
    return r["class"] if r else "outside"


print("\nUniverse and data")
check("OTC company not in universe", "OTCC" not in R)
check("bank not screened anywhere", R["BANK"]["stage"].startswith("not screened"))
check("waste management (SIC 4953) kept in (not a utility)", "FORT" in T)
g = ctxs[T["GOOD"]]
check("revenue CAGR = 10% across tag switch (SalesRevenueNet -> ASC 606 tag)", close(g["revenue_cagr"], 0.10, 1e-6))
nopat = 0.35 * (1 - 0.21)
ic_avg = 0.6 * (1 + 1 / 1.1) / 2
check("ROIC = NOPAT / avg invested capital", close(g["roic_median"], nopat / ic_avg, 1e-4),
      f"{g['roic_median']:.4f} vs {nopat / ic_avg:.4f}")
ni = 0.35 * 0.79
check("FCF conversion after stock pay: (FCF - SBC) / net income", close(g["fcf_conversion"], (1.15 * ni - 0.02 - 0.02) / ni, 1e-4),
      str(g["fcf_conversion"]))
check("share count CAGR is split-proof (-2%/yr despite 2:1 split)", close(g["share_count_cagr"], -0.02, 1e-6),
      f"{g['share_count_cagr']}")
check("inflation test: gross margin change 2021->2023 = +2pp", close(g["gross_margin_change_2021_2023"], 0.02, 1e-9))
fs = qp.load_cached_facts(T["GOOD"])
cd = CompanyData(fs)
rev24 = 1000e6 * 1.1 ** 12
check("annual revenue ignores 10-Q figures", close(cd.get("revenue", 2024) / 1e6, rev24 / 1e6, 1e-3))
check("restated 2019 revenue: latest filing wins", close(cd.get("revenue", 2019) / 1e6, 1000 * 1.1 ** 7, 1e-3))
check("TTM revenue = FY2024 + Q1-2025 - Q1-2024", close(g["ttm_revenue"] / 1e6, rev24 * 1.025 / 1e6, 1e-2),
      f"{g['ttm_revenue'] / 1e6:.1f} vs {rev24 * 1.025 / 1e6:.1f}")
check("year-to-date revenue growth = 10%", close(g["ytd_revenue_growth"], 0.10, 1e-6))
check("latest balance sheet is the 10-Q (2025-03-31)", g["bs_date"] == "2025-03-31")
check("January fiscal year labelled as prior year", ctxs[T["JANF"]]["latest_fy"] == 2024 and fy_label("2025-01-26") == 2024)
check("negative equity company still gets ROIC (operating capital)", ctxs[T["NEGQ"]]["roic_median"] > 0.3)
check("negative equity flagged", any("negative equity" in f for f in ctxs[T["NEGQ"]]["flags"]))
check("serial acquirer flagged", any("serial acquirer" in f for f in ctxs[T["JANF"]]["flags"]))
check("IFRS filer parsed in TWD with live FX", ctxs[T["IFRS"]]["currency"] == "TWD" and
      close(ctxs[T["IFRS"]]["fx_rate"], 0.031, 1e-9))
check("capex under a non-standard tag is found by the fallback (and flagged)",
      ctxs[T["ALTX"]]["fcf_conversion"] is not None and any("non-standard tag" in f for f in ctxs[T["ALTX"]]["flags"]))
check("recession test: SHOK revenue = trend x shock vs prior year (2009: 1.06 x 0.95 - 1; 2020: 1.06 x 0.70 - 1)",
      close(ctxs[T["SHOK"]]["recession_2009_revenue_change"], 1.06 * 0.95 - 1, 1e-3) and
      close(ctxs[T["SHOK"]]["recession_2020_revenue_change"], 1.06 * 0.70 - 1, 1e-3),
      f"{ctxs[T['SHOK']]['recession_2009_revenue_change']}, {ctxs[T['SHOK']]['recession_2020_revenue_change']}")
check("cash runway: BIOX = (cash after Q1 burn) / annual burn",
      close(ctxs[T["BIOX"]]["cash_runway_years"], (500 - 25) / 100, 1e-3), f"{ctxs[T['BIOX']]['cash_runway_years']}")

check("biotech with NO revenue tags is still screened (pre-revenue book)", "NREV" in T and
      cls("hc_clinical", "NREV") == "PASS", cls("hc_clinical", "NREV"))
check("debt missing from the latest 10-Q falls back to the annual figure (no fake net cash)",
      "annual report" in ctxs[T["LEVR"]]["bs_debt_source"] and cls("fortress", "LEVR") == "FAIL")
check("new spin-off with no financials yet is CHECK on Special Situations, not dropped",
      cls("special", "NEWS") == "CHECK", cls("special", "NEWS"))
check("...and doesn't appear on other screens", cls("core", "NEWS") == "outside")
check("52/53-week year ending 2019-06-01 labelled 2018; 2020-05-30 labelled 2019",
      fy_label("2019-06-01") == 2018 and fy_label("2020-05-30") == 2019 and fy_label("2020-06-30") == 2020)
mc = CompanyData({"facts": {"us-gaap": {"Revenues": {"USD": [{"start": "2023-01-01", "end": "2023-12-31", "val": 1,
                                                               "form": "10-K", "filed": "2024-02-01", "accn": "a"}]}},
                            "dei": {"EntityCommonStockSharesOutstanding": {"shares": [
                                {"end": "2024-04-20", "val": 300, "accn": "q", "form": "10-Q", "filed": "2024-05-01"},
                                {"end": "2024-04-20", "val": 100, "accn": "q", "form": "10-Q", "filed": "2024-05-01"}]}}}})
check("share classes on the cover page are summed", mc.dei_latest("EntityCommonStockSharesOutstanding")["val"] == 400)
from qs.valuation import common_classes, primary_ticker  # noqa: E402
check("preferreds/warrants aren't share classes; BRK-A/BRK-B are",
      primary_ticker(["BAC", "BAC-PB"]) == "BAC" and len(common_classes(["BRK-B", "BRK-A"])) == 2
      and len(common_classes(["XYZ", "XYZ-WS"])) == 1)

print("\nPrices and valuation")
q = {"symbol": "X", "currency": "EUR", "exchange": "XETR", "close": "10", "datetime": "2025-06-27"}
check("quote in EUR from a German exchange is rejected", not TwelveData._validate(q, "X", 7, TODAY)["ok"])
q = {"symbol": "X", "currency": "USD", "exchange": "NYSE", "close": "10", "datetime": "2025-05-01"}
check("stale quote is rejected", not TwelveData._validate(q, "X", 7, TODAY)["ok"])
q = {"symbol": "X", "currency": "USD", "exchange": "NASDAQ", "close": "10", "datetime": "2025-06-27"}
check("good US quote accepted", TwelveData._validate(q, "X", 7, TODAY)["ok"])
check("share-class symbol mapping BRK-B -> BRK.B", td_symbol("BRK-B") == "BRK.B")
e = ctxs[T["EMRG"]]
check("market cap = price x cover-page shares", close(e["market_cap_usd"], 18.0 * 60e6, 1))
check("EV = market cap + debt - cash", close(e["ev_usd"], e["market_cap_usd"] + e["bs_debt"] - e["bs_cash_and_sti"], 1))
check("EV/EBITDA uses TTM EBITDA", close(e["ev_ebitda"], e["ev_usd"] / e["ttm_ebitda"], 1e-9))
bad = value(dict(e, pf_close=None), {"all_tickers": ["A", "B"], "latest_annual": {"form": "10-K"}},
            {"ok": True, "price": 18.0 * 1500, "price_date": "2025-06-27"}, 1.0, TODAY)
check("market cap far from the reported public float is held for checking (share-class mix-up)",
      not bad["val_ok"] and "public float" in bad["val_issue"])
check("...and the doubtful market cap can't pass or fail a rule (kept only for display)",
      bad["market_cap_usd"] is None and bad["market_cap_usd_unverified"] is not None)
check("20-F issuer market cap marked unverified (ADR ratio)", "ADR" in (ctxs[T["IFRS"]].get("val_issue") or ""))

print("\nScreens")
expect = {
    "core": {"GOOD": "PASS", "RIVL": "PASS", "PHRM": "PASS", "SLOW": "ONE", "LEVR": "ONE", "LOSS": "FAIL",
             "NEAR": "NEAR", "NCPX": "CHECK", "ALTX": "CHECK", "STEL": "outside", "BANK": "outside"},
    "emerging": {"EMRG": "PASS", "DILU": "ONE", "PRCY": "PRICE", "GOOD": "FAIL", "BIOX": "FAIL"},
    "special": {"SPIN": "PASS", "REOR": "PASS", "NIPO": "FAIL", "GOOD": "outside"},
    "fortress": {"FORT": "PASS", "SHOK": "FAIL", "GOOD": "CHECK", "NCPX": "CHECK", "LEVR": "FAIL"},
    "hc_commercial": {"PHRM": "PASS", "BIOX": "FAIL", "GOOD": "outside"},
    "hc_clinical": {"BIOX": "PASS", "BURN": "FAIL", "PHRM": "outside"},
    "cyclicals": {"STEL": "PASS", "STL2": "ONE", "PEAK": "FAIL", "GOOD": "outside"},
    # second batch
    "owners": {"OWNR": "PASS", "GOOD": "FAIL", "STEL": "outside", "BANK": "outside"},
    "real_assets": {"ROYL": "PASS", "OILP": "FAIL", "GOOD": "outside"},
    "asset_floor": {"CASH": "PASS", "GOOD": "FAIL", "BANK": "outside"},
    "trough_cash": {"TRGH": "PASS", "PEAK": "FAIL", "GOOD": "outside"},
    "hidden": {"SPUN": "PASS", "DROP": "PASS", "GOOD": "FAIL", "BANK": "outside"},
    "red_flags": {"HYPE": "PASS", "EMRG": "FAIL", "GOOD": "FAIL", "BIOX": "outside"},
}
for sid, exp in expect.items():
    for t, want in exp.items():
        got = cls(sid, t)
        r = results[sid].get(T.get(t))
        check(f"{sid}: {t} -> {want}", got == want, f"got {got}" + (f" {r['failed']} {r['check_notes'][:2]}" if r else ""))
check("NCPX: missing capex is a CHECK with the reason, not a FAIL",
      "capital expenditure" in " ".join(results["core"][T["NCPX"]]["check_notes"]))
check("emerging DILU fails on dilution only", results["emerging"][T["DILU"]]["failed"] == ["E8"])
check("emerging PRCY fails on valuation only", results["emerging"][T["PRCY"]]["failed"] == ["E12"])
check("fortress SHOK fails the 2020 test", "F4" in results["fortress"][T["SHOK"]]["failed"])
check("clinical BURN fails runway", results["hc_clinical"][T["BURN"]]["failed"] == ["B2"])
check("cyclicals PEAK fails 'not at peak margins'", "C7" in results["cyclicals"][T["PEAK"]]["failed"])
check("PEAK flagged as an over-earner", ctxs[T["PEAK"]]["over_earning"] is True)
check("event detection: spin-off, bankruptcy, IPO",
      "spin-off" in ctxs[T["SPIN"]]["event_types"] and "bankruptcy" in ctxs[T["REOR"]]["event_types"]
      and "IPO" in ctxs[T["NIPO"]]["event_types"])
check("old-history company with an S-1 is not called an IPO", "IPO" not in (ctxs[T["GOOD"]].get("event_types") or ""))
check("steel industry signal computed from 3 companies",
      ctxs[T["STEL"]].get("industry_margin_percentile") is not None)
check("robustness flag computed for passes", results["core"][T["GOOD"]].get("robust") in (True, False))
o = ctxs[T["OWNR"]]
check("owners: insider share = 1 - public float / value on the float date (45%)",
      close(o.get("insider_share"), 0.45, 1e-6), o.get("insider_share"))
_is = ctxs[T["ISSU"]]
check("owners: insider share uses the shares outstanding at the float date (6%, not 25% after an issue)",
      close(_is.get("insider_share"), 1 - 75 / 80, 1e-6) and results["owners"][T["ISSU"]]["class"] == "FAIL",
      (_is.get("insider_share"), _is.get("insider_basis")))
check("owners: a 10% insider stake fails the defining rule", results["owners"][T["GOOD"]]["failed"][:1] == ["O4"]
      or "O4" in results["owners"][T["GOOD"]]["failed"], results["owners"][T["GOOD"]]["failed"])
check("hard assets: a capex-heavy producer fails 'little reinvestment'",
      "R4" in results["real_assets"][T["OILP"]]["failed"])
check("asset floor: market cap below net cash", ctxs[T["CASH"]]["mcap_to_net_cash"] < 1.0,
      ctxs[T["CASH"]]["mcap_to_net_cash"])
check("trough cash: PEAK fails 'margins below normal'", "T4" in results["trough_cash"][T["PEAK"]]["failed"])
check("trough cash: 5-year average FCF yield computed", ctxs[T["TRGH"]].get("fcf_yield_5y", 0) >= 0.10,
      ctxs[T["TRGH"]].get("fcf_yield_5y"))
check("hidden: discontinued operations mark a spin-off parent", ctxs[T["SPUN"]]["disc_ops_material"] is True
      and "discontinued" in results["hidden"][T["SPUN"]]["gates"]["X3"][3], ctxs[T["SPUN"]].get("disc_ops_note"))
check("hidden: 50% below the 12-month high triggers", close(ctxs[T["DROP"]]["drawdown_12m"], -0.5, 1e-6),
      ctxs[T["DROP"]].get("drawdown_12m"))
check("hidden: ordinary 23% dip doesn't", "X3" in results["hidden"][T["GOOD"]]["failed"])
check("red flags: growth fading under half its 3-year rate is named",
      "growth fading" in ctxs[T["HYPE"]]["red_flag_notes"], ctxs[T["HYPE"]]["red_flag_notes"])
check("red flags: an expensive company with nothing breaking isn't flagged",
      results["red_flags"][T["GOOD"]]["failed"] == ["W4"], results["red_flags"][T["GOOD"]]["failed"])

print("\nOutputs")
import openpyxl  # noqa: E402
wb = openpyxl.load_workbook(out, read_only=True)
need = ["Read_Me", "Overlap", "1 Core", "1 Core - watch", "2 Emerging", "3 Special sits", "4 Fortress",
        "5a HC commercial", "5b HC clinical", "6 Cyclicals", "7 Owner-operators", "8 Hard assets", "9 Asset floor",
        "10 Trough cash", "11 Hidden earnings", "12 Red flags (avoid)", "12 Red flags (avoid) - watch",
        "Events", "Industry_Cycle", "Data_Gaps",
        "All_Companies", "Annual_Data", "Rules", "Industry_Groups"]
missing = [s for s in need if s not in wb.sheetnames]
check("workbook has every sheet", not missing, ", ".join(missing))
check("evidence CSV written", os.path.exists(out.replace(".xlsx", "_evidence.csv")))
lj = json.load(open(os.path.join(qc.OUTPUT_DIR, "latest_results.json")))
check("latest_results.json lists every screen", set(lj["screens"]) == set(BY_ID))

# AI pack + quote verification
zp = qa.build_pack(client, screen="core", top=2, blind=True)
pack = zp[:-4]
txt = open(os.path.join(pack, "C01_fulltext.txt"), encoding="utf-8").read()
check("hidden XBRL header removed from text", "HIDDEN XBRL" not in txt)
check("company name redacted in blind pack", "[COMPANY]" in txt)
check("screen focus written into the pack", os.path.exists(os.path.join(pack, "screen_focus.md")))
scores = [{"company_code": "C01", "traits": {
    "pricing_power": {"score": 5, "quotes": [{"text": "We have raised prices in each of the last five years"}]},
    "market_structure": {"score": 5, "quotes": [{"text": "we are the only company in the world issuing ratings"}]}},
    "bear_case": {"text": "x", "quotes": []}}]
sp = os.path.join(pack, "moat_scores.json")
json.dump(scores, open(sp, "w"))
_, summary, rows = verify(sp, pack)
rt = {r["trait"]: r for r in rows}
check("real quote verified", rt["pricing_power"]["verified"] is True)
check("fabricated quote rejected and score withdrawn",
      rt["market_structure"]["verified"] is False and summary[0]["market_structure"] is None)

# ---- real SEC data (subsets of actual companyfacts files) checked against the companies' reported figures
print("\nReal SEC data")


def real(name):
    with gzip.open(os.path.join(ROOT, "tests", "real_samples", f"{name}_companyfacts_subset.json.gz"), "rt") as f:
        return CompanyData(json.load(f))


aapl = real("aapl")
(am, arows), _ = compute(aapl, cfg, date(2025, 12, 31))
ar = {r["fy"]: r for r in arows}
check("Apple FY2024 revenue = $391.035B (10-K)", aapl.get("revenue", 2024) == 391035000000)
check("Apple FY2024 gross margin = 46.2%", close(ar[2024]["gross_margin"], 0.462, 0.001))
check("Apple FY2024 free cash flow = $108.8B (118.3 OCF - 9.4 capex)", close(ar[2024]["fcf"] / 1e9, 108.8, 0.1))
check("Apple FY2024 total debt = $106.6B (term debt + commercial paper)", close(ar[2024]["total_debt"] / 1e9, 106.6, 0.1))
check("Apple share count falling ~3%/yr through the 2020 4-for-1 split", -0.04 < am["share_count_cagr"] < -0.02,
      f"{am['share_count_cagr']:.4f}")
snow = real("snow")
check("Snowflake year to Jan-2024 labelled FY2023, revenue $2.806B", snow.get("revenue", 2023) == 2806489000)
(sm, _), _ = compute(snow, cfg, date(2025, 6, 30))
check("Snowflake fails consistent profits (operating losses)", sm["operating_loss_years"] >= 5)


def core_class(name, sic="7372", today=date(2026, 10, 5)):
    cd = real(name)
    (m, rows), _ = compute(cd, cfg, today)
    fx = {"USD": (1.0, "USD"), "TWD": (0.031, "s"), "EUR": (1.1, "s")}
    ctx = qp.build_ctx({"cik": 1, "ticker": name.upper(), "all_tickers": [name.upper()], "name": name,
                        "exchange": "NYSE"}, {"sic": sic}, m, rows, cd, cfg, fx, today)
    return BY_ID["core"].evaluate(ctx, cfg, priced=True), ctx


for name in ("aapl", "v", "ma", "cost", "mco"):
    r, _ = core_class(name)
    check(f"real data: {name.upper()} passes Core (as in your test run)", r["class"] == "PASS",
          f"{r['class']} {r['failed']} {r['check_notes'][:1]}")
r, _ = core_class("msft")
check("real data: MSFT is now a near miss on cash conversion (AI capex + stock pay: FCF after SBC < 0.8x net income)",
      r["class"] == "NEAR" and r["failed"] == ["G7"], f"{r['class']} {r['failed']}")
r, _ = core_class("adp")
check("real data: ADP (capex tag not in the old cache) is now CHECK, not FAIL", r["class"] == "CHECK",
      f"{r['class']} {r['check_notes'][:1]}")
r, _ = core_class("odfl")
check("real data: ODFL fails cash conversion and 'revenue not shrinking' (sales below 3 years ago)",
      r["class"] == "FAIL" and r["failed"] == ["G7", "G10"], f"{r['class']} {r['failed']}")
r, _ = core_class("spgi")
check("real data: SPGI is a near miss on ROIC consistency", r["class"] == "NEAR" and r["failed"] == ["G5b"],
      f"{r['class']} {r['failed']}")
for name in ("ko", "intc"):
    r, _ = core_class(name)
    check(f"real data: {name.upper()} fails Core", r["class"] == "FAIL", f"{r['class']} {r['failed']}")
r, c = core_class("mco")
check("real data: Moody's 2009 revenue change computed", c["recession_2009_revenue_change"] is not None)


print("\nFixes from the first live test run (Oct 2026 data from your cache)")


def screen_ctx(name, sic, info=None, today=date(2026, 10, 5)):
    cd = real(name)
    (m, rows), _ = compute(cd, cfg, today)
    fx = {"USD": (1.0, "USD"), "TWD": (0.0315, "s"), "EUR": (1.12, "s")}
    inf = {"sic": sic, **(info or {})}
    return qp.build_ctx({"cik": 1, "ticker": name.upper(), "all_tickers": [name.upper()], "name": name,
                         "exchange": "NYSE"}, inf, m, rows, cd, cfg, fx, today), cd, m


for name, sic in (("lrcx", "3559"), ("dhi", "1531")):
    c, _, _ = screen_ctx(name, sic)
    r = BY_ID["fortress"].evaluate(c, cfg, priced=False)
    check(f"{name.upper()}: operating loss in FY2009 fails Fortress 2009 test (was N/A -> PASS)",
          r["gates"]["F5"][0] == "FAIL" and r["class"] == "FAIL", f"{r['gates']['F5']} {r['class']}")
c, _, _ = screen_ctx("jnj", "2834")
check("JNJ: no operating-income line in any year -> EBIT proxy is a flag, not a hold",
      not c["hold_reasons"] and any("no operating-income line" in f for f in c["flags"]), str(c["hold_reasons"]))
r = BY_ID["hc_commercial"].evaluate(c, cfg, priced=False)
check("JNJ: Healthcare commercial PASS (was CHECK)", r["class"] == "PASS", f"{r['class']} {r['check_notes']}")
c, _, m = screen_ctx("aapl26", "3571")
r = BY_ID["fortress"].evaluate(c, cfg, priced=False)
check("AAPL: interest not tagged -> worst-case 10% estimate passes coverage (was NO DATA)",
      m.get("interest_coverage_estimated") and r["gates"]["F10"][0] == "PASS", str(r["gates"]["F10"]))
c, cd, m = screen_ctx("sndk", "3572")
v, basis = qm.post_event_dilution(cd, m, "2024-11-25")
check("SNDK: post-spin dilution uses the amended 10-Q/A share count (~1%/yr, not 18%)", v is not None and v < 0.03,
      f"{v} {basis}")
check("SNDK: computer storage is in the Semiconductors & memory cycle group", c["cycle_group"] == "Semiconductors & memory")
check("SNDK: 61% margin after a revenue surge (memory cycle) is flagged as peak margins", c["over_earning"] is True)
c, cd, m = screen_ctx("alab", "3674")
v, basis = qm.post_event_dilution(cd, m, "2024-02-21")
check("ALAB: growth company turning profitable (20% margin) is NOT flagged as peak margins", not c.get("over_earning"))
check("ALAB: dilution measured after the IPO = ~5%/yr (raw figure incl. preferred conversion was 74%)",
      v is not None and 0.03 < v < 0.07, f"{v} {basis}")
c, _, _ = screen_ctx("allo", "2836")
check("ALLO: no 'stock pay = 100,000% of revenue' flag for a pre-revenue biotech",
      not any("stock-based pay" in f for f in c["flags"]))
check("ALLO: $1.3M lease interest no longer flags 'debt may be missed'", not c["hold_reasons"], str(c["hold_reasons"]))
tsm_info = json.load(gzip.open(os.path.join(ROOT, "tests", "real_samples", "tsm26_submissions_subset.json.gz"), "rt"))
c, _, _ = screen_ctx("tsm26", "3674", {"latest_annual": tsm_info["latest_annual"]})
r = BY_ID["core"].evaluate(c, cfg, priced=False)
check("TSM: annual report filed but not yet in SEC XBRL -> 'Recent report' is NO DATA + hold, not FAIL",
      r["gates"]["G2"][0] == "NO DATA" and any("isn't in SEC's XBRL data yet" in h for h in r["holds"]),
      str(r["gates"]["G2"]))
c, _, _ = screen_ctx("fico", "7389")
r = BY_ID["core"].evaluate(c, cfg, priced=False)
check("FICO: fails only the debt rule (4.7x) -> 'Failed 1 rule' watch list, not dropped", r["class"] == "ONE"
      and r["failed"] == ["G8"], f"{r['class']} {r['failed']}")

from qs.valuation import names_match
check("quote name check: Moody's Corporation = MOODYS CORP /DE/", names_match("Moody's Corporation", "MOODYS CORP /DE/"))
check("quote name check: D.R. Horton = HORTON D R INC /DE/", names_match("D.R. Horton, Inc.", "HORTON D R INC /DE/"))
check("quote name check: different companies don't match", not names_match("Zillow Group", "Acme Mining Corp"))

# successor registrant (ExxonMobil Holdings Corp files under its own CIK; history sits under Exxon Mobil Corp)
xfs = json.load(gzip.open(os.path.join(ROOT, "tests", "real_samples", "xomh_companyfacts_subset.json.gz"), "rt"))
pred = json.load(gzip.open(os.path.join(ROOT, "tests", "real_samples", "aapl26_companyfacts_subset.json.gz"), "rt"))
pred = dict(pred, entityName="EXXON MOBIL CORP", cik=34088)   # stand-in history, renamed
asked = []
_gf, _gs = qp.get_facts, qp.get_submissions
qp.get_facts = lambda client, cik, cfg_, newer_than=None: (asked.append(cik), pred if cik == 34088 else None)[1]
qp.get_submissions = lambda client, cik, cfg_: {"latest_annual": {"form": "10-K", "reportDate": "2025-12-31"}}
found = qp.find_predecessor(None, cfg, 2115436, xfs, {"name": "ExxonMobil Holdings Corp", "latest_annual": None}, {})
qp.get_facts, qp.get_submissions = _gf, _gs
check("XOM: new holding company -> predecessor CIK 34088 found from the filings' accession numbers",
      found is not None and found[0] == 34088 and asked == [34088], str(asked))
merged = CompanyData(qp.merge_facts(pred, xfs))
check("XOM: merged history has annual data plus the successor's 2026 10-Q", merged.latest_fy() >= 2024
      and merged.latest_bs_date() == "2026-06-30", f"{merged.latest_fy()} {merged.latest_bs_date()}")


print("\nFixes from the first full run (Oct 2026)")
cd = real("fls")
check("FLS: 'Revenues' tag is 0 every year -> the real revenue tag is used ($4.73B in 2025)",
      close(cd.get("revenue", 2025) / 1e9, 4.729, 0.001), str(cd.get("revenue", 2025)))
cd = real("ait")
check("AIT: 'Revenues' tag holds a small line in 2011-16 -> continuity picks total sales ($2.52B in FY2016)",
      close(cd.get("revenue", 2016) / 1e9, 2.519, 0.01) and not any("revenue jumps" in f for f in cd.flags),
      f"{cd.get('revenue', 2016)} {sorted(cd.flags)}")
cd = real("hsy")
check("HSY: revenue tag jump in 2013-14 is outside the window and fixed by continuity - no hold",
      not any("revenue jumps" in f for f in cd.flags) and close(cd.get("revenue", 2013) / 1e9, 7.146, 0.01),
      f"{cd.get('revenue', 2013)} {sorted(cd.flags)}")
cd = real("nvs")
(m, _), _ = compute(cd, cfg, date(2026, 10, 5))
check("NVS: no standard revenue tag -> revenue = gross profit + cost of sales (not 0)",
      m["latest_revenue"] > 40e9 and any("derived" in f for f in cd.flags), f"{m['latest_revenue']}")
cd = real("mth")
res, why = compute(cd, cfg, date(2026, 10, 5))
check("MTH: revenue tag not found but the company is profitable -> not screened as 'revenue = 0'",
      res is None and "revenue not found" in why, str(why))
cd = real("rrc")
res, why = compute(cd, cfg, date(2026, 10, 5))
check("RRC: no pretax tag -> pretax = net income + tax, company screened", res is not None, str(why))
c, cd, m = screen_ctx("tjx", "5651")
r = BY_ID["core"].evaluate(c, cfg, priced=False)
check("TJX: no operating-income line in the latest year -> one EBIT definition for all years, Core PASS",
      r["class"] == "PASS", f"{r['class']} {r['failed']} {r['holds']}")
c, cd, m = screen_ctx("veev", "7372")
r = BY_ID["core"].evaluate(c, cfg, priced=False)
check("VEEV: PP&E capex tag missing after 2019 but PP&E is small -> software capex counts, Core PASS (was CHECK)",
      r["class"] == "PASS" and c.get("fcf_conversion") is not None, f"{r['class']} {r['check_notes']}")
for name, sic in (("ggg", "3561"), ("fix", "1731")):
    c, _, _ = screen_ctx(name, sic)
    check(f"{name.upper()}: small interest bill vs tiny tagged debt is not 'debt partly missed'",
          not any("debt" in h for h in c["hold_reasons"]), str(c["hold_reasons"]))
c, _, _ = screen_ctx("abev", "2080")
check("ABEV: IFRS finance costs (FX etc.) don't trigger 'debt partly missed'",
      not any("debt" in h for h in c["hold_reasons"]), str(c["hold_reasons"]))
c, _, _ = screen_ctx("tol", "1531")
r = BY_ID["core"].evaluate(c, cfg, priced=False)
check("TOL: 2008-09 losses but no 2007-08 sales in SEC data -> downturn rule unverified (NO DATA, with the reason)",
      r["gates"]["G9"][0] == "NO DATA" and "FY2008" in r["gates"]["G9"][3], str(r["gates"]["G9"]))
check("TOL: all debt lines counted (credit line $2.3B, not only $0.2B secured debt) -> ROIC median below 15%",
      c["roic_median"] < 0.15 and "G5a" in r["failed"], f"{c['roic_median']:.3f} {r['failed']}")
c, _, _ = screen_ctx("pool", "5090")
r = BY_ID["core"].evaluate(c, cfg, priced=False)
check("POOL: revenue shrinking 5%/yr over 3 years -> fails only 'revenue not shrinking' (a near miss, not dropped)",
      r["class"] == "ONE" and r["failed"] == ["G10"], f"{r['class']} {r['failed']}")
c, _, _ = screen_ctx("asml", "3559")
r = BY_ID["core"].evaluate(c, cfg, priced=False)
check("ASML: operating loss in FY2009 as sales fell 46% -> fails 'profitable in downturns'",
      "G9" in r["failed"] and "FY2009" in r["gates"]["G9"][3], str(r["gates"]["G9"]))
check("downturn windows tested: 2008-09, 2015-16, 2020, 2022", c["downturns_tested"] == ["2008-09", "2015-16", "2020", "2022"],
      str(c["downturns_tested"]))
r, c = core_class("ma")
check("MA: 2008 litigation charge (sales still grew) passes the downturn rule", r["class"] == "PASS"
      and r["gates"]["G9"][0] == "PASS", f"{r['class']} {r['gates']['G9']}")
print("\nMetric audit fixes (Oct 2026)")
c, _, _ = screen_ctx("aapl26", "3571")
check("AAPL: ROIC shown as computed (~152% median), not capped at 100%", 1.3 < c["roic_median"] < 1.8,
      f"{c['roic_median']:.3f}")
c, _, _ = screen_ctx("jnj", "2834")
r = BY_ID["core"].evaluate(c, cfg, priced=False)
check("JNJ: revenue growth like-for-like after the Kenvue split (5.1%/yr, not 3.0% mixing restated years) -> passes",
      0.045 < c["revenue_cagr"] < 0.056 and "G6" not in r["failed"] and any("like-for-like" in f for f in c["flags"]),
      f"{c['revenue_cagr']:.4f} {r['failed']}")
check("JNJ: R&D from the total tag (~17% of sales), not the acquired-IPR&D-only tag", 0.14 < c["rnd_to_revenue"] < 0.2,
      str(c["rnd_to_revenue"]))
(_m, _rows), _ = compute(real("rrc"), cfg, date(2026, 10, 5))
r16 = {x["fy"]: x for x in _rows}[2016]
check("RRC: capex from the largest tag (oil & gas $466M, not $1-36M of office equipment) -> FCF 2016 negative",
      r16["capex"] > 3e8 and r16["fcf"] < 0, f"{r16['capex']:.0f} {r16['fcf']:.0f}")
c, _, _ = screen_ctx("adp", "7374")
st = BY_ID["real_assets"].gates[3].evaluate(c, cfg, "real_assets")
check("ADP: capex not tagged -> capex / cash flow unknown (NO DATA), never 0% (a false pass on 'little reinvestment')",
      c["capex_to_ocf_3y"] is None and st[0] == "NO DATA", str(st))
c, _, _ = screen_ctx("veev", "7372")
check("VEEV: cycle-average EBITDA never below average EBIT when D&A is missing in some years; capex/D&A only over "
      "years with both", c["normalized_ebitda"] >= c["normalized_ebit"] and c["capex_to_da_3y"] is None,
      f"{c['normalized_ebitda']:.0f} {c['normalized_ebit']:.0f} {c['capex_to_da_3y']}")
c, _, _ = screen_ctx("tsm26", "3674")
check("TSM: USD convenience translations are not a second reporting currency (no permanent hold)",
      "multiple reporting currencies" not in " ".join(c["flags"]), str(c["hold_reasons"]))
_nm = {"roic_median": None, "roic_median_nm": "negative or near-zero invested capital in 7 of 10 years"}
_g5 = [g for g in BY_ID["core"].gates if g.gid == "G5a"][0]
check("ROIC with negative/near-zero invested capital (customer-funded) is 'n/m' and passes the high-returns rule",
      _g5.evaluate(_nm, cfg, "core")[0] == "PASS")
from qs.metrics import _median_nm  # noqa: E402
from qs.metrics import _cash  # noqa: E402
check("cash: short-term investments tagged only inside the combined line are counted (MSFT pre-2018: $133B, not $7.7B)",
      _cash(lambda c, y=None: {"cash": 7.7, "cash_and_sti_combined": 133.0}.get(c)) == 133.0
      and _cash(lambda c, y=None: {"cash": 10.0, "st_investments": 5.0, "cash_and_sti_combined": 15.0}.get(c)) == 15.0)
check("ROIC median counts n/m years as high; none when they are half or more",
      _median_nm([0.1, 0.2, 0.3], 1) == 0.25 and _median_nm([0.1], 1) is None and _median_nm([0.1, 0.5, 0.9], 0) == 0.5)

cni_info = json.load(gzip.open(os.path.join(ROOT, "tests", "real_samples", "cni_submissions_subset.json.gz"), "rt"))
check("CNI: 40-F filer without XBRL statements is explained, not silently missing",
      "40-F" in qp.no_data_hint(cni_info), qp.no_data_hint(cni_info))
xp = json.load(gzip.open(os.path.join(ROOT, "tests", "real_samples", "xpro_submissions_subset.json.gz"), "rt"))
check("XPRO: new registrant after an S-4 reorganization is explained", "S-4" in qp.no_data_hint(xp), qp.no_data_hint(xp))
from qs.screens import u_special
for sic, label in (("6331", "P&C insurer"), ("6199", "crypto treasury / finance"), ("6035", "savings bank")):
    ok, why = u_special({"sic": sic, "event_types": ["recent IPO"]}, {}, cfg)
    check(f"Special Situations excludes a {label} (EV/EBIT meaningless)", not ok, why)
ok, _ = u_special({"sic": "6411", "event_types": ["recent IPO"]}, {}, cfg)
check("Special Situations keeps insurance brokers", ok)
ok, _ = qs_screens.u_core({"sic": "5531", "all_tickers": ["ORLY"]}, {}, cfg)
check("Core screens auto-parts retailers (O'Reilly, AutoZone) - no longer excluded as 'auto dealers'", ok)
ok, _ = qs_screens.u_core({"sic": "6282", "all_tickers": ["MORN"]}, {}, cfg)
check("Core screens Morningstar via config 'screen_anyway' despite the 'investment advice' code", ok)
from qs.report import class_cell
check("All_Companies shows which rules failed", class_cell({"class": "FAIL", "failed": ["G5a", "G8"]}) == "FAIL: G5a G8")
from qs.valuation import value as qv
vv = qv({"currency": "USD", "dei_shares": 100e6, "dei_shares_date": "2026-09-01", "public_float": 9e9,
         "public_float_date": "2025-06-30", "bs_cash_and_sti": 1e8}, {"all_tickers": ["XYZ"], "latest_annual": {"form": "10-K"}, "name": "Xyz"},
        {"ok": True, "price": 40.0, "price_date": "2026-10-02", "symbol": "XYZ", "name": "Xyz Inc"}, 1.0,
        date(2026, 10, 5), td=type("TD", (), {"close_on": lambda self, s, d: 95.0})())
check("price fell 60% since the float date -> float check uses the price on that date, market cap accepted",
      vv["val_ok"] and vv["market_cap_usd"] == 4e9, str(vv.get("val_issue")))
vv = qv({"currency": "USD", "dei_shares": 100e6, "dei_shares_date": "2026-09-01", "bs_cash_and_sti": 1e8},
        {"all_tickers": ["ISR"], "latest_annual": {"form": "20-F"}, "name": "Isr"},
        {"ok": True, "price": 50.0, "price_date": "2026-10-02", "symbol": "ISR", "name": "Isr Ltd"}, 1.0,
        date(2026, 10, 5), listing_type="Common Stock")
check("20-F company listed as ordinary shares (not an ADR) -> market cap accepted", vv["val_ok"], str(vv.get("val_issue")))


print("\nSynthetic edge cases (independent review)")
import synth as sy  # noqa: E402


def syn_ctx(spec, sic="3561", fx=None, info=None):
    cdx = CompanyData(sy.add_share_comparatives(sy.build(spec)) if "WeightedAverageNumberOfDilutedSharesOutstanding"
                      in spec else sy.build(spec))
    resx, whyx = compute(cdx, cfg, date(2026, 10, 5))
    if resx is None:
        return None, cdx, whyx
    mx, rowsx = resx
    cx = qp.build_ctx({"cik": 1, "ticker": "SYN", "all_tickers": ["SYN"], "name": "Synth", "exchange": "NYSE"},
                      {"sic": sic, **(info or {})}, mx, rowsx, cdx, cfg, fx or {"USD": (1.0, "USD")}, date(2026, 10, 5))
    return cx, cdx, mx


tot = {y: (1.6e9 if y <= 2023 else 1.0e9) for y in range(2007, 2026)}
spec = sy.base_company(first=2007, rev0=1e9, growth=0.0)
spec["Revenues"] = ("duration", tot)
spec["SalesRevenueGoodsNet"] = ("duration", {y: v * 0.65 for y, v in tot.items()})
c, cd, m = syn_ctx(spec)
check("a genuine 37% revenue fall is not 'smoothed' with a partial revenue tag",
      cd.get("revenue", 2023) == 1.6e9 and m["revenue_cagr_3y"] < -0.1, f"{cd.get('revenue', 2023)} {m['revenue_cagr_3y']}")
spec = sy.base_company()
spec["PaymentsToAcquirePropertyPlantAndEquipment"] = ("duration", {y: v for y, v in
                                                       spec["PaymentsToAcquirePropertyPlantAndEquipment"][1].items() if y <= 2011})
c, cd, m = syn_ctx(spec)
r = BY_ID["core"].evaluate(c, cfg, priced=False)
check("capex tagged only 2007-11: no estimate for the 10-year window -> Core 'check manually', not PASS",
      r["class"] == "CHECK" and "G7" in r["no_data"], f"{r['class']} {r['no_data']}")
spec = sy.base_company(first=2007, rev0=1e9, growth=0.06, om=0.12, ni_m=0.08)
PT = "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"
for k in ("OperatingIncomeLoss", PT):
    spec[k] = ("duration", {y: v for y, v in spec[k][1].items() if y < 2025})
ni = dict(spec["NetIncomeLoss"][1])
ni[2025] *= 4
spec["NetIncomeLoss"] = ("duration", ni)
c, cd, m = syn_ctx(spec)
check("latest year's EBIT estimated from net income (one-off gain possible) -> hold",
      any("estimated from net income" in h for h in c["hold_reasons"]), str(c["hold_reasons"]))
Iq = "ifrs-full:"
rev = sy.yrs(2016, 2025, lambda y: 5e9 * 1.08 ** (y - 2016))
spec = {Iq + "Revenue": ("duration", rev), Iq + "GrossProfit": ("duration", {y: v * 0.5 for y, v in rev.items()}),
        Iq + "ProfitLossFromOperatingActivities": ("duration", {y: v * 0.25 for y, v in rev.items()}),
        Iq + "ProfitLossBeforeTax": ("duration", {y: v * 0.19 for y, v in rev.items()}),
        Iq + "ProfitLossAttributableToOwnersOfParent": ("duration", {y: v * 0.15 for y, v in rev.items()}),
        Iq + "CashFlowsFromUsedInOperatingActivities": ("duration", {y: v * 0.25 for y, v in rev.items()}),
        Iq + "FinanceCosts": ("duration", {y: v * 0.06 for y, v in rev.items()}),
        Iq + "Assets": ("instant", {y: v * 1.6 for y, v in rev.items()}),
        Iq + "CashAndCashEquivalents": ("instant", {y: v * 0.1 for y, v in rev.items()})}
cdx = CompanyData(sy.build(spec, unit="EUR"))
(mx, rowsx), _ = compute(cdx, cfg, date(2026, 10, 5))
check("no debt tag but finance costs of 6% of revenue -> 'debt may be missed' hold (IFRS too)",
      any("debt may be missed" in f for f in cdx.flags), str(sorted(cdx.flags)))
d2 = sy.build({"Revenues": ("duration", {2024: 1000.0, 2025: 1200.0}),
               "NetIncomeLoss": ("duration", {2024: 80.0, 2025: 120.0})},
              extra={"us-gaap": {"RevenueFromContractWithCustomerExcludingAssessedTax": {"USD": sy.q_entries([
                  ("2026-01-01", "2026-06-30", 700.0, "2026-08-01"), ("2025-01-01", "2025-06-30", 560.0, "2026-08-01")])}}})
check("10-Qs switched revenue tag: trailing 12 months still use them (1,340, not the stale 1,200)",
      CompanyData(d2).ttm("revenue").val == 1340.0, str(CompanyData(d2).ttm("revenue").val))
spec = sy.base_company(first=2016, rev0=5e8, growth=0.20, om=0.06, ni_m=0.045, ocf_m=0.06, capex_m=0.01)
del spec["GrossProfit"]
spec["CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization"] = ("duration", {
    y: v * 0.88 for y, v in spec["Revenues"][1].items()})
c, cd, m = syn_ctx(spec, sic="5045")
r = BY_ID["emerging"].evaluate(c, cfg, priced=False)
check("a 12%-gross-margin distributor fails Emerging's gross-margin rule (cost of sales under the ex-D&A tag)",
      r["gates"]["E6"][0] == "FAIL", str(r["gates"]["E6"]))
bio = {"OperatingIncomeLoss": ("duration", {y: (5e7 if y == 2019 else -8e7) for y in range(2016, 2026)}),
       "NetIncomeLoss": ("duration", {y: (4e7 if y == 2019 else -7e7) for y in range(2016, 2026)}),
       "NetCashProvidedByUsedInOperatingActivities": ("duration", {y: -6e7 for y in range(2016, 2026)}),
       "Assets": ("instant", {y: 6e8 for y in range(2016, 2026)}),
       "CashAndCashEquivalentsAtCarryingValue": ("instant", {y: 5e8 for y in range(2016, 2026)})}
res_b, _ = compute(CompanyData(sy.build(bio)), cfg, date(2026, 10, 5), allow_no_revenue=True)
res_o, why_o = compute(CompanyData(sy.build(bio)), cfg, date(2026, 10, 5))
check("biotech with one profitable year and a company-specific revenue tag is still screened (clinical codes)",
      res_b is not None and res_o is None, str(why_o))

# ---------------------------------------------------------------- web portal
print("\n== Web portal ==")
import gzip as _gz  # noqa: E402
import json as _js  # noqa: E402
import os as _os  # noqa: E402
from datetime import timedelta as _td  # noqa: E402
from qs.massive import Massive, PriceSource  # noqa: E402
from qs import portal as P  # noqa: E402
from qs import summaries as SU  # noqa: E402
_fx = _os.path.join(TMP, "pfx")
_os.makedirs(_os.path.join(_fx, "massive"), exist_ok=True)
_today = date(2026, 10, 5)   # a Monday
_d, _n = _today, 0
while _n < 22:
    if _d.weekday() < 5 and _d != date(2026, 9, 7):    # Labor Day: market closed
        bars = [{"T": "ABC", "o": 10.0, "c": 10.0 + _n * 0, "v": 1000.0, "vw": 10.0},
                {"T": "BRK.B", "o": 480.0, "c": 482.0, "v": 2e6, "vw": 481.0}]
        if _n == 0:
            bars[0].update(o=9.8, c=10.2)
        _js.dump({"status": "OK", "results": bars}, open(_os.path.join(
            _fx, "massive", f"v2_aggs_grouped_locale_us_market_stocks_{_d.isoformat()}.json"), "w"))
        _n += 1
    _d -= _td(days=1)
_js.dump({"results": [{"ticker": "ABC", "name": "ABC Holdings Inc", "type": "CS"},
                      {"ticker": "BRK.B", "name": "Berkshire Hathaway Inc", "type": "CS"}]},
         open(_os.path.join(_fx, "massive", "v3_reference_tickers.json"), "w"))
_ps = PriceSource(Massive("", _os.path.join(TMP, "pcache"), fixtures_dir=_fx, today=_today, log=lambda *a: None),
                  None, log=lambda *a: None)
_q = _ps.quotes([("ABC", "NYSE"), ("BRK-B", "NYSE"), ("NOPE", "Nasdaq")])
check("Massive: open/close of the latest day, SEC 'BRK-B' found as 'BRK.B'",
      _q["ABC"]["ok"] and _q["ABC"]["open"] == 9.8 and _q["ABC"]["price"] == 10.2 and _q["BRK-B"]["ok"]
      and _q["ABC"]["price_date"] == "2026-10-05", str(_q["ABC"]))
check("Massive: average daily traded value over 20 trading days (liquidity rules)",
      abs(_q["ABC"]["avg_volume"] * _q["ABC"]["price"] - 10000.0) < 1e-6,
      str(_q["ABC"].get("avg_volume")))
check("Massive: unknown ticker -> not priced (with the reason), never guessed",
      not _q["NOPE"]["ok"] and "not in Massive" in _q["NOPE"]["reason"], str(_q["NOPE"]))
check("Massive: listing type from the reference list", _ps.instrument_types().get("ABC") == "Common Stock")
_ps2 = PriceSource(Massive("", _os.path.join(TMP, "pcache2"), fixtures_dir=_fx, today=_today + _td(days=12),
                           log=lambda *a: None), None, log=lambda *a: None)
check("Massive: a price older than 7 days is refused", not _ps2.quote("ABC")["ok"], str(_ps2.quote("ABC")))

# month-end closes for the 12-month high (one all-stocks file per month); 2026-08-31 was a Monday
for _me, _c in (("2026-09-30", 11.0), ("2026-08-31", 14.0), ("2026-07-31", 12.0), ("2026-06-30", 9.0)):
    _js.dump({"status": "OK", "results": [{"T": "ABC", "o": _c, "c": _c, "v": 1.0, "vw": _c}]}, open(_os.path.join(
        _fx, "massive", f"v2_aggs_grouped_locale_us_market_stocks_{_me}.json"), "w"))
from qs.valuation import value as _value  # noqa: E402
_hi = _ps.month_end_highs(["ABC", "NOPE"], months=12, splits={})
check("Massive: 12-month high = highest month-end close (14.0 at end of August)",
      _hi.get("ABC") == (14.0, "2026-08-31") and "NOPE" not in _hi, str(_hi))
_hi2 = _ps.month_end_highs(["ABC"], months=12, splits={"ABC": [("2026-09-15", 1.0, 2.0)]})
check("Massive: a 2-for-1 split halves earlier closes - a split never looks like a fall",
      _hi2.get("ABC") == (11.0, "2026-09-30"), str(_hi2))
check("Massive: no split list -> no 12-month high from Massive (Twelve Data's 52-week high instead)",
      _ps.month_end_highs(["ABC"], months=12, splits=None) == {})
_vs = _value({"currency": "USD", "dei_shares": 1e6, "dei_shares_date": "2026-08-01", "bs_cash_and_sti": 0,
              "public_float": 6e6, "public_float_date": "2026-06-30", "pf_close_raw": 20.0,
              "dei_shares_near_float": 0.5e6, "dei_shares_near_float_date": "2026-07-25",
              "recent_splits": [("2026-09-15", 1.0, 2.0)]},
             {"all_tickers": ["ABC"], "name": "ABC Holdings"}, _q["ABC"], 1.0, _today)
check("after a 2-for-1 split: share count put on today's basis, insider share measured on the float date's basis",
      _vs["shares_used"] == 2e6 and abs(_vs["insider_share"] - 0.4) < 1e-9, str(_vs))
_v = _value({"currency": "USD", "dei_shares": 1e6, "dei_shares_date": "2026-08-01", "high_12m": 14.0,
             "public_float": 6e6, "public_float_date": "2026-06-30", "pf_close": 10.0, "bs_cash_and_sti": 0},
            {"all_tickers": ["ABC"], "name": "ABC Holdings"}, _q["ABC"], 1.0, _today)
check("drawdown from the 12-month high, and insider share from the float-date price",
      abs(_v["drawdown_12m"] - (10.2 / 14.0 - 1)) < 1e-9 and abs(_v["insider_share"] - 0.4) < 1e-9, str(_v))
_m2 = Massive("", _os.path.join(TMP, "pcache3"), fixtures_dir=_fx, today=_today, log=lambda *a: None)
_m2.day("2026-08-31", folder="hist")
_path = _os.path.join(TMP, "pcache3", "prices", "massive", "hist", "2026-08-31.json.gz")
_old = _js.load(_gz.open(_path, "rt"))
_old["fetched"] = "2025-01-01"
_old["bars"]["ABC"][1] = 999.0                     # as if fetched before a split
_js.dump(_old, _gz.open(_path, "wt"))
check("past closes older than the refresh window are downloaded again (split-adjusted today)",
      _m2.close_on("ABC", "2026-08-31", fresh_days=12) == 14.0 and _m2.close_on("ABC", "2026-08-31") == 14.0)

_kp = _os.path.join(TMP, "keyinfo.json")
_s1 = P.Sealer("correct horse battery", _kp)
_blob = _s1.seal({"x": [1, 2.5, float("nan")]})
check("portal data is encrypted (no plaintext in the file) and opens with the password",
      b'"x"' not in _blob and _s1.open(_blob) == {"x": [1, 2.5, None]})
_js.dump(dict(_s1.info), open(_kp, "w"))
try:
    P.Sealer("wrong password", _kp).open(_blob)
    _wrong_ok = True
except Exception:  # noqa: BLE001
    _wrong_ok = False
check("portal data does not open with a wrong password", not _wrong_ok)

_g = {g.gid: g for g in BY_ID["core"].gates}
check("rule labels read as plain English",
      P.rule_label(_g["G5a"], cfg, "core") == "at least 15% ROIC, 10-year median"
      and P.rule_label(_g["G1"], cfg, "core") == "at least 8 years of data",
      P.rule_label(_g["G5a"], cfg, "core") + " | " + P.rule_label(_g["G1"], cfg, "core"))

_ctxs = {str(i): {"ticker": f"T{i}", "sic": "7372", "industry": "SERVICES-PREPACKAGED SOFTWARE",
                  "pe": 10.0 + i, "latest_revenue_usd": 1e9 * i} for i in range(1, 7)}
_ctxs["7"] = {"ticker": "T7", "sic": "7371", "industry": "SERVICES-COMPUTER PROGRAMMING", "pe": None,
              "pe_unverified": 99.0, "latest_revenue_usd": 1.0}
_ctxs["8"] = {"ticker": "T8", "sic": "7372", "industry": "SERVICES-PREPACKAGED SOFTWARE", "pe": -5.0,
              "latest_revenue_usd": 1.0}
_groups, _assign = P.peer_groups(_ctxs, 6)
check("peers: same 4-digit industry when 6+ companies; median uses verified, positive multiples only",
      _assign["1"] == "4:7372" and _groups["4:7372"]["med"]["pe"] == 13.5, str(_groups.get("4:7372")))
check("peers: a company in a thin industry falls back to the broader 3-digit group",
      _assign["7"] == "3:737" and "SIC 737x" in _groups["3:737"]["label"], str(_assign.get("7")))

from qs.screens import _floor, red_flag_signals, _hidden_trigger  # noqa: E402
check("asset floor: no debt tag doesn't block the tangible-book test",
      _floor({"mcap_to_net_cash": 0.7, "price_to_tangible_book": 0.6, "bs_debt_found": False,
              "tangible_book_ps_change_3y": 0.05}, cfg, "asset_floor")[0] == "PASS")
check("asset floor: below tangible book with book per share shrinking is a value trap (FAIL), unknown history = NO DATA",
      _floor({"price_to_tangible_book": 0.6, "tangible_book_ps_change_3y": -0.2}, cfg, "asset_floor")[0] == "FAIL"
      and _floor({"price_to_tangible_book": 0.6}, cfg, "asset_floor")[0] == "NO DATA")
check("red flags: profits above cash, recurring restructuring, bought growth, inventory build, capex burn are signals",
      len(red_flag_signals({"profits_above_cash_2y": True, "restructuring_years_5y": 4, "acquisitions_to_ocf_3y": 1.5,
                            "inventory_days_high": True, "inventory_days": 120, "capex_to_da_latest": 3.0,
                            "ttm_fcf": -5}, cfg)) == 5)
from qs.screens import _e_profitable, _e_valuation  # noqa: E402
_hv = {"da_share_of_ebitda": 0.7, "ttm_ebitda": 100, "latest_fy_ebitda": 90, "ttm_operating_income": -10,
       "latest_fy_operating_income": 5, "ev_ebitda": 8.0, "ev_ebit": None, "ev_usd": 1000}
check("emerging: capital-heavy (D&A 70% of EBITDA) is judged on operating profit and EV/EBIT, not EBITDA",
      _e_profitable(_hv, cfg, "emerging")[0] == "FAIL" and _e_valuation(_hv, cfg, "emerging")[0] == "FAIL")
check("asset floor: below cash with no debt tag (and above tangible book) -> check by hand",
      _floor({"mcap_to_net_cash": 0.7, "price_to_tangible_book": 1.5, "bs_debt_found": False}, cfg,
             "asset_floor")[0] == "NO DATA")
check("red flags: a loss year and its margin drop count as one signal",
      len(red_flag_signals({"ttm_operating_income": -5, "operating_margin_change_3y": -0.2}, cfg)) == 1)
check("hidden: a -50% 'fall' when the split list was unavailable is held, not passed",
      _hidden_trigger({"drawdown_12m": -0.5, "price": 10, "splits_unknown": True, "high_12m_used": 20}, cfg,
                      "hidden")[0] == "NO DATA")
_rf = P.screen_payload(BY_ID["red_flags"], results["red_flags"], ctxs, cfg)
_ow = P.screen_payload(BY_ID["owners"], results["owners"], ctxs, cfg)
check("portal: Red Flags is marked as an avoid list; other screens aren't", _rf["avoid"] and not _ow["avoid"])
check("portal: plain-English rule for insider ownership",
      any(g["rule"] == "at least 20% owned by insiders" for g in _ow["gates"]), [g["rule"] for g in _ow["gates"]][:4])
check("portal: all 13 screens, unique gate ids", len(BY_ID) == 13)
_cp = P.screen_payload(BY_ID["core"], results["core"], ctxs, cfg)
check("portal: 'recent report' is applied but hidden from the rules table; no investor names in rationales",
      [g["id"] for g in _cp["gates"] if g["hidden"]] == ["G2"]
      and not any(n in g["why"] for g in _cp["gates"] for n in ("Kantesaria", "Dorsey", "Smith", "Haley", "Stahl")))
check("portal: same table columns on every screen (P/E, EV/EBIT, FCF yield, ROIC 10y median, 5y revenue CAGR)",
      _cp["metrics"] == ["pe", "ev_ebit", "fcf_yield", "roic_median", "revenue_cagr_5y"]
      and _rf["metrics"] == _cp["metrics"])

# statement model: diluted shares restated to today's basis through GOOD's 2-for-1 split (2020)
from qs.metrics import model_years  # noqa: E402
from qs import history as H  # noqa: E402
_cdg = CompanyData(qp.get_facts(client, T["GOOD"], cfg))
(_mm, _rows), _ = compute(_cdg, cfg, TODAY)
_mdl = model_years(_cdg, _rows)
_yrs = {y["fy"]: y for y in _mdl["years"]}
check("model: up to 10 fiscal years with statement lines", 5 <= len(_mdl["years"]) <= 10
      and all(k in _mdl["years"][-1] for k in ("revenue", "net_income", "x_operating_income")))
check("model: shares on today's basis are split-proof (2019 x 2 = 2020 basis, falling 2%/yr)",
      close(_yrs[2019]["shares_basis"] / _yrs[2018]["shares_basis"], 0.98, 1e-6)
      and close(_yrs[2021]["shares_basis"] / _yrs[2019]["shares_basis"], 0.98 ** 2, 1e-6),
      f"{_yrs[2018].get('shares_basis')} {_yrs[2019].get('shares_basis')} {_yrs[2021].get('shares_basis')}")

# historical multiples: price at each fiscal year end x today's-basis shares vs that year's figures
_hctx = {"currency": "USD", "market_cap_usd": 100.0 * _mdl["years"][-1]["shares_basis"], "price": 100.0}
_ser = {f"{y['end'][:7]}": 100.0 for y in _mdl["years"]}
_ym, _why = H.year_multiples(_hctx, _mdl, _ser)
_last = _mdl["years"][-1]
check("history: P/E at a fiscal year end = price x shares / net income",
      _ym and close(_ym[-1][1]["pe"], 100.0 * _last["shares_basis"] / _last["net_income"], 1e-6), str(_why))
_ym2, _why2 = H.year_multiples(dict(_hctx, market_cap_usd=_hctx["market_cap_usd"] * 3), _mdl, _ser)
check("history: share count that doesn't match the market cap (share classes) -> no history, with the reason",
      _ym2 is None and "share" in _why2, _why2)
_av = H.averages(_ym)
check("history: 3-year and 10-year averages", "pe" in _av and _av["pe"][2] == len(_ym), str(_av.get("pe")))
check("valuation verdict: cheaper than own history and peers by >10% -> cheap; dearer on both -> expensive",
      H._verdict("pe", 15, 20, 22) == "cheap" and H._verdict("pe", 30, 20, 22) == "expensive"
      and H._verdict("pe", 15, 20, 12) == "mixed" and H._verdict("fcf_yield", 0.06, 0.04, 0.05) == "cheap")
_pc = {str(i): {"ticker": f"P{i}", "sic": "7372" if i < 4 else "7371", "latest_revenue_usd": 10.0 ** i}
       for i in range(1, 8)}
_pp = H.closest_peers(_pc, 4)
check("closest peers: same 4-digit code first (nearest revenue), then the 3-digit group",
      _pp["2"][:2] == ["1", "3"] and len(_pp["2"]) == 4 and _pp["2"][2] in ("4", "5"), str(_pp["2"]))
check("multiples by industry: banks -> P/E, P/B; loss-makers -> EV/Sales; else P/E, EV/EBIT, FCF yield",
      H.choose_multiples({"sic": "6022"}, [], {}) == ["pe", "pb"]
      and H.choose_multiples({"sic": "7372", "ttm_operating_income": -1}, [], {}) == ["ev_sales"]
      and H.choose_multiples({"sic": "3561", "ttm_operating_income": 5}, [], {})[:3] == ["pe", "ev_ebit", "fcf_yield"])

# 52-week range from weekly high/low files (Massive), split-adjusted
for _dd in (date(2026, 10, 2), date(2026, 10, 1)):
    _js.dump({"status": "OK", "results": [{"T": "ABC", "o": 10, "c": 10, "v": 1, "vw": 10, "h": 12.0 if _dd.day == 2 else 11.0,
                                           "l": 8.0 if _dd.day == 1 else 9.0}]},
             open(_os.path.join(_fx, "massive", f"v2_aggs_grouped_locale_us_market_stocks_{_dd.isoformat()}.json"), "w"))
_m5 = Massive("", _os.path.join(TMP, "pcache5"), fixtures_dir=_fx, today=_today, log=lambda *a: None)
_added, _miss = _m5.backfill_weeks(["ABC"], {}, budget=3, days=6)
_r52 = _m5.ranges_52w(["ABC"], {})
check("52-week range: days folded into weekly high/low within the request budget",
      _added >= 2 and _r52["ABC"]["hi"] == 12.0 and _r52["ABC"]["lo"] == 8.0, f"{_added} {_miss} {_r52}")
_r52s = _m5.ranges_52w(["ABC"], {"ABC": [("2026-10-06", 1.0, 2.0)]})
check("52-week range: a 2-for-1 split after the download halves the stored high/low", _r52s["ABC"]["hi"] == 6.0, str(_r52s))

check("summaries: Claude's JSON answer is parsed even with text around it",
      SU._parse('Here you go:\n{"12": "Makes widgets.", "13": ""}') == {"12": "Makes widgets."})
_st = {"ctxs": {"1": {"cik": 1, "ticker": "A", "latest_annual_accn": "x-1", "latest_annual_doc": "a.htm",
                      "market_cap_usd": 5e9},
                "2": {"cik": 2, "ticker": "B", "latest_annual_accn": "x-2", "latest_annual_doc": "b.htm",
                      "market_cap_usd": 9e9},
                "3": {"cik": 3, "ticker": "C", "latest_annual_accn": "x-3", "latest_annual_doc": "c.htm",
                      "market_cap_usd": 1e9}},
       "classes": {"core": {"1": "PASS", "2": "FAIL", "3": "CHECK"}}}
check("summaries: companies on the lists first, then the largest; done ones skipped until a new 10-K",
      SU.pick(_st, {"3": {"text": "x", "accn": "x-3"}}, 5) == ["1", "2"]
      and SU.pick(_st, {"3": {"text": "x", "accn": "old"}}, 5) == ["1", "3", "2"])

shutil.rmtree(TMP, ignore_errors=True)
print(f"\n{'ALL TESTS PASSED' if not failures else str(len(failures)) + ' FAILED: ' + ', '.join(failures)}")
sys.exit(1 if failures else 0)
