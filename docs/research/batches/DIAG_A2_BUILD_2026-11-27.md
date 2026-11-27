# Diagnostics after A2 build (2026-11-27): TESTING_PROTOCOL 7.6 step 4, the PC job

Registered step built here: 7.6 step 4, "The diagnostic pass of 7.5 order item 2 on the A2-final book". Entry in
gm/CHANGES.md: "Diagnostics after A2" (commit 3fdd3f9), written and committed BEFORE the code (3fd5d1b) and before any
run. The A2 verdict was FAIL (gm_a2_v1), so the A2-final book is A1_INCUMBENT gm-2.0.4-candidate-x1 (77374d7bef), old
path, no grid, on the A1 panel e7f98d44..., engine gm-2.2.1, k = 1. The A1 panel holds Bloomberg values and exists only
on the PC, so every diagnostic statistic comes from the PC job gm_diag_v1. Nothing after 2010-12 was read. No
diagnostic statistic was computed in the cloud, on the free or the A1 panel. gm/ is unchanged (engine_ref.json
unchanged).

## Diagnostics of 7.5 and where each belongs

| Id | Question | Gate (as registered) | Data | Where | Outcome triggers |
|---|---|---|---|---|---|
| X1 | Energy carry a calendar pattern? | calendar means >= 0.25 of signal variance | signals | cloud, DONE before A1 | E13 for natgas, gasoline (done) |
| D1 structural | How many independent bets in Trend? | none (reported) | Trend P&L per market, A1 panel | PC, THIS PASS | baseline for A3 breadth H4 |
| D1 candidates | Does a candidate bring a new driver? | both shares < 1/2, >= 120 months, 8 bp | locked candidate history + live source | BLOCKED | A3 breadth item |
| D2 | Non-signal trading | non-signal share >= 20% in both eras | positions, scalers (A1 panel) | PC, THIS PASS | A3 no-trade buffer item |
| D3 | Book risk understated in named states? | +2 points forward vol, one-sided 90% bound > 0; states to 2009-12 | book returns, US equity and 10-year | PC, THIS PASS | A3 faster book scaler item |
| D4 | Trend early / late in equity falls; Carry in funding breaks | young 5-15% < 0 and > 15% > 0; Carry loses 1998 and 2008; cells < 6 not used | S&P drawdown, family returns | PC, THIS PASS | SPEC_Trend s10 line; SPEC_Carry s11 stop state |
| S1 | Shape report | none (reported) | D4's five states, all pods; Fung-Hsieh factors | PC, THIS PASS (factor part BLOCKED) | report only |
| D5 | Economic trend edge fades with delay? | Sharpe(3 m) < 0.5 x Sharpe(0) | Economic trend alone, A1 panel | PC, THIS PASS | spec wording |
| D6 | Weak trend year = few markets moved? | era slopes differ < 2 NW s.e. | Trend P&L and market Sharpe by year | PC, THIS PASS | Trend breakdown check line |
| X2 | Value paid by prices coming back or by income? | price part <= 0 (90% interval reported) | Value legs, carry values | PC, THIS PASS | "paid by income" register entry |
| M1 | Markets to remove for P4 | two-market Sharpe lower by >= 0.05 in either era | book returns, S&P, US 10-year | PC, THIS PASS | P4 form |
| Falsifier lines (specs s10, A2 item 5) | Trend, Carry, Value, Economic trend design-window falsifiers | holds / does not hold (reported) | A2-final book | PC, THIS PASS | reported only |
| R1 | Local bends on the dollar strip larger than cost a day later? | half of triple-months; month-ends to 2010-11 | ED daily contracts 1-8 (LSEG lock v5) | LATER: after Core book v1, before B2 | Strip reversion enters B2 / dropped unbuilt |
| F0 | Rule-layer floor | >= 48 held months, >= 3 episodes | rule states | LATER (before B2) | judged / analyst watch |
| C1-D1, C1-D2 | Card 1 episodes; already held | < 6 episodes; > 80% same sign | rule states, registered systematic book | LATER (before B2) | rule / leg stays or goes |
| C2-D1, C2-D2 | Card 2 room to ease; cases, overlap | as registered | 3-month rates, rule states | LATER (before B2) | floor versions / version left out |
| C3-D1, C3-D2 | Card 3 duplicate check; quiet months | >= 0.80 dropped; < 60 gate-off months | positions, FEDFUNDS | LATER (before B2) | rule dropped / gate dropped |
| C4-D1, C4-D2 | Card 4 market up, vol up; R5 overlap | median ratio >= 1.25; share >= 0.80; last state month 2010-06 | VIX, daily S&P, rule states | LATER (before B2) | sizing version / R5 note |
| C5-D1, C5-D2 | Card 5 Trend duplicate; slow class breaks | >= 75%; +15 points, breaks to 2008-12 | Trend positions, LSEG curves | LATER (before B2) | R1 not registered / dropped unbuilt |

The registered sealed-month cuts are kept: charter D3 state months end at 2009-12 (in this pass); card 4 D1 last state
month 2010-06 and R1 month-ends to 2010-11 (later pass).

## What the job prints (tools/bbgq/jobs/gm_diag_v1.py on the PC)

1. Checks, PASS / FAIL, STOP before any Bloomberg value is read on a FAIL: gm .py files = engine_ref.json's code block;
   `PASS lib engine_ref.json` (sha256 cebd4932...); `PASS engine gm-2.2.1 and config hashes` (BASE f1d682c384,
   CANDIDATE 438a092b53, A1_INCUMBENT 77374d7bef, A2_CHALLENGER 1faa343535) (C2); six lib files = the sha256 in the job;
   `PASS lib gm\trials.csv book / pod rows | 40 rows | digest 676b7b0f...` (C7: only the book / pod rows are pinned;
   appended diag rows do not matter); `PASS A2 report gm_a2_v1.txt: ok` (A2 JOB DONE, the registered A1 PANEL ID,
   A2 VERDICT FAIL with the A2-final book, the as-run values); store lock id = LOCK_v2; free inputs = the reference.
2. Free arm vs engine_ref.json; the A1 panel rebuilt (about 4 minutes), extension-only, `PASS A1 PANEL ID e7f98d44...`,
   compared with `work\a1\a1_panel_e7f98d4439fc.pkl` (STOP on a difference); nothing is written (C6); EXTENDED lines.
3. `theme scores | ...` (market counts per theme).
4. `PASS A2-final book as run (A2 report): ...`: book net Sharpe 1975-2010 k1 / k0 / d1 = 1.439 / 1.481 / 1.064, pods
   alone trend 1.19 (432), econ 0.53 (432), carry 1.07 (432), value 0.15 (345), P4 1.39 / 1.34 (396); else STOP with
   nothing else printed.
5. The registered pass: `BLOCKED | ...` (2 lines); `D1 | ...` (markets, windows, first-factor share, class loadings,
   pod / mean market Sharpe ratio, candidate half not run); `D2 | ...` (rebuild check, non-signal and scores-held
   shares per era), `D2 GATE`, `COSTDRAG | market | bp/yr (months)` per market; `D3 | ...` (state window, both splits:
   months, state means, difference, one-sided 90% bound), `D3 GATE`; `D4 | ...` (Trend and Carry by state, S&P base;
   each stress window as month count and sign), two `D4 GATE` lines; `CRISIS | ...` (bad-state set, each pod and Carry
   leg in bad / other months); `S1 | ...` (five states x four pods x two bases); `D5 | ...` (delays 0 / 1 / 3 / 6 / 12 at
   k = 1 and on the k = 0 path, the JP8 caution), `D5 GATE`; `D6 | ...` (slope and NW s.e. per era), `D6 GATE`;
   `X2 | ...` per Value leg (covered share, income / price / total %/yr, price 90% interval, exactness), `X2 GATE`;
   `M1 | ...` (1978-2010, 1978-89, 1990-2010), `M1 GATE`; `FALSIFIER | ...` (20 lines); `DIAG SUMMARY | ...`.
6. `TRIAL ROW {...}` x 10 (family diag: D1, D2, D3, D4, S1, D5, D6, X2, M1, FALSIFIERS), then `DIAG JOB DONE`.
Printing: statistics over at least 60 months only; a state, window or group with fewer months shows its month count and
sign only. Expected run time about 8-10 minutes (A1 rebuild about 4 minutes; about 25 book runs).

## Cloud gates (free data, design months only; nothing computed on the A1 panel)

- k = 0 reproduction 24 of 24, difference 0 (tools/bbgq/results/engine_repro_cloud_2026-11-27e_gm-2.2.1.txt).
- Truncation PASS at all 8 cut dates, 21 k = 0 and 37 feature stages (results/engine_trunc_cloud_2026-11-27e_gm-2.2.1.txt).
- tests/run_tests.py ALL TESTS PASSED (results/run_tests_gm_2026-11-27e_gm-2.2.1.txt), incl. tests/diag_a2_smoke.py
  (48 checks: each diagnostic against a direct computation, gates, seal, printing whitelist, facts parser, as-run, the
  C7 digest, the job's STOP paths) and tests/a2_batch_smoke.py (44 checks; gm_a2_v1 tested on the frozen 1.1.0 copy).
- Identity plumbing on the free panel (results/diag_plumbing_cloud_2026-11-27.txt): D2 rebuild = book.run positions
  (difference 0), income + price = total (6.9e-18), theme parts = held Economic trend position (2.2e-16), theme scores
  reproduce E (0), 62 Trend book markets / 61 without cm_aqr_ew. No statistic printed.

## How the coordinator queues it

Prerequisite: the PC runner is up and imports pandas; work\bbg (LOCK_v2 store), work\free\gm_free_inputs.zip (unchanged)
and local\results\gm_a2_v1.txt (from the A2 run) in place.
1. `python3 tools/bbgq/build_engine.py` (done; engine_pkg/DEPLOY.txt lists every file).
2. Copy to `C:\Users\admin\Documents\WRDS results\local\` (same relative path) the files marked new or changed below.
   lib\gm\trials.csv must be the repo version (51 rows: the A1 rerun and A2 challenger rows appended after A2); the job
   checks only its book / pod rows.
3. Read every copied file back (stage it) and compare its sha256 with the table BEFORE queuing.
4. No k = 0 reproduction is needed first (gm/ unchanged; the job itself checks the gm code and the free arm against
   engine_ref.json). Queue `jobs\gm_diag_v1.py` -> `local\jobs\gm_diag_v1.py`; read `local\results\gm_diag_v1.txt`
   (errors `gm_diag_v1.err.txt`).
5. After the run: commit the report to tools/bbgq/results/gm_diag_v1.txt; append the 10 TRIAL ROWs to gm/trials.csv
   (with `when`); append the "outcomes" paragraph under the CHANGES entry (item 7: each gate and what it opens); then
   the A3 entries for any opened item (D2 buffer, D3 scaler) before A3, and the spec / register text lines D4, D5, D6
   and X2 name.

| File (PC destination under local\) | Status | sha256 |
|---|---|---|
| jobs\gm_diag_v1.py | new | 8d50d30e651bd702640ec3df90879ba6bf01641d016b9295afb7c5ce774c9c9a |
| lib\diag_a2.py (1.0.0) | new | b811df2b4a9ad009668856bb0a2fdd84cc03334aa5d4213e473e4165a99e9caa |
| lib\a2_batch.py (1.1.1) | changed | 35339f673f351f43315ad3c7010ba733b6fb8990a6a41feb1ef20de324de58c6 |
| lib\gm\trials.csv (51 rows; book / pod digest 676b7b0f..., N 40) | changed | b7f8a0a7d976af8a65ca715ae14a5d32fc169a9cf9c5220887d349463f985ac6 |
| lib\gm\CHANGES.md (documentation, not checked) | changed | 94c3fd02e8512ab7a8fcab25d35d4d86d8c3ac9344863475fd0025c45c3b1852 |
| lib\engine_ref.json (gm-2.2.1 reference) | unchanged | cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39 |
| lib\a1_panel.py (1.1.0) | unchanged | eb9ef3f7fbd12760e174f9ef1df8573890bed6ca8d36f7d4e5c63eadd822ebb5 |
| lib\gm_engine.py (1.3.0) | unchanged | ac43a33cd8943719ba0efb9bb246473c7bbf59018a6d3b7398f64520eeebd721 |
| lib\bbg_panel.py | unchanged | e0b67a42793e67c129ec8a6c3ed2082390933ea9317898b59b8854387ecf1dcd |
| lib\bbgdata.py (= LOCK_v2 code hash) | unchanged | 0b26bb21b50671dca7c2153d3d66a2a09f7f33eeaa7c96ca536b69bbca8e6351 |
| lib\gm\book.py, config.py and every other gm .py | unchanged | engine_ref.json code.gm_files_sha256 (book 4c57d7fa..., config 7be14369...) |

Note: after lib\a2_batch.py is replaced by 1.1.1, gm_a2_v1 would stop at its hash check (it pins 1.1.0, the record of
the A2 run). That is intended; A2 is not rerun.

## A2 check items applied (CHECK_A2 "can wait")

C1 stale text (README A2 lines, run_tests labels, build_engine docstring); C4 a2_batch-1.1.1 (SPLIT check on
max(maxdiff_parts, maxdiff_held); A2 ran 1.1.0, sha256 87b24d8f..., frozen as tests/data/a2_batch_1.1.0.py); C6 the
A1 panel is compared before use and never written by this job; C2 and C7 pins in the new job (above). C3 and C5 were
handled in the A2 RUN paragraph.

## Not built / blocked

- D1 candidate half: T09 has no registered data entry naming a candidate series and no registered live source; T10
  admission needs a registered live source (LSEG LIVE_START not set) and eight locked contracts per currency (ED is the
  dollar, which T10 excludes; FEI is the only other). So no A3 breadth item is opened by this pass; 7.6 step 5 applies.
  Unblocked by: a data entry naming T09 candidates with a live source, or LSEG LIVE_START (lseg_weekly v2) for T10 plus
  the E12 strip market code.
- S1 Fung-Hsieh part: factor file not obtained and locked.
- No new LSEG pull is needed for this pass. The later R1 diagnostic reads the ED daily strips already in LSEG lock v5
  (all eight quarterly contracts on 5,475 of 5,480 days 1990-2010, LSEG data entry item 3).
