---
tags: [fable, thesis]
code_commit: 78799ed
---
> Step 3.1 spec, approved with corrections at 3.2. Inputs: _data/spec_3.1/. Register: [[Thesis register 1.5]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/78799edd251d9e74a749bd23aa6fc507e9a99d0c/docs/research/specs/SPEC_Card4_flows_volatility.md).
# Pod spec: Card 4, flows and volatility (Cem Karsan)

> **Status (2026-11-23): APPROVED WITH CORRECTIONS at step 3.2.** Written at step 3.1 (Opus, agent C); checked by a
> fresh Opus agent (checks/CHECK_3.2_C.md); its 4 corrections to this spec are applied. Claim ids and quotes
> script-checked (ALL OK). Nothing registered or run; open items go to step 3.4 (check section 4, NOTES_3.1_agent_C.md).

Step 3.1, Agent C, 2026-11-23. Nothing here is registered or run. Sources: CARD_1.4_flows_volatility.md (final text, 26
corrections applied) and its check; THESIS_REGISTER_1.5.md rows T28-T33; code read in gm/daily.py, gm/panel.py,
gm/book.py, gm/signals.py, gm/vol.py, gm/config.py. K = Karsan. "Closed here" marks a choice the notes left open.

## 0. Header

| Item | Value |
|---|---|
| Pod name | Card 4 flows and volatility |
| Type | discretionary pod = rule layer (R1-R4 daily date rules on the S&P 500, R5 monthly curve rule) + shadow analyst |
| Register rows | T28 R1 Year-end window, T29 R2 Option-cycle window, T30 R3 After the ramp, T31 R4 Month-end re-leveraging, T32 R5 Disinflation steepener, T33 analyst layer |
| Source notes | card 4 sections 2 (C2, C3, C5, C8), 4 (R1-R5), 5, 6, 7 (F1-F9), 8, 9, 10 (D1, D2), 11, 13; check sections 2-4 |
| Register status | rule layer in Batch B2, Incubator at best; C4-D1 may add a half-size sizing version to R1-R4; C4-D2 may fold R5 into card 3 R2; R1-R4 without weekly tranches (against rule 2: 3.2/3.4) |
| Dating class | B for R1, R2, R4 (the calendar pattern is dated before 2011: Rozeff and Kinney 1976; Ni, Pearson and Poteshman 2005; Ariel 1987; his re-leveraging mechanism is not); C for R3, R5; n/a for the analyst |
| What rule 5 allows | under the register's reading no rule is clear of the hindsight flag (class B is "hindsight-flagged unless step 3.4 reads rule 5 otherwise"); holdout descriptive only; best class Incubator; Core impossible |

## 1. Economic claim

Over days to months, index prices are set by forced flows more than by news (card s1). R1 and R4: funds that hold risk
constant must buy after gains, at month ends and 1 January, and under-invested managers chase, "Where people have to
chase" ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C04-3|MT206-C04-3]]). R2: dealers short puts buy stock back as the puts decay into monthly expiry; the support is gone
for "one to one and a half weeks" ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C08-4|MT076-C08-4]]) after. R3: large open interest at quarterly expiries turns a fall into
forced selling. R5: when "inflation cyclically is declining" a "counterintuitive steepener" ([[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C08-2|MT206-C08-2]]) starts.
Evidence (card labels): C3 re-leveraging "SHOWN (words): arithmetic stated, no data"; C2 ASSERTED (the 95% has no data
behind it); C5 "SHOWN for one case (2020, dates in the quote)"; C8 ASSERTED by analogy with 1968-82. His own weight on
flows: "maybe 40% at at the best" ([[MT031 - Cem Karsan on the Market’s Quiet Fragility - Systematic Investor - Ep.379#^MT031-C08-3|MT031-C08-3]]).

## 2. What is predicted

| Rule | Quantity | Sign | Where largest |
|---|---|---|---|
| R1 | daily excess return of the S&P 500 inside the year-end window | positive (form C: sign of the year to date) | after a year of large gains ("end of year flows and a year that market is up 25% or very positive", [[MT183 - The Volatility Apocalypse - Systematic Investor 303#^MT183-C13-2|MT183-C13-2]]) |
| R2 | daily S&P excess return from N trading days before monthly expiry to expiry | positive | into expiry |
| R3 | daily S&P excess return in two short windows after a ramp | negative | quarterly expiries after a big year-end run |
| R4 | daily S&P excess return around the turn of the month | sign of the month to date | large monthly moves |
| R5 | return of the pair long bd_us_2y, short bd_us_10y (equal yield sensitivity) | positive | while core inflation falls |
| Analyst | probabilities, section 3A | as stated | n/a |

## 3. Signal

Common (card s4): panel markets as excess returns; rules at equal risk; opposite positions net (also against cards 1-3,
in the shadow book); nothing sized by conviction; every version run and averaged. R1-R4 are date rules on daily closes:
the dates are the signal, so no weekly tranches (fixed by the card; 3.2 checks it against rule 2). A date that is not a
trading day moves to the trading day before. Gates read the close of the day before entry. Expiry day X = the third
Friday of the month (the trading day before it if a holiday). R5 is checked at month end in four weekly tranches.

Daily S&P excess return (closed here: the panel holds monthly excess returns only). For trading day d in month m:
e(d) = ^GSPC price return of day d + c(m) / N(m), where c(m) = panel eq_us_spx monthly excess return minus the ^GSPC
monthly price return (dividends minus cash for that month; before SPY in 1993 also the gap between the French US market return and the S&P 500 price return, since the panel's eq_us_spx is the French market then) and N(m) = trading days in m. So a rule held all month earns
exactly the panel's monthly excess return. Live: SPY total return minus the daily cash rate. A rule's monthly return for the test sheet = the sum over the month's trading days of its position times e(d) (closed here).

R1 Year-end window.
1. Entry (version): close of the last trading day of October ("late October", [[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C05-X1|MT227-C05-X1]]), or close of the last
   trading day on or before 15 December ("the middle of December to the middle of January", [[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C04-2|MT206-C04-2]]).
2. Exit: close of the last trading day on or before 15 January ("till about the middle of January", [[MT104 - Market Structure, Liquidity, and Reflexivity in 2025 - Systematic Investor - Ep.368#^MT104-C17-2|MT104-C17-2]]).
3. Form A: always long. Form B: long only if the S&P close on the day before entry is above the previous year's last
   close (reader's bar), else flat. Form C: long if above, short if below (reader's reading of "a bit of a magnifier to
   whatever is happening going into the end of the year", [[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-2|MT163-C20-2]], as the sign of the year to date).

R2 Option-cycle window.
1. For each X: cycle length = calendar weeks from the previous X to this X (4 or 5).
2. Entry: close of the trading day N trading days before X. Four-week cycle: N = 12 or 15 (version); five-week cycle:
   N = 13 in both versions (his "two and a half" weeks; check item 6).
3. Exit (version): close of X; or close of the next trading day after X ("Opex Fridays and the Mondays are usually the
   strongest day", [[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C05-3|MT227-C05-3]]). Long only; flat in the gap after expiry.

R3 After the ramp.
1. Gate (reader's bar for "after a big run at the end of the year", [[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C08-2|MT132-C08-2]]): the S&P close on the day before entry
   is above its close on the last trading day of the preceding October.
2. Window 1 (version): short from the close of R1's exit day for 10 trading days ("January 13th to 15th window",
   [[MT132 - Regime Shifts, Populism, and 2025 Predictions - Systematic Investor 323#^MT132-C11-1|MT132-C11-1]]).
3. Window 2 (version): short from the close of February's X to the close of the first trading day after March's X
   ("CO started the day after Feb opex. It ended the day after March opex.", [[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C17-3|MT150-C17-3]]).

R4 Month-end re-leveraging.
1. T = last trading day of month m. s = sign of (close of day T-d-1 / close of the last trading day of m-1 minus 1).
2. Hold s (long after a rise, short after a fall, flat if zero) from the close of day T-d to the close of trading day d
   of month m+1. d = 3 or 5 (reader; "some major effects do fall at the end and beginning of months", [[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C02-5|MT206-C02-5]]).

R5 Disinflation steepener.
1. c(t) = 12-month % change of CPILFESL (lag 1, first published where vintages exist, closed here as card 1).
2. On while c(t) < c(t-6). Version 2 also requires FEDFUNDS(t) <= FEDFUNDS(t-6) - 0.25.
3. Position: long bd_us_2y, short bd_us_10y, the 10-year notional = 2-year notional x D2 / D10, par-bond modified
   durations at that month's GS2 and GS10, semiannual (the card 3 R2 construction). Off otherwise; no tail.

Sizing version opened by C4-D1 only (section 13): S&P legs of R1-R4 at half size while the D1 state is on at the
previous month end.

3A. Analyst layer (card s5; W3). Weekly snapshot, public calendars, blind to other analysts, model id logged;
probabilities scored by Brier score against the outcome's frequency since 1990 unless stated.
1. SPY's largest peak-to-trough fall on closes exceeds 3% within 4 weeks; exceeds 10% within 13 weeks.
2. SPY realised volatility over the next 4 weeks above the last 4 weeks (baseline 0.5).
3. VIXCLS higher in 4 weeks; in 13 weeks.
4. Days to X and whether quarterly; SPY higher at the close of X than today; SPY lower 5 trading days after X than at X.
5. For each scheduled Fed decision, inflation release, jobs report or election in the next 4 weeks: SPY higher 5 trading
   days after than at the close before.
6. October to March: SPY higher on 15 January than today; from 15 January, SPY falls 5% or more before the day after
   March's X.
7. Over 4 weeks the five industry ETFs with the best 6-month return do worse than the five worst (June to August tallied
   apart).
8. Over 13 weeks SPY and TLT both fall; GS10 minus GS2 (monthly averages) wider in the third month after the forecast
   month than in it.
9. Rank GLD, FXY, TLT, SPY by 13-week realised volatility against each one's own 5-year median (rank correlation;
   baseline last quarter's ranking).
10. WALCL higher in 13 weeks; SPY higher in 13 weeks, tagged crowd long / short / neither by a named public
    positioning figure (not a sentiment survey).
Plus the W3 standard set (direction and probability at 4 and 13 weeks on the fixed asset list). The open forecasts
F1-F9 go to the ledger as listed. Process lines registered for the analyst: path, not direction; fixed windows.

## 4. Markets

| Market | Role | Earliest usable design month |
|---|---|---|
| eq_us_spx (daily ^GSPC closes, gm/daily.py EQ_DAILY; panel monthly excess return) | R1-R4 | the first January for which daily ^GSPC closes exist from the preceding October on, not before 1975-01; the start of the daily file is not confirmed (register D10; SPY only from 1993) |
| bd_us_2y, bd_us_10y | R5 pair | first month of GS2 and bd_us_2y (reader: GS2 from 1976-06) |

No market enters through a gate.

## 5. Sizing

1. Volatility: engine hybrid estimate for eq_us_spx at the previous month end (gm/vol.py; daily EWMA from ^GSPC where
   daily data exist), fixed for the month; R5 on the pair's own monthly return series (as card 3 R2).
2. Position while a rule is on = direction x 0.40 / vol (engine convention, book.family_positions). Each rule carries
   one unit when on; "Size is fixed while a rule is on" (card s6).
3. Rule position = mean over versions (an off version = 0); pod = R1 + R2 + R3 + R4 net in the S&P (R3 window 1 may net
   against R2's January long; R1 ends at the close R3 window 1 starts) plus R5.
4. No trailing volatility rescaling of a rule or the pod (closed here, as card 1).
5. Pod into the book: WORKFLOW 5.1 vs config.py CANDIDATE family_w (no card pod): shadow only; share and caps for 3.4.

## 6. Version grid

| Rule | Knob 1 | Knob 2 | Versions | With C4-D1 sizing version |
|---|---|---|---|---|
| R1 | entry end-October / mid-December | form A / B / C | 6 | 12 |
| R2 | N 12 / 15 (13 in five-week cycles) | exit at X / next day | 4 | 8 |
| R3 | window 1 / window 2 | - | 2 | 4 |
| R4 | d 3 / 5 | - | 2 | 4 |
| R5 | inflation only / plus Fed cut | - | 2 | 2 |
| Total | | | 16 | 30 |

Averaged with equal weight inside each rule. The sizing version exists only if C4-D1 passes (+14). C4-D2 may remove R5
(folded into card 3 R2 as a note).

## 7. Sample

Design window 1975-01 to 2010-12. R1-R4: from the first January in which every input exists (section 4); daily rules
are evaluated on every trading day inside the window, and a window that would end after 2010-12-31 is cut at the last
trading day of 2010 (closed here: R1 entered in late 2010 is not held into 2011). R5: from the first month of GS2.
Eras 1975-89 and 1990-2010 (reported). Months excluded: none inside. Reported split (reader's knowledge, not in the
notes): listed S&P index options began in 1983, so R2 and R3 window 2 are also reported 1975-82 against 1983-2010.
Never 2011 or later.

## 8. Data

| Input | History, first date | Live, delay | Licence |
|---|---|---|---|
| ^GSPC daily closes | Yahoo daily file read by gm/daily.py; first date not confirmed | Yahoo / SPY, 1 day | free |
| eq_us_spx monthly excess return | free panel (French market before SPY 1993) | SPY total return, cash rate | free |
| Calendar (third Fridays, trading days) | calendar arithmetic | same | n/a |
| CPILFESL, FEDFUNDS, GS2, GS10 | FRED; CPILFESL first-published coverage not confirmed | FRED, lag 1 / 0 | free |
| VIXCLS (C4-D1 only) | FRED from 1990 | FRED, lag 0 | free |
| Analyst series (SPY, TLT, GLD, FXY, VIXCLS, WALCL, industry ETFs, public positioning data) | live | FRED / Yahoo / public | free |

Rule 7: every rule input has a free live source, but the pod cannot be Core (hindsight-flagged; WORKFLOW s6).

## 9. Costs

gm/book.py cost_bp: eq_us_spx 1.0 bp one way, 4 rolls a year; US bonds 1.0 bp, 4 rolls. For daily rules the one-way
cost is charged at every entry and exit, and the roll cost pro rata to days held (closed here). Turnover (reader's
arithmetic from the rule text): R1 one round trip a year; R2 about 12 to 13; R3 up to 2; R4 up to 12; so R2 and R4
carry most of the pod's costs. Double-cost test applies.

## 10. What would prove it wrong

From card s8, fixed now, on the design window:
- In his own terms: a long calm that ends with no fall at all (he names a slow grind as well as a break: "for a stair
  step down", [[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C06-1|MT227-C06-1]]; "the best outcome is a slow boil the frog", [[MT163 - The Calm Before the Storm- AI Risk, and Market Fragility - Systematic Investor - Ep.357#^MT163-C20-3|MT163-C20-3]]).
- R1: in years of large gains (S&P up 15% or more by the day before entry; number this spec's) the year-end window's
  mean daily excess return is no higher than in other years (card: "years of large gains whose year-end window falls").
- R2: the mean daily excess return inside R2 windows is no higher than on gap days (the support is the claim).
- R3: R3 windows show a mean daily excess return of zero or more after gated ramps.
- R4: the short leg's mean is positive (fights the documented turn-of-month effect, Ariel 1987; card s13).
- R5: version 1 is on in about half of all months (card s13); if the pair's gain comes only in months when FEDFUNDS
  falls (the 2-year rallying), it is Trend's easing trade, not his long-end sell-off (number: more than 80% of R5's
  P&L in months with FEDFUNDS down over 6 months; this spec's).
- D1: volatility rising with the market and no larger later falls (card s8).
- Loss path (P3): R2 has the profile 1.3c warns about, "95% of time" with violent exceptions (card s13); its loss event
  is a crash inside a pre-expiry window; the falls of 14-16 October 1987 lay inside an R2 window (X = 16 October 1987,
  reader's calendar arithmetic), and in the two versions that exit at the close of the next trading day the 19 October crash (the Monday after X) is inside the window; in the other two it falls in the gap. R1 and R4 lose in a
  year-end crash (window: 1987, 2008). Flag "loss not seen": no.
- Analyst: answers on width (questions 1-3) no better than base rates at the checkpoint (card s8).

## 11. When it should stop working

Card s8: when widely known ("knowledge is all dampening", [[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C06-5|MT227-C06-5]]); when daily options spread hedging over every day
(zero-day trading "can also unpin markets", [[MT183 - The Volatility Apocalypse - Systematic Investor 303#^MT183-C03-1|MT183-C03-1]]); when volatility supply shrinks, after a break or when rates
fall; when the state manages prices ("will things mean revert? Um in a natural system, yes.", [[MT016 - America's 250-Year Reset feat. Cem Karsan - Systematic Investor - Ep. 407#^MT016-C11-2|MT016-C11-2]]). Stated limit
(card s6): "never a pattern alone", he reads the calendar with flows the rule layer cannot see. Live review
conditions, reported, not switches.

## 12. Knobs that were tuned

| Knob | Origin |
|---|---|
| R1 entry dates, exit date | quotes ([[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C05-X1|MT227-C05-X1]], [[MT206 - Upcoming Big Changes in Global Markets - Systematic Investor 315#^MT206-C04-2|MT206-C04-2]], [[MT104 - Market Structure, Liquidity, and Reflexivity in 2025 - Systematic Investor - Ep.368#^MT104-C17-2|MT104-C17-2]]) |
| R1 form B bar (above last year's close), form C reading | reader |
| R2 X = third Friday | reader (standard listed-option convention, check) |
| R2 N 12 / 15, 13 in five-week cycles | from "one to one and a half weeks" and "two and a half" ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C08-4|MT076-C08-4]]) |
| R2 next-day exit | quote ([[MT227 - Yield Storm Ahead- Preparing for a New Era - Systematic Investor 330#^MT227-C05-3|MT227-C05-3]]) |
| R3 gate, 10-day hold | reader |
| R3 window 2 dates | quote ([[MT150 - Stagflation, Regime Change, and the Clues We Missed - Systematic Investor 347#^MT150-C17-3|MT150-C17-3]]) |
| R4 d 3 / 5 | reader |
| R5 6 months, 0.25 | reader, following card 1 |
| D1 half size, 1.25 | reader |
| Daily excess-return build, cost pro rata | closed here |

Chosen after seeing design results: 0. Chosen with sight of post-2010 history: none flagged by the card; every rule is
first stated 2024 or later.

## 13. Gating diagnostics

Zero slots.
- C4-D1 market up, volatility up (opens the sizing version and question 1's base-rate table). Month ends 1990-01 to
  2010-12. Up-months: S&P above its level 6 months earlier. State on if the month's average VIXCLS is above its average
  6 months earlier. Outcome: the largest peak-to-trough fall of the S&P on daily closes over the next 6 months divided by
  the annualised realised volatility of daily S&P returns over the past 3 months. Gate: median outcome in state-on
  up-months at least 1.25 times the other up-months, whole window and each half (1990-99, 2000-10). Pass: half-size
  sizing version; fail: analyst question only. READS SEALED MONTHS AS WRITTEN: month ends from 2010-07 read 2011
  prices. Proposal for 3.4 (register A, D15): the last state month is 2010-06, as card 5's check cut its D2.
- C4-D2 overlap of R5 (gates R5). Design months: share of R5's on-months inside card 3 R2's state (closed here: either
  of R2's two versions on), and share in which Trend is long bd_us_2y and short or flat bd_us_10y (closed here: by the
  average of Trend's registered versions, long = average signal above 0, short or flat = at or below 0; the register
  notes the versions were not named). Gate: either share at least 0.80 in both versions: R5 is not registered and passes
  as a note to card 3 R2.
The register's duplicate diagnostics of other cards do not cover R1-R4 against Trend; the placebo with shuffled dates
decides that (card R1).

## 14. Overlaps

Re-checked against the code:
- R1, R2, R4 long S&P days against Trend: Trend's S&P position (book.trend_signal, 1/3/12-month signs, CANDIDATE) is
  monthly and long in most rising years, so the date rules' long days often coincide (register C13). R4's monthly sign
  is close to Trend's 1-month horizon for a few days (3.2).
- R3 shorts what Trend holds after a ramp; nets with card 2 R2, card 3 R4, card 1 R4-B shorts.
- No pod reads the calendar (book.py: monthly decisions only).
- R5: same pair as card 3 R2 (register C6, D2); short 10-year as card 2 R1 and card 1 R3; card 1 R1 and R2 buy the
  10-year. Economic trend's inflation theme buys bonds when inflation falls (SIGNS FI inflation -1) on both maturities
  alike, so it does not hold the spread; Trend is probably long the 2-year while the Fed cuts (reader).
- "Not rules" (card s4): weak growth with hot inflation so short stocks and bonds: the growth half is not held (no growth
  theme, config.py econ_themes); hot inflation is held by the inflation theme; long gold and commodities in the
  inflation regime is held by the inflation theme (SIGNS CM +1). Yields up so stocks down = card 2 R2 and card 3 R4.

## 15. Open choices

| # | Choice | Closed how |
|---|---|---|
| 1 | Support before X: reading of "for the next two weeks" ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C07-4|MT076-C07-4]]) (check JP1) | kept as the card places it; confirmed at 3.2: [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293|MT076]] was uploaded 2024-05-02 and May 2024's expiry was the 17th, so the two weeks run into expiry, and the weakness comes after it: "a lot of the all that Bond and charm is now passed coming out of that weekend" ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C06-X1|MT076-C06-X1]]) |
| 2 | Daily S&P and daily cash back to 1975 (JP2) | closed: daily excess return built from ^GSPC daily plus the panel's monthly carry part (section 3); start rule in section 4 |
| 3 | No weekly tranches for date rules (JP3) | card text kept; 3.2 / 3.4 against rule 2 |
| 4 | Form C sign variable (JP4) | rule: year to date, as the card reads it; 3.2 may change it before registration |
| 5 | F8 growth bar (JP5) | 2.2 |
| 6 | Analyst horizons other than 4 and 13 weeks (JP6) | rule: the card's calendar horizons kept (fixed windows, card s6) plus the W3 standard 4- and 13-week set |
| 7 | Panel attribution (JP7) | 2.1 |
| 8 | R4 short leg against the turn-of-month effect (JP8) | placebo and double-cost tests decide (4.3) |
| 9 | Fed dates as a series (JP9) | buy-after-the-event stays dropped (register T91); question 5 uses the public calendar |
| - | Placebo for date rules | proposal for 3.4: move each window to a random start in the same calendar year (R1, R3) or month (R2, R4), same length and same sign rule |
| - | Index options before 1983 | reported split only (section 7); 3.2 |
| - | Register vs note | none found |

## 16. Builder must not change

Signs (R1 long, form C by year-to-date sign; R2 long; R3 short; R4 sign of the month to date; R5 long 2-year, short
10-year); the dates, X and N rules; no tranches for R1-R4, four for R5; the window and the 2010 cut; the grid of section
6 (16 versions), averaged; the daily excess-return build; data sources; engine costs, pro rata rolls and the double-cost
test.

