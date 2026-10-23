# Macro Compass changes

## 3.0.0 (2026-10-23) - act only on extreme readings; benchmark = 20-sector average (user request)
- Calls are made only in months when a reading is extreme (SETTINGS.extreme): economy indicators' 6-month average
  score >= 60 (clearly weak) or <= 40 (clearly strong), market-stress score >= 70, or inflation 6-month average >= 70.
  Otherwise all 20 sectors stay at equal weight. Extreme in 52% of months since 1960.
- Benchmark for the history check, odds, sector history and relative charts: equal-weight average of the 20 sectors
  (was the S&P 500). Live ledger scored the same way; ledger gains an 'extreme' column (no rows written before).
- Tested before choosing (in sample, documented): every month vs dial extremes vs >= 1/4 or >= 1/3 of the 28 core
  indicators in their worst/best fifth, against both benchmarks. All within +-0.5%/yr of equal weight (IR <= 0.3);
  dial extremes chosen as the simplest with hit rates at or above base. Result: +0.2%/yr since 2006 (ETFs) and
  0.0%/yr since 1971 (industry indexes) vs equal weight.
- Also tested, not built: cutting stocks to 50% (rest T-bills) when >= 1/3 of core indicators are in their worst
  fifth: since 2006 11.3%/yr vs S&P 500 11.2%, worst fall -29% vs -51%; since 1975 11.8% vs 12.7%, -39% vs -51%.

## 2.2.1 (2026-10-23) - page only (user request)
- Per-chart notes replaced by one sticky chart key on the right (floating, collapsible on small screens); warning
  level moved into each summary sentence.
- Removed from the page: trade test, state x sector table, track record, background indicators, method. The engine
  still computes them and the live ledger still records every month.

## 2.2.0 (2026-10-23) - page layout + trade test (user request)
- Indicator boxes stacked full width, numbered 1.1, 1.2 ... with official names and one naming convention
  (vs L12M / L6M / L3M); each has a generated summary (what it measures, zone, change vs a year ago, what it
  indicates), a long-history chart and a last-2-years chart marking the reading a year ago vs now, round axis
  levels, and footnotes instead of explanatory text. Section headers show a warning/normal/supportive bar.
- New trade test (engine.entry_test): every past month the economy entered today's situation, $100k in that
  month's calls (long/short equal amounts, no leverage; and long only) vs $100k in the S&P 500, after 1, 2, 3
  years. Descriptive; no effect on the calls.

## 2.1.0 (2026-10-23) - page shows the data, not scores (user request)
- Page rebuilt: conclusion + points A (economy), B (inflation), C (market stress), each with real-unit time series
  of its signals (warning zone = worst third of the signal's own history, recessions shaded), what each signal means
  in plain words, and which sectors did best/worst after past months in the same zone; sector calls with the logic
  and the history check; state x sector table (average next 6/12-month return vs S&P 500); no 0-100 scores and no
  investor names on the page (sources stay in registry.py).
- Data fix: first-published (ALFRED) values that switch units between vintages (billions vs millions) are rescaled
  (engine._unit_breaks); this corrected 'share of household savings in stocks' (froth, background only). Calls unchanged.
- registry.DISPLAY: unit, decimals and plain explanation per indicator (display only).

## 2.0.0 (2026-10-23) - user request: one decision flow from transcript/Galt logic
- Indicators: 38 -> 43. Added Galt's market-stress signals (VIX via Yahoo ^VIX same-day + FRED VIXCLS, S&P 500
  below its 10-month average, junk bonds vs Treasuries 3-month, dollar breakout, chip stocks 12-month drawdown),
  staples vs discretionary, home builders drawdown, stocks-bonds correlation, dollar/oil/rates squeeze.
- New pillar "Market stress" (replaces "credit"); pillars: growth, internals, inflation, stress, liquidity, froth.
- State = three dials: economy stage (mean of growth + market health, same stage rule as 1.0.0), inflation hot
  (6-month average, on 60 / off 50) -> Overheating (expansion/late) or Stagflation (contraction), market stress
  high (on 65 / off 55) as an overlay.
- Industry calls: per-industry drivers and quintile odds removed. Investor playbook per state (registry.RULES, cited
  to Druckenmiller, Karniol-Tambour, Calderini, Eisman, Galt) + stress overlay (registry.STRESS) -> +1/-1 tilt;
  a tilt stands only if past months of the same situation (state+stress, else state; >= 24 months; outcomes
  finished by t) had a mean return vs SPY with the same sign. Backtest adds a "playbook only" curve.
- Seen before publishing (in sample): ETF backtest Aug 2006 - Oct 2026, calls +10.9%/yr vs equal weight +10.4%,
  SPY +11.2%; call hit rates close to base rates. Tested and rejected: adding Money and rates and/or Froth to the
  economy dial or the stress dial (calls 0.1-0.4%/yr worse, fewer recession months marked); they stay as background.
- Ledger columns now record state, inflation_hot, stress_high, six pillars and the investor tilt (no rows had been
  written under 1.0.0).

## 1.0.0 (2026-10-23) - pre-registered
- Indicators, pillars, industries, drivers, thresholds as in registry.py.
- Design choices made while building, before publishing:
  - stage settings (6-month average, 12-month direction +-8, level 45/55, 3-month confirm) were picked for a
    steady stage that marks past recessions as Contraction, checked on 1970-2026 data (in sample). The stage does
    not feed the industry odds or the backtest.
  - the first full build's backtest (calls ~ equal weight, Aug 2006 - Oct 2026) was seen before publishing; no
    rule was changed after it.
- 2026-10-23: FRED_API_KEY added; builds use first-published values from here on (no rule change).
- 2026-10-23: Cloudflare secrets added; the workflow deploys the Worker itself.
- 2026-10-23: page moved off the stock-screener site to its own Worker "macro-compass" (branch macro-site); no rule change.
- 2026-10-23: password removed (user); page and data public. No rule change.
- Known gaps: household-equity indicator needs the next download (series id fixed); FRED_API_KEY not yet set,
  so the first builds use revised data (first-published values once the key is in).
