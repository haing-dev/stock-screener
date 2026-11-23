# Global Macro Book: statistical adoption protocol (pre-registered 2026-11-01)

Replaces the rule "adopt a change only if it raises net Sharpe in both 1990-2010 and 1975-89". That rule is a
two-coin sign test: it ignores how large and how noisy a difference is, and it can never pass a change whose data
start after 1989. Code: `gm/protocol.py` (tests in `gm/stats.py`). Written and committed BEFORE any batch below is run.

## 1. What is compared
- **Incumbent:** the current candidate config (`gm/config.py`, CANDIDATE = gm-2.0 at batch 1).
- **Challenger:** the incumbent with exactly one pre-registered change.
- **Returns:** monthly net returns of the whole book (costs, rolls, borrow included), 10% vol target.
- **Window:** design months only (1975-01 .. 2010-12; the holdout never enters), restricted to months where the
  challenger's new input exists. A window shorter than 120 months = "insufficient data", not tested.

## 2. Tests (all must pass)
| # | Test | Statistic | Pass if |
|---|---|---|---|
| 1 | Superiority | Paired stationary bootstrap of the Sharpe difference (Politis-Romano; mean block 6 months; 10,000 resamples; seed 20261101). One-sided p for H0: dSR <= 0, from the centred bootstrap distribution | Holm-adjusted p < 0.05 across the batch |
| 2 | Economic size | Point estimate dSR (annualised) on the window | dSR >= 0.05 |
| 3 | Non-inferiority per era | For each era (1975-89, 1990-2010) with >= 60 months of challenger data: one-sided 95% lower bound of dSR from the same bootstrap. An era with no new data must give identical returns (max abs difference < 1e-10) and passes | lower bound > -0.10 |
| 4 | Cost robustness | dSR at twice the costs on the window | > 0 |
| 5 | Tail (no "many small gains, rare big loss" profile; Harding 2002, Stine 2009) | Maximum drawdown and worst month on the window (both books at the same vol target) | max fall not worse by more than 2 points and worst month not worse by more than 1 point |

Reported but not decisive: Newey-West (6 lags) alpha t-stat of the challenger-minus-incumbent return against the
incumbent (the Foster-Stine value-add test); skew; Lo (2002) autocorrelation-adjusted Sharpe; the five-state equity
"smile". The bootstrap resamples whole months (all markets together), never single markets, because the 62 markets
are dependent.

## 3. Multiple testing and the trial count
- A **batch** is the list of challengers registered in section 5 before it runs. Holm's step-down correction is
  applied over every challenger in the batch, including any that fail to build (p = 1).
- Every challenger is logged in `gm/trials.csv`, so the whole-book deflated Sharpe counts it.
- A rejected idea is not re-run with tweaks inside the same batch. A changed version needs a new batch entry.
- Winners of a batch are combined into one config and re-tested once against the incumbent (tests 2-5 only; no new
  multiplicity). If the combination fails, winners are added one at a time in order of p-value, keeping each only
  if the combination still passes.

## 4. Why these choices
- Paired bootstrap: incumbent and challenger share most positions, so their returns are highly correlated. Pairing
  uses that, and the block bootstrap keeps autocorrelation and volatility clusters (Ledoit and Wolf 2008).
- Holm: controls the chance of any false adoption in a batch at 5% without the overly strict Bonferroni.
- dSR >= 0.05: below this a gain is within cost-estimate error and not worth extra complexity.
- Non-inferiority margin 0.10: about a third of the bootstrap standard error of a 15-year book Sharpe; a change may
  be neutral in one era but must not clearly hurt it.
- Data that start after 1989 (short-rate futures, forecasts, data surprises) are tested on their own window; the
  earlier era is then identical by construction, so test 3 cannot block them, while tests 1-2 still must pass.

## 5. Batches
### Batch 0: re-test of the gm-2.0 adoptions under this protocol (incumbent gm-1.2)
- B0.1 hybrid volatility.
- B0.2 family shares trend 45 / carry 25 / value 15 / econ 15 (with hybrid volatility, vs hybrid alone).
Consistency rule: a change that fails is reverted in the incumbent before batch 1.

### Batch 1: free data (from the quant-papers review, project doc quant_papers_review_2026-11-01.md)
- E1 economic trend as theme x asset-class portfolios (each block scaled to unit vol, themes equal risk inside the
  family; AQR Economic Trend 2023), keeping the tanh(z/2) scores.
- S1 US 3-month short-rate market (synthetic: -0.25 x monthly change in the month-end 3-month Treasury bill rate,
  FRED DTB3), traded by trend and economic trend with the US short-bond signals; counted at 0.25/1.9 of its notional
  in the gross cap (2-year equivalent). Other countries wait for Bloomberg futures (monthly-average OECD rates would
  create false trends).
- V1 bond value composite: average of the cross-sectional ranks of the real yield and of the 5-year rise in the
  10-year yield (Asness, Moskowitz and Pedersen 2013, Table I Panel C).
- V2 currency value skipping the latest 12 months (real change from t-60 to t-12), so value does not lean against
  the trend window.
- C1 bond carry per unit of duration in the cross-sectional half (2y 1.9, 5y 4.6, 10y 8.5, 30y 18), so long bonds are
  not favoured by construction (Baz et al., Man Group).

Diagnostics run with batch 1 (no adoption decision; they audit the 1.63 design Sharpe):
- trend family alone vs AQR's published TSMOM factor, 1990-2010;
- Lo-adjusted Sharpe, Sortino, skew, worst month, compound growth; rolling 36-month volatility vs the 10% target;
- Sharpe with each of the five biggest-contributing markets removed, and without 2008;
- five-state smile vs world equities; 1987 crash by family and asset class.

Considered and not registered (six-paper review, 2026-11-01; Chua-Koh-Ramaswamy re-read in full 2026-11-02):
yield-curve level and whole-curve slope mean reversion (lose to plain bonds in Chua-Koh-Ramaswamy 2006, Table 1);
their winning adjacent-maturity spread and curvature trades sit at the 11-12-24-month bill/note data seam and track
the size of the deviation (likely measurement noise), are not significant after costs for curvature, and need short-end
instruments we do not trade; Kalman forward-curve forecasts (no better than a random walk, Chua-Ramaswamy-Stine 2008).

### Batch 2: Bloomberg and zero-curve data (final list registered when the data arrive, before testing)
Planned: short-rate futures (contracts about 1 year forward) for US, UK, euro, Canada, Australia, Japan with trend,
economic trend and carry (implied minus spot 3m rate); bond carry with roll-down from zero curves (Fed GSW, Bank of
England, Bundesbank, Japan MoF; pre-1990 coverage allows both eras); commodity carry from the 2nd/3rd or 12-month slope
with same-calendar-month spreads for seasonal energy and grains; equity value composite; growth on first-release
data; bond futures returns vs yield-built returns (data audit).

## 6. Note on the holdout criteria
The standard error of an annual Sharpe estimated from 15 years is about 0.27 at a true Sharpe of 0.5 (Lo 2002). The
holdout pass mark (net Sharpe >= 0.3) is therefore about one standard error below a realistic live Sharpe: it screens
out a broken book, it does not prove skill.

## 7. Registration of the pod-shop programme (WORKFLOW step 3.4, registered 2026-11-23, BEFORE any run)

Nothing in this section has been run. It fixes, before any Batch A, B1 or B2 run: precedence between documents, the
reading of WORKFLOW rule 5, trade timing, the engine and data changes that must come first, the diagnostics, the
batches and their contents, the tests and thresholds, the trial count, the freeze, the holdout and the live
checkpoints. Sources are cited by file and section: register = docs/research/THESIS_REGISTER_1.5.md; specs =
docs/research/specs/SPEC_*.md; checks = docs/research/specs/checks/CHECK_3.2_*.md; power = docs/research/power/POWER_3.3.md;
1.3c = docs/research/fable/THESIS_1.3_method.md; charter = docs/research/fable/CHARTER_1.2.md.
A change to anything in this section after it is committed needs a new numbered sub-section (7.12, 7.13, ...) with its
date and reason, committed before the run it affects. Nothing here is changed silently.

### 7.1 Scope and precedence

1. Sections 1-6 of this protocol stay as written. They governed batches 0 and 1 (run 2026-11-01) and remain the record
   of those runs. They do not govern any run from Batch A on.
2. From Batch A on, this section governs every test, threshold and verdict. Where WORKFLOW.md and this section differ,
   this section wins; WORKFLOW.md stays the plan of work (steps, roles, order). Where a spec and this section differ on a
   test, this section wins; on a signal, market, sample or cost, the spec wins.
3. Market count: the engine has 61 markets, all distinct (gm-1.2.2 removed st_us_2y), plus cm_aqr_ew (trend only, to
   2000-12). Every "62 markets" in sections 1-6 reads "61 markets" from now on (gm/CHANGES.md gm-1.2.2 asked for this
   correction here).
4. Conflicts settled (register F1-F9; 1.3c section 11 item 3; checks):

| # | Topic | WORKFLOW (verbatim) | TESTING_PROTOCOL s1-s6 (verbatim) | Rule from now on | Reason |
|---|---|---|---|---|---|
| F1 | Error level per batch | "Each batch may wrongly adopt a useless pod with at most 2.5% probability (Holm inside the batch)." (s6) | "Holm-adjusted p < 0.05 across the batch" (test 1); "controls the chance of any false adoption in a batch at 5%" (s4) | Holm at 2.5% nominal per batch, over the Core-eligible systematic pods of the batch (7.7 T1). State with it: measured 3.0-3.3% at the null boundary (book Sharpe 1.23, correlation up to 0.3), up to about 5% for one pod at correlation 0.6; about 4% when Strip reversion is the only Core-eligible pod (250 months, rho 0.3: power s3.1 0.040, s3.10 0.038) | Two batches at 2.5% keep the programme near 5% (1.3c P2). 5% measured 5.3-7.0% (power s4 item 2). A nominal 1.25% would keep the 2.5% promise but costs 8-12 points of power at IR 0.4 (power s3.10); the excess at 2.5% is about 1 point at the correlations expected |
| F2 | Era test | "Reported, not decisive: the two eras" (s5) | "Non-inferiority per era ... lower bound > -0.10" under "Tests (all must pass)" (s2) | Reported, not decisive, for pods, rule layers and hygiene items | Decisive, it cuts full-sample pods at IR 0.4 from 0.56 to 0.23 and tests nothing for one-era pods (power s3.2, s4 item 6); for hygiene it drops a neutral change's pass to 0.11-0.94 (power s3.7) |
| F3 | Form of test 1 | "Adds to the book: alpha against the Core book, corrected for the number of pods in the batch." (s5) | "Paired stationary bootstrap of the Sharpe difference" (test 1) | Alpha of the pod on the Core book, centred stationary bootstrap p (7.7 T1). Sharpe difference at the held size: reported | Power at IR 0.4, rho 0.3: alpha 0.60 vs Sharpe difference 0.16 inside the full sheet (power s1 item 4); the Sharpe-difference form judges the held size, which belongs to 5.1 (power s4 item 1; 1.3c P2, D4) |
| F4 | Hygiene test | "must show it does not hurt and improves its own target" (rule 3); "Batch A: hygiene only ... Test = does not hurt." (s6) | "Superiority" with "Holm-adjusted p < 0.05" and "dSR >= 0.05" for every challenger (s2) | Non-inferiority (7.7 H1-H4); "improves its own target" decisive only for items with a written target (A3), reported for A1 and A2 | Superiority passes a neutral change 5% of the time: the wrong question (power s3.7, s4 item 7). A1 (data) and A2 (averaging) have no performance target: their purpose is fidelity and no picking |
| F5 | Double costs | "Survives double costs." (s5) | "dSR at twice the costs on the window > 0" (test 4, defined for a challenger) | Pods and rule layers: alpha at twice the costs above 0 (point estimate). Hygiene: dSR at twice the costs reported | Defines WORKFLOW test 2 for a pod (register F5; power s4 item 3) |
| F6 | Placebo | "Beats its placebo: the same pod with its signal dates shuffled in blocks, keeping the same average long/short exposure." (s5) | none | Decisive for every pod, rule layer and existing pod part (7.7 T3) | WORKFLOW decisive test 3; it is the only test that removes a standing exposure (power s3.5) |
| F7 | Batch names | "Batches B1 and B2: new systematic pods." (s6) | "Batch 2: Bloomberg and zero-curve data" (s5) | Batch names are WORKFLOW's: A1, A2, A3, B1, B2. The old "Batch 2" plan is closed item by item: short-rate futures = T10 (A3, gated); commodity 12-month slope = Curve carry only (B1/B2; Carry keeps F1/F2, so one signal is never registered twice); equity value composite = OFF (7.4); growth on first-release data = dropped (register T37); bond carry roll-down from zero curves = not registered (no spec); bond futures against yield-built returns = an A1 report line | One programme, one budget (WORKFLOW rule 4); CHECK_3.2_B s4 (Batch 2 overlap) |
| F8 | Book weights | "Book: Core pods at equal risk, volatility target, caps." (5.1) | "family shares trend 45 / carry 25 / value 15 / econ 15" (B0.2) | Batch A runs at the CANDIDATE shares (incumbent and challenger alike). The Core book (7.6 step 6 onward, freeze, holdout, live) holds its Core parts at equal risk | B0.2's vector was tested on a book that will not exist after 7.2 removes Economic trend from Core; a share vector is a fitted knob (counted in every spec s12); equal risk has no fitted parameter, and Sharpe ratios are not known (1.3c s5) |
| F9 | Incumbent | "against the incumbent net of its selection inflation (about 0.23 Sharpe)" (4.2); "alpha against the Core book" (s5) | "Incumbent: the current candidate config" (s1) | A2 and A3: incumbent = CANDIDATE gm-2.0.3 (7.4) as run at k = 1 on the A1 data; the 0.23 is printed beside the result, not subtracted. B1, B2: test 1 against Core book v1 (7.6 step 6) | As a margin shift, 0.23 passes a change that truly costs 0.2 at 0.55-1.0, and its own sd (0.11 over 32 variants) is as large as the margin (power s3.7, s4 item 7) |
| - | Deflated Sharpe | "deflated Sharpe from the trial log" (s5, reported) | "Every challenger is logged in gm/trials.csv, so the whole-book deflated Sharpe counts it" (s3) | Dropped as a reported line. Reported instead: the trial count and the selection inflation it implies (7.8) | stats_audit_2026-11-02 s2: the probability is 1.000 at 32, 100 and 300 trials, so it cannot change any reading |
| - | Expanding window | "Anything estimated from data ... uses an expanding window." (s5) | none | Read as "trailing or expanding, never full-sample". The engine's registered trailing windows stand | CHECK_3.2_A s4 item 2: point in time is the purpose; switching windows would be a new rule on seen design data |
| - | Citations (1.3c P1) | - | test 5 cites "Harding 2002, Stine 2009"; reported list "(the Foster-Stine value-add test)" | Test 5 reads: "Tail (realised falls not materially worse; Harding 2002). The profile 'many small gains, rare big loss' is the worry of Stine 2009, slides 4 and 44; this test sees such a loss only if it happened on the window." The reported line reads: "Newey-West (6 lags) alpha t-stat of the challenger-minus-incumbent return against the incumbent (the usual regression test of alpha; Stine 2009, slide 38, doubts the p-value of the plain t-test; Newey-West is on no slide)." | 1.3c P1 and section 11 items 1-2: no slide has a fall statistic; the Foster-Stine-Young test is the martingale test |

5. Martingale test (1.3c section 4): dropped, as a decisive test and as a reported line. A typical path clears the bar
   only at a Sharpe gap of about 0.84; even at the best scale it needs 0.41-0.60, and for the whole book the volatility
   convention sets the result (1.3c D1-D3, check item 5).
6. Book of record until the freeze: BASE gm-1.2.x stays the live paper book unchanged (including its 5% cross-sectional
   momentum family, register C12), apart from registered fixes. Cross-sectional momentum is not registered as a pod
   (register T12). After the holdout the book of record is set by WORKFLOW s6 (7.9).

### 7.2 Rule 5: what "documented before 2011" means and what it earns

1. The unit dated is a pod component: pod x asset class (leg) x version. This is the unit the register's sources
   date (register rows T03, T04, T05 are separate theses per Carry leg; T06's sources cover the equity leg only).
2. A component is documented before 2011 when one confirmed source dated before 2011 states its rule family: what is
   measured, the sign of the position, and the instruments (or an analogue the source itself names). The mechanism need
   not be documented, and parameters (lookbacks, thresholds, and the particular ratio inside a measure family the source uses, such as one valuation ratio for another) need not match; a row that relies on this clause says so.
   Reason: rule 5 exists because "205 of the 227 sources were recorded in 2024-26, and the models know market history to
   mid-2026" (WORKFLOW rule 5), i.e. to keep hindsight out of what the holdout tests. The holdout tests a rule's returns;
   if the rule family was public before 2011, the years 2011-2026 are out of sample for it, whatever story is told about
   it. A missing mechanism is already priced by the evidence grade (all pods are weak). Parameters are either averaged
   grids (no picking, rule 2) or engine conventions counted as knobs (7.8).
   Not enough: a pattern without a rule (register class B "pattern"), a mechanism without the rule, or a source dated 2011
   or later. Under the register's classes: A counts; B counts only where the source states the rule family; C never.
3. Classification (register column 8 and spec section 0; nothing new is dated here):

| Component | Source in the register | Rule family stated? | Rule 5 |
|---|---|---|---|
| Trend, every class and version; markets added through T09 (alternative commodities) | Fung and Hsieh 2001 (T01): trend-following futures strategies and their payoff; "we are not advocating that markets trend" (QP09-C06-4) | yes (trend following on futures of every class, position with the past move; the source models it as a lookback straddle, not our return-sign rule (register T01, SPEC_Trend s0), which item 2 treats as a parameter of the family; mechanism not) | qualified |
| Carry, currencies, version 2 (rank in class) | Lustig and Verdelhan 2007 (T03, class A) | yes | qualified |
| Carry, currencies, version 1 (sign) | Fama 1984 (T03): forward-bias pattern | pattern only | not qualified |
| Carry, energy, versions 1 and 2 | Erb and Harvey 2006 (T04): "rule form, no mechanism" | yes | qualified |
| Carry, bonds, versions 1 and 2; strips through T10 in Carry | none confirmed (T05, class C) | no | not qualified |
| Value, equities, versions 1 and 2 (same measure) | Asness, Liew and Stevens 1997 (T06): value across country indexes, on book to market | yes, under item 2's measure-family clause (rank of country indexes on a valuation ratio; the source's ratio is book to market, ours dividend yield, chosen on design data after the 5-year reversal failed, gm-1.1.0); without the clause: not qualified, and Value would have no Core part | qualified |
| Value, bonds, versions 1 and 2 | none (T06, T07) | no | not qualified |
| Value, currencies, version 1 | Rogoff 1996 (T06): slow PPP reversion, a pattern | pattern only | not qualified |
| Value, currencies, version 2 | QP08 (2015) | no | not qualified |
| Economic trend, all; strips through T10 in Economic trend | sources 2017 and 2023 (T02, class C) | no | not qualified |
| Strips through T10 in Trend | inherit Trend | yes | qualified |
| Curve carry | none (T08, class C) | no | not qualified |
| Strip reversion | Chua, Koh and Ramaswamy 2006 (T11): the rule on estimated Treasury yields; the paper names Eurodollar futures as giving "identical payoff" (QP06-C22-2) | yes (analogue named by the source) | qualified |
| Every card rule layer (cards 1-5) | WORKFLOW s6: "Rule layers of the discretionary playbooks run in B2 for Incubator status only" | n/a | never (rule 6 and s6), whatever the register class (card 4 R1, R2, R4 are B) |

4. What each status may earn:
   - Qualified: the holdout verdict counts (7.9); may be Core if every other Core condition holds (7.7 verdicts).
   - Not qualified: holdout result descriptive; Incubator at best (shadow, WORKFLOW rule 6); may be promoted later only
     on its live record (7.10), where rule 5 no longer binds because live months cannot be in hindsight.
5. Consequences, stated now (charter JP6 and JP9; register H1):
   - Economic trend leaves the Core book (15% of CANDIDATE, 30% of BASE). It runs as an Incubator pod.
   - Carry's Core part = currencies version 2 plus energy versions 1 and 2. Its Incubator part = currencies version 1 and
     bonds (both versions).
   - Value's Core part = equities (both versions). Its Incubator part = bonds and currencies (both versions).
   - Trend is wholly qualified.
   - Departure from WORKFLOW rule 1 ("the unit of work, testing and risk"), registered here: Batch A tests whole pods, but from Core book v1 on each Core part is tested (7.6 step 6) and held at its own equal-risk share, because rule 5 dates legs, not pods (item 1); the split decides which positions the
     Core book holds and which run in shadow.
   - No B1 or B2 pod can be Core under today's data: Curve carry is not qualified; Strip reversion is qualified but has no
     registered live source (rule 7, 7.10). Strip reversion becomes Core-eligible only if LSEG is registered as a live
     source (7.10 item 3) before B2 starts.
   - Power context (power s3.8; register G7): the holdout is a weak screen (all criteria pass 0.31 at true book Sharpe 0.4,
     0.58 at 0.8). A strict reading (class A only) would leave one version of one leg with a verdict and make the one-shot
     holdout judge almost nothing; this reading gives the verdict to the components whose rule could not have been chosen
     with sight of 2011-2026.

### 7.3 Trade timing, holding cut, tranche calendar

1. Decisive timing is k = 1: a position decided at the close of month-end t is traded at the close of the first trading
   day after t and held to the close of the first trading day after month-end t+1. Reported beside it: k = 0 (the
   engine's same-close form, book.py run, timing.py k = 0) and the one-period (one-month) delay of WORKFLOW s5.
   Reason: WORKFLOW s5 ("Every input is used with its live delay (free daily data: one day; official statistics:
   release date)"); the live rule is "trade on the first trading day after month end" (gm/CHANGES.md gm-2.0); the
   timing grid shows about 0.05-0.1 Sharpe lost per day late for the 1/3/12 trend (same entry), so k = 0 is optimistic.
2. k = 1 return of market m for the holding decided at t: the panel's monthly excess return of month t+1, plus the price
   return of m on the first trading day of month t+2, minus the price return of m on the first trading day of month t+1
   (carry and dividends accrue monthly, as timing.py assumes). It applies where a daily price of m exists on both days.
   Where it does not, the k = 0 monthly return is used and the market-month is flagged; the result sheet reports, by
   year, the share of gross position flagged. Costs are charged as today.
3. Pods with their own timing: Strip reversion trades at the next settlement by its spec (native k = 1, months from first
   trading day to first trading day). Curve carry trades at the decision-day settlement (k = 0) because no daily
   far-contract settlements exist; this departure is accepted and reported (spec s3 step 10; CHECK_3.2_B s4); its test 1
   uses the Core book's k = 0 returns so that both series cover the same days. Card 4 R1-R4 are daily date rules: entry
   and exit at the closes their spec names, gates read the close of the day before entry.
4. Information set at a decision: everything published by the close of the trade day. Monthly averages FRED publishes
   at lag 0 (FEDFUNDS, GS1, GS2, GS5, GS10, BAA, TB3MS) include the month's last business days, published by the next
   business day, possibly after the trade-day close: registered as a known one-day tolerance (CHECK_3.2_C s4 item 2), reported, no engine change. TWEXMMTH and DTWEXBGS monthly averages can contain weekly H.10
   values published up to a week later: this is registered as a known and documented deviation (at most one week of a
   6- or 12-month change; card 1 R1 only), reported, no engine change (CHECK_3.2_C s4 item 2).
5. Holding cut and seal: every holding period of every pod, tranche, rule and diagnostic ends at the close of 2010-12-31
   at the latest. No price, settlement or statistic dated after 2010-12-31 is read, printed or used before the holdout.
   Consequences: under k = 1 the decision at month-end 2010-12 is never traded; the holding decided at month-end 2010-11
   ends at the 2010-12-31 close (the move to 2011-01-03 is not read); Strip reversion's last return month is 2010-11 (its
   spec s7); card 4 windows that would run into 2011 end at the last trading day of 2010 (its spec s7).
6. Weekly tranches (rule 2): tranche j = 0, 1, 2, 3 decides on trading day 5 x j after the month's last trading day.
   Trading days = days the New York Stock Exchange is open; a market without a price that day uses its last price
   (SPEC_Trend s3, binding every pod: CHECK_3.2_A s4 item 9, CHECK_3.2_B s4). Each tranche holds a quarter of the pod
   from the close of the trading day after its decision day (k = 1) to the same point after its next decision day.
   Decisions dated after 2010-12-31 do not exist (tranches 1-3 of month-end 2010-12 decide in January 2011); holdings of
   tranches 1-3 decided in December 2010 end at the 2010-12-31 close.
   Monthly design runs use tranche 0 only. The tranche form runs only in the weekly-implementation check (1990-2010,
   reported). In it, a market without daily data holds its tranche-0 position all month and is flagged (register D9:
   free daily data lack non-energy commodities before 2000); coverage is reported. Curve carry has no weekly check
   until daily far-contract settlements are locked (its spec s7). Card 4 R1-R4 have no tranches: their dates are the
   signal, and tranches would move the dates (card 4 spec s3; register B17); this exception to rule 2 is registered.

### 7.4 Engine and data changes before any run

Each item needs its gm/CHANGES.md entry before its code (part (c) lists them), like C1-C4 and gm-1.2.2. None is chosen
from results.

| # | What | Why | Blocks |
|---|---|---|---|
| E1 | Bloomberg switches OFF by default, by registered config flags: Value's Bloomberg equity composite; Carry's farthest-contract commodity curve carry; the alternative commodity columns (until charter D1 admits a market through A3); Bloomberg growth surprise | Different measures on different markets, switched on by which tickers load (register D4-D6, D16); a Bloomberg-only input cannot run live (rule 7) | A1 and every later run |
| E2 | gm/bloomberg.py EQ_INDEX: remove the mappings eq_eu_stoxx50 -> "MXEM Index", eq_us_ndx -> MSCI USA, eq_us_r2k -> MSCI USA; every remaining mapping (a local index to the MSCI index of the same country) is used only if the A1 rule of 7.6 step 2 admits the series | Code defect (NOTES_3.1_agent_A item 3; CHECK_3.2_A s4 item 12) | any Bloomberg equity input (A1) |
| E3 | CPI as-of rule: a country whose OECD CPI series is quarterly enters a quarter's value at the end of the month after the quarter ends; gm/signals.py oecd_sdmx raises an error instead of returning an empty table when the csv cannot be parsed; a metadata job lists, per country, monthly or quarterly and the first date | Look-ahead (SPEC_Economic_trend s3; CHECK_3.2_A s4 item 7: a parse error silently moves every country to FRED) | A1, A2 (Economic trend, Value) |
| E4 | Value, 7 non-US equity markets: the trailing 12-month dividend yield used at month t is the one ending at t-12 (design and live alike); US (SPY) unchanged | The live Ken French file can be up to 12 months stale (ffill limit 12) while the design run used month t (CHECK_3.2_A s4 item 5); using the bound means live is never staler than the backtest. Reported: the lag-0 form | A2 (Value), Core book v1 |
| E5 | Seal and holding cut of 7.3 item 5 in every engine path (monthly k = 0 and k = 1, weekly tranches, daily date rules, diagnostics) | Sealed days were reachable through k = 1, tranches and forward windows (checks A item 9, C item 3; register D15) | every run |
| E6 | k = 1 return form of 7.3 item 2 with flags | 7.3 item 1 | A2 decisive and every later run |
| E7 | Version-grid machinery: each version computed as a complete pod, pod position = equal-weight mean of version positions at the unscaled stage, a missing version counted as 0 (SPEC_Trend s3 step 6); Trend 16, Economic trend sign shape, Carry versions 1/2 as separate signals, Value version 2 | No grid code exists in gm/ | A2 |
| E8 | Weekly tranche engine of 7.3 item 6 | No tranche code exists in gm/ (NOTES_3.1_agent_A item 12) | weekly check |
| E9 | Component masks (pod x class x version) so that the Core book holds only Core parts and the shadow book the rest; Core book at equal risk: each Core part's summed scaled-block return is rescaled to unit volatility (trailing 36-month realised volatility, lagged one month, as the block scaler) and weighted 1/n before the book scaler (book.py family weights alone give a 4-block part up to about twice the risk of a 1-block part) | 7.2, 7.1 F8 | Core book v1, B1, B2, freeze |
| E10 | Test code: alpha bootstrap (7.7 T1) in gm/stats.py; placebo engine (7.7 T3) for monthly signals, rule states and date rules; non-inferiority decision for hygiene (7.7 H1-H4) | Registered statistics need code; power s2 used vectorised copies checked against gm/stats.py | A2 onward |
| E11 | Spread pods: joint caps (a currency's whole Strip contract vector multiplied by the smallest ratio cap_j / abs(x_j); Curve carry's two legs share one cap from the front leg's hybrid volatility); per-instrument gross weight (3-month contracts at 0.25/1.9 of notional) | book.py clips each column alone, which breaks level neutrality (SPEC_Strip_reversion s5; SPEC_Curve_carry s5; CHECK_3.2_B s4) | B1, B2 |
| E12 | Strip market for T10 (only if admitted, 7.6 A3): return and carry formulas of SPEC_Carry s3; cost 8 bp per 2-year-equivalent unit = 1.05 bp per unit of strip face value; rolls 0.5 a year (one of eight equal contracts rolls each quarter: 4 x 1/8) | SPEC_Carry s3, s9 (the spec's 4 full rolls over-cost it by eight times; CHECK_3.2_A s4 item 8) | A3 breadth item |
| E13 | X1 seasonal adjustment of a market's energy carry, coded only if X1's gate opens for that market (SPEC_Carry s3) | register X1 | A1 design run |
| E14 | Daily S&P excess return for card 4 (spec s3: ^GSPC daily price return + the panel's monthly carry part spread over trading days) | No daily excess return exists in the panel | B2 card 4 |
| E15 | A1 data rule (7.6 A1) and the LOCK_v2 reader path; later, the LSEG source (7.10 item 3) and the GB / euro-area 3-month rate replacement (7.10 item 2) as data entries | Data changes are registered like rule changes | A1; LSEG items; live from 2027-01 |

Gate for E1-E5 (fix version, may change design numbers): the truncation test passes at all 8 cut dates for BASE and
CANDIDATE; tests pass; design statistics before and after reported once; one gm/trials.csv row per config, family
"fix". Gate for E6-E14 (feature version): BASE and CANDIDATE at k = 0 reproduce the fix version's reference exactly
(difference 0); truncation test passes, including the k = 1 and tranche paths cut at each date.

Code facts recorded, not changed (any change would need its own entry): Economic trend's euro trade theme reads
Germany's NBDEBIS; Germany's risk theme reads eq_eu_stoxx50 and is credit-only until about 2003-07 (CHECK_3.2_A s4
item 6); no mark series before 1999, so card 1 R5 and card 3 R1 lack the euro leg for 1975-98 (CHECK_3.2_C s4 item 8);
the 16 panel commodities are a hand-picked surviving universe (gm-1.2.0 "Known and documented").

Precondition outside the engine: every PC job that imports pandas or numpy fails today ("An Application Control policy
has blocked this file", gm_repro_v2, 2026-11-22). A1 (Bloomberg history stays on the PC, rule 7) and every LSEG reader
job are blocked until the user's PC runs them again. Free-data runs can run in the cloud on the same inputs zip.

### 7.5 Diagnostics (zero slots, design months only)

No diagnostic adopts anything or uses a Holm slot (charter s5). Each is logged as a design-data run (7.8). Gates are
those of the register section A and the specs, with the fixes named here.

| Id | Question (source) | Gate as registered | Fix at 3.4 | Pass does / fail does |
|---|---|---|---|---|
| X1 | Is energy carry a calendar pattern? (1.3b) | calendar-month means explain >= 0.25 of a market's carry-signal variance | none | that market's carry is seasonally adjusted (E13) before A1 / no change |
| D1 | Independent bets in Trend; does a candidate bring a new driver? (charter) | candidate joins only if both averaged shares < 1/2, >= 120 months before 2011, costed at 8 bp | extended to T10 strip markets: one candidate per currency, admitted only with eight contracts locked and a registered live source; strip gross weight 0.25/1.9, cost and rolls as E12 | qualifying markets form the A3 breadth item / item dropped |
| D2 | Non-signal trading (charter) | non-signal share >= 20% in both eras | none | A3 no-trade buffer item / dropped |
| D3 | Book risk understated in named states? (charter) | forward 12-month vol >= 2 points higher, 90% bootstrap bound > 0 | state months end at 2009-12 (the forward window then ends at 2010-12) | A3 faster scaler item / dropped |
| D4 | Trend early/late in equity falls; Carry in funding breaks (charter) | as registered; cells < 6 months reported only | its stress-window part and Carry's falsifier use one shared bad-state set: config.py STRESS_WINDOWS ending by 2010-12 plus the worst fifth of eq_us_spx months 1975-2010 (SPEC_Carry s10); one script prints one crisis table for all pods | spec lines / none |
| D5 | Does the Economic trend edge fade with delay? (charter) | Sharpe at 3 months' delay < half the no-delay Sharpe | kept as written; the 9-of-12 overlap is printed with it (charter JP8); it only selects wording | claim "slow reaction" / "lasting macro state" |
| D6 | Weak trend year = few markets moved? (charter) | era slopes differ by < 2 Newey-West s.e. | none | breakdown check line / dropped |
| X2 | Value paid by prices coming back or by income? (1.3b) | price part <= 0 on a leg's averaged position | point estimate stays the gate; a 90% bootstrap interval of the price part is reported (1.3b JP5) | "paid by income" entry (design return not cited for the thesis) / none |
| M1 | Markets to remove for P4 (1.3c) | two-market Sharpe lower than S&P-only by >= 0.05 in either era | gate kept: it only defines a reported line (1.3c JP8) | P4 uses S&P and US 10-year / S&P alone |
| S1 | Shape report (charter JP2; new, reported only) | none | five-state equity table per pod (D4's cells); Trend against the Fung-Hsieh trend factors 1994-2010 only if that factor file is obtained and locked first | report only |
| R1 | Local bends on the dollar strip larger than cost a day later? (1.3a) | at least half of triple-months qualify | month-ends end at 2010-11 (the next trading day stays in 2010); a measure with weight on a contract that fails the 15-of-20-day stale screen is excluded from numerator and denominator; a Datastream month-end value on a non-trading day is replaced by the last trading day's settlement, else left out of the normal; no outlier screen, no December check (the expiry-month grouping of the normal is the December guard, QP07-C13-5) | Strip reversion enters B2 / dropped unbuilt and logged |
| F0 | Rule-layer floor (power s3.6, s4 item 8; new) | per rule: at least 48 held months (months the averaged rule holds a non-zero position) and at least 3 episodes (a new episode starts at a held month whose previous held month is 12 or more months earlier) | applies to every card rule, on top of the card's own gates | judged in B2 / "not judgeable": analyst watch condition, not Shelved |
| C1-D1 | Enough episodes? (card 1) | fewer than 6 episodes (condition months, any version) | kept with F0 (both must hold) | rule stays / analyst watch condition |
| C1-D2 | Already held? (card 1) | > 80% of held months same sign as the registered systematic book | reference fixed below | leg stays / leg dropped |
| C2-D1 | Room to ease (card 2) | as registered (pooled, Japan may trigger) | none | floor version added to card 1 R1, R2 (+16, +32 with entry) and a stop line in card 2 / no change |
| C2-D2 | Enough cases, overlap with card 1 R4 (card 2) | version left out if < 24 on-months or < 3 episodes, or > 2/3 inside R4's 4.5 state | kept (a per-version prune) with F0 per rule | version kept / left out |
| C3-D1 | Duplicate check (card 3) | >= 0.80 dropped, 0.50-0.80 flagged | "Core book" read as the registered systematic book (below), because the question is content, not trading status (Core book v1 exists by then but holds Core parts only) | rule kept / dropped before B2 |
| C3-D2 | Quiet months for R1's gate (card 3) | < 60 gate-off months | none | gate kept / gate dropped (R1 4 versions) |
| C4-D1 | Market up, volatility up (card 4) | median ratio >= 1.25, whole window and each half | last state month 2010-06 (the 6-month outcome then ends by 2010-12) | half-size sizing version (+14) / analyst question only |
| C4-D2 | R5 overlap with card 3 R2 and Trend (card 4) | either share >= 0.80 in both versions | none | R5 not registered (note to card 3 R2) / R5 stays |
| C5-D1 | R1 a Trend duplicate? (card 5) | >= 75% of held months with the 12-month Trend versions long | none | R1 not registered / stays |
| C5-D2 | Slow class breaks further than grains? (card 5) | slow class >= 15 points above grains, >= 10 breaks each, breaks to 2008-12 | none; needs a locked LSEG curve history (blocked, 7.11) | R1 built / dropped unbuilt |

"Already held" thresholds: each card keeps its own number (80%, two thirds, 0.80 / 0.50, 0.80, 75%). Reason: each was
written in its note before any data, for that card's question; no source supports one number over another, and
replacing a written gate after the fact is itself an unsupported choice (CHECK_3.2_C s4 item 5). What is unified is the
reference and the counting: the registered systematic book = the four existing pods in their final Batch A form at the
CANDIDATE shares, all parts (Core and Incubator), sign of its net position per market (book.run "pos"); counted over the
months the leg or rule holds a position (any version, tails included). The question is whether the idea is already in
the shop's systematic research book; Core or Incubator is a trading status, not a content question.

Order of running (each step only after the one before):
1. X1 (signals only), before the A1 design run.
2. After A2: D1 (its candidate half only where a locked history exists), D2, D3, D4, D5, D6, X2, M1, S1.
3. After Core book v1 (7.6 step 6), before B2 is run: R1 (needs daily dollar contracts 1-8 locked), C1-D1, C1-D2, C2-D1,
   C2-D2, C3-D1, C3-D2, C4-D1, C4-D2, C5-D1, C5-D2, F0.
Every diagnostic reads positions, signals or its registered outcome only; none reads a sealed day after its fix.

### 7.6 Batches and contents

Step 1. Preconditions: the 7.4 entries and code (fix version, then feature version); step 3.5 checker test on record
(WORKFLOW 3.5); X1 run.

Step 2. Batch A1, data swap (report, no adoption test; WORKFLOW 4.1 "differences explained" governs over s6 "Test = does not hurt", because a data swap kept or dropped by its effect on returns would pick data by results). CANDIDATE on the A1 data
against CANDIDATE on free data, one block at a time (charter s4). Rule for each Bloomberg series (LOCK_v2,
lock id d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9): it may only extend a market's free history
backwards, never replace an overlapping free month (live runs on the free source, rule 7); it must be the same
instrument (same index family or contract root) with status ok in LOCK_v2 (not a copy, not cut); and its monthly
returns must correlate at least 0.95 with the free series over the overlap months up to 2010-12 (just below the lowest
agreement our own bond returns showed against CRSP, 0.965, gm/CHANGES.md gm-2.0). A series failing a condition is not
used and is listed. The A1 panel (its id recorded) is the panel of every later run, B2 included (CHECK_3.2_C s4 item
1); cm_aqr_ew is not a stand-in for card 1 R4-B's basket. A metadata job at each lock (free inputs, LOCK_v2, any
LSEG lock) lists the first date of every series a spec reads (GS2, TWEXMMTH, ^GSPC monthly and daily, IR3TIB01, the
ALFRED first vintages of CPILFESL, M2SL, PCEPILFE, UNRATE, every LSEG series and contract depth); each rule and market
starts at the first month every input exists (specs s7), never at a date chosen from returns (CHECK_3.2_C s4 item 14).

Step 3. Batch A2, grids (hygiene, 7.7 H1-H4). Challenger = CANDIDATE with Trend 16 versions, Economic trend 2, Carry 2,
Value 2 (version counts: SPEC_Trend s6, SPEC_Economic_trend s6, SPEC_Carry s6, SPEC_Value s6; Carry's two versions
reproduce today's half-and-half exactly, so A2 tests averaging, not a new Carry rule). Incumbent = CANDIDATE gm-2.0.3,
k = 1, A1 data. Value version 2's bond leg is already seen (batch-1 V1, protocol_batch1.md; SPEC_Value s12): it is
counted as a seen leg (7.8). Reported with A2: Sharpe by version, by tranche (weekly check), by class and era; Trend's
split into class-average and relative parts (register B12, T12); Trend's carry and price parts; Value next to Trend.
If A2 fails, the incumbent stays without averaging; no cell of a grid is picked.

Step 4. The diagnostic pass of 7.5 order item 2 on the A2-final book.

Step 5. Batch A3, items opened by diagnostics only (charter s5; register B9): breadth (D1, alternative commodities and
T10 strip markets that qualify), no-trade buffer (D2), faster book scaler (D3). Each is tested alone against the A2-final
book by 7.7 H1-H4 with its own target decisive (H4). An item whose preconditions (locked history with the 2011+ seal; a
registered live source for T09/T10 markets) are not met when A3 starts is not run; it may be registered with B1 or B2
before that batch starts, else it waits for the live path (WORKFLOW s6).

Step 6. Core book v1. For each Core part of an existing pod (7.2: Trend; Carry currencies v2 + energy; Value equities),
on the final Batch A design run (k = 1, 1975-01 to 2010-12):
   S1 placebo passes (7.7 T3); S2 its net mean return at twice the costs is above 0; S3 tail test 5 on the Core book with
   and without the part (both rescaled as 7.7 T4); S4 an independent rebuild from the spec alone matches within 15%
   (WORKFLOW 4.5: design net Sharpe and annualised mean each within 15% relative).
   Departure from WORKFLOW s5 ("Decisive, all four"): test 1 is not decisive for these parts. Reported, not decisive: leave-one-out alpha of the part on the other Core parts with its bootstrap p. Reason: these
   parts were adopted after seeing the same design months, so a p-value cannot be read as evidence; the tests that catch
   a broken part or a standing exposure (costs, placebo, tail) stay decisive. Consequence: no Core part of the existing book has a decisive "adds to the book" test on history; S1-S3 pass a working timing part almost always (power s3.2: placebo 0.86-1.00, tail 0.73-0.84), so the holdout is the existing book's only independent test.
   A part that passes S1-S4, with a free live source for every input, is Core. Core book v1 = the Core parts at equal
   risk as defined in 7.4 E9, 10% target, the engine's caps. Every other part of an existing pod (Economic trend; Carry currencies
   v1 and bonds; Value bonds and currencies) and any Core part that fails S1-S4 takes the Incubator rule (7.7) against
   Core book v1: pass = Incubator (shadow), fail = Shelved. If no Core part passes, Core book v1 is empty: B tests read
   alpha against a zero book (the pod's own mean), and there is no holdout run (BASE continues, labelled "no Core book").

Step 7. The pre-B diagnostics of 7.5 order item 3.

Step 8. Batch B1 = Curve carry (2 versions, register T08). It runs only once the LSEG contract history (with delivery
month per observation, last trading and first notice days) is locked with the 2011+ seal. If that lock does not exist
when step 7 ends, Curve carry moves to B2 (charter s3) and B1 is empty; the empty slot is not reused. Exchange calendars
(cattle on CME, Brent on ICE Futures Europe; CHECK_3.2_B s4) are not assumed: a market holds nothing in a month in
which the last trading day or first notice day of either leg, as the LSEG reader reports it, falls inside the holding
month; Brent's far leg is the same rule.

Step 9. Batch B2 = Strip reversion (2 versions), only if R1 passes and daily settlements of dollar contracts 1-8 are
locked (else dropped unbuilt, logged); Curve carry if moved; and every card rule that survives its gates:

| Card | Rules (versions; with entry or sizing versions) | Gates |
|---|---|---|
| 1 | R1 8 (16), R2 8 (16), R3 4 (8), R4 4 (8), R5 4 (8): 28 (56); +16 (+32) floor versions on R1, R2 if C2-D1 passes | C1-D1, C1-D2, F0 |
| 2 | R1 4, R2 4: 8 | C2-D2, F0 |
| 3 | R1 8 (16), R2 2 (4), R3 4 (8), R4 2 (4): 16 (32); R1 drops to 4 (8) if C3-D2 fails | C3-D1, C3-D2, F0; R4 needs the LSEG forward EPS locked and registered (blocked) |
| 4 | R1 6, R2 4, R3 2, R4 2, R5 2: 16; +14 sizing versions on R1-R4 if C4-D1 passes | C4-D1, C4-D2, F0 |
| 5 | R1 8 (16) | C5-D1, C5-D2, F0; needs the LSEG copper and WTI c1 history locked (blocked) |

   Totals as registered: systematic 26 versions (Trend 16, Economic trend 2, Carry 2, Value 2, Curve carry 2, Strip
   reversion 2); card rules 76, or 128 with entry and sizing versions (register G). Held back and not registered: card 1
   R6, card 5 R2. Not registered: the versions the card checks suggested and the cards did not write (card 1 no-tail;
   card 2 R2 6-month window and 5x; card 2 R1 long side; card 5 per-class lag): the source of a version is the card text,
   and the one quote for a no-tail exit is about a stock, not a macro position (MT151-C07-2). Card 5 R1's markets:
   copper, plus WTI in the crude version (the panel holds no cocoa and no other base metal while E1 keeps alternative
   commodities off).
   Budget rule (register E, H5): WORKFLOW's "at most 4" counts new systematic pods only. Card rule layers do not count:
   they can reach Incubator only (WORKFLOW s6), and the Holm count excludes them (counting them would cut the systematic
   pods' power from 0.34 / 0.49 to 0.19 / 0.32 while false adoption stays about 0.03, power s3.3). At most two systematic
   pods exist (Curve carry, Strip reversion), so no batch can exceed 4. Ordering rule if more ever existed: evidence grade
   (strong, moderate, weak), then Core-eligible before not, then lower register id; Strip reversion goes behind every
   stronger candidate (1.3a s3.1).
   Each card rule is tested and labelled on its own (Incubator, Shelved or not judgeable); a card's shadow pod is the
   sum of its Incubator rules, netted with every other card's (register B19). Reason: rules have their own mechanisms
   and samples; judging a card as one sum would let one rule carry another. A netting report shows any standing net
   position left after netting (register C7; reported).

Step 10. Batch review (WORKFLOW 4.6) after B1 and after B2. A failed test is written "not shown", never "refuted", for
pods with these windows (power s4 item 10).

Step 11. Book (WORKFLOW 5.1): Core book v1 plus any B-batch pod that reached Core, all at equal risk. Then the freeze
(7.9).

### 7.7 Tests, thresholds, verdicts

Window. A pod's window = its months with a scaled test return (after the warm-up of its block and book scalers, about
48 months after its first position); the Core book is cut to the same months. Fewer than 120 such months =
"insufficient data", not tested (section 1 rule kept; SPEC_Curve_carry s7, SPEC_Strip_reversion s7). A rule layer's window is every month from the first month all its inputs exist (its spec s7) to 2010-12, off months entering with return 0. The expected window
length is recorded from lock metadata before any run.
Held size. A pod's test return is its block at the book's 10% target with the engine's caps (specs s5). A rule
layer's test return is its position return times 0.10 / 0.40, i.e. 10% volatility per unit of rule risk while on, no
rescaling (card specs s5). In every combined-book statistic a pod or rule enters at lambda = 0.5 of the book's
volatility (equal risk with one of four independent pods, as simulated, power s2), and the combined book is rescaled to
10% by its trailing 36-month realised volatility, lagged one month (the book scaler's convention).

Decisive tests for new pods and rule layers (WORKFLOW s5, made exact):

| # | Test | Statistic | Pass |
|---|---|---|---|
| T1 | Adds to the book | Intercept of the least-squares regression of the pod's monthly net return on the Core book's monthly net return over the window. One-sided p for H0 alpha <= 0 from the centred stationary bootstrap: whole months, mean block 6, 10,000 resamples, seed 20261101, the regression re-fitted in every resample; p = share of resamples with (alpha_b - alpha_hat) >= alpha_hat | Holm-adjusted p < 0.025 over the Core-eligible systematic pods of the batch (a pod qualified under 7.2 with a registered live source for every input when the batch starts). Pods that are not Core-eligible and rule layers: raw p reported, outside the count |
| T2 | Double costs | Alpha of T1 with every cost doubled (strip and curve legs as their specs) | alpha > 0 (point estimate) |
| T3 | Placebo | 1,000 placebos, seed 20261101. Monthly pods and state rules: the score array (before division by volatility) of all markets moved jointly in 12-month blocks in random order (blocks aligned to the window's first month, the last part-block kept), then re-sized with each month's own volatility, scalers and caps, same costs. Card 4 R1-R4: each window moved to a random start in the same calendar year (R1, R3) or month (R2, R4), same length in trading days, gates re-read at the new dates | share of placebos with net Sharpe >= the pod's < 0.05 |
| T4 | Tail | TESTING_PROTOCOL test 5 as registered: combined book (Core book + pod at lambda 0.5) against the Core book alone, both at 10% as above | max fall not worse by more than 2 points and worst month not worse by more than 1 point |

Rule layers must also meet F0 (7.5) to be judged at all.
Hygiene items (A2, A3): H1 one-sided 95% lower bound of dSR (paired stationary bootstrap of section 2, pooled design
window) > -0.10; H2 dSR at twice the costs, reported; H3 tail test 5 between the two books; H4 (A3 only) the item's own
target, point estimate: buffer = lower turnover and net Sharpe not lower (charter D2); faster scaler = realised
volatility nearer 10% and worst fall not deeper (charter D3); breadth = lower first-factor share of Trend's variance
(charter D1). Pass = H1, H3 and, in A3, H4. No Holm across hygiene items (a margin test, not an adoption claim; error at
the margin measured 0.06-0.09, power s3.7).
Verdicts (WORKFLOW s5, made exact):
- Core: passes T1-T4, Core-eligible (7.2 qualified, a registered live source for every input), and the independent
  rebuild matches within 15% (WORKFLOW 4.5). Eligibility is fixed when the batch starts; a live source registered later
  does not reopen a verdict.
- Incubator: not Core, and alpha of T1 above 0 at single costs (point estimate), T3 and T4 pass, and (rule layers) F0
  met. Reason: "positive after costs" read as adding something to the Core book, not as a positive mean (power s4 item
  9). Shadow only.
- Not judgeable (rule layers under F0): analyst watch condition.
- Shelved: the rest; logged, never re-run with tweaks.
Reported, not decisive: the two eras with per-era lower bounds; by asset class; share of versions positive; k = 0 and
the one-month delay; the weekly-implementation check; untouched markets; cost sensitivity; tuned-knob count (7.8);
fragility (largest loss of result when any one year, market or class is removed; flagged when one period gives more
than 40% of the profit); P4; the Sharpe difference of the Core book with the pod at lambda 0.5 (the 5.1 sizing view:
break-even IR about 0.24 at rho 0.3, power s3.2); skew, Lo-adjusted Sharpe; the specs' falsifier lines (specs s10);
the "loss not seen" flag (P3); share of k = 1 months flagged.
P3 scope paragraph (added to section 3): "Error rates here are computed from the months on the window. They do not
cover a pod or a challenger with steady gains and a loss rarer than the window (Stine 2009, slide 44): if the loss has
chance q a month, independently, n months show none with chance (1 - q)^n, and every test here then sees the same
returns as if the loss did not exist. Measured (power s3.4): such a pod with true mean zero is adopted 0.41 times as
often as a true-Sharpe-0.4 pod at n = 432 (bound 0.37). Each pod spec names the event in which its mechanism loses most
and the window months in which it occurred; a spec with none is flagged 'loss not seen'. The flag does not change the
verdict." Flags today: none (every spec names window months), except Curve carry, flagged if no market-month of its
spec s10 item 3 exists in the window.
P4 (reported): specific return of the book w = r - b x m, m = monthly excess return of the S&P 500 (and the US 10-year
if M1 says so), b by least squares with intercept over all months from 1975-01 to the month before, first value in month
37; annualised Sharpe of w beside r, from 1978-01, in every batch report, the holdout report and each quarterly review.
Expected pass rates (power s3.1-3.6; book Sharpe 1.23; rho = correlation with the book):

| Shape | Window | true IR 0 (alpha = 0) | IR 0.2 | IR 0.4 | Note |
|---|---|---|---|---|---|
| Systematic pod, rho 0.3 | 432 months | 0.037 | 0.176 | 0.560 | standalone Sharpe 0.4 at rho 0.3 is IR 0.03: passes 0.057 |
| Systematic pod, rho 0 | 432 months | 0.021 | 0.167 | 0.544 | IR = standalone Sharpe |
| Strip reversion, rho 0.3 | 250 months | 0.040 | 0.138 | 0.383 | |
| Curve carry, rho 0.3 | 260 months | 0.041 | 0.143 | 0.380 | 0.470 at IR 0.4 over 360 months |
| Rule layer on 25% of months, rho 0.3 | 432 months | 0.057 | 0.227 | 0.569 | under 48 held months: at most 0.18 even at on-month Sharpe 1.2 |
| Batch false adoption (B2 at the null, Holm over 2 or 7) | - | 0.030-0.033 | - | - | nominal 0.025; Strip reversion alone (m = 1): 0.040 |
| Incubator rule, rule layer with no skill | - | 0.04-0.06 each | - | - | about 0.2 that any of five passes |

These are the WF_025 readings of power s3, i.e. Core-level passes; an Incubator pass is more frequent (power s3.2
INCUB column 0.53-0.65 at alpha = 0 under the mean reading, about half that under the alpha reading registered here, a halving reasoned from the alpha estimate's symmetry at the null, not simulated: power s4 item 9).

### 7.8 Trial count and hindsight

1. Every run on design data is one row of gm/trials.csv (WORKFLOW 7.1), with its config hash, engine version, data lock
   id and parent: families "book" (a change that could alter the book: A2, A3, Core book v1), "pod" (one row per pod or
   card rule tested in B1/B2), "data" (A1), "diag" (diagnostics, S1, the specs' reported falsifier computations such as
   Strip reversion's non-tradeable variant), "fix" (registered fixes). Today: 39 "book" rows, 4 "fix" rows.
2. Holm counts only the registered Core-eligible challengers of the batch (7.7 T1); earlier logged variants do not
   enter Holm (1.3c JP9). They enter the selection-inflation figure: expected best Sharpe from luck alone over the
   "book" and "pod" rows logged, by the stats_audit method (32 variants gave about 0.23), printed beside every book result.
3. Already seen, counted as such: Value version 2's bond leg (seen inside batch-1 V1; one seen leg in Value's tally);
   batch-1 S1 (a US 3-month market, rejected) is already seen for any T10 strip market in Trend, Economic trend and Carry,
   and for Strip reversion's relation to Carry; the hybrid volatility estimator (chosen on the whole book; one knob in
   every new pod's tally); knobs taken from Macro Compass rules backtested through the holdout years (card 1 R3's
   10-month S&P average; card 2 R1's stock-bond correlation gate): one "seen in a related rule" knob each in the card's
   tally (CHECK_3.2_C s4 item 4).
4. Tuned-knob counts, reported on each result sheet (specs s12): Trend 4, Economic trend 3, Carry 3, Value 3 + 1 seen
   leg; book level 3 (pod share vector, no risk scaler, no scenario limit) for every existing pod; Curve carry 1, Strip
   reversion 1; card 1: 1 seen in a related rule + 1 chosen with post-2010 sight (the R4 gate); card 2: 1 seen in a
   related rule; every card rule is hindsight-flagged in any case.
5. QP08 (2015) dates nothing for rule 5 and its sample runs 52 months into the sealed years: its results are not cited
   as evidence for any pod (register T12, 1.3b JP1). No design change.
6. Deflated Sharpe: dropped (7.1). Reason: 1.000 at every count (stats_audit s2).

### 7.9 Freeze and holdout

1. Freeze (WORKFLOW 5.2), after the B2 review: one record in gm/CHANGES.md and this file holding the frozen Core book's
   config id (gm/config.py cfg_hash), the engine version and git commit, the free-data inputs zip hash, the A1 panel id,
   the Bloomberg lock id (LOCK_v2 d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9, or a later
   registered lock), and the LSEG lock id if LSEG is registered. Nothing that enters the holdout run may change after it.
2. Holdout run: once, on the PC (WORKFLOW 5.3), months 2011-01 to the last complete month in the locked data at the
   freeze (189 months to 2026-09 were assumed in power s3.8), the frozen Core book at k = 1.
3. Criteria (registered 2026-11-01, unchanged; definitions fixed now): net Sharpe >= 0.3 (annualised from monthly net
   returns); worst fall > -25% (largest peak-to-trough fall of the compounded net return index); correlation with the
   S&P <= 0.3 (Pearson, monthly net book return against the eq_us_spx monthly excess return); 2022 positive (compounded
   net return 2022-01 to 2022-12 above 0; register B20, charter JP6). Pass = all four.
4. Which pods get a verdict: the Core book, and each Core part or Core pod (all 7.2-qualified by construction). Pod
   verdict: pass if the pod's net Sharpe at its held size over the holdout is above 0 (no source sets a pod bar; the four criteria are registered for the book; above 0 is the weakest reading of pass, since a part's Sharpe over 189 months has a standard error of about 0.25). Every other registered pod, part
   and card rule: holdout returns reported, descriptive only.
5. Consequences (WORKFLOW s6, restated exactly): "Pass: the Core book becomes the paper book of record. Fail: it still
   runs on paper, labelled as failed, with its expected Sharpe marked down, and no real-money step before the live
   checkpoints. No redesign from holdout data either way." "After the holdout every new pod enters as Incubator and is
   promoted only on its live record."
   Defined now: "expected Sharpe" = the Sharpe the live bands (W5) are centred on. Pass: design net Sharpe (k = 1) minus
   the selection inflation of 7.8 item 2. Fail: the lower of that figure and the holdout net Sharpe, floored at 0 (a mark-down never raises it). A pod that fails its pod verdict
   keeps running with the same label and mark-down; no pod is removed or reweighted on holdout data.
6. Reported with the verdict: P4 (market-removed Sharpe), each criterion's value, the holdout power below, Economic
   trend's delay readings of D5 on the holdout (descriptive; CHECK_3.2_A s4 item 10), and the cards' statement that
   policy starved macro playbooks for much of the window (register C19): context, never an excuse.
7. Power of the criteria (power s3.8, synthetic books, 189 months): all of Sharpe, worst fall and 2022 pass 0.05 / 0.31
   / 0.58 / 0.76 at true book Sharpe 0 / 0.4 / 0.8 / 1.2; the correlation criterion passes 1.00 at true correlation 0 and
   0.92 at 0.2. The worst-fall criterion binds at every Sharpe. The holdout screens out a broken book; it does not prove
   skill (section 6).

### 7.10 Live

1. Weekly cycle as WORKFLOW s6 (W1-W6). Sources: a registered live source = a source with a reader into the engine,
   a data check and a lock, refreshed in W1, whose licence allows its use for live decisions. Free public data qualify.
2. GB and euro-area 3-month rates: the OECD series end 2026-01 and are carried forward at most 12 months
   (panel.py:368-370). Before 2027-01 a data entry in gm/CHANGES.md must register a free replacement for each, chosen
   only by availability and by definition (a 3-month interbank or bill rate of that currency), checked against the OECD
   series on overlap months up to 2010-12 only (no 2011+ statistic before the holdout): mean absolute difference at most
   0.25 percentage point, one usual policy step; a candidate with no overlap before 2011 is accepted on definition and
   listed. Never chosen by returns; used only for months after the OECD series ends. Without it,
   from early 2027 fx_gbp, fx_eur, bd_gb_10y, st_gb_5y, bd_de_10y and st_de_2y have no excess return and leave live
   positions, eq_gb_ftse and eq_eu_stoxx50 fall back to the US rate, and the W5 data-health flag is on (every pod,
   CHECK_3.2_A s4 item 3).
3. LSEG as a registered source requires, in order: a reader into the engine with an as-of function; a data check (start
   dates, gaps, copies) and contract identity per observation (delivery month; last trading and first notice days;
   whether serial months are held); a lock with file hashes and the 2011+ seal, like LOCK_v2; a weekly refresh job on the
   user's PC; and a written statement in the repo that its licence allows live use (the user's statement of 2026-11-20
   covers unpublished research use; live and trading use is not yet stated). Registered as a data entry in gm/CHANGES.md.
   It unblocks: Curve carry and Strip reversion histories, T10 strip markets, T09 candidates, card 3 R4, card 5 R1 and
   C5-D2, card 3 question 2, card 5 scoring; and, as a live source, Core eligibility of Strip reversion (only if done
   before B2 starts).
4. Incubator promotion (WORKFLOW Q: "promotions only at registered checkpoints with stated sample sizes"): checkpoints at
   120 and 180 live months after a pod's first ledger week, then every 60 months. Promotion to the traded book needs: at
   least 120 live months (7.7 window minimum; rule layers also 48 live held months and 3 live episodes); a registered live source for every
   input; T1-T4 on live months only (T1 against the live Core book, Holm at 2.5% over the pods at that checkpoint);
   the independent rebuild. Rule 5 does not bind live months. Shelved at the 120-month checkpoint if the live alpha point
   estimate is at or below 0. Power stated with it: at true IR 0.4 the alpha test passes about 0.24 at 120 months and
   about 0.34 at 180 months (normal approximation, t = 0.4 x root(years)); at true IR 0.4 the 120-month shelving rule removes
   the pod with chance about 0.10, at IR 0 about 0.5.
5. Core pods live: no automatic switch. Each spec's section 11 condition with a series and a threshold is a W5 review
   flag: Curve carry, more than half its markets in backwardation for 12 consecutive month-ends; Strip reversion, flat at
   9 of the last 12 month-end decisions, policy rate below 0.25%, a held gap above the measure's design-window maximum;
   card 1, FEDFUNDS below 0.5 while WALCL is higher than a year earlier; card 2, WALCL higher than 12 months earlier (and
   a short rate below 1.0 if C2-D1 passes); card 3, FEDFUNDS 12-month range below 0.50; Trend's breakdown line if D6
   opens it; Carry's funding break if D4 opens it. Performance band for every pod: live rolling 36-month mean net return
   below the 10th percentile of the design-era rolling 36-month means (SPEC_Curve_carry s11 item 2, applied to all).
   Every other section 11 condition is review text for the quarterly review (Q). A flag leads to a review; any change is
   a new registered version.
6. Forecast ledger and analyst layers: descriptive, never a source of weights (WORKFLOW 2.3, rule 8). Analysts (W3) are
   blind to each other, model id logged; a model change starts a new record. Checkpoints at 200 resolved probability
   forecasts per analyst record, then every 200: mean Brier score against the base rate and against trend continuation,
   one-sided paired stationary bootstrap by week (mean block 13 weeks, because 13-week horizons overlap; 10,000
   resamples, seed 20261101); label "skill shown" if Holm-adjusted p < 0.05 over the analysts at that checkpoint against
   both baselines, else "not shown" (the specs' "no better than the base rate at the registered checkpoint"). No analyst
   layer touches the trade list under this registration: no spec defines how a probability becomes a position, so any use
   needs a new registered version after a "skill shown" label and before step 5.4.

### 7.11 Not registered, blocked, and what would change this section

Blocked (registered conditionally; each runs only when its condition is met, never by redesign):
- LSEG not a registered source: Curve carry (B1/B2), Strip reversion's live source, T10 strips, T09 candidates, card 3
  R4, card 5 R1 and C5-D2, card 3 R1's history before FRED starts (R1 runs on FRED alone, each currency from its own
  start). Unblocked by 7.10 item 3.
- Daily settlements of dollar contracts 3, 5, 6, 7 not pulled, and monthly start dates of contracts 5-8 unknown: R1 and
  Strip reversion (register D8). Unblocked by one LSEG pull and the lock.
- PC jobs that import pandas blocked by Windows Application Control: A1 and every Bloomberg or LSEG job. Unblocked when
  the PC runs them (gm_repro_v2 re-queued and passing).
- Fung-Hsieh factor file not in hand: the S1 factor part.
- GB / euro-area 3-month rates after 2026-01: live only, deadline 2027-01 (7.10 item 2).
Not registered: card 1 R6 and card 5 R2 (held back; a supporting quote before B2 starts would allow registration with
B2, after that the live path only); whole-curve curvature 3-A and the engine's three built spreads (register T43: no
spec); cross-sectional momentum as a pod (T12); every dropped register row (T37-T106); the checker-suggested versions of
7.6 step 9; any mark (DEM) series.
Recorded corrections: agent C's notes (a) 6 and 10 are wrong for the code (no pre-1999 euro series; no World Bank spot);
the register's D11 note on card 1 R4-B carries the start dates of the free panel (CHECK_3.2_C s4 item 15).
What changes this section: only a new numbered sub-section, dated and committed before the run it affects (7 intro).

---

_Section 7 was drafted by an Opus 5.5 agent (effort high) and checked by a fresh Opus agent (APPROVED WITH CORRECTIONS, 32 corrections applied by script); full record in docs/research/registration/ (REGISTRATION_3.4.md with the item table and the gm/CHANGES.md entries, CHECK_3.4.md, SUMMARY_FOR_USER.md). Committed 2026-11-23 before any run._
