# Investor card: Stanley Druckenmiller (Duquesne Family Office)

v1.1 = v1 + DRU2 merged after a FAILED held-out test (A13 item 8)

Material bar: the input holds no word counts, so this card cannot say whether 3 or more documents have 5,000+ words.
6 documents were read (claims found up to transcript lines 285, 453, 464, 504, 583 and, for DRU2, 641). The THIN label
is therefore NOT set here; the caller applies A13 item 8 from the word counts.

Input: v1 = `claims_for_card.json`, 285 claims (66 verified rules: 61 both, 5 third), documents DRU1 2023-06-07,
DRU3 2023-05-10, DRU4 2024-11-06, DRU5 2020-01-06, DRU6 2018-11-13. v1.1 adds `claims_DRU2.json`, DRU2 2022-06-10,
90 claims (26 verified rules: 25 both, 1 third), and the held-out result `heldout_result.json` (17 of 26 DRU2 rules
matched v1; 3 open buy contradictions). Status after each id: (b) = both readers call it a rule, (t) = split, third
reader said rule, (n) = not a verified rule (support only). Rows or cells changed in v1.1 are marked [v1.1].

## 1. What he buys and why

He calls himself a macro investor who works "from the bottom up", listening mainly to companies and to anecdotes
(DRU4-C001 b, DRU3-C006 b), and does not use the employment and top-down statistics economists use (DRU2-C007 b,
DRU2-C010 b). He also watches financial conditions and liquidity (DRU4-C002 b, DRU6-C055 t), reads the inside
of the stock market as "the best economist" (DRU5-C002 b, DRU6-C008 b), in particular whether leading industries such as
the home builders turn up or down (DRU2-C011 b, DRU2-C014 b, DRU2-C015 b), and tries to see the situation 12 to 24 months
ahead rather than invest in the present (DRU4-C037 b, DRU5-C030 b, DRU2-C036 b). For a company his long-term bias is one
whose business will be "much much better" 3 to 5 years out (DRU2-C074 b). He trades five or six asset classes. When equities are
unclear he moves to bonds and currencies (DRU1-C032 b, DRU4-C056 b). When he expects a bad economic outcome his playbook is
to own Treasuries (DRU3-C039 b, DRU5-C013 b, DRU2-C022 b), though in 2022 he was short fixed income while expecting a 2023
recession (DRU2-C024 n, DRU2-C006 n; section 4 item 15). In stocks he has a bias toward growth (DRU2-C073 b) and buys secular
growers, "a 20 to 30 percent grower" in a slow-growth period (DRU5-C015 b); in tech he is "long the disruptors and short the
disrupted" (DRU5-C025 b). He also does "a lot of countercyclical stuff": buying cyclical industries while they lose money,
because capacity shuts over the next 2 or 3 years (DRU2-C075 b, DRU2-C076 b). He gets into a thesis no
later than "the second inning" (DRU6-C034 b) and buys as trends turn up (DRU5-C035 b). He sizes by conviction: he likes
concentrated bets, waits for "fat pitches" and then "swing[s] big" (DRU3-C029 b, DRU4-C060 t, DRU2-C026 b), with 15-20% of
the asset base in a position or 200-300% in macro positions (DRU2-C039 b), and turns the dial up when he is hot and down when
he is cold (DRU2-C043 b, DRU2-C044 b, DRU2-C045 b). The biggest bets go only into
very liquid markets, mostly bonds and currencies, never 30-40% of the fund in one equity (DRU6-C031 b, DRU6-C032 b, DRU6-C045 b).
He buys on intuition and investigates afterwards (DRU2-C054 b, DRU2-C052 b). He sells when the reason he bought is gone,
whatever he paid (DRU4-C049 b, DRU4-C052 b), not because a trade is crowded (DRU2-C082 b), and otherwise holds for two to four
years and waits for technical tops (DRU4-C029 b, DRU4-C042 b).

## 2. Rules by part

Format: id | statement | measure (if computable) | number and direction as stated | strength | claim ids | dates said.
Computable = `computable_final` of the rule claim(s): yes / proxy / no.

### Buy

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rbuy1 [v1.1] | When he expects a bad economic outcome, own Treasuries ("The Playbook I've always used if I expected a bad economic outcome is to own treasuries"); in bear markets he "always made it in Treasuries"; in past bear markets "ignore equities, take them off the table, buy bonds, buy treasuries and go home". Not applied in late 2021 - mid 2022 (short fixed income, DRU2-C024 n); no stated condition for that (section 4 item 15, open) | no (his own recession forecast) | none stated | usually / always | DRU3-C039 (b), DRU5-C013 (b), DRU2-C022 (b, scope: past bear markets); support DRU5-C014 (n), DRU6-C042 (n), DRU6-C043 (n), DRU4-C080 (n), DRU2-C020 (n), DRU2-C064 (n) | 2023-05-10, 2020-01-06, 2022-06-10 (examples 2018-11-13, 2024-11-06) |
| Rbuy2 [v1.1] | Never invest in the present; buy on the situation he sees 12 to 24 months ahead, and on how security prices would reflect it ("Do not invest in the present ... Change moves them") | no | 18 to 24 months ahead (2020, 2024; DRU2-C070 n 2022); 12 to 18 months ahead (DRU2-C036, 2022, general) | always / usually | DRU4-C037 (b), DRU5-C030 (b), DRU2-C036 (b); support DRU4-C038 (n), DRU4-C036 (n), DRU2-C070 (n), DRU2-C071 (n) | 2024-11-06, 2020-01-06, 2022-06-10 |
| Rbuy3 [v1.1] | Bias toward growth stocks, set aside "the last year or two" (to mid 2022); in a period of slow, muted growth, buy secular growth stocks growing 20 to 30 percent ("almost better than a bond") | proxy: growth rate of a secular grower (which growth not specified) | 20 to 30 percent, between; condition "slow muted growth" (the number is DRU5-C015 only) | usually | DRU5-C015 (b), DRU2-C073 (b); support DRU1-C013 (n), DRU5-C017 (n), DRU5-C018 (n), DRU5-C019 (n), DRU2-C077 (n) | 2020-01-06, 2022-06-10 (support 2023-06-07) |
| Rbuy4 | In tech, long the disruptors and short the disrupted | proxy: disruptor vs disrupted classification | none stated | usually | DRU5-C025 (b); support DRU6-C007 (n) | 2020-01-06 (support 2018-11-13) |
| Rbuy5 | Buy into rising trends: "when the trends started to go up that's when I'm supposed to plow in" | proxy: price trend | none stated | usually | DRU5-C035 (b); support DRU5-C045 (n), DRU5-C053 (n) | 2020-01-06 |
| Rbuy6 | Enter a thesis early: not in the "zero inning", maybe not the first, "no later than the second inning" | no (stage of a thesis) | no later than the second inning (of nine) | usually | DRU6-C034 (b); support DRU5-C017 (n) | 2018-11-13 (support 2020-01-06) |
| Rbuy7 | Be willing to buy something back higher than he sold it | no | none stated | usually | DRU4-C046 (b) | 2024-11-06 |
| Rbuy8 [v1.1 new] | Countercyclical: buy cyclical industries while they are losing money, because capacity shuts over the next 2 or 3 years while demand stays ("people were still going to need chemicals"); "I do a lot of countercyclical stuff"; the lessons "still work" after 30 or 40 years. Margins of loss-makers "look better in 3 years", over-earners' come down | proxy: earnings turn from loss (DRU2-C075); support: operating margin versus own history (DRU2-C069 n) | buy while the industry loses money; capacity shuts over 2 to 3 years; margins revert in about 3 years (DRU2-C069 n) | usually | DRU2-C075 (b, scope: sector, example chemicals), DRU2-C076 (b); support DRU2-C069 (n) | 2022-06-10 |
| Rbuy9 [v1.1 new] | Long-term bias: a company he can envision being in a "much much better situation" 3 to 5 years from now | proxy: expected improvement in business in 3 to 5 years | 3 to 5 years ahead | usually | DRU2-C074 (b); support DRU2-C051 (n) | 2022-06-10 |
| Rbuy10 [v1.1 new] | An analyst idea that appeals to him intuitively and fits the "macro matrix" (ticks a bunch of boxes) can get a quick, very large position, then homework (Rproc8) and add or drop (Rsell2); more likely when he already holds the macro view (copper example) | no | none stated ("very large position") | sometimes | DRU2-C050 (b), DRU2-C052 (b); support DRU2-C051 (n), DRU2-C085 (n) | 2022-06-10 |
| Rbuy11 [v1.1 new] | If he expects irresponsible monetary policy and inflation: own Bitcoin when it is a bull phase, gold when it is a bear phase for other assets | no | none stated | sometimes | DRU2-C034 (t) | 2022-06-10 |

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
| Rsell2 [v1.1] | After the first position and the work: sell if it was a mistake, add if it was not ("If the story panned out, add to it. If it didn't pan out, just get rid of it") | no | homework period after buying: two or three weeks (DRU2-C052) | usually | DRU4-C034 (b), DRU2-C052 (b), DRU2-C054 (b); support DRU2-C086 (n) | 2024-11-06, 2022-06-10 |
| Rsell3 | Do not sit in a position he is no longer sure about: "clean house" | no | none stated | usually | DRU4-C051 (b); support DRU2-C038 (n, stale longs or shorts) | 2024-11-06 |
| Rsell4 | As a technician he usually waits for tops; a top is where the rate of rise changes and flattens "for quite some time" | proxy: price top pattern / rate of change of price | none stated | usually | DRU4-C042 (b); support DRU4-C043 (n), DRU4-C044 (n) | 2024-11-06 |
| Rsell5 [v1.1 new] | Do not sell only because a trade has become widely recognised or crowded ("I don't just sell something because people talk about pain trade") | no | none stated | usually | DRU2-C082 (b) | 2022-06-10 |

### Size

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rsize1 [v1.1] | Concentrate: "I like concentrated bets I like fat pitches and then the swing big"; with conviction "bet really big"; diversification does not lower risk; sizing is "70 to 80% of the equation". 2022: "not playing anything as aggressively as I used to" (DRU2-C033 n) | proxy in the claim: number of holdings (no number); DRU2-C039: position size | 15 to 20% of the asset base in a position; "sometimes in macro positions" 200 to 300%, between (DRU2-C039) | usually / always; number sometimes | DRU3-C029 (b), DRU4-C054 (b), DRU4-C060 (t), DRU2-C039 (b); support DRU4-C068 (n), DRU4-C066 (n), DRU5-C051 (n), DRU6-C015 (n), DRU2-C037 (n), DRU2-C041 (n), DRU2-C042 (n), DRU2-C033 (n) | 2023-05-10, 2024-11-06, 2022-06-10 |
| Rsize2 [v1.1] | With no fat pitch, stand and let pitches go by ("I'm waiting for a fat pitch. I'm not shooting at any pins"); keep cash for high-conviction bets and preserve capital | no | none stated | usually; sometimes (DRU2-C026) | DRU3-C030 (b), DRU1-C035 (b), DRU2-C026 (b); support DRU1-C031 (n), DRU1-C034 (n), DRU3-C035 (n), DRU3-C037 (n) | 2023-05-10, 2023-06-07, 2022-06-10 |
| Rsize3 | If concentrating, spread it over several asset buckets (equities, bonds, currencies, commodities), not one | no | "five buckets" / "five or six asset classes" | usually | DRU4-C055 (b), DRU1-C032 (b); support DRU2-C068 (n) | 2024-11-06, 2023-06-07 |
| Rsize4 | Big bets only in very liquid markets, better still ones that trade 24 hours; so most go into bonds and currencies | no | none stated (24-hour trading preferred); example 350% 10-year equivalent in Treasuries, Q4 2000 (DRU2-C064 n) | always / usually | DRU6-C031 (b), DRU6-C032 (b); support DRU4-C058 (n), DRU6-C002 (n), DRU2-C064 (n) | 2018-11-13 (support 2024-11-06, 2022-06-10) |
| Rsize5 | Never 30 or 40 percent of the fund in an equity | no (position size; computable from holdings) | 30 or 40 percent of the fund, below (stated as "never ... 30 or 40"); consistent with 15-20% in Rsize1 | always | DRU6-C045 (b), DRU6-C033 (b) | 2018-11-13 |
| Rsize6 | Start with a meaningful but not "Earth shaking" position, normally about a third of the full position, then do the work. Exception: Rbuy10 (very large at once when an idea fits his macro view; section 4 item 5) | no | "a third of a position" (start) | usually | DRU4-C033 (b), DRU6-C038 (b); support DRU4-C062 (n) | 2024-11-06, 2018-11-13 |
| Rsize7 | Add when the thesis catches on and momentum or a technical signal turns his way ("then you really go for it"); sometimes size comes from fundamentals alone | no | none stated | usually; exception sometimes | DRU6-C014 (b), DRU6-C038 (b), DRU6-C044 (t); support DRU6-C039 (n), DRU6-C043 (n) | 2018-11-13 |
| Rsize8 | Do not pile on late, in the third to fifth inning | no | not after the second inning | usually | DRU6-C035 (b) | 2018-11-13 |
| Rsize9 [v1.1] | Track whether he is hot or cold ("One of my number one jobs"); when hot, "turn the dial way up"; when cold or down, tone down, make small bets and do not trade a lot until the rhythm returns; to concentrate he needs both an exciting investment and a good trading rhythm; exception: a once-in-a-lifetime opportunity | no | none stated | always (tracking) / usually; exception sometimes | DRU6-C048 (b), DRU6-C049 (b), DRU6-C050 (b), DRU6-C051 (b), DRU2-C043 (b), DRU2-C044 (b), DRU2-C045 (b), DRU2-C046 (b), DRU2-C063 (b); support DRU2-C061 (n), DRU2-C065 (n) | 2018-11-13, 2022-06-10 |
| Rsize10 | Get more cautious the minute risk/reward gets "a little dodgy" | no | none stated | usually | DRU6-C011 (b); support DRU5-C006 (n) | 2018-11-13 |
| Rsize11 | No big bet on a small move (example given: ten to 20 basis points) | no | example: 10 bp to 20 bp is too small | usually | DRU6-C057 (b); support DRU3-C032 (n), DRU5-C032 (n) | 2018-11-13 |
| Rsize12 [v1.1 new] | Analysts go on streaks too; as "trigger puller" his job is to size up an analyst who is hot in an area (technical analysts who run cold can even be faded) | no | none stated | usually | DRU2-C048 (b); support DRU2-C047 (n) | 2022-06-10 |

### Process

| id | statement | measure | number / direction | strength | claims | dates |
|---|---|---|---|---|---|---|
| Rproc1 [v1.1] | Macro from the bottom up: listen mainly to companies, especially those that lead the economy; use anecdotal information a lot; do not use employment and other top-down statistics | no | none stated | usually / always | DRU4-C001 (b), DRU3-C006 (b), DRU2-C007 (b), DRU2-C010 (b); support DRU6-C041 (n) | 2024-11-06, 2023-05-10, 2022-06-10 |
| Rproc2 | Trucking as a leading indicator of the economy | no (series not named in the rule; 2022 view names trucking stocks, DRU2-C016 n) | six to eight month lead time; support: 6 to 12 months (DRU2-C009 n), 6 months to a year (DRU2-C017 n) | usually | DRU3-C007 (b); support DRU5-C005 (n, credit leads the economy), DRU2-C016 (n), DRU2-C009 (n), DRU2-C017 (n) | 2023-05-10 (support 2020-01-06, 2022-06-10) |
| Rproc3 | Watch financial conditions; "it's always about liquidity", not earnings or politics | no (claim tags central bank liquidity; no measure) | none stated | usually / always | DRU4-C002 (b), DRU6-C055 (t); support DRU3-C003 (n), DRU6-C006 (n) | 2024-11-06, 2018-11-13 |
| Rproc4 [v1.1] | Use the inside of the market (cyclicals vs defensives, relative strength of industry groups, which industries lead and which lag) to predict the economy; "if the leading industries are turning up or turning down, that's a signal"; "you can just do the home builders themselves" | proxy: relative performance of cyclical vs defensive stocks; relative strength of industry groups; stock price trend of leading industries (DRU2-C011); home builder stock prices (DRU2-C015) | none stated; leading industries named in the note: housing, trucking, retail (DRU2-C011) | always / usually; home builders sometimes | DRU5-C002 (b), DRU6-C008 (b), DRU6-C012 (b), DRU2-C011 (b), DRU2-C014 (b), DRU2-C015 (b); support DRU5-C001 (n), DRU4-C018 (n, computable yes), DRU5-C042 (n), DRU2-C008 (n), DRU2-C009 (n); second signal the bond market (DRU2-C012 n), muted by central banks 2011-2022 (DRU2-C013 n) | 2020-01-06, 2018-11-13, 2022-06-10 |
| Rproc5 | Markets are smarter than he is: if they disagree with his thesis, go back to the drawing board | no | none stated | always / usually | DRU5-C033 (b), DRU6-C009 (b); support DRU4-C009 (n), DRU4-C010 (n), DRU5-C008 (n) | 2020-01-06, 2018-11-13 |
| Rproc6 [v1.1] | Price action versus news: a big part of his process in 2018, "much diminished" by 2020, with more fundamentals planned; 2022: "a very weakened tool versus 20 years ago" (dated change, section 4) | proxy: price action versus news (price reaction to earnings) | none stated | usually -> sometimes | DRU6-C017 (b), DRU5-C041 (b), DRU5-C043 (b); support DRU5-C037 (n), DRU5-C039 (n), DRU5-C040 (n), DRU2-C018 (n), DRU2-C019 (n) | 2018-11-13, 2020-01-06 (support 2022-06-10) |
| Rproc7 | Take a theme and follow the dominoes ("concentric circles") it knocks over; once invested, dig deeper along the chain | no | none stated | usually | DRU4-C065 (b), DRU4-C025 (t) | 2024-11-06 |
| Rproc8 [v1.1] | Invest, then investigate: "if you have the intuition, you buy it and then you do the analysis and then get rid of it if it doesn't pan out as opposed to wait and do the analysis"; waiting may miss much of the move | no | delay he avoids: "two or three months" (DRU4-C032 t, 2024) vs "two or three weeks ... 60 or 70% of the move" (DRU2-C049 n, 2022); OPEN, section 4 item 17. Homework after buying: two or three weeks (DRU2-C052 b) | usually | DRU2-C054 (b), DRU2-C052 (b), DRU4-C032 (t); support DRU4-C030 (n), DRU4-C031 (n), DRU2-C049 (n), DRU2-C053 (n), DRU2-C055 (n), DRU2-C056 (n) | 2024-11-06, 2022-06-10 |
| Rproc9 | He likes to play the turn | no | none stated | usually | DRU4-C067 (b) | 2024-11-06 |
| Rproc10 [v1.1] | When equities are uncertain, use bonds and currencies; most of their action comes in bear markets, so "put the equities in the drawer" | no | none stated | usually | DRU1-C032 (b), DRU4-C056 (b), DRU2-C022 (b); support DRU4-C057 (n), DRU2-C020 (n), DRU2-C021 (n), DRU2-C087 (n) | 2023-06-07, 2024-11-06, 2022-06-10 |
| Rproc11 [v1.1] | Shorts: forecast the situation 12 to 18 months ahead and short what he expects to be priced lower (the 12-18 horizon is also stated in general, DRU2-C036; section 4 item 3). Support, not a rule: in a post-bubble bear market a 15-20% index rally is a shot at going short again (DRU2-C066 n) | no | 12 to 18 months ahead | always / usually | DRU1-C015 (b), DRU1-C016 (b); support DRU1-C018 (n), DRU3-C038 (n), DRU2-C066 (n), DRU2-C027 (n), DRU2-C025 (n) | 2023-06-07 (support 2022-06-10) |
| Rproc12 | Look for big trends held two to four years, not 20 | no (holding period; computable from 13F) | 2 to 4 years, between | usually | DRU4-C029 (b); support DRU1-C023 (n), DRU1-C024 (n) | 2024-11-06 (support 2023-06-07) |
| Rproc13 | As risk manager, keep a bad outcome in the "matrix" even when it is not his forecast | no | none stated | always | DRU3-C013 (b); support DRU2-C002 (n) | 2023-05-10 |
| Rproc14 | Daily routine: check all markets, the papers and overnight emails | no | none stated | usually | DRU4-C083 (b); support DRU4-C082 (n) | 2024-11-06 |
| Rproc15 | Use young analysts to stay on top of trends | no | none stated | usually | DRU4-C022 (b); support DRU4-C023 (n), DRU4-C039 (n), DRU2-C059 (n) | 2024-11-06 (support 2022-06-10) |
| Rproc16 | Machines: know their effect and use them as signals (a very small amount placed with a couple of machines); trust instincts and technical analysis to pick up algo-driven moves | no | "very small amount" (no number) | usually / sometimes | DRU6-C019 (b), DRU6-C020 (b), DRU6-C010 (b); support DRU5-C054 (n), DRU6-C018 (n) | 2018-11-13 |
| Rproc17 | Do not talk publicly about single-stock shorts | no | none stated | usually | DRU5-C023 (b) | 2020-01-06 |
| Rproc18 [v1.1 new] | Ruthless discipline: come in every day "could not be more paranoid" and constantly re-evaluate (stale longs and stale shorts are where most people get in trouble; do not be a slave to past models) | no | every day (stated) | usually | DRU2-C040 (b); support DRU2-C038 (n), DRU2-C023 (n) | 2022-06-10 |
| Rproc19 [v1.1 new] | Know and manage his own bearish bias ("I have a bearish bias, I know it. One of my jobs is to manage myself") | no | none stated | sometimes | DRU2-C088 (b); support DRU2-C035 (n), DRU2-C089 (n), DRU2-C090 (n) | 2022-06-10 |

Count: buy 11, price 0, avoid 2, sell 5, size 12, process 19 (49 rules; v1 41 + 8 new). All 66 v1 verified claims and all
26 DRU2 verified claims are used (DRU2: C007, C010 Rproc1; C011, C014, C015 Rproc4; C022 Rbuy1, Rproc10; C026 Rsize2;
C034 Rbuy11; C036 Rbuy2; C039 Rsize1; C040 Rproc18; C043-C046, C063 Rsize9; C048 Rsize12; C050 Rbuy10; C052 Rproc8,
Rsell2, Rbuy10; C054 Rproc8, Rsell2; C073 Rbuy3; C074 Rbuy9; C075, C076 Rbuy8; C082 Rsell5; C088 Rproc19).

## 3. None stated

- **Price**: none stated. No price claim is a verified rule, in v1 or in DRU2. Multiples show up only as views or anecdotes: market at 20 times
  earnings (DRU3-C045 n), tech at 25 or 30 times (DRU4-C020 n), his growth names at 25-30x against cyclicals at 9x
  (DRU5-C016 n), cloud at 6-10 times sales (DRU6-C029 n, DRU5-C021 n), Google at 20 times, 15 after cash (DRU6-C025 n).
  [v1.1] DRU2 adds only views: very good companies de-rated 60-70% in 2022 without much change in fundamentals (DRU2-C001 n),
  energy companies "still cheap relative to what we see a year or two out" (DRU2-C083 n), big tech "too cheap for me" to
  short in 2022 (DRU2-C078 n). DRU2-C083 measures cheapness against the outlook 1 to 2 years out, consistent with Rbuy2,
  but it is a view.
  He says "I'm not really a value investor" (DRU6-C030 n). What he does price is the asymmetry of the bet: the "fat pitch"
  (DRU3-C031 n, DRU3-C032 n, DRU5-C032 n), which supports Rsize1 and Rsize11 but gives no threshold; sizing as "how much you
  make when you're right and how much you lose when you're wrong" (DRU2-C042 n) is the same idea. The recipe takes price
  from the 13F or a convention, tagged.
- Every other part has at least one verified rule. Within them, these items are none stated: number of holdings, stop-loss
  level, add size, and any leverage or quality screen (section 6). [v1.1] A position size is now stated (Rsize1, DRU2-C039).

## 4. Changes of view and scope

| # | claims | disagreement | reading |
|---|---|---|---|
| 1 [v1.1] | DRU6-C017 (b, 2018-11-13) vs DRU5-C041 (b), DRU5-C043 (b), DRU5-C040 (n) (2020-01-06); DRU2-C019 (n), DRU2-C018 (n) (2022-06-10) | price action versus news was "a big part" of his process in 2018; by 2020 it is "a much diminished part" and he will do more fundamentals; 2022: "a very weakened tool versus 20 years ago" | **dated change of view**: the 2020 statement wins (Rproc6); DRU2 (2022) agrees with it |
| 2 | DRU6-C012 (b) and DRU6-C013 (n) (2018: group relative strength "in the old days", failed in pharma 2018) vs DRU5-C002 (b, 2020: the inside of the market used "every cycle") and DRU5-C042 (n) | does the group or internal signal still work? | **different scope**: DRU5-C042 says the market's message over eight or nine months still holds, but over a week or two it is noise. Both stand: Rproc4 over months, not weeks. [v1.1] DRU2-C011 (b), DRU2-C014 (b) (2022) restate the leading-industry signal as working "over time"; DRU2-C017 (n) "longer lead times, like 6 months to a year" fits the months reading |
| 3 [v1.1] | DRU1-C015 (b, 12 to 18 months for shorts) vs DRU4-C037 (b), DRU5-C030 (b) (18 to 24 months); DRU2-C036 (b, 2022, scope all: 12 to 18 months) and DRU2-C070 (n, same document: 18 or 24 months) | forecast horizon | **v1 reading withdrawn** (it was "different scope, shorts vs investing"): DRU2-C036 gives 12-18 months as his general horizon and DRU2-C070 gives 18-24 in the same interview, so the claims do not support a scope split or a dated change. Read as one range, 12 to 24 months (Rbuy2); Rproc11 keeps 12-18 for shorts as stated |
| 4 [v1.1] | DRU4-C060 (t), DRU3-C029 (b) bet very big vs DRU6-C033 (b), DRU6-C045 (b) no very large equity bet | how big | **different scope**: the very big bets go to liquid bond and currency markets (DRU6-C031 b, DRU6-C032 b). Both stand. DRU2-C039 (b) fits: 15-20% of the asset base, but 200-300% "in macro positions" (example DRU2-C064 n, 350% in Treasuries) |
| 5 [v1.1] | DRU6-C038 (b), DRU6-C014 (b) start with a third and add on a technical or momentum signal vs DRU6-C044 (t), DRU6-C036 (n), DRU6-C043 (n) size from fundamentals alone, in big right away; DRU2-C050 (b), DRU2-C052 (b), DRU2-C051 (n) "a very large position" at once on an analyst idea | when to size up | **different scope**: he calls the first "normally" / "a more normal pattern" (DRU6-C039 n), the second "sometimes". DRU2 names a condition for the second: the idea appeals intuitively AND fits the macro matrix (DRU2-C050 b, strength sometimes), more likely when he already holds the macro view (DRU2-C051 n). Both stand (Rsize6 normal; Rbuy10 / Rsize7 exception) |
| 6 | DRU4-C042 (b) waits for tops, DRU4-C029 (b) holds 2-4 years vs DRU4-C028 (n), DRU4-C041 (n), DRU4-C045 (n) Nvidia sold at 800-900 / above $2 trillion inside about a year; DRU4-C069 (n), DRU4-C070 (n) 2-year short closed at 150 bp | sold before the top | **not a rule conflict**: he calls these mistakes. The rules stand, and the examples fail them (section 5) |
| 7 [v1.1] | DRU4-C046 (b) willing to re-buy higher vs DRU4-C076 (n), DRU3-C022 (n), DRU2-C057 (n) re-bought tech near the 2000 top, "a real emotional really dumb move"; "I knew it was a bad idea at the time" | re-buying higher | **different scope**: the rule is reasoned re-entry, the 2000 case he calls emotion and a mistake against his own view (DRU2-C057 n). Both stand; no rule for telling them apart (gap). Held-out test: closed |
| 8 [v1.1] | DRU4-C067 (b, 2024) "play the turn" vs DRU6-C034 (b, 2018) not in the zero inning, DRU5-C035 (b, 2020) plow in when trends start to go up | entry at the turn or after the trend starts | **open**: the claims do not say whether "the turn" means the zero inning or the first or second inning, or whether his view changed. DRU2-C076 (b) "a lot of countercyclical stuff" may be what "play the turn" means, but no claim links them (item 14) |
| 9 | DRU6-C055 (t) "never been about earnings ... always about liquidity" vs DRU5-C015 (b) 20-30% growers, DRU1-C013 (n) sustainable earnings hold up in recessions | earnings matter or not | **open**, likely different scope (macro driver vs stock choice), but "everything for me" is stated without limits. [v1.1] DRU2-C062 (n) adds that oil, rates and dollar all up "has always been terrible for corporate earnings looking forward": earnings are used as a forward macro read, which leans to the scope reading; still open |
| 10 [v1.1] | DRU3-C030 (b) let pitches go by vs DRU4-C032 (t) do not wait two or three months to analyse; DRU2-C026 (b) "waiting for a fat pitch" vs DRU2-C054 (b) buy on intuition, analyse after (same document) | patience | **different scope**: waiting for a fat pitch vs acting fast once he likes a concept. Both stand; DRU2 states both sides in one interview |
| 11 | DRU3-C039 (b) bad outcome -> own Treasuries vs DRU3-C040 (n) in May 2023 Treasuries were "not exactly a fat pitch"; DRU4-C015 (n) short bonds in 2024 | Treasuries in a feared hard landing | **different scope**: the playbook is subject to the fat-pitch test (Rsize1, Rsize11). Both stand. See item 15 for 2022 |
| 12 | DRU5-C033 (b) markets are smarter than he is vs DRU5-C047 (n) be "a bit of a contrarian", DRU5-C052 (n) good buys at lows feel terrible | follow or fade the market | **open** (support claims only; no rule conflict). [v1.1] Now also touches Rbuy8 (countercyclical, DRU2-C076 b); see item 14 |
| 13 | DRU6-C010 (b, 2018) trust instincts and technical analysis vs DRU5-C043 (b, 2020) more fundamentals | which tool | **dated change** in emphasis (2020 later), part of item 1 |
| 14 [v1.1 new] | DRU2-C075 (b, scope sector), DRU2-C076 (b, scope all), DRU2-C069 (n) buy cyclicals while they lose money, "a lot of countercyclical stuff" vs DRU5-C035 (b) plow in when trends start to go up, DRU6-C034 (b) not in the zero inning | buy before or after the turn | **open** (held-out contradiction 1). Not a dated change: DRU2-C076 says the lessons "still work" over 30 or 40 years, and Rbuy5 (2020) and Rbuy6 (2018) are not withdrawn later. Partly a scope: DRU2-C075 is coded scope sector, with its own trigger (industry losses, capacity shutting over 2-3 years) and a fundamental measure, while Rbuy5 uses a price trend. But DRU2-C076 is unscoped, and no claim says whether a countercyclical buy also waits for the price trend to turn. Both rules are kept; a screen cannot tell which applies |
| 15 [v1.1 new] | DRU3-C039 (b), DRU5-C013 (b), DRU2-C022 (b) own Treasuries when expecting a bad outcome vs DRU2-C024 (n) short fixed income late 2021 - mid 2022 while expecting a 2023 recession (DRU2-C006 n) | the inflation condition on owning bonds | **open, narrowed** (held-out contradiction 2). DRU2-C022 is coded scope period ("past bear markets"; "the way I did it"), and the 2022 position is a dated view (DRU2-C024 n); the playbook is restated as "always used" in 2023 (DRU3-C039 b), so this is not a lasting change of view. What separates 2022 from the playbook is NOT in any quote: "not workable in 2022" is the readers' note on DRU2-C022, and the inflation statements (DRU2-C003 n above 4.5%, DRU2-C004 n above 5% until Fed funds exceed CPI, DRU2-C005 n never tamed without a recession) are principles about inflation and recession that do not mention owning or shorting bonds. So Rbuy1 gets no inflation condition; "inflation above 5%" stays a candidate condition, not a rule |
| 16 [v1.1 new] | DRU2-C066 (n, threshold, 2022) a 15-20% index rally in a post-bubble bear market -> "I'm going to take a shot" (go short) vs DRU5-C035 (b) buy rising trends (Rbuy5) | fade or buy a rising market | **closed, different scope** (held-out contradiction 3): DRU2-C066 is an index-level short trigger in a bear market preceded by an asset bubble (measure "index rally from low"; DRU2-C027 n going back to the short equity position "if the market affords me"; DRU2-C025 n aggressive shorts in a bear market "get your head ripped off in rallies"), while Rbuy5 is a long entry into a rising trend. DRU2-C066 is not a verified rule, so it adds no rule; it is support under Rproc11 |
| 17 [v1.1 new] | DRU4-C032 (t, 2024-11-06) "two or three months" vs DRU2-C049 (n, 2022-06-10) "if you wait two or three weeks ... 60 or 70% of the move will [have] taken place" | Rproc8: the delay that loses the move | **open (number)**: same measure, weeks vs months. The DRU4-C032 quote is not in this folder, so it cannot be re-checked here (the card v1 paraphrase says months). DRU2-C053 (n) "you just don't have time anymore to do deep dive analysis" fits the shorter figure. DRU2-C052 (b) "two or three weeks" is the homework period AFTER buying, a different measure (Rsell2). Rproc8 keeps the method (now on DRU2-C054 b, DRU2-C052 b) and carries both delay numbers, dated, until DRU4-C032 is checked |
| 18 [v1.1 new] | DRU2-C074 (b) business "much much better" 3 to 5 years out vs Rbuy2 12 to 24 months ahead (DRU2-C036 b, DRU4-C037 b, DRU5-C030 b) | horizon | **different measure**: DRU2-C074 is the company's business situation 3-5 years out ("long-term that's my bias"); Rbuy2 is the world and security prices 12-24 months out (DRU2-C036 quote). Both stand (Rbuy9, Rbuy2); related to the 2-4 year holding period (Rproc12) |
| 19 [v1.1 new] | DRU2-C044 (b) hot -> "turn the dial way up" and DRU2-C039 (b) 15-20% / 200-300% vs DRU2-C033 (n, 2022) "not playing anything as aggressively as I used to" | size in 2022 | **not a rule conflict**: DRU2-C033 is an anecdote about his own recent level; the rules stand |

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
| DRU1-C019 (n), DRU1-C020 (n), DRU4-C073 (n), DRU2-C058 (n) | 11-12 internet "also-rans" (1999 short; DRU2: about 10 stocks up seven or eightfold, March 1999, at Soros) | fails: shorted into a bubble, lost 3x (DRU2 note: three to four times) | no verified rule (avoid gap) |
| DRU4-C075 (n), DRU4-C076 (n), DRU3-C022 (n), DRU2-C057 (n) | tech holdings (2000; DRU2 note: about $6 billion bought near the top, $2-3 billion lost) | fails: re-bought near the top out of emotion, against his own view | Rbuy7 (scope, section 4 item 7) |
| DRU2-C060 (n) | technology stocks (January 2000) | "We're in a bubble. I'm selling all the technology stocks" (before the re-buy above) | no verified rule (sell view) |
| DRU2-C059 (n) | VeriSign (1999) | hired two people in their 20s who knew the new companies | Rproc15 |
| DRU1-C004 (n) | Silicon Valley Bank, Bed Bath & Beyond | "tip of the iceberg" (view) | none |
| DRU2-C075 (b) | chemicals (industry) | the rule's own example: buy while losing money, capacity shuts in 2-3 years, demand stays | Rbuy8 |
| DRU2-C051 (n) | a copper company (hypothetical) | a prior 3-5 year bullish copper view would make a very large quick position likely | Rbuy10, Rbuy9 |
| DRU2-C016 (n) | trucking stocks (2022) | down 40% from the high despite record earnings: a warning for the economy | Rproc2, Rproc4 |
| DRU2-C015 (b) | home builders | the leading group to watch | Rproc4 |
| DRU2-C072 (n), DRU2-C079 (n), DRU2-C080 (n) | over-earners: retail, trucking, ocean shipping (2020-2022 shorts) | "the best short-selling period I've ever seen"; by mid 2022, 80% of that set already down | mirror of Rbuy8 (DRU2-C069 n); no verified short or avoid rule |
| DRU2-C078 (n) | big tech (2022) | "too cheap for me for them to be my shorts anymore" | none (price: none stated) |
| DRU2-C083 (n) | energy companies (2022) | "still cheap relative to what we see a year or two out" | none (price: none stated); Rbuy2 |
| DRU2-C084 (n), DRU2-C085 (n), DRU2-C086 (n) | housing (2005-2007 short) | housing chart and home equity loans; shorted "everything to do with housing" within two days of an analyst's case; wrong for 6 months in 2006; held because "the deeper we dug, the more confident we got" | Rbuy10, Rproc8, Rsell2 |

Macro instruments (not companies; they show the size and asymmetry rules):

| claim | instrument | rule |
|---|---|---|
| DRU3-C031 (n), DRU3-C032 (n) | US 2-year at 15 bp, money growth 40% (2021): a fat pitch | Rsize1, Rsize11 |
| DRU4-C069 (n), DRU4-C070 (n) | the same 2-year short, closed at 150 bp, too early | fails Rsell4 |
| DRU4-C061 (n) to DRU4-C064 (n), DRU5-C032 (n) | pound vs Deutsche mark 1992: started at 20-25% of the fund, went to 100%; a one-way bet | Rsize1, Rsize4, Rsize6, Rproc8 |
| DRU6-C036 (n), DRU6-C037 (n) | Deutsche mark 1990: in big at once on conviction | Rsize7 exception |
| DRU6-C039 (n) | euro short 2014: added after the break through 135 | Rsize7 |
| DRU6-C042 (n), DRU6-C043 (n), DRU4-C080 (n) | US Treasuries 2000: kept adding as the evidence built | Rbuy1, Rsize7 exception |
| DRU2-C064 (n), DRU2-C065 (n), DRU2-C061 (n) | US Treasuries Q4 2000: 350% 10-year equivalent of the fund, betting Greenspan would reverse into a recession, after a sabbatical that cleared his head (note: 40% in the quarter) | Rbuy1, Rsize4, Rsize9 (exception) |
| DRU5-C014 (n) | long US 2, 5, 10-year (2018-19) on risk/reward | Rbuy1 |
| DRU2-C024 (n) | late 2021 - mid 2022: short fixed income, short stocks, little in currencies, long some key commodities | section 4 item 15 (Rbuy1 not applied) |
| DRU2-C066 (n), DRU2-C027 (n) | S&P (2022): a 15-20% rally from the low would be a shot at going short again | Rproc11 (section 4 item 16) |
| DRU2-C034 (t) | Bitcoin vs gold under expected inflation | Rbuy11 |
| DRU6-C023 (n), DRU6-C024 (n) | Brazil, South Africa currency "lottery ticket": risk about the carry | Rsize11 (asymmetry) |
| DRU4-C025 (t) | power and uranium as dominoes of the AI theme | Rproc7 |
| DRU3-C014 (n), DRU3-C017 (n) | copper: tight, but no meaningful position before a hard landing | Rsize10 |

## 6. Gaps (what a screen needs that he does not state)

- **Price**: no valuation rule or threshold of any kind (section 3); DRU2 adds only views (DRU2-C001 n, DRU2-C078 n, DRU2-C083 n).
- **Growth (Rbuy3)**: which growth (sales, earnings, cash flow), over what period, how "sustainable" is judged (DRU1-C013 n),
  and what counts as a "slow muted growth" period; when the growth bias is set aside (DRU2-C073 b says he ignored it in
  2020-22, no condition stated).
- **Countercyclical (Rbuy8)** [v1.1]: which industries count as cyclical (the claim names chemicals, DRU2-C075 b), how
  "losing money" is measured (company or industry, operating or net), whether he waits for a price turn (section 4 item 14),
  and the size; the margin mean-reversion support (DRU2-C069 n) gives about 3 years but no margin threshold. The mirror
  (short over-earners, DRU2-C072 n, DRU2-C079 n) has no verified rule and no "above normal" margin threshold.
- **3 to 5 years (Rbuy9)** [v1.1]: no measure of "a much much better situation" (DRU2-C074 b).
- **Analyst ideas (Rbuy10, Rsize12)** [v1.1]: no definition of "fits the macro matrix" or of an analyst's hot streak; no
  size for "a very large position" (DRU2-C050 b, DRU2-C048 b).
- **Bitcoin / gold (Rbuy11)** [v1.1]: no definition of "irresponsible monetary policy", of a bull or bear phase, or of
  position size (DRU2-C034 t).
- **Disruptor / disrupted (Rbuy4)**: no definition or measure; the claims give tech only (DRU5-C025 b) and cloud vs
  retail/staples (DRU6-C007 n).
- **Trend and stage (Rbuy5, Rbuy6, Rsize7, Rsize8)**: no lookback, no definition of a trend start, of a "technical signal",
  or of innings.
- **Top (Rsell4)**: "flattens out for quite some time" (DRU4-C043 n) has no window or rate threshold.
- **Crowding (Rsell5)** [v1.1]: no measure of "widely recognized" (DRU2-C082 b); the rule says only what is NOT a sell reason.
- **Size**: no number of holdings, no full-position size, no add size after the first third, no stop-loss level (Rsell1 is
  thesis-based). [v1.1] A position size is now stated: 15-20% of the asset base, 200-300% in macro positions (DRU2-C039 b,
  strength sometimes); the quote does not say whether the 15-20% means equity positions, and it sits below the "30 or 40
  percent" he never reached (Rsize5).
- **Indicators (Rproc2-Rproc4)**: which trucking series, which financial-conditions or liquidity measure, how cyclicals and
  defensives are defined, which group relative-strength window; the narrowing-leadership signal (DRU4-C018 n) has no
  breadth measure or threshold. [v1.1] DRU2 names home builder stock prices (DRU2-C015 b) and housing, trucking, retail
  as leading industries (DRU2-C011 b note), but gives no turn definition or window. Principles stated but not verified
  rules: the bond market as a signal (DRU2-C012 n), oil, rates and dollar all rising as bad for forward earnings
  (DRU2-C062 n), crypto-Nasdaq correlation as a high-frequency signal (DRU2-C030 n).
- **Hot / cold (Rsize9)**: no definition (drawdown size, time) and no size for "little bets" or for "turn the dial way up"
  (DRU2-C044 b).
- **Re-evaluation and bias (Rproc18, Rproc19)** [v1.1]: process rules with no measurable output.
- **Avoid**: no leverage, quality or liquidity floor for stocks; the 1999 lesson against shorting bubbles early is
  anecdote only (DRU1-C019 n, DRU1-C020 n, DRU4-C073 n, DRU2-C058 n).
- **Scope of a stock screen**: most verified rules concern macro calls and bonds, currencies and commodities (Rbuy1,
  Rbuy11, Rsize3, Rsize4, Rproc10). He made about 70% of his money in currencies and bonds (DRU6-C002 n), but "the biggest
  money I've made in equities have been in growth stocks" (DRU2-C077 n). A US 13F shows only the
  equity longs: shorts, bonds, currencies and the "five buckets" mix are not visible, so a recipe built from it covers
  only part of what he does. [v1.1] He himself cautions against reading 13Fs "because that's old data" (DRU2-C081 n),
  and he acts within days or weeks (Rproc8, DRU2-C085 n), faster than a quarterly filing shows.
