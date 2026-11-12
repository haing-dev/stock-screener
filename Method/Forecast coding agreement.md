---
tags: [method, spec]
file: /home/claude/stock-screener/docs/research/forecasts/CODING_AGREEMENT_2026-11-11.md
---
# Forecast ledger step 2.1: coding and agreement (2026-11-11)

Main coding: Sonnet (effort high), 11 batches of 165 views, spec v1. Independent blind recode of a random 20% (363 views, seed 20261111): Opus (effort high).
Scripts: tools/fcast/pull.py, validate.py, merge.py, agree.py. Data: macro-vault branch, pipeline/forecasts/ (views_raw.jsonl, coded/, recode/, ledger.csv).

## Ledger counts
```
views coded 1815 of 1815 | rows 2102 | missing views 0
kind: {'forecast': 791, 'stance': 179, 'not_forecast': 957, 'conditional': 175}
resolvable (forecast rows): {'partly': 842, 'yes': 167, 'no': 136}
why not: {'no_horizon': 721, 'vague_variable': 123, 'conditional_unmet_unknown': 114, 'unobservable': 19, 'no_direction': 1}
call type: {'macro': 154, 'direction': 619, 'relative': 42, 'event': 155, 'volatility': 52, 'structural': 123}
top variables: [('OTHER', 115), ('US_EQ', 109), ('TREND_FOLLOWING', 71), ('EQ_SINGLE', 65), ('POLICY_EVENT', 63), ('US_10Y', 55), ('EQ_SECTOR', 54), ('US_INFLATION', 52), ('US_POLICY_RATE', 50), ('USD', 40), ('VIX', 31), ('OIL', 31), ('US_TECH', 27), ('GEOPOLITICS', 23), ('EM_EQ', 22), ('GOLD', 20), ('US_GROWTH', 20), ('HEDGE_FUNDS', 19), ('LIQUIDITY', 18), ('GLOBAL_EQ', 16), ('BTC', 15), ('OTHER_RATES', 15), ('US_RECESSION', 15), ('COMMODITIES', 13), ('OTHER_COMMODITY', 13)]
speakers with forecasts: 74 | top: [('John Galt', 231), ('Cem Karsan', 161), ('Stanley Druckenmiller', 75), ('Alan Dunne', 67), ('Niels Kaastrup-Larsen', 65), ('Mark Rzepczynski', 50), ('Ken Tropin', 36), ('Rob Carver', 35), ('Rob Citrone', 33), ('Andrew Beer', 27), ('Katie Kaminski', 25), ('Rich Brennan', 24)]
made year: {'2018': 28, '2019': 4, '2020': 2, '2021': 4, '2022': 91, '2023': 43, '2024': 205, '2025': 350, '2026': 418}
```

## Agreement (main coding vs blind recode)
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

## Reading
- Reliable: whether a view is a forecast, the variable, the direction, the horizon bucket, the date.
- Weaker: `resolvable` (80%, kappa 0.60). The scorer must not rely on this field alone: it applies the mechanical
  tests of SCORING_RULES.md (a series exists, a direction is coded, a stated or default horizon).
- Not usable: `confidence` (55%).
- Copy check: identical free-text notes in 1 of 56 row pairs where both coders wrote a note; no sign of copying.
  Incident: the coders shared one scratch folder and overwrote each other's helper scripts; batch 05 was overwritten
  by another coder's script and restored by its own coder (no row changed); two agents saw about 30 raw input views of
  another file (inputs only, no coded output). All 11 batches and both recode files pass the validator.

## Spec gaps reported by the coders (for spec v2; v1 coding is kept as is)
1. Claims that appear only in the map's view text and in no verbatim quote (a horizon, level or position): code or drop.
   This decides many yes / partly rows.
2. Views relayed from another person (host quoting a guest, a cited paper): whose forecast is it.
3. Conditionals: when is `resolvable` yes; `why_not` for not_forecast rows.
4. Vague horizons ("next few months", "eventually"), calendar-tied horizons (FOMC meetings), ranges ("5 or 10 years"),
   horizons under a month.
5. Rate codes in relative calls (yield or bond return); "bonds" with no tenor; low-return calls with no direction.
6. Missing codes: FX volatility, single countries outside the list, equal-weight / dispersion, stock-bond correlation,
   non-price variables. 115 forecast rows sit in OTHER.
7. Word-only probabilities; a systematic manager's model positions (stance or not).
