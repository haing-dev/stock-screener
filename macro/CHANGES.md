# Macro Compass changes

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
- Known gaps: household-equity indicator needs the next download (series id fixed); FRED_API_KEY not yet set,
  so the first builds use revised data (first-published values once the key is in).
