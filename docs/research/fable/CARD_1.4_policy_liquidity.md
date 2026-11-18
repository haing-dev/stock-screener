# Playbook card 1.4, card 1: policy and liquidity (Druckenmiller, Bessent)

Unit 1.4, written 2026-11-18. Sources: 590 claims from 11 recordings, 2018 to 2026. Quotes are ground truth. Labels: SHOWN (numbers or a worked case in the quote), SHOWN (words), ASSERTED, reader (my inference). D = Druckenmiller, B = Bessent. The years of recalled trades (1992, 1999, 2000, 2012-13) come from claim text unless quoted.

> **Status (2026-11-17): PASS WITH CORRECTIONS.** Written by one Fable 5.2 run (effort HIGH, not max: user rule of
> 2026-11-16) from 590 verbatim claims of Stanley Druckenmiller and Scott Bessent (11 recordings, 2018-2026; no code
> reading), then checked by an independent Opus 5.5 run against the same quotes. The 45 corrections the check required
> are applied in this text; the check is `CARD_1.4_policy_liquidity_check.md`, its summary is the last section. Original
> Fable text, exact input pack and both briefs: macro-vault `pipeline/card_1.4_policy/`. The pack was built by script
> from the ledger (every quote matched), not by a Sonnet agent. Nothing here is registered or run.

## 1. Verdict

1. Playbook: find where policy is out of step with the economy, wait for a cheap one-sided bet, size it big, cut it fast. D reads the Fed through the inside of the stock market; B reads the people who make policy.
2. Part of it can be coded: six rules, 30 versions (60 with the two entry versions of section 6), all averaged; R6 fails the premise check (section 4) and is held back, leaving 28 (56) to register. Liquidity itself, peg breaks, policy personnel and conviction sizing cannot; the 1992 and Japan 2012-13 trades came from those, while the 2000 Treasury trade is coded in R1 and R2.
3. Strongest link: the 1992 peg break. Named loser, numbers in the quotes, both men tell it; but it is one trade of one fund (Soros's), so one case, not two. Rare, not codable.
4. Weakest link: the title idea that the quantity of liquidity drives prices. Asserted; D's 2018 stock short on it lost (claim text), and his 2021 short of the 2-year on "money supply growing at 40 percent" gained by his account from 15 to 150 basis points (MT149-C07-1, MT151-C10-4; trade and year are claim text). Central-bank and Treasury series do not cover most design years (reader); M2SL does, and enters R2 only as a warning.
5. Dating: four rules rest on three recalled pre-2011 actions (R1 and R2 on 2000, R3's stock leg on 1999, R5 on 1992), none dated by a year spoken in the quote; R3's bond leg, R4 and R6 are hindsight-flagged; nothing was recorded before 2018, so all six are hindsight under rule 5.
6. Record (ledger, machine-coded): D 4 of 16 forecasts right, 9 points below base rate, three recession calls missed; B one resolved row.
7. D says bond buying suppressed this playbook and macro was dead for 10 to 15 years: most of the holdout window.
8. Counts: 6 rules, 10 analyst questions, 11 open forecasts, 2 diagnostics.

## 2. Causal model

**C1. Easy money when none is needed.** The Fed eases, or stays easy, while the economy is strong. A bubble forms and bursts, and the next easing is more extreme. Other side: late buyers and lenders to weak borrowers. D, on 1998-99, 2003, the bond-buying years and 2021. MT152-C01-1, MT153-C07-5, MT148-C10-2, MT149-C01-2, MT153-C13-4 ("we had nine percent nominal growth in the fourth quarter and we had one percent rate", SHOWN: numbers in quote; the year 2003 is claim text). ASSERTED as a law. Limits: no definition of a bubble; shorting one early cost a "600 million dollar loss" (MT046-C05-5).

**C2. Tightening into a weakening economy.** The Fed keeps going ("we're going to continue to hike until something either starts to break or financial conditions tighten", MT152-C03-3) while leading parts of the economy turn down. Something breaks, the Fed reverses, short yields fall. Other side: holders positioned for the Fed's stated path. D in 2000 (SHOWN, one worked case: "350% 10-year equivalent", MT148-C11-2) and December 2018 (stated live, MT152-C08-1). "I always made it in Treasuries" (MT152-C07-6) is ASSERTED. Limits: off when inflation is high (2022-23; claim text of MT149-C07-3, whose quote gives only the playbook and the "10-year yielding 350"); his 2018 stock short lost (claim text), but it was made on QT, chain C5, not on this chain ("because I saw a cutie coming", MT152-C07-3).

**C3. Oil, dollar and rates up together.** Earnings fall a year later; then as C2. "the dollar is up interest rates are up and oil is up" (MT151-C12-1); the model is half currency, a quarter oil, a quarter rates and "it looks one year forward" (MT151-C12-2, SHOWN (words); Ed Hyman's model, claim text). Other side: analysts' earnings estimates. D in 2000. Limits: one case; in 2022 the same three rose ("that might sound a little familiar", MT148-C11-1) and he did not buy bonds.

**C4. Inflation above 5% with the policy rate below it.** "once inflation gets above 5%" it has not come down until Fed funds exceeded the CPI (MT148-C02-2), and "it's never been tamed without a recession" (MT148-C02-3). Bonds and stocks fall first, then the economy. Other side: buyers of assets during late bond buying (MT148-C01-1). D, 2022-23. ASSERTED: no episodes are listed. Limits: the recession call missed three times in the ledger.

**C5. Quantity of liquidity.** Central-bank buying, the Treasury's cash balance and money growth move asset prices: "it's always about liquidity" (MT153-C12-2); "it's not even the level it's the rate of change" (MT152-C04-1). Other side: not named (reader: whoever must absorb the bonds the Fed stops buying, MT152-C04-2). D, 2018 and 2023. ASSERTED. Limits: "I had no precedent" (MT153-C12-1); the 2018 short lost (claim text) and the ledger scores his 2018 liquidity calls wrong; against that, he calls the 2021 front-end short on "money supply growing at 40 percent" "a fat pitch" (MT149-C07-1) and took it off "at like 150 basis points" from 15 (MT151-C10-4; trade and year are claim text); "maybe markets don't anticipate the way they used to" (MT153-C12-3); on money supply in 2023, "it's not that simple" (MT149-C03-2).

**C6. A fixed exchange rate between economies that need opposite rates.** The weak one cannot hold rates up (floating-rate mortgages, MT141-C06-1, MT203-C04-1), the peg breaks, and local bonds and stocks then rise. Other side: the defending central bank: "they had to buy an unlimited amount of Sterling" (MT203-C03-3). Both men, 1992. SHOWN: "it was a half a percent" (MT151-C08-4; whether this is the holding cost or the distance from the band is not in the quote, pack problem 9), loss cap "the most they could push us back was 2 and a half%" (MT141-C06-2), gain "fifteen or twenty percent" (MT152-C10-4). Limits: "they come along very very rarely" (MT151-C09-3); such structures "always take longer to break down than you think" (MT203-C04-2).

**C7. A new policy regime, made by people who control the appointments.** An expensive currency, a leader elected on reflation, open seats at the central bank. The currency falls and "equities would be a good derivative of that" (MT141-C10-2). The policy need not succeed for the price to move (MT141-C10-7). Other side: those who say it can never happen, and sellers of cheap options (MT141-C10-5). B on Japan 2012-13 (MT141-C09-3, MT141-C10-1, MT142-C04-1). SHOWN (words), one case. Limits: his 2024 yen call lost (MT203-C10-3).

**C8. Deficits and the reserve currency.** Deficits near 7% of output (MT085-C01-3, MT203-C09-1) are tolerated because of reserve status (MT149-C09-1), until trust goes. B 2024: "my guess is that it's going to eventually be the dollar it could initially be rates" (MT203-C08-4). Other side: foreign holders of Treasuries (MT203-C06-3, MT203-C11-X1). Both, ASSERTED. D rules it out as a signal: "I don't think the entitlement situation is something you should be trading on in the next three to six months" (MT046-C01-2). No rule.

## 3. Indicators

| Indicator | Who uses it and how | Series (data sheet) | Lag |
|---|---|---|---|
| Fed path against the economy | D, all periods (MT152-C03-3, MT153-C07-1) | FEDFUNDS | 0 |
| Central-bank buying, rate of change | D 2018: "if you go from a trillion in central bank buying a year to zero" (MT153-C03-3, MT153-C12-5) | Fed: WALCL. ECB, Bank of Japan: no live series | 0 |
| Treasury cash balance and issuance | D 2023 (MT046-C04-4), 2018 (MT152-C04-2); B 2024 on bill issuance (MT203-C09-2, MT203-C09-3) | WTREGEN, RRPONTSYD (Compass netliq). Bill share: no live series | 0 |
| Money growth | D 2018 falling (MT152-C04-3), 2021 rising (MT149-C07-1, MT151-C01-4), 2023 doubtful (MT149-C03-2) | M2SL | 1 |
| Yield curve | D 2018 amber (MT152-C02-2), 2023 for timing (MT149-C02-7) | GS2, GS5, GS10 | 0 |
| Credit | D: credit leads (MT152-C02-3); 2024 "tight" (MT151-C01-5) | BAA minus GS10; HYG against IEF. Single-name default swaps: no live series | 0 |
| Leading industries inside the stock market | D: housing, trucking, retail, cyclical against defensive (MT152-C02-1, MT148-C03-2, MT148-C04-1, MT148-C04-X1, MT149-C02-4) | ITB, IYT, XRT, KBE against XLP, XLU, XLV; Compass cyc_def, homebuilders, transports; TRUCKD11, PERMIT. No history for the design years | 0; 2; 1 |
| Oil, dollar, rates together | D 2000 (MT153-C10-5, MT151-C12-1) | WTISPLC; TWEXMMTH then DTWEXBGS; GS10, FEDFUNDS; Compass squeeze | 1; 0; 0 |
| Inflation against the policy rate | D 2022 (MT148-C02-2) | CPILFESL (he says CPI; headline is not fetched), FEDFUNDS | 1; 0 |
| Gold against real yields; official gold buying | B 2024 (MT203-C08-2, MT203-C08-3, MT141-C12-6) | GLD, GC=F, Compass realyield. Official buying: no live series | 0 |
| Company talk | Both: "I do a macro from the bottom up" (MT151-C01-1; MT141-C05-1, MT141-C05-2) | no live series; DRCCLACBS for card arrears (MT203-C13-3) | 3 |
| Peg strain: holding cost, band, official words | Both, 1992 (MT151-C08-4, MT151-C09-1, MT141-C06-2) | forwards on LSEG; no list of pegs; statements: no live series | n/a |
| Positioning and option prices; currency value on purchasing power; current account | B (MT203-C03-1, MT203-C06-2, MT141-C09-3, MT142-C03-3); D on the dollar (MT069-C03-3) | not available, or not named on the sheet | n/a |

## 4. Rule layer

Common to all rules. Checked at each month-end with data as known then (lags above); series marked first-published on the data sheet (CPILFESL, M2SL) are used as first published where vintages exist, else latest values, flagged. Markets are the book's panel, as excess returns. A position runs from the first month the condition holds until 12 months after the last such month, unless stated. Reason: "it looks one year forward" (MT151-C12-2), and 12 months is the short end of D's stated horizons (MT046-C05-3). Legs and rules are held at equal risk and opposite positions net; nothing is sized by conviction. Four weekly tranches. Two entry versions for every rule (section 6); every version of a rule is run and averaged. Each formula is the reader's wording.

**R1. Squeeze.** If WTISPLC, the dollar index (TWEXMMTH to its last month, DTWEXBGS after; each L-month change is taken inside one series, reader) and a rate are all above their level L months earlier: long US 2-year note and US 10-year bond. Versions: L 6 or 12; rate FEDFUNDS or GS10; R4 gate on or off (8). The men give only a direction; 6 is the Compass window, 12 the model's horizon. No position while R4's state at 5.0 is on. That gate is the reader's link, made knowing 2022-23, from MT149-C07-3 to the 5% test of MT148-C02-2; the quote of MT149-C07-3 gives only his usual Treasury playbook and the "10-year yielding 350", and that he declined it for inflation is claim text, so the gate is a version, not a fixed part of the rule. Claims: MT153-C10-5, MT153-C11-1, MT148-C11-1, MT151-C12-1, MT151-C12-2, MT151-C12-4. Hindsight: action in 2000, recalled in 2018, 2022 and 2024; one case. Not in the pods: Trend sells bonds when yields rise; this buys them (reader).

**R2. Tightening into warnings.** If FEDFUNDS is at least 0.25 above its level T months earlier, and at least k of three warnings hold: (a) GS5 minus GS2 below zero ("we've inverted", MT152-C02-2); (b) BAA minus GS10 above its level 6 months earlier (MT152-C02-3; the Compass window); (c) 12-month growth of M2SL below its level 24 months earlier ("over the last couple years", MT152-C04-3). Then long US 2-year note and US 10-year bond. Versions: T 6 or 12 (as R1); k 2 or 3; R4 gate on or off (8). The 0.25 is one standard move (reader). Same gate as R1. Claims: MT148-C11-2, MT153-C11-2, MT152-C08-1, MT152-C07-6. Hindsight: 2000 recalled; December 2018 stated live (ledger: the stance scored right, the 50 to 60 basis-point level wrong). Not in the pods: he bought when "there was no price movement" (MT153-C11-2), so before Trend; Carry leans against bonds when the curve is inverted (reader).

**R3. Easing into strength.** If FEDFUNDS is at least 0.25 below its level 3 months earlier, BAA minus GS10 is below its expanding-window median (window from the first month both series exist), and the S&P 500 price level is above its 10-month average (panel index; Compass spx_trend live): short US 10-year bond, long S&P 500. Versions: spread below the median or in the lowest third ("tight" is only a direction); gold (panel gold; GC=F live) at a 12-month high required or not, since gold is in the 2024 quote only (4). The 3 months are one quarter (reader). Source: "to cut 50 basis points with credit spreads tight gold at new highs" (MT151-C01-5). Claims: MT151-C03-3 ("I shorted them literally the day the FED cut"), MT069-C03-6, MT069-C03-X2, MT151-C11-2, MT153-C07-5. Hindsight: the stock leg has a recalled 1999 action ("Everyone knows how I played the Nasdaq melt up in '99", MT069-C06-3; its link to the Fed's easing is claim text of MT151-C11-2), and that episode ended when he "bought the exact top" and lost "two or three billion" (MT069-C06-3, MT148-C11-X1); the bond leg is 2024 only, flagged, and the ledger scores it wrong at 12 months. Not in the pods: after a cut Trend and Carry tend to hold bonds, so the bond leg is opposite; the stock leg probably repeats Trend (diagnostic D2).

**R4. Behind on inflation.** State on while the 12-month change of CPILFESL is above 5.0% and FEDFUNDS is below that change; off otherwise, with no 12-month tail. Action A: short US 10-year bond and 2-year note. Action B: A plus short S&P 500 and long the panel's commodities at equal risk (he names none: "some of the key commodities"; reader) ("a matrix of short fixed income short stocks", MT148-C05-2). Versions: threshold 5.0 or 4.5 (MT148-C02-2, MT148-C02-1, both in quote); action A or B (4). Claims: MT148-C02-3, MT148-C02-X2. Hindsight: stated June 2022; the only related action in a quote is after 2010, a short of the 2-year from 15 to 150 basis points (MT151-C10-4, MT149-C07-1; trade and year are claim text); flagged. Not in the pods: Trend and Economic trend probably hold the same positions while inflation rises (D2); the level test and the exit are new.

**R5. After the fall.** For each G10 currency in the panel other than the dollar whose stock index (and, for the bond version, 10-year bond) is in the panel; the mark and then the euro map to the German index and Bund (reader): trigger when its 6-month return against the dollar is at least 15 points below the median of those currencies. Then long that country's stock index. Versions: 15 or 10 points; stocks only, or stocks plus its 10-year bond (4). The 15 is the size D gives for a break; 10 is an earlier entry and 6 months the Compass window (reader). Claims: "I bought guilts I bought British stocks" (MT151-C09-6); MT141-C10-2. The bond version follows D in 1992; the other follows B, who stayed out: "I don't really need to mess around in the jgb market" (MT203-C10-1). Hindsight: 1992 purchase recalled, one case; B's case is 2012-13. Not in the pods: Trend sells the falling currency; no pod buys the local stocks on the fall. Economic trend may: check at step 3.2.

**R6. Gold that ignores yields.** If over L months GS10 rose, the real 10-year yield (GS10 minus the 12-month change of CPILFESL) rose, and gold rose (panel gold; GC=F live): long gold. Versions: L 3 or 6, short because he speaks of a pullback (2). Claim: MT203-C08-2 ("real rates started going up in the US nominal rates started going up", which he calls normally "a signal that you're going to get a 5 10 could be 15% pullback"). Premise check fails: the long direction and the rise in gold are claim text; on its words the quote points to a pullback. R6 is held back from registration until a quote supports the direction; question 8 covers gold meanwhile. B, 2024. Hindsight: flagged. Not in the pods: Trend is already long rising gold; D2 decides.

Not a rule: liquidity quantity (section 11). It goes to the analyst layer.

## 5. Analyst layer

Every answer is a probability at 4, 13 and 52 weeks (D thinks 12 to 18 months ahead, MT046-C05-3, and 18 to 24, MT151-C05-3). Scoring: Brier score against base rate and against trend continuation, by the ledger's scorer.

1. Fed stance: chances that the R2, R3 or R4 condition (first-listed version of each, gate off) holds at the horizon, or none of them (in step), scored as one four-way Brier score; and the chance FEDFUNDS is lower.
2. Chance GS10 is higher.
3. Chance SPY returns more than SHY.
4. Chance WALCL minus WTREGEN minus RRPONTSYD is higher, with one line on the Treasury's stated borrowing plan.
5. Leading industries: chance that two or more of ITB, IYT, XRT are 20% or more below their 12-month high (Compass window); chance the Compass jobs alarm is on. Today's count is reported, not scored.
6. Chance the latest 12-month change of CPILFESL is higher than today's.
7. Chance DTWEXBGS is lower.
8. Chance GLD is higher; chance PCOPPUSDM is higher.
9. Policy brake (B, MT141-C12-7, MT141-C13-1; D's peg test, MT151-C09-2): up to three policies anywhere that must be reversed, each with a dated public act that would count, its chance, the market and the direction. Scored on the act.
10. Fat pitch: none, or one trade with market, direction, loss cap, a target at least five times the cap, and what would end it. Resolved at the cap, the target or 52 weeks, whichever comes first, and scored in units of the cap; weeks answered none are counted. The five-times ratio is the reader's; no quote gives it.

Each call in 2, 3, 7 and 8 is tagged with or against the 12-month trend and scored apart. This tests "the crowd's right 80% of the time" (MT069-C04-1) and "the crowd is right 85 or 90% of the time" (MT142-C01-3).

## 6. Process rules that are not signals

| What they say | Label | Status |
|---|---|---|
| "sizing is probably 70 to 80% of the equation" (MT148-C08-2); bet big on conviction (MT151-C08-2, MT151-C09-3) | ASSERTED | Dropped for rules: conviction is not codable and the shop fixes risk shares. Question 10 records it. |
| Start with a third, add on price confirmation (MT153-C10-3); "I tend to trade in thirds" (MT141-C10-8) | ASSERTED, both | Version, pod level: full at trigger; or a third at trigger and full once the traded market has moved the trade's way at a month-end. |
| Size down when cold, up when hot: "I had not earned the right to play big" (MT153-C11-4, MT148-C08-3); "you earn the right to take a risk" (MT141-C11-2, MT141-C11-1) | ASSERTED, both | Dropped for rules: B's form ("adding if the p&l is good", MT141-C11-1) is a formula, but the shop fixes risk shares (5.1). As an allocator B does the opposite: "when they are in a slump you add" (MT141-C12-1). Reported line: analyst scores after good and bad runs. |
| Sell when the reason is gone: "if the reason I bought a stock is no longer the case I don't care what I paid for it" (MT151-C07-2, MT069-C03-X3, MT152-C10-5) | ASSERTED | Registered with a deviation: a rule exits 12 months after its condition last held, so it keeps the position for a year after the reason is gone, against this quote; the tail rests on MT151-C12-2 and MT046-C05-3 (section 4). No price stop: they give no level. |
| Big bets only in liquid markets (MT153-C09-3); "you can be one thing but not many" (MT141-C11-5) | ASSERTED | Registered, met by construction: panel futures only. |
| Stand aside without a fat pitch: "keep your gross low" (MT149-C07-2, MT046-C08-1, MT141-C05-6); horizon 18 to 24 months (MT151-C05-3, MT152-C10-2) | ASSERTED | Registered: flat when no rule is on, idle risk is not moved; the 12-month hold and the 52-week answers. |
| Shorting stocks costs more when wrong, and his index shorts were "a disaster" in 2023 (MT046-C05-4, MT046-C05-X1, MT152-C07-5); but 2021-22 was "the best short-selling period I've ever seen" (MT148-C13-4) | SHOWN (words) | Version: R4 with and without the stock short. |

## 7. Dated forecasts still open

Outcomes were not looked up. D's 2026 recording has no stated date (ledger: 2025). For its rows marked none, the default horizon is his stated trade horizon in the same recording, "18 months to 3 years" (MT069-C03-7; reader).

| Who, made | Statement | Horizon | Resolves on | Claims |
|---|---|---|---|---|
| D, 2022-06 | "we look to be short energy for 5 or 10 years": supply short, he is long energy (claim text) | 2027-06 to 2032-06 | WTISPLC higher than in June 2022 | MT148-C06-2 |
| D, 2023-05 | Stocks not higher in ten years (claim text; the quote gives the reasons) | 2033-05 | S&P 500 level | MT149-C10-3 |
| D, 2024-10 | Possible second wave of inflation, as in the 1970s (an analogy conditional on easy conditions; the claim text calls it not a forecast) | none stated, so not resolvable as stated | 12-month change of CPILFESL | MT151-C01-3, MT151-C01-X1 |
| D, 2024-10 | Debt reckoning; stress likelier in late 2025 or early 2026 (claim text) | window passed | no test in the quotes; the ledger must rule | MT151-C02-3, MT151-C02-5, MT151-C02-6 |
| D, 2025 or 2026 | Bearish on the dollar | none | DTWEXBGS | MT069-C03-3 |
| D, 2025 or 2026 | Copper (claim text; the quote names no metal) "very tight for the next 8 years" | about 2033 | PCOPPUSDM | MT069-C03-4 |
| D, 2025 or 2026 | Short bonds against long risk assets; inflation takes off if the Fed cuts into a boom | none | GS10, CPILFESL | MT069-C03-6, MT069-C03-X2 |
| B, 2024-10 | Le Pen president: "I would predict that in the next 18 or 24 months" | closed 2026-10 | still open in the ledger; resolve now | MT141-C13-4, MT141-C13-X1 |
| B, 2024-10 | Long-term bull market in gold; Japan "could be" a secular bull market (Japan: claim text) | none | GLD; Japan index | MT141-C12-6, MT141-C13-3 |
| B, 2024 | The dollar is the eventual release valve, rates perhaps first | none | DTWEXBGS, GS10 | MT203-C08-4 |
| B as Secretary, 2026-03 | "a chance we can move to a substantially lower oil price regime" once the conflict ends (claim text) | medium term | WTISPLC against a pre-war month the ledger fixes before any outcome is read (the level below 60 is summary only) | MT142-C08-1 |

## 8. What would prove it wrong, when it stops, disagreements

**Proves it wrong.** A rule fails its placebo or adds nothing to the Core book. The analyst's Brier score is no better than base rate at the registered checkpoint. Two parts are already in doubt: the three recession calls of 2022-23 built on C4 and the leading industries, and the 2024 bond short built on R3.

**When it stops working.** D says so himself. Bond buying "suppressed all this volatility" (MT152-C05-2); bonds and currencies, the source of "about 70% of my money", were "pretty much squished" (MT153-C03-1); bond-market signals were cancelled (MT152-C01-5, MT148-C03-3); "these algos have taken all the rhythm out of the market" (MT153-C04-3); "the price signals that I learned how to read and how to listen to are broken" (MT152-C11-3); "technical analysis is about 20% as effective today" (MT069-C05-3). In 2026: "Macro has been dead for 10 or 15 years" and no longer is (MT069-C03-2). Stop flag for the spec (reader): FEDFUNDS below 0.5 while WALCL is higher than a year earlier. Reported, never used to switch.

**Disagreements.**
- Currency valuation. B 2024: "in currencies valuation never matters" (MT203-C10-4). D 2026 is bearish on the dollar "mainly because sort of the top of the historic range in terms of purchasing power" (MT069-C03-3). B in 2012 used valuation only with a catalyst (MT141-C09-3). This bears on the Value pod.
- Gold. B: reserve buying (MT141-C12-6) and the fiscal release valve (MT203-C08-4; its link to gold is claim text). D 2026: "It's not so much a monetary trade" (MT069-C03-5).
- Bonds after a currency break. D bought gilts in 1992; B stayed out of Japanese bonds.
- The crowd. Both call it usually right. B still hunts for "how could the consensus be wrong" (MT142-C02-1); D calls being contrary overrated (claim text, MT069-C04-1).
- D against himself. Treasuries were the bear-market trade until 2018 (MT152-C08-1) and not in 2023 (claim text of MT149-C07-3; the quote gives only the playbook and the 3.50 yield). Method was liquidity in 2018 (MT153-C12-2) and company talk in 2024 (MT151-C01-1). His 2023 view (MT149-C03-X2) covers both outcomes and cannot fail; the earlier split "70% inflation ... 30% deflation" (MT148-C16-X1) is a probability and can be scored.
- B against himself. The investor of 2024 said of Treasury issuance: "exactly the wrong thing to do is to move the maturities to the short end" (MT203-C09-2), and saw the US flirting with fiscal dominance (claim text, MT203-C11-2). The Secretary of 2026 calls it (the Treasury market, by the claim text) "the deepest, most liquid, and most most solid in the world" (MT142-C02-2). The quotes do not contradict each other; the clear case of B against himself is in sizing (section 6: MT141-C11-1 against MT141-C12-1). The 2026 words are an official's and are not used as an investor's view.

## 9. Dating table (rule 5)

| Thesis | Does a quote show him acting on it before 2011? | Flag |
|---|---|---|
| R1 squeeze | Yes by context: the 350% position "betting that Greenspan ... will reverse" (MT148-C11-2, MT151-C12-4) falls in Greenspan's tenure, before 2006 (reader); no year is spoken, 2000 is claim text; recalled 2018 to 2024 | one recalled case |
| R2 tightening into warnings | Yes by context, as R1 (MT148-C11-2 names Greenspan; 2000 is claim text); the three warnings are from 2018 | recalled case; warnings flagged |
| R3 easing into strength | Stock leg: yes, 1999 ("the Nasdaq melt up in '99", MT069-C06-3; the Fed link is claim text of MT151-C11-2). Bond leg: no | bond leg hindsight |
| R4 behind on inflation | No; stated 2022 | hindsight |
| R5 after the fall | Yes by context (Quantum Fund, the pound's band: MT151-C08-4, MT151-C09-6); 1992 is claim text; B's case is 2012-13 | one recalled case |
| R6 gold and yields | No; 2024 | hindsight |
| C6 peg break | Yes, 1992, both men | not coded |
| C5 liquidity quantity | No: "I had no precedent" in 2018 (MT153-C12-1) | hindsight by his own words |
| Leading industries | Asserted for 20 or 30 years (MT148-C03-X2); no dated case | hindsight |
| C7 policy personnel | No; Japan is after 2010 (MT142-C03-X1) | hindsight |

No source in the pack was written before 2011, and a recalled action is not a document. Step 1.5 must look for texts from the time.

## 10. Diagnostics (zero slots, positions only, no returns)

**D1. Episode count.** Design months 1975-01 to 2010-12. For each rule, count separate episodes (on-months at least 12 months apart), taking a month as on when any registered version of the rule is on. Gate: fewer than 6 and the rule leaves the rule layer and becomes a watch condition for the analyst. Reason: a placebo that shuffles signal dates needs dates to shuffle. R4 is the likely casualty (reader).

**D2. Already held.** Same months. For each leg, the share of on-months in which the registered systematic pods combined (Trend, Economic trend, Carry, Value, as specified at registration) hold that market with the same sign. Gate: above 80% and the leg is dropped. Aimed at R3's stock leg, R4 and R6.

## 11. Dropped ideas

- Net liquidity as a rule: D's threshold is global and the European and Japanese series are not live; WALCL does not cover the design years.
- Peg break as a rule: no list of pegs, no series for official words, rare.
- Leading industries as a rule: the sector funds do not reach the design years. Question 5 instead.
- Hyman's earnings model: the weights are in the quote, the units are not.
- Policy rate against nominal growth (MT153-C13-4): no trade is attached.
- Bear-market length after a bubble (MT148-C12-1): no codable bubble.
- Fourth-quarter seasonality (MT153-C12-4); Bitcoin in bull phases, gold in bear phases (MT148-C07-1): asides, no series.
- Emerging markets as first casualty of tightening (MT153-C03-6, MT153-C08-2): no threshold, no instrument.
- Selling an overpriced political tail (MT203-C06-2), buying event panics (MT203-C05-3): no option data; no rule for which events.
- Price action against news (MT069-C06-1) and the fiscal reckoning (MT046-C01-2): D himself rules them out.
- Year-end profit taking in currencies (MT141-C11-3): claim text only.

## 12. Numbers, pack problems, first checks

**In a quote:** 70% of profits; a trillion of buying to zero in 12 months; money growth "from about seven and a half percent to four percent"; 40% money growth in 2021 (period not stated); inflation thresholds 4.5% and 5%; weights 50, 25, 25 and one year; 350%; half a percent; 2.5%; fifteen or twenty percent; 10-year at 3.50; cut of 50 basis points; 80% and 85 or 90%; 70 to 80%; 9% growth against a 1% rate; 600 million; 20% as effective; 18 or 24 months; 8 years.

**Summary only (carry no rule):** 2-year at 6.04% and Fed funds at 6.5% in 2000; 40% made in the fourth quarter of 2000; the 2018 sector declines and yield levels; forward cost rising to 6 or 7%; bond short of 25% of assets in 2024; 8% inflation with 3% yields; oil below 60 before the war.

**From the ledger (machine-coded, descriptive):** D has 37 resolved rows, 12 right. The scorecard line counts 16 forecasts, 4 right, 9 points below base rate. B has 1 resolved row, wrong.

**Pack problems.**
1. MT152-C06-3 is the interviewer's sentence; the file note says interviewers' words are excluded. Not used.
2. The earnings forecast of 2000 is down 25% in MT153-C11-1, 35% in MT148-C11-1 and 36% in MT151-C12-2. None is in a quote.
3. MT085 repeats MT151. One statement is scored twice with opposite results: MT085-V001-1 wrong, MT151-V003-1 right.
4. Ten claim ids cited by the ledger are not in the claims file (for example MT142-C08-X2, MT153-C16-X1 and the ids ending R1 or R2).
5. MT203 is dated by its upload, November 2024. Its content precedes the US election and the Japanese prime minister's exit (MT203-C07-X1, MT203-C10-5), so it was recorded earlier (reader).
6. MT069 has no recording date: upload February 2026, ledger 2025. MT152 was uploaded 2020-01-06, but its content and the ledger date it December 2018 (MT152-C02-2, MT152-C05-X1); the card uses December 2018.
7. The digest's scorecard line has no column names and no line for B.
8. MT148-C02-1: the quote says 4.5%; the summary says 4.5 to 5%. MT148-C05-1: the summary adds 8% inflation and 3% yields.
9. MT151-C08-4 reads the half percent as holding cost; MT085-C02-X1 reads the same words as distance from the band.
10. Data sheet: no headline CPI, no European or Japanese central-bank assets, no sector history before the funds exist.

**Opus check, first:** (a) whether Economic trend already holds R1, R2 or R5; (b) the reader's link behind the gate on R1 and R2; (c) each threshold grid against its quote; (d) first dates of GS2, TWEXMMTH and panel gold; (e) the 12-month hold; (f) problems 3 and 5.

## 13. Self-check: the strongest argument against each rule

- R1. One recalled win. The same trio rose in 2022, by his own remark, and he was short bonds; the gate that excuses this was written knowing it, which is hindsight inside the rule.
- R2. The warnings are his 2018 list, which he called amber. Of his December 2018 calls the ledger scores 1 of 11 right (the Treasury stance). Buying bonds on an inverted curve costs carry while waiting.
- R3. Its only live use, the 2024 bond short, is scored wrong. The stock leg is Trend under another name.
- R4. The 1970s are one long episode (reader). Its forecast side has failed three times since it was stated.
- R5. The two cases were chosen policy changes; the rule also buys every crisis fall, where the logic may reverse. It codes the aftermath, not the trade that paid.
- R6. One remark by an investor explaining a position he held. Without the yield test it is Trend on gold.
- All six. Famous investors recalling wins, put into formulas by a reader who knows the history to 2026. Pass or fail, the rule layer says little about the men. Only the analyst layer's live record can.

## Independent check (Opus 5.5, 2026-11-17): summary

Full text: `CARD_1.4_policy_liquidity_check.md`. Verdict section of the check, verbatim:

Checker: Opus 5.5, effort high (quant and risk officer). Inputs read: the card (all), BRIEF_FABLE.md, all 590 quotes of pack/CLAIMS.json (plus machine fields for every id the card leans on), WORKFLOW sections 1-6, DATA_SHEET, FORECASTS.csv (120 rows), SOURCES, DIGEST, BRIEF_V2_RULES. Every cited id was looked up with tools/lookup.py. No web, no code, no backtests.

## 1. Verdict

PASS WITH CORRECTIONS.
1. Numbers: 23 "in quote" numbers checked, all in quote; 7 "summary only" numbers checked, all summary only; ledger counts reproduce (D 37 resolved, 12 right; pools A+B = 16 rows, 4 right; Dec 2018 1 of 11; B 1 resolved, wrong; 10 missing claim ids). 0 numbers contradicted.
2. Chains and attributions: 0 statements of one man given to the other; 9 places where claim text carries a label, a date or a premise the quote does not (2003, "half a percent" as cost, the 2023 Treasury refusal, gold's rise, energy direction, copper, Japan, the release valve, the 1999 action).
3. Rules: all series exist on the data sheet and lags match; 1 rule fails the premise check (R6: the quote points to a pullback, the long is claim text); 1 hidden choice built with 2022 knowledge (the R1/R2 gate, now a version); 5 smaller hidden choices (commodity basket, splice, euro mapping, S&P and gold series, vintages).
4. Omissions that change the record: the 1999 long behind R3 ended in his largest recalled loss; the 2021 front-end short on 40% money growth (a liquidity win) is missing; B's own allocator rule contradicts his hot/cold sizing.
5. 45 corrections (section 3), all applied by apply_check.py; 10 open judgement points; none hands a decision to the user.

Open judgement points, verbatim (none is a decision for the user):

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

Usage: Fable 5.2 high, one run, about 0.34M tokens (the max runs of 1.3a-c took 0.46-0.65M); Opus 5.5 high check, about 0.22M tokens as reported (the run was cut once by the usage limit and resumed).
