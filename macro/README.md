# Macro Compass (macro/)

Where the US economy is in its cycle, and which of 20 industry ETFs that puts at risk or in favour.
Page: its own Cloudflare Worker "macro-compass", built from branch `macro-site` (separate from the stock-screener
site). No password: page and data are public (not indexed by search engines).

## Pipeline (`python -m macro.run all`, workflow `.github/workflows/macro.yml`, weekdays 22:17 UTC + push to macro/)
1. `fetch.py` -> `cache/macro/raw/`: FRED (first-published values via ALFRED when secret FRED_API_KEY is set, else
   the public CSV = latest revised values), Yahoo monthly adjusted closes (Stooq fallback), Kenneth French 49
   industries + market, multpl.com CAPE. Raw files are pushed to branch `macro-data` each run.
2. `engine.py` -> `cache/macro/out/compass.json.gz`:
   - monthly grid from 1960; each FRED number enters only after its release delay (`registry.FRED` lag);
   - 38 indicators (`registry.INDICATORS`, each cited to an investor); score = percentile of the reading within
     its own past (10 years minimum); six pillars = equal-weight average of their indicators;
   - stage from the 6-month average of growth pressure: level (weak >=55, solid <=45, else unchanged) x 12-month
     direction (+-8 points, else unchanged), 3 months to confirm;
   - industries: ETF returns once the ETF trades, French industry proxy before; driver score = average of the
     industry's drivers (sign from the investor's claim); odds at month t = share of past months (outcome finished
     by t) in the same fifth of driver score that lagged / beat the market by 10% (12 months) or 7% (6 months),
     shrunk toward the base rate (k=20), after 15 years of history; call = odds >= 1.5x normal;
   - backtest: 20 ETFs equal weight vs tilted (1.5x / 0.5x) monthly from 2006-07, plus momentum, trend and SPY
     baselines; the same on spliced industry series from the month most industries have odds.
3. `site.py` -> `macro_site/` (page + sealed data + wrangler.jsonc + .assetsignore), force-pushed to `macro-site`.
4. `record.py` -> branch `macro-record` `ledger.csv`: each finished month's calls from Oct 2026, appended once,
   never edited. The engine scores them as they come due ("Live record" on the page).

Rules are pre-registered in `registry.py` (VERSION, SETTINGS). Change = new version, logged in CHANGES.md.
Tests: `tests/macro_smoke.py` (part of `tests/run_tests.py`). Local preview:
`MACRO_PLAIN=1 python -m macro.run site` after a build (unencrypted, never publish).
