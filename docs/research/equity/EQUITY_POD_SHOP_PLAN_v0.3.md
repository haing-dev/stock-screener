# Equity pod shop: evaluation of the workflow idea, and plan v0.3 (2026-11-15)

Status: design only. Nothing here is built, pulled or run. Written in the screener chat (Claude, Fable 5.2) at the
user's request for an independent evaluation of the idea and a plan of our own. A separate Opus agent checked it and
its corrections are applied (section 13). `EQUITY_POD_SHOP_DESIGN_v0.2.md` stays in force as the annex for
everything this plan does not change, every section included; in particular its rules (section 3), evidence design
(4), data gates (6.3), portfolio and risk design (9), test sheet (10), live cycle (11) and terms (20). Where the two
files differ, this plan wins. Section 11 lists every amendment. Numbers marked "proposal" are fixed at registration,
before any run. Inventory numbers come from `library_inventory_2026-11-15.md` (script
`tools/equity/library_stats.py`).

## 1. Verdict

The idea works as a pipeline and is worth building. Three corrections decide whether its results can be trusted.

1. **Ranking investors on their last five years tells us what to read first. It cannot tell us what is true.**
   Five years is mostly luck and style, the last five favoured one style (large US growth stocks), and the people
   in the library are already the ones who did well enough to be interviewed. So the ranking is widened: several
   windows, style taken out, and every manager who files a 13F as the yardstick, not only the famous ones (a 13F
   is the quarterly list of US-listed holdings that managers with over $100M must file). A check on all filers
   shows whether a five-year record predicts the next five at all. A random control group goes through the same
   pipeline. And the US years used for the ranking never count as proof for a strategy.
2. **"Backtest the pods and see which did well" finds a winner even when nothing works.** With no true edge, the
   best of 20 strategies still shows a Sharpe ratio (return per unit of risk) near 0.5 over 15 years by luck alone,
   and about 0.3 over the 36 years of our design era. (The luck in a 15-year Sharpe ratio is about 0.26 either way,
   and the luckiest of 20 lands about 1.9 times that far out.) So the number of tests that can earn a verdict is
   fixed in advance, every pod is measured with the same sheet against a reference book of known factors, and the
   ranking that counts is on data that played no part in the design. Our own WRDS run shows why: the three triage
   screens' warnings picked losers, all of it was the profitability factor, and the registered buy-minus-avoid test
   found no return after factors (`docs/research/triage_wrds/RESULTS.md`).
3. **"Look at what they actually bought" is the strongest new element.** It makes the investors' words checkable
   (do they buy what they describe?) and measurable (what did a stock look like just before they bought it?). One
   fence: rule writers see what the purchases looked like beforehand, never what the stocks did afterwards. What
   they did afterwards is the investor's record, and the ranking has already used it.

The statistical design of v0.2 holds in the author's view. v0.2 never had its own independent review (its step 0);
the check in section 13 covers v0.2 only where this plan relies on it, and the full review is a Stage 0 item. This
plan adds what the new facts require: a front end for 2,257 documents, an investor scorecard, a holdings module, a
foundation track for technique transcripts, and holdout results reported by region. It also puts the cheap,
script-only steps first.

What to expect, honestly:
- Most rule layers of long-only investors will turn out to be known factors (value, quality, momentum). The likely
  products are a tested reference book, exclusion rules that avoid large losers, a small number of pods that add
  something, and a live record for the judgement no rule captures.
- Investor families cannot be proven on history alone. Nearly all of their theses were stated after 2010, by
  people who did well after 2010. History can reject them or support them; the live record promotes them
  (section 8.2).

## 2. What changed since v0.2

| Fact | Detail | Consequence |
|---|---|---|
| The library is about six times larger | `G:\My Drive\Transcripts\Processed Transcripts`: 2,257 documents, 17.0M words. Nearly every document has the full text with line anchors, a short note whose quotes were checked by machine against the text (those not found are marked), and a catalog entry; one search index covers all text | The inventory is almost free: it reads the catalog and notes, not the texts. Reading everything in depth is neither affordable nor needed |
| General Transcripts | 695 documents, 8.3M words (60 of them in a `macro nov 26` subfolder). By the catalog's speaker fields (heuristic): 327 have an investor present, 153 are a host discussing a book or a case, 123 are company executives, 92 authors, academics and others | Only a document with the investor present can establish what that investor said (rule 2 of v0.2). Book episodes are secondary sources |
| Investors | About 240 distinct names, some of them commentators and authors who never ran money; about 190 appear once, 48 twice or more. The 40 most frequent cover 146 documents (2.0M words) | Evidence per investor is thin. The unit of testing stays the family: several investors, one mechanism |
| Dates | 647 of the 695 are dated 2022-26 | Almost every thesis is stated after the holdout period began, by people chosen for doing well in it (section 8.2) |
| Technique content | Tags of about 350 General documents mention valuation, analysis, screening, portfolio construction, risk or shorting by a strict match, 440 by a loose one (overlapping counts) | Foundation track (section 7) |
| Other folders | Healthcare 431 (biotech desk design), AI CEO Interviews 883 (company evidence for the analyst layer, later), Macro 214, Banking 24, Media 10. Raw folders not yet processed (Tech&AI, Energy, Consumer & Retail, Automotive & Industrial, AI Transformation, Real Estate, Crypto) join when they are, and E0.1 is re-run | Out of scope here |
| LSEG Workspace | Runs in Excel on the user's own PC, any day. The macro probes returned dated price history for one company (Apple month-end closes from 1990); company accounts, estimates and holders are untested | Live source and second source, after a probe (section 9) |
| Bloomberg | Campus only, and the download allowance can run out: on 13 Nov it blocked every request until it cleared later that day | No role in the design; optional cross-check sample |
| WRDS | The subscription also holds CRSP mutual funds, mutual fund holdings, Compustat Global, Financial Ratios, and the Global Factor Data (per the WRDS guide; permissions to be checked) | Real fund returns for the scorecard; history outside the US |

## 3. The ideas, one by one

| Idea | What is right | What goes wrong if done plainly | What the plan does |
|---|---|---|---|
| Rank investors by five-year return; read the top 30-40 first | A triage is needed, and data beats reputation | Five years cannot separate skill from luck: a true edge of 3% a year against a typical 10-15% a year of deviation from the market gives a t-value between 0.4 and 0.7, where 2 is the usual bar for "probably not luck". A raw ranking for 2021-25 is a style ranking. Pods built from the winners look good in the years that made them winners. Many speakers have no measurable record | Scorecard (section 5): windows from 2011 on, style taken out, all filers as yardstick, a grade for how well a record can be measured, a cap per style, a control sample, a check of whether records persist at all, the ranking years kept out of the proof |
| Technique transcripts as a foundation | Definitions, valuation, sizing and risk practice are knowledge for the whole shop, not pods | Treating a technique as tested truth, or testing each one for returns (a second, untracked stream of trials) | Foundation track (section 7): each technique becomes a measure definition, a version, a check or an analyst question, or is dropped |
| One agentic pipeline from transcript to backtest | Most of the machinery exists (macro pipeline, WRDS runner, triage engine, forecast ledger) | Agents grading their own work; the model's knowledge of market history leaking into rules; licensed data leaving WRDS or the PC | Stations with a fixed input, output and gate (section 4); six fences (section 8.3) |
| Judge a strategy by the stocks its investors bought | Say-do check and measurable criteria | Using the later returns of those stocks as evidence for our rule. A 13F shows US-listed long positions only, at quarter-end, 45 days late, and not the day of purchase | Holdings module (section 6) |
| Find the pods with consistently high risk-adjusted returns | It is the goal | Best-of-many selection; "return" before known factors and costs are taken out; one era carrying the result | One yardstick (section 8): every screen measured the same way, proof rationed |
| WRDS, LSEG, Bloomberg | Each has a natural role | Mixing vendors inside one backtest; assuming LSEG history is as first reported; building on a source that cannot be refreshed | History on WRDS, live on LSEG, nothing on Bloomberg (section 9) |
| v0.2 as a suggestion | Its statistics, three layers, reference book and risk charter | It assumed 397 documents and no ranking; the holdings check was only pass or fail; it never had its independent review | Kept as annex; amended in section 11; its review is a Stage 0 item |

## 4. The workflow

```mermaid
flowchart TD
  L[(Library: catalog, notes, texts)] --> I[E0.1 Inventory and typing]
  W[(WRDS: prices, accounts, estimates, holdings)] --> SC[E0.4 Investor scorecard]
  I --> SC --> T[E0.5 Tiers, control sample, foundation list]
  T --> C[E2.2 Claims with verbatim quotes]
  C --> K[E2.4 Investor cards: what they say]
  W --> H[E2.5 Holdings fingerprint: what they bought, no returns]
  C --> MR[E2.11 Methods register]
  K --> M[E2.6-2.7 Strategy map and charters]
  H --> M
  MR --> D[E1.3 Field dictionary, versions]
  M --> S[E3.1-3.3 Pod spec, blind rebuild, checks without returns]
  D --> S
  S --> R[E3.5 Registration]
  W --> E[E1 Engine, risk model, reference book]
  E --> X[E4 Tests on WRDS: Batch 0, A, B1, B2, descriptive pass]
  R --> X --> Z[E5 Freeze, sealed samples]
  E --> LV[E6 Live paper book on LSEG data]
  R --> LV
  Z --> B[Book]
  LV --> B
```

| Step | Who | Output | Gate |
|---|---|---|---|
| E0.1 Inventory and typing (widened) | script reads the catalog; Sonnet reads the notes only; Opus recodes a tenth blind | One row per document: speakers and the role of each, kind (investor's own words, secondary, company, technique, macro), style tags, how explicit the criteria are | Agreement between the two coders per field; a field with low agreement is dropped |
| E0.2 Audit of the existing screens and criteria workbook | Opus | One page; each existing screen becomes a candidate family, unverified until tied to quotes | as v0.2 |
| E0.3 Equity paper pack | Sonnet; Opus blind read | Claims with quotes | as v0.2 |
| E0.4 Investor table and scorecard (new) | Sonnet matches speakers to firms and filer ids, Opus checks a sample; script on WRDS | One row per investor: firm, filer id or fund, record grade, record columns (section 5) | Output form fixed first; code passes a planted-error test |
| E0.5 Tiers (new) | script; the tier rule and the "follow the best managers" signal (section 6) are registered before the scorecard is run | Tier A, control sample, tier B, foundation list, reading order | User go |
| E1 Data, engine, risk model, reference book | Opus; WRDS and PC runners | as v0.2 E1.1-E1.8 | Gates G1-G9 of v0.2, with G8 as amended in section 11 |
| E2.1 Pilot | Sonnet; Opus blind read | 16 documents: two per style for six styles, four technique documents. Cost per document, share of criteria a script can compute, whether investors say why the opportunity exists | Decides the size of E2.2 |
| E2.2 Claims | Sonnet extracts; script checks every quote against the text; Opus second read of a fifth | Claim ledger: quote, line, speaker, claim type, rule as stated, data needed | Every quote found in the text; agreement rate on record |
| E2.3 Process maps; E2.10 dated views | as v0.2 | as v0.2 | as v0.2 |
| E2.4 Investor cards | Sonnet; Opus recodes a fifth blind | Fingerprint card per investor (v0.2 7.3), every field with claim ids | Field agreement |
| E2.5 Holdings fingerprint (widened) | script on WRDS | Per investor: what purchases looked like at the end of the quarter before, against sector peers; say-do table (section 6) | Aggregates only; nothing after the purchase |
| E2.6-E2.9 Map, charters, playbook cards, thesis register | script clusters; Fable judges; Opus checks against the quotes | as v0.2 | No return data in any pack |
| E2.11 Methods register (new) | Opus drafts from technique claims; Fable reviews once | One row per technique and its use (section 7) | Every row cites claim ids |
| E3 Specs, checks, registration | Opus; fresh Opus rebuilds blind; scripts | as v0.2 | as v0.2; user go at E3.5 |
| E4 Tests | scripts on WRDS Cloud; verdict by script | Result sheets, verdict class | v0.2 section 10, as amended in 8.1 |
| E5 Freeze and sealed samples | script; Fable verdict; Opus checks the numbers | One run per sealed sample | One-time key |
| E6 Live paper book | PC runner on LSEG data; Opus analysts; Sonnet report | Weekly lists, risk report, ledger, forecasts | The reference book starts once Batch 0 and the two-source check (E1.7) pass |

How the agents are run: a chat session orchestrates and does none of the judged work itself. Every job has a brief
from a template in the repo, an input pack built by a script, an output form checked by a script, a private work
folder, and a line in the usage log. Extraction runs as parallel Sonnet agents. Fable runs one unit a day with its
exact input stored. WRDS jobs go through `tools/wrdsq`, PC jobs through `tools/bbgq`; both return reports only.
Packs for the strategist and the spec writers carry investor ids, with names and firms masked by a script. The
league table of section 5 is stored apart: sessions that write briefs, cards, charters or specs do not open it.
Ledgers, cards, registers and packs live on a branch (`equity-vault`) and in the Obsidian vault; registration and
results in `docs/research/equity/`. The user releases each stage.

Each registered pod is also a live screen, like the current screeners: a weekly long list and short list with the
criteria behind every name.

## 5. Investor scorecard and reading order

### 5.1 How well a record can be measured (grade per investor)
| Grade | Meaning | Examples in the library (to be confirmed at E0.4) |
|---|---|---|
| A | Long-only stock picker whose 13F shows most of the book: a copy of the filing is close to the real portfolio | Giverny (Rochon), Valley Forge (Kantesaria), Semper Augustus (Bloomstran) |
| B | Partly visible: long/short funds (shorts unseen), global books, large private holdings | Greenlight (Einhorn), D1 (Sundheim), TCI (Hohn) |
| C | A 13F exists but says little: credit, macro, multi-manager platforms, books of hundreds of names | Oaktree (Marks), Balyasny, Gotham (Greenblatt), GMO (Grantham) |
| F | A public fund with real returns after fees. A listed company that also runs a business, such as an insurer, is graded on its 13F instead, because its share price mostly reflects that business | Oakmark (Nygren), Acquirers Fund (Carlisle). Markel (Gayner) is graded A or B through its 13F |
| N | No measurable record: authors, analysts, newsletter writers, most hosts | |

### 5.2 What is computed (one script, for every filer in the 13F data, not only ours)
- The copy portfolio: holdings as filed, bought the day after the 45-day deadline and held to the next filing,
  weighted as filed. Also the ten largest positions only, and new positions only. An amended filing counts from
  its own filing date. Option positions are dropped.
- Windows: 2021-25 (the five years asked for), 2016-20, 2011-15 and 2011-25. The scorecard does not compute years
  before 2011: they are the design era, and a ranking on them would leak into its tests.
- Columns: return; return minus the market; return minus each holding's peer group of similar size, value,
  profitability and momentum (stock picking with style taken out); what is left after the standard factors (market,
  size, value, profitability, investment, momentum), with its t-value; worst fall; share of years ahead of peers;
  number of positions; turnover; weight of the ten largest.
- Each column also as a rank among all filers with 10-150 positions and at least $100M (proposal).
- Grade F: real returns after fees for the same windows (CRSP mutual funds and exchange-traded funds on WRDS;
  other funds through LSEG if the probe allows).
- A persistence check on all filers: how well does the rank in one five-year block predict the rank in the next
  (2011-15 to 2016-20, 2016-20 to 2021-25)? This tests the ranking idea itself. If records do not persist, the
  record columns still show who really ran money, but they say little about who to learn from.
- What comes back: statistics per manager. No holdings, no return series.

### 5.3 Tier rule (proposal; committed before the scorecard is run)
- **Tier A, 40 investors, read in depth.** 30 by record: the average of three ranks, all from 2011 onward
  (style-adjusted result over 2011-25; the same for 2021-25; share of the blocks 2011-15, 2016-20 and 2021-25 with
  a positive style-adjusted result), grades A, B or F, at most eight per style. Ranks are taken within each kind
  of record (13F copies, real fund returns), never across them. An investor needs at least five years of record
  after 2010; the ranks use the windows that exist. Plus up to 10 whose documents are the most explicit about
  criteria, whatever their grade: this keeps investors whose record cannot be measured, and styles that had a bad
  decade.
- **Control, 10 investors.** Drawn by a script whose random draw can be repeated exactly, from grades A, B and F
  outside tier A. Same pipeline. No agent is told who is control. A family counts as control-sourced when most of
  its investors are control. Control pods are run for Incubator status only, outside the four slots of a batch,
  like single-investor playbooks (v0.2 section 10); they get the same sealed runs, reported only, and are counted
  in the trial log. With ten investors there may be only one or two such pods, so the comparison in 5.4 is
  descriptive, not a test.
- **Tier B.** Everyone else stays in the inventory with style tags and can be promoted in a later round.
- **Foundation list.** The 40-60 documents (proposal) with the most technique content, whoever speaks.
- Reading order inside tier A: the investor's own words before secondary sources, more explicit documents first.

### 5.4 Fences
- The ranking orders the reading. It gives no weight to a claim, a family or a verdict.
- Extractors, coders, the strategist and the sessions that brief them never see the scorecard or the tier labels.
- The thesis register logs the windows that selected each family's investors. Those US years are never proof for
  that family (section 8.2).
- The scorecard reads returns inside the sealed years. It is a registered descriptive job: a run whose output form
  is fixed and checked before it runs, and which only describes, never decides. The checker reads the code first,
  and nothing per stock comes back. Each run is logged as an opening of the seal (section 11, gate G8).
- After the tests: do pods sourced from tier A do better on untouched data than control-sourced pods? Reported.

### 5.5 What the user sees first
The league table of the library's investors with the five-year column, where each sits among all filers, the
result of the persistence check, and the top-ranked filers we hold no transcript for (candidates for letters or
interviews to add).

## 6. Holdings module: what they bought, as it looked just before they bought it

**Computed** per investor with holdings (13F filings; fund-level holdings for mutual funds), by a script on WRDS
with its output form fixed in advance. For each new position and each large addition: the stock's rank inside its
sector at the end of the previous quarter (a 13F does not show the day of purchase, so this is the last date surely
before it) on every measure in the field dictionary: valuation, profitability, growth, balance sheet, past return,
size, analyst revisions, distance from the 12-month high, short interest. Then the median and spread across all
purchases, the same for exits, the holding period, concentration, and how the profile moved over time.

**Used for**
- A say-do table per investor: stated criterion (claim id), the median rank its purchases reveal, and "agrees",
  "silent" or "contradicts". A contradiction goes back to the investor card, not into a spec.
- Thresholds. A criterion stated only as a direction ("high returns on capital") may take its threshold from what
  the purchases actually looked like (the revealed distribution), for example the level that three quarters of the
  family's purchases in odd years exceed. The say-do check then uses the even years, so it does not check a
  threshold against the purchases that set it. The source is logged as "revealed", next to "quote", "convention"
  and "grid" (v0.2 8.1).
- The family test: investors of one family should buy similar profiles. If they do not, the family is split or
  the difference becomes a version.
- The spec check at E3.3: the pod's long list must contain the family's actual purchases at three times the
  universe rate or more (v0.2 8.3).

**Fences**
- No return after the purchase appears in any output. A past return appears only as a rank at the end of the
  quarter before the purchase.
- Outputs are aggregates over at least 20 purchases per investor (proposal). No stock names leave WRDS here.
- It reads holdings and ranks inside the sealed years, so it is the second registered descriptive job, under the
  same terms as the scorecard.
- Every report states the limits: US-listed long positions, at quarter-end, 45 days late, no shorts, cash or
  non-US lines, and positions filed late under confidential treatment appear only when disclosed.

The same machinery gives one pod candidate that needs no transcript: follow the new positions of managers whose
record was good up to that date, ranked walk-forward (each month uses only the records known by then). Its signal
is registered before the scorecard runs, because the scorecard shows how such copies did after 2010. Its US result
from 2011 is reported only, and 13F has no version outside the US, so it is judged on the design era and the live
record. It competes for a test slot like any family.

## 7. Foundation track

**What goes in:** documents on valuation, analysis technique, accounting quality, screening, portfolio
construction, sizing, selling, risk management and shorting, whoever the speaker is, plus the equity paper pack.

**What comes out:** a methods register. One row per technique: what it is, who states it (claim ids), and its
single use in the shop.

| A technique that is | becomes |
|---|---|
| a way to define a measure (return on invested capital, owner earnings, cash flow after stock pay) | an entry in the field dictionary (E1.3). Where practitioners differ, each definition is a version, never a choice |
| a way to build or protect a portfolio (sizing, concentration, sell rules, stop-losses, hedges) | a version of the construction rule, a hygiene test in Batch A, or a line in the risk charter proposal |
| a way to value a company | part of the expectations link (v0.2 4.1) and the base-rate library (8.4) |
| a way to analyse a business (moat, management, accounting red flags) | a proxy in the proxy layer if a script can compute it; otherwise a question on the analyst sheet (v0.2 11.2), judged live |
| none of these | dropped, with the reason |

A technique is never tested for returns on its own and never adds a test slot. Batch A keeps the list of v0.2
section 10, with a maximum number of hygiene tests fixed at E3.5; a technique can only take a place on that list.

## 8. One yardstick for every pod

### 8.1 The measurement (v0.2 sections 4, 9 and 10; the changes are listed here and in section 11)
- Same universe, same point-in-time rules, same costs and borrow fee for every pod in a market. Outside the US the
  shortable set needs a stand-in (section 9).
- Criteria become scores ranked inside the sector. Gates only for eligibility and exclusions.
- One construction rule: long the top group and short the bottom group in each sector, equal money on both
  sides, no net market exposure, monthly tranches, a no-trade band.
- Five decisive tests: the pod adds to the reference book after all costs (corrected for the number of pods in the
  batch); it is not worse in any era; it survives doubled costs; it beats random portfolios of the same shape; it
  does not worsen the tail.
- Reported for every pod, not decisive: the pod on its own; the long side against sector peers (what a long-only
  holder would have earned); the short side; how fast the signal fades; what each criterion contributes; turnover;
  capacity; results by size and sector; and the same test with the source investors' own holdings left out (does
  the rule work beyond the stocks they picked?).
- Verdict by script, in the classes of v0.2 4.4: Core (passes every sample that can count; joins the book), Sleeve
  (works, but the reference book already holds it), Exclusion (a warning rule used as a filter), Incubator
  (promising but unproven; runs live in shadow), Shelved.
- Budget for verdicts: Batch 0 (plumbing), Batch A (hygiene on the reference book), B1 and B2 (at most four pods
  each, chosen by a script, v0.2 8.5). A failed pod is not re-run with tweaks.
- Every screen is still measured. Each family with a spec that gets no slot runs the same sheet once on the design
  era, after the batch verdicts are final. That run is labelled descriptive: it cannot earn a verdict, it is
  counted in the trial log, and such a pod is an Incubator pod judged on its live record. So the measurement is
  the same for all; only the proof is rationed.
- A league table of every measured pod is published, labelled descriptive, with the number of trials behind it.

### 8.2 Samples
| Sample | Use |
|---|---|
| Design era: US, 1975-2010 | Building and design tests |
| Untouched regions: developed markets outside the US, 1990-2010 | Sealed; one run after the freeze |
| Holdout, US, 2011 onward | Sealed until the freeze, except for the two registered descriptive jobs (5.4 and 6). One run. A verdict only for a family whose thesis is documented before 2011, whose sources have no career overlap, whose investors were not picked on those years, and whose spec took nothing from holdings after 2010. For every other family: reported, not a verdict |
| Holdout, outside the US, 2011 onward | Sealed until the freeze; one run, reported apart from the US part. A verdict under the same conditions as the US part. For the other families it can support a promotion at the live checkpoint, and only if two things registered at E3.5 hold: the family's source investors built their records mainly in the US (proposal: under 20% outside), and in 1990-2010 the pod's added return in the US and outside it were not closely linked (proposal: correlation under 0.5) |
| Live | Reference book from Stage 1; each pod from registration; promotions at registered checkpoints |

Tier A is picked on returns after 2010, and almost every thesis in the library is stated after 2010. So an
investor family cannot become Core on history: v0.2 4.4 and the macro rule (a pod flagged for hindsight is never
Core) stand. It is judged in this order: the design era, the untouched regions, the two holdout parts as reported,
then its live record, where it can be promoted. The reference book, and any family built only from sources
published before 2011 with no ranking involved, can be Core on history.

Three consequences. Data outside the US is part of the engine from Stage 1. Tier A must be complete before the
freeze, because the sealed samples are run once. And a pod that needs an input found only in the US (13F
ownership, short interest, insider trades) has no test outside the US: it is judged on the design era and the
live record.

### 8.3 Six fences
1. **Selection.** The ranking orders reading only; the persistence check and the control sample show whether it
   helped.
2. **Returns.** No agent that writes claims, cards, charters or specs is given a return, of a stock or of an
   investor. The models still know from training how famous investors and stocks did, so the packs for the
   strategist and the spec writers carry investor ids, with names and firms masked.
3. **Hindsight.** No company name, date or event in a rule. Every threshold traces to a quote, a convention, the
   grid or the revealed distribution. A fresh agent rebuilds each spec blind.
4. **Trials.** Slots fixed and registered before any run; one sheet; correction for the number of pods; no re-runs;
   every descriptive run counted.
5. **Samples.** A sample counts as proof only if it could not have shaped the pod's sources (8.2).
6. **Checkers.** No step grades itself; checkers are tested with planted errors.

## 9. Data plan

| Need | History for backtests | Live | Notes |
|---|---|---|---|
| Prices, returns, delistings | CRSP on WRDS (yearly update; ended 2025-12 at our October pull) | LSEG on the PC | Free fallback: Massive |
| Accounts as known on the day | Compustat on WRDS with report dates | LSEG fundamentals with source dates | Free fallback for the US: SEC filings, 2009 onward |
| Analyst estimates | I/B/E/S on WRDS | LSEG (I/B/E/S) | |
| Holdings | 13F and mutual fund holdings on WRDS; SEC 13F data sets from 2013 | SEC 13F (free); LSEG ownership | The WRDS 13F file is compared with the SEC's own at E1.2 |
| Insider trades | SEC Form 4 data sets (free; `triage/owners.py` reads them) | same | WRDS insider table: no permission. The SEC data sets start in 2006, so the design era has five years of insider data, under the ten years a design test needs |
| Short interest | Compustat on WRDS (to be checked) | LSEG (to be probed) | |
| Markets outside the US | Compustat Global and Global Factor Data on WRDS (to be checked) | LSEG, Datastream | No 13F ownership, short interest or insider data outside the US; delisting returns to be checked. The shortable set there needs a stand-in fixed at E1.4 |
| Fund returns for the scorecard | CRSP mutual funds, including exchange-traded and closed-end funds | LSEG fund data (to be probed) | |
| Factor returns | Fama-French and Global Factor Data on WRDS | Ken French's site | |

**LSEG Workspace: what is established**
- On the user's PC the Excel functions work: dated price history for one company (Apple month-end closes from
  1990, `RDP.Data`; the older `TR` was tried only on the S&P 500), and Datastream (`DSGRID`). Source:
  `tools/bbgq/results/lseg_probe_v1.txt`. Company accounts, estimates and holders were not tested.
- LSEG's fact sheet: up to 108,000 active and inactive companies, public and private; US history from 1983, other
  countries from 1995; values as reported, standardised and restated; "point-in-time details on the source
  publication"; 700+ industry operating metrics.
- Fields exist for the period end, the source filing date and whether a value is original or restated
  (`TR.F.SourceDate`, `.FundUpdType`, `.periodenddate`). In the cited thread the last one came back empty on
  weekdays, and the thread does not show that first-reported values can be pulled. Holders of a stock can be listed
  as of a past date (`TR.InvestorFullName`, `TR.PctOfSharesOutHeld` with a date); the summary ownership field has
  no history. Source: LSEG developer community.
- Estimates: LSEG's programming library lists past consensus snapshots for the last 12 months only in that
  interface; I/B/E/S itself starts in 1976 for the US and 1987 elsewhere, and its full history is on WRDS.
- Limits of the programming interface (Python): about 5 requests a second, 50 MB a minute, 3,000 rows per history
  request, and a daily cap that resets at local midnight. Excel has its own limits.

**What only a probe on the user's PC can settle (E1.1; one workbook of about 150 formulas, one refresh)**
- A universe that includes dead companies; identifiers to join with WRDS.
- First-reported values in bulk, with dates, for companies known to have restated.
- Analyst consensus as it stood on past dates, and how far back.
- Holders by quarter and how far back; insider trades; short interest.
- Datastream: accounts, lists of dead stocks, past index members.
- Fund returns; LSEG's own model scores (StarMine); the size of request Excel accepts; whether the licence covers
  the programming interface (if so, pulls run as scripts on the PC runner, without Excel).

**Roles.** History stays on WRDS unless the probe shows first-reported values and dead companies on LSEG. LSEG is
the live source, the second source for the check that WRDS-built and LSEG-built scores agree (gate G7), and the
source for what WRDS lacks. Bloomberg has no role: no input of any pod may exist only there. The 4,512-stock
workbook stays as an optional one-off cross-check.

**Licences.** WRDS is licensed for academic research and paper trading, and its data may not be loaded into AI
tools: jobs run on WRDS Cloud and only statistics return. LSEG data stays on the PC under the same practice;
whether that licence is for academic use only is to be confirmed. Before any real money, the live path must run on
data whose licence allows it (step E5.5); the free SEC and price route in the repo is kept working for that reason.

## 10. Stages and effort

| Stage | Content | Output for the user |
|---|---|---|
| 0. Know the library and the data | E0.1 inventory; E0.4 scorecard; E0.5 tiers; E1.1 LSEG probe (one refresh by the user); E1.2 WRDS table check; the independent review of v0.2 as a whole | Investor league table; whether records persist; tier lists and reading order; what LSEG and WRDS return under these licences |
| 1. Measurement engine and pilot | E0.2; E1.3-E1.7; Batch 0; reference book live on paper once the two-source check passes; E2.1 pilot | A working reference book with its weekly risk report; measured cost and yield per transcript |
| 2. Library | E2.2-E2.11 for tier A, control and foundation; E0.3; E1.8 | Claim ledger, investor cards, holdings fingerprints, strategy map, charters, methods register |
| 3. Specs, registration, tests | E3; Batch A; B1; B2; the descriptive pass | Verdict per registered pod; the same sheet for every other family; each pod's live screen from registration |
| 4. Freeze, sealed samples, book | E5 | Final verdicts; the book |

Effort, in tokens. The Fable figures come from the macro program's log. The other figures are estimates (the log
has about 0.6M for one engine build and 0.3M for its check); the pilot replaces the extraction figure with a
measurement.
- Stage 0: typing about 700 notes, about 1.5M (Sonnet); scorecard and probe builds, perhaps 1M (Opus).
- Extraction: perhaps 50-60k per document for both reads. Tier A, control and foundation may come to 110-200
  documents (the 40 most frequent investors cover 146; a tier chosen by record will cover fewer): 6-12M (Sonnet,
  with Opus on a fifth).
- Fable: one map, 6-12 charters, one register review, two batch reviews, one verdict (playbook cards and the monthly
  reviews once live are not counted): 11-17 units of 0.65-0.9M, each with an Opus check of about 0.3M.
- Engine, risk model, specs and checks: perhaps 5-8M (Opus).

One Fable unit a day stays the rule.

## 11. Amendments to v0.2

| v0.2 | Amendment |
|---|---|
| 4.2 Samples | Holdout results are reported by region. The US part gives a verdict only under the conditions in 8.2; otherwise it is reported. The non-US part gives a verdict under the same conditions; for other families it can support a promotion at the live checkpoint under the rule in 8.2. 4.4 is unchanged |
| 6.1 Sources | The library is `Processed Transcripts`. Bloomberg has no role. Insider trades come from the SEC data sets. CRSP mutual funds and mutual fund holdings join the list |
| 6.3 Gate G8 | The two registered descriptive jobs (scorecard and holdings module) may read US data from 2011 on before the freeze. Each run is logged as an opening of the seal. Data outside the US from 2011 on stays sealed until the freeze |
| 7.1 Pilot | 16 documents: twelve investor documents (two per style) and four technique documents. The inventory questions are answered from the catalog first |
| 7.2 Claim types | Add "technique" (a definition or method) for the methods register. Every claim carries its source class: the investor's own words, or secondary |
| 7.4 Families | "Investor" means a person who ran money (grades A, B, C or F), not an author or host. Secondary sources count as at most one published source per family |
| 8.1 Spec | A threshold may also come from the revealed distribution, set on half of the purchases (section 6) |
| 8.3 Say-do | Purchases (new positions and large additions) replace holdings. Ranks are taken at the end of the quarter before the purchase, price-based ones included, inside the registered descriptive job; this replaces "accounting measures only" for quarters after 2010. The check uses the half of the purchases that did not set a threshold |
| 8.5 Slots | Control-sourced pods run for Incubator status only, outside the slots. The "follow the best managers" pod is a candidate, its signal registered before the scorecard |
| 10 Test sheet and budget | Reported lines add the test with the source investors' own holdings left out. Batch A has a maximum number of hygiene tests fixed at E3.5. Families with a spec and no slot get one descriptive run on the design era after the batch verdicts (8.1) |
| 13 Steps | New: E0.4, E0.5, E2.11. Widened: E0.1, E2.5 |
| 14 Order | Stage 0 precedes Stage 1. E1.7 (the two-source check) moves to Stage 1, before the reference book goes live, as v0.2 6.1 requires |
| 16 Reuse | Add the processed library (texts with line anchors, checked quotes, search index) and `tools/wrdsq/tri_wrds_adapter.py` (CRSP, Compustat and 13F panel with resumable pulls) |
| 17 Needed from the user | Section 14 here adds to it |
| E5.5 Execution | Add the licence check before real money (section 9) |

## 12. What can go wrong

| Risk | Answer |
|---|---|
| Most investors appear once, so families are thin | A family needs three investors who ran money, or two plus a published source; the inventory's style tags show the whole population; thin groups become single-investor playbooks (Incubator) |
| A 13F copy misleads (grades B and C) | Grades; real fund returns where they exist; every scorecard row states what it cannot see |
| Records do not persist | The persistence check says so in Stage 0, before any reading is ordered by record. The tier then leans on how explicit the documents are |
| Data outside the US is weaker, or not permitted | Checked at E1.2 before anything depends on it. If it fails, support from recent years rests on the live record alone, and the plan says so |
| LSEG history is restated or drops dead companies | History stays on WRDS; our own archive starts with the first live week |
| Everything turns out to be a known factor | Then the reference book, the exclusion rules and the live analyst record are the product |
| Token cost | Tiers; pilot before scale; the cheap steps first |
| University licences end | Free US route kept working; archive kept |

## 13. Independent check

A separate Opus agent (effort high) checked the first draft on 2026-11-15: `EQUITY_POD_SHOP_PLAN_v0.3_check.md`.
Verdict: PASS WITH CORRECTIONS, with 5 must-fix, 17 should-fix and 14 minor findings. It re-ran the inventory
script (all counts matched), recomputed the arithmetic, fetched the LSEG pages, and checked every reference to v0.2.

What it changed, in substance:
1. The ranking used returns from before 2011, the years in which the design tests run. It now uses 2011 onward only.
2. A 13F does not show the day of purchase. Purchases are now described at the end of the quarter before.
3. The two jobs that read sealed years had no rule allowing it. Gate G8 is amended and each run is logged.
4. The "follow the best managers" pod would have been designed after seeing its own answer. Its signal is now
   registered before the scorecard runs.
5. Counting the non-US holdout as proof for every family broke two rules the plan keeps, and many library
   investors built their records outside the US. See decision 1 below.
6. Wording that claimed more than the sources show (the LSEG probe, the triage result, the Bloomberg status, the
   effort figures) is corrected, and jargon is explained where it first appears.

Two findings were design decisions. Both are settled by rule, not by taste, and can be reopened at registration.
1. **Can an investor family be Core on history?** No. The checker offered (a) keep the v0.2 and macro rule, or
   (b) let the non-US holdout count under conditions. This plan takes (a): one rule across the shop, and the
   premise of (b) fails for many investors. The conditions of (b) are kept as the rule for when the non-US holdout
   may support a promotion at the live checkpoint.
2. **Does every screen get a history test?** The user asked for every screen to be measured. The budget of eight
   slots stays for verdicts, and every other family with a spec gets one descriptive run (8.1). The checker
   offered this as option (b); option (a) was live screens only.

Added by the author after the check, and seen by the checker only in its re-check: the persistence check (5.2),
the test with the source investors' own holdings left out (8.1), E1.7 moved to Stage 1, the review of v0.2 as a
Stage 0 item, and the note on raw folders not yet processed.

Re-check of the corrected text: PENDING.

Not verified by anyone yet: whether the named managers file 13F with the coverage their grades assume (E0.4);
Compustat Global delisting returns and short-interest coverage (E1.2); that the SEC 13F data sets start in 2013
(the page did not load for the checker).

## 14. Needed from the user (facts, not design choices)
1. A go for Stage 0.
2. One refresh of the LSEG probe workbook at home, once it is built.
3. Whether the LSEG licence covers the programming interface, if known (the probe also tests it).
4. How long WRDS and LSEG access will last, and whether the LSEG licence is for academic use only.
5. PDFs for the equity paper pack (the list comes with E0.3).
Only before real money: account size, broker, and whether the account can short.

## 15. Sources

Repo: `EQUITY_POD_SHOP_DESIGN_v0.2.md`; `EQUITY_POD_SHOP_PLAN_v0.3_check.md`; `library_inventory_2026-11-15.md`;
`docs/research/triage_wrds/RESULTS.md`; `docs/research/WORKFLOW.md` (the macro rules); `tools/bbgq/results/lseg_probe_v1.txt`;
`tools/wrdsq/GUIDE_FOR_NEW_CHATS.md` (WRDS subscription and licence).

Web, read 2026-11-15:
- LSEG, "The Data Library for Python: maximum usage reference guide":
  https://developers.lseg.com/en/article-catalog/article/the-data-library-for-python-maximum-usage-reference-guide
- LSEG Company Fundamentals fact sheet:
  https://www.lseg.com/content/dam/data-analytics/en_us/documents/fact-sheets/lseg-company-fundamentals-fact-sheet.pdf
- LSEG developer community, original and restated flags on fundamentals:
  https://community.developers.lseg.com/discussion/132467/company-fundamental-fundupdtype-sometimes-returns-nat-sometimes-value-ie-original-restated
- LSEG developer community, ownership over time:
  https://community.developers.lseg.com/discussion/44105/instituitional-ownership-over-time
- LSEG Data Library, estimates content:
  https://cdn.refinitiv.com/public/lseg-lib-python-doc/2.0.0.2/book/en/sections/content-layer/estimates/about-estimates.html
- SEC Insider Transactions Data Sets (start 2006; read by the checker): https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets

From the writer's knowledge, to be verified when the papers enter the pack: Carhart (1997) on the weak persistence
of fund performance; Cohen, Polk and Silli on managers' best ideas; Daniel, Grinblatt, Titman and Wermers (1997) on
peer groups by size, value and momentum; Harvey, Liu and Zhu (2016) and Bailey and Lopez de Prado (2014) on
selection among many backtests.
