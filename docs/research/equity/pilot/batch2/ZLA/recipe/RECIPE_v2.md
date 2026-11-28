# Recipe v2: Val Zlatev (Analog Century Management), gate G8 revision round (A10 item 9)

One revision of RECIPE_v1.md after its recall result (RECALL_FEEDBACK.md: decisive recall 7.4%, lift 2.12, 90%
interval [0.70, 3.78], gate FAIL). Built from CARD.md (file THIN: 2 documents, ZLA1 2025-03-12 and ZLA2 2022-02-02, no
held-out document), the field dictionaries v0.1 / v1.0 and construction_13F.txt. No return of any kind was seen; the
feedback was used only to locate where v1 may misread him; every change rests on a card quote. No number is new: every
number is the v1 number (quote or convention) or a grid cell already in v1.

## 0. Change table (8 changes)

| id | v1 | v2 | claim ids | why (one line) |
|---|---|---|---|---|
| B1 | GICS industries 453010, 452010, 452020 only (electronic components only in the grid) | GICS industry groups 4530 (Semiconductors & Semiconductor Equipment) and 4520 (Technology Hardware & Equipment), all of their industries | ZLA2-C015, ZLA2-C043 | His named list is "semiconductors, semiconductor capital equipment, communications equipment, tech hardware"; the standard GICS reading of "tech hardware" is the group named Technology Hardware & Equipment, which v1 cut down by its own judgement (no quote excludes instruments or components) |
| B1-g | grid {B1 set}, {B1 set + 45203015} | grid {v1 narrow set: 453010, 452010, 452020}, {v2 set: groups 4520 + 4530}; average | ZLA2-C015, ZLA2-C043 | Keeps the narrow v1 reading as one cell, since "tech hardware" is not defined in his words |
| B3a | gross margin TTM >= median of all B1 stocks at the quarter-end | gross margin TTM >= median of the stock's own GICS sub-industry in the eligible universe (fewer than 5 peers: its GICS industry; still fewer than 5: the B1 set) | ZLA1-C008, ZLA1-C044, ZLA1-C045; ZLA1-C043 | "High market share" is share of the company's own market against its competitors (ZLA1-C043: "its competitors"); a chip maker and a storage maker do not compete, so the margin trace of share is read against same-market peers, not the whole hard-tech pool |
| B3a-g | top 1/2, top 1/3 of the B1 set | top 1/2, top 1/3 of the same peer set as B3a | same as B3a | Follows the B3a peer change; the two strictness levels are unchanged |
| B3b | decisive: gross margin TTM not below a year ago | FULL FORM ONLY (same measure and number) | ZLA1-C044, ZLA1-C045; ZLA1-C014, ZLA1-C016, ZLA2-C044 | "Moats that give confidence the company keeps (or increases) its gross margins" is a forward claim about what the moat will do, not a test of last year's change; his own words say hard-tech margins swing with the cycle (old "trading vehicle"), so a one-year change mainly reads the cycle |
| P1 | price / FY2 consensus EPS <= 20 | price / year-3 EPS estimate <= 20, year-3 EPS = FY2 mean x (FY2 mean / FY1 mean); FY1 <= 0: FY2 mean alone; no lower bound | ZLA1-C011, ZLA1-C012; ZLA1-C010 | The quoted multiple sits on earnings "two or three years out"; FY2 is year 2 at most, so the nearer end of his horizon was the only one tested; year 3 is reached by carrying consensus's own FY1-to-FY2 growth one more year; the number 20 is unchanged (quote) |
| P1-g | grid {<= 15, <= 20} on FY2 | grid {FY2, year-3 estimate} x {<= 15, <= 20}: 4 cells, average | ZLA1-C011, ZLA1-C012 | Both ends of "two or three years out" and both ends of the quoted 15-20 band |
| S2 | sell on failing B1, B3a, B3b, B4a, B4b (A2 in full form) | decisive: sell on failing B1, B3a, B4a, B4b; full form also B3b and A2; P1-only failure still KEPT | ZLA1-C001, ZLA1-C003; ZLA1-C044, ZLA1-C045 | Follows B3b leaving the decisive form: the sell screen tests the same criteria as the buy screen in each form |

Consequences without a change of reading (not counted): the short sleeve uses the v2 B1 set; A1 is unchanged and still
has no extra effect inside B1 (groups 4520 and 4530 hold no software, IT services or internet industries).

---

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
| B1 | RB1, RX6; ZLA2-C015 (always), ZLA2-C043, ZLA2-C011 | X01 GICS industry group | IN {4530 Semiconductors & Semiconductor Equipment (industry 453010: 45301010 Semiconductor Materials & Equipment, 45301020 Semiconductors), 4520 Technology Hardware & Equipment (452010 Communications Equipment, 452020 Technology Hardware, Storage & Peripherals, 452030 Electronic Equipment, Instruments & Components)} | convention | His four named groups read by their standard GICS names: semiconductors and semi capital equipment = group 4530; communications equipment and "tech hardware" = group 4520 (Technology Hardware & Equipment). No quote narrows "tech hardware" further. Software and internet sit in other groups |
| B1-g | same | X01 GICS industry / sub-industry | grid: {v1 narrow set 453010, 452010, 452020} and {groups 4520 + 4530}; average the two | grid | "Tech hardware" is not defined in his words: the narrow reading (makers of chips, network gear and computers only) is kept as one cell |
| B3a | RB3; ZLA1-C008, ZLA1-C044, ZLA1-C045 (always); ZLA1-C043 | Q04 gross margin, TTM (R03 or R01-R02, over R01) | >= median of Q04 among eligible stocks in the same GICS sub-industry at the same quarter-end (fewer than 5 such stocks with Q04: same GICS industry; still fewer than 5: all B1 stocks) | convention | "High market share and high staying power ... keeps its gross margins": high margin against the company's own competitors is the computable trace of share and moat; he gives no level, so "high" = top half of the peers it competes with |
| B3a-g | same | Q04 | grid: top 1/2, top 1/3 of the same peer set as B3a; average | grid | "high" read at two strictness levels |
| B3b | RB3; ZLA1-C044, ZLA1-C045; ZLA1-C014, ZLA1-C016, ZLA2-C044 | new: Q04 TTM at the quarter-end minus Q04 TTM four quarters earlier (needs 8 consecutive quarters) | >= 0 percentage points; FULL FORM ONLY | convention | "Keep (or increase) its gross margins" read literally as not lower than a year ago. Full form only: his sentence is about the confidence a moat gives for margins ahead, and a one-year trailing change in hard tech mostly reads the cycle he describes (ZLA1-C014, ZLA2-C044) |
| B4a | RB4; ZLA1-C009 (always) | B01 net debt / EBITDA TTM (R31 or R30-R18, over R09; EBITDA <= 0 = missing = fail; net cash passes) | < 2.0 | convention | "Healthy balance sheet": 2x net debt/EBITDA is the usual line between moderate and stretched leverage; he gives no number |
| B4a-g | same | B01 | grid: < 1.0, < 2.0, < 3.0; average | grid | no stated level |
| B4b | RB4; ZLA1-C009 | Q06 free-cash-flow margin TTM ((R41-R42) / R01) | > 0 | convention | "healthy ... cash flows": positive free cash flow is the plain reading |

## 2. PRICE (when cheap enough)

| id | card rule / claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| P1 | RP2; ZLA1-C011 (always), ZLA1-C012 (sometimes); RP1, ZLA1-C010 | new: price / year-3 EPS estimate, where year-3 EPS = FY2 EPS mean x (FY2 EPS mean / FY1 EPS mean) (TR.EPSMean Period=FY1, FY2 over TR.PriceClose; WRDS ibes.statsum_epsus fpi 1 and 2; latest means within 35 days before the quarter-end, same share basis as E01); FY1 mean <= 0 or missing: year-3 EPS = FY2 mean; year-3 EPS <= 0 = fail | <= 20; NO lower bound | quote | "the multiple say 15-20 on that X", X = earnings potential "two or three years out". 20 = top of his band; no floor because he is "not a slave to cheap companies" (RP1) and bought at 12-15x (ZLA2-C026). FY3 is not a dictionary input, so year 3 is consensus FY2 carried one more year at consensus's own FY1-to-FY2 growth (the plain extrapolation; still consensus, still below his own view for names he likes) |
| P1-g | same | earnings basis: FY2 mean, or the year-3 estimate above | grid: {FY2, year-3} x {<= 15, <= 20}; 4 cells, average | grid | both ends of "two or three years out" and both ends of the quoted band; caption garbled ("1520") |

## 3. AVOID (exclusions)

| id | card rule / claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| A1 | RB1 "(not software or internet)"; ZLA2-C015; views ZLA1-C058, ZLA1-C060, ZLA1-C061 | X01 GICS industry | EXCLUDE 451030 Software, 451020 IT Services, 451010 Internet Software & Services (code to 2018), 502030 Interactive Media & Services, 255020 Internet & Direct Marketing Retail (to 2023) / 255030 Broadline Retail | convention | Rule 3 of the brief: the industries he excludes, by GICS name. Inside B1 this has no extra effect; it guards the grid and any later widening of B1 |
| A2 | RB5 (usually); ZLA1-C004; support ZLA1-C052, ZLA1-C053 | E04 forward EPS growth (FY2 mean / FY1 mean - 1; FY1 <= 0 = missing = fail) | EXCLUDE if < 0 | convention | His short-book mark is "EPS contraction"; a long he would buy does not have consensus EPS falling. Inverts a short rule (card section 3 candidate), so FULL FORM ONLY |

## 4. SELL (paper portfolio, long side)

| id | card rule / claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| S1 | RS2; ZLA2-C030 (always); RS1, ZLA2-C013, ZLA2-C027 | new: (position value - cost of the position) / portfolio value, checked at each month-end close | exit when <= -1.5% of the portfolio | quote | "1.5% of AUM means exit"; in a paper portfolio the weights are known, so his fund-level loss limit is computable. This is how "cut losers, do not double down" (RS1) becomes a number |
| S2 | RX1; ZLA1-C001, ZLA1-C003 (always); RP1; ZLA1-C044, ZLA1-C045 | the screen itself, at each quarter-end | decisive form: sell a holding that fails B1, B3a, B4a or B4b; full form: also B3b and A2; a holding that fails ONLY P1 is KEPT | convention | "Buy and hold for an extended period" and no valuation exit stated: a price rise alone does not force a sale; a broken margin, balance-sheet or cash-flow test does. The sell screen uses the same non-price criteria as the buy screen of each form |
| S2-g | same; construction_13F (median holding 4 quarters, 48% still held after 1 year) | same | grid: {S2 as written}, {sell on failing any criterion of the form incl. P1}; average | grid | his revealed turnover (33% of the book new each year) is higher than "extended period" suggests |
| S3 | RS1/RS2 | none | a stock sold under S1 cannot be re-bought for the next quarter-end | convention | "sell and move on" (ZLA2-C027): no re-entry at the next scan |

## 5. SIZE

| id | card rule / claims | measure | comparison and number | TAG | why |
|---|---|---|---|---|---|
| Z1 | RZ1; ZLA2-C028 (always) | weight at entry | equal weight across the names held; cap 10% per name; the rest in cash | convention | "I shouldn't be placing huge bets": equal weight, and 10% is the common ceiling for a single holding in a diversified fund |
| Z2 | RZ1; construction_13F | number of names N | N = 21 (top 21 of the pass set by the ranking rule) | revealed-13F | median 21 names in his 13F |
| Z3 | RZ1; construction_13F | weight cap | 8% per name (largest weight 8%, 90th pct 9%); new positions start at 3.5% | revealed-13F | his revealed concentration |
| Z4 | none (mechanics) | rebalance | at each quarter-end only; positions drift between quarter-ends (no trimming of winners) | convention | buy and hold (RX1); no trim rule stated |

**Ranking rule inside the pass set (rule 5).** Unchanged from v1. He states no explicit order of preference. His long
criteria come in a fixed order (themes, market share with staying power, balance sheet, multiple: ZLA1-C007 to
ZLA1-C011). Themes are not computable, so rank by the next one: **Q04 gross margin TTM, highest first**; ties broken by
E04 (FY2/FY1 growth, highest first), the nearest trace of his "earnings two or three years out". Existing holdings that
still pass (S2) keep their place before new names fill free slots (RX1). Tag: convention.

## 6. The two forms

**DECISIVE form (quote and convention numbers only):**
pass = B1 (GICS groups 4520 + 4530) AND B3a (top half of same-sub-industry peers) AND B4a (< 2.0) AND B4b (> 0) AND P1
(<= 20 on the year-3 estimate, no floor), with A1. Hold every passer at equal weight, cap 10% (Z1); sell by S1 (-1.5% of
portfolio), S2 (failing B1, B3a, B4a or B4b), S3; rebalance at quarter-ends (Z4). Ranking rule only needed if a name
limit is imposed (it is not in this form). 11 criteria.

**FULL form:** decisive criteria with their grids averaged (B1-g, B3a-g, B4a-g, P1-g, S2-g) plus B3b and A2 (both also
in S2); N = 21 by the ranking rule (Z2), cap 8% with new positions at 3.5% (Z3). Report each grid cell and the average;
the average is the full-form result.

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
- RB3 market share (ZLA1-C008): no market-share data; only the gross-margin half is used (B3a level against
  same-market peers in both forms; B3b change in the full form).
- RP2 "his own view" of earnings (ZLA1-C011): his estimate is not observable; consensus FY2 carried to year 3 stands in
  (usually lower than his view for the names he likes).
- RS2 / ZLA2-C029 the 1% "re-evaluate" step, and the open 50 bp step (card section 4 row 1): no machine action; only
  the 1.5% exit is used.
- RZ1 "not huge bets": no number; 10% (convention) and 8% (revealed) stand in.

## 8. Coverage and main risk

**Coverage of his buy rules (decisive form):** of his 5 buy rules, the decisive form implements 3: RB1 fully (now by
the standard GICS reading of all four named groups), RB4 fully on convention numbers, RB3 in part (gross-margin level
against same-market peers; the margin-change half is now full form only; market share not computable) = 3 of 5 = 60%,
the same count as v1, with RB3 thinner in the decisive form than in v1. The full form adds RB3's change half (B3b) and
RB5 (as avoid A2 and in the short sleeve) = 4 of 5 = 80%. RB2, the first of his four long criteria, is still not
covered. Both price rules are used (RP2 on the year-3 basis, RP1 as "no floor"); of sell and size rules, RS2 (exit
step), RS1 (through RS2), RS4 (short sleeve) and RZ1 (convention) are used.

**Risk that v2 now fits his purchases rather than his words.** Every change was written after seeing which criteria
reject his purchases, so each must be read as possibly steered, however good its quote. The risk is largest where a
change targets one of the two biggest rejectors and the quote allows more than one reading: (1) P1 (rejects 59% in
v1): the move from FY2 to a year-3 estimate is supported by "two or three years out" (ZLA1-C011), and v1's own risk
section had already flagged FY2 as too near before any result, but the extrapolation formula (FY2 x FY2/FY1) is our
construction, not his, and it loosens the rule most for fast-growing names, exactly the ones he bought; the number 20
is unchanged. (2) B3b (rejects 46%): moving it to the full form rests on reading "keeps (or increases)" as a forward
claim about the moat (ZLA1-C044, ZLA1-C045) and on his cyclical-margin statements (ZLA1-C014, ZLA2-C044); the literal
reading v1 used is as defensible, and the move removes a large rejector from the decisive form without a number being
tuned, so it is the change most open to the charge of fitting; it is kept, unchanged, in the full form so the two
readings can be compared. (3) B1 widening (rejects 13%): "tech hardware" mapped to the GICS group name is a standard
reading, but it admits instruments, EMS and distributors that he never names, and it was made knowing some purchases
sit outside the v1 set; the narrow v1 set stays as a grid cell. (4) B3a peer change carries the least risk: its
effect on his purchases is not known in advance (it can raise or lower the pass rate by industry), and it follows from
"market share" being a within-market idea (ZLA1-C008, ZLA1-C043). No change touches a sell or size number, no new
number was introduced, and no criterion uses anything after the quarter-end. Because the file rests on two documents
with no held-out document, the only independent test of whether v2 reads his words better is a document or period not
used here; the recall result of v2 on the same purchases cannot by itself settle it.

Counts: BUY 5 criteria (B1, B3a, B3b, B4a, B4b; + 3 grids), PRICE 1 (P1; + 1 grid), AVOID 2 (A1, A2), SELL 3 (S1-S3;
+ 1 grid), SIZE 4 (Z1-Z4). Decisive form: 11 (BUY 4: B1, B3a, B4a, B4b; PRICE 1: P1; AVOID 1: A1; SELL 3: S1, S2, S3;
SIZE 2: Z1, Z4). Full form adds B3b, A2, Z2, Z3 and the 5 grids. Not computable: 10 fully + 4 partly = 14.
Changes from v1: 8 (B1, B1-g, B3a, B3a-g, B3b, P1, P1-g, S2).
