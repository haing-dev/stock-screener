# Recipe: Cliff Sosin (CAS Investment Partners), gate G6

Built from CARD.md v1.1 only (file THIN; held-out test FAILED; SOS1 merged, so v1.1 is untested on unseen material),
FIELD_DICTIONARY_v1.0.md, field_dictionary_v0.1.csv and construction_13F.txt. **construction_13F.txt says there is no
13F construction profile for this investor (not in the eq_conv panel), so no number in this recipe is tagged
`revealed-13F`.** No number was set by looking at any return or holding outcome.

Applied at each quarter-end to the eligible US stocks (1,500 largest, GICS sector known; US primary listing). All
measures as known on the day (dictionary v1.0 rule 1: first-reported accounts usable from announcement + 1 day; TTM =
last four consecutive quarters; ratio with denominator <= 0 = missing). Sector percentile = rank inside the GICS sector
among eligible stocks at the quarter-end, 0 = worst, 1 = best. **For a pass/fail test a missing measure FAILS** (the
book's "missing = 0.5" is a ranking convention, not a pass).

Line format: id | card rule(s) and claim ids | measure | comparison and number | TAG | why this measure stands in for his words

Common definitions used below:
- LOSS = new: EBIT TTM (R08 TR.F.EBIT, sum of last four quarters) <= 0. PROFITABLE = EBIT TTM > 0.
- IND_PCT(m) = new: percentile of measure m among eligible stocks in the same GICS industry (6 digits) at the
  quarter-end; if the industry has fewer than 5 eligible stocks, use the industry group (4 digits); if still fewer than
  5, the sector (2 digits). Higher = better.
- SEC_PCT(m) = percentile of m inside the GICS sector (dictionary rule 4), higher = better (for V14, lower V14 = better,
  so the percentile is taken on -V14).

## 1. BUY (what qualifies)

- B1 | Rbuy2 (SOS2-C023 both, SOS3-C030 third, SOS3-C031 third; outcome SOS3-C019; margin vs industry SOS1-C022) + Ravoid1 (SOS3-C077 both, SOS3-C075 both) | Q04 gross margin (R03 or R01-R02, over R01, TTM), as IND_PCT(Q04) | IND_PCT(Q04) > 0.50 (margin above the median of its industry) | convention | His one named comparison for the advantage is margins "so much higher than everybody else's" (SOS1-C022), and SOS3-C019 names good margins as the outcome of the gadget; "higher than everybody else's" read as at least above the industry middle. Gross margin, not operating margin, because Ravoid2 says loss-makers are NOT excluded: gross margin is defined for a loss-maker, operating margin would exclude every one by construction. A narrow advantage (Ravoid1, "move on") = failing B1.
- B2 | Rbuy2 (SOS3-C019: "high return on capital") | Q01 return on invested capital | SEC_PCT(Q01) > 0.50; applies to PROFITABLE stocks only; LOSS stocks are exempt and handled by A1 | convention | SOS3-C019 names high return on capital as the outcome of an enduring advantage; "high" read as above the sector median. Exempting loss-makers keeps Ravoid2's "not excluded" (a loss-maker's ROIC is negative by construction; he underwrites its path to profit instead, SOS3-C074).

## 2. PRICE (when cheap enough)

- P1 | Rprice1 (SOS3-C033 both, SOS2-C026 both; margin of safety SOS1-C044) | PROFITABLE: V01 earnings yield (EBIT TTM / EV); LOSS: V03 forward earnings to price (consensus EPS next 12 months / price) | SEC_PCT(V01) >= 0.50 for PROFITABLE; SEC_PCT(V03) >= 0.50 and V03 > 0 for LOSS | convention | "Does it make a lot of money relative to the price?" = earnings per unit of price; "a lot" read as at least as much as the typical stock in its sector. For a loss-maker he prices the path to profit (Cardlytics, Carvana examples SOS2-C049, SOS1-C020); the consensus forward earnings is the only computable stand-in for that path. The margin of safety (SOS1-C044) has no size: the sector-median bar is the only convention applied.

(The "will it grow a lot relative to the price?" half of Rprice1 is used in the ranking, section 6, not as a gate:
he states the direction, "higher earnings and growth per unit of price = better", not a bar.)

## 3. AVOID (exclusions)

- A1 | Ravoid2 (SOS3-C079 both, SOS3-C074 both; lesson SOS3-C073) | LOSS (new: EBIT TTM <= 0) | LOSS stocks are not excluded; in the ranking they come after every PROFITABLE stock in the pass set | convention (0 = the card's own measure "operating profit below zero") | "Not excluded, but less interest": ranking them last is the plain reading of "less interest"; the size of his haircut is not stated (full form adds it as a grid).
- A2 | Ravoid3 (SOS3-C086 both; SOS3-C085) | US primary listing (universe rule) | Non-US stocks would go last; the eligible universe holds only US stocks, so the rule never binds | convention | He ranks non-US last, not out; with a US-only universe this is satisfied by construction.

Industries he excludes: **none** (card section 6: no sector limits stated; the SOS1 sector cautions on prime lending,
subprime lending, low-growth multi-level marketers and chemicals have rule_status no and are not rules). Outside the
recipe, as a **measurement scope** (not his rule): GICS industry groups 4010 Banks and 4030 Insurance, and Real Estate
(group 4040 / sector 60) are not scored, because B1 (gross margin) and P1 (EBIT / EV) are not defined for them in the
dictionary; this is the engine's registered generic exclusion. Biotech (sub-industry 35201010) is NOT dropped: he says
AI tools make life-science and biotech companies more approachable (SOS1-C054); most are LOSS and go to the bottom by A1.

## 4. SELL

- S1 | Rsell1 (SOS3-C010 both, SOS3-C009 both; SOS2-C010; SOS1-C031) + Rsell4 (SOS2-C061 both) | none (rule of omission) | A holding is never sold because it fails P1 (price) or because its weight or price has risen; no valuation or price-loss trigger | convention | He owns "with a premise of owning it forever", sells only to upgrade, on misunderstanding or on model failure; valuation sales were an early-career practice he left (card section 4, later wins).
- S2 | Rbuy6 (SOS3-C088 third; SOS3-C089) + Rsell1 "upgrade" (SOS3-C010; United Rentals -> Ashtead SOS2-C010) | ranking score of section 6, recomputed each quarter-end for holdings and candidates | A non-held stock in the pass set replaces the lowest-scored holding only if its score is higher than that holding's score; at most one such swap per quarter-end | convention | "A new idea must beat what he already holds": beating = a higher score on the same yardstick. He gives no margin, so none is added.
- S3 | Rsell2 (SOS3-C011 both, SOS3-C012 both; examples SOS1-C036, SOS1-C038, SOS1-C039, SOS1-C040) | B1 at the quarter-end | A holding that fails B1 (gross margin no longer above its industry median) is sold at that quarter-end and its slot is refilled from the top of the ranked pass set | convention | He sells when outcomes no longer line up with his model of the business; the only machine-readable part of the model is the advantage proxy the stock was bought on. The example re-basing of growth (SOS1-C038) has no threshold and is not used.
- S4 | Rsell3 (SOS3-C014 both) | count of upgrade swaps (S2) in the last four quarter-ends | Upgrade swaps (S2) allowed only if none happened in the previous three quarter-ends (at most 1 per rolling year). S3 sales are not blocked by S4 but are counted and reported against "about one a year" | quote (1 a year: "on average one position bought and/or sold a year"); mechanical form (rolling four quarters) = convention | The number is his; the cap applies to the discretionary swaps so that a broken thesis is never held only to meet a turnover target.

## 5. SIZE

- Z1 | Rsize1 (SOS3-C013 both, SOS3-C090 third, SOS3-C009 both) | number of slots N | N = 6 | convention (midpoint of the quoted 4-8; 4, 8 and "up to 10" are quote) | He states four to eight, up to ten once; with no 13F profile the decisive form takes the middle of his own range.
- Z2 | Rsize1 (no weighting rule stated, card section 3) | slot weight | Each slot = 1/N of capital at entry; a slot with no stock that passes stays in T-bills (no stock that fails B1 or P1 is bought to fill it) | convention | No weighting rule is stated; equal slots are the neutral reading of "a handful". Waiting in cash follows "study adjacent businesses while waiting" (Rprocess7, SOS3-C046) and Rbuy6 (only buy what beats the alternative).
- Z3 | Rsell4 (SOS2-C061 both; SOS1-C032, SOS1-C033) | holding weight | No rebalancing and no trimming: weights drift with price between entries and exits; proceeds of a sale go to the replacement only | convention | He rejects trimming a winner by rule ("diversifying once something went over 30%" is the rule he rejects); the open cap on adding (Rsize2) has no amount and is not applied.

## 6. Ranking inside the pass set (paper portfolio of N names)

His stated order: business and price first, management after (Rbuy1, SOS3-C053 both; management not computable);
loss-makers less interest (Ravoid2); narrower advantages less interest (Ravoid1); non-US last (Ravoid3, does not bind);
"higher earnings and growth per unit of price = better" (Rprice1).

1. PROFITABLE before LOSS (A1).
2. Inside each group: SCORE = 0.5 x BUSINESS + 0.5 x PRICE (Rbuy1 names business and price together with no weights:
   equal halves, convention).
   - BUSINESS = IND_PCT(Q04) (wider margin lead = wider advantage, Ravoid1).
   - PRICE = mean of SEC_PCT(V01) (LOSS: SEC_PCT(V03)) and SEC_PCT(-V14) (V14 = forward P/E over expected EPS growth;
     lower = more growth per unit of price). If V14 is missing (no growth estimate, or growth <= 0), PRICE = the
     earnings-yield percentile alone.
3. Ties: larger company market value (L01c) first (convention).

Portfolio: at the first quarter-end, hold the top N of the ranked pass set. After that, only S2 (upgrade, capped by S4)
and S3 (thesis break) change holdings; a stock that leaves the pass set on price stays (S1).

## 7. DECISIVE form (quote and convention numbers only)

B1 (IND_PCT(Q04) > 0.50) and B2 (SEC_PCT(Q01) > 0.50, PROFITABLE only) and P1 (sector percentile >= 0.50 on V01, or on
V03 > 0 for LOSS); A1 (LOSS ranked last, no haircut beyond that); A2 (US universe); S1-S4 (S4 at 1 swap per rolling
year); Z1 N = 6; Z2 equal slots, empty slots in T-bills; Z3 no trimming; ranking of section 6.

## 8. FULL form (decisive form plus grids; every grid point run and the results averaged, never picked)

- G-B1 | B1 bar | IND_PCT(Q04) > {0.50, 0.67, 0.80} | grid | "so much higher than everybody else's" can be read from above the middle to top fifth; no number given.
- G-P1 | P1 bar | sector percentile >= {0.50, 0.67, 0.80} | grid | size of the margin of safety not stated (SOS1-C044).
- G-A1 | Ravoid2 haircut on a LOSS stock's forward earnings before P1 and ranking | V03 x (1 - h), h in {0, 0.25, 0.50} | grid | "underwrites the path to profit with a haircut", size not stated (SOS3-C074).
- G-Z1 | N | {4, 6, 8} | grid (end points are quote) | his stated range four to eight.

Grid size 3 x 3 x 3 x 3 = 81 versions, equal weight. B2, S1-S4, Z2, Z3 and the ranking are the same in every version.

## 9. Not computable (card rules no dictionary measure can express)

Fully not computable (17):
- Rbuy3 | simple enough to understand but hard enough that others miss it (SOS3-C025 third) | no measure of simplicity or of what others miss.
- Rbuy4 | good businesses others do not think good; a worry that scares others away (SOS2-C015 third; SOS3-C038, SOS1-C005) | short interest (O01) is the card's proxy, but he never searches for battleground stocks (Rprocess2, always) and doubt is "a feature of what he ends up owning, not a search filter" (card section 4). Not used as a gate; O01 may be shown beside the names, not scored.
- Rbuy5 | management reasoning quality, weighted more than before (SOS2-C033, SOS2-C037, SOS3-C056 both) | no measure of reasoning; founder / insider control "isn't necessarily an absolute requirement" (SOS2-C035), so O02 is not a stand-in.
- Rprice2 | market-share sizing exercise (SOS2-C048 third) | needs his own addressable-market estimate per company.
- Rsize2 | no adding above a certain share of the fund (SOS3-C065 both) | amount not stated; open contradiction with the 30% and mid-40s% weights (card section 4).
- Rsize3 | buy more on a fall when his data say the business is fine (SOS1-C016 third) | needs his own data reading (Rprocess6); no size of fall or amount.
- Rprocess1-Rprocess11 (11 rules) | idea sourcing, rigour, management judgement, evidence sources, alternative data, reading, AI use, independence, call technique, expert transcripts | these are how he works, not properties of a stock. Rprocess1 (always) says he uses NO quantitative screen: the recipe exists only as the machine stand-in the pipeline needs.

Partly not computable (4; the computable part is in the recipe):
- Rbuy1 | management as the third criterion (SOS3-C053) | only the business-and-price ordering is used.
- Rbuy2 | "enduring", "layered and interwoven", "invariant to technological change" (SOS3-C030, SOS3-C031, SOS3-C017, SOS3-C018) | only the outcome proxies (margin vs industry, return on capital) are used; past-stability measures (S02, S04) are not, because the card speaks of the advantage's future durability and Ravoid2 admits young loss-makers.
- Rprice1 | extrapolating the long-term future from the gadget and the size of the margin of safety (SOS3-C033, SOS1-C044) | trailing EBIT / EV and consensus forward earnings stand in for his long-run estimate.
- Rsell2 | a thesis-breaker named in advance (SOS1-C040, SOS1-C042) and growth re-basing (SOS1-C038) | qualitative and no threshold; only "the bought-on advantage proxy fails" (S3) is used.

## 10. Coverage and main risk

Buy rules covered: 3 of 6 (50%), and only one in full: Rbuy6 (S2, upgrade only if the new name scores higher); Rbuy1
(business-and-price ordering, management dropped) and Rbuy2 (outcome proxies only) partly; Rbuy3, Rbuy4, Rbuy5 not at
all. Of his two "always" buy rules (Rbuy1, Rbuy4), one is partly covered and one not. Price: Rprice1 partly, Rprice2 not
(1 of 2 partly). Counting buy plus price rules: 4 of 8 touched, 1 fully.

Main risk. Sosin's edge, in his words, is owning a handful of good businesses that the market does NOT think are good,
found one at a time without any screen (Rprocess1, always), and his named holdings are of that kind: doubted, heavily
shorted, often loss-making or just crashed, priced on a long-run earnings path he estimates himself (Carvana, Cardlytics,
Herbalife). The recipe instead picks profitable companies whose margins and returns already stand above their peers on
first-reported accounts and that look cheap on trailing or consensus earnings, i.e. a generic sector-relative
quality-and-value basket. Such companies are mostly ones the market already sees as good (or cheap for visible reasons),
which is the opposite of his pari-mutuel premise; the doubt he seeks is deliberately not scored (Rbuy4 vs Rprocess2),
loss-makers are pushed to the bottom (A1) although his largest position was one, and trailing EBIT / EV cannot see the
normalised earnings he paid for. So a pass or fail of this recipe will mostly test "concentrated, low-turnover
sector-relative quality-value", not Sosin's judgement; and because the card is thin, failed its held-out test, and has no
13F construction profile, even the construction numbers (N, turnover) rest on single 2025 quotes.

## Count

Criteria per part: BUY 2 (B1, B2), PRICE 1 (P1), AVOID 2 (A1, A2), SELL 4 (S1-S4), SIZE 3 (Z1-Z3); ranking rule 1;
full-form grids 4. Not computable: 17 rules fully + 4 partly (21 entries). Tags: quote 1 (S4's number; plus the end points
of the Z1 range), convention 11 (B1, B2, P1, A1, A2, S1, S2, S3, Z1, Z2, Z3; also S4's rolling-year form and the
ranking weights), grid 4, revealed-13F 0 (no 13F profile).
