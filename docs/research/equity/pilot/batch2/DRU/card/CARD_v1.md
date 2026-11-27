# Investor card: Stanley Druckenmiller (Duquesne Family Office)

Material bar: the input holds no word counts, so this card cannot say whether 3 or more documents have 5,000+ words.
5 documents were read (claims found up to transcript lines 285, 453, 464, 504 and 583). The THIN label is therefore NOT
set here; the caller applies A13 item 8 from the word counts.

Input: `claims_for_card.json`, 285 claims (66 verified rules: 61 both, 5 third), documents DRU1 2023-06-07,
DRU3 2023-05-10, DRU4 2024-11-06, DRU5 2020-01-06, DRU6 2018-11-13. Status after each id: (b) = both readers call it a
rule, (t) = split, third reader said rule, (n) = not a verified rule (support only).

## 1. What he buys and why

He calls himself a macro investor who works "from the bottom up", listening mainly to companies and to anecdotes
(DRU4-C001 b, DRU3-C006 b). He also watches financial conditions and liquidity (DRU4-C002 b, DRU6-C055 t), reads the inside
of the stock market as "the best economist" (DRU5-C002 b, DRU6-C008 b), and tries to see the situation 18 to 24 months
ahead rather than invest in the present (DRU4-C037 b, DRU5-C030 b). He trades five or six asset classes. When equities are
unclear he moves to bonds and currencies (DRU1-C032 b, DRU4-C056 b). When he expects a bad economic outcome his playbook is
to own Treasuries (DRU3-C039 b, DRU5-C013 b). In stocks he buys secular growers, "a 20 to 30 percent grower" in a slow-growth
period (DRU5-C015 b), and in tech he is "long the disruptors and short the disrupted" (DRU5-C025 b). He gets into a thesis no
later than "the second inning" (DRU6-C034 b) and buys as trends turn up (DRU5-C035 b). He sizes by conviction: he likes
concentrated bets, waits for "fat pitches" and then "swing[s] big" (DRU3-C029 b, DRU4-C060 t). The biggest bets go only into
very liquid markets, mostly bonds and currencies, never 30-40% of the fund in one equity (DRU6-C031 b, DRU6-C032 b, DRU6-C045 b).
He sells when the reason he bought is gone, whatever he paid (DRU4-C049 b, DRU4-C052 b), and otherwise holds for two to four
years and waits for technical tops (DRU4-C029 b, DRU4-C042 b).

## 2. Rules by part

Format: id | statement | measure (if computable) | number and direction as stated | strength | claim ids | dates said.
Computable = `computable_final` of the rule claim(s): yes / proxy / no.

### Buy

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rbuy1 | When he expects a bad economic outcome, own Treasuries ("The Playbook I've always used if I expected a bad economic outcome is to own treasuries"); in bear markets he "always made it in Treasuries" | no (his own recession forecast) | none stated | usually / always | DRU3-C039 (b), DRU5-C013 (b); support DRU5-C014 (n), DRU6-C042 (n), DRU6-C043 (n), DRU4-C080 (n) | 2023-05-10, 2020-01-06 (examples 2018-11-13, 2024-11-06) |
| Rbuy2 | Never invest in the present; buy on the situation he sees 18 to 24 months ahead | no | 18 to 24 months ahead | always | DRU4-C037 (b), DRU5-C030 (b); support DRU4-C038 (n), DRU4-C036 (n) | 2024-11-06, 2020-01-06 |
| Rbuy3 | In a period of slow, muted growth, buy secular growth stocks growing 20 to 30 percent ("almost better than a bond") | proxy: growth rate of a secular grower (which growth not specified) | 20 to 30 percent, between; condition "slow muted growth" | usually | DRU5-C015 (b); support DRU1-C013 (n), DRU5-C017 (n), DRU5-C018 (n), DRU5-C019 (n) | 2020-01-06 (support 2023-06-07) |
| Rbuy4 | In tech, long the disruptors and short the disrupted | proxy: disruptor vs disrupted classification | none stated | usually | DRU5-C025 (b); support DRU6-C007 (n) | 2020-01-06 (support 2018-11-13) |
| Rbuy5 | Buy into rising trends: "when the trends started to go up that's when I'm supposed to plow in" | proxy: price trend | none stated | usually | DRU5-C035 (b); support DRU5-C045 (n), DRU5-C053 (n) | 2020-01-06 |
| Rbuy6 | Enter a thesis early: not in the "zero inning", maybe not the first, "no later than the second inning" | no (stage of a thesis) | no later than the second inning (of nine) | usually | DRU6-C034 (b); support DRU5-C017 (n) | 2018-11-13 (support 2020-01-06) |
| Rbuy7 | Be willing to buy something back higher than he sold it | no | none stated | usually | DRU4-C046 (b) | 2024-11-06 |

### Price

none stated (no verified rule; see section 3).

### Avoid

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Ravoid1 | Do not own something only because it will fall less than a down market | no | none stated | usually | DRU5-C027 (b) | 2020-01-06 |
| Ravoid2 | No very large bet in an equity: an equity is an illiquid instrument and he never trusted his analysis enough for that (number in Rsize5) | no | see Rsize5 | always | DRU6-C033 (b), DRU6-C045 (b) | 2018-11-13 |

### Sell

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rsell1 | "if the reason I bought a stock is no longer the case I don't care what I paid for it": sell when the thesis is gone, cost basis irrelevant, including a loss the market found before him | no | none stated | always | DRU4-C049 (b), DRU4-C052 (b), DRU4-C050 (b) | 2024-11-06 |
| Rsell2 | After the first position and the work: sell if it was a mistake, add if it was not | no | none stated | usually | DRU4-C034 (b) | 2024-11-06 |
| Rsell3 | Do not sit in a position he is no longer sure about: "clean house" | no | none stated | usually | DRU4-C051 (b) | 2024-11-06 |
| Rsell4 | As a technician he usually waits for tops; a top is where the rate of rise changes and flattens "for quite some time" | proxy: price top pattern / rate of change of price | none stated | usually | DRU4-C042 (b); support DRU4-C043 (n), DRU4-C044 (n) | 2024-11-06 |

### Size

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rsize1 | Concentrate: "I like concentrated bets I like fat pitches and then the swing big"; with conviction "bet really big" | proxy in the claim: number of holdings (no number) | none stated | usually / always | DRU3-C029 (b), DRU4-C054 (b), DRU4-C060 (t); support DRU4-C068 (n), DRU4-C066 (n), DRU5-C051 (n), DRU6-C015 (n) | 2023-05-10, 2024-11-06 |
| Rsize2 | With no fat pitch, stand and let pitches go by; keep cash for high-conviction bets and preserve capital | no | none stated | usually | DRU3-C030 (b), DRU1-C035 (b); support DRU1-C031 (n), DRU1-C034 (n), DRU3-C035 (n), DRU3-C037 (n) | 2023-05-10, 2023-06-07 |
| Rsize3 | If concentrating, spread it over several asset buckets (equities, bonds, currencies, commodities), not one | no | "five buckets" / "five or six asset classes" | usually | DRU4-C055 (b), DRU1-C032 (b) | 2024-11-06, 2023-06-07 |
| Rsize4 | Big bets only in very liquid markets, better still ones that trade 24 hours; so most go into bonds and currencies | no | none stated (24-hour trading preferred) | always / usually | DRU6-C031 (b), DRU6-C032 (b); support DRU4-C058 (n), DRU6-C002 (n) | 2018-11-13 (support 2024-11-06) |
| Rsize5 | Never 30 or 40 percent of the fund in an equity | no (position size; computable from holdings) | 30 or 40 percent of the fund, below (stated as "never ... 30 or 40") | always | DRU6-C045 (b), DRU6-C033 (b) | 2018-11-13 |
| Rsize6 | Start with a meaningful but not "Earth shaking" position, normally about a third of the full position, then do the work | no | "a third of a position" (start) | usually | DRU4-C033 (b), DRU6-C038 (b); support DRU4-C062 (n) | 2024-11-06, 2018-11-13 |
| Rsize7 | Add when the thesis catches on and momentum or a technical signal turns his way ("then you really go for it"); sometimes size comes from fundamentals alone | no | none stated | usually; exception sometimes | DRU6-C014 (b), DRU6-C038 (b), DRU6-C044 (t); support DRU6-C039 (n), DRU6-C043 (n) | 2018-11-13 |
| Rsize8 | Do not pile on late, in the third to fifth inning | no | not after the second inning | usually | DRU6-C035 (b) | 2018-11-13 |
| Rsize9 | Track whether he is hot or cold; when cold or down, make small bets until the rhythm returns; exception: a once-in-a-lifetime opportunity | no | none stated | always (tracking) / usually; exception sometimes | DRU6-C048 (b), DRU6-C049 (b), DRU6-C050 (b), DRU6-C051 (b) | 2018-11-13 |
| Rsize10 | Get more cautious the minute risk/reward gets "a little dodgy" | no | none stated | usually | DRU6-C011 (b); support DRU5-C006 (n) | 2018-11-13 |
| Rsize11 | No big bet on a small move (example given: ten to 20 basis points) | no | example: 10 bp to 20 bp is too small | usually | DRU6-C057 (b); support DRU3-C032 (n), DRU5-C032 (n) | 2018-11-13 |

### Process

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rproc1 | Macro from the bottom up: listen mainly to companies; use anecdotal information a lot | no | none stated | usually | DRU4-C001 (b), DRU3-C006 (b); support DRU6-C041 (n) | 2024-11-06, 2023-05-10 |
| Rproc2 | Trucking as a leading indicator of the economy | no (series not named) | six to eight month lead time | usually | DRU3-C007 (b); support DRU5-C005 (n, credit leads the economy) | 2023-05-10 (support 2020-01-06) |
| Rproc3 | Watch financial conditions; "it's always about liquidity", not earnings or politics | no (claim tags central bank liquidity; no measure) | none stated | usually / always | DRU4-C002 (b), DRU6-C055 (t); support DRU3-C003 (n), DRU6-C006 (n) | 2024-11-06, 2018-11-13 |
| Rproc4 | Use the inside of the market (cyclicals vs defensives, relative strength of industry groups) to predict the economy | proxy: relative performance of cyclical vs defensive stocks; relative strength of industry groups | none stated | always / usually | DRU5-C002 (b), DRU6-C008 (b), DRU6-C012 (b); support DRU5-C001 (n), DRU4-C018 (n, computable yes), DRU5-C042 (n) | 2020-01-06, 2018-11-13 |
| Rproc5 | Markets are smarter than he is: if they disagree with his thesis, go back to the drawing board | no | none stated | always / usually | DRU5-C033 (b), DRU6-C009 (b); support DRU4-C009 (n), DRU4-C010 (n), DRU5-C008 (n) | 2020-01-06, 2018-11-13 |
| Rproc6 | Price action versus news: a big part of his process in 2018, "much diminished" by 2020, with more fundamentals planned (dated change, section 4) | proxy: price action versus news (price reaction to earnings) | none stated | usually -> sometimes | DRU6-C017 (b), DRU5-C041 (b), DRU5-C043 (b); support DRU5-C037 (n), DRU5-C039 (n), DRU5-C040 (n) | 2018-11-13, 2020-01-06 |
| Rproc7 | Take a theme and follow the dominoes ("concentric circles") it knocks over; once invested, dig deeper along the chain | no | none stated | usually | DRU4-C065 (b), DRU4-C025 (t) | 2024-11-06 |
| Rproc8 | Invest, then investigate: waiting two or three months to analyse a concept he likes may miss much of the move | no | "two or three months" is the delay he avoids | usually | DRU4-C032 (t); support DRU4-C030 (n), DRU4-C031 (n) | 2024-11-06 |
| Rproc9 | He likes to play the turn | no | none stated | usually | DRU4-C067 (b) | 2024-11-06 |
| Rproc10 | When equities are uncertain, use bonds and currencies; most of their action comes in bear markets, so "put the equities in the drawer" | no | none stated | usually | DRU1-C032 (b), DRU4-C056 (b); support DRU4-C057 (n) | 2023-06-07, 2024-11-06 |
| Rproc11 | Shorts: forecast the situation 12 to 18 months ahead and short what he expects to be priced lower | no | 12 to 18 months ahead | always / usually | DRU1-C015 (b), DRU1-C016 (b); support DRU1-C018 (n), DRU3-C038 (n) | 2023-06-07 |
| Rproc12 | Look for big trends held two to four years, not 20 | no (holding period; computable from 13F) | 2 to 4 years, between | usually | DRU4-C029 (b); support DRU1-C023 (n), DRU1-C024 (n) | 2024-11-06 (support 2023-06-07) |
| Rproc13 | As risk manager, keep a bad outcome in the "matrix" even when it is not his forecast | no | none stated | always | DRU3-C013 (b) | 2023-05-10 |
| Rproc14 | Daily routine: check all markets, the papers and overnight emails | no | none stated | usually | DRU4-C083 (b); support DRU4-C082 (n) | 2024-11-06 |
| Rproc15 | Use young analysts to stay on top of trends | no | none stated | usually | DRU4-C022 (b); support DRU4-C023 (n), DRU4-C039 (n) | 2024-11-06 |
| Rproc16 | Machines: know their effect and use them as signals (a very small amount placed with a couple of machines); trust instincts and technical analysis to pick up algo-driven moves | no | "very small amount" (no number) | usually / sometimes | DRU6-C019 (b), DRU6-C020 (b), DRU6-C010 (b); support DRU5-C054 (n), DRU6-C018 (n) | 2018-11-13 |
| Rproc17 | Do not talk publicly about single-stock shorts | no | none stated | usually | DRU5-C023 (b) | 2020-01-06 |

Count: buy 7, price 0, avoid 2, sell 4, size 11, process 17 (41 rules; all 66 verified claims are used).

## 3. None stated

- **Price**: none stated. No price claim is a verified rule. Multiples show up only as views or anecdotes: market at 20 times
  earnings (DRU3-C045 n), tech at 25 or 30 times (DRU4-C020 n), his growth names at 25-30x against cyclicals at 9x
  (DRU5-C016 n), cloud at 6-10 times sales (DRU6-C029 n, DRU5-C021 n), Google at 20 times, 15 after cash (DRU6-C025 n).
  He says "I'm not really a value investor" (DRU6-C030 n). What he does price is the asymmetry of the bet: the "fat pitch"
  (DRU3-C031 n, DRU3-C032 n, DRU5-C032 n), which supports Rsize1 and Rsize11 but gives no threshold. The recipe takes price
  from the 13F or a convention, tagged.
- Every other part has at least one verified rule. Within them, these items are none stated: number of holdings, stop-loss
  level, add size, and any leverage or quality screen (section 6).

## 4. Changes of view and scope

| # | claims | disagreement | reading |
|---|---|---|---|
| 1 | DRU6-C017 (b, 2018-11-13) vs DRU5-C041 (b), DRU5-C043 (b), DRU5-C040 (n) (2020-01-06) | price action versus news was "a big part" of his process in 2018; by 2020 it is "a much diminished part" and he will do more fundamentals | **dated change of view**: the 2020 statement wins (Rproc6) |
| 2 | DRU6-C012 (b) and DRU6-C013 (n) (2018: group relative strength "in the old days", failed in pharma 2018) vs DRU5-C002 (b, 2020: the inside of the market used "every cycle") and DRU5-C042 (n) | does the group or internal signal still work? | **different scope**: DRU5-C042 says the market's message over eight or nine months still holds, but over a week or two it is noise. Both stand: Rproc4 over months, not weeks |
| 3 | DRU1-C015 (b, 12 to 18 months for shorts) vs DRU4-C037 (b), DRU5-C030 (b) (18 to 24 months) | forecast horizon | **different scope** (shorts vs investing in general): both stand (Rproc11, Rbuy2) |
| 4 | DRU4-C060 (t), DRU3-C029 (b) bet very big vs DRU6-C033 (b), DRU6-C045 (b) no very large equity bet | how big | **different scope**: the very big bets go to liquid bond and currency markets (DRU6-C031 b, DRU6-C032 b). Both stand |
| 5 | DRU6-C038 (b), DRU6-C014 (b) start with a third and add on a technical or momentum signal vs DRU6-C044 (t), DRU6-C036 (n), DRU6-C043 (n) size from fundamentals alone, in big right away | when to size up | **different scope**: he calls the first "normally" / "a more normal pattern" (DRU6-C039 n), the second "sometimes". Both stand (Rsize7) |
| 6 | DRU4-C042 (b) waits for tops, DRU4-C029 (b) holds 2-4 years vs DRU4-C028 (n), DRU4-C041 (n), DRU4-C045 (n) Nvidia sold at 800-900 / above $2 trillion inside about a year; DRU4-C069 (n), DRU4-C070 (n) 2-year short closed at 150 bp | sold before the top | **not a rule conflict**: he calls these mistakes. The rules stand, and the examples fail them (section 5) |
| 7 | DRU4-C046 (b) willing to re-buy higher vs DRU4-C076 (n), DRU3-C022 (n) re-bought tech near the 2000 top, "a real emotional really dumb move" | re-buying higher | **different scope**: the rule is reasoned re-entry, the 2000 case he calls emotion. Both stand; no rule for telling them apart (gap) |
| 8 | DRU4-C067 (b, 2024) "play the turn" vs DRU6-C034 (b, 2018) not in the zero inning, DRU5-C035 (b, 2020) plow in when trends start to go up | entry at the turn or after the trend starts | **open**: the claims do not say whether "the turn" means the zero inning or the first or second inning, or whether his view changed |
| 9 | DRU6-C055 (t) "never been about earnings ... always about liquidity" vs DRU5-C015 (b) 20-30% growers, DRU1-C013 (n) sustainable earnings hold up in recessions | earnings matter or not | **open**, likely different scope (macro driver vs stock choice), but "everything for me" is stated without limits |
| 10 | DRU3-C030 (b) let pitches go by vs DRU4-C032 (t) do not wait two or three months to analyse | patience | **different scope**: waiting for a fat pitch vs acting fast once he likes a concept. Both stand |
| 11 | DRU3-C039 (b) bad outcome -> own Treasuries vs DRU3-C040 (n) in May 2023 Treasuries were "not exactly a fat pitch"; DRU4-C015 (n) short bonds in 2024 | Treasuries in a feared hard landing | **different scope**: the playbook is subject to the fat-pitch test (Rsize1, Rsize11). Both stand |
| 12 | DRU5-C033 (b) markets are smarter than he is vs DRU5-C047 (n) be "a bit of a contrarian", DRU5-C052 (n) good buys at lows feel terrible | follow or fade the market | **open** (support claims only; no rule conflict) |
| 13 | DRU6-C010 (b, 2018) trust instincts and technical analysis vs DRU5-C043 (b, 2020) more fundamentals | which tool | **dated change** in emphasis (2020 later), part of item 1 |

## 5. Examples

Companies:

| claim | company | fits / fails | rule |
|---|---|---|---|
| DRU1-C012 (n), DRU1-C022 (n), DRU3-C024 (n), DRU3-C025 (n) | Nvidia | fits: AI held as a secular grower through a feared recession | Rbuy3, Rbuy2 |
| DRU1-C024 (n) | Nvidia | fits: to own "at least two or three years" | Rproc12 |
| DRU4-C024 (n) | Nvidia | bought a "good chunk" a month before ChatGPT; he calls it luck | Rproc7, Rproc8 |
| DRU4-C028 (n), DRU4-C041 (n), DRU4-C045 (n) | Nvidia | fails: sold at 800-900, above $2tn market value, well inside the planned years; no second chance | Rsell4, Rproc12 |
| DRU3-C024 (n) | Microsoft | fits: held as AI exposure | Rbuy3 |
| DRU6-C025 (n), DRU6-C026 (n), DRU6-C027 (n) | Google | fits: disruptor and AI leader at 20x earnings; he holds | Rbuy4 |
| DRU6-C026 (n) | Campbell's Soup | disrupted, at the same 20x multiple | Rbuy4 (short side) |
| DRU6-C007 (n) | retail, staples (no company named) | short the disrupted | Rbuy4 |
| DRU5-C017 (n), DRU5-C018 (n), DRU5-C022 (n), DRU6-C029 (n) | cloud companies (none named) | fits: "second inning of a nine inning game", long-duration growth | Rbuy3, Rbuy6 |
| DRU6-C030 (n) | Apple | missed ("not really a value investor") | none (price: none stated) |
| DRU5-C038 (n) | Facebook | fails: fell after great earnings, then rose to 220, so the signal failed | Rproc6 |
| DRU6-C013 (n) | pharmaceuticals (group) | fails: the worst group with no news, then reversed | Rproc4 (group signal), Rproc6 |
| DRU5-C001 (n) | auto, building, bank stocks (groups) | fits: down 25-35% while the index fell 10-13% | Rproc4 |
| DRU5-C026 (n) | financials (short) | the group needs rising rates | no verified rule (view) |
| DRU1-C019 (n), DRU1-C020 (n), DRU4-C073 (n) | 11-12 internet "also-rans" (1999 short) | fails: shorted into a bubble, lost 3x | no verified rule (avoid gap) |
| DRU4-C075 (n), DRU4-C076 (n), DRU3-C022 (n) | tech holdings (2000) | fails: re-bought near the top out of emotion | Rbuy7 (scope, section 4 item 7) |
| DRU1-C004 (n) | Silicon Valley Bank, Bed Bath & Beyond | "tip of the iceberg" (view) | none |

Macro instruments (not companies; they show the size and asymmetry rules):

| claim | instrument | rule |
|---|---|---|
| DRU3-C031 (n), DRU3-C032 (n) | US 2-year at 15 bp, money growth 40% (2021): a fat pitch | Rsize1, Rsize11 |
| DRU4-C069 (n), DRU4-C070 (n) | the same 2-year short, closed at 150 bp, too early | fails Rsell4 |
| DRU4-C061 (n) to DRU4-C064 (n), DRU5-C032 (n) | pound vs Deutsche mark 1992: started at 20-25% of the fund, went to 100%; a one-way bet | Rsize1, Rsize4, Rsize6, Rproc8 |
| DRU6-C036 (n), DRU6-C037 (n) | Deutsche mark 1990: in big at once on conviction | Rsize7 exception |
| DRU6-C039 (n) | euro short 2014: added after the break through 135 | Rsize7 |
| DRU6-C042 (n), DRU6-C043 (n), DRU4-C080 (n) | US Treasuries 2000: kept adding as the evidence built | Rbuy1, Rsize7 exception |
| DRU5-C014 (n) | long US 2, 5, 10-year (2018-19) on risk/reward | Rbuy1 |
| DRU6-C023 (n), DRU6-C024 (n) | Brazil, South Africa currency "lottery ticket": risk about the carry | Rsize11 (asymmetry) |
| DRU4-C025 (t) | power and uranium as dominoes of the AI theme | Rproc7 |
| DRU3-C014 (n), DRU3-C017 (n) | copper: tight, but no meaningful position before a hard landing | Rsize10 |

## 6. Gaps (what a screen needs that he does not state)

- **Price**: no valuation rule or threshold of any kind (section 3).
- **Growth (Rbuy3)**: which growth (sales, earnings, cash flow), over what period, how "sustainable" is judged (DRU1-C013 n),
  and what counts as a "slow muted growth" period.
- **Disruptor / disrupted (Rbuy4)**: no definition or measure; the claims give tech only (DRU5-C025 b) and cloud vs
  retail/staples (DRU6-C007 n).
- **Trend and stage (Rbuy5, Rbuy6, Rsize7, Rsize8)**: no lookback, no definition of a trend start, of a "technical signal",
  or of innings.
- **Top (Rsell4)**: "flattens out for quite some time" (DRU4-C043 n) has no window or rate threshold.
- **Size**: no number of holdings, no maximum weight below the "30 or 40 percent" he never reached (Rsize5), no full-position
  size, no add size after the first third, no stop-loss level (Rsell1 is thesis-based).
- **Indicators (Rproc2-Rproc4)**: which trucking series, which financial-conditions or liquidity measure, how cyclicals and
  defensives are defined, which group relative-strength window; the narrowing-leadership signal (DRU4-C018 n) has no
  breadth measure or threshold.
- **Hot / cold (Rsize9)**: no definition (drawdown size, time) and no size for "little bets".
- **Avoid**: no leverage, quality or liquidity floor for stocks; the 1999 lesson against shorting bubbles early is
  anecdote only (DRU1-C019 n, DRU1-C020 n, DRU4-C073 n).
- **Scope of a stock screen**: most verified rules concern macro calls and bonds, currencies and commodities (Rbuy1,
  Rsize3, Rsize4, Rproc10). He made about 70% of his money in currencies and bonds (DRU6-C002 n). A US 13F shows only the
  equity longs: shorts, bonds, currencies and the "five buckets" mix are not visible, so a recipe built from it covers
  only part of what he does.
