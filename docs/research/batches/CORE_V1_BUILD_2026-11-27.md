# Core book v1 build (2026-11-27): TESTING_PROTOCOL 7.6 steps 5 and 6, the PC job

**UPDATED for core_v1 1.1.0** after the independent check (CHECK_CORE, APPROVED WITH CORRECTIONS; corrections
registered in gm/CHANGES.md e18bc33 before the code 57cc241). M2 option A: S4 covers the full spec, so the rebuild gets
RAW inputs (docs/research/batches/S4_INTERFACE.md v2) and derives the carry measure, the value measure and the
volatility model itself; the job first checks the raw inputs reproduce the engine's measures exactly. N2 gap rule:
dated clarification in CHANGES and SPEC_Trend s3 (written with sight of the engine). C1, C2, C4 applied. M1 (rank
weights clipped) and the move to interface v2 are the rebuild agent's: rebuild_s4 1.0.0 (3febdce7...) reads the v1
keys and is NOT accepted. The hash table at the end is the one to use.

Registered steps built here:
- 7.6 step 5, A3: gm/CHANGES.md "A3: empty" (commit 7038311): the diagnostics opened no A3 item (D2, D3 closed; D1
  candidate half blocked); the D1 breadth item is not run (preconditions unmet); how it may return with B1 / B2 is
  quoted. No code, no run, no trial row.
- 7.6 step 6, Core book v1: gm/CHANGES.md "Core book v1" (commit 28f14a6), written and committed BEFORE the code and
  before any run, together with the S4 interface docs/research/batches/S4_INTERFACE.md.

The book is the A2-final book A1_INCUMBENT gm-2.0.4-candidate-x1 (77374d7bef), engine gm-2.2.1, on the A1 panel
e7f98d44..., k = 1, design months 1975-01..2010-12. The A1 panel holds Bloomberg values and exists only on the PC, so
every statistic of S1-S4, the Incubator rule and Core book v1 comes from the PC job gm_core_v1. Nothing after 2010-12
was read. No such statistic was computed in the cloud, on the free or the A1 panel. gm/ is unchanged (engine_ref.json
unchanged).

## What is tested

| Part | Mask (config.CORE_PARTS / SHADOW_PARTS) | Test | Outcome |
|---|---|---|---|
| trend | (trend, *, *) | S1 placebo, S2 2x-cost mean, S3 tail with / without, S4 rebuild, live source | Core, or the Incubator rule |
| carry | (carry, FX, 2), (carry, CM, 1), (carry, CM, 2) | same | Core, or the Incubator rule |
| value | (value, EQ, *) | same | Core, or the Incubator rule |
| econ | (econ, *, *) | Incubator rule (T1 alpha > 0, T3, T4) against Core book v1 | Incubator or Shelved |
| carry_shadow | (carry, FX, 1), (carry, FI, *) | Incubator rule | Incubator or Shelved |
| value_shadow | (value, FI, *), (value, FX, *) | Incubator rule | Incubator or Shelved |
| carry_fx_v2, carry_energy | the two Carry Core legs alone | S4 comparison reported only | none |

## What the job prints (tools/bbgq/jobs/gm_core_v1.py on the PC)

1. Checks, PASS / FAIL, STOP before any Bloomberg value is read on a FAIL: gm .py files = engine_ref.json's code block;
   `PASS lib engine_ref.json` (sha256 cebd4932...); `PASS engine gm-2.2.1 and config hashes` (BASE f1d682c384,
   CANDIDATE 438a092b53, A1_INCUMBENT 77374d7bef, A2_CHALLENGER 1faa343535); seven lib files = the sha256 in the job
   (core_v1, diag_a2, a2_batch, a1_panel, gm_engine, bbg_panel, bbgdata); `PASS lib rebuild_s4.py` (= REBUILD_SHA) and
   `PASS rebuild_s4.py imports none of gm, gm_engine, ...`; `PASS lib gm\trials.csv book / pod rows | 40 rows | digest
   676b7b0f...`; `PASS A2 report gm_a2_v1.txt: ok`; `PASS diagnostics report gm_diag_v1.txt: ok | A3 empty`; store lock
   id = LOCK_v2; free inputs = the reference.
2. Free arm vs engine_ref.json; the A1 panel rebuilt (about 4-6 minutes), extension-only, `PASS A1 PANEL ID
   e7f98d44...`, compared with `work\a1\a1_panel_e7f98d4439fc.pkl` (STOP on a difference); nothing written; EXTENDED
   lines.
3. `PASS raw inputs reproduce the engine's measure | carry currencies / carry energy (before E13) / value equities (E4)
   | markets | max abs diff | missing pattern` (else STOP; also STOP if A1 admitted a dividend-yield extension);
   `rebuild inputs | R (612, 65) | D (..., 61) | days ... | rate3m (612, 14) | fx_rate_country 13 | eia 4 | french_with
   (612, 7) | french_without (612, 7) | us_total | us_price | cost 65 | ...`; `PASS rebuild <VERSION> | ok | months in
   1975-01..2010-12: ...` (else STOP: no S4 line, no statistic).
4. `PASS A2-final book as run (A2 report): ...` (book k1 / k0 / d1 1.439 / 1.481 / 1.064, pods alone, P4), else STOP.
5. `PARTS | ...`; `PART | <part> | Sharpe ... | mean %/yr ...` for the 3 candidates, 3 shadow parts and 2 legs (k = 1,
   1975-2010 and eras); per candidate `S1 | ...` (window, part Sharpe, 1,000 placebos, share, PASS / FAIL), `S2 | ...`
   (2x-cost mean %/yr), `S3 | ...` (two margins in points, max drawdown levels), `S4 | ...` (engine and rebuild Sharpe and
   mean, relative differences, common months, correlation), `LIVE | ...` (markets held at 2010-12, missing free inputs),
   `LOO | ...` (alpha %/yr, beta, bootstrap p: reported only), `VERDICT | ...`; `S4 REPORTED | ...` for the two legs.
6. `CORE BOOK V1 | parts ... | config hash ...` (or `CORE BOOK V1 EMPTY | ...`); `BOOK | core_v1 | k1 / k0 / d1 | costs
   x1 / x2 | 1975-2010 / 1975-89 / 1990-2010 | months | Sharpe | mean | vol | max drawdown | skew | Lo Sharpe`;
   `FLAGGED | core_v1 | ...`; `P4 | core_v1 | S&P 500 alone (M1) | ...`; selection inflation (N 40 book / pod rows);
   tuned knobs.
7. `INCUBATOR | <part> | T1 alpha, beta, raw p | T2 alpha at 2x costs | T3 placebo share | T4 ... | INCUBATOR /
   SHELVED` for the 3 shadow parts and every candidate that is not Core; `CORE V1 VERDICT | Core: ... | not Core: ... |
   Incubator: ... | Shelved: ... | insufficient data: ...`.
8. `TRIAL ROW {...}` (family book, one row), then `CORE V1 JOB DONE`.
Printing: statistics over at least 60 months only (smaller groups: count and sign); worst-month levels never printed.
Expected run time: the A1 rebuild plus about 6,000 book runs for the placebos (6 parts x 1,000; about 0.3 s each in the
cloud, so roughly 30-90 minutes on the PC).

## Cloud gates (free data, design months only; nothing computed on the A1 panel)

core_v1 1.1.0 (2026-11-27): run_tests ALL TESTS PASSED (results/run_tests_gm_2026-11-27h_gm-2.2.1.txt; core_v1_smoke 75
checks: interface v2 keys, no engine-built measure in the inputs, copies, raw_check pass / fail cases, the check
formulas by hand, C4 no .pyc under lib\); free-panel identities PASS (results/core_plumbing_cloud_2026-11-27b.txt: the
raw inputs reproduce the engine's currency carry (13 markets), energy carry before E13 (4) and equity value with E4
(8) with max abs difference 0 and no missing-pattern difference; inputs rate3m (612, 14), eia 4 x (612, 2),
french_with / french_without (612, 7), us_total / us_price (612)). gm/ unchanged, so the k = 0 reproduction and
truncation results below stand. 1.0.0 gates as below.

- k = 0 reproduction 24 of 24, difference 0 (tools/bbgq/results/engine_repro_cloud_2026-11-27f_gm-2.2.1.txt).
- Truncation PASS at all 8 cut dates, 21 k = 0 and 37 feature stages, 0 failing end-to-end or alone
  (results/engine_trunc_cloud_2026-11-27f_gm-2.2.1.txt).
- tests/run_tests.py ALL TESTS PASSED (results/run_tests_gm_2026-11-27g_gm-2.2.1.txt), incl. tests/core_v1_smoke.py
  (70 checks: masks partition the pods; S1 identity map and placebo share; S2, S3 against direct computations; S4 pass /
  fail at 0, +10% and +20%, own months; interface keys, copies, validate refusals, forbidden-import scan; live check;
  zero-book alpha; leave-one-out = alpha_boot; both verdict branches (non-empty Core book with a failed candidate
  taking the Incubator rule, and the EMPTY branch with "T4 not applicable" and a trial row without Sharpe columns);
  seal; printing; diag facts; the job's STOP paths: REBUILD_SHA unset, a changed rebuild, a rebuild importing gm, no A2
  or diagnostics report, a changed core_v1.py, a non-LOCK_v2 store).
- Identity plumbing on the free panel (results/core_plumbing_cloud_2026-11-27.txt): Core + shadow masks partition each
  pod (difference 0); the identity date map reproduces all 6 parts alone (difference 0, no missing-pattern
  difference); interface inputs R (612, 65), D (12668, 61), days 10,349, C (612, 31), V (612, 28), vol (612, 65), cost
  65, em_borrow 7, classes 4; the stub output validates; live-source check runs (held at 2010-12: trend 61, carry 15,
  value 8 markets; missing free inputs none). No statistic printed.
- `python3 tools/bbgq/core_plumbing.py --rebuild` additionally runs the real rebuild on the free-panel inputs and prints
  only whether its output passes the interface checks: for the coordinator at queue step 1 (not run by the builder).

## How the coordinator queues it (in this order)

1. BLOCKED until the corrected S4 rebuild is accepted: rebuild_s4 1.0.0 (1204233, sha256 3febdce7...) reads interface
   v1 and has the M1 clip; the separate agent delivers a version on interface v2 (raw inputs; carry, value and
   volatility derived from the specs) with M1 fixed. Accept it (its own self-test; an
   independent read that it follows the specs and S4_INTERFACE.md, imports none of the forbidden modules, prints
   nothing; `python3 tools/bbgq/core_plumbing.py --rebuild` for the interface checks on free data). Then, in one commit
   BEFORE queuing: a dated line under the gm/CHANGES.md "Core book v1" entry giving rebuild_s4.py's version and sha256
   (item 4e), and REBUILD_SHA = that sha256 in tools/bbgq/jobs/gm_core_v1.py (the job STOPs while REBUILD_SHA is None).
2. `python3 tools/bbgq/build_engine.py` (copies rebuild_s4.py when present; engine_pkg/DEPLOY.txt lists every file).
3. Copy to `C:\Users\admin\Documents\WRDS results\local\` (same relative path) the files marked new or changed below,
   plus lib\rebuild_s4.py. lib\gm\trials.csv must be the repo version (61 rows; the job pins only its book / pod rows).
4. Read every copied file back (stage it) and compare its sha256 with the table (and rebuild_s4.py with REBUILD_SHA)
   BEFORE queuing.
5. Queue `jobs\gm_core_v1.py` -> `local\jobs\gm_core_v1.py`; read `local\results\gm_core_v1.txt` (errors
   `gm_core_v1.err.txt`). Needs `local\results\gm_a2_v1.txt` and `local\results\gm_diag_v1.txt` from the earlier runs.
   No k = 0 reproduction is needed first (gm/ unchanged; the job checks the gm code and the free arm).
6. After the run: commit the report to tools/bbgq/results/gm_core_v1.txt; append the TRIAL ROW to gm/trials.csv (with
   `when`); append the "outcomes" paragraph under the CHANGES entry (item 9: each part's verdict, Core book v1's parts
   and config hash, each shadow part's status). Then 7.6 step 7 (the pre-B diagnostics of 7.5 order item 3).

| File (PC destination under local\) | Status | sha256 |
|---|---|---|
| jobs\gm_core_v1.py (core_v1 1.1.0 pinned; REBUILD_SHA = 4f191fea... set 2026-11-27, CHANGES item 4e) | new | d89862a0266415c589ce40f768c983dc47dfb4ded088a2a5ccabb9c6d30fe67a |
| lib\core_v1.py (1.1.0) | new | ee01320501fd1ec1f1fcc8b89dca91000e7644f728ed67cbb9e4ac674b04549e |
| lib\rebuild_s4.py (1.1.0, separate agent, commit 4a5d5b6; accepted and registered, CHANGES item 4e) | new | 4f191fea1dfac0ae4f67ddd3974c92dd79969f6fa5414ef107de70d5315ed17d |
| lib\gm\trials.csv (61 rows; book / pod digest 676b7b0f..., N 40) | unchanged since the diagnostics run | e61e94a4906a932a1353de1edb916a0c2e12c640f09b8a1525ce5c60cba8cabe |
| lib\gm\CHANGES.md (documentation, not checked) | changed | eaa5adf8e4f78327f9e5a2035342f0d3971c7050f6fdfb71dd0cfa671eeb17db |
| lib\diag_a2.py (1.0.1) | unchanged | 3264a5381c13b124d2566d02f263e21905f4e901680c1af7c2134f0bd558be1b |
| lib\a2_batch.py (1.1.1) | unchanged | 35339f673f351f43315ad3c7010ba733b6fb8990a6a41feb1ef20de324de58c6 |
| lib\a1_panel.py (1.1.0) | unchanged | eb9ef3f7fbd12760e174f9ef1df8573890bed6ca8d36f7d4e5c63eadd822ebb5 |
| lib\gm_engine.py (1.3.0) | unchanged | ac43a33cd8943719ba0efb9bb246473c7bbf59018a6d3b7398f64520eeebd721 |
| lib\bbg_panel.py | unchanged | e0b67a42793e67c129ec8a6c3ed2082390933ea9317898b59b8854387ecf1dcd |
| lib\bbgdata.py (= LOCK_v2 code hash) | unchanged | 0b26bb21b50671dca7c2153d3d66a2a09f7f33eeaa7c96ca536b69bbca8e6351 |
| lib\engine_ref.json (gm-2.2.1 reference) | unchanged | cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39 |
| lib\gm\*.py | unchanged | engine_ref.json code.gm_files_sha256 |
| tests\data\rebuild_s4_stub.py (0.0.2, interface v2; cloud tests only; never ships) | - | 4bf94e8f7ebe975061fe90cd76b1c4668c6a3c6b65b4e547dc96eef5cb6979b5 |

## Blocked / open

- S4 needs the independent rebuild (above, step 1): until REBUILD_SHA is registered the job stops at its checks.
- Live-source condition recorded, not blocking (entry item 4f): GB and euro-area 3-month rates need a registered free
  replacement before 2027-01 (7.10 item 2).
- Not part of this step: 7.6 step 7 diagnostics (R1, F0, card diagnostics), B1 / B2.
