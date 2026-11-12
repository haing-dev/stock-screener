---
tags: [method, spec]
file: /home/claude/stock-screener/docs/research/forecasts/SCORECARD_2026-11-12.md
---
# Forecast ledger scorecard (2026-11-12)

Rules: SCORING_RULES v1 (5e058b3) (docs/research/forecasts/SCORING_RULES.md). Scorer: tools/fcast/score.py, scorecard.py. Cache `fetched` stamps: {"raw": "2026-10-23 02:18 UTC", "research": "2026-10-30 17:42 UTC"}. Descriptive only: never used for weights, pod selection or design.
Outcome data dated 2011+ are used here solely to resolve these recorded forecasts (and each forecast's own trend baseline); base rates use 1990-2010 only. Nothing here is a return of the book, a pod or a backtest, and no market return is shown as such.

## What this does and does not show

It shows how often the dated views in the ledger came true under fixed mechanical rules, and whether that beats two naive forecasters: calling the direction at its 1990-2010 base rate, and extending the last 12 months. It does not show that any investor has skill: the views were selected by interviewers and by the argument maps, coded by one model (agreement below), mostly made in 2024-26 and still largely open, and they overlap heavily in time, so the resolved rows reflect few independent market episodes. Rows the coder marked not resolvable, not_forecast, year-dated or on variables without a free series are counted, not scored. Nothing here is an input to any pod, weight or selection.

## Funnel

Ledger rows 2102. Scorable (pass the mechanical tests: pool, date, horizon, series, direction) 556 = resolved 329 + open 227. Unscorable 1546 (not pooled 1076, excluded 37, duplicates 215, unscored 218).

| Pool | rows | excluded | duplicate | unscored | open | resolved |
|---|---|---|---|---|---|---|
| A headline (forecast, coder yes) | 154 | 7 | 43 | 25 | 25 | 54 |
| B (forecast, coder partly) | 467 | 9 | 100 | 122 | 95 | 141 |
| C stance | 171 | 10 | 16 | 22 | 42 | 81 |
| D conditional (condition ignored) | 171 | 3 | 45 | 30 | 48 | 45 |
| E structural | 63 | 8 | 11 | 19 | 17 | 8 |
| not pooled | 1076 | 0 | 0 | 0 | 0 | 0 |

Reasons (rows not resolved and not open):

| Status | Reason | rows |
|---|---|---|
| not pooled | not_forecast | 957 |
| duplicate | duplicate | 215 |
| unscored | no free series | 139 |
| not pooled | resolvable=no (vague_variable) | 99 |
| excluded | date too coarse (year) | 20 |
| not pooled | resolvable=no (unobservable) | 19 |
| excluded | horizon above 60 months | 15 |
| unscored | event not scorable in v1 | 14 |
| unscored | sector keyword not matched | 14 |
| unscored | commodity keyword not matched | 13 |
| unscored | country keyword not matched | 12 |
| unscored | relative leg without a total-return series | 7 |
| unscored | WEO file reports no actual for the end year | 6 |
| unscored | currency keyword not matched | 5 |
| unscored | data gap | 4 |
| unscored | volatility call on a non-market series | 2 |
| excluded | horizon below 5 trading days | 2 |
| unscored | direction not usable for an event variable | 1 |
| unscored | no direction convention (PRIVATE_CREDIT) | 1 |
| not pooled | resolvable=no (no_direction) | 1 |

By variable code (pooled rows only):

| Code | pooled | resolved | open | unscored | excluded | duplicate | main unscored reason |
|---|---|---|---|---|---|---|---|
| US_EQ | 105 | 49 | 23 | 2 | 4 | 27 | event not scorable in v1 |
| EQ_SINGLE | 64 | 0 | 0 | 27 | 0 | 37 | no free series (EQ_SINGLE) |
| TREND_FOLLOWING | 64 | 19 | 33 | 0 | 2 | 10 |  |
| OTHER | 59 | 0 | 0 | 55 | 0 | 4 | no free series (OTHER) |
| US_10Y | 55 | 32 | 14 | 0 | 2 | 7 |  |
| POLICY_EVENT | 53 | 0 | 0 | 35 | 5 | 13 | no free series (POLICY_EVENT) |
| US_INFLATION | 52 | 21 | 17 | 7 | 3 | 4 | event not scorable in v1 |
| EQ_SECTOR | 51 | 1 | 6 | 14 | 2 | 28 | sector keyword not matched |
| US_POLICY_RATE | 50 | 24 | 13 | 2 | 2 | 9 | event not scorable in v1 |
| USD | 40 | 14 | 10 | 0 | 2 | 14 |  |
| OIL | 31 | 11 | 12 | 1 | 1 | 6 | event not scorable in v1 |
| VIX | 31 | 19 | 5 | 0 | 0 | 7 |  |
| US_TECH | 26 | 6 | 7 | 0 | 2 | 11 |  |
| EM_EQ | 21 | 2 | 5 | 0 | 1 | 13 |  |
| GOLD | 20 | 11 | 3 | 0 | 5 | 1 |  |
| US_GROWTH | 19 | 11 | 7 | 0 | 1 | 0 |  |
| LIQUIDITY | 17 | 4 | 5 | 2 | 0 | 6 | event not scorable in v1 |
| GLOBAL_EQ | 16 | 7 | 5 | 0 | 0 | 4 |  |
| OTHER_RATES | 15 | 1 | 1 | 13 | 0 | 0 | country keyword not matched |
| US_RECESSION | 15 | 7 | 6 | 1 | 0 | 1 | direction not usable for an event variable |
| BTC | 14 | 8 | 5 | 0 | 0 | 1 |  |
| COMMODITIES | 13 | 3 | 9 | 0 | 0 | 1 |  |
| OTHER_COMMODITY | 13 | 0 | 0 | 13 | 0 | 0 | commodity keyword not matched |
| GEOPOLITICS | 12 | 0 | 0 | 10 | 0 | 2 | no free series (GEOPOLITICS) |
| HEDGE_FUNDS | 11 | 0 | 0 | 10 | 0 | 1 | no free series (HEDGE_FUNDS) |
| US_CURVE | 10 | 7 | 3 | 0 | 0 | 0 |  |
| EURUSD | 9 | 5 | 1 | 0 | 0 | 3 |  |
| US_DEFICIT_DEBT | 8 | 4 | 1 | 3 | 0 | 0 | event not scorable in v1 |
| US_TERM_PREMIUM | 8 | 3 | 5 | 0 | 0 | 0 |  |
| CN_EQ | 7 | 6 | 1 | 0 | 0 | 0 |  |
| CREDIT_SPREADS | 6 | 5 | 1 | 0 | 0 | 0 |  |
| GLOBAL_EQ>US_EQ | 6 | 3 | 3 | 0 | 0 | 0 |  |
| OTHER_FX | 6 | 0 | 0 | 5 | 1 | 0 | currency keyword not matched |
| AGRI | 5 | 2 | 0 | 1 | 0 | 2 | data gap |
| COPPER | 5 | 1 | 3 | 0 | 1 | 0 |  |
| JP_EQ | 5 | 1 | 2 | 0 | 2 | 0 |  |
| NATGAS | 5 | 4 | 1 | 0 | 0 | 0 |  |
| RATES_VOL | 5 | 3 | 2 | 0 | 0 | 0 |  |
| TREND_FOLLOWING>HEDGE_FUNDS | 5 | 0 | 0 | 4 | 0 | 1 | relative leg without a total-return series |
| USDJPY | 5 | 3 | 2 | 0 | 0 | 0 |  |
| EU_GROWTH | 4 | 0 | 0 | 4 | 0 | 0 | WEO file reports no actual for the end year |
| JP_RATES | 4 | 4 | 0 | 0 | 0 | 0 |  |
| US_30Y | 4 | 0 | 4 | 0 | 0 | 0 |  |
| CN_GROWTH | 3 | 0 | 1 | 2 | 0 | 0 | WEO file reports no actual for the end year |
| EU_EQ | 3 | 2 | 1 | 0 | 0 | 0 |  |
| EU_EQ>US_EQ | 3 | 2 | 0 | 0 | 0 | 1 |  |
| EU_RATES | 3 | 3 | 0 | 0 | 0 | 0 |  |
| GBPUSD | 3 | 3 | 0 | 0 | 0 | 0 |  |
| US_EQ>US_TECH | 3 | 0 | 2 | 0 | 0 | 1 |  |
| EM_FX | 2 | 2 | 0 | 0 | 0 | 0 |  |
| GLOBAL_GROWTH | 2 | 0 | 0 | 2 | 0 | 0 | no free series (GLOBAL_GROWTH) |
| IN_EQ | 2 | 1 | 1 | 0 | 0 | 0 |  |
| JP_EQ>EU_EQ | 2 | 0 | 2 | 0 | 0 | 0 |  |
| SILVER | 2 | 2 | 0 | 0 | 0 | 0 |  |
| URANIUM | 2 | 1 | 1 | 0 | 0 | 0 |  |
| US_2Y | 2 | 2 | 0 | 0 | 0 | 0 |  |
| CN_EQ>GLOBAL_EQ | 1 | 1 | 0 | 0 | 0 | 0 |  |
| CN_EQ>US_EQ | 1 | 1 | 0 | 0 | 0 | 0 |  |
| COMMODITIES>GLOBAL_EQ | 1 | 0 | 0 | 0 | 1 | 0 |  |
| EQ_SECTOR>EQ_SECTOR | 1 | 0 | 1 | 0 | 0 | 0 |  |
| EQ_SINGLE>EQ_SINGLE | 1 | 0 | 0 | 1 | 0 | 0 | relative leg without a total-return series |
| GOLD>OIL | 1 | 1 | 0 | 0 | 0 | 0 |  |
| JP_INFLATION | 1 | 0 | 0 | 1 | 0 | 0 | WEO file reports no actual for the end year |
| OTHER_RATES>US_10Y | 1 | 0 | 0 | 1 | 0 | 0 | relative leg without a total-return series |
| PRIVATE_CREDIT | 1 | 0 | 0 | 1 | 0 | 0 | no direction convention (PRIVATE_CREDIT) |
| REAL_ESTATE | 1 | 1 | 0 | 0 | 0 | 0 |  |
| URANIUM>OIL | 1 | 0 | 1 | 0 | 0 | 0 |  |
| USDCNY | 1 | 1 | 0 | 0 | 0 | 0 |  |
| US_EQ>EU_EQ | 1 | 1 | 0 | 0 | 0 | 0 |  |
| US_EQ>GLOBAL_EQ | 1 | 1 | 0 | 0 | 0 | 0 |  |
| US_EQ>TREND_FOLLOWING | 1 | 0 | 1 | 0 | 0 | 0 |  |
| US_JOBS | 1 | 0 | 1 | 0 | 0 | 0 |  |
| US_REAL_YIELD | 1 | 1 | 0 | 0 | 0 | 0 |  |
| US_SMALL>EQ_SINGLE | 1 | 0 | 0 | 1 | 0 | 0 | relative leg without a total-return series |
| US_SMALL>US_EQ | 1 | 1 | 0 | 0 | 0 | 0 |  |
| US_SMALL>US_TECH | 1 | 1 | 0 | 0 | 0 | 0 |  |

## Hit rates and baselines

Cells need >= 20 resolved rows from >= 6 start months; intervals: circular block bootstrap over start months, blocks of 12, 2,000 draws, seed 20261112, 90%. 'vs base' / 'vs trend': above = interval above 0. Move = change in the stated direction divided by the dead band (flat calls and events excluded).

### Pools (coder resolvable yes = A, partly = B; stated vs default horizon)

| Cell | n resolved | n open | start months | hit rate [90%] | sign-only hit | hit - base rate [90%] (n) | vs base | hit - trend [90%] (n) | vs trend | agrees with trend | move (band units) | Brier skill (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A (coder yes, stated horizon) | 54 | 25 | 26 | 37% [22%, 45%] | 50% | +6 pp [-5 pp, +12 pp] (53) | not distinguishable | -15 pp [-38 pp, +0 pp] (54) | not distinguishable | 33% | +0.68 | too few (0) |
| B, stated horizon (coder partly) | too few (5) | 2 | 5 | | | | | | | | | | |
| B, default horizon (coder partly) | 136 | 93 | 29 | 40% [34%, 49%] | 53% | +8 pp [+2 pp, +17 pp] (134) | above | -8 pp [-16 pp, +7 pp] (136) | not distinguishable | 37% | +1.35 | too few (0) |
| A+B | 195 | 120 | 34 | 39% [32%, 45%] | 53% | +8 pp [+1 pp, +14 pp] (192) | above | -9 pp [-21 pp, -1 pp] (195) | below | 36% | +1.18 | too few (0) |
| A+B stated horizon | 59 | 27 | 28 | 39% [29%, 45%] | 52% | +7 pp [+0 pp, +12 pp] (58) | above | -12 pp [-35 pp, +2 pp] (59) | not distinguishable | 34% | +0.73 | too few (0) |
| A+B default horizon | 136 | 93 | 29 | 40% [34%, 49%] | 53% | +8 pp [+2 pp, +17 pp] (134) | above | -8 pp [-16 pp, +7 pp] (136) | not distinguishable | 37% | +1.35 | too few (0) |
| C stance | 81 | 42 | 26 | 48% [40%, 53%] | 58% | -1 pp [-7 pp, +4 pp] (77) | not distinguishable | +9 pp [+1 pp, +17 pp] (81) | above | 62% | +0.80 | too few (0) |
| C stance, coder yes | too few (1) | 1 | 1 | | | | | | | | | | |
| C stance, coder partly | 80 | 41 | 26 | 49% [40%, 54%] | 59% | +0 pp [-7 pp, +5 pp] (76) | not distinguishable | +9 pp [+1 pp, +17 pp] (80) | above | 61% | +0.86 | too few (0) |
| D conditional (condition ignored) | 45 | 48 | 19 | 42% [30%, 55%] | 56% | -3 pp [-9 pp, +9 pp] (41) | not distinguishable | +0 pp [-11 pp, +24 pp] (45) | not distinguishable | 31% | +0.59 | too few (0) |
| E structural | too few (8) | 17 | 6 | | | | | | | | | | |

### By call type, pool A (headline)

| Cell | n resolved | n open | start months | hit rate [90%] | sign-only hit | hit - base rate [90%] (n) | vs base | hit - trend [90%] (n) | vs trend | agrees with trend | move (band units) | Brier skill (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direction | 31 | 13 | 18 | 32% [19%, 48%] | 46% | +1 pp [-9 pp, +15 pp] (30) | not distinguishable | -16 pp [-46 pp, +20 pp] (31) | not distinguishable | 32% | -0.27 | too few (0) |
| event | too few (4) | 0 | 4 | | | | | | | | | | |
| macro | too few (13) | 8 | 12 | | | | | | | | | | |
| relative | too few (2) | 1 | 2 | | | | | | | | | | |
| volatility | too few (4) | 3 | 4 | | | | | | | | | | |

### By variable family, pool A (headline)

| Cell | n resolved | n open | start months | hit rate [90%] | sign-only hit | hit - base rate [90%] (n) | vs base | hit - trend [90%] (n) | vs trend | agrees with trend | move (band units) | Brier skill (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| commodities | too few (1) | 3 | 1 | | | | | | | | | | |
| credit and vol | too few (4) | 2 | 4 | | | | | | | | | | |
| equity | too few (19) | 5 | 12 | | | | | | | | | | |
| fx | too few (3) | 0 | 3 | | | | | | | | | | |
| macro | too few (9) | 6 | 8 | | | | | | | | | | |
| other | too few (4) | 3 | 3 | | | | | | | | | | |
| rates | too few (14) | 6 | 12 | | | | | | | | | | |

### By horizon bucket, pool A (headline)

| Cell | n resolved | n open | start months | hit rate [90%] | sign-only hit | hit - base rate [90%] (n) | vs base | hit - trend [90%] (n) | vs trend | agrees with trend | move (band units) | Brier skill (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <=3m | too few (18) | 0 | 12 | | | | | | | | | | |
| >12-36m | too few (5) | 5 | 4 | | | | | | | | | | |
| >3-12m | 30 | 16 | 18 | 33% [24%, 42%] | 46% | +0 pp [-8 pp, +9 pp] (30) | not distinguishable | -27 pp [-47 pp, -8 pp] (30) | below | 33% | +0.02 | too few (0) |
| >36-60m | too few (1) | 4 | 1 | | | | | | | | | | |

### By year made, pool A (headline)

| Cell | n resolved | n open | start months | hit rate [90%] | sign-only hit | hit - base rate [90%] (n) | vs base | hit - trend [90%] (n) | vs trend | agrees with trend | move (band units) | Brier skill (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2018 | too few (2) | 0 | 2 | | | | | | | | | | |
| 2022 | too few (7) | 0 | 5 | | | | | | | | | | |
| 2023 | too few (3) | 0 | 1 | | | | | | | | | | |
| 2024 | too few (19) | 1 | 8 | | | | | | | | | | |
| 2025 | too few (17) | 14 | 8 | | | | | | | | | | |
| 2026 | too few (6) | 10 | 2 | | | | | | | | | | |

### By call type, pools A+B (A and B together; extra view, not a rules-v1 headline)

| Cell | n resolved | n open | start months | hit rate [90%] | sign-only hit | hit - base rate [90%] (n) | vs base | hit - trend [90%] (n) | vs trend | agrees with trend | move (band units) | Brier skill (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direction | 113 | 72 | 31 | 32% [24%, 41%] | 45% | +1 pp [-7 pp, +10 pp] (110) | not distinguishable | -18 pp [-32 pp, +0 pp] (113) | not distinguishable | 40% | -0.46 | too few (0) |
| event | too few (8) | 6 | 8 | | | | | | | | | | |
| macro | 47 | 31 | 24 | 60% [44%, 71%] | 74% | +26 pp [+13 pp, +37 pp] (47) | above | +17 pp [-7 pp, +31 pp] (47) | not distinguishable | 43% | +6.00 | too few (0) |
| relative | too few (9) | 3 | 8 | | | | | | | | | | |
| volatility | too few (18) | 8 | 11 | | | | | | | | | | |

### By variable family, pools A+B (A and B together; extra view, not a rules-v1 headline)

| Cell | n resolved | n open | start months | hit rate [90%] | sign-only hit | hit - base rate [90%] (n) | vs base | hit - trend [90%] (n) | vs trend | agrees with trend | move (band units) | Brier skill (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| commodities | too few (13) | 15 | 7 | | | | | | | | | | |
| credit and vol | 20 | 6 | 14 | 30% [0%, 38%] | 45% | +3 pp [-27 pp, +11 pp] (20) | not distinguishable | -15 pp [-60 pp, +4 pp] (20) | not distinguishable | 5% | -0.07 | too few (0) |
| equity | 53 | 25 | 23 | 25% [18%, 32%] | 33% | -5 pp [-8 pp, +0 pp] (53) | not distinguishable | -43 pp [-57 pp, -15 pp] (53) | below | 32% | -1.38 | too few (0) |
| fx | too few (12) | 6 | 8 | | | | | | | | | | |
| macro | 36 | 29 | 22 | 47% [31%, 57%] | 62% | +12 pp [+2 pp, +17 pp] (36) | above | +8 pp [-28 pp, +29 pp] (36) | not distinguishable | 36% | +1.58 | too few (0) |
| other | too few (12) | 15 | 7 | | | | | | | | | | |
| rates | 49 | 24 | 21 | 43% [29%, 63%] | 64% | +15 pp [+3 pp, +31 pp] (49) | above | -12 pp [-29 pp, +8 pp] (49) | not distinguishable | 47% | +4.70 | too few (0) |

### By horizon bucket, pools A+B (A and B together; extra view, not a rules-v1 headline)

| Cell | n resolved | n open | start months | hit rate [90%] | sign-only hit | hit - base rate [90%] (n) | vs base | hit - trend [90%] (n) | vs trend | agrees with trend | move (band units) | Brier skill (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <=3m | too few (19) | 0 | 12 | | | | | | | | | | |
| >12-36m | too few (6) | 6 | 5 | | | | | | | | | | |
| >3-12m | 169 | 110 | 30 | 38% [32%, 45%] | 52% | +7 pp [-0 pp, +15 pp] (167) | not distinguishable | -11 pp [-22 pp, -1 pp] (169) | below | 36% | +1.11 | too few (0) |
| >36-60m | too few (1) | 4 | 1 | | | | | | | | | | |

### By year made, pools A+B (A and B together; extra view, not a rules-v1 headline)

| Cell | n resolved | n open | start months | hit rate [90%] | sign-only hit | hit - base rate [90%] (n) | vs base | hit - trend [90%] (n) | vs trend | agrees with trend | move (band units) | Brier skill (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2018 | too few (6) | 0 | 2 | | | | | | | | | | |
| 2021 | too few (2) | 0 | 1 | | | | | | | | | | |
| 2022 | 32 | 0 | 6 | 53%  | 65% | +23 pp  (32) | no interval | +12 pp  (32) | no interval | 47% | +5.57 | too few (0) |
| 2022, without MT067 (25% of cell) | 24 | 0 | 6 | 46%  | 58% | +14 pp  (24) | no interval | +12 pp  (24) | no interval | 38% | +2.44 | too few (0) |
| 2023 | too few (10) | 0 | 4 | | | | | | | | | | |
| 2024 | 60 | 1 | 9 | 42%  | 53% | +7 pp  (58) | no interval | -12 pp  (60) | no interval | 28% | +0.54 | too few (0) |
| 2025 | 77 | 34 | 10 | 40%  | 56% | +9 pp  (76) | no interval | -3 pp  (77) | no interval | 40% | +0.56 | too few (0) |
| 2026 | too few (8) | 85 | 2 | | | | | | | | | | |

## Stated probabilities

Resolved rows with a stated probability: 0 (all pools). Brier skill is in the tables above (shown at n >= 20). Calibration buckets (shown at n >= 20):

| Bucket | n | mean stated | hit rate |
|---|---|---|---|
| 0.0-0.2 | too few (0) |  |  |
| 0.2-0.4 | too few (0) |  |  |
| 0.4-0.6 | too few (0) |  |  |
| 0.6-0.8 | too few (0) |  |  |
| 0.8-1.0 | too few (0) |  |  |

## Per speaker (pools A+B)

**Descriptive only; not a skill estimate; never used for weights or selection.** Speakers with >= 15 resolved rows, alphabetical, no intervals.

| Speaker | n | hit rate | hit - base rate (n) |
|---|---|---|---|
| Cem Karsan | 54 | 39% | +9 pp (52) |
| Niels Kaastrup-Larsen | 15 | 47% | +13 pp (15) |
| Stanley Druckenmiller | 16 | 25% | -9 pp (16) |

## Open rows by expected resolution quarter

| Quarter | open rows |
|---|---|
| 2026-Q2 | 1 |
| 2026-Q3 | 4 |
| 2026-Q4 | 34 |
| 2027-Q1 | 28 |
| 2027-Q2 | 47 |
| 2027-Q3 | 65 |
| 2027-Q4 | 23 |
| 2028-Q1 | 3 |
| 2028-Q2 | 3 |
| 2028-Q3 | 2 |
| 2028-Q4 | 3 |
| 2029-Q1 | 3 |
| 2029-Q2 | 3 |
| 2029-Q3 | 3 |
| 2029-Q4 | 1 |
| 2030-Q1 | 1 |
| 2030-Q3 | 1 |
| 2031-Q1 | 1 |
| 2031-Q2 | 1 |

## Rule gaps (narrowest reading applied; SCORING_RULES.md unchanged)

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

Level use among resolved rows: level ignored (no level series): 13; level ignored (unit mismatch): 2; level move: 5; level moverange: 6; level range on r/DEXUSEU: 1; level range on r/DGS10: 1; level range on r/DGS2: 1; level range on r/D__GSPC: 1; level threshold on cb:JP10: 1; level threshold on r/DCOILBRENTEU: 1; level threshold on r/DEXUSEU: 1; level threshold on r/DEXUSUK: 2; level threshold on r/DGS10: 5; level threshold on r/DGS2: 1; level threshold on r/Y_BTC_USD: 1

## Known limits (SCORING_RULES.md section 7)

- Selection: who gets interviewed, which views the argument maps kept as "current views", and which posts the X
  extraction kept. The pool is not a random sample of anyone's forecasts.
- Coding error: one model coded each view; the blind 20% recode agreement (`CODING_AGREEMENT_*.md`, tools/fcast/agree.py)
  is attached to every scorecard. Horizons and levels the coder converted from words carry that error.
- Hindsight in what counts as resolvable: the coder decided `resolvable`, told not to use hindsight but knowing
  history to mid-2026; a coder can unconsciously make hits easier to resolve.
- Short sample: most rows were made 2024-26, many are still open; few independent start months; one macro period.
- Overlap: many rows share the same months and markets, so rows are far from independent (hence month blocks).
- Measurement: price indices ignore dividends; FEDFUNDS and IMF series are monthly averages; upload date can be later
  than the recording; Nasdaq-100 vs Composite and other index ambiguity; 1990-2010 base rates come from a falling-yield
  era and may flatter "yields up" calls; bands were set by judgement, not fitted.

## Coding agreement (CODING_AGREEMENT_2026-11-11.md)

```
views coded by both: 363 (recode sample 363)
is a forecast (view level): agree 93.9% | kappa 0.88 | main yes 160 | recode yes 176
rows per view: main 1.14 | recode 1.21
views both call a forecast: 157 (best-matching row pair per view)
  variable_code (exact)    agree  89.8% | kappa 0.89
  variable family          agree  92.4% | kappa 0.91
  direction                agree  92.4% | kappa 0.89
  kind                     agree  89.8% | kappa 0.78
  call_type                agree  89.8% | kappa 0.84
  resolvable               agree  79.6% | kappa 0.60
  horizon bucket           agree  95.5% | kappa 0.89
  made_date (month)        agree  98.7% | kappa 0.99
  confidence               agree  55.4% | kappa 0.42
resolvable table (main -> recode): {('yes', 'yes'): 26, ('partly', 'no'): 15, ('partly', 'yes'): 8, ('partly', 'partly'): 87, ('no', 'no'): 12, ('no', 'partly'): 7, ('yes', 'partly'): 1, ('no', 'yes'): 1}
same variable family + direction + resolvable: 72.6%
```
