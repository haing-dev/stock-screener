# LSEG weekly live file (TESTING_PROTOCOL 7.10 item 3, step 4)

## What the user does (once a week)
1. Open `G:\My Drive\Screener project\LSEG\10_weekly_live\LSEG_weekly_live.xlsx` in Excel with Workspace signed in; wait until cell B4 of the Check sheet has not changed for one minute.
2. Press Ctrl+S (same name, same folder).
3. Tell Claude "weekly saved".

Nothing else: no remote control, no copying. The file uses relative dates (`TODAY()`), so the same file is refreshed every week.

## What it holds (`code/build_lseg_weekly.py`, 244 formulas)
| Sheet | Series | Reader of the live value |
|---|---|---|
| Curves | daily closes, last 70 days, of continuous positions c1..cK of the 16 Curve carry commodities (K = up to 18: the positions a front leg >= 3 months out and its 12-month-later contract can occupy) | Curve carry (both legs, front-leg volatility); card 5 R1 (CL c1, HG c1) |
| Strips | daily settlements, last 70 days: 3m SOFR c1-12, Euribor c1-12, 3m SONIA c1-8 | Strip reversion live strips (dollar = SOFR, sterling = SONIA, euro = Euribor); T10 strip markets |
| Monthly | S&P 500 12-month forward EPS (IBES aggregate `@:USSP500` A12FE), last 13 month-ends | card 3 R4 |
| Identity now | expiry, last trade and first notice date of the contract each live position holds today (RDP.Data over the Positions list) | contract identity cross-check against the locked calendar |

Field names in "Identity now" (`TR.ExpiryDate`, `TR.LastTradeDate`, `TR.FirstNoticeDate`) are the same guesses as the L11 calendar: once L11 shows which names work, set `ID_FIELDS` in the builder and rebuild the file (one time).
Not in the file: series whose live source is free data (FX, bonds, equities, FRED rates): the free weekly cycle reads those. Not usable live before the licence statement (7.10 item 3 step 5) and the LIVE_START entry.

## What the PC job does (`code/jobs/lseg_weekly_v1.py`)
- Reads the saved file only (env `LSEG_WEEKLY`, else the path above) with the same reader as the history (`lsegdata.read_workbook`).
- `lsegdata.live_ingest`: appends new rows to `local\work\lseg\live\live_long.pkl` with the ingest number and time (append-only: a value that changed for a date already stored is added as a revision, the old row stays); writes the "Identity now" rows to `live\identity_live.csv`; logs the ingest in `live\ingests.csv` with the file hash and the hash of the live table after the ingest (a chain). The same saved file (same hash) is never ingested twice, so queuing the job again is harmless.
- Prints metadata only: file, save time, rows added / revised per root, failed blocks, STALE series (last value more than 3 business days before the save day; monthly: last completed month-end missing), identity rows with a date, agreement of today's identity with the locked calendar + roll rule (counts), and a CALENDAR HORIZON warning when the L11 calendar lists fewer than 24 months of contracts ahead.
- Queue it as a new job name each week (runner rule): copy `lseg_weekly_v1.py` to `local\jobs\lseg_weekly_<yyyymmdd>.py`.

## How a pod reads live values
`lsegdata.Panel(work, live=True).asof(day)` serves design + sealed history + the live store, only for as-of dates on or after `LIVE_START`, and only once `LIVE_START` is set by the registered gm/CHANGES.md data entry (it is `None` now: live mode is refused). Live-only series (not in the history catalog) get the default delay of 1 day.
