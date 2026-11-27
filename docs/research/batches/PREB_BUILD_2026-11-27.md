# Pre-B diagnostics build (2026-11-27): TESTING_PROTOCOL 7.6 step 7, 7.5 order item 3, the PC job

Registered in gm/CHANGES.md "Pre-B diagnostics" (commit 6497db6) BEFORE any code; two corrections found while coding
registered before the code commit (bd6e3f5); code fd760ae. NOT RUN: no diagnostic statistic was computed in the cloud
on the free, A1 or LSEG data. gm/ is unchanged (engine_ref.json unchanged).

Reference book: the A2-final book A1_INCUMBENT gm-2.0.4-candidate-x1 (77374d7bef), engine gm-2.2.1, A1 panel
e7f98d44..., book.run "pos". LSEG: LOCK_LSEG_v5 90322681..., design part, as of 2010-12-31, held-back instruments hidden.
Core book v1 is EMPTY; no diagnostic changes its reference because of it (entry item 3: C3-D1 "Core book" = the
registered systematic book, "content, not trading status").

## The step-7 diagnostics

| Id | Question | Gate | Sealed cut | Data | Where | Trigger | Status |
|---|---|---|---|---|---|---|---|
| R1 | Local bends on the dollar strip larger than cost and still there the next day? | qualifying / eligible triple-months >= 0.5 | month-ends 1990-01..2010-11; holding end by calendar arithmetic (no 2011 date read) | LSEG ED quarterly contracts, Datastream daily (L14, deliveries 1982-2012, identity in the code), NYSE days | PC | PASS: Strip reversion in B2 (both versions); FAIL: dropped unbuilt, logged | RUNS |
| C1-D1 | Enough episodes (card 1)? | fewer than 6 episodes of condition months (any version) -> analyst watch condition; with F0 | decisions to 2010-11 | R5: panel.fx_usd_value | PC | rule stays / watch condition | R5 RUNS; R1-R4 BLOCKED (FEDFUNDS, GS2, GS5, GS10, BAA, TWEXMMTH/DTWEXBGS, WTISPLC, CPILFESL, M2SL not in any registered source) |
| C1-D2 | Card 1 legs already held? | > 80% of held market-months same sign as the registered systematic book -> leg dropped | decisions to 2010-11 | R5 + book pos | PC | leg stays / dropped | R5 legs RUN; R1-R4 legs BLOCKED (as C1-D1) |
| C2-D1 | Room to ease: do bonds stop balancing stocks near a zero short rate? | >= 30 pooled low-rate worst-fifth months, other mean > 0, low mean < half -> floor versions on card 1 R1, R2 + card 2 stop line | design months 1975-01..2010-12 | TB3MS, IR3TIB01 JP / DE then EZ / GB / CA (free), A1 panel bonds and indexes | PC | floor versions or no change | RUNS |
| C2-D2 | Card 2 versions: enough cases, overlap with card 1 R4 | version left out if < 24 on-months, < 3 episodes, or > 2/3 in R4's 4.5 state | - | GS10, CPILFESL, UNRATE (ALFRED), FEDFUNDS | - | version kept / left out | BLOCKED |
| C3-D1 | Card 3 duplicate of the systematic book? | >= 0.80 dropped, 0.50-0.80 flagged | decisions to 2010-11 | R4: LSEG S&P 500 forward EPS, ^GSPC month-end, TB3MS, book pos | PC | rule kept / flagged / dropped | R4 RUNS; R1 (FEDFUNDS gate versions), R2 (GS2, GS10), R3 (FEDFUNDS, GS1, GS2, PCEPILFE) BLOCKED |
| C3-D2 | Quiet months for card 3 R1's activity gate | < 60 gate-off months -> gate dropped (R1 4 versions) | - | FEDFUNDS | - | gate kept / dropped | BLOCKED |
| C4-D1 | Market up, volatility up: larger later fall? | median ratio >= 1.25 whole window and each half -> half-size version | last state month 2010-06 | VIXCLS, ^GSPC daily | - | +14 sizing versions / analyst question | BLOCKED (VIXCLS) |
| C4-D2 | Card 4 R5 overlap with card 3 R2 and Trend | either share >= 0.80 in both versions -> R5 not registered | - | CPILFESL, FEDFUNDS, GS2, GS10 | - | R5 note / stays | BLOCKED |
| C5-D1 | Card 5 R1 a Trend duplicate? | >= 75% of held market-months with the 12-month Trend versions long -> not registered | decisions to 2010-11 | LSEG HG c1, CL c1 (monthly), A1 panel (Trend 12-month versions, vol) | PC | R1 stays / not registered | RUNS (real-ceiling versions need CPILFESL but cannot change held months: entry item 5 F0 f) |
| C5-D2 | Slow class breaks further than grains? | copper share >= grains + 0.15, >= 10 breaks each | breaks to 2008-12 | LSEG c1 of HG, CL (reported), W, C, S | PC | R1 built / dropped unbuilt | RUNS; reported cocoa / LME line NOT computed (held-back instruments, correction 2) |
| F0 | Rule-layer floor | >= 48 held months and >= 3 episodes -> judged in B2, else not judgeable | decisions to 2010-11 (daily rules: days to 2010-12-31) | as the rules | PC | judged in B2 / watch condition | card 1 R5, card 3 R4, card 4 R1-R4, card 5 R1 RUN; card 1 R1-R4, card 2 R1-R2, card 3 R1-R3, card 4 R5 BLOCKED |

Known from the rule text before any run (entry correction 1): card 4 R2 has one episode on any data and R4 one
episode unless its versions cancel 11 months running, so both read "not judgeable" under F0 as registered.

Card rule-layer engine: NOT built. Only the minimal positions each runnable diagnostic needs (card 1 R5, card 3 R4,
card 4 R1-R4 day windows, card 5 R1), positions only, no rule return. 7.5 requires no full layer engine for any of
these; the full engine (returns, costs, placebo date mover use, T1-T4) belongs to B2.

## What unblocks the BLOCKED rows

One registered data entry "card inputs (FRED / ALFRED)" (entry item 4): GS1, GS2, GS5, GS10, FEDFUNDS, BAA, TWEXMMTH,
DTWEXBGS, WTISPLC, VIXCLS, UNRATE and the ALFRED first vintages of CPILFESL, M2SL, PCEPILFE, UNRATE, fetched once,
cut at 2010-12-31, locked apart from the free inputs zip, with the 7.6 step 2 metadata listing; then a job
gm_diag_preb_v2 under its own dated entry. No LSEG pull is needed (so no builder in docs/data_requests/). B2 cannot
start before those rows run.

## What the job prints (tools/bbgq/jobs/gm_diag_preb_v1.py on the PC)

1. Checks, STOP before any Bloomberg or LSEG value on a FAIL: gm code = engine_ref.json; `PASS lib engine_ref.json`
   (cebd4932...); engine gm-2.2.1 and the four config hashes; 9 lib files = LIB_SHA; `PASS lib gm\trials.csv book / pod
   rows | 41 rows | digest f200d02c...`; A2, diagnostics and Core book v1 reports (CORE V1 JOB DONE, CORE BOOK V1 EMPTY);
   Bloomberg store LOCK_v2; LSEG store lock id read from its manifest = LOCK_LSEG_v5; free inputs = the reference.
2. Free arm vs reference; A1 panel rebuilt, extension-only, `PASS A1 PANEL ID e7f98d44...`, compared with the saved
   file; nothing written.
3. `card inputs | fx values ... | rates ...` (months and first dates only).
4. `PASS A2-final book as run (A2 report)` (else STOP); `--- PRE-B DIAGNOSTICS ...`; `CORE BOOK READING | ...`; the
   `BLOCKED | ...` lines; `R1 | ...` (contracts, coverage, month-ends, first normals, left-out counts, per K_n
   qualifying / eligible / share), `R1 GATE | ... | PASS / FAIL`; `C1-D1 | card 1 R5 | ...`; `C1-D2 | card 1 R5
   stock leg / bond leg | ...`; `C2-D1 | ...` (counts by country, pooled and Japan means in %/yr over >= 60 months, else
   count and sign), `C2-D1 GATE`; `C3-D1 | card 3 R4 | ...`; `C5-D1 | card 5 R1 | ...` and the reported book-sign line;
   `C5-D2 | reported line not computed ...`, slow / grains / crude break counts, `C5-D2 GATE`; `F0 | <rule> | held
   months | episodes | ...`; `PRE-B SUMMARY | ...`.
5. Eight `TRIAL ROW {...}` lines (family diag, no Sharpe columns), then `PREB JOB DONE`.
Printing: shares and means only over at least 60 months (else count and sign); counts, PASS / FAIL, ids; no LSEG or
Bloomberg value.

## Cloud gates (no diagnostic statistic computed)

- k = 0 reproduction 24 of 24, difference 0 (tools/bbgq/results/engine_repro_cloud_2026-11-27g_gm-2.2.1.txt).
- Truncation PASS at all 8 cut dates, 21 k = 0 and 37 feature stages, 0 failing end-to-end or alone (tools/bbgq/results/engine_trunc_cloud_2026-11-27g_gm-2.2.1.txt).
- tests/run_tests.py ALL TESTS PASSED (tools/bbgq/results/run_tests_gm_2026-11-27i_gm-2.2.1.txt), incl.
  tests/diag_preb_smoke.py, 52 checks on synthetic panels and a mock LSEG store (R1 strip identity, gap by an
  independent brute force, stale screen, seal; card rule signals by hand; every gate; LsegView on a mini lsegdata store
  incl. the hidden held-back instrument; report printing and seal; the job's STOP paths in the PC layout).
- `python3 tools/bbgq/build_engine.py`: engine_pkg/ built (DEPLOY.txt lists every file).

## Queue order (coordinator)

1. `python3 tools/bbgq/build_engine.py` (done for this note; rerun if anything changes).
2. Copy to `C:\Users\admin\Documents\WRDS results\local\` (same relative path) the files marked new or changed below.
   lib\gm\trials.csv must be the repo version (63 lines; the job pins only its book / pod rows: 41, f200d02c...).
3. Read every copied file back (stage it) and compare its sha256 with the table BEFORE queuing.
4. Queue `jobs\gm_diag_preb_v1.py` -> `local\jobs\`; it needs `local\results\gm_a2_v1.txt`, `gm_diag_v1.txt`,
   `gm_core_v1.txt`, `work\bbg\` (LOCK_v2) and `work\lseg\` (LOCK_LSEG_v5). No k = 0 reproduction first (gm/ unchanged;
   the job checks the gm code and the free arm). Read `local\results\gm_diag_preb_v1.txt`.
5. After the run: commit the report to tools/bbgq/results/gm_diag_preb_v1.txt; append the 8 TRIAL ROWs to gm/trials.csv;
   an "outcomes" paragraph under the CHANGES entry (item 6); spec text edits citing it.
6. Then the "card inputs (FRED / ALFRED)" data entry and gm_diag_preb_v2 for the blocked rows; then 7.6 step 8 (B1 =
   Curve carry if its contract-history lock condition holds, else moved to B2) and step 9 (B2).

| File (PC destination under local\) | Status | sha256 |
|---|---|---|
| jobs\gm_diag_preb_v1.py (diag_preb 1.0.0 pinned) | new | c32c9019049459060ba7cdaf920539ef135094c75291793a85fe3727aa66fc11 |
| lib\diag_preb.py (1.0.0) | new | 072b3dbe075353cc2ad6a3b2a95e0c50e97221ec05a8fddcf20b813493d11c77 |
| lib\lsegdata.py (1.0.0 = LOCK_LSEG_v5 code hash; already on the PC) | unchanged (verify) | 0d1b500ddb2e931ab4069ac8fd6fed0c16778da85b2665d3fcafadfae16198de |
| lib\lseg_rules.py (1.1.0; already on the PC) | unchanged (verify) | 5686999172a22c76b7190f8df210c93ffc09a6737f32301df030080dccc42da9 |
| lib\lseg_engine_map.csv (= lock config) | unchanged (verify) | 8812f20d4d6dadcbfe5171cbe92b03a57f65ba01599a6d17d842130864bbaa15 |
| lib\lseg_exclusions.csv (= lock config) | unchanged (verify) | 8e2ca054128ce420543d8e06252af14255a8492064a647e73e69dde90fb45bf9 |
| lib\lseg_live_sources.csv (= lock config) | unchanged (verify) | 37e42068a8ae7f36ee12ece245c3c17b6cc27ac6f51b52078d54e1a891c4c77f |
| lib\lseg_roots.csv (= lock config) | unchanged (verify) | 7a8caf01fbc70108af78be145337b41ac7e0050fc3f326211c997dc1a9991ee3 |
| lib\lseg_untouched.csv (= lock config; hides cocoa and LME cash) | unchanged (verify) | 17ec5fb38c2cc3b3f337adac2478d04c100fb949bcbcfe159fd53f26ef705185 |
| lib\gm\trials.csv (63 lines; book / pod digest f200d02c..., N 41) | changed (Core book v1 row) | 2774b59568595183383345840a8988aa6af26551dc31ceaab4a1f3c0ec806581 |
| lib\gm\CHANGES.md (documentation, not checked; changes again with the build-note commit) | changed | 644698e4a3b9cc2185aefa6c3f2e7db7761acd0b283cf15a15c8d511291366b4 |
| lib\diag_a2.py (1.0.1) | unchanged | 3264a5381c13b124d2566d02f263e21905f4e901680c1af7c2134f0bd558be1b |
| lib\a2_batch.py (1.1.1) | unchanged | 35339f673f351f43315ad3c7010ba733b6fb8990a6a41feb1ef20de324de58c6 |
| lib\a1_panel.py (1.1.0) | unchanged | eb9ef3f7fbd12760e174f9ef1df8573890bed6ca8d36f7d4e5c63eadd822ebb5 |
| lib\gm_engine.py (1.3.0) | unchanged | ac43a33cd8943719ba0efb9bb246473c7bbf59018a6d3b7398f64520eeebd721 |
| lib\bbg_panel.py | unchanged | e0b67a42793e67c129ec8a6c3ed2082390933ea9317898b59b8854387ecf1dcd |
| lib\bbgdata.py (= LOCK_v2 code hash) | unchanged | 0b26bb21b50671dca7c2153d3d66a2a09f7f33eeaa7c96ca536b69bbca8e6351 |
| lib\engine_ref.json (gm-2.2.1 reference) | unchanged | cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39 |
| lib\gm\*.py | unchanged | engine_ref.json code.gm_files_sha256 |
| tests\diag_preb_smoke.py (cloud tests only; never ships) | - | 4a55c8231255766bf7404b69e4554df5beedaa3d54092fdeb3f9628f2ee6d1b8 |
