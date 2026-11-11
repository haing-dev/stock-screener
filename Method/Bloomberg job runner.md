---
tags: [method, spec]
file: /home/claude/stock-screener/tools/bbgq/README.md
---
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
