---
tags: [fable, thesis]
code_commit: dd88b92
---
> Fable 5.2 max; the 20 corrections of the independent check are applied. Exact inputs: _data/thesis_1.3_rates/. See [[Thesis 1.3a - Independent check]], [[Charter 1.2 - Systematic charter]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/dd88b9212f379079ef81ee41f61dab5479f367db/docs/research/fable/THESIS_1.3_rates.md).
# Thesis note 1.3a: rates and curve ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]])

Fable unit 1.3a, 2026-11-14. Source logic only: no code, no data, nothing after 2010. Labels: SHOWN = the quote
gives a test with numbers; SHOWN (words) = the quote reports a test's outcome, its numbers are summary only;
ASSERTED = no test; (reader) = my inference; (summary only) = not in a quote, nothing built on it. bp = basis point,
0.01%. A claim id without a paper prefix belongs to the paper named last before it in the same sentence or table
row, else to [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]. The papers share one idea: a curve is a long-run average curve plus bends that fade.

> **Status (2026-11-14): PASS WITH CORRECTIONS.** Written by one Fable 5.2 run (effort max) from the verbatim quotes of
> three papers ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]], [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]], [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]]; no code reading), then checked by an independent Opus 5.5 run against the same quotes.
> The 20 corrections the check required are applied in this text; the check is `THESIS_1.3_rates_check.md`, its summary
> is section 10. Original Fable text, exact input pack and both briefs: macro-vault `pipeline/thesis_1.3_rates/`.
> Nothing here is registered or run (registration = WORKFLOW step 3.4).

## 1. Verdict

Spec one new pod, **Strip reversion**: fade local bends in short-rate futures curves with [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]'s two local rules.
Grade weak. Batch B2, behind every stronger candidate, and only if diagnostic R1 passes and daily prices are locked.
Do not spec: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]'s Treasury-bill form, whole-curve reversion (the engine's three built spreads stay untraded),
the [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] model as a signal, a [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] commodity forecast pod. Front-end carry is not a pod: short-rate futures
enter existing pods as markets (non-US only) through the charter's breadth check D1.
Established: on estimated Treasury yields 1973-2000 local reversion paid up to about five times the equity benchmark (rule 2-B; 3.3 times for 3-B)
per unit of risk before costs, and faded after the late 1980s. On traded Eurodollar futures a related curve model ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]]: long-run curve plus decaying habitat and date parts, one of 6 chosen by AIC) added
0.03 and 0.30 bp a trade (5- and 250-day holds) to always-long. Weakest link: no test of the local rule on traded prices.

## 2. What the three papers establish

| # | Statement | Label | Claims | In the quote | Limits |
|---|---|---|---|---|---|
| 1 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]: fading spread gaps between neighbouring maturities (rule 2-B) and curvature gaps among three neighbours (3-B) paid several times both benchmarks per unit of risk before costs; both add to a share holding | SHOWN | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C18-3|QP06-C18-3]], C18-4, C19-1, C23-4 | 2-B "about 5.1 times" the equity benchmark, 3-B "about 3.3 times"; "about 5.9 times" and "about 3.8 times" the bond benchmark; alpha "t-statistics of 9.1758 and 4.9836" | US, 1973-2000; estimated yields, not prices; signals use past data (C10-6), risk is matched "after all the payoffs are realized" (C17-4); other test values summary only |
| 2 | After costs only 2-B stays ahead on every test; a cost of about 0.01% of value traded removes the excess over the benchmarks | SHOWN (words; one number) | C21-5, C21-6, C05-7 | 2-B "under all measures"; 3-B "in the t-tests but not in the D-M tests"; break-even "about 0.01% of the value of bonds traded" | cost "half basis point" a trade (C21-2) from a "5-year average" of spreads (C21-1), used for all 28 years; benchmarks pay none (C21-4b) |
| 3 | Level and whole-curve slope reversion do not beat holding bonds; whole-curve curvature is not significant | SHOWN (words) | C18-1, C18-2, C20-2 | "only strategies 2-B, 3-A and 3-B yield higher payoffs"; 3-A "does not significantly outperform" | one-month horizon; values summary only |
| 4 | The edge faded | SHOWN (words) | C03-6, C25-5 | "diminished since the late 1980s"; 3-B "by 1990" had "fallen below the two benchmarks" | 10-year averages, no sub-period test; cause ("improved in efficiency", C26-1) ASSERTED |
| 5 | Profit grows with gap size; the most profitable segments lie at 10 to 23 months | SHOWN | C24-2, C24-3, C24-5 | "correlation = 0.814" (2-B), 0.763 (3-B); "10-month to 23 month portion" | in-sample; segment shares summary only |
| 6 | Offered reason: maturity habitats. Futures are named as a cheap stand-in for a bond pair | ASSERTED, after the results | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C25-1|QP06-C25-1]], C24-5, C22-2; [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-3|QP07-C08-3]] | "preferred habitats that are dictated by the nature of liabilities and investments"; "highly liquid Eurodollar futures gives identical payoff" | no holder or flow data; the futures form is untested |
| 7 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]]: model forecasts of Eurodollar forward rates beat no-change, not significantly | SHOWN | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C18-1|QP07-C18-1]], C18-2 | gain "0.02 basis points" (5 days) to "6.31 basis points" (250 days); "not statistically significant at the usual levels" | forecasts 1991-2008; one model of 6, chosen on data to 10/28/1991 (C14-4, C17-3) |
| 8 | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]]: trading the forecast direction earns barely more than always holding the futures, since the average curve slopes up; the model wins on days when the two disagree | SHOWN; reason ASSERTED | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-1|QP07-C19-1]] to C19-5 | model "1.19 basis point" (5 days) to "49.04 basis points" (250 days) a trade; always-long 1.16 to 48.74; the model will "more often than not, predict a fall"; "NW-stat reaching 7.953" | differences 0.03 and 0.30 bp (reader); no costs counted (reader: C18-5 defines profit as the average rate move); not risk-adjusted; overlapping windows (C18-3); no count of disagreement days; rates fell (author's knowledge) |
| 9 | Contract-level ripples last | ASSERTED | [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C13-5|QP07-C13-5]], C17-2; [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C21-1|QP12-C21-1]] | "persistent blips in the data for December contracts"; "can be expected to persist over the short-term" | one illustration; cuts against quick reversion in futures (reader) |
| 10 | [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]]: the same split is said to fit commodity curves and beat no-change forecasts; futures-built curves are noisy, stale in places, seasonal | ASSERTED (slides, charts) | [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C35-1|QP12-C35-1]], C17-2, C20-2, C22-1, C31-1, C11-1 | "Out-of-sample performance superior to random walk benchmark"; "Differencing magnifies random noise"; a price "stayed same as on prior day"; spreads "non-stationary as time gap increases"; "Strong seasonal pattern" | statistics summary only; sample and loss not stated; no claim reports a trade; "Many unresolved questions" (C35-2) |

t-test, D-M test, NW-stat: significance tests (the last two allow for serial correlation). Alpha: return beyond the
share market's part.

## 3. Candidate pods

### 3.1 Strip reversion (to spec)

**Mechanism chain.** (1) Some borrowers and lenders must deal at one maturity, "with little regard for the
implication of the forward rates on future spot rates" ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-3|QP07-C08-3]]; [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C25-1|QP06-C25-1]]: "asset-liability management
constraints"). ASSERTED. (2) Their demand bends the curve there and at nearby maturities ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C08-4|QP07-C08-4]]). [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] models the bend "as a smooth curve" over nearby maturities, since "investors treat them as close substitutes" ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-4|QP07-C10-4]]), and treats contract-level misfits as persistent microstructure ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C17-2|QP07-C17-2]]), so the scale of a habitat bend is not established, and a bend between adjacent quarterly contracts may be the persistent kind (reader).
ASSERTED. (3) The bend fades. [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] assumes it: "a simple yet intuitive model ... would be that they decay towards
zero at some rate" ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-5|QP07-C10-5]]). ASSERTED. (4) We hold the cheap point against its neighbours and are paid as the
bend fades. SHOWN only on estimated Treasury yields (rows 1, 2); untested on futures.

**Other side.** The maturity-bound hedgers and lenders, who pay to deal at their own date. Named, not shown: no
paper has holder or flow data, and the reading came after the results ("provides some support", C24-5). Why they
keep paying is answered against us: traders learned to "rapidly seek out" these trades (C26-2) and the scope
"diminished since the late 1980s" (C03-6).

**Evidence grade: weak.**
- One test, on yields that are estimated ("approximate", C09-4b) and interpolated twice (C09-6, C10-2); signal and
  trade come from the same file (reader: no quote gives a dealing price).
- It may be an artefact (reader): independent errors in neighbouring yields make gaps that close next month, and a
  back-test dealing at recorded yields earns them. Four facts fit. The most profitable trades sit at the 10-11 month
  points, where the file's monthly maturities end and its yearly ones begin (C24-2, C09-5, C10-1); the authors read
  this as segmentation (C24-5). Whole-curve trades, where such errors are small against the gap, do not significantly beat the
  benchmarks (row 3). Payoff tracks gap size at 0.814 (C24-3), which needs large gaps that vanish within the month,
  while [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] finds its curve model useful "most notably at longer forecast horizons" ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C07-7|QP07-C07-7]]): bends that fade
  slowly. A reward five times the share market's for 28 years is implausible for a liquid market.
- Risk is standard deviation only (C05-2); the edge faded (row 4); on traded futures no spread trade was run and
  ripples are said to last (rows 8, 9).
- Chance is not the worry (alpha t of 9.1758, C23-4; 6 strategies, C20-3, at least two run in two versions, C13-1, C14-3; whether the t allows for serial correlation is not stated). Tradability is. Also against: arbitrage trades are "frequently constructed in the transition between the short- end and the long-end" (C25-2), the pod's target segment; differences of contract yields are "non-stationary as time gap increases" ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|QP12-C31-1]]), which bears on this pod's own normal (spread n compares contract n with contracts up to 21 months nearer; reader); "Moving medians of length 3 cannot patch a period with a sustained anomaly" ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C26-1|QP12-C26-1]]), so data errors can outlast R1's one-day test. Text against chart readings (summary only): C24-5 places "the most profitable trade segments" at 10-23 months, but the readings of Figure 5 give 2-B's largest shares to the 1-2 and 2-3 month spreads (C37-1), which no futures strip can trade.

**Rule family.** *Instruments:* per currency with all eight contracts in the locked history at that date (no strip is built from fewer), the first eight quarterly three-month rate futures expiring after the
holding month (the strip; two years, where the paper's most profitable segments sit: C24-5). *Curve:* point n is the
average of the first n contract rates (reader's construction of [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]'s zero-coupon yields; futures as stand-in for
bonds: C22-2). *Measures:* the adjacent spread, point n minus point n-1 (rule 2-B, C13-5); the adjacent curvature,
the spread into a point minus the spread out of it (rule 3-B, C15-4; formula in claim text only, C14-4). *Normal,
without look-ahead:* the expanding average of each measure over all earlier month-ends ("simple average ... till the
preceding month", C10-6), by currency, position and expiry month of contract n (December contracts carry lasting
ripples, [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C13-5|QP07-C13-5]]), from 60 calendar months of history on (about 15 month-ends per expiry-month group). Futures rates are forward rates, so [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]'s one-month-forward
step (C10-4) needs no formula (reader). *Signal:* gap = measure minus normal, at the settlement prices of the tranche's decision day; the trade is made at the next trading day's settlement.
*Entry:* spread gap positive: buy point n, sell point n-1 (C14-1); with the weighting below this is, in contracts, long contract n against an equal-weight short of contracts 1 to n-1 at equal DV01 (reader's algebra, section 7 item 3); curvature gap positive: buy the
middle point, sell both neighbours; negative gaps the reverse; no position while the absolute gap is below c x 2 x (sum of the absolute weights of the measure on the contract rates), with c = half a bp per contract per side (spread n: sum 2/n; curvature at point n: (2n+4)/(n(n+1))), i.e. the
round-trip cost. *Exit:* after one month, then a new trade (C11-1); four weekly tranches. *Weighting:* each pair and
triple earns the same per bp of gap change (C14-2); currencies carry equal risk. *Risk scaling:* a currency's net
position is scaled to the shop's standard market target on its current volatility; no contract is held larger than
the shop's standard position in that contract alone (leg cap).

**Version grid** (both run, averaged):

| Dimension | Levels | Why uncertain | n |
|---|---|---|---|
| Local measure | adjacent spread (2-B); adjacent curvature (3-B) | The spread rule is the paper's stronger result, but when all pairs lean one way their legs cancel into the whole-curve slope bet that did not beat holding bonds (row 3; reader). The curvature rule isolates one bend and ignores level and slope (C15-3 for the whole-curve form; reader for equal steps), but it is the rule that fell below the benchmarks (row 4). Which measures a habitat bend is unsettled. | 2 |

**Fixed.** Everything in the rule family except the measure. Sign of the gap at fixed size, the tested form (C14-1).
Graded sizing is dropped: [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]]'s decay model would support it (C08-5), but only the sign was tested and a graded
rule adds size exactly when bends widen (case 3 below). Expanding normal from 60 months (reader's setting; the
paper's 102 months followed its benchmark's start, [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C11-3|QP06-C11-3]], C11-4). No normal passes from a reference rate to its
successor (Eurodollar to SOFR; the old rate carried bank credit risk, [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C07-5|QP07-C07-5]]). A contract counts only if its
settlement price changed on 15 of the last 20 trading days before the decision day (the screen applies to signals; month-ends without daily data enter the normal unscreened) (stale prices bend a curve, [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C22-1|QP12-C22-1]]; reader's
setting). Costs at the registered rate, at least half a bp of rate per contract traded ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]'s assumption for bonds,
C21-2).

**Data.** History (LSEG, pulled, not yet in the engine): dollar strip monthly, contracts 1-4 from 1981-12, 9-12 from
1987-06, to 2023; daily only for contracts 1, 2, 4, 8, from 1989-12; euro from 1994, yen 1989 (6 contracts), Swiss
franc 1991 (8, ended); sterling 1-5 from 1988 and Canadian 2-8 from 1990-91 on Bloomberg, no live feed. Live: SOFR
and SONIA futures from 2018, Euribor, on LSEG, whose licence for trading use is unverified (charter check): no
registered live source, so not Core today (rule 7). Missing: daily prices for dollar contracts 3, 5, 6, 7 and every
other strip (without them the trade is made at the price that gave the signal, which earns the noise suspected in
[[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]); start dates of dollar contracts 5-8. Design sample: the dollar from 1990-01 at the earliest, 21 years against
the test sheet's 1975-2010, all in the years the authors call diminished.

**Stops working.** (1) Ample arbitrage capital: gaps stay below cost and the rule goes flat (reader, from the
authors' account, C26-2). (2) A front end pinned by policy: a flat strip (reader). (3) Funding stress: bends widen
before they fade and a levered pair loses most when dealers withdraw (reader; no quote covers it). (4) A new
reference rate or contract design: the normal no longer applies.

**Relation.** A separate mechanism: pay for meeting maturity-bound demand. Not Carry: positions follow the gap, and
most of the roll cancels between the two sides of a pair (reader). Not Value as built (a rank across markets); the
nearest idea is value against a market's own history, applied to curve shape (reader).

**Rule 5.** Documented before 2011 on the pack's date fields: coverage notes give a "2005 FMA conference version"
and "Journal of Fixed Income 15(4), 2006" (machine notes, not quotes); the quotes agree (sample ends 29 December
2000, C09-4; a 2003 paper is cited, C22-4). What is dated is the rule on Treasury yields; the futures form is our
translation. [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]], the same split on Eurodollar futures, is not dated in the pack: sample to 1/28/2008 ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C02-3|QP07-C02-3]]),
January 2009 still ahead ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C09-7|QP07-C09-7]]), so 2008 (reader; Journal of Fixed Income 2008, author's knowledge). My
reading: dated before 2011, flagged as translated at step 1.5.

**Batch: B2,** only if (a) daily prices for dollar contracts 1-8 are locked and (b) R1 passes; else dropped and
logged, not re-run. With a registered live source it takes a place only if one is free after every candidate graded
moderate or strong. Without one it runs for Incubator status only, outside the batch's error count (reader's
reading), like the playbook rule layers (WORKFLOW section 6): it cannot be Core (rule 7) and should not raise the
bar for pods that can.

### 3.2 Candidates not to spec

Rejected: no rule family, grid or data line.

| Candidate | Mechanism and other side | Grade | Why not | Relation | Rule 5 | Batch |
|---|---|---|---|---|---|---|
| [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] as written: Treasury bills and notes at monthly maturities | as 3.1 | weak, as a trade | Not buildable: no monthly bill curve in the data sheet; one version trades "maturities one month apart from one month to 60 months" (C14-3), mostly interpolated points (C10-1); break-even "about 0.01%" of value (C05-7) | separate mechanism | yes: 2005, 2006 (coverage notes) | not now |
| Whole-curve reversion: level, slope, curvature (1-A, 1-B, 2-A, 3-A); includes the engine's three built spreads | "the yield curve mean-reverts to an unconditional curve" (C03-1); no other side: pattern, no mechanism | none (level, slope); weak (curvature) | Level and whole-curve slope fail (row 3); whole-curve curvature (3-A) is above both benchmarks but not significantly (C18-1, C20-2), "marginally better" after costs (C21-6), and adds significantly to an S&P holding after costs and Bonferroni (C23-3): weak, and outranked by the local forms | own-history value on rates (reader) | yes, as above | not now |
| [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] model as a signal: trade each contract in the forecast direction | the three-part curve split; other side for its habitat part as 3.1 | weak | Adds 0.03 and 0.30 bp to always-long (row 8); forecast gain not significant (row 7); 6 state variables ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C15-1|QP07-C15-1]]) | its profit is Carry (row 8) | not dated in the pack; 2008 (reader) | not now |
| Front-end carry: always long the strip | forward rates drift down as contracts age, since the average curve slopes up ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-3|QP07-C19-3]]); "the term risk premium" ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C05-5|QP06-C05-5]]); other side not stated | weak: SHOWN once ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-2|QP07-C19-2]]), 1991-2008, no costs, not risk-adjusted | Not a new mechanism | the Carry pod's rule on new markets | as Carry (open in the charter) | none: markets, section 4 |
| Commodity curve forecast ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]]) | curve shape returns to its long-run form ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C13-3|QP12-C13-3]], C14-1); no other side: pattern, no mechanism | none: statistics summary only | Slides; no sample, no loss function, no trade | would overlap Curve carry | not dated in the pack (claim text has a 7 Nov 2008 example) | not now |

### 3.3 [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] and the charter's Curve carry

Data rules for that spec, from [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] quotes: real contracts, not interpolated fixed-maturity prices (C23-1, C28-1);
no front contract in its delivery month (C29-1, C30-1; reader's setting); a stale-price screen as in 3.1 (C22-1);
for seasonal commodities the same delivery month a year later as far leg (C11-1); sizing on current spread
volatility, since far-apart contracts have no stable normal (C31-1). Charter point 5: no quote here bears on the
backwardation switch (flat when the front price is above the 12-month price). [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] says the curve returns to its
long-run shape (C13-3, C14-1), so in backwardation the pair pays roll while waiting for a fade of unknown size
(reader): an uncertainty that does not rest on the seller. The two versions stand.

## 4. The two deferred proposals

**U01-T4, short-rate futures as markets.** Registered as markets added to existing pods: candidates in an extension (registered at 3.4; the charter's D1 names new commodity markets) of the charter's
breadth item, under its D1 gate; no pod, no slot. One market per currency, the eight contracts of the 3.1 strip in
equal parts, only where eight contracts are in the locked history and a live source is registered: today the euro (Euribor from 1994) at most; sterling has contracts 1-5 on Bloomberg (no live feed) and starts 1999-2002 on LSEG, the yen has 6 contracts. They join the fixed-income block of Trend,
Economic trend and Carry with unchanged rules, except that Carry needs a new measure for a strip market (the roll down the strip, the gain as contracts age), whose formula and scaling against bond carry in the fixed-income rank the spec writes at step 3.1. Not the
dollar: the engine holds its driver, the US 2-year note (reader: its yield is near the average of the first eight
forward rates), twice. Only with a registered live source (rule 7). Reasons in the quotes: what the strip paid was
the roll down an upward-sloping curve ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-2|QP07-C19-2]], C19-3), which is Carry's mechanism; the settled rate carried bank
credit risk ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C07-5|QP07-C07-5]]), so history and live instrument differ. No paper here tests Trend or Economic trend on
these markets: the proposal's prior (0.37-0.70, unverified) gets no support.

**U05-T5, spread gate.** Split. The three built yield spreads: dropped, they stay untraded. The nearest test, the
whole-curve slope against its own history, did not beat holding bonds ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C18-1|QP06-C18-1]], C18-2, SHOWN in words), and
spreads between far-apart points are "non-stationary as time gap increases" ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|QP12-C31-1]], ASSERTED, said of futures contract yields; its use for bond yield spreads is reader): no stable normal
(if they run between countries the papers are silent: no thesis). The gate: two fixed rules in Strip reversion. No
position below the round-trip cost: the authors' own idea, to trade when deviations "exceed certain thresholds"
(C22-1, ASSERTED), with payoff rising with gap size (C24-3, SHOWN). The leg cap with sizing on current volatility:
the paper sized "after all the payoffs are realized" (C17-4) and offers no rule. His levels (2%, 10%) are not
adopted: unverified.

## 5. Diagnostics

One, zero slots, design months only.

**R1. Are there local bends on the strip that are larger than their trading cost and still there a day later?**
- Computation: for the dollar strip at month-ends 1990-01 to 2010-12 and the six triples of neighbouring points
  (where a normal exists), take the curvature gap of 3.1 on the signal day and on the next day, each against the
  triple's round-trip cost as in the entry rule of 3.1 (half a bp per contract per side, times 2, times (2n+4)/(n(n+1)) for the curvature at point n). Count triple-months where both are larger than
  the cost and have the same sign; no return and no later change is computed.
- Data: daily settlement prices of dollar contracts 1-8; monthly prices from 1981-12 for the normal.
- Gate, fixed now: if at least half of the triple-months qualify, both versions go to B2 registration. If fewer, the
  pod is dropped unbuilt: without local bends above cost the spread version is only the whole-curve slope bet (row
  3). The run is logged as a design-data trial (step 7.1).

## 6. Numbers used

- In quote, [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]: 5.1, 3.3, 5.9, 3.8 times (C18-3, C18-4, C19-1); 0.01% (C05-7); half a bp, 5-year average (C21-2,
  C21-1); 6 strategies (C20-3); t 9.1758, 4.9836 (C23-4); 0.814, 0.763 (C24-3); 10-11, 10-11-23, 10 to 23 months
  (C24-2, C24-5); 9-10-11 (C40-1); late 1980s, 1990 (C03-6, C25-5); 29 December 2000 (C09-4); January 1973 to
  December 2000 (C17-3); 102 months (C11-3); 2003 (C22-4).
- In quote, [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]]: 1/28/2008 (C02-3); 10/28/1991 (C17-3); January 2009 (C09-7); 6 models (C14-4); 6 state variables
  (C15-1); 0.02, 6.31 bp (C18-1); 1.19, 49.04 bp at 5 and 250 days (C19-1); 1.16, 48.74 bp (C19-2); 7.953 (C19-5);
  about 40 contracts (C13-4).
- Reader arithmetic, dating: 0.03, 0.30 bp ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-1|QP07-C19-1]] minus C19-2); 28 years ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C17-3|QP06-C17-3]]); 21 years (1990-01 to
  2010-12); 2008 for [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] (from C02-3, C09-7).
- Summary only, not built on: 2005, 2006 ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] coverage notes; date fields for rule 5); 11.8, 0.001, 0.25-0.36,
  1994-95 ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C30-1|QP06-C30-1]], C34-1, C35-1, C42-1); 1.919, 1.804 ([[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C19-5|QP07-C19-5]]); 7 Nov 2008, 15 days ([[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C04-1|QP12-C04-1]], C20-2).
  Unverified and unused: 0.37-0.70, 2%, 10% (deferred proposals).
- Not claims: strip dates and contract counts (data sheet); 1975-2010 and 2011 (WORKFLOW).
- Reader's settings: 8 contracts, 60 months, 15 of 20 days, half of triple-months; cost floor half a bp (C21-2).

## 7. For the Opus check; what the papers leave unanswered

Check first:
1. The grade: every [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] test value outside rows 1 and 5 is summary only (the quotes are table titles); the grade
   should lean on none.
2. The artefact reading: is there a quote on dealing prices, or on a gap between signal and trade?
3. The translation to futures (reader's algebra): the spread between neighbouring points equals contract n's rate
   minus the average of the nearer contracts, divided by n; pairs that lean one way cancel into the whole-strip
   trade; ageing inside a quarter is ignored; the curvature formula is claim text ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C14-4|QP06-C14-4]]).
4. Data: daily prices for all eight contracts (the sheet lists four); which strips are live.
5. R1's two reader settings, and that it reads no return.

Unanswered by the papers: whether local reversion exists in traded prices, and after 1990; who the habitat traders
are; how the edge behaves in funding stress; how [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]]'s profit splits between whole-curve and local parts, and
between roll and reversion; any country but the US; [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]]'s sample, loss function and any trade.

## 8. Pack problems

- Paper against paper: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] earns from gaps that close within a month (C24-3, C24-4); [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] treats contract-level
  misfits as lasting (C17-2). [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C22-2|QP06-C22-2]] calls the futures payoff "identical" to a bond pair; [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C07-5|QP07-C07-5]] says the
  futures rate carries bank credit risk.
- [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]], summary against quote: C06-1's quote starts at "than the current transaction cost", so the claim's direction
  ("below") is not in it; C20-3's quote says results stay "highly significant" after the correction, its claim says
  3-B fails it, on summary-only p-values; C21-4b's quote stops at "traded without any"; both formulas (C10-5,
  C14-4), the dates 2005 and 2006 and "Bloomberg, Nov 2003" (C21-1) are claim text or coverage notes.
- [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] map: cites C05-6b (a benchmark definition) for the 0.01% cost, which is in C05-7; grades the main result
  "strong - t up to 11.8, DM p 0.001" on C30-1's summary fields, whose quote is a table title.
- [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]], text against exhibits: C19-3 calls autocorrelations "small", C34-1 and C35-1 read 0.25-0.36 off charts;
  C25-5 says "by 1990", C42-1 reads 1994-95 (both summary only); C24-2 names the 10-11-23 month curvature trade, the
  figure title in C40-1 the 9-10-11 (quote against quote).
- [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]], quote against quote: C02-4 ("better out-of-sample predictions") and C18-2 ("not statistically significant");
  C30-2 (fit errors "serially uncorrelated") and C17-2 (they persist); C19-5 says the model wins "for all holding
  periods" while its summary fields give 1.919 and 1.804 at 5 and 20 days; no date field.
- [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]]: every forecast statistic is summary only, yet the map grades the result "moderate"; C35-2's claim adds "no
  trading application" to the quote "Many unresolved questions"; "15 days" (C20-2) is claim text; no date.
- Data sheet against the papers' needs: [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] needs Treasury yields at monthly maturities (absent); [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] used about
  40 contracts daily (C13-4), the sheet has 12 monthly and 4 daily; [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] used CRB Trader prices (C19-1). The sheet
  gives no start for dollar contracts 5-8, no live source licensed for trading (it lists SOFR and SONIA futures on LSEG, refreshable) and no names for the three built spreads.
- U01-T4 says "already in Batch 2" and "No new slot"; WORKFLOW keeps B2 for new pods and the charter treats new
  markets as a Batch A breadth item.
- Charter, Carry: energy carry is "the slope between the first two" contracts, where [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C20-2|QP12-C20-2]] and C30-1 place the
  most noise.

## 9. Self-check

- Against Strip reversion. The evidence is weak and may be noise in a yield file. The design sample is 21 years
  inside the era the authors call diminished: the likeliest result is "Shelved". Inside the error count it would
  raise the bar for the other B2 pods. The futures form is ours: a failure would not refute [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]], a pass would not
  confirm it. R1 screens for size, not for reversion: large bends that never fade get through.
- Against rejecting [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] as written. It is the only form the paper tested; if the profit was real it lived in bills,
  where our translation does not go.
- Against rejecting whole-curve reversion and dropping the three spreads. The paper tests one month and one
  country's curve; slower reversion is not refuted.
- Against rejecting the [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]] model. On the days it disagreed with always-long it won (NW-stat 7.953): a possible
  signal for leaving front-end carry, unused.
- Against front-end carry as markets only. It is the one profit in this pack shown on traded prices.
- Against rejecting a [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] pod. If its summary-only statistics are right, commodity curve shape is forecastable and
  we use none of it.

## 10. Independent check (Opus 5.5, 2026-11-14): summary

Full text: `THESIS_1.3_rates_check.md`.

Verdict: PASS WITH CORRECTIONS. No conclusion reversed; 0 of 6 pod grades changed.
- Numbers (38 from the papers): 36 in quote, 2 correct reader arithmetic, 0 contradicted. The 10 summary-only numbers
  are tagged and none is built on. All 104 cited claim ids resolve; every quoted phrase is verbatim.
- Statements (21): 17 supported, 4 partly (corrected above).
- The rule family, diagnostic R1 and the short-rate-futures entry held 7 hidden choices (how trades map to futures legs,
  how a gap in bp compares with a cost per contract, the 60-month history, trade timing, which currencies and short
  strips count, the stale-price screen, the carry measure for strip markets). The corrections fix each one.

Quotes against Strip reversion that the note did not use (now cited in the text):
1. [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0#^QP07-C10-4|QP07-C10-4]]: habitat bends sit in a smooth, slow component ("investors treat them as close substitutes ... as a smooth
   curve"); contract-level misfits are treated as microstructure expected to persist (C17-2, C14-1). The only futures
   paper puts the bends this pod fades in the part it expects to last.
2. [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C25-2|QP06-C25-2]]: arbitrage trades are "frequently constructed in the transition between the short- end and the long-end",
   the segment the pod targets; with C26-2 and C03-6 this weakens the case that anyone kept paying in 1990-2010, the
   pod's whole design sample.
3. [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C31-1|QP12-C31-1]]: differences of contract yields are "non-stationary as time gap increases" (the pod's measures span up to
   21 months); [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)#^QP12-C26-1|QP12-C26-1]]: anomalies of about 3 weeks survive the filter, so bad prints can pass R1's one-day test.

Open judgement points (not corrections; none is a decision for the user), with the step that closes each:
| # | Point | Closed at |
|---|---|---|
| 1 | Define the measures on contract (forward) rates, not on curve points built from them | pod spec 3.1 |
| 2 | Leftover roll exposure in the pairs: "most of the roll cancels" is not shown | pod spec 3.1 |
| 3 | Running a pod without a live source "outside the batch's error count" is not in WORKFLOW | registration 3.4 |
| 4 | [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] (2006) names Eurodollar futures as the way to trade it (C22-2): does that document the futures form before 2011? | thesis register 1.5 |
| 5 | R1 tests only gap size and one-day persistence; may need an outlier screen or a December-contract check | registration 3.4 |
| 6 | Whole-curve curvature is rejected without a version or diagnostic despite significant alpha after costs (C23-3) | thesis register 1.5 |
| 7 | Expiry-month groups pool month-ends at different times to expiry | pod spec 3.1 |
| 8 | Curve carry keeps two versions on the note's own argument; [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]] adds no quote support | pod spec 3.1-3.2 |
| 9 | The cost floor of half a bp per contract is borrowed from 2003 Treasury spreads | 3.1 / 3.4 |

Rule 5 (checker's knowledge, not in the pack): [[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)|QP06]] appeared in the Journal of Fixed Income in 2006; the underlying
three-part curve model in the Review of Financial Studies in 2008. No journal publication confirmed for [[QP07 - Predicting Short-term Eurodollar Futures (Chua, Ramaswamy, Stine; Rodney L. White Center 0|QP07]]; the [[QP12 - Modeling the Yield Curve (slides Stine, Chua, Ramaswamy)|QP12]]
slides are undated.

Usage: Fable 5.2 max, one run, about 0.65M tokens; Opus 5.5 high check, about 0.28M tokens.

