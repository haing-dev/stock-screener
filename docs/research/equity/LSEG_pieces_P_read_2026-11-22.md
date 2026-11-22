# LSEG pieces P01-P18 read back (2026-11-22)

Files: `G:\My Drive\Screener project\LSEG\08_pieces_v4` P01-P18 (+ B01, B02, which had also loaded), read in the cloud
with `tools/equity/lseg/read_stage_b.py` (metadata only; LSEG values stay off the repo). Coverage is measured among the
1,500 largest companies by market value at each December (monthly panel v1).

| Input | Result | Coverage among the 1,500 largest |
|---|---|---|
| P01 GICS today | 5,065 rows; blocks carry no instrument column, rows align with the input list (LSEG name = list name for 100%) | **66% (2010) rising to 99% (2025)**: GICS is empty for 1,874 companies, 1,773 of them dead |
| P02-P05 close as traded | 5,537 lines, 1.1 million month rows | 99-100% |
| P06-P15 + Q2_v1 quarterly book items (first reported) | 4,520 companies with quarters, 361,290 company-quarters | revenue, net income and equity within 200 days: 92% (2010) to 97% (2025) |
| P16-P18 FY1 consensus EPS by month | 4,636 companies; 45 rows with impossible dates | latest value within 60 days of month-end: 87% (2010) to 94% (2025). Matching on the exact month gives only ~70%, because LSEG's monthly date often falls in the previous month |
| B01-B02 other quarterly items | 500 companies | (pods, later) |

## Problem and fix
Without a sector a stock is not ranked (A8 2a), so the dead companies would drop out of the early years
(survivorship bias). Fix: piece **P19** (`docs/data_requests/build_lseg_sector_fix.py`, Datastream static: NAME,
GGISN, INDM, ICBIN, and WC07021 as a guess, for all 5,065 companies; about 25,000 values; saved to the pieces folder).
Companies with both P01 GICS and a Datastream code give the crosswalk for the rest (rule in A11 item 3).

## Next
P19 refresh -> sector crosswalk -> the LSEG run of the reference-book engine (A8 item 4: the registered primary form;
written to `TRIAL_LOG.md` before it runs) -> dashboard v0 and the names review (A10 item 10).
