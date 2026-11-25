# LSEG as a registered source: reader, data check, contract identity, lock, weekly refresh (2026-11-24)

TESTING_PROTOCOL 7.10 item 3 lists five steps before LSEG is a registered source. Steps 1-4 are built here as code and
job files and tested on mock workbooks only (no LSEG value was read in the cloud). Step 5, the written licence statement
for live and trading use, is the user's. Nothing here is registered or run on real data.

| 7.10 item 3 step | Built | Where |
|---|---|---|
| 1 reader into the engine with an as-of function | `lsegdata.py` (build, Panel, AsOf, seal, untouched hiding, engine-id map) | code/ |
| 2 data check (start dates, gaps, copies) and contract identity per observation | `jobs/lseg_check_v1.py`; identity from `Calendar` + roll rule, checked on sample contracts; the pull that supplies it: `build_lseg_contract_pull.py` -> `docs/L11_contract_identity.xlsx` | code/, docs/ |
| 3 lock with file hashes and the 2011+ seal, like LOCK_v2 | `jobs/lseg_build_v1.py` -> `local\work\lseg\{manifest.json, LOCK, lock.json, catalog.csv, design\, sealed\, calendar*.pkl}` | code/ |
| 4 weekly refresh job on the user's PC | `build_lseg_weekly.py` -> `docs/LSEG_weekly_live.xlsx`; `jobs/lseg_weekly_v1.py`; LSEG_WEEKLY.md | code/, docs/ |
| 5 licence statement | not built (user) | - |

## 1. Files
- `code/lsegdata.py` (lsegdata-1.0.0): the only code that reads the LSEG workbooks or the derived tables. Stdlib + numpy + pandas + openpyxl (the PC's local\pylib). Reads the four functions of the pulls (RHistory, RDP.Data, DSGRID, RDP.HistoricalPricing) from the formula text in row 4 of each block (never guessed from values); statuses ok / empty / invalid / no-dates / copy / wrong-series; series id `"<fn>:<code>|<field>"` (e.g. `DS:BMUS02Y|RI`, `HP:CLc1|CLOSE`, `DS:<EDc1>|X`) with per M / D; long tables split at 2010-12-31 by observation date; as-of guard; holdout key (None) and live flag (LIVE_START None) both refuse today; every refused or granted attempt goes to `sealed_access.log`; contract calendar and `Calendar.held(root, n, day)`; append-only weekly live store.
- Config next to it (registered inputs: their hashes enter the lock): `lseg_live_sources.csv` (kind and delay per file / sheet / code), `lseg_exclusions.csv` (wrong series: CEDCS00, LSSCS00, MBACS00, LESCS00, GSPTTOT, GSPTEXR), `lseg_untouched.csv` (instruments the book does not trade, mirror of tools/bbgq/untouched_markets.csv), `lseg_engine_map.csv` (116 series -> engine ids, proposals), `lseg_roots.csv` (22 futures roots: continuous-series ids, positions pulled, roll anchor, what the spec needs). `lseg_spec_needs.csv` is read by the check only.
- Jobs (PC runner, cwd = `Documents\WRDS results\local`): `lseg_build_v1.py`, `lseg_check_v1.py`, `lseg_weekly_v1.py`. All print metadata only (export whitelist); the tests scan every job output for any mock value (none found).
- Builders (cloud, openpyxl): `build_lseg_contract_pull.py` -> `docs/L11_contract_identity.xlsx` (175 formulas + a 12,736-row contract list); `build_lseg_weekly.py` -> `docs/LSEG_weekly_live.xlsx` (244 formulas). Both use the layout of `docs/data_requests/lseg_pull_helpers.py` (Check sheet, row 2 id, row 3 label, row 4 formula text, row 6 formula) and only functions that returned dated data in the probes.
- Tests: `tests/test_lseg.py` (driver) + `tests/make_mocks.py` (mock workbooks in the real layouts, invented numbers, a synthetic futures market with a known roll rule; L11 and weekly mocks filled from the real builder templates). Output: `tests/test_output.txt`.

## 2. What each job does
**lseg_build_v1** reads every `L*.xlsx` in `LSEG_DIRS` (default: `Documents\WRDS results\lseg\pull_2026-11-12` and `G:\My Drive\Screener project\LSEG\09_contract_identity`), newest file per key (L1a ... L11), lists P probes and other files as not read; prints CANDIDATE, FILE (sha256, save day), SHEET (block and status counts), STATUS, FAILED (code, status, first error text), COPYGROUP, DROPPED (rows after the save day, weekend rows, undated rows), TABLE (rows, series, date range, content hash), DATE RULE per function, CALENDAR per root, WARN, CODE / CONFIG hashes, LOCK, then the whole `lock.json` (to be committed as `docs/research/lseg/LOCK_LSEG_v1.json`: lock id, file hashes, counts, per series the first / last design date and the design and sealed counts). A rebuild moves the old manifest to `work\lseg\history\`; the same files give the same lock id; one changed value gives a new one (tested).

**lseg_check_v1** (design part only; the sealed table is never opened): STATUS; NEED (each spec input of `lseg_spec_needs.csv`: OK / LATE / SHORT / MISSING with the missing positions); GAP (> 2 months / > 10 business days); STALE (6 months / 10 days unchanged); COPY (copy groups, whole-array identical pairs, identical 24-month / 60-day runs shared by different instruments); DSDATE (month-end rule per function; Datastream month-ends on US / UK holidays, whose value is the previous trading day's, unscreened); LABEL (monthly value vs the daily copy of the same series: is the month label's value the month's last daily value); IDENTITY per root (positions with design data, calendar: listed months = serial months or not, anchor dates, first notice; roll rule checked on sample contracts by value matching; Curve carry depth: can the 12-month-later leg be found inside the pulled positions in each design month; Strip depth: do the first eight quarterly contracts sit inside the monthly and daily positions) with a VERDICT COMPLETE / PARTIAL / NONE and what is missing; PROBE (which guessed field names returned dates); ENGINE; SEALED (structure only).

**lseg_weekly_v1**: see LSEG_WEEKLY.md.

## 3. Contract identity: what is missing today and how L11 supplies it
With the files pulled so far the answer is NO for every root: continuous closes (CLc1 ... CLc24, `<EDc1>` ... `<EDc12>`) carry no delivery month, the roll day cannot be seen in prices, and nothing says whether serial months are positions. Exactly missing, per root: (1) the delivery month per observation, (2) last trading and first notice days per contract, (3) the listed months, (4) the roll rule of the continuous series, (5) depth for the legs (heating oil and gasoline beyond c12, copper beyond c12, gold / silver beyond c12, platinum beyond c6, soybeans beyond c9, sugar beyond c6, coffee / cotton / cattle beyond c6), and (6) Eurodollar daily contracts 3, 5, 6, 7 (R1). On the mock data before L11 the check prints `IDENTITY VERDICT <root> | NONE` with these items.

L11 (`docs/L11_contract_identity.xlsx`) asks for: Calendar (12,736 contract RICs of 22 roots, 1972-2029, both the expired form `CLZ5^9` = Dec 1995 and the live form `CLF7`, in 13 blocks of 1,000 x 4 date fields; an unlisted month returns an error, which answers the serial-month question); Calendar test (12 contracts x 10 candidate field names); Contract sample (two contracts per root monthly over their life and one daily around its expiry: matched to the continuous series they show which position held the contract on each date and the roll day relative to last trade / first notice); Identity probe (12 guesses that might give the held contract as a time series directly); Curve depth (37 extra positions); ED daily (`<EDc3>`, `<EDc5>`, `<EDc6>`, `<EDc7>` from 1989-12-29, the form that worked in L10).
GUESSES to be confirmed by the refresh: every TR field name for contract dates (`TR.ExpiryDate`, `TR.LastTradeDate`, `TR.LastTradingDate`, `TR.FirstNoticeDate` in the full calendar; ten names in the test); the expired-RIC form for RDP.HistoricalPricing and for Datastream (`<CLZ5^0>`); Datastream explicit end dates and the `LTDT` datatype; the gasoline root before RBOB (`HU`); RIC roots of SONIA (`SON3`) and Euroswiss / short sterling individual contracts. If the calendar names fail, the PROBE lines show which test names worked: change `CAL_FIELDS` in the builder and pull the Calendar sheet again (one small file).
The roll rule is not assumed: `lseg_roots.csv` says `last_trade` (a position keeps a contract through its last trading day), and the check counts agreement on the samples; a root is COMPLETE only with a calendar anchor for every design-era contract, first notice days for every design-era contract of the roots whose delivery notices start before the last trading day (metals, grains, coffee, cotton, cattle; energy and sugar expire before the delivery month: to be confirmed from the exchange rules), the depth its spec needs, and at least 10 matched sample observations with 99% agreement. On the mock market, heating oil and Eurodollar reach COMPLETE, WTI and gold PARTIAL (depth), the rest NONE.

## 4. Order on the PC
0. Deploy: write `lsegdata.py`, the five config CSVs and `lseg_spec_needs.csv` to `local\lib`, the three jobs to the repo; READ THE LIB FILES BACK and compare hashes before queuing (lesson of 2026-11-22). Precondition: pandas loads on the PC (gm_repro_v3 passed 2026-11-24; Smart App Control is on).
1. Queue `lseg_build_v1` (it can run now, on L1a-L10: the store and lock of what exists, identity NONE). Commit the printed lock.json as `docs/research/lseg/LOCK_LSEG_v1.json`.
2. Queue `lseg_check_v1`; write a short note from its lines (NEED, GAP, COPY, DSDATE, LABEL, IDENTITY).
3. User: refresh and save L11 (below). Then queue `lseg_build_v1` again (new lock id: L11 added) and `lseg_check_v1` again. If the calendar field names failed: rebuild L11 with the names the test sheet proved, refresh, rebuild.
4. Write the gm/CHANGES.md data entry (section 6) with the final lock id and LIVE_START, and the licence statement (user), BEFORE any use. Then set `LIVE_START` in `lsegdata.py` (a code change: new lsegdata version, registered in that entry).
5. Weekly from then on: LSEG_WEEKLY.md.

## 5. What the user must do
- L11 (once, about 175 formulas): put `docs/L11_contract_identity.xlsx` in `G:\My Drive\Screener project\LSEG\09_contract_identity\` (Claude copies it there through the bridge), open it in Excel with Workspace signed in, wait until B4 of the Check sheet stops changing, Ctrl+S. Errors in some blocks are expected (guesses).
- Weekly (3 lines, LSEG_WEEKLY.md): open `G:\My Drive\Screener project\LSEG\10_weekly_live\LSEG_weekly_live.xlsx`, wait for B4, Ctrl+S, say "weekly saved".
- The licence statement for live and trading use (7.10 item 3 step 5), in writing, in the repo.

## 6. Draft gm/CHANGES.md data entry (for the coordinator to commit before first use)
```
## data: LSEG registered as a source (registered <date>, BEFORE first use): TESTING_PROTOCOL 7.10 item 3, 7.4 E15
Registered data entry (no rule changes). LSEG Workspace / Datastream pulls L1a-L11 saved on the user's PC become a
registered source through lsegdata-1.0.0 (tools/bbgq/lib/lsegdata.py, code sha256 <sha>) with its five config files
(lseg_live_sources.csv, lseg_exclusions.csv, lseg_untouched.csv, lseg_engine_map.csv, lseg_roots.csv; hashes in the
lock). Lock: docs/research/lseg/LOCK_LSEG_v1.json, lock id <id> (job lseg_build_v1, <date>); data check: job
lseg_check_v1 (report tools/bbgq/results/lseg_check_v1.txt).
1. History: observations dated <= 2010-12-31 are the design part; later ones are sealed (opened only by the holdout key
   or, for as-of dates on or after LIVE_START, by the live flag; every attempt logged). As-of rule: an observation is
   known at its observation date plus the delay of lseg_live_sources.csv (market closes and settlements 0 days,
   decisions at the close, TESTING_PROTOCOL 7.3 item 4; economic series 45 / 60 / 90 days, no release dates in these
   pulls). RHistory / HistoricalPricing month labels after the file's save day are dropped.
2. Contract identity: a continuous position cN holds the N-th listed contract whose last trading day is on or after
   the day (lseg_roots.csv roll_on), with listed months, last trading, first notice and expiry days from the L11
   calendar; registered per root only where lseg_check_v1 printed IDENTITY VERDICT COMPLETE (list: <roots>). A market-
   month whose leg cannot be identified holds nothing (SPEC_Curve_carry s3, 7.6 step 8). Roots not COMPLETE stay
   unregistered for the pods that need identity.
3. Scope: LSEG serves the inputs the specs list as LSEG (Curve carry curves, Strip reversion strips incl. Eurodollar
   daily 1-8, T10 strip markets if admitted, card 3 R4 forward EPS, card 5 R1 fronts and C5-D2 lines, card 3 R1
   deposit-rate history as a cross-check). It never replaces a free-data series the engine already uses, except
   through the A1-style rule of 7.6 step 2 (same instrument, extend backwards only, overlap correlation >= 0.95 up to
   2010-12), applied per series and listed.
4. Live: weekly file LSEG_weekly_live.xlsx refreshed by the user and read by job lseg_weekly_v1 (append-only live
   store, ingest log with table hashes). LIVE_START = <date>; set in lsegdata-1.0.1 with this entry. Live use only
   with the licence statement <path> in the repo (7.10 item 3 step 5).
5. Not served by LSEG (Bloomberg LOCK_v2 or nothing): see docs/research/lseg/LSEG_SOURCE_PLAN.md section 7.
```

## 7. Open items
- Licence statement for live and trading use (user; 7.10 item 3 step 5). Without it LSEG stays research-only and no pod can be Core on an LSEG input (rule 7).
- L11 not refreshed: every identity verdict is NONE until then; the field names and expired-RIC forms are guesses.
- Not on LSEG (from the 2026-11-12 read-backs): short sterling c1 before 1999-06 and c2-c8 before 2002-03 (Bloomberg L1-L5 from 1988); Canada BA c2-c8 (Bloomberg BA2-BA8; Strip spec already keeps BA out); Euroyen c7-c8; CAD swaps before 2009 (Bloomberg CMPN from 1989), euro and Japan inflation swaps; lumber, JGB mini, AUD 30y swap, GSCI platinum, Baltic Dry, VIX (no licence), SG CTA / BTOP50; credit spreads, commodity fundamentals, economic first release / consensus, MSCI valuation ratios; daily history beyond c1/c2 for commodities (no daily far-contract settlements: Curve carry stays k = 0 and has no weekly check, 7.3 item 3); daily Euribor / short sterling / Euroswiss contracts 3-8 (those strips cannot enter Strip reversion until pulled: one small pull like the ED daily sheet, not in L11).
- Live strips: Eurodollar ended 2023, short sterling and Euroswiss 2021, Euroyen 2024: live dollar strip = SOFR (from 2018; a 60-month normal needs SOFR month-ends from 2018 to 2023, sealed history today), sterling = SONIA (2018), no live Swiss strip; no normal passes from one reference rate to its successor (Strip spec s3 step 5).
- Delays are a registered convention, not measured: economics 45 / 60 / 90 days; IBES forward EPS counted known at its month label (IBES computes it mid-month).
- Holiday flags use approximate US / UK calendars (Datastream last weekday month-ends that are holidays carry the previous day's value); they flag, they do not screen (CHECK_3.2_B s4: "the reader should flag them").
- The copy rule needs 3 different instruments (Bloomberg used 5): the LSEG read-back had no pasted copies, and pairs are reported for review; the check also reports shared identical runs.
- `lseg_engine_map.csv` is a proposal: Datastream benchmark return indexes are not the free source's par-yield construction, TOTMK indexes are not the panel's indexes; any use goes through the A1-style rule.
- Untouched list mirrors the Bloomberg one by pattern; card 5 C5-D2 reads cocoa and LME with `allow_untouched=True`.
- The weekly file's TEXT(TODAY(),"dd-mmm-yyyy") dates assume an English Excel locale (as the pull files' fixed dates).
- Live-only series (not in the history catalog) get the default delay of 1 day and are not hidden by the untouched list.
- The UK / euro-area 3-month rate replacement (7.10 item 2) must be a FREE source; it is not part of this work.
