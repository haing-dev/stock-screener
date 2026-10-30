# WRDS automation: guide for a new chat or project

Read this before any WRDS work. The setup is already done (Oct 2026). Don't redo it, and don't ask the user for a
password.

## 1. What is already in place
| Piece | Where | What it does |
|---|---|---|
| WRDS account | username `ttdlisa` (UBC) | Subscription list: see section 8 |
| Job runner on WRDS Cloud | `~/wrdsq/wrdsq.py` (v1.0.5) | Runs a JSON job on a WRDS compute node (falls back to the batch queue, then the login node for light jobs); stores data in `~/wrdsq/data`; prints metadata and results only |
| Windows runner on the user's PC | scheduled task "WRDS runner" -> `Documents\WRDS results\wrds_watch.ps1` | Every 10 minutes: sends new job files to WRDS, saves the reports, retries when WRDS is busy, 3-hour watchdog |
| Saved login | `C:\Users\admin\.wrds\secret.txt` (Windows DPAPI) + `askpass.cmd/.ps1` | Answers the ssh password prompt. Only that Windows user on that PC can decrypt it. Claude never sees it |
| Shared folder | `C:\Users\admin\Documents\WRDS results` | The only place Claude reads and writes (device bridge) |
| Source code | GitHub `haing-dev/stock-screener`, `tools/wrdsq/` (wrdsq.py, runner/, lib/, jobs/, mkjob.py) | Version history of everything above |

Folder layout on the PC:
```
Documents\WRDS results\
  jobs\            <- Claude drops job JSON files here (runner picks them up)
  jobs\done\       <- finished jobs (moved by the runner)
  lib\             <- Python modules Claude writes; the runner copies them to ~/wrdsq/lib on WRDS each round
  results\         <- <job>.txt (report) and <job>.progress.txt (runner progress / errors)
  wrdsq.py         <- runner program; the runner copies it to WRDS each round (update = overwrite this file)
  runner_status.txt, runner_log.txt
```

## 2. Hard rules
1. **WRDS AI policy**: "loading Data retrieved from WRDS into LLMs and other Generative A.I. tools is prohibited".
   - Never bring data rows back.
   - Reports may contain only:
     - metadata: library, table and column names, row counts, date ranges;
     - results: test statistics, Sharpe ratios, coefficients, counts, rankings of a handful of names.
   - Never call `.head()`, never print DataFrames of values, never print per-date or per-firm series.
   - Data stays in `~/wrdsq/data` on WRDS.
2. **Credentials**:
   - Never ask for or handle the WRDS password, and never put credentials in GitHub, chat or the shared folder.
   - If the login fails, the runner writes `LOGIN FAILED` in `runner_status.txt`. Ask the user to run one
     `ssh ttdlisa@wrds-cloud.wharton.upenn.edu` in PowerShell (and approve Duo if asked), or to redo the
     password-saving step if they changed the password.
3. **Licence**: academic, non-commercial research and paper trading only.
4. **The user does not code.**
   - Don't give terminal steps when the runner can do it.
   - If a manual step is unavoidable, give exactly one PowerShell line to paste.
   - Never use .bat or .ps1 files that need double-clicking: Windows blocks them.
5. **Storage**: 10 GB home quota (pulls are refused above 90%).
   - Aggregate in SQL.
   - Select only the columns you need.
   - Delete datasets you no longer need (`delete` step).

## 3. Workflow for any project
1. **Check the runner is alive.**
   - Read `runner_status.txt` and `runner_log.txt`: list the folder with `device_list_dir`, then stage the files with
     `device_stage_files`.
   - `idle, last check <time>` within the last ~15 minutes means it's alive.
2. **Explore (metadata job).** Steps `libraries`, `tables`, `search`, `describe`. Mark the job `"head_ok": true`
   (light).
3. **Pull and aggregate (pull steps).** Aggregate in SQL to the level the research needs, for example
   country x month or industry x month.
4. **Analyse (python steps, or a module in `lib\`).**
   - Print statistics only.
   - Put long code in a module `lib\<project>.py`.
   - Call it from a short python step: `import <project>\n<project>.run(load, out, sql=sql)`.
5. **Write the job.** Write the job JSON to `jobs\<name>.json` via `device_commit_files`.
   - Write module files **first**, then the job.
   - Use a new job name each time (`<project>_v2`, `_v3`, ...). The report is written to `results\<name>.txt`.
6. **Schedule a check-back.** Use `send_later`, 15-20 minutes for small jobs. Then read `results\<name>.txt`
   (and `.progress.txt` if the report is empty).
7. **Commit your job and lib files** to the GitHub repo (`tools/wrdsq/jobs`, `tools/wrdsq/lib`) so they are
   versioned.

## 4. Job format
```json
{"name": "proj_explore", "head_ok": true, "steps": [
  {"do": "libraries"},
  {"do": "tables", "libraries": ["crsp", "comp"]},
  {"do": "search", "terms": ["dividend yield", "statsum"], "libraries": ["comp", "ibes"]},
  {"do": "describe", "table": "crsp.msf", "date": "date"},
  {"do": "pull", "name": "my_agg", "date": "m", "sql": "select ... group by ..."},
  {"do": "python", "code": "d = load('my_agg'); out('rows', len(d), 'Sharpe %.2f' % 0.5)"},
  {"do": "datasets"}, {"do": "delete", "names": ["old"]}, {"do": "export", "names": ["x"]}]}
```

| Step | Use |
|---|---|
| `libraries` / `tables` / `search` / `describe` | Metadata only. `search` matches table and column names |
| `pull` | Runs SQL and saves `~/wrdsq/data/<name>.csv.gz`. The report shows only rows, columns, size and date range |
| `python` | Helpers available: `sql(q)` returns a DataFrame from WRDS (the literal `%` is fine); `load(name)` and `save(name, df)`; `out(...)` prints; `db`, `pd`, `np`, `DATA`, `LIB`. `~/wrdsq/lib` is importable. Output is capped at 60k characters; errors come back as tracebacks |
| `export` | Copies files for the **user** to download to their own PC (never to the chat) |
| `"head_ok": true` | Lets aggregate SQL plus light pandas run on the login node when no compute node is free. Don't use it for heavy pulls of raw rows |

## 5. Gotchas learned the hard way
- **device_commit_files caching.** A reused staged path can upload stale content. Always stage under a **new file
  name** (e.g. `/mnt/user-data/outputs/<file>_v7.py`), commit with `force: true`, then check the size on the device
  with `device_list_dir`.
- **Large tables.** Big stock-level tables are slow, e.g. `contrib_global_factor.global_factor` (444 columns). Filter
  hard (country list, `eom >= ...`, `size_grp in ('mega','large','small')`) and aggregate in SQL.
- **Restricted tables.** Some appear in listings but are blocked (no subscription):
  - `ibes.glcountry`, `ibes.igactry*` (I/B/E/S Global Aggregates and Guidance);
  - Datastream, OptionMetrics and Markit (only samples).

  Check access with a `describe` or `limit 1` before designing around a table.
- **I/B/E/S country codes.** Map them by estimate currency: pre-1999 currencies separate the euro countries; `BPN`
  = GBP; Brazil `LB` reports in USD. The implementation is `lib/gm_country.py::_ibes_map`.
- **Stale or local-currency sources.**
  - `macrofin.macro_uncertainty` stops in 2019.
  - `wrdsapps_windices` returns are local currency and miss the US and Canada.
  - Global Factor Data (JKP) ends at the last December. CRSP is an annual update.
- **Outliers.** Check the largest single-month value before trusting results: a 419% country-month came from one bad
  stock return.
- **Report encoding.** `.progress.txt` is UTF-16 (PowerShell); decode it with `iconv -f utf-16`.

## 6. Updating the runner
- **WRDS-side program:** edit `tools/wrdsq/wrdsq.py`, bump `VERSION`, commit, and write it to
  `Documents\WRDS results\wrdsq.py` (fresh staged name). The runner copies it to WRDS on its next round.
- **Windows runner:** edit `tools/wrdsq/runner/wrds_watch.ps1` and write it to the folder. The scheduled task runs the
  new file on its next round. The task itself never needs re-registering.
- **To stop automation** (user, PowerShell): `Unregister-ScheduledTask -TaskName "WRDS runner" -Confirm:$false`.

## 7. If something breaks
| Symptom | Cause / fix |
|---|---|
| `runner_status.txt` says `LOGIN FAILED` | Password changed or Duo needed. The user logs in once in PowerShell, or redoes the saved-password line (in the repo history: `tools/wrdsq/runner/askpass.ps1` notes) |
| Report says `no WRDS compute node was available` | WRDS is busy; the runner retries automatically every 10 minutes |
| Report empty / missing `=== END` | Check `.progress.txt`. The runner retries twice, then gives up |
| Status stuck on `running ...` for more than 3 hours | The watchdog stops it on the next round |
| Status unchanged for many hours | PC off or user signed out (the task runs only while signed in) |

## 8. Subscription (Oct 2026, subscribed, excluding samples)
- **Compustat:** North America and Global (daily updates); Bank, Execucomp, Segments.
- **CRSP** (annual update): stock, indexes, CCM, Treasuries, mutual funds.
- **LSEG:** I/B/E/S estimates (US + international summary/detail), 13F, mutual fund holdings.
- **Other market and macro data:** TRACE; Cboe VIX data; FRB rates and FX; Fama-French; Dow Jones; Penn World Tables;
  Macro Finance Society.
- **Contributed:** Global Factor Data (JKP), characteristic returns, others.
- **WRDS apps:** World Indices, Beta Suite, Financial Ratios, Event Studies, Backtest Basic, linking tables.
- **Not subscribed:** Datastream, OptionMetrics, Markit, MSCI, FactSet, TAQ, Worldscope, Bond Returns by WRDS,
  I/B/E/S Global Aggregates.
