# Pod spec: Card 1, policy and liquidity (Druckenmiller, Bessent)

Step 3.1, Agent C, 2026-11-23. Nothing here is registered or run. Sources: CARD_1.4_policy_liquidity.md (final text, 45
corrections applied) and its check; THESIS_REGISTER_1.5.md rows T13-T19; code read in gm/signals.py, gm/book.py,
gm/config.py, gm/panel.py, gm/vol.py. D = Druckenmiller, B = Bessent. "Closed here" marks a choice the notes left open.

## 0. Header

| Item | Value |
|---|---|
| Pod name | Card 1 policy and liquidity |
| Type | discretionary pod = rule layer (R1-R5; R6 held back) + shadow analyst |
| Register rows | T13 R1 Squeeze, T14 R2 Tightening into warnings, T15 R3 Easing into strength, T16 R4 Behind on inflation, T17 R5 After the fall, T18 R6 Gold that ignores yields (held back), T19 analyst layer |
| Source notes | card 1 sections 2 (C1-C8), 4 (R1-R6), 5 (analyst), 6 (process), 7 (forecasts), 8, 9 (dating), 10 (D1, D2), 13; check sections 2-4 |
| Register status | rule layer in Batch B2, Incubator at best (WORKFLOW s6); gated by C1-D1 (episode count) and C1-D2 (already held); R1 and R2 may gain a floor version from C2-D1 (card 2); analyst layer shadow only (W3) |
| Dating class | C for R1-R6 (register column 8; card s9: "a recalled action is not a document"); n/a for the analyst |
| What rule 5 allows | no holdout verdict for any rule; holdout results descriptive only; best class Incubator; Core impossible (rule 6: hindsight-flagged pods run in shadow) |

## 1. Economic claim

Policy that is out of step with the economy is later reversed, and the positions built on the stated path lose. Who pays,
per rule (card s2): R1 analysts' earnings estimates (C3); R2 holders positioned for the Fed's stated path (C2); R3 late
buyers and lenders to weak borrowers (C1); R4 buyers of assets during late bond buying (C4); R5 the defending central
bank, "they had to buy an unlimited amount of Sterling" (MT203-C03-3).
Evidence grade, card labels (no card grades its rules strong / moderate / weak): C2 is SHOWN, one worked case, the
"350% 10-year equivalent" (MT148-C11-2); C3 is SHOWN (words); C1 and C4 are ASSERTED; C6 is SHOWN with numbers but is
one case, not two (card s1 item 3); C5 liquidity is ASSERTED and not coded. Every rule is hindsight (card s9).

## 2. What is predicted

| Rule | Quantity | Sign | Where largest (card) |
|---|---|---|---|
| R1 | monthly excess return of bd_us_2y and bd_us_10y over the 12 months after the condition last held | positive | after oil, dollar and rates rose together, once earnings fall ("it looks one year forward", MT151-C12-2) |
| R2 | same two legs | positive | Fed still hiking while warnings are on, before prices move ("there was no price movement", MT153-C11-2) |
| R3 | bd_us_10y (short) and eq_us_spx (long), 12-month tail | 10-year negative, S&P positive | easing while credit is tight and stocks rise |
| R4 | bd_us_10y and bd_us_2y (short); version B adds eq_us_spx (short) and panel commodities (long) | bonds negative, S&P negative, commodities positive | while core inflation is above 5% and Fed funds below it |
| R5 | that country's stock index (and 10-year bond in one version) | positive | after a G10 currency's fall far below its peers |
| Analyst | probabilities of the events in section 3A at 4, 13, 52 weeks | as stated | n/a |

## 3. Signal

Common to R1-R5 (card s4, check items 9-10, closed where marked):
1. Decision at each month end t with data as known then. Lags (data sheet): FEDFUNDS 0, GS2 0, GS5 0, GS10 0, BAA 0,
   TWEXMMTH 0, DTWEXBGS 0, WTISPLC 1, CPILFESL 1, M2SL 1. A lag of 1 means the last value used at t is month t-1.
2. CPILFESL and M2SL: each month's first-published value from ALFRED where a vintage exists; a change (12-month growth)
   is computed from two first-published values. Months with no vintage use the latest value and carry a flag; the
   share of flagged months is reported. Closed here: "first published" read as the value of the month's first
   vintage, the simplest form of the card's words.
3. A rule is "on" in a condition month. Its position runs from the first condition month to 12 months after the last
   one (R1, R2, R3, R5; card s4), except R4 (no tail). The 12-month tail is fixed (see section 15).
4. Positions decided at t are held over month t+1 (book.run convention, pos.shift(1)) and traded on the first trading
   day after t. Four weekly tranches (charter s4): tranche 0 decides at t; tranches 1-3 one, two, three weeks later with
   the data known on those days; each holds a quarter. Monthly design runs use tranche 0; the 1990-2010 weekly check
   runs all four.
5. Entry versions (pod level, card s6): E1 full size at the first condition month; E3 one third at the first condition
   month, full once that leg's cumulative excess return since the entry month end is above zero at a month end; once
   full it stays full to the end of the episode; a new episode starts at one third again. Closed here: "moved the
   trade's way" is judged per leg, on its cumulative panel excess return.
6. Every version is run and averaged; an off version counts as zero.

R1 Squeeze.
1. Inputs: WTISPLC; dollar index D = TWEXMMTH up to its last month, DTWEXBGS after (monthly average of daily values,
   the same averaging as TWEXMMTH, closed here); rate r = FEDFUNDS or GS10 (version).
2. Condition at t: x(t) > x(t-L) for each of WTISPLC, D and r, using the latest known values (WTISPLC compares t-1 with
   t-1-L). Each L-month change of D is taken inside one series: TWEXMMTH while both ends lie in its range, else
   DTWEXBGS (check item 11). L = 6 or 12.
3. Gate version: no position in a month in which R4's state at 5.0 is on (R4 step 2).
4. Position: long bd_us_2y and long bd_us_10y.

R2 Tightening into warnings.
1. Condition at t: FEDFUNDS(t) >= FEDFUNDS(t-T) + 0.25, with T = 6 or 12, and at least k of three warnings, k = 2 or 3:
   (a) GS5 minus GS2 < 0 ("we've inverted", MT152-C02-2); (b) BAA minus GS10 > its value at t-6; (c) 12-month growth
   of M2SL < its value 24 months earlier ("over the last couple years", MT152-C04-3).
2. In a month without GS2, warning (a) counts as not holding (closed here; affects only months before GS2 starts,
   which section 7 excludes anyway).
3. Gate version as R1 step 3. Position: long bd_us_2y and long bd_us_10y.

R3 Easing into strength.
1. Condition at t: FEDFUNDS(t) <= FEDFUNDS(t-3) - 0.25; and BAA minus GS10 below the median (version a) or at or below
   the 33.3rd percentile (version b) of its values from the first month both series exist up to t; and the S&P 500
   month-end price level (^GSPC close, the series panel.py reads; spx_trend live) above the mean of its last 10
   month-end levels including t.
2. Gold version: also require the panel gold level at a 12-month high, i.e. the cumulated cm_gold excess-return index
   at t is the highest of the 12 month ends t-11..t. Closed here: the index is built as book.trend_signal builds levels
   (cumulated panel excess returns), so history and live use one construction; live from GC=F.
3. Position: short bd_us_10y, long eq_us_spx.

R4 Behind on inflation.
1. Core inflation c(t) = 12-month % change of CPILFESL (lag 1, first published). State on while c(t) > H and
   FEDFUNDS(t) < c(t); H = 5.0 or 4.5 (both in quote, MT148-C02-2, MT148-C02-1). No tail.
2. Action A: short bd_us_10y and short bd_us_2y. Action B: A plus short eq_us_spx and long a commodity basket. The
   basket holds every panel commodity with a return that month (cm_wti, cm_brent, cm_natgas, cm_heatoil, cm_gasoline,
   cm_gold, cm_silver, cm_copper, cm_platinum, cm_corn, cm_wheat, cm_soybeans, cm_sugar, cm_coffee, cm_cotton,
   cm_cattle; not cm_aqr_ew, no Bloomberg alternative commodities), equal risk inside the basket. Closed here: action
   B has four legs at equal risk (2-year, 10-year, S&P, basket), so the 16 commodities do not outweigh the rest.

R5 After the fall.
1. Universe: G10 currencies in the panel, other than the dollar, whose stock index and 10-year bond are in the panel:
   fx_eur (mark, then euro: eq_de_dax, bd_de_10y; check item 20), fx_jpy (eq_jp_nikkei, bd_jp_10y), fx_gbp (eq_gb_ftse,
   bd_gb_10y), fx_aud (eq_au_asx, bd_au_10y), fx_cad (eq_ca_tsx, bd_ca_10y). Code fact: the panel has no Swiss,
   New Zealand, Swedish or Norwegian stock index (panel.py EQUITY), so fx_chf, fx_nzd, fx_sek, fx_nok are out.
2. For each, m(t) = % change of its month-end USD value (panel.fx_usd_value) over 6 months. Closed here: the price
   change, not the panel FX excess return, because the trigger is a break in the price.
3. Trigger at t: m(t) <= median of m(t) across the universe currencies with data that month minus G, G = 15 or 10
   points; at least three currencies must have data, else no trigger. Closed here: "those currencies" = the universe
   of step 1.
4. Position: long that country's stock index (version "stocks"), or long the index and its 10-year bond (version
   "stocks and bond"). 12-month tail per currency.

R6 Gold that ignores yields: HELD BACK, not built. Release condition: a quote of B (or D) in a pack that supports a
long gold position while nominal and real yields rise; card s4 and check item 21; step 1.5 searched MT203, MT141,
MT142 and found none. Until then question 8 covers gold. If released, its rule text is card s4 R6 as drafted (L 3 or
6, long gold), registered as a new trial. The check's other option (a short-gold rule on "a 5 10 could be 15%
pullback", MT203-C08-2) is for 3.2 and needs a new card text (register T18).

3A. Analyst layer (card s5; WORKFLOW W3). Weekly, from the fixed snapshot, blind to other analysts; model id logged, a
model change starts a new record. Each answer is a probability at 4, 13 and 52 weeks, logged before the week starts,
scored by Brier score against base rate and against trend continuation (step 2.2 scorer). Questions:
1. Chances that the R2, R3 or R4 condition (first-listed version, gate off) holds at the horizon, or none (one four-way
   Brier score); chance FEDFUNDS is lower.
2. GS10 higher. 3. SPY returns more than SHY. 4. WALCL minus WTREGEN minus RRPONTSYD higher (plus one line on the
   Treasury's borrowing plan). 5. Two or more of ITB, IYT, XRT 20% or more below their 12-month high; Compass jobs
   alarm on (today's count reported, not scored). 6. Latest 12-month change of CPILFESL higher than today's.
7. DTWEXBGS lower. 8. GLD higher; PCOPPUSDM higher. 9. Policy brake: up to three policies that must be reversed, each
   with a dated public act, its chance, market and direction; scored on the act. 10. Fat pitch: none, or one trade with
   market, direction, loss cap, a target at least five times the cap (reader's ratio) and its end condition; resolved
   at cap, target or 52 weeks; scored in units of the cap; weeks answered none counted.
Calls in 2, 3, 7, 8 are tagged with or against the 12-month trend and scored apart. The 11 open forecasts of card s7 go
to the ledger as they stand. The analyst never touches the trade list (rule 6) and never overrides the rule layer.

## 4. Markets

| Market (panel id) | Role | Earliest usable design month |
|---|---|---|
| bd_us_10y | R1, R2 long; R3, R4 short | 1975-01 (DGS10 month-end) |
| bd_us_2y | R1, R2 long; R4 short | first month of bd_us_2y in the panel (DGS2 plus stooq; panel.py BONDS, charter s4); reader's recollection: DGS2 from 1976-06 |
| eq_us_spx | R3 long; R4-B short | 1975-01 (French US market before SPY) |
| 16 panel commodities | R4-B basket | each from its first panel month; before about 2000 many are World Bank monthly average spot (panel flag "spot avg") |
| eq_de_dax, eq_jp_nikkei, eq_gb_ftse, eq_au_asx, eq_ca_tsx | R5 long | first panel month of each, not before 1975-01 |
| bd_de_10y, bd_jp_10y, bd_gb_10y, bd_au_10y, bd_ca_10y | R5 bond version | first panel month of each |
| fx_eur, fx_jpy, fx_gbp, fx_aud, fx_cad | R5 trigger input only, not traded | first month of panel.fx_usd_value; fx_eur before 1999: the panel's source (stooq eurusd) is not shown to be the mark in the code; builder records what it is |

Markets entering through a gate: none added. C1-D2 may remove a leg (section 13). Gold (cm_gold) is an input to R3's
version only.

## 5. Sizing

1. Volatility: the engine hybrid estimate (gm/vol.py estimate with config CANDIDATE vol "hybrid": 0.7 x fast EWMA,
   daily half-life 35 days where free daily data exist, else monthly half-life 6; 0.3 x 10-year; floor 0.75 x
   10-year), known at month end. The charter fixes "the hybrid estimate outside Trend" (s4).
2. Leg notional while on = direction x 0.40 / vol / k, k = legs of the rule (R1, R2, R3: 2; R4-A 2, R4-B 4; R5: 1 or 2
   per triggered country). 0.40 per market is the engine convention (book.family_positions). Closed here: each rule
   carries one unit of risk however many legs; legs are at equal risk (card s4); nothing is sized by conviction (card
   s6). Inside the R4-B basket each commodity gets 1/n of the basket leg.
3. R5 with several triggered countries: each triggered country is one unit (closed here: the rule is per currency).
4. Rule position = mean over its versions; pod position = sum over R1-R5; opposite positions in one market net (card
   s4). Flat when no rule is on: idle risk is not moved (card s6).
5. No trailing volatility rescaling of a rule or of the pod (closed here: a trailing scaler on a rule that is often
   flat would lever up its on-months). Tests compare pod and placebo in these units.
6. Pod into the book: WORKFLOW 5.1 says "Core pods at equal risk"; config.py CANDIDATE family_w (trend 0.45, econ 0.15,
   carry 0.25, value 0.15, xsmom 0) holds no card pod. This pod cannot be Core, so it runs in the shadow book only;
   its shadow share, the book caps (book.run: per-market cap, 5x gross) and netting across cards (register B19) are
   for 3.4. WORKFLOW 5.1 and TESTING_PROTOCOL B0.2 (45/25/15/15) disagree on book weights (register F8): 3.4.

## 6. Version grid

| Rule | Knob 1 | Knob 2 | Knob 3 | Versions | With entry E1/E3 |
|---|---|---|---|---|---|
| R1 | L 6 / 12 | rate FEDFUNDS / GS10 | R4 gate off / on | 8 | 16 |
| R2 | T 6 / 12 | k 2 / 3 | R4 gate off / on | 8 | 16 |
| R3 | spread below median / lowest third | gold high not required / required | - | 4 | 8 |
| R4 | H 5.0 / 4.5 | action A / B | - | 4 | 8 |
| R5 | G 15 / 10 | stocks / stocks and bond | - | 4 | 8 |
| Total | | | | 28 | 56 |

Averaged with equal weight inside each rule, never picked. Opened only by a diagnostic: C2-D1 (card 2) adds a floor
version (short rate TB3MS at least 1.0) to R1 and R2 if its gate passes, doubling each (+16, +32 with entry).
Removed by a diagnostic: C1-D1 (a rule with fewer than 6 episodes leaves the layer), C1-D2 (a leg above 80% already
held is dropped). R6 (2 versions, 4 with entry) is held back and not counted.

## 7. Sample

Design window 1975-01 to 2010-12, monthly. Rule starts (first month every input of at least half the versions exists):
R1 1975-01 (TWEXMMTH from 1973-01 plus 12 months; the 2-year leg from bd_us_2y's first month); R2 the first month of
GS2 (all versions read warning (a)); R3, R4, R5 1975-01 (R5 per market from its first panel month plus 6 months).
Eras as TESTING_PROTOCOL: 1975-89 and 1990-2010 (reported, not decisive: WORKFLOW s5). Months excluded: before each
rule's start; none inside. Never 2011 or later. The weekly-tranche check: 1990-2010.

## 8. Data

| Input | History source, first date | Live source, delay | Licence |
|---|---|---|---|
| FEDFUNDS, GS2, GS5, GS10, BAA, TB3MS | FRED; GS2 start not on the sheet (reader: 1976-06) | FRED, lag 0 | free |
| CPILFESL, M2SL | FRED / ALFRED first-published; vintage coverage of the design years not confirmed (register D12) | FRED, lag 1 | free |
| WTISPLC | FRED | FRED, lag 1 | free |
| TWEXMMTH, DTWEXBGS | FRED; TWEXMMTH from 1973-01, DTWEXBGS daily from 2006 (reader) | FRED (DTWEXBGS), lag 0 | free |
| ^GSPC month-end, panel returns (bonds, equities, FX values, commodities, gold) | free panel (gm/panel.py) from 1975 | free daily / monthly closes, 1 day | free |
| Analyst series (WALCL, WTREGEN, RRPONTSYD, ETFs, PCOPPUSDM, GC=F, GLD) | n/a (live only) | FRED / Yahoo | free |

Rule 7: every rule input has a free live source, but the pod cannot be Core in any case (dating class C; rule layers
run "for Incubator status only", WORKFLOW s6).

## 9. Costs

Engine costs (gm/book.py cost_bp, charged as in book.run: one-way cost on each change in position plus rolls on held
positions): US bonds 1.0 bp one way, 4 rolls a year; eq_us_spx 1.0 bp, 4 rolls; other developed equity indexes 2.0
bp, 4 rolls; WTI, Brent, heating oil, gasoline 4.0 bp, 12 rolls; natural gas 6.0 bp, 12 rolls; other commodities 4.0
bp, 5 rolls. Turnover: no figure in the notes; state rules with a 12-month tail change position rarely (reader). The
double-cost test (WORKFLOW decisive test 2, cost_mult 2.0) applies.

## 10. What would prove it wrong

Fixed now, on the design window, positions only from the rule; numbers are this spec's, from the card's direction:
- R1, R2: the averaged position earns a mean monthly excess return of zero or less over its held months; or, in more
  than half of the episodes, GS2 is higher 12 months after the last condition month than at it (the Fed did not reverse,
  against C2/C3).
- R3: the bond leg earns zero or more on its held months (rates did not rise after easing into strength); or the stock
  leg's gain comes only from months in which Trend's average S&P position is long by the same sign (no new source).
- R4: in state months the 10-year leg's mean excess return is zero or more.
- R5: the stock leg's mean excess return over the 12 months after triggers is zero or less; or it is positive only in
  episodes in which Economic trend's trade theme already held the same long.
- Loss path (protocol item P3): R1, R2 lose most in inflationary tightening; such months are in the window (1977-81).
  R3 loses in a melt-up that ends ("bought the exact top", MT069-C06-3; 1999-2000 in the window). R4 loses when
  inflation falls fast with bonds rallying (1982 in the window). R5 loses when a fall continues (crisis falls in the
  window, e.g. 1998 for the yen). Flag "loss not seen": no.
- Analyst: Brier score no better than the base rate at the registered live checkpoint (card s8).

## 11. When it should stop working

From card s8, as live review conditions (reported, never used to switch): bond buying that "suppressed all this
volatility" (MT152-C05-2) and guided policy; "the price signals that I learned how to read and how to listen to are
broken" (MT152-C11-3); D's own view that "Macro has been dead for 10 or 15 years" (MT069-C03-2). Stop flag (card s8,
reader): FEDFUNDS below 0.5 while WALCL is higher than a year earlier. Kill conditions are those of the shop's
registered live checkpoint (3.4); this spec adds no automatic switch.

## 12. Knobs that were tuned

| Knob | Origin |
|---|---|
| 12-month tail | quote: "it looks one year forward" (MT151-C12-2), MT046-C05-3 |
| R1 L 6 / 12 | Compass window / the model's horizon (reader) |
| R1 rate FEDFUNDS / GS10; R1, R2 R4 gate | reader; the gate was "made knowing 2022-23" (card R1) |
| R2 0.25, T 6 / 12, k 2 / 3, 6-month spread window, 24-month M2 window | reader; Compass window; "over the last couple years" (MT152-C04-3) |
| R3 0.25 over 3 months, median / lowest third, 10-month average, gold 12-month high | reader; quote for the trio: "to cut 50 basis points with credit spreads tight gold at new highs" (MT151-C01-5) |
| R4 5.0 / 4.5 | quote (MT148-C02-2, MT148-C02-1) |
| R5 15 / 10 points, 6 months | 15 is D's break size; 10 earlier entry; 6 months Compass window (reader) |
| Entry thirds | quote: "I tend to trade in thirds" (MT141-C10-8) |
| 0.40 / vol, hybrid vol | engine convention (book.py, charter s4) |
| Splice rule, first-published rule, basket legs, per-leg entry test | closed here (section 3) |

Chosen after seeing design results: 0 (no gm_trials.csv row or CHANGES entry touches any card knob). Chosen with sight
of post-2010 history, as the card says: 1 (the R4 gate). Every rule is hindsight-flagged in any case.

## 13. Gating diagnostics

Zero slots, positions only, no returns of the rule, design months 1975-01 to 2010-12.
- C1-D1 episode count (gates R1-R5). A month is on when any registered version's condition holds (tail months not
  counted; closed here, as card 2's wording). A new episode starts at an on-month whose previous on-month is 12 or more
  months earlier (closed here: the register notes the gap was not fixed). Gate: fewer than 6 episodes, the rule leaves
  the layer and becomes an analyst watch condition. Card: R4 is the likely casualty.
- C1-D2 already held (gates each leg). Share of months in which the leg holds a position (any version, tail
  included) where the registered systematic pods combined hold that market with the same sign. Combined = sign of the
  incumbent book's net position in that market (book.run "pos" of the registered CANDIDATE config with the specs of
  Agent A). Closed here: the register notes the combination was not fixed. Gate: above 80%, the leg is dropped.
- C2-D1 (card 2) room to ease: if it passes, R1 and R2 gain a floor version (TB3MS at least 1.0); see card 2 spec.
None of these reads a sealed month. The five "already held" thresholds across cards (80%, two thirds, 0.80/0.50,
0.80, 75%) are the notes'; 3.2 may set one (register C13).

## 14. Overlaps

Re-checked against the code (gm/signals.py, CANDIDATE config):
- R1, R2 long bonds against Trend (book.trend_signal: mean sign of 1/3/12-month excess return, short after yields
  rise) and against Economic trend's monetary theme (signals.themes: m = 12-month change of the 2-year yield, SIGNS FI
  monetary -1: short bonds after rates rise). Carry (signals.carry_values: yield minus 3-month rate) is short a bond
  whose yield is below the 3-month rate, so on an inverted curve it opposes R2 too. Confirmed.
- R3: the stock leg (S&P above its 10-month average) is close to Trend's long (C1-D2 measures it); after cuts Trend
  and Carry tend to hold bonds, so the bond leg is opposite (card; consistent with the code).
- R4: Economic trend's inflation theme (zchg of headline CPI yoy, OECD CPALTT01, lag 1) is short bonds and equities and
  long commodities when inflation rises (SIGNS FI -1, EQ -1, CM +1). Partial overlap: R4 tests a level of core CPI,
  the pod a 12-month change of headline. Card 2 R1 shorts the 10-year in the same 1975-81 months (card 2 D2).
- R5: Economic trend's trade theme (t = 12-month change of minus log BIS NEER, lag 1; SIGNS EQ trade +1, FI trade -1)
  is long a country's stocks after its currency weakens and short its bonds. So R5's stock leg partly repeats the pod
  and its bond version opposes it (register C3). Trend sells the falling currency (R5 does not trade it). C1-D2
  measures both at 3.2.
- Across cards: R1, R2 buy the 10-year and 2-year where card 2 R1, card 3 R2 and card 4 R5 sell the 10-year, and R2
  buys the 2-year where card 3 R3 sells it (register C7): nets in the shadow book.
Must be measured: C1-D2 at its run (before B2); netting check that nets leave no standing position at 3.2.

## 15. Open choices

| # | Choice | Closed how |
|---|---|---|
| 1 | R6 drop or short-gold form (check JP1) | held back; release condition in section 3; new text needed for any short form: 3.2 |
| 2 | 12-month tail against "if the reason I bought a stock is no longer the case I don't care what I paid for it" (MT151-C07-2) (JP2) | rule: tail fixed, registered with this deviation (register B14); no no-tail version, since the brief takes versions from the notes and none is in the card |
| 3 | R1/R2 gate at all (JP3) | kept as a version (card text); whether it may exist at all: 3.2 |
| 4 | Dollar index (JP4) | rule: the card's splice; the design window lies inside TWEXMMTH, live inside DTWEXBGS; DX-Y.NYB not used |
| 5 | Core vs headline CPI (JP5) | rule: CPILFESL, the only CPI on the data sheet; the episode-set difference is reported at C1-D1 |
| 6 | R5 misses a break inside a peg (JP6) | 3.2 with C1-D1 episode dates |
| 7 | Q9 self-chosen events (JP7) | 2.2 (ledger rules version) |
| 8 | Grade of C6 when both accounts are one trade (JP8) | closed by the register (T17: "one case, not two"); C6 is not coded |
| 9 | GS2 start (JP9) | rule: R2 starts at GS2's first month (section 7) |
| 10 | B's 2026 official statements in the ledger (JP10) | 2.3 |
| - | Episode gap, D2 combination, splice averaging, first-published reading, basket legs, R5 median set, per-leg entry | closed in sections 3 and 13 |
| - | Register vs note | none found for this card |

## 16. Builder must not change

Signs (R1, R2 long bonds; R3 short 10-year, long S&P; R4 short bonds, B also short S&P and long commodities; R5 long
index and bond); the 12-month tail and R4's no tail; the design window 1975-01 to 2010-12 and each rule's start; the
grid of section 6 (28 versions, 56 with entry), averaged; the inputs and lags of section 3; FRED and the free panel as
sources; engine costs (book.cost_bp) and the double-cost test; R6 stays held back.
