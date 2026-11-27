# Recipe: Derek Pilecki (Gator Capital) (gate G6)

Inputs: CARD.md (labelled THIN, financials specialist; 2 documents, 2025-10-02 and 2026-04-02),
field_dictionary_v0.1.csv, FIELD_DICTIONARY_v1.0.md, construction_13F.txt. No returns were seen; no number is tuned.
Card rule ids are the card's own (Rbuy / Rprice / Ravoid / Rsell / Rsize / Rproc; the brief's RB / RP / RA / RS / RZ /
RO map to these).

## 0. Mechanics (apply to every criterion)

- Screen date: each quarter-end (Mar, Jun, Sep, Dec month-end), plus one extra date for the December sleeve (B4).
  Eligible set = the 1,500 largest US stocks with a known GICS sector; every value as known on the day (dictionary
  v1.0 rules 1-3: first-reported accounts usable from announcement + 1 day, TTM = last four consecutive quarters,
  average equity = (latest + four quarters earlier) / 2, a ratio with denominator <= 0 is missing).
- Comparison group = GICS industry group inside Financials: 4010 Banks, 4020 Financial Services (Diversified
  Financials before 2023), 4030 Insurance. If a group has fewer than 10 ranked members on the date, rank inside sector
  40 instead. Percentile ranks: 0 = lowest, 1 = highest value of the measure.
- GICS structure: the March 2023 structure (payment processors such as PayPal, WEX, Global Payments are in 4020,
  sub-industry 40201060). History: LSEG gives today's code (known look-ahead, dictionary X01); WRDS gives the code at
  the month. For WRDS history before 2023, a stock in 45102020 counts as Financials only if its code today is
  40201060.
- The reference book's generic exclusions (4010, 4030, sub-industry 35201010, sector 60) do NOT apply: banks and
  insurers are his field.
- Missing data: a gate whose measure is missing is failed (the stock does not pass). In ranks, a missing measure
  takes 0.5 (dictionary rule 4), which fails every "above the median" gate.

## 1. BUY (what qualifies)

| id | card rule(s), claims | measure | comparison and number | TAG | why this measure stands in for his words |
|---|---|---|---|---|---|
| B1 | Rbuy4 (PIL1-C033, PIL2-C068), Ravoid2 (PIL1-C030, PIL1-C031, PIL2-C067) | Q03 return on equity (NI TTM / average common equity) | rank inside industry group > 0.5 (above the group median) | convention | "higher-ROE companies" and "ignore ... uninteresting ROEs": "higher" read as above the median of comparable firms; group-relative because bank, insurer and asset-manager ROEs differ by business model |
| B2 | Rbuy4 (PIL1-C033, PIL2-C068) | new: TBVPS_q = (R33 - R24) / R39 (split-adjusted shares; WRDS: (ceqq - intanq) / (cshoq x ajexq)); growth = (TBVPS_t + sum of R16 dividends per share over the last 12 quarters) / TBVPS_{t-12 quarters} - 1; TBVPS_{t-12} <= 0 = missing. Applied to groups 4010 and 4030 only | > 0 | convention | "managements compounding tangible book value": tangible book per share, dividends added back, higher than three years earlier. Only for balance-sheet businesses (banks, insurers), where he prices on tangible book (PIL1-C062, PIL2-C050); for fee businesses tangible book is not his yardstick. Note: R24 (intangibles incl. goodwill) is the one raw item whose LSEG name is still open |
| B3 | Rbuy2 (PIL2-C016, PIL1-C019, PIL1-C018; principle PIL2-C015) | P02 momentum 6-1 (total return months t-6 .. t-2, dictionary v0.1) | > 0 | convention | "the stock has to be moving ... paying up a little for confirmation": a positive medium-term return is the plain reading of "moving"/"started to work"; the dictionary lists P02 for him. Open O1 (gate or timing) is resolved as a gate because Rbuy2 is stated as a requirement ("cheap is not enough") |
| B4 | Rbuy5 (PIL1-C092, PIL1-C093, PIL2-C009) | new: lag = total return from the last December month-end to the November month-end (compounded TR1Mo) minus the median of the same return in the stock's industry group | December sleeve: at the November month-end, from stocks that pass B1, B2, P1, A1, A2 (B3 waived), buy the 2 or 3 with the most negative lag | quote (2 and 3 names, two versions averaged) | "in December buy two or three names that did not perform well": calendar-year return against the sector is the card's measure; the November month-end is the last month-end before he buys. B3 is waived because a laggard fails momentum by construction; A2 is kept (Ravoid3 is stated without a seasonal exception). Sleeve names join the normal SELL rules from the next quarter-end (March); his holding period for them is not stated |
| B1-g (full form only) | Rbuy6 (PIL2-C042, PIL1-C052), open O3 | Q03 | versions: rank > 0.5 (as B1) and rank > 1/3 (only the bottom third out), averaged | grid | "quality is not a hard gate ... everything has a price" (sometimes) against Rbuy4 (usually): the softer version keeps the mediocre-ROE cut but admits middle-ROE names |

## 2. PRICE (when cheap enough)

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| P1 | Rprice1 (PIL1-C088, PIL1-C087; support PIL2-C003, PIL2-C045, PIL2-C063) | value score: groups 4010, 4030 = mean of the in-group percentile ranks of V02 earnings to price (NI TTM / L01c) and V07 tangible book to price ((R33 - R24) / L01c); group 4020 = rank of V02 alone. Negative E/P or tangible book = ranks as expensive | value score in the cheapest 30% of its industry group (rank >= 0.70) | convention | "buy cheap financials" (always) with no stated cut-off: "cheap" read as the cheapest 30% (the standard value break of Fama-French). The measures are the ones his examples use: P/E (8x, 10x, single-digit, PIL1-C053, PIL2-C048, PIL1-C062) and tangible book (1x, 60%, 35%, PIL1-C062, PIL2-C050); ranking inside the industry group is a partial stand-in for Rprice2 (each kind of business judged against its own multiples) |

## 3. AVOID (exclusions)

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A1 | Rproc1 (PIL1-C021; support PIL1-C022) | X01 GICS sector | exclude every sector except 40 Financials: 10 Energy, 15 Materials, 20 Industrials, 25 Consumer Discretionary, 30 Consumer Staples, 35 Health Care, 45 Information Technology (except the pre-2023 payment names mapped above), 50 Communication Services, 55 Utilities, 60 Real Estate (equity REITs; mortgage REITs are in 40 since 2023 and stay in) | convention | "stay in financials, do not buy outside it": his field read as GICS Financials; his examples (banks, insurers, brokers, asset managers, data providers, payment fintech) all sit there under the 2023 structure |
| A2 | Ravoid3 (PIL1-C045; support PIL1-C042, PIL1-C044, PIL1-C046, PIL2-C019) | new: close at the screen month-end <= the lowest month-end close of the previous 11 months (split-adjusted close, monthly file) | exclude if true (a new 12-month low) | convention | "do not catch a falling knife ... stocks going straight down": a stock making a new 12-month low is still falling; this is the mirror of P03 (distance from the 12-month high) built from the same input |

Ravoid2's ROE leg is B1 (and S2 for holdings). Its "growing through M&A" leg has no number and adds no selection
while B1 holds, so it is not built (see section 7).

## 4. SELL

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S1 | Rsell3 (PIL2-C071, PIL2-C072, PIL2-C074), Rsell2 (PIL2-C022; support PIL2-C085, PIL2-C021, PIL2-C089) | P1 value score and P02 | sell a non-enduring holding at a quarter-end if value score rank < 0.5 (no longer in the cheaper half of its group) AND P02 <= 0 | convention | "for sale at the right price" read as: the price has left the cheap half; "let winners run, do not sell just because the target is hit" read as: keep it while momentum is still positive. PIL2-C021 (sell a little at target, let it run while the chart looks good) supports joining the two conditions |
| S2 | Rbuy4, Ravoid2 (PIL2-C067 "never hold the average bank long term", PIL1-C030) | B1 and B2 | sell any holding (enduring included) that fails B1 or (groups 4010, 4030) B2 at a quarter-end | convention | the quality gates he buys on are kept while holding: a holding whose ROE drops into the group's lower half has become the "mediocre" bank he ignores. This is NOT Rsell1 (his "evidence I was wrong" is judgement, section 7) |
| S3 | Rsell3 (PIL2-C070, PIL2-C071) | Q03 rank among the holdings | at each quarter-end the 30% (version 1) / 40% (version 2) of holdings with the highest Q03 rank are "enduring": exempt from S1, still subject to S2. Versions averaged | quote (30-40%; which names are enduring = convention: the highest-ROE holdings) | "30-40% of names enduring, held for a long time; 60-70% for sale at the right price". He does not say which names are enduring; his quality focus (Rbuy4) makes the highest-ROE holdings the natural reading |
| S4 (full form only) | Rsell2, Rsell3 | quarters held | S1 is not applied before a holding has been held 4 quarter-ends | revealed-13F (median holding 4 quarters) | fills the missing holding horizon for the "for sale" part from his own 13F; S2 still applies at once |

## 5. SIZE

| id | card rule(s), claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| Z1 | Rsize1 (PIL1-C001, PIL1-C061; support PIL1-C002, PIL1-C004) | number of holdings | at most N = 40 (version 1) / 45 (version 2) names; versions averaged. Fewer passers = fewer names (no filling from non-passers) | quote | "40 or 45" long names (the later count; 25 was earlier). The 13F shows 54 names but only 26 effective: the quote wins |
| Z2 | Rsize2 (PIL1-C005, PIL1-C003; support PIL1-C063, PIL1-C064) | entry weight | a new name enters at (4/3) x (1 / n), n = number of holdings after entry; the book stays 100% long, so other holdings are cut pro rata to fund it (sale proceeds first) | quote (4% new against 3% average) | the long-only paper book cannot copy 40-45 x 3% (his gross above 100%); it keeps his stated ratio of new to average position. The 13F start weight (1.7%) is lower: the quote wins |
| Z3 | Rsize3 (PIL1-C006, PIL1-C007, PIL1-C009, PIL1-C035, PIL2-C023, PIL2-C024) | trades in held names | no top-ups and no rebalancing back to target: holdings drift with price (winners grow, losers shrink) | convention | "add rarely ... not when down ... no adding in down markets": no adds to losers; drift is the only "adding to winners" the machine does, which matches "rarely" |
| Z4 (full form only) | Rsize2 (no maximum stated, card section 3) | weight at a quarter-end | trim any holding above 12% back to 12%, proceeds pro rata to the others | revealed-13F (90th percentile of his largest weight = 12%) | fills the missing position cap from his own 13F; only bites when few names pass |

Ranking inside the pass set (rule 5): new names are taken in order until the book holds N names.
- R1 (decisive): highest value score first (Rprice1 is his only "always" rule); ties broken by fewer FY1 estimates
  (E05, Rbuy3 "less trafficked", PIL1-C012) | convention.
- R2 (full form, version averaged with R1): mean of in-group ranks of the value score, Q03, P02 and (1 - rank of E05)
  | convention: his joined principle "value plus momentum" (PIL2-C015) with the quality focus (Rbuy4) and the
  less-trafficked preference (Rbuy3), equal weights because he states no order among them.
- The December sleeve (B4) is ranked by lag only and its 2-3 names enter even if the book is at N (the book then
  holds up to N + 3 until the next sells).

## 6. The two forms

**Decisive form** (only `quote` and `convention` numbers): universe and mechanics of section 0; BUY B1, B2, B3;
PRICE P1; AVOID A1, A2; December sleeve B4; SELL S1, S2, S3; SIZE Z1, Z2, Z3; ranking R1.
A stock passes at a quarter-end if A1 and A2 do not exclude it and B1, B2 (banks and insurers), B3 and P1 all hold.

**Full form** (adds `revealed-13F` and `grid`): the decisive form plus B1-g (ROE gate versions averaged), S4 (4-quarter
minimum before S1), Z4 (12% cap) and ranking R2 averaged with R1. Versions to average: N 40/45 x enduring 30/40% x
sleeve 2/3 names (decisive), times B1-g x R1/R2 (full).

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
share count change would need an invented threshold, and B1 already removes the low-ROE banks it targets).

Out of scope of the long-only paper portfolio (4): Rbuy7 shorts (PIL2-C056), Rsell4 short momentum (PIL2-C054),
Rsize4 net 50 / a little leverage (PIL1-C073, PIL2-C058; needs a short book), Rsize5 high-beta short trades
(PIL1-C074). A reported long/short form could add them later; none has a screenable number.

## 8. Coverage and main risk

Buy rules covered: of 7 card buy rules, 2 fully (Rbuy2 as B3, Rbuy5 as B4), 3 partly (Rbuy4 as B1 + B2 without
"well run"; Rbuy3 only in the ranking; Rbuy6 only as the full-form grid B1-g), 2 not (Rbuy1 not computable, Rbuy7
short book): 5 of 7 touched (71%), 2 of 7 fully (29%). Of all 31 card rules, 14 are used (Rbuy2-6, Rprice1, Ravoid2,
Ravoid3, Rsell2, Rsell3, Rsize1-3, Rproc1), 13 are not computable, 4 are out of scope.

Main risk: the recipe picks statistically cheap, above-median-ROE, rising financials among the 1,500 largest; he picks
ideas that clear a thesis-based double in three years, usually through a catalyst the screen cannot see (CEO change at a
laggard, temporary earnings miss, deleveraging, activist or tender offer: Carlyle, PayPal, WEX), and a cheap
high-ROE financial without such a catalyst may be cheap for a reason. The universe also tilts away from him: the
largest-1,500 financials are dominated by banks and insurers, while his examples lean to fintech, asset managers,
brokers, data providers and smaller names (European banks are outside a US screen); his 13F book is far more
concentrated (26 effective names, top ten 51%, largest 9%) than an equal-ratio 40-45-name paper book. The momentum gate
and the new-low exclusion would have rejected his best-documented contrarian buy (regional banks right after the 2023
failures, open O4), and S2's median ROE line may churn names he would hold; historical GICS for payment names relies
on today's codes. All thresholds are conventions on a THIN card (two documents, both 2025-26), so a pass on history
says little about fidelity to him until the recall test on his own 13F purchases.
