# Cross-check: transcript gap review vs the current book (gm-1.2.0), 2026-10-31

Input: `claude/transcript_gap_review_2026-10-31.md` (166 new transcripts; Harding/Winton and Judes read in full).
Each point is sorted into: **Already in the book**, **Do now with free data**, **Needs Bloomberg** (added to workbook
v3), or **Decision for you**.

**Holdout caution.** Winton's speed and crowding evidence, and the alternative-markets evidence, are mostly from
2011-2026, which is our holdout. They may be used only as outside priors for pre-registered variants, each tested on
1990-2010 and counted as a trial.

---

## 1. Harding / Winton, point by point
| # | Point | Our system today | Verdict |
|---|---|---|---|
| H1 | Trend Sharpe about 0.5 long-run, falling since the 1970s | Trend family 1.08 (1975-89) and 1.30 (1990-2010). No decay is visible inside the design period, so the decay sits in the holdout. Live target 0.4-0.8 | Do now: a decade table (1975-84, 85-94, 95-04, 05-10) as a report, not a rule |
| H2 | Crowding pushed Winton slower; fast trend decayed most | Trial 9: 1/3/12 is best in design, but with a 1-month delay every speed gives about 1.1. The fast leg's extra is execution-dependent | **Decision**: switch to slower trend (6/12) on Winton's prior, accepting a lower design Sharpe, or keep 1/3/12 and run the T+k diagnostic first (recommended) |
| H3 | Never switch speed by regime | Fixed design; risk scalers rejected | Already in the book |
| H4 | Risk is not volatility; binding scenario tests (worst day/week, 1990 oil, 2013 taper, Feb 2007, Feb 2018) | Stress P&L is diagnostic only (2008/2020/2022/1994) | Do now: add the windows; test a binding limit (book scaled so each scenario loses at most about 2-3%) as a variant |
| H5 | Trend is not a reliable equity hedge after a steady rally | 1987 = -19% in our book | Do now: split crisis results by whether trend was short before the fall; build the equity-beta cap (planned) as a variant |
| H6 | Use high-frequency data for vol and correlation even when trading slowly | 36-month monthly vol | Do now: EWMA on monthly data plus daily where free (FRED yields 1962+, H.10 FX 1971+, Yahoo indexes, EIA energy). Commodities need Bloomberg daily |
| H7 | Effective number of markets; alternative markets | Equal weight inside a class; no alternative markets | Do now: cluster weights. Needs Bloomberg: alternative commodities (added) |
| H8 | Government macro data unreliable; PMI £2m "inconclusive" | Econ trend 30%, on CPI (little revised) + market themes; growth OFF; ablation: book without econ 1.57 vs 1.47 with | **Decision**: cut econ to 15-20% before the holdout (supported by our own ablation and Harding), or keep 30% (AQR uses 50%). Needs Bloomberg: first-release CPI with release dates (already in the Economics sheet) |
| H9 | Very long ag history, weather | Grains from 2000, front-month | Needs Bloomberg: GSCI ag ER indexes (1970s+, in Returns). Weather: out of scope |
| H10 | Fixed 75/25 trend/other; carry in FX, commodities and bonds, not equities | Fixed shares; equity carry rejected | Already in the book. Note: our trend share is 30%, so crisis behaviour leans on the other families |
| H11 | Data cleaning is the core | Non-energy commodities use unadjusted Yahoo front-month (fake roll jumps) | Needs Bloomberg: GSCI/BCOM excess-return indexes replace them (Returns sheet). **Top priority** |
| H12 | Trend on single stocks doesn't work | n/a | No action |

---

## 2. Trend design gaps (§2 of the review)
| Item | Verdict |
|---|---|
| 1 Continuous capped signal instead of the average of signs | Do now (one trial). Fixes a breach of our own "continuous scores" rule |
| 2 Second estimator (EMA crossover, breakout); report Sharpe spread across the grid | Do now |
| 3 Volatility: EWMA blend plus long-run floor; size-at-entry variant | Do now (monthly EWMA); daily needs free data plus Bloomberg daily for commodities (optional sheet) |
| 4 T+1/3/5/10 delay grid, multi-day execution, no-trade buffer, tick-size split | Do now with free daily data (2000+ fully; 1990s partly). A diagnostic first, then a buffer variant |
| 5 Trend/carry double count: spot-only trend | Do now (spot FX and yields are in the panel) |
| 6 Cluster weights; equal risk across classes contested | Do now: cluster weights as a variant. Class weights stay equal (pre-registered) |
| 7 Asymmetric equity speeds, acceleration, asset-class trend, long-horizon reversal | Do now: acceleration and asset-class trend only (2 trials). The rest is lower value |
| 8 Skew premium; COT hedger premium; betting against beta | Do now: skew (free). COT: CFTC free (extend the download beyond the current selected markets) |
| 9 Universe: alternative commodities, credit, synthetic markets, deferred energy | Needs Bloomberg: alternative commodities. Do now (free): credit from FRED ICE BofA total-return indexes (IG 1973+, HY 1986+, minus Treasuries); EIA contracts 3-4 (already downloaded); trading the 3 built spreads |
| 10 Binding scenario limits; broader beta cap (USD, duration, commodities) | Do now as variants. Add windows Aug 2024, Apr 2025, Feb 2007, Feb 2018, 1990 oil, 2013 taper |
| 11 Crowding gauge covering the design period | Needs Bloomberg: SG CTA/Trend, HFRI, Barclay CTA/BTOP50 (Benchmarks sheet). Do now: synthetic CTA, PC1 share |
| 12 Regime-reporting definitions | Do now (report only) |
| 13 Margin rule; stress-scaled costs | Do now: margin <= 30% rule; costs x 3 in stress months as a sensitivity |

---

## 3. New macro mechanisms (§3 of the review)
| Mechanism | Data | Verdict |
|---|---|---|
| Intermediary capital ratio (He-Kelly-Manela) | Free (Manela website, 1970+) | Do now: candidate risk-appetite input (same-sign test) |
| BIS credit-to-GDP gap, cross-country | Free (BIS) | Do now: cross-sectional equity/bond/FX candidate |
| Treasury market noise (Hu-Pan-Wang) | Free (1987+) | Do now: risk-scaler candidate (scalers have failed so far, so low prior) |
| Convenience yield (Aaa - 10y) | Already downloaded (AAA10YM) | Do now |
| Lagged monetary transmission (effective vs market rate) | US Z.1 only | Later (US only) |
| Oil burden / GDP | Free | Do now: commodity/bond candidate |
| Fed model, E/P - 10y, per country | Needs Bloomberg: EquityValuation sheet (trailing and forward P/E) | Bloomberg |
| Policy-rate dispersion | Free (rates in the panel) | Do now: report / tilt variant |
| Central-bank gold buying | IMF IFS / WGC | Later |
| Oil/gas energy-content relative value | Free (EIA, in hand) | Do now |
| Market-implied policy path (gap #4) | Needs Bloomberg: RatesFutures sheet (Eurodollar/SOFR, fed funds, Euribor, short sterling/SONIA, BAX, Aussie bills) | Bloomberg. Also gives a real front-end market instead of 2y notes |
| Real-rate differentials for FX and gold (gap #5) | Needs Bloomberg: Breakevens sheet | Bloomberg |
| Dollar funding stress (gap #2) | Needs Bloomberg: FXBasis sheet (optional) | Bloomberg |
| GPR -> inflation theme; container volumes; SPF 10y; WASDE / EIA storage | Free | Later, lower priority |

---

## 4. Decisions for you (before the holdout runs)
1. **Holdout pass criteria.** The review is right that "2020 and 2022 not negative" plus a worst fall above -20% can
   fail a sound book: a normal bad year is -10% to -13% at 10% vol, and live drawdowns are 2-4x backtests.
   Proposed criteria:
   - net Sharpe at least 0.3;
   - worst fall above -25%;
   - correlation with the S&P 500 at most 0.3;
   - 2022 positive (trend's signature year);
   - drop the 2020 test.

   This must be set now and logged, never after seeing the result.
2. **Economic trend share:** keep 30%, or cut to 15-20% (Harding H8 + our ablation)?
3. **Trend speed:** keep 1/3/12 pending the T+k diagnostic (recommended), or go slower now on Winton's prior?

---

## 5. Bloomberg workbook v3 (what changed for the trip)
`Bloomberg_macro_UBC.xlsx`, 285 tickers, sheets in priority order:

| # | Sheet | Tickers | What it is |
|---|---|---|---|
| 1 | Economics | 35 | Unchanged: first release, consensus, release date |
| 2 | Returns | 47 | 16 original + 19 alternative commodities: cocoa, OJ, hogs, feeder cattle, KC wheat, oats, rice, soymeal, soyoil, lumber, palladium, LME aluminium/zinc/nickel/lead/tin, gasoil, EU carbon, TTF gas |
| 3 | Curves | 105 | Same commodity set |
| 4 | RatesFutures | 23 | New |
| 5 | EquityValuation | 23 | New. MSCI country P/E, forward P/E, P/B, dividend yield, forward EPS. Fills EM equity value; a possible live substitute for the WRDS revisions signal; Fed model |
| 6 | Breakevens | 9 | New |
| 7 | Benchmarks | 6 | New |
| 8 | Surprise | 9 | Unchanged |
| 9 | FXBasis | 3 | Optional |
| 10 | DailyCommodities | 25 | Optional: daily excess-return indexes from 1990, for H6 and the execution test |

---

## 6. Suggested order of work (all design period, all counted)
1. Free now:
   - continuous trend signal;
   - EWMA vol with a floor;
   - T+k delay grid;
   - cluster weights;
   - spot-only trend;
   - scenario windows and limit;
   - decade table;
   - credit markets from FRED;
   - intermediary capital ratio and credit gap as candidates.
2. After Bloomberg:
   - replace non-energy commodities with excess-return indexes, add alternative commodities (capped at about 30% of
     commodity risk), commodity carry;
   - short-rate futures market and implied-path theme;
   - EM equity value and forward-EPS revisions;
   - first-release CPI;
   - crowding gauge.
3. Freeze gm-2.0 with the decisions above, then run the holdout once.
