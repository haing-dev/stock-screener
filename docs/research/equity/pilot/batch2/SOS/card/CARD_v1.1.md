v1.1 = v1 + SOS1 merged after a FAILED held-out test (A13 item 8)

# Investor card: Cliff Sosin (CAS Investment Partners)

**File THIN (below the material bar, A13 item 8)**: v1 was built from 2 documents (SOS2 2020-09-10, SOS3 2025-04-29).
The held-out document SOS1 (2025-05-08) was then tested against v1 (heldout_result.json: 4 of 9 rules matched, 2 open
sell contradictions, FAILED) and is now merged. With SOS1 merged there is no held-out document left: v1.1 has not been
tested on unseen material. Word counts are not in the input.

Input: `claims_for_card.json` (151 claims: 36 rule_status both, 9 third, 106 no) + `claims_SOS1.json` (58 claims: 7
both, 2 third, 49 no). Rule ids: R + part + number (buy, price, avoid, sell, size, process). Strength and computability
come from the claims (`strength`, `computable_final`). both / third after an id = its rule_status; ids without a mark
only support the rule. **[v1.1]** marks what SOS1 added or changed.

## 1. What he buys and why

He buys a handful of businesses, four to eight, sometimes up to ten (SOS3-C013 both, SOS3-C090 third), "with a premise
of owning it forever" (SOS3-C009 both). What matters most is "the business and the price" (SOS3-C053 both). The business
must have an enduring competitive advantage, a "gadget", "some quirk about how the world works" (SOS2-C023 both,
SOS2-C025), best "a bunch of these things that are working together", "layered and and interwoven" and invariant to
technological change (SOS3-C030 third, SOS3-C031 third, SOS3-C017, SOS3-C018), so that competition cannot drive profits
to zero (SOS3-C016). It must be one that other people do not see as good: "The goal is to buy the good businesses that
other people don't think are the good businesses... it's a pari-mutuel betting system" (SOS2-C015 third), simple enough
to understand but hard enough that "everyone else misses it" (SOS3-C025 third); "you need something that scares people
away" (SOS3-C038); "the blowups of the past in different sectors and sort of the complexity of it has generally kept
people out" (SOS1-C005). Price is judged by extrapolating the long-term future from the gadget and comparing it with the
price: "does it make a lot of money relative to the price? Is it going to grow a lot relative to the price?" (SOS2-C026
both, SOS3-C033 both), with a margin of safety because things "sometimes go right, sometimes go wrong" (SOS1-C044).
Management judged by the soundness of its reasoning (SOS2-C033 both, SOS2-C037 both) now weighs more than it used to
(SOS3-C056 both). He finds ideas one at a time, with no screen and a "very unstructured" top of the funnel (SOS2-C018
both, SOS2-C021 both, SOS1-C055 both), grows a circle of competence outward (SOS1-C006 third), and runs calls with
open-ended questions, follow-ups saved for the end (SOS1-C047 both, SOS1-C049 both). He sells to upgrade, when he finds
he misunderstood the business, or when his model of it fails (SOS3-C010 both, SOS3-C011 both, SOS3-C012 both; Herbalife
case SOS1-C036, SOS1-C039, SOS1-C040), and when a holding falls while the data say the business is fine he may buy more
(SOS1-C016 third).

## 2. Rules by part

Format: id | statement | measure | number and direction as he states it | strength | claim ids | dates said

### Buy
- Rbuy1 | The business and the price come first; management follows | none (ordering of criteria) | none stated | always | SOS3-C053 both; supports SOS3-C032 | 2025-04-29
- Rbuy2 | Own a business with an enduring competitive advantage ("gadget"): several advantages working together, layered, hard to copy and invariant to technological and social change | proxy: enduring / layered competitive advantage (outcome per SOS3-C019: high return on capital, good margins; **[v1.1]** margins "so much higher than everybody else's" give the ability to absorb a downturn, SOS1-C022, proxy margin vs industry; no number) | none stated | usually | SOS2-C023 both, SOS3-C030 third, SOS3-C031 third; supports SOS2-C025, SOS3-C016, SOS3-C017, SOS3-C018, SOS3-C019, SOS3-C028, **[v1.1]** SOS1-C022, SOS1-C034 | 2020-09-10, 2025-04-29 (support 2025-05-08)
- Rbuy3 | The business is simple enough to understand but hard enough that others miss it | none (not computable) | none stated | usually | SOS3-C025 third; supports SOS3-C022, SOS3-C023, SOS3-C024, SOS3-C020, **[v1.1]** SOS1-C005 | 2025-04-29 (support 2025-05-08)
- Rbuy4 | Buy good businesses that other people do not think are good businesses (pari-mutuel: an opportunity needs a worry that scares others away; **[v1.1]** past blowups and complexity keep others out, SOS1-C005) | proxy: market doubt, e.g. short interest (SOS2-C015; but see Rprocess2) | none stated | always | SOS2-C015 third; supports SOS2-C013, SOS2-C014, SOS2-C016, SOS3-C038, SOS3-C041, SOS3-C043, **[v1.1]** SOS1-C005 | 2020-09-10 (supports also 2025-04-29, 2025-05-08)
- Rbuy5 | Management must make well-reasoned business decisions and explain sound reasons, judged on the reasoning, not the outcome; management "matters a lot" and is weighted more than before | proxy: management decision / reasoning quality | none stated | usually | SOS2-C033 both, SOS2-C037 both, SOS3-C056 both; supports SOS2-C035, SOS2-C036, SOS2-C038, SOS2-C039, SOS2-C040, SOS3-C055 | 2020-09-10, 2025-04-29
- Rbuy6 | A new idea must beat what he already holds; a great business is skipped if selling A to buy B does not pay | none (relative to own holdings) | none stated | usually | SOS3-C088 third; supports SOS3-C089 | 2025-04-29

### Price
- Rprice1 | Cheap = the business makes a lot of money and will grow a lot relative to the price, judged by extrapolating its long-term future from its competitive gadget; valuation comes after the business is understood; **[v1.1]** a margin of safety is needed because outcomes vary | proxy: earnings yield and growth relative to price; **[v1.1]** discount to estimated value (SOS1-C044) | none stated (higher earnings and growth per unit of price = better; size of the margin of safety not given) | usually | SOS3-C033 both, SOS2-C026 both; supports SOS3-C032, SOS2-C003, **[v1.1]** SOS1-C044, SOS1-C020 | 2020-09-10, 2025-04-29 (support 2025-05-08)
- Rprice2 | Size the opportunity with a market-share exercise (e.g. if every advertiser spent a small share of revenue on it, against total retail sales) | proxy: addressable market | none stated ("50 bits" of revenue in the one example) | sometimes | SOS2-C048 third (first reader rule, second view) | 2020-09-10

### Avoid
- Ravoid1 | Less interest in businesses with narrower advantages; where the consumer surplus and the advantage are small, "move on" | proxy: width of competitive advantage / consumer surplus | none stated | usually | SOS3-C077 both, SOS3-C075 both; supports SOS3-C076, SOS3-C021 | 2025-04-29
- Ravoid2 | Loss-making companies are not excluded, but he is less interested and underwrites the path to profit with a haircut | yes: operating profit below zero | none stated (direction: loss-making -> less interest; size of the haircut not given) | sometimes | SOS3-C079 both, SOS3-C074 both; supports SOS3-C073 | 2025-04-29
- Ravoid3 | Non-US stocks go to the bottom of the list, after all American stocks | yes: US domicile | none stated (non-US ranked last, not excluded) | usually | SOS3-C086 both; supports SOS3-C085 | 2025-04-29

SOS1 adds no avoid rule: its avoid claims are sector principles with rule_status no (prime lending as "selling disaster
insurance", SOS1-C002; false signals in subprime lending, SOS1-C004; "A business that's growing 2% is dangerously close to
shrinking 2%", multi-level marketers, SOS1-C037; chemicals harder than he thought, SOS1-C045). They are listed in
section 5 and section 6, not used as rules.

### Sell
- Rsell1 | Own with the premise of forever; sell to upgrade to something better or on discovering he misunderstood the business. **[v1.1] narrowed**: "only" now reads "only for these reasons or when his model of the business fails (Rsell2)"; valuation alone is not a current trigger (early-career valuation sales were a dated earlier practice, section 4) | none | none stated | always | SOS3-C010 both, SOS3-C009 both; supports SOS2-C010, **[v1.1]** SOS1-C031 | 2025-04-29 (support 2025-05-08)
- Rsell2 | Compare what happens with the predictions of his model of the business; if they do not line up, update the model, maybe throw it out, and sell what he no longer understands. **[v1.1] widened in scope (examples only)**: this covers re-basing expected growth on recent years when growth proves elusive and cutting the position (Herbalife 2020-21, SOS1-C036, SOS1-C038), and selling when a thesis-breaker he had named in advance and monitored then occurs (Herbalife: effective weight-loss drug named 2018, SOS1-C040; monitored, SOS1-C042; GLP-1 results 2022, "well that's that", SOS1-C039) | none (**[v1.1]** proxy in the one example: revenue growth re-based on recent years, SOS1-C038, no number) | none stated | usually | SOS3-C011 both, SOS3-C012 both; supports **[v1.1]** SOS1-C036, SOS1-C038, SOS1-C039, SOS1-C040, SOS1-C042, SOS1-C035, SOS1-C031 | 2025-04-29 (examples 2025-05-08, meant 2018, 2020-21, 2022)
- Rsell3 | Low turnover: on average one position bought and/or sold a year | proxy: positions changed per year (computable_final no) | about one a year | usually | SOS3-C014 both | 2025-04-29
- Rsell4 | Hold readily ("fall in love with my companies"); the average mistake is selling too soon; **[v1.1]** do not trim a winner by rule once it is large: "you will inevitably never own something that really does tremendously well for you" | none | none stated (**[v1.1]** the trimming rule he rejects is "diversifying once something went over 30%", SOS1-C033, an example about others) | sometimes | SOS2-C061 both; supports SOS2-C060, **[v1.1]** SOS1-C032, SOS1-C033 | 2020-09-10 (support 2025-05-08)

### Size
- Rsize1 | Concentrated: a handful of well-understood holdings, watched closely | number of holdings (computable_final no) | between four and eight, up to 10 at one point | usually | SOS3-C013 both, SOS3-C090 third, SOS3-C009 both; supports SOS3-C080, SOS3-C081, SOS3-C078 | 2025-04-29
- Rsize2 | He does not buy more of a position above a certain share of the fund | position weight (computable_final no) | none stated (amount not given; above it, no adding) | usually | SOS3-C065 both | 2025-04-29
- **[v1.1] NEW** Rsize3 | When the stock falls (or moves "crazy" with no connection to the data) but his data say the business is fine, he can live with it and, with spare cash, buy more | none (computable_final no; needs a price fall plus a business-is-fine reading from his own data) | none stated (no size of fall, no amount added) | sometimes | SOS1-C016 third; supports SOS1-C015, SOS1-C021, SOS1-C014 | 2025-05-08

### Process
- Rprocess1 | No quantitative top-of-funnel screen; ideas come organically, one company at a time; **[v1.1]** the top of the funnel is "very unstructured" | none | none stated | always | SOS2-C018 both, SOS2-C020 both, SOS2-C021 both, **[v1.1]** SOS1-C055 both; supports SOS2-C005, SOS2-C011 | 2020-09-10, **[v1.1]** 2025-05-08
- Rprocess2 | He never searches for battleground (heavily shorted) stocks; they arise by accident | none | none stated | always | SOS2-C012 both; supports SOS2-C011 | 2020-09-10
- Rprocess3 | After getting to know a business, be rigorous: model how it and its industry compete, using a set of frameworks for how a company makes money in a competitive world; **[v1.1]** examples include stress tests of the model (price elasticity of demand, a 30% demand drop, a 10% used-car price shock per unit) | none | none stated | usually | SOS2-C022 both, SOS3-C026 both; supports SOS3-C034, SOS3-C036, **[v1.1]** SOS1-C024, SOS1-C025, SOS1-C027, SOS1-C008, SOS1-C009 | 2020-09-10, 2025-04-29 (examples 2025-05-08)
- Rprocess4 | Judge management as the culture of the whole organisation and how its people are assembled, not mainly whether the CEO is great | proxy: organisational culture / design | none stated | usually | SOS2-C028 both, SOS2-C031 both, SOS2-C032 both; supports SOS2-C029, SOS2-C034 | 2020-09-10
- Rprocess5 | Evidence on management comes from listening to them in public over time and, best, from former employees (meetings tell little) | none | none stated | usually | SOS3-C058 both, SOS3-C059 both; supports SOS3-C057, SOS3-C060, SOS3-C061 | 2025-04-29
- Rprocess6 | Instrument a holding with outside data (track every unit sold against a peer and market indices; scraped and card data via a consulting firm) to see a turn; **[v1.1] narrowed**: the most useful use of alternative data is to step back and validate the broader hypothesis, not to read week-to-week sales ("this week's sales are light ... what does that tell you about next week's sales? it's sort of like nothing") | none | none stated | usually | SOS3-C052 both, SOS3-C068 both, SOS3-C084 third, **[v1.1]** SOS1-C013 both; supports SOS3-C069, **[v1.1]** SOS1-C012, SOS1-C018, SOS1-C008 | 2025-04-29, **[v1.1]** 2025-05-08
- Rprocess7 | Read broadly and study companies one after another, including adjacent businesses while waiting; **[v1.1]** build a circle of competence and keep growing around it; count each day a success if he has learned something incrementally; learning is cumulative and transfers to other contexts | none | none stated | usually | SOS3-C035 both, SOS3-C046 third, **[v1.1]** SOS1-C056 both, SOS1-C006 third; supports SOS3-C047, **[v1.1]** SOS1-C053, SOS1-C058 | 2025-04-29, **[v1.1]** 2025-05-08
- Rprocess8 | Uses AI tools daily, especially where much information is on the internet; **[v1.1]** AI tools make life-science and biotech companies feel more approachable | none | none stated | usually | SOS3-C082 both; supports **[v1.1]** SOS1-C054 | 2025-04-29 (support 2025-05-08)
- Rprocess9 | Works fairly independently, without a large team | none | none stated | usually | SOS3-C083 both | 2025-04-29
- **[v1.1] NEW** Rprocess10 | Call technique (expert calls and management meetings): start with open-ended questions, let them talk and stay quiet; do not ask follow-ups during the answer, write them down and ask them after; it works "really well for management teams" too; they then talk about things he did not know and show how they think | none | none stated (calls take longer; he has the budget, SOS1-C050) | usually | SOS1-C047 both, SOS1-C049 both, SOS1-C051 both; supports SOS1-C048, SOS1-C050 | 2025-05-08
- **[v1.1] NEW** Rprocess11 | Reads expert-call transcripts too, and rates their quality as "very mixed" | none | none stated | sometimes | SOS1-C052 both | 2025-05-08

## 3. None stated

Every part has at least one verified rule. Parts or items with no stated number (the recipe then uses the 13F or a
convention, tagged):
- buy: no number for advantage, doubt or management (Rbuy2-Rbuy5); **[v1.1]** "margin vs industry" (SOS1-C022) is named,
  with no number.
- price: no valuation number (Rprice1); **[v1.1]** no size of the margin of safety (SOS1-C044); the market-share exercise
  is one example (Rprice2).
- avoid: no size of the loss-making haircut (Ravoid2); non-US is ranked last, not cut off (Ravoid3).
- size: no position cap amount (Rsize2), no weighting rule; only the count 4-8 (up to 10) is stated (Rsize1);
  **[v1.1]** no size of fall or amount added for Rsize3.
- sell: only turnover is stated (about one a year, Rsell3); no price or valuation trigger; **[v1.1]** the growth re-basing
  in Rsell2 has no threshold (SOS1-C038).
- process: **[v1.1]** Rprocess10-Rprocess11 are not computable (technique and sources).

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
  about screens for top-decile outcomes (SOS2-C019, a view, not his practice), but he does no screening (SOS2-C018);
  **[v1.1]** in 2025 the top of the funnel is still "very unstructured" (SOS1-C055).
- Concentration, DIFFERENT SCOPE (both stand): concentration produced the fund's success (SOS3-C080), yet "on the
  margin there's room to be more diversified", especially for companies "less ... stout" (SOS3-C081), applied as "a
  teaspoon of medicine" (SOS3-C078). Same 2025 document.
- Loss-makers, DATED CHANGE OF VIEW (later wins): the Carvana lesson that going from unprofitable to profitable is
  harder than on paper (SOS3-C073) leads to the 2025 haircut (SOS3-C074, SOS3-C079): Ravoid2 stands.
- Position cap, OPEN: he does not add above "a certain amount" of the fund (SOS3-C065, 2025), yet Carvana was "mid-40s%
  of capital" in 2020 (SOS2-C001), Herbalife "as much as a 30% position" (SOS2-C002), and in 2022 he "bought a bunch
  more" Carvana while it was "by far" his biggest position (SOS3-C064, SOS3-C066). With no amount stated, it cannot be
  told whether these broke the rule or whether the rule came after them. **[v1.1]** SOS1 adds weight to the size side
  ("I've never been in this position where ... I have so much invested in a single stock", SOS1-C057; the poison pill
  meant "I couldn't buy more", SOS1-C017) but states no amount: still OPEN.
- **[v1.1]** Cap on adding vs no trimming, DIFFERENT SCOPE (both stand): Rsize2 limits buying more above a share of the
  fund (SOS3-C065); Rsell4 rejects trimming a winner by rule once it is large (SOS1-C032, SOS1-C033). One governs adding,
  the other selling; neither gives an amount.
- **[v1.1]** Adding on falls vs the cap, DIFFERENT SCOPE (both stand): Rsize3 (buy more when the stock falls and the data
  say the business is fine, SOS1-C016) applies below the Rsize2 cap; the claims do not say what he does when a fallen
  holding is already above it.
- Contained businesses vs pricing, DIFFERENT SCOPE (both stand): he likes contained businesses (SOS3-C022, SOS3-C023)
  but says easy contained ones get priced in (SOS3-C024, SOS3-C037); Rbuy3 resolves it (simple, yet missed).
- Moral panics, DIFFERENT SCOPE (both stand): one can buy into moral panics and do well (SOS3-C041, SOS3-C043), but
  they bring legislative or regulatory risk (SOS3-C042).
- **[v1.1]** Alternative data, DIFFERENT SCOPE (both stand): he tracks a holding unit by unit with outside data
  (SOS3-C052, SOS3-C068, SOS3-C084) and waits to "see it turn" (SOS3-C067), but the most useful use is to validate the
  broader hypothesis (SOS1-C013) and one light week says "sort of like nothing" about the next (SOS1-C012). The data test
  the thesis and its turns, not weekly moves.
- **[v1.1]** Management meetings, DIFFERENT SCOPE (both stand): Rprocess5 ranks sources and says meetings tell little
  (SOS3-C058, SOS3-C059); Rprocess10 says how he runs a meeting or call when he has one and that the technique "works
  really well for management teams" (SOS1-C051). One is about how much a source weighs, the other about how to question;
  the claims do not say whether the technique changes how much a meeting tells. Noted as a tension, not a contradiction.
- **[v1.1]** Herbalife sale on a named risk vs Rsell1 "only", CLOSED AS DIFFERENT SCOPE (on example claims): the 2022 sale
  on the GLP-1 results (SOS1-C039) was neither an upgrade nor a misunderstanding (Rsell1, SOS3-C010), but it fits Rsell2
  (SOS3-C011, SOS3-C012): the risk was part of his model in advance ("if there was a really effective medical treatment
  for weight loss, that'd be really bad", SOS1-C040, meant 2018), he was "constantly monitoring" it (SOS1-C042), and when
  it occurred the model no longer held. The sale also followed a model update: by 2020-21 growth had "proven to be
  elusive" and he re-based expected growth on 2014-21 and cut the position (SOS1-C036, SOS1-C038). Rsell1's "only" is
  narrowed to include Rsell2 (section 2). Limit: every SOS1 claim here is an example (rule_status no); he does not state
  "sell when a named thesis-breaker occurs" as a rule, so it stays inside Rsell2 and is not a separate rule.
- **[v1.1]** Early-career valuation sales vs Rsell1, CLOSED AS DATED CHANGE OF VIEW (later wins, date open): "in my very
  early days ... I sold both of those kind of for valuation type reasons" (Celanese, Ashland; SOS1-C043, self-dated as
  early career). His later stated rules have no valuation trigger: the average mistake is selling too soon (SOS2-C061,
  2020) and he sells to upgrade or on misunderstanding (SOS3-C010, 2025), and does not trim winners by rule (SOS1-C032,
  2025). Later wins: Rsell1 stands. Limits: the year of the early sales is not given, and the lesson he draws in SOS1 is
  about chemicals being hard to predict (SOS1-C045) and early overconfidence (SOS1-C046), not an explicit rejection of
  selling on valuation; the change is therefore inferred from the dated contrast, not stated by him.
- Herbalife cut as growth proved elusive (SOS1-C036): closed by the held-out test as a fit to Rsell2 and Rsell1's
  "misunderstood" (heldout_result.json); kept closed.
- **[v1.1]** Growth extrapolation, DATED LESSON (both stand): he extrapolates the long-term future (Rprice1, SOS3-C033), but
  on Herbalife "I kind of thought the past would be prologue" was a mistake (SOS1-C035) and in 2021 he switched to recent
  growth (SOS1-C038). Rprice1 stands; the lesson sits in Rsell2 (update the model when outcomes disagree).

## 5. Examples

| id | company | rule |
|---|---|---|
| SOS2-C006, SOS2-C007, SOS2-C008, SOS2-C009 | Herbalife (belief-driven, durable demand; cheaper rivals such as GNC soy protein do not break it) | Rbuy2 fits |
| SOS2-C003 | Herbalife (more expensive, less attractive; still owned) | Rprice1 |
| SOS2-C005 | Herbalife (showed up quantitatively cheap on screens before he studied it) | Rprocess1 (scope) |
| SOS2-C002 | Herbalife (as much as 30% position) | Rsize2 (open) |
| **[v1.1]** SOS1-C035, SOS1-C036, SOS1-C038 | Herbalife (assumed past growth would continue; by 2020-21 growth elusive; re-based on 2014-21; position cut) | Rsell2 |
| **[v1.1]** SOS1-C040, SOS1-C042, SOS1-C039 | Herbalife (weight-loss drug named as a thesis-breaker 2018; monitored; sold on GLP-1 results 2022) | Rsell2 (scope, section 4) |
| **[v1.1]** SOS1-C041 | Novo, Lilly (not bought after the GLP-1 sale; "mistake") | none (anecdote) |
| SOS3-C045 | multi-level marketers (owned) | Rbuy4 support (bad but not illegal, SOS3-C043) |
| **[v1.1]** SOS1-C037 | multi-level marketers ("growing 2% is dangerously close to shrinking 2%") | none (sector principle) |
| SOS2-C010 | United Rentals sold to buy Ashtead | Rsell1 (upgrade) |
| **[v1.1]** SOS1-C043, SOS1-C045 | Celanese, Ashland (sold on valuation in his very early days; chemicals harder than he thought) | Rsell1 (dated change, section 4) |
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
| **[v1.1]** SOS1-C018, SOS1-C008 | Carvana (average delivery times and headcount tracked as demand signs; ABS performance data for its non-prime loans) | Rprocess6 |
| **[v1.1]** SOS1-C009, SOS1-C010, SOS1-C011, SOS1-C007 | Carvana financing (9% gain on sale checked against loan economics; loans perform better; prime experience selects good non-prime borrowers; ~couple thousand dollars profit per unit) | Rprocess3, Rbuy2 support |
| **[v1.1]** SOS1-C020 | Carvana (long-run earnings per car x 20 million cars = $60bn, then discounted) | Rprice1 (example) |
| **[v1.1]** SOS1-C024, SOS1-C025, SOS1-C027 | Carvana (price elasticity work; 30% demand drop vs 4% price cut; 10% car-price shock ~ $400 a car) | Rprocess3 (stress tests) |
| **[v1.1]** SOS1-C022, SOS1-C023, SOS1-C034 | Carvana (margins far above the industry absorb a downturn; used cars more stable than thought; technology in its direction) | Rbuy2 support |
| **[v1.1]** SOS1-C026, SOS1-C028, SOS1-C029, SOS1-C030 | Carvana risks rejected (cheap-EV stranded inventory; shared self-driving fleets add dead-head miles; cost per mile varies; people like to own things) | none (views) |
| **[v1.1]** SOS1-C014, SOS1-C015, SOS1-C021, SOS1-C019 | Carvana (beats with mixed stock reactions; data make "crazy" moves easier to live with; worrying about the stock is wasted energy; "never been a better investment" risk-adjusted, May 2025) | Rsize3 support |
| SOS3-C046 | CarMax, car dealerships (studied while waiting) | Rprocess7 |
| SOS3-C073, SOS3-C076 | Carvana (loss-making path to profit; survived on large margins) | Ravoid2 lesson |
| SOS3-C075 | Carvana (lesson against narrower advantages) | Ravoid1 lesson |
| SOS2-C001, SOS3-C064, SOS3-C066, SOS3-C067, SOS3-C070, SOS3-C071 | Carvana (mid-40s% in 2020; added at 80 in 2022; half now, half on a visible turn; poison pill at 5% stopped buying) | Rsize2 (open) |
| **[v1.1]** SOS1-C017, SOS1-C057 | Carvana ("I couldn't buy more" on the way up; never so much in one stock) | Rsize2 (open) |
| **[v1.1]** SOS1-C033 | Berkshire Hathaway long-term holders (did not diversify once over 30%) | Rsell4 |
| **[v1.1]** SOS1-C031 | Stanford selling Google around its IPO (sell decision as serious as the buy) | Rsell1, Rsell2 support |
| **[v1.1]** SOS1-C002, SOS1-C003, SOS1-C004, SOS1-C005, SOS1-C006 | prime vs non-prime lending, securitisations (prime = selling disaster insurance; non-prime brings information; false signals; past blowups and complexity keep others out; reached by growing his circle of competence) | Rprocess7, Rbuy4 support; avoid notes only |
| SOS3-C077 | "pencils" (works, but small consumer surplus) | Ravoid1 fails |
| SOS3-C086 | Chinese stock pitched to him | Ravoid3 (last on the list) |
| SOS3-C085 | UK (naivety hard to overcome) | Ravoid3 support |
| SOS3-C089 | Google 2010 (looked cheap; passed, holdings did better) | Rbuy6 |
| SOS3-C061 | Capital One (former employees impress) | Rprocess5 |
| SOS2-C040 | retailers (sensitive to who runs them) | Rbuy5 |
| SOS2-C030, SOS2-C034 | Boeing, Starbucks (leader fit; organisation sets what it can do) | Rprocess4 support |
| SOS3-C082 | Medicaid managed care (AI for document-heavy sectors, note) | Rprocess8 |
| **[v1.1]** SOS1-C054 | life science and biotech (more approachable with AI tools) | Rprocess8 |
| SOS3-C044 | oil companies (shunning does not make them very cheap) | Rprice1 support |
| **[v1.1]** SOS1-C001 | stopped public podcasts: followers make buying and selling harder | none (process principle, no rule) |

## 6. Gaps (what a screen needs that he does not state)

- Valuation: no earnings-yield, multiple, growth or discount-rate threshold (Rprice1, SOS3-C033 calls them "pretty
  trivial calculations" but gives none). Cardlytics figures (SOS2-C049) and **[v1.1]** the Carvana per-car sum
  (SOS1-C020) are cases, not rules; **[v1.1]** margin of safety named (SOS1-C044) with no size.
- Advantage: no measure for "enduring", "layered" or wide; return on capital and margins are named only as the outcome
  (SOS3-C019), with no number; Carvana's ~10.5% vs dealers' ~4.5% EBITDA margin (SOS3-C051) and 13-14% vs 5% (SOS3-C076)
  are anecdotes; **[v1.1]** "margin vs industry" (SOS1-C022) is a proxy with no threshold.
- Doubt: no measure or threshold; short interest is a proxy he does not screen on (Rbuy4 vs Rprocess2).
- Management: no computable measure; founder or insider control "isn't necessarily an absolute requirement" (SOS2-C035).
- Contained / simple-but-missed business (Rbuy3): no measure.
- Loss-makers: size of the haircut not stated (Ravoid2).
- Universe: no market-cap, liquidity or sector limits stated; only US first (Ravoid3); no ethical screen beyond law
  (SOS3-C040, not a verified rule). **[v1.1]** Sector cautions in SOS1 (prime lending SOS1-C002, subprime false signals
  SOS1-C004, low-growth multi-level marketers SOS1-C037, chemicals SOS1-C045) are principles, not exclusion rules.
- Size: no position cap amount (Rsize2), no starting or maximum weight; staged entry "I'll buy half now and I'll buy half when I can see it turn" is one
  example (SOS3-C067); anecdotal weights 30% (SOS2-C002) and mid-40s% (SOS2-C001) -> recipe uses the 13F. **[v1.1]**
  Rsize3 (add on falls when data say fine, SOS1-C016) gives no size of fall, no amount and no data test; it needs his own
  data (Rprocess6), so a screen can only approximate it (e.g. a 13F addition after a price fall: convention, tagged).
- Sell: no price, valuation or loss trigger; only "upgrade", "misunderstood" and model failure (Rsell1-Rsell2) and
  turnover of about one a year (Rsell3); holding horizon only as "forever" premise and 3-10-year feedback loops
  (SOS3-C006). **[v1.1]** Growth re-basing (SOS1-C038) has no threshold; a named thesis-breaker (SOS1-C040) is
  qualitative.
- Downside test by inversion (SOS2-C055) and **[v1.1]** stress tests (SOS1-C024, SOS1-C025, SOS1-C027) are examples, not
  verified rules: no measure.

## 7. What v1.1 changed (against v1)

- Matched and merged: SOS1-C055 both -> Rprocess1; SOS1-C013 both -> Rprocess6 (narrowed: validate the broad hypothesis,
  not weekly moves); SOS1-C056 both, SOS1-C006 third -> Rprocess7.
- New rules: Rsize3 (add on falls when data say the business is fine; SOS1-C016 third), Rprocess10 (open-ended call
  technique, follow-ups after, also for management; SOS1-C047, SOS1-C049, SOS1-C051 both), Rprocess11 (expert-call
  transcripts, quality mixed; SOS1-C052 both).
- Narrowed or widened: Rsell1 ("only" now includes Rsell2; valuation sales an earlier practice), Rsell2 (scope widened on
  example claims SOS1-C036, SOS1-C038, SOS1-C039, SOS1-C040, SOS1-C042), Rsell4 (no trimming of winners by rule;
  SOS1-C032, SOS1-C033), Rprice1 (margin of safety; SOS1-C044), Rbuy2 (margin vs industry; SOS1-C022), Rprocess3 (stress
  test examples), Rprocess8 (biotech note; SOS1-C054).
- Contradictions: Herbalife named-risk sale (SOS1-C039) CLOSED as different scope via Rsell2 (on example claims only);
  early-career valuation sales (SOS1-C043) CLOSED as dated change of view (later wins; year open; inferred, not stated by
  him). Position cap (Rsize2) still OPEN.

## Count

Rules per part: buy 6, price 2, avoid 3, sell 4, size 3, process 11 (total 29; v1: 26).
Open contradictions: 1 (position cap Rsize2 vs the Carvana / Herbalife weights and the 2022 add; SOS1 adds weight but no
amount); plus the date (not the direction) of the management change and the year of the early valuation sales are
open. Closed in v1.1: 2 (Herbalife named-risk sale, early-career valuation sales). Tension noted, not a contradiction:
Rprocess5 (meetings tell little) vs Rprocess10 (technique works for management teams).
No held-out document remains: v1.1 is untested on unseen material.
