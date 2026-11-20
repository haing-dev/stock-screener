# Equity build structure: proposal v0.1 (2026-11-19)

Status: SUGGESTION ONLY. Nothing here is built, registered or run. It becomes plan v0.4 on the user's go.
Builds on `EQUITY_POD_SHOP_PLAN_v0.3.md` (pipeline, test sheet, samples, fences), its annex v0.2, the review of
18 Nov (`EQUITY_POD_SHOP_DESIGN_v0.2_review.md`), the scorecard (`SCORECARD_RESULTS_2026-11-18.md`), the hedge fund
leaderboard and the foundation ranking (`hf_leaderboard/`).

## 1. The goal, in the user's words (2026-11-19)
"We will use a list of maybe top 30 investors, each with their transcripts, holding history with conviction (those
tickers with larger weight), to build a book of strategies (like the 'screeners' we built before) and then trying to
find stocks from that screeners to build a book of portfolio and backtest them both historically and looking
forward, to see which strategies consistently outperform. The purpose is to have an effective agentic workflow that
are independent, non-biased that act like independent pod shops, from reviewing foundational logic of these
investors, then use company data pulled from wrds/lseg, standardize them to build a reliable, consistent tracker
with like for like metrics to identify the good investment candidates at attractive valuation (also actively
considering what top investors are buying latest in their 13f), then build the paper portfolio with backtest. The
design should be scientific, data-driven with cross verification between steps."

## 2. Verdict
Plan v0.3 already is this pipeline (transcripts and holdings -> strategy specs -> one test sheet -> live paper
book), and Stage 0 of it is done. The proposal keeps it and changes five things (section 6). The structure below
restates it as five desks and a referee, so that every step has an owner, an output and a check by someone else.

## 3. Structure
| Desk | Produces | Built by | Cross-check (gate) |
|---|---|---|---|
| 1. Roster and evidence | Roster: 30 investors by the user's rule (5-year return on the leaderboard, gated by process material) + the random control group of 10 already drawn. Per investor: claim ledger (verbatim quotes of what they say they do), conviction holdings history from 13F (largest weights, new positions, additions, holding time; 13D filings for stakes above 5%), investor card | Scripts; Sonnet extracts; script on WRDS for holdings | Every quote found in the text by script; Opus re-reads a fifth blind (agreement on record); WRDS 13F compared with the SEC's own files; say-do table: each stated criterion against what the conviction purchases looked like at the end of the quarter before purchase (agrees / silent / contradicts) |
| 2. Strategy book | One pod per strategy family (several investors, one mechanism): charter (why it should pay, who is on the other side), then a spec a script can run. Every threshold is tagged quote / revealed by purchases / convention / grid; open choices become versions that are averaged, never picked. The 14 archived screens and the 3 triage screens enter as candidate families | Fable judges the map and charters; Opus writes specs | Opus checks charters against the quotes; a fresh agent rebuilds each screen from the written spec alone (rank correlation at least 0.95, list overlap at least 0.9; the old Fortress screen reached 0.58); the pod's long list must hold the family's actual purchases at three times the universe rate |
| 3. Company data | Field dictionary: one written definition per measure (valuation, profitability, growth, balance sheet, revisions, price), as known on the day, ranked inside the sector so companies compare like for like. Built on WRDS for history and on LSEG (PC) plus free SEC and price data for today | Opus; WRDS and PC runners | Market and factor returns match the published ones; cutting the data at any date leaves earlier scores unchanged; no copied or doubled series; WRDS-built and LSEG-built scores agree (rank correlation at least 0.9) before anything goes live; 20 hand checks per measure against filings |
| 4. History tests | Each pod as a rule-based portfolio on one test sheet, measured against a plain reference book (value, momentum, quality, expectations; sources before 2011 only). Verdict classes: Core, Sleeve, Exclusion, Incubator, Shelved | Scripts on WRDS Cloud; verdict by script | The number of tests that count is fixed and registered first; no re-runs with tweaks; doubled costs; 1,000 random portfolios of the same shape as placebo; results recomputed by a second implementation; every run counted in a trial log |
| 5. Live tracker and paper book | Tracker: every company with its like-for-like measures, a valuation panel (against its own history and its sector), which registered screens it passes, and the owner panel (the roster's latest 13F moves and largest weights, with the filing delay). Paper portfolio per registered pod in an append-only ledger. Analyst notes as dated forecasts | PC runner and scripts; Opus analysts; Sonnet report | Monthly check that each paper portfolio equals what its frozen rule gives; data refresh differences logged; forecasts scored by script at registered checkpoints |
| Referee | Registration log, seal and lock id, trial count, scoreboard, league table of every measured pod with the number of trials behind it | Scripts; a session that does none of the judged work | Checkers are tested with planted errors; every result carries the spec version, engine version and data lock |

## 4. What keeps the pods independent and unbiased
1. One pod, one team, one private folder. Pods do not see each other's specs before registration, and no agent that
   writes claims, cards, charters or specs is given any return.
2. Strategy writers get investor ids with names masked, and see only what conviction purchases looked like before
   the purchase (aggregates over at least 20 purchases), never the names or what happened after: the models already
   know which stocks rose.
3. No step grades itself. A different model checks each step; verdicts come from scripts and registered rules.
4. Agents write rules; they never pick stocks in a backtest. Agent judgement (moat, management, thesis fit) is
   recorded as dated forecasts and judged on the live record only.
5. The control group and the placebo go through the same pipeline, so the result shows whether choosing investors by
   return helped at all.
6. Slots for registered tests are given by a script on rules fixed beforehand (thesis grade, material, say-do
   agreement), not by how promising a pod looks.

## 5. Data routes
- History: WRDS (CRSP, Compustat, I/B/E/S, 13F; Compustat Global outside the US). Jobs run on WRDS Cloud through the
  seal reader; only statistics and lists come back. CRSP ends 2025-12, so WRDS cannot be the live source.
- Live: LSEG on the user's PC (first-reported accounts, consensus, holders, insiders all confirmed by the probe of
  18 Nov), with SEC filings, SEC 13F and Massive prices as the free route that the triage site already uses.
- What agents and a tracker page may show: lists and figures built from free data. LSEG-built figures stay on the PC
  until the licence question is answered (forecasts against consensus are scored by a PC job; hit rates come back).
- 13F: quarter-end holdings of US-listed long positions, up to 45 days late. The owner panel states that delay.

## 6. Changes to plan v0.3 (they make v0.4, together with the six must-fixes M1-M6 of the review)
1. Roster rule v2: 5-year manager-weighted return on the leaderboard, gated by process material
   (`FOUNDATION_RANKING_2026-11-20.md`), registered as an amendment to the tier rule of `STAGE0_REGISTRATION.md`.
   The control group stays. Each investor keeps a return rank, so the tests can show whether rank mattered.
2. Holdings module widened to conviction: weight rank inside the portfolio, additions, holding time (the definition
   of a conviction purchase is registered before the job runs; proposal: among the five largest weights, or a new
   position or addition of at least 1% of the portfolio; versions averaged).
3. The tracker goes live early, with the reference book, as soon as the two-source check passes, before any investor
   pod is registered. Pods are added to it at registration.
4. "What top investors are buying" has two uses: the owner panel (information for the user) and the registered
   "follow the best managers" pod (walk-forward, all filers, new positions and weights), which competes for a test
   slot. It is not a filter on other pods unless a registered version says so: 13F records did not persist in the
   scorecard (rank correlation +0.14 and -0.05).
5. Valuation: the value leg of the reference book, a stated criterion inside a pod where its investors state one,
   and a display panel for every candidate. "Screen plus valuation gate" is a version of a pod, registered with it.

## 7. Build order
1. Plan v0.4 (this structure, the five changes, M1-M6); registration of the roster rule v2 and of the conviction
   definition.
2. Engine, field dictionary, two-source check, reference book (plan Stage 1; needs no transcript). In parallel a
   pilot end to end for the three core investors (Zlatev, Druckenmiller, Kantor) and one control: claims, conviction
   holdings, say-do, first cards. It measures cost per document and the share of criteria a script can compute.
3. Tracker v0 and the reference book live on paper.
4. Strategy map, charters, specs, blind rebuilds, registration; tests on the design years.
5. Each registered pod joins the tracker and the paper book.
6. Roster filled to 30; freeze; sealed samples run once; scoreboard.

## 8. What exists, what is missing
- Exists: the processed library with machine-checked notes (2,319 documents); the inventory of 635 documents and 241
  investors with filer ids; the seal, reader and checker; the WRDS and PC runners; scorecard and leaderboard code;
  the LSEG equity probe; the test sheet and its review; the triage pipeline on free data with its site and ledger;
  the macro program's methods (planted-error audit, charter and card units, forecast ledger).
- Missing: 21 of the 30 roster investors (9 qualify today); quote-level claims for stock-picker transcripts; the
  conviction holdings module; the field dictionary and two-source data layer; the engine and reference book;
  strategy cards and specs; the tracker; the strategy ledger.

## 9. Limits to accept
- The roster is picked on 2021-25 returns, and almost every thesis is stated after 2010. So the US years 2011-25 are
  reported and never prove an investor pod. Evidence comes from the US design years (1980-2010 after M5), developed
  markets outside the US, and the live record.
- Live returns are slow evidence: a pod that truly adds 3% a year needs roughly 10 to 30 years of live returns to
  show it on its own (tracking error of 5% to 8% a year). The early live evidence is the machinery (portfolio equals
  rule, costs, turnover), the business-outcome links (do selected companies beat consensus: hundreds of results a
  year) and pooled comparisons (investor pods against control pods and the reference book).
- Sector and theme strategies (hard tech, energy) need measures a general company table lacks, and many cannot be
  expressed for 1980-2010. They run as sector pods or single-investor playbooks (Incubator), judged live.
- Most rule layers will turn out to be known factors. Then the reference book, the exclusion rules and the live
  analyst record are the product (plan v0.3 section 1).

## 10. Needed from the user (facts, not design choices)
1. Whether the LSEG licence is for academic use only and whether per-company figures built from it may leave the PC.
2. More long-form material for the parked high-return names, or agreement that the roster is filled from
   well-documented library investors further down the return ranking.
3. A go to write plan v0.4.
