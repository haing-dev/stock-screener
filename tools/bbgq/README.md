# bbgq: Bloomberg research data on the user's PC (2026-11-10)

The pulled Bloomberg workbooks stay on the PC (`Documents\WRDS results\mscifreedata\Bloomberg_UBC_pull_2026-11-04\pulled results`).
They never go to git, the Obsidian vault, chat or Claude's cloud workspace. Research and paper trading only.

How it runs: the scheduled task "WRDS runner" (`tools/wrdsq/runner/wrds_watch.ps1`, every 10 minutes) also runs local
jobs. Claude writes a Python file to `Documents\WRDS results\local\jobs\<name>.py` (modules to `local\lib\` first); the
PC runs it with `BBG_DIR` (the workbooks), `BBG_WORK` (`local\work`, derived tables, stays on the PC) and writes what
the job prints to `local\results\<name>.txt` (errors: `<name>.err.txt`). Status: `local\runner_status.txt`.
Use a new job name each time. Commit every job and module here (`tools/bbgq/jobs`, `tools/bbgq/lib`).

## Export whitelist (what a job may print)
Allowed: file, sheet, ticker and field names; counts; date ranges; coverage and fill shares; error strings; summary
statistics over at least 60 months or 250 days (Sharpe, mean, volatility, t-statistics, drawdown, turnover,
correlations, hit rates); pass/fail; config and lock ids.
Not allowed: any per-date series of prices, yields, returns or signals; any single data value; `.head()` or printed
tables of values. Claude never stages files from `local\work` or the workbooks themselves.
Holdout: until the one-time key is used, jobs print no price statistics for dates after 2010-12-31 (structure only).

## Block 2 (WORKFLOW 0.2-0.4): reader, data check, lock and seal
- `lib/bbgdata.py` is the only code that reads the workbooks or the derived tables. Copy it, `live_sources.csv` and
  `untouched_markets.csv` to `local\lib\` (it looks for the two CSVs next to itself or one folder up).
- `jobs/bbg_build_v1.py`: builds `local\work\bbg\` = `catalog.csv`, `design\{monthly,daily}.pkl` (to 2010-12-31),
  `sealed\{monthly,daily}.pkl` (2011+), `manifest.json`, `LOCK`. Prints metadata, hashes and the lock id. A rebuild
  (e.g. after file 5 is re-pulled) moves the old manifest and catalog to `work\bbg\history\` and gives a new lock id;
  unchanged files (same content and modification time) give the same lock id.
- `jobs/bbg_check_v1.py`: data check of the design tables, must-have list, sealed structure only.
- Use in later jobs: `P = bbgdata.Panel(os.environ["BBG_WORK"]); v = P.asof("2005-06-30"); v.series(sid)` (or
  `v.known(sid)` for values placed on the day they became known). Series id = `"TICKER|FIELD"` (duplicates of the same
  ticker and field in another sheet: `"TICKER|FIELD#<file>.<sheet>"`). Dates after 2010-12-31 raise `HoldoutSealed`;
  untouched markets need `Panel(..., allow_untouched=True)`; the sealed tables need the holdout key
  (`HOLDOUT_KEY_SHA256`, unset). Every refused or granted attempt goes to `work\bbg\sealed_access.log`.
- `live_sources.csv` (sheet defaults, conservative) and `untouched_markets.csv` are registered inputs: changing either
  changes the lock id. Test here: `python3 tests/bbgq_smoke.py` (mock workbooks from the real templates).

## Block 3 (WORKFLOW 0.5): re-pull reader, engine on the PC, truncation test, Bloomberg adapter (2026-11-11)
Brief: `BLOCK3_BRIEF.md`. Nothing in `gm/` was changed.

Re-pull (reader `lib/bbgdata.py` 1.1.0):
- Files named `R<n>_...` in `pulled results` are re-pull workbooks (suffixes ` 1`, `(1)`, `_CUT`, `_VALUES` are fine; with
  two candidates for one R number the newest by modification time is used, the other is named in a WARNING line).
  Their sheets `<file digit> <sheet>` belong to that original sheet. Per (file, sheet, ticker, field): a re-pulled block
  that came back ok REPLACES the first-pull block; requesting / invalid / empty leaves the first pull in place ("kept
  first"); a block only in the R file is ADDED. Ids, duplicates, live sources and held-back flags come out as if the block
  had been in the original sheet. Catalog: new columns `source` (first / R<n>), `first_pull_status`, `first_pull_first`,
  `first_pull_count`, `first_pull_n_design`, `repull_status`. First-pull copies of replaced series (design dates only):
  `work\bbg\design\replaced_first.pkl`. The R hashes are in the manifest and the lock id.
  Without R files the tables are byte-identical to 1.0.0 (only the catalog gains the new columns, so the lock id changes).
- `jobs/bbg_build_v2.py`: as v1 plus RSHEET lines (each R sheet, its original sheet, block counts) and MERGE lines per
  original sheet (re-pulled, replaced, of which the first pull had failed, added, kept first, median first valid date
  before -> after). `jobs/bbg_check_v2.py`: as v1 plus REPULL lines (replaced series vs their first-pull copy over
  common design months: months compared, months equal within 1e-6 relative; series that differ are named with counts);
  SERIES lines end with the source. The v1 jobs still work unchanged.

Engine on the PC (deploy with `python3 tools/bbgq/build_engine.py`, which fills `tools/bbgq/engine_pkg/`, git-ignored;
`engine_pkg/DEPLOY.txt` lists every file with its size and PC destination):
- `lib\gm\` = the gm package unchanged; `lib\gm_engine.py` (runner: path shim, fingerprint, comparison, truncation);
  `lib\bbg_panel.py` (Bloomberg adapter); `lib\engine_ref.json`; `lib\bbgdata.py` + the two CSVs;
  `work\free\gm_free_inputs.zip` (the 239 free files the engine opens, 9 MB; unpacked by the jobs into
  `work\free\research` and `work\free\raw`). Path shim: `gm_engine.setup(free_dir)` sets `gm.panel.RD` / `RAW` (module
  variables every gm loader reads at call time) and switches the old single-file Bloomberg reader off.
- Input compatibility: the PC has no xlrd, so the 17 binary .xls inputs (EIA futures, RBA history) ship as xlsx content
  under the same name (pandas picks the reader from the content); build_engine checks every gm read of each file gives
  an identical DataFrame (floats written exactly). Tested here in a pandas 3.1.1 / numpy 2.5.4 environment without xlrd.
- `engine_ref.py` -> `engine_ref.json` (committed): design-period fingerprint of the cloud run (BASE and CANDIDATE:
  net and gross Sharpe, mean, vol, worst drawdown 1975-2010 and 1990-2010; per-year sums of book returns; per-market
  sums of |positions|, volatility, family positions and signals; months with a return per market), gm commit and file
  hashes, config hashes, library versions, input file hashes. Re-run it (and build_engine) whenever gm/ or an input
  changes.
- `jobs/gm_repro_v1.py`: unpacks the inputs, checks the gm code and input hashes, runs the engine, compares with the
  reference. Read: one PASS/FAIL line per item with the largest absolute difference and the tolerance (book returns
  1e-8, positions 1e-6, statistics 1e-6, counts exact); the gate is the last line `REPRODUCTION PASS`.
- `engine_trunc.py` (cloud) / `jobs/gm_trunc_v1.py` (PC, ~25 min): truncation test at 8 cut dates 1980-2010. Inputs are
  cut at the loader level (gm_engine.Cut wraps gm's loader functions; no observation dated after T reaches the rules).
  Per cut and stage: end-to-end PASS/FAIL with differing market-months, max abs diff, first..last month, markets; then
  the same stage ALONE (its inputs from the full run, cut at T): a failure that disappears there is inherited.
  `cause` lines attribute every failure; `--- causes found` gives where / why / proposed fix (not applied).
- `jobs/gm_bbg_map_v1.py` (needs a bbg build in `work\bbg`): per market and engine input, the Bloomberg series id the
  adapter would serve, its status and copy, first design month, design months, months served as of 2010-12-31 and
  whether gm would use it; what stays on free data; a dry run of the adapter (counts only).
- Adapter use in a later job: `wb = bbg_panel.Source(work, asof="2010-12-31").workbook(markets=[...])`, then
  `gm_engine.run(free_dir, bbg=wb)` (or `with bbg_panel.using(wb): ...`). Market data are dated by observation month,
  economic releases by the month they became known; a series with a one-day live delay ends at 2010-11.
- Tests: `python3 tests/bbgq_smoke.py` (reader, ~17 min) and `python3 tests/bbgq_engine_smoke.py` (engine, ~12 min;
  `BBGQ_ALT_PYTHON=<python>` also runs the reproduction in another environment).

### Block 3 follow-up (bbgdata 1.2.0, 2026-11-11, after the independent check and bbg_diag_v2)
- Copied blocks: inside one workbook, blocks with the same number of fields and identical value arrays (same dates,
  values equal to 9 significant digits, at least 12 numbers) under 5 or more DIFFERENT tickers get status `copy`: not
  usable (no series id, not in the tables), catalog column `copy_group` = blocks in the group. No member is kept as
  the owner: the real series, where it is in the workbook (JYBSV1 Curncy in file 1), has a longer history than the pasted
  copies and so is not in the identical group. Alias pairs and the same ticker in two sheets stay ok. A copy in an R file
  never replaces anything; a first-pull copy is replaced by an ok re-pull, otherwise it stays unusable.
  **With the real data a build without R files now differs from bbgdata 1.0.0 by exactly the copy blocks** (the mock
  identity test checks this with a planted copy group; elsewhere tables are identical).
- Several files for one R number: no `_CUT` first, then most ok blocks (after copy detection), then most design
  observations, then newest; every candidate is a CANDIDATE line at the top of bbg_build_v2.
- A re-pull replaces the current block only if that is not ok (incl. copy) or the re-pull has at least as many design
  observations; else `repull_status` = `R<n>:shorter` (MERGE lines and SHORTER lines in the check). The same key in two R
  files: the later file wins on the same rule (warning). R sheet names are matched to file <digit>'s sheets ignoring case
  and spaces; a sheet that matches none is skipped with a warning (its blocks are not read).
- bbg_build_v2: CANDIDATE, COPYGROUP (up to 10 example tickers), COPIES per file|sheet; bbg_check_v2: COPIES per original
  sheet (first-pull copies replaced / still unusable / re-pulled copies ignored, in ticker fields), SHORTER.
- Truncation with Bloomberg inputs: `gm_engine.Cut` also wraps `gm.bloomberg.load` (months <= T);
  `jobs/gm_trunc_v1.py bbg` (or env GM_TRUNC_BBG=1) feeds the adapter's tables; the report's first and last lines say
  whether Bloomberg inputs were in the run. Cause C4: gm's "more than 24 months over the whole sample" gates.
- Live delay: every Bloomberg market sheet has a one-day live delay, so `Source(asof="2010-12-31")` does not serve the
  2010-12 month-end of those series (it becomes known on 2011-01-01); design runs with Bloomberg inputs end at 2010-11
  for them.
- engine_ref.json no longer holds hashes of the input files (they contain data after 2010); the reproduction checks the
  unpacked files against the zip's own manifest and the reference's file list and sizes. It now also hashes gm/data/*.csv
  (RBI_CALLMONEY_M.csv; a hash only).
- Keep pandas below 4 on the PC (the engine and the reference were checked on pandas 3.0.5 and 3.1.1 only).

### Engine look-ahead fixes (gm-1.2.1 / gm-2.0.1-candidate, registered in gm/CHANGES.md 2026-11-11, built 2026-11-12)
| Cause | Where | Status |
|---|---|---|
| C1 dividend proxy from all design months | gm/panel.py | FIXED: mean up to each month (> 60 overlap months), else the constant; changes 631 equity market-months |
| C2 local-rate stand-in start | gm/panel.py | FIXED: `& rl.notna().cummax()`; no design number changes |
| C3 whole-sample 500-day gate | gm/daily.py | FIXED: gate dropped; no design number changes |
| C4 whole-sample 24 / 36-month gates on Bloomberg series | gm/panel.py, signals.py, bloomberg.py, config.py | FIXED: counted up to each month; GSCI before BCOM by fixed order; inactive on free data |
Truncation test: PASS at all 8 cut dates for BASE and CANDIDATE (free data), and at 3 dates with mock Bloomberg inputs.
The reference `engine_ref.json` is for gm-1.2.1; `engine_ref_gm-1.2.0.json` keeps the old one.

