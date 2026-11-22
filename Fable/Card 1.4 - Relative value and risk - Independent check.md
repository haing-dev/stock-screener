---
tags: [fable, thesis]
code_commit: 5c79343
---
> Opus 5.5 high, against the verbatim quotes. See [[Card 1.4 - Relative value and risk]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/5c79343e5cc571c6958ef38b7000b6ec1c6bdd02/docs/research/fable/CARD_1.4_relative_value_risk_check.md).
# Independent check of playbook card 1.4 (3 of 5): macro relative value and risk (Graham Capital, Elliott)

Checker: Opus (quant and risk officer), 2026-11-22. Read: the card in full; all 361 quotes of pack/CLAIMS.json (with claim text for every id the card cites); WORKFLOW_sections_1-6.md, BRIEF_V2_RULES.md, DATA_SHEET.md, FORECASTS.csv (all 99 rows, resolved rows re-tallied by script), SOURCES.md, DIGEST.md; the author's brief. All 125 ids in the card looked up: 112 claim ids exist with the speaker and period the card gives; the 13 others are 7 ledger row ids (V-ids) and the six missing ledger claim ids that pack problem 1 names correctly. No code, no backtest, no web.

## 1. Verdict

PASS WITH CORRECTIONS.
1. Numbers: about 45 checked (table in A); 30 in quote and used correctly, 3 tagged summary-only correctly, 9 ledger figures reproduced exactly (15 of 40, 12.6, 10 of 17, six from 2022, 0 of 7, 1 of 10, 4 of 6, the 2022 FEDFUNDS rows), 4 rest on claim text for their meaning (the 100 bp slope, the 10% team correlation, the period of the 22 moves, 4.75 read from a garbled caption), 1 not in the pack (forward EPS "from 1985"); 0 contradicted.
2. Chains and attributions: 7 chains, quotes say what is claimed in all 7; 5 overstatements: Singer's "loss" and "before it closes" (C7), the "SHOWN" label on Singer's process rows, team correlation, pooling Singer's stock rows into Calderini's claim.
3. Rules: 4 rules, directions supported by the quotes; 1 premise problem (R3 measure 1 cannot be on at its own source case and is negative carry by construction), 3 hidden choices (R1 series splice and live source, R2 duration, question 6/8 units), R1 inputs are research-only series.
4. Dating table: right on every row (the one pre-2011 date, "in 1998", is in the quote). Shop rules: no decision for the user; versions averaged; F2 and F7 rest on claim text; 4 analyst questions need a tighter scoring rule; the card runs 4,730 words against a 3,000-4,000 budget.
5. 41 required corrections (section 3), all applied to the preview; none changes the rule count, the version count or a hindsight flag.

## 2. Findings A to F

### A. Numbers

| Number in the card | Source | Status |
|---|---|---|
| 361 claims, 11 recordings, 10 Graham + 1 Elliott | SOURCES.md, CLAIMS.json | correct |
| 13 moves in 11 years, 60 in 36 months | [[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C02-1|MT214-C02-1]] | in quote |
| 13 hikes in 11 years (2022 telling) | [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C01-2|MT066-C01-2]] | in quote |
| "1325" basis points | [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C03-4|MT089-C03-4]] | in quote (13 and 25 run together); pack problem 7 correct |
| 22 changes; 76 since 2022 | [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C01-1|MT092-C01-1]] | in quote; the period "2010-21" for the 22 is claim text (card says "in quote"): correction 33 |
| about 100 bp average since 1990, as high as 300 | [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C01-3|MT092-C01-3]] | in quote; that it is the 2-to-10-year slope is claim text. Card says so in section 12 but uses 1.0 as "his figure" in R2: correction 11 |
| 100 bp inverted, now about 60 | [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C08-1|MT089-C08-1]] | in quote ("two1" read as 2s10s is plausible, claim text says 2s10s) |
| 4.75 then 4.25 | [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C04-X1|MT066-C04-X1]] | "four and a quarter" in quote; 4.75 is a reading of "4-3 now for uh 75": correction 35 |
| forward P/E just under 19; normal 16 or 17; 4 or 5% | [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C07-2|MT089-C07-2]], [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C07-3|MT089-C07-3]] | in quote ("RIS stre" read as risk-free: plausible) |
| gap 0.3 to 1.3 | reader arithmetic | correct (100/19 = 5.26; minus 5 = 0.26, minus 4 = 1.26) |
| P/E 24 a half | [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C02-2|MT092-C02-2]] | in quote (cited, not used as a number) |
| 300 bp above pricing | [[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C03-2|MT113-C03-2]] | in quote |
| minus 2% a year for 7 years | [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-2|MT122-C04-2]] | in quote |
| 25 years without duration premium; 1980; 5% bid | [[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C07-2|MT214-C07-2]], [[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C07-3|MT214-C07-3]], [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C06-4|MT092-C06-4]] | in quote |
| stock-bond correlation 40% | [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C02-3|MT092-C02-3]] | in quote |
| 10% "between teams" | [[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C06-1|MT214-C06-1]] | number in quote ("it used to be on average 10%"); the referent is claim text: corrections 19, 34 |
| two thirds of three quarters | [[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C03-3|MT214-C03-3]] | in quote |
| one to two months, maybe three | [[MT062 - Global Macro- Discretionary vs. Systematic - Who Wins- - Global Alts 2025 - Pablo Calderin#^MT062-C03-4|MT062-C03-4]] | in quote; it is the QUANT programs' horizon: correction 30 |
| 22 to 25 teams; 25% discretionary | [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C01-2|MT092-C01-2]], [[MT062 - Global Macro- Discretionary vs. Systematic - Who Wins- - Global Alts 2025 - Pablo Calderin#^MT062-C01-X2|MT062-C01-X2]] | in quote |
| two percent target | [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C04-2|MT066-C04-2]] | in quote |
| minus 0.5 correlation | [[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C04-4|MT113-C04-4]] ("minus 50") | in quote |
| 2010-20 anomaly | [[MT067 - Graham's 2022 Virtual Investment Symposium- Discretionary Strategies Panel#^MT067-C10-2|MT067-C10-2]] | in quote; F6 resolves on 2010-19: correction 41 |
| 30% fall 2008, 88% loss 1974, risk meeting since 2007 | [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-3|MT122-C04-3]], [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C05-1|MT122-C05-1]], [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C06-1|MT089-C06-1]] | summary only, correctly tagged and unused |
| Ledger: 15 of 40, base 12.6; rates 10 of 17 (6 from 2022); stocks 0 of 7; currencies 1 of 10; other 4 of 6 | FORECASTS.csv | reproduced exactly (base sum 12.58). The tallies include five rows the card itself disputes; without them 15 of 35, base 10.8: correction 36 |
| Three 2022-09 FEDFUNDS rows scored on one move (2.33 to 5.33) | MT067-V001-2, V010-1, V017-2 | correct |
| Steepener rows: 2022 +0.14, 2023 +0.20 (band 0.25, wrong); 2024 right | MT066-V002-2, MT089-V004-1, MT133-V002-2 | correct, but the 2024 row is Calderini's and its steepener is view text: correction 13 |
| Equity rows 2023 and 2025 both wrong (R4) | MT089-V002-1, MT092-V001-1 | correct |
| Forward EPS "from 1985" | not in the pack (DATA_SHEET gives no start) | not found: corrections 16, 17 |
| Bands F1 0.25, F2 0.10, F7 2% | ledger band column | match the ledger's bands for those series |
| 16 versions (8+2+4+2), 32 with sizing | card | arithmetic correct |
| Reader grids (gate 0.50, L 6/12, bars 3.0/4.0, 1.0/0.0, D1 0.80/0.50, D2 60) | card | reader's, each with a stated reason |

### B. Causal chains and indicators

- C1 to C6: every quoted phrase is in its claim, by the named speaker; dates match the ledger's made dates ([[MT067 - Graham's 2022 Virtual Investment Symposium- Discretionary Strategies Panel|MT067]] 2022-09, [[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini|MT113]] 2023-03, [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive|MT089]] 2023-04, [[MT121 - Optimizing Investment Alpha with Customized Completion Portfolios Featuring Chris Jones, P|MT121]] 2021-11 inferred). Labels are fair. Minor, no correction: "a colleague" ([[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C05-2|MT214-C05-2]]: "he said") and "earlier cycles" ([[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C03-1|MT113-C03-1]] says "always ... for the first 18 months") lean on claim text; C2 lists [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C01-3|MT066-C01-3]] as an application of the rule, but that quote only says divergence is "good for macro Trading".
- C7 overstates: the quotes give the price ("minus 2% inflation per year for 7 years"), daily marks, a crowded dealer and "I kept the trade". The loss, its size, the instrument, the year and the leverage are claim text, and NOTHING in quote or claim text says the gap later closed. The heading "widens the gap before it closes", "the winner" and verdict line 4 "Singer's worked loss (SHOWN, one case)" go beyond the pack (corrections 2, 6, 7). Note also that the C04 cluster mixes two Singer cases: [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-1|MT122-C04-1]] is a bankruptcy claim, so "lever something up" ([[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-4|MT122-C04-4]]) need not belong to the linker trade.
- Speakers kept apart: mostly yes. Two lapses: the stock-ledger line pools Singer's two equity rows with Graham's under Calderini's claim (correction 32) and verdict line 5 (correction 3); the steepener ledger line counts Calderini's row as Tropin's rule (correction 13). Firm framework and personal views are kept apart well (C1 "firm-level", section 6 who-columns).
- Indicators table: every series named is on the data sheet. But the R1 inputs (IR3TIB01 rates, EX currencies) sit under "More FRED series fetched for research", not the live list; the live cycle has only FXY, FXF, FXE, UUP, DX-Y.NYB for currencies and no foreign short rate (correction 40). Lags for Compass indicators are not given on the sheet; the card's 0 is an assumption.

### C. Rules

- R1 Hawkish currency. Direction supported ([[MT090 - Ken Tropin on Macro Hive Podcast- Markets, Risk, AI-Driven Technology, and What Comes Next#^MT090-C07-1|MT090-C07-1]]). Hidden choices: (a) splice between FRED 3-month series and LSEG deposit rates where FRED starts late (correction 8); (b) the US leg uses a T-bill rate (TB3MS) against interbank rates abroad, so a flight to T-bills (e.g. 2008) moves the US change against the others (open point 2); (c) shape B shorts the smallest-change currency twice when the dollar has the largest change (equal-risk basket includes it): acceptable, but it should be stated in the spec. No live source for any input on the free cycle (correction 40). "Hawkish" in the pack is perception ([[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C07-5|MT089-C07-5]] "the perception is the ECB is now more hawkish"); the card already says delivered is not promised. Economic trend duplication cannot be checked from the pack (section 5).
- R2 Steepener. Direction right (long 2-year, short 10-year gains when the slope widens). The bar 1.0 is a number in quote whose meaning (2s10s) is claim text, so under v2 rule 3 it can only be a reader's version (correction 11). DV01 sizing needs a duration for each leg; the panel holds excess returns, not durations, so the formula must be fixed now (correction 12). The self-check line "while the curve is inverted the position costs carry" is labelled reader; its sign depends on curve shape (per unit of duration the 2-year leg can out-carry the 10-year leg), so leave it to D1 / step 3.1, no correction.
- R3 Cuts priced too early. Direction right (short the 2-year against easing he doubts, [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C02-5|MT066-C02-5]], [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C08-3|MT089-C08-3]]). PREMISE PROBLEM: in Tropin's own example the curve still prices a rise to 4.75, so GS2 is above FEDFUNDS and measure 1 (FEDFUNDS minus GS2) is negative: R3 cannot be on at its source case of October 2022; it fires only after the last hike is priced (as in 2023). And whenever measure 1 is on, the 2-year yields at least 0.50 below cash: negative carry by construction, so a directional Carry rule holds the same short and R3 adds only the inflation filter (corrections 14, 15). Self-check "Card 1's trade of 2000 ... a similar state": in 2000 core inflation was low, so R3 would be off; "similar" is loose (reader's knowledge; no correction).
- R4 No alternative. Arithmetic right; direction supported; "from 1985" not in the pack (corrections 16, 17); source LSEG, flagged correctly.
- Common block: state rules with no tail are justified by the quant programs' horizon, not the discretionary one (correction 30); otherwise consistent with cards 1 and 2. No look-ahead found in the rule formulas themselves (expanding mean in R2; PCEPILFE first published, lag 2); the activity gate and the 1.0 bar were chosen knowing 2010-25, and the card says so (D2, expanding-mean version).

### D. All 361 quotes: contradictions, omissions, attributions, duplicates

Contradicting the card:
1. McCann: "in times of the higher correlation we actually have a higher information ratio among our PMS" ([[MT067 - Graham's 2022 Virtual Investment Symposium- Discretionary Strategies Panel#^MT067-C05-2|MT067-C05-2]]). The card lists crowding ([[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C06-X2|MT214-C06-X2]]) as a condition under which the playbook "should stop working"; the firm's risk officer says high correlation between PMs comes with a HIGHER information ratio. The two Graham statements disagree; the card shows only one (correction 31).
2. F2 credits Tropin with "no further Fed cuts in 2026". The quote reports "some people"; his own words in the same recording point to cuts: "there's going to be an enormous pressure on the new chair to to really stimulate the economy" ([[MT090 - Ken Tropin on Macro Hive Podcast- Markets, Risk, AI-Driven Technology, and What Comes Next#^MT090-C06-2|MT090-C06-2]]), "a lot of pressure from the administration to get rates lower" ([[MT090 - Ken Tropin on Macro Hive Podcast- Markets, Risk, AI-Driven Technology, and What Comes Next#^MT090-C04-X1|MT090-C04-X1]]) (correction 26).
3. Pack problem 3 calls [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C04-X1|MT066-C04-X1]] a description of the market. The quote continues "and then I think we start to see that ease back down in the middle of 23 to maybe four and a quarter": it can be his own view, and his "I'm skeptical" ([[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C02-5|MT066-C02-5]]) is about easing at the END of 2023. Ambiguous, not clearly miscoded (correction 37).

Important ideas omitted:
4. Tropin on decay: "there's no way you can do what worked 10 years ago and expect it to always work in the future" ([[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C06-3|MT089-C06-3]]; also [[MT090 - Ken Tropin on Macro Hive Podcast- Markets, Risk, AI-Driven Technology, and What Comes Next#^MT090-C02-2|MT090-C02-2]]), and markets were "less efficient then" ([[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C01-5|MT066-C01-5]], [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C01-2|MT089-C01-2]]). The source himself expects rules to decay: the strongest "should stop working" line for four rules built on 2022-25 views (correction 31).
5. Graham's own quant side is trend, value and carry ("one is based on Trend the other one is based on value or long-running reversion the other one is based on Curry", [[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C08-3|MT113-C08-3]]; "yield and carry, relative value", [[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C04-2|MT214-C04-2]]), and "If they're trends, usually you're doing pretty well" ([[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C03-4|MT214-C03-4]]). So the firm's "relative value" is largely our Value and Carry pods, and its results ride Trend: the title theme adds less than the verdict implies (correction 1).
6. Tropin's application of his own currency rule in the same December 2025 recording: "Japan is the most hawkish that I can remember" ([[MT090 - Ken Tropin on Macro Hive Podcast- Markets, Risk, AI-Driven Technology, and What Comes Next#^MT090-C06-4|MT090-C06-4]]). No currency call in the quote, but it is the live case for R1 and question 2 (correction 39).
7. Singer also cites the deficit (over 6% of GDP, [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C07-4|MT122-C07-4]]) without a trade: parallel to C4, kept apart correctly by omission; no correction.

Attribution: no statement of one speaker is given to another. Pooling across speakers in ledger counts: corrections 3, 13, 32.

Duplicates: R2's short-10-year leg overlaps card 2's R1 (card says so); R3 measure 1 duplicates directional bond Carry by construction (above); R1 may duplicate Economic trend for currencies if its inputs include short-rate changes (cannot verify; section 5); R4 does not duplicate cards 1-2 (card 2's R2 is a yield-rise trigger, card 1's R4-B an inflation level). The "not rules" paragraph (2022 positions = Trend / Economic trend) is consistent with the digest. Graham and Elliott are otherwise kept apart (Singer appears only in C6, C7, section 6 and F-context).

### E. Dating table

Every row checked against its quote. Only "Mix quant and discretionary" has a pre-2011 date in the words ("in 1998", [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C01-1|MT089-C01-1]]): correct. C4's 1980 recollection is clients' losses, not his trade: correct. C7 year is claim text: correct. C2 is first STATED 2025-12 but first APPLIED 2023-04 ([[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C07-5|MT089-C07-5]]): no effect on the flag (correction 38). Other pre-2011 recollections in the pack ([[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C03-2|MT089-C03-2]] CTA long bonds, undated in the quote; [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C03-4|MT122-C03-4]] convertible hedging, years claim text; [[MT067 - Graham's 2022 Virtual Investment Symposium- Discretionary Strategies Panel#^MT067-C03-1|MT067-C03-1]] "mid 90s") carry no rule. Every signal thesis correctly hindsight-flagged.

### F. Rules of the shop

- No decision handed to the user: none found.
- Versions averaged: stated for all rules and the sizing version.
- Open choices: all are versions or diagnostics with fixed gates, except the hidden choices listed in C (corrections 8, 12, 24, 25).
- Analyst questions: Q2 is not scoreable for sterling, Canadian dollar and krona on the free sheet (correction 22); Q4 on weekly returns gives 4 points at the 4-week horizon (correction 23); Q6 and Q8 lack a unit (corrections 24, 25). Q1 on FEDFUNDS (a monthly average) is scoreable but slow to show a late-month cut; acceptable.
- Forecasts: all seven are open as of 2026-11-22 by their stated windows. F2 and F7 rest on claim text (corrections 4, 26). F3 and F4 needed a band / a no-trigger rule (corrections 27, 28, 29). F6 window does not match the quote, and that he means volatility is claim text (correction 41).
- D1, D2: zero-slot, fixed gates, no returns read: compliant.
- Length: 4,730 words against 3,000-4,000; no correction (do not cut content in a check).

## 3. Required corrections

1. Verdict 2: relative value has two mentions, and the instrument of Singer's trade is claim text.
- Find: `Relative value gets one definition ("either directionally or from a Rel value point of view", [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C02-2|MT089-C02-2]]), one named trade (Tropin's curve steepener) and one worked case (Singer's Japanese inflation-bond trade).`
- Replace: `Relative value gets two mentions: Tropin's definition ("either directionally or from a Rel value point of view", [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C02-2|MT089-C02-2]]) and a quant family next to "yield and carry" ([[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C04-2|MT214-C04-2]]; Graham's quant side is trend, value and carry, [[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C08-3|MT113-C08-3]], which our Trend, Value and Carry pods already hold). It has one named trade (Tropin's curve steepener) and one worked case (Singer's convergence trade; that it was in Japanese inflation-linked bonds is claim text).`
Reason: [[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C04-2|MT214-C04-2]] names relative value; the instrument is only in the claim text of [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-2|MT122-C04-2]].

2. Verdict 4: the quotes show no loss.
- Find: `plus Singer's worked loss (SHOWN, one case)`
- Replace: `plus Singer's worked case (price and daily marks in the quote; the loss, its size and the year are claim text; one case)`
Reason: [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-2|MT122-C04-2]], -C04-3, -C04-X2 quotes give the price, the marks and "I kept the trade", no loss.

3. Verdict 5: split the ledger by firm and show the rule-relevant currency rows.
- Find: `5. Weakest link: stocks (0 of 7 ledger rows right) and currencies (1 of 10).`
- Replace: `5. Weakest link: stocks (0 of 7 ledger rows right: Graham 0 of 5, Singer 0 of 2) and currencies (1 of 10, all Graham; the four rows that follow the hawkish-currency idea, MT089-V003-1, MT089-V003-2, MT113-V002-1, MT133-V002-1, are 0 of 4, reader's grouping).`
Reason: FORECASTS.csv: equity rows MT122-V001-1 and MT122-V003-1 are Singer's; the only right currency row is MT092-V004-1 (dollar range).

4. Verdict 8: two of the seven forecasts rest on claim text.
- Find: `8. Counts: 4 rules, 10 analyst questions, 7 open forecasts, 2 diagnostics.`
- Replace: `8. Counts: 4 rules, 10 analyst questions, 7 open forecasts (F2 and F7 rest on claim text and are context only, so 5 carry a quoted statement), 2 diagnostics.`
Reason: v2 rule 3; [[MT090 - Ken Tropin on Macro Hive Podcast- Markets, Risk, AI-Driven Technology, and What Comes Next#^MT090-C04-1|MT090-C04-1]] reports "some people"; [[MT090 - Ken Tropin on Macro Hive Podcast- Markets, Risk, AI-Driven Technology, and What Comes Next#^MT090-C07-1|MT090-C07-1]] has no range.

5. C2: one cited application is not an application of the rule.
- Find: `Applied in 2022-24 by Tropin and Calderini ([[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C01-3|MT066-C01-3]], [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C07-5|MT089-C07-5]], [[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C07-2|MT113-C07-2]], [[MT133 - Resilient Strategies- Tailwinds in Left-Tail Scenarios - Pablo Calderini#^MT133-C05-1|MT133-C05-1]]).`
- Replace: `Applied in 2023-24 by Tropin and Calderini ([[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C07-5|MT089-C07-5]], [[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C07-2|MT113-C07-2]], [[MT133 - Resilient Strategies- Tailwinds in Left-Tail Scenarios - Pablo Calderini#^MT133-C05-1|MT133-C05-1]]; the ECB-hawkish reason in [[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C07-2|MT113-C07-2]] is claim text); [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C01-3|MT066-C01-3]] (2022) says only that divergence is "good for macro Trading".`
Reason: [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C01-3|MT066-C01-3]] quote states no currency rule; [[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C07-2|MT113-C07-2]] quote gives only "banking issues in the U.S".

6. C7 heading: the closing of the gap is in no source.
- Find: `**C7. A crowded, levered convergence trade marked daily: forced selling widens the gap before it closes.**`
- Replace: `**C7. A crowded convergence trade marked daily: forced selling can widen the gap (leverage is claim text; whether the gap later closed is in neither quote nor claim text).**`
Reason: [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-X2|MT122-C04-X2]] ends at "I kept the trade"; [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-4|MT122-C04-4]] may belong to the bankruptcy case of [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-1|MT122-C04-1]].

7. C7 other side: "the winner" is not in the pack.
- Find: `Other side: those sold out; the winner keeps capital for "special opportunities" ([[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C05-4|MT122-C05-4]]).`
- Replace: `Other side: those sold out (claim text). Keeping capital for "special opportunities" ([[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C05-4|MT122-C05-4]]) is a general statement in the quote, not tied to this trade; the trade's outcome is not in the pack.`
Reason: [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C05-4|MT122-C05-4]] quote has no link to the linker trade; its 2008 context is claim text.

8. Indicators table, R1 series: fix the splice.
- Find: `LSEG 3-month deposit rates where these start late.`
- Replace: `LSEG 3-month deposit rate of the same currency until the FRED series starts; each L-month change is taken inside one series.`
Reason: hidden choice; same convention as card 1's dollar series.

9. Section 3, central-bank activity row: the gate uses the Fed only.
- Find: `| FEDFUNDS, 12-month range. ECB, BoE policy rates: no live series | 0 |`
- Replace: `| FEDFUNDS, 12-month range (Fed only; his counts cover three banks). ECB, BoE policy rates: no live series | 0 |`
Reason: R1's gate departs from C1's three-bank count; the card should say so where the indicator is defined.

10. Section 6, low-volatility row: McCann describes an effect; the floor is the reader's remedy.
- Find: `| Low volatility must not inflate size (C6) | McCann. ASSERTED |`
- Replace: `| Low volatility must not inflate size (C6) | McCann describes the effect, ASSERTED; the floor is the reader's remedy (Keelan sizes in volatility units, [[MT067 - Graham's 2022 Virtual Investment Symposium- Discretionary Strategies Panel#^MT067-C08-3|MT067-C08-3]]) |`
Reason: [[MT067 - Graham's 2022 Virtual Investment Symposium- Discretionary Strategies Panel#^MT067-C05-3|MT067-C05-3]] states the effect, not a rule; the firm's own sizing ([[MT067 - Graham's 2022 Virtual Investment Symposium- Discretionary Strategies Panel#^MT067-C08-3|MT067-C08-3]]) is what inflates size in calm markets.

11. R2 bar: the referent of 100 bp is claim text.
- Find: `bar 1.0, his figure ("The historical average since 1990 is about 100 basis points", [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C01-3|MT092-C01-3]])`
- Replace: `bar 1.0, from his figure ("The historical average since 1990 is about 100 basis points", [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C01-3|MT092-C01-3]]; that the figure is the 2-to-10-year slope is claim text, so 1.0 is a reader's version)`
Reason: v2 rule 3: a meaning found only in claim text cannot carry a threshold.

12. R2 sizing: fix the duration formula.
- Find: `sized to equal sensitivity to a 0.01 change in yield, so the pair gains when S widens (reader; he speaks of the slope in basis points).`
- Replace: `sized to equal sensitivity to a 0.01 change in yield, so the pair gains when S widens (reader; he speaks of the slope in basis points). Durations: modified duration of a 2-year and a 10-year par bond at that month's GS2 and GS10, fixed now (reader).`
Reason: the panel holds excess returns, not durations; otherwise a hidden choice.

13. R2 ledger: split by speaker.
- Find: `Ledger: three steepener rows (2022, 2023, 2024); the slope rose each time, twice by less than the ledger's band (scored wrong).`
- Replace: `Ledger: three steepener rows. Tropin's of 2022 and 2023 (MT066-V002-2, MT089-V004-1): the slope rose by 0.14 and 0.20, under the 0.25 band, scored wrong. Calderini's of 2024 (MT133-V002-2) scored right, but that he held a steepener is ledger view text, not in his quote.`
Reason: FORECASTS.csv note on MT133-V002-2; keep the speakers apart.

14. R3 premise check.
- Find: `The 0.50 is the easing in Tropin's example: "75 at year end", then "four and a quarter" ([[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C04-X1|MT066-C04-X1]]).`
- Replace: `The 0.50 is the easing in Tropin's example: "75 at year end", then "four and a quarter" ([[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C04-X1|MT066-C04-X1]]; 4.75 is a reading of the garbled "4-3 now for uh 75"). Premise check: in that example a rise to 4.75 is still priced, so the 2-year sits above the funds rate and measure 1 is negative; measure 1 cannot be on at R3's own source case (October 2022) and fires only once the last hike is priced, as in 2023 ([[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C08-3|MT089-C08-3]]); measure 2 counts only easing priced inside the second year (reader).`
Reason: neither measure counts easing from a priced peak, which is what the quote describes.

15. R3 against Carry: duplication by construction.
- Find: `Shorting a 2-year note that yields less than cash is what a directional Carry rule would do (D1 decides).`
- Replace: `With measure 1 the 2-year yields at least 0.50 below FEDFUNDS whenever R3 is on, so its carry is negative by construction: a directional Carry rule would hold the same short, and R3 adds only the inflation filter (D1 decides).`
Reason: arithmetic of the condition FEDFUNDS minus GS2 >= 0.50.

16. R4 series: start year not in the pack.
- Find: `(LSEG S&P 500 12-month forward EPS, from 1985)`
- Replace: `(LSEG S&P 500 12-month forward EPS; its start year is not in the pack, to be confirmed at step 3.1)`
Reason: DATA_SHEET.md gives no start for the forward EPS series.

17. R4 self-check: same.
- Find: `It has data from 1985 only and no free live source.`
- Replace: `Its history start is not in the pack (to be confirmed at step 3.1) and it has no free live source.`
Reason: as correction 16.

18. Section 6 first row: the fixed-size rule is the reader's.
- Find: `| Singer (C7). SHOWN, one case | Registered for the pod (R2 above all) |`
- Replace: `| Singer (C7). Reader's rule: the quotes show he kept the trade ([[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-X2|MT122-C04-X2]]) and warn against leverage on a misunderstood risk ([[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-4|MT122-C04-4]], ASSERTED); "never add as it loses" is in no quote | Registered for the pod as a reader's rule (R2 above all) |`
Reason: no quote states a sizing rule; SHOWN requires a worked case of the rule itself.

19. Section 6: team correlation is claim text.
- Find: `team correlation "on average 10%" ([[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C06-1|MT214-C06-1]])`
- Replace: `"it used to be on average 10%" ([[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C06-1|MT214-C06-1]]; that it is the correlation between teams is claim text)`
Reason: [[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C06-1|MT214-C06-1]] quote does not name what the 10% measures.

20. Section 6: Singer's capital rows are assertions.
- Find: `| Singer. SHOWN (words) | Spec line`
- Replace: `| Singer. ASSERTED | Spec line`
Reason: [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C05-6|MT122-C05-6]] and [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C05-3|MT122-C05-3]] state an objective and a generalisation; no worked case.

21. Section 6: "cut fast" is claim text.
- Find: `Cut fast ("exit positions without a great deal of expense", [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C04-4|MT066-C04-4]])`
- Replace: `Exit cheaply ("exit positions without a great deal of expense", [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C04-4|MT066-C04-4]]: a liquidity point; "early" and "cut" are claim text)`
Reason: the quote is about the cost of exit, not its speed.

22. Question 2: not scoreable on the R1 series for all seven currencies.
- Find: `2. Name the most hawkish of R1's seven central banks. Will its currency beat the median of the seven? Scored on the R1 series.`
- Replace: `2. Name the most hawkish of R1's seven central banks. Will its currency beat the median of the seven against the dollar? Scored on LSEG FX spot (the R1 EX series are monthly research series; Yahoo carries only FXY, FXF, FXE and UUP).`
Reason: DATA_SHEET.md lists the EX series under research only.

23. Question 4: too few points.
- Find: `4. Will the correlation of weekly SPY and IEF returns over the window be positive?`
- Replace: `4. Will the correlation of daily SPY and IEF returns over the window be positive? (Weekly returns would give only 4 points at 4 weeks.)`
Reason: scoreability.

24. Question 6: define the unit.
- Find: `Will it extend by half a unit more? ([[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C05-X1|MT066-C05-X1]].)`
- Replace: `Will it extend by half a unit more, a unit being its own 6-month volatility (standard deviation of the last 126 daily returns times the square root of 126)? Markets with a free daily source only. ([[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C05-X1|MT066-C05-X1]].)`
Reason: hidden choice; the panel is monthly.

25. Question 8: define the risk unit.
- Find: `Probability that it loses more than one risk unit, scored on the paper record.`
- Replace: `Probability that it loses more than one risk unit (the position's target standard deviation over the forecast window), scored on the shadow paper record.`
Reason: scoreability.

26. F2: not his forecast.
- Find: `| F2 | No further Fed cuts in 2026 (his doubt is claim text; the quote reports "some people") |`
- Replace: `| F2 | Context only, not scored as his: no further Fed cuts in 2026 is claim text; the quote reports "some people", and his own words point the other way ("enormous pressure on the new chair to to really stimulate the economy", [[MT090 - Ken Tropin on Macro Hive Podcast- Markets, Risk, AI-Driven Technology, and What Comes Next#^MT090-C06-2|MT090-C06-2]]; [[MT090 - Ken Tropin on Macro Hive Podcast- Markets, Risk, AI-Driven Technology, and What Comes Next#^MT090-C04-X1|MT090-C04-X1]]) |`
Reason: v2 rule 3; contradicted by his quotes in the same recording.

27. F3: subject is claim text.
- Find: `| F3 | Powell's successor is "on the accommodative side of the ledger" |`
- Replace: `| F3 | Powell's successor (claim text) is "on the accommodative side of the ledger" |`
Reason: [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C06-2|MT092-C06-2]] quote has no subject.

28. F3 resolution: give a band and a reference.
- Find: `| FEDFUNDS lower | [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C06-2|MT092-C06-2]] |`
- Replace: `| FEDFUNDS more than 0.10 below its level at that first meeting | [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C06-2|MT092-C06-2]] |`
Reason: "lower" alone is not scoreable; 0.10 is the ledger's band for FEDFUNDS.

29. F4: no trigger, no score.
- Find: `| wrong in the first month GS10 averages above 5.0 |`
- Replace: `| wrong in the first month GS10 averages above 5.0; not scored if GS10 never reaches 5.0 |`
Reason: the statement is conditional on the level being reached.

30. Section 4 common block: the horizon quote is the quant side's.
- Find: `Reason: Graham's horizons are short ("one to two month Horizon maybe three months", [[MT062 - Global Macro- Discretionary vs. Systematic - Who Wins- - Global Alts 2025 - Pablo Calderin#^MT062-C03-4|MT062-C03-4]];`
- Replace: `Reason: Graham's horizons are short (its quant programs: "our Quant programs typically run one to two month Horizon maybe three months", [[MT062 - Global Macro- Discretionary vs. Systematic - Who Wins- - Global Alts 2025 - Pablo Calderin#^MT062-C03-4|MT062-C03-4]];`
Reason: the quote is about the quant programs, not the discretionary PMs the card draws its rules from.

31. Section 8: crowding is disputed inside Graham; add the decay warning.
- Find: `when positions are crowded ([[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C06-X2|MT214-C06-X2]]).`
- Replace: `when positions are crowded ([[MT214 - Why Macro Investing Matters More Than Ever - Kenneth Tropin on Markets, Volatility & Oppor#^MT214-C06-X2|MT214-C06-X2]]), though McCann says the information ratio among their PMs is higher in times of higher correlation ([[MT067 - Graham's 2022 Virtual Investment Symposium- Discretionary Strategies Panel#^MT067-C05-2|MT067-C05-2]]), so the two disagree. Tropin expects any rule to decay: "there's no way you can do what worked 10 years ago and expect it to always work in the future" ([[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C06-3|MT089-C06-3]]), and edge was larger when "markets were less efficient" ([[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C01-5|MT066-C01-5]]).`
Reason: omitted contradicting and decay quotes.

32. Section 8: do not pool Singer's rows into Calderini's claim.
- Find: `([[MT133 - Resilient Strategies- Tailwinds in Left-Tail Scenarios - Pablo Calderini#^MT133-C05-X1|MT133-C05-X1]]). Ledger: 0 of 7.`
- Replace: `([[MT133 - Resilient Strategies- Tailwinds in Left-Tail Scenarios - Pablo Calderini#^MT133-C05-X1|MT133-C05-X1]]). Ledger: his one equity row (MT113-V001-1, short in 2023-03) scored wrong; all 7 equity rows are wrong (5 Graham, 2 Singer).`
Reason: keep the speakers and the firms apart.

33. Section 12: the period of the 22 is claim text.
- Find: `| 22 changes in 2010-21; 76 since 2022 | [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C01-1|MT092-C01-1]] | in quote; conflicts with the row above |`
- Replace: `| 22 changes; 76 since 2022 | [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C01-1|MT092-C01-1]] | in quote; the period of the 22 (2010-21) is claim text, so the conflict with the row above is likely but not verified |`
Reason: [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C01-1|MT092-C01-1]] quote gives no period for the 22.

34. Section 12: the 10% referent.
- Find: `Stock-bond correlation at 40%; between teams 10%;`
- Replace: `Stock-bond correlation at 40%; 10% (between teams: claim text);`
Reason: as correction 19.

35. Section 12: 4.75 is a reading.
- Find: `| Priced path 4.75, then 4.25 | [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C04-X1|MT066-C04-X1]] | in quote (garbled) |`
- Replace: `| 75 at year end, then four and a quarter (read as 4.75, then 4.25) | [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C04-X1|MT066-C04-X1]] | in quote (garbled; 4.75 is a reading) |`
Reason: the quote reads "4-3 now for uh 75".

36. Section 12: the ledger tallies include the disputed rows.
- Find: `| FORECASTS.csv | machine-coded; grouping is the reader's |`
- Replace: `| FORECASTS.csv | machine-coded; groups as in the ledger's group column (other = macro, vol, commodities); the counts include the five rows disputed below (MT089-V005-1, MT066-V002-3, MT133-V001-1, MT066-V005-1, MT066-V003-1); without them 15 of 35, base rates imply 10.8 |`
Reason: card 2 reported both; re-tallied from FORECASTS.csv.

37. Pack problem 3: the quote is ambiguous.
- Find: `he describes the market, and says of that pricing "I'm skeptical" ([[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C02-5|MT066-C02-5]]).`
- Replace: `but it goes on "and then I think we start to see that ease back down in the middle of 23": it can be read as the market's path or as his own view, and his "I'm skeptical" ([[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C02-5|MT066-C02-5]]) is about easing at the end of 2023. The row is ambiguous, not clearly miscoded.`
Reason: full quote of [[MT066 - Graham Capital Management's Tropin on Why Macro is Killing It#^MT066-C04-X1|MT066-C04-X1]].

38. Dating table C2: first application.
- Find: `| C2 hawkish currency (R1) | 2025-12 | No | hindsight |`
- Replace: `| C2 hawkish currency (R1) | 2025-12 stated; applied from 2023-04 ([[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C07-5|MT089-C07-5]]) | No | hindsight |`
Reason: [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C07-5|MT089-C07-5]] (ledger date 2023-04) applies the idea; no effect on the flag.

39. C2: Tropin's own live case.
- Find: `Calderini liked the yen on value ([[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C07-3|MT113-C07-3]]), against the rule (reader).`
- Replace: `Calderini liked the yen on value ([[MT113 - Navigating a New World Order- Macro Strategies for Uncertain Times - Pablo Calderini#^MT113-C07-3|MT113-C07-3]]), against the rule (reader). In the recording that states the rule Tropin calls Japan "the most hawkish that I can remember" ([[MT090 - Ken Tropin on Macro Hive Podcast- Markets, Risk, AI-Driven Technology, and What Comes Next#^MT090-C06-4|MT090-C06-4]]); the quote draws no currency call from it.`
Reason: omitted quote, the live case for R1 and question 2.

40. Section 3, relative-hawkishness row: R1's inputs are research-only.
- Find: `| not on the sheet; 1 assumed |`
- Replace: `| not on the sheet; 1 assumed. All these 3-month and EX series are research-only on the data sheet (not fetched in the live cycle); live inputs would be LSEG deposit rates and FX spot on the PC; Yahoo has only FXY, FXF, FXE, UUP, DX-Y.NYB |`
Reason: DATA_SHEET.md lists them under "More FRED series fetched for research"; workflow rule 7.

41. F6: resolve on the period as spoken.
- Find: `| mean VIXCLS 2022-10 to 2027-09 above its 2010-19 mean |`
- Replace: `| mean VIXCLS 2022-10 to 2027-09 above its 2010-01 to 2020-12 mean (the period as spoken; that he means volatility is claim text) |`
Reason: [[MT067 - Graham's 2022 Virtual Investment Symposium- Discretionary Strategies Panel#^MT067-C10-2|MT067-C10-2]] says "the 2010-20 period"; the volatility referent is in the claim text only.

## 4. Open judgement points

1. Whether R3 keeps measure 1 at all, given that it is negative carry by construction and off at its source case; D1 against Carry decides, step 3.2 may replace it with an easing-from-priced-peak measure (LSEG futures) as a new version before registration.
2. R1's US leg on TB3MS against interbank rates abroad: keep, or use the LSEG US 3-month deposit rate for like-for-like (step 3.1).
3. Whether R1 duplicates Economic trend for currencies: needs Economic trend's input list (not in the pack; step 3.2 with D1).
4. Whether the five disputed ledger rows are re-coded (step 2.2-2.3 owner), and which tally the thesis register uses (step 1.5).
5. Whether Singer's fixed-size rule adds anything to state rules that already hold fixed size (step 3.1: drop as redundant or keep as a spec line).
6. Crowding: risk line or stop condition, given McCann against Tropin (step 3.1 spec "when it should stop working").
7. The sign of R2's carry on an inverted curve (self-check line, reader): settle from the design data at D1 / step 3.1, without returns.
8. F6 reference period 2010-01 to 2020-12 includes the 2020 spike; whether "2010-20" means the decade 2010-19 (step 2.2 scoring rules owner).

## 5. What I could not verify

- Economic trend's actual inputs (whether short-rate changes enter): not in the pack.
- Notes 1.3a and 1.3b (rates and carry theses): not in the digest (card's pack problem 10 is correct), so R2 against Strip reversion / the engine's built spreads and R1, R3 against the Carry thesis could not be checked.
- Start dates of IR3TIB01 and LSEG deposit series in the design years, hence D2's count; start of the forward EPS series.
- Whether "two1" in [[MT089 - Ken Tropin on How to Run a Successful Macro Hedge Fund by Bilal Hafeez, Macro Hive#^MT089-C08-1|MT089-C08-1]] and the referent in [[MT092 - Kenneth Tropin, Chairman and Founder of Graham, Featured on the Risk and Return Podcast#^MT092-C01-3|MT092-C01-3]] are the 2s10s slope (needs the transcript beyond the quote).
- The direction of the yield values I used for the R3 premise check beyond what the quote itself implies (a priced rise to 4.75 with the funds rate below it); no data were read.
- Which trade "lever something up" ([[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-4|MT122-C04-4]]) refers to: the linker trade or the bankruptcy claim of [[MT122 - Paul Singer - Podcast - In Good Company - Norges Bank Investment Management#^MT122-C04-1|MT122-C04-1]].

