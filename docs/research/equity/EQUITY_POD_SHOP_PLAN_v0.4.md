# Equity pod shop: plan v0.4 (2026-11-20)

Status: plan and registrations. Nothing in it has been built or run. It replaces plan v0.3 where they differ;
v0.3 and the design annex v0.2 stay in force for everything not restated here (section 12 lists the amendments).
Sources of the changes: the user's direction of 19 Nov and feedback of 20 Nov
(`EQUITY_BUILD_STRUCTURE_PROPOSAL_v0.1.md`), the independent review of v0.2
(`EQUITY_POD_SHOP_DESIGN_v0.2_review.md`, must-fixes M1-M6 and the should-fixes that touch them), the roster read
(`hf_leaderboard/ROSTER_SCREENABILITY_2026-11-20.md`). The registered rules are in `V04_REGISTRATION.md`.
Not yet checked by an independent agent (section 13).

## 1. Goal (user, 2026-11-19)
About 30 top investors, each with transcripts and a 13F holding history with conviction (largest weights), are
turned into a book of strategies (screens). Each strategy picks stocks from one like-for-like company table,
runs as a paper portfolio and is tested on history and forward, to see which strategies outperform consistently.
The work is done by independent pods and desks that check each other; it is data-driven and registered before it
is run.

## 2. What changed against v0.3
| # | Change | Why |
|---|---|---|
| 1 | Roster rule v2: record on 2011-25 or on the 5-year leaderboard, process material, and a new **screenability** gate | User: an investor is useful only if a screen on calculable measures can be built from what they say |
| 2 | Main test period **US 2010-01 to 2025-12** (was: design years before 2011, 2011+ sealed) | User: older years are another market and most funds did not exist |
| 3 | Three same-period checks replace the missing clean sample: outside the US, control-investor pods, source holdings left out | The roster is chosen on the test years |
| 4 | Company data from **LSEG first** (history 2010+ and live, read on the PC); WRDS for 13F holdings and as cross-check | User preference; one source for backtest and live |
| 5 | Holdings module widened to **conviction** (weight rank, new positions, additions, holding time) | User direction |
| 6 | Tracker and reference book go live early; owner panel on the tracker | User direction |
| 7 | "Follow the best managers" is a registered pod, not a filter on other pods | 13F records did not persist in the scorecard |
| 8 | Valuation is a version of a pod, plus a display panel | Proposal 6.5 |
| 9 | Review must-fixes M1-M6 applied (section 8) | Review |

## 3. Structure: five desks and a referee
| Desk | Produces | Built by | Check by someone else (gate) |
|---|---|---|---|
| 1. Roster and evidence | Roster by rule v2 and the control group of 10. Per investor: claim ledger (verbatim quotes), conviction holdings history from 13F, investor card | Scripts; Sonnet extracts; WRDS job for holdings | Every quote found in the text by script; Opus re-reads a fifth blind; say-do table (each stated criterion against what conviction purchases looked like the quarter before purchase) |
| 2. Strategy book | One pod per strategy family: charter (why it should pay, who is on the other side), then a spec a script can run. Every threshold tagged quote / revealed by purchases / convention / grid; open choices are versions that are averaged | Fable judges map and charters; Opus writes specs | Opus checks charters against the quotes; a fresh agent rebuilds each screen from the spec alone (rank correlation at least 0.95, list overlap at least 0.9); screenability measured |
| 3. Company data | Field dictionary (`FIELD_DICTIONARY_v0.1.md`): one written definition per measure, as known on the day, ranked inside the sector. LSEG files on the PC, one loader, one lock | Opus; PC runner | No copied or doubled series; cutting the data at any date leaves earlier scores unchanged; 20 hand checks per measure against filings; cross-check against WRDS on a sample (rank correlation at least 0.9) |
| 4. History tests | Each pod as a rule-based portfolio on one test sheet against the reference book. Verdict classes: Passed on history, Sleeve, Exclusion, Incubator, Shelved | Scripts; verdict by script | Number of counted tests fixed first; no re-runs with tweaks; doubled costs; 1,000 random portfolios of the same shape; results recomputed by a second implementation; trial log |
| 5. Live tracker and paper book | Tracker: every company with its measures, a valuation panel, the screens it passes, the owner panel (roster's latest 13F moves and largest weights, with the filing delay). Paper portfolio per registered pod in an append-only ledger. Analyst notes as dated forecasts | PC runner and scripts; Opus analysts; Sonnet report | Monthly check that each paper portfolio equals its frozen rule; refresh differences logged; forecasts scored by script |
| Referee | Registration log, lock ids, trial count, scoreboard with the number of trials behind each line | Scripts; a session that does none of the judged work | Checkers tested with planted errors; every result carries spec, engine and data-lock versions |

## 4. Fences
1. One pod, one team, one private folder. No agent that writes claims, cards, charters or specs is given any return.
2. Strategy writers see masked investor ids and only what conviction purchases looked like before the purchase
   (aggregates over at least 20 purchases), never names or later returns.
3. No step grades itself: a different model checks each step; verdicts come from scripts and registered rules.
4. Agents write rules; they never pick stocks in a backtest. Agent judgement is recorded as dated forecasts and
   judged on the live record only.
5. The control group and the placebo go through the same pipeline.
6. Test slots are given by a script on rules fixed beforehand (v0.2 8.5 as amended in section 8), not by how
   promising a pod looks.
7. New with the 2010-2025 test period: return data of 2010-2025 are opened only by the test desk's scripts in
   counted runs. Company measures (accounts, estimates, prices as levels) may be read by every desk; portfolio or
   signal returns may not. Each run is logged in the trial log before it starts.

## 5. Roster (rule v2; registered in `V04_REGISTRATION.md` R1)
An investor enters the roster when all three hold:
1. **Record.** Top 40% of all measured managers on 2011-25 in the scorecard (`rank_share` at least 0.60, at
   least five years of record; 13 of the 21 are in the top quarter, 3 between 0.60 and 0.75, 5 enter on the leaderboard), or top 50 of the 5-year leaderboard 2021-25.
   The bar is the lowest record among the 21 accepted on 20 Nov and is fixed from here on.
2. **Material.** At least one long document in which the investor explains the method in their own words.
3. **Screenability** (new). The investor's stated criteria allow a screen on consistently calculable measures.
   First read: grade A or B in `roster_screenability_2026-11-20.csv`. Measured in the pilot: at least half of the
   stated criteria can be computed by a script from the field dictionary, and the calculable part selects stocks
   on its own. An investor who fails the measured gate leaves the roster and goes to the analyst notes.

Roster at registration: 21 investors (7 grade A, 11 grade B, 3 borderline to be settled in the pilot); 16
judgement-led investors set aside; 9 places open, filled only by investors who pass all three bars. The control
group of 10 (drawn at Stage 0) stays. Every investor keeps the record rank, so the tests can show whether rank
mattered. The roster orders the reading and defines the pods; it is never evidence that a pod works.

Families expected from the 21 (to be settled by the strategy map): quality compounders; cheap and good;
owner-operators and hard assets; cyclicals at the trough; growth and technology adoption; financials; growth at
a set expected return.

## 6. Conviction holdings (WRDS 13F; registered in R2)
Source `tfn.s34` first versions (Stage 0 table check). Per roster and control investor and quarter-end
2009-12 to 2025-12: weight of each holding, weight rank, new position, addition, reduction, exit, quarters held.
A **conviction purchase** is a new position or an addition that (version a) puts the stock among the five
largest weights, or (version b) adds at least 1% of the portfolio. Both versions are computed and averaged.
Outputs: per investor the conviction list (stays on WRDS), and for the strategy writers only aggregates of what
conviction purchases looked like at the end of the quarter before purchase (sector rank of each measure, at
least 20 purchases per cell, odd years set a threshold, even years check it). The job is a registered descriptive
job (seal-exempt, logged, code hash).

## 7. Data plan
| Need | Source | Note |
|---|---|---|
| Company accounts 2008-2026, annual and quarterly, **as first reported**, with announcement dates | LSEG Workspace (`TR.F.*`, `ReportingState=Orig`) | Two years before 2010 for growth and averages; longer lookbacks (5 and 10 years) need 2000+ |
| Consensus as it stood, actuals, report dates | LSEG (`TR.EPSMean` and relatives) | Monthly snapshots |
| Prices, total returns, market value, volume, monthly; daily where a measure needs it | LSEG Workspace and Datastream | Dead companies by ISIN; Datastream pads dead series flat (cut at the delisting date) |
| Company list incl. companies that died 2010-2025 | Workspace screen active or inactive (retire dates from 2006) and Datastream dead lists | Counts per year checked against CRSP delistings |
| Sector | GICS from LSEG; history of the code if available, else current code with a logged limit | Review S6 |
| Short interest, free float, insider and institutional ownership | Datastream / Workspace | Coverage to be shown by test file 2 |
| Managers' holdings | WRDS 13F (`tfn.s34`); SEC 13F files for the live owner panel | Not on LSEG |
| Cross-check | WRDS (CRSP, Compustat, I/B/E/S) on a sample of company-months; results only come back | WRDS rows stay on WRDS |
| Outside the US (same-period check) | LSEG developed markets, pulled only before the freeze | Review section 4 |

Rules: the user states that WRDS and LSEG data may be used freely as long as nothing is published; the site has
a password; the work is not commercial. LSEG files stay on the PC and out of the repository; agents may read
LSEG figures; the tracker shows them behind the password. WRDS keeps its own written term on AI tools, so WRDS
jobs return results, not rows. Point in time: a figure is usable from its original announcement date plus one
trading day; where the date is missing, period end plus 90 days (annual) or 45 days (quarterly).
The file plan (how many workbooks, how many companies per file) is written after test file 2
(`docs/data_requests/lseg_equity_probe2_2026-11-20/`) is read back.

## 8. Test sheet (registered in R3-R6; review M1-M6 applied)
**Portfolios.** Long book of a pod = the stocks its spec selects, held in 12 monthly tranches; each tranche is
formed once and held 12 months; at each monthly review a holding whose rank has left the top two groups is sold
early (M3). Weights equal inside a tranche, position cap 2.5%. The long/short form of v0.2 (sector- and
market-neutral, shortable set, borrow fee) is computed for every pod as well; the **decisive form is long-only
against the reference book and the sector-matched universe**, because the user's use is a paper portfolio of
long candidates. The long/short form is a reported line.

**Reference book v1 (M2).** Registered before Batch 0 from sources published before 2011 only: value (earnings
yield and book to price), momentum (12 months skipping the last), quality (return on equity, accruals, the
Piotroski score), expectations (analyst revisions over three months; a slow form, since the published horizon is
under three months). Ranked inside the sector, equal weight across the four groups, same construction as a pod.
Measures defined in the field dictionary; no post-2010 study may add, drop or redefine a measure. Any change
starts a new live record (v2) while v1 continues on paper.

**Five decisive tests** (each on the added return of the pod over the reference book, after costs):
1. Added return above zero: regression alpha on the reference book, p-value from the registered whole-month
   bootstrap, Holm at 2.5% per batch.
2. Eras (M1): in each era of at least 60 months (2010-14, 2015-19, 2020-25) the point estimate of the added
   return is not below zero by more than one standard error of that era's estimate (Newey-West). The power table
   reports the joint pass rate of tests 1 and 2.
3. Added return above zero at doubled costs.
4. Placebo (M6): 1,000 random portfolios with the pod's number of names per sector, its average holding period
   and the same costs. Statistic: the added return of test 1. Pass: above the 95th percentile.
5. Tail: the worst fall of book plus pod is not worse than the book's by more than 2 points, the worst month by
   more than 1 point.

**Three same-period checks** (new; reported with every verdict, and required for "Passed on history"):
- A. Outside the US: the same spec on developed markets outside the US, 2010-2025, run once after the freeze.
  Pass: added return above zero (point estimate).
- B. Control: the pod's added return is above the 90th percentile of the pods built by the same pipeline from the
  control investors (pooled over control pods and their versions).
- C. Source holdings left out: the pod is re-run with every stock removed in the quarters in which one of its
  own source investors held it among the conviction holdings. Pass: the added return keeps its sign and at least
  half its size.

**Classes.** Passed on history = five tests and checks B and C pass (A is added at the freeze). Sleeve, Exclusion,
Incubator, Shelved as in v0.3. No investor pod is called Core on history: the roster and almost every thesis come
from the test years. Core is given by the live rule only (v0.3 8.2).

**Budget.** Batch 0 (plumbing; reference book signals checked in their published form), Batch A (hygiene of the
reference book, targets named at registration), B1 and B2 (at most 4 pods each = 8 counted slots, Holm 2.5% per
batch). Every other pod gets one descriptive run (Incubator at most). Power check before a slot is given: pass
rate of tests 1 and 2 at an added information ratio of 0, 0.3 and 0.5 on 192 months; under 50% at 0.5 = no slot.

**Other review fixes.** M4: stress episodes inside the test period run in the counted runs only; cross-source
score checks on later months are rank correlations only. M5: no design era before the data exist; years before
2010 are a side check on WRDS (2001-2009), reported, never decisive, and only for measures whose inputs exist.
S1 definitions as written in tests 1, 3 and 5. S9: a missing measure takes the sector median score; a stock
missing more than half of a pod's measures is not ranked. S12: nominal account size $10m for cost and liquidity
limits.

## 9. What stays unseen, and what is honest to claim
- The US years 2010-2025 are no longer a holdout. The 2026 months before a pod goes live are run once at the
  freeze and reported; the live record is the final word.
- A pass on history means: the rule added to the reference book in the same years in which its investors were
  chosen, outside the US, against control investors, and without its investors' own holdings. That is weaker than
  an untouched sample and it is stated on every scoreboard line.
- Live returns are slow evidence (a pod adding 3% a year needs roughly 10 to 30 years alone). Early live evidence
  is the machinery, the business-outcome links and pooled comparisons (v0.3 section 12).

## 10. Build order (user paces the steps)
| Step | What | User does |
|---|---|---|
| 1 | Plan v0.4 and registrations (this file) | - |
| 2 | Field dictionary v0.1 and LSEG test file 2 | Refresh one workbook |
| 3 | LSEG data files (count set by step 2); loader, lock, checks | Refresh the files |
| 4 | WRDS 13F conviction holdings job | One login |
| 5 | Engine, reference book v1, Batch 0, second implementation | - |
| 6 | Pilot end to end: Greenblatt, Terry Smith, Zlatev and one control investor (claims, conviction holdings, say-do, card, spec, blind rebuild, screenability measured) | - |
| 7 | Tracker v0 and the reference book live on paper | Set the site password |
| 8 | Strategy map, charters, specs, registration, tests; roster filled as investors pass | - |
| 9 | Paper portfolios per registered pod; freeze; outside-US run; scoreboard | - |

## 11. Limits
- Thresholds "revealed by purchases" come from the same years as the test. Check C and the odd/even-year split
  limit this; they do not remove it.
- LSEG history as first reported is one vendor's record; the WRDS sample check is the only second opinion.
- Sector and theme investors (Zlatev, Pilecki, Kantor) give sector pods with few names; they can reach Incubator
  and the live record, rarely a counted slot.
- Most rule layers will prove to be known factors; then the reference book, the exclusions and the tracker are
  the product.

## 12. Amendments to v0.3 and v0.2
| Where | v0.3 / v0.2 | v0.4 |
|---|---|---|
| v0.3 5.3 tier rule | Tier A = 40 by record and explicit criteria | Roster rule v2 (section 5); tiers stay as the reading order of the library |
| v0.3 6 holdings module | Sector ranks of purchases | Conviction purchases (section 6) |
| v0.3 8.2 samples; v0.2 4.2 | Design US 1975-2010, holdout 2011+ | Main period US 2010-2025 with checks A-C; 2001-09 side check; live final |
| v0.3 8.1; v0.2 10 | Five tests on the long/short book | Tests as in section 8, long-only decisive, long/short reported |
| v0.3 9 data | History on WRDS, LSEG second source | LSEG first, WRDS 13F and cross-check |
| v0.3 8.2 "Core on history" | Reference book only | Unchanged; investor pods "Passed on history" at most |
| v0.2 5 reference book | Final list at E3.5 | v1 registered before Batch 0 (M2) |
| v0.2 9.2 steps 6-7 | Tranches and band | M3 wording |
| v0.2 9.3, G7 | Stress on 2020/2021 in Batch 0 | M4 |
| Seal (`SEAL_LOG.md`) | US 2011+ sealed until the freeze | Returns of 2010-2025 opened only in counted runs (fence 7); outside US sealed until the freeze; WRDS reader unchanged until the engine exists |

## 13. Checks still due
An independent Opus check of this plan and of `V04_REGISTRATION.md` (on the user's go; no subagent was used for
this version). Points to test first: power of tests 1-2 on 192 months; whether check B has enough control pods to
give a 90th percentile; the size of check C's removal; the point-in-time rule on LSEG announcement dates.
