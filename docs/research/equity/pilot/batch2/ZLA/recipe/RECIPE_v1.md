# Recipe: Val Zlatev (Analog Century Management), gate G6

Built from CARD.md (file THIN: 2 documents, ZLA1 2025-03-12 and ZLA2 2022-02-02, no held-out document), the field
dictionaries v0.1 / v1.0 and construction_13F.txt. No return of any kind was seen; no number is tuned.

**Scope.** He runs a long/short fund; his 13F shows longs only. The paper portfolio below is LONG-ONLY (the decisive
form of the registration); the short sleeve at the end is reported only. Applied at each quarter-end to the eligible
US stocks (1,500 largest, GICS known). Measures follow FIELD_DICTIONARY v1.0 rules 1-3 (as known on the day,
first-reported accounts, TTM = four consecutive quarters, ratio with denominator <= 0 = missing). **In this screen a
missing measure FAILS the criterion** (no 0.5 fill: that rule is for sector ranks only). GICS must be the code at the
quarter-end (WRDS comp.co_hgic history; LSEG TR.GICS* is today's code = known look-ahead, report it).

Line format: id | card rule(s) and claim ids | measure | comparison and number | TAG | why this measure.

## 1. BUY (what qualifies)

| id | card rule / claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| B1 | RB1, RX6; ZLA2-C015 (always), ZLA2-C043, ZLA2-C011 | X01 GICS industry | IN {453010 Semiconductors & Semiconductor Equipment (45301010 Semiconductor Materials & Equipment, 45301020 Semiconductors), 452010 Communications Equipment, 452020 Technology Hardware, Storage & Peripherals} | convention | His four named groups map one-to-one to these three GICS industries (semis + semi cap equipment share 453010); software and internet sit elsewhere in GICS |
| B1-g | same | X01 GICS sub-industry | grid: {B1 set} and {B1 set + 45203015 Electronic Components}; average the two | grid | "Tech hardware" may include electronic components; instruments, EMS and distributors are not hard-tech makers and stay out |
| B3a | RB3; ZLA1-C008, ZLA1-C044, ZLA1-C045 (always) | Q04 gross margin, TTM (R03 or R01-R02, over R01) | >= median of Q04 among stocks passing B1 at the same quarter-end | convention | "high staying power ... keeps its gross margins": high margin is the computable trace of share and moat; he gives no level, so "high" = top half of his own universe |
| B3a-g | same | Q04 | grid: top 1/2, top 1/3 of the B1 set; average | grid | "high" read at two strictness levels |
| B3b | RB3; ZLA1-C044, ZLA1-C045 | new: Q04 TTM at the quarter-end minus Q04 TTM four quarters earlier (needs 8 consecutive quarters) | >= 0 percentage points | convention | "keep (or increase) its gross margins" read literally: not lower than a year ago |
| B4a | RB4; ZLA1-C009 (always) | B01 net debt / EBITDA TTM (R31 or R30-R18, over R09; EBITDA <= 0 = missing = fail; net cash passes) | < 2.0 | convention | "Healthy balance sheet": 2x net debt/EBITDA is the usual line between moderate and stretched leverage; he gives no number |
| B4a-g | same | B01 | grid: < 1.0, < 2.0, < 3.0; average | grid | no stated level |
| B4b | RB4; ZLA1-C009 | Q06 free-cash-flow margin TTM ((R41-R42) / R01) | > 0 | convention | "healthy ... cash flows": positive free cash flow is the plain reading |

## 2. PRICE (when cheap enough)

| id | card rule / claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| P1 | RP2; ZLA1-C011 (always), ZLA1-C012 (sometimes); RP1, ZLA1-C010 | new: price / FY2 consensus EPS mean (TR.EPSMean Period=FY2 over TR.PriceClose; WRDS ibes.statsum_epsus fpi 2; latest mean within 35 days before the quarter-end, same share basis as E01; FY2 EPS <= 0 = fail) | <= 20; NO lower bound | quote | "the multiple say 15-20 on that X" on earnings 2-3 years out. 20 = top of his band; a P/E below 15 is allowed because he is "not a slave to cheap companies" (RP1) and bought at 12-15x (ZLA2-C026). FY2 consensus is the nearest dictionary input to his own 2-3-year estimate (FY3 is not a dictionary input) |
| P1-g | same | same | grid: <= 15, <= 20; average | grid | the quoted band read as either end; caption garbled ("1520") |

## 3. AVOID (exclusions)

| id | card rule / claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A1 | RB1 "(not software or internet)"; ZLA2-C015; views ZLA1-C058, ZLA1-C060, ZLA1-C061 | X01 GICS industry | EXCLUDE 451030 Software, 451020 IT Services, 451010 Internet Software & Services (code to 2018), 502030 Interactive Media & Services, 255020 Internet & Direct Marketing Retail (to 2023) / 255030 Broadline Retail | convention | Rule 3 of the brief: the industries he excludes, by GICS name. Inside B1 this has no extra effect; it guards the grid and any later widening of B1 |
| A2 | RB5 (usually); ZLA1-C004; support ZLA1-C052, ZLA1-C053 | E04 forward EPS growth (FY2 mean / FY1 mean - 1; FY1 <= 0 = missing = fail) | EXCLUDE if < 0 | convention | His short-book mark is "EPS contraction"; a long he would buy does not have consensus EPS falling. Inverts a short rule (card section 3 candidate), so FULL FORM ONLY |

## 4. SELL (paper portfolio, long side)

| id | card rule / claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S1 | RS2; ZLA2-C030 (always); RS1, ZLA2-C013, ZLA2-C027 | new: (position value - cost of the position) / portfolio value, checked at each month-end close | exit when <= -1.5% of the portfolio | quote | "1.5% of AUM means exit"; in a paper portfolio the weights are known, so his fund-level loss limit is computable. This is how "cut losers, do not double down" (RS1) becomes a number |
| S2 | RX1; ZLA1-C001, ZLA1-C003 (always); RP1 | the screen itself, at each quarter-end | sell a holding that fails B1, B3a, B3b, B4a, B4b (or A2 in the full form); a holding that fails ONLY P1 is KEPT | convention | "Buy and hold for an extended period" and no valuation exit stated: a price rise alone does not force a sale; a broken margin, balance-sheet or cash-flow test does |
| S2-g | same; construction_13F (median holding 4 quarters, 48% still held after 1 year) | same | grid: {S2 as written}, {sell on failing any criterion incl. P1}; average | grid | his revealed turnover (33% of the book new each year) is higher than "extended period" suggests |
| S3 | RS1/RS2 | none | a stock sold under S1 cannot be re-bought for the next quarter-end | convention | "sell and move on" (ZLA2-C027): no re-entry at the next scan |

## 5. SIZE

| id | card rule / claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| Z1 | RZ1; ZLA2-C028 (always) | weight at entry | equal weight across the names held; cap 10% per name; the rest in cash | convention | "I shouldn't be placing huge bets": equal weight, and 10% is the common ceiling for a single holding in a diversified fund |
| Z2 | RZ1; construction_13F | number of names N | N = 21 (top 21 of the pass set by the ranking rule) | revealed-13F | median 21 names in his 13F |
| Z3 | RZ1; construction_13F | weight cap | 8% per name (largest weight 8%, 90th pct 9%); new positions start at 3.5% | revealed-13F | his revealed concentration |
| Z4 | none (mechanics) | rebalance | at each quarter-end only; positions drift between quarter-ends (no trimming of winners) | convention | buy and hold (RX1); no trim rule stated |

**Ranking rule inside the pass set (rule 5).** He states no explicit order of preference. His long criteria come in a
fixed order (themes, market share with staying power, balance sheet, multiple: ZLA1-C007 to ZLA1-C011). Themes are not
computable, so rank by the next one: **Q04 gross margin TTM, highest first**; ties broken by E04 (FY2/FY1 growth,
highest first), the nearest trace of his "earnings two or three years out". Existing holdings that still pass (S2) keep
their place before new names fill free slots (RX1). Tag: convention.

## 6. The two forms

**DECISIVE form (quote and convention numbers only):**
pass = B1 AND B3a (top half) AND B3b (>= 0 pt) AND B4a (< 2.0) AND B4b (> 0) AND P1 (<= 20 on FY2, no floor), with A1.
Hold every passer at equal weight, cap 10% (Z1); sell by S1 (-1.5% of portfolio), S2 (non-price failure), S3; rebalance
at quarter-ends (Z4). Ranking rule only needed if a name limit is imposed (it is not in this form). 12 criteria.

**FULL form:** decisive criteria with their grids averaged (B1-g, B3a-g, B4a-g, P1-g, S2-g) plus A2; N = 21 by the
ranking rule (Z2), cap 8% with new positions at 3.5% (Z3). Report each grid cell and the average; the average is the
full-form result.

**Short sleeve (long/short, REPORTED ONLY; not part of either long form):** short pool = B1 AND E04 < 0 (RB5 "EPS
contraction", ZLA1-C004, convention) AND B3b < 0 (gross margin TTM below a year ago: "margin is threatened",
convention); cover at a fall of 20% / 30% from entry (RS4, ZLA1-C005, ZLA1-C006: grid {20, 30}, quote); S1 loss limit
applies. "Not growing that much" has no number and is not used.

## 7. Not computable

Fully not computable (10):
- RB2 themes / inflection points (ZLA1-C007, ZLA1-C002): no theme list rule and no share of revenue by theme; a growth
  or margin-acceleration proxy would pick cyclical upturns, which he separates from secular themes (ZLA1-C014 vs
  ZLA1-C016). Not forced.
- RS3 more patience in a market crash (ZLA2-C031, ZLA2-C032): "crash" undefined, no number.
- RZ2 fund drawdown 8-12% "something is going wrong" (ZLA2-C037): no action stated.
- RZ3 gross below 100% in high volatility (ZLA2-C039): regime undefined; a long-only book is at or below 100% anyway.
- RX2 theme first, then bottom-up work; RX3 supply-chain research; RX4 the two or three key numbers in a print;
  RX7 analyst freedom at 5-15% adverse moves; RX8 in-house idea generation: research process, no screen form.
- RX5 one-sigma noise / two-three-sigma attention (ZLA2-C007): computable but it directs attention, not a trade; window
  not stated.

Partly not computable (4; the computable part is used above):
- RB3 market share (ZLA1-C008): no market-share data; only the gross-margin half is in B3a/B3b.
- RP2 "his own view" of earnings (ZLA1-C011): his estimate is not observable; FY2 consensus stands in (nearer and
  usually lower than his view for the names he likes).
- RS2 / ZLA2-C029 the 1% "re-evaluate" step, and the open 50 bp step (card section 4 row 1): no machine action; only
  the 1.5% exit is used.
- RZ1 "not huge bets": no number; 10% (convention) and 8% (revealed) stand in.

## 8. Coverage and main risk

Coverage: of his 5 buy rules, the decisive form implements 3 (RB1 fully, RB4 fully on convention numbers, RB3 in part:
margin yes, market share no) = 60%; the full form adds RB5 (as avoid A2 and in the short sleeve) = 4 of 5 = 80%. RB2,
the first of his four long criteria, is not covered. Both price rules (RP1, RP2) are used; of sell and size rules, RS2
(exit step), RS1 (through RS2), RS4 (short sleeve) and RZ1 (convention) are used.

Main risk: the screen will select a different kind of company than he does. It picks hard-tech companies that already
earn high and steady gross margins, carry little debt, generate cash, and trade at 20x or less on consensus EPS one to
two years out: mature, cash-rich incumbents (network equipment, storage and PC hardware, analog and mixed-signal chips,
semi equipment after a down-cycle). His longs are the companies that drive a new theme (Nvidia is his example), whose
earnings two or three years out he sets well above consensus; on consensus FY2 EPS those names usually trade above 20x,
so P1 removes exactly the stocks his edge is about, while the margin and cash tests keep the mature segments (phones,
PCs, consumer electronics) that he names as his short pool (ZLA1-C052). B3b also admits cyclical margin recoveries,
the "trading vehicle" part of hard tech he moved away from. On top, his 13F book turns over fast (median holding 4
quarters, 33% new each year) despite his buy-and-hold words, the file rests on two documents with no held-out check,
and the 15-20 band comes from a garbled caption. The recall test on his own conviction purchases is the place where this
risk shows; expect low recall from P1 and the missing theme rule.

Counts: BUY 5 criteria (B1, B3a, B3b, B4a, B4b; + 3 grids), PRICE 1 (P1; + 1 grid), AVOID 2 (A1, A2), SELL 3 (S1-S3;
+ 1 grid), SIZE 4 (Z1-Z4). Decisive form: 12 (B1, B3a, B3b, B4a, B4b, P1, A1, S1, S2, S3, Z1, Z4). Not computable: 10
fully + 4 partly = 14.
