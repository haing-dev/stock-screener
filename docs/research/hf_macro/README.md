# Macro Compass: hedge-fund-style research (2026-10-29, research only, live rule unchanged)

## What was done
1. All 61 files in `Processed Transcripts/Macro Transcripts` read in full by 7 readers -> 1,062 rules
   (`transcript_rules/batch1-7.md`). Galt: only the rules in macro/registry.py (raw X posts not available).
2. Four coders turned every rule the data allowed into a coded hypothesis: 731 hypotheses (`hyp_b12/b34/b56/b7.py`,
   notes with skipped rules and data gaps in `hyp_b*_notes.md`). Kinds: cut, gate, block (re-entry), defensive asset,
   sleeve, location (countries/regions/sectors), overlay (long/short pairs).
3. Data: 452 free series (Yahoo ETFs/indexes/futures incl. Korea, Brazil, EM, commodities, bonds, FX, volatility; FRED;
   AQR long-history sets; Shiller; World Bank pink sheet; CBOE; CFTC; AAII; NY Fed; Fed EBP; Ken French).
   Snapshot: branch `macro-research-data`. Fetch: `python -m macro.run research_fetch` (macro/fetch_research.py).
4. Independent audit (`AUDIT.md`) of the test code. Fixed: Yahoo non-US monthly bars dated one month early; synthetic
   Treasuries now priced exactly from month-end yields (corr 0.99 with TLT/IEF/SHY, was 0.72); gold signal uses prices
   known at t; no gold before 1975 (US ownership illegal); costs 0.2%; a cost-parameter bug.
5. Every hypothesis evaluated vs the live 4.1 book (`run_all.py`, `analyze_all.py`): screen (Sharpe gain > 0.02 in both
   halves, no CAGR loss, worst fall not > 2 pts deeper), shuffled-timing placebo (200 draws), Benjamini-Hochberg FDR 10%.

## Results
- 690 usable hypotheses; 7 pass the screen; 5 placebo p < 0.05; 1 passes FDR: B004 (Gromen) 10% commodities while the
  commodity index is up over 12 months and above its 10-month average (+0.03 Sharpe, ~0 CAGR).
- Earlier "candidate 5.0" (16.2%/yr) was overstated: after fixes 15.1%; its squeeze cut is fragile (threshold 70 -> worse
  than live; out-of-sample 1982-96 +0.1%/yr); the melt-up cut rests on 2 episodes (1980-81, 1987).

| corrected, 0.2% costs (CAGR / worst / Sharpe) | 1966-74 | 1975-2000 | 2001-2026 | 1975-2026 |
|---|---|---|---|---|
| S&P 500 | -0.8 / -47 | 15.9 / -30 / 0.62 | 9.0 / -51 / 0.53 | 12.4 / -51 / 0.58 |
| Live 4.1 | 7.4 / -15 | 16.3 / -15 / 0.72 | 11.3 / -20 / 0.80 | 13.8 / -20 / 0.76 |
| P1 live + sector tilt + commodity-trend sleeve | 9.2 / -14 | 16.7 / -15 / 0.76 | 11.7 / -18 / 0.84 | 14.2 / -18 / 0.80 |
| P2 P1 + melt-up cut | 9.2 / -14 | 18.4 / -15 / 0.91 | 11.7 / -18 / 0.84 | 15.0 / -18 / 0.88 |
| P3 P2 + presidential cycle (Hirsch) | 10.9 / -9 | 19.2 / -11 / 1.02 | 12.9 / -18 / 0.94 | 16.0 / -18 / 0.98 |

Presidential cycle = stocks at most 50% Apr-Sep of a midterm year; no cuts from Q4 of the midterm year to Q2 of the
pre-election year (A033/A032, placebo p 0.045/0.055; published 1967, so most of the sample is after publication).
- Multi-asset books: four-quadrant growth/inflation book 7.0%/yr (fails); walk-forward quadrant 10.5%; trend-filtered
  risk parity 8.8%, worst -9%; 70% P/C5 + 30% risk parity ~14%, worst -13% (a lower-risk option).
- Rejected (examples): country momentum (1997-2011 only), US vs ex-US, dollar-trend EM, EM rebound, oil importers,
  gold/2y/trend/commodities instead of T-bills, trend sleeve (own build), puts (-3%/yr), daily crash cap, AAII
  sentiment, credit/EPU/valuation/narrow-leadership/curve/oil-shock cuts, dollar/yen/franc holdings.

## Data still wanted (cannot be fetched automatically)
MSCI country/region gross USD monthly from inception (Korea, Brazil, China, India, Taiwan, Mexico, Japan, EM, EAFE);
ICE BofA HY OAS full history (1996+); S&P forward EPS / revisions; ISM PMI and new orders; country CAPE (Research
Affiliates / StarCapital); EMBI spreads; Galt's raw X posts; event dates (tariffs, export controls, IEA releases).
Round-3 free series (yields 1/5/7/20y, regional Fed surveys, EBP, TED, China PPI/imports, uranium, EU gas, Ken French 49
industries/beta portfolios) are downloaded but the rules that waited on them are not yet coded.
