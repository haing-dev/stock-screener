# Step 3.3: power check (WORKFLOW v2.1), brief of 2026-11-23

You are the quant and risk officer. WORKFLOW 3.3: "Power check: simulated pods with known true Sharpe (0, 0.2, 0.4) run
through the test sheet -> pass rates; decisive statistic and thresholds fixed." Step 3.4 then registers the batches,
tests and thresholds. Your job: build the simulation as a script, run it on SYNTHETIC data only, and write the
pass-rate tables and a proposal of the decisive statistic and thresholds that 3.4 can register.

Work dir: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/power_3.3 (write only here: code in work/, results in this folder). Repo
/home/claude/stock-screener is read-only; import from it freely (gm/stats.py paired_sr_test, holm, nw_alpha_t,
bootstrap; gm/audit.py holdout_power; gm/protocol.py compare/decide) so the simulated tests ARE the registered code
where it exists. No market data at all: every return series is simulated. The only real-data facts you may use are
the design-era book facts already on record (BOOK_FACTS_design_era.md: volatility, autocorrelation, skew of the book,
correlations, 1975-2010 only). Never anything from 2011+. No web, do not spawn agents.

## Inputs (read first)
- /home/claude/stock-screener/docs/research/WORKFLOW.md sections 5-6 (test sheet, verdict, budget, holdout).
- /home/claude/stock-screener/docs/research/global_macro/TESTING_PROTOCOL.md (registered tests 1-5, bootstrap, Holm, eras).
- /home/claude/stock-screener/docs/research/fable/THESIS_1.3_method.md (+ _check.md): protocol items P1-P4, the "loss
  not seen" row (zero-mean pod with a hidden loss adopted >= 0.37 x as often as a Sharpe-0.4 pod at 432 months),
  the five WORKFLOW vs TESTING_PROTOCOL conflicts, sizing arithmetic.
- /home/claude/stock-screener/docs/research/THESIS_REGISTER_1.5.md sections A, B, E, F (diagnostics, protocol items,
  budget, conflicts).
- /home/claude/stock-screener/docs/research/specs/ (all 11 specs, section 7 sample, section 6 grids, section 9 costs;
  checks/CHECK_3.2_*.md section 4): they fix each pod's sample length, on-month share, version count, costs.
- /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/thesis_1.3_method/pack/BOOK_FACTS_design_era.md.

## What to simulate
1. A "book" series (the Core book stand-in) with the design-era book's monthly volatility, autocorrelation and fat
   tails (state the generator: e.g. GARCH(1,1) or Student-t with the book's kurtosis; justify from BOOK_FACTS).
2. Pod series with true Sharpe 0, 0.2, 0.4 (annual, after costs), correlation with the book rho in {0, 0.3, 0.6}, and
   the pod shapes the specs need:
   a. full-sample systematic pod, 432 months (1975-2010);
   b. short-sample pods: ~250 months (Strip reversion, 1990-2010) and ~200-260 months (Curve carry; use its spec);
   c. intermittent rule layers: positions only in a share of months (use each card spec's expected on-month share or
      episode counts; at least 10%, 25%, 50%), with the rest flat;
   d. a zero-mean pod with a hidden loss rarer than the window (as 1.3c P3) to report its adoption rate.
3. Costs: a gross series and a cost drag per spec section 9 so "double costs" can be tested; placebo as the spec /
   WORKFLOW defines it (signal dates shuffled in blocks, same average exposure) - simulate it as a pod whose signal is
   a block-shuffled copy, so the placebo test's own power and false-alarm rate are measured.
4. Batches: B1 with 1 pod (Curve carry), B2 with up to 2 systematic pods + 5 rule layers; Holm inside the batch.

## Tests to run on every simulated pod (each variant where WORKFLOW and TESTING_PROTOCOL disagree)
- Test 1 adds to the book: (i) alpha on the book with whole-month stationary bootstrap p-value (1.3c P2), (ii) paired
  Sharpe difference of book vs book+pod at the held size (TESTING_PROTOCOL test 1); Holm at 2.5% (WORKFLOW) and at 5%
  (TESTING_PROTOCOL) per batch.
- Test 2 double costs, test 3 placebo, test 4 tail (TESTING_PROTOCOL test 5 as written), era test (reported in
  WORKFLOW, decisive in TESTING_PROTOCOL: run both readings).
- Batch A hygiene: "does not hurt" (non-inferiority, TESTING_PROTOCOL margin) vs superiority: pass rates for a change
  with true effect -0.1, 0, +0.1 Sharpe on the book.
- Incubator rule (WORKFLOW s5): positive after costs and passes placebo and tail.
- Holdout criteria (WORKFLOW s6): pass rates for a book with true Sharpe 0, 0.4, 0.8, 1.2 over the holdout length
  (use gm/audit.py holdout_power if it fits; 2011-01..2026-?: take the months stated in BOOK_FACTS / audit).

## Output: POWER_3.3.md (+ the script work/power_3_3.py, deterministic seeds, and the raw tables as CSV)
1. Summary in ten lines: what the sheet can and cannot detect; the proposal.
2. Generator and its calibration (with the BOOK_FACTS numbers used and why).
3. Pass-rate tables: for each pod shape x true Sharpe x rho: each test alone, the four decisive together, Incubator,
   each conflict variant; false-adoption rate per batch (true Sharpe 0) under each Holm level; hidden-loss row.
4. Proposal for 3.4: the decisive statistic for test 1, the threshold of each decisive test, the batch error level,
   whether the era test is decisive, the hygiene test form, and the minimum on-months / episodes below which a rule
   layer cannot be judged (with the pass rates that justify each). Every proposal states its effect on the pass
   chance. No decision is handed to the user; where two readings are close, say which and why.
5. What the simulation does not capture (fat-tail misspecification, regime shifts, overlap between pods) and how big
   a mistake that could be.
6. Runtime and how to re-run.
Reply with section 1 and the key table (four decisive tests together, per shape and true Sharpe at rho 0.3).
