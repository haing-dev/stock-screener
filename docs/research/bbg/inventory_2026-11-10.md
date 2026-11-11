# Bloomberg pull: inventory (2026-11-10, job bbg_inventory_v2)

Metadata only (names, counts, date ranges). Monthly sheets run 1969-12 to 2026-10-30, daily sheets 1990-01 to 2026-11-04.
Cells hold values, not formulas, except the tickers saved while still loading.

| File | Sheet | Tickers | OK | Still loading when saved | Invalid ticker | No values | Median history of OK tickers |
|---|---|---|---|---|---|---|---|
| 1 | Economics | 35 | 35 | 0 | 0 | 0 | 52 years |
| 1 | RatesFutures | 75 | 73 | 0 | 0 | 2 | 18 years |
| 1 | SpotRates3m | 12 | 12 | 0 | 0 | 0 | 18 years |
| 1 | Curves | 140 | 140 | 0 | 0 | 0 | 18 years |
| 1 | Returns | 47 | 47 | 0 | 0 | 0 | 18 years |
| 1 | Yields | 43 | 43 | 0 | 0 | 0 | 18 years |
| 1 | EquityTR | 21 | 21 | 0 | 0 | 0 | 43 years |
| 1 | BondFutures | 32 | 32 | 0 | 0 | 0 | 18 years |
| 1 | EquityValuation | 23 | 23 | 0 | 0 | 0 | 32 years |
| 1 | Breakevens | 9 | 9 | 0 | 0 | 0 | 18 years |
| 1 | Benchmarks | 6 | 6 | 0 | 0 | 0 | 18 years |
| 1 | Surprise | 9 | 9 | 0 | 0 | 0 | 18 years |
| 1 | Volatility | 14 | 14 | 0 | 0 | 0 | 28 years |
| 1 | FXBasis | 3 | 2 | 0 | 1 | 0 | 23 years |
| 1 | DailyCommodities | 25 | 24 | 0 | 1 | 0 | 53 years |
| 2 | EconUS | 51 | 47 | 0 | 4 | 0 | 57 years |
| 2 | EconIntl | 70 | 63 | 0 | 7 | 0 | 33 years |
| 2 | PolicyMoney | 41 | 34 | 0 | 7 | 0 | 32 years |
| 2 | Conditions | 23 | 14 | 0 | 9 | 0 | 30 years |
| 3 | YieldsExtra | 71 | 71 | 0 | 0 | 0 | 23 years |
| 3 | Swaps | 72 | 72 | 0 | 0 | 0 | 23 years |
| 3 | Credit | 47 | 47 | 0 | 0 | 0 | 23 years |
| 3 | FXSpot | 56 | 56 | 0 | 0 | 0 | 23 years |
| 3 | FXForwards | 93 | 93 | 0 | 0 | 0 | 23 years |
| 3 | FXVol | 130 | 130 | 0 | 0 | 0 | 23 years |
| 3 | FXBasis | 18 | 16 | 0 | 1 | 1 | 23 years |
| 3 | RatesFutExtra | 47 | 47 | 0 | 0 | 0 | 23 years |
| 4 | EquityIndexes | 81 | 73 | 8 | 0 | 0 | 39 years |
| 4 | SectorsStyles | 52 | 51 | 0 | 1 | 0 | 37 years |
| 4 | VolComplex | 39 | 33 | 0 | 3 | 3 | 23 years |
| 4 | Benchmarks2 | 20 | 5 | 0 | 14 | 1 | 33 years |
| 4 | ETFs | 69 | 69 | 0 | 0 | 0 | 20 years |
| 5 | ComFront | 48 | 8 | 40 | 0 | 0 | 38 years |
| 5 | ComCurve | 528 | 219 | 295 | 4 | 10 | 36 years |
| 5 | ComIndexes | 23 | 9 | 12 | 2 | 0 | 50 years |
| 5 | ComFundamentals | 32 | 10 | 20 | 1 | 1 | 40 years |
| 6 | DailyFutures | 188 | 186 | 0 | 0 | 2 | 34 years |
| 6 | DailyFX | 50 | 50 | 0 | 0 | 0 | 37 years |
| 7 | DailyRates | 49 | 49 | 0 | 0 | 0 | 34 years |
| 7 | DailyEquity | 31 | 31 | 0 | 0 | 0 | 37 years |
| 7 | DailyVol | 36 | 36 | 0 | 0 | 0 | 25 years |
| 7 | DailyIndexes | 11 | 8 | 0 | 3 | 0 | 37 years |

| File | Tickers | OK | Still loading | Invalid | No values |
|---|---|---|---|---|---|
| 1 | 494 | 490 | 0 | 2 | 2 |
| 2 | 185 | 158 | 0 | 27 | 0 |
| 3 | 534 | 532 | 0 | 1 | 1 |
| 4 | 261 | 231 | 8 | 18 | 4 |
| 5 | 631 | 246 | 367 | 7 | 11 |
| 6 | 238 | 236 | 0 | 0 | 2 |
| 7 | 127 | 124 | 0 | 3 | 0 |
| all | 2470 | 2017 | 375 | 58 | 20 |

## Tickers that did not load

Still loading when the file was saved (re-pull): file 5 (ComFront, ComCurve, ComIndexes, ComFundamentals) and 8 in file 4 EquityIndexes.

Invalid ticker or no values, by sheet:
- 1 RatesFutures (2): L 6 Comdty, YE7 Comdty
- 1 FXBasis (1): JYBSV1 Curncy
- 1 DailyCommodities (1): SPGSRBP Index
- 2 EconUS (4): JLTOTOTL Index, PITLSAVE Index, PRODNFR Index, COSTNFR Index
- 2 EconIntl (7): RSSAEMUY Index, EUITEMUY Index, ECMSLNFY Index, GRIORTYA Index, JNMOCHNY Index, CGE9MOM Index, CNLNTSF Index
- 2 PolicyMoney (7): CHRR7D Index, TUBR1W Index, FARBRSBL Index, RRPONTSYD Index, UKBSTOTA Index, SZNBSIGH Index, THREEFYTP10 Index
- 2 Conditions (9): GSUSFCI Index, STLFSI4 Index, OFRFSI Index, CESIUSDI Index, CESIEURI Index, CESIEEMA Index, BBGUSSUR Index, PCUSTOTR Index, BULLISH Index
- 3 FXBasis (2): BPBSV1 Curncy, ADBSV5 Curncy
- 4 SectorsStyles (1): SPXT10UP Index
- 4 VolComplex (6): V2X Index, VNKY Index, SPXRV30 Index, MOVE Index, SMOVE1M Index, SKEW25D Index
- 4 Benchmarks2 (15): NEIXSTTI Index, NEIXTI Index, NEIXMTI Index, NEIXMULT Index, HEDGMF Index, HFRXGL Index, HFRXM Index, HFRXEH Index, HFRXRVA Index, HFRIFWI Index, HFRIEHI Index, HFRIRVA Index, SPRPAU10 Index, NEIXMFI Index, BARCCTA Index
- 5 ComCurve (14): KC8 Comdty, KC9 Comdty, KC10 Comdty, KC12 Comdty, CC11 Comdty, FC11 Comdty, FC12 Comdty, LH12 Comdty, RR8 Comdty, RR10 Comdty, RR11 Comdty, QC12 Comdty, RS11 Comdty, RS12 Comdty
- 5 ComIndexes (2): GSCBCAR Index, BCOMCRV Index
- 5 ComFundamentals (2): DOESCUSH Index, GOLDLNPM Index
- 6 DailyFutures (2): L 8 Comdty, YE8 Comdty
- 7 DailyIndexes (3): NEIXCTA Index, NEIXCTAT Index, NEIXSTTI Index
