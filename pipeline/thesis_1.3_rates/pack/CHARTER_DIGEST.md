# Digest of the systematic charter (docs/research/fable/CHARTER_1.2.md, 2026-11-13), verbatim extracts

## 1. Verdict

The notes agree, mostly by assertion, on how to build trend: size by volatility, mix speeds, count price drivers
not markets, never time it. They do not establish why trends exist (four mechanisms conflict). Tests with numbers
come from one paper (U01), one blog (U02) and studies only described on air. Pods: Trend, Economic trend, Carry,
Value (existing book) and Curve carry (new, B1); the notes give no thesis for Carry or Value. Versions to average:
16, 2, 2, 1 and 2, each in four weekly tranches. The one pass has six diagnostics. It decides three Batch A items
(new commodity markets, a no-trade buffer, a faster book scaler) and four lines in pod specs, and adopts nothing;
the other 26 proposals are folded in or dropped. Largest unverified dependency: the one new pod rests on a seller's
unshown claims (U04). Rule 5 is open: no note dates a thesis before 2011; Economic trend's sources are 2017 and 2023.


## 3. The systematic pods

The notes are one paper on economic trend (U01) and six practitioner units on price trend. They support two pods as
theses (Trend, Economic trend) and one thin new candidate (Curve carry). Carry and Value are in the book, but their
theses must come from step 1.3 (QP15, QP08), which also fills the other B1 and B2 places; short-rate futures
(U01-T4) go to its rates note.

**Trend** (existing book; grid tested in Batch A2)
- Chain: macro change → investors digest information slowly (U04 MT116-C02-1 'slow digestion of information'; MT216-C12-1 'a journey that takes you from some valuation level to the new valuation level'); benchmark and career constraints are claim text of MT087-C11-1 only → the move continues for weeks to months → we hold its direction on many markets. ASSERTED in four
  notes (row 8), tested in none.
- Other side: not established. Fragments: allocators who rebalance against moves (U04 MT216-C14-X2; U05
  MT073-C15-2, C15-3). U07: the payment shrinks as capital arrives (MT070-C01-2). The rival mechanisms in row 8
  imply other payers.
- Before 2011: not established in the notes (U07's dated early text, QP14 of 1994, is about method). Fung and
  Hsieh (2001) would settle it (reader); the Opus check reads it.
- Instruments: 62 ids (18 equity indexes, 15 bonds and notes, 13 currencies, 16 commodities; panel.py:304-352; 61 distinct; plus cm_aqr_ew, trend only, to 2000 (panel.py:543-551; book.py:121-122)).
- Rule: position = average over versions of a score of the past 1-, 3-, 6- or 12-month excess return, times 40%
  over market volatility, equal weight inside four equal-risk asset classes.
- Engine: BASE 30%, CANDIDATE 45%, as the sign of 1-, 3- and 12-month returns (config.py:17, 20, 63;
  book.py:60-76).
- Stops working: markets pinned by policy (U06 MT014-C16-1); falls that reverse within days or stay shallow (U03
  MT194-C06-2, MT045-C12-2).
- The notes add the version grid, the breadth item and the crisis profile.

**Economic trend** (existing book)
- Chain: macro news → investors update slowly (not named) → prices move late in the direction of the news → we
  hold each market in the direction of the 12-month change in four macro themes (U01 C01-1, C02-3, C04-8). Only the
  end result is SHOWN (row 7). Other side: not established.
- Before 2011: no, on the pack's evidence: the sources are from 2017 and 2023 (U01 C03-7). I know no earlier
  source for the combined rule (reader); the paper cites Eichenbaum and Evans for one sign (U01 C14-15b). Unless
  step 1.5 finds one, the verdict rule (WORKFLOW section 5) makes this an Incubator pod, run in shadow.
- Instruments and rule: the same 62 markets. Per market, the average over four themes (consumer prices,
  trade-weighted currency, 2-year yield, risk appetite) of the 12-month change over its 10-year volatility, signed
  by the paper's table (signals.py:94-98, 210-219, 223-231).
- Engine: BASE 30%, CANDIDATE 15%.
- Stops working: prices detached from fundamentals for long (U01 C03-6, C09-5); a weak 2010s (claim text of C06-3; its quote is the row label 'Jan. 2010 - Dec. 2019'; 'quiet macro data' is reader).
- The notes add U01's reading and U07's null (row 7). Overlap with Trend: section 8, item 8.

**Carry** (existing book)
- Chain, other side: not established; the notes treat carry only as a sleeve beside trend (row 11).
- Before 2011: not established; step 1.3 should date it. Candidates (reader): Brunnermeier, Nagel and Pedersen
  (2008) for currencies; Gorton and Rouwenhorst (2006) for commodities.
- Instruments and rule: bonds and notes, currencies, four energy futures; no equities (signals.py:330-338;
  book.py:106). Half the sign of carry, half its rank within the asset class (book.py:131). Carry = bond yield
  minus the 3-month rate, the rate gap to the dollar, or the slope between the first two energy contracts.
- Engine: BASE 20%, CANDIDATE 25%. Stops working: a funding break (U06 MT083-C05-1, ASSERTED).
- The notes add form ideas only (carry against its own history, neutral to the market: U04 MT173-C15-3, C15-X2,
  MT173-C17-2), passed to step 1.3.

**Value** (existing book)
- Chain, other side, stop regime: not established. The notes say only that returns revert beyond about a year
  (U02 MT064-C20-2 'anything longer than a year is is when mean reversion kicks in'; MT044-C07-2 'In the very long run, it mean reverts') and that reversion belongs in its own engine (U04 MT116-C13-2) (claim text).
- Before 2011: not established; our protocol cites Asness, Moskowitz and Pedersen 2013 (TESTING_PROTOCOL.md:61);
  step 1.3 should date it.
- Instruments and rule: rank within the asset class of equity indexes on dividend yield, long bonds on real
  yield, currencies on five-year real depreciation (signals.py:352-384). Engine: 15% in both. The notes add nothing.

**Curve carry** (new; B1, or B2 if its history is not locked when B1 is registered)
- Chain: holders and hedgers of commodities trade the near contracts (reader) → near contracts lose more on each roll, the move to the next contract, than far ones (ASSERTED: 'doing it on the front has a negative roll yield', MT167-C03-X2) → the gap stays as pay for taking the other side (a premium 'shared between consumers and and and producers', MT167-C02-X1) → we hold the
  far contract against the near one (MT130-C08-1). ASSERTED by one seller. Other side: not established; U04 does
  not name who pays.
- Before 2011: not established. 'probably goes back 15 years' (MT130-C08-X1) is in the quote, but it dates the QIS-format design to about 2011; it is not a live record and does not establish pre-2011 documentation. Erb and Harvey (2006) date roll
  yield as a return source (reader); a pre-2011 source for this spread must be found in step 1.5.
- Instruments and rule: per commodity with a contract about 12 months out: long that contract, short the front,
  equal face value, sized on the spread's current volatility with a cap on the face value of each leg (U05's
  warning, row 12). One version is flat in backwardation (front price above the 12-month price).
- Engine: not built; nearest code bloomberg.py:128-142 and panel.py:254-261.
- Stops working: a supply shock that keeps the front above later contracts (U04 MT167-C02-2).
- Cannot be Core today: no registered live source (section 6).


## 4. Version grids

Each version is run as its own pod; the pod is the equal-weight average of its versions' positions. A dimension is
listed only where the right choice is uncertain, never because a level is expected to earn more.

| Pod | Dimension | Levels | Why uncertain | n |
|---|---|---|---|---|
| Trend | lookback | 1, 3, 6, 12 months | No speed can be chosen in advance (row 3). Our 1/3/12 was picked among four sets on design data (CHANGES.md:113-116); 6 months restores what that pick left out. | 4 |
| Trend | signal shape | sign; return over volatility, capped at 2 (book.py:70-76) | Sources prefer the graded form; our trial preferred the sign (row 4). | 2 |
| Trend | volatility estimate | hybrid (70% fast estimate from daily returns, 30% ten-year, with a floor); 36-month (vol.py:38-52) | The fast estimate may give up long moves (row 1) and was adopted on Sharpe alone (CHANGES.md:128). BASE runs one, CANDIDATE the other (config.py:23, 64). | 2 |
| Economic trend | signal shape | a smooth capped function (tanh) of the scaled change (signals.py:245); its sign (not built) | The paper does not say how a signal becomes a position (U01 section 4). | 2 |
| Carry | form | sign of carry; rank within class | Sources split: directional (U03 MT021-C13-1) or neutral to the market (U04 MT173-C15-X2). This is today's half-and-half. | 2 |
| Value | none | rank within class | The notes give no reason. | 1 |
| Curve carry | backwardation switch | always on; flat in backwardation | The switch is the seller's rule, described in 2025-26 after losses (U04 MT130-C10-4, C09-1): it may be hindsight. | 2 |

Totals: Trend 16 (4 x 2 x 2), Economic trend 2, Carry 2, Value 1, Curve carry 2.

Rebalance days: every pod runs in four weekly tranches (slices that decide one week apart; tranche 0 decides at
month end, as today), tested in the 1990-2010 weekly check, not in the monthly runs.

Fixed: sizing at 40% over volatility, equal weight in class, four classes at equal risk scaled over 36 months
(book.py:132, 138-139, 191; config.py:26-27); the hybrid estimate outside Trend; costs (book.py:46-57); the 12-month
change, four themes and sign table of Economic trend; the 12-month contract in Curve carry. Book: Core pods at
equal risk (WORKFLOW 5.1), 10% volatility target, 5x cap on total face value, per-market cap (config.py:28-30).

Batch A, as it follows. A1: data swap, one block at a time (U07-T4's method), alternative-commodity columns off,
st_us_2y removed (bd_us_2y's series is a superset: the same DGS2 months plus any stooq months before DGS2, panel.py:486-488, 496); registered as a design change before the run. A2: the grids and tranches,
with Sharpe reported by tranche and asset class. Three more items enter only if D1-D3 open them.

Fate of every VARIANTS level:

| Level | Fate | Reason |
|---|---|---|
| A0, B0, D0, G0, H0 (current markets, class weights, book scaler, commodity carry, themes) | fixed | A0 minus the doubled US 2-year note |
| A1 + alternative commodities | Batch A breadth item, gated by D1 | breadth is hygiene (rule 3); markets enter on their drivers, never on their results |
| A2 + wider emerging currencies | dropped | no design-era history in hand (forwards from about 2010 on LSEG; Bloomberg on campus only); no live source |
| B1 weights by first-factor loading | dropped | needs a smoothing choice (shrinkage) no data can make (U05 section 8); the built cluster weights changed nothing (CHANGES.md:54) |
| C0 hybrid, C1 36-month | versions in Trend | |
| C2 slow only | dropped | already 30% of the hybrid and its floor (vol.py:48-51) |
| C3 static at entry | dropped | not built; no design-era test in the notes |
| D1 6-month correlation x 1-month volatility | dropped as written | the audit found its source statement partly wrong; a faster scaler is a Batch A risk item gated by D3 |
| E0 sign 1/3/12 | versions in Trend, plus a 6-month lookback | rule 2 averages speeds; VARIANTS has no speed level |
| E1 continuous, average 10, cap 20 | version in Trend in the built form (cap 2) | Carver's scaling needs an estimated scalar and differs mainly in the cap (reader) |
| E2 volatility-regime attenuation | dropped | audit: no mechanism, grade weak; justified only by expected gain; U04 asserts the opposite |
| F0 monthly, day 1 | tranche 0 of four | |
| F1 day 3 | dropped as a level | the later tranches trade after the month-end turn |
| F2 weekly re-read | Batch A2 weekly tranches | a full weekly re-read is a speed change of unknown sign (U06-T3) |
| F3 no-trade buffer | Batch A cost item, gated by D2 | |
| G1 calendar spread | the Curve carry pod | |
| H1 forecast-based themes | dropped | no usable history and no live source for consensus forecasts |
| S0, S1, P0, P1 | dropped | nothing is selected; WORKFLOW section 6 fixes the holdout |
| Excluded list (carry tilt, geopolitical theme, spread trading) | dropped; spreads go to the step 1.3 rates note | section 5 |

## Lines of the charter that defer items to this thesis note
- theses must come from step 1.3 (QP15, QP08), which also fills the other B1 and B2 places; short-rate futures
- (U01-T4) go to its rates note.
- | U01-T4 short-rate futures | deferred to the step 1.3 rates note | LSEG history pulled, not read; our synthetic 3-month market lost (protocol_batch1.md:8) |
- | U05-T5 spread gate | recorded for the step 1.3 rates note and as the leg cap in Curve carry | the three built spreads are not traded (panel.py:353; signals.py:28) |

## 11. Independent check (Opus 5.5, 2026-11-13): summary

Full text: `CHARTER_1.2_check.md` (tables A-D per number, statement, premise and pre-2011 claim).

Verdict: PASS WITH CORRECTIONS. The pod list, the averaging logic and the accounting of the 34 proposals hold; no
error of the Carver note is carried.
- Numbers from sources (19): 11 are in the quote, 6 are summary only (U01's Sharpe figures are chart reads in claim
  text; the blog figures), 1 was misread ("15 years" is the age of a product design, not a live record), 1 has no
  claim id (2023, confirmed by our own doc). Numbers from our code and docs: 13 of 13 confirmed.
- Statements (27): 10 supported, 14 partly, 2 not supported (Value's reversion ids; the backwardation switch of Curve
  carry exists only in claim text), 1 contradicted (Curve carry "said to survive crowding": the quotes say the
  opposite). All corrected above.
- Diagnostic premises (6): D4 and D5 could be registered as written; D1, D2, D3 and D6 had hidden choices in their
  gates. The gates above are the corrected, fixed forms. D1's candidate-market part still waits for a locked history.
- Doubled market CONFIRMED by code reading: `bd_us_2y` and `st_us_2y` are the same series wherever the 2-year yield
  exists, in returns, daily volatility and every signal. The book has 61 distinct markets; the US 2-year note holds
  2/15 of each fixed-income block instead of 1/14 and can hold twice the per-market cap. Removing `st_us_2y` changes
  design numbers, so it needs a registered engine version (gm/CHANGES.md) before any run. Effect on Sharpe: unknown.

What the two unseen sources change (claim ids in the check, section 4):
1. Fung and Hsieh: trend pays like "bills and lookback straddles": strong positive skew, a mean that is not
   significant in the primitive strategy. Judged by Sharpe or linear alpha alone, a smoother rule that has given up
   that shape can win. A Trend pod should also be reported by equity state and against the published straddle factors.
2. Fung and Hsieh: trend funds earned in both equity tails (1987, 1990: in quote). Our engine lost in the 1987 crash
   from long equities (CHANGES.md:134-135). The crisis payoff is a property of how the rule is run, not of "trend";
   commodities showed no such payoff in their sample. Their funds held the least capital in stock indexes.
3. Eckhardt's firm does not resize with volatility ("we don't want to restrain it", MT020-C06-3, speaker Santino) and
   calls resizing a hidden reversion trade (C07-X1, Seibert); Eckhardt says alternative markets are "in practice ...
   actually worse" (C11-1) and wants distribution-free statistics needing 10-30 times more data (C12-2). All ASSERTED.
   This cuts against row 1, the dropped static end of the volatility grid, the breadth item, and normal-theory gates.

Open judgement points (not corrections; none is a decision for the user). Each is closed at the named step under the
rules already written, before registration:
| # | Point | Closed at |
|---|---|---|
| 1 | A static or slow-only volatility version in Trend: three sources give stated model uncertainty there, which is this charter's own test for a version dimension | pod spec 3.1-3.2 |
| 2 | A zero-slot shape report per pod: the five-state equity table per pod, and Trend against the Fung-Hsieh factors 1994-2010 (report only) | registration 3.4 (diagnostic pass) |
| 3 | Whether the breadth item earns a Batch A place, given Eckhardt and the commodity result of Fung and Hsieh | registration 3.4 |
| 4 | One mechanism per pod: Trend's signal includes carry; Economic trend's risk theme includes equity momentum. Make each a version, or write the blend into the thesis | pod spec 3.1-3.2 |
| 5 | Curve carry: two versions, or only "always on" (the switch is summary only) | thesis note 1.3 + pod spec |
| 6 | Economic trend under rule 5 (sources 2017 and 2023): Incubator would take 15% (CANDIDATE) or 30% (BASE) out of the traded book untested; the reading of "2022 positive" is not pre-committed | thesis register 1.5; registration 3.4 |
| 7 | Class risk as a version dimension in Trend (equal risk to equities against where trend funds held capital) | pod spec 3.1-3.2 |
| 8 | D5 may not separate slow reaction from a lasting state (a 3-month delay keeps 9 of 12 months) | registration 3.4 |
| 9 | Rule 5 for Trend: Fung and Hsieh (2001) document the strategy and its payoff but "are not advocating that markets trend". Does a documented strategy without a documented cause count? | thesis register 1.5 |

Not verifiable in this check: the blog digest numbers (no post text), QP14, the size of the doubled-market effect
(needs a run), contract start dates of 12-month LSEG contracts, LSEG licence terms for trading use.

Usage: Fable 5.2 max, one run, about 0.67M tokens; Opus 5.5 high check, about 0.36M tokens.
