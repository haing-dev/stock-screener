# Recipe v2: Derek Pilecki (Gator Capital) (gate G8 revision round, A10 item 9)

Inputs: RECIPE_v1.md, CARD.md (labelled THIN, financials specialist; 2 documents, 2025-10-02 and 2026-04-02),
field_dictionary_v0.1.csv, FIELD_DICTIONARY_v1.0.md, construction_13F.txt, RECALL_FEEDBACK.md (used only to locate
where v1 may misread him; every change below rests on card claims). No returns were seen; no number is tuned to the
feedback. Card rule ids are the card's own (Rbuy / Rprice / Ravoid / Rsell / Rsize / Rproc).

## Change table

| id | v1 | v2 | claim ids | why (one line) |
|---|---|---|---|---|
| B1 | Q03 rank inside industry group > 0.5 (above the median) | Q03 rank > 0.30 (out only if in the lowest 30% of the group) | PIL1-C030, PIL1-C031, PIL2-C042, PIL1-C052 | the cut he states is "uninteresting / low ROEs" (Ravoid2) and he says quality is not a hard gate ("everything has a price", Rbuy6), so the gate removes low ROE, not the lower half; 30% = the same Fama-French break v1 uses for "cheap" |
| B1-g | full-form versions rank > 0.5 and rank > 1/3, averaged | full-form versions rank > 0.30 (as decisive) and rank > 0.5 (v1 reading of "higher"), averaged | PIL1-C033, PIL2-C068, PIL2-C042 | keeps the v1 reading of "focus on higher-ROE companies" as a grid version, now beside the decisive floor instead of a third ad-hoc cut |
| P1 | value score in the cheapest 30% of its industry group | cheapest 30% of its industry group OR cheapest 30% of its own last 60 month-ends | PIL2-C045, PIL1-C088, PIL1-C087 | the card names two yardsticks for "cheap": against peers and against the stock's own history (PIL2-C045); v1 used only the first; 60 months = the dictionary's own-history window (V12) |
| S1 | sell a non-enduring holding if group value rank < 0.5 AND P02 <= 0 | sell if the value score has left the cheaper half on BOTH yardsticks (group rank < 0.5 AND own-history rank < 0.5) AND P02 <= 0 | PIL2-C071, PIL2-C045, PIL2-C022 | "for sale at the right price" must use the same meaning of cheap as the buy rule, else a name bought on own-history cheapness is sale-eligible at once |
| S2 | sell any holding that fails B1 (median) or B2 | sell any holding that fails B1 v2 (lowest 30%) or B2 | PIL2-C042, PIL1-C030, PIL1-C031 | he owns some companies that are not the highest quality (Rbuy6); the holding rule follows the buy floor so a name is not bought and sold on the same line |
| S3 | enduring = the 30% / 40% of holdings with the highest Q03 rank | same, but only holdings with Q03 group rank > 0.5 can be enduring | PIL2-C067, PIL2-C070, PIL2-C071 | "never hold the average bank (KRE) long term" (always): a holding at or below its group's ROE median stays "for sale", never enduring |
| R1 | rank new names by value score; ties by fewer FY1 estimates | rank by the mean of the in-group value-score rank and the in-group Q03 rank; ties by fewer FY1 estimates | PIL1-C033, PIL2-C068, PIL1-C088, PIL1-C012 | with B1 now a floor, his "focus on higher-ROE companies" (Rbuy4) enters through the order of entry; equal weights because he states no order between cheap and quality |

Number of changes: 7 (two change the decisive pass set: B1, P1; five follow from them or act only after entry:
B1-g, S1, S2, S3, R1).

## 0. Mechanics (apply to every criterion)

- Screen date: each quarter-end (Mar, Jun, Sep, Dec month-end), plus one extra date for the December sleeve (B4).
  Eligible set = the 1,500 largest US stocks with a known GICS sector; every value as known on the day (dictionary
  v1.0 rules 1-3: first-reported accounts usable from announcement + 1 day, TTM = last four consecutive quarters,
  average equity = (latest + four quarters earlier) / 2, a ratio with denominator <= 0 is missing).
- Comparison group = GICS industry group inside Financials: 4010 Banks, 4020 Financial Services (Diversified
  Financials before 2023), 4030 Insurance. If a group has fewer than 10 ranked members on the date, rank inside sector
  40 instead. Percentile ranks: 0 = lowest, 1 = highest value of the measure.
- Own-history rank (new in v2, used by P1 and S1): for a measure M of a stock, the share of the stock's own month-end
  values of M over the previous 60 month-ends (t-60 .. t-1) that are lower than or equal to M at t; each past value as
  known at that past month-end (same rules 1-3). At least 48 of the 60 month-ends must be present (80%, the presence
  share of dictionary P01: 9 of 11), else the own-history rank is missing. 60 months = the window of dictionary V12
  (earnings yield against own history) | convention.
- GICS structure: the March 2023 structure (payment processors such as PayPal, WEX, Global Payments are in 4020,
  sub-industry 40201060). History: LSEG gives today's code (known look-ahead, dictionary X01); WRDS gives the code at
  the month. For WRDS history before 2023, a stock in 45102020 counts as Financials only if its code today is
  40201060.
- The reference book's generic exclusions (4010, 4030, sub-industry 35201010, sector 60) do NOT apply: banks and
  insurers are his field.
- Missing data: a gate whose measure is missing is failed (the stock does not pass). This takes precedence over rank
  filling: a stock with Q03 missing fails B1 even though B1's floor (0.30) is below the 0.5 fill. In composite ranks
  (R1, R2) a missing measure takes 0.5 (dictionary rule 4). In P1, a missing own-history rank leaves only the group
  leg (the stock passes P1 only if it passes the group leg).

## 1. BUY (what qualifies)

| id | card rule(s), claims | measure | comparison and number | TAG | why this measure stands in for his words |
|---|---|---|---|---|---|
| B1 | Ravoid2 (PIL1-C030, PIL1-C031, PIL2-C067), Rbuy6 (PIL2-C042, PIL1-C052), Rbuy4 (PIL1-C033, PIL2-C068) | Q03 return on equity (NI TTM / average common equity) | rank inside industry group > 0.30 (out only if in the lowest 30% of its group) | convention (30% = the Fama-French low/high break, the same break P1 uses for "cheap") | the exclusion he states is "mediocre ... uninteresting ROEs" (Ravoid2); "quality is not a hard gate ... everything has a price" (Rbuy6) rules out a median line as a hard gate. "Low ROE" read as the lowest 30% of comparable firms; group-relative because bank, insurer and asset-manager ROEs differ by business model. His "focus on higher-ROE companies" (Rbuy4) is carried by the ranking R1 and by S3, not by this gate |
| B2 | Rbuy4 (PIL1-C033, PIL2-C068) | new: TBVPS_q = (R33 - R24) / R39 (split-adjusted shares; WRDS: (ceqq - intanq) / (cshoq x ajexq)); growth = (TBVPS_t + sum of R16 dividends per share over the last 12 quarters) / TBVPS_{t-12 quarters} - 1; TBVPS_{t-12} <= 0 = missing. Applied to groups 4010 and 4030 only | > 0 | convention | "managements compounding tangible book value": tangible book per share, dividends added back, higher than three years earlier. Only for balance-sheet businesses (banks, insurers), where he prices on tangible book (PIL1-C062, PIL2-C050); for fee businesses tangible book is not his yardstick. Note: R24 (intangibles incl. goodwill) is the one raw item whose LSEG name is still open |
| B3 | Rbuy2 (PIL2-C016, PIL1-C019, PIL1-C018; principle PIL2-C015) | P02 momentum 6-1 (total return months t-6 .. t-2, dictionary v0.1) | > 0 | convention | "the stock has to be moving ... paying up a little for confirmation": a positive medium-term return is the plain reading of "moving"/"started to work"; the dictionary lists P02 for him. Open O1 (gate or timing) is resolved as a gate because Rbuy2 is stated as a requirement ("cheap is not enough"). Unchanged in v2: well quoted (rule 3) |
| B4 | Rbuy5 (PIL1-C092, PIL1-C093, PIL2-C009) | new: lag = total return from the last December month-end to the November month-end (compounded TR1Mo) minus the median of the same return in the stock's industry group | December sleeve: at the November month-end, from stocks that pass B1, B2, P1, A1, A2 (B3 waived), buy the 2 or 3 with the most negative lag | quote (2 and 3 names, two versions averaged) | "in December buy two or three names that did not perform well": calendar-year return against the sector is the card's measure; the November month-end is the last month-end before he buys. B3 is waived because a laggard fails momentum by construction; A2 is kept (Ravoid3 is stated without a seasonal exception). Sleeve names join the normal SELL rules from the next quarter-end (March); his holding period for them is not stated |
| B1-g (full form only) | Rbuy4 (PIL1-C033, PIL2-C068), Rbuy6 (PIL2-C042, PIL1-C052), open O3 | Q03 | versions: rank > 0.30 (as B1) and rank > 0.5 (above the group median: the reading of "higher-ROE companies" as a gate), averaged | grid | open O3 (how far price overrides quality) is not settled by the card: the floor reading (Ravoid2 + Rbuy6) and the median reading (Rbuy4 as a gate) are averaged |

## 2. PRICE (when cheap enough)

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| P1 | Rprice1 (PIL1-C088, PIL1-C087; support PIL2-C003, PIL2-C045, PIL2-C063) | value score: groups 4010, 4030 = mean of the ranks of V02 earnings to price (NI TTM / L01c) and V07 tangible book to price ((R33 - R24) / L01c); group 4020 = rank of V02 alone. Computed two ways: (g) in-group percentile ranks; (h) own-history ranks (section 0), mean of the two own-history ranks for 4010 / 4030. Negative E/P or tangible book = ranks as expensive (in (h): a negative current value is not cheap) | passes if (g) >= 0.70 (cheapest 30% of its industry group) OR (h) >= 0.70 (cheapest 30% of its own last 60 month-ends) | convention | "buy cheap financials" (always) with no stated cut-off: "cheap" read as the cheapest 30% (the standard value break of Fama-French). The card names two yardsticks he uses for cheap: comparable firms and the stock's own history (PIL2-C045; card section 6); v1 used only peers. The measures are the ones his examples use: P/E (8x, 10x, single-digit, PIL1-C053, PIL2-C048, PIL1-C062) and tangible book (1x, 60%, 35%, PIL1-C062, PIL2-C050); ranking inside the industry group is a partial stand-in for Rprice2 (each kind of business judged against its own multiples). The big-bank comparison (PIL2-C063) is a group-level view and is not built |

## 3. AVOID (exclusions)

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A1 | Rproc1 (PIL1-C021; support PIL1-C022) | X01 GICS sector | exclude every sector except 40 Financials: 10 Energy, 15 Materials, 20 Industrials, 25 Consumer Discretionary, 30 Consumer Staples, 35 Health Care, 45 Information Technology (except the pre-2023 payment names mapped above), 50 Communication Services, 55 Utilities, 60 Real Estate (equity REITs; mortgage REITs are in 40 since 2023 and stay in) | convention | "stay in financials, do not buy outside it": his field read as GICS Financials; his examples (banks, insurers, brokers, asset managers, data providers, payment fintech) all sit there under the 2023 structure |
| A2 | Ravoid3 (PIL1-C045; support PIL1-C042, PIL1-C044, PIL1-C046, PIL2-C019) | new: close at the screen month-end <= the lowest month-end close of the previous 11 months (split-adjusted close, monthly file) | exclude if true (a new 12-month low) | convention | "do not catch a falling knife ... stocks going straight down": a stock making a new 12-month low is still falling; this is the mirror of P03 (distance from the 12-month high) built from the same input. Unchanged in v2: well quoted (rule 3) |

Ravoid2's ROE leg is B1 (and S2, S3 for holdings). Its "growing through M&A" leg has no number and is not built (see
section 7).

## 4. SELL

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S1 | Rsell3 (PIL2-C071, PIL2-C072, PIL2-C074), Rsell2 (PIL2-C022; support PIL2-C085, PIL2-C021, PIL2-C089); PIL2-C045 | P1 value score (g) and (h), P02 | sell a non-enduring holding at a quarter-end if the value score is no longer in the cheaper half on either yardstick ((g) < 0.5 AND (h) < 0.5; a missing (h) counts as < 0.5) AND P02 <= 0 | convention | "for sale at the right price" read as: the price has left the cheap half on the yardsticks he buys on; "let winners run, do not sell just because the target is hit" read as: keep it while momentum is still positive. PIL2-C021 (sell a little at target, let it run while the chart looks good) supports joining the two conditions |
| S2 | Ravoid2 (PIL1-C030, PIL1-C031), Rbuy6 (PIL2-C042), Rbuy4 (B2 leg) | B1 and B2 | sell any holding (enduring included) that fails B1 (Q03 in the lowest 30% of its group) or (groups 4010, 4030) B2 at a quarter-end | convention | a holding whose ROE drops into the low-ROE band has become the "mediocre ... uninteresting ROE" name he ignores; he owns some companies that are not the highest quality (Rbuy6), so the line is the buy floor, not the median. This is NOT Rsell1 (his "evidence I was wrong" is judgement, section 7) |
| S3 | Rsell3 (PIL2-C070, PIL2-C071), Ravoid2 (PIL2-C067) | Q03 rank among the holdings; Q03 rank in the industry group | at each quarter-end, among holdings with Q03 group rank > 0.5, the 30% (version 1) / 40% (version 2) of all holdings with the highest Q03 group rank are "enduring" (fewer if fewer holdings are above the group median): exempt from S1, still subject to S2. Versions averaged | quote (30-40%; which names are enduring = convention: the highest-ROE holdings above their group median) | "30-40% of names enduring, held for a long time; 60-70% for sale at the right price". He does not say which names are enduring; his quality focus (Rbuy4) makes the highest-ROE holdings the natural reading, and "never hold the average bank (KRE) long term" (PIL2-C067, always) keeps a holding at or below its group's ROE median out of the long-held part |
| S4 (full form only) | Rsell2, Rsell3 | quarters held | S1 is not applied before a holding has been held 4 quarter-ends | revealed-13F (median holding 4 quarters) | fills the missing holding horizon for the "for sale" part from his own 13F; S2 still applies at once |

## 5. SIZE

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| Z1 | Rsize1 (PIL1-C001, PIL1-C061; support PIL1-C002, PIL1-C004) | number of holdings | at most N = 40 (version 1) / 45 (version 2) names; versions averaged. Fewer passers = fewer names (no filling from non-passers) | quote | "40 or 45" long names (the later count; 25 was earlier). The 13F shows 54 names but only 26 effective: the quote wins |
| Z2 | Rsize2 (PIL1-C005, PIL1-C003; support PIL1-C063, PIL1-C064) | entry weight | a new name enters at (4/3) x (1 / n), n = number of holdings after entry; the book stays 100% long, so other holdings are cut pro rata to fund it (sale proceeds first) | quote (4% new against 3% average) | the long-only paper book cannot copy 40-45 x 3% (his gross above 100%); it keeps his stated ratio of new to average position. The 13F start weight (1.7%) is lower: the quote wins |
| Z3 | Rsize3 (PIL1-C006, PIL1-C007, PIL1-C009, PIL1-C035, PIL2-C023, PIL2-C024) | trades in held names | no top-ups and no rebalancing back to target: holdings drift with price (winners grow, losers shrink) | convention | "add rarely ... not when down ... no adding in down markets": no adds to losers; drift is the only "adding to winners" the machine does, which matches "rarely" |
| Z4 (full form only) | Rsize2 (no maximum stated, card section 3) | weight at a quarter-end | trim any holding above 12% back to 12%, proceeds pro rata to the others | revealed-13F (90th percentile of his largest weight = 12%) | fills the missing position cap from his own 13F; only bites when few names pass |

Ranking inside the pass set (rule 5): new names are taken in order until the book holds N names.
- R1 (decisive): highest mean of the in-group value-score rank (P1 (g)) and the in-group Q03 rank first (Rprice1
  "buy cheap financials", PIL1-C088; Rbuy4 "focus on higher-ROE companies", PIL1-C033, PIL2-C068; equal weights
  because he states no order between them); ties broken by fewer FY1 estimates (E05, Rbuy3 "less trafficked",
  PIL1-C012) | convention.
- R2 (full form, version averaged with R1): mean of in-group ranks of the value score, Q03, P02 and (1 - rank of E05)
  | convention: his joined principle "value plus momentum" (PIL2-C015) with the quality focus (Rbuy4) and the
  less-trafficked preference (Rbuy3), equal weights because he states no order among them.
- The December sleeve (B4) is ranked by lag only and its 2-3 names enter even if the book is at N (the book then
  holds up to N + 3 until the next sells).

## 6. The two forms

**Decisive form** (only `quote` and `convention` numbers): universe and mechanics of section 0; BUY B1, B2, B3;
PRICE P1; AVOID A1, A2; December sleeve B4; SELL S1, S2, S3; SIZE Z1, Z2, Z3; ranking R1.
A stock passes at a quarter-end if A1 and A2 do not exclude it and B1 (Q03 not in the lowest 30% of its group), B2
(banks and insurers), B3 and P1 (cheapest 30% of its group or of its own last 60 month-ends) all hold.

**Full form** (adds `revealed-13F` and `grid`): the decisive form plus B1-g (ROE floor 0.30 and median 0.5 averaged),
S4 (4-quarter minimum before S1), Z4 (12% cap) and ranking R2 averaged with R1. Versions to average: N 40/45 x
enduring 30/40% x sleeve 2/3 names (decisive), times B1-g x R1/R2 (full).

## 7. Not computable (and out of scope)

Not computable (13):
- Rbuy1 double in 3 years (PIL1-C013): needs his own target value per idea; no method stated, and no dictionary
  measure is his thesis (G08 is another investor's stand-in, so not forced).
- Ravoid1 pass on ~20% upside (PIL2-C013, PIL2-C014): the flip side of Rbuy1; same reason.
- Rprice2 higher multiples for "human interaction" businesses, low ones for capital-intensive ones (PIL1-C055): no
  measure classifies trust work or regulatory capital intensity; only the in-group ranking of P1 stands in partly.
- Rprice3 wait until the price gives a double / the idea develops (PIL1-C016): ties to Rbuy1.
- Rprice4 ignore where the stock has been (PIL2-C088): no measure; meaning unclear (open O5).
- Rsell1 re-underwrite on a fall; sell if real evidence shows he was wrong (PIL1-C036, PIL1-C037): judgement.
- Rsize6 trade smaller after a poor stretch (PIL1-C085): no number, "sometimes".
- Rproc2 running watch list (PIL1-C015, PIL2-C005): the pass set is the machine's list; no criterion of its own.
- Rproc3 100-120 company meetings a year (PIL1-C025): no data.
- Rproc4 tender offers as an idea source (PIL2-C100): no tender-offer field in the dictionary (buybacks R46 are not
  tender offers).
- Rproc5 AI review of 10-K risk factors (PIL1-C056): no field.
- Rproc6 look at charts, do not buy on charts (PIL2-C018): no measure (and it is the other side of open O1).
- Rproc7 be active when markets move (PIL2-C029, PIL2-C038, PIL2-C072): no number.
Partial legs not built: Rbuy4 "well run" management (no measure); Ravoid2 "growth through M&A" (no number; e.g. C04
share count change would need an invented threshold). With B1 loosened to a floor, the M&A leg now selects more than
in v1, but no stated number exists, so it stays unbuilt.

Out of scope of the long-only paper portfolio (4): Rbuy7 shorts (PIL2-C056), Rsell4 short momentum (PIL2-C054),
Rsize4 net 50 / a little leverage (PIL1-C073, PIL2-C058; needs a short book), Rsize5 high-beta short trades
(PIL1-C074). A reported long/short form could add them later; none has a screenable number.

## 8. Coverage and main risk

Buy rules covered in the DECISIVE form: of 7 card buy rules, 2 fully (Rbuy2 as B3, Rbuy5 as B4), 3 partly (Rbuy4 as
B2 + the ROE leg of R1 and S3, without "well run"; Rbuy6 as the floor reading of B1, now in the decisive form instead
of only the full-form grid; Rbuy3 only as the R1 tie-break), 2 not (Rbuy1 not computable, Rbuy7 short book): 5 of 7
touched (71%), 2 of 7 fully (29%). v1's decisive form touched 4 of 7 (Rbuy6 only in the full form). Of all 31 card
rules, 14 are used (Rbuy2-6, Rprice1, Ravoid2, Ravoid3, Rsell2, Rsell3, Rsize1-3, Rproc1), 13 are not computable, 4
are out of scope.

Main risk (unchanged from v1 in substance): the recipe picks statistically cheap, not-low-ROE, rising financials among
the 1,500 largest; he picks ideas that clear a thesis-based double in three years, usually through a catalyst the
screen cannot see (CEO change at a laggard, temporary earnings miss, deleveraging, activist or tender offer: Carlyle,
PayPal, WEX). The universe tilts away from him (39 of his 83 conviction purchases are outside it; his examples lean to
fintech, asset managers, brokers, data providers and smaller names), his 13F book is far more concentrated (26
effective names, top ten 51%, largest 9%) than a 40-45-name paper book, and the momentum gate and new-low exclusion
would have rejected his regional-bank buying after the 2023 failures (open O4). Both are kept because they are well
quoted.

Risk that v2 fits his purchases rather than his words: the two changes that move the decisive pass set, B1 and P1, are
exactly the two criteria the feedback showed rejecting most purchases (59% and 42%), so both carry this risk and should
be read that way by the recall re-test. B1 carries the larger risk: the median gate of v1 was a defensible reading of
"higher-ROE companies" (Rbuy4, usually, both documents), and the floor reading rests on Ravoid2 (PIL1-C030 verified by
both readers, PIL1-C031 by the third only) and on Rbuy6, a "sometimes" rule whose PIL1-C052 claim was verified by the
third reader only; the feedback also printed the rejection share of a 1/3 floor (33.9%), and the 0.30 floor is close
to it, although 0.30 was taken from the break P1 already used in v1, not from that line. The v1 median reading is kept
as a full-form grid version (B1-g) so the cost of the loosening stays visible. P1's own-history leg rests on PIL2-C045,
which the card lists as support for Rprice1 and in its gap list ("comparisons named are own history"), not as a
verified rule with its own number; the 60-month window and 80% presence floor are dictionary conventions, not his
words. If the re-test passes mainly through the own-history leg on stocks that are expensive against their peers,
that is a sign of fit rather than fidelity. S1, S2, S3 and R1 do not change which stocks pass at the quarter-end, so
they cannot raise recall; S3's new median condition tightens a rule (PIL2-C067) and works against fit. B2, B3, A1, A2
and B4 are unchanged although B3 and A2 reject 20% and 15% of his purchases, because their quotes stand (rule 3). The
card stays THIN (two documents, both 2025-26), so even a pass says little about how he chose stocks in 2010-2020.
