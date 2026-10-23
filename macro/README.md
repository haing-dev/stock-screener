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
   - 43 indicators (`registry.INDICATORS`, each cited to an investor or Galt's X posts); score = percentile of the
     reading within its own past (10 years minimum); six pillars = equal-weight average of their indicators;
   - state from three dials: economy stage from the 6-month average of growth + market health (level weak >=55,
     solid <=45, else unchanged; 12-month direction +-8; 3 months to confirm); inflation hot (on 60 / off 50) turns
     expansion/late into Overheating and contraction into Stagflation; market stress high (on 65 / off 55) is an overlay;
   - industries: ETF returns once the ETF trades, French industry proxy before; tilt = investor playbook for the
     state (`registry.RULES`) + stress overlay (`registry.STRESS`); a tilt becomes a call only if past months of
     the same situation (outcome finished by t, >= 24 months) had a mean return vs the market with the same sign;
     odds of lagging / beating by 10% (12 months) or 7% (6 months) shown, shrunk toward the base rate (k=20);
   - backtest: 20 ETFs equal weight vs tilted (1.5x / 0.5x) monthly from 2006-07, plus playbook-only, momentum,
     trend and SPY baselines; the same on spliced industry series from the month most industries have calls;
   - trade test: each past entry into today's state (+ risk-off flag), $100k in that month's calls (long/short
     and long only) vs $100k in the S&P 500 after 1/2/3 years (`entry_test`).
3. `site.py` -> `macro_site/` (page + sealed data + wrangler.jsonc + .assetsignore), force-pushed to `macro-site`.
4. `record.py` -> branch `macro-record` `ledger.csv`: each finished month's calls from Oct 2026, appended once,
   never edited. The engine scores them as they come due ("Live record" on the page).

Rules are pre-registered in `registry.py` (VERSION, SETTINGS). Change = new version, logged in CHANGES.md.
Tests: `tests/macro_smoke.py` (part of `tests/run_tests.py`). Local preview:
`python -m macro.run site` after a build (public build, same as published).
