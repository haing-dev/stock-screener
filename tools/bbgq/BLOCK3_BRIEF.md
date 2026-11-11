# Block 3 build brief (WORKFLOW v2.1 step 0.5): reader update for the re-pull, engine on the PC

Repo: /home/claude/stock-screener (work on main; do NOT commit or push, the orchestrator does). Read first:
`CLAUDE.md` (sections "Global Macro Book" and the 2026-11-10 / 11-11 status lines), `docs/research/WORKFLOW.md`
(sections 2, 4 phase 0, 5), `tools/bbgq/README.md` (how jobs run on the PC, export whitelist), `tools/bbgq/BLOCK2_BRIEF.md`
(what block 2 built), `tools/bbgq/lib/bbgdata.py`, `tests/bbgq_smoke.py`, `docs/research/bbg/LOCK_v1_check_2026-11-11.md`
(state of the pulled data), `docs/data_requests/build_bloomberg_repull.py` (layout of the re-pull workbooks),
the engine `gm/` (config, panel, signals, book, vol, daily, timing, run, protocol, stats, bloomberg, holdout).

## Situation
- The Bloomberg workbooks sit on the user's Windows PC and never leave it. You cannot see them. Jobs are single .py files
  the PC runs with cwd = `Documents\WRDS results\local`, env `BBG_DIR`, `BBG_WORK` (= local\work), PYTHONPATH =
  local\lib;local\pylib. PC: Python 3.15, numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, openpyxl 3.1.5, NO pyarrow.
  Only printed reports come back and they must obey the export whitelist.
- Lock v1 is provisional: files 1 and 3 have cut-off monthly history (and those copies disagree with other copies), file 5
  is partly loaded. On Friday 13 Nov the user re-pulls seven workbooks R1..R7 (templates in
  `docs/data_requests/bloomberg_repull_2026-11-13/`): data sheets named `<original file digit> <original sheet>`
  (e.g. `1 Curves`, `5 ComCurve` which appears in two R files with different tickers), same block layout as before, plus
  a `Check` sheet to skip. The pulled R files will be saved into the same `pulled results` folder, names starting with
  `R<n>_` and possibly carrying suffixes (` 1`, `(1)`, `_CUT`, `_VALUES`).
- The book engine is `gm/` (BASE = gm-1.2.0 live paper book, CANDIDATE = gm-2.0). It builds its panel from free data
  in `cache/macro/raw/research` (present in this sandbox, 118 MB, free sources) and `gm/data`.
- HOLDOUT RULE (hard): nothing computed from returns, prices or positions dated after 2010-12-31 may be printed,
  logged, asserted on in a way that reveals it, or looked at by you. All comparisons, fingerprints and statistics in this
  block use dates <= 2010-12-31 only. Hashes over data after 2010 are not needed; do not make them.
- The engine's rules are pre-registered. Do NOT change the behaviour of anything in `gm/` (no fixes, no refactors that
  alter numbers). If you find a problem, report it. Compatibility edits that provably leave every number unchanged are
  allowed only if the PC's pandas 3.1.1 / Python 3.15 requires them, and you must list each one.

## Part A: reader update for the re-pull (small; do this first)
`tools/bbgq/lib/bbgdata.py` -> version bbgdata-1.1.0:
1. `find_workbooks` also accepts re-pull workbooks: file name matches `^\s*R(\d+)\D`. Several R files per number can
   exist (e.g. `R2_x.xlsx` and `R2_x_CUT.xlsx`): use the newest by modification time, warn about the others.
2. In an R workbook each data sheet `<d> <Sheet>` holds blocks that belong to original file `<d>`, sheet `<Sheet>`.
   Rule: a re-pulled block REPLACES the first-pull block with the same (file digit, sheet, ticker, field) when the
   re-pulled block has status ok. When the re-pulled block is requesting / invalid / empty, the first-pull block is kept
   (if any). A block that exists only in the R file is added. Series ids, duplicate handling, live-source tags and
   untouched flags must come out exactly as if the block had been in the original sheet (sheet-level defaults are looked
   up by the ORIGINAL file digit and sheet).
3. The catalog gets a column `source` (`first` or the R file number, e.g. `R2`) and, for replaced blocks, the first-pull
   first valid date and count (so the report can show how much history the re-pull added). The manifest and lock id
   include the R workbooks' hashes. A build with no R files present must give byte-identical tables and the same
   catalog content as today apart from the new columns (state how you checked this on the mocks).
4. `jobs/bbg_build_v2.py` and `jobs/bbg_check_v2.py` (copies of v1 with the new report lines: per R file the sheets and
   block counts, replaced / added / kept-first counts per original sheet, and per original sheet the median first valid
   date before and after). Keep v1 jobs untouched. In the check, for a replaced block also compare the re-pulled series
   with the first-pull copy over their common design months and print counts only (months compared, equal within
   1e-6 relative).
5. Extend `tests/bbgq_smoke.py`: mock R files built from the real R templates (random-walk values consistent with the
   mock originals for the same ticker and field where the original was not cut; one R sheet with a requesting block;
   one `_CUT` twin with an older modification time), then assert the replacement rule, unchanged ids, the no-R-files
   identity, a changed lock id when R files appear, and the whitelist scan. It must still print "BBGQ SMOKE OK".

## Part B: the engine on the PC
Goal: the same `gm/` code runs on the PC, first on free data (must reproduce the cloud result), later on Bloomberg data
through `bbgdata.Panel`. Deliver under `tools/bbgq/` (plus tests under `tests/`):
1. `build_engine.py`: assembles what the PC needs into `tools/bbgq/engine_pkg/` (git-ignored build output): the `gm/`
   package copied unchanged (list any compatibility edit), and a zip of the free inputs the engine reads
   (`cache/macro/raw/research` minus anything the engine never opens, plus `gm/data`). Print the file list and sizes.
   Say exactly where each piece must be placed under `Documents\WRDS results\local\` (suggest `lib\gm\` and
   `work\free\...`) and how the engine finds it there (an environment variable or a small path shim is fine, as long
   as `gm/` numbers do not change; if `gm/panel.py` hard-codes the repo path, solve it without editing behaviour).
2. `engine_ref.py` -> `engine_ref.json` (committed): the reference fingerprint of the cloud run on free data, DESIGN
   PERIOD ONLY (months <= 2010-12): for BASE and CANDIDATE the net Sharpe ratio, mean, volatility and worst drawdown
   over 1975-2010 and over 1990-2010; per market the count of non-missing return months; and a compact numeric
   fingerprint that allows a tolerance comparison across library versions (for example, per calendar year the sum of
   book returns rounded to 1e-10, and per market the sum of absolute positions rounded to 1e-8). Include code version
   (git commit of gm/), config hashes and library versions.
3. `jobs/gm_repro_v1.py` (runs on the PC): unpack the free inputs if needed, run panel -> signals -> book for BASE and
   CANDIDATE, compare with `engine_ref.json` (shipped next to the job in `lib\`), print per item PASS/FAIL with the
   largest absolute difference and the tolerance (book returns 1e-8, positions 1e-6, statistics 1e-6), library
   versions, run time. Design period only. Ends with "=== END ===".
4. Truncation test (`tools/bbgq/engine_trunc.py`, runnable here and as PC job `jobs/gm_trunc_v1.py`): for at least six
   cut dates T spread over 1980-2010, rerun the engine with every input cut at T (no observation dated after T can be
   read: do it at the loader level, not by editing gm behaviour) and compare signals and positions for all decision
   months <= T with the full run. Report per cut date PASS/FAIL per stage (panel returns, each signal family,
   volatility estimate, positions) with counts of differing market-months and the largest absolute difference, and
   for every failure the place in the code that causes it (for example an estimate that uses the whole sample).
   Do NOT fix failures; list them with a one-line proposed fix each. This is the gate "truncation test passes" and
   honest failures are the useful output.
5. Bloomberg adapter `tools/bbgq/lib/bbg_panel.py`: serves the series the engine needs from `bbgdata.Panel(...).asof(T)`
   instead of the old single-file reader `gm/bloomberg.py` (same series, same conventions; read that file and its test
   `tests/gm_bloomberg_smoke.py`). It must not change `gm/`; it provides the objects `gm` expects (or a thin wrapper
   that swaps the data source) so that a later job can run the book with Bloomberg inputs for chosen markets. Include
   job `jobs/gm_bbg_map_v1.py`: for each market and each signal input of the engine, which Bloomberg series id would be
   used, whether it is present and usable in the current lock (status, first valid design date, design months), and
   what stays on free data. Metadata only. Test it on the mock workbooks of the smoke test.
6. Weekly implementation: do not build it. Report in five lines what exists today (gm/timing.py, gm/daily.py) and what
   is missing for a weekly-tranche implementation check on 1990-2010 (WORKFLOW section 5, Batch A2).
7. `tests/bbgq_engine_smoke.py`: runs the reproduction against the reference here, one truncation date, the adapter on
   mocks, and a whitelist scan of every new job's output (no dated value rows; nothing after 2010). Prints
   "BBGQ ENGINE SMOKE OK". If a pandas 3.1.1 / numpy 2.5.4 environment can be created here with pip, run the
   reproduction in it as well and report the differences (this sandbox has pandas 3.0.5).
8. Update `tools/bbgq/README.md` with a "Block 3" section (what each file does, how to deploy, how to read the reports).

## Rules
- Reports obey the export whitelist: names, counts, date ranges, pass/fail, differences, and summary statistics over at
  least 60 months of the design period. No per-date rows, no single data value.
- Jobs must finish in under 60 minutes on a laptop and must not crash on a missing optional input: report and continue.
- Keep it readable: a non-coder's project, checked by a second agent afterwards. No new dependencies.
- Do not read or write outside `tools/bbgq/`, `tests/bbgq_*.py`, `.gitignore` (one line for engine_pkg) unless a
  compatibility edit in `gm/` is unavoidable (then list it).
- Use scratch space only under `/tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/b3/`.

Reply with: files written; both smoke results; the reference statistics table (design period); the truncation table
with every failure and its cause; the adapter coverage in one paragraph; exact deployment list for the PC (file ->
destination, sizes); every assumption the first PC run should confirm; anything you could not do.
