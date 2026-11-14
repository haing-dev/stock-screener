---
tags: [fable, thesis]
code_commit: dd88b92
---
> Opus 5.5 high, against the verbatim quotes. See [[Thesis 1.3a - Rates and curve]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/dd88b9212f379079ef81ee41f61dab5479f367db/docs/research/fable/THESIS_1.3_rates_check.md).
# Independent check of thesis note 1.3a (rates and curve), 2026-11-14

Checker: Opus 5.5 (quant and risk officer), against the verbatim quotes in pack/QP06.json, [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]].json and [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]].json and the
other pack files. No code, no data, no backtests, nothing after 2010. Tools in opus_work/: lookup.py (claim id -> quote),
cited_ids.py (every id the note cites), quoted_strings.py (every phrase the note puts in quotation marks, against all quotes).

## 1. Verdict

**PASS WITH CORRECTIONS.**
- Numbers: 38 paper numbers checked: 36 in quote, 2 correct reader arithmetic, 0 contradicted, 0 claim ids not found, 0 without id; the 10 summary-only numbers are all tagged and none is built on. All 104 cited ids resolve; every quoted phrase is verbatim.
- Statements: 21 checked: 17 supported, 4 partly (row 2's cost wording, mechanism step 2, the artefact bullet on whole-curve trades, the rejection of whole-curve curvature), 0 not supported, 0 contradicted.
- Grades: 0 of 6 pod grades changed (Strip reversion stays weak, B2 behind stronger candidates). The rule family, R1 and the U01-T4 entry hold 7 hidden choices; C finds 4 quotes against Strip reversion that the note does not use.
- 20 required corrections (section 3); none reverses a conclusion. The largest: [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] models habitat bends as smooth and contract-level misfits as lasting, so the scale the pod trades is not established (mechanism step 2).

## 2. Tables and findings

### A. Numbers from the papers

| # | Number | Where in the note | Claim id | Verdict |
|---|---|---|---|---|
| 1 | 5.1 times the equity benchmark (2-B) | section 1 ("about five times"), row 1, section 6 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C18-3|QP06-C18-3]] | in quote ("about 5.1 times"); section 1 drops "up to" (C03-3: "by up to 5.1 times") and applies 2-B's figure to "local reversion" (correction 1) |
| 2 | 3.3 times (3-B, equity) | row 1 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C18-4|QP06-C18-4]] | in quote |
| 3 | 5.9 times (2-B, bonds) | row 1 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C19-1|QP06-C19-1]] | in quote |
| 4 | 3.8 times (3-B, bonds) | row 1 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C19-1|QP06-C19-1]] | in quote |
| 5 | t 9.1758 | row 1, 3.1, section 6 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C23-4|QP06-C23-4]] | in quote |
| 6 | t 4.9836 | row 1 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C23-4|QP06-C23-4]] | in quote |
| 7 | about 0.01% of value traded | row 2, 3.2, section 6 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C05-7|QP06-C05-7]] | in quote |
| 8 | half a basis point | row 2, 3.1 Fixed, R1 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C21-2|QP06-C21-2]] | in quote ("half basis point") |
| 9 | 5-year average | row 2 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C21-1|QP06-C21-1]] | in quote |
| 10 | January 1973 to December 2000 | section 1, row 1, section 6 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C17-3|QP06-C17-3]] | in quote |
| 11 | 28 years | row 2, 3.1 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C17-3|QP06-C17-3]] | reader arithmetic, correct |
| 12 | late 1980s | section 1, row 4 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C03-6|QP06-C03-6]] | in quote |
| 13 | by 1990 | row 4 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C25-5|QP06-C25-5]] | in quote |
| 14 | 0.814 | row 5, 3.1 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C24-3|QP06-C24-3]] | in quote |
| 15 | 0.763 | row 5 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C24-3|QP06-C24-3]] | in quote |
| 16 | 10-11 month spread, 10-11-23 curvature | 3.1, section 6 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C24-2|QP06-C24-2]] | in quote |
| 17 | 10 to 23 months | row 5, 3.1 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C24-5|QP06-C24-5]] | in quote |
| 18 | 9-10-11 | sections 6, 8 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C40-1|QP06-C40-1]] | in quote (figure title) |
| 19 | 6 strategies | 3.1, section 6 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C20-3|QP06-C20-3]] | in quote ("we tested 6 strategies") |
| 20 | 29 December 2000 | 3.1 rule 5 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C09-4|QP06-C09-4]] | in quote |
| 21 | 102 months | 3.1 Fixed | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C11-3|QP06-C11-3]] | in quote |
| 22 | 2003 | 3.1 rule 5 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C22-4|QP06-C22-4]] | in quote ("Foster and Stine (2003)") |
| 23 | one month apart, 1 to 60 months | 3.2 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C14-3|QP06-C14-3]] | in quote |
| 24 | 0.02 bp (5 days) | row 7 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-1|QP07-C18-1]] | in quote |
| 25 | 6.31 bp (250 days) | row 7 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-1|QP07-C18-1]] | in quote |
| 26 | 10/28/1991 | row 7, section 6 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-3|QP07-C17-3]] | in quote |
| 27 | 6 candidate models | row 7 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C14-4|QP07-C14-4]] | in quote |
| 28 | 1.19 bp | row 8 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-1|QP07-C19-1]] | in quote |
| 29 | 49.04 bp | row 8 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-1|QP07-C19-1]] | in quote |
| 30 | 1.16 bp | row 8 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-2|QP07-C19-2]] | in quote |
| 31 | 48.74 bp | row 8 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-2|QP07-C19-2]] | in quote |
| 32 | NW-stat 7.953 | row 8, section 9 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-5|QP07-C19-5]] | in quote |
| 33 | 0.03 and 0.30 bp | section 1, row 8, 3.2 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-1|QP07-C19-1]] minus C19-2 | reader arithmetic, correct (1.19-1.16; 49.04-48.74) |
| 34 | 6 state variables | 3.2 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C15-1|QP07-C15-1]] | in quote |
| 35 | 1/28/2008 | 3.1 rule 5, section 6 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C02-3|QP07-C02-3]] | in quote |
| 36 | January 2009 | 3.1 rule 5 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C09-7|QP07-C09-7]] | in quote |
| 37 | about 40 contracts | sections 6, 8 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C13-4|QP07-C13-4]] | in quote ("approximately 40 active contracts") |
| 38 | forecasts 1991-2008 | row 7 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-3|QP07-C17-3]], C02-3 | in quote (both dates) |

Tagged summary only and not built on, confirmed not in any quote: 2005, 2006 ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] coverage notes), 11.8, 0.001, 0.25-0.36,
1994-95 ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]), 1.919, 1.804 ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-5|QP07-C19-5]] summary), 7 Nov 2008, 15 days ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] claim text). Proposal numbers 0.37-0.70, 2%,
10%: correctly marked unverified and unused. Data-sheet numbers (strip starts, contract counts, SOFR/SONIA 2018): all agree
with pack/DATA_AVAILABILITY.md. Reader's settings (8 contracts, 60 months, 15 of 20 days, half of triple-months) are
labelled as such.

### B. Statements and labels

| Statement | Label in note | Verdict | Note |
|---|---|---|---|
| Row 1: 2-B and 3-B paid several times both benchmarks per unit of risk before costs; both add to a share holding | SHOWN | supported | multiples and t in quote (C18-3, C18-4, C19-1, C23-4); value-add is "even after accounting for transaction costs" (C23-3, not cited) |
| Row 2: after costs only 2-B stays ahead on every test; a tiny cost removes the profit | SHOWN (words; one number) | partly | C05-7: the cost "would have eliminated the excess returns", not the profit; 2-B survives 0.5 bp (C21-5) (correction 3) |
| Row 3: level and whole-curve slope do not beat bonds; whole-curve curvature not significant | SHOWN (words) | supported | C18-1, C18-2, C20-2 |
| Row 4: the edge faded | SHOWN (words) | supported | C03-6, C25-5; C25-4 (not cited) says both 2-B and 3-B "narrowed" |
| Row 5: profit grows with gap size; most profitable segments 10-23 months | SHOWN | supported | C24-3, C24-4, C24-5 in quote; the chart readings disagree (summary only, correction 20) |
| Row 6: maturity habitats offered after the results; futures named as stand-in | ASSERTED | supported | C25-1, C24-5, C22-2, [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-3|QP07-C08-3]] |
| Row 7: [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] forecasts beat no-change, not significantly | SHOWN | supported | C18-1, C18-2, C14-4, C17-3 |
| Row 8: model barely beats always-long; wins on days of disagreement | SHOWN; reason ASSERTED | supported | "no costs (C18-5)" is an inference from the profit definition, not in the quote (correction 4) |
| Row 9: contract-level ripples last | ASSERTED | supported | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C13-5|QP07-C13-5]], C17-2, [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C21-1|QP12-C21-1]] |
| Row 10: [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] split said to fit commodity curves; data noisy, stale, seasonal | ASSERTED | supported | conservative label: C35-1 reports a test outcome, which the note's own key would call SHOWN (words) |
| Chain (1): habitat participants deal at one maturity | ASSERTED | supported | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-3|QP07-C08-3]] says "primarily concerned with", softer than "must deal" |
| Chain (2): their demand bends the curve at neighbouring maturities only | ASSERTED | partly | C08-4 has "(and nearby maturities)", but [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-4|QP07-C10-4]] says habitat shifts reach a range of nearby maturities ("investors treat them as close substitutes") and treats the deviation "as a smooth curve", and [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] assigns contract-level misfits to persistent microstructure (C17-2) (correction 5) |
| Chain (3): the bend fades | ASSERTED | supported | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-5|QP07-C10-5]], C08-5 |
| Chain (4): paid as the bend fades, shown only on estimated Treasury yields | SHOWN only on yields | supported | |
| Other side: maturity-bound hedgers, named not shown; arbitrage erodes it | ASSERTED | supported | omits C25-2 (arbitrage trades cluster at the very segment), see C |
| Evidence bullet: whole-curve trades do not beat the benchmarks | reader | partly | 3-A's payoff is above both benchmarks (C18-1: "only strategies 2-B, 3-A and 3-B yield higher payoffs"), not significantly (C20-2) (correction 6) |
| 3.2 [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] as written: not buildable | - | supported | C14-3, C10-1, C05-7; data sheet has no monthly bill curve |
| 3.2 Whole-curve reversion: "The paper's own tests fail" | grade none / weak | partly | true for level and 2-A; 3-A is "marginally better" after costs (C21-6) and has "significant value-add even after accounting for transaction costs and the bonferonni correction" (C23-3) (correction 7) |
| 3.2 [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] model as a signal: weak | - | supported | |
| 3.2 Front-end carry: weak, SHOWN once | - | supported | |
| 3.2 [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] forecast pod: none | - | supported | |

### C. Evidence judgement

Grades against sample, out of sample, costs, risk, variants and caveats:
- Strip reversion, weak: consistent. In the quotes: one US sample 1973-2000 on estimated, twice-interpolated yields (C09-4b,
  C09-6, C10-2); decisions out of sample on an expanding normal (C10-6, C17-5) but risk matched ex post (C17-4); a cost
  floor from 2003 bond spreads applied to all years (C21-1, C21-2) with cost-free benchmarks (C21-4b, truncated); risk =
  standard deviation only (C05-2); the edge narrowed for both rules and 3-B fell below the benchmarks by 1990 (C25-4,
  C25-5); no test on traded prices. A grade above weak would need a test of the local rule on futures. I would not change it.
- Whole-curve reversion, none / weak: grade consistent; the stated reason understates 3-A (see B, correction 7).
- [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] model, weak: consistent (forecast gain not significant, C18-2; one AIC choice among 6, C14-4; no costs; overlapping
  windows, C18-3; the authors say richer forms may do better, C15-2).
- Front-end carry, weak: consistent (one sample 1991-2008, no costs, bp per trade, not risk-adjusted, C18-5, C19-2).
- [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]], none: consistent (every statistic summary only; "Many unresolved questions", C35-2).
- Curve carry: the note does not regrade it; no quote here bears on it beyond data handling.

Quotes that weaken or contradict a pod the note proposes and that the note does not use:
1. [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-4|QP07-C10-4]]: "Changes in demand or supply at a given maturity habitat can affect a range of surround- ing maturities —
   investors treat them as close substitutes — which allows us to treat the maturity-specific deviation as a smooth
   curve." (also C10-2b "investors treat them as close substitutes"). With C17-2 (misfits "can be expected to persist") and
   C14-1 ("we elected to incorporate these microstructure features into the forecast"), the only futures paper puts habitat
   effects in a smooth component and the contract-scale bends in a component it forecasts to persist. That is the scale
   Strip reversion bets will fade. The note cites C17-2 (row 9) but not C10-4, and its mechanism step 2 says "only".
2. [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C25-2|QP06-C25-2]]: "Arbitrage trades in the fixed income market are frequently constructed in the transition between the
   short- end and the long-end of the yield curves." The authors offer it as support for segmentation, but it also says
   arbitrage capital already concentrates on the pod's target segment; with C26-2 and C03-6 it weakens the answer to who keeps paying
   in 1990-2010, the pod's whole design sample.
3. [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|QP12-C31-1]]: "Differences in yields of adjacent contracts are non-stationary as time gap increases". The note uses it
   against the three built spreads and for Curve carry sizing, but not against its own normal: under the note's
   construction spread n is contract n against the average of contracts 1 to n-1 (its own algebra, section 7 item 3), up
   to 21 months apart, and the expanding-average normal presumes a stable level.
4. [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C26-1|QP12-C26-1]]: "Moving medians of length 3 cannot patch a period with a sustained anomaly" (C26-2b: "persists for about 3
   weeks"). Data errors can outlast R1's one-day persistence test, so R1 can pass on bad prints; the note's screen catches
   stale prices only ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C22-1|QP12-C22-1]]).
Lesser, not used by the note: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C16-1|QP06-C16-1]] ("the curvatures of the hypothetical bonds are zero. Hence, the trade does not work
with hypothetical bonds"): 3-B's evidence beyond 12 months comes from yearly-spaced triples, so the strip's quarterly
triples have no tested counterpart there. [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C13-1|QP06-C13-1]] and C14-3: 1-B and 2-B were each run in two versions, more variants
than the 6 the Bonferroni counted (C20-3). [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C29-1|QP12-C29-1]] and C30-1 (front contracts noisiest) are applied to Curve carry but
not to the strip's contract 1, which can be weeks from expiry at the end of the holding month. [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C22-3|QP06-C22-3]] (dealers "take a
cut" on derivative replication) bears on OTC routes, little on listed futures.
Quotes that favour pods or rejections and are not used: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C26-4|QP06-C26-4]] ("trading opportunities still exist in yield-spread
mean-reversion strategies") favours the spread version over curvature; [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C23-3|QP06-C23-3]] favours 3-A (correction 7); [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C20-2|QP07-C20-2]]
restates the [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] model's edge over buy-and-hold "especially over longer holding periods".

### D. Rule specification

1. Leg instruction ambiguous: "buy point n (buy its futures)" can be read as contract n alone. With the duration
   weighting (C14-2) the net position is long contract n against an equal-weight short of contracts 1 to n-1 at equal
   DV01 (checker's algebra, agrees with the note's section 7 item 3). Correction 8.
2. Units of the cost gate: the gap is in bp of a zero-point spread or curvature, the cost in bp of rate per contract; the
   conversion is not given, in the entry rule or in R1. Using the measure's weights w on the contract rates, the round trip
   of a position earning 1 per bp of the measure costs c x 2 x sum|w|: for spread n, w = 1/n on contract n and -1/(n(n-1))
   on each nearer contract, sum 2/n; for curvature at point n (equal steps), w = -1/(n+1), (n+2)/(n(n+1)) and
   -2/((n-1)n(n+1)) on each nearer contract, sum (2n+4)/(n(n+1)) (checker's algebra, sums verified to be level-neutral).
   Also "at least half a bp" leaves the gate's cost open. Corrections 9, 19.
3. Normal length: "from 60 months of history on" with expiry-month groups can mean 60 calendar months or 60 observations
   per group (20 years; the dollar normal would start about 2001). Only the first fits the note's 1990 design start.
   Correction 10.
4. Timing: "at the prior day's settlement prices" does not say when the trade is made. Correction 11.
5. Currency set: "per currency" is open, and the yen (6 contracts), sterling (1-5 on Bloomberg) and Canada do not have
   eight contracts in the data sheet. Corrections 12, 14.
6. Stale-price screen: needs daily prices; months before daily data (the normal from 1981) cannot be screened, and the note
   does not say whether the screen applies to the normal. Correction 13.
7. U01-T4 carry: "unchanged rules (carry = the roll down the strip ...)" is a new carry measure; the Carry pod defines carry
   only for bonds (yield minus 3-month rate), currencies and energy (charter digest), and ranks it within the
   fixed-income class, so its formula and scaling are a hidden choice. Correction 15.
Look-ahead: none found. The normal is an expanding mean of earlier month-ends ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C10-6|QP06-C10-6]], "till the preceding month"),
groups use the known expiry month, the screen uses trailing days, no normal crosses from Eurodollar to SOFR, and volatility
scaling follows the shop's standard estimator. R1: fixed gate (half of triple-months), no return read, logged as a trial;
its only hidden choice is the cost conversion (item 2). It cannot run until daily prices of dollar contracts 3, 5, 6, 7
are pulled, which the note states.

### E. Rules of the shop

- Versions averaged, not picked: yes (two measures, both run, averaged).
- No decision handed to the user: none found.
- One mechanism per pod: yes (pay for meeting maturity-bound demand). "most of the roll cancels between the two sides of a
  pair" is reader and not shown: with a concave average curve, near contracts roll down more than far ones, so a residual
  roll exposure correlated with the gap sign is possible (open point 2).
- Version dimension has a model-uncertainty reason: yes ("Which measures a habitat bend is unsettled"); the rest of the
  reason leans on evidence strength, which is acceptable as context.
- Data table against DATA_AVAILABILITY.md: agrees on every date and count it gives. Omits LSEG short sterling (1999-2002)
  and LSEG Canada BA 1 and 9-12 (harmless). Section 4's "eight contracts ... euro, sterling, and the yen" does not fit the
  sheet (correction 14). Section 8 says the sheet gives "no live source"; it lists SOFR and SONIA futures on LSEG,
  refreshable, without a trading licence (correction 18).
- Live source: Strip reversion is flagged not Core today (rule 7); the U01-T4 markets enter "Only with a registered live
  source". Correct.
- Batch: running a systematic pod without a live source "outside the batch's error count" is not in WORKFLOW (section 6
  gives that only to playbook rule layers); the note marks it as its reading (open point 3).
- Rule 5: the pack dates [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] only through coverage notes ("published Journal of Fixed Income 15(4), 2006"; "2005 FMA
  conference version"), which the note correctly calls machine notes; the quotes agree (sample to 29 December 2000, C09-4;
  Foster and Stine 2003, C22-4). [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] and [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] have no date field; the note's 2008 for [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] rests on C02-3 and C09-7
  (reader) plus "Journal of Fixed Income 2008, author's knowledge".
  Checker's knowledge: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] is the Chua, Koh and Ramaswamy paper published in the Journal of Fixed Income in 2006, which
  agrees with the coverage note (checker's knowledge). The three-part decomposition behind [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] and [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] (CFRS, cited in
  [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C06-2|QP07-C06-2]] without a year in the quote) was published as Chua, Foster, Ramaswamy and Stine, "A Dynamic Model for the
  Forward Curve", Review of Financial Studies, 2008 (checker's knowledge). I cannot confirm with certainty a journal
  publication of [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] or the date of the [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] slides. The futures implementation of [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] is itself named, untested, in the
  2006 paper (C22-2), so "the futures form is our translation" is true of the rule, not of the idea (open point 4).

### F. The two deferred proposals

- U01-T4 (short-rate futures as markets): partly supported. The Carry link rests on in-quote numbers ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-2|QP07-C19-2]]) and the
  authors' asserted reason (C19-3); credit risk of the old contract is in quote (C07-5). Adding the markets to Trend and
  Economic trend rests on the charter's breadth logic, not on these papers, which the note says ("No paper here tests Trend
  or Economic trend"). Three gaps: D1 in the charter names new commodity markets, so this is an extension of its scope
  (correction 16); the carry measure is new (correction 15); the eight-contract strip does not exist for the yen and
  sterling in the data sheet (correction 14). The exclusion of the dollar on driver grounds is reader and coherent with the
  charter's "count price drivers not markets".
- U05-T5 (spread gate): partly supported. Dropping the three built spreads rests on 2-A failing at one month on US 1-60
  month forwards (C18-1, C18-2) and on [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|QP12-C31-1]], which is said of futures contract yields; applying it to government bond
  spreads is a reader transfer (correction 17). The spreads' definitions are not in the pack, which the note flags. The
  "gate" adopted is not U05's volatility-ratio gate but [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]'s untested cost-threshold idea (C22-1) and the charter's leg
  cap; the note says so ("the authors' own idea"). U05's levels are rightly not adopted; these papers neither support nor
  refute a volatility-ratio gate.

## 3. Required corrections

Each "Find" string is copied from the note and occurs there exactly once (checked by script); replace it with "Replace".

1. Section 1.
   - Find: `local reversion paid about five times the equity benchmark`
   - Replace: `local reversion paid up to about five times the equity benchmark (rule 2-B; 3.3 times for 3-B)`
   - Reason: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C03-3|QP06-C03-3]] "by up to 5.1 times"; [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C18-4|QP06-C18-4]] "about 3.3 times" for 3-B.

2. Section 1.
   - Find: `On traded Eurodollar futures the same curve model added`
   - Replace: `On traded Eurodollar futures a related curve model ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]]: long-run curve plus decaying habitat and date parts, one of 6 chosen by AIC) added`
   - Reason: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] uses an expanding average (C10-6), [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] a different model: [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C02-1|QP07-C02-1]] "a three-part functional decomposition"; [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C14-4|QP07-C14-4]] "lowest AIC among the 6 candidate models".

3. Section 2, row 2.
   - Find: `After costs only 2-B stays ahead on every test; a tiny cost removes the profit`
   - Replace: `After costs only 2-B stays ahead on every test; a cost of about 0.01% of value traded removes the excess over the benchmarks`
   - Reason: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C05-7|QP06-C05-7]] "the implied transaction costs that would have eliminated the excess returns".

4. Section 2, row 8.
   - Find: `no costs (C18-5)`
   - Replace: `no costs counted (reader: C18-5 defines profit as the average rate move)`
   - Reason: [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-5|QP07-C18-5]]'s quote defines profit as "the cross-sectional average movement in (or against) the predicted direction"; it does not mention costs.

5. Section 3.1, mechanism chain step (2).
   - Find: `Their demand bends the curve there and at neighbouring maturities only ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-4|QP07-C08-4]]).`
   - Replace: `Their demand bends the curve there and at nearby maturities ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-4|QP07-C08-4]]). [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] models the bend "as a smooth curve" over nearby maturities, since "investors treat them as close substitutes" ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-4|QP07-C10-4]]), and treats contract-level misfits as persistent microstructure ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-2|QP07-C17-2]]), so the scale of a habitat bend is not established, and a bend between adjacent quarterly contracts may be the persistent kind (reader).`
   - Reason: [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-4|QP07-C10-4]] "can affect a range of surround- ing maturities ... which allows us to treat the maturity-specific deviation as a smooth curve"; [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-2|QP07-C17-2]] "can be expected to persist over the short-term".

6. Section 3.1, evidence grade, artefact bullet.
   - Find: `Whole-curve trades, where such errors are small against the gap, do not beat the`
   - Replace: `Whole-curve trades, where such errors are small against the gap, do not significantly beat the`
   - Reason: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C18-1|QP06-C18-1]] "only strategies 2-B, 3-A and 3-B yield higher payoffs compared with the two benchmarks" (3-A is whole-curve); [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C20-2|QP06-C20-2]] "3-A does not significantly outperform".

7. Section 3.2, whole-curve row.
   - Find: `The paper's own tests fail (row 3)`
   - Replace: `Level and whole-curve slope fail (row 3); whole-curve curvature (3-A) is above both benchmarks but not significantly (C18-1, C20-2), "marginally better" after costs (C21-6), and adds significantly to an S&P holding after costs and Bonferroni (C23-3): weak, and outranked by the local forms`
   - Reason: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C23-3|QP06-C23-3]] "Strategies 2-B, 3-A and 3-B are found to have significant value-add even after accounting for transaction costs and the bonferonni correction"; [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C21-6|QP06-C21-6]] "Strategy 3-A remains marginally better than the benchmarks".

8. Section 3.1, rule family, entry.
   - Find: `*Entry:* spread gap positive: buy point n (buy its futures), sell point n-1 (C14-1)`
   - Replace: `*Entry:* spread gap positive: buy point n, sell point n-1 (C14-1); with the weighting below this is, in contracts, long contract n against an equal-weight short of contracts 1 to n-1 at equal DV01 (reader's algebra, section 7 item 3)`
   - Reason: "its futures" can be read as contract n alone, a level bet; [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C14-2|QP06-C14-2]] duration-weights each leg ("approximately equal payoff contribution").

9. Section 3.1, rule family, cost gate.
   - Find: `no position while the gap is below the trade's`
   - Replace: `no position while the absolute gap is below c x 2 x (sum of the absolute weights of the measure on the contract rates), with c = half a bp per contract per side (spread n: sum 2/n; curvature at point n: (2n+4)/(n(n+1))), i.e. the`
   - Reason: the gap is in bp of a zero-point measure and the cost in bp of rate per contract; without the conversion the gate is a hidden choice. Half a bp from [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C21-2|QP06-C21-2]] "pay a transaction cost of half basis point"; the weights follow the note's own algebra (section 7 item 3).

10. Section 3.1, rule family, normal.
    - Find: `from 60 months of history on`
    - Replace: `from 60 calendar months of history on (about 15 month-ends per expiry-month group)`
    - Reason: 60 observations per group would need about 20 years and start the dollar normal near 2001, against the note's 1990 design start; the brief requires no hidden choice.

11. Section 3.1, rule family, signal.
    - Find: `*Signal:* gap = measure minus normal, at the prior day's settlement prices.`
    - Replace: `*Signal:* gap = measure minus normal, at the settlement prices of the tranche's decision day; the trade is made at the next trading day's settlement.`
    - Reason: the note's data line says the purpose of daily prices is to trade at a price other than the one that gave the signal; "prior day" leaves the trade day open.

12. Section 3.1, rule family, instruments.
    - Find: `*Instruments:* per currency, the first eight quarterly three-month rate futures expiring after the`
    - Replace: `*Instruments:* per currency with all eight contracts in the locked history at that date (no strip is built from fewer), the first eight quarterly three-month rate futures expiring after the`
    - Reason: DATA_AVAILABILITY.md: "Euroyen 6 contracts", "Short sterling contracts 1-5", "Canada BA contracts 1 and 9-12" (LSEG); the currency set was open.

13. Section 3.1, Fixed, stale screen.
    - Find: `settlement price changed on 15 of the last 20 trading days`
    - Replace: `settlement price changed on 15 of the last 20 trading days before the decision day (the screen applies to signals; month-ends without daily data enter the normal unscreened)`
    - Reason: daily prices exist only from 1989-12 and only for contracts 1, 2, 4, 8 (DATA_AVAILABILITY.md); whether the normal is screened was unstated.

14. Section 4, U01-T4.
    - Find: `equal parts: euro, sterling, and the yen if its contract is live.`
    - Replace: `equal parts, only where eight contracts are in the locked history and a live source is registered: today the euro (Euribor from 1994) at most; sterling has contracts 1-5 on Bloomberg (no live feed) and starts 1999-2002 on LSEG, the yen has 6 contracts.`
    - Reason: DATA_AVAILABILITY.md: "Euroyen 6 contracts (1989+)", "short sterling only from 1999-2002", "Short sterling contracts 1-5 from 1988" (Bloomberg, "no live feed"); no live yen source is listed.

15. Section 4, U01-T4, carry.
    - Find: `with unchanged rules (carry = the roll down the strip, the gain as contracts age)`
    - Replace: `with unchanged rules, except that Carry needs a new measure for a strip market (the roll down the strip, the gain as contracts age), whose formula and scaling against bond carry in the fixed-income rank the spec writes at step 3.1`
    - Reason: charter digest, Carry: "Carry = bond yield minus the 3-month rate, the rate gap to the dollar, or the slope between the first two energy contracts" and "half its rank within the asset class"; no strip measure exists.

16. Section 4, U01-T4, registration.
    - Find: `Registered as markets added to existing pods: candidates in the charter's`
    - Replace: `Registered as markets added to existing pods: candidates in an extension (registered at 3.4; the charter's D1 names new commodity markets) of the charter's`
    - Reason: charter digest, verdict: the pass "decides three Batch A items (new commodity markets, a no-trade buffer, a faster book scaler)"; short-rate futures are not in D1's stated scope.

17. Section 4, U05-T5.
    - Find: `([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|QP12-C31-1]], ASSERTED)`
    - Replace: `([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|QP12-C31-1]], ASSERTED, said of futures contract yields; its use for bond yield spreads is reader)`
    - Reason: [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|QP12-C31-1]] "Differences in yields of adjacent contracts are non-stationary as time gap increases" is about contracts.

18. Section 8, data sheet.
    - Find: `gives no start for dollar contracts 5-8, no live source and no names for the three built spreads.`
    - Replace: `gives no start for dollar contracts 5-8, no live source licensed for trading (it lists SOFR and SONIA futures on LSEG, refreshable) and no names for the three built spreads.`
    - Reason: DATA_AVAILABILITY.md: "LSEG Workspace + Datastream (user's own PC, refreshable any day ...)", "Successor SOFR futures from 2018", "SONIA from 2018".

19. Section 5, R1 computation.
    - Find: `triple's round-trip cost at half a bp of rate per contract traded.`
    - Replace: `triple's round-trip cost as in the entry rule of 3.1 (half a bp per contract per side, times 2, times (2n+4)/(n(n+1)) for the curvature at point n).`
    - Reason: same unit gap as correction 9; without it the gate of R1 has a hidden choice.

20. Section 3.1, evidence grade (omitted quotes) and section 8.
    - Find: `- Chance is not the worry (alpha t of 9.1758, C23-4; 6 strategies, C20-3). Tradability is.`
    - Replace: `- Chance is not the worry (alpha t of 9.1758, C23-4; 6 strategies, C20-3, at least two run in two versions, C13-1, C14-3; whether the t allows for serial correlation is not stated). Tradability is. Also against: arbitrage trades are "frequently constructed in the transition between the short- end and the long-end" (C25-2), the pod's target segment; differences of contract yields are "non-stationary as time gap increases" ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|QP12-C31-1]]), which bears on this pod's own normal (spread n compares contract n with contracts up to 21 months nearer; reader); "Moving medians of length 3 cannot patch a period with a sustained anomaly" ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C26-1|QP12-C26-1]]), so data errors can outlast R1's one-day test. Text against chart readings (summary only): C24-5 places "the most profitable trade segments" at 10-23 months, but the readings of Figure 5 give 2-B's largest shares to the 1-2 and 2-3 month spreads (C37-1), which no futures strip can trade.`
    - Reason: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C25-2|QP06-C25-2]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|QP12-C31-1]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C26-1|QP12-C26-1]], [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C13-1|QP06-C13-1]] ("We consider two versions of the trade"), [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C14-3|QP06-C14-3]]; [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C37-1|QP06-C37-1]]'s figures are summary only (its quote is the figure title), so they qualify, not replace, C24-5.

## 4. Open judgement points (not corrections)

1. Measures on contract (forward) rates instead of zero points: [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]]'s habitat bend lives in forward rates, and the zero-point form makes spread n a contract-n-against-nearer-contracts slope; closed at spec 3.1.
2. Residual roll in the pairs: "most of the roll cancels" is unshown; a concave average curve gives near contracts more roll-down, possibly correlated with the gap sign; report it or write it into the thesis at spec 3.1.
3. A systematic pod without a live source run "outside the batch's error count" is not in WORKFLOW section 6 (rule layers only); registration 3.4 settles it under the written rules.
4. Rule 5 for the futures form: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]'s 2006 text names Eurodollar futures as the implementation (C22-2), untested; whether that counts as documented before 2011 is for the thesis register 1.5.
5. R1 screens size and one-day persistence only; an outlier screen ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C24-1|QP12-C24-1]], C26-1) or a check on December contracts may be needed so bad prints and lasting blips do not pass; registration 3.4.
6. Whole-curve curvature (3-A, significant alpha against the S&P after costs, C23-3) is rejected without a version or diagnostic; thesis register 1.5.
7. The expiry-month groups pool month-ends at different times to expiry (ageing ignored, section 7 item 3); spec 3.1 decides whether that needs an adjustment.
8. Curve carry keeps both versions on a reader argument; charter open point 5 gains no quote support from [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]]; spec 3.1-3.2.
9. The cost floor of half a bp per contract is borrowed from 2003 Treasury spreads (C21-1, C21-2); the registered futures cost is set at 3.1/3.4.

## 5. What I could not verify

- Whether [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]'s paired t-tests and the alpha t of 9.1758 allow for serial correlation (the D-M results are in words only;
  C19-3 calls autocorrelations "small", the chart readings of C34-1/C35-1 are summary only).
- Every [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] figure value (segment shares, 10-year averages and their crossing dates) and every [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] statistic: summary
  only.
- Whether [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]'s Figures 7-8 and Table 4 use gross or net payoffs (C23-3's quote says the value-add holds after costs; the
  figure "net profit" wording is claim text).
- The journal publication of [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] and the date of the [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] slides (not in the pack; not known to me with certainty).
- Start dates of dollar contracts 5-8, the number of Euribor contracts, LSEG licence terms, and the definitions of the
  engine's three built spreads (not in the pack).
- The note's reader settings (8 contracts, 60 months, 15 of 20 days, the 50% gate of R1) have no source to check against;
  they are fixed and labelled, which is all the rules require.

