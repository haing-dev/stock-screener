# Investor scorecard: build note (2026-11-18, revised after the code check)

The code is built to the binding spec, `STAGE0_REGISTRATION.md` sections 2-9, 11 and 12. The readings in section 3
are registration section 12. This revision applies the code check `SCORECARD_CODE_CHECK.md`: all five blocking
findings and every non-blocking finding that can change a number or leak (section 5). Nothing has run on WRDS yet.

## 1. Files
| File | What it is |
|---|---|
| `tools/equity/wrds/eq_scorecard.py` | The seal-exempt WRDS lib module. The frozen investor table and the document list sit between the `FROZEN INPUT` markers |
| `tools/equity/make_scorecard_job.py` | Reads `inventory/frozen_investors.csv` and `inventory/inventory.csv`, rewrites only the input block, and writes the two job files |
| `tools/wrdsq/jobs/eq_sc_pull_v1.json` | The pulls. Re-run as `eq_sc_pull_v1b`, `v1c`, ... until `pull_status` prints `ALL PULLS COMPLETE`. A `delete` step of `eq_sc_*` data sets is allowed here (for a re-pull after an input change) |
| `tools/wrdsq/jobs/eq_scorecard_v1.json` | Build plus 4 report steps. `build` refuses to start unless every pull is complete and the stored pull key matches |
| `tools/equity/wrds/eq_reader.py` | The seal reader. Table and data-set constants are read-only. `exempt` is keyword-only. Stored data sets are declared with their own date column. `count()` returns row counts by year and is allowed on sealed months |
| `tools/equity/seal_check.py` | The pre-send checker (rules in its docstring). Prints PASS or REFUSED and the lock id |
| `tools/equity/seal_exempt.json` | The registered scorecard job: its module, code hash, two name patterns and the functions each pattern may call |
| `tools/equity/wrds/eq_precheck.py`, `tools/wrdsq/jobs/eq_precheck_v1.json` | Pre-run structure checks, run as a non-exempt job (section 6) |
| `tests/eq_scorecard_smoke.py` | Invented data. 39 scorecard checks and 32 seal checks. Mutations: the 6 planted errors of section 11 and the code check's 14 extra mutations |

## 2. Functions (module)
| Function | Does |
|---|---|
| `pull_base` | Pulls `tfn.s34names`, the `stocknames_v2` CUSIP map, the factors, the `firm_ratio` book-to-market (Jan-Jun 2010-25), `fund_hdr` and `fund_style` |
| `pull_crsp` | Pulls `crsp.msf_v2`, all securities, 2009-06..2025-12, one data set per year |
| `pull_agg` | Runs one SQL aggregate per year: matched positions, matched value and filed value per filer and quarter |
| `candidates` / `pull_hold` | A loose pre-filter: median positions 3-200, median value at least $75M, at least 30 months. Library 13F filers are always kept. Then the holdings rows per year. `eq_sc_cand` stores the pull key |
| `pull_funds` | Pulls every share class of every fund (class group, else portfolio) that has a class ever coded ED, and of every library fund. `eq_sc_fmeta` stores the pull key |
| `pull_status` | Prints `ALL PULLS COMPLETE`, or what is missing or stale |
| `Panel`, `Peers` | The CRSP arrays and the DGTW groups: formed in June, held July-June, value-weighted by the previous month-end value |
| `_positions` | Matches holdings: CUSIP valid at the quarter-end, CRSP price at the quarter-end. One filing per manager and quarter (the latest report date) |
| `_schedule`, `_hold`, `_books` | Handle holding months, the missed-quarter rule, buy and hold, the variants and the library books. Turnover and new positions are computed quarter by quarter |
| `_book_windows`, `_fund_windows`, `_stats`, `ols_nw` | Compute window statistics, the rank-group tests and the Newey-West alpha |
| `_results`, `_tiers`, `_persist` | Compute rank shares, scores, tiers, best-scored lists, persistence and counts |
| `build` / `report` | `build` prints the elapsed time after each stage, keeps its tables inside the module, saves only the report lines and returns nothing. On any error it prints only the exception class and the module line. `report` prints one part of under 55,000 characters |

## 3. Readings where the spec left room (registration section 12)
1. **Investor rank share.** The investor's alpha over its frozen months replaces its own filers or funds in the window's rank group. Share = (number below + half the number equal) / (group size − 1). It exists only if one of its filers or funds is a member of that group.
2. **A window's filings.** The filings whose holding months, cut to the frozen months, fall in the window.
3. **Empty filing.** A filing with no position matched to a CRSP price counts as a missed quarter.
4. **Missed quarters (registration 3.5, replaces the first reading).** If the next quarter's filing is missing, the last portfolio is held three more months (six in all, one buy-and-hold period), whether or not the filer files again. If the quarter after is missing too, the spell ends. A filer that stops therefore has its last portfolio held 3 + 3 months.
5. **Entry weights.** Quarter-end weights are the weights at entry.
6. **Matched security.** Any `msf_v2` security with a price in the quarter-end month counts as matched. The CUSIP comes from the `stocknames_v2` row valid at the quarter-end, ties to the lowest permno. A row's filed value uses the 13F price (0 if missing). Two report dates of one manager in one calendar quarter: the latest is kept. The build log counts report dates that are not quarter-ends.
7. **Peer-adjusted return.** A holding with no return that month is left out, with weights rescaled. Annualised as mean × 12. Coverage shares are means.
8. **DGTW details.**
   - Universe: CRSP common shares (EQTY/COM/NS) on NYSE, NYSE American or Nasdaq at the end of June. Foreign-incorporated and REIT/trust common shares stay in, as registered; the report header states this.
   - Book-to-market: the latest `firm_ratio` row dated January-June of the formation year, which must be > 0. If that date carries two different values, the stock has no book-to-market that year; the build log prints the count.
   - Momentum needs all twelve returns. NYSE breakpoints use the NYSE stocks of the universe. Book-to-market and momentum fifths are taken over all stocks of the cell, ties by permno.
9. **Market.** Fama-French market excess return + T-bill.
10. **Years ahead of the market.** Only calendar years with all twelve months count.
11. **Turnover and medians.**
   - Turnover uses only pairs of filings exactly one quarter apart, both in the window: half the sum of absolute weight changes, averaged, × 4.
   - The ten-largest weight is the sum of the ten largest weights of each filing; medians are taken over the window's filings.
12. **New positions.** Measured against the filing exactly one quarter earlier; otherwise that quarter has no months in the variant.
13. **Funds.**
   - Share classes are grouped by the current `fund_hdr`: crsp_cl_grp, else crsp_portno, else the class alone. This is a classification look-ahead, not a return one; `fund_hdr_hist` was not used.
   - Each frozen fundno stands for every class of its group.
   - A class's weight is its TNA at the previous month-end. TNA ≤ 0 (CRSP −99) and returns < −1 count as missing.
   - "ED" means every record month in the window has a class with an objective code starting ED in force.
   - Index: any class with a non-empty index_fund_flag. Mean assets: the mean of the summed positive class TNA.
14. **Several mgrno.** They are one filer. When two file the same quarter, the larger matched value is used.
15. **Several funds of one investor.** One record, combined by previous month-end assets (registration section 12).
16. **Score part (iii).** The population is the filers (funds) in the rank group of at least one block. The value is the share of blocks with 36 months in which alpha > 0.
17. **Score and eligibility.**
   - Months of record are counted after the cut.
   - No rank share means no score and no place by record, but the investor can be drawn as control. If 10 or fewer are eligible for control, all are taken.
   - `record_kind` decides fund versus 13F.
18. **Explicit places.** Only `role` = investor with `ran_money` = yes; the `role` column is now required. Missing explicitness ranks last.
19. **Best-scored lists.**
   - Score: the same three-part mean, computed only for filers (funds) with at least 60 months in 2011-25.
   - Left out: every filer in any frozen `mgrnos` or `known_mgrnos`, and the whole class group of every fund in `fundnos` or `known_fundnos`.
   - Printed: name, score and the three rank shares.
20. **Statistics or rank shares only.** Statistics are printed if the window or the 2011-25 record has 60 months. Every matched investor gets an `INV` line, even with 0 months.
21. **Newey-West.** Bartlett weights with the factor n/(n−k). Gaps in a record are treated as adjacent months.
22. **Foundation list.** Uses the `words` column of `inventory.csv` (now present).
23. **Pull key.** A hash of the library 13F filers and library fundnos, the two inputs the pulls depend on. A change in either needs a re-pull of `eq_sc_cand`, `eq_sc_hold_*`, `eq_sc_fret_*` and `eq_sc_fmeta`. A change only in grades, styles, months or names does not.
24. **Read range.** Design months are also read, outside "2010-06 to the seal end": `msf_v2` from 2009-06 (momentum), factors from 2009-01, `firm_ratio` from 2010-01. Registration section 1 should say so.
25. **Seal rules for SEAL_LOG.**
   - Equity jobs use no pull or export steps, and only the pull job may delete `eq_sc_*`.
   - The registered scorecard runs under `eq_sc_pull_v<n>[x]` (pulls) and `eq_scorecard_v<n>[x]` (build/report). Its steps are fixed templates.
   - Each run logs the code hash printed in the report header (computed at run time from the module file), the input hash and the lock id.

## 4. Expected run on WRDS (estimates; nothing measured)
| Job / step | Rows (est.) | Stored (est.) | Time (est.) |
|---|---|---|---|
| eq_sc_pull: base | ~0.8M | ~20 MB | < 5 min |
| eq_sc_pull: crsp | ~1.7M | ~40 MB | ~5 min |
| eq_sc_pull: agg | ~0.5M (SQL over 3-9M s34 rows per year) | ~15 MB | 30-90 min |
| eq_sc_pull: hold | 4-7k filers, 10-20M rows | 200-400 MB | 20-40 min |
| eq_sc_pull: funds | ~3-4M | ~70 MB | 5-10 min |
| eq_scorecard: build | memory est. 3-5 GB | report only | 15-40 min |

The pull budgets sum to 2.25 h per run, and each pull stops starting new data sets once its budget is used. Expect one or two pull runs, then one build run, about 0.5 GB of the quota in all. Only runs of `eq_scorecard_v<n>` open the seal for results. Pull runs print only row counts and are logged as reads.

## 5. Code check findings: what was done
- **B1 (seal checker):** every route A1-A14 is closed and each is a refused job in the smoke test.
  - Reader: constants are read-only mappings, `exempt` is keyword-only, data sets are declared, and date columns are validated.
  - Checker: refuses too many positional arguments, any access to reader internals, dunder attributes, lib files shadowing standard modules (for every job), scorecard data-set names outside `load_ds`, `eq_sc_*` in non-eq jobs, and deletes of scorecard data sets.
  - Exempt jobs are template-only and limited to the functions registered per name.
  - `build` returns nothing and `stock_returns` is gone.
- **B2:** TNA ≤ 0 and returns < −1 count as missing, for funds and stocks. The smoke world has −99 months.
- **B3:** split into two jobs (pull job, build job). The build prints its time per stage.
- **B4:** the pull key is stored with the candidates and the fund pulls. `build` and `pull_status` refuse stale or incomplete pulls.
- **B5:** `known_mgrnos` and `known_fundnos` (whole class groups) are left out of the best-scored lists.
- **Non-blocking:**
  - 1: superseded by registration 3.5 (the rule no longer depends on the future).
  - 2: counted by the precheck.
  - 3: kept as registered, stated in the header.
  - 4: ambiguous book-to-market dates dropped and counted.
  - 5: whole class groups pulled.
  - 6: registered.
  - 7: documented (reading 13).
  - 8: reading 24.
  - 9: run-time code hash in the header.
  - 10: atomic saves.
  - 11: sanitized errors (pulls re-raise only class and first line, ids and number runs masked; build prints class and module line only).
  - 12: `INV` line for every matched investor.
  - 13: role required.
  - 14: turnover and new positions computed per quarter.
  - 15: latest report date per quarter, with a count.
  - 16: deletes restricted.
  - 17: tests C21-C34 and S12-S30 added.
  - 18: not ours.

## 6. Pre-run check (`eq_precheck_v1`, non-exempt, counts only)
1. Delisting returns, 2001-2010: `msf_v2` rows by `mthdelflg` with and without `mthret`; `stkdelists` rows with a `delret`; whether `msf_v2` has a row and a return in the delisting month; and how many delisting returns are not reflected.
2. Per year from 2010: manager-quarters in `tfn.s34`, all, and those without a first version (`fdate = rdate`), through `eq_reader.count`.
3. Largest absolute factor value, 1990-2010 (decimals check).
4. `firm_ratio` 2005-2010: permno-dates with more than one row, and with two different book-to-market values.

## 7. Output vs spec section 8
| Section 8 item | Report block |
|---|---|
| Row per matched investor: grade, kind, months, section 4 columns per window, rank shares | `LIBRARY INVESTORS`: an `INV` header line, then one line per window. Columns: a, t, r, rm, pa, pv, dd, yb, np, tw, to, p10, pn, fv, ms, rk |
| Tier lists | `TIERS`: by record, explicit, control, tier B, foundation |
| 25 filers and 10 funds without a document | `BEST-SCORED ...`: name, score, three rank shares |
| Persistence and counts | `PERSISTENCE` (rho and the 5x6 tables, 13F and funds apart) and `COUNTS` |

The header carries the code hash, input hash, pull key and peer universe. The report holds no holding, stock, return series or style/sector/factor average; the smoke test checks that no CUSIP or permno appears in it.
