# Pod spec: Card 3, macro relative value and risk (Graham Capital, Elliott)

Step 3.1, Agent C, 2026-11-23. Nothing here is registered or run. Sources: CARD_1.4_relative_value_risk.md (final text,
41 corrections applied) and its check; THESIS_REGISTER_1.5.md rows T23-T27; code read in gm/signals.py, gm/book.py,
gm/config.py, gm/panel.py, gm/vol.py. "Closed here" marks a choice the notes left open.

## 0. Header

| Item | Value |
|---|---|
| Pod name | Card 3 macro relative value and risk |
| Type | discretionary pod = rule layer (R1-R4) + shadow analyst |
| Register rows | T23 R1 Hawkish currency, T24 R2 Steepener, T25 R3 Cuts priced too early, T26 R4 No alternative, T27 analyst layer |
| Source notes | card 3 sections 2 (C1-C7), 4 (R1-R4), 5, 6 (process), 7 (F1-F7), 8, 9, 10 (D1, D2), 13; check sections 2-4 |
| Register status | rule layer in Batch B2, Incubator at best; gated by C3-D1 (duplicate check) and C3-D2 (quiet months for R1's gate); R4 has no registered source (LSEG) |
| Dating class | C for R1-R4 (register column 8; card s9: every signal thesis hindsight); n/a for the analyst |
| What rule 5 allows | no holdout verdict; descriptive only; best class Incubator; Core impossible |

## 1. Economic claim

Central banks move against what markets price, and the side that trusted the path pays. R1: "the country that has the
most hawkish central bank has the strongest currency" (MT090-C07-1); other side not named. R2: a large deficit with no
pay for duration lifts long yields against short ones; long-bond holders pay ("people got killed in duration",
MT214-C07-3). R3: when the curve prices easing that inflation will not allow, holders of the guided path lose (C3). R4:
stocks dear against cash fall; buyers who "buy every dip" (MT089-C07-4) are the other side.
Evidence (card labels): C2 ASSERTED ("usually"); C3 SHOWN (words) for 2022, one case; C4 ASSERTED, one number in quote;
R4 no label beyond its quotes. The register adds: ledger currency rows that follow R1's idea 0 of 4; R3 has a premise
problem (measure 1 cannot be on at its own source case); both live uses of R4 lost.

## 2. What is predicted

| Rule | Quantity | Sign | Where largest |
|---|---|---|---|
| R1 | monthly excess return of the six currencies against the dollar (fx_jpy, fx_chf, fx_eur, fx_gbp, fx_cad, fx_sek) | long the currency whose 3-month rate rose most | when central banks are active (C1) |
| R2 | return of the pair long bd_us_2y, short bd_us_10y at equal yield sensitivity | positive (slope widens) | flat or inverted curve |
| R3 | monthly excess return of bd_us_2y | negative | easing priced while core inflation is high |
| R4 | monthly excess return of eq_us_spx | negative | forward earnings yield below cash |
| Analyst | probabilities, section 3A, 4 and 13 weeks | as stated | n/a |

## 3. Signal

Common (card s4): decision at month end t with data as known then; PCEPILFE as first published where vintages exist,
else latest, flagged (closed here as card 1: first-vintage values); state rules: on while the condition holds, off
otherwise, no tail; size fixed while on; held over t+1, traded the first trading day after t; four weekly tranches
(charter s4; design runs tranche 0; weekly check 1990-2010); every version run and averaged; off = zero.

R1 Hawkish currency.
1. 3-month rates: US TB3MS; Japan IR3TIB01JPM156N; Switzerland IR3TIB01CHM156N; mark then euro IR3TIB01DEM156N then
   IR3TIB01EZM156N; UK IR3TIB01GBM156N; Canada IR3TIB01CAM156N; Sweden IR3TIB01SEM156N. Before a FRED series starts,
   the LSEG 3-month deposit rate of the same currency; each L-month change is taken inside one series (check item 8).
2. Lag: 1 month for every rate in the row, TB3MS included (closed here: the card gives the row one lag, "1 assumed";
   equal timing on both sides of each difference). So the change used at t is r(t-1) minus r(t-1-L).
3. Change c_i over L months, L = 6 or 12, for the dollar and the six currencies.
4. Shape A: each of the six is long against the dollar if c_i > c_US, short if c_i < c_US, flat if equal.
5. Shape B: rank the seven changes; long the largest, short the smallest. If the dollar is the largest, the long leg is
   "long dollar" = short each of the other six as one equal-risk basket; if the dollar is the smallest, the short leg
   is long the other six as one basket. When the dollar is largest, the smallest currency is thus shorted twice (once
   as the short leg, once inside the basket): stated as the card's rule (check C).
6. Activity gate (version): on only while the highest minus the lowest FEDFUNDS of the last 12 months (t-11..t) is at
   least 0.50.
7. Positions in the panel FX markets (long a currency = long fx_xxx).

R2 Steepener.
1. S(t) = GS10(t) minus GS2(t) (lag 0).
2. On while S(t) < 1.0 (version a) or S(t) < the mean of S over all months from its first value up to t, once 120
   values exist (version b; off before).
3. Position: long bd_us_2y, short bd_us_10y, the 10-year notional = 2-year notional x D2 / D10, with D the modified
   duration of a par bond at that month's yield, semiannual coupon: D_n = (1 - (1 + y/2)^(-2n)) / y, y = GS_n / 100
   (check item 12; closed here: semiannual, the convention of panel.par_ret). The panel's built spread sp_us_2s10s (fixed
   durations 1.9 and 8.0) is not used: it is the untraded spread of register T43.

R3 Cuts priced too early.
1. Priced easing: measure 1 = FEDFUNDS minus GS2; measure 2 = 2 x (GS1 minus GS2). Lags 0.
2. Core inflation p(t) = 12-month % change of PCEPILFE (lag 2, first published).
3. On when priced easing >= 0.50 and p(t) > B, B = 3.0 or 4.0.
4. Position: short bd_us_2y.

R4 No alternative.
1. E(t) = 100 x LSEG S&P 500 12-month forward EPS (@:USSP500, A12FE; digest) at month end divided by the S&P 500 index
   level at the same month end (^GSPC close; closed here: the level the panel already reads).
2. On while E(t) minus TB3MS(t) < B, B = 1.0 or 0.0. Position: short eq_us_spx.
3. Lag 0: the consensus value as of the month end (Datastream monthly with a month-end start date returns the last
   weekday; digest).

Sizing version (all four rules, card s6): volatility used for sizing = the larger of the current estimate and its
expanding median (from its first value to t).

3A. Analyst layer (card s5; W3). Weekly snapshot, blind, model id logged; probabilities at 4 and 13 weeks, logged before
the week starts, Brier score against base rate and trend continuation; abstention allowed and logged.
1. FEDFUNDS at least 0.25 lower. 2. Name the most hawkish of R1's seven central banks; will its currency beat the
median of the seven against the dollar (scored on LSEG FX spot). 3. GS10 minus GS2 wider, with the reason (premium or
cuts). 4. Correlation of daily SPY and IEF returns over the window positive. 5. VIXCLS above 25 at any time. 6. The
panel market with the largest 6-month move in units of its 6-month volatility (126 daily returns x sqrt 126; free
daily markets only) extends by half a unit. 7. Name the scheduled event most likely to move dollar, 10-year and stocks
together; on that day UUP, IEF and SPY move as one trade. 8. For each open rule-layer position: its kind of risk
(directional, convergence, event), the path that loses most, and the chance it loses more than one risk unit (the
position's target standard deviation over the window), scored on the shadow record. 9. Next core PCE print puts the
3-month annualised rate above the 12-month rate. 10. SPY more than 10% lower.
The analyst never overrides the rule layer: "interventions that are not about Alpha ever" (MT062-C07-2). Open
forecasts F1, F3-F6 go to the ledger; F2 and F7 are context only (claim text).

## 4. Markets

| Market | Role | Earliest usable design month |
|---|---|---|
| fx_jpy, fx_chf, fx_eur, fx_gbp, fx_cad, fx_sek | R1 | first month with a panel return and a rate change of length L; with LSEG deposit rates from 1975 (digest), 1975-07 (L 6) and 1976-01 (L 12); fx_eur before 1999 is the panel's EUR series, whose pre-1999 source (stooq eurusd) is not shown to be the mark: the builder records it |
| bd_us_2y, bd_us_10y | R2 pair; R3 short 2-year | first month of GS2 (reader: 1976-06) and of bd_us_2y |
| eq_us_spx | R4 | first month of the LSEG forward EPS series (digest: 1985) |

No market enters through a gate. Code fact: only these seven rates and currencies; Australia, New Zealand, Norway are
not in R1 (card).

## 5. Sizing

1. Volatility: engine hybrid estimate (gm/vol.py, CANDIDATE "hybrid"); sizing version: max(estimate, expanding median of
   the estimate). For the R2 pair, the estimate is taken on the pair's own monthly return series built from panel
   bd_us_2y and bd_us_10y with each month's weights (closed here).
2. Leg notional while on = direction x 0.40 / vol / k: R1 shape A k = 6 (each currency one leg), shape B k = 2 (a
   basket leg holds its six currencies at equal risk inside it); R2 one leg (the pair); R3, R4 one leg.
3. Fixed size while on (card s6: Singer's reader's rule; register B16): the notional is set at the month a state turns on
   and kept until it turns off (each weekly tranche fixes its own notional on its own on-day). Closed here: "fixed size" read as fixed for the
   life of an on-run, since state rules already hold one size per month; this answers check JP5 by keeping it as a
   rule, not a version.
4. Signals net before sizing: "you can net the signals" (MT121-C06-2): opposite positions in one market net inside the
   pod; the beta cap is left to the book (5.1).
5. Rule position = mean over versions; pod = sum of rules. No trailing volatility rescaling of a rule or the pod (closed
   here, as card 1).
6. Pod into the book: WORKFLOW 5.1 equal risk vs config.py CANDIDATE family_w (no card pod); shadow only; share, caps,
   netting across cards for 3.4.

## 6. Version grid

| Rule | Knob 1 | Knob 2 | Knob 3 | Versions | With sizing version |
|---|---|---|---|---|---|
| R1 | L 6 / 12 | shape A / B | activity gate off / on | 8 | 16 |
| R2 | bar 1.0 / expanding mean (>= 120 months) | - | - | 2 | 4 |
| R3 | measure 1 / measure 2 | bar 3.0 / 4.0 | - | 4 | 8 |
| R4 | bar 1.0 / 0.0 | - | - | 2 | 4 |
| Total | | | | 16 | 32 |

Averaged with equal weight inside each rule. Removed by a diagnostic: C3-D2 (fewer than 60 gate-off months: the gate is
dropped and R1 has 4 versions, 8 with sizing); C3-D1 (a rule at 0.80 or more is dropped). No version is opened by a
diagnostic.

## 7. Sample

Design window 1975-01 to 2010-12, monthly. Starts (first month every input of at least half the versions exists): R1
1975-07 if every LSEG deposit rate starts in 1975-01 (the L 6 versions; L 12 join 1976-01); if a currency's rate starts
later, that currency joins when its change exists. R2 and R3 the first month of GS2 (every version reads GS2). R4 the
first month of the LSEG forward EPS series (digest: 1985). Eras 1975-89 and 1990-2010 (reported; R4's first era holds
about 60 months only). Months excluded: none inside. Never 2011 or later.

## 8. Data

| Input | History, first date | Live, delay | Licence |
|---|---|---|---|
| TB3MS, FEDFUNDS, GS1, GS2, GS10 | FRED (GS2 start not on the sheet) | FRED, lag 0 | free |
| IR3TIB01 3-month rates (JP, CH, DE, EZ, GB, CA, SE) | FRED research series (data sheet: "fetched for research", not in the live cycle); starts not on the sheet | none on the free cycle | free history; no live source |
| LSEG 3-month deposit rates | LSEG Datastream, from 1975 (digest) | LSEG on the user's PC, not registered as live | LSEG, not registered |
| FX returns (panel) | free panel | free daily, 1 day | free |
| PCEPILFE | FRED / ALFRED first-published | FRED, lag 2 | free |
| S&P 500 12-month forward EPS | LSEG @:USSP500 A12FE, from 1985 (digest; card and check say not in their pack) | LSEG only | LSEG, not registered |
| ^GSPC month-end; panel eq_us_spx | free | Yahoo, 1 day | free |
| Analyst: LSEG FX spot (Q2), VIXCLS, SPY, IEF, UUP | live | LSEG / FRED / Yahoo | mixed |

Rule 7: R1 (no live source for any foreign rate on the free cycle) and R4 (LSEG only) cannot be Core; R2 and R3 have
free live inputs; the pod cannot be Core in any case (dating class C; WORKFLOW s6).

## 9. Costs

gm/book.py cost_bp: G10 currencies 2.0 bp one way, 4 rolls a year; US bonds 1.0 bp, 4 rolls; eq_us_spx 1.0 bp, 4 rolls;
charged as in book.run. Turnover: not given in the notes; R1 shape A re-signs a currency whenever its rate change
crosses the dollar's (likely the highest turnover in the pod, reader). Double-cost test applies.

## 10. What would prove it wrong

Card s8 (a)-(d), fixed now, on the design window:
- (a) A rule is not positive after costs or fails its placebo.
- (b) R1's gate-on versions do no better than its gate-off versions (against C1).
- (c) The pod loses on average in the worst tenth of S&P months, against "about two thirds of three quarters of the
  time" (MT214-C03-3) negative correlation.
- R3, mechanism check: R3 claims the front end reprices toward inflation; if its short earns mainly through the
  negative carry it holds by construction (measure 1) rather than a rise in GS2 over its on-months, the source is
  Carry, not the mechanism (reported with C3-D1).
- Loss path (P3, named per rule): R1 loses when a hawkish currency is already crowded ("a crowded trade too",
  MT066-C05-2) and reverses, as in a flight to the dollar (1980s and 2008 in the window); R2 loses when an inverted
  curve inverts further while waiting (1978-81 in the window); R3 loses when the Fed cuts as priced; R4 loses when stocks
  keep rising from dear levels (1997-2000 in the window). Flag "loss not seen": no.
- (d) Analyst: a question scores worse than the base rate at the registered live checkpoint.

## 11. When it should stop working

Card s8: central banks on hold and guiding the path (their account of 2010-21); crowding, but the card records the
disagreement: the risk officer says "in times of the higher correlation we actually have a higher information ratio
among our PMS" (MT067-C05-2). Closed here (check JP6): crowding is a reported risk line, not a stop condition, because
the source's own risk officer contradicts it. Tropin expects decay: "there's no way you can do what worked 10 years ago
and expect it to always work in the future" (MT089-C06-3). R2 switches off by construction once the slope is above
the bar. Live review conditions, reported.

## 12. Knobs that were tuned

| Knob | Origin |
|---|---|
| R1 L 6 / 12 | Compass window / yearly span of his counts (reader) |
| R1 rate change as "hawkish" | reader (delivered, not promised) |
| R1 activity gate 0.50 | reader, "chosen knowing which decade was quiet" (card s13) |
| R1 lag 1, splice | card row ("1 assumed"); check item 8 |
| R2 bar 1.0 | number in quote, "The historical average since 1990 is about 100 basis points" (MT092-C01-3); its meaning as 2s10s is claim text, so reader's version; learned in 2025 |
| R2 expanding mean, 120 months; par durations | reader; closed here (semiannual) |
| R3 0.50 | his example (MT066-C04-X1, a reading of a garbled caption) |
| R3 measures 1 / 2; bars 3.0 / 4.0 | reader (target plus one, twice target) |
| R4 bars 1.0 / 0.0 | from "just under 19 that seems high to me" (MT089-C07-2) and 4-5% cash: gap 0.3 to 1.3 (reader) |
| Low-volatility floor | reader's remedy for MT067-C05-3 |
| 0.40 / vol, hybrid vol | engine convention |

Chosen after seeing design results: 0. Chosen with sight of post-2010 history, as the card says: 2 (the activity gate;
the 1.0 bar of R2, which the expanding-mean version exists to remove).

## 13. Gating diagnostics

Zero slots, positions only, design months 1975-01 to 2010-12.
- C3-D1 duplicate check (gates R1-R4). For each rule and version: share of on-months in which its sign equals the sign
  of the "Core book's" net position in the same market (for R2, each leg). Gate: 0.80 or more, dropped before B2; 0.50
  to 0.80 kept and flagged. Same count against cards 1 and 2 rules in shared markets (reported). AS WRITTEN IT CANNOT
  RUN: no Core book exists before B1 and B2 are judged (register A, H4). Proposal for 3.4 (the wording card 1's check
  fixed in its D2): read "Core book" as the registered systematic pods combined, i.e. the sign of the incumbent book's
  net position (book.run "pos", CANDIDATE config). Added reported lines (register C2, C8): R1 against Economic trend's
  monetary-theme currency positions alone; R3 against Carry's directional bond position alone. No gate on these.
- C3-D2 quiet months (gates R1's gate). Count design months in which the activity gate is off (FEDFUNDS 12-month range
  below 0.50). Gate: fewer than 60, the gate is dropped and R1 has 4 versions.
Sealed months: none read.

## 14. Overlaps

Re-checked against the code:
- R1 against Economic trend: the pod's currency score already holds this idea as its monetary theme: for each fx market,
  local minus US 12-month change of the 2-year yield (US, DE for the euro, CA, AU, JP) or of the lagged OECD 3-month rate
  (others), z-scored, sign FX monetary +1 (signals.themes m, econ_scores rel, SIGNS). R1 at L 12, shape A, is close to
  one quarter of that score (four themes); differences: tanh of a z-score, 2-year yields for JP, DE, CA. Confirmed
  (register C2). Measured in C3-D1's added line.
- R1 against Carry: Carry holds the higher rate (carry_values FX = local minus US 3-month rate); R1 the rising rate.
- R2: Trend trades each maturity alone; Value and Economic trend hold no curve spread (book: no sp_ market in any family
  is traded; signals.BD lists bonds only). Carry: on a flat curve the 10-year's carry is small or negative, so the short
  10-year leg may repeat it (C3-D1). Same pair as card 4 R5 (card 4 D2) and same short 10-year as card 2 R1.
- R3 against Carry: with measure 1 on, the 2-year yields at least 0.50 below FEDFUNDS; Carry's bond signal is yield
  minus the lagged 3-month rate (TB3MS for the US), so Carry's directional half (book.py kind "half": half sign, half rank) is short bd_us_2y in such months by construction, unless
  TB3MS sits well below FEDFUNDS (register C8). Economic trend's inflation theme also shorts the 2-year while inflation
  rises. R3 nets with card 1 R2's 2-year long.
- R4 nets with card 2 R2, card 1 R4-B, card 4 R3, R4 shorts; Karsan's "good timing mechanism" (MT104-C02-1) remark runs
  against it (register C14).
- "Not rules" (card s4): short bonds and stocks, long dollar while inflation rises and central banks tighten: partly
  held (inflation and monetary themes). The core-inflation point passes to the Economic trend spec (Agent A): the pod
  uses headline CPI (OECD CPALTT01), not core.

## 15. Open choices

| # | Choice | Closed how |
|---|---|---|
| 1 | Keep R3 measure 1 (check JP1) | kept as a version (card text); C3-D1 against Carry decides; a priced-peak measure on LSEG futures would be a new version: 3.2 |
| 2 | R1 US leg TB3MS vs LSEG US deposit rate (JP2) | rule: TB3MS (free, on the data sheet); the LSEG US deposit rate is a reported cross-check only |
| 3 | R1 duplicates Economic trend (JP3) | code facts in section 14; size at 3.2 with C3-D1's added line |
| 4 | Disputed ledger rows (JP4) | 2.2-2.3; both tallies carried (15 of 40, 15 of 35) |
| 5 | Singer's fixed size (JP5) | rule (section 5 item 3) |
| 6 | Crowding: risk line or stop (JP6) | risk line (section 11) |
| 7 | Sign of R2's carry on an inverted curve (JP7) | measured, not decided: reported from design positions at C3-D1 |
| 8 | F6 period (JP8) | 2.2 |
| - | C3-D1 "Core book" | note's text kept; cannot run as written; proposal for 3.4 (section 13) |
| - | Lag of the rate row, par-duration convention, pair volatility, R4 index level | closed in sections 3 and 5 |
| - | Register vs note | the register gives R4 a start "confirmed by the digest" (1985); the card says the start is not in its pack. Not a conflict of substance: the start comes from the digest, the card's text on the series is kept |

## 16. Builder must not change

Signs (R1 long the currency with the larger rate rise; R2 long 2-year, short 10-year; R3 short 2-year; R4 short S&P);
state rules with no tail; the window and starts; the grid of section 6 (16 versions, 32 with sizing), averaged; the
rate series, splice and lags; the duration formula; data sources; engine costs and the double-cost test.
