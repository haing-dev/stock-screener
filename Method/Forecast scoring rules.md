---
tags: [method, spec]
file: /home/claude/stock-screener/docs/research/forecasts/SCORING_RULES.md
---
# Forecast ledger: scoring rules v1 (WORKFLOW step 2.2, 2026-11-12)

Applies to `pipeline/forecasts/ledger.csv` (macro-vault branch; fields in `FORECAST_SPEC.md`). Written before any
outcome was computed. The scorer (step 2.3) applies every rule below by script; where a rule needs a choice, the choice
is fixed here. Scoring is descriptive (WORKFLOW section 2 rule 8, section 8 item 7): it is never a source of weights,
pod selection or design.

## 1. Which rows are scored
Each row lands in exactly one pool, tested in this order:
| Pool | Rows | Horizon |
|---|---|---|
| D conditional | `kind` = conditional, unless `resolvable` = no for a reason other than `conditional_unmet_unknown` | stated, else default |
| C stance | `kind` = stance, `resolvable` yes or partly | stated, else default |
| E structural | `call_type` = structural, `resolvable` yes or partly | stated, else 36 |
| A headline | `kind` = forecast, `resolvable` = yes | stated (`horizon_months`) |
| B default-horizon | `kind` = forecast, `resolvable` = partly | `horizon_months` if given, else default |
Not scored: `kind` = not_forecast; `resolvable` = no (counted by `why_not`); `date_precision` = year (date too coarse);
rows whose `variable_code` has no series (section 3); rows above the maximum horizon.

- Conditional rows are scored as if unconditional and kept in their own pool, never merged into A or B. Deciding
  whether the condition held needs judgement; ignoring it needs none, and keeping the pool apart stops it from
  colouring the headline numbers.
- Default horizons (months) when `horizon_months` is null: direction 12, relative 12, macro 12, event 12,
  volatility 6, structural 36.
- Maximum horizon 60 months; longer rows are excluded and counted. Minimum: 5 trading days.
- A row whose end date (or the publication of its end reading) falls after the last date of its series is **open**.
  It is re-checked on every run after a cache refresh and scored once it resolves. Open rows are never marked to
  market. Once resolved, the result is frozen (written once to `scored_frozen.csv` with the run date, the cache
  `fetched` stamps and this rules version); later data revisions do not change it.

## 2. Outcome definitions
**Dates.** Resolved made date: day precision = `made_date`; month = last calendar day of the month; quarter = last day
of the quarter. Start = first observation strictly after the resolved made date. End date = resolved made date plus
`horizon_months` calendar months (fractional part x 30.44 days); end value = last observation on or before it. A
gap of more than 10 trading days at either point -> unscored (data gap).
Monthly series (Yahoo month-end closes, IMF and FRED monthly): start = the value of the month containing resolved made
date + 1 day; end = the value of the month `round(h)` months later; h < 1 on a monthly series -> unscored.

**Measured change** (by family of the series in section 3):
- Prices, ETFs, indices, commodities, FX, BTC, balance sheets, house prices: simple % change, end/start - 1.
- Yields, spreads in points, policy rates, curve, real yield, term premium: change in percentage points.
- Credit spreads: change as % of the start spread. Volatility indices (VIX, MOVE): change as % of the start level.
- Macro readings: see the macro rule below.

**Dead band** (12-month size, scaled by sqrt(h/12) with h clipped to 1..60, unless marked "fixed"):
equities, REITs, trend following 4%; commodities 6%; FX 2%; BTC 15%; liquidity and house prices 2%; yields, curve,
real yield, term premium 0.25 pt; policy rates 0.10 pt fixed; credit spreads 10% of start spread; VIX and MOVE 15%
of start level fixed; inflation 0.3 pt fixed; unemployment 0.2 pt fixed; GDP growth 0.5 pt fixed; debt/GDP 1 pt
fixed; deficit 10% of the start 12-month deficit fixed; realised-volatility ratio 10% fixed.
Outcome category: up if change > +band, down if change < -band, else flat. `up`/`down` hit when the category
matches; `flat`/`range` hit when the category is flat. A sign-only hit (ignoring the band) is printed as a secondary column.

**Level.** If `level` parses (strip $ , ; k = x1000; bp = /100 pt): two numbers joined by "-", "to" or "between" =
range, hit if the end value is inside. One number with a sign or a move word (up, down, gain, fall, rise, drop), or a
"%" on a price-family variable = move size, which replaces the band. One number otherwise = threshold T in series
units ("%" on rate or macro variables is a level): up/event_yes or "above, over, at least, >" -> hit if end >= T;
down or "below, under, <" -> end <= T; flat/range with no side word -> |end - T| <= band. The threshold alone decides.
Guard: price-family T outside 0.25x-4x the start value, or rate/macro T more than 10 points from start -> level
ignored (unit mismatch), direction scored. A touch hit (window max/min reaches T) is printed as a secondary column.
Index names in `variable_text` pick the level series: S&P/SPX ^GSPC, Nasdaq ^IXIC (Nasdaq 100/NDX: level ignored),
Russell ^RUT, Nikkei ^N225, Euro Stoxx ^STOXX50E, DAX ^GDAXI, FTSE ^FTSE, CAC ^FCHI, Hang Seng ^HSI, Shanghai
000001.SS, Sensex ^BSESN, Nifty ^NSEI, Kospi ^KS11, DXY/dollar index DX-Y.NYB, Brent DCOILBRENTEU; else the code's
default series if marked L in section 3, else the level is ignored.

**Relative calls** (`A>B`, or `outperform`/`underperform`): outcome = total return of A minus total return of B over
the same window, using the "relative" column of section 3 (a rate code means the bond ETF, the policy rate means
cash). If either leg is monthly, both use month-end values. Band = the larger of the two legs' bands. Single-code
outperform/underperform: equity codes against SPY (US_EQ against ACWI); other codes = up/down. A leg without a
relative series -> unscored.

**Volatility calls** (`higher_vol`/`lower_vol`): on VIX or RATES_VOL they mean up/down of the index. On any other
variable with a daily series: realised volatility = standard deviation of daily log changes (daily changes for
yields), annualised, over (start, end], against the same over the equal-length window ending at start (at least 63
trading days). higher_vol hit if the ratio > 1.10, lower_vol if < 0.90. Monthly-only series -> unscored.

**Event calls.** Scorable: (1) US_RECESSION: a recession starts inside (start, end] when USREC turns 0 -> 1, or
when two consecutive quarters of negative A191RL1Q225SBEA both end inside the window. event_yes resolves on the first
such sign; event_no resolves 12 months after the end date (NBER dating lag). (2) Equity codes whose `variable_text`
matches crash or bear market: maximum drawdown inside the window, from the running peak starting at the start value,
>= 20%; correction: >= 10%. (3) Any code with a parseable threshold `level`: touch rule (series reaches T inside the
window). All other events (POLICY_EVENT, GEOPOLITICS, default, deal, law, election) are unscored in v1.

**Macro calls.** Start reading = the last reference period published before the resolved made date, using fixed
publication lags after the period ends: CPI 15 days, unemployment 7, GDP 30 (quarter), PCE 30, M2 30, Fed funds 1,
WALCL 1, Treasury monthly statement 15, debt/GDP 90, Case-Shiller 60. End reading = the last reference period ending on
or before the end date; it resolves when published under the same lag. If the end period is not later than the start
period -> unscored (horizon too short for the data). Quantities: inflation = 12-month % change of the index; growth =
4-quarter % change of real GDP; unemployment = rate; policy rate = monthly average, end month taken one month later
so a decision in the last month counts in full; WEO annual (CN_GROWTH, EU_GROWTH, JP_INFLATION) = the value for a
calendar year in the first WEO vintage that reports it as actual; start year = last full year before made date; end
year = the year containing the end date if it is on or after 1 July, else the year before. Vintage: first release
(`_FR` files) where it exists; CPIAUCNS is never revised; otherwise the vintage in the cache at the resolving run,
frozen then.

## 3. variable_code -> series
Files under `cache/macro/raw/` (`r/` = `research/`; no prefix = the root folder). D = daily, W = weekly, M = monthly, Q = quarterly, A = annual.
"Through" = last date in the cache on 2026-11-12. L = default series also used for levels. Base proxy = series used
for the base rate only, when the main series has fewer than 60 monthly start points in the base window.
| Code | Direction / level series | Through | Relative (total return) | Base proxy |
|---|---|---|---|---|
| US_EQ | r/D__GSPC D, price L | 2026-10-30 | r/D_SPY | |
| US_TECH | r/D__IXIC D, price | 2026-10-30 | r/D_QQQ | |
| US_SMALL | r/D__RUT D L | 2026-10-30 | r/D_IWM | |
| EU_EQ | r/D__STOXX50E D L | 2026-10-30 | r/D_EZU (USD) | r/D__FCHI |
| JP_EQ | r/D__N225 D L | 2026-10-30 | r/D_EWJ | |
| CN_EQ | r/D__HSI D L; "Shanghai, A-share, CSI" -> r/D_000001_SS | 2026-10-30 | r/D_MCHI | r/Y_FXI |
| IN_EQ | r/D__BSESN D | 2026-10-30 | r/D_INDA | none (base n/a) |
| EM_EQ | r/Y_EEM M | 2026-10 | r/Y_EEM | |
| GLOBAL_EQ | r/Y_ACWI M | 2026-10 | r/Y_ACWI | r/D_SPY |
| EQ_SECTOR | keyword table below, monthly ETFs (Y_ file in r/ if present, else root) | 2026-10-22 to 10-30 | same | |
| EQ_SINGLE | no free series here: not scored yet | | | |
| EQ_VALUE_VS_GROWTH | r/Y_IWD minus r/Y_IWF M (up = value ahead) | 2026-10 | same | |
| US_POLICY_RATE | r/FEDFUNDS M | 2026-09 | r/Y_BIL | |
| US_2Y / US_10Y / US_30Y | r/DGS2 / r/DGS10 / r/DGS30 D L | 2026-10-28 | Y_SHY / r/D_IEF / r/D_TLT | |
| US_CURVE | r/T10Y2Y D (steeper = up) | 2026-10-29 | none | |
| US_REAL_YIELD | r/DFII10 D L | 2026-10-28 | r/Y_TIP | |
| US_TERM_PREMIUM | THREEFYTP10 D | 2026-10-16 | none | |
| EU_RATES | r/cb_de_10y D L; "ECB, policy, hike, cut" -> r/ECBDFR D | 2026-10-30 | none | |
| JP_RATES | r/cb_jp_jgb_all + cb_jp_jgb_recent 10Y D L; "BoJ, policy, hike, cut" -> 2Y column | 2026-10-29 | none | |
| UK_RATES | r/cb_gb_yields IUDMNPY D L; "BoE, policy, hike, cut" -> IUDSNPY | 2026-10-28 | none | |
| OTHER_RATES | country name -> r/IRLTLT01{CC}M156N M (CA AU IT FR ES NL CH SE NO DK KR MX NZ ZA AT BE PT) | 2026-09 | none | |
| USD | r/D_DX_Y_NYB D L | 2026-10-30 | r/Y_UUP | |
| EURUSD | r/DEXUSEU D L | 2026-10-23 | none | |
| USDJPY | r/DEXJPUS D L | 2026-10-23 | none | |
| GBPUSD | r/DEXUSUK D L | 2026-10-23 | none | |
| USDCNY | r/DEXCHUS D L | 2026-10-23 | none | |
| EM_FX | r/DTWEXEMEGS D, inverted (EM currencies up = up) | 2026-10-23 | none | |
| OTHER_FX | currency keyword -> r/DEX* D (AUD USAL, NZD USNZ, CAD CAUS, CHF SZUS, MXN MXUS, BRL BZUS, INR INUS, KRW KOUS, ZAR SFUS, NOK NOUS, SEK SDUS, HKD HKUS, TWD TAUS); up = that currency gains on USD unless the text quotes a pair (USDxxx / xxxUSD) | 2026-10-23 | none | |
| GOLD | r/D_GC_F D L | 2026-10-30 | r/D_GLD | |
| SILVER | r/D_SI_F D L | 2026-10-30 | r/Y_SLV | |
| OIL | r/DCOILWTICO D L; "Brent" -> r/DCOILBRENTEU | 2026-10-27 | r/Y_USO | |
| NATGAS | r/D_NG_F D L | 2026-10-30 | r/Y_UNG | |
| COPPER | r/D_HG_F D L | 2026-10-30 | r/Y_CPER | |
| URANIUM | r/PURANUSDM M L | 2026-09 | r/Y_URA | |
| AGRI | crop keyword (OTHER_COMMODITY table), else r/Y_DBA M | 2026-10 | r/Y_DBA | r/PFOODINDEXM |
| COMMODITIES | r/Y_DBC M | 2026-10 | r/Y_DBC | r/PALLFNFINDEXM |
| OTHER_COMMODITY | keyword: platinum D_PL_F, palladium Y_PA_F, cocoa Y_CC_F, coffee D_KC_F, sugar D_SB_F, cotton D_CT_F, wheat D_ZW_F, corn D_ZC_F, soy D_ZS_F, cattle D_LE_F, heating oil D_HO_F, gasoline D_RB_F, iron ore PIORECRUSDM, aluminium PALUMUSDM, nickel PNICKUSDM, zinc PZINCUSDM, lithium Y_LIT; else not scored | 2026-09 to 10-30 | none | |
| CREDIT_SPREADS | r/BAMLH0A0HYM2 D (HY OAS) when it covers the window and the 12 months before; else r/DBAA minus r/DGS10 D | 2026-10-29 | r/Y_HYG (asset) | DBAA-DGS10 |
| PRIVATE_CREDIT | no direction convention in the spec: not scored yet | | | |
| VIX | r/D__VIX D L | 2026-10-30 | none | |
| RATES_VOL | r/Y__MOVE M L | 2026-10 | none | |
| US_GROWTH | r/GDPC1 Q (4-quarter change) | 2026 Q3 | none | |
| US_RECESSION | USREC M + r/A191RL1Q225SBEA Q (event rule) | 2026-09 / Q3 | none | |
| US_INFLATION | r/CPIAUCNS M; "core" -> r/CPILFESL_FR; "PCE" -> r/PCEPI ("core PCE" r/PCEPILFE) | 2026-09 | none | |
| US_JOBS | r/UNRATE_FR M (up = unemployment up) | 2026-09 | none | |
| US_DEFICIT_DEBT | "debt" -> r/GFDEGDQ188S Q; else 12-month sum of r/MTSDS133FMS M, sign flipped (wider deficit = up) | 2026 Q2 / 2026-09 | none | |
| GLOBAL_GROWTH | no world series here: not scored yet | | | |
| CN_GROWTH | r/imf_weo_vintages NGDP_RPCH CHN A | 2026_OCT vintage | none | none (base n/a) |
| EU_GROWTH | same, simple mean of DEU FRA ITA ESP A | 2026_OCT vintage | none | none (base n/a) |
| JP_INFLATION | same, PCPIPCH JPN A (FRED/OECD monthly Japan CPI stop 2021-06) | 2026_OCT vintage | none | none (base n/a) |
| LIQUIDITY | r/WALCL W; "M2, money supply" -> r/M2SL; "reserves" -> r/WRESBAL; "ECB" -> r/ECBASSETSW; "BoJ" -> r/JPNASSETS | 2026-10-28 | none | |
| BTC | r/Y_BTC_USD M L | 2026-10 | same | none (base n/a) |
| REAL_ESTATE | "home, house, housing price" -> r/CSUSHPINSA M; else r/Y_VNQ M | 2026-08 / 2026-10 | r/Y_VNQ | |
| TREND_FOLLOWING | r/aqr_tsmom_factors TSMOM M (cumulative excess return) | 2026-05 | r/Y_DBMF | |
| HEDGE_FUNDS, POLICY_EVENT, GEOPOLITICS, OTHER | no free series here: not scored yet | | | |
EQ_SECTOR keywords (case-insensitive on `variable_text`, first match wins): semiconductor/semis/chip SMH; software
IGV; biotech XBI; regional bank KRE; bank KBE; insur KIE; financial XLF; junior miner GDXJ; gold miner/gold stock
GDX; uranium URA; copper miner COPX; lithium LIT; rare earth REMX; homebuild XHB; defen(c|s)e/aerospace ITA;
airline JETS; E&P/exploration XOP; energy/oil stock/oil compan XLE; mining/miner XME; health/pharma XLV; utilit XLU;
staples XLP; retail XRT; discretionary/consumer XLY; transport IYT; industrial XLI; material/chemical XLB;
communication/telecom/media VOX; real estate/REIT VNQ; tech XLK; else not scored. All keyword tables use the same rule.
Through-dates move with each cache refresh (macro research fetch); the scorer prints the `fetched` stamps it used.

## 4. Baselines (fixed now)
- **Base window**: monthly start points from 1990-01 to 2010-12 (or the series start, if later), windows ending by
  2010-12. It ends before every forecast date and keeps base rates inside the design era (the 2011+ holdout is not
  summarised). At least 60 start points, else the base proxy, else base rate n/a.
- **(a) Base rate** p = share of same-length windows in the base window whose outcome falls in the forecast's
  category (same band, threshold converted to the move it requires from the start value, same event definition).
- **(b) Trend continuation** = the category of the variable's own change from the last observation on or before
  made date - 12 months to the last observation on or before made date (12-month band). Volatility: higher if
  realised vol over the h-length window before start (>= 63 days) exceeds the 12 months before that. Events:
  persistence (an event in the prior 12 months predicts event_yes). Relative: sign of the 12-month return difference.
- **(c) Brier** for rows with `probability` q (applies to the stated outcome): Bf = (q - hit)^2 against Bb = (p - hit)^2.
- **Beats**: base rate if mean(hit - p) has a 90% interval above 0; trend if mean(hit - trend hit), on the same rows,
  has a 90% interval above 0; Brier if mean(Bb - Bf) has a 90% interval above 0. Interval across 0 = "not
  distinguishable"; below 0 = "below". Rows with a baseline n/a drop out of that comparison only (counted).

## 5. Aggregation
- Duplicates: sort by resolved made date, then `forecast_id`; a row is a duplicate if a kept row with the same `who`,
  `variable_code` (exact, including A>B) and `direction` was made in the 30 days before it. Earliest kept, the rest
  counted. Applied across all pools.
- Tables (pool A headline, A+B line, then one line each for C, D, E): by `call_type`; by family (equity, rates, fx,
  commodities, credit and vol, macro, other; relative calls by their first leg); by horizon bucket (<=3, >3-12,
  >12-36, >36-60 months, effective horizon); by year made. Columns: n resolved, n open, hit rate, sign-only hit,
  mean (hit - p), mean (hit - trend hit), share agreeing with trend, mean move in the stated direction in band units,
  Brier skill (n with probability).
- Intervals: circular block bootstrap over calendar months of the start date (all rows starting in a month move
  together), blocks of 12 consecutive months, 2,000 draws, seed 20261112, 90% percentile interval.
- Minimum: a number is shown only for cells with >= 20 resolved non-duplicate rows from >= 6 distinct start months;
  else "too few (n)". If one source holds more than 20% of a cell, the cell is also printed without that source.
- Per-speaker table: speakers with >= 15 resolved rows in A+B; n, hit rate, mean (hit - p); no intervals, no ranking,
  alphabetical, headed "descriptive only; not a skill estimate; never used for weights or selection".
- Calibration (rows with `probability`): buckets 0-0.2, 0.2-0.4, 0.4-0.6, 0.6-0.8, 0.8-1, each shown at n >= 20.

## 6. What the scorecard prints, and never prints
Prints: the funnel (ledger rows -> pools -> duplicates -> no series -> excluded -> open -> resolved, by reason), the
tables of section 5, open rows by expected resolution quarter, the rules version, cache stamps and the coding
agreement table. Never prints: any return, Sharpe or drawdown of the book, a pod or a backtest; statistics of a
variable over 2011+ not tied to a forecast; per-row realised moves (they stay in `scored.csv` for audit). The
scorecard is not an input to any pod spec, weight or selection. Outcome data dated 2011+ are used here solely to
resolve the investors' recorded forecasts (and each forecast's own trend baseline); base rates use 1990-2010 only.

## 7. Known limits
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

## 8. Change log
- v1, 2026-11-12: written before any outcome was computed.
