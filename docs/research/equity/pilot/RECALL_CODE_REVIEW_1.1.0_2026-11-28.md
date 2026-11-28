# Independent review of eq_recall 1.1.0 (commit 7eb877d), before any 1.1.0 run

Read only on the repo. Reviewer did not write the code. Line numbers refer to tools/equity/wrds/eq_recall.py at 7eb877d.

## Verdict

- **pull() safe.** The four new steps (rc_fqx2, rc_funda2, rc_ibes2, rc_idx) use subscription tables only, store on WRDS,
  are skipped when already stored, and a failure prints FAILED without stopping the job. Nothing already stored is re-pulled.
- **run() safe as to leaks and look-ahead. No blocker.** No company, ticker, permno, gvkey, CUSIP or row is printed. Every
  input is known at t, except one point that the recipe itself requires: Pilecki's sector mapping uses today's GICS code (N8).
  No forward return is read anywhere.
- **kantesaria_v1 is unchanged.** Every function it uses is byte-identical to 1.0.3, or differs only by added columns and
  rows that its path filters back out. The smoke test reproduces 1.0.3's sections, summary rows and pass panel exactly.
- **Two should-fixes, best done before the run.** S1: the I/B/E/S share-basis mix-up gives wrong P/E-type pass flags for
  some stocks in decisive Zlatev P1 and Nygren P4. S2: the reference-book baseline (gate condition c5) cannot score banks or
  insurers, so it is close to meaningless for Pilecki and partly for Nygren. Two smaller should-fixes follow.
- `python3 tests/eq_recall_smoke.py` prints `RECALL SMOKE OK`. `seal_check.code_hash` of the file is
  db3651587e32f58ab9fdd6c9ba666d6a45fd725f6af8b062471b0cc8a9bbb276, which equals the `code_sha256` of job `recall` in
  tools/equity/seal_exempt.json. seal_check passes eq_recall_pull_v2.json and eq_recall_v2.json.

## BLOCKER

None.

## SHOULD-FIX

**S1. I/B/E/S estimates and CRSP price are put on different share bases (ibes2_at 946-954; used by zlatev_v1 P1 1284,
nygren_v1 P4 / G2-G4 1391, 1400-1402, sosin_v1 1476).**
- ibes.statsum_epsus is the *adjusted* summary file: every per-share figure is restated to the latest split basis of the
  WRDS vintage (pulled 2026-11).
- `padj_ib` puts the price at t on the basis of `cf_last`. That is the last CRSP factor in ref_msf, which ends 2025-12.
  - Any stock that split between 2026-01 and the I/B/E/S vintage gets a P/FY2 and a PV wrong by the split factor at
    *every* quarter-end 2009-2025. A 2:1 split doubles P/FY2, so the stock fails ZLA P1 and NYG P4 where it should pass.
  - CRSP's price factor also moves for some non-split distributions (spin-off type events) that I/B/E/S does not adjust.
    That is a second, smaller source of the same error.
- Not a look-ahead, because only bases are aligned. But the pass flags are wrong for an identifiable subset, and both
  criteria are decisive.
- E04 (FY2/FY1), the long-term growth input and the FY1 estimate count are basis-free and not affected. KAN v1's E01
  (reference book only) has the same issue but must stay as in 1.0.3.
- **Fix:** add a pull of `ibes.statsumu_epsus` (unadjusted; same query as `_ibes2`, fpi 1 and 2). In ibes2_at, compute
  `pfy2 = prc_t / fy2_unadj` and `pv = prc_t / V(unadjusted E1)` with no CRSP factor. Both are then on the basis of the
  statistic date, which is at most 35 days before t.
- **Minimum alternative:** keep the method, label ZLA P1 / NYG P4 "basis: I/B/E/S vintage vs CRSP 2025-12", and report the
  results as provisional.

**S2. Reference-book baseline for the recipes with house exclusions off (rank_panel 750; evaluate 1859-1861; gate c5
1948).**
- rank_panel scores only rows that are not excluded, so every bank (4010), insurer (4030), pre-2016 4040, sector-60 and
  biotech row has `sec_pct` = NaN, which means ref = False.
- Pilecki buys almost only banks, insurers and 4020 names. Baseline (2) therefore has recall of about 0 on his purchases
  and condition c5 ("lift above the reference-book baseline") passes by construction. The same happens, in part, to
  Nygren's bank purchases.
- The base rate of `ref` in the sector-40 cells is also diluted by unscorable rows.
- **Fix:** for `universe == "all"` recipes, compute the reference score on the recipe's own set: the same
  `rank_panel` code without `~u.excluded`, inside-sector percentile.
- **Minimum alternative:** print the share of counted purchases with no reference score. When that share is above 50%,
  print c5 as "not informative" rather than yes.
- Register either choice before the run.

**S3. Pilecki fallback group is ranked only among the fallback names (pilecki_v1 1329-1331).**
- The recipe says: when a group has fewer than 10 members, "rank inside sector 40 instead".
- The code relabels the small group's members `cmpg = "40"`. pct01 then ranks them only among themselves, not among all
  eligible financials.
- Checked on a hand case: 10 banks + 4 insurers gives the insurers ranks 0 / .33 / .67 / 1 among themselves.
- Probably no effect in practice, because each of 4010 / 4020 / 4030 has well over 10 eligible names among the 1,500
  largest. But the code does not do what the recipe says.
- **Fix:** for fallback rows, take `pct01(v.where(fin), [P.yyyymm])` (all financials at t). Print the number of
  group-quarters that fall back.

**S4. Sosin line prints a 13F filer number (run 2057-2058).**
- RECALL_SPEC_v1 says the job prints "no investor id beyond the masked label". The line prints "13F filer 21801".
- It is a public filer number, not WRDS row data, so this is low risk.
- **Fix:** drop the number from the printed line and keep it in the registration; adjust the smoke assertion at
  tests/eq_recall_smoke.py (the "Sosin: not in eq_conv_panel ..." check).

## NOTE

N1. **Li Lu on the house set (RECIPES 1628).** The recipe's section 0 says "No industry is excluded" and adds that banks
and insurers "usually have B1 missing and fail by construction". That wording reads as if banks were meant to be in the
set. Under the registered house set, his bank purchases (e.g. a large money-centre bank, a regional bank) are dropped
from the count, not counted as misses, so recall is higher than under the recipe's own reading. This is a registered
judgement (A13 item 21), and the dropped count is printed ("in a house-excluded industry ... not counted"). Read that
line. Consider reporting Li Lu on both sets. Druckenmiller on the house set is in line with his recipe ("only if the pilot
universe requires it").

N2. **The spec text conflicts with the registration.** RECALL_SPEC_v1 still says insurance is excluded "in every pod,
recipe or not". A13 item 21 overrides this for pilecki_v1 and nygren_v1. Add a one-line amendment to the spec so the
record agrees with itself.

N3. **Base-rate definition.** For the house-set recipes, cells are exactly 1.0.3's (same rows, same order, same
`rank(method="first")`). For pilecki_v1 / nygren_v1, the size thirds of sectors 40 and 60 (and 35, with biotech) are
taken over the wider set. The definition is unchanged ("eligible stocks at the same t, sector, size third"); only
"eligible" is the recipe's own set. Purchases, base rates, the control baseline and the cross table all use the same set,
so this is internally consistent.

N4. **Stahl B4 (1198-1201).** A stock with no I/B/E/S match (a link failure, or no statistic within 35 days) has n1
missing. It is counted as "no estimate = 0" and passes B4, and so passes B3|B4. This raises recall and base alike. n1
coverage is in the section 1 table; read it before trusting the Stahl level.

N5. **Stahl O05 (957-973).**
- Timing is correct: 13F `rdate` = t-3 months, `fdate = rdate` (first vintage), filed by t. Units are correct: s34 shares
  are in units, CRSP shrout in thousands x 1000.
- "None found = missing = fails" is the registered reading; in the 1,500 largest a miss is mostly a CUSIP gap.
- Name patterns can pick up several BlackRock filing entities in the same quarter (double counting). This shifts the
  level, but only the within-sector rank is used.
- Suggest printing the median `nmgr` per quarter-end (already pulled, not used) to show gaps or jumps in the manager set.

N6. **Index-manager name print (pull 318-321).** The printed names are 13F filer names of the index managers only (public
SEC filer names; the same kind of output as eq_match). Acceptable.

N7. **Li Lu full form b2_12 (905-907, 1440).** The literal reading makes the low12 version always true, so that version
is "no B2". This is registered. Another reading ("made a new 12-month low within the last 12 months") would need 23
months of prices. Reported only.

N8. **Look-ahead through today's GICS: Pilecki only (pil_groups 1307-1315; recall_extra 1001-1009).**
- Nygren does not use the today's-code columns.
- Pre-2016 group 4040 names and pre-2023 45102020 names are classed by their last co_hgic spell. The recipe states this
  rule itself.
- Effect: survivorship in the classification. A payment processor or mortgage REIT that disappeared before 2023 / 2016
  keeps its old code and fails A1.
- Small for his purchases; not a return look-ahead.

N9. **Hohn percentiles (1236, 1239).** S02 and S03 sector percentiles are taken over the whole eligible set at t, before
A1 / A2 (the registered general rule). The recipe's "AVOID -> BUY -> PRICE" order could be read as ranking after the
exclusions. It matters in sectors 30 and 40 only.

N10. **Nygren A2 missing = excluded (1395).** This is registered. It excludes names with fewer than 13 consecutive
quarters of accounts.

N11. **Memory.** The kantesaria_v2 full form is 1,296 boolean columns over about 75k rows. `attach` runs a groupby mean
over all of them three times. A synthetic test of the same size peaked at about 1 GB, which is fine on WRDS Cloud.

N12. **Fragile order of calls.** recall_quarter_measures2 relies on recall_quarter_measures having already made
intanq numeric on the same frame (build_panel 692-693). It is correct as written.

## Checked correct (recipe by recipe, decisive form against the recipe text)

**kantesaria_v2**
- Decisive form: B1, B2, B3 (whole-set median before AVOID), B5 on 5 fiscal years (`g06_5`), B6, P1 (FCF after share pay
  minus the 10-year Treasury), A1-A4 with the v1 codes.
- A5 is excluded only when both 3-year windows are > 0.50. `c06_prev` = `lag(c06, 3)` covers fiscal years t-5..t-3.
  Missing = fails. The strict variant applies to both windows.
- B4, P2, P3 are full form only.
- Full form: 3x3x3x2x3x2x2x2 = 1,296 versions, with B9, B10 and A7 in every one. A10 is the v1 one-window reading.

**druckenmiller_v1**
- G = GR3 >= 0.20 AND GR1 >= 0.20 AND P02 > 0. GR3 with a base <= 0 is missing; an end value <= 0 counts as -100%.
- C = sector in {10, 15, 20, 25} AND the industry EBIT TTM sum < 0, with >= 3 members having EBIT, over the eligible set.
- No price criterion. A1 is a weight rule, correctly not implemented.

**stahl_v1**
- B1: Q06 > 0 OR B04 >= 0. B2: C04 (cshfdq x ajexq against 12 quarters before) <= 1.
- B3: O05 below the sector median AND C04 < 1. B4: n1 below the sector median, with none = 0 passing.
- Full form: 4 entry rules; the other 32-version dimensions change ranking and size only.

**hohn_v1**
- A1 and A2 use the exact GICS codes. B1: S04* = 10 of 10, with the denominator <= 0 AND EBIT > 0 branch.
- B1i: 20305010 / 20305020 AND S01 = 0.
- B2: S02 sector percentile <= 0.5. P1: V04 > 0 and V04 - 10-year Treasury >= 0.
- Full form: B4, A3, P1g 0 / 1 / 2.

**zlatev_v1**
- B1: industries 453010, 452010, 452020. B3a: >= median of the B1 set at t. B3b: >= 0 (8 quarters).
- B4a: B01 < 2 (EBITDA <= 0 fails, net cash passes). B4b: Q06 > 0. P1: P/FY2 <= 20 (FY2 <= 0 fails); see S1.
- A1 uses the six industries.
- Full form: 24 versions with A2.

**pilecki_v1**
- A1: the 2023 structure as the recipe states.
- B1: ROE rank > 0.5, missing = 0.5. B2: banks and insurers only; base <= 0 is missing; missing dividends = 0.
- B3: P02 > 0. P1: re-ranked value score >= 0.70. A2: new 12-month low, with ties counting as a new low and missing =
  fail.
- B4 is registered NOT IMPLEMENTED and labelled on every block. Full form: B1 at 0.5 / 1/3.

**nygren_v1**
- B1: best rank <= 250 over the eligible set. B2: V10 + g >= 8%. V and PV as in recipe section 0.
- r = max(8%, 10-year), flagged. g is clipped to [0, 10%]. Long-term growth is read as percent / 100. FY1/FY2 NTM
  weighting as registered.
- A1-A3 as the recipe states. Full form: 10 books, with G5-G9 equal to the decisive book.

**lilu_v1**
- B1: Q02 sector percentile >= 0.667. B2: the 12-month low falls in t-2..t.
- P1: B/P >= 1 OR P2: EBIT/EV sector percentile >= 0.8.
- A1 (accruals, reversed < 0.2) and A2 (operating-margin deviation > 0.8): missing = not excluded.
- Full form: 10 versions.

**Look-ahead**
- Quarterly items are used from rdq + 1 day (else datadate + 45 days), stale after 270 days. Annual items are used from
  datadate + 90 days, stale after 550 days.
- I/B/E/S: statpers <= t and within 35 days. 13F: rdate = t-3.
- Prices: all windows end at t (P02 = t-5..t-1, at least 4 of 5). Monthly data are cut at 2025-09 and no forward return
  exists.
- GICS is taken at t (co_hgic spells), apart from N8. The Treasury is the last value on or before t; the job stops on any
  gap.

**Pull SQL**
- comp.fundq cshfdq / ppentq / dvpsxq and comp.funda seq / mib / txt / pi go through `_select_existing`.
- ibes.statsum_epsus: fpi '0' / '1' / '2', measure EPS, with fpedats and numest.
- tfn.s34 (fdate = rdate, shares > 0) for the mgrnos found in tfn.s34names (the table is used by eq_match).
- CUSIPs are normalised to 8 characters on both sides. gvkey goes through keynorm on both sides. Every merge is a left
  merge on deduplicated keys, so no row is added.

**Statistics (RECALL_SPEC_v1)**
- Purchases are evaluated at the quarter-end before. Versions a and b are averaged; the 20-purchase floor applies per
  version.
- Cells are quarter x sector x size third on the recipe's set (N3).
- Bootstrap: 2,000 quarter draws, seed 20261127 for every investor, 5th-95th percentiles.
- The gate is unchanged. Baseline (1) is pooled control and baseline (2) the reference top fifth (see S2).
- Per-criterion shares and the masked cross table are as in 1.0.3.

**kantesaria_v1**
- Unchanged from 1.0.3: quarterly_table, account_measures, recall_quarter_measures, ibes_revision, rank_panel,
  price_measures, treasury_at, attach, summarize, investor_purchases, load_conv, sets_for, kantesaria_v1 and its entry
  function.
- Changed only by additions: annual_table (new columns), build_panel (new quarterly columns), recall_panel (keeps the
  excluded rows, which recipe_set removes again; cells moved to add_cells with the same code).
- The smoke test passes against 1.0.3 read from git; b51b623 = 818a5f8 for this file.
