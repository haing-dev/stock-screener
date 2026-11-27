# Recipe: Dev Kantesaria (gate G6, blind rebuild for G7)

Inputs: CARD_v1.1.md (held-out test FAILED, K174 merged), FIELD_DICTIONARY_v1.0.md, field_dictionary_v0.1.csv,
construction_13F.txt. No returns were seen; no number below was chosen by any outcome.

## 0. How the screen runs

- When: every quarter-end, on the eligible set (1,500 largest US companies, GICS known on the day). Accounts as first
  reported and usable on the day (dictionary v1.0 rules 1-3). TTM = last four quarters; "fiscal year" values = the
  last reported fiscal years.
- Cut-offs given as "median" or "third" are percentiles across the whole eligible set (all sectors, before the AVOID
  exclusions), among companies with the measure present. They are not sector ranks: he compares across industries
  ("first screen is business quality", K189-C019), not inside them.
- All criteria are pass/fail and every one must pass (no scores that offset each other): RA12, "one negative factor
  can make a company uninvestable" even when the other boxes are checked (K105-C098, K105-C101).
- A missing measure = fail (his bar is "exceedingly high", K105-C019; RB1). This is the opposite of the reference
  book's "missing = 0.5" and is deliberate.
- Pass set = passes BUY and AVOID. Buy list = pass set that also passes PRICE. Ranking (section 6) orders the buy list.
- Universe (RB20; K105-C047, K290-C017, K065-C076): US, at least mid-cap. Met by the eligible set itself; no extra
  size floor (C2: large size is an outcome, not a screen).

Line format: id | card rule(s) and claim ids | measure | comparison and number | TAG | why this measure.

## 1. BUY (what qualifies)

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| B1 | RB6 (K105-C021, K105-C022, K189-C068, K290-C020) | new: number of fiscal years with first-reported revenue (R01) and net income (R13) in the accounts | >= 10 | quote | "great business quality for the last 10, 20, 30, 50 years": 10 is his lowest number. The record must exist before it can be extrapolated. |
| B2 | RB1, RB3, RB6 (K065-C002, K105-C013, K290-C018, K105-C021) | S01 loss years in the last 10 fiscal years | = 0 | convention | A "compounding machine" with a 10-year record of quality and earnings that should not "worry you" has no loss year; zero is the plain reading of "never trade reliability". |
| B3 | RB2, RB3 (K189-C019, K290-C011, K105-C013, K290-C018) | S03 revenue predictability: standard deviation of yearly revenue growth over the last 10 fiscal years (the 9 rates within them) | in the lowest third of the eligible set | convention | Predictability is the side he never gives up ("always"), so the stricter cut: "very predictable" read as the low tercile of growth volatility. Only account-based measure of a predictable path in the dictionary. |
| B4 | RB2, RB4 (K105-C097, K065-C035, K105-C014, K189-C021) | G01 revenue growth, 5 years: compound growth of TTM R01 vs TTM 20 quarters earlier | above the eligible-set median | convention | "Very strong topline ... organic growth" over "five to 10 year" horizons, yet "happy to give up some growth" (K290-C018) and Colgate fails on low growth (K189-C020): above-median is the reading that is strong but not maximal. Organic vs acquired is not split in the data (see A5). |
| B5 | RB4 (K105-C097, K105-C014) | G02 diluted EPS growth, 5 years (R14 history); base <= 0 = missing | above the eligible-set median | convention | "Topline and bottom line" growth: the bottom-line half of RB4, same cut as B4. |
| B6 | RB13 (K105-C034, K105-C035, K174-C007) | new: Q05 operating margin TTM (R07 / R01) minus Q05 of the fiscal year five years earlier | >= 0 | convention | "Margins go up over time": direction from the quote, 0 = not down; 5 years = his growth horizon (RB4 "five to 10 year"), longer than the dictionary's 3-year G06 to read "over time", not one cycle. |
| B7 | RB14, RA5 mirror (K105-C036, K065-C009, K290-C053, K290-C085, K174-C010; K065-C039) | new: reinvestment rate = capex TTM (R42) / cash flow from operations TTM (R41); R41 <= 0 = fail | in the lowest third of the eligible set | convention | "Little reinvestment, preferably zero", "does not have to reinvest heavily ... to keep it going": capex as a share of the cash the business makes is his word "reinvestment"; low tercile = "very low". Also carries RA5 ("highly capital intensive" excluded), so RA5 has no separate line. |
| B8 (full form only) | RB16, RB15 (K290-C087, K105-C040; support K174-C011, K174-C012) | C04 diluted share count (R15) vs three years before | < 1.00 (count down) | convention | "We love it when a great compounding machine buys back a lot of their stock": a net fall in the share count is the observable part; "a lot" has no number, so any net fall. Strength "usually": full form only. |

## 2. PRICE (when cheap enough)

A pass-set company passes PRICE if P1 OR P2 passes. PRICE gates entries and additions only; it never forces a sale
(S3).

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| P1 | RP4, RP5, RP2 (K065-C092, K065-C093, K105-C155, K065-C074, K065-C075, K105-C042) | new: free cash flow after share pay yield minus 10-year Treasury = (R41 - R42 - R44) TTM / L01c minus the 10-year Treasury yield at the quarter-end (V13 with share pay deducted) | > 0 percentage points | convention | He ranks by FCF yield against the 10-year Treasury and wants "a large gap with the risk-free rate", FCF measured after stock compensation. No gap number is stated (K065-C094 note), so the floor is the minimum reading: the yield exceeds the risk-free rate. Trailing, not consensus forward (C13: forward multiples warned against; his own forward model, RP3, is not available). |
| P2 | RP8 (K189-C013, K065-C013, K290-C021, K174-C026) | P03 distance from the 12-month high (close / highest close of 12 months - 1) | <= -40% | quote | Scare entries (about a third): the stock "significantly dropped", "40%, 50%"; "a sudden 40% drop". 40% is his lower number. Passes PRICE even if P1 fails, because the scare route is a separate way in. |

## 3. AVOID (exclusions)

GICS names below are matched by name across GICS revisions (codes as of the 2023 structure; older codes in brackets).

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A1a | RA1, RA2 (K065-C034, K105-C075, K105-C076, K290-C067, K065-C036) | X01 GICS sub-industry | excluded: Pharmaceuticals 35202010, Biotechnology 35201010, Health Care Equipment 35101010 (devices), Health Care Facilities 35102020 (hospitals), Health Care Technology 35103010 (healthcare IT) | quote | Each is named in his words: "no pharmaceuticals ... no biotech ... no medical devices ... no hospitals ... no healthcare IT". |
| A1b | RA1 (K065-C034, K105-C077; C14 open) | X01 GICS sector | excluded: the rest of Health Care (sector 35): Health Care Supplies 35101020, Health Care Distributors 35102010, Health Care Services 35102015, Managed Health Care 35102030, Life Sciences Tools & Services 35203010 | convention | "No healthcare" read as the whole sector; the named parts cover 5 of the sector's 6 industries. C14 (rule or outcome for the wider list) is open; whole-sector is the standard reading of "no healthcare". |
| A2 | RA2 (K065-C036, K105-C037) | X01 GICS industry group | excluded: Technology Hardware & Equipment 4520 (Communications Equipment, Technology Hardware Storage & Peripherals, Electronic Equipment Instruments & Components) | convention | "Hardware technology" = the GICS group of that name. Semiconductors and semiconductor equipment are NOT excluded (ASML is a stated fit, K189-C023; TSMC fails on capital intensity and scale, which B7 catches). |
| A3 | RA3, RA2 "minerals" (K065-C037, K065-C036; support K065-C006, K105-C064) | X01 GICS sector / industry / sub-industry | excluded: Energy (sector 10, all); Metals & Mining 151040 (incl. aluminium, copper, gold, precious metals, silver, steel, diversified); Commodity Chemicals 15101010; Fertilizers & Agricultural Chemicals 15101030; Paper & Forest Products 151050; Agricultural Products & Services 30202010 | convention | "Prospects tied to commodity prices": the GICS groups whose revenue is a commodity price. Industrial gases, specialty chemicals and construction materials are not excluded (pricing set by contract or local market, not a traded commodity). |
| A4 | RA4 (K065-C038) | X01 GICS | excluded: Banks 4010; Commercial & Residential Mortgage Finance 40201050 (Thrifts & Mortgage Finance 40102010); Consumer Finance 402020; Mortgage REITs 402040 (in Real Estate group 4040 before 2016); insurance underwriters (Life & Health, Multi-line, Property & Casualty, Reinsurance in 403010; Insurance Brokers NOT excluded); Utilities (sector 55); Real Estate (sector 60; group 4040 before 2016) | convention | "Fortunes tied to where interest rates will be": the standard rate-sensitive groups (net interest income, investment-yield underwriting, bond-proxy utilities and REITs). Fee businesses in Financials stay in: rating agencies, exchanges and data, payment processors are his own fits (Moody's, S&P Global, Visa, Mastercard; section 5 of the card). Matches the generic-book exclusions in dictionary X01 (4010, 4030, 4040, 60) except brokers. |
| A5 | RA11, RS4 (K290-C080, K105-C041, K290-C081, K105-C100, K174-C010) | new: number of the last 5 fiscal years in which acquisitions (R48) > 0.25 x cash flow from operations (R41) | >= 3 -> excluded | convention | "Companies that need acquisitions as part of their long-term strategies" ("five companies every year"): repetition is the mark, so a count of material acquisition years; one large offensive deal (acceptable, C6, K290-C081) trips at most one or two years. 3 of 5 = most years; 0.25 = a quarter of the cash the business makes. |
| A6 (full form only) | RA7 (K065-C084) | B01 net debt / EBITDA TTM ((R30 - R18) / R09; EBITDA <= 0 = fail) | > g -> excluded; grid g = {2, 3, 4}, averaged | grid | "No leverage at the company level": direction only, no number, strength "usually". |

## 4. SELL

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S1 | RS3, RS4 (K065-C081, K105-C020, K290-C061, K065-C082, K290-C082) | the BUY criteria (B1-B7) and A5, re-applied to each holding | sell at the quarter-end when the holding has failed any of them at two consecutive quarter-ends | convention | "Sell on a change in business quality", "misuse of free cash flow" (A5); two consecutive quarter-ends = a change that lasts, the reading of "sell rarely" (RS7). |
| S2 | RA1-RA4 (claims as A1-A4) | X01 GICS on the day | sell at the first quarter-end the holding is classed in an A1-A4 group | convention | Exclusions are "always" rules; a reclassification into one is a change in what the business is. |
| S3 | RS6, RS1, RS7 (K290-C049, K065-C079, K065-C086, K105-C004; support K105-C133) | price and valuation | no sale and no trim because of price, valuation or weight drift; PRICE failing only stops additions | convention | Do not sell for a P/E move "from 26 to 29"; 100% of intrinsic value triggers a review, "not an automatic sale"; horizon "10 years, 20 years, 30 years". |
| S4 (full form only) | RS5 (K065-C083) | B01 net debt / EBITDA TTM | sell when > g at two consecutive quarter-ends; grid g = {3, 4, 5}, averaged | grid | "Sell if the company takes on excessive leverage"; "excessive" has no number; set one turn above the A6 entry grid so a holding is not sold at the entry bar. |
| S5 (full form only) | RS2, RS1 (K065-C085, K065-C080, K105-C131, K065-C079) | P1 gap of holdings vs buy-list names | when the book holds 14 names (Z3) and a buy-list name ranks in the top 10 of the buy list, it replaces the holding with the lowest P1 gap if that gap is <= 0; at most one switch per quarter-end | convention | "The easiest decision for exiting ... is when we find something that we like better"; P1 <= 0 is the stand-in for "reaches 100% of intrinsic value, justify why still held". One a quarter keeps turnover low (RS7). Strength "usually / sometimes": full form only. |
| S6 (check, both forms) | RS7, RO6 | share of the paper book's positions still held 1 / 3 / 5 years after entry | report against his 13F: 70% / 38% / 12% | revealed-13F | Report only; no rule is changed by it. |

## 5. SIZE

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| Z1 | RZ1 (K290-C024, K105-C018, K105-C158, K189-C015; support K105-C132) | target number of holdings N | N = 10; new entries only from the top N of the ranked buy list | convention | "Our 8 to 12 best ideas", "just a range": 10 = the middle of the quoted range (and the 10 holdings of K105-C132). |
| Z2 | RZ1, RZ5, C9 (K189-C016 not verified; K189-C036) | weights | each holding at 1 / max(n, 8) of the book at entry, n = names held; the rest in cash; weights then drift (S3); entries funded pro rata from cash, then from all holdings | convention | No weight rule is stated (card section 3); equal weight is his stated "ideal" (K189-C016). The floor of 8 (his lowest number) stops a thin pass set from putting a third of the book in one name; cash then exceeds his "0% to 5%" (RZ5, quote) and is reported. |
| Z3 | RZ2 (K105-C161, K105-C159, K105-C055) | maximum number of holdings | <= 14 | quote | "No problem owning 14"; "reluctant to invest in our 17th best idea". Because sales are rare (S1-S3), the book may run above N up to 14 while held names keep passing. |
| Z4 | RO2 (K065-C018, K189-C006) | new names entered in the last 12 months | <= 3 (not applied at the first quarter-end, when the book is first filled) | quote | "One to three great ideas a year". Additions to held names do not count. |
| Z5 (full form only) | RZ3, RZ4 (K189-C004, K189-C017, K065-C054, K189-C005) | target weights by rank in the held book (rank = section 6 at the quarter-end) | ranks 1-5: 26%, 22%, 18%, 13%, 11%; the rest share 10% equally; a holding below its target is raised to it only at a quarter-end where it passes PRICE; never cut for being above (S3); replaces Z2 | revealed-13F | His 13F: largest weight 26%, top 5 = 90%, effective names 5.2. "Few decisions, but ... big", added "when the market is not properly assessing intrinsic value". Caveat: 13F weights include drift, not only intent. |
| Z6 (full form only) | RZ4 (K065-C054, K189-C005) | weight of a new position at entry | 1.7% of the book, then raised under Z5 at later quarter-ends | revealed-13F | His 13F: new positions start at 1.7%; additions are 72% of his buys ("another 13, 14, 15 times along the way"). |

## 6. Ranking inside the buy list

His stated order: business quality first (the BUY and AVOID screen, "our first screen is business quality",
K189-C019), then rank-order by the free cash flow yield against the 10-year Treasury, preferring the largest gap
(RP4, RP5; K065-C092, K065-C093, K105-C154, K105-C155). Rule: sort the buy list by the P1 gap, largest first (at one
quarter-end the Treasury is common to all names, so this is the order of FCF-after-share-pay yield). Ties: the lower
B3 growth volatility first (predictability before growth, RB3). P2 names that fail P1 are ranked by their P1 gap like
the others. The deserved-yield-by-quality step of RP4 is not stated in numbers and is not built.

## 7. The two forms

DECISIVE form (quote and convention numbers only; firm rules, strength "always" or "always / usually", except P1/P2
which carry the price part): B1-B7, P1-P2, A1a, A1b, A2, A3, A4, A5, S1-S3, Z1-Z4, ranking of section 6. Check S6
reported.

FULL form = decisive + B8 (buybacks), A6 (leverage grid {2, 3, 4}), S4 (leverage sell grid {3, 4, 5}), S5 (switch
into something better), Z5 (revealed-13F rank weights, replacing Z2), Z6 (1.7% entry). The leverage grid is run as
3 versions, each pairing the A6 entry bar with the S4 sell bar one turn above it: (A6 2, S4 3), (3, 4), (4, 5). The
three version portfolios are averaged with equal weight.

Reported, not rules: RB5 portfolio growth (weighted 5-year FCF per share growth G03 of the held book, against his
"high teens to low 20s", K065-C051, K290-C015; a forward target for the portfolio, not a per-company bar); RO3 pass-set
size each quarter against his pond of "40 to 50" / "50 or 60" (K105-C017, K189-C018, K290-C076); cash against RZ5
0-5%; S6 survival.

## 8. Not computable (card rules no dictionary measure can express)

| rule | reason |
|---|---|
| RB7 | Dominance (monopoly / duopoly / oligopoly) "for at least the next 10 years": no market-share or industry-structure measure; durability is a judgement. |
| RB8 | Natural vs forced use of the product: no measure of customer benefit or lock-in. |
| RB9 | Form of the advantage (industry dynamics, technology lead, network effect): not observable in accounts. |
| RB10 | Price rises above inflation for a decade plus: no product-price data; gross margin rejected as a stand-in (moves with mix and costs). |
| RB11 | Cheap, essential "must-have" product priced far below the value delivered: no measure. |
| RB12 | Industry volumes rising: no volume data; industry revenue growth mixes price and volume, rejected. |
| RB18 | Business "your idiot nephew could run": no measure of management dependence. |
| RB19 | Many levers (pricing, volumes, flexible costs): no measure. |
| RB21 | Temporary vs structural volume drop: needs a judgement about the future; B3 cannot tell them apart (see section 9). |
| RB22 | Inflection on a long-dominant business that others "may not have realized": no measure of the change, no window, one case; it also needs RB7. |
| RP1 | DCF value with his discount rate: no discount rate stated. |
| RP3 | His conservative FCF model without optionality: his own forecast, not data. |
| RP6 | 30-60% below intrinsic value: intrinsic value is not computable (C3 open). |
| RP7 | Pre-set buy price per company: his private line, not data. |
| RP9 | Market neglect (two thirds of entries): no measure of attention stated; trailing the market (support K065-C014) cannot separate neglect from a deserved fall. |
| RP10 | No sum-of-the-parts valuation: a method he does not use; nothing to screen. |
| RA6 | No low-quality turnarounds: no separate measure; covered only indirectly by B2-B7. |
| RA8 | Dual class with a CEO "anointed for life", pet projects: no ownership-structure field; counting listed share lines misses unlisted super-voting classes, rejected. |
| RA10 | Big technology (FANG) with Amazon as a stated exception: a named group, not a classification. |
| RA13 | Advantage from scale or volume: not observable. |
| RA14 | Could "go down 90% tomorrow": no measure stated. |
| RA15 | Coerced use (avoid form of RB8): no measure. |

Partly covered only: RB1 (quality as a whole: B2-B7 are pieces of it), RB15 (capital allocation: A5, B8).
Computable but left out: RB17 ("virtually no cash", usually, no number; his own fits hold cash, so any number would be
a guess), RA9 (share pay: already charged in P1 through RP2; no level for "too much").
Process rules that are not screen rules: RO1, RO4, RO5, RO7-RO16 (13). RO2 is used (Z4), RO3 and RO6 support checks
and S3; RA12 sets the structure (all criteria must pass).

## 9. Coverage and main risk

Coverage of his 22 buy rules: the decisive form implements 7 (RB2, RB3, RB4, RB6, RB13, RB14, RB20) and part of RB1 =
7 of 22 (32%), 36% counting the partial one; the full form adds RB16 and part of RB15 = 8 of 22 (36%), 45% counting
partial rules. RB5 is reported only. The 10 rules that make up his core idea of a business (dominance, natural
monopoly, pricing power, cheap essential product, form of advantage: RB7-RB12, RB22) are all not computable.

Main risk: the recipe selects steady, capital-light, growing companies with rising margins and an FCF yield above the
Treasury, but it cannot see what makes his companies his: a dominant, naturally chosen position with pricing power
(RB7-RB11). So the pass set will hold many good-but-ordinary compounders (consumer brands, distributors, IT services,
industrial niche firms) next to the rare toll collectors he owns, and likely be larger than his pond of 40-60 (the RO3
check will show by how much). The PRICE gate pulls the other way from him: he pays 2-3% FCF yields for the best
compounders (Moody's at 5-6% was "cheap", K065-C095) and buys on scares or neglect, while P1 needs a yield above the
10-year Treasury, so in high-rate years the buy list tilts to cheaper, slower or lower-quality names and his kind of
company may enter only through the 40% drawdown route. Three of his own cases would also be missed for data reasons:
the 10-year account record (B1) keeps out recent listings such as Visa and Mastercard for years after their IPOs
unless pre-IPO years are in the accounts; the growth and margin bars (B4-B6) reject the FICO inflection (RB22), which
was bought because volume-only growth was about to change; and the reinvestment bar (B7) rejects Amazon, his named
exception. Finally, by his own statement numeric screens "just don't work" and only narrow the universe (C5,
K065-C008, K105-C038); any failure of this recipe is a failure of the stand-in as much as of his method.
