---
tags: [method, spec]
file: X_EXTRACT_BRIEF.md
---
# Extraction brief for MT228 (X posts of John Galt, @AtlasShrug1)

Work dir: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/L0
Read EXTRACT_SPEC.md there first: same goal, same claim schema, same quote rule. This brief only adds what is different
for a feed of short dated posts.

Source: docs/MT228.txt. 167 chunks [C001]..[C167], oldest first. Each post starts with its date, e.g. "(2026-10-15) ...".
Images and charts were not captured, so some posts refer to things you cannot see; do not guess their content.
You extract ONLY the chunk range given in your task, but you may read earlier chunks for context.

## What to extract
The reader is a systematic macro researcher. This author trades mostly small AI / semiconductor / critical-mineral
stocks, but also reads the macro cycle from market tickers. Priorities, in order:
1. RULES and TELLS: any statement that some ticker, ratio, sector, data series or event leads or signals something
   broader (e.g. "home builders roll over first", "the dollar breaking out means a liquidity squeeze").
2. FORECASTS: any dated call on an index, sector, country ETF, rate, currency, commodity, the economy or policy
   (direction, level, by when if stated), with the reasoning he gives.
3. FRAMEWORK: how he thinks the cycle works (capex cycle, liquidity, positioning, valuation, politics), how he sizes,
   hedges, takes profits, when he says he is wrong.
4. TRACK RECORD statements: where he says a past call of his worked or failed (kind = "self_reported").
5. SINGLE STOCKS: record a claim only when the post gives (a) an explicit position or price / valuation call WITH a
   reason that reflects a sector, cycle or macro view, or (b) uses the stock as a tell for something broader. At most
   one claim per stock per chunk. Pure company chatter, replies, jokes and retweeted headlines without a view are not
   claims: mention them in the coverage note (e.g. "NBIS valuation chatter; jokes").
One claim per distinct idea per chunk. If he repeats an idea in a later chunk, record it again there (the date
matters), but keep it short.

## Output
Write /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/xgalt/sonnet/part_<first>_<last>.json:
{"source_id": "MT228", "part": "C0xx-C0yy",
 "summary": "3 lines: what he argued in this stretch of time",
 "coverage": [{"chunk": "C001", "claims": 2, "note": "..."}, ...],      // EVERY chunk of your range
 "claims": [{
   "claim_id": "MT228-C012-1", "chunk": "C012", "speaker": "John Galt",
   "as_of": "2026-10-15",                      // the date printed at the start of the post the quote comes from
   "kind": "rule | forecast | framework | position | self_reported | observation",
   "tickers": ["SMH", "EWY"],                  // every $ticker or index the claim is about, may be empty
   "quote": "verbatim, copied character-for-character from that post, max 40 words (keep his spelling, $ signs, emojis)",
   "claim": "X means / causes Y because Z (one sentence, your words)",
   "mechanism": "<as in EXTRACT_SPEC>", "asset_class": "<as in EXTRACT_SPEC>",
   "indicator": "exact ticker / ratio / series he watches, or empty",
   "horizon": "days | weeks | months | years | unspecified",
   "direction": "what goes up/down or long/short, or empty",
   "forecast": {"variable": "", "call": "up | down | level ... ", "by_when": "date or empty"},   // only for kind = forecast, else omit
   "conditions": "", "testable": "yes | partly | no - reason", "speaker_confidence": "high | medium | low",
   "time_bound": "yes | no"}]}

## Rules
- The quote must be an exact substring of the chunk named in "chunk" (a script checks it after lower-casing and
  collapsing whitespace). Do not include the leading "(date)" in the quote. Never stitch two posts together.
- claim_id = MT228-<chunk>-<n>, n counting from 1 inside each chunk; coverage counts must match.
- After writing, validate: JSON loads; every chunk of your range is in coverage; counts match; every quote is found in
  its chunk; every as_of is a date that appears in that chunk. Fix what fails, then stop.
- Use only docs/MT228.txt and the two spec files. Scratch files only in xgalt/tmp_<first>/.
Reply with: claims by kind (counts), the five most important rules or tells you found (one line each with claim id),
and any problem.
