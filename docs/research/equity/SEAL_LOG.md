# Equity pod shop: seal log

The seal (plan v0.3 section 8.2). Sealed until the freeze: US months from 2011-01 to the seal end, and months outside
the US from 1990-01 to the seal end. **Seal end: 2025-12** (the last CRSP stock month found by the WRDS table check
on 2026-11-17). Months after it are never holdout.

Mechanism: every equity job reads through `tools/equity/wrds/eq_reader.py`, whose date and region limits refuse
sealed months; `tools/equity/seal_check.py` checks each job before it is sent and refuses direct table reads; only
the two seal-exempt jobs (scorecard, holdings) pass, each with a registered code hash. The lock id is the hash of
the reader, the checker and the list of exempt jobs. Allowed on sealed months before the freeze: structure checks
(counts, coverage, date ranges, identifiers), correlations with published series, estimation inputs of the live
book. Never a mean, Sharpe ratio, drawdown, stress result or chart of any portfolio, signal, factor or pod.

Lock id: e680ca33c77ec51ed50372ec66e5733001cd4867adf1e692f88a4e2645015099 (2026-11-18; reader a99b5c80853e, checker 7fbfc654946e, exempt list f7f6560bc43c)

## A. Reads made before the seal existed
| When | What | Years | What was seen |
|---|---|---|---|
| 2026-10-30/31 | Triage screens on WRDS (`docs/research/triage_wrds/RESULTS.md`), train 2008-15, test 2016-24 | US 2008-24 | Returns of the three triage screens and their cells; factor loadings. No test passed; calls load on profitability |
| before 2026-10 | "Top performer" 13F pick test noted in crash-triage `pipeline/fit.py` | US 1998-2023 | Not in this repo; report to be found (biotech step B0.1) |
| 2026-11-15 | Biotech crash-triage re-run (`docs/research/equity/biotech_checks/2026-11-15`) | US biotech 2020-26 | Returns of triage calls against the biotech index |
| since 2026-10-22 | Live triage screens on free data (branch `triage-record`) | US 2024-26 | Live calls and marks |
| 2026-10-30/31 | Pulls kept on WRDS Cloud (`tri_*`, `bio_*` data sets: CRSP, Compustat, 13F, I/B/E/S extracts) | to 2026 | Data stay on WRDS; used only by the jobs above |
| 2026-11-17 | `eq_tables_v1`, `eq_tables_v2` | all | Metadata only: tables, columns, counts, date ranges |
| 2026-11-18 | `eq_precheck_v1` (counts only, through the reader's named checks; report `Screenerdata\runner\results\eq_precheck_v1.txt`) | design era 2001-10; 13F counts by year 2010-25 | Counts only: every delisting 2001-10 has a monthly return in its last month (5,402 of 5,402); manager-quarters without a first version: 20 in 2010, 1 in 2017, 0 otherwise; factors in decimals; 958 firm_ratio permno-dates with two book-to-market values |
| 2026-11-17 | `eq_match_v1` (phase A of the scorecard) | 13F from 2010-06 | Names and ids of filers and funds; per filer the number of quarters, positions and size. No return |

## B. Openings of the seal by the seal-exempt jobs
| When | Job | Code hash | Inputs | What came back |
|---|---|---|---|---|
| 2026-11-18 | `eq_sc_pull_v1` (pulls only; re-runs v1b, v1c... until complete) | f7f542646da4... (input c77e38e77851...) | CRSP, 13F, firm_ratio, factors, CRSP funds, 2009-06 to 2025-12, stored on WRDS | Pull status lines only |
