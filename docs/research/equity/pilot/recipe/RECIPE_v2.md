# Recipe: Dev Kantesaria (Valley Forge Capital), gate G8 revision round (A10 item 9), v2

Built from `RECIPE_v1.md`, `CARD_v1.1.md` (label: held-out test FAILED, K174 merged), `field_dictionary_v0.1.csv`,
`FIELD_DICTIONARY_v1.0.md`, `construction_13F.txt` and `RECALL_FEEDBACK.md` only. The feedback (recall, base rate,
lift, interval, share of his purchases each criterion rejects) was used only to locate where v1 may misread him;
every change below rests on card claims whose quoted words support the new reading. No return of any kind was seen;
no number below was set by looking at an outcome or at his holdings' accounts.

## Change table (v1 -> v2)

Four substantive changes (C1-C4) and two follow-on changes (C5-C6) that keep other lines consistent with them. All
four substantive changes loosen v1; see section 9 for what that means.

| id | v1 | v2 | claim ids | why (one line) |
|---|---|---|---|---|
| C1 | B4 (S03 standard deviation of yearly revenue growth, 10 years, < universe median) in the decisive form | B4 moved unchanged to the full form; the decisive form tests predictability through B1, B2 and B3 | K290-C071, K290-C074 (RB21; C8 "that type of cyclicality doesn't bother me"); K105-C014, K105-C097 (RB4 horizon "five to 10 year"); K290-C016 ("five years out ... and 10 years out"); K290-C018, K105-C013 (RB3 stays) | He wants the path predictable over five to ten years and says temporary volume cycles do not bother him; the year-to-year spread of revenue growth counts those cycles as unpredictability. |
| C2 | B5 operating-margin change over 3 years > 0 (G06, dictionary window) | B5 over 5 fiscal years > 0; full form adds B13, a grid of 3 / 5 / 9 years (v1's 3 years kept as a version) | K105-C034 ("margins go up over time"), K105-C035, K174-C007 ("still have a tremendous amount of operating leverage"); K290-C071, K290-C074 (RB21, C8); K105-C014 ("five to 10 year") | "Over time" is a trend, not a 3-year change; with operating leverage a temporary volume dip he tolerates lowers margins for a year or two, so the shortest horizon he names is the stated reading. |
| C3 | Price pass = P1 AND (P2 OR P3) | Price pass = P1 alone; P2 and P3 move to the full form, where P5 averages "no trigger" with v1's "trigger required" | K189-C005 ("when the market is not properly assessing intrinsic value"), K065-C054 ("another 13, 14, 15 times along the way"), K189-C006 ("where there is a disconnect"), K065-C093, K105-C155 (RP5 gap), K174-C026 ("near-term share price volatility doesn't bother us at all"); K065-C022, K105-C068 ("no bad time to buy a compounding machine"); RP9 "no measure of neglect stated" (K189-C014, K290-C022) | The neglect / scare split describes how first entries came about, not a gate; his stated test for buying, and for the additions that are 72% of his 13F buys, is a gap between price and value, which P1 measures. |
| C4 | A5 excluded when acquisitions / operating cash flow > 0.50 over one 3-year sum | A5 excluded when the ratio is > 0.50 in BOTH the latest 3-year sum and the 3-year sum before it; full form A10 keeps v1's one-window reading as a version | K290-C080 ("need acquisitions as part of their long-term strategies"), K105-C041 ("we like offensive acquisitions"), K290-C081 ("serious cost and revenue synergies that go out 10 plus year"), K105-C100 (serial buying "not a playbook ... that ends well"); C6 | v1 said single offensive deals pass (C6), but one large deal can exceed half of three years' operating cash; "long-term strategies" means a lasting pattern, so the bar must hold over two windows. |
| C5 | K1 decisive quality score = mean percentile of G01, G02, S03 (reversed), G06 (3 years), C01 (reversed) | K1 decisive quality score = mean percentile of G01, G02, G06 (5 years), C01 (reversed); full form adds S03 (reversed), B7, B8 (reversed) | as C1 and C2; K189-C019, K290-C011 (RB2, "first screen is business quality") | Follow-on: the score uses the decisive BUY measures, so it moves with C1 and C2. |
| C6 | S2 sells when a holding fails A5 (one 3-year window) | S2 sells when a holding fails A5 as read in v2 (two windows) | as C4; K065-C082, K290-C082 (RS4); K290-C084 ("many acquisitions to prop up slowing growth") | Follow-on: the sell test of misused cash uses the same reading of acquisition-led growth as the buy-side exclusion. |

Unchanged on purpose, although the feedback shows they reject some of his purchases: B2 (no loss year; "year after
year", "never willing to trade reliability", K065-C003, K105-C013, K290-C018), B3 (both lines, "a very strong topline
and bottom line organic growth profile", K105-C097), B6 (capex below the median; "very low capital expenditure",
K105-C036, K065-C009), P1 (gap to the 10-year Treasury, K065-C093, K105-C155). A1-A4 reject none of his purchases and
stay because the quotes name those areas. Brief rule 3: a well-quoted rule is not dropped because it rejects
purchases. Purchases of a stated exception (Amazon: capital intensity, optionality, big tech; C4, C11, C16) are
expected to fail and no change was made to pass them.

## Recipe

Line format: id | card rule(s) and claim ids | measure | comparison and number | TAG | why this measure stands in
for his words. Measures are computed as the dictionary v1.0 states (as known on the day, first-reported, TTM flows,
a ratio with a denominator at or below zero is missing). **A missing measure fails the criterion** (the dictionary's
"missing = sector median" rule is for the reference book's ranks, not for a pass/fail screen).

Fixed reading conventions used throughout (stated once, applied everywhere, never varied per criterion):
- C-MED: an adjective he gives without a number ("very strong growth", "very low capex", "very predictable") =
  better than the median of the eligible universe at the same quarter-end. The universe is the 1,500 largest US
  stocks with a known GICS sector, BEFORE the AVOID exclusions (so the bar does not depend on the exclusion list).
  Percentiles are across the whole universe, not inside the sector: he compares businesses across industries.
- C-DIR: a stated direction without a number ("margins go up") = the sign of the change over the stated window; where
  he gives no window, the shortest horizon he names for a business's path, five years ("five to 10 year", K105-C014),
  which is also the dictionary's growth window used in B3 (v2, C2).
- Grid versions (full form only) replace C-MED by better than the 50th / 67th / 80th percentile, averaged.

Universe (not a criterion): 1,500 largest US stocks, GICS sector known, after the house exclusions of the dictionary
(X01: groups 4010, 4030, 4040, sector 60, sub-industry 35201010). RB20 ("very US-centric", K105-C047, K290-C017) is
met by the universe itself. GICS must be the history (WRDS `comp.co_hgic`); the LSEG form of X01 is today's code
(known look-ahead) and is not acceptable for A1-A4 in a historical run.

## 1. BUY (what qualifies)

### Decisive form

| id | card rule(s) / claim ids | measure | comparison and number | TAG | why this measure stands in |
|---|---|---|---|---|---|
| B1 | RB6 (K105-C021, K105-C022, K189-C068, K290-C020) | new: number of consecutive fiscal years, ending at the latest fiscal year known at the quarter-end, with first-reported R01 (revenue) and R13 (net income) present | >= 10 | quote | "10, 20, 30, 50 years": the lowest number he names. The record of dominance itself is not observable; ten years of accounts is the record we can check, and B2, B3 and B5 need it. |
| B2 | RB1, RB3, RB6 (K065-C002, K065-C003, K105-C013, K290-C018) | S01 loss years in the last 10 | = 0 | convention | "compound intrinsic value year after year"; "never willing to trade reliability". A loss year is the plainest break of predictability that accounts show. In v2 this is the main decisive test of RB3 (C1). |
| B3 | RB2, RB4 (K189-C019, K290-C011, K105-C097, K065-C035, K105-C014) | G01 revenue growth 5 years AND G02 diluted EPS growth 5 years (compound) | both > universe median (C-MED) | convention | "a very strong topline and bottom line organic growth profile": he names both lines, so both are tested. Five years is the lower end of his "five to 10 year" path. Organic vs acquired is not separable in accounts; A5 removes acquisition-led growth. |
| B5 | RB13 (K105-C034, K105-C035, K174-C007); RB21 (K290-C071, K290-C074) | new: operating margin (Q05, R07 / R01) of the latest fiscal year minus the same 5 fiscal years before (G06 on a 5-year window) | > 0 (C-DIR) | convention | "margins go up over time"; direction stated, no window. "Over time" is read at the shortest horizon he names for the path (five years, K105-C014), so that a temporary volume dip, which he tolerates (RB21), is not read as a falling trend (v2, C2). |
| B6 | RB14; mirror RA5 (K105-C036, K065-C009, K290-C053, K290-C085, K174-C010; K065-C039) | C01 capital expenditure to revenue, TTM | < universe median (C-MED) | convention | "very low capital expenditure", "does not have to reinvest heavily"; not "highly capital intensive". He gives no cut-off (K065-C009 reader note), so only the median reading is used. RA5 is implemented here, not as a separate line. |

(B4 has moved to the full form, C1; ids are kept as in v1 so that the two versions can be compared line by line.)

RB1 ("really high-quality businesses") has no measure of its own: it is implemented only as the conjunction of
B1-B3, B5 and B6 (and RA12, "one negative factor can make a company uninvestable", K105-C098, is met by construction:
every criterion must pass). RB3 (predictability) is expressed in the decisive form by B1 (a ten-year record), B2 (no
loss year) and B3 (growth over five years in both lines); the steadiness of yearly revenue growth (B4) and of margins
(B8) are full-form tests, because he tolerates temporary volume cycles (RB21, C8) and states predictability over a
five-to-ten-year path (K105-C014, K290-C016), not year by year.

### Full form (adds to the decisive form)

| id | card rule(s) / claim ids | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| B4 | RB3, RB2 (K105-C013, K290-C018, K290-C013, K105-C014); limited by RB21 (K290-C071, K290-C074) | S03 standard deviation of yearly revenue growth, 10 years | < universe median (C-MED, low = predictable) | convention | "a very predictable path to organic growth": the steadiness of the revenue path. Full form only (v2, C1): it also counts temporary volume cycles, which he says do not bother him. |
| B7 | RB14 (K105-C036, K290-C053) | new: R08 EBIT TTM / average of (R25 total assets - R24 intangibles incl. goodwill) | > universe median (C-MED) | convention | "high return on tangible assets" is the first thing he names in RB14. |
| B8 | RB3 (K105-C013, K105-C167 avoid form) | S02 operating-margin standard deviation, 10 fiscal years | < universe median (C-MED) | convention | A company "whose next earnings release worries you" has unstable margins. |
| B9 | RB16 (K290-C087; support K174-C011, K174-C012) | C04 diluted share count against three years before | < 1.00 | convention | "buys back a lot of their stock": no number; the minimum reading is a falling share count. Strength usually. |
| B10 | RB20 (K065-C076, K290-C017, K290-C077) | L01c market value (company) | >= $2bn (nominal) | convention | "at least mid-cap": $2bn is the standard mid-cap floor. Strength usually; C2 says size is an outcome, so full form only. |
| B11 | grid on B3, B4, B6, B7, B8 | as above | better than the 50th / 67th / 80th percentile, three versions averaged | grid | "very" may mean stricter than the median; no number is given. |
| B12 | RB5 (K065-C051, K290-C015) | portfolio check: weighted mean of G03 (FCF per diluted share growth 5 years) over the paper portfolio | report whether >= 15% ("high teens" read from its lower bound) | quote | His only growth number is for the weighted portfolio, not for a stock; it is REPORTED each quarter and never used to select or drop a name. |
| B13 | RB13 (K105-C034, K105-C035, K174-C007) | B5 measure on a window of 3 / 5 / 9 fiscal years (9 = the longest change B1's ten years allow) | > 0, three versions averaged | grid | "over time": no window stated; v1's 3-year reading stays as one version (v2, C2). |

## 2. PRICE (when cheap enough)

Price pass (decisive) = P1. His stated test for buying, first entries and additions alike, is a gap between today's
free cash flow yield and what the business deserves against the risk-free rate (RP4, RP5: K065-C092, K065-C093,
K105-C154, K105-C155); he adds "another 13, 14, 15 times along the way" (K065-C054) "when the market is not properly
assessing intrinsic value" (K189-C005), and additions are 72% of his 13F buys (construction_13F). Neglect (two thirds
of entries) and a scare (one third) are how first entries came about (K189-C014, K290-C021, K290-C022); neglect has no
stated measure (RP9) and both are full-form tests (P2, P3, P5; v2, C3). Price tests apply at entry and at additions
only; a holding is never sold on them (S4).

### Decisive form

| id | card rule(s) / claim ids | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| P1 | RP2, RP4, RP5 (K065-C074, K065-C075, K105-C042, K065-C092, K105-C154, K065-C093, K105-C155); RZ4 (K065-C054, K189-C005) | new: (R41 cash flow from operations - R42 capex - R44 share-based pay), TTM, / L01c, minus the 10-year US Treasury yield at the quarter-end (= V13 with share pay deducted) | > 0 | convention | "a large gap with the risk-free rate", no number (K065-C094 reader note); the minimum reading of a gap is a positive one; "larger is better" goes into the ranking. Share pay is deducted because he measures FCF after buying back the stock issued as pay (RP2; R44 is the stand-in for that cost). Trailing FCF stands in for his own conservative forward model (RP3, RP4); consensus forward multiples are NOT used (C13). |

### Full form

| id | card rule(s) / claim ids | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| P2 | RP8 (K189-C013, K065-C013, K290-C021, K174-C026) | P03 close / highest close of the last 12 months - 1 | <= -0.40 | quote | "40%, 50%", "a sudden 40% drop": the number is his; the 12-month window is the dictionary's (convention, he gives "suddenly" only). Scare trigger; used only inside P5 (v2, C3). |
| P3 | RP9 (K189-C014, K290-C022; support K065-C014) | new: 12-month compound total return of the stock (TR 1-month, months t-11 .. t) minus the same for the value-weighted eligible universe (L01c weights) | < 0 | convention | "no one is paying attention"; the only stated sign of neglect is that it can "trail the general market" (K065-C014). Neglect trigger; used only inside P5 (v2, C3). |
| P4 | RP5 (K065-C093, K105-C155) | P1 gap | > 0 / >= 1 / >= 2 percentage points, three versions averaged | grid | "a large gap": no number. |
| P5 | RP8, RP9 (K189-C014, K290-C021, K290-C022) against RZ4 (K065-C054, K189-C005) and C3 (K065-C022, K105-C068) | entry trigger | two versions averaged: (i) no trigger (the decisive form); (ii) P1 AND (P2 OR P3) for every purchase (v1) | grid | Whether the neglect / scare split is a gate or a description of how entries arose is not stated; both readings are run (v2, C3). |

## 3. AVOID (exclusions)

### Decisive form

| id | card rule(s) / claim ids | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A1 | RA1 (K065-C034, K105-C075, K105-C076, K290-C067) | X01 GICS (history) | exclude sector 35 Health Care: 351010 Health Care Equipment & Supplies, 351020 Health Care Providers & Services, 351030 Health Care Technology, 352010 Biotechnology, 352020 Pharmaceuticals, 352030 Life Sciences Tools & Services | convention | He names pharma, biotech, devices, hospitals and healthcare IT (always): five of the six industries; the whole sector is the plain reading of "no healthcare". C14 (breadth) is open: narrow version A8. |
| A2 | RA2 (K065-C036, K105-C037, K065-C037) | X01 | exclude industry group 4520 Technology Hardware & Equipment (software 4510 and semiconductors 4530 not excluded) and industry 151040 Metals & Mining | convention | "hardware technology", "minerals": the GICS group and industry with those names. Drug R&D is in A1. |
| A3 | RA3 (K065-C037; support K065-C006, K105-C064) | X01 | exclude sector 10 Energy, sector 15 Materials, sub-industry 30202010 Agricultural Products & Services | convention | "prospects tied to commodity prices": the GICS areas whose output is a commodity. |
| A4 | RA4 (K065-C038) | X01 | exclude sector 55 Utilities, sector 60 Real Estate, group 4010 Banks (incl. pre-2023 40102010 Thrifts & Mortgage Finance), group 4040 (pre-2016 Real Estate incl. mortgage REITs), sub-industries 40201050 Commercial & Residential Mortgage Finance, 40202010 Consumer Finance, 40204010 Mortgage REITs | convention | "fortunes tied to where interest rates will be": spread lenders, rate-set regulated returns, property. 4010, 4040 and 60 are also house exclusions; group 4030 Insurance is out by the house rule, NOT by his words. Financial Exchanges & Data (Moody's, S&P Global) and payment processors stay in. |
| A5 | RA11 (K290-C080, K105-C041, K290-C081, K105-C100, K174-C010); C6 | C06 acquisitions / cash flow from operations, 3-year sums, for fiscal years t-2 .. t AND for fiscal years t-5 .. t-3 | excluded when > 0.50 in BOTH windows | convention | "companies that need acquisitions as part of their long-term strategies": the plain reading is that most operating cash goes to buying companies, as a lasting pattern ("long-term strategies"; serial buying "not a playbook ... that ends well"). One large offensive deal falls in one window and passes, as C6 says it should ("we like offensive acquisitions"); v1's one window did not deliver that (v2, C4). The 0.50 bar and the 3-year window are v1's; "five companies every year" is an example and deal counts are not in the dictionary. |

RA5 is B6; RA9 ("issuing too much compensation") is priced in by the share-pay deduction in P1 (RP2) and gets no
separate cut-off (he gives none); RA12 is the conjunction.

### Full form

| id | card rule(s) / claim ids | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A6 | RA7 (K065-C084) | B01 net debt / EBITDA, TTM | > 1 / > 2 / > 3 excluded, three versions averaged; EBITDA <= 0 = fail | grid | "no leverage": direction only, strength usually. |
| A7 | RA8 (K065-C045, K189-C071) | new: company has 2 or more listed common lines in the universe file (L01c sums more than one line) | excluded | convention | Dual-class with a listed second class is visible; an unlisted super-voting class is not (partial). Strength usually. |
| A8 | RA1 narrow version (C14 open) | X01 | exclude only 351010, 352010, 352020; averaged with A1 as two versions | grid | C14: hospitals and healthcare IT may be excluded by outcome, not by rule. |
| A9 | RA4 wide version | X01 | A4 plus sub-industry 25201030 Homebuilding; averaged with A4 as two versions | grid | Homebuilders' fortunes follow mortgage rates; not named by him. |
| A10 | RA11 (K290-C080, K105-C100); C6 | C06, latest 3-year sum only (v1 reading) | > 0.50 excluded; averaged with A5 as two versions | grid | How long a pattern makes acquisitions a "long-term strategy" is not stated; v1's one-window reading stays as a version (v2, C4). |

## 4. SELL

Rebalancing and selling happen only at quarter-ends.

### Decisive form

| id | card rule(s) / claim ids | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S1 | RS3 (K065-C081, K105-C020, K290-C061); RB21 (K290-C071, K290-C074) | B2, B6, A1-A4 | sell at the first quarter-end where a holding shows a loss year (B2 fails), fails B6, or moves into an excluded GICS code | convention | "a change in business quality or risk". The growth and margin tests (B3, B5) do NOT trigger a sale on their own: he tolerates temporary volume drops in a quality business (RB21). |
| S2 | RS4 (K065-C082, K290-C082; support K290-C084) | C06 (A5, two windows) | sell when a holding fails A5 (acquisitions > 0.50 of operating cash in both the latest and the previous 3-year window) | convention | "misuse of free cash flow"; his own example of a failing S&P Global is "many acquisitions to prop up slowing growth", a pattern, not one deal (v2, C6). |
| S3 | RS2 (K065-C085, K065-C080, K105-C131); RO2 (K065-C018) | quality score of the ranking rule (section 6) | when the book holds N names and a name that passes BUY, PRICE and AVOID has a higher quality score than the lowest-scored holding, sell that holding and buy the new name; at most 3 new names in any 12 months | convention (comparison); quote (3) | "the easiest decision for exiting ... is when we find something that we like better"; "trading a lower-quality name for a higher-quality one". The yardstick is quality, not price. "One to three great ideas a year" caps the churn. The first formation date fills the book to N (the cap starts after it). |
| S4 | RS6, RS7 (K290-C049, K065-C086, K105-C004); RS1 review only (K065-C079) | P1 (and P2, P3 in the full form) | a holding is never sold because it fails a price test or because its price or multiple rose | convention | "Do not sell because the P/E moved from 26 to 29"; low turnover is the intended result; RS1 at 100% of intrinsic value is a review, not a sale (C12). |

### Full form

| id | card rule(s) / claim ids | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S5 | RS5 (K065-C083) | B01 net debt / EBITDA | sell when > 3 / > 4, two versions averaged | grid | "excessive leverage": no number. |
| S6 | RS3 with RB21 | B3 or B5 | sell when B3 or B5 fails at 4 / 8 consecutive quarter-ends (versions averaged; plus a version with no such sale) | grid | Separates a lasting change in growth or margins from a temporary drop; no window is stated. B5 is read on its v2 5-year window (and on B13's windows in the B13 versions). |

## 5. SIZE

### Decisive form

| id | card rule(s) / claim ids | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| Z1 | RZ1, RZ2 (K290-C024, K105-C018, K105-C158, K189-C015, K105-C161) | number of holdings | N = 10 (if fewer pass, hold those that pass) | convention | Midpoint of his quoted 8 to 12 ("just a range"); K105-C132 also says 10. Never above 12, inside the RZ2 limit of 14. |
| Z2 | RZ3, C9 (K189-C016 ideal; K189-C004) | weights | each new name enters at 1/N of the book (funded pro rata from the other holdings); no rebalancing between entries and exits; weights drift | convention | C9 is open (equal weight is his stated ideal, concentration his practice, no weight rule); equal weight at entry is the neutral reading and drift reflects "sell rarely" (RS7). |
| Z3 | RZ5 (K189-C036; support K105-C123) | cash | 0%; unfilled slots (fewer than N passers) are held in the value-weighted eligible universe, at 1/N per empty slot | quote (0-5%); stand-in = convention | "probably 0% to 5%": the paper book must not sit in cash when the screen finds too few names; the universe is the neutral filler. |

### Full form

| id | card rule(s) / claim ids | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| Z4 | RZ1 | N | 8 / 10 / 12 (grid, from his range) and 9 (revealed: median names in his 13F) | grid / revealed-13F | Range stated; 13F shows 9 names (8 at >= 1%). |
| Z5 | RZ3 (K189-C004, K189-C017) | target weight by rank in the book (section 6) | 26 / 24 / 18 / 13 / 9 / 4 / 3 / 2 / 1 % for ranks 1-9 (scaled to N) | revealed-13F | Fitted only to the 13F shape: largest weight 26%, top-5 90%, top-10 100%; gives effective names ~5.4 vs 5.2 in the 13F. "Concentrate on the ones far stronger than others". |
| Z6 | RZ4 (K065-C054, K189-C005) | entry and additions | a new name enters at 1.7%; at each later quarter-end where it still passes BUY and PRICE it moves 1/k of the way to its Z5 target, k = 2 / 4 / 8 (averaged) | revealed-13F (1.7%); grid (k) | 13F: new positions start at 1.7%, 72% of buys are additions; he adds "13, 14, 15 times" while the market misprices it. |
| Z7 | RZ3 | largest weight | trim to 32% at a quarter-end if above | revealed-13F | 90th percentile of his largest weight in the 13F; he states no maximum. |

## 6. Ranking inside the pass set (for the paper portfolio of N names)

| id | card rule(s) / claim ids | rule | TAG |
|---|---|---|---|
| K1 | RB2 / "first screen is business quality" (K189-C019, K290-C011); RP4, RP5 (K065-C092, K105-C154, K105-C155); never sacrifice quality for price (K105-C056, K105-C057, K290-C045) | Quality score = mean of the universe percentiles of G01, G02, the B5 margin change (5 years) and C01 (reversed) (the decisive B3, B5, B6 measures; v2, C5); the full form adds S03 (reversed, B4), B7 and B8 (reversed), and uses each B13 window in its own version. Split the pass set into thirds by quality score; order by third (best first), and inside a third by the P1 gap (largest first). Take the top N, subject to S3. | convention |

Why: he ranks companies by the FCF yield each deserves for its growth and predictability and wants the largest gap
to that deserved yield; the map from quality to deserved yield is not stated (card section 3), so quality orders first
and the gap orders within a band of similar quality.

## 7. Not computable (card rules no dictionary measure can express)

| part | rule | reason |
|---|---|---|
| BUY | RB7 dominance (monopoly / duopoly / oligopoly, dominant for 10 more years) | market share and its durability are not in the dictionary; a judgement (card section 6). |
| BUY | RB8 natural dominance (net benefit, not lock-in) | no observable measure of why customers use the product. |
| BUY | RB9 form of advantage (industry dynamics, technology lead, network effect) | no measure. |
| BUY | RB10 pricing power above inflation | prices per unit are not in accounts; revenue growth mixes price and volume, which he separates. |
| BUY | RB11 cheap, essential, must-have product | price relative to the value delivered is not observable. |
| BUY | RB12 rising industry volumes | no volume data; industry revenue growth would mix in price. |
| BUY | RB15 capital allocation used wisely | a judgement; partly touched by A5 / S2 (acquisitions) and B9 (buybacks), not expressed. |
| BUY | RB18 business "your idiot nephew could run" | no measure of dependence on management. |
| BUY | RB19 many levers to pull | no measure. |
| BUY | RB21 temporary vs structural volume drop | no measure; reflected only in the design: S1 does not sell on B3 or B5, B5 is read over five years, B4 is full form only (v2, C1, C2). |
| BUY | RB22 inflection on a long-dominant business (one case, FICO) | no measure of a change in price-driven vs volume growth, of latent pricing power, or of "others may not have realized"; rests on one case. |
| PRICE | RP1 discounted cash flow value | no discount rate stated; his own model. |
| PRICE | RP3 conservative FCF model without optionality | his own forecast; only the trailing stand-in in P1 is possible. |
| PRICE | RP6 30-60% below intrinsic value | intrinsic value is his own estimate (C3 open). |
| PRICE | RP7 pre-set buy price | his own line in the sand. |
| PRICE | RP10 no sum-of-the-parts valuation | a statement about method; nothing to screen. |
| AVOID | RA6 no fixing up low-quality businesses | judgement; the BUY conjunction keeps low quality out but does not express turnarounds. |
| AVOID | RA10 big technology (FANG) | a named group with a named exception (Amazon); a name list would be chosen with hindsight; no GICS code matches it. |
| AVOID | RA13 scale-based advantage | no measure of the source of advantage. |
| AVOID | RA14 could go down 90% tomorrow | no measure of permanent-loss risk stated. |
| AVOID | RA15 coerced use | no measure (mirror of RB8). |
| SELL | RS1 at 100% of intrinsic value, review | intrinsic value not computable (and it is a review, not a sale; S4 keeps the name). |

Count: 22 (buy 11, price 5, avoid 5, sell 1, size 0). Process rules RO1, RO3-RO16 describe how he works, not what a
screen tests, and are outside the recipe (RO2 is used in S3). RP8 and RP9 are computable stand-ins (P2, P3) but are
full form only in v2.

Computable but left out: RB17 ("holds virtually no cash", usually): a cash test pulls against A6/S5 (no leverage) and
he gives no number; adding it would be a weak rule (brief rule 2).

## 8. The two forms

**Decisive form** (quote and convention numbers only): BUY B1, B2, B3, B5, B6 (5 criteria); PRICE P1 (1); AVOID
A1-A5 (5, + house exclusions); SELL S1-S4 (4); SIZE Z1-Z3 (3); ranking K1 with the decisive quality score. One
version, nothing averaged.

**Full form**: the decisive form plus B4, B7-B13, P2-P5 (P2 and P3 enter through P5), A6-A10, S5-S6, Z4-Z7, with
every grid's versions run and averaged (no version picked), and the revealed-13F sizing (Z5-Z7) in place of Z1-Z2 in
its own version. v1's readings of B4 (decisive), B5 (3 years), the entry trigger and A5 (one window) are each one
version inside B4, B13, P5 and A10.

## 9. Coverage and main risk

Coverage of his 22 buy rules, decisive form: RB2 (B3), RB3 (B1, B2), RB4 (B3), RB6 (B1, B2), RB13 (B5), RB14 (B6),
plus RB1 as the conjunction = 7 of 22 (32%), as in v1; the full form adds RB5 (reported only), RB16 and RB20 = 10 of
22 (45%). Of the 14 buy rules he states always or always/usually, the decisive form expresses 7 (50%), and none of the
four he puts at the centre of the business (RB7 dominance, RB8 natural dominance, RB10 pricing power, RB11 cheap
essential product). The count is unchanged, but RB3 (predictability, "always") is now expressed more thinly: by a
ten-year record and the absence of a loss year, without a steadiness measure (C1). RB21 is still not expressed; v2
only stops two v1 measures from contradicting it. Every expressed rule is a stand-in (accounts for a judgement), not
the rule itself.

Risk that v2 fits his purchases rather than his words: all four substantive changes loosen v1, and each sits exactly
where the feedback showed large rejections (P2 or P3 58.8%, B4 21.1%, B5 20.4%, A5 20.4%), while the rules the feedback
also flagged but whose quotes allow no other reading (B2 28.4%, B3 18.7%, B6 15.2%, P1 18.7%) were left alone; that
pattern is what a fit would look like too, so a higher recall on the same 29 purchases is partly built in and is not
independent evidence. The largest risk is C3: dropping the neglect / scare trigger removes the criterion that rejected
most purchases, and its basis is an inference (the 2:1 split describes entries; additions follow the gap, K189-C005,
K065-C054); an equally possible reading is that the trigger applies to first entries but not to additions, which the
screen cannot apply without knowing the holding, and P5 keeps v1's reading only as a full-form version. The decisive
form now says nothing about timing beyond a positive yield gap, so its base rate will rise and its lift may fall. C1 is
next: it takes a steadiness test of an "always" rule out of the decisive form on the strength of RB21, a "usually"
rule. C2 carries a number risk: five years is a stated convention (the lower end of "five to 10 year" and B3's
window), but it was chosen after seeing that the 3-year window rejects a fifth of his purchases; B13 keeps 3 years as
a version. C4 is the best grounded (v1 already claimed that single offensive deals pass, C6, and its measure did not
deliver it), but the two-window form is new structure and would also pass a company that makes one large purchase
every four to six years. None of the changes uses a forward return or anything after the quarter-end, and no number
was set from the feedback. The card itself failed its held-out test, so v2 should be judged on purchases or documents
it has not been revised against before any of these readings is trusted.
