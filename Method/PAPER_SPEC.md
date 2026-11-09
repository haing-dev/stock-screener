---
tags: [method, spec]
file: papers/PAPER_SPEC.md
---
# Paper extraction spec v2 (2026-11-05: + claim role, + reasoning map)

Goal: a complete, verifiable ledger of everything in ONE research paper that a systematic macro researcher could use,
precise enough that the strategy can be rebuilt and re-tested from the ledger alone. Completeness beats brevity.
Read the WHOLE document: every chunk [C01]..[Cnn] (one chunk = one PDF page), including footnotes, exhibit notes and
appendices. Footnotes often hold the exact construction (data substitutions, lags, sample periods): extract them.
Exhibits that are charts: look at the page image `img/<SOURCE_ID>-p-NN.png` (NN = page number, two digits) with the
Read tool and record what the exhibit shows (numbers you can read, direction, period), with the exhibit title as quote.

## What counts as a claim (extract ALL)
- Mechanism: why the effect exists (cause -> effect), and evidence offered for it.
- Signal construction: every input series, transformation, lookback, lag, scaling, sign, weighting, rebalancing,
  universe, data substitution by period, costs assumed, volatility target. One claim per distinct design choice.
- Results: every reported number (Sharpe, return, vol, correlation, t-stat, drawdown, hit rate) with its sample,
  gross/net, and the exhibit it comes from.
- Robustness / regime / sub-period findings; when it works and when it fails; comparisons with other strategies.
- Caveats, limitations, hypothetical/backtest disclaimers that change how results should be read.
- Implementation claims (capacity, turnover, costs, combination weights with other strategies).
- Citations used as evidence for a mechanism (name + what they showed).
Exclude: boilerplate legal disclosures (one claim summarising them is enough), author bios, repetition.

## Output: papers/<engine>/<SOURCE_ID>.json, exactly this shape
{
 "source_id": "QP01",
 "speakers": ["author names (affiliation)"],
 "summary": "3 lines max: question, method, main conclusion",
 "approach_tags": ["economic trend", ...],
 "coverage": [{"chunk": "C01", "claims": 2, "note": "topics; 'nothing actionable: <reason>' if 0"}, ...],  // EVERY chunk
 "claims": [
  {"claim_id": "QP01-C03-1", "chunk": "C03", "speaker": "authors",
   "quote": "verbatim words copied exactly from that chunk's TEXT, max 40 words (never from an image)",
   "claim": "X means / causes Y because Z (one sentence, your words)",
   "claim_type": "mechanism | construction | result | robustness | caveat | implementation | citation",
   "exact_rule": "the operational rule if any, precise enough to code (inputs, transform, lookback, sign, scaling), or empty",
   "data_needed": "series and sources needed to replicate, or empty",
   "reported_result": "numbers exactly as reported with sample/period/gross-net and exhibit, or empty",
   "exhibit": "Exhibit n or footnote n or empty",
   "mechanism": "slow_reaction | risk_premium | overshoot | cycle_persistence | liquidity_flows | policy_reaction | crowding_positioning | seasonality | fiscal_debt | structural_shift | risk_management | research_method | behavioral | new: <name>",
   "asset_class": "equities | rates | fx | commodities | credit | multi | other",
   "indicator": "exact series / signal named, or empty",
   "horizon": "days | weeks | months | years | unspecified",
   "direction": "long/short or up/down implication, or empty",
   "conditions": "when it works / fails, or empty",
   "testable": "yes | partly | no - one short reason",
   "speaker_confidence": "high | medium | low (as the authors express it)",
   "time_bound": "yes | no",
   "role": "premise | mechanism_step | design_choice | evidence | conclusion | qualifier | context"}
 ]
}

## Rules
- Quote = character-for-character copy from the text of the chunk named in "chunk" (a script checks it). Footnote
  quotes count; keep hyphenation as printed.
- Every chunk appears in coverage; per-chunk claim counts must match the claims list.
- Write the file, then validate it: JSON loads, every chunk covered, counts match, every quote found in its chunk
  (lowercase, whitespace-collapsed substring test is enough).
- Use only the paper (text + its page images). Do not read any other extraction output or notes.

## Reasoning map (ONLY when your task says "with reasoning map")
The point of this project is the authors' logical foundation, not isolated facts: why they believe markets behave
this way, how one step leads to the next, why each design choice follows, and what the evidence does and does not
prove. Add a top-level key "reasoning" to the same JSON. Every element cites claim_ids from YOUR claims list (add
claims if a needed step has no claim yet). Anything the authors did not say is your inference: put it only in the
fields marked (reader) or set "stated": "implicit".
"reasoning": {
 "question": "the problem the authors try to solve and why it matters to an investor",
 "thesis": {"statement": "central conclusion in one or two sentences", "claim_ids": []},
 "foundations": [{"premise": "belief about how markets/economies behave that the argument rests on",
   "type": "empirical | theoretical | behavioural | institutional | assumed", "stated": "stated | implicit",
   "support": "how the authors justify it (test, citation, intuition, none)", "claim_ids": []}],
 "mechanism_chain": [{"step": 1, "from": "cause", "to": "effect", "why": "the link as the authors explain it",
   "evidence": "test | citation | example | assertion", "claim_ids": []}],
 "design_rationale": [{"choice": "a construction decision", "reason_given": "why (or 'not given')",
   "alternatives": "what they compared or mention", "sensitivity": "what changes if varied, or 'not shown'", "claim_ids": []}],
 "evidence_map": [{"result": "a key finding", "tests": "which premise or step it tests", "rules_out": "",
   "does_not_rule_out": "(reader) alternative explanations still open", "strength": "strong | moderate | weak - why",
   "claim_ids": []}],
 "regimes": [{"condition": "when", "effect": "what happens to the logic or results", "claim_ids": []}],
 "gaps_and_conflicts": [{"issue": "unspecified detail, internal conflict, untested assumption, data problem",
   "type": "unspecified | conflict | untested | data", "claim_ids": []}],
 "relations": [{"other_idea": "e.g. price trend, carry, value", "relation": "complement | substitute | special case | contradicts",
   "why": "", "claim_ids": []}],
 "forward_looking_inputs": "(reader) which observable inputs this logic says lead future prices, over what horizon,
   through which step of the chain, and what would make them stop working",
 "reader_inferences": ["(reader) every inference you made that the authors did not state"]
}
Validate that every claim_id cited in "reasoning" exists in your claims list.
