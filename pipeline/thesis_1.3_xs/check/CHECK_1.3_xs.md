# Independent check of thesis note 1.3b (value / momentum / carry; QP15, QP08), Opus 5.5, 2026-11-15

Checked file: fable_work/THESIS_1.3_xs.md (as of 2026-11-15 07:42). Ground truth: the verbatim "quote" fields of
pack/QP15.json (283 claims) and pack/QP08.json (142 claims), all read. Every claim id the note cites (169 citations,
104 distinct) was resolved with opus_work/lookup.py and opus_work/verify_note.py: all 104 exist, and every phrase the
note puts in double quotes occurs in the quote of a claim cited on the same line. No code, data or 2011-2026 results
were used.

## 1. Verdict

PASS WITH CORRECTIONS (22 required corrections, section 3).
- Numbers from the papers: 34 checked; 27 in quote (5 with a scope from claim text or exhibit field, correctly flagged; 2 with a scope misattributed: 1.8 to 3.1 to carry, "25 years" to value in general), 6 summary only and correctly tagged, 0 contradicted, 0 ids not found, 1 without a claim id (2013, sourced to the digest); the note's own arithmetic (52 of 304, 0.74) is right.
- Statements: 25 checked (14 table rows, 6 mechanism chains, 5 load-bearing claims elsewhere): 14 supported, 10 partly, 0 not supported, 1 contradicted ("No source runs trend with the class hedged": both papers run it).
- Pod grades: 1 of 3 changed. Value: from "moderate pooled" to weak (no per-class figure in a quote for any traded leg except bonds, which fail; survivorship, self-contradiction and rising cross-market correlation unmentioned). Carry weak and cross-sectional momentum weak stand.
- Main omissions: QP15's own doubt that behavioural models fit (C03-10, C53-3, C22-1), the only cited carry test (QP08-C05-1), the FX exception to daily trading (QP08-C13-1) and the momentum bias (QP08-C26-5); hidden choices remain in X1 (trailing window) and X2 (versions).

## 2. Findings

### Table A. Numbers taken from the papers

| # | Number in the note | Claim id | Verdict | Note |
|---|---|---|---|---|
| 1 | 0.42 | QP08-C17-1 | in quote | full sample 1990-Apr 2015, 52 sealed months; the verdict uses it although section 4 says it is not used (corr. 3) |
| 2 | 0.96 | QP08-C17-1 | in quote | as 1 |
| 3 | 1.8 to 3.1 | QP08-C13-3 | in quote, scope misattributed | the quote covers the three cross-asset styles; carry's own 3.1 is summary only; the note cites it for Carry (corr. 10) |
| 4 | 51% | QP08-C18-5b | in quote | directional form per exhibit field (flagged); full sample incl. 2011-15 |
| 5 | 25 years | QP08-C18-1 | in quote | equities per claim text; the note generalises to value (corr. 6, 7) |
| 6 | three years | QP08-C27-1 | in quote | |
| 7 | January 1990 | QP08-C09-4 | in quote | |
| 8 | April 2015 | QP08-C09-4 | in quote | |
| 9 | 1976 | QP08-C08-6 | in quote | |
| 10 | half (hedged) | QP08-C23-4 | in quote | |
| 11-14 | 0.75 / 0.28 / 1.27 / 1.25 | QP08-C21-3 | summary only | correctly tagged; nothing built on them |
| 15 | -0.60 | QP15-C17-1 | in quote | stocks per claim text (flagged) |
| 16 | -0.49 | QP15-C18-1 | in quote | non-stock classes per exhibit field (flagged); Table I correlations are of "residual returns from the benchmark" (QP15-C12-3b), not mentioned |
| 17 | -0.28 | QP15-C22-4 | in quote | stocks, lagged market value per claim text (flagged) |
| 18 | -0.53 | QP15-C22-4b | in quote | the quote's -0.53 is value in one stock market against momentum in OTHER stock markets; the claim text of C22-4 pairs -0.28 with a same-market -0.53; the note raises this in section 7 and builds nothing on it |
| 19 | 0.18 | QP15-C19-2 | in quote | bonds, 5-year yield change |
| 20 | 0.83 | QP15-C10-1 | in quote | U.S. stocks only, correctly scoped |
| 21 | -0.95 | QP15-C35-1 | in quote | average over all eight markets incl. stocks |
| 22 | 1.81 | QP15-C35-1 | in quote | as 21 |
| 23 | 24 basis points | QP15-C43-1 | in quote | meaning (liquidity premium) per claim text, flagged |
| 24 | 1998 | QP15-C51-4 | in quote | |
| 25 | 5-year, 10-year | QP15-C09-5 | in quote | |
| 26 | 12 months | QP15-C09-1b | in quote | |
| 27 | July 2011 | QP15-C07-2b | in quote | |
| 28 | 1972 | QP15-C06-4 | in quote | |
| 29 | 2012 | QP15-C04-5 | in quote | |
| 30 | 1985 | QP15-C09-6 | in quote | |
| 31 | 1990 to 2008 | QP15-C02-7 | in quote | years of six cited papers |
| 32 | Sharpe ratios and t-statistics by class | QP15-C14-2 to C15-4 | summary only | correctly tagged (quotes are row labels) |
| 33 | rival bond measures | QP15-C16-1 | summary only | correctly tagged |
| 34 | 2013 (QP15's year) | none (digest) | no claim id | the digest is named as source; checker's knowledge: Journal of Finance 2013 is correct |
| 35 | 52 of 304 months; 1 - 0.51 squared | (note's own) | arithmetic checked | 304 = Jan 1990-Apr 2015; 52 = Jan 2011-Apr 2015; 1 - 0.26 = 0.74 |

### Table B. Statements and labels

| Item | Note's label | Verdict | Reason (quote words) |
|---|---|---|---|
| Row 1 momentum better directionally | SHOWN | supported | "more than doubles its Sharpe ratio from 0.42 to 0.96" (QP08-C17-1); limits omit "we likely give a positive bias to momentum predictors" (QP08-C26-5) (corr. 5b) |
| Row 2 value cross-asset, poor directionally | SHOWN (words) | partly | words in QP08-C21-3; the limit's reason, "25 years ... was bound to underperform" (C18-1), concerns equities per claim text, not "one-way markets" in general |
| Row 3 carry alike in both forms | SHOWN (words) | supported | "carry works about equally well in both" (C21-3) |
| Row 4 algebra of the forms | ASSERTED (algebra) | supported | "weights are equal to time series weights minus the cross sectional average" (C21-4); the row's own limit is right but is ignored in section 1 and in Carry's grid (corr. 3, 11) |
| Row 5 value and momentum everywhere | SHOWN (words) | supported | "consistent and ubiquitous evidence" (QP15-C02-2); pooled with stocks, flagged |
| Row 6 bonds fail | SHOWN | supported | "only able to produce a Sharpe ratio of 0.18" (C19-2) |
| Row 7 value against momentum | SHOWN | supported | three numbers in quote; scopes from claim text, flagged |
| Row 8 recessions and funding | SHOWN (words) | supported | "significantly negatively related to recessions" (C28-7b); "only after 1998" (C51-4) |
| Row 9 tested risks do not explain value | SHOWN (words); logic ASSERTED | supported | "cannot explain why both value and momentum earn positive risk premia" (C34-2); pooled with stocks |
| Row 10 return chasing and flows | ASSERTED | partly | supported as asserted, but the row omits QP15's "not a prediction of existing behavioral models" (C03-10) and "difficult to reconcile under existing behavioral theories" (C53-3) |
| Row 11 carry by class | ASSERTED | supported | quotes as cited |
| Row 12 market factor gives carry no role | ASSERTED (derivation) | supported | "The sign of the forward bias is independent of carry" (C04-3) |
| Row 13 equity carry close to equity value | SHOWN | supported | "correlation is 51%" (C18-5b) |
| Row 14 value mirrors carry in C, K | ASSERTED | partly | C09-1 supports for currencies (a model); C14-4's literal words say deep value goes with "higher carry", the opposite reading unless "carry" means cost of carry; the cited Koijen result says carry is relatively "uncorrelated with factors such as value and momentum" (QP08-C05-1) |
| Chain Carry, common idea | reader | supported (as reader) | labelled reader; C03-3 shows only that forwards are biased |
| Chain Carry, currencies | ASSERTED | partly | C04-5 asserts a risk premium; "savers" are not in any quote, yet the verdict attributes them to QP08 (corr. 1) |
| Chain Carry, commodities | ASSERTED | supported | "producers selling futures to insure themselves" (C05-5); "incented by hedgers" (C05-7) |
| Chain Carry, bonds | pattern, no mechanism | supported | "Rates tend to roll down the curve" (C05-9) names no payer; but then the verdict's "thesis supplied" overstates (corr. 1) |
| Chain Value | ASSERTED | partly | pieces are asserted, but QP15 offers C04-6 and C04-8b to explain the liquidity loadings, not the premium (C34-2 says liquidity loadings deepen the value puzzle); assembly is the author's (corr. 12) |
| Chain cross-sectional momentum | ASSERTED / reader | partly | "separate from the cross-sectional momentum strategies we study here" (QP15-C04-4) is turned into "two forms, not two payers", which the quote does not say (corr. 15) |
| Verdict: CS momentum = Trend minus class average | (C21-4) | partly | exact only for positions proportional to one shared signal (claim text); Trend uses 1/3/6/12-month sign or capped shapes, CS momentum MOM2-12 rank |
| Carry grid: average = directional with half hedged | (row 4) | partly | the sign and rank versions are not proportional to the signal; if all carries are positive the sign version is all long and the rank version half long, half short; sign minus its mean is zero |
| Carry rivals: "none is tested" | reader | partly | QP08 cites a test: carry "is partially explained by recession and volatility risk" (C05-1) |
| "No source runs trend with the class hedged" | (C02-1) | contradicted | QP08 tests cross-sectional momentum on the same futures ("took long/short positions on the six most extreme assets", C12-3; Sharpe 0.42, C17-1); QP15 runs rank-weighted cross-sectional momentum (C10-4); C02-1 describes practice only |
| Section 4: the 25-year reason "for value" | ASSERTED | partly | equities per claim text of C18-1 |

### C. Evidence judgement

Grades:
- Carry, weak: consistent. One sellers' paper (Man Group), one in-sample run 1990-Apr 2015 (52 sealed months), gross of costs with daily trading (C09-6), styles chosen "because they have worked" (C02-4), survivorship "will likely favor value and carry" (C26-4), no carry figure in a quote. Add: QP08's FX carry (and FX value) results come from a different holding rule, "two exceptions" held a year (C13-1), so its FX evidence does not transfer directly to a monthly rule.
- Value, "moderate pooled": NOT consistent; change to weak. For the three legs the shop trades, the only figure in a quote is the bond leg's 0.18, which fails (C19-2, C19-1b). Index and currency evidence is words only and, in QP15, pooled with stocks. QP15's "in every asset class" (C01-1) is contradicted by its own bond result. Survivorship favouring value (QP08-C26-4) is cited for Carry but not for Value. Both groups sell the strategy. The rule-2 spirit (no grade above weak from summary-only figures) applies because the words "significant" rest on tables whose numbers are summary only.
- Cross-sectional momentum, weak: consistent; add the momentum bias QP08 itself names (C26-5).

Quotes that weaken or contradict a proposed pod or a reason the note gives, and that the note does not mention:
1. QP15-C03-10 "such correlation structure is not a prediction of existing behavioral models"; C53-3 "difficult to reconcile under existing behavioral theories"; C22-1 "these asset classes have different types of investors, institutional and market structures"; C18-3 (equity-built theories "may not easily apply to other asset classes"). Together they cut against the Value working reading (return chasing) exactly in the classes the shop trades.
2. QP08-C05-1 (citing Koijen et al.): carry is relatively "uncorrelated with factors such as value and momentum but is partially explained by recession and volatility risk". The only cited test across classes favours the risk rival for Carry and cuts against "Value is the opposite trade in currencies and commodities" (row 14). QP15-C04-5 dates this paper 2012 in a quote: no pre-2011 support.
3. QP15-C51-3 "(0.16 pre-1998 vs. 0.64 post-1998)" and C51-2 "has risen from 0.31 to 0.71" (value strategies across markets, pooled with stocks); C18-2 "small improvements in Sharpe ratios" from diversifying across classes; C22-2 market-neutral styles correlate across classes more than passive exposures. Value's three legs are closer to one bet in the second half of the design era than their count suggests, and the regime break sits inside 1975-2010.
4. QP08-C26-5 "we likely give a positive bias to momentum predictors": weakens row 1, which the note uses for directional-only Trend and against cross-sectional momentum.
5. QP08-C13-1 FX carry and FX value are "two exceptions" to daily rebalancing (held a year per claim text): the note's limit "daily trading" is incomplete for exactly the legs Carry and Value trade.
6. QP15-C12-3b: Table I value-momentum correlations (-0.49, -0.60) are of "residual returns from the benchmark", i.e. after removing each class's market, which supports the note's point that the hedge is shown only against the class-neutral part, but also means it is not a raw-return correlation.
7. QP15-C08-3: with recent prices "the value premium is slightly reduced" (the note cites C08-3 only for the correlation side); the shop's Value uses current prices.
8. QP15-C26-3b's bond path and QP08's chart reads are summary only and partly in 2011-15: correctly not used.
Supporting quotes the note does not use (for balance, not corrections): QP08-C15-4 "Remarkably, performance is consistently positive for value" (rolling chart incl. 2011-15, not usable for design); QP15-C18-6 ex ante volatility weights give "similar results" (mitigates the C49-3 look-ahead); QP15-C48-3 futures have "much lower trading costs than stocks"; QP15-C19-4b multiple value measures give "even more reliable risk premia" (supports Value's 2-version grid).
In-sample vs out-of-sample: both papers are single in-sample runs; QP15 claims uniform simple measures as a guard (C19-1) and splits sub-periods only for correlations (Table VII). Variants tried: QP08 "other configurations ... comparable" (C12-4), "some potentially creeps in from experience" (C26-3); QP15 reports three alternative bond measures beside the first choice (C12-2). The note states these.

### D. Rule specification

1. Carry and Value rules are precise only by reference to the engine (digest, signals.py and book.py lines). Left open in the note's own text: bond maturity for "bond yield", energy slope formula and sign, rank-to-weight map, ties and missing markets, the inflation measure and lag in Value's real yield. Acceptable for existing pods if the spec (3.1) copies the coded definitions; not checkable here (no code).
2. Value version 2, bonds: "5-year change" does not fix the lag (point 60 month-ends earlier, or QP15's 4.5-5.5-year average used for commodities and currencies). Fixed in corr. 19 to the literal reading.
3. Value version 2, currencies: expanding mean over all history to date, at least 60 months: no look-ahead; CPI base cancels in the deviation; release lags come from WORKFLOW section 5. Sign (cheap = real rate below its average) should be written in the spec.
4. X1: gate fixed (0.25 share, at least five earlier same-month values, both versions, per market, no signal before). Hidden choice: whether the trailing 12-month average includes the current month (corr. 17). The gate uses a full design-sample statistic of signals only (no returns): acceptable as a zero-slot diagnostic.
5. X2: hidden choice: whether the gate reads each version or the averaged position (corr. 18). The income formulas assume the engine's currency excess return includes the rate gap and that the bond yield used is the one in Carry's signal: not verifiable without code. The gate is a point estimate with no noise band (open point 5).
6. Cross-sectional momentum rule (not registered) is precise (MOM2-12, rank weights, monthly).

### E. Rules of the shop

1. Versions averaged, not picked: yes (Carry 2, Value 2, Trend per charter); "keeping it alone would be a pick" is the right logic.
2. No decision handed to the user: none found.
3. One mechanism per pod: Carry has three payers under one asserted idea (risk transfer), and its bond leg has no mechanism in the pack; the verdict calls the thesis "supplied" (corr. 1; open point 2). Value: one working reading with rivals kept apart: yes.
4. Model-uncertainty reason per dimension: Carry form (which part is paid), Value anchor (fair value unobservable; papers differ): stated; "No gain is expected" for Value version 2 is explicit.
5. Data table against pack/DATA_AVAILABILITY.md: agrees (engine 1975, 3-month rates, consumer prices; LSEG dividend yields 1973, bond yields 1979-12; no index book-to-price, no consensus forecasts). "No curve depth for a one-year contract" overstates the sheet, which states no depth at all (corr. 20).
6. Live source flags: the sheet says the engine (Carry and Value included) runs live every week on free data, so live sources exist by implication; the note flags the inputs the sheet does not list and passes them to the code check. No pod needs a not-Core-eligible flag on the pack's evidence; X1 and Value version 2 add no new inputs.
7. Rule 5 dating: supported by the pack (QP15 undated, sample to July 2011, cites 2012; QP08 sample to April 2015). Checker's knowledge, marked:
   - QP15: Asness, Moskowitz and Pedersen, "Value and Momentum Everywhere", Journal of Finance 68(3), 2013 (checker's knowledge, certain). Earlier working-paper versions existed; I cannot certify their date or asset coverage (checker's knowledge, uncertain).
   - QP08: Baz, Granger, Harvey, Le Roux and Rattray, "Dissecting Investment Strategies in the Cross Section and Time Series", SSRN working paper, 2015 (checker's knowledge); I know of no journal publication with certainty.
   - Pre-2011 sources (checker's knowledge, certain): Keynes, A Treatise on Money (1930), normal backwardation; Fama (1984), Journal of Monetary Economics, forward premium in currencies; Fama and Bliss (1987), American Economic Review, forward spreads and bond excess returns; Lustig and Verdelhan (2007), American Economic Review (cited in QP08-C04-5, year only in claim text); Erb and Harvey (2006), Financial Analysts Journal (in the quote of QP15-C02-7 for commodity momentum); Gorton and Rouwenhorst (2006), Financial Analysts Journal; Asness, Liew and Stevens (1997), Journal of Portfolio Management, value and momentum across country equity indexes (named only in the claim text of QP15-C02-7). The last is the strongest candidate to date the Value thesis for the index leg before 2011; step 1.5 must read it.
   - The author's "Keynes 1930, Fama 1984, Fama and Bliss 1987" are correct as dates (checker's knowledge).

### F. Asset-class scope and the three questions

1. Scope is kept apart in the table (S flagged in rows 5, 7, 9; QP08 has no stocks, correctly I, B, C, K). Two lapses: the verdict's "funding-liquidity risk has the wrong sign" is pooled with stocks without saying so (corr. 4); QP15-C51-3's correlation rise is pooled (corrections that cite it say so).
2. Carry thesis: partly supported. Commodities: asserted payer in quotes. Currencies: risk premium asserted; payer (savers) is the author's. Bonds: no payer in the pack. Grade weak is right.
3. Value thesis: payer not established, honestly stated; the working reading must face QP15's doubt about behavioural theories (corr. 13). Grade weak (corr. 2, 14).
4. Cross-sectional momentum against Trend: the algebra (C21-4) supports "relative part of a directional book" only approximately for the engine's Trend; rejection as a separate pod (shared mechanism) is supported as reader; rejection as a Trend version rests on a risk-shape argument (removes the class-wide position) that is the author's, plus full-sample Sharpe ratios that include sealed months (open points 1, 3).
5. Directional against cross-asset: rows 1-3 are in quote or words; registration (Trend directional, Carry both, Value cross-asset) follows from the note's reasoning; the Trend part leans on QP08 numbers the note says it does not use (corr. 3).

## 3. Required corrections

1. Section 1, Carry line.
- Find: `**Carry: thesis supplied in three parts, grade weak on this pack.** Payers: savers who want safe currencies and hedgers of commodities (QP08, asserted); borrowers who fix long rates (reader: QP08 names no payer for bonds).`
- Replace: `**Carry: thesis supplied for currencies and commodities (asserted), not for bonds (pattern, no mechanism in the pack); grade weak on this pack.** Payers: hedgers of commodities (QP08, asserted); for currencies QP08 asserts a risk premium (QP08-C04-5) and the savers who pay it are my reading (reader); borrowers who fix long rates (reader: QP08 names no payer for bonds).`
- Reason: QP08-C04-5 quote "low-yielding currencies hold their own in low domestic consumption states" names no saver; QP08-C05-9 "Rates tend to roll down the curve" names no payer, so the bond leg is "pattern, no mechanism" by the brief's rule.

2. Section 1, Value line (grade).
- Find: `Pattern moderate (two papers agree in words); payer not established.`
- Replace: `Grade weak: the pattern rests on words in two sellers' papers; the only per-class figure in a quote is the bond leg's 0.18, which fails (QP15-C19-2), and survivorship "will likely favor value and carry" (QP08-C26-4); payer not established.`
- Reason: QP15-C19-2 "we are only able to produce a Sharpe ratio of 0.18"; QP08-C26-4 "This kind of bias will likely favor value and carry"; all index and currency figures are summary only (QP15-C14-2 to C15-4 quotes are row labels).

3. Section 1, cross-sectional momentum line.
- Find: `It is what is left of Trend once each asset class's average position is removed (QP08-C21-4). No payer of its own; the weaker form (Sharpe 0.42 against 0.96, QP08-C17-1).`
- Replace: `Roughly, it is what is left of Trend once each asset class's average position is removed (QP08-C21-4; exact only for positions proportional to one shared signal, claim text; our Trend uses other lookbacks and sign or capped shapes, reader). No payer of its own; QP08 finds it the weaker form (Sharpe 0.42 against 0.96, QP08-C17-1, over 1990 to April 2015 including 52 sealed months, so not a design-era fact).`
- Reason: QP08-C21-4 "cross sectional portfolio weights are equal to time series weights minus the cross sectional average" holds for linear signals (claim text "With linear signals"); section 4 of the note says "I use its logic (row 4), not its Sharpe ratios", yet the verdict cites QP08-C17-1 "from 0.42 to 0.96".

4. Section 1, weakest link.
- Find: `The risks the authors test do not explain it; funding-liquidity risk has the wrong sign (QP15-C03-4, C34-2).`
- Replace: `The risks the authors test do not explain it; funding-liquidity risk has the wrong sign (QP15-C03-4, C34-2; pooled with individual stocks); and the authors find the cross-asset pattern "difficult to reconcile under existing behavioral theories" (QP15-C53-3), which cuts against the working reading too.`
- Reason: QP15-C03-4 "globally across asset classes" pools the four stock markets; QP15-C53-3 "difficult to reconcile under existing behavioral theories" is unmentioned and bears on the behavioural working reading.

5. Section 2, limits common to all rows (QP08 trading).
- Find: `before costs (C09-6); daily trading (C21-1);`
- Replace: `before costs (C09-6); daily trading (C21-1), except FX carry and FX value, the "two exceptions" held about a year (C13-1; holding rule per claim text);`
- Reason: QP08-C13-1 "{FX, carry} and {FX, value} are two exceptions here because mean reversion in FX is slower"; these are the legs Carry and Value trade.

6. Section 2, row 1 limits.
- Find: `no test of the gap; holds "to the extent that the global factor is trending" (QP08-C22-1)`
- Replace: `no test of the gap; holds "to the extent that the global factor is trending" (QP08-C22-1); markets that grew since 1990 mean "we likely give a positive bias to momentum predictors" (QP08-C26-5, claim text for the cause); 52 of 304 months sealed`
- Reason: QP08-C26-5 "we likely give a positive bias to momentum predictors" weakens the row the note uses for directional-only Trend.

7. Section 2, row 2 limits.
- Find: `authors blame one-way markets (QP08-C18-1)`
- Replace: `authors blame trending global factors (QP08-C22-4); the "25 years" reason (QP08-C18-1) is about equities (claim text)`
- Reason: QP08-C22-4 "major global factors have exhibited very strong trends which have by definition hurt reversion based value predictors"; the claim text of C18-1 ties "25 years" to stocks trending up (Table 5 equity value).

8. Section 2, row 14 limits.
- Find: `| C, K | a model; correlations summary only |`
- Replace: `| C, K | a model; correlations summary only; the quote's "higher carry" reads as the cost of carry (contango), i.e. lower carry for a holder (reader, from the footnote formula of QP08-C14-5b; section 8 item 3); the carry paper QP08 cites finds carry relatively "uncorrelated with factors such as value and momentum" (QP08-C05-1) |`
- Reason: QP08-C14-4 "a low spot price (revealing deep value) goes hand in hand with a lower convenience yield (or higher carry" literally pairs deep value with higher carry; QP08-C05-1 "uncorrelated with factors such as value and momentum".

9. Section 3, Carry rivals.
- Find: `The predictions are mine (reader); none is tested.`
- Replace: `The predictions are mine (reader); none is tested here. The one cited test across classes leans to risk: carry "is partially explained by recession and volatility risk" (QP08-C05-1, words only; the paper is dated 2012 in QP15-C04-5).`
- Reason: QP08-C05-1 "partially explained by recession and volatility risk"; QP15-C04-5 "Koijen et al. (2012) document global carry returns".

10. Section 3, Carry stops working.
- Find: `QP08 reports drawdowns "of order 1.8 to 3.1 times the volatility" (QP08-C13-3)`
- Replace: `QP08 reports cross-asset drawdowns "of order 1.8 to 3.1 times the volatility" across its three styles (QP08-C13-3; carry's own figure is summary only)`
- Reason: QP08-C13-3 "maximum drawdowns per style are of order 1.8 to 3.1 times the volatility" covers value, carry and momentum; carry's -3.1 is in the reported_result field only.

11. Section 3, Carry grid.
- Find: `By row 4 the average is roughly directional carry with half its class-wide position hedged.`
- Replace: `Row 4 is exact only for positions proportional to the signal; a sign version and a rank version are not, so the average is a mix of the two forms, not exactly directional carry with half its class-wide position hedged (reader; section 7 item 3).`
- Reason: QP08-C23-4 "the combined portfolio is just the time series portfolio with half of the cross sectional mean hedged out" rests on C21-4, linear signals per claim text; with all carries positive the sign version is all long while sign minus its mean is zero.

12. Section 3, Value chain label.
- Find: `**Chain, working reading (ASSERTED).**`
- Replace: `**Chain, working reading (reader, assembled from ASSERTED pieces: QP15 offers C04-6 and C04-8b to explain the liquidity loadings, not the value premium; C05-1 is a cited model whose size "remains an open question", C05-4b).**`
- Reason: QP15-C34-2 "cannot explain why both value and momentum earn positive risk premia"; C04-6 and C04-8b sit in the crowding story for liquidity exposure; QP15-C05-4b "matching the magnitude of our empirical findings remains an open question".

13. Section 3, Value chain, behavioural doubt.
- Find: `The crowd keeps paying because money follows past returns; whether that is big enough is open (row 10).`
- Replace: `The crowd keeps paying because money follows past returns; whether that is big enough is open (row 10). QP15 adds that "such correlation structure is not a prediction of existing behavioral models" (QP15-C03-10) and is "difficult to reconcile under existing behavioral theories" (C53-3), since the classes have "different types of investors, institutional and market structures" (C22-1).`
- Reason: QP15-C03-10, C53-3 and C22-1 quotes as given; unmentioned and they weaken the working reading in the classes traded.

14. Section 3, Value grade.
- Find: `- **Grade.** Pattern: moderate pooled (two groups, different measures and samples, agree in words; QP15 kept`
- Replace: `- **Grade: weak.** Pattern: two groups, different measures and samples, agree in words, pooled; QP15's "in every asset class" (C01-1) fails for bonds in the same paper (C19-1b); survivorship "will likely favor value and carry" (QP08-C26-4); value strategies moved together far more after 1998, "0.16 pre-1998 vs. 0.64 post-1998" (QP15-C51-3, pooled with stocks), so the legs diversify less than their count suggests (QP15 kept`
- Reason: QP15-C19-1b "our weakest results pertain to bonds, which do not produce statistically reliable premia"; QP08-C26-4 "will likely favor value and carry"; QP15-C51-3 "(0.16 pre-1998 vs. 0.64 post-1998)"; no figure for an index or currency leg is in a quote.

15. Section 3, cross-sectional momentum chain.
- Find: `two forms, not two payers.`
- Replace: `QP15 calls them separate and says nothing of payers; that they share Trend's payer is my reading (reader).`
- Reason: QP15-C04-4 "which is separate from the cross-sectional momentum strategies we study here" says separate; it does not address payers.

16. Section 3, cross-sectional momentum, not a Trend version.
- Find: `No source runs trend with the class hedged: "in futures trading, momentum is typically applied directionally" (QP08-C02-1).`
- Replace: `In practice futures momentum is run directionally: "in futures trading, momentum is typically applied directionally" (QP08-C02-1); both papers test the hedged form only as research (QP08-C12-3, QP15-C10-4).`
- Reason: QP08-C12-3 "took long/short positions on the six most extreme assets (three on each side)" applies to momentum too (QP08-C17-1 "from 0.42"); QP15-C10-4 "weight securities in proportion to their cross-sectional rank"; C02-1 describes practice only.

17. Section 5, X1 gate (trailing window).
- Find: `of the signal minus its trailing 12-month average.`
- Replace: `of the signal minus its trailing 12-month average (the 12 month-ends up to and including that month-end, as in QP08's "1Y moving average", QP08-C10-2).`
- Reason: hidden choice in the gate; QP08-C10-2 "the average difference between the raw carry and its 1Y moving average" is the model.

18. Section 5, X2 gate (versions).
- Find: `- Gate: a price part of zero or less enters the leg`
- Replace: `- Gate: computed on the leg's averaged position (equal-weight average of its versions, as traded), over all design months in which the leg holds a position; a price part of zero or less enters the leg`
- Reason: the computation is "per Value leg ... and version" but the gate does not say which result decides when versions disagree: a hidden choice.

19. Section 3, Value rule, version 2 bond measure.
- Find: `"the 5-year change in the yields of 10-year bonds" (QP15-C09-5);`
- Replace: `"the 5-year change in the yields of 10-year bonds" (QP15-C09-5; today's yield minus the yield 60 month-ends earlier, long the largest rise; the exact lag is not in the quote, reader);`
- Reason: hidden choice; QP15-C09-5 "similar to the negative of the past 5-year return" fixes the sign, not the lag (QP15-C09-3 uses a 4.5-5.5-year average for commodities).

20. Section 8, item 7.
- Find: `no curve depth for a one-year contract,`
- Replace: `no stated curve depth (the sheet gives start years, not whether a contract one year out exists),`
- Reason: pack/DATA_AVAILABILITY.md says "futures curves from 1973 (grains, softs, metals), WTI 1983, Brent 1988, natural gas 1990" and is silent on depth; QP08-C10-3 "the contract exactly expiring one year later".

21. Section 4, value reason.
- Find: `and for value "25 years, the value factor`
- Replace: `and for equity value (claim text) "25 years, the value factor`
- Reason: QP08-C18-1 exhibit Table 5; claim text "Equity value in time series had negative Sharpe (-0.13) since stocks trended up 25 years".

22. Section 9, last bullet.
- Find: `- **Against grading Value's pattern moderate.** Its by-class numbers are summary only and both groups sell it.`
- Replace: `- **For grading Value above weak.** Two groups with different measures and samples report the cross-asset pattern in words; if the by-class tables (summary only) are right, the pooled pattern is moderate.`
- Reason: follows corrections 2 and 14 (grade now weak); QP08-C21-3 "value works well in the cross section" and QP15-C02-2 "consistent and ubiquitous evidence" are the case for a higher grade.

## 4. Open judgement points (not corrections)

1. Whether QP08 full-sample figures (52 of 304 months sealed) may support design choices at all (equity carry out via 51%, Trend directional via 0.42 and 0.96): closes at thesis register 1.5 and registration 3.4.
2. Carry's bond leg has no mechanism in the pack: keep it in the pod as pattern, or require a dated source at 1.5 before it counts for the Carry thesis: 1.5 and spec 3.1.
3. Asymmetry: Carry registered in both forms on doubt about which part is paid, Trend directional only; consistent only if Trend's thesis is specifically about class-wide moves: spec 3.1-3.2.
4. The book holds Value with directional Trend, not with cross-sectional momentum; QP15's immunity of the 50/50 mix to funding shocks (C34-4) may not carry over: report in A2 (note's point iii), registration 3.4.
5. X2's gate is a point estimate (price part at or below zero) with no noise band: registration 3.4.
6. Placebo test for existing pods, Carry's directional bond leg as a standing long position (note's item 6): registration 3.4.
7. Rule 5: Asness, Liew and Stevens (1997) may date value and momentum in country indexes before 2011; Fama (1984) and Fama and Bliss (1987) date the carry patterns in currencies and bonds (checker's knowledge): thesis register 1.5.
8. Excluding equities from Carry rests on a directional 51% correlation; the cross-asset overlap is unknown: spec 3.1.
9. Commodities left out of Value on the mirror argument while currencies, where the same model applies (QP08-C09-1), stay in: spec 3.1 (the note's self-check names it).

## 5. What I could not verify

- Engine facts (no code reading): bond maturity in Carry and Value, inflation measure and release lag in Value's real yield, whether the currency value measure is QP15's, whether energy carry is already calendar-adjusted, whether the engine's currency excess return includes the rate gap, rank-to-weight maps.
- Date and asset coverage of QP15's first circulated version; any journal publication of QP08.
- Whether LSEG energy curves hold a contract one year out over the design era; LSEG licence terms for trading use.
- The Koijen et al. figures behind QP08-C05-1 (not in the pack).
- Any per-class figure of either paper (summary only by construction of the pack).
