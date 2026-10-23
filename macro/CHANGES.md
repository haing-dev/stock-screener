# Macro Compass changes

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
