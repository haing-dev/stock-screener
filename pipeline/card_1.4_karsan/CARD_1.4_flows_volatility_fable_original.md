# Playbook card 1.4 (4 of 5): flows and volatility (Cem Karsan)

Source: 785 claims, 16 recordings, 2024-05 to 2026-07, one speaker (K). Quotes are ground truth; they are short fragments, so much detail survives only as claim text and is marked. Labels: SHOWN, SHOWN (words), ASSERTED, reader.

## 1. Verdict

1. Playbook: over days to months, index prices are set by forced flows (dealers hedging options, sellers of volatility, funds re-leveraging on a calendar) more than by news. K trades the path and the width of outcomes with options, sized by positioning, under a macro view of structural inflation.
2. Little can be coded. The engine (dealer positions, volatility supply, skew, positioning) has no series on the data sheet, and his instrument, the option, is not in the book. Left is the calendar skeleton: 5 rules, 16 versions, all hindsight-flagged; four date rules on the S&P 500, one curve rule.
3. Strongest link: his account of calm markets (volatility supply pins the index and scatters single stocks), told alike in ten recordings (reader's count), one named precedent (2017 to 2018). His year-end rally calls are 3 of 3 in the ledger, over two seasons.
4. Weakest link: turning flows into direction. He says so: "maybe 40% at at the best" (MT031-C08-3). Ledger (machine-coded, scored at end dates): 28 of 68 right; US stocks 5 of 18 (rises 5 of 7, falls 0 of 8, flat 0 of 3); volatility 5 of 15, scored on the VIX, which he rejects.
5. Dating: nothing is documented before 2011 except a recalled observation about 1998 to 2002, which carries no rule.
6. Counts: 5 rules, 10 analyst questions, 9 open forecasts, 2 diagnostics.

## 2. Causal model

All chains are K's own; no firm process is described. Period: the cases named.

**C1. Volatility supply pins the index.** Buyers of structured products and option funds sell index options; dealers who hold them buy dips and sell rallies; the index goes quiet and single stocks must offset each other. Other side: product buyers, short volatility for yield; then long/short equity funds. Cases: 2017, 2023 to 2026. "index fall Supply means the market is going to have a very hard time breaking down" (MT183-C02-2); "if something goes up, something else has to go down" (MT016-C12-5); MT132-C03-3, MT163-C08-1. ASSERTED; the offset logic is SHOWN (words). Limit: nothing on the sheet measures supply.

**C2. Time and falling volatility make dealers buy.** Hedgers pay for puts ("this is why skew exists", MT076-C11-1); "dealers are short puts" and short stock (MT206-C05-1); as the puts decay dealers buy stock back, most into expiry (MT076-C07-4), through holidays (claim text of MT206-C04-4) and once an event has passed (MT076-C07-2). After expiry the support is gone for "one to one and a half weeks" (MT076-C08-4). Other side: put buyers. ASSERTED; the 95% of MT076-C11-3 has no data behind it. Limits: his own 40%; widely absorbed by now (MT031-C08-X1); "knowledge is all dampening" (MT227-C06-5). Only the calendar is observable.

**C3. Re-leveraging.** Gains are collateral. Institutions that hold risk constant must buy after gains, bunched at month-end and 1 January: "call it about 10%" arrives then (MT206-C03-2) against "about 100 billion dollars" traded a day (MT206-C04-1). It reverses after falls (MT076-C07-1, MT206-C05-2). Other side: under-invested managers, "Where people have to chase" (MT206-C04-3). MT206-C02-2, MT104-C16-2. SHOWN (words): arithmetic stated, no data; the asset base changes between tellings (section 12).

**C4. Unpinning.** Calm stores risk; a break needs leverage in few hands plus a spark (MT202-C16-1, MT183-C04-1). Volatility first rises with the market, then a warning shot, later the larger fall (MT183-C10-1): "you start to see volatility increase into a rally" (MT104-C08-2); "a warning shot which we often see before a bigger move" (MT126-C08-2). Other side: holders of short-volatility carry (MT202-C06-3). Cases: 1998 to 2002, 2017 to 2018, August 2024 (MT132-C09-3, MT202-C04-1). ASSERTED from recalled cases; "it usually takes way longer than you expect" (MT206-C17-2). Observable in part: VIXCLS rising while the S&P rises (D1).

**C5. Falls run from expiry to expiry.** Large open interest at quarterly expiries turns a fall into forced selling. "CO started the day after Feb opex. It ended the day after March opex." (MT150-C17-3); "quarterly expirations are the biggest risk" (MT227-C06-2); MT227-C06-3, MT076-C03-6. Other side: dealers short downside options. SHOWN for one case (2020, dates in the quote); the 2025 repeat is claim text.

**C6. Positioning beats news.** "if the world is long" the odds favour a fall (MT016-C02-3); while institutions are short "it's hard for uh markets to go down" (MT163-C20-1); in thin summers "Momentum value versus value often leads the market lower" (MT163-C08-2). Other side: the crowd. ASSERTED. No positioning series on the sheet.

**C7. The market is the liquidity.** A rising market creates collateral and more buying ("the biggest provider of liquidity", MT104-C07-1); a falling one drains it, so policy must respond (MT016-C05-3). Other side: holders of money, through inflation (MT104-C08-3). ASSERTED, with one worked case (MT202-C12-1). Card 1's liquidity theme; no rule.

**C8. Structural inflation.** Inequality feeds populism, spending and protection; inflation comes in waves; rising yields cut multiples; stocks and bonds fall together; volatility moves to currencies, bonds and gold; the curve steepens as cyclical inflation falls. MT206-C08-2, MT150-C10-2, MT031-C10-1, MT031-C09-3. Other side: holders of stock and bond mixes (MT031-C12-2). ASSERTED by analogy with 1968 to 1982; "it's not good for predicting one-year, two-year outcomes or five-year outcomes" (MT031-C11-1).

## 3. Indicators

| Indicator | How K uses it | Series | Lag |
|---|---|---|---|
| Days to monthly and quarterly expiry; four or five-week cycle | support before, gap after (MT076-C08-4) | calendar arithmetic | none |
| S&P gain year to date and month to date | size and sign of period-end flows (MT104-C16-2, MT076-C07-1) | SPY; panel S&P daily | 1 day |
| VIX against market direction | late-rally tell (MT104-C11-2); but "The VIX is not what you should be looking at" (MT132-C06-1) | VIXCLS, ^VIX | 1 day |
| Realised volatility; time without a 3% fall | pinned state (MT202-C04-2) | SPY | 1 day |
| Fixed-strike implied volatility; skew by maturity | his fear gauge and warning (MT031-C02-6, MT227-C04-1, MT163-C21-X1) | no live series | |
| Volatility supply (product issuance, open interest); dealer gamma, vanna, charm | the key input (MT132-C05-3, MT076-C08-2, MT031-C08-1) | no live series | |
| Single-stock against index volatility | "four times the volatility of the constituents" (MT183-C01-1) | no live series; he drops breadth inside a quarter (MT183-C05-1) | |
| Momentum against value; hedge-fund baskets | lead for the index (MT163-C08-2, MT076-C06-1) | no live series; question 7 uses the 20 industry ETFs | 1 day |
| Cash share, margin debt, institutional position | crowding (MT031-C02-2, MT104-C16-3) | no live series; Compass hh_equity is quarterly | 3 months |
| 10-year yield, curve, core inflation, Fed rate | regime and steepener (MT150-C18-1, MT206-C08-2) | GS10, GS2, CPILFESL, FEDFUNDS | 0 to 1 month |
| Volatility of gold, currencies, bonds against stocks | where volatility goes (MT031-C10-1) | realised only: GLD, FXY, TLT, SPY | 1 day |

## 4. Rule layer

Common to all rules. Panel markets as excess returns: S&P 500 (daily closes; SPY live), US 2-year note, US 10-year bond. Rules at equal risk; opposite positions net, also against cards 1 to 3; nothing sized by conviction; every version run and averaged. R1 to R4 are date rules on daily closes: the dates are the signal, so no weekly tranches (fixed here; step 3.2 checks it against shop rule 2). A date that is not a trading day moves to the trading day before. Gates read the close of the day before entry. Expiry day X is the third Friday of the month: the reader's reading of his Opex, defined in no quote. R5 is checked at month-end as in cards 1 to 3.

**R1. Year-end window.** Long S&P 500 from entry to exit. Entry: the last trading day of October ("late October", MT227-C05-X1) or the last trading day on or before 15 December ("the middle of December to the middle of January", MT206-C04-2). Exit: the last trading day on or before 15 January ("till about the middle of January", MT104-C17-2). Form A: always long. Form B: long only if the S&P is above the previous year's last close, since the flows come from the year's gain: "we would lose all those positive flows at the end of the year" (MT206-C05-2). Form C: long if above, short if below: "a bit of a magnifier to whatever is happening going into the end of the year" (MT163-C20-2). Versions: 6. Also MT206-C03-2, MT104-C16-2. Hindsight: first stated 2024; flagged. Ledger: three direction calls right, one level call wrong; in the first season after he stated it the S&P stood at 6075.11 on 2024-12-05 and 5842.91 on 2025-01-14. Not in the pods: none reads the calendar. Trend is often long the S&P on the same days, so the placebo with shuffled dates is the test that counts.

**R2. Option-cycle window.** Long S&P 500 from the close N trading days before X to the close of X; flat otherwise. N is 12 or 15: a four-week cycle less a gap of one and a half weeks or of one (MT076-C08-4); with N 12 a five-week cycle leaves his "two and a half". Second choice: also hold through the next trading day, since "Opex Fridays and the Mondays are usually the strongest day" (MT227-C05-3). Versions: 4. That the gap sits after expiry rests on "for the next two weeks" into May expiry (MT076-C07-4) and on claim text of MT076-C06-X1. No short in the gap: he speaks of risk, not of a fall. Also MT031-C03-1, MT163-C09-1. Hindsight: 2024; flagged. Not in the pods: as R1. The rule is long 55 to 75% of days (reader), so most of its return is plain exposure.

**R3. After the ramp.** Gate: the S&P is above its close on the last trading day of October. Window 1: short S&P 500 from R1's exit day for 10 trading days ("January 13th to 15th window", MT132-C11-1; "one and a half to two week window", MT132-C08-3). Window 2: short from the close of February's X to the close of the first trading day after March's X (MT150-C17-3; "if we can hang on through Feb, then kind of creates potential energy for March", MT150-C17-X2). Versions: the two windows (2). Also MT132-C08-2, MT227-C06-3. Hindsight: window 2 is one dated case, 2020; window 1 is one live call, wrong at 12 months in the ledger (MT132-V005-1); the 2026 pullback call was wrong too (MT104-V001-2); flagged. Not in the pods: Trend is long after a ramp; this is the opposite.

**R4. Month-end re-leveraging.** T is the month's last trading day. Take the sign of the S&P's move from the previous month's last close to the close of day T minus d minus 1. Hold that sign (long after a rise, short after a fall) from the close of day T minus d to the close of trading day d of the next month. The count d is 3 or 5 (2 versions); he gives no days: "some major effects do fall at the end and beginning of months" (MT206-C02-5). After gains, "reinvestment happens fund etc. at the end of month" (MT206-C03-X1); after a falling month levered funds "take their risk to constant to where it was last month" (MT076-C07-1). Hindsight: 2024; flagged. Not in the pods: Trend's fastest version looks back one month, so R4 may repeat it for a few days (step 3.2).

**R5. Disinflation steepener.** On while the 12-month change of CPILFESL (first published where vintages exist, lag 1) is below its value 6 months earlier: when "inflation cyclically is declining", "we start to see a counterintuitive steepener" (MT206-C08-2). Version 2 also needs FEDFUNDS at least 0.25 below its level 6 months earlier; that every cut steepens the curve is claim text of MT206-C10-5, so it is a version. The 6 months and the 0.25 follow card 1 (reader). Action: long US 2-year note, short US 10-year bond, equal sensitivity to a 0.01 change in yield, built as card 3's R2. Off otherwise. Versions: 2. Also MT031-C13-4. Hindsight: 2024; flagged. Ledger: steepener stances 1 of 2; his 10-year level calls 0 of 3. Against the cards: card 3's R2 holds the same pair on another condition (a flat slope); card 1's R3 and card 2's R1 hold the same 10-year short; card 1's R1 and R2 buy the 10-year. Economic trend buys bonds when inflation falls, and Trend is probably long the 2-year while the Fed cuts (reader). D2 decides.

**Not rules, because Economic trend or Trend would hold the same position** (reader; step 3.2 confirms): weak growth with hot inflation, so short stocks and bonds (MT076-C01-1, MT150-C04-5, MT221-C16-3); the tariff chain from companies to consumers (MT163-C09-2); a strong jobs number as the trigger for a fall (MT227-C05-X2); long gold and commodities in the inflation regime (MT132-C15-2, MT126-C16-3). Yields up, so stocks down (MT150-C10-2) is card 2's R2 and card 3's R4.

## 5. Analyst layer

Weekly, from the fixed snapshot and public calendars. Answers are probabilities unless stated, scored by Brier score against a baseline: the outcome's frequency since 1990 unless stated.

1. Calm or break. SPY's largest peak-to-trough fall on closes exceeds 3% within 4 weeks; exceeds 10% within 13 weeks.
2. Width. SPY's realised volatility over the next 4 weeks is above the last 4 weeks. Baseline 0.5.
3. VIX. VIXCLS is higher in 4 weeks; in 13 weeks.
4. Cycle. State days to X and whether it is quarterly. SPY is higher at the close of X than today; SPY is lower 5 trading days after X than at X.
5. Event. For each scheduled Fed decision, inflation release, jobs report or election in the next 4 weeks: SPY is higher 5 trading days after than at the close before.
6. Season (October to March). SPY is higher on 15 January than today; from 15 January, SPY falls 5% or more before the day after March's X (5% is the reader's).
7. Rotation. Over 4 weeks the five industry ETFs with the best 6-month return do worse on average than the five worst ("do the opposite", MT016-C12-6). Baseline: frequency since the ETFs exist; June to August tallied apart.
8. Stocks and bonds. Over 13 weeks SPY and TLT both fall; GS10 minus GS2 is wider.
9. Where the volatility is. Rank GLD, FXY, TLT and SPY by 13-week realised volatility against each one's own 5-year median. Scored by rank correlation; baseline: last quarter's ranking.
10. The put and the crowd. WALCL is higher in 13 weeks; SPY is higher in 13 weeks, with one tag (crowd long, crowd short, neither) naming the public survey behind it. Tags tallied.

## 6. Process rules that are not signals

- Path, not direction: "it's very hard to predict Direction" (MT076-C04-3); "bet on both paths" (MT163-C23-1). ASSERTED. Registered for the analyst (probabilities, fixed windows); dropped for the rule layer, which has no options.
- Fixed windows: a trade is dropped when its window passes (MT132-C08-3). ASSERTED. Registered: the date rules never extend.
- Shorts only in narrow windows: betting against the market is "the hardest thing you can do" (MT132-C09-X4). Registered: R3 and R4 hold the only shorts, a few weeks at most.
- Never a pattern alone: "you can't put all your eggs in one basket and go all in for that reason" (MT132-C10-X6); he reads a seasonal pattern with flows. The rule layer cannot see flows: it tests the calendar without his eyes. Registered as a stated limit in the pod spec.
- Carry needs convexity: "whenever you have a tail with leverage" there must be convexity elsewhere (MT202-C07-X1, MT221-C05-1). The book holds no options. Registered as an exclusion: no rule that is long only because volatility is pinned (section 11).
- Sizing by positioning (MT202-C06-1): dropped, no data. Size is fixed while a rule is on.
- Horizon: structural bets run a year or more, "this could take several years" (MT163-C07-X1). Dropped for rules; it sets the 13-week and decade forecasts.
- Judging risk: good ratios over 5 to 10 years can hide "tremendous tails" (MT031-C06-3); he prefers "area under the curve" (MT031-C06-4). Version: a reported drawdown-area line for this pod, not decisive. Agrees with thesis note 1.3c.

## 7. Dated forecasts still open

| # | Statement | Made | Resolves |
|---|---|---|---|
| F1 | Large state buying of shares "after the midterms and before June in a meaningful way" (MT016-C08-1, MT016-C06-2) | 2026-07-04 | by 2027-06-30; analyst-coded: a federal programme buying listed shares of many companies |
| F2 | "a pretty ugly November to June" (MT016-C09-2); flows gone after mid-December (MT016-C14-1) | 2026-07-04 | SPY return from 2026-11-03 to 2027-06-30 negative; largest fall reported |
| F3 | November to June: "full throttle re-engagement" with Iran (MT016-C08-4, MT016-C14-3) | 2026-07-04 | US military action against Iran by 2027-06-30; analyst-coded |
| F4 | 2026 like 2022: "the pain trade will be market down and interest rates up" (MT221-C16-3) | 2025-12 | at 2026-12-31: S&P below end-2025; GS10 above December 2025. Ledger so far: S&P 6966.28 on 2026-01-09, 7722.72 on 2026-10-02 |
| F5 | China moves on Taiwan: "about as high as 50% in the next 4 years" (MT206-C13-2); a coin flip in two to three years (MT183-C05-2; Taiwan is claim text) | 2024-09; 2024-07-10 | by 2028-09 and 2027-07; analyst-coded blockade, embargo or attack; scored as probability 0.5 |
| F6 | "the trade in gold in the next decade" is long-dated calls (MT183-C16-2) | 2024-07-10 | 2034-07: GC=F above its level at the date; option value not observable |
| F7 | "FX is going to be the best play in V for the decade" (MT163-C06-3; MT031-C10-1) | 2025-07-17 | 2035-07: realised volatility of panel currencies, against their own prior ten years, above the S&P's ratio (reader's rule; implied volatility has no series) |
| F8 | "you're in a decade of stagflation" (MT206-C10-4) | 2024-09 | 2034-09: average 12-month change of CPILFESL above 3.0 (reader's bar) |
| F9 | A state fund buys "10 to 15 trillion dollars of equities" within a decade by printing money (MT016-C05-5) | 2026-07-04 | 2036-07; analyst-coded |

Context only. "a bigger one is coming" within "12 to 18 months" (MT126-C08-3): window closed 2026-09, row MT126-V006-1 unscored; the S&P was 5667.56 on 2025-03-21 and 7537.43 on 2026-07-06. The midterm drawdown row (MT031-V004-1) rests on view text.

## 8. What would prove it wrong; when it should stop; disagreements

Wrong, in his own terms: a long calm that ends without a violent break; volatility rising with the market and no larger moves after (D1); years of large gains whose year-end window falls; analyst answers on width (questions 1 to 3) no better than base rates at the checkpoint.

Stop working: when widely known (MT227-C06-5, MT031-C08-X1); when daily options spread hedging over every day, since zero-day trading "can also unpin markets" (MT183-C03-1; the dilution is the reader's); when supply shrinks, after a break or when rates fall (higher rates made the products attractive, MT183-C03-X1); when the state manages prices: "will things mean revert? Um in a natural system, yes." (MT016-C11-2). His premise that structural flows are "much bigger than it's ever been" (MT031-C07-3) also means design years should show less: history can neither confirm nor refute the date rules (reader).

Against himself.
- He ranks direction as hard and flows as 40% at best, yet gives dated directions throughout; the falls are 0 of 8 at end dates. Two falls did come inside their windows and reversed ("We targeted likely September. It happened in August.", MT132-C09-4; row MT227-V002-1 has the sign right).
- Year-end is always strong (MT206-C04-2), or magnifies either way (MT163-C20-2).
- From 2024-12 to 2025-12 he called a top or a large fall in five recordings (reader's count); in 2026-07 it is "this is the don't fight the Fed thing, but on steroids" (MT016-C11-1). In that recording the state cannot allow a "decline of more than 20%" (MT016-C05-3) and also "probably wants a bit of a crisis" (MT016-C14-2).
- He grades his 5% yield call "we called that we were about 10 days late" (MT227-C01-2); the ledger has the 10-year at 4.77 and scores it wrong (MT183-V005-1).
- Long volatility is what research favours (MT221-C04-2), yet it "is always frustrating" (MT016-C03-6) and blind put buying loses (MT202-C05-1). Stock-index volatility is the wrong one to own in this regime (MT163-C05-2), yet most of his dated trades are in it.
- The 1968 to 1982 real loss is told as 70%, 67%, about 50% and 55 to 60% (MT132-C10-2, MT227-C07-3, MT163-C16-1, MT031-C11-4), all in quote; election years outside the period earn 5% or six to seven (MT132-C10-1, MT031-C16-1).

Against cards 1 to 3. Agrees with card 2's R1 (real rates cannot stay negative, MT104-C09-2) and R2, with card 3's steepener, and with card 1's R3. Conflicts with card 1 where it buys Treasuries, and with its title idea: for K the market itself, not the central bank, is the largest source of liquidity (MT104-C07-1). Conflicts with card 3's R4: valuations are no "good timing mechanism" (MT104-C02-1). On sizing he sides with cards 2 and 3 (spread first, then leverage, MT031-C06-1) against card 1. Card 3 shrinks before events; K buys after them: the two fit.

## 9. Dating table for rule 5

| Thesis | Held before 2011, by the quote? | Status |
|---|---|---|
| Late in a rally volatility rises with prices; own calls | Recalled: "when I started in the business in '98, '99, 2000, 2001, 2002" (MT031-C03-3); an observation, no trade record | not a rule |
| Volatility supply and unpinning | Cases 2017 to 2018, 2024 | hindsight |
| Hedging calendar (R2) | "I've added vol and charm", absorbed in the last four or five years (MT031-C08-X1) | hindsight |
| Year-end and month-end re-leveraging (R1, R4) | First stated 2024 | hindsight |
| Expiry-to-expiry falls (R3) | Case 2020 | hindsight |
| Steepener (R5) | 2024 | hindsight |
| Structural inflation; volatility in currencies and gold | "four or five years" (MT031-C09-7) | hindsight |

Checker's knowledge, not in the pack: turn-of-year and expiry-week patterns have published sources before 2011. Step 1.5 may date the pattern, not his mechanism.

## 10. Diagnostics (zero slots)

**D1. Market up, volatility up.** Month-ends 1990-01 to 2010-12 (VIXCLS starts in 1990, reader). Up-months: S&P above its level 6 months earlier. State on if the month's average VIXCLS is also above its average 6 months earlier. Outcome: realised volatility of daily S&P returns over the next 6 months. Gate: the median outcome in state-on up-months is at least 1.25 times that in the other up-months, in the whole window and in each half (1990 to 1999, 2000 to 2010). Pass: the state is registered as a sizing version (S&P legs of R1 to R4 at half size while on; half is the reader's) and gives question 1 a base-rate table. Fail: analyst question only. Why 1.25: recent volatility already predicts volatility; the state must add a visible quarter. Two market cycles: descriptive.

**D2. Overlap of R5.** Design months 1975 to 2010. Share of R5's on-months that fall inside card 3's R2; share in which Trend is long the US 2-year. Gate: either share at least 0.80 in both versions. Then R5 is not registered as its own rule and its condition passes to step 3.2 as a note on card 3's R2.

## 11. Dropped ideas

- Long while pinned (MT076-C09-1): many small gains and a rare large loss; he pairs it with options the book lacks; his 2024-07 pinned call (MT183-V001-1) scored wrong.
- Election-year long, next-year short: outside his populist label election years earn 5 to 7% by his own count; the label is hand-made ("it may feel like cherry-picking", MT206-C16-X2); the design window holds two such elections.
- Midterm-year short (MT016-C14-4): nine midterm years in the design window, no threshold; kept as F2.
- Summer fade of winners; the crowd as a contrary signal (MT016-C12-6, MT016-C02-3): no factor or positioning series; question 7.
- Buy after the event (MT076-C07-2): Fed meeting dates are not a series on the sheet; question 5.
- Every option trade (calendars, right-tail calls, gold calls funded by oil puts, MT031-C09-2): no options, no data.
- Oil bought cheap and sold dear (MT150-C11-2): the Value pod; his 40 (MT150-C12-3) is a 2025 number.
- A neglected market turning up, "90% of scenarios" (MT206-C06-2): Value with Trend; the years are claim text.
- Stock baskets for inflation (MT031-C04-5): single stocks, not in the panel.
- Client allocation of 30 to 50% to non-correlated strategies (MT163-C17-1): not a pod rule.

## 12. Numbers, pack problems, first checks

In quote: 40% (MT031-C08-3); one to one and a half and two and a half weeks (MT076-C08-4); 95% (MT076-C11-3, MT227-C05-3); 10% on 1 January and 100 billion a day (MT206-C03-2, MT206-C04-1); 3% in 2017 (MT202-C04-2); four times (MT183-C01-1); 13 to 15 January (MT132-C11-1); 50% in 4 years (MT206-C13-2). Summary only: 125 years behind the year-end window; the 2025 February to March fall; asset bases of 250 and 300 trillion (in quote elsewhere: "200 trillion of equities", MT104-C16-2); 6.5% for the 10-year. Reader: 0.25 and 6 months in R5; d in R4; N in R2; 10 days in R3; 1.25, 0.80 and half size in section 10; all ledger tallies (from FORECASTS.csv: 28 of 68; 26 of 64 where a base rate exists, mean base rate 0.34).

Pack problems.
1. Many quotes are fragments that carry no statement: MT183-C02-1 stops mid-sentence, MT132-C10-5 is "many, many times, most", MT031-C16-X1 and MT206-C11-X2 state nothing. Their claim text cannot be checked.
2. Caption errors hide key words: vol appears as ball, fall, V, VA, vault, volume; vanna as Bond (MT076-C06-X1). A search for vanna finds nothing.
3. MT150-C17-3: the claim says 2020 and 2025 both ran expiry to expiry; the quote names only Covid.
4. MT076-C13-5: the quote says "211%"; the claim says strongly positive.
5. Thirteen claim ids cited by the ledger are not in the claims file: MT002-C07-3, MT002-C04-4, MT016-C02-6, MT031-C03-R1, MT150-C13-R1, MT150-C14-R1, MT163-C17-X3, MT202-C17-R1, MT202-C16-R1, MT202-C12-R5, MT206-C08-1, MT227-C12-R2, MT227-C14-R1.
6. Twenty-one ledger rows marked resolvable carry no status; at least ten have closed windows (for example MT126-V006-1, MT227-V005-1, MT076-V005-1, MT163-V001-2).
7. Path calls are scored at end dates only; long-dated volatility views on the VIX (MT031-V002-3); the three-week Olympic view at six months (MT183-V006-1).
8. MT016-V002-2 codes higher volatility; the quote (MT016-C13-4) says only that flows are less positive.
9. Sources give upload dates, the ledger earlier made dates (MT206: 2024-10-06 against 2024-09).

Opus check first: (a) R2's placing of the gap after expiry and X as the third Friday; (b) form C's reading of MT163-C20-2; (c) R4's direction; (d) the ledger tallies in section 1; (e) whether any quote dates the 2025 fall.

## 13. Self-check: the strongest argument against each rule

- R1: a known seasonal pattern (checker's knowledge); the up-year gate is momentum under another name; about 36 windows in the design era; his own first season lost.
- R2: mostly plain exposure; he caps the effect at 40% and calls it absorbed; strong "95% of time" (MT227-C05-3) with violent exceptions is the profile note 1.3c warns against; design years precede the flows.
- R3: one dated case, a pandemic; both later live uses missed; it shorts what Trend holds.
- R4: the days are the reader's; the commonly described month-end rebalancing runs the other way (checker's knowledge); it may be one-month Trend.
- R5: inflation falls in about half of all months (reader), so version 1 is close to the standing steepener he says he holds (MT031-C13-4); in easing cycles curves steepen because the 2-year falls, which Trend holds; a pass would not show his long-end sell-off.
