# Recipe v2: Chris Hohn (TCI Fund Management), gate G8 revision round (A10 item 9)

Inputs: RECIPE_v1.md, CARD.md (THIN: 2 documents, HOH2 2025-05-14, HOH3 2025-11-13, no held-out document),
FIELD_DICTIONARY_v1.0.md, field_dictionary_v0.1.csv, construction_13F.txt, RECALL_FEEDBACK.md (recall of v1, decisive:
15.9%, base 7.1%, lift 2.24, 90% [1.42, 3.17]; gate failed on recall < 25%). No returns were seen. The feedback was used
only to see WHERE v1 may misread him; every change below rests on a card claim, and no number was set or moved by the
feedback (every number is `quote`, `convention` with its standard reading, or `grid`, as in v1).

## 0. Changes from v1

| id | v1 | v2 | claim ids | why (one line) |
|---|---|---|---|---|
| C1 (B1) | S04* = 10 of 10: Q01 > 15% in every one of the 10y | 10y median of Q01 > 15% (same OR clause for capital <= 0; same 10-year record required) | HOH2-C002, HOH3-C005, HOH2-C005, HOH3-C003, HOH3-C046; HOH3-C021 re-read | His words ask for barriers "strong enough over the long term" because "Competition kills profits": a long-run level of return, not a perfect count of years; v1 took "every year" from obviousness (HOH3-C021), which is a judgement of the barrier (N3), not a count of years, and v1's own ranking already measures the barrier by the 10y median |
| C2 (B2) | decisive: S02 in the more stable half of the sector | FULL FORM ONLY; S02 stays in the ranking (section 6) | HOH2-C003 (Ravoid2), HOH3-C046 (Rbuy12) | Ravoid2's object is "cheap average businesses whose earnings power is unpredictable": an average business is what B1 rejects; the stability reading rests on Rbuy12 ("usually", "little change from year to year", no measure), and a sector median split calls half of every sector "unpredictable", which he does not say |
| C3 (A1) | exclude GICS sector 25 as coded at the date | exclude GICS sector 25 as coded at the date EXCEPT industry group 2540 (Media, in sector 25 until the 2018 GICS change); media stays a full-form exclusion (A3) | HOH2-C016, HOH3-C028, HOH3-C029; HOH2-C035-C037 (media = note) | "No discretionary demand" is about the demand for the product; the 2018 GICS move of Media out of sector 25 changed a label, not demand, so v1 excluded media in the decisive form only before 2018 although v1 itself rules media a note-only (full-form) exclusion |
| C4 (S2) | sell when S04* < 8 of 10 | sell when the B1 test fails (10y median of Q01 <= 15%); B1i holdings unchanged (sell when S01 > 0) | HOH3-C012, HOH2-C052 | Follows C1: "hold good companies because their barriers persist"; the median test already tolerates bad years, so the separate looser hold bar is no longer needed and would now be stricter than entry |

Kept although the feedback shows they reject purchases (rule 3; the quotes still support them): the 10-year record
inside B1 (missing for 9.6% of purchases; Rbuy11 "what's going to be around rather than what's new", HOH3-C006,
HOH3-C047, HOH3-C052, gives no ground for a shorter record), P1 (12.4%; Rprice2 and Rsell4, HOH2-C053, HOH2-C062), B4
(full form, 35.7%; Rbuy7, HOH2-C018), P1g (full form; grid). A2 and A3 reject none and are unchanged.

---

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
| B1 | Rbuy1 (always), Rbuy12; Ravoid2 (always) through "average"; HOH2-C002, HOH3-C005, HOH2-C005, HOH3-C003, HOH3-C046, HOH2-C003 | v2: 10y median of the yearly Q01 values. A year whose Q01 denominator (total equity + total debt - cash and short-term investments) is <= 0 counts as above every other value if EBIT R08 > 0 and below every other value if EBIT <= 0; a year with Q01 missing for any other reason counts as at or below 15% | median > 15%; all 10 fiscal years must exist | convention | "Competition kills profits": a lasting barrier is the observable reason a return on capital stays high over the long term ("strong enough over the long term", Rbuy1; "things that compound over the long term", Rbuy12). The long-run level is the 10y median, the same measure v1 uses for barrier strength in the ranking; it lets a recession or write-off year pass, which a barrier survives. The 15% is the dictionary's S04 bar, not his. A business below it is the "average business" of Ravoid2. The OR clause keeps capital-light firms with negative equity (rating agencies, HOH2-C017) from failing on a missing ratio |
| B1i | Rbuy3 (usually; alternative route to B1); HOH2-C006, HOH3-C014, HOH3-C023 | X01 sub-industry in {Airport Services, Highways & Railtracks} AND S01 = 0 | sub-industry in list; 0 loss years in 10y | quote (the two types are named in the cited claims) | Hard-asset infrastructure is a barrier type he names (physical assets) whose accounting return on capital is low by construction, so B1 would reject what he likes; the route replaces the return test with the sub-industry plus no loss year. A stock passes BUY with B1 OR B1i |
| B2 | Rbuy12 (usually), Ravoid2; HOH3-C046, HOH2-C003, HOH3-C010, HOH2-C068 | S02 (standard deviation of operating margin, 10y) | in the more stable half of its GICS sector (sector percentile of S02, low = stable, <= 50th) | convention | FULL FORM ONLY (v2): "little change from year to year" (Rbuy12, "usually") read as a stable margin, median split as the plain reading of "predictable" when no number is given. Not decisive because Ravoid2's quote is about "cheap average businesses", which B1 removes, and Rbuy12 names no measure. S02 still enters the decisive ranking (section 6) |
| B3 | Rbuy8 (usually); HOH2-C019, HOH2-C001, HOH3-C049 | none (G01 not used) | no growth criterion | convention | He states growth is not required; adding one would contradict him. Recorded so that no later version adds a growth floor without a new claim |
| B4 | Rbuy7 (usually); HOH2-C018 | S03 (standard deviation of yearly revenue growth, 10y) | in the more stable half of its GICS sector | convention | Recurring, predictable revenue shows as steady revenue growth. FULL FORM ONLY: "usually", and the quote vs note on HOH2-C018 is open on the card |
| B5 | Rbuy13 (usually); HOH2-C040 | count of the pass set (AVOID + BUY + PRICE) | report each quarter vs "maybe 200" | quote | Reported check, not a filter: his ~200 is a global list, so a US pass set well above 200 means the screen is looser than his list (watch this after C1-C3, which all loosen the pass set) |

## 2. PRICE (when cheap enough)

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| P1 | Rprice2, Rsell4; HOH2-C053, HOH2-C062, HOH2-C057 | V13 (free-cash-flow yield V04 minus the 10-year Treasury yield on the day) | V13 >= 0 | convention | Price at or below a long-horizon DCF value. With no discount rate, growth or margin stated, the standard zero-margin reading is a perpetuity of current free cash flow valued at r - g = the 10-year Treasury yield (long-run growth offsets the risk premium). It is lenient on purpose: "doesn't quite matter what you pay" for a really good company "to a point" (HOH2-C057). Free cash flow because a DCF discounts cash, not earnings. V04 <= 0 fails |
| P1g | same | V13 | V13 >= 0, >= +1, >= +2 percentage points; results averaged | grid | FULL FORM ONLY: where "the point" lies is open on the card; three margins, none chosen |

## 3. AVOID (exclusions; applied first)

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A1 | Ravoid1 (always), Rbuy6 (always); HOH2-C015, HOH2-C016, HOH3-C027, HOH3-C028, HOH3-C029 | X01 sector and industry group, as coded at the date | v2: exclude GICS sector Consumer Discretionary (25) except industry group 2540 Media (which sat in sector 25 until the 2018 GICS change and is no longer part of it); i.e. sector 25 as GICS now defines it | convention | GICS's own definition of discretionary demand is the standard mapping of "no discretionary things" / "essential product or service"; the card has no other classification. The definition is held fixed over time because his words are about demand, which the 2018 relabelling did not change; this also makes the WRDS form (history of codes) and the LSEG form (today's codes) agree. Media is excluded by A3 (full form), where v1 already placed it as a note-only exclusion (HOH2-C035-C037). Uses only codes known at the date |
| A2 | Ravoid3 (always); HOH2-C033, C034, C038, C039 | X01 industry group / sub-industry | exclude: Banks (industry group 4010); Automobiles & Components (2510); retail = Consumer Discretionary Distribution & Retail (2550, formerly Retailing) and Consumer Staples Distribution & Retail (3010, formerly Food & Staples Retailing); Insurance (4030); commodities and commodity manufacturing = Energy (sector 10) and Materials (sector 15); Tobacco (sub-industry 30203010); traditional asset managers = Asset Management & Custody Banks (40203010) | quote (the list is in the cited claims; the GICS mapping is convention) | His "long list of companies we don't invest in", read literally onto GICS. Financial Exchanges & Data and rating agencies (4020) stay in, as his examples require |
| A3 | Ravoid3 (note items); HOH2-C021 (airlines), HOH2-C035-C037 notes | X01 | also exclude Airlines (20302010), Wireless Telecommunication Services (50102010), Media (industry 502010, incl. Advertising 50201010; before 2018 the same companies under industry group 2540) | convention | FULL FORM ONLY: these come from reader notes (and one example claim), not his listed words. Interactive Media & Services (502030) is not Media and stays in. v2 adds the pre-2018 code so that media is treated alike in every year (follows C3) |

## 4. SELL

| id | card rule, claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S1 | Rsell1 (usually); HOH2-C052, HOH3-C009, HOH3-C012, HOH3-C048 | none | no time-based exit, no price-gain exit, no stop-loss | convention | "Hold the company forever"; no price, loss or time trigger is stated (card section 3) |
| S2 | Rsell1, Rbuy1; HOH3-C012, HOH2-C052 | v2: the B1 measure (10y median of Q01) | sell when B1 fails (median <= 15%, or fewer than 10 years); for B1i holdings: sell when S01 > 0 | convention | Holding needs only that the barrier persists ("hold good companies because their barriers persist"); the barrier test that admitted the stock no longer passing is the plain sign it no longer shows. The median already tolerates bad years, so the hold bar equals the entry bar (v1's looser 8-of-10 hold bar existed only because entry required 10 of 10) |
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

1. Barrier score = mean of two percentiles taken inside the pass set: 10y median of Q01 (a year with denominator
   <= 0 and EBIT > 0 counts as above every other value), higher = better; and S02, lower = better. (Rbuy1 "most important",
   HOH2-C002; Ravoid2; Rbuy12.) Ties broken by market value L01c, larger first (HOH2-C060, principle only). TAG convention.
   Unchanged in v2; after C2 this is where margin stability acts in the decisive form.
2. Keep the 2N stocks with the highest barrier score (barriers first, Rprice1 HOH2-C045). TAG convention.
3. Among those, order by V13, highest first; the top N are the target book (valuation after, Rprice2). TAG convention.
4. Essential vs discretionary (Rbuy6, ranked equal to barriers, card section 4 "Open") is already a pass/fail in A1, so
   it adds no ranking key.
5. FULL FORM grid (Rbuy3 "likes" hard-asset infrastructure): B1i names ranked first in step 1, on / off, averaged. TAG grid.

## 7. The two forms

DECISIVE FORM (quote and convention numbers only): A1 (v2), A2; B1 (v2) or B1i; P1 (V13 >= 0); ranking steps 1-4;
SELL S1, S2 (v2), S3, S4; SIZE Z1-Z5 (N = 10 and 15 averaged, equal weight at entry, no rebalancing, long only). B3 (no
growth filter) and B5 (pass-set count vs 200) are recorded and reported.

FULL FORM: the decisive form plus B2 (S02 margin stability, moved here in v2), B4 (S03 revenue stability), A3 (note
exclusions), P1g (V13 margin grid 0 / 1 / 2), ranking step 5 (infrastructure first on / off), S5 (13F turnover cap) and
Z6 (13F weight schedule, N = 9) in place of Z1-Z3. Every grid is averaged; no value is picked.

Counts, full form: BUY 5 (B1, B1i, B2, B3, B4) + 1 reported check (B5); PRICE 2 (P1, P1g); AVOID 3 (A1-A3);
SELL 5 (S1-S5); SIZE 6 (Z1-Z6) = 21 criteria (unchanged). Decisive form: BUY 3 (B1, B1i, B3), PRICE 1 (P1), AVOID 2
(A1, A2), SELL 4 (S1-S4), SIZE 5 (Z1-Z5) = 15 (v1: 16). Not computable: 13 (section 8).

## 8. Not computable

| id | card rule, claims | reason |
|---|---|---|
| N1 | Rbuy2; HOH3-C017, HOH3-C027, HOH2-C004 | Number and type of barriers ("maybe five") cannot be counted from accounts, prices or consensus |
| N2 | Rbuy4; HOH3-C015, HOH2-C008 | Network effects and intellectual property have no dictionary measure; GICS does not mark them |
| N3 | Rbuy5; HOH3-C021 | Obviousness is a judgement. v1 covered it partly by the 10-of-10 entry bar; v2 drops that reading (C1), so it is now not covered at all |
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

## 9. Coverage (decisive form) and main risk

Coverage of the card's 14 buy rules, decisive form: 4 implemented (Rbuy1 by the B1 proxy, Rbuy3 by B1i, Rbuy6 through
A1, Rbuy8 as a deliberate absence of a growth filter) = 29% (v1: 5 = 36%, plus Rbuy5 partly). Rbuy12 moved to the full
form with B2 (it still acts through the ranking), and the partial cover of Rbuy5 is gone (C1). The full form adds Rbuy12
and Rbuy7 = 6 of 14 = 43% (unchanged). Rbuy13 is a reported check. Of the four "always" buy rules, 2 are covered (Rbuy1
by proxy, Rbuy6 by exclusion); durability over 20-30 years and conviction are not computable. Of the "always" avoid
rules, Ravoid1 (A1) and Ravoid3 (A2) are direct, Ravoid2 is now covered through B1 ("average businesses") rather than
a stability filter.

The main risk of v1 still holds and grows: the decisive form is a generic quality screen (long-run return on capital
above 15%, not dear against Treasuries, outside his excluded industries), filled in the US 1,500 by asset-light,
high-margin firms that he reaches, if at all, by judged and obvious barriers rather than by accounts; the final 10-15
are chosen by our ranking, not by him. With B2 out of the decisive form and B1 loosened, the pass set is larger; B5
(count vs "maybe 200") must be read before any result.

Risk that v2 fits his purchases rather than his words. All four changes loosen the screen, and all four touch exactly
the criteria the feedback showed rejecting most of his purchases (B1 62%, B2 55%, A1 34%); none tightens anything. That
direction is itself the warning. Specifically: (1) C2 carries the most risk. It removes from the decisive form a filter
that rejected about half of his purchases, on a reading of one claim (HOH2-C003, rule status "third", strength
"always") as being about "average" businesses; a reader who takes "earnings power is unpredictable" as a free-standing
test would keep B2, and the card gives no second quote to settle it. The full form keeps the v1 reading, so the
difference between the two forms' recall will show how much of v2's gain rests on this one reading. (2) C1 keeps the
15% bar but replaces "every year" by the median; the median was preferred over other loosened counts (for example 8 of
10) because v1's own ranking already uses it, not because of the feedback, but among the possible loosenings it is a
generous one (up to four years below the bar pass), and the claim it re-reads (HOH3-C021, obviousness) was in v1 the
reason for strictness; the change is defensible on his words but was looked for because the feedback pointed at B1.
(3) C3 can matter only for 2010-2018 and only for media companies; if those are what drove A1's rejections, the gain
comes from companies that his own notes (HOH2-C035-C037) say he excludes, so the decisive form would then admit names
the full form rejects. That would be a sign of fit to his 13F rather than to his words, and the full-form recall (with
A3) is the check. (4) C4 follows mechanically from C1 and does not affect recall. The card is THIN (two 2025
documents, no held-out document), so "the quote decides" rests on two talks given after the period being tested; a
v2 pass on recall should be read as "consistent with his words under these readings", not as confirmation of them.
