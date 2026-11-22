# Equity pod shop: plan v0.5 (2026-11-22)

Status: design adjusted on the user's feedback of 22 Nov. It replaces plan v0.4 where they differ (section 13);
v0.4, v0.3 and the annex v0.2 stay in force for everything not restated here. The registered rules are in
`V04_REGISTRATION.md` addendum A10. Built or run so far: the reference book (Batch 0, trial T001), the conviction
holdings, the say-do tables. No recipe, pod, hit rate or winner test exists yet. Not yet checked by an independent
agent (section 14).

## 1. Purpose (user, 2026-11-22)
The tools have three uses and are judged on them:
1. **Spot individual winners early.**
2. **Control risk.**
3. **Construct portfolios.**

The end product is a **private dashboard on the website**. The investors' material is the source of the rules.
Before a rule is tested, it must be shown to be what the investor says and what the investor does (sections 4-6).

## 2. What changed against v0.4
| # | Change | User, 22 Nov |
|---|---|---|
| 1 | Judged on the three uses: a scorecard with the blocks Winners / Risk / Construction replaces the single "added return" verdict. The five tests of v0.4 stay inside it | "judge it based on that" |
| 2 | A material bar per investor; thin files are filled before a recipe is written | "review which key investors has thin materials then we can go look for it" |
| 3 | Every claim tagged (rule, threshold, example, anecdote ...) and dated; a second agent checks every rule-like claim blind | "need to have an agent to review and verify" |
| 4 | Held-out document test | "okay do that" |
| 5 | A recipe has five parts including construction. Each pod runs in an **investor form** (as concentrated and as long-held as the investor says or the 13F shows) beside the broad form. Concentration is tested as such | "test concentration too if the investors said that or in the past their portfolio reflects that" |
| 6 | Recall test: does the recipe, applied at the quarter-end before, find the investor's own purchases? A kill criterion for the premise follows the pilot | "you have their buy history quarter by quarter" |
| 7 | Names review: dashboard v0 shows each pilot recipe's picks beside the investor's holdings as soon as the first LSEG files load | "design that as part of the process" |
| 8 | Analyst layer moved up: the screen generates ideas; dated forecasts are scored live | "okay too" |
| 9 | The end product is named: the private dashboard (section 10) | "the final result should still be a private dashboard" |

Two earlier suggestions were not answered and are not built in as rules: "fewer investors, deeper" (the material
bar orders the work instead) and "judge on business outcomes first" (business outcomes are a reported line).

## 3. The path from an investor to the dashboard
Each gate is checked by someone other than the builder. Pass rules are registered in A10.

| Gate | What | Built by | Checked by | Pass rule |
|---|---|---|---|---|
| G1 Material | The investor's file meets the bar | Script on the inventory | Referee | At least 3 own-words documents of 5,000 words or more; one written primary source or one document with explicit criteria. Else "thin": material is collected first |
| G2 Claims | Verbatim quotes, each with tags and dates | Sonnet | Script finds every quote in the text | All quotes exact |
| G3 Verification | Second blind tagging of every rule-like claim and 30% of the rest; 10 planted errors | Opus, without sight of the first tags | Script compares; Fable reads disputes | Agreement 90% (rule-like or not) and 85% (part, computable); 9 of 10 planted errors found. A claim is a rule only if both readers say so |
| G4 Card | The method in five parts (buy, price, avoid, sell, size), built WITHOUT one held-out document | Opus | A second agent against the quotes | Every line traces to a verified rule |
| G5 Held-out | The held-out document read against the card | A fresh agent | Script | 70% of its rule-like claims already on the card; no open contradiction on buy, price or sell. Then it is merged |
| G6 Recipe | Screen, price rule, avoid rules, sell rule, construction, and the analyst checklist (what a script cannot compute). Every number tagged with its origin | Opus | A second agent against the card; screenability counted twice (R1) | v0.4 |
| G7 Blind rebuild | A fresh agent rebuilds the screen from the written recipe alone | Sonnet | Script | Rank correlation 0.95, list overlap 0.9 (v0.4) |
| G8 Recall | The recipe at the quarter-end before each of the investor's conviction purchases | Script on WRDS | Registered rule | Lift 2.0 or more (90% interval above 1.25), recall 25% or more, lift above the control investors' and the reference screen's |
| G9 Names review | Current picks beside the investor's latest 13F on the dashboard | Script; read by the referee and the user | Registered rule | At least 5 of the 10 largest holdings pass the non-price criteria |
| G10 History | Scorecard W / R / C on 2010-2025, one logged run per pod | Test-desk scripts | Second implementation; registered rules | Section 7 |
| G11 Live | First flags with a live placebo; analyst memo and forecasts per flag; paper portfolios in both forms | Scripts; analyst agents | Scored by script | Sections 8-9 |

**Kill criterion** (after the pilot, between G8 and G9): the premise "an investor's stated method can be written
as a screen that describes what they buy" stands if at least 2 of the 3 pilot investors pass G8 after at most one
revision round in which every change cites a quote. If not, no further recipes are written: the material goes to
the analyst layer as checklists, and the dashboard is built on the reference book, the owner panel and the
analysts' forecasts.

## 4. Reading the investors
### 4.1 Material bar
- M1 volume: at least 3 documents of 5,000 words or more in the investor's own words.
- M2 depth: a primary written source (letter, manual, book) or a document graded "explicit criteria".
- M3 parts: a verified buy rule from quotes. For price, avoid, sell and size: a verified rule, a verified statement
  that none applies, or "none stated" (then the part comes from the 13F or a convention and is tagged so).
- Recorded, not a bar: the span of the dated documents. The earliest dated statement of a rule is its thesis
  date; results are also shown for the months after it (before it, the rule is hindsight).

First read (`MATERIAL_REVIEW_2026-11-22.md`): 2 of the 21 files are ready (Greenblatt, Kantesaria). The library
holds interviews; letters, manuals and books are mostly missing, and those are where investors write rules down
with a date. Two of the three pilot investors are thin: Terry Smith (2 interviews of 2022, nothing on price,
avoid, sell or size) and Zlatev (2 interviews). Collect first: Fundsmith's annual letters 2010-2025 and Owner's
Manual, then Zlatev's podcasts. An investor is never dropped for a thin file; the recipe waits.

### 4.2 Tags (per claim)
kind: rule / threshold / example / anecdote / principle / view / mistake. part: buy / price / avoid / sell /
size / other. scope: all holdings / a sector / a period / one company. Date said and period meant. computable:
yes / by proxy / no. strength: always / usually / sometimes. Only verified rules and thresholds enter a recipe;
examples and anecdotes illustrate a rule on the card and never set a threshold.

### 4.3 Verification by a second agent
A different model tags blind: every claim the first reader tagged rule or threshold, plus a random 30% of the
rest, plus 10 planted items (5 anecdotes dressed as rules, 5 altered thresholds). Disputes go to a third reading
on the quote alone. A file that misses the agreement bars is re-extracted, not patched.

### 4.4 Held-out document
For every investor with 3 or more long documents, a script draws one (seeded, 5,000 words or more) that the card
writer never sees. After the card is written, a fresh agent lists what the held-out document adds, contradicts
and confirms. Low coverage means the file is not yet complete: more material first. After the test the document
is merged and the result stays on the card.

## 5. The recipe and its construction
A recipe = what a script can run (screen, price rule, avoid rules, sell rule, construction) + the analyst
checklist (the judgement the investor applies after the screen). Every number carries its origin: quote /
revealed by purchases (odd years set it, even years check it) / revealed by 13F / convention / grid (versions,
averaged, never picked).

Each pod is run in two forms:
- **Broad form**: every stock that passes, held under the tranche rule of v0.4 (R4). It tests the logic.
- **Investor form**: the number of names, the weights, the cap and the holding rule come from the investor's
  words, else from the 13F history (job `eq_prof`: number of names, top-5 weight, largest weight, starting weight,
  holding time, share of the book that is new each year). Where words and 13F differ by more than a factor of
  two, both are versions. Entry needs the whole recipe; a holding stays while it meets the non-price criteria and
  is sold on a stated sell rule or after four failing quarter-ends.

What the 13F already shows (`eq_conv_v2`): Kantesaria, Hohn and Dorsey hold about 9 names with 71-90% in the top
five; Terry Smith 31 with 39%; Greenblatt's filer holds about 910 (a quantitative book). The reference book holds
about 150. So the investor form differs a great deal between pods, as it should.

## 6. Does the recipe describe the investor?
1. **Blind rebuild** (G7): the written recipe is complete enough that a stranger gets the same list.
2. **Recall** (G8): of the investor's conviction purchases (R2) in the universe, the share that passed the recipe
   at the quarter-end before. Base rate = pass rate of stocks of the same quarter, sector and size third.
   Lift = recall / base rate. Two baselines: the same recipe on the control investors' purchases (is it specific
   to this investor?) and the reference-book screen on this investor's purchases (does it describe them better
   than plain factors?). The decisive form uses only thresholds from quotes and conventions; thresholds revealed
   by purchases are checked on even years only. The writer gets back only the rates and, per criterion, the share
   of purchases it rejects; never names.
3. **Names review** (G9): the first time real names are looked at. Read by the referee and the user, not by the
   recipe writer. A miss uses the same single revision round as the recall test.
4. **Say-do table** (done, A9) stays on the card: stated criteria beside what the purchases looked like.

## 7. The scorecard: how a pod is judged
One logged run per pod prints all three blocks. Definitions (A10): a **first flag** is a stock entering the pod's
pass set after 12 months outside it. Outcome = total return over the next **36 months** (12 and 60 reported),
ranked inside sector and month: winner = top fifth, big winner = top tenth, loser = bottom fifth, big loser =
bottom tenth; permanent loss = minus 50% or worse. **Net hit rate** = share of first flags that became winners
minus share that became losers; a random list scores 0. The yardstick is a **matched placebo**: random stocks of
the same month, sector and size third, 5,000 sets.

**W. Winners early**
- W1 (decisive): net hit rate above the matched placebo (Holm 2.5% across the pods of a batch), not below the
  placebo in any era, at least 100 first flags.
- W2 (label "beyond the reference book"): the same against random stocks that also match the reference-book score.
- Early (label "finds them early"): the same on flags of stocks that were not already 36-month winners.
- Reported: time to recognition (how much of the gain came after month 12); business winners (growth of
  operating profit over 36 months) and how often a business winner became a price winner; results after the
  thesis date.

**R. Risk**
- R1: fewer big losers among first flags than the placebo (5% level); permanent-loss rate reported.
- R2 (avoid rules): the stocks an avoid rule flags turn out losers at least 1.5 times as often as winners,
  significantly (Holm 2.5% across the avoid rules of a batch), and it does not throw out big winners more often
  than chance.
- R3 = the tail test of v0.4 (worst fall and worst month of book plus pod).
- Reported: the stated sell rule against never selling and against the rank rule.

**C. Construction**
- C1 (broad form) = tests 1-4 of v0.4: added return over the reference book, by era, at doubled costs, against
  1,000 random portfolios.
- C2 (investor form): 1,000 portfolios built by the investor-form rule with names drawn at random from the
  passers. "Concentration sound at N" when at least 60% of them end ahead of the sector-matched universe after
  costs and at most 10% fall more than 15 points deeper than it. "The ranking helps" when the recipe's own
  top-N beats 95% of the draws. A concentration curve (5, 10, 20, 40, all) is printed; N is never picked from it.
  C2 describes what holding few names of this list did; it is not extra evidence of skill. Holding fewer names
  widens the range of results and raises the expected result only if the choice inside the list is better than
  chance. That choice is the investor's judgement, which only the live analyst record can test.

**Classes** (a pod carries every label it earns; the dashboard shows all three blocks)
| Class | Needs | Use on the dashboard |
|---|---|---|
| Winner list | W1 and checks B and C on W1 | Candidates page |
| Portfolio | C1, R3 and checks B and C (= v0.4 "Passed on history") | Paper portfolio |
| Risk rule | R2 | Red flag on every company; exclusion in its own pod |
| Full pass | Winner list + Portfolio + R1 | All three |
| Tail sleeve, Incubator, Shelved | As v0.4 | Shown as such |

Check B = better than the pods built the same way from the control investors. Check C = the result survives
without the stocks its own source investors held. No investor pod is Core on history; Core comes from the live
rule only. The reference book gets its own scorecard first (trial T002), as the bar every pod is shown against.
Each block is its own family of tests: the chance of one false label per batch is up to 7.5% (v0.4: 2.5%); a
Full pass needs all three.

## 8. Analyst layer (live only)
For each new first flag of a registered pod, and any company the user adds: a memo within the month. It answers
the investor's checklist from filings and transcripts with quotes, sets three scenarios, gives probabilities
(winner, loser, permanent loss over 36 months), names kill criteria as observable conditions, makes 3 to 5
forecasts that resolve within 12 months, and gives a grade. Stored with its date, never edited. Scored by script
(Brier score against base rates and against the pod's historical rates). Checkpoint at 200 resolved forecasts:
the grade ranks candidates on the dashboard only if it beats the base rate; otherwise memos are shown as notes.
No analyst judgement enters a backtest.

## 9. Live record
Paper portfolios in both forms for each registered pod (append-only ledger). With every live first flag the
script records 20 matched random names, so live hit rates have their own placebo. Monthly check that each paper
portfolio equals its frozen rule. The live record decides promotion (v0.4).

## 10. Dashboard (the end product)
| Page | Shows |
|---|---|
| Winners | New and standing first flags per pod: class, historical net hit rate, early or late, months since the flag, owners (roster 13F), red flags, analyst grade |
| Company | Like-for-like measures ranked in the sector, valuation panel, recipes passed and failed (which criterion), owners, memo, forecasts, kill criteria |
| Investors | Card with quotes, material depth, say-do table, recall, construction profile, picks beside holdings |
| Portfolios | Paper portfolios in both forms: holdings, weights, trades, returns against the universe and the reference book |
| Risk | Per portfolio: concentration, sector weights, falls, liquidity, overlap between pods, crowding, exclusions hit, kill criteria triggered |
| Scoreboard | W / R / C per pod, with the number of trials behind each line and what the result can and cannot claim |
| Log | Registrations, trial log, data and code versions |

Private: behind the site password, as its own page of the website; the existing pages are not changed. Only the
derived figures that are displayed leave the PC; LSEG files and WRDS rows never do.

## 11. Build order (user paces the steps)
| Step | What | Needs |
|---|---|---|
| 5b | Scorecard code in the engine (first flags, outcomes, placebo, investor form, draws) with tests; T002 = the reference book's own scorecard; construction profiles (`eq_prof_v1`) | WRDS runner (PC on) |
| 5c | Second implementation of engine and scorecard by a separate agent | User's go |
| 6a | Material for thin files into the library | User saves the documents |
| 6b | Pilot through G1-G8: Greenblatt first (file ready), Terry Smith and Zlatev when their files pass G1, one control investor; kill decision | User's go (agents) |
| 7 | Dashboard v0: reference-book list, company table, pilot picks beside holdings (G9) | LSEG pieces P01-P18; site password |
| 8 | Other investors in order of material depth; strategy map, charters, recipes; slots; history scorecards | - |
| 9 | Live: flags with placebo, analyst memos, paper portfolios in both forms, scoreboard; freeze; outside-US run | - |

If Zlatev's file still misses G1 after the search, the next grade-A investor with a ready file (Kantesaria) takes
the pilot place.

## 12. Limits
- Winners are measured in the same years in which the investors were chosen. Checks B and C, the thesis-date
  split and the live placebo limit this; they do not remove it.
- A 36-month outcome leaves 13 formation years (2010-2022), about four separate windows, in a period that
  favoured quality and growth. Hit rates from it are weak evidence.
- Concentrated investors made few purchases (Kantesaria 32, Li Lu 17 in 16 years): recall intervals are wide;
  under 20 purchases recall is not measurable.
- The recall test and the one revision round fit the recipe to purchases of the test years; check C is the guard.
- A backtest of the investor form cannot reproduce which names the investor would have chosen from the list.
- Three test families instead of one raise the chance of a false label (section 7).

## 13. Amendments to v0.4
| Where | v0.4 | v0.5 |
|---|---|---|
| Section 1 goal | Which strategies outperform consistently | Three uses (winners early, risk, construction); dashboard as the product |
| 5 roster rule 2 "Material" | One long document | Material bar M1-M3 before a recipe is written; the roster itself is unchanged |
| 3 desk 1 check | Opus re-reads a fifth blind | Tags; every rule-like claim verified blind; held-out document |
| 3 desk 2 | Spec = screen | Recipe in five parts; investor form; recall test; kill criterion |
| 8 portfolios | One form (tranches, 2.5% cap) | Broad form (unchanged) and investor form |
| 8 tests, classes | Five tests; Passed on history / Sleeve / Exclusion / Incubator / Shelved | Scorecard W / R / C; classes of section 7; the five tests are C1 and R3; Exclusion is tested by R2 |
| 8 budget | 8 pod slots | 8 pod slots, each one run printing all blocks; at most 8 avoid rules per batch |
| 10 build order | Steps 5-9 | Section 11 |
| Fence 2 | Writers see aggregates of 20 purchases | Unchanged; recall feedback is rates only; the names review is read by the referee and the user |

## 14. Checks still due
An independent check of this plan and of A10 (on the user's go; none was used for v0.4 or v0.5). To test first:
the power of W1 at 100 to 300 first flags; whether the placebo match (month, sector, size third) is tight enough;
the recall bars on investors with few purchases; whether check B has enough control pods; the 60% / 10% bars of C2.
