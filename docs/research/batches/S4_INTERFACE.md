# S4 interface v2: the independent rebuild of the Core parts (TESTING_PROTOCOL 7.6 step 6 S4)

**Version 2 (2026-11-27, after CHECK_CORE M2, the coordinator's option A; gm/CHANGES.md "Core book v1", corrections
paragraph).** Version 1 (commit 28f14a6, in this file's git history) handed over the engine's carry measure, value
measure and volatility estimate. Version 2 hands over RAW inputs only: the rebuild derives the carry measure, the
value measure and the volatility model itself from the spec text (section 2a below). Section 1 (the function and its
keys) is unchanged; section 3 adds the raw-input check; section 4 is unchanged.

Written 2026-11-27 by the Core book v1 builder, BEFORE the job code, for the separate agent that writes
`tools/bbgq/lib/rebuild_s4.py` from the specs alone. The builder does not read, write or edit that file. The PC job
`tools/bbgq/jobs/gm_core_v1.py` (library `tools/bbgq/lib/core_v1.py`) calls exactly the function below.

Registered test (7.6 step 6): "S4 an independent rebuild from the spec alone matches within 15% (WORKFLOW 4.5: design
net Sharpe and annualised mean each within 15% relative)."

## 1. The function

```python
VERSION = "rebuild_s4-<x.y.z>"          # module constant, printed by the job

def part_returns(inputs: dict, cut: str = "2010-12-31") -> dict:   # -> dict[str, pandas.Series]
```

Returns monthly NET returns at k = 1 (TESTING_PROTOCOL 7.3 items 1-2, holding cut 7.3 item 5), cost multiple 1, one
series per key below, each scaled as that part would be held ALONE: its own block scaling, the part's unit-volatility
rescaling and the book's 10% target, with the engine's caps and costs as registered (TESTING_PROTOCOL 7.4 E9, 7.7
"Held size"; specs s3, s5, s9; gm/CHANGES.md "gm-2.1.0 feature version" items 4-5 and closed item 5).

| Key | Part | Components (pod, class, version) | Decisive in S4 |
|---|---|---|---|
| `"trend"` | Trend | every class, every version (the A2-final book has one Trend form: sign of 1, 3 and 12-month excess return, averaged) | yes |
| `"carry"` | Carry's Core part as ONE part: currencies version 2 (rank in class) plus energy versions 1 (sign) and 2 (rank) | FX v2, CM v1, CM v2 | yes |
| `"value_eq"` | Value's Core part: equities (the A2-final book has version 1 only) | EQ, all versions | yes |
| `"carry_fx_v2"` | Carry currencies version 2 alone | FX v2 | no (reported) |
| `"carry_energy"` | Carry energy versions 1 and 2 alone | CM v1, CM v2 | no (reported) |

`"carry"` is decisive because 7.2 item 5 and 7.6 step 6 name ONE Carry Core part ("Carry currencies v2 + energy"),
held as one part of the equal-risk Core book (config.CORE_PARTS: three parts, n = 3). Its two legs alone are reported
only. All five keys are required: a missing key, an exception, or a series that breaks section 3 makes the job STOP
before any S4 line (a broken rebuild is not a failed part).

Each series: `pandas.Series` of floats, index = `pandas.PeriodIndex` with freq "M" (the month the return is earned),
no month after `cut`'s month, NaN (or absent) in months without a net return (warm-up of the scalers, no position).
Decimal units per month (0.01 = 1%).

## 2. `inputs` (exactly what the job passes; deep copies)

RAW month-end and daily inputs, before any engine signal or volatility code. Every frame holds design months only:
nothing dated after 2010-12-31. Monthly frames have a `pandas.PeriodIndex` with freq "M" over 1960-01..2010-12 (612
rows; the row labelled t is the month t, observed at its last trading day); NaN = no value. Market ids are the
engine's strings. Units are stated per key; "decimal" means 0.01 = 1%.

| Key | Type and shape | Content |
|---|---|---|
| `"R"` | DataFrame, 612 x 65 | monthly EXCESS return of each market in month t, decimal (futures-style: equities over the local 3-month rate, bonds over the 3-month rate, currencies incl. the rate gap, commodities excess return): the A1 panel (free data, Bloomberg-extended backwards where A1 admitted a series). Includes `cm_aqr_ew` (to 2000-12) and three `sp_*` spread columns that no pod trades. This is also the monthly input of the volatility model |
| `"D"` | DataFrame, DatetimeIndex of days (12,668 rows, 1962-01-02..2010-12-31), 61 columns | daily return of each market with free daily data, decimal: for `bd_*` and `st_*` the PRICE return (minus duration x yield change); for every other market the LOG return. The daily file's own 25% filter is already applied (no value with absolute size 0.25 or more). NaN = no value that day. This is the daily input of the volatility model ("where free daily data exist" = the market is a column of D with a value) |
| `"days"` | DatetimeIndex (10,349 days) | NYSE open days = dates of the daily ^GSPC closes, to 2010-12-31. "Month-end" = a month's last NYSE day, "first trading day" = its first |
| `"rate3m"` | DataFrame, 612 x 14, columns `"US", "EZ", "JP", "GB", "CH", "AU", "NZ", "CA", "SE", "NO", "MX", "BR", "KR", "ZA"` | local 3-month interest rate, PERCENT per year (5.0 = 5%), the monthly figure FOR month t: OECD monthly average of the 3-month interbank rate (US: the 3-month Treasury bill TB3MS, spliced with the OECD series; EZ: the euro-area series spliced onto Germany before it starts; JP, CH, BR, KR, ZA, with their OECD call-money alternatives where the 3-month series is absent). NOT lagged: these monthly averages are published after the month ends, so the carry rule's one-month lag (section 2a) is the rebuild's to apply. Where a series stops, the loader has already carried its last value forward for at most 12 months |
| `"fx_rate_country"` | dict, 13 entries | currency market -> its `rate3m` column: `fx_eur` EZ, `fx_jpy` JP, `fx_gbp` GB, `fx_chf` CH, `fx_aud` AU, `fx_nzd` NZ, `fx_cad` CA, `fx_sek` SE, `fx_nok` NO, `fx_mxn` MX, `fx_brl` BR, `fx_krw` KR, `fx_zar` ZA; the dollar rate is column `"US"` |
| `"eia"` | dict, 4 entries `cm_wti`, `cm_natgas`, `cm_heatoil`, `cm_gasoline` -> DataFrame 612 x 2, columns `1` and `2` (int) | settlement price of NYMEX contract 1 (front) and contract 2 (next) at month-end t, USD per unit of the contract (EIA daily settlements, last value of the month), with the A1 data swap included (for `cm_wti`: Bloomberg contract months before the free EIA history starts, A1 block 2) |
| `"french_with"` | DataFrame, 612 x 7, columns `eq_de_dax, eq_gb_ftse, eq_fr_cac, eq_jp_nikkei, eq_ca_tsx, eq_au_asx, eq_hk_hsi` | Ken French international country market portfolio, monthly return WITH dividends, decimal (USD), month t (Germany, UK, France, Japan, Canada, Australia, Hong Kong) |
| `"french_without"` | DataFrame, 612 x 7, same columns | the same portfolios, monthly return WITHOUT dividends, decimal |
| `"us_total"` | Series, 612 | SPY ETF monthly TOTAL return (change of the dividend-adjusted month-end close), decimal, month t (from 1993-02) |
| `"us_price"` | Series, 612 | S&P 500 index (^GSPC) monthly PRICE return, decimal, month t |
| `"cost"` | dict market -> (one_way_bp, rolls_per_year) | the engine's cost table for every `R` column (bp of notional per unit traded; futures rolls a year, each roll charged as a round trip of the held position) |
| `"em_borrow"` | tuple of market ids | emerging equity markets whose SHORT positions pay 1% a year borrow |
| `"classes"` | dict class -> tuple of id prefixes | `{"EQ": ("eq_",), "FI": ("bd_", "st_"), "FX": ("fx_",), "CM": ("cm_",)}` |
| `"meta"` | dict | informational only: config name and hash of the A2-final book (gm-2.0.4-candidate-x1, 77374d7bef), A1 panel id, engine version |

Not in `inputs` (the rebuild derives them from the spec text): the carry measure, the value measure, the volatility
estimate, trend scores, ranks, signs, class division, the 0.40 risk unit, block / part / book scalers, the 10% target,
caps, the k = 1 return form, cost timing, the holding cut. Bond yields, CPI and exchange-rate levels are not passed:
no Core part reads them (bond carry, bond and currency value are shadow parts, outside S4's keys).

## 2a. Registered rules the rebuild applies itself (quoted; the specs govern, these are their texts)

1. Carry measure, currencies (SPEC_Carry s3 step 2): "Currencies (13): ((local 3-month rate - US 3-month rate) / 100),
   lagged 1 month (OECD monthly averages)." With `rate3m` and `fx_rate_country`: the value at month-end t uses the
   rates of month t - 1.
2. Carry measure, energy (SPEC_Carry s3 step 3): "Energy (cm_wti, cm_natgas, cm_heatoil, cm_gasoline): 12 x (F1 / F2 -
   1), EIA NYMEX contracts 1 and 2 at month end; positive = backwardation." F1, F2 = `eia[m][1]`, `eia[m][2]` at t.
3. E13 seasonal adjustment (SPEC_Carry s3, X1; gm/CHANGES.md "X1 outcome": the gate opened for `cm_natgas` and
   `cm_gasoline` only): "that market's carry in both versions becomes carry minus the mean, over all earlier
   same-calendar month-ends (at least five; no signal before), of (carry minus its trailing 12-month mean, the 12
   month-ends up to and including that month-end)." Applied to those two markets only; the other two energy markets
   and the currencies are unadjusted.
4. Value measure, equities (SPEC_Value s3 item 1): "trailing 12-month dividend yield. Seven countries: Ken French
   country market return with minus without dividends, summed over 12 months ... US: SPY total return minus S&P 500
   price return, summed over 12 months, clipped to [0, 0.10] (from 1993)." With E4 for the seven non-US markets
   (TESTING_PROTOCOL 7.4 E4): "the trailing 12-month dividend yield used at month t is the one ending at t-12 (design
   and live alike); US (SPY) unchanged", and gm/CHANGES.md gm-1.2.3 closed item 3: "the lag-12 value at t is exactly
   the 12-month sum ending at t-12, with no carry-forward ... so a file that does not reach t-12 gives no value". The
   12-month sums need all 12 months (US too). Higher = cheaper.
5. Volatility (SPEC_Trend s3 step 4, the "hybrid" model the A2-final book uses for every pod and for the per-market
   cap): "max(0.7 x fast + 0.3 x slow, 0.75 x slow), fast = EWMA of daily squared log returns, half-life 35 days, at
   least 40 days, where free daily data exist (daily.py), else EWMA of monthly squared returns, half-life 6 months, at
   least 12; slow = 120-month standard deviation, at least 36; fast alone until slow exists, m36 where neither exists",
   m36 = "36-month standard deviation of monthly R, at least 12 months, x sqrt(12)". Daily input = `D` (section 2: for
   bonds and notes D holds price returns; the model uses D's values as given), monthly input = `R`; annualised.
6. Class blocks (gm/CHANGES.md "gm-2.2.1 fix", item 2): "cm_aqr_ew is in a class block only when the class is CM and the
   family is Trend"; every other market sits in the class of its prefix (`classes`); `sp_*` columns are in no class.
7. Trend level at interior gap months (gm/CHANGES.md "Core book v1", dated clarification N2; SPEC_Trend s3 amendment of
   2026-11-27): "the level lvl of a market exists at every month-end from its first month with a monthly excess return
   onward, including later months without a return (interior gaps); a gap month adds a return of 0, so lvl(t) =
   lvl(t-1) there, and the score at and after a gap month is computed from that level like any other month; lvl is
   missing only before the market's first return." (Written with sight of the engine, so S4 does not test this point.)
8. Bloomberg switches (TESTING_PROTOCOL 7.4 E1) are off: no Bloomberg composite, curve carry or alternative commodity
   appears in the inputs; nothing to apply.
Timing (7.3 items 1-2, 5), sizing (7.7 "Held size", specs s5) and costs (specs s9) are as before: the specs and the
registered texts, unchanged by version 2.

## 3. Rules the job enforces before using the output

0. (v2) Before the rebuild runs, the job checks that the raw inputs reproduce the engine's own measures exactly: the
   currency and energy carry of SPEC_Carry s3 steps 2-3 (before E13) and the equity dividend yields of SPEC_Value s3
   item 1 with E4 (max abs difference and missing pattern; nothing else printed); a difference STOPs the job. This
   checks the packaging of the inputs, not the rebuild.

1. `rebuild_s4.py` imports nothing from the engine or the job's libraries: the job scans the module's source and STOPS
   if it imports `gm`, `gm_engine`, `a1_panel`, `a2_batch`, `diag_a2`, `core_v1`, `bbgdata` or `bbg_panel`. Allowed:
   the Python standard library, numpy, pandas.
2. No file, network or environment access; no randomness; no printing needed (stdout is captured and discarded).
3. Every series: PeriodIndex "M", float, no value after the cut month, at least 120 non-missing months in
   1975-01..2010-12 (7.7 window minimum), no infinite value.
4. The module's sha256 is registered in the job (REBUILD_SHA) before the job is queued; a different file STOPs the job.

## 4. What the job compares (decisive for `trend`, `carry`, `value_eq`)

Over 1975-01..2010-12, each series over its own months with a net return (the A2 convention): annualised net Sharpe
(mean / standard deviation x sqrt(12), ddof 1) and annualised mean (12 x monthly mean). Engine figure = the same part
alone from the engine (a one-part equal-risk book of E9 with that part's mask, gm.execution.run_k1, A2-final config,
A1 panel). Pass = |rebuild - engine| / |engine| <= 0.15 for BOTH the Sharpe and the mean. Reported beside: months of
each series, common months and the correlation of the two series on them; the same lines for the two Carry legs
(not decisive).
