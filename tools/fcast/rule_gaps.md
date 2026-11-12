Cases the v1 text does not settle mechanically. Each was given the narrowest reading in tools/fcast/score.py (tag GAP-n
in the code where it applies). SCORING_RULES.md v1 stays as committed (5e058b3); a v2 would settle these before use.

1. Keyword tables: "country name" and "currency keyword" read as the listed code plus its English name or adjective
   (e.g. "Canadian", "rupee"); nothing else is inferred.
2. Publication lags not listed (WRESBAL, ECBASSETSW weekly; JPNASSETS monthly): 1 day for weekly, 30 days for monthly.
3. `round(h)` for monthly windows rounds half up.
4. Level text: a four-digit year after a month word or after by / in / until / end / of / from / since is a date and is
   removed before parsing ("high in December 2027" has no level).
5. Several numbers in `level` that do not form a range: level ignored, direction scored.
6. A range written with signs or with "%" on a price variable ("-20% to -30%", "-125 to -150bp") is a range of moves,
   not of end values.
7. Relative calls: the band of a leg is its code's family band; bond-ETF, cash and HYG legs (rate, policy-rate, credit
   codes) have no % band in the rules and are skipped for the band; if neither leg has one, the row is unscored.
8. Relative legs on different trading calendars: the second leg is read at the first leg's start and end dates (last
   observation on or before).
9. Volatility trend baseline: "exceeds" -> higher, otherwise lower (the trend never predicts flat).
10. CN_GROWTH, EU_GROWTH, JP_INFLATION: the WEO file in the cache holds current and forward years only, no backcast
    actuals, so "the first vintage that reports it as actual" is almost never present. Rows whose end year has passed
    with no actual in the file are unscored; later end years stay open.
11. "Minimum: 5 trading days": rows whose horizon ends fewer than 5 trading days after the made date are excluded
    (not stretched to 5 days).
12. The macro reading rule (publication lags, reference periods) is applied by variable, whatever the `call_type`:
    US_GROWTH, US_INFLATION, US_JOBS, US_DEFICIT_DEBT, US_POLICY_RATE, LIQUIDITY and Case-Shiller house prices.
    Market variables coded `call_type` = macro use the market rule.
13. Thresholds and level ranges need a level series (an index name in `variable_text`, or a code marked L). Macro codes
    and US_POLICY_RATE are not marked L, so their stated levels ("near 2%", "about 4.25%") are ignored and the
    direction is scored. Move sizes ("+50 to +100 bp", "+15%") need no level series and are always applied.
14. Recession calls: event_yes resolves early on a sign; without a sign both event_yes and event_no resolve 12 months
    after the end date (USREC must cover that month). event_no is not resolved early when a sign appears.
15. Drawdown and touch events resolve at the end date only (no early resolution). Touch needs a level series (as 13).
16. The `direction` field decides the method; `call_type` is used only for default horizons, pools and tables
    (e.g. call_type event with direction up is scored as a direction call; event_yes on a variable that is neither
    the recession code nor matched by a drawdown keyword nor given a usable threshold is unscored).
17. Duplicates use the exact `variable_code`, so two different sectors coded EQ_SECTOR by one speaker within 30 days
    count as one. Year-dated rows are excluded before the duplicate pass (they have no usable date).
18. Relative base rates use a leg's base proxy only where the proxy is a price or return series (SPY for ACWI, FXI for
    MCHI, IMF food and all-commodity indices for DBA and DBC); other short legs leave the base rate n/a.
19. A threshold read on a named index (not the code's default series) converts to the required move from that index's
    start value; the base rate applies that move to the code's base series.
20. Bootstrap month: the start date's month for market rows; for macro, WEO and recession rows (whose recorded start is
    a reading period or the made date) the month of made date + 1 day.
21. Monthly values built from daily series (for relative legs) and Yahoo monthly files drop an incomplete last month
    (last stamp before the month's last weekday).
22. The unit guard for thresholds on VIX, MOVE and credit spreads uses the 0.25x-4x ratio (they are % measured), not
    the 10-point rule.
23. A flat or range call with one threshold and no side word on a % measured series: hit if |end / T - 1| <= band.
24. CREDIT_SPREADS: HY OAS "covers the window and the 12 months before" is read as: HY's first date is at least 12
    months before the made date; otherwise Baa minus 10-year is used for the outcome and the trend.
25. A missing reference month at the end of a macro window (October 2025 CPI is absent from the cache) is a data gap:
    the row is unscored, not moved to the next month.
26. Scored rows were frozen on the first full run (2026-11-12) into scored_frozen.csv; earlier development runs used
    `--no-freeze` and froze nothing.
27. Intervals: a circular bootstrap with 12-month blocks gives zero spread when a cell's start months span 12 months or
    fewer (one block always covers the whole cell). Such cells show the point values with "no interval" instead of a
    verdict.
