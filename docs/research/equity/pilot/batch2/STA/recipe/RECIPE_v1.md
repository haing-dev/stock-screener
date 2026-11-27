# Recipe: Murray Stahl (Horizon Kinetics), gate G6

Inputs: CARD.md v1.1 (labels: thin; held-out FAILED, STA2 merged), field_dictionary_v0.1.csv, FIELD_DICTIONARY_v1.0.md,
construction_13F.txt (2 filers, 102 filer-quarters, 2010-2025, no returns). No outcome of any kind was seen; no number
below was chosen with sight of a result.

Applied at each quarter-end to the eligible US stocks (1,500 largest by L01c, GICS sector known). All measures as known
on the day (dictionary v1.0 rule 1: first-reported accounts usable from announcement + 1 day; TTM = last four
consecutive quarters; ratio with a denominator <= 0 = missing). "Sector median / percentile" = among ranked universe
members of the same GICS sector at that quarter-end (dictionary rule 4). A missing measure FAILS a gate unless the line
says otherwise.

Line format: id | card rule(s) and claim ids | measure | comparison and number | TAG | why this measure stands in for his words

## 1. BUY (what qualifies)

Pass = B1 AND B2 AND (B3 OR B4). B3 and B4 are his two measures of the same neglect idea (card section 4 item 6), kept
as alternatives so each can be checked on its own.

- B1 | Rbuy2 (STA3-C047, C048: "rare company that's not likely to access the capital markets") | new: Q06 (FCF TTM / revenue TTM) > 0 OR B04 ((cash and short-term investments - total debt) / L01c) >= 0 | FCF margin > 0, or net cash >= 0 | convention | A company that funds itself from its own cash flow, or holds more cash than debt, has no need to go to the capital markets; the OR keeps firms whose assets are dormant (low current cash flow, Rbuy1) but which carry no net debt.
- B2 | Rbuy2 (STA3-C047, C048) and Rbuy3 (STA3-C080; support C074, C075: TPL shares down about 3% a year) | C04 (diluted shares now / diluted shares 12 quarters earlier, split-adjusted as in B05) | <= 1.00 (share count not up over 3 years) | convention | "Not likely to access the capital markets" read as no net equity issuance; flat counts (royalty trusts) pass, buybacks pass. TPL's 3% a year is an example, not a threshold, so no buyback rate is required here.
- B3 | Rbuy3 (STA3-C080 "not included in any index" and "keep buying back their stock"; support STA3-C043, C044, STA2-C013) | O05 (share held by the three largest index managers, latest 13F holdings filed by the quarter-end) AND C04 | O05 below the sector median AND C04 < 1.00 (share count down over 3 years) | convention | Index membership is not in the dictionary and almost every stock in the 1,500 largest sits in some broad index, so "outside every index" is read as least owned by index funds; "below the median" is the minimal reading of a comparative where no level is given. The strict C04 < 1.00 is his second, conjoined condition ("keep buying back").
- B4 | Rbuy4 (STA2-C009 "traffic in the world of less scrutinized"; support STA2-C006, C007, C008, C012, C001) | E05 (number of estimates in the FY1 mean, latest within 35 days before the quarter-end; no estimate = 0, which passes) | below the sector median | convention | The card's own proxy for scrutiny is analyst coverage; "less scrutinized" is a comparative with no level, read as below the middle of the sector.

Full form only (replaces the B3 and B4 cut-offs, everything else unchanged):
- B3g | as B3 | O05 | below the sector percentile c, c in {0.33, 0.50}, results averaged | grid | No level stated; two readings of "few owners", the decisive 0.50 and a stricter third.
- B4g | as B4 | E05 | below the sector percentile c, c in {0.33, 0.50}, results averaged | grid | As B3g.

## 2. PRICE (when cheap enough)

He states no valuation level (card section 3 and 6). The decisive form has no PRICE criterion.

Full form only:
- P1 | Rprice1 (STA1-C030, third; support C031; example San Juan Basin Royalty Trust, dividend cut to zero) | new: DPS TTM (R16) <= (1 - d) x DPS TTM four quarters earlier, with DPS TTM four quarters earlier > 0; AND P03 (close / highest close of the last 12 months - 1) <= -f; AND Q05 (operating margin TTM) > 0 | d in {0.5, 1.0}; f in {0.25, 0.40}; Q05 > 0; four combinations averaged | grid (d = 1.0 is the "cut to zero" in the quote, an example only) | Dividend cut and the price fall are what he names; "production still cost-effective" is read as a positive operating margin. Use: inside the pass set, names meeting P1 rank ahead of all others (it is a "sometimes" rule, so it orders entry and never gates it).

## 3. AVOID (exclusions)

None. He states no exclusion rule and names no industry to avoid (card section 3); he rejects sector labels as
non-predictive (STA3-C035, card section 4 item 4). The 13F aggregates carry no sector information. No AVOID criterion
is added. Note for registration: if the generic-book exclusions of dictionary X01 are applied to this pod (groups 4010,
4030, 4040, sector 60, sub-industry 35201010), sector 60 (Real Estate) removes land owners of the kind he names
(STA2-C011, C012); those exclusions are not his and are listed here so the registration step can decide them.

## 4. SELL

- S1 | Rsell2 (STA2-C021, C022, C025: "we don't throw out dirty water until we have clean water"), Rsell4 (STA2-C047; support C048, C049), Rsell1 direction (STA3-C082) | the BUY gates of section 1 and the ranking K1 | A holding is sold (whole position) only when, at a quarter-end, (a) it fails the BUY pass AND (b) a pass-set name not held is available to take its place and is bought with the proceeds the same day. Never sold on price, on a fall in rank, on weight, or on leaving the 1,500 largest while it still has data (it is then judged on the same gates against its sector's universe median). Failing holdings are paired worst-ranked first with the best-ranked unheld names. Delisting or takeover: proceeds held as cash to the next quarter-end. | convention | "Inferior prospective return" has no measure; a holding that no longer meets his own entry criteria is the stand-in for the inferior one, and the sale waits for the replacement in hand (C025). Price and momentum are excluded as triggers because he rejects swapping on falling off the new-high list (C047, C048). Selling the whole position (not "some") is the paper-portfolio convention.

Full form only:
- S2 | Rsell2, Rsell1 (high bar to sell) | replacements per rolling four quarter-ends | <= 13% of N, rounded to the nearest whole name (3 for N = 21 or 22) | revealed-13F ("new per year 13%") | Holds the paper book to the rate at which his own book took in new names. Consistent with the 13F holding record (median holding 29 quarters; still held after 1 / 3 / 5 years 93 / 78 / 64%), which is not used as a parameter.

## 5. SIZE

- Z1 | Rsize1 (STA2-C014: "less than 5%" at the start; support C026, C029) | weight at purchase | a new name enters at the proceeds of the sale it replaces, capped at 4.99% of portfolio value; any excess is added pro rata to the current holdings | quote (5%) | Direct statement of the starting size.
- Z2 | Rsize1 (STA2-C014) | number of names N at the first formation | N = 21, equal weight 1/21 = 4.76% | quote (derived: the smallest N whose equal weight is below the quoted 5%) | He gives no number of holdings; 21 is the smallest book that obeys his start size. The 13F effective number of names (21.1) agrees; it is a check, not the source. The 20-name portfolio of STA2-C015 is hypothetical and not used.
- Z3 | Rsize2 (STA2-C016; support C015, C017, C018, C019, C020) | rebalancing | none: weights drift, no trim and no cap at any size; dividends are held as cash and added pro rata at the next quarter-end | convention | "Leave winners alone, do not trim them to cap their size." The 13F agrees (largest weight median 13%, 90th percentile 55%).

Full form only:
- Z1r | Rsize1, Rsize2 | weight at purchase | a new name enters at 0.9%; the rest of the sale proceeds is added pro rata to the current holdings | revealed-13F ("new position starts at 0.9%"; additions are 49% of his buys) | His book starts names well below the 5% ceiling and adds to existing holdings.
- Z2g | as Z2 | N | N in {21, 22}, averaged | revealed-13F (21 = effective names 21.1; 22 = names >= 1%) | The two 13F readings of how many positions matter in his book.

## 6. Ranking inside the pass set (paper portfolio of N names)

- K1 | Rbuy3, Rbuy4, Rbuy2 (support STA1-C022, STA3-C054: royalty and land firms need no reinvestment) | mean of four sector percentiles, each reversed so that low = good: E05 (fewer estimates), O05 (less index-fund ownership), C04 (more shares retired), C01 (capex / revenue TTM, less reinvestment); missing = 0.5 (dictionary rule 4), except E05 with no estimate = 0 | highest mean first; ties: smaller L01c first (STA3-C043, "too small to be in an index") | convention (equal weights) | He states no order of preference among his buy rules; the ranking weights his neglect measures and the no-reinvestment attribute equally. Full form: P1 names first, then K1.

## 7. Decisive and full forms

- DECISIVE (quote and convention only): BUY B1, B2, B3, B4; PRICE none; AVOID none; SELL S1; SIZE Z1, Z2, Z3; ranking K1.
- FULL: BUY B1, B2, B3g, B4g; PRICE P1; AVOID none; SELL S1, S2; SIZE Z1r, Z2g, Z3; ranking P1 then K1. Grid
  combinations: B3g x B4g x P1 x Z2g = 2 x 2 x 4 x 2 = 32 versions, all averaged with equal weight; no version is
  picked.

## 8. Not computable

Card rules no dictionary measure can express (11):
1. Rbuy1 (dormant assets, STA3-C039): no measure of assets that could produce but do not; no definition of "hard asset"; the one figure (Franco Nevada, 2/3 to 70% non-producing, STA1-C025) is company-reported reserve data, not in the dictionary.
2. Rbuy5 (private companies, STA2-C043, C046): private companies are outside the listed universe; hurdles not stated.
3. Rbuy6 (private, no competition or proprietary, STA2-C045): private scope; no measure of competition or of "proprietary".
4. Rprice2 (private, not on cash flow, STA2-C044): private scope.
5. Rsell1 (no sale without a very compelling reason, STA3-C082): said of TPL only; its general content enters through S1.
6. Rsell3 (sell some of a big position that lost appreciation potential, STA2-C023): "appreciation potential" has no measure, and the share to sell is not given; no size-based trim is made (Z3).
7. Rprocess1 (index products, STA3-C030 to C032): the firm's index business, not stock selection.
8. Rprocess2 (hold unconventional positions, STA3-C061): no measure of "off the beaten track" beyond the neglect gates B3, B4.
9. Rprocess3 (read printed originals, STA3-C069, C071, STA2-C052): a research habit.
10. Rprocess4 (crypto in the commodity bucket, STA1-C044): not a US-stock rule.
11. Rprocess5 (zero management pay at FRMO, STA3-C068): his own firm's policy.

Parts of used rules that are not computable (expressed only by proxy): the literal "not included in any index" of
Rbuy3 (proxy O05); "executing its business plan" in Rsell4 (only its "do not sell on price" half is implemented);
"production still cost-effective" in Rprice1 (proxy Q05 > 0). Principles that are not card rules are not used:
owner-operators (O02 exists, but no verified rule, STA3-C012, C029, C036 to C038), spin-off parents (STA3-C041), long
product life cycles (STA2-C010).

## 9. Coverage and main risk

Coverage: the recipe implements 3 of his 6 buy rules (50%): Rbuy2 in part (self-funding and no issuance, not the scarce
hard asset), Rbuy3 and Rbuy4 by proxy; of the 4 buy rules that apply to listed stocks it covers 3 (75%). The core rule,
Rbuy1 (dormant assets), is not covered. Price: 1 of 2 rules, full form only.

Main risk: the recipe screens for attributes that surround his idea, not the idea itself. It selects self-funding,
share-retiring companies with low index-fund ownership or thin analyst coverage in every sector, which in the 1,500
largest US stocks will mostly be mid-cap industrials, consumer, software or controlled companies with nothing to do with
land, royalties, scarce licences or dormant hard assets, the things his examples share (TPL, Franco Nevada, San Juan
Basin, LandBridge, exchanges). Two further gaps push the same way: the universe of the 1,500 largest leaves out the
small, unindexed firms he names (Dundee, Urbana, SJT at about $150 million), so the neglect gates measure relative, not
absolute, neglect among stocks that are all in some index; and a generic sector-60 exclusion, if applied, would remove
land owners. The recall test on his own purchases (the step after this recipe) is where this shows: a low hit rate there would mean the
recipe found a "neglected compounder" style rather than his hard-asset style.
