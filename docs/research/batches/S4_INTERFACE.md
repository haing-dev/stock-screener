# S4 interface: the independent rebuild of the Core parts (TESTING_PROTOCOL 7.6 step 6 S4)

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

## 2. `inputs` (exactly what the job passes; deep copies, so mutation is harmless but should not be relied on)

Every frame holds design months only: nothing dated after 2010-12-31. Market ids are the engine's strings
(`eq_us_spx`, `bd_us_10y`, `st_de_2y`, `fx_jpy`, `cm_wti`, `sp_us_2s10s`, ...).

| Key | Type and shape | Content |
|---|---|---|
| `"R"` | DataFrame, PeriodIndex "M" 1960-01..2010-12 (612 rows), 65 columns | monthly EXCESS return of each market in month t (futures-style: equities over the local 3-month rate, bonds over the 3-month rate, currencies incl. the rate gap, commodities excess return), the A1 panel (free data, Bloomberg-extended backwards where A1 admitted a series). NaN = no return. Includes `cm_aqr_ew` (Trend, CM block only, to 2000-12) and three spread columns `sp_*` that no pod trades |
| `"D"` | DataFrame, DatetimeIndex (daily, about 12,700 rows to 2010-12-31), 61 columns | daily return of each market with free daily data: for `bd_*` and `st_*` the PRICE return (minus duration x yield change); for every other market the LOG return. NaN = no value that day |
| `"days"` | DatetimeIndex | NYSE open days = dates of the daily ^GSPC closes, to 2010-12-31 (gm/CHANGES.md gm-2.1.0 closed item 1). "Month-end" = a month's last NYSE day, "first trading day" = its first |
| `"C"` | DataFrame, PeriodIndex "M", columns = the non-equity markets with a carry value (bonds, notes, currencies, the 4 energy markets) | Carry's measure at month-end t, annualised decimal, as the A2-final book reads it: bonds/notes yield minus 3-month rate; currencies the rate gap to the dollar; energy 12 x (F1 / F2 - 1) from EIA contracts 1-2, with the E13 seasonal adjustment already applied to `cm_natgas` and `cm_gasoline` (gm/CHANGES.md "X1 outcome"). Known at month-end t |
| `"V"` | DataFrame, PeriodIndex "M", columns = `fx_*`, `bd_*`, `eq_*` with a value | Value version 1's measure at month-end t (higher = cheaper; Value is long the high end of the in-class rank). Equities: trailing 12-month dividend yield, for the 7 non-US markets the one ending at t - 12 (E4), US at t. Known at month-end t |
| `"vol"` | DataFrame, PeriodIndex "M", same 65 columns as `R` | the engine's annualised volatility estimate of each market at month-end t (the A2-final config's hybrid model: daily EWMA where daily data exist, else monthly EWMA, blended with a 10-year estimate, with a floor; SPEC_Trend s5). USE IT AS GIVEN for every w x 0.40 / vol sizing and for the per-market cap: the volatility model is a shared input here, not part of what S4 re-derives |
| `"cost"` | dict market -> (one_way_bp, rolls_per_year) | the engine's cost table for every `R` column (bp of notional per unit traded; futures rolls a year, each roll charged as a round trip of the held position) |
| `"em_borrow"` | tuple of market ids | emerging equity markets whose SHORT positions pay 1% a year borrow |
| `"classes"` | dict class -> tuple of id prefixes | `{"EQ": ("eq_",), "FI": ("bd_", "st_"), "FX": ("fx_",), "CM": ("cm_",)}` |
| `"meta"` | dict | informational only: config name and hash of the A2-final book (gm-2.0.4-candidate-x1, 77374d7bef), A1 panel id, engine version |

Not in `inputs` (the rebuild derives them from the specs): trend scores, ranks, signs, class division, the 0.40 risk
unit, block / part / book scalers, the 10% target, caps, the k = 1 return form, cost timing, the holding cut.

## 3. Rules the job enforces before using the output

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
