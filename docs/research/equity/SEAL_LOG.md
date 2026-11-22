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

Lock id: 66a9d9c66e431ec6e52ef263197c1e02d316513f0d274b60bd4b37847f11dba0 from Addendum A (before: e680ca33c77ec51ed50372ec66e5733001cd4867adf1e692f88a4e2645015099, 2026-11-18; reader a99b5c80853e, checker 7fbfc654946e, exempt list f7f6560bc43c)

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
| 2026-11-18 | `eq_sc_pull_v1` (pulls only; 3,177 s; base, CRSP and funds complete, 13F aggregates 2010-19 of 2010-25; report `scorecard_check/eq_sc_pull_v1_report.txt`), then `eq_sc_pull_v1b` | f7f542646da4... (input c77e38e77851...) | CRSP, 13F, firm_ratio, factors, CRSP funds, 2009-06 to 2025-12, stored on WRDS | Pull status lines only |
| 2026-11-18 | `eq_sc_pull_v1b` (first attempt stopped by the runner's 3-hour watchdog after its saves; retry printed ALL PULLS COMPLETE, 73 data sets, pull key 45671094f38c9a10, 6,542 candidate filers; report `scorecard_check/eq_sc_pull_v1b_report.txt`) | f7f542646da4... | as above | Pull status lines only |
| 2026-11-18 | `eq_scorecard_v1` (build + report: the opening of the seal; ran 243 s, 16:21 PC time, once) | f7f542646da4... printed at run time = registered (input c77e38e77851...; header input hash 1f58666e... is the module's own hash of the same table, reading 22; lock e680ca33...) | the stored `eq_sc_*` data sets | Section 8 only: 90 matched-investor rows, tiers, persistence, 25 filers and 10 funds without a document, counts. Report `scorecard_check/eq_scorecard_v1_report.txt`; results `SCORECARD_RESULTS_2026-11-18.md` |
| 2026-11-18 | `eq_scorecard_v2` CANCELLED BEFORE IT RAN at the user's request (the queued file was replaced by a metadata-only job `eq_scorecard_v2_cancelled`); no second opening. It was: (Addendum A, registered before the run; code check RUN) | 49adb08739090e36... (input c77e38e77851...; pull key 45671094f38c9a10; lock 66a9d9c6...) | the stored `eq_sc_*` data sets | Section 8 plus Addendum A lists only |
| 2026-11-19 | `eq_hf_pull_v1` (queued; hedge fund leaderboard, user request 2026-11-18, `HF_LEADERBOARD_REGISTRATION.md`; third seal-exempt job, entry `hf_leaderboard` in `seal_exempt.json`) then `eq_hf_v1` (report) | 04b59fd5b396... (lock cc6c2920...) | 13F first versions 2020-12..2026-03, CRSP msf_v2 2020-10..2025-12, s34names, stocknames_v2 (SQL aggregates per filer-quarter, stored on WRDS as `eq_hf_*`) | Per-filer statistics (top 250 of US + UK/Europe >= $1bn) and quarterly top-20 returns of 12 named validation funds |
| 2026-11-19 | `eq_hf_pull_v1` ran 3,153 s (ALL PULLS COMPLETE); `eq_hf_v1` report ran 08:27 PC (after a hung WRDS login, cleared by the watchdog); `eq_hf_v2` queued (report only, ranked on start-of-quarter weights = the website's method) | 04b59fd5... then 0f78ced5... | the stored `eq_hf_*` data sets | As registered |

## Plan v0.4 (2026-11-20): what the seal means from here
Registered in `V04_REGISTRATION.md` R3 (user decision of 20 Nov: tests on 2010-2025). US 2010-01 to 2025-12 is the
main test period, not a holdout. Returns of portfolios, signals and factors in those months are computed only by
the test desk's scripts in runs written to the trial log before they start; levels of company measures are open.
Still sealed until the freeze: every market outside the US 2010-2025, and US months from 2026-01. The WRDS reader
(`eq_reader.py`) and its lock are unchanged until the engine exists; the three seal-exempt jobs stay as logged; the
conviction holdings job (R2) will be the fourth, with its code hash entered before it runs.
- 2026-11-21: seal-exempt job 4 `universe_check` registered (V04_REGISTRATION.md A1): eq_univ_check_v1, CRSP listing
  levels 2009-2025 only (no returns); counts and at most 30 company names come back.
- 2026-11-21: `eq_univ_check_v1` ran (code 46e6bcdc...): rule not met, cause = matching key (V04_REGISTRATION.md A2).
  Logged bug-fix rerun `eq_univ_check_v2` queued (code 8c28d777..., same data, counts and at most 70 names).
- 2026-11-21: `eq_univ_check_v2` ran (rule not met: dead lists ended at S). `eq_univ_check_v3` queued: same code
  8c28d777..., input extended with DEADUS11-12 (V04_REGISTRATION.md A3).
- 2026-11-21: `eq_univ_check_v3` ran: rule met (A4). Seal-exempt job 5 `conviction_holdings` registered and queued:
  `eq_conv_v1` (code d9320b04...), 13F first versions + CRSP names / quarter-end prices 2009-12..2025-12, no returns.
- 2026-11-21: `eq_conv_v1` ran with a quarter-filter bug (counts void). Logged bug-fix rerun `eq_conv_v2` queued
  (code ad0dde91..., same data; ids added from v1's name search; V04_REGISTRATION.md A5).
- 2026-11-22: seal-exempt job 6 `reference_book` registered (V04_REGISTRATION.md A8; TRIAL_LOG.md T001): `eq_ref_pull_v1`
  (CRSP msf_v2 / dsf_v2 aggregates, CCM links, Compustat fundq, GICS history, I/B/E/S summary, CRSP names, FF
  factors, 2007-2025, stored on WRDS as `ref_*`) then `eq_ref_v1` (Batch 0: reference book v1 and the published-form
  checks of its measures, US 2010-2025; summary statistics only). Code c8705b6f... (1.0.1); lock ca2e3b04...
- 2026-11-22: `eq_ref_pull_v1` ran (215 s, all tables). `eq_ref_v1` stopped before any return (account join bug; counts and
  coverage only came back). Logged bug-fix rerun `eq_ref_v1b` queued: eq_ref 1.0.2 (code e5a7ee9c...), same stored data;
  lock 6243526a...
- 2026-11-22: `eq_ref_v1b` ran the stale 1.0.1 code (delivery error) and stopped before any return. `eq_ref_v1c` queued with
  1.0.2 (e5a7ee9c..., PC lib file checked byte for byte before queuing).
