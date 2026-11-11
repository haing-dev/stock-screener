# Block 2 build brief (WORKFLOW v2.1 steps 0.2-0.4): reader, data check, lock and seal

Repo: /home/claude/stock-screener (work on main; do not push, the orchestrator commits). Read first:
`docs/research/WORKFLOW.md` (sections 2, 4 phase 0, 5), `tools/bbgq/README.md` (how jobs run on the PC and the export
whitelist), `tools/bbgq/jobs/bbg_inventory_v2.py` (working example of a job and of the workbook layout),
`tools/bbgq/results/bbg_inventory_v2.txt` (REAL metadata of the pulled files: every sheet, ticker, field, row count,
fill %, failures), `docs/data_requests/build_bloomberg_v5.py` + `docs/data_requests/bloomberg_v5/bloomberg_v5_tickers.csv`
(files 2-7: label, ticker, fields, periodicity), `docs/data_requests/build_bloomberg.py` (file 1), `gm/bloomberg.py`
(the old single-file reader and the tickers the engine needs), `gm/panel.py` (the 62 markets of the current book).

## Situation
Seven Bloomberg workbooks sit on the user's Windows PC. They must never leave it. You cannot see them: you build and
test here against mock workbooks, the orchestrator then runs your jobs on the PC and reads only the printed report.
PC: Python 3.15, numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, openpyxl 3.1.5 in `local\pylib`; NO pyarrow. A job is one
.py file run with cwd = `Documents\WRDS results\local`, env `BBG_DIR` (workbooks), `BBG_WORK` (= local\work, derived
data stays there), PYTHONPATH = local\lib;local\pylib. Start every job with
`sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]`.
Facts from the inventory: file names carry suffixes ("1_Bloomberg_macro_UBC_6 1.xlsx", "2_... (1).xlsx"), so match
files by their leading digit; each data sheet is blocks side by side (row 2 label, row 3 ticker, row 4 "date" then
field names, row 5+ dates and values; a block is n_fields + 2 columns wide); a "Check" and a "Read me" sheet must be
skipped; monthly sheets have 683 dated rows from 1969-12-31 with blanks before a series starts; daily sheets have
9,613-13,458 rows from 1990; dates may be datetimes or Excel serial numbers; cells can hold strings such as
"#N/A N/A", "#N/A Invalid Security", "#N/A Requesting Data..."; some fields are not prices (file 2: ECO_RELEASE_DT is
a date, ACTUAL_RELEASE, BN_SURVEY_MEDIAN); the same ticker can appear in several sheets or files on purpose.
2,017 of 2,470 tickers loaded; file 5 will be re-pulled later, so a rebuild must be a clean, versioned re-run.

## Deliverables (all under tools/bbgq/)
1. `lib/bbgdata.py`: the only code that touches the workbooks and the derived tables.
   - `build(bbg_dir, work_dir)`: read every workbook once (openpyxl read-only, values) -> a catalog (one row per
     file / sheet / ticker / field: label, periodicity, kind of field (price-like, rate-like, date, other), status
     ok / requesting / invalid / empty, first and last valid date, count, the series id it is stored under,
     duplicate-of, live_source, live_delay_days, untouched flag) and two tables per periodicity, split at 2010-12-31:
     `work\bbg\design\{monthly,daily}.pkl` (dates <= 2010-12-31) and `work\bbg\sealed\{monthly,daily}.pkl` (later
     dates). Month-end index for monthly, business-day index for daily. Pickle with pandas (no pyarrow).
     Write `work\bbg\manifest.json`: sha256, size and mtime of each raw workbook; sha256 of each table and of the
     catalog; counts; code version; build time. The lock id is the sha256 of the manifest with the build time removed.
   - Live source tags: a sheet-level default from `tools/bbgq/live_sources.csv` that you write (columns: file digit,
     sheet, live_source in {free_daily, official_release, bloomberg_only}, live_delay_days, note). Economic series
     with an ECO_RELEASE_DT field use the actual release date instead of a fixed delay. Be conservative: when unsure,
     bloomberg_only.
   - Untouched markets: a named list `tools/bbgq/untouched_markets.csv` (file digit, sheet, ticker, label, reason).
     Rule: tradable markets of a type the current book already trades (commodity futures, currencies, government
     bond yields, equity indices) that are NOT among the 62 markets in gm/panel.py and are not needed as a new
     instrument type by the planned pods (short-rate futures, swaps, forwards and vol on existing currencies, credit
     and economic series are NOT untouched). Aim for a set of a few dozen: the alternative commodities
     (gm/bloomberg.py ALT_COMMOD), emerging-market currencies and emerging-market bond yields the book does not
     trade. List what you chose and why; the orchestrator reviews it before the lock.
   - Access: `Panel(work_dir)` loads DESIGN tables only. `panel.asof(date)` returns an object whose every getter
     returns data dated <= date and, per series, shifted by its live delay (release date for economic series), so
     nothing later than what was knowable on `date` can come out; asking for a date after 2010-12-31 raises
     `HoldoutSealed`. Untouched series are invisible unless `Panel(..., allow_untouched=True)`. The sealed tables can
     only be opened by `Panel(..., holdout_key=...)` when sha256(key) equals the module constant
     `HOLDOUT_KEY_SHA256` (None for now, so it always refuses); every attempt is appended to
     `work\bbg\sealed_access.log`.
2. `jobs/bbg_build_v1.py`: calls build and prints metadata only: per file and sheet the counts by status, tables'
   shapes, per field name the share of numeric / date / string cells (so field types can be verified blind), the
   catalog counts by kind, live source and untouched, every hash and the lock id. Ends with "=== END ===".
3. `jobs/bbg_check_v1.py`: the data check on the DESIGN tables (dates <= 2010-12-31): per series first / last valid
   date and count; gaps inside the valid range; stale runs; jumps (robust, MAD-based, on log changes for price-like
   and on differences for rate-like series); non-positive values in price-like series; duplicates that disagree
   across sheets or files; series with fewer than 120 design months (or 1,250 design days). Thresholds are constants
   at the top of the file with a one-line reason each. Then a must-have check: every ticker that gm/bloomberg.py
   and the Batch 2 plan in docs/research/global_macro/TESTING_PROTOCOL.md need is present and usable. For the SEALED
   tables print structure only: shape, per sheet the count of series with any value after 2010 and the last date.
   Output: per sheet a line of counts by flag, then the flagged tickers with their flag codes. No data values, no
   per-date lines, nothing computed from prices after 2010-12-31.
4. `tests/bbgq_smoke.py` (repo root tests/): builds mock workbooks in a temp dir from the real templates
   (`docs/data_requests/bloomberg_v5/*.xlsx` and `docs/data_requests/Bloomberg_macro_UBC.xlsx`, same sheet and block
   layout, real tickers and fields, random-walk values, some blocks with error strings, serial dates in one sheet,
   one requesting block, dates through 2026) with the awkward real file names, then runs both jobs as subprocesses
   the way the PC runner does and asserts: all blocks catalogued; design tables end <= 2010-12-31 and sealed start
   after; `asof(d)` never returns a later date (property test over random dates, including the release-date rule);
   `HoldoutSealed` is raised and logged; untouched series are hidden by default; a second build on unchanged files
   gives the same lock id; job output passes a whitelist scan (no line that looks like a dated data row; no number
   from the mock data values appears in the output). Print "BBGQ SMOKE OK".

## Rules
- Reports obey the export whitelist in tools/bbgq/README.md. When in doubt, print a count, not a value.
- Jobs must not crash on one bad sheet: catch, report, continue. Aim for under 15 minutes on about 60 MB of xlsx.
- Keep it simple and readable: a non-coder's project, reviewed by a second agent later. No new dependencies.
- Do not touch gm/ in this block. Do not read or write anything outside tools/bbgq/ and tests/bbgq_smoke.py.
Reply with: files written, the smoke test result, the untouched list in one paragraph (count by type), every
assumption you had to make about the real files that the first PC run should confirm, and anything you could not do.
