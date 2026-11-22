---
tags: [fable, thesis]
code_commit: 8022603
---
> Opus 5.5 high, against the verbatim quotes. See [[Card 1.4 - Flows and volatility]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/802260310f098ba5e2b1020dc240e79a8c0d6e5f/docs/research/fable/CARD_1.4_flows_volatility_check.md).
# Independent check of card 1.4 #4, flows and volatility (Cem Karsan), 2026-11-22

Checker: Opus (quant and risk officer). Ground truth: the quote field of all 785 claims (all read), plus FORECASTS.csv (174 rows, 68 resolved), DATA_SHEET, SOURCES, DIGEST, WORKFLOW 1-6. No code, no web, no backtests.

## 1. Verdict

PASS WITH CORRECTIONS (26 corrections).
A: 173 ids cited; 160 are in the claims file, and the 13 that are not appear only in the card's own list of missing ledger ids (correct). Every quoted phrase in the card is in the quote of the id it cites (checked by script). About 60 numbers checked: none contradicted by a quote; 2 misplaced (the 10% put at month-end; "first season lost"); 1 ledger reading contradicted by the ledger's own levels (the 2026 pullback call); all ledger tallies in section 1 reproduce exactly (28 of 68; 26 of 64, base rate 0.344; stocks 5 of 18 = 5/7, 0/8, 0/3; volatility 5 of 15).
B-C: the chains are faithful and labelled with care; one speaker throughout, no misattribution found. Rules: R4 and R5 have the right direction; R1 form B cites a quote about a 20% fall for an up-year bar; R2's fixed N breaks his five-week figure; R3's gate is an unlabelled reader's bar; D1 would pass on volatility persistence alone; D2's Trend test reads one leg of a spread. No rule needs options data; every series is on the sheet (daily S&P history before 1993 is not confirmed by the sheet).
D-F: the falsifier "a calm that ends without a violent break" ignores his own repeated slow-grind path; the card-1 conflict on liquidity is overstated; omitted: the two-strong-years rule, his admission that the steepener was not playing out, technical levels. Dating table rests on quote words (correct: nothing before 2011 carries a rule). No decision is handed to the user.

## 2. Findings

### A. Numbers

In quote and correctly cited: 40% ([[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C08-3|MT031-C08-3]]); 1 to 1.5 and 2.5 weeks ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C08-4|MT076-C08-4]]); 95% ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C11-3|MT076-C11-3]], [[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C05-3|MT227-C05-3]]); 10% on 1 January and 100 billion a day ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C03-2|MT206-C03-2]], [[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C04-1|MT206-C04-1]]); 3% in 2017 ([[MT202 - Trump 2.0 & The Unpinning of Volatility - Systematic Investor 307#^MT202-C04-2|MT202-C04-2]]); four times ([[MT183 - The Volatility Apocalypse - Systematic Investor 303#^MT183-C01-1|MT183-C01-1]]); 13th to 15th January ([[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C11-1|MT132-C11-1]]); 50% in 4 years ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C13-2|MT206-C13-2]]); 20% ([[MT016 - America's 250-Year Reset feat. Cem Karsan - Systematic Investor - Ep. 407#^MT016-C05-3|MT016-C05-3]], [[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C05-2|MT206-C05-2]]); 12 to 18 months ([[MT126 - Politics, Markets & Power Plays - Systematic Investor 338#^MT126-C08-3|MT126-C08-3]]); 10 to 15 trillion ([[MT016 - America's 250-Year Reset feat. Cem Karsan - Systematic Investor - Ep. 407#^MT016-C05-5|MT016-C05-5]]); 200 trillion ([[MT104 - Market Structure, Liquidity, and Reflexivity in 2025 - Systematic Investor - Ep.368#^MT104-C16-2|MT104-C16-2]]); 5% yield and 10 days late ([[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C01-2|MT227-C01-2]]); real losses 70%, 67%, about 50%, 55-60% ([[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C10-2|MT132-C10-2]], [[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C07-3|MT227-C07-3]], [[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C16-1|MT163-C16-1]], [[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C11-4|MT031-C11-4]]); 5% and six-seven ([[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C10-1|MT132-C10-1]], [[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C16-1|MT031-C16-1]]); 211% ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C13-5|MT076-C13-5]]); 30 to 50% ([[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C17-1|MT163-C17-1]]); 90% ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C06-2|MT206-C06-2]]); 40 ([[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C12-3|MT150-C12-3]]); 5 to 10 years ([[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C06-3|MT031-C06-3]]).
Summary only, correctly tagged: 125 years, the 2025 Feb-March fall, 250 and 300 trillion, 6.5%.
Ledger numbers: 6075.11, 5842.91, 6966.28, 7722.72, 5667.56, 7537.43, 4.77 all match FORECASTS.csv. Tallies in section 1 reproduce exactly. "Scored on the VIX": 11 of the 15 volatility rows (2 on MOVE, 2 on gold).
Problems:
- C3: "call it about 10%" is the share that comes in on 1 January; the card says it arrives "then", meaning month-end and 1 January.
- R1 ledger sentence and section 13: "first season lost" uses the 2024-12-05 start; the row that follows his first statement (MT206-V001-1, 2024-10-01 to 2025-01-14) gained 2.35% and is scored right. Neither is an R1 entry day.
- R3: the 2026 pullback row (MT104-V001-2) is scored from 2025-10-13; the ledger's own levels show the S&P 2.65% lower on 2026-03-10 (6781.48) than on 2026-01-09 (6966.28). It cannot count as a miss of a January-February pullback. Conversely, by ledger levels the 2025 window 1 lost (5842.91 on 2025-01-14, 5994.57 on 2025-02-03, +2.6%).
- Reader numbers are tagged (N, d, 10 days, 0.25, 6 months, 1.25, 0.80, half size, 5% in Q6, 3.0 in F8), except R3's gate (correction 7).

### B. Causal chains and labels

C1-C8 match their quotes. Labels are conservative and correct (SHOWN only for the 2020 expiry-to-expiry case, SHOWN (words) for the offset logic and the re-leveraging arithmetic). The card keeps K's mechanism claims apart from his dated views and from his firm's "we" calls; "no firm process is described" is fair ([[MT016 - America's 250-Year Reset feat. Cem Karsan - Systematic Investor - Ep. 407#^MT016-C13-1|MT016-C13-1]] names a three-leg frame, but the quote is a fragment, "There's three majors. There's flows.").
- C3: the 10% placement (above).
- C2/R2: that the support sits before X rests on reading "for the next two weeks" ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C07-4|MT076-C07-4]], ledger made date 2024-04-25) against a 17 May 2024 expiry (checker's knowledge), and on [[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C03-1|MT031-C03-1]] ("the week leading into it and the week of"); [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C06-X1|MT076-C06-X1]]'s "that weekend" is probably the weekend of the April 2024 Iran attack ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C05-4|MT076-C05-4]] speaks of a long weekend), so the card is right to call it claim text. Placement accepted with that caveat (judgement point 1).
- Section 8: "Year-end is always strong ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C04-2|MT206-C04-2]])": no quote says always; the claim text of [[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C04-2|MT206-C04-2]] itself puts almost all window gains in up years, so it may agree with [[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-2|MT163-C20-2]] rather than conflict.
- Section 8: "Two falls did come inside their windows": [[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C09-4|MT132-C09-4]] says the 2024 fall came early ("It happened early"); only the 2025 fall (MT227-V002-1) came inside its window.
- Section 8, card 1: K agrees liquidity drives prices ("markets are a function of liquidity", [[MT104 - Market Structure, Liquidity, and Reflexivity in 2025 - Systematic Investor - Ep.368#^MT104-C02-2|MT104-C02-2]]; "QT QE different story direct impact on markets", [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C13-2|MT076-C13-2]]); he differs on its main source. "Conflicts with its title idea" overstates.
- Section 9 and 13 label outside facts "checker's knowledge" although the writer supplied them. The checker confirms them: January and turn-of-month effects (Rozeff and Kinney 1976; Ariel 1987) and expiry pinning (Ni, Pearson and Poteshman 2005) were published before 2011.

### C. Rules

Common: all series are on the sheet (SPY, ^VIX, VIXCLS, GS2, GS10, CPILFESL, FEDFUNDS); no options data needed. Gates read the prior close; no look-ahead found. CPILFESL first-published with lag 1 is right. Open: the sheet does not say from when the panel's daily S&P closes (and a daily cash rate for excess returns) exist; SPY starts 1993 (judgement point 2).
- R1: entries and exit in quote. Form B's bar (above last year's close) is the reader's; the cited quote's only number is a 20% fall ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C05-2|MT206-C05-2]]); [[MT183 - The Volatility Apocalypse - Systematic Investor 303#^MT183-C13-2|MT183-C13-2]] ("end of year flows and a year that market is up 25% or very positive") supports the up-year idea better. Form C's "whatever is happening" read as the year-to-date sign is a reader's choice. Direction long: supported.
- R2: (a) X as third Friday is the reader's but is the standard listed-option convention (checker's knowledge), not a hidden choice. N 12 or 15 fits a four-week cycle; in a five-week cycle N 15 leaves a two-week gap against his "two and a half" ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C08-4|MT076-C08-4]]). Fix: N 13 in five-week cycles. The next-day version is in quote ([[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C05-3|MT227-C05-3]]). Long only, no short in the gap: supported.
- R3: window 1 and 2 timing in quote; holding 10 days reader (tagged). The gate "above the last October close" is an unlabelled reader's bar for "after a big run" ([[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C08-2|MT132-C08-2]]). Evidence lines need the ledger corrections above. Short direction: supported by [[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C08-2|MT132-C08-2]], [[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C11-1|MT132-C11-1]], [[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C17-X2|MT150-C17-X2]].
- R4: (c) direction matches his words: after gains "reinvestment happens fund etc. at the end of month" ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C03-X1|MT206-C03-X1]]); after a fall levered funds cut to constant risk ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C07-1|MT076-C07-1]]). d is the reader's (tagged). Checker's knowledge: the turn-of-month effect is positive regardless of the month's sign, so the short leg fights a documented pattern; the placebo will show it.
- R5: direction right (long 2-year, short 10-year gains when the slope widens, [[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C08-2|MT206-C08-2]]). Missing: four weekly tranches (shop rule 2, as cards 1-3); and his own 2024-10 admission "it's not playing out" ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C11-1|MT206-C11-1]]). Overlap with card 3's R2 and Trend correctly flagged.
- D1: VIXCLS from 1990 correct. The state (VIX average above its level 6 months ago) coincides with rising realised volatility, and volatility persists, so next-6-month realised volatility will be higher in the state by persistence alone; the gate does not test his claim, which is a larger later fall ([[MT183 - The Volatility Apocalypse - Systematic Investor 303#^MT183-C10-1|MT183-C10-1]], [[MT126 - Politics, Markets & Power Plays - Systematic Investor 338#^MT126-C08-2|MT126-C08-2]]), and the "adds a visible quarter" sentence is not what the test measures.
- D2: Trend long the 2-year does not repeat a duration-neutral spread if Trend is also long the 10-year; the test must read both legs.

### D. All 785 quotes

Contradicting the card:
1. The falsifier "a long calm that ends without a violent break": he repeatedly names a slow grind lower as the likely path: "for a stair step down" ([[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C06-1|MT227-C06-1]]), "the best outcome is a slow boil the frog" ([[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-3|MT163-C20-3]]), "this is more of a 2022 type decline" ([[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C22-1|MT163-C22-1]]), and Q1 2026 long-volatility hedges made "no real money" in a slow fall ([[MT016 - America's 250-Year Reset feat. Cem Karsan - Systematic Investor - Ep. 407#^MT016-C03-5|MT016-C03-5]]). Only a calm that ends with no fall counts against him.
2. [[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C09-4|MT132-C09-4]] (fall came early) against "inside their windows".
3. [[MT104 - Market Structure, Liquidity, and Reflexivity in 2025 - Systematic Investor - Ep.368#^MT104-C02-2|MT104-C02-2]] and [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C13-2|MT076-C13-2]] against the stated conflict with card 1's title idea.
Omitted ideas:
4. "two years back to back positive like that uh has an expected negative return the following year" ([[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C07-2|MT227-C07-2]]): a codable annual S&P idea, neither a rule nor dropped; its 2025 call (MT227-V005-1, window closed, unscored) went the other way by ledger levels.
5. His concession on the steepener ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C11-1|MT206-C11-1]]), relevant to R5's record.
6. Technical and trigger levels: CTA rebalancing points ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C05-X1|MT076-C05-X1]]), "you get below technical levels" ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C06-X1|MT076-C06-X1]]), confluence of levels ([[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C17-1|MT150-C17-1]], [[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C17-X1|MT150-C17-X1]]); no level is in a quote.
7. "This is why sell in May, by the way, happens." ([[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C17-4|MT150-C17-4]]): the other half of his calendar, no dates.
8. Sentiment versus positioning: he treats cash and margin positioning as slower and firmer ([[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C02-1|MT031-C02-1]], [[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C02-2|MT031-C02-2]]) and notes record sentiment while institutions are short ([[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-X1|MT163-C20-X1]], [[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-1|MT163-C20-1]]); question 10 tags by a sentiment survey.
9. Open ledger row MT016-V003-2 (oil and commodity volatility up November to June) is not among the forecasts; minor.
Attribution: one speaker; no statement of the hosts or other panelists is attributed to him in the card. Attribution inside the four panels (F4 rests on [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381|MT221]]) relies on caption names (section 5).
Duplicates: R5 = card 3's R2 pair (flagged, D2); R1, R2, R4 long S&P overlap Trend (flagged); R3 and R4 shorts net against card 2's R2 and card 3's R4 (flagged). No rule needs options data; options mechanisms are correctly marked "no live series".

### E. Dating

Each "hindsight" row rests on quote words: [[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C03-3|MT031-C03-3]] (1998-2002, an observation of a good trade, no own action stated), [[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C08-X1|MT031-C08-X1]] (last four or five years), [[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C09-7|MT031-C09-7]] (four or five years), 2017-18 and 2020 cases recalled in 2024-25. No quote documents a pre-2011 action; correct. The outside-literature line is mislabelled (correction 18).

### F. Rules of the shop

No decision for the user. Versions averaged. Every open choice is a version, a tagged reader's choice, a diagnostic with a fixed gate, or dropped; exceptions: R3's gate (unlabelled), section 6's "Version" for a reported line (not a version). Analyst questions are answerable from public data and scoreable; Q8 needs the monthly GS10/GS2 timing stated; Q10's tag should name a positioning source. Q4-Q6 and Q9 use horizons other than W3's 4 and 13 weeks (judgement point 6). Forecasts F1-F9 are open at 2026-11-22 and dated; F4's made date 2025-12 matches the ledger; F8 resolves the inflation half only (judgement point 5). Date rules without weekly tranches are passed to step 3.2 (acceptable).

Answers to the card's first checks: (a) placement accepted with caveat; third Friday is standard. (b) Form C is a reader's reading; corrected label. (c) R4's direction matches the quotes. (d) Tallies reproduce exactly. (e) No quote dates the 2025 fall: [[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C17-3|MT150-C17-3]] names only Covid; [[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C15-2|MT031-C15-2]] and [[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C16-X2|MT150-C16-X2]] give no dates.

## 3. Required corrections

1. Section 1: state how many volatility rows are on the VIX.
- Find: `volatility 5 of 15, scored on the VIX, which he rejects.`
- Replace: `volatility 5 of 15, 11 of them scored on the VIX, which he rejects ([[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C06-1|MT132-C06-1]]).`
Reason: FORECASTS.csv: 11 VIX, 2 MOVE, 2 gold rows.

2. C3: the 10% is the 1 January share only.
- Find: `bunched at month-end and 1 January: "call it about 10%" arrives then ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C03-2|MT206-C03-2]])`
- Replace: `bunched at month-end and 1 January; of the new capital "call it about 10%, um, comes in on January 1st" ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C03-2|MT206-C03-2]]), no month-end share is given, and that 10% is set`
Reason: the quote ties 10% to 1 January only.

3. R1 form B: the bar is the reader's; cite the quote that fits.
- Find: `Form B: long only if the S&P is above the previous year's last close, since the flows come from the year's gain: "we would lose all those positive flows at the end of the year" ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C05-2|MT206-C05-2]]).`
- Replace: `Form B: long only if the S&P is above the previous year's last close (reader's bar), since the flows come from the year's gain: "end of year flows and a year that market is up 25% or very positive" ([[MT183 - The Volatility Apocalypse - Systematic Investor 303#^MT183-C13-2|MT183-C13-2]]); the one number he ties to losing them is a fall of 20%: "If we were to lose 20% of the market, we would lose all those positive flows at the end of the year" ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C05-2|MT206-C05-2]]).`
Reason: [[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C05-2|MT206-C05-2]]'s threshold is a 20% fall, not a gain.

4. R1 form C: label the reading.
- Find: `Form C: long if above, short if below: "a bit of a magnifier to whatever is happening going into the end of the year" ([[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-2|MT163-C20-2]]).`
- Replace: `Form C: long if above, short if below: "a bit of a magnifier to whatever is happening going into the end of the year" ([[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-2|MT163-C20-2]]); reading "whatever is happening" as the sign of the year to date is the reader's.`
Reason: the quote does not say which move is magnified.

5. R1 ledger: the first season after his first statement rose.
- Find: `Ledger: three direction calls right, one level call wrong; in the first season after he stated it the S&P stood at 6075.11 on 2024-12-05 and 5842.91 on 2025-01-14.`
- Replace: `Ledger: three direction calls right, one level call wrong. In the first season after he stated it the S&P rose from 5708.75 on 2024-10-01 to 5842.91 on 2025-01-14 (MT206-V001-1, right); from 6075.11 on 2024-12-05 it fell (MT132-V004-1, wrong); levels on R1's exact entry days are not in the pack.`
Reason: FORECASTS.csv rows MT206-V001-1 and MT132-V004-1.

6. R2: fix N in five-week cycles to his own figure.
- Find: `N is 12 or 15: a four-week cycle less a gap of one and a half weeks or of one ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C08-4|MT076-C08-4]]); with N 12 a five-week cycle leaves his "two and a half".`
- Replace: `N is 12 or 15 in a four-week cycle: 20 trading days less a gap of one and a half weeks or of one ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C08-4|MT076-C08-4]]). In a five-week cycle N is 13 in both versions: 25 trading days less his "two and a half" weeks (a fixed 15 would leave two).`
Reason: the quote sets the gap by cycle length; N 15 contradicts it in five-week cycles.

7. R3: label the gate.
- Find: `Gate: the S&P is above its close on the last trading day of October.`
- Replace: `Gate (reader's bar for "after a big run at the end of the year", [[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C08-2|MT132-C08-2]]): the S&P is above its close on the last trading day of October.`
Reason: no quote gives this threshold.

8. R3 evidence: the 2026 call is not shown wrong; the 2025 window 1 lost.
- Find: `the 2026 pullback call was wrong too (MT104-V001-2); flagged.`
- Replace: `the 2026 pullback call is scored wrong from its 2025-10-13 start (MT104-V001-2), yet the ledger's own levels have the S&P 2.7% lower on 2026-03-10 (6781.48) than on 2026-01-09 (6966.28), so it is not a miss of a January-February pullback; by the ledger's levels window 1 lost in 2025 (5842.91 on 2025-01-14, 5994.57 on 2025-02-03); flagged.`
Reason: FORECASTS.csv rows MT104-V001-1, MT104-V001-2, MT206-V001-1, MT227-V002-1.

9. R5: weekly tranches as in cards 1-3 (shop rule 2).
- Find: `R5 is checked at month-end as in cards 1 to 3.`
- Replace: `R5 is checked at month-end in four weekly tranches, as in cards 1 to 3.`
Reason: cards 1-3 and shop rule 2 use four weekly tranches for month-end rules.

10. R5: add his own concession.
- Find: `Ledger: steepener stances 1 of 2; his 10-year level calls 0 of 3.`
- Replace: `Ledger: steepener stances 1 of 2; his 10-year level calls 0 of 3; in 2024-10 he said the steepener he had argued for months was "not playing out" ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C11-1|MT206-C11-1]]).`
Reason: omitted quote bearing on R5's record.

11. Question 8: the yield series are monthly.
- Find: `Over 13 weeks SPY and TLT both fall; GS10 minus GS2 is wider.`
- Replace: `Over 13 weeks SPY and TLT both fall; GS10 minus GS2 (monthly averages) is wider in the third month after the forecast month than in the forecast month.`
Reason: GS10 and GS2 are monthly on the sheet; a 13-week horizon is otherwise undefined.

12. Question 10: tag by positioning, which he separates from sentiment.
- Find: `with one tag (crowd long, crowd short, neither) naming the public survey behind it.`
- Replace: `with one tag (crowd long, crowd short, neither) naming the public positioning figure behind it (allocation, cash or margin data, not a sentiment survey: he treats cash and margin positioning as slower and firmer, [[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C02-1|MT031-C02-1]], [[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C02-2|MT031-C02-2]], and reads record sentiment against short institutions, [[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-X1|MT163-C20-X1]]).`
Reason: the card's tag conflates sentiment with positioning.

13. Section 6: a reported line is not a version.
- Find: `Version: a reported drawdown-area line for this pod, not decisive.`
- Replace: `Registered as a reported line (drawdown area) for this pod, not decisive and not a version.`
Reason: versions are averaged signal variants (shop rule 2).

14. Section 8: the falsifier ignores his slow-grind path.
- Find: `Wrong, in his own terms: a long calm that ends without a violent break;`
- Replace: `Wrong, in his own terms: a long calm that ends with no fall at all (not merely without a violent break: he also names a slow grind lower as the likely path, "for a stair step down", [[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C06-1|MT227-C06-1]], "the best outcome is a slow boil the frog", [[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-3|MT163-C20-3]]);`
Reason: the quotes allow both a violent and a slow end.

15. Section 8: the 2024 fall came early, not inside its window.
- Find: `Two falls did come inside their windows and reversed ("We targeted likely September. It happened in August.", [[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C09-4|MT132-C09-4]]; row MT227-V002-1 has the sign right).`
- Replace: `Two falls did come and reversed: one before its window ("We targeted likely September. It happened in August. It happened early.", [[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C09-4|MT132-C09-4]]; row MT183-V002-1 scored wrong at its end date), one inside it (row MT227-V002-1 has the sign right: 5994.57 to 5569.06 by 2025-04-30).`
Reason: [[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C09-4|MT132-C09-4]] quote; FORECASTS.csv.

16. Section 8: no quote says year-end is always strong.
- Find: `- Year-end is always strong ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C04-2|MT206-C04-2]]), or magnifies either way ([[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-2|MT163-C20-2]]).`
- Replace: `- Year-end is the strongest window ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C04-2|MT206-C04-2]]) yet a magnifier either way ([[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-2|MT163-C20-2]]); no quote says it is always strong, and the claim text of [[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C04-2|MT206-C04-2]] puts almost all its gains in up years, so the two may agree (R1's forms cover both readings).`
Reason: overstated contradiction.

17. Section 8, card 1: he agrees that liquidity drives prices.
- Find: `Conflicts with card 1 where it buys Treasuries, and with its title idea: for K the market itself, not the central bank, is the largest source of liquidity ([[MT104 - Market Structure, Liquidity, and Reflexivity in 2025 - Systematic Investor - Ep.368#^MT104-C07-1|MT104-C07-1]]).`
- Replace: `Conflicts with card 1 where it buys Treasuries. On its title idea he agrees that liquidity drives prices ("markets are a function of liquidity", [[MT104 - Market Structure, Liquidity, and Reflexivity in 2025 - Systematic Investor - Ep.368#^MT104-C02-2|MT104-C02-2]]; "QT QE different story direct impact on markets", [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C13-2|MT076-C13-2]]) and differs on the source: for K the market itself, not the central bank, is "the biggest provider of liquidity" ([[MT104 - Market Structure, Liquidity, and Reflexivity in 2025 - Systematic Investor - Ep.368#^MT104-C07-1|MT104-C07-1]]).`
Reason: quotes [[MT104 - Market Structure, Liquidity, and Reflexivity in 2025 - Systematic Investor - Ep.368#^MT104-C02-2|MT104-C02-2]] and [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C13-2|MT076-C13-2]].

18. Section 9: the outside facts are the writer's; the checker confirms them.
- Find: `Checker's knowledge, not in the pack: turn-of-year and expiry-week patterns have published sources before 2011.`
- Replace: `Writer's knowledge, not in the pack, confirmed by the checker: turn-of-year and expiry-week patterns have published sources before 2011 (Rozeff and Kinney 1976 on January, Ariel 1987 on the turn of the month, Ni, Pearson and Poteshman 2005 on prices pinned at option expiry).`
Reason: the label named the wrong source of the knowledge.

19. D1: measure the later fall, scaled by volatility already seen.
- Find: `Outcome: realised volatility of daily S&P returns over the next 6 months.`
- Replace: `Outcome: the largest peak-to-trough fall of the S&P on daily closes over the next 6 months, divided by the annualised realised volatility of daily S&P returns over the past 3 months (his claim is a larger later fall, [[MT183 - The Volatility Apocalypse - Systematic Investor 303#^MT183-C10-1|MT183-C10-1]], [[MT126 - Politics, Markets & Power Plays - Systematic Investor 338#^MT126-C08-2|MT126-C08-2]]).`
Reason: as written, volatility persistence alone passes the gate.

20. D1: the reason must match the corrected outcome.
- Find: `Why 1.25: recent volatility already predicts volatility; the state must add a visible quarter.`
- Replace: `Why 1.25 and the scaling: recent volatility already predicts the size of falls, so the outcome is divided by it; the state must then add a visible quarter.`
Reason: consistency with correction 19.

21. D2: a spread is repeated only if Trend holds both legs.
- Find: `share in which Trend is long the US 2-year.`
- Replace: `share in which Trend is long the US 2-year and short or flat the US 10-year (R5 is a duration-neutral spread; Trend long both legs does not repeat it).`
Reason: one-leg overlap does not show duplication.

22. Section 11: add the two omitted calendar ideas.
- Find: `- Midterm-year short ([[MT016 - America's 250-Year Reset feat. Cem Karsan - Systematic Investor - Ep. 407#^MT016-C14-4|MT016-C14-4]]): nine midterm years in the design window, no threshold; kept as F2.`
- Replace: `- Midterm-year short ([[MT016 - America's 250-Year Reset feat. Cem Karsan - Systematic Investor - Ep. 407#^MT016-C14-4|MT016-C14-4]]): nine midterm years in the design window, no threshold; kept as F2. After two strong years a weak third ("two years back to back positive like that uh has an expected negative return the following year", [[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C07-2|MT227-C07-2]]): no threshold in the quote; his 2025 use (row MT227-V005-1, window closed, unscored) went the other way (5994.57 on 2025-02-03, 6939.03 on 2026-01-30); dropped. Sell in May ("This is why sell in May, by the way, happens.", [[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C17-4|MT150-C17-4]]): no dates in the quote; dropped.`
Reason: codable ideas in the quotes, neither used nor dropped.

23. Section 11: add technical levels.
- Find: `- Stock baskets for inflation ([[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C04-5|MT031-C04-5]]): single stocks, not in the panel.`
- Replace: `- Stock baskets for inflation ([[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C04-5|MT031-C04-5]]): single stocks, not in the panel. Technical and trigger levels (CTA rebalancing points, [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C05-X1|MT076-C05-X1]]; "you get below technical levels", [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C06-X1|MT076-C06-X1]]; confluence, [[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C17-1|MT150-C17-1]], [[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C17-X1|MT150-C17-X1]]): no level is in a quote (the 200-day average is claim text); analyst only.`
Reason: omitted part of his path reading.

24. Section 13 R1: relabel and correct the first-season line.
- Find: `- R1: a known seasonal pattern (checker's knowledge); the up-year gate is momentum under another name; about 36 windows in the design era; his own first season lost.`
- Replace: `- R1: a known seasonal pattern (writer's knowledge, confirmed by the checker); the up-year gate is momentum under another name; about 36 windows in the design era; his own first season fell from early December (MT132-V004-1) but rose from 1 October (MT206-V001-1).`
Reason: FORECASTS.csv; label.

25. Section 13 R3: match the corrected evidence.
- Find: `- R3: one dated case, a pandemic; both later live uses missed; it shorts what Trend holds.`
- Replace: `- R3: one dated case, a pandemic; window 1 lost in 2025 by the ledger's levels and the 2026 pullback call is unproven either way; it shorts what Trend holds.`
Reason: correction 8.

26. Section 13 R4: relabel.
- Find: `the commonly described month-end rebalancing runs the other way (checker's knowledge)`
- Replace: `the commonly described month-end rebalancing runs the other way, and the turn-of-month effect is positive whatever the month's sign, so the short leg fights it (writer's and checker's knowledge, Ariel 1987)`
Reason: label; adds the documented pattern the short leg trades against.

## 4. Open judgement points

1. R2's support before X rests on reading "for the next two weeks" (2024-04-25) against the 17 May 2024 expiry; [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C06-X1|MT076-C06-X1]]'s "that weekend" may be the Iran weekend, not an expiry (step 3.1-3.2).
2. Whether a daily S&P total-return series and a daily cash rate exist back to 1975 for R1-R4; if not, the design window for the date rules starts later (step 3.1).
3. Date rules without weekly tranches against shop rule 2 (step 3.2, registration 3.4).
4. Form C's sign variable (year to date, or the move since entry) (step 3.2).
5. F8 resolves only the inflation half of "stagflation"; whether to add a growth bar (step 2.2).
6. Analyst questions 4-6 and 9 use horizons other than W3's 4 and 13 weeks (step 3.1, W3 spec).
7. Attribution inside the four panels (F4 rests on [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381|MT221]]) relies on caption names (step 2.1 recode).
8. R4's short leg against the turn-of-month effect: the placebo and double-cost tests decide (step 4.3).
9. Buy after the event: Fed meeting dates are a published calendar like expiry dates; whether a fixed date table counts as a series (step 3.1).

## 5. What I could not verify

- Who speaks inside the four multi-guest panels beyond the caption names; claim text generally.
- S&P levels on the exact R1-R4 entry and exit days (not in the pack); the R3 2025 window-1 result is from nearby ledger dates.
- The recording context of [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293|MT076]] (which weekend, which expiry); expiry dates and the third-Friday convention are checker's knowledge.
- Whether the ledger's machine scoring and its series are correct; tallies were reproduced from FORECASTS.csv as given.
- The literature dates in correction 18 are from memory (no web).

