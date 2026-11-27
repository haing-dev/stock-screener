# Pre-B diagnostics build (2026-11-27): TESTING_PROTOCOL 7.6 step 7, 7.5 order item 3, the PC job

**UPDATED for diag_preb 1.1.0** (every row runs; nothing blocked). Registered in gm/CHANGES.md "Pre-B diagnostics"
(6497db6) BEFORE any code; two corrections before the code (bd6e3f5); code 1.0.0 fd760ae; then the data entry "card
inputs (FRED / ALFRED first release, macro-data branch)" (12e108c) and the addendum 1.1.0 (6146c2c), both before the
1.1.0 code (049ab75). The job gm_diag_preb_v1 had not run, so it is extended in place (no v2). NOT RUN: no
diagnostic statistic was computed in the cloud on the free, A1, LSEG or card-input data. gm/ is unchanged
(engine_ref.json unchanged).

Reference book: the A2-final book A1_INCUMBENT gm-2.0.4-candidate-x1 (77374d7bef), engine gm-2.2.1, A1 panel
e7f98d44..., book.run "pos". LSEG: LOCK_LSEG_v5 90322681..., design part, as of 2010-12-31, held-back instruments hidden.
Core book v1 is EMPTY; no diagnostic changes its reference because of it (entry item 3: C3-D1 "Core book" = the
registered systematic book, "content, not trading status").

## The step-7 diagnostics

| Id | Question | Gate | Sealed cut | Data | Where | Trigger | Status |
|---|---|---|---|---|---|---|---|
| R1 | Local bends on the dollar strip larger than cost and still there the next day? | qualifying / eligible triple-months >= 0.5 | month-ends 1990-01..2010-11; holding end by calendar arithmetic (no 2011 date read) | LSEG ED quarterly contracts, Datastream daily (L14, deliveries 1982-2012, identity in the code), NYSE days | PC | PASS: Strip reversion in B2 (both versions); FAIL: dropped unbuilt, logged | RUNS |
| C1-D1 | Enough episodes (card 1)? | fewer than 6 episodes of condition months (any version) -> analyst watch condition; with F0 | decisions to 2010-11 | card inputs (FEDFUNDS, GS2, GS5, GS10, BAA, TWEXMMTH / DTWEXBGS, WTISPLC, CPILFESL and M2SL first release), panel.fx_usd_value, A1 panel (gold) | PC | rule stays / watch condition | RUNS, R1-R5 |
| C1-D2 | Card 1 legs already held? | > 80% of held market-months same sign as the registered systematic book -> leg dropped | decisions to 2010-11 | rule legs + book pos | PC | leg stays / dropped | RUNS, every leg of R1-R5 |
| C2-D1 | Room to ease: do bonds stop balancing stocks near a zero short rate? | >= 30 pooled low-rate worst-fifth months, other mean > 0, low mean < half -> floor versions on card 1 R1, R2 + card 2 stop line | design months 1975-01..2010-12 | TB3MS, IR3TIB01 JP / DE then EZ / GB / CA (free), A1 panel bonds and indexes | PC | floor versions or no change | RUNS |
| C2-D2 | Card 2 versions: enough cases, overlap with card 1 R4 | version left out if < 24 on-months, < 3 episodes, or > 2/3 in R4's 4.5 state | decisions to 2010-11 | card inputs (GS10, CPILFESL and UNRATE first release, FEDFUNDS), ^GSPC, A1 panel | PC | version kept / left out | RUNS |
| C3-D1 | Card 3 duplicate of the systematic book? | >= 0.80 dropped, 0.50-0.80 flagged | decisions to 2010-11 | R1: OECD 3-month rates + TB3MS (free) and FEDFUNDS; R2, R3: GS1, GS2, GS10, FEDFUNDS, PCEPILFE first release; R4: LSEG forward EPS, ^GSPC, TB3MS | PC | rule kept / flagged / dropped | RUNS, R1-R4 (after C3-D2) |
| C3-D2 | Quiet months for card 3 R1's activity gate | < 60 gate-off months -> gate dropped (R1 8 versions with sizing) | design months 1975-2010 | FEDFUNDS | PC | gate kept / dropped | RUNS |
| C4-D1 | Market up, volatility up: larger later fall? | median ratio >= 1.25 in 1990-01..2010-06 and each half -> half-size version | last state month 2010-06 | VIXCLS (monthly mean), ^GSPC daily | PC | +14 sizing versions / analyst question | RUNS |
| C4-D2 | Card 4 R5 overlap with card 3 R2 and Trend | either share >= 0.80 in both versions -> R5 not registered | decisions to 2010-11 | CPILFESL first release, FEDFUNDS, GS2, GS10; A2-final Trend score | PC | R5 note / stays | RUNS |
| C5-D1 | Card 5 R1 a Trend duplicate? | >= 75% of held market-months with the 12-month Trend versions long -> not registered | decisions to 2010-11 | LSEG HG c1, CL c1 (monthly), A1 panel (Trend 12-month versions, vol) | PC | R1 stays / not registered | RUNS (real-ceiling versions cannot change held months: entry item 5 F0 f) |
| C5-D2 | Slow class breaks further than grains? | copper share >= grains + 0.15, >= 10 breaks each | breaks to 2008-12 | LSEG c1 of HG, CL (reported), W, C, S | PC | R1 built / dropped unbuilt | RUNS; reported cocoa / LME line NOT computed (held-back instruments, correction 2) |
| F0 | Rule-layer floor | >= 48 held months and >= 3 episodes -> judged in B2, else not judgeable | decisions to 2010-11 (daily rules: days to 2010-12-31) | as the rules | PC | judged in B2 / watch condition | RUNS for all 17 card rules, each after its card's own gates (addendum A2) |

Known from the rule text before any run (entry correction 1): card 4 R2 has one episode on any data and R4 one
episode unless its versions cancel 11 months running, so both read "not judgeable" under F0 as registered.

Card rule-layer engine: NOT built. Only the minimal positions each diagnostic needs (every card rule's positions,
signs and held months; card 3's fixed-size notional and sizing version because they decide card 3 R1's averaged sign),
positions only, no rule return. 7.5 requires no full layer engine for any of
these; the full engine (returns, costs, placebo date mover use, T1-T4) belongs to B2.

## Card inputs (data entry "card inputs", LOCK_CARD_v1)

Source: origin/macro-data at 264d0a2cc2f74d02264b30a52d5e8f0950db9cca. 19 files (sha256 per file in the entry and in
docs/research/card_inputs/LOCK_CARD_v1.json): root GS1, GS2, GS5, GS10, FEDFUNDS, BAA, TWEXMMTH, DTWEXBGS, WTISPLC,
VIXCLS (the Macro Compass live fetch), root M2SL and PCEPILFE (ALFRED first release: the branch manifest says how =
"first release", so their first vintages DO exist), research/CPILFESL_FR and UNRATE_FR (first release), research/
CPILFESL, UNRATE, M2SL, PCEPILFE (latest: months before the first vintage, flagged, as every card spec allows), and
the root manifest.json (provenance). Lock id 6c154f7d736cefd141fac2252a71536811e7440724d8e3cb4d4eacfecb8e3110.
Packaging: a SEPARATE small zip work\free\gm_card_inputs.zip (sha256 4f84b01d..., deterministic, built from git by
tools/bbgq/build_card_inputs.py inside build_engine), checked file by file by lib\card_inputs.py; the free inputs zip,
its digest, engine_ref.json and the k = 0 reproduction are unchanged. Cut at 2010-12-31 on parsing; lags from the
specs (FEDFUNDS, GS*, BAA, TWEXMMTH, DTWEXBGS, VIXCLS 0; WTISPLC, CPILFESL, M2SL, UNRATE 1; PCEPILFE 2). First-release
breaks (PCEPILFE rebases 2003-11, 2009-06; M2SL 1983-01, 1996-01): changes across them use latest values, flagged.

Nothing stays blocked. No LSEG pull is needed (no builder in docs/data_requests/).

## What the job prints (tools/bbgq/jobs/gm_diag_preb_v1.py on the PC)

1. Checks, STOP before any Bloomberg or LSEG value on a FAIL: gm code = engine_ref.json; `PASS lib engine_ref.json`
   (cebd4932...); engine gm-2.2.1 and the four config hashes; 10 lib files = LIB_SHA (incl. card_inputs.py); `PASS lib gm\trials.csv book / pod
   rows | 41 rows | digest f200d02c...`; A2, diagnostics and Core book v1 reports (CORE V1 JOB DONE, CORE BOOK V1 EMPTY);
   Bloomberg store LOCK_v2; LSEG store lock id read from its manifest = LOCK_LSEG_v5; `PASS card inputs
   gm_card_inputs.zip | 19 files, each = its LOCK_CARD_v1 sha256 | lock id 6c154f7d...` (else STOP); free inputs = the
   reference.
2. Free arm vs reference; A1 panel rebuilt, extension-only, `PASS A1 PANEL ID e7f98d44...`, compared with the saved
   file; nothing written.
3. `card inputs | fx values ... | rates ...` (months and first dates only).
4. `PASS A2-final book as run (A2 report)` (else STOP); `--- PRE-B DIAGNOSTICS ...`; `CORE BOOK READING | ...`;
   `R1 | ...`, `R1 GATE`; `CARD INPUTS | <series> | ... flagged share 1975-2010 ... | breaks ...` (CPILFESL, M2SL,
   PCEPILFE changes, UNRATE level); `C2-D1 | ...`, `C2-D1 GATE`; per card 1 rule `C1-D1 | card 1 Rn | ...` and
   `C1-D2 | card 1 Rn <leg> leg | ...`; per card 2 version `C2-D2 | card 2 Rn version ... | kept / left out`;
   `C3-D2 | ...`; `C3-D1 | card 3 Rn | ...`; `C4-D1 | <window> | ...`, `C4-D1 GATE`; `C4-D2 | card 4 R5 version n |
   ...`, `C4-D2 GATE`; `C5-D1 | ...`; `C5-D2 | ...`, `C5-D2 GATE`; `F0 | <rule> | held months | episodes | ... | <gate
   note>` for the 17 card rules; `PRE-B SUMMARY | ...`.
5. Twelve `TRIAL ROW {...}` lines (family diag, no Sharpe columns), then `PREB JOB DONE`.
Printing: shares and means only over at least 60 months (else count and sign); counts, PASS / FAIL, ids; no LSEG or
Bloomberg value.

## Cloud gates (no diagnostic statistic computed)

1.1.0 (2026-11-27):
- k = 0 reproduction 24 of 24, difference 0 (tools/bbgq/results/engine_repro_cloud_2026-11-27h_gm-2.2.1.txt).
- Truncation PASS at all 8 cut dates, 21 k = 0 and 37 feature stages (results/engine_trunc_cloud_2026-11-27h_gm-2.2.1.txt).
- tests/run_tests.py ALL TESTS PASSED (results/run_tests_gm_2026-11-27j_gm-2.2.1.txt), incl. tests/diag_preb_smoke.py
  71 checks: the 1.0.0 checks plus the card inputs reader (lags, daily means, first release vs latest with flags, a
  planted rebase break, seal, the lock on the real git files: hashes only, no value used), card 1 R1 / R4, C2-D2,
  C3-D2, card 3 R1 / R2, fixed size, card 4 R5, C4-D2, C4-D1 by hand or by construction, the report with every line and
  no BLOCKED line, 12 trial rows, the seal on all inputs, the job's STOP paths (12 PASS lib lines).
- `python3 tools/bbgq/build_engine.py`: engine_pkg/ built with work/free/gm_card_inputs.zip.
1.0.0: as before (results/*_2026-11-27g / i).

## Queue order (coordinator)

1. `python3 tools/bbgq/build_engine.py` (done for this note; rerun if anything changes).
2. Copy to `C:\Users\admin\Documents\WRDS results\local\` (same relative path) the files marked new or changed below,
   including `work\free\gm_card_inputs.zip`.
   lib\gm\trials.csv must be the repo version (63 lines; the job pins only its book / pod rows: 41, f200d02c...).
3. Read every copied file back (stage it) and compare its sha256 with the table BEFORE queuing.
4. Queue `jobs\gm_diag_preb_v1.py` -> `local\jobs\`; it needs `local\results\gm_a2_v1.txt`, `gm_diag_v1.txt`,
   `gm_core_v1.txt`, `work\bbg\` (LOCK_v2), `work\lseg\` (LOCK_LSEG_v5) and `work\free\gm_card_inputs.zip`
   (LOCK_CARD_v1). No k = 0 reproduction first (gm/ unchanged;
   the job checks the gm code and the free arm). Read `local\results\gm_diag_preb_v1.txt`.
5. After the run: commit the report to tools/bbgq/results/gm_diag_preb_v1.txt; append the 12 TRIAL ROWs to gm/trials.csv;
   an "outcomes" paragraph under the CHANGES entry (item 6); spec text edits citing it.
6. Then 7.6 step 8 (B1 = Curve carry if its contract-history lock condition holds, else moved to B2) and step 9 (B2).

| File (PC destination under local\) | Status | sha256 |
|---|---|---|
| jobs\gm_diag_preb_v1.py (diag_preb 1.1.0 and card_inputs 1.0.0 pinned) | new | 76e93713cf9079845b7fac39c305ca1c61bf6cca168f4bdbb86835497473f8f8 |
| lib\diag_preb.py (1.1.0) | new | 5273944bcb9811ccba83510da3359996e28def8eb8b89a4408ed3efad855c64e |
| lib\card_inputs.py (1.0.0) | new | 4091f84bcbb11f43061bcc0330520a4a5580cb775895148a38849c0fbcab7b80 |
| work\free\gm_card_inputs.zip (LOCK_CARD_v1 6c154f7d...) | new | 4f84b01d07ad59da05ad7e8ca4e78b31b1ed687941c6852da804c685be1b068d |
| lib\lsegdata.py (1.0.0 = LOCK_LSEG_v5 code hash; already on the PC) | unchanged (verify) | 0d1b500ddb2e931ab4069ac8fd6fed0c16778da85b2665d3fcafadfae16198de |
| lib\lseg_rules.py (1.1.0; already on the PC) | unchanged (verify) | 5686999172a22c76b7190f8df210c93ffc09a6737f32301df030080dccc42da9 |
| lib\lseg_engine_map.csv (= lock config) | unchanged (verify) | 8812f20d4d6dadcbfe5171cbe92b03a57f65ba01599a6d17d842130864bbaa15 |
| lib\lseg_exclusions.csv (= lock config) | unchanged (verify) | 8e2ca054128ce420543d8e06252af14255a8492064a647e73e69dde90fb45bf9 |
| lib\lseg_live_sources.csv (= lock config) | unchanged (verify) | 37e42068a8ae7f36ee12ece245c3c17b6cc27ac6f51b52078d54e1a891c4c77f |
| lib\lseg_roots.csv (= lock config) | unchanged (verify) | 7a8caf01fbc70108af78be145337b41ac7e0050fc3f326211c997dc1a9991ee3 |
| lib\lseg_untouched.csv (= lock config; hides cocoa and LME cash) | unchanged (verify) | 17ec5fb38c2cc3b3f337adac2478d04c100fb949bcbcfe159fd53f26ef705185 |
| lib\gm\trials.csv (63 lines; book / pod digest f200d02c..., N 41) | changed (Core book v1 row) | 2774b59568595183383345840a8988aa6af26551dc31ceaab4a1f3c0ec806581 |
| lib\gm\CHANGES.md (documentation, not checked) | changed | the repo version at the build-note commit |
| lib\diag_a2.py (1.0.1) | unchanged | 3264a5381c13b124d2566d02f263e21905f4e901680c1af7c2134f0bd558be1b |
| lib\a2_batch.py (1.1.1) | unchanged | 35339f673f351f43315ad3c7010ba733b6fb8990a6a41feb1ef20de324de58c6 |
| lib\a1_panel.py (1.1.0) | unchanged | eb9ef3f7fbd12760e174f9ef1df8573890bed6ca8d36f7d4e5c63eadd822ebb5 |
| lib\gm_engine.py (1.3.0) | unchanged | ac43a33cd8943719ba0efb9bb246473c7bbf59018a6d3b7398f64520eeebd721 |
| lib\bbg_panel.py | unchanged | e0b67a42793e67c129ec8a6c3ed2082390933ea9317898b59b8854387ecf1dcd |
| lib\bbgdata.py (= LOCK_v2 code hash) | unchanged | 0b26bb21b50671dca7c2153d3d66a2a09f7f33eeaa7c96ca536b69bbca8e6351 |
| lib\engine_ref.json (gm-2.2.1 reference) | unchanged | cebd4932e8643f14c541258abe68809a4e3c119f0c384beaa3d656b44c955e39 |
| lib\gm\*.py | unchanged | engine_ref.json code.gm_files_sha256 |
| tests\diag_preb_smoke.py (cloud tests only; never ships) | - | cea4ae2f14542962b8d51b25bfdd0783a170f7d89623750f5eb6db99d0604f78 |
| tools\bbgq\build_card_inputs.py (cloud builder; never ships) | - | eb61f119fed530dd9a2660085613d85b259f941deae76177f3f387f5373cd9bd |
| docs\research\card_inputs\LOCK_CARD_v1.json (repo lock record) | - | ab3a08cd002885bd994c9199dc8b89bb3bea0abec016e3d1eb05118e7649eea1 |
