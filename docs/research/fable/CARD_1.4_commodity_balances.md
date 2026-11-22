# Playbook card 1.4 (5 of 5): commodity balances (Pierre Andurand)

Sources: MT124 (2022-03), MT125 (2022-09), MT123 (2024-05), all named; MT115 (late 2014), identity only probable, marked [P]. Labels: SHOWN, SHOWN (words), ASSERTED, reader. Quotes are auto-captions, copied as they stand; square brackets are my gloss. Summary only = in machine text, not in a quote.

> **Status (2026-11-22): PASS WITH CORRECTIONS.** Written by one Fable 5.2 run (effort high) from 201 verbatim claims
> of Pierre Andurand (Andurand Capital) in 4 recordings: MT124 (2022-03), MT125 (2022-09), MT123 (2024-05), and MT115
> (late 2014), whose speaker is only probably Andurand (every statement from it is marked [P]); no code reading.
> Checked by an independent Opus 5.5 run against the same quotes; the 33 corrections it required are applied in this
> text. The check is `CARD_1.4_commodity_balances_check.md`, its summary is the last section. Exact inputs, briefs and
> this run's original: macro-vault `pipeline/card_1.4_andurand/`. Nothing here is registered or run.

## 1. Verdict

1. Playbook: work out supply growth against demand growth, so whether inventories rise or fall, then the price needed to keep them between empty and full. Bet on large moves, months to years, where demand cannot flex and new supply is years away. Never sell options. Cut when the market stops making sense.
2. Little can be coded. His inputs (inventories, output, demand, spare capacity, exports, positions) have no series on the data sheet, which sees prices, the futures curve (LSEG, on the PC) and unemployment.
3. Most of the codable part is already in the book: his reading of the curve is Carry and Curve carry, his large moves overlap Trend only while prices run his way (reader; his 2022 structural long was held through a give-back, MT125-C08-6), his demand and inflation views are Economic trend. New: 2 rules, both hindsight-flagged; R2 fails the premise check and is held back (section 4), so R1 alone goes forward, with 8 versions (16 with the sizing version), and only if diagnostic D2 passes.
4. Strongest link: the arithmetic of demand that cannot flex (cocoa, worked in the quotes) and the storage limit (one recalled case with a number).
5. Weakest link: the supply forecast inside the balance, and so any dated price. The 200 below (MT124-C08-6) is conditional ("then") and undated in its quote; its ten-month horizon is ledger view text, and its premise, the Russian cut, never came, so the miss is a supply miss before it is a price miss (reader). In March 2022 he said Russia would have to cut "at least two million bars a day" [barrels] and that "around 200 oil" would then balance the market; the ledger has Brent at 118.11, then 78.40 ten months later; in 2024 he says there was "no Supply response at all". Ledger (machine-coded): 5 resolved rows, 3 right; two score an output forecast on the oil price (pack problem 6), leaving 2 of 3 price rows right, one by 0.6 points over the band.
6. Dating: nothing is documented before 2011. The earliest recording is 2014, identity probable. One recalled observation from the Lehman episode carries no rule.
7. Against the cards: agrees with card 1 on fast cuts (concentration rests on claim text only, section 6), with card 4 on forced flows in thin markets; conflicts with card 3's process, with our own volatility sizing, and with the Value pod.
8. Counts: 2 rules (R2 held back), 10 analyst questions, 3 open forecasts (4 more as context; 8 closed windows without a score), 2 diagnostics.

## 2. Causal model

1. **Balance to inventories to price.** Supply growth against demand growth sets the direction of inventories; "the price should move in order to keep the the inventories within kind of uh kind of in range that makes the market function" (MT124-C04-1; MT124-C02-4, MT123-C09-1). Other side: traders anchored on the old range (MT123-C04-2). Firm-level, all years. ASSERTED; one recalled case with a number: empty storage "could only take one and a half months of this really low demand before all the tanks were full" (MT124-C03-4; that this is April 2020 is claim text). Limit: no inventory series on our sheet.
2. **Demand that cannot flex plus slow supply gives a very large move, capped only where demand finally gives way.** For oil he puts that point at "around 200 oil" (MT124-C08-6): price must "bring that demand down by one and a half million bucks a day" [barrels] (MT124-C07-2). Oil: "ten percent move in the price it has an impact of maybe 0.15 percent" (MT115-C05-3 [P]); "you don't really generally have such thing as demand destruction for oil" (MT124-C07-3). Cocoa: 1.7 grams a day costs "1.7 Cent per day" (MT123-C02-7), SHOWN, his arithmetic. Copper likewise (MT123-C08-5), ASSERTED. Supply lags: see R1. So "you run out of inventories and then the price can go anywhere" (MT123-C02-5). Other side: shorts in delivered futures (MT123-C05-3); in cocoa the buyers were producers short of crop (MT123-C05-5). 2022 to 2024. Limit: the oil version produced the missed 200 call.
3. **The curve is the gauge.** "backwardation means the front end the first contracts are much higher than the back contracts and and it means that the market is very tight physically" (MT124-C02-2). Empty tanks at a delivery point: "then you can go to any price" (MT124-C03-5). Other side: whoever must deliver or take delivery. ASSERTED; his 2022 dollar figures are summary only. Observable on LSEG. This is what Carry trades.
4. **Only barrels the market does not expect move the price; feared losses that do not arrive fade.** "it's just the fears of how the sanctions will bite" (MT124-C02-3); Iran's return is "expected by the market" (MT124-C09-X1); the expected Russian loss: "we have not seen that yet" (MT125-C06-3); Gaza has "no impact at all" on supply (MT123-C10-3); Iraq in 2014 likewise (MT115-C04-X1 [P]). Other side: buyers of headlines. ASSERTED: the quotes speak of supply, not price; that oil fell because the expected Russian loss did not come is claim text of MT125-C06-3, and fear itself "keeps the market tight" (MT124-C02-3). Against his own forecast (section 8). Limit: no series for expected supply.
5. **Official buffers delay the price, then run out.** Reserve releases of "up to 5 million barrels a day for 12 months" (MT124-C07-1) "will have to stop" (MT125-C06-6); spare capacity sits with "only saudi kuwait and uae" (MT124-C09-2). Other side: governments. ASSERTED. No live series.
6. **Only a large recession or a credit shock cuts oil demand.** "so not small recessions but large recessions" (MT124-C08-1); "at the time we didn't see that demand was being hit but when le mans went burst" [Lehman, so 2008; reader] (MT124-C08-2). ASSERTED, one recalled case. Observable through UNRATE. Economic trend already trades it.
7. **Thin markets feed on themselves.** "if a market is twice as volatile they're gonna have half of the position in barrels" (MT125-C08-3); speculative length "went from 1.4 billion Barrels in 2018 to 300 million today" (MT125-C08-2); oil fell "from 105 to 95 dollars in less than 24 hours" (MT125-C08-1; "no news" is claim text, the quote ends "and there was no") and "then the price doesn't mean anything" (MT125-C08-5). Other side: funds that size by volatility, as our book does, and hedgers who must trade (MT125-C08-4). SHOWN (words), 2022 (MT125) and 2024 (cocoa: "less liquidity ... and then the Vol volatility increases", MT123-C05-6). Limit: no position data on the sheet.
8. **Long deficits go unpriced because capital is short-term.** Copper demand grows "1 million tons" a year while supply growth goes "zero to negative" (MT123-C08-2); funds with "very tight draw Downs" [loss limits] "tend to try to trade for the next few days" (MT123-C08-3). Other side: multi-strategy pods. ASSERTED; the figures are his firm's model output. Not observable.

## 3. Indicators

| Indicator | Who uses it and how | Series on the data sheet | Lag |
|---|---|---|---|
| Inventory level, direction, storage headroom; spare capacity | Core of his process (MT124-C02-4, MT124-C02-1, MT124-C03-4, MT123-C09-3, MT124-C09-2, MT125-C07-2) | no live series (EIA is not on the sheet) | - |
| Inventory to demand ratio | Cocoa: "at 19% and that's what drove us to $28,000 a ton of today's dollars"; "might go down to 13%" (MT123-C04-6, MT123-C05-1, MT123-C05-2) | no live series | - |
| Curve shape, front against back | Physical tightness (MT124-C02-2) | LSEG commodity futures curves, on the PC; the sheet names no contract codes | one day |
| Supply against demand growth; producer exports; crop surveys | Year-by-year balance and early reads (MT123-C09-1, MT115-C04-1 [P], MT123-C02-3, MT123-C04-1) | no live series | - |
| Speculative positions, open interest | Is a move fund-driven; market depth (MT125-C08-2, MT125-C08-X1, MT123-C05-4) | not available (positioning and flow data) | - |
| Real price against the earlier real peak | How far a shortage can carry (MT123-C04-4, MT124-C11-5) | WTISPLC, PCOPPUSDM, LSEG front contracts; deflator CPILFESL (reader: no quote names his deflator, and his two conversions, x5.1 for 1977 to 2024 and x1.47 for 2008 to 2022, need not use one index) | 1 month |
| Size of a recession | Oil demand falls only in large ones (MT124-C08-1) | UNRATE; Compass jobs_alarm | 1 month |
| Prices and their swings | Outcome; volatility up, positions down (MT125-C08-3) | WTISPLC, PCOPPUSDM, PIORECRUSDM; DBC and panel daily closes | 1 month; one day |

## 4. Rule layer

**Already held by the pods (not rules here; step 3.2 confirms).**
- Carry, directional: long a commodity whose front is above the back, short the reverse. That is chain 3 as far as it can be coded; no quote of his states a trade on the curve's sign (reader) (MT124-C02-2, MT124-C03-4).
- Curve carry (proposed): which contract month to hold. He says only "we'll pick like a month" (MT124-C03-X1); the quote names only the front month; the deferred month (December Brent) is summary only.
- Trend: his trades as he tells them, "the large moves in the old market" [oil] (MT124-C02-5), in part: his energy book "worked well in the first half of the year" 2022, but he held the "structural bullish position" through the give-back that followed (MT125-C08-6), which Trend would not; no quote says when he entered cocoa against its range (reader).
- Economic trend. Four of his rules would duplicate it: a large recession, so short oil (MT124-C08-1, MT125-C06-8); high inflation, so hold "energy it's agricultural products it's food it's metal" (MT124-C10-1); higher rates with dear energy cut spending (MT125-C11-5); China reopening adds demand (MT125-C06-7). One point passes to its spec: he says small recessions do not cut oil demand.

**Common to both rules**, as in cards 1 to 4 so the layers net (reader): checked at each month-end with data as known then; panel markets as excess returns; equal risk; opposite positions net; four weekly tranches; every version run and averaged. P is the month-end close of the front contract on LSEG commodity futures curves (codes fixed at step 3.1; a market without an LSEG curve or a panel return is out).

**R1. Range break where supply is slow.** Trigger month (reader's proxy: he enters on the balance, not on the price; the range is what other traders anchor on, MT123-C04-2): P is above every earlier month-end P, with at least 120 months of history (reader: a range must exist before it can break; card 2's minimum). Markets (reader's class: he says "metals" and names only copper, so precious metals are left out, since no quote ties their price to mine supply): copper and the other base metals in the panel ("for metals it takes anywhere between seven and fifteen years", MT124-C10-3; "10 to 15 years to bring a new mine", MT123-C08-4) and cocoa ("three to five years for that Cocoa Tree", MT123-C07-2). Not grains ("within a year you can change things", MT124-C10-3; he says it of all "agricultural products", so cocoa's place in the slow class rests on the 2024 quote alone, MT123-C07-2). No other market: no supply-lag quote. Action: long from the trigger month until H months after the last trigger month. Versions (8): H 36, the shortest lag he gives in the class (cocoa's three years; for metals, the only class the design window tests, he says "at least five years", MT124-C10-X1, so both versions sit below it), or 24 (reader; his bullish bets run "a few months or a few years", MT124-C02-X1); crude oil added or not (new projects take "seven years time", MT124-C10-4, but "only the u.s has a shorter cycle of probably 12 months", MT124-C11-1); real ceiling on or off: the position ends once P divided by CPILFESL (lag 1, first published where vintages exist) passes its own earlier high, his yardstick for how far a shortage carried (MT123-C04-4, MT123-C05-1, MT124-C11-5); using it as an exit is the reader's. Source logic: range traders "don't really ask themselves what makes that price right" (MT123-C04-2); without a supply response "then you need to have a demand response" (MT123-C04-3); such markets give a "position that you can hold for longer" (MT123-C07-3). Hindsight: 2022 and 2024; flagged. One live case, cocoa 2024, with no score in the pack. By his own figure the earlier cocoa high was in 1977 (MT123-C04-4), so cocoa cannot trigger between 1977 and 2024 (reader): the design window tests base metals and crude only. Not in the pods: Trend is long at a new high but leaves when its return turns; R1 stays through falls, which he sizes for ("be able to take a 50% move", MT123-C05-7). Value leans against what has risen far (digest B; reader): the opposite bet. Cards 1 to 4 hold no single commodity (card 1's R4-B holds them all above an inflation level). Registered only if D2 passes and D1 does not call it a duplicate.

**R2. Paper fall in a tight market. HELD BACK (Opus check): premise check fails.** In the source case he reduced: "I want to to reduce my positions" (MT125-C08-7); and the coded form holds neither of his two conditions, a thin market and a fall on no news (no position or news series), so what is left is Carry's long after a fall. Held back from registration until a quote supports buying such a fall; analyst question 6 covers it meanwhile. As drafted: Markets: crude oil in the panel (his statements are on oil). On when (i) the front contract is above the second contract at month-end and (ii) P has fallen by at least X over L months. Versions (4): X and L are 10% over 1 month or 20% over 3 months; gap version a, any positive gap, or b, a positive gap that is, as a share of P, no smaller than L months earlier, so the physical gauge did not loosen while the price fell (reader). The 10% rounds his case (ten dollars from 105 is 9.5%) "from 105 to 95 dollars in less than 24 hours" (MT125-C08-1), a one-day move read at a monthly check; 20% over 3 months is a slower version (both reader). For the gap he says only "much higher" (MT124-C02-2). Action: long crude while (i) holds, at most 12 months (card 1's convention; the ledger's default horizon). Off when the front falls below the second. Source logic: in a thin market a fall on no news carries no information (chain 7), while "look at my supply and demand balance for the next few years to me it looks bullish right" (MT125-C07-1). Joining chain 3 to chain 7 is the reader's: no quote says the curve stayed tight in September 2022. Hindsight: 2022; flagged. Ledger: his oil call of 2022-09 (MT125-V002-1) scored right, WTI 84.02 to 89.56 in 12 months, 6.6% against a 6% band. Not in the pods: Carry is already long here and Trend's shorter lookbacks are short or flat, but its 12-month versions can still be long after a 1- or 3-month fall (reader); R2 sides with Carry where the two disagree. It adds weight, not information (D1). Cards 1 to 4: no oil position of its own; card 1's R4-B holds crude with the other panel commodities while its inflation state is on.

**Not rules.** Fading a fear spike that the curve does not confirm: fails the premise check, since on his account fear alone "keeps the market tight" (MT124-C02-3). Anything read from inventories, spare capacity, exports or positions: no live series; analyst layer.

## 5. Analyst layer

Each answer cites its public source and date and gives probabilities at 4 and 13 weeks, scored by Brier score against the base rate on LSEG front contracts (WTI, copper, cocoa) unless stated.

1. Oil stocks: rising or falling against the seasonal norm (public weekly and monthly reports)? Probability that WTI is higher.
2. Curve: probability that the gap between the first and second WTI contract is wider than today. Scored on the LSEG curve.
3. Barrels lost: for each disruption in the news, have exports fallen (yes with a figure, no, unknown)? Probability that WTI is above its pre-event level at 13 weeks. The yes and no answers are tallied later.
4. Buffers: stated spare capacity and reserve releases under way. Probability that the main producer group announces higher output within 13 weeks. Scored on the announcement.
5. Demand: UNRATE against its 12-month low. Probability that the gap is 0.5 or more at 13 weeks (the usual bar for any recession, as jobs_alarm; he says only large ones cut oil demand, so the answer also states whether the rise looks large, reader) and that WTI is lower. Scored on UNRATE and price.
6. Thin market: has oil moved 9% or more in a day (his 105 to 95), or is 20-day volatility twice its one-year average? If yes, probability that half the move is reversed. Scored on panel daily closes.
7. Positions (public weekly report): speculative net length in oil, copper and cocoa against a year ago; did price move with it or against it? Probability that the last 13 weeks' price direction continues.
8. Copper: visible exchange stocks against the start of the year; price against the path of his fourfold call (PCOPPUSDM). Probability that copper is higher.
9. Cocoa: latest published inventory to grinding ratio against his markers 19% and 13%; West African arrivals against a year ago. Probability that cocoa is higher.
10. Real room: for oil, copper and cocoa, price over CPILFESL as a share of its earlier peak (by script); name any panel commodity at a nominal high but below its real peak. Probability that it is higher at 13 weeks.

## 6. Process rules that are not signals

- Never sell options: "we don't sell options we either flat options or long options" (MT124-C03-1); options for "a big move in a short period of time" (MT124-C03-2). ASSERTED, firm-level. Dropped: the book holds no options (as card 4).
- Size to survive: "be able to take a 50% move Mo against you on the way" (MT123-C05-7). ASSERTED. Sizing version for R1 and R2: notional set to the smaller of the volatility-sized notional and the notional at which a 50% adverse move costs one year of the rule's volatility budget (its annual risk allocation; reader's bar); the other version is volatility sizing as in cards 1 to 4.
- Cut what you cannot explain: "I don't understand really what's going on in the market", so "I want to to reduce my positions" (MT125-C08-7). SHOWN (words): he reports doing it in 2022, after he "gave back some gains" (MT125-C08-6). No exact trigger, so not coded. Registered for the analyst: a view is marked as not understood when price moves against it by more than one monthly standard deviation with no cause it can cite; such views are scored apart.
- Do not short a delivered commodity without stocks: "it's a dangerous commodity to short" (MT123-C05-3). Registered for this pod: no short while the front is above the second contract. Both rules are long, so it binds nothing today; it passes to step 3.1 as a note for Trend and Value.
- Horizon: bullish bets "a few months or a few years", bearish "over generally a few months" (MT124-C02-X1). ASSERTED. Used for R1's hold.
- Concentration: few markets; coffee "looked interesting as well" (MT123-C06-X1); that he left it is claim text, and no quote speaks of concentration (MT123-C05-7 points to smaller sizes). Dropped: rules stay at equal risk.

## 7. Dated forecasts still open

- F1. Copper "could go up four times" over five years. Made 2024-05-16; to 2029-05. Resolves on PCOPPUSDM: direction (ledger rule) and the fourfold level. MT123-C09-7, MT123-C09-6.
- F2. Copper "deficit that are more than a million tons and eventually more than 3 million tons in 2030". Made 2024-05-16. Resolves on a published balance; no live series. MT123-C09-5.
- F3. US shale has room for "10 years of also of strong supply". Made 2022-03; to 2032. Resolves on US output; no live series. MT124-C04-2. By 2024 he is unsure: "about to Peak or not we don't know" (MT123-C10-2).
- Context only: commodity supply "will actually cap the type of economic growth" over ten years (MT124-C11-2; no variable); US gas export capacity "not before you know 2026 or 2027" (MT125-C09-2); "we might lose some oil from Iran" under tighter sanctions (MT123-C11-3; conditional); strikes on Russian ports (MT123-C10-4; conditional).
- Closed windows without a score in the pack, for step 2.3: cocoa "above $20,000 a ton later this year" (2024; MT123-C05-8); cocoa to 13% after another deficit (MT123-C05-2); copper supply growth "zero to negative" by end 2025 (MT123-C08-2); copper's 2024 deficit above visible stocks (MT123-C09-3); US shale growth to 2024 (MT125-C07-3); US supply above expectations within 12 months (MT124-C09-3); gas prices high for two years (MT125-C11-2); the gas shortage solved in two to three (MT125-C04-3).

## 8. What would prove it wrong; when it stops; disagreements

**Wrong if:** inventories reach his markers and price does not go non-linear (cocoa near 13%, copper stocks exhausted); or his supply forecasts miss as often as the consensus he calls conservative (MT123-C02-2); or, in his own words for cocoa, "a bumper crop in West Africa next year" (MT123-C06-1), with the price then "towards ... five or $6,000 a ton" (MT123-C06-3). R1: D2 fails. R2: falls in a backwardated market continue as often as other falls.

**Stops working when:** supply gets faster or cheaper, the 2014 point from gas (MT115-C05-1 [P], claim text beyond the quote); governments clear the market by mandate, release or cap instead of price (MT124-C07-X2, MT125-C06-1, MT125-C03-5); the market is too thin for price to inform (MT125-C08-5); long-horizon money arrives and prices deficits early (MT124-C10-2).

**Against himself.**
- Russian supply: March 2022, a cut of "at least two million bars a day" (MT124-C06-3); September 2022, "we have not seen that yet" (MT125-C06-3), yet a loss "between one and two million barrels a day" is still expected (MT125-C06-5); 2024, "no Supply response at all" (MT123-C10-1).
- Supply response: in 2014 "there's not no like stable oil price that can last for the next 10 years" (MT115-C05-2 [P]); in 2022 "this time we might not have it" (MT124-C11-4; that it means a supply response is claim text).
- Demand: price does not destroy oil demand (MT124-C07-3), yet in the same recording price must "bring that demand down by one and a half million bucks a day" (MT124-C07-2) and "around 200 oil will be enough to to bring demand down" (MT124-C08-6); the "switch of about 35 percent for oil" (MT125-C02-5) is gas demand moving to oil, so it is no contradiction (reader); and cocoa grindings fell while demand "generally goes up" (MT123-C04-7, MT123-C02-6; he reads the fall as destocking).
- Staying power: sizing for a 50% adverse move (2024) against cutting a structural position he no longer understood (2022).

**Against cards 1 to 4 and the pods.**
- Card 1: agrees on fast cuts and real assets in inflation (its R4-B); concentration is claim text here (section 6). On oil in a squeeze he is split: the economy carried dear oil for years (MT124-C08-3), yet rates with dear energy cut spending (MT125-C11-5).
- Card 2: no quote of his speaks to spreading risk; a conflict on it would rest on claim text (reader).
- Card 3: conflicts. It sizes by volatility on short horizons; he blames volatility sizing for the "Snowball Effect" (MT125-C08-3) and short-horizon capital under tight loss limits for unpriced deficits (MT123-C08-3).
- Card 4: agrees that forced flows set prices over days to weeks; holds that the balance wins over months to years.
- Pods: with Trend and Carry; against Value in slow-supply markets; against volatility sizing as a habit.

## 9. Dating table (rule 5)

| Thesis | Earliest statement in the pack | Pre-2011 action in a quote? | Status |
|---|---|---|---|
| R1 range break, slow supply | 2022 (lags), 2024 (range, hold) | No | hindsight |
| R2 paper fall in a tight market | 2022-03 (curve), 2022-09 (thin market) | No | hindsight |
| Balance, inventories, price (chain 1) | 2014 [P]; 2022 | No; the storage case is after 2010 (claim text) | hindsight |
| Large recession cuts oil demand (chain 6) | 2022 | The Lehman episode recalled as an observation, no trade | hindsight; no rule |
| Process rules (options, 50%, cut) | 2022, 2024 | No | hindsight |

The claim text of MT124-C02-5 dates shorts to 2008 and 2014-15; the quote does not.

## 10. Diagnostics (zero slots; design months to 2010; gates fixed now)

- **D1 overlap (positions only, no returns).** R1: share of on-months in which the Trend versions with the longest lookback are long the same market by their average sign. At 75% or more, R1 is a Trend duplicate and is not registered. R2: share of on-months in which the average sign of the Trend versions is negative. Reported only while R2 is held back (section 4); if a quote later supports it, under 50% R2 is not the disagreement cell it claims and is not registered. Reported only: overlap with card 1's R4-B.
- **D2 premise of R1's class filter.** Count range breaks (first trigger month after at least 12 months without one) up to 2008-12, so that every 24-month outcome ends inside the design months, in the slow class (base metals and cocoa; crude, a version, reported apart) and in wheat, corn and soybeans. Measure: share of breaks with P higher 24 months later than at the break. Gate: slow class at least 15 points above grains, with at least 10 breaks in each class. Otherwise R1 is dropped unbuilt, since the class filter is its only thesis; too few breaks counts as not passed.

## 11. Dropped ideas

- Change in backwardation as a signal: the figures are summary only.
- Storage nearly full, so short: Carry holds it. Short oil in a large recession: Economic trend.
- Buying a thin-market fall on price alone: his own action then was to reduce.
- Gas against oil by energy content (MT125-C11-X1): only "marginally bullish oil" (MT125-C11-1); no conversion factors in the pack.
- Long uranium, gas exporters, reactor builders (MT125-C09-3, MT125-C09-4): no series on the sheet; one ledger row, right.
- Oil used per unit of output (MT124-C12-1), pension flows into commodities (MT124-C10-2), climate and softs (MT123-C07-1), currencies and the rule of law (MT124-C09-5): no series or no variable.
- European gas arithmetic (most of MT125): policy advice, not a trading rule. Its one unfiled trading stance: "early this year I became less bullish on carbon" because mandates come top down (MT125-C10-3); a past stance with no horizon and no series named on the sheet.

## 12. Numbers, pack problems, first checks

**In quote:** 0.15% per 10% [P]; one and a half months of storage; 5 million barrels a day for 12 months; at least two million barrels a day; around 200; the supply lags of R1; 105 to 95; 1.4 billion to 300 million barrels; twice the volatility, half the position; 19%, 13%, $28,000, 1977; above $20,000; 50%; 35%; one million tons, zero to negative; more than 3 million tons in 2030; four times. **Ledger (machine-coded):** 118.11, 78.40, 84.02, 89.56, the 6% band. **Summary only (carry nothing):** backwardation of $2, then $4 to $5; cocoa ratio 21% against 35 to 40%; cocoa downside $7,000 to $5,000; the dated shorts. **Reader's:** 120 months, 24 and 36, 10% and 20%, 12 months, 9%, the gates of section 10.

**Pack problems.**
1. MT115-C03-4: the quote ("we lost um you know a day of production") supports none of its claim text.
2. Claim text only: the dated shorts of MT124-C02-5; all dollar figures of MT124-C02-2; April 2020 in MT124-C03-4; the 21% and 35 to 40% of MT123-C04-8; the downside figures of MT123-C05-8.
3. MT123-C05-8: the quote opens "you have to be out completely", a cut fragment; read alone it says the opposite of the claim (reader).
4. MT123-C10-1: Iran's exports and US growth are claim text; the quote covers Russia only. MT125-C06-8: the upward skew is claim text.
5. MT123-C02-7: the caption reads "$110,000 a ton"; his arithmetic fits $10,000 (reader).
6. Ledger rows MT124-V002-1 and MT125-V002-2 score forecasts of Russian output on the WTI price (one right, one wrong); by MT123-C10-1 both missed on their own variable. The first is scored at 12 months though its horizon text is a matter of weeks.
7. Ledger row MT123-V001-1 (cocoa, 2024) has a closed window and no score; section 7 lists seven more.
8. MT124-C08-2 puts $147 at about $200 today in claim text; the quote of MT124-C11-5 says "150 dollars then is 220 today".
9. The data sheet names no LSEG contract codes and does not list the panel's commodities; whether cocoa and the base metals are traded there is unknown.
10. MT115: identity probable only; no alias entry.

**Opus check, first:** (a) R2's join of chains 3 and 7; (b) R1's real-ceiling exit and class list; (c) verdict line 5 and the ledger recount; (d) what Carry, Trend and Economic trend already hold; (e) MT125 for any trading statement filed here as policy advice.

## 13. Self-check: the strongest argument against each rule

- **R1.** It is Trend with a longer leash, built from one live case whose outcome the pack does not show. The design window has no cocoa case and few metal breaks. A nominal high is common in any inflation, so the rule may be an inflation bet that Economic trend and card 1 already hold. The 2014 panel [P] argues that technology brings cheaper supply (claim text). Holding through a 50% fall suits a man who can cut on judgement, not a fixed rule. For copper he names a fast supply response too: "when prices go up you get more scrap Supply" (MT123-C09-2).
- **R2.** His own action in the source case was to reduce. Carry already holds the position, so the rule doubles a bet. The one scored case passed by 0.6 points. Thin markets fall "more easily than ever" (MT125-C08-X2), so falls can continue. The 10% comes from one day, and the join to the curve is mine.

## Independent check (Opus 5.5, 2026-11-22): summary

Full text: `CARD_1.4_commodity_balances_check.md`. Verdict section of the check, verbatim:

## 1. Verdict

PASS WITH CORRECTIONS (33 corrections; 0 contradicted numbers, 0 wrong ids, 0 MT115 statements without the [P] flag).
A. Numbers: 41 checked; 33 in quote, 5 ledger (all match FORECASTS.csv), 3 rightly marked summary only; 1 rounding to state (105 to 95 is 9.5%, not 10%); the 200 call is cited without its id, and its ten-month horizon is ledger view text, not quote.
B. Chains: 8 chains, 6 sound; chain 4 is labelled SHOWN (words) but its price step is claim text (ASSERTED); chain 2's "no ceiling" overstates (he puts oil's demand point at "around 200"); "his realised trades are Trend" is contradicted by MT125-C08-6 (a structural long held through a give-back).
C. Rules: R1 sound after 5 fixes (hidden class choices, holding lag reason, trigger labelled as proxy). R2 fails the premise check: in its source case he reduced (MT125-C08-7), and its coded form holds neither of his conditions (thin market, no news): held back, like card 1's R6. Count after correction: 1 rule forward (8 versions, 16 with sizing), 1 held back.
D-F. D2 reads 24-month outcomes past 2010-12 (look-ahead into the seal: cut at 2008-12); 6 important omissions; concentration rests on claim text only; dating table correct (nothing before 2011); no decision handed to the user; all forecasts correctly open or closed.

Open judgement points, verbatim (none is a decision for the user):

1. R1 holding grid {24, 36} sits below his metals lag (at least 5 years); whether to use a per-class lag (36 cocoa, 60 metals) is for step 3.1 as a registered version, not now.
2. R1 crude version: his 12-month US cycle (MT124-C11-1) and shale discipline (MT124-C04-4, MT125-C07-5) pull opposite ways; step 3.2 judges whether crude belongs in the slow class at all.
3. Which base metals have an LSEG futures curve and a panel return (LME metals may not): step 3.1; if only copper, D2's 10-break floor likely fails, which drops R1.
4. Roll convention for "the front contract at month-end" (delivery month): step 3.1.
5. Economic trend duplicates (recession short oil, inflation long commodities, China reopening): whether the pod reads Chinese growth is not in the pack; step 3.2.
6. R2 release from hold: only if step 1.5 or a later pack finds a quote of him buying a fall in a backwardated market.
7. Ledger rows MT124-V001-1 (conditional, undated 200 call scored at 10 months) and MT124-V002-1 / MT125-V002-2 (output scored on price): step 2.3 rescoring.
8. Deflator for the real-ceiling version (CPILFESL vs a headline or global index): step 3.1, as a version if kept.

Usage: Fable 5.2 high, about 0.27M tokens; Opus 5.5 high check, about 0.24M tokens.
