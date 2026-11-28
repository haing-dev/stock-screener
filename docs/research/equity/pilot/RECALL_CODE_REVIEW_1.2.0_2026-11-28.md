# Independent review: tools/equity/wrds/eq_recall.py 1.2.0 (commit e6a8cab), before it runs on WRDS

Reviewer: Opus, read-only on the repo. Inputs: the 1.1.2 to 1.2.0 diff (git 0dcc1c8 to e6a8cab), RECIPE_v2.md x5 (with the v1
to v2 change tables), V04_REGISTRATION A13 item 24, RECALL_SPEC_v1, RECALL_CODE_REVIEW_1.1.0, the v2b report (for sizes).

## Verdict

- **pull() is SAFE to run** (eq_recall_pull_v3). The new SQL uses the right tables and columns. The filters match rc_idx
  (fdate = rdate, shares > 0). Each step is resumable per data set, and the result sizes are small.
- **run_part(3) is SAFE to run** (eq_recall_v3). There are **no blockers**. I found no look-ahead and no identifier in
  the output, and the statistics are unchanged. The v1 recipes are unchanged: the 1.1.2 code is untouched, and the
  smoke test shows all ten 1.1.2 recipes identical on the mock. Part 3 output is estimated at about 42,000 characters,
  under the 60,000 limit.
- **Two SHOULD-FIX items change the decisive pass set** (S1, S2). Both are small, and the results cannot be un-seen once
  the job runs. So I recommend deciding on them before eq_recall_v3 runs: either register a fix (a 1.2.1 line in A13)
  or accept them as stated readings. Neither one invalidates a run done as is.

Checks run (item 7):
- `python3 tests/eq_recall_smoke.py` -> **RECALL SMOKE OK**. This includes "1.2.0: all 10 1.1.2 recipes identical to
  eq_recall 1.1.2 on the mock" and "run_part(1)+(2)+(3) = run(), parts under 60,000".
- `seal_check.code_hash(file text)` = 9babac6eebab5c7be898d21da71a941839c31d65e7a8876360e204919d7febb8, which equals
  `code_sha256` for job "recall" in tools/equity/seal_exempt.json.
- `seal_check.py tools/wrdsq/jobs/eq_recall_v3.json` -> PASS; `eq_recall_pull_v3.json` -> PASS (lock 0057930e...).
- pandas 3.0.5 here; the smoke test passes on it.

## BLOCKER

None.

## SHOULD-FIX

**S1. zlatev_v2 year-3 EPS turns a forecast loss into a positive EPS (l. 1807).**
`y3 = FY2 x (FY2 / FY1)` when FY1 > 0. If FY1 > 0 and FY2 < 0, then y3 = FY2^2 / FY1 > 0, so the line
`p3.where(y3 > 0)` does not catch it. For example, FY1 = 0.10 and FY2 = -2.00 gives y3 = +40, which passes P1 at any
price up to 800.

The code follows the recipe text literally (RECIPE_v2 l. 18 / l. 53, and A13 item 24, both give the formula). But the
stated rule "year-3 EPS <= 0 = fail" and the intent ("carry consensus's FY1-to-FY2 growth one more year") clearly
exclude a company that consensus expects to lose money in FY2. The case is rare inside B4a / B4b, but it is a pure
artefact of the formula.

Fix: `y3 = np.where(P.fy2b <= 0, np.nan, ...)`, i.e. FY2 <= 0 fails the year-3 leg, the same as the FY2 cell (pfy2
needs FY2 > 0). Register it as a reading in A13 before the run. At minimum, add the count of decisive passes with
FY2 <= 0 to diag_zlatev_v2. Today that count is hidden inside "need the year-3 leg (price / FY2 not <= 20)".

**S2. stahl_v2 O05 = 0 is set when O05 is missing for any reason, not only when no index-manager holding exists
(l. 1056 with o05_at l. 1139-1146).**
`o05z = o05 if o05 present, else 0 if listed`. But o05_at leaves O05 missing in two other cases:
- the index managers do hold the stock, but CRSP has no row at t-3 (the `inner` merge with msf, l. 1143). This happens
  for a stock outside the COM filter at t-3: an OTC listing that moved to NYSE/AMEX/Nasdaq between t-3 and t, or a
  share-type change.
- CRSP shrout <= 0 or missing.

The stock is still in the 13F list (the index managers are filers), so it gets O05 = 0. That is "held by no index
manager", which is false. The registration says 0 only when "no index-manager holding is found". Expect few cases.

Fix: build a set of (permno, ym) with an index-manager holding from the matched rc_idx rows (`x` before the msf merge).
Then set `o05z = 0` only where listed AND not in that set; where an index holding exists but O05 cannot be computed,
leave it missing. This is a one-line change in o05_at (return the held set) plus one in recall_extra2.

**S3. The "provisional (split basis)" label is not given to zlatev_v2 (l. 2608).**
`extra` labels only zlatev_v1 and nygren_v1 when ibes.statsumu_epsus is unreadable. zlatev_v2's P1 uses the same
fy1b / fy2b / px_ib basis. Add `"zlatev_v2": ["P1 provisional (split basis)"]`. This has no effect now: the v2b pull
log says the unadjusted basis is readable. It matters only if a rerun cannot read the table.

## NOTE

N1. **Check 1, criteria against RECIPE_v2.** Except for S1 and S2, every decisive criterion matches its RECIPE_v2 text and
A13 item 24 on measure, cut-off, direction, comparison group, missing rule and universe:
- **druckenmiller_v2 (l. 1685-1707):** branch G = (GR3 >= 0.20 OR E04 >= 0.20) AND P02 > 0. Branch C = sector
  10/15/20/25 AND IND_NI < 0, where IND_NI is the sum of niq-TTM over the eligible rows of the GICS industry at t, with
  at least 3 present. A missing measure fails only its own side (fillna(False) before the OR). E04 is adjusted
  FY2/FY1 - 1 with FY1 <= 0 missing (l. 999). House set.
  - Minor: IND_NI sums per eligible LINE, so a company with two eligible share classes counts twice. This is the same
    as v1's IND_EBIT. Note only.
- **stahl_v2 (l. 1710-1735):** B1 as v1. B2 is C04s <= 1 and B3 is O05z below the sector median AND C04s < 1, with
  C04s = cshoq x ajexq now / 12 consecutive fiscal quarters before (l. 597-603). That is split-adjusted, and the ratio
  is invariant to later restatements of ajexq. B4 as v1. Own set (universe "all"), with the house set as a second line
  (also_house). Full form: 4 entry rules via stahl_v1_full (same flag names).
- **hohn_v2 (l. 1737-1769, 678-681):** A1 = not (sector 25 and group != 2540). A2 as v1. The B1 median of 10 consecutive
  years has denominator <= 0 -> +-1e9 by EBIT sign, and other missing -> -1e9. +1e9 with -1e9 in the 5th/6th places
  averages to 0, which fails. A pretax loss leaves the tax rate missing, so Q01 is missing and counts as -inf (same
  as v1's S04*). P1 needs V04 > 0 and a gap >= 0. B2 and B4 are full form only. A3 = v1 + group 2540.
  - Minor: the recipe says "sector 25 as GICS now defines it". Only the Media relabelling is undone. Pre-2018 names in
    IT that GICS moved into 25 in 2018 (internet retail from 451010) pass A1 before 2018. That matches the registered
    wording ("except industry group 2540"). Note only.
- **zlatev_v2 (l. 1771-1833):**
  - B1 is groups 4520 and 4530.
  - B3a is the median of same-sub-industry peers with a margin (>= 5), else the industry (>= 5), else that version's
    B1 set (_peer_thr).
  - B4a < 2 and B4b > 0.
  - P1 is unadjusted FY1/FY2 against the CRSP price at t as traded (l. 1004-1006). FY1 <= 0 or missing uses FY2 alone.
  - A1 as v1. The full form has 2 x 2 x 3 x 2 x 2 = 48 versions, with B3b and A2.
- **pilecki_v2 (l. 1835-1876):**
  - B1 = ROE present and rank > 0.30; P1 = group leg >= 0.70 OR own-history leg >= 0.70.
  - The own-history leg for 4010/4030 is the mean of both own ranks (NaN if either is missing); for 4020 it is the V02
    rank. A missing own leg leaves the group leg only.
  - A2, B2 and B3 as v1. Own set; B4 is not implemented and labelled.
  - Full form: B1 > 0.30 / > 0.5.

N2. **pil_history (l. 1063-1127) is correct as registered.**
- Window months t-60..t-1 (`A[i, m-60:m]`), at least 48 present, share of past values <= the value at t. A negative
  value at t ranks 0.
- Each past value as known then: CRSP permco value at that month-end, ccm link valid that month (primary preferred),
  quarterly accounts as-of avail <= month-end with the 270-day stale rule. That is the same rule as the value at t in E.
- No month after t-1 is read, and msf is cut at T1.
- **Is rc_msf0 enough for 2009-2010?** Yes. For t = 2009-12 the window is 2004-12..2009-11, and rc_msf0 covers
  2004-01..2006-12 with ref_msf from 2007-01 (no overlap, no gap). The binding input is the accounts, not prices:
  ref_fq and rc_fqx start at datadate 2004-01-01, so V02 (needs a 4-quarter TTM) exists from about 2005-01/03
  (calendar-year banks and insurers). That leaves 2-4 window months missing at the first quarter-ends, about 56 of 60,
  above 48. V07 (balance-sheet items) exists from about 2004-05. No extra pull is needed.
- rc_msf0 omits mthret. That is fewer fields than "same fields as ref_msf", which is harmless and means no return is
  read.

N3. **Check 2, look-ahead.** No new look-ahead.
- 13F list: rdate = t-3 (the last 13F quarter-end before t, filed by t), the same t-3 as o05_at. CUSIP is mapped
  through CRSP names valid at that rdate (l. 1050).
- Residual: s34 rows with fdate = rdate may include a filing submitted after t (a late filer). That only affects
  whether a stock counts as "listed by any filer", and it is the same convention as rc_idx and eq_conv. Negligible.
- I/B/E/S: latest statistic within 35 days before t (unchanged).
- GICS at t from co_hgic; today's code only in the existing v1 pil_groups mappings, which are labelled.
- rc_msf0 is used only in pil_history (grep confirms).

N4. **Check 3, pull SQL.**
- rc_msf0: crsp.msf_v2 with the same COM filter and casts as ref_msf, about 3 years x ~7k lines = ~250k rows.
- rc_s34sec_<y>: tfn.s34, `fdate = rdate and rdate between .. and shares > 0 group by rdate, cusip`. The 17 yearly
  steps cover rdate 2009-06..2025-06, which matches IDX0/IDX1 and t-3 for t in 200912..202509. About 20-30k CUSIPs per
  quarter, so about 100k rows per step.
- Runtime: rc_idx (same table and filter, restricted to index-manager mgrnos, 2009-2025 in one query) took about 94 s.
  An all-filer yearly query is probably a full scan plus aggregation of about 12-15M rows: an estimated 2-5 min per
  step, 40-80 min in total. Budget is 7000 s, and the budget is checked only before each step, so one step can run past
  it. Resumable: rerun eq_recall_pull_v3 (as v3b) until "ALL PULLS COMPLETE". Well within WRDS limits.
- Optional speed-up: `count(*)` in place of `count(distinct mgrno)` (nmgr is never used).
- Units: shrout is in thousands (x1000), and Compustat money is in millions (x1e6), consistently.

N5. **Check 4, v1 unchanged.** The diff from 0dcc1c8 only adds things or extends lists: TARGETS (v2 entries inserted,
v1 entries unchanged), VERSION, PARTS[3], _needed, load_inputs, the rq3 concat, the q01_med10 key, the recall_extra2
call, and evaluate's diag hook.
- No v1 function body changed. The new E columns (o05_listed, o05z, v02_own, v07_own, rq_c04s, q01_med10) are not
  read by any v1 recipe.
- TARGETS order does not affect numbers (the bootstrap seed is re-drawn per summarize call). rc_pass_* names are per
  recipe, so nothing is overwritten.
- The smoke test confirms all ten 1.1.2 recipes are identical on the mock.
- Side effect: run() and run_part(1/2) now also need the new pulls before they compute.

N6. **Check 5, statistics.** v2 blocks go through the same evaluate / summarize: seed 20261127, 2000 quarter draws, the
gate, control and reference baselines, the per-criterion table and the masked cross table.
- Every v2 block carries V2_LABEL ("revision after seeing recall v1: same purchases, not independent evidence") plus
  the v1 labels; the buy-rule coverage counts are updated to the v2 recipes (DRU 4 of 11, HOH 4 of 14).
- The four diagnostics (l. 1878-1912) print counts only: decisive passes and counted purchases on "either", by the
  registered split. recall_extra2 prints shares, and pil_history prints counts.
- pilecki_v2's P1h "measure missing" column checks v02_own only; for 4010/4030, v07_own can also be the missing one.
  Cosmetic.

N7. **Check 6, output.** No company, ticker, permno, gvkey or CUSIP is printed; stahl's CUSIPs stay inside the job.
Size estimate from the v2b report, per block:
- header about 1.8k; druckenmiller_v2 about 6.3k; stahl_v2 about 7.2k (house line + diag); hohn_v2 about 6.8k;
  zlatev_v2 about 7.8k (8 full_extra lines + diag); pilecki_v2 about 7.4k; summary about 2k; longer label lines about
  +0.5k per block.
- Total about 42k characters, under 60,000. The smoke test checks the parts under 60,000 on the mock.

N8. **Efficiency.** `_peer_thr` (l. 1779, 1783) uses `transform(lambda x: x.quantile(q))` over about 10k (quarter,
sub-industry) groups, 16 times. That takes seconds to a minute, which is fine. `groupby(keys).quantile(q)` mapped back
would be faster and avoids the UDF path for groups with NaN keys (it works on pandas 3.0.5 here; the WRDS pandas
version is not checked).

## Summary in plain terms

The new code is ready to run, and nothing in it would leak data or peek at the future. Two small rules behave
differently from what the recipes mean:
- For Zlatev, a company that analysts expect to lose money in two years can get a positive "year-3 earnings" figure
  and pass the price test.
- For Stahl, a stock that the index funds do own can, in rare cases, be scored as "owned by no index fund".

Both are quick fixes. It is best to decide on them before the run, because the results cannot be un-seen afterwards.
