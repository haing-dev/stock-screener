# Bloomberg data lock v1 and data check (block 2, 2026-11-11)

Metadata only. Reports: `tools/bbgq/results/bbg_build_v1.txt`, `bbg_check_v1.txt`. Hashes: `LOCK_v1.json`.
Code: `tools/bbgq/lib/bbgdata.py` (bbgdata-1.0.0), jobs `bbg_build_v1.py`, `bbg_check_v1.py`. Ran on the PC in 49 s + 2 s.

## What is locked
- Lock id `f5a4fb7cd3776b2a3bee4158e13cdb218fe99615b996d4886e65973477dc072a` (sha256 over the 7 workbook hashes, the two config lists, the 4 table hashes and the catalog).
- Design tables (what research may see): monthly 493 month-ends x 3,056 series (1969-12 to 2010-12), daily 5,480 days x 415 series (1990 to 2010-12-31).
- Sealed tables (2011 onward): monthly 191 rows, daily 4,134 rows. The reader refuses them (no key exists yet); every attempt is logged on the PC.
- Held-back markets: 45 markets, 269 tickers, 285 series (11 alternative commodities, 15 emerging-market currencies, 19 emerging-market bond yields), invisible to the reader by default.
- As-of access: every getter returns only what was knowable on the asked date (fixed delay per sheet; actual release date for 556 economic series).
- Live-source tags (sheet-level defaults): Bloomberg only 2,457 series, free daily 425, official release 589.

## Status: PROVISIONAL. Two of the seven files came back with cut-off history
The workbooks ask for monthly history from 31 Dec 1969 (`build_bloomberg.py`, `build_bloomberg_v5.py`), but:
- **File 1**: RatesFutures, SpotRates3m, Curves, Returns, Yields, BondFutures, Breakevens, Benchmarks, Surprise start on **2009-06-30** (19 design months). Economics, EquityTR, EquityValuation, Volatility and DailyCommodities are complete.
- **File 3**: all eight sheets (YieldsExtra, Swaps, Credit, FXSpot, FXForwards, FXVol, FXBasis, RatesFutExtra) start on **2004-04-30** (81 design months).
- **File 5**: 527 of 823 fields still "Requesting Data" when saved (ComFront 200, ComCurve 295, ComIndexes 12, ComFundamentals 20).
- **File 4**: EquityIndexes 64 fields (8 tickers) still "Requesting Data".
Two independent readers agree (block 1 inventory: fill 31% and 40%), and the same contract has full history in another file
(CL2: file 1 from 2009-06, file 5 from the 1980s). Cause is on the pull side and not known.

Effect on the must-have list (260 groups: 160 usable, 100 not): not usable = all 16 commodity excess-return indexes (monthly),
30 of 48 commodity curve points, all 7 short-rate futures groups, 4 of 6 spot 3m rates, 10 of 12 non-US 2y/10y yields, all 9 bond
futures, 3 breakevens, 6 of 9 surprise indexes, 3 first-release items, 2 forward EPS, 10 of 11 held-back commodity indexes.
Usable = equity total return 18/18, valuation P/E, P/B, D/P 48/48, forward EPS 14/16, first-release economics 54/57.

**Needed before Batch A1 (data swap) and Batch B:** re-pull files 1, 3 and 5 and the 8 EquityIndexes tickers of file 4 with full
history, then re-run `bbg_build` -> lock v2 (v1 stays on record). Block 3 (engine on the PC, reproduce the book on free data) and
everything on daily data do not depend on the re-pull.

## History by sheet (design period, up to 2010)
*Long history = read ok with at least 120 design months (monthly) or 1,250 design days (daily).

| File | Sheet | Fields | Read ok | Long history* | Most common first date (count) |
|---|---|---|---|---|---|
| 1 | Economics | 140 | 136 | 91 | 1996-12-31 (18) |
| 1 | RatesFutures | 75 | 70 | 1 | 2009-06-30 (69) |
| 1 | SpotRates3m | 12 | 12 | 1 | 2009-06-30 (11) |
| 1 | Curves | 140 | 140 | 1 | 2009-06-30 (139) |
| 1 | Returns | 47 | 47 | 1 | 2009-06-30 (46) |
| 1 | Yields | 43 | 43 | 7 | 2009-06-30 (36) |
| 1 | EquityTR | 42 | 42 | 40 | 1969-12-31 (12) |
| 1 | BondFutures | 32 | 32 | 0 | 2009-06-30 (32) |
| 1 | EquityValuation | 115 | 115 | 87 | 1995-01-31 (24) |
| 1 | Breakevens | 9 | 9 | 0 | 2009-06-30 (9) |
| 1 | Benchmarks | 6 | 6 | 0 | 2009-06-30 (6) |
| 1 | Surprise | 9 | 9 | 0 | 2009-06-30 (6) |
| 1 | Volatility | 14 | 14 | 11 | 2003-10-31 (3) |
| 1 | FXBasis | 3 | 2 | 0 | 2003-07-31 (1) |
| 1 | DailyCommodities | 25 | 24 | 24 | 1990-01-01 (15) |
| 2 | EconUS | 204 | 158 | 102 | 1969-12-31 (29) |
| 2 | EconIntl | 280 | 196 | 91 | 2004-04-30 (11) |
| 2 | PolicyMoney | 41 | 32 | 30 | 1969-12-31 (5) |
| 2 | Conditions | 23 | 14 | 8 | 2003-01-31 (5) |
| 3 | YieldsExtra | 71 | 71 | 5 | 2004-04-30 (65) |
| 3 | Swaps | 72 | 72 | 2 | 2004-04-30 (67) |
| 3 | Credit | 47 | 47 | 0 | 2004-04-30 (46) |
| 3 | FXSpot | 56 | 56 | 6 | 2004-04-30 (50) |
| 3 | FXForwards | 93 | 93 | 5 | 2004-04-30 (88) |
| 3 | FXVol | 130 | 129 | 13 | 2004-04-30 (111) |
| 3 | FXBasis | 18 | 15 | 0 | 2004-04-30 (13) |
| 3 | RatesFutExtra | 47 | 45 | 3 | 2004-04-30 (41) |
| 4 | EquityIndexes | 648 | 560 | 252 | 2006-03-31 (32) |
| 4 | SectorsStyles | 208 | 180 | 126 | 1986-12-31 (26) |
| 4 | VolComplex | 39 | 30 | 6 | 2004-03-31 (4) |
| 4 | Benchmarks2 | 20 | 5 | 5 | 1999-11-30 (2) |
| 4 | ETFs | 276 | 172 | 55 | 1998-12-31 (24) |
| 5 | ComFront | 240 | 40 | 38 | 1995-01-31 (10) |
| 5 | ComCurve | 528 | 203 | 169 | 1969-12-31 (29) |
| 5 | ComIndexes | 23 | 9 | 9 | 1969-12-31 (3) |
| 5 | ComFundamentals | 32 | 9 | 8 | 1986-04-30 (2) |
| 6 | DailyFutures | 188 | 170 | 162 | 1990-01-02 (84) |
| 6 | DailyFX | 50 | 49 | 46 | 1990-01-01 (24) |
| 7 | DailyRates | 49 | 47 | 42 | 1990-01-02 (11) |
| 7 | DailyEquity | 62 | 62 | 62 | 1990-01-02 (24) |
| 7 | DailyVol | 36 | 33 | 30 | 2003-10-02 (10) |
| 7 | DailyIndexes | 11 | 8 | 8 | 1990-01-02 (7) |

## Data check flags (4,204 series)
clean 1,073; SHORT (under 120 months / 1,250 days) 1,659; REQ 591; STALE runs 306; JUMP 303; held back 282; no value before 2011 265;
INV 94; GAP 73; EMPTY 48; duplicates that disagree 30; release-date junk 17, late 5; non-positive price 1.
Release dates: 14,463 dated cells; 2,255 before the observation date; 558 more than 31 days before (ignored, fixed delay used); 57 more than 120 days after.
Not yet reviewed series by series: JUMP, STALE, GAP and DUPDIFF lists (done in block 3 for the markets the engine uses).
