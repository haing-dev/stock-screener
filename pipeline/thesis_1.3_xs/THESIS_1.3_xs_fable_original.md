# Thesis note 1.3b: value, momentum and carry across markets (QP15, QP08)

Fable unit 1.3b, 2026-11-15. Source logic only: no code, no data, no results of ours.
Labels: SHOWN = the quote gives a test with numbers. SHOWN (words) = the quote reports a test, numbers summary only. ASSERTED = no test. reader = my inference. Words in double quotes are copied from the quote field of a claim cited on the same line.
Terms: *cross-asset* = markets ranked against each other inside an asset class, long the top, short the bottom, no net position. *Cross-sectional* means the same. *Directional* = each market long or short on its own signal. *Carry* = what a holder earns if prices do not move. *Sharpe ratio* = return per unit of risk. *Backwardation* = the near futures contract costs more than later ones.

## 1. Verdict

- **Carry: thesis supplied in three parts, grade weak on this pack.** Payers: savers who want safe currencies and hedgers of commodities (QP08, asserted); borrowers who fix long rates (reader: QP08 names no payer for bonds). Evidence: one sellers' paper, 1990 to April 2015, before costs.
- **Value: thesis supplied with a reservation.** Pattern moderate (two papers agree in words); payer not established. Working reading: investors chase winners until prices overshoot, and Value is paid when prices come back. Two rivals kept apart.
- **Cross-sectional momentum: neither a pod nor a Trend version.** It is what is left of Trend once each asset class's average position is removed (QP08-C21-4). No payer of its own; the weaker form (Sharpe 0.42 against 0.96, QP08-C17-1).
- **Registration:** Trend directional only. Carry in both forms: 2 versions, unchanged. Value cross-asset only.
- **Changes to the charter:** Value from 1 version to 2 (a second anchor for bonds and currencies). Carry's grid stays; equities stay out. Two zero-slot diagnostics (X1, X2).
- **Rule 5:** the pack dates neither paper before 2011. Step 1.5 must date older sources for both pods, or the verdict rule makes them Incubator.
- **Weakest link:** nobody establishes who pays Value. The risks the authors test do not explain it; funding-liquidity risk has the wrong sign (QP15-C03-4, C34-2).
- **Limits on everything:** before costs; both author groups sell these strategies; QP08's sample runs 52 months into our sealed years.

## 2. What the two papers establish

Covers: S = individual stocks, I = country equity indexes, B = bonds or rates, C = currencies, K = commodities.
Limits common to all rows. QP08: January 1990 to April 2015 (QP08-C09-4); I, B as swaps, C, K, no stocks (C09-5); before costs (C09-6); daily trading (C21-1); whole sample; styles "popular because they have worked" (C02-4); "There was no fitting in this exercise" (C26-3), other set-ups called similar without figures (C12-4); authors at Man Group (speakers field). QP15: 1972 to July 2011, later starts by class (QP15-C06-4, C07-2b); S pooled with I, B, C, K; before costs (C48-1); monthly (C48-4); whole sample; one measure per style and class (C19-1), bonds excepted; class weights from "realized volatility over the full sample" (C49-3); AQR "invests in, among other things, value and momentum strategies" (C01-5b).
Our design months (to 2010) lie inside QP15's sample and, from 1990, inside QP08's: a design-era test largely repeats the papers and adds little evidence (reader).

| # | Statement | Label | Claims | Words or numbers that carry it | Covers | Limits |
|---|---|---|---|---|---|---|
| 1 | Momentum earns more directionally than across assets | SHOWN | QP08-C17-1, C21-3 | "momentum more than doubles its Sharpe ratio from 0.42 to 0.96"; "momentum works well in time series, but poorly in the cross section" | I, B, C, K | no test of the gap; holds "to the extent that the global factor is trending" (QP08-C22-1) |
| 2 | Value works across assets, poorly directionally | SHOWN (words) | QP08-C21-3 | "value works well in the cross section, poorly in time series" | I, B, C, K | authors blame one-way markets (QP08-C18-1); zero point of the directional signal not stated |
| 3 | Carry works alike in both forms | SHOWN (words) | QP08-C21-3 | "carry works about equally well in both cross section and time series" | I, B, C, K | survivorship (dead markets dropped) "will likely favor value and carry" (QP08-C26-4) |
| 4 | A cross-asset book is the directional book minus the class average; an equal mix hedges half of it | ASSERTED (algebra) | QP08-C21-4, C23-4 | "cross sectional portfolio weights are equal to time series weights minus the cross sectional average"; "with half of the cross sectional mean hedged out" | any | exact only when positions are proportional to the signal (claim text) |
| 5 | Value and momentum pay in every market studied | SHOWN (words) | QP15-C02-2 | "consistent and ubiquitous evidence of value and momentum return premia across all the markets we study" | S, I, B, C, K as one claim | figures by class are summary only; bonds fail (row 6) |
| 6 | Bonds: no reliable premium with the first-choice measures | SHOWN | QP15-C19-2, C19-1b | "we are only able to produce a Sharpe ratio of 0.18"; "do not produce statistically reliable premia" | B | other measures are reported beside it (figures summary only) |
| 7 | Value and momentum move against each other | SHOWN | QP15-C17-1, C18-1, C22-4 | "averaging about –0.60" (S, per claim text); "within each asset class that averages –0.49" (I, B, C, K, per exhibit field); "of –0.28" (S with market value lagged a year, per claim text) | S; I, B, C, K | partly built in (reader, from QP15-C08-3, C09-6): value uses today's price, and in B, C, K it is itself a past return; no lagged test there |
| 8 | Cross-sectional momentum does worse in recessions and when funding (borrowing for traders) tightens; value does worse when funding eases (after 1998 only) | SHOWN (words) | QP15-C28-7b, C51-4, C35-1 | "significantly negatively related to recessions, especially among nonstock asset classes"; "these patterns appear only after 1998"; market by market the link is weak, t-statistics "for value is –0.95 and for momentum is 1.81" | pooled; I, B, C, K most for recessions | a same-month link, not a forecast (reader) |
| 9 | The risks tested do not explain Value | SHOWN (words); logic ASSERTED | QP15-C03-4, C34-2, C03-3, C43-1 | "liquidity risk is negatively related to value"; "cannot explain why both value and momentum earn positive risk"; "only modest links to macroeconomic variables" | pooled | liquidity risk is paid ("24 basis points per month", meaning per claim text), so Value sits on the wrong side of it |
| 10 | Why the two exist: return chasing and fund flows | ASSERTED | QP15-C04-6, C05-4b, C01-4b | "investors chase returns and flock to the assets whose prices appreciated most recently"; "remains an open question" | any | authors: "a challenge to existing behavioral, institutional, and rational asset pricing theories" |
| 11 | Carry by class: risk (C), hedging and storage (K), roll-down (B) | ASSERTED | QP08-C04-5, C05-5, C05-8, C05-9 | "hold their own in low domestic consumption states"; "producers selling futures to insure themselves"; "links backwardation to tight inventories"; "Rates tend to roll down the curve" | C, K, B | citations and textbook logic |
| 12 | The market factor alone gives carry no pay | ASSERTED (derivation) | QP08-C04-3 | "The sign of the forward bias is independent of carry" | any | a model |
| 13 | Equity carry is close to equity value | SHOWN | QP08-C18-5b, C04-4 | "correlation is 51%, confirming that both strategies are similar in nature"; "The higher the dividend yield, the higher the carry" | I | directional form (claim text); 51% leaves about three quarters of the variation unshared (reader) |
| 14 | Value mirrors carry in currencies and commodities | ASSERTED | QP08-C09-1, C14-4 | "the value premium is perfectly neutralized by the carry"; "a low spot price (revealing deep value) goes hand in hand with a lower convenience yield" | C, K | a model; correlations summary only |

## 3. Pods

### Carry (existing book)

- **Chain.** A forward price is set by people passing on a price risk; whoever takes it earns the gap if the price does not move (reader). QP08 shows only that a forward must be biased (QP08-C03-3); by row 12 the payer must be named class by class (quotes in row 11).
  - Currencies (ASSERTED): a risk premium; the implied payers are savers who accept low rates on currencies that hold up in bad states.
  - Commodities (ASSERTED): producers who insure against price falls, or hedgers on either side (QP08-C05-7).
  - Bonds: pattern, no mechanism. The quote names no payer; claim text of QP08-C05-9 mentions a liquidity premium and preferred habitat; borrowers who fix a long rate are my reading (reader).
  - They keep paying because the need for safety or insurance stays (reader).
- **Rivals.** Currencies: pay for losses in bad states (QP08-C04-5); for a jump that "has not materialized" (C05-3), so the sample flatters carry; or for a central bank regaining trust (C05-4), so no bad state follows. Commodities: insurance, so pay follows hedgers' net position; or storage (C05-8), so the slope only reports scarcity. The predictions are mine (reader); none is tested.
- **Grade: weak on this pack.** One sellers' paper; one sample; before costs; emerging markets included (claim text of QP08-C29-1) with the survivorship of row 3; no figure for carry alone in a quote. QP15 only cites a carry paper. This grades the pack, not the literature.
- **Rule.** Markets: bonds and notes, currencies, four energy futures (digest). Signal: bond yield minus the 3-month rate; 3-month rate gap to the dollar; slope between the first two energy contracts. Version 1, directional: long if carry is positive, short if negative. Version 2, cross-asset: position by rank of carry inside the class. Weights, sizing and the four weekly tranches are the charter's.
- **Grid: 2, unchanged; averaged.** Dimension: form. Doubt: QP08 finds the forms alike (row 3) and does not say which part is paid, class-wide or relative. By row 4 the average is roughly directional carry with half its class-wide position hedged. Fixed: markets; no equities, since equity carry rises with the dividend yield Value already ranks on (row 13). Dropped: roll-down, the gain as a bond ages down a rising curve ("carry + roll down", QP08-C10-4); it needs a second maturity per market, shown on LSEG only, licence for live use unverified (digest).
- **Data.** Engine panel from 1975, live weekly on free data. The sheet lists 3-month rates, not bond yields or second energy contracts.
- **Stops working.** Rate gaps and slopes near zero everywhere (reader). A bad state is the risk being paid: QP08 reports drawdowns "of order 1.8 to 3.1 times the volatility" (QP08-C13-3) and "negative performances for at least three years" (C27-1). Failure signs: currency losses without a bad state; no hedger paying ("backwardation is not the norm", C05-6); a long rise in yields, as the directional bond leg may be a standing long position (C17-2b).
- **Relations.** Trend holds carry too: a carry premium "will accumulate though the total return and produce a momentum effect" (QP08-C18-4, ASSERTED; charter point 4). Value is the opposite trade in currencies and commodities (row 14). In bonds Value's real yield and Carry's signal differ only by the short rate less inflation (reader); X2 shows whether Value's bond leg is paid by income.
- **Rule 5.** Not before 2011 on the pack: QP08's sample "ends in April 2015" (QP08-C09-4); the cross-asset carry paper is dated in a quote, "Koijen et al. (2012) document global" (QP15-C04-5); Keynes and the theory of storage carry no year (QP08-C05-5, C05-8). (author's knowledge) Older sources exist: Keynes 1930 (commodities), Fama 1984 (currencies), Fama and Bliss 1987 (bonds). Step 1.5 must cite one per class.
- **Batch.** Existing book.

### Value (existing book)

- **Chain, working reading (ASSERTED).** Investors chase recent winners (row 10) until flows "eventually push prices away from fundamentals causing reversals or value effects" (QP15-C05-1). That crowd is the other side. Value "represents a contrarian view" (C04-8b) and is paid as prices come back. The crowd keeps paying because money follows past returns; whether that is big enough is open (row 10).
- **Rivals.** Risk: cheap assets carry "a higher long term exposure to consumption risk" (QP08-C09-2, on S), so they should lose in bad states; rows 8 and 9 show the opposite sign for funding stress and little for macro. Anchor without a payer: the real economy closes the gap, as when producers "boost (reduce) supply" (QP08-C08-4); then forwards should hold it and nothing is left after income (row 14), yet QP15's currency returns "implicitly include the local interest rate differential" (QP15-C07-3b) and row 5 reports a premium, in words. The chase fits row 7 and the losses during one-way moves (QP08-C22-4), but row 7 is partly built into the measure.
- **Grade.** Pattern: moderate pooled (two groups, different measures and samples, agree in words; QP15 kept "the most studied or simplest measure in each case", QP15-C19-1). Weak for any one class: the only figure in a quote is 0.18, for bonds. Mechanism: not established; X2 tests its core claim.
- **Rule.** Markets: equity indexes, long bonds, currencies (digest). Cross-asset only: rank inside the class, long cheap, short dear. Version 1 (today): dividend yield; real yield (yield minus inflation); five-year real fall of the currency. Version 2 (added): dividend yield; "the 5-year change in the yields of 10-year bonds" (QP15-C09-5); the real (price-adjusted) exchange rate against its own average over all history to date, at least 60 months ("relative PPP", QP08-C11-3; the window is mine). Sizing and tranches as for Carry.
- **Grid: 2 (was 1); averaged.** Dimension: anchor, a fundamental level (QP08-C06-8) or the market's own level five years ago (QP15-C09-6). Doubt: fair value cannot be observed; the papers differ for bonds and currencies; "Most practical implementations use a variety of measures for a given style" (QP15-C50-3). No gain is expected: version 2 adds the measure of row 6. Version 1's bond measure is close to the alternative that looked better in QP15's own sample (figures summary only); keeping it alone would be a pick. Fixed: form; markets; one equity measure (book value over price, QP15-C09-2, is unavailable; the five-year measure is checked against it on U.S. stocks only: 0.83, QP15-C10-1). Excluded: QP15's yield-minus-short-rate measure (claim text of QP15-C16-1), which is Carry's signal. Not added: commodities, traded for value in both papers (QP15-C09-3, QP08-C11-5) but not in the engine; a cheap commodity has low carry (row 14), so the leg would mostly reverse Carry and Curve carry.
- **Data.** Engine panel, live on free data; version 2 needs five years of each series first. The sheet lists consumer prices, not dividend yields or bond yields (LSEG: from 1973 and 1979-12). Consumer prices enter at release date (WORKFLOW section 5). Unavailable for QP15's own measures: index book value over price; the forecasts in "Value = real bond yield (10-year yield to 5-year inflation forecast)" (QP15-C16-2b).
- **Stops working.** While the chase lasts: "very strong trends which have by definition hurt reversion based value predictors" (QP08-C22-4). When the anchor moves for good: the dividend yield "can be time-varying and thus not necessarily a measure of value" (C08-2). When funding eases (row 8). When income given up while waiting exceeds the price gain (row 14).
- **Relations and testing.** Row 7 is shown against cross-sectional momentum only, the part of Trend left after the class average (row 4). So: (i) Value is judged by what it adds to a book holding Trend (WORKFLOW test 1), never alone; (ii) in A2 version 2 is read with Trend's old grid and its new one; (iii) losses while Trend's relative part gains are expected; losses together are the warning.
- **Rule 5.** QP15 has no date in the pack. Its sample runs to "July 2011" (QP15-C07-2b); it cites 2012 work (C04-5); the digest says 2013. "A previous version of this paper" (C30-4) is undated; (author's knowledge, to be verified) working papers circulated in 2008-09 with the same classes. Older dated sources in quotes: "DeBondt and Thaler (1985)" for the five-year measure on S (C09-6); the "overshooting model (1976)" for currencies (QP08-C08-6). Claim text calls QP15's evidence for value in B, C and K new (QP15-C02-2), so the date of its first version decides; step 1.5 must find it.
- **Batch.** Existing book; version 2 enters with the A2 grids.

### Cross-sectional momentum (not registered)

- **Rule it would use.** Rank a class on "the return over the past 12 months skipping the most recent month" (QP15-C09-1b); long winners, short losers, weights by rank, monthly (C10-4, C48-4).
- **Chain and grade.** Trend's stories, no payer of its own: return chasing (QP15-C04-6), slow reaction and flows (QP08-C06-3, C06-5; ASSERTED by citation). QP15 calls time-series momentum "separate from the cross-sectional momentum strategies we study here" (QP15-C04-4): two forms, not two payers. Weak as its own pod: it pays in words (row 5) and is the weaker form (row 1), less so in currencies and commodities, "where a global factor is much less apparent" (QP08-C22-3).
- **Not a Trend version.** A version averages over doubt about one bet. This form removes the class-wide position (row 4), the only part that can be short a whole class in a crisis, the profile the charter wants reported for Trend. It does worse in recessions and funding squeezes (row 8). No source runs trend with the class hedged: "in futures trading, momentum is typically applied directionally" (QP08-C02-1).
- **Not a pod.** Trend already holds the relative part. A second pod would double it and hedge part of Trend's class-wide position (row 4): a new risk shape, not a new return source.
- **Data:** complete. **Rule 5:** QP15-C02-7 dates momentum in currencies and commodities to work of 1990 to 2008 (of use for the charter's open point 9). **Batch:** not now. For the Trend spec, one reported line: return split into class-average and relative parts.

### Other candidates

| Candidate | Support | Fate | Reason |
|---|---|---|---|
| Directional value | QP08, row 2 | rejected | another bet: the whole class returns to a fixed anchor (section 4) |
| Equity-index carry | QP08-C10-2 | rejected | row 13 |
| A pod of half value, half momentum | QP15-C18-4 | rejected | two mechanisms; the mix arises in the book |
| Switching styles on funding stress, or forms on correlations | QP15-C51-4; QP08-C27-3 | rejected | row 8: same-month, after 1998, weak by market; the second is only "suggestive of a framework"; both are timing |
| Curve carry's switch (charter point 5) | QP08-C05-7, reader | two versions stand | far against near loses carry in backwardation if the curve is steepest in front: a reason that owes nothing to the seller's hindsight |

## 4. Directional or cross-asset

What QP08 shows per style is rows 1 to 3: momentum better directional, carry alike, value better cross-asset. The authors' reasons are ASSERTED: class-wide factors trended (QP08-C22-1), and for value "25 years, the value factor, which relies largely on mean reversion, was bound to underperform." (QP08-C18-1).
Registration. Trend: directional, 16 versions as in the charter. Carry: both forms, 2 versions. Value: cross-asset only, 2 versions.

- 52 of QP08's 304 months lie in 2011 to April 2015: its comparison is no design-era fact. I use its logic (row 4), not its Sharpe ratios.
- Value is not also registered directionally. The cross-asset form needs markets to share an anchor. The directional form needs the anchor to stand still, which QP08 doubts (QP08-C08-2), and it bets against the class-wide move Trend holds on purpose: another bet, not doubt about the same one. No source argues for it, and QP08's test cannot be rebuilt (section 8, item 4).

## 5. Diagnostics (zero slots, design months to 2010-12)

**X1. Is energy carry a calendar pattern?** Signals only.
- Why: QP08 measures commodity carry with "the first future and the contract exactly expiring one year later" (QP08-C10-3) and takes the calendar out of equity carry (C10-2). Our rule uses neighbouring contracts (digest); in a seasonal market their slope is partly the expected seasonal price change (reader).
- Compute: per energy market, over all month-ends with a signal, the share of the carry signal's variance explained by its twelve calendar-month averages. Engine signal.
- Gate: 0.25 or more (a materiality line fixed here, not tuned) replaces that market's signal, in both versions, by the signal minus the average, over all earlier months of the same calendar month (at least five; no signal before), of the signal minus its trailing 12-month average. Registered with the A1 design changes before any run. Below: no change.

**X2. Is Value paid by prices coming back, or by income?** Design-era returns in two parts.
- Why: the thesis says cheap markets get dearer; if the pay is all income, the leg is carry (rows 13, 14).
- Compute: per Value leg (equities, bonds, currencies) and version, split each market's monthly excess return into income (one twelfth of: dividend yield minus 3-month rate; bond yield minus 3-month rate; rate gap to the dollar; at the prior month-end) and price change (the rest; for bonds it includes roll-down, which cannot be split off without a second maturity). Apply the leg's positions to each part and sum, before costs. Engine panel.
- Gate: a price part of zero or less enters the leg in the thesis register (1.5) as paid by income; its design-era return may then not be cited for the Value thesis in the spec, the batch review or the hold-out verdict. Positive: no entry. No position changes. The split by leg goes into the Value and Carry specs.

## 6. Numbers used

- **In the quote.** QP08: 0.42 and 0.96 (C17-1); 1.8 to 3.1 (C13-3); 51% (C18-5b); 25 years (C18-1); three years (C27-1); January 1990, April 2015 (C09-4); 1976 (C08-6). QP15: –0.60 (C17-1); –0.49 (C18-1); –0.28 (C22-4); –0.53 (C22-4b); 0.18 (C19-2); 0.83 (C10-1); –0.95 and 1.81 (C35-1); 24 basis points (C43-1); 1998 (C51-4); 5-year, 10-year (C09-5); 12 months (C09-1b); July 2011 (C07-2b); 1972 (C06-4); 2012 (C04-5); 1985 (C09-6); 1990 to 2008 (C02-7).
- **Summary only; named, nothing built on them.** QP08 value 0.75 cross-asset against 0.28 directional and carry 1.27 against 1.25 (QP08-C21-3). In QP15 every Sharpe ratio and t-statistic by class (QP15-C14-2 to C15-4) and the rival bond measures (C16-1). 2013 as QP15's year (digest).
- **Not from the papers.** Mine: 52 of 304 months; three quarters (1 minus 0.51 squared); the gate 0.25, five and 60 months. Years marked author's knowledge. Version counts, four energy futures, 1975, 1973 and 1979-12 are the digest's or the sheet's.

## 7. For the Opus check, and what is left open

Look first at:
1. Code facts I could not see: the inflation term and its release lag in Value's real yield; whether the currency measure is QP15's; whether energy carry is already calendar-adjusted; whether the inputs the sheet omits are in the engine.
2. The scope of –0.60 and –0.49 (claim text and exhibit field only) and the pairing of –0.28 with "–0.53" (QP15-C22-4b). QP08's map tags the trending-factor reason of row 1 as tested; the quotes assert it (QP08-C22-1).
3. Row 4 on our sign and rank versions, which are not proportional to the signal: check the half-hedge reading on positions.
4. Rule 5: date and asset classes of QP15's first circulated version; a dated carry source per class.
5. Hidden choices in the gates of X1 and X2.
6. Whether existing pods face the placebo (test 3); WORKFLOW does not say, and Carry's directional bond leg is the case in point. Closed at 3.4.

Left open by the papers: who pays Value and who pays bond carry; which carry reading holds in currencies and in commodities; whether anything survives costs; whether the gap between forms outlives 1990 to 2015; how cross-asset Value moves against directional Trend; why bonds fail.

## 8. Pack problems

1. QP15 against itself: "We find significant return" premia "in every asset class" (QP15-C01-1); bonds "do not produce statistically reliable premia" (C19-1b).
2. Label quotes. For QP15 Tables I and II and QP08 Tables 3, 5, 7, 9, 10 and 12 the quote is a title or row label, such as "Fixed income" (QP15-C15-1). Every figure by class is in summary fields.
3. QP08's carry sign. "the carry is positive (negative) if the interest rate is greater (smaller) than the dividend yield" (QP08-C04-1) against "The higher the dividend yield, the higher the carry" (C04-4). For commodities the summary formula of C10-3 and "higher carry" in C14-4 point one way, C05-7 (buy backwardation) the other. Our rule does not lean on the paper's convention.
4. QP08-C12-6: the quote is damaged ("take positions equivalent to N 1 ."); the sign rule of the directional book is summary only. With "We used dividend yield as value indicator" (C11-4) and C17-2b the rule as quoted is always long equities. The zero point is not in the pack.
5. QP15-C09-4: the quote defines currency value on "the 5-year return on the exchange rate"; the price-level adjustment is claim text only. The digest's engine rule is the adjusted one.
6. Pack against digest. Energy carry on the first two contracts against contracts a year apart (QP08-C10-3). Value's bond measure follows QP15's alternative (QP15-C16-2b), not its first choice (C09-5); its equity measure is QP08's (QP08-C11-4), not QP15's (QP15-C09-2).
7. Data sheet against papers: beyond the Data lines of section 3 (no index book value, no consensus forecasts), no curve depth for a one-year contract, no GDP growth for QP08's rates value (QP08-C12-1), swaps on LSEG only.
8. Dates and sealed years. Neither file has a date field (QP15: digest 2013, quotes cite 2012; QP08: sample end April 2015). QP08's summary fields carry chart reads of 2011 to 2015 (QP08-C15-4, C20-2, C24-2). Not used.

## 9. Self-check

- **Against the Carry thesis.** Three payers under one name; the common idea is mine and the bond payer is not in the pack. QP08's own model gives carry no pay without a second factor (row 12). The evidence is one sellers' paper, before costs, flattered by survivorship by its own account.
- **Against the Value thesis.** The authors say no theory fits (row 10). The chase is asserted, and the negative link to momentum that favours it is partly built into the measure (row 7). Value may be carry under another name in bonds and equities (X2), or nothing after income in currencies (row 14).
- **Against rejecting cross-sectional momentum.** QP15 documents it over decades with one fixed signal. The hedge for Value (–0.49) is shown for this form only, and a sign-based Trend may hold less of the relative part than I assume.
- **Against rejecting directional value.** Its poor result may belong to 1990 to 2015 alone. If class-wide factors turn, it pays when Trend loses; leaving it out keeps the book one-sided on asset-class direction.
- **Against keeping equities out of Carry and commodities out of Value.** The first rests on "similar in nature" at 51% (QP08-C18-5b), so most variation is not shared. For the second, both papers include commodities, and the mirror argument (row 14) holds for currencies too, which stay.
- **Against grading Value's pattern moderate.** Its by-class numbers are summary only and both groups sell it.
