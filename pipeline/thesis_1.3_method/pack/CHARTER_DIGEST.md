# Digest for thesis note 1.3c (testing method): verbatim extracts

Extracts are copied unchanged from the repo files named in each heading. Their numbers are not ground truth for this note.

# A. Systematic charter (docs/research/fable/CHARTER_1.2.md, 2026-11-13)

## 1. Verdict

The notes agree, mostly by assertion, on how to build trend: size by volatility, mix speeds, count price drivers
not markets, never time it. They do not establish why trends exist (four mechanisms conflict). Tests with numbers
come from one paper (U01), one blog (U02) and studies only described on air. Pods: Trend, Economic trend, Carry,
Value (existing book) and Curve carry (new, B1); the notes give no thesis for Carry or Value. Versions to average:
16, 2, 2, 1 and 2, each in four weekly tranches. The one pass has six diagnostics. It decides three Batch A items
(new commodity markets, a no-trade buffer, a faster book scaler) and four lines in pod specs, and adopts nothing;
the other 26 proposals are folded in or dropped. Largest unverified dependency: the one new pod rests on a seller's
unshown claims (U04). Rule 5 is open: no note dates a thesis before 2011; Economic trend's sources are 2017 and 2023.

## 5. The one diagnostic pass

One pass on design months (1975-2010) with the existing engine, run with Batch A2 and logged. It adopts nothing
and uses no place in a batch's error budget (Holm slot). "Item" = a Batch A hygiene item or a line in a pod spec.
Thresholds are reader choices fixed here: 20% and one half come from the notes (U02-T3, U06-T2), the rest are mine.

| Id | Question | Computation | Merges | Gate, fixed now | Premise ids |
|---|---|---|---|---|---|
| D1 | How many independent bets does Trend hold? Which candidates bring a new driver? | Trend profit and loss per market at equal risk (book.py:60-76, 132) on the 61 distinct markets (st_us_2y dropped). Principal components (common factors) of monthly excess returns in each trailing 60-month design window, on markets with all 60 months; report, averaged over windows, the first factor's share of variance, each class's mean loading, and pod Sharpe over mean market Sharpe. Per candidate with a locked history: in the same windows, the share of its variance explained by the held markets' first three factors, and its R-squared on the single held market with the highest absolute correlation, each averaged over windows. | U05-T1, U06-T1 | A candidate joins the breadth item only if both averaged shares are under one half, it has 120 months before 2011 (TESTING_PROTOCOL.md:12), and it is costed at the 8 bp charged for EM currencies (U06-T2). The item is registered with the markets that qualify, under the 30% cap (book.py:140-148); if none, dropped. Candidate results are never read. | U05 MT205-C12-2, C13-1; U06 MT083-C08-2, MT111-C06-2, MT158-C13-1; U07 MT177-C13-1, C14-1 |
| D2 | How much trading is not caused by signals? | Rebuild positions with volatilities and scalers (the multipliers that bring each block and the book to target risk) held at last month's values, then with scores held (book.py:95-151, 191, 198); turnover = sum of absolute position changes (book.py:212-216). Cost drag per market (U02-T2 c) is reported. | U02-T2 (b, c) | If the non-signal share, 1 - (turnover with volatilities and all scalers held at last month's values) / (actual turnover), is at least 20% in both eras (1975-89, 1990-2010), a no-trade buffer is registered as a Batch A cost item (target: lower turnover, net Sharpe not lower); else dropped. Width: trade a market only if its target moves by more than 10% of its standard vol-adjusted position (MT026-C08-2: 'if it was less than 10%, I wouldn't bother trading'; 'standard position' is claim text), scaled by relative cost as in U02-T3 (MT026-C11-1: 'a wider buffer if an instrument's more expensive'); not B13's 10% of target. | U02 MT137-C14-1; MT026-C08-1, C08-2; no number relied on |
| D3 | Is book risk understated in states we can name? | Realised volatility of book returns over the next 12 months against the 10% target (book.py:197-199; config.py:28), split by (a) the sign of the trailing 12-month correlation of US equity and 10-year bond returns, (b) the top tenth of mean absolute trend score (book.py:72). Resampling (bootstrap) as stats.py:122-131. | U03-T3, U04-T2 | If either split shows realised forward 12-month volatility at least 2 points higher in the named state than in the other months, with the one-sided 90% bootstrap bound of that difference above zero (stationary bootstrap, mean block 12 months, because the forward windows overlap; seed as stats.py), a faster book scaler (U03-T3's form: 70% 12-month EWMA + 30% 36-month book volatility, floor 0.75 x the 36-month value) is registered as a Batch A risk item (target: realised volatility nearer 10%, worst fall not deeper); else dropped. | U03 MT194-C16-3, C17-1, C17-2; MT021-C06-1; U04 MT087-C07-1 ('if your barometer is 90%. Then more likely than not you have a lot of directional exposures'), MT087-C09-3 (performance only) |
| D4 | Does Trend lose early in equity falls and pay late? Does Carry lose in funding breaks? | Sort design months by the fall of the S&P 500 (eq_us_spx, compounded excess return; the source's base, MT194-C06-1) from its 24-month high; report the same table for the four-market average of protocol.py:200 (under 5%, 5-15%, over 15%) and its age (up to 2 months, more). Mean return of each family per cell (book.py:218-220) and in the six design-era stress windows (config.py:68-70). | U03-T2 | If Trend's mean is negative in the young 5-15% cell and positive beyond 15%, its spec lists "young, shallow equity fall" as an expected-loss state; else no such line. If Carry loses in both the 1998 and 2008 windows, its spec lists "funding break" as its stop state; else dropped. A cell with fewer than 6 months is reported, not used. | U03 MT194-C06-2, C06-4; MT045-C05-3, C06-1; MT021-C13-2; U06 MT083-C05-1 |
| D5 | Does the economic-trend edge fade when applied late? | Economic trend alone, net, positions applied 0, 1, 3, 6 and 12 months late (config.py:17, 32; book.py:208-209). | U01-T1 | If the Sharpe at 3 months' delay is under half the no-delay Sharpe, the spec claims slow reaction and names "no fading with delay" as what would prove it wrong; else it claims a lasting macro state. | U01 C01-1, C02-3, C04-8 |
| D6 | Is a weak trend year a year in which few markets moved? | Per design year and market: Sharpe of trend profit and loss at equal risk (book.py:60-76, 132) and of the market itself; regress the first on the absolute value of the second, by era (one regression per era on year-level cross-market means: mean trend Sharpe on mean |market Sharpe|; Newey-West slope standard error, 2 lags, extending stats.py:165-182, which returns only the intercept t). | U05-T2 | If the slope differs between eras by less than two standard errors, "trend return per unit of market move, against the design slope" is registered as Trend's breakdown check; else dropped. | U05 MT221-C07-1, C10-2; MT223-C12-1 |

Own-doc support for D3: realised 36-month volatility ran from 4.9% to 14.2% against 10%
(protocol_diagnostics.md:4, 6). D4's 15% is U03's figure (unverified); 5% and 2 months are U03's reader choices.

Proposals dropped, deferred or folded elsewhere:

| Proposal | Fate | Reason |
|---|---|---|
| U01-T2 sign audit | dropped | signs are fixed by the source and may not change after results (WORKFLOW 3.1); pruning cells is selection |
| U01-T3 forecast themes; U02-T4 attenuation | dropped | with levels H1 and E2 |
| U01-T4 short-rate futures | deferred to the step 1.3 rates note | LSEG history pulled, not read; our synthetic 3-month market lost (protocol_batch1.md:8) |
| U02-T1, U04-T4 forecast buckets | dropped | their only use was to decide on U02-T5, now a version |
| U02-T3 buffer; U06-T2 alternative commodities | Batch A items if D2, D1 open | U02-T3's premise was corrected by the audit (row 13); U06-T2's admission rule is kept |
| U02-T5 capped continuous trend; U04-T3 calendar spread | a version in Trend; the Curve carry pod | |
| U03-T1 volatility speed by shock | dropped | both estimators are averaged; Batch A2 reports each version in the stress windows |
| U03-T4 geopolitical risk | dropped | sources from 2024-26; the note itself expects a weak result |
| U04-T1, U06-T3 (and U02-T2 a) day-one loss, weekly re-read | folded into the Batch A2 tranche report | tranche 0 is the month-end trade; U04-T1's prediction is unclear in sign (section 8, item 7) |
| U05-T3 carry tilt of trend | dropped | justified only by expected gain, on evidence its source calls unproven; needs forwards not in hand |
| U05-T4 inflation split | dropped | gates nothing; its 4.5% boundary is claim text; the two eras already split high and low inflation (reader) |
| U05-T5 spread gate | recorded for the step 1.3 rates note and as the leg cap in Curve carry | the three built spreads are not traded (panel.py:353; signals.py:28) |
| U07-T1 shape audit; U07-T3 frozen against continuing | dropped | dimensions S and P are gone; tail and fragility lines are in the test sheet |
| U07-T2 real against simulated trend | dropped | results by lookback and era come with the versions; the CTA index series are not in hand |
| U07-T4 data corrections | the method of Batch A1 | |
| No-test lists U01-T5, U03-T5, U04-T5, U06-T4, U07-T5 | stand, with three changes forced by rule 2 | the sign form of Economic trend (U01-T5) is now a version; trend speed (U03-T5, U07-T5) is averaged, not settled; U06-T4's planted-error test was done as audit 1.1 |

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

# B. Thesis note 1.3a, rates and curve (docs/research/fable/THESIS_1.3_rates.md, 2026-11-14)

## 1. Verdict

Spec one new pod, **Strip reversion**: fade local bends in short-rate futures curves with QP06's two local rules.
Grade weak. Batch B2, behind every stronger candidate, and only if diagnostic R1 passes and daily prices are locked.
Do not spec: QP06's Treasury-bill form, whole-curve reversion (the engine's three built spreads stay untraded),
the QP07 model as a signal, a QP12 commodity forecast pod. Front-end carry is not a pod: short-rate futures
enter existing pods as markets (non-US only) through the charter's breadth check D1.
Established: on estimated Treasury yields 1973-2000 local reversion paid up to about five times the equity benchmark (rule 2-B; 3.3 times for 3-B)
per unit of risk before costs, and faded after the late 1980s. On traded Eurodollar futures a related curve model (QP07: long-run curve plus decaying habitat and date parts, one of 6 chosen by AIC) added
0.03 and 0.30 bp a trade (5- and 250-day holds) to always-long. Weakest link: no test of the local rule on traded prices.

## 5. Diagnostics

One, zero slots, design months only.

**R1. Are there local bends on the strip that are larger than their trading cost and still there a day later?**
- Computation: for the dollar strip at month-ends 1990-01 to 2010-12 and the six triples of neighbouring points
  (where a normal exists), take the curvature gap of 3.1 on the signal day and on the next day, each against the
  triple's round-trip cost as in the entry rule of 3.1 (half a bp per contract per side, times 2, times (2n+4)/(n(n+1)) for the curvature at point n). Count triple-months where both are larger than
  the cost and have the same sign; no return and no later change is computed.
- Data: daily settlement prices of dollar contracts 1-8; monthly prices from 1981-12 for the normal.
- Gate, fixed now: if at least half of the triple-months qualify, both versions go to B2 registration. If fewer, the
  pod is dropped unbuilt: without local bends above cost the spread version is only the whole-curve slope bet (row
  3). The run is logged as a design-data trial (step 7.1).

# C. Thesis note 1.3b, value / momentum / carry (docs/research/fable/THESIS_1.3_xs.md, 2026-11-14)

## 1. Verdict

- **Carry: thesis supplied for currencies and commodities (asserted), not for bonds (pattern, no mechanism in the pack); grade weak on this pack.** Payers: hedgers of commodities (QP08, asserted); for currencies QP08 asserts a risk premium (QP08-C04-5) and the savers who pay it are my reading (reader); borrowers who fix long rates (reader: QP08 names no payer for bonds). Evidence: one sellers' paper, 1990 to April 2015, before costs.
- **Value: thesis supplied with a reservation.** Grade weak: the pattern rests on words in two sellers' papers; the only per-class figure in a quote is the bond leg's 0.18, which fails (QP15-C19-2), and survivorship "will likely favor value and carry" (QP08-C26-4); payer not established. Working reading: investors chase winners until prices overshoot, and Value is paid when prices come back. Two rivals kept apart.
- **Cross-sectional momentum: neither a pod nor a Trend version.** Roughly, it is what is left of Trend once each asset class's average position is removed (QP08-C21-4; exact only for positions proportional to one shared signal, claim text; our Trend uses other lookbacks and sign or capped shapes, reader). No payer of its own; QP08 finds it the weaker form (Sharpe 0.42 against 0.96, QP08-C17-1, over 1990 to April 2015 including 52 sealed months, so not a design-era fact).
- **Registration:** Trend directional only. Carry in both forms: 2 versions, unchanged. Value cross-asset only.
- **Changes to the charter:** Value from 1 version to 2 (a second anchor for bonds and currencies). Carry's grid stays; equities stay out. Two zero-slot diagnostics (X1, X2).
- **Rule 5:** the pack dates neither paper before 2011. Step 1.5 must date older sources for both pods, or the verdict rule makes them Incubator.
- **Weakest link:** nobody establishes who pays Value. The risks the authors test do not explain it; funding-liquidity risk has the wrong sign (QP15-C03-4, C34-2; pooled with individual stocks); and the authors find the cross-asset pattern "difficult to reconcile under existing behavioral theories" (QP15-C53-3), which cuts against the working reading too.
- **Limits on everything:** before costs; both author groups sell these strategies; QP08's sample runs 52 months into our sealed years.

## 5. Diagnostics (zero slots, design months to 2010-12)

**X1. Is energy carry a calendar pattern?** Signals only.
- Why: QP08 measures commodity carry with "the first future and the contract exactly expiring one year later" (QP08-C10-3) and takes the calendar out of equity carry (C10-2). Our rule uses neighbouring contracts (digest); in a seasonal market their slope is partly the expected seasonal price change (reader).
- Compute: per energy market, over all month-ends with a signal, the share of the carry signal's variance explained by its twelve calendar-month averages. Engine signal.
- Gate: 0.25 or more (a materiality line fixed here, not tuned) replaces that market's signal, in both versions, by the signal minus the average, over all earlier months of the same calendar month (at least five; no signal before), of the signal minus its trailing 12-month average (the 12 month-ends up to and including that month-end, as in QP08's "1Y moving average", QP08-C10-2). Registered with the A1 design changes before any run. Below: no change.

**X2. Is Value paid by prices coming back, or by income?** Design-era returns in two parts.
- Why: the thesis says cheap markets get dearer; if the pay is all income, the leg is carry (rows 13, 14).
- Compute: per Value leg (equities, bonds, currencies) and version, split each market's monthly excess return into income (one twelfth of: dividend yield minus 3-month rate; bond yield minus 3-month rate; rate gap to the dollar; at the prior month-end) and price change (the rest; for bonds it includes roll-down, which cannot be split off without a second maturity). Apply the leg's positions to each part and sum, before costs. Engine panel.
- Gate: computed on the leg's averaged position (equal-weight average of its versions, as traded), over all design months in which the leg holds a position; a price part of zero or less enters the leg in the thesis register (1.5) as paid by income; its design-era return may then not be cited for the Value thesis in the spec, the batch review or the hold-out verdict. Positive: no entry. No position changes. The split by leg goes into the Value and Carry specs.
