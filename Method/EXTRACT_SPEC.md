---
tags: [method, spec]
file: EXTRACT_SPEC.md
---
# Extraction spec v0 (pilot, 2026-11-02)

Goal: turn one transcript into a complete, verifiable ledger of every idea a systematic macro researcher could use.
Completeness matters more than brevity. You read the WHOLE document, every chunk [C01]..[Cnn].

## What counts as a claim (extract ALL of these)
- How markets or the economy work (cause -> effect), incl. historical analogies used as evidence.
- An indicator / signal / data series and what it says or predicts.
- A strategy, portfolio-construction, sizing, risk-management, execution or cost method.
- A research or testing method (backtests, overfitting, evaluation, track records).
- A regime or condition statement (when something works or fails).
- A specific market view with its reasoning (mark time_bound = yes).
- A named data source or number that supports a mechanism (e.g. "CTAs lost 8% in Q3").
Exclude: greetings, plugs, biography with no method content, repetition of an idea already recorded (one claim per
distinct idea; do not split one idea into many, do not merge two ideas into one).

## Output: one JSON file (UTF-8), exactly this shape
{
 "source_id": "MT00n",
 "speakers": ["name (role)", ...],
 "summary": "3 lines max: who, what approach, main conclusions",
 "approach_tags": ["trend following", ...],
 "coverage": [{"chunk": "C01", "claims": 3, "note": "topics covered"}, {"chunk": "C02", "claims": 0, "note": "nothing actionable: intro and sponsor read"}, ...],   // EVERY chunk listed
 "claims": [
  {"claim_id": "MT00n-C03-1", "chunk": "C03", "speaker": "name",
   "quote": "verbatim words copied exactly from that chunk, max 40 words, keep caption spelling errors",
   "claim": "X means / causes Y because Z (one sentence, your words)",
   "mechanism": "one of: slow_reaction | risk_premium | overshoot | cycle_persistence | liquidity_flows | policy_reaction | crowding_positioning | seasonality | fiscal_debt | structural_shift | risk_management | research_method | behavioral | new: <name>",
   "asset_class": "equities | rates | fx | commodities | credit | multi | other",
   "indicator": "exact series / signal named, or empty",
   "horizon": "days | weeks | months | years | unspecified",
   "direction": "what goes up/down or long/short, or empty",
   "conditions": "when it works / fails, or empty",
   "testable": "yes | partly | no - one short reason",
   "speaker_confidence": "high | medium | low (as the speaker expresses it)",
   "time_bound": "yes | no"}
 ]
}

## Rules
- The quote MUST be copied character-for-character from the chunk named in "chunk" (a script will check it).
- Every chunk appears in "coverage"; claims count per chunk must match the claims list.
- Write the file, then validate it: `python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print(len(d['claims']), len(d['coverage']))" <file>`.
- Do not read any other extraction output or note files. Use only the transcript file you are given.
