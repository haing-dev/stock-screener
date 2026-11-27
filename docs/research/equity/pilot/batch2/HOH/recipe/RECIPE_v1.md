# Recipe: Chris Hohn (TCI Fund Management), gate G6

Inputs: CARD.md (THIN: 2 documents, HOH2 2025-05-14, HOH3 2025-11-13, no held-out document), FIELD_DICTIONARY_v1.0.md,
field_dictionary_v0.1.csv, construction_13F.txt. No returns were seen; no number below was set by an outcome.

Applied at each quarter-end to the eligible US stocks (1,500 largest, GICS sector known). Every measure follows the
dictionary's as-known rules (first-reported accounts usable from announcement + 1 day; ratio with denominator <= 0 is
missing; sector percentiles inside the GICS sector at the date). "10y" = the last 10 fiscal years of first-reported
annual accounts; a company with fewer than 10 such years fails any 10y criterion.

Order of application (Rprice1, HOH2-C045 "always": valuation only after the barriers satisfy him):
AVOID -> BUY -> PRICE -> ranking -> SIZE; SELL runs on the held names at the same quarter-end.

Line format: id | card rule(s), claim ids | measure | comparison and number | TAG | why this measure stands in for his words.

## 1. BUY (what qualifies)

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| B1 | Rbuy1 (always), Rbuy5; HOH2-C002, HOH3-C005, HOH2-C005, HOH3-C003, HOH3-C021 | new: S04* = number of the 10y in which Q01 > 15% OR (Q01 denominator, total equity + total debt - cash and short-term investments, <= 0 AND EBIT R08 > 0) | S04* = 10 of 10 | convention | "Competition kills profits": a lasting barrier is the only observable reason a return on capital stays high year after year. Every year (not most) because the barrier must be obvious (Rbuy5) and the rule is "always". The 15% is the dictionary's S04 bar, not his. The OR clause keeps capital-light firms with negative equity (rating agencies, HOH2-C017) from failing on a missing ratio |
| B1i | Rbuy3 (usually; alternative route to B1); HOH2-C006, HOH3-C014, HOH3-C023 | X01 sub-industry in {Airport Services, Highways & Railtracks} AND S01 = 0 | sub-industry in list; 0 loss years in 10y | quote (the two types are named in the cited claims) | Hard-asset infrastructure is a barrier type he names (physical assets) whose accounting return on capital is low by construction, so B1 would reject what he likes; the route replaces the return test with the sub-industry plus no loss year. A stock passes BUY with B1 OR B1i |
| B2 | Ravoid2 (always), Rbuy12; HOH2-C003, HOH3-C046, HOH3-C010, HOH2-C068 | S02 (standard deviation of operating margin, 10y) | in the more stable half of its GICS sector (sector percentile of S02, low = stable, <= 50th) | convention | "No cheap average businesses whose earnings power is unpredictable" and "little change from year to year": a stable margin is the accounting trace of predictable earnings power. Median split = the plain reading of "predictable" when no number is given |
| B3 | Rbuy8 (usually); HOH2-C019, HOH2-C001, HOH3-C049 | none (G01 not used) | no growth criterion | convention | He states growth is not required; adding one would contradict him. Recorded so that no later version adds a growth floor without a new claim |
| B4 | Rbuy7 (usually); HOH2-C018 | S03 (standard deviation of yearly revenue growth, 10y) | in the more stable half of its GICS sector | convention | Recurring, predictable revenue shows as steady revenue growth. FULL FORM ONLY: "usually", and the quote vs note on HOH2-C018 is open on the card |
| B5 | Rbuy13 (usually); HOH2-C040 | count of the pass set (AVOID + BUY + PRICE) | report each quarter vs "maybe 200" | quote | Reported check, not a filter: his ~200 is a global list, so a US pass set well above 200 means the screen is looser than his list |

## 2. PRICE (when cheap enough)

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| P1 | Rprice2, Rsell4; HOH2-C053, HOH2-C062, HOH2-C057 | V13 (free-cash-flow yield V04 minus the 10-year Treasury yield on the day) | V13 >= 0 | convention | Price at or below a long-horizon DCF value. With no discount rate, growth or margin stated, the standard zero-margin reading is a perpetuity of current free cash flow valued at r - g = the 10-year Treasury yield (long-run growth offsets the risk premium). It is lenient on purpose: "doesn't quite matter what you pay" for a really good company "to a point" (HOH2-C057). Free cash flow because a DCF discounts cash, not earnings. V04 <= 0 fails |
| P1g | same | V13 | V13 >= 0, >= +1, >= +2 percentage points; results averaged | grid | FULL FORM ONLY: where "the point" lies is open on the card; three margins, none chosen |

## 3. AVOID (exclusions; applied first)

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A1 | Ravoid1 (always), Rbuy6 (always); HOH2-C015, HOH2-C016, HOH3-C027, HOH3-C028, HOH3-C029 | X01 sector | exclude GICS sector Consumer Discretionary (25) | convention | GICS's own definition of discretionary demand is the standard mapping of "no discretionary things" / "essential product or service"; the card has no other classification |
| A2 | Ravoid3 (always); HOH2-C033, C034, C038, C039 | X01 industry group / sub-industry | exclude: Banks (industry group 4010); Automobiles & Components (2510); retail = Consumer Discretionary Distribution & Retail (2550, formerly Retailing) and Consumer Staples Distribution & Retail (3010, formerly Food & Staples Retailing); Insurance (4030); commodities and commodity manufacturing = Energy (sector 10) and Materials (sector 15); Tobacco (sub-industry 30203010); traditional asset managers = Asset Management & Custody Banks (40203010) | quote (the list is in the cited claims; the GICS mapping is convention) | His "long list of companies we don't invest in", read literally onto GICS. Financial Exchanges & Data and rating agencies (4020) stay in, as his examples require |
| A3 | Ravoid3 (note items); HOH2-C021 (airlines), HOH2-C035-C037 notes | X01 | also exclude Airlines (20302010), Wireless Telecommunication Services (50102010), Media (industry 502010, incl. Advertising 50201010) | convention | FULL FORM ONLY: these come from reader notes (and one example claim), not his listed words. Interactive Media & Services (502030) is not Media and stays in |

## 4. SELL

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S1 | Rsell1 (usually); HOH2-C052, HOH3-C009, HOH3-C012, HOH3-C048 | none | no time-based exit, no price-gain exit, no stop-loss | convention | "Hold the company forever"; no price, loss or time trigger is stated (card section 3) |
| S2 | Rsell1, Rbuy1; HOH3-C012 | S04* (as B1) | sell when S04* < 8 of 10 | convention | Holding needs only that the barrier persists ("hold good companies because their barriers persist"); two years in ten below the bar is the plain sign it no longer shows. Entry needs 10 of 10 (obviousness, Rbuy5); the hold bar is lower so one bad year does not force a sale of a held barrier. For B1i holdings: sell when S01 > 0 |
| S3 | Ravoid1-3 | X01 | sell at the quarter-end a holding is classified into an A1/A2 exclusion | convention | The exclusions are "always" rules |
| S4 | Rsell3, Rsell4; HOH2-C061, HOH2-C062 | V13 and the ranking of section 6 | replace a holding only when (a) its V13 < 0 AND (b) a pass-set stock not held ranks above it; the best such candidate replaces it | convention | "Sell when intrinsic value is not as good as other things" is relative, and "price at or below intrinsic value" is the bound: both conditions together |
| S5 | Rsell2 (outcome); construction_13F "new per year 23%" | count of new names per rolling 4 quarters | at most round(0.23 x N) new names per rolling 4 quarters (2 at N = 9 or 10, 3 at N = 15); excess replacements wait | revealed-13F | FULL FORM ONLY: his US 13F turnover. Report the realised average holding period against his stated 8 years (HOH2-C051) and the 13F median of 6 quarters |

## 5. SIZE

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| Z1 | Rsize1 (usually); HOH2-C071 | number of holdings | N = 10 and N = 15, results averaged | quote | "10 or 15 stocks"; both ends of his range, none chosen |
| Z2 | Rsize1; HOH2-C071 | weight | equal weight 1/N at entry (10% at N = 10) | convention | "10% type holdings" is exactly 1/N at N = 10; equal weight is the plain reading at N = 15 |
| Z3 | Rsell1, Rprocess7; HOH2-C052, HOH2-C082 | weight | no rebalancing of held names (weights drift); exits and entries trade at 1/N of the current book, funded from cash and sale proceeds | convention | An owner holding "forever" does not trim winners; the 13F concentration (top 5 = 85%) is consistent with drift |
| Z4 | Rsize1 | weight | if fewer than N stocks pass, hold all passers at 1/N each and the rest in cash | convention | Concentration is secondary to quality (HOH3-C013): never fill places with stocks that fail |
| Z5 | Ravoid5 (usually); HOH2-C084, HOH3-C040 | book | long only, no short leg | convention | "Rarely short"; the only exception (fraud, HOH3-C043) is not computable |
| Z6 | Rsize1; construction_13F (names 9, effective names 6.0, top-5 85%, top-10 100%, new position 2.7%) | weight schedule | N = 9; weights by rank in the book 27 / 19 / 16 / 12 / 11 / 6 / 4 / 3 / 2 % (top-5 = 85%, effective names 5.97); a new name enters at 2.7% for its first quarter, then takes its rank weight; rebalance to the schedule at each quarter-end | revealed-13F | FULL FORM ONLY: matches the 13F names, top-5, top-10 and effective names; the largest weight is 27% vs the 13F 31% (the four aggregates cannot all be met at once) |

## 6. Ranking inside the pass set (his stated order: barriers first, valuation after)

1. Barrier score = mean of two percentiles taken inside the pass set: new: 10y median of Q01 (a year with denominator
   <= 0 and EBIT > 0 counts as above every other value), higher = better; and S02, lower = better. (Rbuy1 "most important",
   HOH2-C002; Ravoid2.) Ties broken by market value L01c, larger first (HOH2-C060, principle only). TAG convention.
2. Keep the 2N stocks with the highest barrier score (barriers first, Rprice1 HOH2-C045). TAG convention.
3. Among those, order by V13, highest first; the top N are the target book (valuation after, Rprice2). TAG convention.
4. Essential vs discretionary (Rbuy6, ranked equal to barriers, card section 4 "Open") is already a pass/fail in A1, so
   it adds no ranking key.
5. FULL FORM grid (Rbuy3 "likes" hard-asset infrastructure): B1i names ranked first in step 1, on / off, averaged. TAG grid.

## 7. The two forms

DECISIVE FORM (quote and convention numbers only): A1, A2; B1 or B1i, B2; P1 (V13 >= 0); ranking steps 1-4;
SELL S1-S4; SIZE Z1-Z5 (N = 10 and 15 averaged, equal weight at entry, no rebalancing, long only). B3 (no growth
filter) and B5 (pass-set count vs 200) are recorded and reported.

FULL FORM: the decisive form plus B4 (S03 revenue stability), A3 (note exclusions), P1g (V13 margin grid 0 / 1 / 2),
ranking step 5 (infrastructure first on / off), S5 (13F turnover cap) and Z6 (13F weight schedule, N = 9) in place of
Z1-Z3. Every grid is averaged; no value is picked.

Counts, full form: BUY 5 (B1, B1i, B2, B3, B4) + 1 reported check (B5); PRICE 2 (P1, P1g); AVOID 3 (A1-A3);
SELL 5 (S1-S5); SIZE 6 (Z1-Z6) = 21 criteria. Decisive form: BUY 4 (B1, B1i, B2, B3), PRICE 1 (P1), AVOID 2 (A1, A2),
SELL 4 (S1-S4), SIZE 5 (Z1-Z5) = 16. Not computable: 13 (section 8).

## 8. Not computable

| id | card rule, claims | reason |
|---|---|---|
| N1 | Rbuy2; HOH3-C017, HOH3-C027, HOH2-C004 | Number and type of barriers ("maybe five") cannot be counted from accounts, prices or consensus |
| N2 | Rbuy4; HOH3-C015, HOH2-C008 | Network effects and intellectual property have no dictionary measure; GICS does not mark them |
| N3 | Rbuy5; HOH3-C021 | Obviousness is a judgement; only partly covered by the 10-of-10 entry bar in B1 |
| N4 | Rbuy9; HOH2-C023, HOH2-C024, HOH3-C018 | Pricing power needs revenue split into price and volume; accounts give only the total |
| N5 | Rbuy10; HOH2-C028 | Weak competition needs market shares and rivals' conduct; none in the dictionary |
| N6 | Rbuy11 (always); HOH3-C006, HOH3-C047, HOH3-C052 | Being around and dominant in 20-30 years is a forecast; "dominant" = top-2 market share is not computable; B1's 10-year record is the past trace only |
| N7 | Rbuy14 (always); HOH2-C063 | Conviction is a state of the analyst |
| N8 | Rprice3; HOH2-C067 | "Will the business be around?" is a judgement test (same gap as N6) |
| N9 | Ravoid4; HOH3-C026 | "Fast-changing technology" has no definition, and the card's examples (Microsoft, Alphabet, Visa held) rule out excluding the GICS technology sectors |
| N10 | Ravoid3 notes; HOH2-C035-C037 | Fossil-fuel utilities (GICS does not record fuel mix) and "most manufacturing" (no boundary) |
| N11 | Ravoid5 exception; HOH2-C086, HOH3-C043 | Fraud shorts need forensic judgement ("a very high bar") |
| N12 | Rsell2; HOH2-C051, HOH3-C008 | The 8-year average holding is an outcome, not a trigger; reported only (S5) |
| N13 | Rprocess1-8; HOH3-C007, HOH2-C049, C069, C074, C048, C046, C047, C072, C082, C077, HOH3-C031, C033, HOH2-C089 | Research, team, management, reference checks, intuition, engagement and hiring are process; no screen form |

## 9. Coverage and main risk

Coverage of the card's 14 buy rules: the decisive form implements 5 (Rbuy1, Rbuy3, Rbuy6 through A1, Rbuy8 as a
deliberate absence of a growth filter, Rbuy12) = 36%, with Rbuy5 partly; the full form adds Rbuy7 = 6 of 14 = 43%;
Rbuy13 is a reported check. Of the four "always" buy rules, 2 are covered (Rbuy1 by proxy, Rbuy6 by exclusion); the
other two (durability over 20-30 years, conviction) are not computable. Price, avoid, sell and size are covered by
convention, with no number of his own except N = 10 to 15.

Main risk: the recipe is, in effect, a generic quality screen (ten straight years of high return on capital, a
stable margin, not dear against Treasuries, outside his excluded industries), and in the US 1,500 that set is filled
by asset-light, high-margin firms: software, semiconductors and IT services, medical devices and drugs, branded
staples, distributors and data firms. Hohn reaches his few names the other way round, from judged, obvious, multiple
barriers (physical monopolies, network effects, duopolies such as aircraft engines) and essential demand, and he
avoids fast-changing technology that a ten-year return record cannot tell apart from a lasting barrier; patent-cliff
drugs and "not every brand" are further cases where a high return is not his kind of barrier. The infrastructure he
likes most has low accounting returns, and the B1i route covers only airports and toll roads, which barely exist among
US listings, so his hard-asset side is largely missing. With a pass set likely far larger than his 9 US 13F names,
the choice of the final 10-15 is made by our ranking (barrier score, then free-cash-flow yield), not by him; the paper
book can therefore score well or badly for reasons that say little about his method. The card is THIN (two 2025
documents, no held-out test), so the rules themselves rest on two talks given after the period being tested.
