# Independent re-implementation: Fortress

An agent that never saw the screener's code implemented the Fortress rules from their written text (validation/reimpl/fortress_rules.md) on the 38 real SEC samples, as of 2026-10-01. Its interpretation notes: validation/reimpl/independent_notes.md.

- Companies compared: 38
- Passing (PASS or PASS*): screener 10, independent 9, both 7
- **Jaccard of the pass lists: 0.58** (protocol: >= 0.9 with every difference explained)
- Rule outcomes agreeing: 424 of 455 (93%)

## Companies classified differently

| File | Screener | Independent |
| --- | --- | --- |
| hsy_companyfacts_subset.json.gz | PASS | FAIL |
| jnj_companyfacts_subset.json.gz | PASS | FAIL |
| tsm26_companyfacts_subset.json.gz | ONE | PASS* |
| tsm_companyfacts_subset.json.gz | ONE | PASS* |
| veev_companyfacts_subset.json.gz | PASS | FAIL |

## Rule outcomes that differ

| File | Rule | Screener | Independent |
| --- | --- | --- | --- |
| aapl26_companyfacts_subset.json.gz | F10 | PASS | NO DATA |
| aapl_companyfacts_subset.json.gz | F10 | PASS | NO DATA |
| abev_companyfacts_subset.json.gz | F5 | N/A | NO DATA |
| alab_companyfacts_subset.json.gz | F8 | FAIL | NO DATA |
| alab_companyfacts_subset.json.gz | F12 | NO DATA | FAIL |
| allo_companyfacts_subset.json.gz | F11 | PASS | NO DATA |
| asml_companyfacts_subset.json.gz | F13 | PASS | FAIL |
| fls_companyfacts_subset.json.gz | F9 | FAIL | PASS |
| hsy_companyfacts_subset.json.gz | F9 | PASS | FAIL |
| jnj_companyfacts_subset.json.gz | F7 | PASS | FAIL |
| jnj_companyfacts_subset.json.gz | F13 | PASS | FAIL |
| nvs_companyfacts_subset.json.gz | F3 | PASS | NO DATA |
| nvs_companyfacts_subset.json.gz | F4 | PASS | NO DATA |
| nvs_companyfacts_subset.json.gz | F5 | N/A | NO DATA |
| nvs_companyfacts_subset.json.gz | F7 | PASS | NO DATA |
| nvs_companyfacts_subset.json.gz | F13 | PASS | NO DATA |
| odfl_companyfacts_subset.json.gz | F10 | PASS | NO DATA |
| pool_companyfacts_subset.json.gz | F13 | PASS | FAIL |
| rrc_companyfacts_subset.json.gz | F6 | FAIL | NO DATA |
| rrc_companyfacts_subset.json.gz | F7 | FAIL | NO DATA |
| rrc_companyfacts_subset.json.gz | F8 | FAIL | NO DATA |
| rrc_companyfacts_subset.json.gz | F9 | PASS | NO DATA |
| rrc_companyfacts_subset.json.gz | F10 | PASS | NO DATA |
| rrc_companyfacts_subset.json.gz | F13 | PASS | NO DATA |
| sndk_companyfacts_subset.json.gz | F12 | NO DATA | FAIL |
| snow_companyfacts_subset.json.gz | F2 | FAIL | PASS |
| tsm26_companyfacts_subset.json.gz | F2 | FAIL | PASS |
| tsm26_companyfacts_subset.json.gz | F5 | N/A | NO DATA |
| tsm_companyfacts_subset.json.gz | F2 | FAIL | PASS |
| tsm_companyfacts_subset.json.gz | F5 | N/A | NO DATA |
| veev_companyfacts_subset.json.gz | F13 | PASS | FAIL |

Differences per rule: F13 6, F10 4, F5 4, F9 3, F7 3, F2 3, F8 2, F12 2, F11 1, F3 1, F4 1, F6 1

Each difference must be explained (a different but defensible definition, a data issue, or a bug) before this check counts as passed; explanations go below.

## Explanations

Result (2026-10-20): **check not passed** (Jaccard 0.58 < 0.9). Rule outcomes agree 93% (424 of 455), but five
companies are classified differently, and every one of them traces to a rule whose written text allows more than
one reading (agent's notes: validation/reimpl/independent_notes.md):

- **F13 inflation test (6 differences; JNJ, VEEV).** "-2% change in margin": percentage points or relative change,
  and which fiscal years count as 2021 and 2023. The text names neither.
- **F2 recent report (3; TSM x2, SNOW).** The text doesn't say whether "1.6 years" runs from the period end or the
  filing date. TSM's newest annual report isn't in SEC's XBRL data yet.
- **F5 2009 test (4).** "Younger than the recession" can't be read off the data for 20-F filers. The screener marks
  these N/A; the agent marked them NO DATA.
- **F10 interest coverage (4).** Which interest line to use, and what to do when interest expense isn't tagged
  (Apple after FY2023).
- **F9 leverage (3; HSY).** Net debt and EBITDA aren't defined in the text (cash only or with securities; which debt
  tags). To review: HSY and FLS, where the two definitions disagree on the side of the threshold.
- **F7 stable margins (JNJ).** Sample or population standard deviation (5.01 vs 4.75 against a 5.0 limit).

No screener bug is established; the finding is that the written rules underspecify the screen. Fix without
changing any rule: publish the exact definitions (ROIC, net debt, EBITDA, interest, FCF, fiscal-year labels,
standard deviation, missing-data handling) next to each rule. Then re-run this check with a fresh agent.
