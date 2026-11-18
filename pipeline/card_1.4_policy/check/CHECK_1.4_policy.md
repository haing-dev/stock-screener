# Independent check of playbook card 1.4 (policy and liquidity), 2026-11-18

Checker: Opus 5.5, effort high (quant and risk officer). Inputs read: the card (all), BRIEF_FABLE.md, all 590 quotes of pack/CLAIMS.json (plus machine fields for every id the card leans on), WORKFLOW sections 1-6, DATA_SHEET, FORECASTS.csv (120 rows), SOURCES, DIGEST, BRIEF_V2_RULES. Every cited id was looked up with tools/lookup.py. No web, no code, no backtests.

## 1. Verdict

PASS WITH CORRECTIONS.
1. Numbers: 23 "in quote" numbers checked, all in quote; 7 "summary only" numbers checked, all summary only; ledger counts reproduce (D 37 resolved, 12 right; pools A+B = 16 rows, 4 right; Dec 2018 1 of 11; B 1 resolved, wrong; 10 missing claim ids). 0 numbers contradicted.
2. Chains and attributions: 0 statements of one man given to the other; 9 places where claim text carries a label, a date or a premise the quote does not (2003, "half a percent" as cost, the 2023 Treasury refusal, gold's rise, energy direction, copper, Japan, the release valve, the 1999 action).
3. Rules: all series exist on the data sheet and lags match; 1 rule fails the premise check (R6: the quote points to a pullback, the long is claim text); 1 hidden choice built with 2022 knowledge (the R1/R2 gate, now a version); 5 smaller hidden choices (commodity basket, splice, euro mapping, S&P and gold series, vintages).
4. Omissions that change the record: the 1999 long behind R3 ended in his largest recalled loss; the 2021 front-end short on 40% money growth (a liquidity win) is missing; B's own allocator rule contradicts his hot/cold sizing.
5. 45 corrections (section 3), all applied by apply_check.py; 10 open judgement points; none hands a decision to the user.

## 2. Findings A to F

### A. Numbers
In quote, confirmed: 70% of money (MT153-C03-1); a trillion to zero in 12 months (MT153-C03-3); 7.5% to 4% M2 growth (MT152-C04-3); 40% money growth (MT149-C07-1, MT151-C01-4); 4.5% and 5% (MT148-C02-1, C02-2); 50/25/25 and one year (MT151-C12-2); 350% (MT148-C11-2, MT151-C12-4); half a percent (MT151-C08-4, C09-1, MT085-C02-X1); 2.5% (MT141-C06-2); fifteen or twenty percent (MT152-C10-4); 10-year at 350 (MT149-C07-3); 50 basis points (MT151-C01-5); 80% (MT069-C04-1); 85 or 90% (MT142-C01-3); 70 to 80% (MT148-C08-2); 9% against 1% (MT153-C13-4); 600 million (MT046-C05-5); 20% as effective (MT069-C05-3); 18 or 24 months (MT141-C13-4); 8 years (MT069-C03-4); 7% of GDP (MT085-C01-3, MT203-C09-1); 50 to 60 basis points (MT152-C08-1); 12 to 18 months (MT046-C05-3); 5 or 10 years (MT148-C06-2).
Summary only, confirmed: 6.04% and 6.5% (MT153-C10-5, MT152-C07-6 claim text); 40% in Q4 2000 (MT148-C11-2, MT151-C12-4); 2018 sector declines and curve levels (MT152-C02-1, C02-2); forwards 0.5% to 6-7% (MT151-C09-4); bond short 25% of NAV (MT151-C03-3); 8% inflation with 3% yields (MT148-C05-1); oil below 60 (MT142-C08-1). Earnings forecasts 25/35/36% are all claim text (pack problem 2 confirmed).
Reader numbers, correctly labelled: 0.25, L/T 6 or 12, 3 months, lowest third, 15/10 points, 6-month window, 3/6 for R6, 80% and 6-episode gates, 0.5 stop flag. Not labelled: the five-times target of question 10 (no quote; corrected, item 25). Ledger: digest line "16 | 25% | -9 pp" = pools A and B (7 + 9 rows, 3 + 1 right); the card's 4 of 16 is right.

### B. Causal chains and indicators
- C1: 2003 is claim text (item 5). "The next easing is more extreme" has a quote the card does not cite (MT152-C03-1, "a lot more crazy monetary stuff"); MT152-C01-1's quote does not say it. Minor, not corrected.
- C2: "off when inflation is high" rests on claim text of MT149-C07-3 (the quote is cut after "10-year yielding 350"); the 2018 short was made on QT ("because I saw a cutie coming"), i.e. C5, not C2 (item 6).
- C3: correct; Hyman attribution is claim text and labelled.
- C4: correct; "other side" is reader but not labelled (minor).
- C5: one-sided. It lists the 2018 loss but omits the 2021 front-end short on "money supply growing at 40 percent ... that was a fat pitch" (MT149-C07-1) closed "at like 150 basis points" from 15 (MT151-C10-4) (items 3, 7).
- C6: "half a percent" is labelled SHOWN holding cost, but the quote does not say what it is; the card's own pack problem 9 shows two readings (item 8). The two men tell one Soros-fund trade, so it is one case (item 2). "Local bonds and stocks then rise" is claim text (gilts "down 2 points" is in MT151-C09-6's summary only); not corrected.
- C7: correct. MT203-C10-1 (no JGBs) is placed in 2012-13 by its claim text; the quote is from 2024 and has no period. Acceptable with that caveat.
- C8: the gold link of the release valve is claim text (item 38).
- Periods: MT152 is uploaded 2020-01-06; the card uses December 2018 from content and ledger without saying so (item 45). MT151/MT141 are dated 2024-10 by content (pre-election), consistent with the ledger.
- Indicators table: every id resolves to the right man; every series id is on the data sheet with the lag shown.

### C. Rules
- Common: the 12-month tail is one fixed choice with a quoted reason, but it contradicts the "sell when the reason is gone" rule the card registers (item 27; judgement point 2). Vintages unspecified (item 9). The section 6 entry versions double the grid but were not counted (items 1, 10). Versions were not said to be averaged (item 10).
- R1: direction supported by one recalled case (MT153-C10-5, MT151-C12-1/4, MT148-C11-2). The R4 gate is a hidden choice made with 2022-23 knowledge, from claim text of MT149-C07-3 (items 12-13). The TWEXMMTH/DTWEXBGS splice mixes two indexes (item 11; judgement point 4).
- R2: elements all present; warnings are 2018 words (flagged). Gate as R1 (item 14). GS2's first month may fall after 1975-01 (cannot verify; judgement point 9).
- R3: direction supported for the bond leg (MT151-C03-3, MT151-C01-5); the stock leg's quote evidence is MT069-C06-3, not MT151-C11-2 (items 17, 41). Gold, S&P and median-window series were unspecified (items 15-16).
- R4: both thresholds in quote; "commodity basket" undefined (item 18); core CPI stands in for the CPI he names (flagged in the card; judgement point 5). The only R4-type action in a quote (2-year short, MT151-C10-4) was omitted (item 19).
- R5: G10 scope, euro mapping and panel availability undefined (item 20). The trigger is versus the dollar relative to a median, while the 1992 case was a break versus the mark with other ERM currencies falling too (judgement point 6).
- R6: fails. The quote says rising real and nominal rates are "normally ... a signal that you're going to get a 5 10 could be 15% pullback"; that gold rose anyway and that this is bullish is claim text. A trade direction from claim text cannot be registered (BRIEF_V2 rules 3 and 6) (item 21).
- Look-ahead: none in the data timing as written (lags match the sheet). The look-ahead is in design: the R1/R2 gate.

### D. All 590 quotes read: contradictions, omissions, misattribution
Contradicting the card:
- MT203-C08-2: B's words point to a gold pullback on rising yields, not the long of R6.
- MT069-C06-3, MT148-C11-X1, MT151-C11-3: the 1999 melt-up long (R3 stock leg's only pre-2011 case) ended with "bought the exact top" and a "two or three billion" loss.
- MT141-C12-1: B as allocator adds to managers "in a slump", against his own "you earn the right to take a risk" (MT141-C11-2), which the card presents as a shared view.
- MT148-C13-4: "the best short-selling period I've ever seen", against "shorting stocks rarely pays" (item 28).
- MT151-C07-2 against the card's 12-month tail (item 27).
- MT148-C16-X1 gives probabilities (70/30), so "cannot fail" is wrong for it (item 36).
Important omissions:
- The 2021 front-end short on 40% money growth (MT149-C07-1, MT151-C10-4): his one recalled liquidity win, with numbers in quote (and an early exit: "they went to 500").
- Reported failures: the post-1987 depression call (MT046-C04-X1), his Japan record "the last 15 years" (MT046-C06-4, relevant beside B's Japan case), index shorts "a disaster" (MT046-C05-X1, cited only in section 6).
- Both men's trend element: "you see the momentum start to change in your favor then you really go for it" (MT153-C05-3), "I'm a technician" (MT151-C06-1), "if you're in a big Trend the big Trend covers up a lot of the mistakes" (MT203-C15-1), "things really used to Trend a lot more" (MT141-C07-1). Part of the recalled P&L may be the Trend pod's; this supports the card's self-check but is not stated.
- B's liquidity rule "you can be one thing but not many" is cited; its meaning (concentrated, illiquid or leveraged, not all three) is claim text. Fine.
- "Bear markets" as D's profit source: MT148-C05-1, MT153-C03-2, MT151-C07-6 support R2's direction and are not cited (minor).
Misattribution: none. Every cited id was checked for speaker. Two near-misses: "the crowd's right 80%" is D quoting Soros (MT069-C04-1), and "I only swing at strikes" is B quoting someone else (MT141-C05-6); the card does not misassign them.

### E. Dating table
No "Yes" in the table rests on a year spoken in a quote. R1 and R2 can be placed before 2006 by "Greenspan" in MT148-C11-2 (reader knowledge of his tenure); R5 and C6 by "Quantum fund" and the band (context); R3's stock leg by "'99" in MT069-C06-3, not by the cited MT151-C11-2. Corrected in items 39-42 and 4. The card's closing sentence (a recalled action is not a document) is right, so all six rules are hindsight-flagged under rule 5 and can reach Incubator only.

### F. Rules of the shop
- No decision is handed to the user. Open choices: the gate and entry versions were not counted or averaged (fixed, items 1, 10, 12, 14); diagnostics had undefined scope (D1 versions, D2 "Core book" before Core exists; items 43-44).
- Analyst questions: Q1 (categorical stance) and Q5 (a count of today's data) were not scoreable as written; Q10 had no resolution horizon (items 23-25). Q9 lets the analyst choose its own events (judgement point 7). Header horizon cited the wrong claim (item 22).
- Forecasts: the energy row had no direction and could be read as a short (item 30); the "second wave" row is an analogy the pack itself calls not a forecast (item 31); copper, Japan and the oil conditions are claim text (items 32-34); MT069 rows had no horizon although the recording gives one (item 29). Le Pen and debt-reckoning windows have closed: due, not open (the card says so).

## 3. Required corrections

1. Verdict line 2: count versions with the gate and entry versions, say they are averaged, hold R6 back, and correct the claim about where the profits came from.
- Find: `2. About a third can be coded: six rules, 22 versions. Liquidity itself, peg breaks, policy personnel and conviction sizing cannot, and the recalled profits came from those.`
- Replace: `2. Part of it can be coded: six rules, 30 versions (60 with the two entry versions of section 6), all averaged; R6 fails the premise check (section 4) and is held back, leaving 28 (56) to register. Liquidity itself, peg breaks, policy personnel and conviction sizing cannot; the 1992 and Japan 2012-13 trades came from those, while the 2000 Treasury trade is coded in R1 and R2.`
Reason: 8 + 8 + 4 + 4 + 4 + 2 = 30 after items 12 and 14; section 6 adds an entry version to every rule; R6 per item 21; the 2000 trade (MT148-C11-2) is in R1/R2.

2. Verdict line 3: the two accounts are of one trade.
- Find: `Named loser, numbers in the quotes, both men as witnesses. Rare, not codable.`
- Replace: `Named loser, numbers in the quotes, both men tell it; but it is one trade of one fund (Soros's), so one case, not two. Rare, not codable.`
Reason: MT151-C08-4 ("Quantum fund"), MT141-C06-2 ("push us back"): same fund, same trade; a second witness is not a second case.

3. Verdict line 4: the liquidity record is one loss and one win; M2SL covers the design years.
- Find: `Asserted; D's own 2018 trade on it lost (claim text); no series for the design years.`
- Replace: `Asserted; D's 2018 stock short on it lost (claim text), and his 2021 short of the 2-year on "money supply growing at 40 percent" gained by his account from 15 to 150 basis points (MT149-C07-1, MT151-C10-4; trade and year are claim text). Central-bank and Treasury series do not cover most design years (reader); M2SL does, and enters R2 only as a warning.`
Reason: MT149-C07-1 "that was a fat pitch"; MT151-C10-4 "from 15 to basis point to 150"; M2SL is on the data sheet and used in R2.

4. Verdict line 5: four rules, three actions, no spoken year.
- Find: `5. Dating: three rules rest on one recalled pre-2011 action each (2000, 1998-99, 1992); three are hindsight-flagged; nothing was recorded before 2018.`
- Replace: `5. Dating: four rules rest on three recalled pre-2011 actions (R1 and R2 on 2000, R3's stock leg on 1999, R5 on 1992), none dated by a year spoken in the quote; R3's bond leg, R4 and R6 are hindsight-flagged; nothing was recorded before 2018, so all six are hindsight under rule 5.`
Reason: section 9 lists Yes for R1, R2, R3 (stock), R5; years are claim text except "'99" (MT069-C06-3).

5. C1: the year 2003 is claim text.
- Find: `("we had nine percent nominal growth in the fourth quarter and we had one percent rate", SHOWN for 2003)`
- Replace: `("we had nine percent nominal growth in the fourth quarter and we had one percent rate", SHOWN: numbers in quote; the year 2003 is claim text)`
Reason: MT153-C13-4 quote has no year; "In 2003" is in its claim field.

6. C2 limits: the inflation reason and the 2018 short are mislabelled.
- Find: `Limits: off when inflation is high (2022-23, MT149-C07-3); his 2018 stock short on the same idea lost (claim text, MT152-C07-3).`
- Replace: `Limits: off when inflation is high (2022-23; claim text of MT149-C07-3, whose quote gives only the playbook and the "10-year yielding 350"); his 2018 stock short lost (claim text), but it was made on QT, chain C5, not on this chain ("because I saw a cutie coming", MT152-C07-3).`
Reason: MT149-C07-3 quote has no inflation; MT152-C07-3 quote names QT.

7. C5 limits: add the 2021 win.
- Find: `the short lost (claim text) and the ledger scores his 2018 liquidity calls wrong;`
- Replace: `the 2018 short lost (claim text) and the ledger scores his 2018 liquidity calls wrong; against that, he calls the 2021 front-end short on "money supply growing at 40 percent" "a fat pitch" (MT149-C07-1) and took it off "at like 150 basis points" from 15 (MT151-C10-4; trade and year are claim text);`
Reason: risk-officer balance; both quotes are his.

8. C6: "half a percent" is not shown to be a holding cost.
- Find: `SHOWN: holding cost "it was a half a percent" (MT151-C08-4)`
- Replace: `SHOWN: "it was a half a percent" (MT151-C08-4; whether this is the holding cost or the distance from the band is not in the quote, pack problem 9)`
Reason: MT151-C08-4 and MT085-C02-X1 claim fields give two readings; the quote gives neither.

9. Common rule text: vintages.
- Find: `Checked at each month-end with data as known then (lags above).`
- Replace: `Checked at each month-end with data as known then (lags above); series marked first-published on the data sheet (CPILFESL, M2SL) are used as first published where vintages exist, else latest values, flagged.`
Reason: hidden choice; M2SL is revised, the data sheet offers first-published values.

10. Common rule text: averaging.
- Find: `Two entry versions for every rule (section 6).`
- Replace: `Two entry versions for every rule (section 6); every version of a rule is run and averaged.`
Reason: shop rule 2; the card never states it.

11. R1: splice of two dollar indexes.
- Find: `the dollar index (TWEXMMTH to its last month, DTWEXBGS after)`
- Replace: `the dollar index (TWEXMMTH to its last month, DTWEXBGS after; each L-month change is taken inside one series, reader)`
Reason: a change across the splice would compare two different indexes.

12. R1 versions: gate on or off.
- Find: `Versions: L 6 or 12; rate FEDFUNDS or GS10 (4).`
- Replace: `Versions: L 6 or 12; rate FEDFUNDS or GS10; R4 gate on or off (8).`
Reason: the gate is a choice made with 2022-23 knowledge from claim text (item 13); an open choice becomes a version.

13. R1 gate reason: label the claim text and the hindsight.
- Find: `That gate is the reader's link from MT149-C07-3, where he declines his usual hedge with the "10-year yielding 350", to the 5% test of MT148-C02-2.`
- Replace: `That gate is the reader's link, made knowing 2022-23, from MT149-C07-3 to the 5% test of MT148-C02-2; the quote of MT149-C07-3 gives only his usual Treasury playbook and the "10-year yielding 350", and that he declined it for inflation is claim text, so the gate is a version, not a fixed part of the rule.`
Reason: MT149-C07-3 quote; v2 rule 3.

14. R2 versions: same gate.
- Find: `Versions: T 6 or 12 (as R1); k 2 or 3 (4).`
- Replace: `Versions: T 6 or 12 (as R1); k 2 or 3; R4 gate on or off (8).`
Reason: as item 12.

15. R3: define the median window and the S&P series.
- Find: `BAA minus GS10 is below its expanding-window median, and the S&P 500 is above its 10-month average: short US 10-year bond, long S&P 500.`
- Replace: `BAA minus GS10 is below its expanding-window median (window from the first month both series exist), and the S&P 500 price level is above its 10-month average (panel index; Compass spx_trend live): short US 10-year bond, long S&P 500.`
Reason: the panel holds excess returns; the level and the window start were hidden choices.

16. R3: gold series.
- Find: `gold at a 12-month high required or not`
- Replace: `gold (panel gold; GC=F live) at a 12-month high required or not`
Reason: series id missing.

17. R3 hindsight: right quote for 1999, and how it ended.
- Find: `Hindsight: the stock leg has a recalled 1998-99 action;`
- Replace: `Hindsight: the stock leg has a recalled 1999 action ("Everyone knows how I played the Nasdaq melt up in '99", MT069-C06-3; its link to the Fed's easing is claim text of MT151-C11-2), and that episode ended when he "bought the exact top" and lost "two or three billion" (MT069-C06-3, MT148-C11-X1);`
Reason: MT151-C11-2's quote shows no action; MT069-C06-3 and MT148-C11-X1 do.

18. R4: define the commodity leg.
- Find: `A plus short S&P 500 and long the commodity basket`
- Replace: `A plus short S&P 500 and long the panel's commodities at equal risk (he names none: "some of the key commodities"; reader)`
Reason: MT148-C05-2 names no commodities; "basket" was undefined.

19. R4 hindsight: the omitted action.
- Find: `Hindsight: stated June 2022, no earlier action in a quote; flagged.`
- Replace: `Hindsight: stated June 2022; the only related action in a quote is after 2010, a short of the 2-year from 15 to 150 basis points (MT151-C10-4, MT149-C07-1; trade and year are claim text); flagged.`
Reason: MT151-C10-4 quote.

20. R5: scope and euro mapping.
- Find: `For each G10 currency in the panel other than the dollar:`
- Replace: `For each G10 currency in the panel other than the dollar whose stock index (and, for the bond version, 10-year bond) is in the panel; the mark and then the euro map to the German index and Bund (reader):`
Reason: hidden choices.

21. R6: the direction is not in the quote.
- Find: `Claim: MT203-C08-2 ("real rates started going up in the US nominal rates started going up", normally the sign of a pullback).`
- Replace: `Claim: MT203-C08-2 ("real rates started going up in the US nominal rates started going up", which he calls normally "a signal that you're going to get a 5 10 could be 15% pullback"). Premise check fails: the long direction and the rise in gold are claim text; on its words the quote points to a pullback. R6 is held back from registration until a quote supports the direction; question 8 covers gold meanwhile.`
Reason: BRIEF_V2 rules 3 and 6.

22. Analyst header: wrong citation for 12 months.
- Find: `(the men think 12 to 24 months ahead, MT151-C05-3)`
- Replace: `(D thinks 12 to 18 months ahead, MT046-C05-3, and 18 to 24, MT151-C05-3)`
Reason: MT151-C05-3 says 18 to 24.

23. Question 1: make it scoreable.
- Find: `1. Fed stance: one of tightening into weakness, easing into strength, behind on inflation, in step; and the chance FEDFUNDS is lower.`
- Replace: `1. Fed stance: chances that the R2, R3 or R4 condition (first-listed version of each, gate off) holds at the horizon, or none of them (in step), scored as one four-way Brier score; and the chance FEDFUNDS is lower.`
Reason: a label has no outcome; the rule states are computable.

24. Question 5: a count of today's data is not a forecast; horizons as the header.
- Find: `5. Leading industries: how many of ITB, IYT, XRT are 20% or more below their 12-month high (Compass window); chance the Compass jobs alarm is on at 26 and 52 weeks.`
- Replace: `5. Leading industries: chance that two or more of ITB, IYT, XRT are 20% or more below their 12-month high (Compass window); chance the Compass jobs alarm is on. Today's count is reported, not scored.`
Reason: header fixes 4, 13 and 52 weeks and probabilities.

25. Question 10: resolution horizon; label the ratio.
- Find: `Scored in units of the cap; weeks answered none are counted.`
- Replace: `Resolved at the cap, the target or 52 weeks, whichever comes first, and scored in units of the cap; weeks answered none are counted. The five-times ratio is the reader's; no quote gives it.`
Reason: no end date; 5x is in no quote.

26. Section 6: hot/cold sizing reason and B's own contradiction.
- Find: `Dropped for rules: it is about a person's judgement, not a formula.`
- Replace: `Dropped for rules: B's form ("adding if the p&l is good", MT141-C11-1) is a formula, but the shop fixes risk shares (5.1). As an allocator B does the opposite: "when they are in a slump you add" (MT141-C12-1).`
Reason: MT141-C11-1, MT141-C12-1 quotes; WORKFLOW 5.1.

27. Section 6: the tail contradicts the quote it claims to register.
- Find: `Registered: a rule exits on its condition and the 12-month clock only. No price stop: they give no level.`
- Replace: `Registered with a deviation: a rule exits 12 months after its condition last held, so it keeps the position for a year after the reason is gone, against this quote; the tail rests on MT151-C12-2 and MT046-C05-3 (section 4). No price stop: they give no level.`
Reason: MT151-C07-2 against the common rule of section 4.

28. Section 6: shorting row overstated.
- Find: `Shorting stocks rarely pays (MT046-C05-4, MT046-C05-X1, MT152-C07-5)`
- Replace: `Shorting stocks costs more when wrong, and his index shorts were "a disaster" in 2023 (MT046-C05-4, MT046-C05-X1, MT152-C07-5); but 2021-22 was "the best short-selling period I've ever seen" (MT148-C13-4)`
Reason: MT148-C13-4.

29. Forecasts: default horizon for MT069 from his own words.
- Find: `D's 2026 recording has no stated date (ledger: 2025).`
- Replace: `D's 2026 recording has no stated date (ledger: 2025). For its rows marked none, the default horizon is his stated trade horizon in the same recording, "18 months to 3 years" (MT069-C03-7; reader).`
Reason: makes those rows resolvable from a quote.

30. Forecasts: energy row direction.
- Find: `| D, 2022-06 | "we look to be short energy for 5 or 10 years" | 2027-06 to 2032-06 | WTISPLC against June 2022 |`
- Replace: `| D, 2022-06 | "we look to be short energy for 5 or 10 years": supply short, he is long energy (claim text) | 2027-06 to 2032-06 | WTISPLC higher than in June 2022 |`
Reason: the quote can be misread as a short position; ledger direction is up.

31. Forecasts: the second wave is an analogy.
- Find: `| D, 2024-10 | Second wave of inflation, as in the 1970s | none stated |`
- Replace: `| D, 2024-10 | Possible second wave of inflation, as in the 1970s (an analogy conditional on easy conditions; the claim text calls it not a forecast) | none stated, so not resolvable as stated |`
Reason: MT151-C01-3 and C01-X1 quotes and fields.

32. Forecasts: copper is claim text.
- Find: `| D, 2025 or 2026 | Copper "very tight for the next 8 years" |`
- Replace: `| D, 2025 or 2026 | Copper (claim text; the quote names no metal) "very tight for the next 8 years" |`
Reason: MT069-C03-4 quote.

33. Forecasts: Japan is claim text and hedged.
- Find: `Long-term bull market in gold; Japan a secular bull market`
- Replace: `Long-term bull market in gold; Japan "could be" a secular bull market (Japan: claim text)`
Reason: MT141-C13-3 quote.

34. Forecasts: oil row conditions and yardstick.
- Find: `once the conflict ends | medium term | WTISPLC against the pre-war level |`
- Replace: `once the conflict ends (claim text) | medium term | WTISPLC against a pre-war month the ledger fixes before any outcome is read (the level below 60 is summary only) |`
Reason: MT142-C08-1 quote has neither the condition nor the level.

35. Section 8: 2023 refusal is claim text.
- Find: `Treasuries were the bear-market trade until 2018 (MT152-C08-1) and not in 2023 (MT149-C07-3).`
- Replace: `Treasuries were the bear-market trade until 2018 (MT152-C08-1) and not in 2023 (claim text of MT149-C07-3; the quote gives only the playbook and the 3.50 yield).`
Reason: as item 6.

36. Section 8: the 70/30 split can be scored.
- Find: `His inflation-or-deflation views (MT148-C16-X1, MT149-C03-X2) cover both outcomes and cannot fail.`
- Replace: `His 2023 view (MT149-C03-X2) covers both outcomes and cannot fail; the earlier split "70% inflation ... 30% deflation" (MT148-C16-X1) is a probability and can be scored.`
Reason: MT148-C16-X1 quote.

37. Section 8: B against himself, not shown by the cited pair.
- Find: `The Secretary of 2026 calls the Treasury market the most solid in the world (MT142-C02-2).`
- Replace: `The Secretary of 2026 calls it (the Treasury market, by the claim text) "the deepest, most liquid, and most most solid in the world" (MT142-C02-2). The quotes do not contradict each other; the clear case of B against himself is in sizing (section 6: MT141-C11-1 against MT141-C12-1).`
Reason: MT142-C02-2 quote names no market; the two statements are compatible.

38. Section 8: gold link of the release valve.
- Find: `Gold. B: reserve buying and the fiscal release valve (MT141-C12-6, MT203-C08-4).`
- Replace: `Gold. B: reserve buying (MT141-C12-6) and the fiscal release valve (MT203-C08-4; its link to gold is claim text).`
Reason: MT203-C08-4 quote does not mention gold.

39. Dating table R1.
- Find: `| R1 squeeze | Yes, 2000 (MT153-C10-5, MT151-C12-4); recalled 2018 to 2024 |`
- Replace: `| R1 squeeze | Yes by context: the 350% position "betting that Greenspan ... will reverse" (MT148-C11-2, MT151-C12-4) falls in Greenspan's tenure, before 2006 (reader); no year is spoken, 2000 is claim text; recalled 2018 to 2024 |`
Reason: rule 5 asks for words in the quote; MT153-C10-5 and MT151-C12-4 carry no date.

40. Dating table R2.
- Find: `| R2 tightening into warnings | Yes, 2000 (MT148-C11-2); the three warnings are from 2018 |`
- Replace: `| R2 tightening into warnings | Yes by context, as R1 (MT148-C11-2 names Greenspan; 2000 is claim text); the three warnings are from 2018 |`
Reason: as item 39.

41. Dating table R3.
- Find: `| R3 easing into strength | Stock leg: yes, 1999 (MT151-C11-2). Bond leg: no |`
- Replace: `| R3 easing into strength | Stock leg: yes, 1999 ("the Nasdaq melt up in '99", MT069-C06-3; the Fed link is claim text of MT151-C11-2). Bond leg: no |`
Reason: as item 17.

42. Dating table R5.
- Find: `| R5 after the fall | Yes, 1992 (MT151-C09-6); B's case is 2012-13 |`
- Replace: `| R5 after the fall | Yes by context (Quantum Fund, the pound's band: MT151-C08-4, MT151-C09-6); 1992 is claim text; B's case is 2012-13 |`
Reason: no quote says 1992.

43. D1: which versions count.
- Find: `For each rule, count separate episodes (on-months at least 12 months apart).`
- Replace: `For each rule, count separate episodes (on-months at least 12 months apart), taking a month as on when any registered version of the rule is on.`
Reason: with 4 to 8 versions the count was undefined.

44. D2: reference book exists before the tests.
- Find: `the share of on-months in which the Core book holds that market with the same sign.`
- Replace: `the share of on-months in which the registered systematic pods combined (Trend, Economic trend, Carry, Value, as specified at registration) hold that market with the same sign.`
Reason: Core is decided only after B1/B2 (WORKFLOW 4.4); B2 runs the rule layers.

45. Pack problems: MT152 dating.
- Find: `6. MT069 has no recording date: upload February 2026, ledger 2025.`
- Replace: `6. MT069 has no recording date: upload February 2026, ledger 2025. MT152 was uploaded 2020-01-06, but its content and the ledger date it December 2018 (MT152-C02-2, MT152-C05-X1); the card uses December 2018.`
Reason: SOURCES upload date 2020-01-06; FORECASTS made_date 2018-12.

## 4. Open judgement points
1. R6: drop it, or keep it as a short-gold rule on B's literal words (rising real and nominal rates signal a pullback), which runs against his stated gold view; closes at 1.5 (look for a supporting quote) or 3.2.
2. The 12-month tail against "sell when the reason is gone": keep fixed (quoted horizon) or add a no-tail version; closes at 3.1-3.2.
3. Whether the R1/R2 gate should exist at all once it is a version (it carries 2022-23 knowledge into the design era, mainly 1974-81); closes at 3.2.
4. Dollar index: splice of TWEXMMTH (majors) and DTWEXBGS (broad), or DX-Y.NYB throughout; closes at 3.1.
5. Core CPI for D's CPI test: episode set differs from headline (1970s, 2022); no headline series on the sheet; closes at 3.1.
6. R5 trigger versus the dollar relative to a median may miss a break inside a peg where neighbours fall too (1992); check with D1 episode dates at 3.2.
7. Question 9 lets the analyst pick its events; easy events flatter the Brier score; scoring rule for self-chosen events at the ledger's next rules version (2.2).
8. Evidence grade of C6 when both accounts are one trade; closes at 1.5.
9. GS2 may start after 1975-01, which would shorten R2's warning (a) and R1's 2-year leg is unaffected; closes at 3.1 (series start dates).
10. Whether B's 2026 official statements belong in the forecast ledger at all (row MT142-C08-1) given the card treats them as an official's; closes at 2.3.

## 5. What I could not verify
- Series start dates (GS2, TWEXMMTH, DTWEXBGS, WALCL, WTREGEN, RRPONTSYD, panel gold, first-published vintages): not in the pack; statements about them are reader knowledge.
- Years of recalled trades (1987, 1992, 1999, 2000, 2003, 2012-13, 2021): only "'99" is spoken; the rest are claim text or context.
- What "a half a percent" was (forward cost or distance from the band).
- Recording dates of MT069, MT203 (pre-August 2024 rests on the Kishida reading, reader), MT152 (content, not upload).
- Outcomes of the open forecasts (not looked up, as instructed); the digest's base-rate arithmetic beyond the pool A+B row count.
- Auto-caption accuracy of the quotes ("cutie" = QT, "guilts" = gilts, "Fords" = forwards are readings).
