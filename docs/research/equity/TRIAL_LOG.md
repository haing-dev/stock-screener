# Equity pod shop: trial log

Plan v0.4 fence 7 (R3): every run that computes portfolio, signal or factor returns of 2010-2025 is written here
BEFORE it starts. Columns: id, date written, run (job names), code hash, registration, what it computes, counted as.

| id | written | run | code | registration | computes | counted as |
|---|---|---|---|---|---|---|
| T001 | 2026-11-22 | `eq_ref_pull_v1` (pulls only), `eq_ref_v1` (WRDS) | eq_ref 1.0.1 c8705b6fe5b6... (input 9aee97e0232f...) | V04_REGISTRATION A8; FIELD_DICTIONARY_v1.0 part 1 | reference book v1 long book under R4, its benchmarks, and the published-form spread of each of its 7 measures, US 2010-2025 | Batch 0 (plumbing; no verdict) |
| T001 note | 2026-11-22 | `eq_ref_pull_v1` ran (ALL PULLS COMPLETE, 215 s). `eq_ref_v1` stopped at section 1 (report `eq_ref_v1_report.txt`): no account measure joined (gvkey text keys differed after the CSV round trip and the link join), so nothing was ranked and the run crashed before any return. Logged bug fix: eq_ref 1.0.2 (e5a7ee9c...), reproduced and fixed in `tests/eq_ref_smoke.py` (lines without a link + CSV round trip); rerun `eq_ref_v1b`, same data, same registration | - | - | - | no return computed | still T001 |
| T001 note | 2026-11-22 | `eq_ref_v1b` ran the OLD code 1.0.1 (the file copied to the runner's lib was a stale 1.0.1 copy; delivery error, verified afterwards by reading the PC file back) and stopped at the same place: no return computed (report `eq_ref_v1b_report.txt`). The PC lib now holds 1.0.2 (checked byte for byte); rerun `eq_ref_v1c`, same data, same registration | - | - | - | no return computed | still T001 |
| T001 result | 2026-11-22 | `eq_ref_v1c` (eq_ref 1.0.2 e5a7ee9c..., 52 s) | - | A8 | done: `BATCH0_REFERENCE_BOOK_2026-11-22.md`, report `eq_ref_v1c_report.txt` (book net - sector-matched +1.0% a year, NW t 1.24; plumbing checks pass) | Batch 0, no verdict |
