# Investor card: Cliff Sosin (CAS Investment Partners)

**File THIN (below the material bar, A13 item 8)**: the card was built from 2 documents (SOS2 2020-09-10, SOS3
2025-04-29); one more is held out and was not read. Word counts are not in the input.

Input: `claims_for_card.json` (151 claims: 36 rule_status both, 9 third, 106 no). Rule ids: R + part + number
(buy, price, avoid, sell, size, process). Strength and computability come from the claims (`strength`,
`computable_final`). both / third after an id = its rule_status; ids without a mark only support the rule.

## 1. What he buys and why

He buys a handful of businesses, four to eight, sometimes up to ten (SOS3-C013 both, SOS3-C090 third), "with a premise
of owning it forever" (SOS3-C009 both). What matters most is "the business and the price" (SOS3-C053 both). The business
must have an enduring competitive advantage, a "gadget", "some quirk about how the world works" (SOS2-C023 both,
SOS2-C025), best "a bunch of these things that are working together", "layered and and interwoven" and invariant to
technological change (SOS3-C030 third, SOS3-C031 third, SOS3-C017, SOS3-C018), so that competition cannot drive profits
to zero (SOS3-C016). It must be one that other people do not see as good: "The goal is to buy the good businesses that
other people don't think are the good businesses... it's a pari-mutuel betting system" (SOS2-C015 third), simple enough
to understand but hard enough that "everyone else misses it" (SOS3-C025 third); "you need something that scares people
away" (SOS3-C038). Price is judged by extrapolating the long-term future from the gadget and comparing it with the price:
"does it make a lot of money relative to the price? Is it going to grow a lot relative to the price?" (SOS2-C026 both,
SOS3-C033 both). Management judged by the soundness of its reasoning (SOS2-C033 both, SOS2-C037 both) now weighs more
than it used to (SOS3-C056 both). He finds ideas one at a time, with no screen (SOS2-C018 both, SOS2-C021 both), and sells
only to upgrade or when he finds he misunderstood the business (SOS3-C010 both).

## 2. Rules by part

Format: id | statement | measure | number and direction as he states it | strength | claim ids | dates said

### Buy
- Rbuy1 | The business and the price come first; management follows | none (ordering of criteria) | none stated | always | SOS3-C053 both; supports SOS3-C032 | 2025-04-29
- Rbuy2 | Own a business with an enduring competitive advantage ("gadget"): several advantages working together, layered, hard to copy and invariant to technological and social change | proxy: enduring / layered competitive advantage (outcome per SOS3-C019: high return on capital, good margins; no number) | none stated | usually | SOS2-C023 both, SOS3-C030 third, SOS3-C031 third; supports SOS2-C025, SOS3-C016, SOS3-C017, SOS3-C018, SOS3-C019, SOS3-C028 | 2020-09-10, 2025-04-29
- Rbuy3 | The business is simple enough to understand but hard enough that others miss it | none (not computable) | none stated | usually | SOS3-C025 third; supports SOS3-C022, SOS3-C023, SOS3-C024, SOS3-C020 | 2025-04-29
- Rbuy4 | Buy good businesses that other people do not think are good businesses (pari-mutuel: an opportunity needs a worry that scares others away) | proxy: market doubt, e.g. short interest (SOS2-C015; but see Rprocess2) | none stated | always | SOS2-C015 third; supports SOS2-C013, SOS2-C014, SOS2-C016, SOS3-C038, SOS3-C041, SOS3-C043 | 2020-09-10 (supports also 2025-04-29)
- Rbuy5 | Management must make well-reasoned business decisions and explain sound reasons, judged on the reasoning, not the outcome; management "matters a lot" and is weighted more than before | proxy: management decision / reasoning quality | none stated | usually | SOS2-C033 both, SOS2-C037 both, SOS3-C056 both; supports SOS2-C035, SOS2-C036, SOS2-C038, SOS2-C039, SOS2-C040, SOS3-C055 | 2020-09-10, 2025-04-29
- Rbuy6 | A new idea must beat what he already holds; a great business is skipped if selling A to buy B does not pay | none (relative to own holdings) | none stated | usually | SOS3-C088 third; supports SOS3-C089 | 2025-04-29

### Price
- Rprice1 | Cheap = the business makes a lot of money and will grow a lot relative to the price, judged by extrapolating its long-term future from its competitive gadget; valuation comes after the business is understood | proxy: earnings yield and growth relative to price | none stated (higher earnings and growth per unit of price = better) | usually | SOS3-C033 both, SOS2-C026 both; supports SOS3-C032, SOS2-C003 | 2020-09-10, 2025-04-29
- Rprice2 | Size the opportunity with a market-share exercise (e.g. if every advertiser spent a small share of revenue on it, against total retail sales) | proxy: addressable market | none stated ("50 bits" of revenue in the one example) | sometimes | SOS2-C048 third (first reader rule, second view) | 2020-09-10

### Avoid
- Ravoid1 | Less interest in businesses with narrower advantages; where the consumer surplus and the advantage are small, "move on" | proxy: width of competitive advantage / consumer surplus | none stated | usually | SOS3-C077 both, SOS3-C075 both; supports SOS3-C076, SOS3-C021 | 2025-04-29
- Ravoid2 | Loss-making companies are not excluded, but he is less interested and underwrites the path to profit with a haircut | yes: operating profit below zero | none stated (direction: loss-making -> less interest; size of the haircut not given) | sometimes | SOS3-C079 both, SOS3-C074 both; supports SOS3-C073 | 2025-04-29
- Ravoid3 | Non-US stocks go to the bottom of the list, after all American stocks | yes: US domicile | none stated (non-US ranked last, not excluded) | usually | SOS3-C086 both; supports SOS3-C085 | 2025-04-29

### Sell
- Rsell1 | Own with the premise of forever; sell only to upgrade to something better or on discovering he misunderstood the business | none | none stated | always | SOS3-C010 both, SOS3-C009 both; supports SOS2-C010 | 2025-04-29
- Rsell2 | Compare what happens with the predictions of his model of the business; if they do not line up, update the model, maybe throw it out, and sell what he no longer understands | none | none stated | usually | SOS3-C011 both, SOS3-C012 both | 2025-04-29
- Rsell3 | Low turnover: on average one position bought and/or sold a year | proxy: positions changed per year (computable_final no) | about one a year | usually | SOS3-C014 both | 2025-04-29
- Rsell4 | Hold readily ("fall in love with my companies"); the average mistake is selling too soon | none | none stated | sometimes | SOS2-C061 both; supports SOS2-C060 | 2020-09-10

### Size
- Rsize1 | Concentrated: a handful of well-understood holdings, watched closely | number of holdings (computable_final no) | between four and eight, up to 10 at one point | usually | SOS3-C013 both, SOS3-C090 third, SOS3-C009 both; supports SOS3-C080, SOS3-C081, SOS3-C078 | 2025-04-29
- Rsize2 | He does not buy more of a position above a certain share of the fund | position weight (computable_final no) | none stated (amount not given; above it, no adding) | usually | SOS3-C065 both | 2025-04-29

### Process
- Rprocess1 | No quantitative top-of-funnel screen; ideas come organically, one company at a time | none | none stated | always | SOS2-C018 both, SOS2-C020 both, SOS2-C021 both; supports SOS2-C005, SOS2-C011 | 2020-09-10
- Rprocess2 | He never searches for battleground (heavily shorted) stocks; they arise by accident | none | none stated | always | SOS2-C012 both; supports SOS2-C011 | 2020-09-10
- Rprocess3 | After getting to know a business, be rigorous: model how it and its industry compete, using a set of frameworks for how a company makes money in a competitive world | none | none stated | usually | SOS2-C022 both, SOS3-C026 both; supports SOS3-C034, SOS3-C036 | 2020-09-10, 2025-04-29
- Rprocess4 | Judge management as the culture of the whole organisation and how its people are assembled, not mainly whether the CEO is great | proxy: organisational culture / design | none stated | usually | SOS2-C028 both, SOS2-C031 both, SOS2-C032 both; supports SOS2-C029, SOS2-C034 | 2020-09-10
- Rprocess5 | Evidence on management comes from listening to them in public over time and, best, from former employees (meetings tell little) | none | none stated | usually | SOS3-C058 both, SOS3-C059 both; supports SOS3-C057, SOS3-C060, SOS3-C061 | 2025-04-29
- Rprocess6 | Instrument a holding with outside data (track every unit sold against a peer and market indices; scraped and card data via a consulting firm) to see a turn | none | none stated | usually | SOS3-C052 both, SOS3-C068 both, SOS3-C084 third; supports SOS3-C069 | 2025-04-29
- Rprocess7 | Read broadly and study companies one after another, including adjacent businesses while waiting | none | none stated | usually | SOS3-C035 both, SOS3-C046 third; supports SOS3-C047 | 2025-04-29
- Rprocess8 | Uses AI tools daily, especially where much information is on the internet | none | none stated | usually | SOS3-C082 both | 2025-04-29
- Rprocess9 | Works fairly independently, without a large team | none | none stated | usually | SOS3-C083 both | 2025-04-29

## 3. None stated

Every part has at least one verified rule. Parts or items with no stated number (the recipe then uses the 13F or a
convention, tagged):
- buy: no number for advantage, doubt or management (Rbuy2-Rbuy5).
- price: no valuation number (Rprice1); the market-share exercise is one example (Rprice2).
- avoid: no size of the loss-making haircut (Ravoid2); non-US is ranked last, not cut off (Ravoid3).
- size: no position cap amount (Rsize2), no weighting rule; only the count 4-8 (up to 10) is stated (Rsize1).
- sell: only turnover is stated (about one a year, Rsell3); no price or valuation trigger.

## 4. Changes of view and scope

- Management, DATED CHANGE OF VIEW (later wins): earlier he gave management little weight beyond avoiding frauds
  (SOS2-C027, recalled in 2020 as his view five years earlier; SOS3-C054, recalled in 2025 as his view five years
  earlier); now "management matters a lot. So, it gets weighted into my thinking in a way it wasn't before" (SOS3-C056,
  2025). Later wins: Rbuy5 stands. Timing is unclear: in 2020 he already said "I've come to think a lot more about how
  the people are assembled" (SOS2-C031), while in 2025 he places himself "firmly" business-only five years earlier
  (SOS3-C054). The direction is the same; only the date of the change is open.
- Management vs business, DIFFERENT SCOPE (both stand): business and price still come first (SOS3-C053, 2025) while
  management weighs more than before (SOS3-C056, 2025); "A great team with a terrible business is ... going to be a slog"
  (SOS3-C055). He does not spend much time on whether the CEO is great (SOS2-C032) but judges the organisation and the
  reasoning (SOS2-C028, SOS2-C033): CEO greatness vs organisation, both stand.
- Doubt and short interest, DIFFERENT SCOPE (both stand): his holdings end up doubted and heavily shorted (SOS2-C013,
  SOS2-C014, SOS2-C016) and he aims for good businesses others do not think good (SOS2-C015), but he never searches for
  battleground stocks (SOS2-C012) and found a highly-shorted screen "very hard" (SOS2-C011). Doubt is a feature of what
  he ends up owning, not a search filter.
- Screens, DIFFERENT SCOPE (both stand): Herbalife showed up on screens as quantitatively cheap (SOS2-C005) and he muses
  about screens for top-decile outcomes (SOS2-C019, a view, not his practice), but he does no screening (SOS2-C018).
- Concentration, DIFFERENT SCOPE (both stand): concentration produced the fund's success (SOS3-C080), yet "on the
  margin there's room to be more diversified", especially for companies "less ... stout" (SOS3-C081), applied as "a
  teaspoon of medicine" (SOS3-C078). Same 2025 document.
- Loss-makers, DATED CHANGE OF VIEW (later wins): the Carvana lesson that going from unprofitable to profitable is
  harder than on paper (SOS3-C073) leads to the 2025 haircut (SOS3-C074, SOS3-C079): Ravoid2 stands.
- Position cap, OPEN: he does not add above "a certain amount" of the fund (SOS3-C065, 2025), yet Carvana was "mid-40s%
  of capital" in 2020 (SOS2-C001), Herbalife "as much as a 30% position" (SOS2-C002), and in 2022 he "bought a bunch
  more" Carvana while it was "by far" his biggest position (SOS3-C064, SOS3-C066). With no amount stated, it cannot be
  told whether these broke the rule or whether the rule came after them.
- Contained businesses vs pricing, DIFFERENT SCOPE (both stand): he likes contained businesses (SOS3-C022, SOS3-C023)
  but says easy contained ones get priced in (SOS3-C024, SOS3-C037); Rbuy3 resolves it (simple, yet missed).
- Moral panics, DIFFERENT SCOPE (both stand): one can buy into moral panics and do well (SOS3-C041, SOS3-C043), but
  they bring legislative or regulatory risk (SOS3-C042).

## 5. Examples

| id | company | rule |
|---|---|---|
| SOS2-C006, SOS2-C007, SOS2-C008, SOS2-C009 | Herbalife (belief-driven, durable demand; cheaper rivals such as GNC soy protein do not break it) | Rbuy2 fits |
| SOS2-C003 | Herbalife (more expensive, less attractive; still owned) | Rprice1 |
| SOS2-C005 | Herbalife (showed up quantitatively cheap on screens before he studied it) | Rprocess1 (scope) |
| SOS2-C002 | Herbalife (as much as 30% position) | Rsize2 (open) |
| SOS3-C045 | multi-level marketers (owned) | Rbuy4 support (bad but not illegal, SOS3-C043) |
| SOS2-C010 | United Rentals sold to buy Ashtead | Rsell1 (upgrade) |
| SOS2-C024, SOS3-C029 | Ashtead / Sunbelt, construction equipment rental (scale, fixed fleets, Cournot market) | Rbuy2 fits |
| SOS3-C027 | cruise lines (fixed capacity, Cournot) | Rbuy2 fits (framework example) |
| SOS3-C023 | cigarettes (contained business; software tooling the uncontained contrast) | Rbuy3 fits |
| SOS3-C036 | early nicotine vaping company (unnamed) | Rprocess3 (framework gave confidence) |
| SOS2-C042, SOS2-C043, SOS2-C045 | Cardlytics (reach, natural monopoly) | Rbuy2 fits |
| SOS2-C048 | Cardlytics (advertiser share of retail sales) | Rprice2 |
| SOS2-C049, SOS2-C050, SOS2-C051, SOS2-C053 | Cardlytics (~100m net income on return to earlier revenue per user, against ~$2bn market cap) | Rprice1 |
| SOS2-C055, SOS2-C056, SOS2-C057, SOS2-C058 | Cardlytics (downside by inversion; ~$2bn floor) | Rprice1 support (example only) |
| SOS3-C047, SOS3-C048, SOS3-C050 | Carvana (economies of scope, gets better as it gets bigger; fast conviction after years of study) | Rbuy2, Rprocess7 |
| SOS3-C056, SOS3-C062, SOS3-C063 | Carvana management | Rbuy5 |
| SOS3-C052, SOS3-C069, SOS3-C084 | Carvana tracked car by car against CarMax and indices | Rprocess6 |
| SOS3-C046 | CarMax, car dealerships (studied while waiting) | Rprocess7 |
| SOS3-C073, SOS3-C076 | Carvana (loss-making path to profit; survived on large margins) | Ravoid2 lesson |
| SOS3-C075 | Carvana (lesson against narrower advantages) | Ravoid1 lesson |
| SOS2-C001, SOS3-C064, SOS3-C066, SOS3-C067, SOS3-C070, SOS3-C071 | Carvana (mid-40s% in 2020; added at 80 in 2022; half now, half on a visible turn; poison pill at 5% stopped buying) | Rsize2 (open) |
| SOS3-C077 | "pencils" (works, but small consumer surplus) | Ravoid1 fails |
| SOS3-C086 | Chinese stock pitched to him | Ravoid3 (last on the list) |
| SOS3-C085 | UK (naivety hard to overcome) | Ravoid3 support |
| SOS3-C089 | Google 2010 (looked cheap; passed, holdings did better) | Rbuy6 |
| SOS3-C061 | Capital One (former employees impress) | Rprocess5 |
| SOS2-C040 | retailers (sensitive to who runs them) | Rbuy5 |
| SOS2-C030, SOS2-C034 | Boeing, Starbucks (leader fit; organisation sets what it can do) | Rprocess4 support |
| SOS3-C082 | Medicaid managed care (AI for document-heavy sectors, note) | Rprocess8 |
| SOS3-C044 | oil companies (shunning does not make them very cheap) | Rprice1 support |

## 6. Gaps (what a screen needs that he does not state)

- Valuation: no earnings-yield, multiple, growth or discount-rate threshold (Rprice1, SOS3-C033 calls them "pretty
  trivial calculations" but gives none). Cardlytics figures (SOS2-C049) are one case, not a rule.
- Advantage: no measure for "enduring", "layered" or wide; return on capital and margins are named only as the outcome
  (SOS3-C019), with no number; Carvana's ~10.5% vs dealers' ~4.5% EBITDA margin (SOS3-C051) and 13-14% vs 5% (SOS3-C076)
  are anecdotes.
- Doubt: no measure or threshold; short interest is a proxy he does not screen on (Rbuy4 vs Rprocess2).
- Management: no computable measure; founder or insider control "isn't necessarily an absolute requirement" (SOS2-C035).
- Contained / simple-but-missed business (Rbuy3): no measure.
- Loss-makers: size of the haircut not stated (Ravoid2).
- Universe: no market-cap, liquidity or sector limits stated; only US first (Ravoid3); no ethical screen beyond law
  (SOS3-C040, not a verified rule).
- Size: no position cap amount (Rsize2), no starting or maximum weight; staged entry "I'll buy half now and I'll buy half when I can see it turn" is one
  example (SOS3-C067); anecdotal weights 30% (SOS2-C002) and mid-40s% (SOS2-C001) -> recipe uses the 13F.
- Sell: no price, valuation or loss trigger; only "upgrade" and "misunderstood" (Rsell1-Rsell2) and turnover of about one
  a year (Rsell3); holding horizon only as "forever" premise and 3-10-year feedback loops (SOS3-C006).
- Downside test by inversion (SOS2-C055) is an example, not a verified rule: no measure.

## Count

Rules per part: buy 6, price 2, avoid 3, sell 4, size 2, process 9 (total 26).
Open contradictions: 1 (position cap Rsize2 vs the Carvana / Herbalife weights and the 2022 add); plus the date (not
the direction) of the management change is open.
