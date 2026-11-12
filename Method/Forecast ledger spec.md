---
tags: [method, spec]
file: /home/claude/stock-screener/docs/research/forecasts/FORECAST_SPEC.md
---
# Forecast ledger: normalisation spec v1 (WORKFLOW step 2.1, 2026-11-11)

Purpose: turn each dated view (one line of `pipeline/forecasts/batches/batch_NN.jsonl` on the macro-vault branch) into
zero to three forecast rows: who / date / variable / direction / horizon. Descriptive record only; never used for weights.

## Hard rules for the coder
1. Code only what the speaker said (the `view`, `reasoning` and verbatim `quotes`). The quotes are the ground truth; if
   the view text and the quote disagree, follow the quote and set `note`.
2. NEVER use knowledge of what happened afterwards. Do not judge whether a call was right, do not look anything up, do
   not let hindsight decide what counts as resolvable. Code as if you were reading it on the day it was said.
3. No guessing: a field the speaker did not state is null (or `unstated`). Do not invent horizons or levels.
4. One row per distinct prediction. A view with no prediction gives one row with `kind` = `not_forecast`.
   At most three rows per view (the three most specific).
5. Output: one JSON object per line in `pipeline/forecasts/coded/<same file name>`, fields exactly as below, then run
   `python3 /home/claude/stock-screener/tools/fcast/validate.py <output file> <input file>` until it prints OK.

## Fields
| field | values |
|---|---|
| view_id | copied from the input |
| row | 1, 2 or 3 |
| who | copied from input `speaker` |
| made_date | date the view was stated, `YYYY-MM-DD`, `YYYY-MM` or `YYYY`; take it from `as_of_text`, else `upload_date` |
| date_precision | `day` / `month` / `quarter` / `year` |
| kind | `forecast` (a statement about a future value, direction or event) / `conditional` (if X then Y) / `stance` (a position or preference with a clear direction, e.g. "long gold", "underweight US equities") / `not_forecast` (description, explanation, method, past performance, advice without direction) |
| variable_code | one code from the list below; relative calls use `A>B` with two codes (first is expected to do better) |
| variable_text | the variable in the speaker's words, max 12 words |
| direction | `up` / `down` / `flat` / `range` / `outperform` / `underperform` / `higher_vol` / `lower_vol` / `event_yes` / `event_no` |
| level | stated target, threshold or size as text with unit (e.g. "above 5%", "+20%", "$4,000"), else null |
| horizon_months | number of months to the stated end of the forecast (a stated date is converted from made_date), else null |
| horizon_text | the speaker's own words for the horizon (e.g. "by year end", "next decade"), else null |
| condition | the if-part in max 20 words when kind = `conditional`, else null |
| probability | stated probability 0-1, else null |
| confidence | `high` / `medium` / `low` / `unstated` (speaker's own emphasis, not yours) |
| call_type | `direction` (a market price or rate goes up/down) / `relative` (A against B) / `macro` (growth, inflation, jobs, policy rate path) / `event` (a discrete event happens or not: recession, default, policy action, deal) / `volatility` / `structural` (regime claim over 3+ years) |
| resolvable | `yes` (variable observable in public data, direction clear, horizon stated) / `partly` (variable and direction clear, horizon missing or vague) / `no` (vague variable, no direction, or unobservable) |
| why_not | when resolvable is not `yes`: `no_horizon` / `vague_variable` / `no_direction` / `unobservable` / `conditional_unmet_unknown` |
| claim_ids | copied from the input |
| note | max 20 words, only when something needs flagging (quote disagrees with view, two speakers merged, date unclear), else null |

## variable_code list
Equities: `US_EQ` (S&P 500 / US stocks broadly), `US_TECH` (Nasdaq, AI / mega-cap tech), `US_SMALL`, `EU_EQ`, `JP_EQ`,
`CN_EQ` (China, Hong Kong), `IN_EQ`, `EM_EQ`, `GLOBAL_EQ`, `EQ_SECTOR` (a named sector or industry), `EQ_SINGLE` (a
named company), `EQ_VALUE_VS_GROWTH`.
Rates: `US_POLICY_RATE`, `US_2Y`, `US_10Y`, `US_30Y`, `US_CURVE` (steeper = up), `US_REAL_YIELD`, `US_TERM_PREMIUM`,
`EU_RATES`, `JP_RATES` (JGB yields, BoJ), `UK_RATES`, `OTHER_RATES`.
Currencies: `USD` (broad dollar), `EURUSD`, `USDJPY`, `GBPUSD`, `USDCNY`, `EM_FX`, `OTHER_FX`.
Commodities: `GOLD`, `SILVER`, `OIL`, `NATGAS`, `COPPER`, `URANIUM`, `AGRI`, `COMMODITIES` (broad), `OTHER_COMMODITY`.
Credit and volatility: `CREDIT_SPREADS` (wider = up), `PRIVATE_CREDIT`, `VIX` (equity volatility), `RATES_VOL`.
Macro: `US_GROWTH`, `US_RECESSION` (event), `US_INFLATION`, `US_JOBS` (unemployment up = up), `US_DEFICIT_DEBT`,
`GLOBAL_GROWTH`, `CN_GROWTH`, `EU_GROWTH`, `JP_INFLATION`, `LIQUIDITY` (central-bank balance sheets, money supply).
Other: `BTC` (bitcoin, crypto), `REAL_ESTATE`, `TREND_FOLLOWING` (CTA / managed futures performance),
`HEDGE_FUNDS` (other strategy performance), `POLICY_EVENT` (law, tariff, election, central-bank or government action),
`GEOPOLITICS`, `OTHER` (use `variable_text`).
