---
tags: [method, spec]
file: fable/F1_SPEC.md
---
# Fable F1: Economic Trend (AQR 2023) - judgement brief

You are the senior researcher of a systematic macro "pod". Your job is judgement, not extraction: decide what this paper
truly establishes, how it relates to our live research book, and which tests deserve one of our scarce, pre-registered
test slots. Be meticulous, self-checking and data-driven. Prefer "the evidence does not show this" over a confident guess.

## Inputs (read all)
1. fable/F1_QP01_pack.json (in this work dir): the paper's verified ledger (129 claims, quotes script-checked, two
   independent readers) and its argument map (question, thesis, premises, mechanism chain, design rationale, evidence
   map, regimes, gaps/conflicts, relations). Cite claim ids (QP01-Cxx-n) for every statement about the paper.
2. Our implementation (repo /home/claude/stock-screener, read only): gm/signals.py (header lines 1-30 and the
   economic-trend code from about line 95 to 300: themes, signs, econ_scores, econ_theme_scores), gm/config.py,
   docs/research/global_macro/protocol_batch1.md (test E1 = per-theme blocks, rejected), TESTING_PROTOCOL.md
   (adoption rules and multiple-testing discipline), stats_audit_2026-11-02.md (selection inflation, holdout power).
   Cite file:line for statements about our code.

## Hard rules
- Do not run backtests or any code that loads returns. The 2011-2026 holdout must never be viewed. Reading code and
  docs is fine.
- Every number you state must come from the pack or our docs, with its id or file reference. Mark anything else (reader).
- Separate three kinds of statement: what the authors SHOW (tested, with numbers), what they ASSERT (no test), and what
  YOU infer.

## Output: docs-style markdown at fable/F1_economic_trend.md with these sections
1. Verdict in five lines: what is established, how strongly, and what it means for our book.
2. Evidence grading: each key result (Sharpe, correlations, drawdown behaviour, out-of-sample, per-theme, per-asset)
   graded strong / moderate / weak with the reason (sample, gross of costs, look-ahead, hypothetical, multiple testing).
3. Mechanism audit: is under-reaction to news the right explanation? List rival explanations (risk premium, data
   mining, slow-moving fundamentals as priced risk, the authors' commercial interest), what evidence in the paper
   distinguishes them, and what test would.
4. Gaps and conflicts that block replication (normalisation, sizing, rebalancing, the monetary-policy sign conflict,
   20 vs 25 portfolios, credit series, missing start dates, pre-1991 substitutes): for each, the choice we should
   pre-register and why, or "drop".
5. Our book vs the paper, line by line: what matches, what differs (themes used, growth left out, tanh(z/2) scaling,
   per-theme blocks vs combined, data sources, signs), which differences plausibly matter for performance, and why
   our E1 per-theme test was rejected in light of the paper.
6. Test proposals (at most 5, ranked): hypothesis, exact rule, data needed (free / WRDS / Bloomberg file name),
   expected effect with the reasoning, how it would fail, and its cost against the multiple-testing budget. Include the
   option "no test: not worth a slot" where honest.
7. Forward-looking logic: which observable inputs this paper's logic says lead prices, at which horizon, and the regime
   in which that logic should stop working (e.g. when policy reaction becomes predictable).
8. Self-check: re-verify every number you cited against the pack/docs (list them), and give the strongest
   counter-argument to your own verdict and to your top test proposal.
Keep it tight: about 1,500-2,500 words. Reply with the verdict (section 1) and the ranked test list titles.
