# Investor scorecard: independent code check (2026-11-18)

Reader: a separate agent that did not build the code. Read: `STAGE0_REGISTRATION.md` (all), `SCORECARD_BUILD_NOTE.md`
section 3, `eq_scorecard.py` (code sha256 a7792a0f...), `eq_reader.py`, `seal_check.py`, `seal_exempt.json`,
`make_scorecard_job.py`, `eq_scorecard_v1.json`, `tests/eq_scorecard_smoke.py`, `wrdsq.py`, the guide, plan v0.3
sections 5, 6, 8.2, `SEAL_LOG.md`, the WRDS table reports. Nothing in the repo was edited. Work folder:
`.../scratchpad/check_a/` (`pgrun.py`, `mut.py`, `nw_check.py`, `seal/attack.py`).

## 1. Verdict: FIX FIRST (5 blocking findings)

The scorecard logic itself is close to the spec: holdings timing, buy and hold, spells, weights, rank groups, rank
shares, investor substitution, score, tiers, control draw, persistence and the report form all match the
registration and the 22 readings, and the Newey-West code is right. All module SQL runs on a real Postgres with the
real column names and types (section 5). What must change before the run: the seal checker can be defeated in
several simple ways (B1), fund assets are wrong whenever CRSP codes a missing TNA as -99 (B2), the job as written can
hit the runner's 3-hour watchdog inside `build` (B3), a re-run with a corrected investor file silently uses stale
pulls (B4), and the "best-scored, no document" list can name filers the library does have documents for (B5). Each
fix changes the code hash, so `seal_exempt.json` and the lock id are set after the fixes.

## 2. Blocking findings

**B1. The seal checker does not hold (rule breach: plan 8.2, SEAL_LOG mechanism).** `seal_check.py`, `eq_reader.py`.
Every case below PASSES `seal_check.check_job` (reproduced: `seal/attack.py`; the reader cases also run at run time):
- A1/A2 `eq_reader.read(sql, 'crsp.msf_v2', cols, '2011-01', '2025-12', None, True)`: `exempt` passed by position
  (the checker only looks at keywords), in a step or in a lib module. Reads sealed months.
- A3/A4 `eq_reader.SEAL_START['us'] = 999999` or `eq_reader.TABLES.update(...)`: a subscript store or a method call
  on a reader constant is not "writing to eq_reader" for the checker. The next `read` of 2011-25 passes.
- A5/A6 `eq_reader.load_ds(load, 'eq_sc_msf_2015', 'mthret', 'us', '1900-01', '2010-12')`: the caller picks the
  date column; a float column parses as 1970-01 and every row comes back (all 2015 returns; same with `mtna` on
  `eq_sc_fret_*`). The caller also picks the region (a global data set can be read as "us").
- A7 a file `statistics.py` (or `fractions.py`) in a lib folder: `check_module` skips names in STDLIB_OK without
  looking at the lib folders, and on WRDS `~/wrdsq/lib` is first on `sys.path`, so `import statistics` runs unchecked
  code (`sys._getframe(1).f_globals['sql']`). Both names are not preloaded by the runner process.
- A9-A13 any job named `eq_scorecard_v<n>[x]` may hold any step code: `exempt=True` in reader calls,
  `eq_scorecard._load_years(load, 'eq_sc_msf', [2015])` then printing it, `f = eq_scorecard.stock_returns(load)`
  (an identity function hands back `load`), or `out(eq_scorecard.build(...)['M'].to_string())` (build returns the
  monthly book returns, the panel and the holdings tables). The registered output form is not enforced.
- A8 a job whose name does not start with `eq_` is not checked at all (it can `load('eq_sc_msf_2015')`; the older
  `tri_*`/`bio_*` data sets on WRDS also hold 2011+ data).

Minimal fix (all in the reader and checker; lock id changes):
```python
# eq_reader.py: exempt keyword-only, constants frozen, stored data sets declared like tables
import types
TABLES = types.MappingProxyType({...}); SEAL_START = types.MappingProxyType({"us": 201101, "nonus": 199001})
DATASETS = types.MappingProxyType({"eq_sc_msf_": ("yyyymm", "us"), "eq_sc_fret_": ("caldt", "us"), ...})
def read(sql, table, cols, lo, hi, where=None, *, exempt=False): ...
def load_ds(load, name, lo, hi, *, exempt=False):      # date column and region come from DATASETS, not the caller
    ...; refuse if the column is not datetime-parseable for every row or not an int yyyymm in 190001..210012
# seal_check.py
READER_FUNCS = {"read", "load_ds", "SealError"}         # no access to TABLES / SEAL_START / SEAL_END / sealed
# check_module: if mod in STDLIB_OK and find_module(mod, libs): err("lib folder shadows %s" % mod)
#   and at start of check_job: refuse if any lib folder holds a file named like a STDLIB_OK module
# exempt job: every python step must match one registered template, and eq_reader may not be imported:
STEP_RE = re.compile(r"^import eq_scorecard\neq_scorecard\.(pull_base|pull_crsp|pull_agg|pull_hold|pull_funds|"
                     r"build|report)\(((sql|load|save|out|DATA|\d+|budget=\d+)(, )?)+\)$")
# check every job, whatever its name: a non-exempt job that names an eq_sc_ data set or imports eq_scorecard is refused
```
and make `build` return `None` (keep the tables inside the module) and drop `stock_returns` (it is an identity).
Add A1-A13 as seal tests S14+ in the smoke test.

**B2. Fund assets include CRSP's missing code -99 (wrong rank group, section 5 assets floor).** `_fund_months` /
`_combine`: weights drop TNA <= 0, but `t = f[np.isfinite(f.mtna)].groupby(...).mtna.sum()` adds -99 for every
class-month with missing TNA. Reproduced on invented data: one $20M class plus a class reporting -99 gives mean assets
-79, so the fund leaves the rank group; any portfolio with such a class has its assets understated by 99 per class.
Library fund investors combine several portfolios, so they are hit too. Fix, first lines of `_fund_months`:
```python
f["mtna"] = pd.to_numeric(f.mtna, errors="coerce").where(lambda s: s > 0)     # CRSP -99 = missing
f["mret"] = pd.to_numeric(f.mret, errors="coerce").where(lambda s: s >= -1)   # guard against any missing code
```
Add a -99 class to the smoke world (fund 5002 in a few months) and check fund 5001+5002 assets.

**B3. The job can be killed inside `build` (failed run = second opening of the seal).** `make_scorecard_job.job()`
puts five pulls (budgets 1,200 + 1,500 + 3,600 + 1,800 + 1,200 s = 2.6 h, plus overrun because the budget is only
checked before each data set) and `build` (est. 15-40 min) in one job; the PC runner's watchdog stops any job after
3 hours. If `build` has started, the run counts as an opening (build note section 4) and returns nothing. Fix: two
jobs. `eq_scorecard_v1` = the five pulls + `datasets`, re-run as `v1b`, `v1c` until each pull prints "complete";
then `eq_scorecard_v2` = `build` + `report` steps only. In `build`, print the elapsed time after each stage.

**B4. A re-run with a corrected investor file uses stale pulls without noticing.** Plan 5.4 lets the investor list
and filer ids change between runs. `pull_hold` writes `eq_sc_cand` once and `pull_funds` filters on the library
fundnos at pull time; both are skipped on a re-run because the data sets exist. A filer or fund added to the frozen
file then has no holdings or no extra share classes, and `build` produces a missing or wrong row with no warning.
Fix (reasoned):
```python
# pull_hold: step("eq_sc_cand", lambda: pd.DataFrame({"mgrno": candidates(load)}).assign(input=input_sha()))
# pull_funds: save("eq_sc_fmeta", pd.DataFrame({"input": [input_sha()]})) after the last fret year
# build, after the presence check:
if load("eq_sc_cand").input.iloc[0] != input_sha() or load("eq_sc_fmeta").input.iloc[0] != input_sha():
    out("build: pulls were made for another investor input; delete eq_sc_cand, eq_sc_hold_*, eq_sc_fret_*, "
        "eq_sc_fmeta and pull again"); return None
```

**B5. "Best-scored filers without a library document" can list filers with documents (section 8 breach).**
`_results`: `libm = set(_lib_mgrnos())` takes mgrnos of `record_kind == "13f"` rows only, and the frozen file carries
no mgrno for fund-ranked investors. Concrete case: I010 Greenblatt is ranked on his funds and his row says "Gotham
Asset Management is the filer"; Gotham can appear in the list. Fix: phase A2 writes the matched filer ids of
fund-ranked investors into `mgrnos` (the generator already accepts them; `_books` and `candidates` use 13f rows
only), and the exclusion uses every id in the file:
```python
libm = {int(m) for p in INV for m in p.get("mgrnos", [])}
libg = set(hdr[hdr.crsp_fundno.isin([int(f) for p in INV for f in p.get("fundnos", [])])].gid)
```

## 3. Non-blocking findings
1. Bridging depends on the future (gap 4): months 4-6 after a filing count only if the filer files again two
   quarters later. Forced by registration 3.5; a small survivorship tilt. Say so in the spec text.
2. Late first versions: `fdate = rdate` cannot show filings made after the 45-day deadline, which still enter at
   the deadline (look-ahead the data cannot measure). Before the run, a structure count (allowed on sealed months)
   of (mgrno, rdate) pairs whose first fdate is after rdate shows how many quarters the rule turns into gaps.
3. Peer universe (gap 8) is EQTY/COM/NS without `usincflg = 'Y'` and `issuertype in ('ACOR','CORP')`, so it holds
   foreign-incorporated and REIT/trust common shares (CRSP's map of share codes 10/11 uses both). Decide before
   REGISTERED; if changed, also change the smoke reference `ref_groups`.
4. `_bm_table` keeps the largest `bm` when firm_ratio has several rows for one permno and date. Prefer dropping
   permno-years whose latest date has more than one distinct `bm`, and print that count.
5. `pull_funds` takes classes that ever had an ED code; classes of the same portfolio without a style row are not
   pulled, so the combination by assets misses them. Pull by class group / portfolio of ED classes.
6. Library fund investors with several funds are combined by assets into one series (I008 Davis 3 funds, I010
   Greenblatt 3 incl. an absolute-return fund, I036 Nygren 2, I095 Wood 3) and ranked if any of their groups is in
   the pool. Not in the 22 readings: add it, or rank on the largest ED fund only.
7. `fund_hdr` is the current header (index flag, class group): a classification look-ahead, not a return one.
   `crsp.fund_hdr_hist` exists if wanted. Document in gap 13.
8. Read range: the job reads `msf_v2` from 2009-06, factors from 2009-01 and firm_ratio from 2010-01, outside
   registration section 1 "2010-06 to the seal end". Design months, not sealed; amend the table text.
9. No run-time code hash: the report prints the input hash but not the hash of the code that actually ran. The
   module may read its own source (`__file__`; it is not AST-scanned) and print `code_hash` in the report header,
   so SEAL_LOG B records what ran on WRDS, not what was checked locally (two lib folders feed `~/wrdsq/lib`).
10. Non-atomic saves: a job stopped while writing leaves a truncated `.csv.gz` that `have()` treats as done;
    `build` then fails loudly. Write `name + "_tmp"` and `os.replace` it (the module may import `os`).
11. Any SQL error prints the SQL in the traceback, including the IN list of ~4-7k candidate mgrnos (identifiers,
    and enough to fill the 60,000-character cap). Wrap each `step` in try/except printing the exception class and
    the first 200 characters before "[SQL:".
12. Section 8 asks for one row per matched investor; an investor whose filer has no matched filing gets no `INV`
    line. Print it with months 0.
13. Gap 17 text is stale: the frozen file now has a `role` column (the code reads it).
14. Memory: `_books` holds P, the shifted copy, the outer merge for turnover and the new-position merge at once
    (tens of millions of rows). Compute turnover and new positions per quarter inside the quarter loop and `del`.
15. Two rdates of one manager in one calendar quarter would be summed into one filing (`groupby q`). Print the count
    of non-quarter-end rdates (expected 0) or keep the latest rdate per (mgrno, quarter).
16. `delete` steps pass in equity jobs, so any `eq_` job can remove the scorecard's stored data sets.
17. Tests. Extra mutations run against the smoke checks (`mut.py`); NOT caught: factors one month late in the
    regression; peer-group returns equal-weighted; peer-group weights from the same month; turnover not halved;
    score part (iii) dropped; tier ties by fewer documents; statistics printed from 48 months; result from 24
    months; rank group up to 250 positions; value floor $50M; top-10 not renormalised; a missing return counted
    as -100%; best list including library filers; persistence fifths of block 2 over all filers (14 of 18). Rules
    with no test: DGTW group returns, factor alignment, turnover, score part (iii), tie-breaks, the 36/60 thresholds,
    rank-group bounds, -99 TNA, multi-fund investors, the 60-month print rule. Weak: C05b (`>= 1` filer in the
    stopped column, not filer 2), C15 and C19 recompute with the code's own formula, C18 (a range), C20 (`> 40`).
    The seal tests miss A1-A13.
18. The runner on WRDS reports v1.0.7; the repo holds `wrdsq.py` 1.0.5. I read 1.0.5.

## 4. Seal checker: what I tried
| Attempt | Checker | Reads sealed data at run time |
|---|---|---|
| A1 `exempt` by position, in a step | PASS | yes (reader returns rows) |
| A2 same, inside a lib module | PASS | yes |
| A3 `eq_reader.SEAL_START['us'] = 999999` | PASS | yes |
| A4 `eq_reader.TABLES.update(...)` | PASS | yes (re-declares a table) |
| A5 `load_ds(..., 'mthret', 'us', '1900-01', '2010-12')` on `eq_sc_msf_2015` | PASS | yes, all rows |
| A6 same with `mtna` on `eq_sc_fret_2015` | PASS | yes, all rows |
| A7 `statistics.py` in the lib folder | PASS | yes (unscanned code) |
| A8 job named `tri_peek` with `load('eq_sc_msf_2015')` | PASS (not checked) | yes |
| A9 `eq_scorecard_v7` with `eq_reader.read(..., exempt=True)` | PASS | yes |
| A10 `eq_scorecard_v8` printing `eq_scorecard._load_years(load, ...)` | PASS | yes |
| A11 `eq_scorecard.stock_returns(load)` used as `load` | PASS | yes |
| A12 printing the return value of `build` | PASS | yes |
| A13 `eq_scorecard.stock_returns(sql)('select ...')` | PASS | yes |
| A14 `delete` of `eq_sc_hold_2015` in an `eq_` job | PASS | no (integrity only) |
Refused, as they should be: direct `sql`/`load` names (also aliased), `open`/`getattr`/`__import__`, `importlib`,
`os`, `**kwargs`, keyword `exempt=` outside exempt jobs, `from eq_scorecard import`, pull/export steps, a lib module
that uses `sql` directly, a changed module (hash), code in the input block. `read` itself is sound against injected
`where` clauses because rows outside the months are refused after the fetch.

## 5. Verified, and what I could not verify without WRDS
Verified here: Newey-West equals a loop computation (alpha 0.005000, t 1.4622 on an autocorrelated example; same
form as `qs/btstats.ols_nw`). Every module query (`pull_base`, `pull_crsp`, `AGG_SQL`, `pull_hold`, `pull_funds`
with the library-class clause) ran on a local PostgreSQL 16 with tables built from the real column names and types
and the smoke world, through SQLAlchemy 2.1 `text()` + psycopg2 as `wrdsq._sql` does (`::float8` casts and `like
'ED%'` work); the SQL aggregate equals the independent aggregate in all 16 years; the built report equals the
fake-sql report except 2 alphas changed in the second decimal by NUMERIC(10,6) rounding. The smoke suite passes
(pandas 3.0.5, Python 3.13).
Not verifiable here:
- Whether `msf_v2.mthret` holds the delisting return in the delisting month and how often it is NULL there. Check
  on design months: 2001-2010 delistings in `crsp.stkdelists` with non-null `delret` against `msf_v2` rows with
  `mthdelflg` set and non-null `mthret` (counts only).
- How many s34 quarters have no `fdate = rdate` rows (finding 2); whether s34 holds repeated rows per (mgrno, rdate,
  cusip, fdate) (they are summed); whether every rdate is a quarter-end (finding 15).
- That `ff.fivefactors_monthly` is in decimals (NUMERIC(8,6) suggests so; the triage jobs used it the same way).
- Memory and time of `build` on a compute node (est. 3-6 GB, 15-40 min); qrsh time limits.
- That `~/wrdsq/lib` on WRDS holds exactly the checked `eq_scorecard.py` and `eq_reader.py` (finding 9).
- How many CRSP fund class-months carry TNA -99 after 2010 (B2 is a defect whatever the count).

## 6. Effort
About 2.5 hours of agent time: reading ~3,400 lines, a local PostgreSQL run of all queries, 18 extra mutations,
14 checker attacks, the Newey-West re-derivation, and this note.
