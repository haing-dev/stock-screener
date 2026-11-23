# Pod spec: Card 2, regime and debt cycle (Bridgewater)

> **Status (2026-11-23): APPROVED WITH CORRECTIONS at step 3.2.** Written at step 3.1 (Opus, agent C); checked by a
> fresh Opus agent (checks/CHECK_3.2_C.md); its 5 corrections to this spec are applied. Claim ids and quotes
> script-checked (ALL OK). Nothing registered or run; open items go to step 3.4 (check section 4, NOTES_3.1_agent_C.md).

Step 3.1, Agent C, 2026-11-23. Nothing here is registered or run. Sources: CARD_1.4_regime_debt_cycle.md (final text,
29 corrections applied) and its check; THESIS_REGISTER_1.5.md rows T20-T22; code read in gm/signals.py, gm/book.py,
gm/config.py, gm/vol.py. RD = Dalio, BP = Prince, GJ = Jensen, KT = Karniol-Tambour. "Closed here" marks a choice the
notes left open.

## 0. Header

| Item | Value |
|---|---|
| Pod name | Card 2 regime and debt cycle |
| Type | discretionary pod = rule layer (R1, R2) + shadow analyst |
| Register rows | T20 R1 Not paid to hold, T21 R2 Rates-only repricing, T22 analyst layer |
| Source notes | card 2 sections 2 (chains 1, 5, 7), 4 (R1, R2), 5 (analyst), 6 (process), 7 (F1-F9), 8, 9, 10 (D1, D2), 13; check sections 2-4 |
| Register status | rule layer in Batch B2, Incubator at best (WORKFLOW s6; card s9 "Both rules are Incubator at best"); gated by C2-D2 (cases and overlap with card 1 R4); C2-D1 belongs to this card but acts on card 1's R1 and R2 and adds a stop line here; analyst shadow only |
| Dating class | C for R1 and R2 (register column 8); n/a for the analyst |
| What rule 5 allows | no holdout verdict; holdout descriptive only; best class Incubator; Core impossible |

## 1. Economic claim

R1 (RD, chain 1): as debt grows, holders need a real return, "if you don't have a return in relation to inflation that
is High Enough by holding that debt you won't hold that debt" (MT058-C06-3); the central bank then "is forced to choose
between is interest rates Rising a lot" (MT058-C07-2) or printing (claim text). Bond holders pay when yields rise. R2
(KT, chain 5): a 1.5-point rise in the 10-year yield lowers fair value by about 15% (MT147-C04-4); if stocks fell only
that much, no profit fall is priced, "the market is not expecting a very significant slowdown" (MT147-C05-2), and
shareholders pay when profits fall.
Evidence (card labels): chain 1 ASSERTED; chain 5 "SHOWN (one worked case; arithmetic, not evidence of returns)" (card
s2); card s9: "Both rules are Incubator at best". The register notes R2's live 2022 call scored wrong at 12 months.

## 2. What is predicted

| Rule | Quantity | Sign | Where largest |
|---|---|---|---|
| R1 | monthly excess return of bd_us_10y while the state is on (no tail) | negative | real yield low, and (gate version) bonds no longer hedge stocks |
| R2 | monthly excess return of eq_us_spx from the first on-month to 12 months after the last | negative | after a sharp rise in the 10-year yield that stocks have only partly priced; tight labour market (gate version) |
| Analyst | probabilities of the events in section 3A at 4 and 13 weeks | as stated | n/a |

## 3. Signal

Common (card s4, "taken from card 1 so the two layers net cleanly"): decision at month end t with data as known then;
lags GS10 0, CPILFESL 1, UNRATE 1; CPILFESL and UNRATE as first published where vintages exist, else latest, flagged
(closed here as in card 1: each month's first-vintage value; changes from two first-published values; share of
flagged months reported). Positions decided at t are held over t+1 and traded on the first trading day after t. Four
weekly tranches (charter s4; monthly design runs use tranche 0; weekly check 1990-2010). Every version run and
averaged; off = zero. Card 1's two entry versions are not used (card s4).

R1 Not paid to hold.
1. Real yield y(t) = GS10(t) minus the 12-month % change of CPILFESL (lag 1, first published).
2. Bar version a: on while y(t) < 0.0. Bar version b: on while y(t) is at or below the 33.3rd percentile of all values
   of y from its first month up to t, and only once at least 120 values exist (before that, version b is off).
3. Hedge gate (version): also require the correlation of the 12 monthly excess returns t-11..t of eq_us_spx and
   bd_us_10y (panel) to be above zero. Gate off: no such requirement.
4. Position: short bd_us_10y while on; off otherwise; no tail.
5. US only: the sheet names no inflation series for other countries (card).
6. Stop-working line (live only, not a gate in the backtest; card s8): WALCL rising over 12 months. If C2-D1 passes:
   a second live stop line, short rate TB3MS below 1.0 (card s10).

R2 Rates-only repricing.
1. Rise d(t) = GS10(t) minus GS10(t-12).
2. On when d(t) >= X (X = 1.5, her figure, or 1.0, reader) and the S&P 500 12-month % price change (^GSPC month-end
   close, t vs t-12) is >= -10 x d(t). Example: d = 1.5 requires a fall of no more than 15%.
3. Labour gate (version): also require UNRATE (lag 1, first published) at or below the lowest of the prior 240 monthly
   values.
4. Position: short eq_us_spx from the first on-month until 12 months after the last on-month.

3A. Analyst layer (card s5; WORKFLOW W3). Weekly snapshot, blind to other analysts, model id logged; probabilities at 4
and 13 weeks unless stated; Brier score against the event's base rate (step 2.2 scorer).
1. Daily 10-year Treasury yield on the horizon date at least 0.25 higher than on the question date.
2. Correlation of weekly SPY and IEF returns over the next 13 weeks above zero (13 weeks only).
3. For US, UK, Japan, Germany: 10-year bond, currency (dollar index for the US) and stock index all fall over 13 weeks.
4. Given the S&P 500's 12-month change and 10 x the 12-month change of GS10, SPY falls at least 4%.
5. SPY returns less than the equal-weight non-US stock indexes of the panel, in dollars.
6. US 10-year bond returns less than the equal-weight non-US 10-year bonds of the panel.
7. FXE rises; FXY rises.
8. 12-month change of CPILFESL in the last release before the horizon is 3.0 or more; T5YIFR higher than today.
9. At least two dissents at the next scheduled FOMC meeting.
10. One development no coded rule reads, with one forecast on the fixed asset list; for R1 and R2: would you override
    today's position, yes or no. Overrides are logged and scored by the rule's next 13-week return with and without
    them; they never change the rule's position (card s6, BP's side, "now you're going to live with it", MT049-C05-2).
The open forecasts F1-F7 go to the ledger as listed (F8 closed, F9 context only).

## 4. Markets

| Market | Role | Earliest usable design month |
|---|---|---|
| bd_us_10y | R1 short | 1975-01 |
| eq_us_spx | R2 short | 1975-01 |
| eq_us_spx, bd_us_10y returns | R1 hedge gate input | 1975-01 (12 months of panel returns exist from the 1960s) |
| bd_us_10y, bd_de_10y, bd_jp_10y, bd_gb_10y, bd_ca_10y and eq_us_spx, eq_de_dax, eq_jp_nikkei, eq_gb_ftse, eq_ca_tsx | C2-D1 inputs only (section 13) | first panel month of each |

No market enters through a gate.

## 5. Sizing

1. Volatility: engine hybrid estimate (gm/vol.py, CANDIDATE "hybrid"; charter s4 fixes it outside Trend).
2. Position while on = direction x 0.40 / vol (one leg per rule; book.family_positions convention). Equal risk between
   rules; nothing sized by conviction; "Survive first" (card s6): the pod sits under the book's caps in the shadow
   book. No stops (card s6: none given).
3. Rule position = mean over versions; pod = R1 + R2 (different markets, so no netting inside the pod).
4. No trailing volatility rescaling of a rule or the pod (closed here, as card 1).
5. Pod into the book: WORKFLOW 5.1 "Core pods at equal risk" against config.py CANDIDATE family_w, which has no card
   pod; this pod is shadow only; its share, caps and netting across cards (register B19) are for 3.4.

## 6. Version grid

| Rule | Knob 1 | Knob 2 | Versions |
|---|---|---|---|
| R1 | bar 0.0 / expanding lowest third (>= 120 months) | hedge gate off / on | 4 |
| R2 | X 1.5 / 1.0 | labour gate off / on | 4 |
| Total | | | 8 |

Averaged with equal weight inside each rule. Removed by a diagnostic: C2-D2 leaves out any version with fewer than 24
on-months or fewer than 3 episodes, or with more than two thirds of its on-months inside card 1 R4's state; a rule with
no version left is not run. No version is added by a diagnostic here (C2-D1 adds versions to card 1, not to this card).

## 7. Sample

Design window 1975-01 to 2010-12, monthly; both rules start 1975-01 (every input exists; version b of R1 needs 120
months of y, available long before 1975; the labour gate needs 240 months of UNRATE, from 1968). Eras 1975-89 and
1990-2010 (reported). Months excluded: none. Never 2011 or later.

## 8. Data

| Input | History, first date | Live, delay | Licence |
|---|---|---|---|
| GS10, TB3MS | FRED, 1953 / 1934 (reader) | FRED, lag 0 | free |
| CPILFESL, UNRATE | FRED / ALFRED first-published; vintage coverage of design years not confirmed (register D12) | FRED, lag 1 | free |
| ^GSPC month-end (Yahoo file read by signals.equity_dy and daily.py, not a panel series; first date not confirmed); panel eq_us_spx, bd_us_10y | free panel, 1975 | Yahoo / panel, 1 day | free |
| WALCL (stop line only) | FRED, late 2002 (checker's recollection) | FRED, lag 0 | free |
| Analyst series (daily 10-year yield, SPY, IEF, FXE, FXY, T5YIFR, panel) | live only | FRED / Yahoo | free |

Rule 7: every input has a free live source, but the pod cannot be Core (dating class C; WORKFLOW s6).

## 9. Costs

gm/book.py cost_bp: bd_us_10y 1.0 bp one way, 4 rolls a year; eq_us_spx 1.0 bp, 4 rolls; charged as in book.run.
Turnover: not given in the notes; R1 is a slow state rule, R2 has a 12-month tail (reader). Double-cost test applies.

## 10. What would prove it wrong

From card s8, fixed now, on the design window:
- R1: the 10-year's mean excess return in R1 on-months is no worse than in off-months (card's own falsifier).
- R2: the S&P's return in the 12 months after on-months is no lower than in other months (card's own falsifier); both sets use months up to 2009-12 only, so no 12-month look reads 2011.
- R2, mechanism check (reported with the falsifier): R2 claims stocks fall from a later profit fall, not from further
  rate rises; if the S&P's loss after on-months comes with GS10 rising a further 1.0 or more over the same 12 months (on-months up to 2009-12 only)
  in most episodes, the gain is a rates bet, not the profit bet she names (numbers this spec's).
- Loss path (P3): R1 loses most when the central bank prints and bonds rally with low real yields (chain 1's other
  branch); the window holds low-real-yield bond rallies (1975-76, 2008-10). R2 loses in a rate shock followed by a boom
  (window: 1980s). Flag "loss not seen": no.
- Analyst: Brier score no better than the base rate at the registered live checkpoint.

## 11. When it should stop working

Card s8: the central bank buys the bonds (R1 stop line, WALCL rising over 12 months; live only); short rates sit at zero
(chain 7; "rates were already zero it was sort of a breaking point of the paradigm", MT147-C02-X2; if C2-D1 passes, a
short rate below 1.0 becomes a stop line); the framework is public, with "many investors trying to chase the same"
(MT053-C03-1) thing. These are live review conditions, reported, not switches.

## 12. Knobs that were tuned

| Knob | Origin |
|---|---|
| R1 bar 0.0 | quote direction "High Enough" (MT058-C06-3); 0.0 = holder loses to inflation (reader) |
| R1 lowest third, 120 months | reader |
| R1 hedge gate, 12-month correlation above zero | reader, joining MT138-C06-X1 and MT068-C10-3; same window and threshold as the Macro Compass stockbond switch (data sheet; macro/registry.py derisk 4.1.0, bonds_if_corr_below 0.0), adopted there after backtests from 1975 that include the design and holdout years: seen in a related rule |
| R2 X 1.5 and multiplier 10 | quote (MT147-C04-4) |
| R2 X 1.0 | reader (earlier entry) |
| R2 12-month yield window | Compass window, not hers (card R2) |
| R2 12-month hold | card 1's convention |
| R2 labour gate at a 240-month low | reader ("in decades" read as two decades) |
| 0.40 / vol, hybrid vol | engine convention |

Chosen after seeing design results: 0 in gm_trials.csv and CHANGES; seen in a related rule of another tool: 1 (the hedge gate's window and threshold, Macro Compass). Chosen with sight of post-2010 history as the notes state it: none named
explicitly; both rules are hindsight-flagged (card s9).

## 13. Gating diagnostics

Zero slots, design months 1975-01 to 2010-12, no returns of the rule read.
- C2-D2 enough cases and overlap (gates each version of R1, R2). On-months = condition months, not R2's hold months
  (card). Episodes = runs of on-months at least 12 months apart (closed here as in card 1: a new episode starts at an
  on-month whose previous on-month is 12 or more months earlier). Gate: a version with fewer than 24 on-months or fewer
  than 3 episodes is left out of its rule's average. Overlap gate: a version whose on-months fall more than two thirds
  of the time in card 1 R4's state "(either threshold)" is left out; closed here: either threshold = the 4.5 state,
  which contains the 5.0 state. A rule with no version left is not run.
- C2-D1 room to ease (does not gate this card's rules). Countries with a 10-year bond, a stock index in the panel and a
  3-month rate on the card's list: US (TB3MS), Japan, Germany (IR3TIB01DEM156N then IR3TIB01EZM156N), UK, Canada. Code
  fact: the card's Swiss and Swedish rates have no panel bond or index (panel.py BONDS, EQUITY), so they drop out;
  Australia has a bond and index but no rate on the card's list. Per country, its worst fifth of design months for its
  stock index; mean 10-year bond excess return in those months when the short rate is below 1.0, against 1.0 or above.
  Gate (card): the other mean above zero and the low-rate mean less than half of it, on at least 30 low-rate months
  among the worst-fifth months pooled across countries (Japan also reported apart): a floor version (short rate at
  least 1.0) is added to card 1 R1 and R2, and a short rate below 1.0 becomes a stop line here. Fewer than 30 months: no
  change. Closed here: pooled as written; Japan alone may trigger it (note's text wins; check JP5).
Sealed months: none read.

## 14. Overlaps

Re-checked against the code:
- R1 against Value: Value is cross-asset only (book.family_positions: value kind "cs"; signals.value_values bonds =
  10-year yield minus trailing 3-year CPI mean, ranked inside the bond class), so it can be short bd_us_10y only
  relative to other bonds, never as a directional short. Confirmed.
- R1 against Economic trend: its inflation theme (headline CPI yoy change) and monetary theme (12-month change of the
  2-year yield) short bonds when inflation or rates rise (SIGNS FI -1); a level of the real yield is not in the pod.
  Partial overlap in rising-inflation months.
- R1 against card 1 R4 action A: both short the 10-year in 1975-81 (register C5): C2-D2 overlap gate.
- R1 agrees with card 3 R2's and card 4 R5's short 10-year legs; opposes card 1 R1, R2 (register C6, C7).
- R2 against Economic trend: the equity monetary theme is short US equities after a 12-month rise in the US 2-year
  yield (signals.themes m; SIGNS EQ monetary -1). The card's "Economic trend reads growth and inflation releases" is
  wrong for the code: partial overlap with R2's yield trigger (register C4). C2-D2 does not measure it; 3.2 does.
- R2 nets with card 1 R4-B, card 3 R4, card 4 R3, R4 shorts (register T21).
- "Not rules" (card s4): growth falling so long bonds is NOT held, since the code has no growth theme (config.py
  econ_themes: inflation, trade, monetary, risk; signals.ECON_THEMES). Inflation rising so short bonds and stocks, long
  commodities IS held by the inflation theme. Bonds of the country that can ease against one that cannot: not held as
  a spread (Economic trend is directional per country). A slow currency move: Trend holds it. 3.2 re-files the growth
  and spread items (register C1, T75).

## 15. Open choices

| # | Choice | Closed how |
|---|---|---|
| 1 | R2 6-month yield window (check JP1) | not added: the brief takes versions from the notes and register only (R2 = 4); recorded for 3.4, which may register it before any run |
| 2 | R2 labour gate measure (JP2) | kept as the card writes it; whether to replace it: 3.2 (C2-D2 may drop it) |
| 3 | R1 long side on GJ's "interest rates have risen and real interest rates have risen such that there is a place for bonds in portfolios" (MT068-C10-X1) (JP3) | not added: no rule text in the card, and the long would repeat card 1 R1, R2; recorded for 3.2 |
| 4 | D2 two-thirds threshold (JP4) | the note's number; 3.2 may set a different fixed number before any run |
| 5 | Japan alone triggers D1 (JP5) | closed: pooled as written (section 13) |
| 6 | F1 core vs headline (JP6) | 2.2-2.3 |
| 7 | Question 9 proxy (JP7) | W3 template |
| 8 | R2 5x version (JP8) | not added, as item 1; recorded for 3.4 |
| 9 | Chain 6 spread held by a pod (JP9) | code: not held (section 14); 3.2 re-files it |
| - | First-published reading, episode gap, "either threshold" | closed in sections 3 and 13 |
| - | Register vs note | none found |

## 16. Builder must not change

Signs (R1 short 10-year; R2 short S&P); R1 has no tail, R2 a 12-month tail; the window 1975-01 to 2010-12; the grid of
section 6 (8 versions), averaged; inputs and lags; FRED and the free panel as sources; engine costs and the double-cost
test; overrides never change positions.
