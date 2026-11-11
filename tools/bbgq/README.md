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
