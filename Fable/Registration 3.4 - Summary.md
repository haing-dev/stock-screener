---
tags: [fable, thesis]
code_commit: c32ce07
---
> One-page summary. See [[Registration 3.4]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/c32ce077b96bb13f580359e8f3e937f418e1191c/docs/research/registration/SUMMARY_FOR_USER.md).
# Registration (step 3.4): one-page summary

Registered 2026-11-23 as section 7 of TESTING_PROTOCOL.md after an independent check (32 corrections applied). Nothing has been run.

**What gets tested, in this order**
1. Engine fixes first: switch off Bloomberg-only inputs, fix the wrong index map, stop reading quarterly inflation
   before it was published, lag non-US dividend yields as late as they arrive live, and make sure nothing after
   31 Dec 2010 can be read. Then new engine features: trading one day after the signal (as live), version averaging,
   weekly tranches, and the test code.
2. Batch A, upkeep of the existing book (test: "does not hurt"). A1 adds Bloomberg history only before the free data
   start (reported, not tested; needs the PC to run pandas again). A2 averages each pod's versions (Trend 16, Economic trend 2, Carry 2,
   Value 2). A3 runs only the upkeep items the diagnostics open (more markets, a no-trade buffer, a faster risk scaler).
3. Core book v1 is formed from the parts of the existing pods allowed into Core (below). They must pass placebo, double costs, tail and an independent rebuild; "adds to the book" is only reported for them (they were designed on the same years), so the holdout is the existing book's only independent test.
4. B1: Curve carry. B2: Strip reversion (only if its diagnostic passes) plus the card rules that pass their gates (up
   to 76 versions in 17 rules, 128 with entry and sizing versions, more if card 2 or card 4 diagnostics add versions).
5. Freeze, then one holdout run on 2011-2026.

**What can and cannot pass**
- "Documented before 2011" means a pre-2011 source states the rule (what is measured, which way, on what), even
  without a cause. Can be Core: Trend, currency carry in its ranked form, energy carry, equity value. Run in shadow:
  Economic trend, bond carry, directional currency carry, bond value, currency value. So Economic trend leaves the
  traded book (15% of the candidate). The Core book holds its parts at equal risk; the old 45/25/15/15 split no longer
  fits the book that is left.
- No new pod can become Core with today's data, so B1 and B2 only decide Incubator or Shelved: Curve carry has no
  pre-2011 source; Strip reversion has one but no registered live data source; card rules are shadow-only by design.
- "Adds to the book" passes a truly good new pod (information ratio 0.4 over 36 years) about 56% of the time, about 38%
  for the shorter spread pods, and about 3-4% if it adds nothing (4% for the spread pods). A pod that only repeats what the book holds is
  correctly rejected. A failed pod is written up as "not shown", not "refuted".
- Card rules with fewer than 48 active months or fewer than 3 episodes cannot be judged; they become analyst watch
  items.

**What is blocked (and what unblocks it)**
- LSEG is not yet a registered source: it needs a reader, a lock with the 2011 seal, a weekly refresh on your PC, and a
  written statement that the licence allows live use. Until then it blocks Curve carry, Strip reversion, the
  short-rate futures markets, card 3 R4 and card 5 R1.
- Eurodollar daily prices for contracts 3, 5, 6 and 7 (one small LSEG pull): blocks Strip reversion's diagnostic.
- Windows blocks pandas on the PC: stops A1 and every Bloomberg or LSEG job.
- UK and euro 3-month rates stop updating in early 2027: a free replacement must be registered before then.

**At the holdout**
- The frozen Core book passes if all four hold: net Sharpe at least 0.3, worst fall better than -25%, correlation with
  the S&P at most 0.3, 2022 positive. Even a good book (true Sharpe 0.8) passes only about 58% of the time: this screens
  out a broken book; it does not prove skill.
- Pass: the Core book becomes the paper book of record. Fail: it keeps running on paper, labelled failed, its expected
  Sharpe cut to the holdout Sharpe if that is lower (not below 0), and no real-money step before the live checkpoints. Nothing is
  redesigned from holdout data either way.
- After the holdout any pod is promoted only on its live record, at checkpoints after 120 and 180 live months (a good
  pod passes only about 1 in 4 at 120 months and 1 in 3 at 180). Analysts are scored at every 200 resolved forecasts;
  they never touch positions under this registration.

Items left to 3.4: 100; 93 settled, 7 blocked (LSEG registration, LSEG licence statement, T09/T10 market histories,
Eurodollar daily pull, Fung-Hsieh factor file, PC pandas block, UK/euro rate replacement: rule and deadline set).

