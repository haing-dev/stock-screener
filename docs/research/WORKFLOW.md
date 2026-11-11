# Macro pod shop: workflow v2.0 (final design, 2026-11-11)

Status: design only, nothing executed yet; execution starts when the user says go.
Replaces the routing and schedule in `docs/research/PLAYBOOK.md` and the selection procedure in
`docs/research/fable/foundation/VARIANTS.md` (its table of design choices becomes the version grid).
`docs/research/global_macro/TESTING_PROTOCOL.md` stays and gets a new section at step 3.4.
An independent Opus reader reviewed the draft; its findings are folded in (section 8).

## 1. What we are building
A small systematic-macro shop run as pods. A pod is one way of making money (one mechanism) with its own written
spec, backtest, live record and risk budget. The book is the pods combined at fixed risk shares. Signals are slow
(weeks to months); predictions and the trade list are produced every week. Paper record first.

Two kinds of pod:
- **Systematic pod**: fixed rules, backtested on history.
- **Discretionary pod**: one investor playbook, in two layers. The *rule layer* is the playbook's if-then rules,
  backtested like a systematic pod but flagged for hindsight. The *analyst layer* is an agent that reads the playbook
  card and a fixed weekly data snapshot and makes dated forecasts. It cannot be backtested (the model already knows
  history), so it is judged only on its live record.

## 2. Rules of the shop
1. The pod is the unit of work, testing and risk. Sources feed pods.
2. Inside a pod every registered version is run and averaged (speeds, volatility estimates, signal shapes; rebalance
   days as weekly tranches). The list of versions is fixed at registration; changing it later counts as a new trial.
3. Two questions, two tests. A new return source (a pod) must show it adds. A hygiene change (robustness, cost, risk,
   breadth) must show it does not hurt and improves its own target.
4. The testing budget is fixed in advance: Batch A, two batches of new pods, freeze, one holdout run. After that, new
   ideas are judged only on the live record.
5. Evidence ladder, weakest to strongest: design era (to 2010) -> untouched markets -> holdout 2011-26 -> live record.
   The holdout verdict counts only for pods whose thesis was documented before 2011: 205 of the 227 sources were
   recorded in 2024-26, and the models know market history to mid-2026.
6. Hindsight-flagged pods and analyst pods run in shadow: forecasts are logged and scored, and they never touch the
   trade list before a registered live checkpoint.
7. Bloomberg data are research history. They stay on the PC, jobs run there, and only summary statistics come back
   (no per-date series). Live runs on free data, or on data licensed for trading. A pod without a live source for
   every input cannot be Core.
8. Everything predicted is logged before the fact and scored after.
9. Fable judges small inputs, and every Fable output gets an independent Opus check. Opus builds, tests and audits; a
   fresh Opus agent rebuilds what matters. Sonnet extracts and operates. Scripts do everything that needs no model.
   No step grades itself.

## 3. Who does what
| Tier | Role in the shop | Steps |
|---|---|---|
| Fable 5.2, effort max | Strategist: charter, thesis notes, playbook cards, batch reviews, holdout verdict, monthly forecast, quarterly review | 1.2-1.4, 4.6, 5.3, M, Q |
| Opus 5.5, effort high | Quant and risk officer: data, engine, specs, tests, independent checks and rebuilds; weekly analysts | 0.1-0.5, 1.1, 1.5, 2.2-2.3, 3.1-3.4, 4.1-4.5, 5.1-5.4, W3 |
| Sonnet 5.5, effort high | Research assistant and operations: packs, forecast ledger, file moves, weekly report, alerts | 1.4 packs, 2.1, W1, W6, 7.3 |
| Scripts, GitHub Actions, PC runner | Everything mechanical: data checks, backtests, verdicts, scoring, ledgers | 0.3-0.4, 4.4, W1-W5, 7.1-7.2 |

The chat is orchestrated on Opus; Fable is called only for its own steps and reads kilobytes, never bulk text or code.

## 4. Steps
| # | Step | Agent | Gate / output |
|---|---|---|---|
| **0** | **Data lock (on the PC)** | | |
| 0.1 | Set up: local job runner (same pattern as the WRDS runner), Python check, export whitelist, inventory of the pulled files (cells hold values, not formulas) | Opus; Sonnet moves files | runner alive; inventory complete |
| 0.2 | One reader for files 1-7 -> clean tables (monthly 1969+, daily 1990+); each series tagged with its live source and delay | Opus | every ticker read or listed as failed |
| 0.3 | Data check: to 2010 in full; 2011+ structure only (dates, gaps), no price statistics | script; Opus triage | must-have series usable; differences from free data explained |
| 0.4 | Lock and seal: file hashes committed; 2011+ behind a one-time key; untouched markets named and sealed | script | lock id |
| 0.5 | Engine on the PC (monthly tests, weekly implementation); must reproduce the current book on free data first | Opus; fresh Opus re-check | match within tolerance |
| **1** | **Thesis library** | | |
| 1.1 | Fable audit: planted-error test on the small Eckhardt pack; independent re-derivation of the ten key statements of the Carver note | Opus plants and scores; Fable runs | at least 80% of planted errors caught and none carried into a conclusion; else tighten the brief and fact-check every Fable note |
| 1.2 | Systematic charter: one consolidation of the seven notes (what is established, the systematic pods, their version grids, the queued checks cut down to one diagnostic pass) | Fable, 1 run; then Opus checks it against claims and code and reads the remaining trend sources (Eckhardt, Fung and Hsieh) for contradictions | charter + check |
| 1.3 | Thesis notes for new systematic pods: rates and curve (QP06, QP07, QP12); cross-sectional value / momentum / carry (QP15, QP08); testing method (QP13) | Fable, narrow brief: source logic only, no code reading, one-page digest of earlier notes | 2-3 notes |
| 1.4 | Playbook cards: policy and liquidity (Druckenmiller, Bessent); regime and debt cycle (Bridgewater); macro relative value and risk (Graham, Elliott); flows and volatility (Karsan); commodity balances (Andurand). Card = causal model, indicators with exact series, if-then rules, dated forecasts, what would prove it wrong | Sonnet builds packs; Fable writes cards | 5 cards |
| 1.5 | Thesis register: every thesis -> pod, rule sketch, data (history, live source), evidence grade, documented before 2011 (with the source) or hindsight-flagged | Opus; script checks ids | one table |
| **2** | **Forecast ledger (cloud, free data, descriptive)** | | |
| 2.1 | Dated views pulled from the 188 maps by script, normalised to who / date / variable / direction / horizon | Sonnet; Opus recodes 20% blind | agreement reported |
| 2.2 | Scoring rules written before any outcome is looked at: what counts as resolvable, default horizons, baselines (base rate, trend continuation) | Opus | committed |
| 2.3 | Scorecard pooled by call type. Descriptive only, never used for weights. Forecasts still open are scored as they resolve. The same scorer later serves our pods and analysts | Opus builds; script runs | scorecard |
| **3** | **Specs and registration** | | |
| 3.1 | One-page pod spec: mechanism, markets, signal, sizing, version grid, data (history, live source and delay), costs, predictions, drop rule | Opus | spec |
| 3.2 | Spec check: faithful to the card and claims? can it fail? is the hindsight flag right? | fresh Opus agent; Fable only to settle a disagreement | approved spec |
| 3.3 | Power check: simulated pods with known true Sharpe (0, 0.2, 0.4) run through the test sheet -> pass rates; decisive statistic and thresholds fixed | script; Opus | pass-rate table |
| 3.4 | Registration: batches, pods, grids, tests, error budget, freeze rule, holdout consequences, live checkpoints written into TESTING_PROTOCOL.md and committed before any run | Opus | one-page summary to the user |
| **4** | **Design-era tests (PC, to 2010)** | | |
| 4.1 | Batch A1, data swap: the current design on Bloomberg data; differences explained | Opus | report |
| 4.2 | Batch A2: weekly tranches and version averaging against the incumbent net of its selection inflation (about 0.23 Sharpe): must not hurt. Plus the diagnostic pass | Opus | report |
| 4.3 | Batches B1 and B2: new pods, at most 4 each, on the test sheet (section 5) | Opus | result sheets |
| 4.4 | Verdict by rule: Core / Incubator / Shelved | script | verdict |
| 4.5 | Independent rebuild of each Core pod from its written spec alone; results must match | fresh Opus agent | match report |
| 4.6 | Batch review from the result tables only: what is refuted, what goes into the next registered batch. No re-runs with tweaks | Fable; Opus checks the numbers | review note |
| **5** | **Book, freeze, holdout** | | |
| 5.1 | Book: Core pods at equal risk, volatility target, caps. No switching between pods | Opus | book config |
| 5.2 | Freeze: config id + lock id (pass chances and consequences were registered at 3.4) | Opus | freeze record |
| 5.3 | One holdout run on the PC. Verdict for pods documented before 2011, the rest descriptive. No redesign | script; Fable writes the verdict; Opus checks the numbers | holdout report |
| 5.4 | Execution spec, before any real trade: instrument per market, rolls, minimum sizes for the account, weekly cost budget, risk limits | Opus | spec |
| **6** | **Live weekly cycle (paper, free data)** | | |
| W1 | Data refresh and checks | Actions / script; Sonnet triages alerts | snapshot |
| W2 | Core pods: signals -> positions -> trade list; each signal also stated as a probability from its design-era hit rate | script | trade list |
| W3 | Shadow: Incubator pods; analyst pods (each reads its card and the same snapshot, blind to the others; dated forecasts with probabilities at 4 and 13 weeks on a fixed asset list; model id logged, a model change starts a new record) | script; Opus analysts | forecasts |
| W4 | Ledger: predictions and positions appended before the week starts | script | append-only ledger |
| W5 | Scoring: resolved predictions, live against backtest bands, flags | script | scorecard |
| W6 | Weekly report, one page, fixed template | Sonnet | note in Obsidian |
| M | Monthly: reads the month's ledger and scorecards, adds its own dated forecasts (shadow-scored) | Fable | forecasts + one page |
| Q | Quarterly review; promotions only at registered checkpoints with stated sample sizes | Fable; Opus checks | review |
| **7** | **Always on** | | |
| 7.1 | Trial log counts every run on design data, diagnostics and grid changes included | script | trials.csv |
| 7.2 | Every Fable output stored with its exact input; ids and numbers checked | script; Opus | check log |
| 7.3 | Obsidian stays the single store: Method/WORKFLOW, Pods/, Tests/, Forecasts/, Weekly/ | Sonnet | vault |
| 7.4 | Usage: token estimate before each step, actual after | - | usage log |

Order: 0.1-0.5 first. In parallel in the cloud: 1.1, then 2.1-2.3 and 1.2. Then 3.3-3.4 and 4.1-4.2. Fable units
1.3-1.4 run one at a time on the user's word, then 1.5, 3.1-3.2, and 4.3-4.6 per batch, then 5.
The weekly cycle starts for the existing book as soon as 0.5 is done (W1, W2, W4, W5), and W3 as soon as the cards
exist, because live evidence only accrues with calendar time.

## 5. Test sheet and verdict (thresholds fixed at 3.3-3.4, before any run)
Design tests are monthly on 1975-2010; one weekly-implementation check runs on 1990-2010. Every input is used with
its live delay (free daily data: one day; official statistics: release date).

Decisive, all four:
1. Adds to the book: alpha against the Core book, corrected for the number of pods in the batch.
2. Survives double costs.
3. Beats its placebo: the same pod with its signal dates shuffled in blocks, keeping the same average long/short
   exposure.
4. Tail: worst fall and worst month of the book not materially worse (TESTING_PROTOCOL test 5).

Reported, not decisive: the two eras; by asset class; share of versions positive; one-period trading delay; untouched
markets; deflated Sharpe from the trial log; the weekly-implementation check.

Verdict:
- **Core**: passes the four decisive tests, thesis documented before 2011, a live source for every input, and the
  independent rebuild matches.
- **Incubator**: not Core, but positive after costs and passes placebo and tail. Includes hindsight-flagged pods and
  pods waiting for a live source. Shadow only.
- **Shelved**: the rest. Logged; not re-run with tweaks.

## 6. Testing budget, freeze, holdout
- Batch A: hygiene only (data swap, weekly tranches, averaging). Test = does not hurt.
- Batches B1 and B2: new systematic pods. Each batch may wrongly adopt a useless pod with at most 2.5% probability
  (Holm inside the batch). Rule layers of the discretionary playbooks run in B2 for Incubator status only.
- Freeze after the B2 review, then one holdout run. Criteria as registered: net Sharpe >= 0.3, worst fall > -25%,
  correlation with the S&P <= 0.3, 2022 positive.
- Pass: the Core book becomes the paper book of record. Fail: it still runs on paper, labelled as failed, with its
  expected Sharpe marked down, and no real-money step before the live checkpoints. No redesign from holdout data
  either way.
- After the holdout every new pod enters as Incubator and is promoted only on its live record.

## 7. What each pod has to hand over every week
Positions, and for each asset on the fixed list a direction with a probability at 4 and 13 weeks. Systematic pods
derive the probability from design-era hit rates by signal strength; analysts state it. All of it goes into the ledger
before the week starts.

## 8. What the independent review changed
1. Holdout: verdict limited to pods documented before 2011; consequences written before the run; no price statistics
   on 2011+ in the data check.
2. A fixed number of batches and an error budget for the whole programme, with a freeze point.
3. Four decisive tests instead of a chain of ten; a power check before registration; mechanical definitions of Core
   and Incubator; hindsight-flagged pods can never be Core.
4. Backtest and live use the same delays; design tests stay monthly with one weekly check; live source required.
5. Export whitelist and value check on the PC; Bloomberg for research only, live on free data.
6. Version grids fixed at registration; Batch A split into data swap, then averaging.
7. Forecast scoring is descriptive, not a source of weights.
8. Analysts run in shadow, with the model id logged.
9. Fable no longer checks work built from its own notes; the weekly report moves to Sonnet, Fable forecasts monthly.
10. Placebo keeps the pod's average exposure; untouched markets are named and sealed up front.

## 9. Needed from the user
- The folder with the pulled Bloomberg files (the expected folder holds only the blank templates).
- Whether Bloomberg can be refreshed regularly and used for live signals. Default if not: live runs on free data only.
- Before step 5.4 only: account size and broker.
