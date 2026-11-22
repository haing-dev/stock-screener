---
tags: [fable, thesis]
code_commit: 9f052b1
---
> Opus 5.5 high, against the verbatim quotes. See [[Card 1.4 - Regime and debt cycle]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/9f052b1186e6c2b05f93c46a14f5b82238ca8d9a/docs/research/fable/CARD_1.4_regime_debt_cycle_check.md).
# Independent check of playbook card 1.4 (2 of 5): regime and debt cycle (Bridgewater)

Checker: Opus (quant and risk officer), 2026-11-22. Card: fable_work/CARD_1.4_regime_debt_cycle.md. Ground truth: the "quote" field of all 183 claims in pack/CLAIMS.json (all read), plus FORECASTS.csv, DATA_SHEET.md, DIGEST.md, SOURCES.md, WORKFLOW sections 1-6. Every quoted phrase in the card was matched by script (opus_work/qcheck.py) and every claim id with tools/lookup.py.

## 1. Verdict

PASS WITH CORRECTIONS (29 corrections, none changes a rule's direction or removes a rule).
Quotes: 77 quoted phrases, all verbatim, all under the right id; 82 ids cited, 81 in the pack, the 82nd ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C14-4|MT058-C14-4]]) cited correctly as missing. Numbers: about 45 checked, 0 contradicted, 5 summary-only numbers all labelled correctly; ledger figures match FORECASTS.csv; one count inconsistent (1 disputed row stated, 2 disputed in the card's own pack problems).
Misreadings: 7 places where claim text is presented as a quote's content (zero-rate hedge on [[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-2|MT138-C06-2]], "falling together" on [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-3|MT068-C10-3]], tariffs inflationary, referent of [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C18-2|MT068-C18-2]], losses on bonds, aggregate profit identity, KT's "mechanical answer" read as support); 2 dating errors ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-2|MT058-C05-2]] names 2008); 2 forecasts listed as open that are not (F8 closed, F9 has no horizon).
Rules: R1 and R2 are codable from the data sheet with explicit grids; R1 overlaps card 1's R4 in the 1970s and its "Value may hold it" note contradicts DIGEST C (Value is cross-asset only); R2's labour gate was off when KT spoke (checker's recollection). Both stay Incubator at best; D2 gains an overlap gate, D1 gets a defined scope.
Omissions (D): RD's named debt dynamic ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-3|MT058-C05-3]]), BP-versus-GJ on overriding the system ([[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C05-2|MT049-C05-2]] against [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C15-2|MT068-C15-2]]), GJ's real-rate case for bonds ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-X1|MT068-C10-X1]]) is RD's mechanism, not a disagreement.

## 2. Findings

### A. Numbers

In quote and correctly used: 1.5 points, 10-year stream, 15% ([[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C04-4|MT147-C04-4]]); 30 and 3 ([[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C04-2|MT147-C04-2]]); up to 80% ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C04-2|MT058-C04-2]]); 25-year duration, 2 to 2.5 times leverage, 40 years to zero ([[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C07-2|MT049-C07-2]]); 8% of GDP ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C07-1|MT058-C07-1]]); "two and a half", "three range" ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C08-1|MT068-C08-1]]); 2.5 growth with 1.5 from AI ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C08-X2|MT068-C08-X2]]); 15 years ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C09-3|MT068-C09-3]]); 2008 crisis ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-2|MT058-C05-2]]); 1930s ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C12-2|MT058-C12-2]]); "26" ([[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C03-4|MT138-C03-4]]).
Summary only, labelled so by the card: Japan 300% / Brazil 60-80% ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C09-1|MT068-C09-1]] claim), breakeven 2.25-2.5 ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C08-1|MT068-C08-1]] claim), 1 point of 2% growth ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C07-4|MT068-C07-4]] claim), five times the capital ([[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C07-1|MT049-C07-1]] claim), 5-10% of world GDP ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C11-1|MT058-C11-1]] claim; the quote has 5 to 10 trillion dollars). Correct.
Ledger, checked against FORECASTS.csv: 13 resolved rows, hits on MT138-V002-1, MT138-V003-2, MT138-V004-2, MT138-V006-1, MT147-V004-1 = 5 of 13 (correct); S&P 3,825.33 to 4,450.38 = +16.3% (correct); MT068-V002-1 end value 2.0657, resolved 2026-10-30, end target 2026-12-30, level "2 to 2.5%" (pack problem 2 correct); [[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-5|MT138-C06-5]] direction field "long oil, caution gold" (pack problem 3 correct); the four missing claim ids (pack problem 10) confirmed NOT FOUND. Inconsistency: verdict 4 says "one row disputed" while pack problems 2 and 3 dispute two scored rows (5 of 11 without them). Corrected (item 2).
Reader's arithmetic: 25 uncorrelated equal bets for an 80% cut (1 - 1/5) and a cap near 68% at correlation 0.1 (1 - sqrt 0.1) are both right.
Speaker's arithmetic, not flagged by the card: a level 10-year earnings stream has a duration near 5 (annuity at 3%: about 5.2), so 1.5 points imply about 7.5%, not 15%; KT's 15% treats the stream as one payment in year 10. R2's multiplier 10 is in the quote, so it stays, but the self-check should say it is loose on her own premise (item 28).
Reader's thresholds are all listed in section 12 except "worst fifth" (D1), "two dissents" (question 9), 3.0 (question 8, from "three range"); none carries a hidden result.

### B. Causal chains and indicators

- Chain 1 (RD 2023): quotes right; "on bonds" for [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C14-X1|MT058-C14-X1]] is claim text (item 5). RD's own named dynamic, "debt creation and debt monetization that whole dynamic and last time that happened was in 1930 to 45 period" ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-3|MT058-C05-3]]), is the closest the pack comes to the debt-cycle framework and is not cited anywhere; the verdict's "none ... states ... a debt-cycle template" is too strong (item 1).
- Chain 2 (GJ 2025): correctly marks directions as claim text. But the indicator table, question 3 and section 8 then use "all three fall together" as if quoted (items 11, 23).
- Chain 3: fine; "if politics forces rates down" is claim text of [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C08-2|MT068-C08-2]] (minor, not corrected).
- Chain 4 (KT 2022): the quote of [[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C01-1|MT147-C01-1]] gives two routes ("raise revenue or get people to pay ... without paying labor"); "only if" and the aggregate identity are claim text (item 6). "A mechanical answer" ([[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C01-X2|MT147-C01-X2]]) is cited as support, but her sentence limits the identity: people "have to choose to borrow for a reason" (item 7).
- Chain 5: arithmetic correctly labelled; see A for the duration point.
- Chain 6: correct; the Fed-stuck reading is claim text but the card says "perhaps".
- Chain 7: [[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-2|MT138-C06-2]] is about duration and currency ALPHA ("great alpha spaces ... coming back in a big way"), not about the hedge; the zero-rate failure of the hedge is the conditions field of [[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-X1|MT138-C06-X1]]. KT's 2022 line "rates were already zero it was sort of a breaking point of the paradigm" ([[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C02-X2|MT147-C02-X2]]) is the quote that fits (item 8).
- Chain 8: "You get tariffs" does not say inflationary (item 9); the referent of "I thought it would have bigger impact" is claim text (item 10).
- Speakers and levels: kept apart well; NY is marked second-hand. Chain 7 merges BP's 1980s-style mandate and KT's 2025 client remark under "firm-level", labelled as such: acceptable.
- Indicators: every series id is on the data sheet (GS10, CPILFESL, THREEFYTP10, WALCL, UNRATE, TB3MS, T5YIFR, the IR3TIB01 series; Compass realyield, stockbond, y10_chg). Lags match the sheet.

### C. Rules

R1 (Not paid to hold).
- Series GS10 and CPILFESL on the sheet, lags 0 and 1, holding rule "no tail", action short US 10-year: complete. Bar grid 0.0 / expanding lowest third (min 120 months) with reasons; hedge gate (12-month correlation above zero) marked reader. No look-ahead (expanding window).
- Direction: RD's quote supports "holders leave when the real return is not high enough" ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C06-3|MT058-C06-3]]) and "rates Rising a lot" as one branch ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C07-2|MT058-C07-2]]); printing as the other branch is claim text, which the card says. GJ 2025 ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-X1|MT068-C10-X1]]) states the same test from the other side (real rates rose, so bonds have a place): it supports the mechanism, and the card lists it as a disagreement (item 21).
- Overlap: at bar 0 the rule is on when GS10 is below core CPI growth, which in 1975-1981 coincides largely with card 1's R4 state (core CPI above 5 and Fed funds below it; reader). Card 1 R4 action A also shorts the US 10-year, so in design months R1 partly double-counts card 1. The card's "R1 does not need 5.0" is true but does not address it (item 12, D2 gate item 27).
- "Value may hold this position if its bond anchor is a real yield": DIGEST C registers Value "cross-asset only", so Value holds no directional US bond position (items 12 and 29).
- WALCL stop line: WALCL starts in late 2002 (checker's recollection, not the pack); the card leaves unclear whether it gates the backtest (item 20).
R2 (Rates-only repricing).
- Series GS10, S&P 500 (panel; SPY live), UNRATE (first-published, lag 1): on the sheet. Threshold 1.5 and multiplier 10 in quote; 1.0, 240 months reader with reasons; 12-month window and 12-month hold borrowed from the Compass and card 1, stated. Direction (short stocks) is supported by [[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C05-1|MT147-C05-1]] and [[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C05-2|MT147-C05-2]].
- Hidden choice, weak: the 12-month yield window is not hers; her 1.5-point example matches a rise of about 1.4 points from December 2021 to May 2022, roughly five months (checker's recollection). Left as an open point.
- June 2022 (card's request b), checker's recollection, not the pack: GS10 rose about 1.11 (April), 1.28 (May), 1.62 (June) on a year earlier; S&P 12-month change about -1%, -2%, -12%. So X = 1.0 was on from end-April, X = 1.5 from end-June; condition (ii) held. UNRATE was 3.6 in April and May 2022 against 3.5 in September 2019 and February 2020, so the labour gate (at or below the 240-month low) was OFF when she spoke: the quote's "tightest labor market in decades" is not what UNRATE measured then (item 28).
- Overlap with card 1's R4-B (short S&P above 5% core inflation) is limited to 1978-81 (reader); covered by the same D2 gate.
- D2 likely drops the labour-gated versions (one episode, 1999-2000, reader's expectation); that is the gate working, not a defect.
"Not rules" list: duplicates of Economic trend and Trend are named; the claim that Economic trend or Trend would hold the cross-country bond spread from chain 6 is a guess, correctly deferred to 3.2.

### D. All 183 quotes: contradictions, omissions, attributions, duplicates

Contradictions with the card:
1. [[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-2|MT138-C06-2]] is about alpha returning, not the hedge failing (chain 7; item 8).
2. [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C15-2|MT068-C15-2]]: GJ's quote makes systemizing a new shock the mistake; the card uses it to back "no override of the rule layer" without saying the quote points the other way (item 16).
3. [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-X1|MT068-C10-X1]] is RD's real-return test met, not a disagreement with RD (item 21).
4. [[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C07-2|MT049-C07-2]]: the mandate "could shift the duration from uh 40 years all the way down to zero": an active duration book, not a standing long-bond hedge as "founding story" implies (item 22).
5. [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-2|MT058-C05-2]] names the 2008 crisis: the card twice says "no year" / "neither is dated" (items 3, 24).
Important omissions:
- RD: [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-3|MT058-C05-3]] (debt creation and monetization, 1930-45 dynamic), [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C06-1|MT058-C06-1]] (five forces), [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C06-4|MT058-C06-4]] (transfers above lost income drive spending), [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C07-1|MT058-C07-1]]'s loop (central-bank losses need recapitalisation, adding to deficits; the 8% is used only as context), [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-1|MT058-C05-1]] (surprises are events outside one's lifetime: study history).
- GJ: [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C15-1|MT068-C15-1]] (survival came mainly from "risk control"); [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C02-3|MT068-C02-3]] (look beneath the index: "split up the equity market"); [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C08-X1|MT068-C08-X1]] (AI J-curve: disinflation comes later), relevant to F1 and question 8.
- BP: [[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C05-2|MT049-C05-2]] (code the view "and now you're going to live with it"), which disagrees with GJ's COVID lesson; [[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C04-2|MT049-C04-2]] (checks a forecaster's past reports), which backs the forecast ledger; [[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C06-1|MT049-C06-1]] (businesses = operating margin plus a market bet).
- KT: [[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C01-3|MT138-C01-3]] ("Markets have barely started pricing in") and [[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C01-X1|MT138-C01-X1]] (prices assume the US keeps beating), the 2025 form of chain 5's "what is priced"; [[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C04-1|MT147-C04-1]] and [[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C03-5|MT147-C03-5]]/C03-6 (margin headwinds: inelastic inflation, globalisation done, taxes at lows), the rest of chain 4.
- NY: [[MT053 - Episode 4- Noah Yechiely - Former Head of Equities at Bridgewater Associates#^MT053-C01-X1|MT053-C01-X1]] ("all assets tends to go up and down together"), the plainest statement in the pack of why diversification needs uncorrelated streams.
Attribution: no statement of one speaker is given to another. "Modern mercantalism" is cited to KT ([[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C01-2|MT138-C01-2]]) though BP uses it too ([[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C11-2|MT049-C11-2]], cited in the same sentence): fine.
Duplicates: R1 with card 1 R4 (1975-81, reader), R2 with card 1 R4-B (1978-81), neither with Economic trend as far as the pod descriptions go; growth/inflation regime rules correctly dropped as Economic trend duplicates.

### E. Dating table

- Debt squeeze: "no year" is wrong; [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-2|MT058-C05-2]] is dated before 2011 by the event it names, but it is a use of 1930s history, not of R1's real-yield test, and no trade is described. Flag stays hindsight (item 24).
- Rates-only repricing: live 2022, flagged: correct.
- Levered bond mandate: undated in the quote, correct; "first" and the client are claim text ([[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C07-1|MT049-C07-1]]).
- Diversification: undated in the quote; the 1982 context is claim text ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C04-1|MT058-C04-1]]): correct.
- [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C04-1|MT058-C04-1]] ("August 1982 ... the exact bottom ... the Dow was at 777") is a dated pre-2011 market fact, but his action is claim text; not a thesis for a rule. No row needed.
- "Both rules are Incubator at best": consistent with WORKFLOW 6 (rule layers run in B2 for Incubator status only).

### F. Rules of the shop

- No decision is handed to the user. Every open choice is a version, a diagnostic or dropped, except R2's 12-month yield window (fixed by convention, stated) and F1's core-versus-headline choice (open points).
- Versions averaged: yes; D2 removes thin versions by a fixed gate.
- D1: the gate is fixed but its consequence targets "every rule of cards 1 and 2 that buys bonds as a hedge": no rule in either card buys bonds as a hedge, so as written it can change nothing; and "30 low-rate months" does not say pooled or per country (items 25, 26).
- D2: "on-months" for R2 is ambiguous (condition months or the 12-month hold) (item 27).
- Analyst questions: answerable and Brier-scoreable, except question 1, which resolves on GS10, a monthly average that cannot settle a 4-week question (item 14). "Fixed asset list" in question 10 is the W3 list of the workflow: fine.
- Forecasts: F8's default window closed in May 2026 (pack problem 11) and F9 has no horizon ("forever") and no live series; neither is an open, scoreable forecast (items 4, 18, 19). F2's "calendar 2026" comes from view text (item 17).

## 3. Required corrections

1. Verdict 1: the debt-cycle claim is too strong.
- Find: `The framework the brief names is not in the quotes: none of the 183 states growth and inflation regimes, risk parity, or a debt-cycle template.`
- Replace: `The framework the brief names is not laid out in the quotes: none of the 183 states growth and inflation regimes or risk parity; the nearest to a debt-cycle template is RD naming a recurring dynamic, "the amounts of debt creation and debt monetization that whole dynamic and last time that happened was in 1930 to 45 period" ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-3|MT058-C05-3]]), with no stages or thresholds; NY's growth-and-inflation remark is second-hand ([[MT053 - Episode 4- Noah Yechiely - Former Head of Equities at Bridgewater Associates#^MT053-C03-3|MT053-C03-3]]).`
Reason: [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-3|MT058-C05-3]] states a recurring debt dynamic; omitting it misstates what the pack holds.

2. Verdict 4: disputed-row count.
- Find: `Ledger (machine-coded): 5 of 13 resolved rows right, one row disputed;`
- Replace: `Ledger (machine-coded): 5 of 13 resolved rows right; this card disputes two of them (MT068-V002-1 resolved early, MT138-V005-1 not scoreable; pack problems 2 and 3), leaving 5 of 11;`
Reason: pack problems 2 and 3 dispute two scored rows, both scored wrong.

3. Verdict 5: RD's use of history is dated by its quote.
- Find: `Two pre-2011 actions are recalled (BP's levered bond hedge, RD's use of 1930s history); neither is dated in its quote and neither carries a rule.`
- Replace: `Two pre-2011 uses are recalled: BP's levered bond-futures mandate (no year in the quote) and RD's use of 1930s history, which the quote ties to the 2008 crisis ("that understanding of History led me to be able to anticipate the 2008 financial crisis", [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-2|MT058-C05-2]]), so it is dated before 2011; neither quote describes a trade, and neither carries a rule.`
Reason: [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-2|MT058-C05-2]] names the 2008 crisis.

4. Verdict 6: open-forecast count.
- Find: `6. Counts: 2 rules, 10 analyst questions, 9 open forecasts, 2 diagnostics.`
- Replace: `6. Counts: 2 rules, 10 analyst questions, 7 open forecasts (F1-F7; F8's window has closed and F9 has no horizon or live series, both kept as context), 2 diagnostics.`
Reason: F8 is closed (pack problem 11); F9 cannot resolve.

5. Chain 1: "on bonds" is claim text.
- Find: `investors who "all lost a lot of money" on bonds ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C14-X1|MT058-C14-X1]])`
- Replace: `investors who "all lost a lot of money" ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C14-X1|MT058-C14-X1]]; that the losses are on bonds is claim text)`
Reason: the quote does not name the asset.

6. Chain 4: the quote gives two routes; the identity is claim text.
- Find: `A business grows its margin only if people pay "without paying labor" ([[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C01-1|MT147-C01-1]]).`
- Replace: `A business grows its margin if it can "raise revenue or get people to pay for its products without paying labor" ([[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C01-1|MT147-C01-1]]); that aggregate profits need non-wage spending is claim text.`
Reason: "only if" drops the revenue route in the quote.

7. Chain 4: "a mechanical answer" limits the identity.
- Find: `SHOWN (words): an accounting identity, which she calls "a mechanical answer" ([[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C01-X2|MT147-C01-X2]]).`
- Replace: `SHOWN (words): an accounting identity, which she herself limits: "that's a mechanical answer right these are all people governments individuals businesses they have to choose to borrow for a reason" ([[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C01-X2|MT147-C01-X2]]); the identity alone does not say that borrowing will fade.`
Reason: the full quote qualifies, not supports, the chain.

8. Chain 7: [[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-2|MT138-C06-2]] is about alpha, not the hedge.
- Find: `The hedge had no room "where rates were zero" ([[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-2|MT138-C06-2]]).`
- Replace: `That the hedge had no room at zero rates is claim text ([[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-X1|MT138-C06-X1]]); the quotes say only that "rates were already zero it was sort of a breaking point of the paradigm" (KT 2022, [[MT147 - Sohn 2022 - A Macro Approach with Karen Karniol-Tambour#^MT147-C02-X2|MT147-C02-X2]]) and that duration and currency alpha "seemed uninteresting for a while where rates were zero and are kind of coming back in a big way" ([[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-2|MT138-C06-2]]), which is about alpha, not the hedge.`
Reason: misreading of the cited quote.

9. Chain 8: tariffs-inflationary is claim text.
- Find: `It is inflationary: "You get tariffs" ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C07-2|MT068-C07-2]]), and`
- Replace: `GJ calls it inflationary: "You get tariffs" ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C07-2|MT068-C07-2]]; the inflation link for tariffs is claim text), and`
Reason: the quote names tariffs without saying inflationary; only [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C07-3|MT068-C07-3]] says inflationary.

10. Chain 8: referent of GJ's concession.
- Find: `GJ concedes: "I thought it would have bigger impact than it has" ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C18-2|MT068-C18-2]]).`
- Replace: `GJ concedes: "I thought it would have bigger impact than it has" ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C18-2|MT068-C18-2]]; that "it" is mercantilism is claim text).`
Reason: the quote does not say what "it" is.

11. Indicators: "falling together" is claim text.
- Find: `| Bonds, currency, stocks falling together | GJ ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-3|MT068-C10-3]]) |`
- Replace: `| Bonds, currency, stocks falling together | GJ: the quote says only that the correlation "will shift" ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-3|MT068-C10-3]]); falling together is claim text of [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C08-3|MT068-C08-3]] |`
Reason: chain 2 itself marks directions as claim text.

12. R1: Value is cross-asset only; overlap with card 1 R4.
- Find: `Value may hold this position if its bond anchor is a real yield (check at 3.2); card 1's R4 needs core inflation above 5.0 or 4.5, R1 does not.`
- Replace: `Value is registered cross-asset only (DIGEST C), so it holds no directional US bond position, at most a relative one (check at 3.2); card 1's R4 needs core inflation above 5.0 or 4.5, R1 does not, yet in 1975-1981 the two are probably on together (reader), so D2 measures the overlap.`
Reason: DIGEST C; card 1 R4 action A also shorts the US 10-year.

13. R2: hold reason states that the yield window is not hers.
- Find: `The 12-month window is the Compass one for the yield;`
- Replace: `The 12-month window is the Compass one for the yield, not hers (her example gives no window);`
Reason: make the borrowed lookback explicit as a reader's choice.

14. Question 1: GS10 cannot resolve a 4-week question.
- Find: `1. Treasuries (chain 1): GS10 at least 0.25 higher.`
- Replace: `1. Treasuries (chain 1): the daily 10-year Treasury yield on the horizon date at least 0.25 higher than on the question date (public daily figure; GS10 is a monthly average and cannot resolve a 4-week question).`
Reason: resolvability.

15. Process, spread risk: NY's correlation remark belongs here.
- Find: `Already the shop's rule (equal risk).`
- Replace: `Already the shop's rule (equal risk). NY, second-hand: "all assets tends to go up and down together they are correlated" ([[MT053 - Episode 4- Noah Yechiely - Former Head of Equities at Bridgewater Associates#^MT053-C01-X1|MT053-C01-X1]]).`
Reason: omitted quote that bears on the rule.

16. Process, overrides: GJ's quote points the other way; BP disagrees with him.
- Find: `Registered: no override of the rule layer; would-be overrides are logged and scored (question 10).`
- Replace: `GJ's quote makes systemizing a new shock the error, and he puts survival on "risk control" ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C15-1|MT068-C15-1]]); BP takes the other side: "laying it out the way you think it works to the point that you've literally coded into the computer and now you're going to live with it" ([[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C05-2|MT049-C05-2]]). Registered: no override of the rule layer (BP's side and the shop's rule); GJ's side is carried by the analyst layer, whose would-be overrides are logged and scored (question 10).`
Reason: contradiction with [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C15-2|MT068-C15-2]] and an omitted disagreement inside the pack.

17. F2: horizon from view text.
- Find: `| calendar 2026 | full-year 2026 real GDP growth | [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C08-X2|MT068-C08-X2]] |`
- Replace: `| next year (view text; the quote names no year), read as calendar 2026 | full-year 2026 real GDP growth | [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C08-X2|MT068-C08-X2]] |`
Reason: the quote has no year.

18. F8: not open.
- Find: `| window closed 2026-05, never scored |`
- Replace: `| not open: default window closed 2026-05, never scored; to be scored late by the ledger, not counted as open |`
Reason: section title says "still open".

19. F9: not scoreable.
- Find: `| none | profits to GDP (no live series) |`
- Replace: `| none ("forever"); not scoreable, context only, not counted as open | profits to GDP (no live series) |`
Reason: no horizon and no live series.

20. Stop line: WALCL live only.
- Find: `R1's stop line for the spec: WALCL rising over 12 months.`
- Replace: `R1's stop-working line for the spec, read live only and not a gate in the backtest: WALCL rising over 12 months (WALCL starts in late 2002 on the checker's recollection, so it covers few design years).`
Reason: removes a hidden choice about the backtest.

21. Disagreements: GJ's bond line is RD's mechanism.
- Find: `GJ 2025: "there is a place for bonds in portfolios" ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-X1|MT068-C10-X1]]).`
- Replace: `GJ 2025: "interest rates have risen and real interest rates have risen such that there is a place for bonds in portfolios" ([[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-X1|MT068-C10-X1]]): RD's own real-return test, met two years later, so a different reading of the level, not of the mechanism.`
Reason: the truncated quote hid its condition.

22. Disagreements: BP's mandate was not a standing long.
- Find: `BP's founding story is a levered long-bond hedge.`
- Replace: `BP's recalled mandate held bond futures at 25-year duration but "could shift the duration from uh 40 years all the way down to zero" ([[MT049 - Episode 12- Bob Prince - Co-CIO of Bridgewater Associates#^MT049-C07-2|MT049-C07-2]]): an active duration book, not a standing long; that it was the first such mandate is claim text.`
Reason: quote content; "founding" is claim text.

23. Against card 1: chain 2's directions are claim text.
- Find: `chain 2 says that at a fiscal limit all three fall together, and`
- Replace: `chain 2's claim text (not its quotes) says that at a fiscal limit all three fall together, and`
Reason: consistency with chain 2's own limits.

24. Dating table: [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-2|MT058-C05-2]] names 2008.
- Find: `No action. History let him "anticipate the 2008 financial crisis" ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-2|MT058-C05-2]]): a recalled use, no rule, no year`
- Replace: `No action. History let him "anticipate the 2008 financial crisis" ([[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C05-2|MT058-C05-2]]): a use of the 1930s debt history dated before 2011 by the event it names, but no trade and nothing about the real-yield test of R1`
Reason: the quote carries a date; the hindsight flag for R1 still stands.

25. D1: the consequence targets rules that do not exist.
- Find: `a floor version (short rate at least 1.0) is added at step 3.1 to every rule of cards 1 and 2 that buys bonds as a hedge,`
- Replace: `a floor version (short rate at least 1.0) is added at step 3.1 to card 1's R1 and R2 (the rules that buy bonds on the expectation of easing; card 2 has no bond-buying rule),`
Reason: no rule in either card buys bonds as a hedge, so the gate could change nothing.

26. D1: define the month count.
- Find: `on at least 30 low-rate months,`
- Replace: `on at least 30 low-rate months among the worst-fifth months pooled across countries (Japan also reported apart),`
Reason: pooled or per country was unstated; Japan supplies most low-rate months.

27. D2: on-month definition and an overlap gate with card 1.
- Find: `Gate: a version with fewer than 24 on-months or fewer than 3 episodes is reported and left out of its rule's average; a rule with no version left is not run.`
- Replace: `On-months are months the condition holds, not months of R2's 12-month hold. Gate: a version with fewer than 24 on-months or fewer than 3 episodes is reported and left out of its rule's average; a rule with no version left is not run. Overlap gate, fixed now: a version of R1 or R2 whose on-months fall more than two thirds of the time in card 1's R4 state (either threshold) is reported and left out of its rule's average, since it would add mostly a position card 1 already holds.`
Reason: duplication with card 1 R4 (short 10-year; R4-B short stocks) in the 1970s.

28. Section 13: duration arithmetic, labour gate in 2022, Value.
- Find: `The 10-year stream is a round number; a longer one makes condition (ii) easier to meet.`
- Replace: `The 10-year stream is a round number; a longer one makes condition (ii) easier to meet, and on her own premise it is too long: a level 10-year stream has a duration near 5 (checker's arithmetic), so 1.5 points imply about 7.5%, not 15; the quoted 10 is kept. On the checker's recollection (not the pack) UNRATE was 3.6 in April and May 2022 against 3.5 in 2019-20, so the labour-gated versions were off when she spoke, and the 1.5-point rise she describes took about five months, not twelve.`
Reason: strongest arguments against R2 that the self-check missed.

29. Section 13, R1: Value cannot hold the directional trade; card 1 R4 may.
- Find: `Value may already hold the trade.`
- Replace: `Value can hold at most its relative form (it is registered cross-asset only), but card 1's R4 may hold much of it in the 1970s (D2).`
Reason: DIGEST C; overlap with card 1 R4.

## 4. Open judgement points

1. R2's yield window: add a 6-month version (her example rise took about five months) or keep 12 months only; closes at 3.1 (spec) with the version count fixed at 3.4.
2. R2's labour gate: UNRATE at a 240-month low did not fire in 2022; whether a different registered measure (LNS14024887 or a 12-month low) should replace it, or the gate is left to D2 to drop; closes at 3.2.
3. R1 symmetry: GJ's [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-X1|MT068-C10-X1]] implies the long side (high real yield, hold bonds); a long version is not in the card; closes at 3.1 (and would overlap card 1 R1/R2).
4. D2 overlap gate threshold (two thirds) is the checker's; 3.2 may set a different fixed number before any run.
5. D1 pooled count is dominated by Japan 1995-2010; whether Japan alone may trigger the floor version; closes at 3.1.
6. F1 resolves on core CPI (CPILFESL) though GJ does not say core or headline; ledger used headline CPI; closes at 2.2-2.3.
7. Question 9 (two dissents) is a proxy for F3 ("chairman may be in the minority"); a direct question (any meeting where the chair votes on the losing side) may be better; closes at W3 template.
8. R2's 10x multiplier: on her own premise about 5x; whether a 5x version is added (stricter condition (ii)); closes at 3.1.
9. Whether Economic trend or Trend really holds the cross-country bond spread of chain 6 (card's "not rules" list); closes at 3.2.

## 5. What I could not verify

- Anything outside the quotes: actual GS10, S&P, UNRATE values in 2021-22 and series start dates (THREEFYTP10 1990, WALCL late 2002) are the checker's recollection, as the card's are; they agree with the card's recollection.
- Which countries and years the panel's 10-year bond excess returns cover (D1 feasibility).
- What Value's second anchor is and what exactly Economic trend trades (DIGEST gives only the verdict lines).
- Card 1's two entry versions (not in the pack).
- Context around each quote (only the quote field is ground truth): e.g. whether RD's [[MT058 - Five Forces Shaping the Global Economy - With Ray Dalio, Founder of Bridgewater Associates#^MT058-C06-3|MT058-C06-3]] speaks of government bonds specifically (the claim says so; the quote says "that debt").
- Whether the R1 and R2 on-months overlap card 1's R4 as much as estimated; D2 will count it.

