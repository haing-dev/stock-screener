---
tags: [method, equity, biotech, design]
status: draft v0.1, design only
---
> Source: repo `docs/research/equity/BIOTECH_DESK_DESIGN_v0.1.md` (commit bf94537). Sector desk inside [[Equity pod shop design v0.2]], built on the crash-triage tool and the healthcare transcripts. Self-review only; not yet independently checked.

# Biotech desk: design v0.1 (hedged long/short, event-driven; draft for discussion, 2026-11-15)

Status: design only. Nothing here is built, pulled or registered. One thing was run: a read-only re-run of the public
crash-triage backtest, to describe what it shows (section 3.2; scripts and output in `biotech_checks/2026-11-15/`).

This file is the sector desk for biotech inside the equity pod shop (`EQUITY_POD_SHOP_DESIGN_v0.2.md`). The shop's
rules apply unchanged: quotes as ground truth, three layers (rule, proxy, analyst), link-by-link tests, versions
averaged, registration before any run, the seal, a fixed budget, one code path for backtest and live, independent
checks, licensed data kept where the licence puts them. This file covers only what biotech changes.

It is a self-review by the author (Claude, Fable 5.2), written from the seat of an experienced biotech investor; an
independent check is still due. Numbers marked "proposal" are placeholders, fixed at registration (step B3). Section
18 explains the terms.

## 1. What we are building

A biotech book that tries to earn stock-picking return and little else:
- a **long book** of 25 to 50 small positions chosen by pods;
- a **hedge** against the biotech index, so the sector's swings cancel;
- an **exclusion list** that keeps predictable losers out;
- a small **short sleeve**, only for a rule that has passed its own test, in stocks that can be borrowed;
- an **odds ledger**: dated probability forecasts on trial results and FDA decisions, scored against base rates.

Slow by design: daily closing prices only; entries at the next open after public news; holdings last weeks to more
than a year; nothing trades inside the day.

| Goal | Product |
|---|---|
| Know the specialists' strategies and their logic | Thesis library: claims with quotes, fingerprint cards, charters (B2) |
| Know every dated event | Event database, and a catalyst calendar as it was known on each day (B1) |
| Screen in real time | Daily triage (exists) plus a weekly desk run |
| A portfolio per strategy | Pod portfolios, sized by loss-if-wrong, hedged |
| Proof | Design-era tests on WRDS, one holdout run, live ledgers |

## 2. Why biotech needs its own design

| What is different | Consequence for the design |
|---|---|
| Most companies have no sales or profit | Earnings-based measures are empty. Value is cash plus the odds-weighted worth of the drugs |
| Returns arrive on a few dated events: trial results, FDA decisions, financings, takeovers | The event is the unit of analysis. Every position carries its next event and a rule for it |
| Outcomes are lopsided: most positions lose, a few multiply | Averages mislead. Tests use medians, hit rates, and results without the best few names |
| Companies live on share sales | Financing terms and cash runway are first-order inputs |
| A single stock can fall 80% or double overnight | Risk is budgeted by loss-if-wrong per event, not by volatility |
| Shorting is dangerous: takeovers, surprise data, scarce borrow | The hedge is the index. Single-name shorts must earn their place |
| No licensed drug-pipeline database (neither WRDS nor LSEG has one) | The event data are built from public filings and registries |
| Structured trial data start around 2005 to 2008 | History is short. The live record carries more weight than elsewhere in the shop |
| The investors are specialists whose careers overlap the holdout years | By the shop's rule the holdout cannot crown a strategy here. It can only reject one |

## 3. What exists, and what the data say

### 3.1 The crash-triage tool (repo `haing-dev/crash-triage`, public, live)
- Universe: 1,041 US pharma and biotech companies by SEC industry code; 598 listed today.
- Two scans on daily closes. **Crash**: a fall of 50% or more within five trading days, with one day of 25% or more.
  **Slide**: 30% or more below the six-month high with no such day.
- Inputs as of the entry day: enterprise value against cash, other Phase 2+ trials, financing terms, insider trades,
  funds holding it at 2% or more of their reported portfolio ("high conviction owners"), a "top performer" fund
  list, short interest, and for crashes the cause and the safety wording of the announcement. A model reads the
  press release; each fact is tied to a verbatim quote.
- Calls by a fixed rule. **Avoid**: a going-concern warning, a price under $1, or toxic financing. **Buy candidate**:
  none of those, market value of $50M or more, and one of three: enterprise value no more than its cash (so valued
  at up to about twice its cash), two or more high conviction owners, or a top-performer owner. **Watch**: the rest.
- Live ledger since 18 October 2026.

### 3.2 A re-run of its backtest (descriptive only)
Public code and data as of 15 November 2026. Calls made on the entry day, with a full year of outcome. "vs XBI" is
the stock's return minus the return of the XBI biotech fund over the same days. A single return is capped at +500%.
The rules were chosen on these same episodes, so the table describes; it proves nothing.

| Call | Episodes | Mean return | Median return | Mean vs XBI, 12 months | Beat XBI | t (monthly means) | Mean vs XBI at 3 / 6 months |
|---|---|---|---|---|---|---|---|
| Crash: Buy candidate | 150 | +26% | -8% | +15 points | 41% | 1.7 | +2 / +6 |
| Crash: Watch | 154 | -34% | -59% | -35 points | 17% | -5.7 | -16 / -23 |
| Crash: Avoid | 490 | -42% | -79% | -59 points | 14% | -9.8 | -13 / -34 |
| Slide: Buy candidate | 1,168 | +8% | -14% | +1 point | 39% | 0.9 | 0 / +2 |
| Slide: Watch | 894 | -13% | -36% | -14 points | 29% | -3.6 | -5 / -10 |
| Slide: Avoid | 631 | -18% | -48% | -28 points | 22% | -7.3 | -9 / -14 |

More from the same run:
- Crash Buy candidates without their three best episodes: +7 points against XBI. By entry year: 2021 +13, 2022 -2,
  2023 +25, 2024 -1, 2025 +53. Two years carry the result.
- Crash Buy candidates with a top-performer owner (23 episodes): +40 points at six months, and 65% beat XBI. The
  other 127: -1 point at six months, +11 at twelve (t of 1.2).
- Avoid calls lag XBI in every entry year, for crashes and for slides.
- The repo's own report (an older run, against similar biotechs) has the same shape: Buy candidates +19% against
  +9%, 37% beat them; Avoid median -74%.

### 3.3 How to read it
1. **The tool sorts well, and the sorting power sits on the losing side.** Avoid and Watch calls lag by wide margins
   in every year. The WRDS test of the general stock triage found the same: the warnings work.
2. **The Buy side is unproven.** +15 points with a t of 1.7, a negative median, and half the edge in three episodes.
   There is no quick rebound on average: +2 points after three months.
3. **For slides the Buy call has shown nothing** against XBI.
4. **What looks best is the smallest group**: Buy candidates owned by a top-performer fund. 23 episodes are too few
   to trust, and that fund list is ranked on the outcomes of earlier episodes with settings chosen on this history.
5. **Most crashed stocks deserve it.** The tool marks 19% of crashes as Buy candidates. One investor in the notes
   puts the share that do not deserve the fall at about two in ten.
6. **Part of the older history has been used once.** A code comment records a WRDS test of the top-performer pick
   on 1998-2023 (trained on 1998-2019, tested on 2020-2023) and says the slide screen showed no edge over XBI. The
   report is in neither repo. Step B0.1 finds it.

### 3.4 The healthcare transcripts
37 transcripts in the research store. 26 are specialist investors, ten people: Peter Kolchinsky of RA Capital (9),
Rod Wong of RTW (6), Jim Flynn of Deerfield (2), Dave Johnson of Caligan (2), one each for Bihua Chen (Cormorant),
Eli Casdin, Joseph Edelman (Perceptive), Lars Theill (Crescat), Chris Liu (RTW) and Annie Lamont (Oak HC/FT), and
one shared panel. Two people give 15 of the 26. The other 11 are company and science talks; they inform the analyst
layer, not the strategy map.

All have fact-checked notes. None has claims with verbatim quotes yet. So everything this file takes from them is a
prior, to be confirmed at step B2.

### 3.5 Other assets
- Archived screens in `qs/screens.py`: "Healthcare - Pre-revenue & clinical" (valued near or below cash; a two-year
  funding gap of at most 20% of market value) and "Healthcare - Commercial".
- `validation/managers.json`: Deerfield, RA Capital and Cormorant mapped to their 13F filings.
- `tools/fcast` (forecast ledger and scorer), `tools/wrdsq` (WRDS runner), `tools/bbgq` (PC runner).
- Connectors for PubMed and bioRxiv, for the analyst layer.

## 4. Critique: what a top biotech investor would change

| # | Weakness today | Why it matters | Change |
|---|---|---|---|
| 1 | Cut-offs and the call rule were chosen on the same 2020-26 episodes the backtest reports | The numbers are in-sample | Freeze the rules as they stand. Treat 2020-26 as spent. Seek proof elsewhere (7.2) |
| 2 | The Buy call reads as "buy" | It is a lopsided bet with a low hit rate and a thin edge | A shortlist for analysis and a small-position pod. Never a concentrated bet |
| 3 | The strongest result, Avoid, is not a portfolio rule | Keeping out the predictable losers is the most reliable gain in this sector | Exclusion list on every pod from day one |
| 4 | Outcomes are averaged per event | Crashes cluster in bad months, and nobody can buy them all | Calendar-time portfolios with position caps |
| 5 | One market cycle: boom in 2020-21, bear market to 2025 | The result may belong to the cycle | Results by year and by state of the sector; older history |
| 6 | A model that may know what happened later read the old press releases | Labels can carry hindsight | Masked re-read test; judgement fields are forward only (8.3) |
| 7 | The top-performer list ranks funds on the outcomes of earlier episodes, with settings chosen on the same history; 13F shows longs only, late | The best-looking result rests on the fewest cases and the most choices | Truncation test; specialists defined from holdings alone; crowding measured |
| 8 | Entry at the close of the detection day; no costs | Not tradable as measured, least of all in very small stocks | Next open; spreads by price and size; capacity reported |
| 9 | Compared with an index, not hedged | A comparison is not a position | A designed hedge, tested as held |
| 10 | Twelve months for everything | Arbitrary, and slow to resolve | Horizons of 3, 6 and 12 months registered and averaged |
| 11 | Only the aftermath of bad news | Most of what specialists describe lies elsewhere: odds, launches, financings | More pods, from the thesis library (section 6) |
| 12 | No sizing, exits or event rules | In biotech, sizing is the craft | Risk charter (section 9) |
| 13 | No measure of what the price already assumes | Good news that was expected does not pay | Expectation measures and the odds ledger (sections 6 and 11) |
| 14 | Cash is treated as a floor | Cash is a floor only if the spending stops | Cash after burn to the next event; signs that cash will be returned or redeployed |
| 15 | The cause of a crash is recorded but not used | A manufacturing problem and a failed drug are different bets | Recovery by cause; the FDA's rejection letters are now public |
| 16 | No learning loop | The same mistakes repeat unseen | Monthly attribution; a post-mortem on every loss above a set size |

## 5. Principles in the specialists' notes, and where each lands

From the fact-checked notes. Not yet claims with quotes.

| Principle | Heard from | Design feature |
|---|---|---|
| The price already holds the consensus odds. Profit needs a different and better view | Chen, Edelman, Wong, Johnson | Odds ledger scored against base rates; every pod states what the price assumes |
| Some odds are better: a known genetic cause, a mechanism already proven, a sharper molecule on proven biology | Chen, Flynn, Wong | Measurable priors in the Odds pod |
| Size by what is lost if wrong. Single-drug development names stay small. Large positions need a marketed product underneath | Wong, Theill, Edelman | Loss-if-wrong budget; weight caps by stage (9.2) |
| Expect to be wrong about four times in ten | Wong | Hit rate and loss size tracked monthly; no pod judged on hit rate alone |
| After a fall, most deserve it. The craft is telling a bad trial from a bad drug | Chen, Theill | Aftermath pod with cause coding; a cause sheet from the analyst |
| Do not hold a crowded good-news event; expectations move first | Casdin, Theill, Edelman | Run-up diagnostic; exit rules before events |
| Value has a floor: cash after burn, approved products, royalties, milestones. The pipeline is an option on top | Johnson, Flynn, Wong | Asset-floor pod; a three-to-one payoff rule as a version |
| Financing decides who survives. A company can raise about 10-20% of its value at a time | Wong, Casdin, Kolchinsky | Funding-gap exclusion; financing-reset pod |
| Consensus adjusts slowly to a launch, up and down | Edelman, Wong | Launch-drift pod on sales surprises |
| Specialist ownership separates "core" companies from "peripheral" ones | Kolchinsky | Specialist footprint as a baseline rule and an input |
| Do not build takeovers into value or size | Casdin | Takeover gains reported apart; never an input |
| Stay inside what you understand | Wong, Chen | The analyst's view counts only in disease areas where its record beats the base rate |
| Re-underwrite at every event | Wong | Every position re-scored when its event resolves; kill facts watched by script |

## 6. Candidate pods, exclusions, and what stays out

All are priors. The strategy map (B2.3) confirms, merges or drops them. A family needs three independent investors,
or two plus a published source (the shop's rule).

| Pod | Mechanism: who is on the other side | In the notes | Rule-layer inputs | What we know |
|---|---|---|---|---|
| P1 Aftermath | After a failure, holders who must or will sell (threshold sellers, funds that cannot hold a broken stock) push some prices below the worth of what is left | Theill, Chen, Kolchinsky, Wong | Crash and slide scans; cash after burn; other programs; cause; terms; specialist owners | Section 3.2: the sorting works; the Buy side is unproven |
| P2 Asset floor | A mismatched investor base and neglect leave marketed products, royalties and cash priced below their worth | Johnson, Flynn, Wong | Net cash, product sales, royalties, debt; activist filings | Not tested |
| P3 Run-up | Attention arrives late: stocks sit in a "catalyst desert", then wake before a dated result | Johnson, Theill. Casdin reports the opposite for the last one to three months | Calendar as known; months to the expected result | Not tested. One diagnostic first |
| P4 Odds | The market prices average odds; measurable features shift the true odds | Chen, Flynn, Wong, Johnson, Theill | Phase, disease area, drug type, genetic support, proven mechanism, earlier result and trial design | Not tested. Starts as a forecast ledger |
| P5 Launch drift | Analysts anchor. In the first years of a launch, beats follow beats and misses follow misses | Edelman, Wong, Theill | Reported sales against consensus (I/B/E/S; LSEG live) | Not tested. The most standard test of the seven |
| P6 Specialist footprint | Specialists see more (private stakes, primary research), and their concentrated positions carry it | Kolchinsky; the triage inputs | 13F: specialists by holdings, position size, new positions | Triage inputs positive; too few cases; circularity risk |
| P7 Financing reset | A needed share sale hangs over the price. Once priced on clean terms with specialist buyers, the overhang is gone | Wong, Casdin, Kolchinsky | Offering filings: size, discount, warrants, named buyers; runway after the deal | Only the triage "raise" input. Must beat the known weakness of stocks after share issues |

**Exclusions.** Tested in Batch A as predictors of large losers, then applied to every pod.
- E1 going-concern warning. E2 price under $1. E3 toxic financing outstanding. Evidence: the Avoid rows in 3.2.
- E4 crashed and not a Buy candidate, for 12 months. Evidence: the Watch row.
- E5 funding gap: cash needed for the next two years above 20% of market value. From Wong's rule of thumb and the
  archived clinical screen.
- E6 no specialist owner (Kolchinsky). To be tested with care: small companies are under-owned for other reasons.
- E7 a failed trial re-read on a subgroup found afterwards (Chen).
- E8 serial dilution: share count up by half or more in a year, or a reverse split.

**What stays out.**
- Timing the sector (buying biotech bear markets: Casdin, Wong, Flynn). The book stays hedged. The state of the
  sector is reported and results are split by it.
- Takeover bets. Reported as a share of return.
- Views on FDA leadership and drug-pricing policy. Logged in the forecast ledger; no rule trades on them.
- Private and crossover investing; debt and royalty deals.

**Where the investors disagree.** Each charter records it.
- The months before a result: Johnson and Theill describe a run-up. Casdin's own data show strong catalysts one to
  three months out paying less.
- After bad news: Theill cites a rebound within 100 days, from a paper on about 20 events. Chen says eight in ten
  deserve the fall. Our own Buy candidates show +2 points after three months.
- Baskets: Chen says they do not work. Theill holds about 30 names, Edelman more than 200.
- Science risk: Johnson avoids it. Chen and Wong take it where the odds are high.
- Shorts: Edelman's method began with a short. Wong cut his short sizes after a takeover loss.
- Drug type: Flynn says antibodies are twice as likely to work as small molecules. The BIO report gives 9.1%
  against 5.7% from Phase 1. Claims get checked like this throughout.

## 7. Evidence design

### 7.1 The chain
1. **Rule -> selection.** An independent rebuild matches. The long list overlaps what specialists hold (not used
   for P6, where it would be circular).
2. **Selection -> outcome in the world.** More trials met their goal, more drugs were approved, sales beat, the
   company survived. No prices.
3. **Outcome -> surprise.** The outcome was better than what was priced: the reaction on the day, the consensus. No
   portfolio returns.
4. **Surprise -> price.** The hedged portfolio earned it after costs.

For P4, link 2 is the heart: forecasts against outcomes. A pod that cannot beat the base rate on outcomes is never
tested on prices.

### 7.2 Samples, and what is already spent
| Sample | Definition (proposal) | Use |
|---|---|---|
| Spent | Crash and slide episodes 2020-2026, for the triage rules and inputs. Possibly 1998-2019 for the top-performer pick; B0.1 settles it | Description only |
| Design era | US-listed biotech, 2001-2010. The start is fixed at B0, once event coverage by year is known | Building, diagnostics, design tests |
| Holdout | 2011 to the latest data: the shop's seal. For a rule that uses an input already scored on 2020-26, only 2011-2019 counts | One run after the freeze |
| Live | Triage ledger since 18 October 2026; odds ledger and paper book from Stage 1 | Forward record |

Three limits, stated plainly:
- No untouched regions. Biotech markets outside the US are small and their event data poor.
- Career overlap. The transcripts date from 2021 to 2026 and the specialists built their records mostly after 2010.
  By the shop's rule the holdout then reports; it gives no verdict.
- So on this desk **history can reject a pod, and only the live record can promote one**.

### 7.3 What the live record can and cannot prove
Single outcomes vary by about 90 to 110 points over a year (from the re-run). That sets how many resolved calls a
question needs.

| Question | Size seen in 3.2 | Resolved calls needed | Calls a year | Time |
|---|---|---|---|---|
| Do crash Avoid calls lag XBI? | -59 points | about 25 | about 115 | The first year of resolved calls |
| Do slide Avoid calls lag XBI? | -28 points | about 90 | about 125 | About a year |
| Do crash Buy candidates beat XBI? | +15 points | about 410 | about 30 | About 14 years |
| The same, if the true edge is +10 | | about 930 | about 30 | About 30 years |

(80% power, one-sided test at 2.5%, independent events. Events cluster in time, so the true need is higher.)

Consequences:
- The exclusions can be confirmed live within about two years of the ledger's start, since calls need 12 months to
  resolve.
- **The Buy side of P1 cannot be proven live.** Its evidence must come from older history on WRDS, where crashes
  number in the thousands. That is why the audit of the earlier test (B0.1) comes first.
- The odds ledger resolves fastest. Every pivotal trial result and FDA decision in the universe is a scored forecast,
  whether or not the book holds the stock. The yearly count is taken at B0.

### 7.4 Statistics for lopsided payoffs
- Mean and median, hit rate, and average gain against average loss.
- Calendar-time portfolios: monthly, hedged, with the position caps of section 9. Event averages are shown but
  decide nothing.
- Confidence bounds by bootstrap, resampling whole months and whole companies.
- Fragility: the result without the three best positions of each year, and without takeovers.
- Returns include delisting returns. A bankrupt stock counts as a total loss unless a payout is recorded.
- Costs: entry at the next open; half the quoted spread by price and size group; a borrow fee on the hedge.

### 7.5 What a pod is compared with
1. The hedge index: XBI from 2006, and our own equal-weight universe index before that and as a cross-check after.
   BioCentury reported on 15 July 2024 that the XBI's index stopped being equal-weighted in June 2024 and now
   weights by trading volume. The hedge test in Batch A allows for this.
2. Matched peers: same size group and stage.
3. Baseline rules: cheap against cash with two years of runway; specialist-owned. A pod must add to these.
4. Placebo: 10,000 sets of random entries matched on month, size and stage.
5. Costs at the registered level and at double.

### 7.6 Verdict classes
- **Core**: passes the design-era test sheet; not negative after costs in the holdout; passes its live checkpoint
  (proposal: 60 resolved positions and 18 months); a live source for every input; an independent rebuild matches.
- **Exclusion**: predicts large losers in the design era and in the live ledger. Used as a filter.
- **Baseline**: works, but adds nothing to the baseline rules.
- **Incubator**: sound logic and partial evidence. Runs at small size or in shadow.
- **Shelved**: the rest. Logged; not re-run with tweaks.

## 8. Data plan

### 8.1 Sources
| Source | Gives | History | Runs |
|---|---|---|---|
| SEC EDGAR | Press releases in 8-K filings (results, FDA letters, deals); quarterly and annual reports (cash, going concern, financing terms); offering documents; insider trades; 13F, 13D and 13G | Filings from the 1990s; fuller 8-K reporting from August 2004; insider forms electronic from mid-2003 | Cloud, free |
| ClinicalTrials.gov | Trials, phases, goals, enrolment, dates, sponsors, and every past version of each record | Registry from 2000; broad from 2005-2007; results from 2008 | Cloud, free. The `cthist` package pulls version histories; AACT offers monthly copies |
| FDA | Approvals (Drugs@FDA); rejection letters on openFDA: 200+ in July 2025 (most already public in approval files), 89 more in September 2025, and prompt release since | Letters mainly from 2020 | Cloud, free |
| Open Targets | Genetic evidence linking drug targets to diseases, by dated release | To probe | Cloud, free |
| PubMed, bioRxiv | Papers and preprints for the analyst layer | | Connectors |
| WRDS | CRSP prices and delistings, Compustat quarterly cash, I/B/E/S estimates, 13F holdings, short interest | Decades | WRDS Cloud; statistics only |
| LSEG | Live prices, estimates, ownership | | PC; the probe is shared with step E1.1 of the shop |
| crash-triage | Daily closes, short interest, 13F and insider collectors, the press-release reader | 2020 onward | GitHub Actions |

Not available: commercial pipeline and sales-forecast databases, prescription data, options data. Two consequences.
There is no consensus peak-sales figure per drug, so "what the price assumes" is measured by proxies (run-up, short
interest, specialist ownership, the reaction on the day) and described by the analyst in words. And launches are
tracked on reported quarterly sales only.

Public tables built in the cloud (events, calendar) are uploaded to WRDS Cloud and joined there with returns. Only
statistics come back.

### 8.2 The event database and the calendar as known (the core build)
- One row per dated event: company; date and time; type; trial id; drug; disease; outcome as stated; source link;
  the verbatim sentence.
- Types: trial result by phase; interim look; FDA filing accepted, decision date set, approval, rejection, clinical
  hold, advisory vote; priced financing with size, discount, warrants and named buyers; partnership; takeover offer;
  going-concern warning; reverse split; strategic review; workforce cut.
- The calendar as known on each day: expected dates and windows ("results in the second half"), taken from earlier
  filings, each with the date it was said. Slipped dates are kept. They are a real cost.
- Built by Sonnet from 8-K exhibits. A script checks every quote. Opus re-reads a fifth blind. Fields with low
  agreement are dropped.
- Design era first. Events for 2011-2019 are extracted only at the freeze.
- A pilot of 200 events measures cost and agreement before anything is scaled.

### 8.3 The hindsight rule for history read by a model
A model that reads a 2015 press release may know what became of the drug. So:
- Backtests may use only fields that copy a stated fact with its quote: dates, numbers, "did not meet its primary
  endpoint".
- Fields that need judgement (was it the drug or the trial?) are forward only.
- Masked test: a sample is re-read with company, drug and dates hidden. A field that agrees less than 90% of the
  time is removed from backtests.

### 8.4 Gates before any test
| Gate | Pass when |
|---|---|
| BG1 Probe | We know what each source returns, and its limits |
| BG2 Universe | Listed biotechs by year and the share delisted look right; delisting returns are present |
| BG3 Coverage | At least 95% of the FDA's new-drug approvals of a test year are in the event database with the right date (proposal) |
| BG4 Coding | Two readers agree on at least 90% of key fields |
| BG5 Hindsight | The masked re-read agrees at 90% or better on every field used |
| BG6 Truncation | Cutting the data at any date leaves every earlier input, call and calendar entry unchanged |
| BG7 Two sources | Free prices and WRDS prices agree on overlapping months |
| BG8 Seal | Holdout years locked; lock id recorded |

## 9. Book construction and risk charter (proposals; fixed at B3)

### 9.1 Universe
US-listed drug developers and sellers by industry code, reviewed yearly. Main book: market value of $100M or more,
price of $1 or more, a floor on median daily trading value. Aftermath sleeve: from $50M, as in the triage. Large
pharma is out.

### 9.2 Sizing by loss-if-wrong
- Each position gets a loss scenario by type: a single-drug company held through a pivotal result or FDA decision; a
  company with several programs; a company with a marketed product; an Aftermath name. Placeholders: -70%, -40%,
  -30%, -60%. At B3 they are replaced by the bad-case losses measured in the design era.
- No position may cost more than 0.5% of capital in its scenario. So a single-drug company held through its result
  is at most about 0.7% of capital.
- The scenario losses of all events due inside any 30 days sum to at most 3% of capital.
- Weights follow the pod's score inside these caps. No weight is raised because a stock fell.

### 9.3 The hedge
- A short position in the biotech index, sized to the book's measured sensitivity, to keep net sensitivity within
  0.1.
- The instrument (XBI, a larger-company fund, or a basket of universe names) is set in Batch A by a rule: the one
  that leaves the least risk in the design era.

### 9.4 Single-name shorts
Off by default. A short sleeve opens only for a pod that passes the test sheet on its short side, and then:
- stocks with a market value of $1bn or more, short interest below 15% of the float, and high institutional
  ownership;
- no pivotal result or FDA decision due inside the holding window; no announced offer or strategic review;
- at most 0.5% of capital each, cut back past 0.75%; the sleeve at most 15% of capital.

The first candidate is the losing side of P5: launch misses in liquid names. Avoid-type names stay exclusions. They
are small, low-priced and scarce to borrow, which is probably why they keep falling.

### 9.5 Limits
| Limit | Proposal |
|---|---|
| Long book | Up to 100% of capital; 25 to 50 positions |
| Hedge and shorts | Up to 100% of capital |
| Net sensitivity to the biotech index | Within 0.1 |
| Largest position | 3% with a marketed product; 1.5% in development; 1% in Aftermath |
| One disease area | At most 30% of the long book |
| One drug target or class | At most 10% of the long book |
| Stocks under $100M | At most 10% of capital in total |
| Runway | Cash for 12 months past the next key event, or the name waits for its financing |
| Liquidity | A position can be sold in five days at a fifth of normal volume |
| Exclusions | E1 to E8, as accepted in Batch A |

Risk is budgeted by loss-if-wrong. Volatility and drawdown are reported against that budget. There is no price
stop: prices here jump past any stop. Exits are by time, by event and by kill facts.

### 9.6 What the desk does not do
No sector timing, no options, no leverage beyond the hedge, no averaging down, and no position without a dated next
event or a stated reason for having none.

## 10. Test sheet and budget
Design-era tests run on WRDS Cloud, monthly, on calendar-time portfolios built with the rules of section 9. Fewer
than 60 months or 100 positions is "insufficient data", not tested (proposal).

Decisive, all six:
1. **Positive after costs, hedged, and adds to the baseline rules.** One-sided; corrected for the number of pods in
   the batch (Holm).
2. **Not a few names.** Still positive without the three best positions of each year.
3. **Both halves.** The lower confidence bound stays above a small negative margin in each half of the design era.
4. **Double costs.**
5. **Placebo.** Above the 95th percentile of matched random entries.
6. **Tail.** The worst month and worst fall of the book with the pod are not materially worse than without it.

Reported, not decisive: by year; by state of the sector; by event type and cause; by size; share of return from
takeovers; hit rate; gain against loss; holding days; capacity.

Link tests that use no prices: forecast accuracy against base rates (P4); survival, and return of programs after a
crash, by cause (P1); whether a sales beat is followed by another (P5); whether the runway holds after a financing
(P7).

Budget:
- **Batch 0** (no slots): plumbing. Our universe index tracks XBI where both exist. Average moves on event days look
  as published.
- **Batch A**: hygiene, on the baseline rules only: cost model, entry timing, hedge instrument, horizons, each
  exclusion.
- **Batch B**: at most four pods, ranked by script on the number of independent investors, the share of criteria in
  the rule layer, and power. The batch may wrongly adopt a useless pod with at most 2.5% probability.
- **Replication of P1** on the older history: registered, and reported with the trial log. It takes no slot and can
  only say "reject" or "keep in Incubator".
- **Diagnostics** with gates fixed in advance (no slots): the return profile by month before a result (P3);
  recovery by cause of crash (P1).
- **Freeze**, then one holdout run. No redesign from it.

## 11. Live cycle
| When | What | Who |
|---|---|---|
| Daily | Crash and slide scan on closes; calls to the ledger (exists) | GitHub Actions; script |
| Weekly W1 | Refresh events and the calendar: new 8-K filings, registry changes, FDA calendar | script; Sonnet reads |
| W2 | Candidates per pod; exclusions; target book under the limits of section 9; hedge size | script |
| W3 | Risk report: loss-if-wrong by month, concentration by area and class, runway table, liquidity, every limit with its headroom | script |
| W4 | Odds sheets for every pivotal result and FDA decision due in the next eight weeks | Opus analysts |
| W5 | Ledger appended before the week starts | script; append-only branch |
| W6 | Scoring of resolved forecasts and positions; kill facts; stale inputs | script |
| W7 | One-page report, fixed template | Sonnet |
| Monthly | Attribution; post-mortems; review | script; Fable |
| Quarterly | Specialist map from new 13F filings; promotions at registered checkpoints only | script; Fable; Opus checks |

**The odds sheet** (one fixed form per event):
1. The event, its date window, and the source.
2. The reference class and its base rate.
3. A probability that the trial meets its main goal, or that the FDA approves.
4. Reasons, each tied to a source: earlier data with their uncertainty, trial design, evidence for the mechanism,
   the comparison drug, regulatory precedent.
5. The three likeliest ways to fail.
6. What the price seems to assume, in words.
7. Kill facts.

**Rules for the ledger.**
- Logged before the event. Scored with a proper score (Brier) against the base rate and against a simple feature
  model, overall and by disease area.
- Every event in the universe gets a sheet, held or not, so the record grows fast.
- After a crash, a cause sheet: the drug, the trial, the regulator or the balance sheet. Scored later on whether
  the program came back.
- The analyst's view may tilt sizes only after a registered checkpoint (proposal: 200 resolved forecasts), only
  inside registered bounds, and only in disease areas where its own record beats the base rate.
- The model id is logged. A model change starts a new record.

## 12. Steps
| # | Step | Agent | Gate / output |
|---|---|---|---|
| **B0** | **Audit and probes** | | |
| B0.1 | Trial log: find the earlier WRDS test of the triage rules; list every variant tried and the years used | Opus; PC runner | which years are spent |
| B0.2 | Truncation test of the triage inputs, calls and the top-performer list | Opus; script | BG6 for the existing tool |
| B0.3 | Masked re-read of 100 past press releases | Sonnet; script scores | BG5 for the existing fields |
| B0.4 | Re-run of 3.2 with next-open entry and spreads | script | cost-adjusted table |
| B0.5 | Freeze the triage rules: tag, config id, change log | Opus | "Aftermath v0" on record |
| B0.6 | Probes: press-release coverage by year; registry histories; FDA letters; Open Targets; WRDS tables; LSEG fields; the count of pivotal results and FDA decisions a year | Opus; Sonnet | BG1; counts |
| B0.7 | Inventory of the 37 transcripts | Sonnet | table |
| **B1** | **Event database** | | |
| B1.1 | Codebook and the 200-event pilot | Opus writes; Sonnet reads; Opus re-reads blind | cost; BG4 |
| B1.2 | Design-era extraction; calendar as known | Sonnet; script quote checks | BG3, BG6 |
| B1.3 | Universe, prices, cash and holdings on WRDS; upload of the public tables | Opus; WRDS runner | BG2, BG7, BG8 |
| **B2** | **Thesis library** | | |
| B2.1 | Claims with verbatim quotes from the 26 investor transcripts and any added sources | Sonnet; Opus second read | claim ledger |
| B2.2 | Process maps and fingerprint cards, with stage focus, science risk, event rules and shorts | Sonnet; Opus recodes a fifth | cards |
| B2.3 | Strategy map | script clusters; Fable judges; Opus checks | families |
| B2.4 | Charter per family, with the disagreements and the link-2 diagnostic | Fable; Opus check | charters |
| B2.5 | Thesis register; dated views to the forecast ledger | Opus; Sonnet | table |
| **B3** | **Specs and registration** | | |
| B3.1 | Pod specs; blind re-implementation | Opus; fresh Opus agent | approved specs |
| B3.2 | Loss scenarios and the risk charter from design-era data | Opus; script | charter |
| B3.3 | Odds sheet, base rates and scoring rules, frozen before outcomes | Opus | spec |
| B3.4 | Power check; slot ranking; registration | script; Opus | one-page summary to the user |
| **B4** | **Design-era tests (WRDS Cloud)** | | |
| B4.1 | Batch 0 and Batch A | Opus | reports |
| B4.2 | Diagnostics and the P1 replication | Opus | reports |
| B4.3 | Batch B; verdict by rule; independent rebuild of each passing pod | Opus; script; fresh Opus agent | result sheets |
| B4.4 | Batch review from the tables only; every statement quotes its number | Fable; Opus checks | review note |
| **B5** | **Freeze and holdout** | | |
| B5.1 | Freeze; extract the 2011-2019 events; one holdout run | Opus; Sonnet; script | report |
| B5.2 | Verdict | Fable; Opus checks the numbers | verdict note |
| **B6** | **Live** (section 11), from Stage 1 | | |

## 13. Order of work
1. **Stage 1, no new history needed.** B0. The paper book on the existing triage calls, with exclusions, hedge and
   the sizes of section 9, as an Incubator. The odds ledger. Output: one page on what is spent, whether the old
   inputs hold as of their dates, what the masked test shows, the cost-adjusted table, and the counts.
2. **Stage 2.** B1 and B2.
3. **Stage 3.** B3 and B4.
4. **Stage 4.** B5. Promotions by live checkpoints.

Effort, from what the macro program measured: about 6 to 9 Fable units (one map, four to six charters, one batch
review, one verdict), each about 0.65-0.9M tokens plus about 0.3M for its Opus check. The cost of the event build is
unknown until the pilot.

## 14. What can go wrong, and the answer built in
| Risk | Answer |
|---|---|
| Too few events for a firm conclusion | Power check first. Pods without power are judged live or shelved. No pooling that was not registered |
| Hindsight in history read by a model | Quote rule; masked test; judgement forward only |
| The Buy side never reaches proof | It stays an Incubator pod at small size. The desk then rests on exclusions, the hedge, and whichever of P2 to P7 pass |
| One market cycle | Results by year and state of the sector; older history |
| Specialist crowding: the same names fall together | Area and class caps; the hedge; crowding reported from 13F |
| A short blows up | Shorts off by default; a small tested sleeve; none into dated events |
| Policy shocks (FDA, pricing) | Not modelled. Caps by area. Views logged, not traded |
| The event build costs too much | Pilot first; design era first; holdout years only at the freeze |
| Entry and exit windows fitted to noise | Windows come from quotes; versions averaged; diagnostics with fixed gates |
| Costs in very small stocks | Next-open entry; spreads; the $100M floor in the main book; capacity reported |
| Results rest on takeovers | Reported apart; the "three best positions" test |
| University licences end | The free path (SEC, registries, FDA, daily closes) carries the live cycle |
| A model change breaks the analyst record | Model id logged; new record on change |

## 15. Needed from the user (facts, not design choices)
1. A go per stage.
2. More specialist transcripts or letters, if there are any. Ten investors today, two of them giving most of the
   material. Most useful: investors who buy companies below cash and push for the cash to be returned; long/short
   managers who talk about their shorts; a second voice on launches.
3. The LSEG probe pull, shared with the equity shop (step E1.1).
4. The PC switched on for step B0.1, so the earlier WRDS results can be found.

## 16. Points most likely to change
- Which years count as spent, after B0.1.
- Whether the hedge is XBI or a basket.
- The start of the design era (2001 or 2004).
- Whether P4 is workable without a commercial pipeline database.
- The $100M floor.
- Whether any single-name short ever leaves the Exclusion class.
- The checkpoint sizes for the live record.

## 17. References
Checked on the web (2026-11-15):
- BIO, Informa Pharma Intelligence and QLS Advisors, "Clinical Development Success Rates and Contributing Factors
  2011-2020": 7.9% from Phase 1 to approval; 12,728 phase transitions; biologics 9.1%, small molecules 5.7% (read
  from the CPHI summary; the phase-by-phase rates are in the full report).
- FDA press announcements of 10 July 2025 and 4 September 2025 on publishing complete response letters; FDA Law Blog
  on the first batch.
- `cthist` R package (version histories of ClinicalTrials.gov records); AACT (copies of the registry).
- BioCentury, 15 July 2024, "Biotech losing its XBI barometer".
- Princeton University Library data FAQ (Compustat short interest on WRDS).
- PubMed records: Wong, Siah and Lo (2019) on trial success rates; Rothenstein and others (2011) on stock prices
  around oncology announcements; Hwang (2013) on stock returns and trial results; Minikel and others (2024) on
  genetic evidence and clinical success.

From the designer's knowledge, to be verified when each enters the store: Hay and others (2014) on success rates;
Nelson and others (2015) on genetic evidence; Lo, Siah and Wong (2019) on predicting approvals from trial features;
Thakor and others (2017) on the returns of the sector; Loughran and Ritter (1995) on returns after share issues. Not
found: the 2025 paper on about 20 binary events that Theill cites.

## 18. Terms
- **Pivotal trial, result, main goal**: the late-stage trial an approval rests on; the first public summary of its
  outcome; the single measure the trial was designed to move (primary endpoint).
- **FDA decision date; rejection letter**: the date by which the FDA must answer a filing (PDUFA date); the letter
  it sends when it does not approve (complete response letter).
- **Runway; funding gap**: how long the cash lasts at the current rate of spending; the cash still to be raised.
- **Enterprise value against cash**: what the market pays for the company beyond its cash, as a multiple of that cash.
  Below zero means the company is priced under its cash.
- **13F, 13D**: quarterly holdings reports of large funds; filings by holders of 5% or more who intend to press for
  change.
- **Specialist**: a fund with most of its reported holdings in biotech.
- **XBI**: the largest fund tracking small and mid-size US biotech stocks.
- **Hedge; net sensitivity**: a short position that offsets the sector's moves; how much the book still moves when
  the index moves by one.
- **Base rate**: how often something has happened across all similar cases.
- **Brier score**: a score for probability forecasts; lower is better.
- **Calendar-time portfolio**: a test that holds the positions as an investor would, month by month, instead of
  averaging events.
- **Loss-if-wrong**: what a position costs if its event goes badly.
- **Kill facts**: observable facts that end a thesis.
- **Placebo; Holm correction; seal; holdout**: as in the shop design (section 20 there).
