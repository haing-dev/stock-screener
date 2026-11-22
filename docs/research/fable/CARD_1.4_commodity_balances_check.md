# Independent check of playbook card 1.4 (5 of 5): commodity balances (Pierre Andurand)

Checker: Opus 5.5, effort high (quant and risk officer), 2026-11-22. Ground truth: the "quote" field of all 201 claims in pack/CLAIMS.json (all read), plus FORECASTS.csv, DATA_SHEET.md, SOURCES.md, DIGEST.md, WORKFLOW sections 1-6. All 108 ids the card cites exist (lookup.py: 0 not found); 97 claims are not cited.

## 1. Verdict

PASS WITH CORRECTIONS (33 corrections; 0 contradicted numbers, 0 wrong ids, 0 MT115 statements without the [P] flag).
A. Numbers: 41 checked; 33 in quote, 5 ledger (all match FORECASTS.csv), 3 rightly marked summary only; 1 rounding to state (105 to 95 is 9.5%, not 10%); the 200 call is cited without its id, and its ten-month horizon is ledger view text, not quote.
B. Chains: 8 chains, 6 sound; chain 4 is labelled SHOWN (words) but its price step is claim text (ASSERTED); chain 2's "no ceiling" overstates (he puts oil's demand point at "around 200"); "his realised trades are Trend" is contradicted by MT125-C08-6 (a structural long held through a give-back).
C. Rules: R1 sound after 5 fixes (hidden class choices, holding lag reason, trigger labelled as proxy). R2 fails the premise check: in its source case he reduced (MT125-C08-7), and its coded form holds neither of his conditions (thin market, no news): held back, like card 1's R6. Count after correction: 1 rule forward (8 versions, 16 with sizing), 1 held back.
D-F. D2 reads 24-month outcomes past 2010-12 (look-ahead into the seal: cut at 2008-12); 6 important omissions; concentration rests on claim text only; dating table correct (nothing before 2011); no decision handed to the user; all forecasts correctly open or closed.

## 2. Findings

### A. Numbers (every number in the card)

| Number in the card | Where | Status |
|---|---|---|
| 0.15% per 10% | MT115-C05-3 [P] | in quote |
| one and a half months of storage | MT124-C03-4 | in quote (April 2020 = claim text, as the card says) |
| up to 5 million barrels a day for 12 months | MT124-C07-1 | in quote |
| at least two million barrels a day | MT124-C06-3 | in quote ("by two at least two million bars a day") |
| around 200 | MT124-C08-6 | in quote; the card never cites MT124-C08-6; the quote is conditional ("then") and has no date |
| Brent 118.11 -> 78.40, ten months | FORECASTS MT124-V001-1 | ledger, matches (2022-03-11 to 2023-01-10); horizon "this year" is view text; no MT124 quote contains "this year" (grep) |
| WTI 84.02 -> 89.56, 6.6% vs 6% band | MT125-V002-1 | ledger, matches (change 0.0659, band 0.06) |
| 5 resolved rows, 3 right; 2 of 3 price rows | FORECASTS | correct (V001-1 wrong, MT124-V002-1 right, MT125-V002-1 right, MT125-V002-2 wrong, MT125-V004-1 uranium right) |
| 1.7 grams, 1.7 Cent | MT123-C02-7 | in quote; caption "$110,000" (pack problem 5 correct: arithmetic fits $10,000) |
| 7-15 years, 10-15 years, 3-5 years, 7 years, 12 months | MT124-C10-3, MT123-C08-4, MT123-C07-2, MT124-C10-4, MT124-C11-1 | in quote |
| 105 to 95 in less than 24 hours | MT125-C08-1 | in quote; it is 9.5%; R2's "10%" rounds it and question 6 uses 9% (consistent once stated) |
| 1.4 billion (2018) to 300 million barrels | MT125-C08-2 | in quote |
| twice as volatile, half the position | MT125-C08-3 | in quote |
| 19%, 13%, $28,000, 1977 | MT123-C05-1, MT123-C05-2, MT123-C04-4 | in quote |
| above $20,000 | MT123-C05-8 | in quote |
| 50% | MT123-C05-7 | in quote |
| 35% | MT125-C02-5 | in quote ("within months" is the card's, not the quote's) |
| 1 million tons a year, zero to negative | MT123-C08-2 | in quote |
| more than 3 million tons in 2030 | MT123-C09-5 | in quote |
| four times, 5 years | MT123-C09-7 | in quote |
| 10 years of strong supply | MT124-C04-2 | in quote |
| 150 then is 220 today | MT124-C11-5 | in quote |
| $2, $4-5 backwardation; 21% vs 35-40%; $7,000 to $5,000 | MT124-C02-2, MT123-C04-8, MT123-C05-8 | summary only, correctly marked |
| $147 about $200 | MT124-C08-2 | summary only, correctly marked (pack problem 8) |
| 120 months, 24, 36, 10%, 20%, 12 months, 9%, 0.5, gates 75% / 50% / 15 points / 10 breaks | card | reader, marked as such (36 is called his lag in R1 but listed as reader in section 12: it is cocoa's lag, see C) |

No number is contradicted by its quote.

### B. Causal chains, labels, speakers

1. Chain 1 (balance -> inventories -> price): quotes support it (MT124-C04-1, MT124-C02-4, MT123-C09-1, MT115-C04-1 [P]). ASSERTED is right.
2. Chain 2: quotes support inelastic demand (MT115-C05-3 [P], MT124-C07-3, MT123-C02-6, MT123-C08-5) and "the price can go anywhere" (MT123-C02-5). But "a move with no ceiling" ignores that, in the same 2022 recording, price must cut demand "by one and a half million bucks a day" (MT124-C07-2) and "around 200 oil will be enough to to bring demand down" (MT124-C08-6). Corrected.
3. Chain 3: supported (MT124-C02-2, MT124-C03-5). He uses the curve as a gauge; no quote states a trade on its sign, so "Carry holds chain 3 in full" is the reader's. Corrected.
4. Chain 4: the quotes speak of supply ("expected by the market", "we have not seen that yet", "no impact at all on oil supply"), not of price. That oil fell because the expected Russian loss did not come is claim text of MT125-C06-3. And MT124-C02-3 says the fear itself "keeps the market tight", i.e. feared losses do move price. SHOWN (words) is too strong: ASSERTED. Corrected.
5. Chain 5: supported. Chain 6: supported (Lehman = reader, said). Chain 8: supported.
6. Chain 7: supported, but "on no news" is claim text (quote ends "and there was no"); the 2024 half has no id (MT123-C05-6 is the quote). Corrected.
7. Speakers: every MT115 use carries [P]; no statement of a host is attributed to him (all 201 claims are his by the pack note). Firm-level and personal views are kept apart adequately.
8. Verdict 3 "his realised trades are Trend": MT125-C08-6 is a "structural bullish position on energy" that "worked well in the first half of the year and then we gave back some gains" - held through the reversal, which Trend would not do; the card itself uses this difference to separate R1 from Trend. "Cocoa once it left its range" has no quote (MT123-C02-1 says an analyst proposed cocoa "in January"). Corrected.

### C. Rules

R1 (range break where supply is slow)
- Series: LSEG front contracts (sheet: "commodity futures curves") and CPILFESL (lag 1, first-published): on the sheet. Contract codes not on the sheet (pack problem 9, correct).
- Trigger: a nominal all-time high is the reader's proxy; he enters on the balance (exports, ratio), and the "range" is what other traders anchor on (MT123-C04-2). Not labelled as reader. Corrected.
- Class: he says "metals" (MT124-C10-3, MT124-C10-X1) and names only copper; the restriction to base metals (precious metals out) is a hidden choice. Corrected (labelled with a reason).
- Grains out: MT124-C10-3 says "for agricultural products it's pretty fast like within a year": all agricultural products, cocoa included. Only the 2024 quote (MT123-C07-2) makes the cocoa tree slow. Must be said. Corrected.
- Copper: he also names a fast supply response, scrap: "when prices go up you get more scrap Supply" (MT123-C09-2). Omitted. Added to the self-check.
- Holding: H 36 is cocoa's three years; for metals, the only markets the design window tests, his shortest stated lag is "at least five years" (MT124-C10-X1). Reason corrected; the grid itself is kept (open point).
- Real ceiling: the yardstick (real price vs earlier real peak) is his; the deflator is not named in any quote; his two conversions imply factors of about 5.1 (1977 to 2024) and 1.47 (2008 to 2022). CPILFESL is the reader's. Corrected in the indicator table.
- Direction: long is supported by MT123-C04-3, MT123-C07-3, MT123-C02-5. No look-ahead in the rule itself.
- Versions: 2 x 2 x 2 = 8, all averaged. Correct.

R2 (paper fall in a tight market)
- Premise check fails. (i) The source case is September 2022, and his action then was "I want to to reduce my positions" (MT125-C08-7) after giving back gains (MT125-C08-6); the card's own dropped-ideas list says so. (ii) His mechanism has two conditions, a thin market (MT125-C08-X1, C08-2) and a fall on no news (MT125-C08-1); the coded rule has neither (no position or news series). What is left is "Carry is long and the price fell", a reader's dip filter on Carry; the card itself says it "adds weight, not information". (iii) "Fear alone keeps the market tight" was enough for the card to drop the fear-fade rule; the same standard drops R2. Held back until a quote supports buying such a fall; analyst question 6 covers it.
- Further errors in the text: "Trend is short or flat" is not guaranteed (12-month versions can be long after a 1- or 3-month fall); "Cards 1 to 4: no oil position" is wrong (card 1's R4-B is long the panel's commodities, crude included); "at most 12 months (card 1's convention)" is not card 1's convention, which is a 12-month tail after the last on-month (digest D) - moot while held back.

Shared: "P is the month-end close of the front contract" leaves the roll date open (front contract in its delivery month); step 3.1 fixes it (open point). Sizing version: "one-year risk budget" undefined; corrected to a stated formula.

### D. All 201 quotes: contradictions, omissions, duplicates, data, MT115

Contradictions of the card by a quote
1. MT125-C08-6 and MT125-C08-7 contradict "his realised trades are Trend" and the long direction of R2.
2. MT124-C07-2 and MT124-C08-6 (price must cut oil demand, at "around 200") contradict chain 2's "no ceiling"; they are also the real "against himself" pair for MT124-C07-3, whereas the card's chosen pair (MT125-C02-5) is gas demand switching to oil, which is no contradiction.
3. MT124-C10-3 ("agricultural products ... within a year") against the cocoa slow class of R1.
4. MT123-C06-X1 says coffee "looked interesting as well"; that he left it is claim text, yet the card's "Concentration" process rule and its agreement with card 1 (and conflict with card 2) rest on it. No quote speaks of concentration; MT123-C05-7 (size for a 50% adverse move) points toward smaller sizes.
5. MT124-C02-3 (fear keeps the market tight) against chain 4's "feared losses fade".

Important ideas omitted
1. His own bear case and falsifier for cocoa: "a bumper crop in West Africa next year" (MT123-C06-1), price then "towards ... five or $6,000 a ton" (MT123-C06-3), with a floor from restocking (MT123-C06-4). Added to section 8.
2. Copper scrap as a fast supply response (MT123-C09-2). Added to the self-check.
3. The shale supply mechanism: shareholder discipline (MT124-C04-4, MT124-C04-X1), depleted acreage (MT125-C07-4), 80% first-year decline (MT125-C07-5). It bears on R1's crude version (a 12-month US cycle, MT124-C11-1, places crude nearer the fast class) and on F3. Not corrected (context; open point for 3.1).
4. EU carbon: "early this year I became less bullish on carbon" (MT125-C10-3), the one trading stance in MT125 the card does not file anywhere (answer to the card's check item e). Added to dropped ideas.
5. What the price assumes about duration: "the market doesn't believe that um we will lose this oil for very long" (MT124-C08-5) - his reading of the curve's implied outage, relevant to chain 4 and analyst question 3. Not corrected.
6. 2022 says history gives no guide ("new territory", MT124-C01-X1); 2024 builds on history ("look at a bit more history", MT123-C04-5; the 1977 analogue). Not corrected; noted.

Attribution: no statement of one speaker is given to another. MT115: every use is flagged [P]; nothing rests on MT115 alone except the 0.15% elasticity (paired with MT124-C07-3) and the 2014 points in section 8 (flagged).

Duplicates: R1 against card 1's R4-B is measured in D1 (reported). Card 1's R6 (gold, held back) is the only single-commodity rule in cards 1-4; immaterial. R2 duplicates Carry by construction (condition (i) is Carry's long). Economic trend: the pack describes it as growth and inflation surprises (digest F); whether it reads Chinese growth (China reopening, MT125-C06-7) is not in the pack (open point).

Data: R1 and R2 use only LSEG curves and CPILFESL. Analyst questions 1, 3, 4, 7, 8, 9 need public reports not on the sheet (EIA, COT, exchange stocks, ICCO): allowed for the analyst layer, which reads public information.

### E. Dating table

Correct. No quote describes an action before 2011. MT124-C08-2 ("when le mans went burst") is an observation; MT115-C05-1 ("what people were saying in natural gas in 2008") is an observation [P]; the dated shorts (late 2008, 2014-15, before Covid) are claim text of MT124-C02-5. All theses are hindsight-flagged.

### F. Rules of the shop

- No decision is handed to the user. Versions are averaged. Open choices are versions or gated diagnostics.
- D2 look-ahead: breaks up to 2010-12 with an outcome 24 months later read prices into 2011-2012, inside the sealed holdout. Cut at 2008-12. D2 also left open whether crude (a version) counts in the slow class: fixed (reported apart).
- D1 "the Trend pod's slowest version" is ambiguous (several Trend versions share the longest lookback): fixed.
- Analyst questions: answerable and scoreable; question 5's 0.5 bar is the usual bar for any recession (jobs_alarm), not for a large one as labelled: corrected.
- Forecasts: F1-F3 open and dated (F1 to 2029-05, F2 2030, F3 to 2032); the 8 closed windows are indeed closed by 2026-11; MT125-C09-2 (export capacity "2026 or 2027") is rightly context.

## 3. Required corrections

1. Verdict 3: "his realised trades are Trend" is contradicted by MT125-C08-6.
- Find: `his realised trades are Trend`
- Replace: `his large moves overlap Trend only while prices run his way (reader; his 2022 structural long was held through a give-back, MT125-C08-6)`
Reason: MT125-C08-6 "structural bullish position ... worked well in the first half of the year and then we gave back some gains"; the card itself separates R1 from Trend on this.

2. Verdict 3: counts after R2 is held back.
- Find: `New: 2 rules, 12 versions (24 with the sizing version), both hindsight-flagged; R1 only if diagnostic D2 passes.`
- Replace: `New: 2 rules, both hindsight-flagged; R2 fails the premise check and is held back (section 4), so R1 alone goes forward, with 8 versions (16 with the sizing version), and only if diagnostic D2 passes.`
Reason: see correction 16.

3. Verdict 5: the weakest link is the supply forecast; the 200 is conditional and undated in its quote; the id was missing.
- Find: `5. Weakest link: turning a balance into a dated price.`
- Replace: `5. Weakest link: the supply forecast inside the balance, and so any dated price. The 200 below (MT124-C08-6) is conditional ("then") and undated in its quote; its ten-month horizon is ledger view text, and its premise, the Russian cut, never came, so the miss is a supply miss before it is a price miss (reader).`
Reason: no MT124 quote contains "this year"; the card's own evidence (MT123-C10-1) shows the supply premise failed.

4. Verdict 7: concentration rests on claim text.
- Find: `agrees with card 1 on concentration and fast cuts`
- Replace: `agrees with card 1 on fast cuts (concentration rests on claim text only, section 6)`
Reason: no quote speaks of concentration; MT123-C06-X1 says coffee "looked interesting as well".

5. Verdict 8: counts.
- Find: `8. Counts: 2 rules, 10 analyst questions`
- Replace: `8. Counts: 2 rules (R2 held back), 10 analyst questions`
Reason: follows correction 16.

6. Chain 2 title overstates: he names the price at which oil demand gives way.
- Find: `**Demand that cannot flex plus slow supply gives a move with no ceiling.**`
- Replace: `**Demand that cannot flex plus slow supply gives a very large move, capped only where demand finally gives way.** For oil he puts that point at "around 200 oil" (MT124-C08-6): price must "bring that demand down by one and a half million bucks a day" [barrels] (MT124-C07-2).`
Reason: both quotes are in the same 2022 recording as MT124-C07-3.

7. Chain 4 label: the price step is claim text.
- Find: `SHOWN (words), against his own forecast (section 8). Limit: no series for expected supply.`
- Replace: `ASSERTED: the quotes speak of supply, not price; that oil fell because the expected Russian loss did not come is claim text of MT125-C06-3, and fear itself "keeps the market tight" (MT124-C02-3). Against his own forecast (section 8). Limit: no series for expected supply.`
Reason: MT125-C06-3, MT123-C10-3, MT115-C04-X1 quotes contain no price statement.

8. Chain 7: "no news" is claim text.
- Find: `on no news (MT125-C08-1)`
- Replace: `(MT125-C08-1; "no news" is claim text, the quote ends "and there was no")`
Reason: quote of MT125-C08-1.

9. Chain 7: the 2024 half needs its id.
- Find: `SHOWN (words), 2022 and 2024. Limit: no position data on the sheet.`
- Replace: `SHOWN (words), 2022 (MT125) and 2024 (cocoa: "less liquidity ... and then the Vol volatility increases", MT123-C05-6). Limit: no position data on the sheet.`
Reason: brief v2 rule 4.

10. Indicator table: the deflator is the reader's.
- Find: `WTISPLC, PCOPPUSDM, LSEG front contracts; deflator CPILFESL`
- Replace: `WTISPLC, PCOPPUSDM, LSEG front contracts; deflator CPILFESL (reader: no quote names his deflator, and his two conversions, x5.1 for 1977 to 2024 and x1.47 for 2008 to 2022, need not use one index)`
Reason: MT123-C04-4 (5,500 to 28,000), MT124-C11-5 (150 to 220); "global GDP deflator" is claim text.

11. Carry: he never states a trade on the curve's sign.
- Find: `That is chain 3 in full`
- Replace: `That is chain 3 as far as it can be coded; no quote of his states a trade on the curve's sign (reader)`
Reason: MT124-C02-2 defines backwardation as a gauge of tightness only.

12. Curve carry: the quote does name the front month.
- Find: `the months named are summary only`
- Replace: `the quote names only the front month; the deferred month (December Brent) is summary only`
Reason: MT124-C03-X1 "if we want to be long the front month contract".

13. Trend bullet: give-back and cocoa entry.
- Find: `an energy book that "worked well in the first half of the year" 2022 (MT125-C08-6), cocoa once it left its range.`
- Replace: `in part: his energy book "worked well in the first half of the year" 2022, but he held the "structural bullish position" through the give-back that followed (MT125-C08-6), which Trend would not; no quote says when he entered cocoa against its range (reader).`
Reason: MT125-C08-6; MT123-C02-1 says only that an analyst proposed cocoa in January.

14. R1 markets: the base-metal class is a hidden choice.
- Find: `Markets: copper and the other base metals in the panel`
- Replace: `Markets (reader's class: he says "metals" and names only copper, so precious metals are left out, since no quote ties their price to mine supply): copper and the other base metals in the panel`
Reason: MT124-C10-3, MT124-C10-X1 say "metals"; brief: no hidden choice.

15. R1: his 2022 words put all agricultural products in the fast class.
- Find: `Not grains ("within a year you can change things", MT124-C10-3).`
- Replace: `Not grains ("within a year you can change things", MT124-C10-3; he says it of all "agricultural products", so cocoa's place in the slow class rests on the 2024 quote alone, MT123-C07-2).`
Reason: quote of MT124-C10-3.

16. R2 held back: premise check fails.
- Find: `**R2. Paper fall in a tight market.** Markets: crude oil in the panel (his statements are on oil).`
- Replace: `**R2. Paper fall in a tight market. HELD BACK (Opus check): premise check fails.** In the source case he reduced: "I want to to reduce my positions" (MT125-C08-7); and the coded form holds neither of his two conditions, a thin market and a fall on no news (no position or news series), so what is left is Carry's long after a fall. Held back from registration until a quote supports buying such a fall; analyst question 6 covers it meanwhile. As drafted: Markets: crude oil in the panel (his statements are on oil).`
Reason: same standard the card applies to the fear-fade rule; card 1's R6 precedent.

17. R2: 105 to 95 is 9.5%.
- Find: `The 10% is his case`
- Replace: `The 10% rounds his case (ten dollars from 105 is 9.5%)`
Reason: arithmetic; question 6 uses 9%.

18. R2: Trend is not necessarily short or flat.
- Find: `Carry is already long here and Trend is short or flat;`
- Replace: `Carry is already long here and Trend's shorter lookbacks are short or flat, but its 12-month versions can still be long after a 1- or 3-month fall (reader);`
Reason: a 10% one-month fall does not reverse a 12-month trend in general.

19. R2: card 1's R4-B holds crude.
- Find: `Cards 1 to 4: no oil position.`
- Replace: `Cards 1 to 4: no oil position of its own; card 1's R4-B holds crude with the other panel commodities while its inflation state is on.`
Reason: digest D, R4 action B.

20. R1 holding: 36 months is cocoa's lag, not the metals lag.
- Find: `H 36, the shortest lag he gives for this class, or 24`
- Replace: `H 36, the shortest lag he gives in the class (cocoa's three years; for metals, the only class the design window tests, he says "at least five years", MT124-C10-X1, so both versions sit below it), or 24`
Reason: MT123-C07-2, MT124-C10-X1.

21. R1 trigger: label the price trigger as a proxy.
- Find: `Trigger month: P is above every earlier month-end P`
- Replace: `Trigger month (reader's proxy: he enters on the balance, not on the price; the range is what other traders anchor on, MT123-C04-2): P is above every earlier month-end P`
Reason: no quote has him entering on a price break.

22. Sizing version: state the formula.
- Find: `notional capped so that a 50% adverse move costs no more than the rule's one-year risk budget (reader's bar)`
- Replace: `notional set to the smaller of the volatility-sized notional and the notional at which a 50% adverse move costs one year of the rule's volatility budget (its annual risk allocation; reader's bar)`
Reason: "one-year risk budget" was undefined (hidden choice).

23. Concentration process rule rests on claim text.
- Find: `coffee "looked interesting" and was left (MT123-C06-X1). Dropped: rules stay at equal risk.`
- Replace: `coffee "looked interesting as well" (MT123-C06-X1); that he left it is claim text, and no quote speaks of concentration (MT123-C05-7 points to smaller sizes). Dropped: rules stay at equal risk.`
Reason: quote of MT123-C06-X1.

24. Section 8 demand: the wrong pair.
- Find: `yet industry made "a switch of about 35 percent for oil" away from gas within months (MT125-C02-5), and cocoa`
- Replace: `yet in the same recording price must "bring that demand down by one and a half million bucks a day" (MT124-C07-2) and "around 200 oil will be enough to to bring demand down" (MT124-C08-6); the "switch of about 35 percent for oil" (MT125-C02-5) is gas demand moving to oil, so it is no contradiction (reader); and cocoa`
Reason: quotes; "within months" is not in MT125-C02-5.

25. Section 8 card 1.
- Find: `- Card 1: agrees on concentration, fast cuts and real assets in inflation (its R4-B).`
- Replace: `- Card 1: agrees on fast cuts and real assets in inflation (its R4-B); concentration is claim text here (section 6).`
Reason: as correction 23.

26. Section 8 card 2.
- Find: `- Card 2: conflicts on spreading risk.`
- Replace: `- Card 2: no quote of his speaks to spreading risk; a conflict on it would rest on claim text (reader).`
Reason: as correction 23.

27. Section 8 wrong-if: add his own stated bear case.
- Find: `his supply forecasts miss as often as the consensus he calls conservative (MT123-C02-2).`
- Replace: `his supply forecasts miss as often as the consensus he calls conservative (MT123-C02-2); or, in his own words for cocoa, "a bumper crop in West Africa next year" (MT123-C06-1), with the price then "towards ... five or $6,000 a ton" (MT123-C06-3).`
Reason: omitted falsifier stated by him.

28. D1: R2 part reported only while held back.
- Find: `Under 50%, R2 is not the disagreement cell it claims and is not registered.`
- Replace: `Reported only while R2 is held back (section 4); if a quote later supports it, under 50% R2 is not the disagreement cell it claims and is not registered.`
Reason: follows correction 16.

29. D1: "slowest version" is ambiguous.
- Find: `share of on-months in which the Trend pod's slowest version is long the same market`
- Replace: `share of on-months in which the Trend versions with the longest lookback are long the same market by their average sign`
Reason: several Trend versions share the longest lookback.

30. D2: look-ahead into the sealed years and crude left open.
- Find: `Count range breaks (first trigger month after at least 12 months without one) in the slow class and in wheat, corn and soybeans.`
- Replace: `Count range breaks (first trigger month after at least 12 months without one) up to 2008-12, so that every 24-month outcome ends inside the design months, in the slow class (base metals and cocoa; crude, a version, reported apart) and in wheat, corn and soybeans.`
Reason: a 2009-2010 break measured 24 months later reads 2011-2012 prices (sealed).

31. Dropped ideas: the one MT125 trading stance not filed.
- Find: `- European gas arithmetic (most of MT125): policy advice, not a trading rule.`
- Replace: `- European gas arithmetic (most of MT125): policy advice, not a trading rule. Its one unfiled trading stance: "early this year I became less bullish on carbon" because mandates come top down (MT125-C10-3); a past stance with no horizon and no series named on the sheet.`
Reason: card's check item (e).

32. Self-check R1: copper has a fast supply source.
- Find: `Holding through a 50% fall suits a man who can cut on judgement, not a fixed rule.`
- Replace: `Holding through a 50% fall suits a man who can cut on judgement, not a fixed rule. For copper he names a fast supply response too: "when prices go up you get more scrap Supply" (MT123-C09-2).`
Reason: omitted quote against R1's class.

33. Analyst question 5: the bar is for any recession.
- Find: `(reader's bar for large)`
- Replace: `(the usual bar for any recession, as jobs_alarm; he says only large ones cut oil demand, so the answer also states whether the rise looks large, reader)`
Reason: MT124-C08-1 "not small recessions but large recessions".

## 4. Open judgement points

1. R1 holding grid {24, 36} sits below his metals lag (at least 5 years); whether to use a per-class lag (36 cocoa, 60 metals) is for step 3.1 as a registered version, not now.
2. R1 crude version: his 12-month US cycle (MT124-C11-1) and shale discipline (MT124-C04-4, MT125-C07-5) pull opposite ways; step 3.2 judges whether crude belongs in the slow class at all.
3. Which base metals have an LSEG futures curve and a panel return (LME metals may not): step 3.1; if only copper, D2's 10-break floor likely fails, which drops R1.
4. Roll convention for "the front contract at month-end" (delivery month): step 3.1.
5. Economic trend duplicates (recession short oil, inflation long commodities, China reopening): whether the pod reads Chinese growth is not in the pack; step 3.2.
6. R2 release from hold: only if step 1.5 or a later pack finds a quote of him buying a fall in a backwardated market.
7. Ledger rows MT124-V001-1 (conditional, undated 200 call scored at 10 months) and MT124-V002-1 / MT125-V002-2 (output scored on price): step 2.3 rescoring.
8. Deflator for the real-ceiling version (CPILFESL vs a headline or global index): step 3.1, as a version if kept.

## 5. What I could not verify

- Speaker identity of MT115 (pack note only).
- Whether the LSEG curves carry cocoa, base metals and grains with history from the 1970s, and which commodities are in the panel (data sheet silent).
- Trend's version grid in detail (the digest gives only "16"), so D1's wording rests on the description.
- Whether the auto-captions are right where garbled (e.g. "$110,000", "Apple" for cocoa, "le mans" for Lehman).
- The CPI factors I quote in correction 10 come from the quotes' own numbers; I did not check them against any index (no data).
- Outcomes of R1's single live case (cocoa 2024) and of the closed windows: not in the pack.
