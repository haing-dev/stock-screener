v1.1 = v1 + K174 merged after a FAILED held-out test (A13 items 7-8)

# Investor card: Dev Kantesaria (Valley Forge Capital), gate G4 (v1.1)

Input v1: `claims_for_card.json` only (433 claims; 175 verified rules = 169 `both` + 6 `third`) from four documents:
K065 = 2021-10-22, K105 = 2022-10-27, K189 = 2024-11-20, K290 = 2024-12-05.
Input added in v1.1: `claims_K174.json` (28 claims; 8 verified rules = 6 `both` + 2 `third`) from the held-out
document K174 = 2023-05-29 (FICO breakdown), and `heldout_result.json` (5 of 8 K174 rules matched, 3 open
contradictions in the buy part). After this merge K174 is no longer held out.

### Changes in v1.1
- Merged into existing rules: K174-C001 -> RB1; K174-C007 -> RB13; K174-C010 -> RB14 and RA11; K174-C014 -> RB7,
  RB8; K174-C026 -> RP8; K174-C023 -> RO4. Support added (rule_status no): RB9, RB11, RB16, RO9 (ids in the tables).
- New rules: RB22 (dominant business at an inflection in pricing or growth; one case, K174 only), RP10 (no sum of the
  parts, K174-C019), RA15 (no coerced use, avoid form of RB8, K174-C013).
- Narrowed, not deleted: RB6 (the extrapolated record is the record of dominance; an observed change in the growth
  profile is RB22), RB10 (the decade-plus record of price rises is the usual test, not required under RB22).
- Held-out contradictions closed as different scope: C17 (K174-C003 vs RB10), C18 (K174-C005 vs RB10), C19
  (K174-C024 vs RB6). New note C20 (FICO: neglect vs scare). Section 4 has the readings.

Every statement cites claim ids. Text marked "(reader note)" comes from a claim's `note` field, not from the quote.
Rule ids: RB buy, RP price, RA avoid, RS sell, RZ size, RO process (RO13-RO16 are claims tagged part `other`).
Status codes after each id in the rule tables: b = both, t = third; ids after "support:" are principles, examples or
views (rule_status no) and only support the rule.

## 1. What he buys and why (in his terms)

He holds that there is "only one universal truth": buy "really high-quality businesses", "compounding machines" that
compound intrinsic value "year after year for many years" (K065-C002, K105-C003, K065-C003). His "first screen is
business quality", defined as "the perfect intersection between growth and predictability" (K189-C019, K290-C011), and
he will give up growth for predictability but never "trade reliability" (K105-C013, K290-C018). Such businesses are
natural monopolies, duopolies or oligopolies whose customers use the product because it is to their net benefit
(K065-C060, K105-C031, K105-C071), have already shown excellence for "10, 20, 30, 50 years" (K105-C021), sell a cheap,
essential, must-have product (K105-C103, K105-C104, K290-C056) with pricing power above inflation (K105-C096, K290-C055)
in an industry with rising volumes (K065-C042, K105-C032), are capital light with rising margins (K105-C036,
K105-C034), and allocate capital well, preferably by buying back stock (K105-C040, K290-C087). His "fishing pond" is
about 50 such companies in the world (K105-C017, K189-C018), from which he owns "8 to 12 of the best" (K105-C018,
K290-C024). He values them by discounted free cash flow after the cost of stock compensation (K065-C090, K065-C074),
rank-orders them by the free cash flow yield each deserves for its growth and predictability against the 10-year
Treasury (K065-C092, K065-C093, K105-C154, K105-C155), and buys at a margin of safety, "generally 30 to 60% below what
we think they're worth" (K065-C025, K065-C052), usually when the market neglects the company (two thirds of entries)
or when a regulatory, legal or competitive scare has knocked the stock down (one third) (K189-C014, K290-C021,
K290-C022); near-term volatility "gives us the opportunity to buy into great businesses" (K174-C026). In 2023 he
listed the elements of an ideal business: "dominant Market position tremendous pricing power provides great value for
the price of its product long runway for pricing power operating leverage not a lot in the way of reinvestment a
natural networking effect" (K174-C021). The FICO case adds a second way in: a business long known to be dominant whose
growth profile changes, when "many others in the marketplace may not have realized" it (K174-C024, K174-C003,
K174-C023). He avoids healthcare, high R&D risk, commodity and interest-rate exposure, capital intensity, leverage,
poor capital allocation, dual-class control and acquisition-led growth (K065-C034, K065-C036, K065-C037, K065-C038,
K065-C039, K065-C084, K065-C045, K290-C080), and sells rarely: on a change in business quality, misuse of cash,
excessive leverage, or to switch into something better (K065-C081, K065-C082, K065-C083, K065-C085).

## 2. Rules by part

Columns: id | statement in plain words | measure (computable tag) | number and direction as he states it | strength |
claim ids | dates said.

### Buy (22 rules)

| id | statement | measure | number / direction | strength | claim ids | dates said |
|---|---|---|---|---|---|---|
| RB1 | Buy only "really high-quality businesses", "compounding machines" that compound intrinsic value year after year for many years; the bar for business quality is "exceedingly high". | business quality (proxy) | none stated | always | K065-C002 b, K105-C003 b, K105-C019 b, K174-C001 b; support: K065-C003, K105-C058, K105-C119, K174-C020, K174-C021 | 2021-10-22, 2022-10-27, 2023-05-29 |
| RB2 | Business quality is defined as "the perfect intersection between growth and predictability": high growth that is also very predictable. | organic growth + predictability (proxy) | none stated | always | K189-C019 b, K189-C021 b, K290-C011 b, K290-C013 t, K105-C014 b | 2022-10-27, 2024-11-20, 2024-12-05 |
| RB3 | Predictability is never sacrificed: "happy to give up some growth in exchange for predictability"; "never willing to trade reliability"; a company whose next earnings release worries you should not be owned. | earnings predictability (proxy) | none stated | always | K290-C018 b, K105-C013 b, K105-C167 t (avoid form); support: K290-C012 | 2022-10-27, 2024-12-05 |
| RB4 | "A very strong topline and bottom line organic growth profile"; a very predictable path to organic growth and higher free cash flow over five to ten years. | organic revenue and earnings growth (yes); FCF growth (proxy) | per company: none stated; horizon "five to 10 year" | always | K105-C097 b, K065-C035 b, K105-C014 b; support: K105-C059, K065-C026 | 2021-10-22, 2022-10-27 |
| RB5 | Portfolio-level growth target: the weighted portfolio should grow "in high teens", some holdings "low 20s", predictably over the next decade. | FCF per share growth (K065) / weighted organic growth (K290) (proxy) | high teens to low 20s per year, portfolio weighted average (>=) | usually | K065-C051 b, K290-C015 b | 2021-10-22, 2024-12-05 |
| RB6 | A long record that is extrapolated, not a predicted step change: great business quality "for the last 10, 20, 30, 50 years"; business models "around for decades"; businesses that "don't change a lot". Scope (v1.1): the record extrapolated is the record of dominance and business quality; it does not bar acting on a change in the growth profile that is already "happening" on a business whose "dominant position" was known for a long time (K174-C024, K174-C023): that case is RB22 (see C19). | length of record of quality / dominance (proxy) | 10, 20, 30, 50 years; "decades" (>=) | always (K290-C020: usually, not every holding) | K105-C021 b, K105-C022 b, K189-C068 b, K290-C020 b, K105-C083 b; support (scope): K174-C023, K174-C024 | 2022-10-27, 2024-11-20, 2024-12-05 |
| RB7 | Dominant businesses (monopoly, duopoly, oligopoly) "not subject to significant disruption", in industries whose dynamics are stable; must stay dominant "for at least the next 10 years" or it fails the predictability bar. | market position; durability of dominance (proxy) | dominance for at least the next 10 years (>=) | always | K290-C002 b, K105-C031 b, K065-C041 b, K189-C022 b, K290-C017 b, K174-C014 t; support: K105-C070, K065-C004 | 2021-10-22, 2022-10-27, 2023-05-29, 2024-11-20, 2024-12-05 |
| RB8 | The dominance must be "natural": customers are not forced "through twisting arms or contractual arrangements"; it is to their net benefit to use the product ("we believe in what we call Natural monopolies or oligopolies"). Avoid form: RA15. | customer benefit vs lock-in (proxy) | none stated | always | K105-C071 b, K065-C060 b, K174-C014 t; support: K174-C015, K174-C017 | 2021-10-22, 2022-10-27, 2023-05-29 |
| RB9 | The advantage should come from industry dynamics stable "for many decades" or a technology lead, rather than scale (see RA13). In the FICO case the protection named is the network effect, not the product itself: "two kids in a dorm room at MIT could come up with an equivalent mathematical model ... what matters is the networking effect". | form of competitive advantage (proxy) | none stated | usually | K189-C025 b; support: K189-C023, K174-C018, K174-C021 | 2024-11-20 (support 2023-05-29) |
| RB10 | Pricing power over long periods ("a strong focus", "a hallmark"): raise prices above inflation, a pattern that has played out for a long time, not a sudden change. Scope (v1.1): the decade-plus record of price rises is the test for the usual holding (RB6 case); it is not required under RB22, where pricing power had gone unused (FICO "had not increased the prices of its scores for 25 years" before 2016) and is shown instead by a product priced far below the value it delivers and a "long runway for pricing power" (K174-C005, K174-C004, K174-C016, K174-C021; see C17, C18). | price increases vs inflation (proxy) | "a few percent above the rate of inflation for a decade plus preferably 20 or 30 years"; at 10% inflation, 13-14% price rises (>=); 10% vs 2% given as illustration; not applied under RB22 | always / usually (usual-holding scope) | K105-C096 b, K105-C102 b, K290-C055 b, K189-C048 b, K189-C046 b, K065-C010 b, K065-C041 b, K105-C103 b; support: K105-C033, K189-C047, K065-C061; support (scope): K174-C005, K174-C016 | 2021-10-22, 2022-10-27, 2024-11-20, 2024-12-05 |
| RB11 | The product is cheap and essential, a "must-have": low in price relative to what it does, customers "may gripe about it" but keep using it. FICO: "scores are extremely cheap relative to the loan sizes". | low-priced essential product; price relative to the value of the decision it supports (proxy) | none stated (10% vs 2% inflation is an illustration, K105-C103) | always / usually | K105-C104 b, K105-C103 b, K290-C056 b, K065-C040 b; support: K189-C056, K174-C004, K174-C016 | 2021-10-22, 2022-10-27, 2024-12-05 (support 2023-05-29) |
| RB12 | The industry's volumes go up significantly over time: strong secular trends, strong volume growth (with pricing growth on top). | industry volume growth (proxy) | none stated | always / usually | K105-C032 b, K065-C042 b; support: K105-C060, K105-C144 | 2021-10-22, 2022-10-27 |
| RB13 | Operating leverage: "margins go up over time", with room to grow margins even at 50-100 billion market caps; businesses "that still have a tremendous amount of operating leverage". | operating margin trend (yes); margin expansion potential (proxy) | direction up; no number | always / usually | K105-C034 b, K105-C035 b, K174-C007 b; support: K065-C004, K174-C006 | 2022-10-27, 2023-05-29 |
| RB14 | Capital light: high return on tangible assets, very low capital expenditure, little reinvestment, "preferably zero" (he says that is not reality); a business that "does not have to reinvest heavily in the business to keep it going". Mirror of RA5. | return on tangible assets; capex intensity; reinvestment rate (yes / proxy) | reinvestment "preferably zero" (<=), no cut-off for the others; FICO example: capex "less than 10 million dollars" in two fiscal years at a market cap "approaching 20 billion dollars" (K174-C009) | always / usually | K105-C036 b, K065-C009 b, K290-C053 b, K290-C085 b, K174-C010 b; support: K174-C008, K174-C009 | 2021-10-22, 2022-10-27, 2023-05-29, 2024-12-05 |
| RB15 | Capital allocation is "the final piece": once the money is earned, is it used wisely? Management matters mainly on capital allocation, not execution. | capital allocation (proxy) | none stated | always | K105-C040 b, K105-C109 b; support: K290-C086 | 2022-10-27 |
| RB16 | Preference for heavy buybacks: "we love it when a great compounding machine buys back a lot of their stock". | share repurchases (yes) | "a lot"; no number | usually | K290-C087 b; support: K290-C086, K290-C073, K105-C063, K174-C011, K174-C012 | 2024-12-05 (support 2023-05-29: FICO used "all of their free cash flow essentially to buy back a tremendous amount of stock"; share count down 20% in five years and 25% in ten per reader note K174-C012) |
| RB17 | Preference for a company that "holds virtually no cash because it keeps them from making mistakes". | cash held by company (yes) | "virtually no cash" (<=); no number | usually | K290-C088 b | 2024-12-05 |
| RB18 | Businesses "your idiot nephew could run"; not ones that need Steve Jobs or Warren Buffett. | dependence on exceptional management (proxy) | none stated | always | K105-C107 b, K105-C108 b (avoid form); support: K065-C071 | 2022-10-27 |
| RB19 | Many different levers to pull to reach financial targets (pricing, volumes, flexible costs). | number of levers (proxy) | none stated | usually | K105-C072 b; support: K065-C097 | 2022-10-27 |
| RB20 | Universe: "very US-centric", outside the US "only opportunistically"; generally large US caps ("at least mid-cap, but usually large-cap"), because dominant businesses tend to be large. | US listing (yes); market cap (yes) | at least mid-cap, usually large-cap; no dollar figure (50-100 billion describes holdings, K105-C035) | usually | K105-C047 b, K290-C017 b, K065-C076 b, K290-C076 b; support: K290-C077, K290-C078 | 2021-10-22, 2022-10-27, 2024-12-05 |
| RB21 | Volume cyclicality is tolerated when the drop is temporary, because the focus is long-term earnings power (and it gives a chance to buy more, RP9). | temporary vs structural volume drop (proxy) | none stated | usually | K290-C071 b, K290-C074 b; support: K290-C073 | 2024-12-05 |
| RB22 | (new in v1.1) A business long known to be dominant can be bought at an inflection in pricing or growth that is already happening and that "many others in the marketplace may not have realized". FICO: "we were following this company for a long time knew of its dominant position"; growth "was completely related to volume" in the early years, "but that changed in 2018 which got us interested"; "we were worried about its organic growth profile and then we realized that there was a change happening". The pricing power was latent: no price rises "for 25 years" before 2016, yet the score is "so cheap relative to the loan decisions being made" that there is "a tremendous runway for pricing power". RB7, RB8, RB13, RB14 still apply (K174-C021 lists them for FICO); RB6 and RB10 apply only in their narrowed scope. | change in organic growth (price-driven vs volume-only) on a long-dominant business; start of price increases after a long pause; product price vs value delivered (proxy) | none stated; case values: no price rises in the 25 years before 2016 (K174-C005), growth profile changed in 2018 (K174-C003) | sometimes (one case) | no verified rule claim states it in general; support: K174-C003, K174-C024, K174-C002, K174-C005, K174-C016, K174-C004, K174-C021, K174-C023 t (process rule, the dominance was known first), K174-C025 | 2023-05-29 |

### Price (10 rules)

| id | statement | measure | number / direction | strength | claim ids | dates said |
|---|---|---|---|---|---|---|
| RP1 | Value is "all about discounted cash flow" of free cash flow; the edge is in the discount rate, set by assessing future risk. | DCF of free cash flow (proxy) | none stated (no discount rate given) | always | K065-C090 b; support: K065-C091, K105-C010, K065-C001 | 2021-10-22 |
| RP2 | Free cash flow is measured after the cost of buying back the stock issued as compensation. | FCF after stock compensation (yes) | none stated | always | K065-C074 b, K065-C075 b, K105-C042 b; support: K065-C073 | 2021-10-22, 2022-10-27 |
| RP3 | Free cash flow is modelled "very conservatively"; optionality is liked subjectively but never added to the base case or expectations. | FCF model without optionality (no) | none stated | always | K105-C145 b, K105-C146 b | 2022-10-27 |
| RP4 | Rank-order businesses by the forward free cash flow yield he is willing to pay (years 2021-2023 named in 2021); the yield a company deserves is set by its business quality (growth and predictability) and by the risk-free rate. | forward FCF yield (yes); required yield by quality rank (proxy) | forward years: the next three calendar years as said in 2021; required yield per quality: none stated | always / usually | K065-C092 b, K105-C153 b, K105-C154 b, K105-C155 b | 2021-10-22, 2022-10-27 |
| RP5 | Compare the ranked set with the 10-year US Treasury (the risk-free proxy): want "a large gap with the risk-free rate" and the most promising gap between today's FCF yield and the yield the company should trade at. | FCF yield minus 10-year Treasury yield (yes); gap to required yield (proxy) | gap direction: larger is better; no number (reader note K065-C094: "No numeric gap stated") | usually | K065-C093 b, K065-C094 b, K105-C155 b | 2021-10-22, 2022-10-27 |
| RP6 | Margin of safety on entry: initial purchases "at a significant discount, generally 30 to 60% below what we think they're worth", at a price "that compensates for things that could go wrong". | discount to intrinsic value (proxy) | 30 to 60% below intrinsic value at initial purchase (between) | always / usually | K065-C052 b, K065-C025 b, K105-C150 b; support: K105-C156 | 2021-10-22, 2022-10-27 |
| RP7 | A fixed buy price set in advance: "we know at any given moment what price we want to buy our favorite companies at"; "a specific line in the sand for buying and selling", accepting that some names are missed. | pre-set buy price (no) | none stated | always / usually | K065-C020 b, K105-C050 t; support: K105-C049, K105-C052 | 2021-10-22, 2022-10-27 |
| RP8 | Entry on a scare (about one third of entries): the stock "significantly dropped" on a regulatory, legal, legislative or competitive issue or a bad earnings release that he judges misunderstood or overblown; act quickly on a sudden drop in a long-followed stock. "near-term share price volatility doesn't bother us at all it actually gives us the opportunity to buy into great businesses"; "the more volatility ... the better for long-term investors like us". | drawdown from high (proxy) | down "40%, 50%" (K189-C013); a sudden 40% drop (K065-C013); share of entries "onethird" | sometimes / usually (volatility as opportunity: always, K174-C026) | K290-C021 b, K189-C013 b, K189-C061 b, K105-C039 b, K105-C082 b, K065-C013 b, K174-C026 b; support: K174-C027, K174-C028 | 2021-10-22, 2022-10-27, 2023-05-29, 2024-11-20, 2024-12-05 |
| RP9 | Entry on market neglect (about two thirds of entries): the company is "sitting there in plain sight, no one is paying attention"; a temporary volume drop is also a chance to buy more. | market neglect (proxy) | share of entries "two thirds"; no measure of neglect stated | usually | K189-C014 b, K290-C022 b, K290-C072 b; support: K065-C014 | 2024-11-20, 2024-12-05 |
| RP10 | (new in v1.1) No sum-of-the-parts valuation: "arguably today based on its growth profile we don't really believe in some of the parts at our firm" (reader note: does not value companies by sum of the parts; "some of the parts" read as a transcription of "sum of the parts"). Said in the FICO discussion, which also notes that its "software business has margins uh far lower than the scores business" (K174-C006); the claims do not say the two statements are linked. | valuation method (no) | none stated | usually | K174-C019 b; support: K174-C006 | 2023-05-29 |

### Avoid (15 rules)

| id | statement | measure | number / direction | strength | claim ids | dates said |
|---|---|---|---|---|---|---|
| RA1 | No healthcare: "no pharmaceuticals ... no biotech ... no medical devices ... no hospitals ... no healthcare IT"; biotech and drug development "inherently lack the predictability that we need" (products can be pulled for side effects). | sector (yes) | excluded | always | K065-C034 b, K105-C075 b, K105-C076 b, K290-C067 b; support: K105-C077 | 2021-10-22, 2022-10-27, 2024-12-05 |
| RA2 | High R&D risk and large upfront investment with unknown return: biotech, pharma, medical devices, "hardware technology", "minerals"; e.g. "invest a billion dollars to find the next blockbuster drug". | R&D intensity / outcome risk (proxy) | excluded; no number | always | K065-C036 b, K105-C037 b, K065-C037 b | 2021-10-22, 2022-10-27 |
| RA3 | Companies "whose prospects are tied to commodity prices". | commodity price exposure (proxy) | excluded | always | K065-C037 b; support: K065-C006, K105-C064 | 2021-10-22 |
| RA4 | Companies "whose fortunes are tied to where interest rates will be". | interest-rate sensitivity (proxy) | excluded | always | K065-C038 b | 2021-10-22 |
| RA5 | "Highly capital intensive" businesses. Mirror of RB14. | capital intensity (yes) | excluded at "highly"; no cut-off | always | K065-C039 b; support: K189-C024, K290-C058 | 2021-10-22 |
| RA6 | No buying "a low-quality business and fixing it up" (no activism, no turnarounds). | business quality (proxy) | excluded | always | K065-C070 b; support: K105-C056, K105-C057 | 2021-10-22 |
| RA7 | No leverage at the company level. | net debt to EBITDA (yes) | direction: low; no number | usually | K065-C084 b | 2021-10-22 |
| RA8 | Dual-class structures "where the CEO is anointed for life"; CEOs with many pet projects. | dual-class share structure (proxy) | excluded | usually | K065-C045 b, K189-C071 b; support: K290-C047 | 2021-10-22, 2024-11-20 |
| RA9 | Poor capital allocation and excessive compensation: "issuing too much compensation", "using free cash flow in a poor way". | stock compensation; use of cash (proxy) | none stated | usually | K105-C110 b, K065-C044 b; support: K065-C073 | 2021-10-22, 2022-10-27 |
| RA10 | Big technology (FANG) avoided over 17 years, for capital allocation, dual class and pet projects (and, 2024, for unpredictable AI monetisation). Amazon is a stated exception (see section 4, C4). | sector / named group (no) | excluded "over our 17 years" | usually | K189-C070 b, K189-C071 b, K065-C044 b; support: K189-C073, K189-C074 | 2021-10-22, 2024-11-20 |
| RA11 | Growth by acquisition: no companies "that need acquisitions as part of their long-term strategies" (e.g. buying five companies a year); defensive acquisitions are penalised; acceptable deals are "offensive" with "serious cost and revenue synergies that go out 10 plus year". | reliance on acquisitions; acquisition type (proxy) | synergies 10+ years (>=); "five companies every year" is an example | always / usually | K290-C080 b, K105-C041 b, K290-C081 b, K105-C100 t, K174-C010 b ("does not have to make defensive Acquisitions"); support: K105-C099, K290-C083 | 2022-10-27, 2023-05-29, 2024-12-05 |
| RA12 | One negative factor can make a company "uninvestable" even if all the other boxes (pricing power, volume growth, capital intensity, margin expansion) are checked. | single disqualifying factor (proxy) | "one or two factors" | usually | K105-C098 b, K105-C101 b | 2022-10-27 |
| RA13 | None of the ~50 pond companies wins "through size advantage or volume advantage" (scale-based models). | scale-based advantage (proxy) | excluded | always | K105-C105 b; support: K189-C024, K105-C106 | 2022-10-27 |
| RA14 | Nothing "that could go down 90% tomorrow"; such businesses are "not our fishing pond". | risk of permanent loss (proxy) | a possible 90% fall (excluded); no measure stated | always | K290-C019 b; support: K065-C043, K105-C162 | 2024-12-05 |
| RA15 | (new in v1.1) No businesses where users must be forced to use the product: "we don't invest in businesses where you have to twist somebody's Farm to use the product or service" ("Farm" read as "arm", as in "twisting arms", K105-C071). Mirror of RB8. FICO passes: "you're not forcing anybody to use the score everyone can go out tomorrow and use Vantage score". | coerced vs voluntary use (proxy) | excluded | always | K174-C013 b; support: K174-C015, K174-C017; buy form: K105-C071, K065-C060 (RB8) | 2023-05-29 |

(Two avoid-form claims are merged into buy rules: K105-C108 into RB18, K105-C167 into RB3. In v1.1 the avoid-form
claim K174-C013 gets its own rule RA15 because the held-out test found no avoid rule for it. The price-side reading of RA6, "never sacrifice business quality for valuation", is supported by K105-C056, K105-C057, K105-C058, K290-C045, K065-C007.)

### Sell (7 rules)

| id | statement | measure | number / direction | strength | claim ids | dates said |
|---|---|---|---|---|---|---|
| RS1 | When a holding "reaches 100% of our intrinsic value we have to justify why they are still in the portfolio" (a review, not an automatic sale). | price / intrinsic value (proxy) | 100% (>=) triggers review | usually | K065-C079 b | 2021-10-22 |
| RS2 | Holdings compete against the shortlist; "the easiest decision for exiting a company is when we find something that we like better", which is how most things leave; volatility can allow trading a lower-quality name for a higher-quality one. | relative attractiveness (no / proxy) | none stated | usually / sometimes | K065-C085 b, K065-C080 b, K105-C131 t; support: K105-C134 | 2021-10-22, 2022-10-27 |
| RS3 | Sell on a change in business quality or risk from something new, or a competitive dynamic; names also leave the pond on a change in business quality. | change in business quality (proxy) | none stated | usually | K065-C081 b, K105-C020 b, K290-C061 b; support: K290-C023 | 2021-10-22, 2022-10-27, 2024-12-05 |
| RS4 | Sell on misuse of free cash flow or bad capital allocation; "capital allocation is absolutely something that can ruin a great business". | capital allocation (proxy) | none stated | usually | K065-C082 b, K290-C082 t; support: K290-C084 | 2021-10-22, 2024-12-05 |
| RS5 | Sell if the company "takes on excessive leverage". | leverage (yes) | "excessive"; no number | usually | K065-C083 b | 2021-10-22 |
| RS6 | Do not sell a compounding machine because its P/E "moved from 26 to 29". | P/E change (no) | a move from 26 to 29 is not a reason (example) | usually | K290-C049 b | 2024-12-05 |
| RS7 | Sell rarely: low turnover is the natural result of wanting quality and sustainability "for the next 10 years, 20 years, 30 years". | turnover (no) | holding horizon 10-30 years | usually | K065-C086 b, K105-C004 b; support: K105-C133, K105-C132, K065-C027, K290-C063 | 2021-10-22, 2022-10-27 |

### Size (5 rules)

| id | statement | measure | number / direction | strength | claim ids | dates said |
|---|---|---|---|---|---|---|
| RZ1 | Own "our 8 to 12 best ideas"; "just a range ... not a hard number". | number of holdings (no) | 8 to 12 (between) | always / usually | K290-C024 b, K105-C018 b, K105-C158 b, K189-C015 b; support: K105-C132 (10 holdings) | 2022-10-27, 2024-11-20, 2024-12-05 |
| RZ2 | Upper limit: "no problem owning 14"; "mid-teens is probably as high as you'll ever see"; "reluctant to invest in our 17th best idea". | number of holdings (no) | <= mid-teens; 14 acceptable; 17th idea rejected | usually / sometimes | K105-C161 b, K105-C159 b, K105-C055 b; support: K105-C160, K290-C025 | 2022-10-27 |
| RZ3 | Concentrate: "we make few decisions, but when we make them, they're big"; concentrate on the ones "far stronger than others". | position weight (no) | none stated | usually | K189-C004 b, K189-C017 b; support: K189-C003, K105-C162; contrast K189-C016 (see C9) | 2024-11-20 |
| RZ4 | Scale in and add over time when the market is not properly assessing intrinsic value: buy at "many different intervals", "another 13, 14, 15 times along the way". | number of additions (no) | 13, 14, 15 further purchases (example of a long holding) | usually / sometimes | K065-C054 b, K189-C005 b; support: K065-C053, K065-C030 | 2021-10-22, 2024-11-20 |
| RZ5 | Cash near zero: "around 1% ... probably 0% to 5% in the future". | fund cash level (no) | 0% to 5% (between) | sometimes | K189-C036 b; support: K105-C123 (<1% in 2022), K189-C035, K189-C037 | 2024-11-20 |

### Process (16 rules)

| id | statement | measure | number / direction | strength | claim ids | dates said |
|---|---|---|---|---|---|---|
| RO1 | Research is reading: "95% of the time we are reading 10-Ks, 10-Qs"; "no rote way to screen for these types of companies"; he does the primary work himself, no "army of analysts". | none | 95% of time reading | always / usually | K065-C012 b, K105-C038 b, K065-C016 b, K105-C084 b, K189-C001 b; support: K065-C008, K105-C094, K105-C095 | 2021-10-22, 2022-10-27, 2024-11-20 |
| RO2 | Look at hundreds of companies to find "one to three great ideas a year"; find "a few instances every year, every few years where there is a disconnect". | ideas per year (no) | 1 to 3 a year (between); "every year, every few years" (2024) | usually | K065-C018 b, K189-C006 b | 2021-10-22, 2024-11-20 |
| RO3 | Keep a shortlist ("fishing pond") of about 50 companies with very little turnover; add "a couple" of names a year (2022) / every few years (2024); five to seven of them foreign. | size of shortlist (no) | "50 or so" (2022), "40 to 50" (2024-11), "50 or 60" (2024-12) | always / usually | K105-C017 b, K105-C054 b, K105-C019 b, K189-C018 b, K189-C069 b, K290-C076 b, K105-C020 b | 2022-10-27, 2024-11-20, 2024-12-05 |
| RO4 | Follow a company for years before buying ("seven years, 10 years"; a monitoring phase of earnings releases, filings, analyst days), occasionally months for a short-term opportunity; "we like to be great historians of companies". | years followed (no) | 7 to 10 years usual; months "sometimes" | usually / sometimes | K105-C078 b, K105-C081 b, K065-C013 b, K105-C079 b, K174-C023 t; support: K105-C080, K174-C001 | 2021-10-22, 2022-10-27, 2023-05-29 |
| RO5 | Keep a view of intrinsic value "every day for every company" in the portfolio and on the shortlist; update intrinsic values at every quarterly earnings; think daily about "subtle changes to business quality both up or down". | none | quarterly update; daily view | always / usually | K065-C078 b, K065-C019 b, K290-C061 b, K290-C065 b | 2021-10-22, 2024-12-05 |
| RO6 | Long horizon: no short-term trading; focus on earnings power "five years out ... and 10 years out", "10 plus years", "10, 20 year time frames"; "as if the stock market were closed for 10 years". | horizon (no) | 5 to 10 years (K290-C016); 10+ years (K290-C048, K189-C011); 10-20 years (K189-C038) | always | K105-C002 b, K105-C008 b, K105-C061 b, K189-C011 b, K189-C038 b, K290-C016 b, K290-C048 b | 2022-10-27, 2024-11-20, 2024-12-05 |
| RO7 | Bottom-up only: not picking macro trends or countries; do not spend time on matters that are unpredictable or uncontrollable (no entry timing on rates, elections, Fed). | none | none stated | always | K290-C075 b, K105-C073 b; support: K065-C024, K065-C055, K105-C130, K105-C171, K290-C006 | 2022-10-27, 2024-12-05 |
| RO8 | Judge a year by the underlying earnings of the companies, not by the portfolio's price change. | none | none stated | always | K065-C063 b | 2021-10-22 |
| RO9 | Assimilate a large set of future risk factors and home in on "the two three four things that truly matter for the next 10 or 20 years". | none | 2 to 4 factors | usually | K290-C064 b, K189-C008 b, K105-C012 b; support: K189-C007, K189-C009, K065-C001, K174-C025 ("looking forward in assessing future risk and future growth") | 2022-10-27, 2024-11-20, 2024-12-05 |
| RO10 | Debate decisions inside the firm (and with company management); ask "what is stopping you from investing at this moment"; stay insular, away from New York noise; experts only for what he cannot figure out; raise capital allocation concerns privately. | none | none stated | usually / sometimes | K105-C084 b, K105-C085 b, K105-C088 b, K105-C090 b, K105-C091 b, K105-C089 b, K065-C072 b; support: K105-C087, K105-C114 | 2021-10-22, 2022-10-27 |
| RO11 | Target a win rate of "90% plus of our ideas". | win rate (no) | 90%+ (>=) | always | K105-C149 b; support: K105-C147, K065-C064 | 2022-10-27 |
| RO12 | Put an idea "on the side burner" if there are concerns or it is not easy. | none | none stated | usually | K105-C165 b; support: K105-C163, K105-C166 | 2022-10-27 |
| RO13 | Shorting is rare ("five times in 14 years") and needs "a huge margin of safety". [part other] | none | 5 times in 14 years | usually | K065-C031 b; support: K065-C032 | 2021-10-22 |
| RO14 | Default to common stock; occasionally LEAPS. [part other] | instrument (no) | LEAPS: two situations in 14 years (support) | usually | K065-C088 b; support: K065-C089 | 2021-10-22 |
| RO15 | Deviate from the playbook only if circumstances warrant it, "very carefully" and "with a large margin of safety". [part other] | none | none stated | sometimes | K065-C033 b | 2021-10-22 |
| RO16 | Public equities preferred over any other asset class on risk-reward. [part other] | asset class (no) | none stated | always | K189-C030 b; support: K189-C027, K189-C029 | 2024-11-20 |


## 3. None stated

Every part has at least one verified rule. What is missing inside parts (the recipe fills these from the 13F or a
convention, tagged):
- Size: no rule for position weights (only 8-12 names, "concentrate", RZ1-RZ3; equal weight at 12 is an unverified
  "ideal", K189-C016) and no maximum position size. -> weights from the 13F or a convention.
- Sell: no price level that forces a sale (RS1 is a review at 100% of intrinsic value), no leverage number (RS5).
  -> holding period / exits from the 13F.
- Price: no required yield per quality rank and no numeric gap to the 10-year Treasury (RP4-RP5; K065-C094 reader
  note). -> convention or grid.
- v1.1: K174 adds no size or sell rule and no number for any of the gaps above (its rules are RB1, RB7, RB8, RB13,
  RB14, RA11, RA15, RP8, RP10, RO4; K174-C001 to K174-C028).

## 4. Changes of view and scope

| # | claims that disagree | reading |
|---|---|---|
| C1 | "fairly open-minded about ... geography" (K065-C040, 2021) vs "always been very US-centric ... outside the US only opportunistically" (K105-C047, 2022), "generally large US cap" (K290-C017), 5-7 foreign names on the shortlist (K290-C076), foreign investments "the most work with the least amount of gain" (K105-C045, K105-C046). | Different scope, both stand: no hard geographic exclusion, US-centric in practice. Not a dated change (K105-C047 says "always"). |
| C2 | "open-minded about market capitalization" (K065-C040) vs "at least mid-cap, but usually large-cap" (K065-C076, same document; reader note: "Result of quality focus, not a stated screen"), K290-C017, K290-C077 (not US small cap). | Different scope: no hard size floor; large size is an outcome. Both stand. |
| C3 | Initial purchases "generally 30 to 60% below what we think they're worth" (K065-C052) vs "even if you're paying a fair price, in the long run ... a much better way" (K065-C007), "no bad time to buy a compounding machine" (K065-C022, K105-C068), intrinsic value growth "overcomes whether you've overpaid by 10 or 15%" (K290-C008, 2024). | OPEN. Partly scope (K065-C052 is about the first purchase; the others are principles about the long run), but K065-C052 and K065-C007/C022 are from the same 2021 document, so it is not a dated change. Whether the 30-60% discount is a requirement or a typical outcome is unresolved. |
| C4 | "We have avoided big technology over our 17 years" (K189-C070, 2024), capital allocation still "our concern on a going forward basis" (K189-C073) vs "it's been a mistake not to own these companies. We do own Amazon" (K065-C046, K065-C047, 2021), "the learning lesson ... these business models were so powerful" (K189-C072), "a big omission was the big tech companies" (K290-C046), Amazon accepted despite capital intensity (K105-C140) as an exception (K105-C143). | Not a change of view: the omission is admitted in 2021 and 2024 but the avoid rule is restated in 2024 (K189-C070, K189-C073, K189-C074). Amazon is a named exception. Both stand. |
| C5 | "stock screens just don't work" (K065-C008), "no rote way to screen" (K105-C038), "no easy way to just have rules around what is investable" (K290-C060) vs "Our first screen is business quality" (K189-C019), "quantitative parameters ... lines that you're not going to cross" (K105-C052), a numeric screen "will reduce the universe" (K065-C011). | Different scope: "screen" in K189-C019 is his judgement filter; numeric screens only narrow the universe. Both stand; it limits how far a mechanical recipe can represent him (see gaps). |
| C6 | "we like offensive acquisitions" (K105-C041) vs "we just don't like companies that need acquisitions as part of their long-term strategies" (K290-C080), serial buying "not a playbook ... that ends well" (K105-C100). K105-C099 reads "we just like businesses that grow by acquisition" next to the Valeant failure (reader note: likely means they do NOT). | Different scope: single offensive deals with long synergies are acceptable (K290-C081); acquisition-dependent growth is not. Both stand. K105-C099 is a likely transcription inversion; not used for a rule. |
| C7 | Shortlist additions "a couple of names a year" (K105-C020, 2022) vs "a couple names to our short list every few years" (K189-C069, 2024); pond size "50 or so" (K105-C017, 2022), "40 to 50" (K189-C018, 2024-11), "50 or 60" (K290-C076, 2024-12); new ideas "one to three ... a year" (K065-C018, 2021) vs "a few instances every year, every few years" (K189-C006, 2024). | OPEN in the numbers (no stated change; figures are approximate). If read as dated, the later (slower) rate wins. |
| C8 | Avoid commodity- and rate-tied companies (K065-C037, K065-C038), cyclicals "will end badly" (K105-C064) vs "that type of cyclicality doesn't bother me" and volume drops are a chance to buy more (K290-C071, K290-C072, K290-C074). | Different scope: commodity-price or rate-driven fortunes are excluded; temporary volume cycles in a quality business are tolerated. Both stand. |
| C9 | Concentrate on the ones "far stronger than others" (K189-C017) vs "if I could find 12 equally good companies and equal weight them ... that would be my ideal" (K189-C016, not a verified rule; same document). | OPEN for sizing: the ideal is equal weight, practice is concentration on the strongest; no weight rule either way. |
| C10 | Cash "as high as 20%" historically, "low single digits" more recently (K065-C023, 2021), "much higher cash positions" in the past (K105-C124) vs lesson that "holding cash is a drag on returns" (K189-C035) and 0-5% going forward (K189-C036, 2024). | Dated change of view: later wins (RZ5, 0-5%). |
| C11 | Reinvestment "preferably zero" (K290-C085) vs "most of the companies that we have do require some reinvestment" (same claim) and Amazon accepted despite capital intensity (K105-C140). | Different scope: a preference, not a cut-off; Amazon is the stated exception. Both stand. |
| C12 | At 100% of intrinsic value "we have to justify" holding (K065-C079, 2021) vs do not sell for a P/E move "from 26 to 29" (K290-C049, 2024), "sometimes the best thing to do is to do nothing" (K105-C133). | Different scope: RS1 is a review trigger, not a sale rule; RS6 says a modest re-rating alone is not a reason. Both stand. |
| C13 | Rank on forward free cash flow yield for 2021-2023 (K065-C092) vs "be careful on forward PE multiples" (K189-C063, K189-C065, K189-C067, K290-C050, K290-C052). | Different scope: his own conservative FCF model (RP3) vs consensus forward P/E, which he says misses price increases (K189-C066, K290-C051). Both stand; a screen must not substitute consensus forward multiples. |
| C14 | Healthcare exclusion lists hospitals and healthcare IT in 2021 (K065-C034) vs later statements naming only pharma, biotech, medical devices, drug development (K105-C075, K290-C067). | OPEN in breadth: K065-C034 describes the portfolio ("It turns out ..."), the later ones give the predictability reason for drug-related areas only. Whether hospitals and healthcare IT are excluded by rule or by outcome is not stated. |
| C15 | "great business quality for the last 10, 20, 30, 50 years" (K105-C021) vs "not true of every company" (K290-C020 reader note) and "quality can get better or worse" (K290-C023). | Different scope: usual, not absolute (RB6 strength "usually" for K290-C020). Both stand. |
| C16 | Optionality not in the base case (K105-C145, K105-C146) vs Amazon held for an expected inflection and "the most optionality" (K105-C141, K105-C142). | Different scope: subjective plus vs model input; Amazon is the stated exception (K105-C143). Both stand. |
| C17 | (held-out, v1.1) Interest in FICO was triggered by a change: growth "was completely related to volume" in the early years, "but that changed in 2018 which got us interested" (K174-C002, K174-C003, 2023-05-29) vs RB10: pricing power as a long-running pattern, "not a sudden change" (K105-C096, K290-C055, K189-C048; 2021-2024). | CLOSED, different scope. Not a dated change of view: RB10 is stated before (2021-10-22, 2022-10-27) and after (2024-11-20, 2024-12-05) K174. The FICO trigger is a change in the growth profile of a business whose dominance he already knew (K174-C023, K174-C024), with the pricing room shown by price vs value (K174-C004, K174-C016). Written as its own buy rule RB22; RB10's long-record test is narrowed to the usual holding. Both stand. |
| C18 | (held-out, v1.1) "prior to 2016 FICO had not increased the prices of its scores for 25 years" (K174-C005), so FICO had no decade-plus record of above-inflation price rises when he became interested in 2018 (K174-C003), vs RB10's number "a few percent above the rate of inflation for a decade plus preferably 20 or 30 years" (K105-C096). | CLOSED, different scope. The claims do not date his first purchase; they date the interest (2018, K174-C003) and the buying chances ("over the last five years", K174-C028). At any of those dates the record of price rises was shorter than RB10's decade. What he cites instead is latent pricing power: "scores are extremely cheap relative to the loan sizes", "a tremendous runway for pricing power that still delivers exceeding value to the end users", "long runway for pricing power" (K174-C004, K174-C016, K174-C021). RB10's number applies to the usual holding, not to RB22. v1 section 5 already lists FICO's later mortgage-score rise under C13 (K189-C066, K290-C051). Both stand. |
| C19 | (held-out, v1.1) "we were worried about its organic growth profile and then we realized that there was a change happening that many others in the marketplace may not have realized" (K174-C024) vs RB6 (v1 wording: a long record that is extrapolated, not a predicted step change; K105-C021, K189-C068, K290-C020). | CLOSED, different scope. What is extrapolated in the FICO case is the record of dominance ("we were following this company for a long time knew of its dominant position", K174-C023; "following Fair Isaac for many years", K174-C001); the change he acts on is one "happening", i.e. observed, not predicted (K174-C024). RB6 is narrowed to the record of dominance and quality; an observed change in growth on such a business is RB22. Not a dated change: RB6 is restated after K174 (2024-11-20, 2024-12-05). C15 (record "not true of every company") stays as it was. Related but separate: Amazon was held for an "expected" inflection as a stated exception (K105-C141, K105-C142, K105-C143; C16); RB22 does not cover a predicted inflection. |
| C20 | (v1.1) FICO bought on market neglect (K290-C022, RP9; v1 section 5) vs "many opportunities to buy the company at depressed levels over the last five years because of some of the items like the fhfa decision or what was happening with synchrony" (K174-C028, RP8 form). | Different scope, both stand: K174-C028 names buying chances, not his own purchases; the claims do not say which entries or additions used the scare-driven dips. Not counted as a held-out contradiction. |

Open: C3 (entry discount required or typical), C7 (pond size and idea rate numbers), C9 (equal weight vs
concentration), C14 (breadth of the healthcare exclusion). The three held-out contradictions (C17, C18, C19) are
closed as different scope; RB22 rests on one case (FICO) and no verified rule claim states it in general.

## 5. Examples

| id(s) | company | fits / fails | rule |
|---|---|---|---|
| K065-C057, K065-C058, K065-C061, K189-C054, K189-C055, K189-C057, K189-C062, K290-C070 | Moody's, S&P Global | fit: natural duopoly ("90% of all the debt in the world"), toll collectors, inflation-plus pricing, capital efficient, network effect, cannot be undercut | RB7, RB8, RB10, RB11, RB14 |
| K065-C059, K189-C058, K189-C060, K290-C068 | Moody's, S&P Global | entry: after housing-related litigation; bought S&P Global at $17.50 and Moody's at $16.50 in early 2009 | RP8 |
| K065-C095 | Moody's | traded at a 5-6% FCF yield at times (reader note: at 10% 10-12 years ago, judged worth 3%) | RP4 |
| K290-C084 | S&P Global | would fail if it made many acquisitions to prop up slowing growth | RS4, RA11 |
| K105-C080, K290-C022, K189-C066, K290-C051 | Fair Isaac (FICO) | fit: monopoly in US consumer credit scores, followed seven years before buying, bought on market neglect; forward multiple misses its price increases (mortgage score +100%) | RB7, RO4, RP9, C13 |
| K174-C002, K174-C003, K174-C005, K174-C023, K174-C024 | Fair Isaac (FICO), v1.1 | fit at an inflection: dominance known for a long time; growth volume-only in the early years, changed in 2018; no price rises in the 25 years before 2016 | RB22, RB6 (narrowed), RB10 (narrowed), C17-C19 |
| K174-C004, K174-C015, K174-C016, K174-C017, K174-C018 | Fair Isaac (FICO), v1.1 | fit: score cheap relative to loan size, users benefit, use is voluntary (VantageScore available), protection = network effect, not the model | RB8, RB9, RB11, RA15 |
| K174-C006, K174-C007, K174-C008, K174-C009, K174-C011, K174-C012 | Fair Isaac (FICO), v1.1 | fit: operating leverage (software margins far below scores), capex under $10m in two fiscal years at ~$20bn market cap, free cash flow used for buybacks, share count down 20% / 25% over five / ten years (reader note) | RB13, RB14, RB16 |
| K174-C020, K174-C021 | Fair Isaac (FICO), v1.1 | "if you had to design an ideal business from scratch FICO has most of the elements" (list in K174-C021) | RB1, RB7, RB10, RB11, RB13, RB14, RB9 |
| K174-C028 | Fair Isaac (FICO), v1.1 | buying chances at depressed levels on the FHFA decision and Synchrony over 2018-23 (period per claim) | RP8, C20 |
| K174-C022 | IPOs and SPACs 2020-23 (period per claim) | fail: "almost a thousand" came to market; none "whose business model is as compelling" | RB1 |
| K065-C015, K065-C019 | Monster Beverage | entry after a health scare (reader note: fell 40% in a few days); intrinsic value updated every quarter | RP8, RO5 |
| K065-C069 | Monster Beverage, Nike | sold; both did well after | RS2 context (exits that later did well) |
| K105-C069, K189-C049, K189-C050 | Visa, Mastercard | entry after the Durbin amendment drop; Visa "tremendous pricing power" | RP8, RB10 |
| K189-C023, K189-C025, K189-C026 | ASML | fit: monopoly with a 10-15 year technology lead; chosen as "the most predictable way to participate in AI" | RB7, RB9, RB3 |
| K189-C024 | TSMC | fail: very capital intensive, advantage from scale | RA5, RA13 |
| K189-C026 | Nvidia, Microsoft, Google | passed over for ASML on predictability | RB3 |
| K189-C020 | Colgate | fail: very predictable but low organic growth | RB2, RB4 |
| K065-C046, K105-C140, K105-C141, K105-C142, K105-C143 | Amazon | owned as an exception: capital intensity outlier, expected inflection (AWS, advertising per reader note), optionality | RA10 exception, C4, C11, C16 |
| K105-C106 | Amazon e-commerce | fail as a standalone: gains scale and share but would not excite him | RA13 |
| K065-C044, K189-C070, K189-C071, K290-C046, K290-C047 | FANG / big tech, Google search | avoided for capital allocation, dual class, pet projects; admitted omission | RA8, RA9, RA10 |
| K065-C065, K065-C066, K065-C067, K065-C068 | American Dairy | fail (largest loss, ~4% drag in 2010): Chinese infant formula, bought at a single-digit multiple, early industry battle | RA6 (cheap price did not protect); RB20 (foreign) |
| K105-C099; K290-C080 (reader note) | Valeant (also Constellation, TransDigm in the reader note) | fail: growth by acquisition | RA11 |
| K290-C057 | Broadridge | fail: near-monopoly in proxy voting but "not a great compounder" (dominance alone not enough) | RB7 not sufficient, RB1 |
| K290-C058 | Boeing, Airbus | fail: a duopoly with issues (reader note: capital intensive, labour, subsidies) | RA5, RB7 not sufficient |
| K290-C059 | Nike, Under Armour, Adidas | fail: could have been an oligopoly but fought for market share | RB7 |
| K065-C089 (reader note) | eBay, Nike | LEAPS positions, two in 14 years | RO14 |
| K105-C067, K290-C014 | Coca-Cola (pre-WWII, 1928) | fit: compounder where macro timing or valuation did not matter | RO7, RB6 |
| K105-C057, K290-C045 | washing machine maker at P/E 8 or 12 vs Microsoft at IPO at P/E 35 | cheap low quality is the wrong approach; skipping the compounder for a low multiple is "a tragic mistake" | RA6 |

## 6. Gaps (what a screen needs that he does not state)

- Predictability (RB2, RB3, RB7): no measure and no threshold; "dominant for at least the next 10 years" (K290-C002)
  is a judgement.
- Organic growth per company (RB4): no number; the only number is the portfolio weighted average, high teens to low 20s
  (K065-C051 FCF per share; K290-C015 organic growth). Organic vs acquired growth split is not defined.
- Long record (RB6): "10, 20, 30, 50 years", "decades" (K105-C021, K189-C068) without a measure of what "great quality"
  was over that record.
- Pricing power (RB10): stated as price rises vs inflation (K290-C055, K189-C048); no account-based stand-in is given.
- Inflection (RB22, v1.1): no measure of the change in growth profile, no window, no test of "others ... may not have
  realized" (K174-C024), and no measure of latent pricing power beyond price vs value delivered ("cheap relative to
  the loan sizes", K174-C004, K174-C016); one case only (FICO). Which purchases used RB22 rather than RB6/RB10 is
  not stated.
- Sum of the parts (RP10): states what he does not use; the only reason given is "based on its growth profile"
  (K174-C019).
- Return on tangible assets, capex intensity, reinvestment (RB14, RA5): directions only; no cut-off (K065-C009
  reader note "no cut-off given").
- Operating margin trend (RB13): direction only; no window.
- Buybacks and company cash (RB16, RB17): "a lot", "virtually no cash"; no numbers.
- Leverage (RA7, RS5): no net debt / EBITDA or other number.
- Stock compensation (RP2, RA9): the adjustment method is stated (FCF after buying back issued stock), the level
  that counts as "too much" is not.
- Valuation (RP1, RP4, RP5): no discount rate, no mapping from quality rank to required FCF yield, no numeric gap to
  the 10-year Treasury (K065-C094 reader note); the forward years are his own conservative model (RP3), not consensus.
- Margin of safety (RP6): 30-60% below intrinsic value is the only number, and intrinsic value itself is unstated
  (C3 open).
- Entry triggers (RP8, RP9): drawdown size given (40%, 50%) but no window ("suddenly", "a few days" per K065-C015
  reader note) and no test of "misunderstood"; "market neglect" has no measure ("trail the general market",
  K065-C014).
- Size universe (RB20): "at least mid-cap, usually large-cap" with no dollar floor; US-centric with foreign
  "opportunistically" (no share).
- Sector exclusions (RA1-RA4, RA10): only healthcare names sub-industries; "hardware technology", "minerals",
  "tied to commodity prices", "tied to interest rates" and "big technology" have no classification list.
- Acquisitions (RA11): no count or spend that makes a company a serial acquirer (five a year is an example).
- Scale-based advantage, natural vs coerced dominance, exceptional-management dependence, pet projects, a possible
  90% fall (RA13, RB8, RB18, RA8, RA14): no observable measure stated.
- Size (RZ1-RZ4): no weights, no maximum position size, no rule for when to add (only "when the market is not properly
  assessing intrinsic value", K189-C005).
- Sell (RS1-RS7): intrinsic value needed for RS1; no rule for how much "better" a replacement must be (RS2).
- He says numeric screens do not find his companies and only narrow the universe (K065-C008, K065-C011, K105-C038):
  any recipe built from these rules is a stand-in for a reading-led process (C5).
