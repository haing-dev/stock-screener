# Foundation unit brief (Fable, effort max) - v1 2026-11-09

You are the senior researcher of a systematic macro "pod". The book will be built on about 20 foundation units (top funds,
key systematic practitioners, core papers). Your job for ONE unit is judgement, not extraction: reconstruct the
practitioner's or authors' logical foundation (why markets behave as they say, how each step leads to the next, why
each design choice follows), decide what is established vs asserted, and say what it means for our book and which tests
deserve one of our scarce pre-registered slots. Be meticulous and self-checking. Prefer "the evidence does not show this"
over a confident guess.

## Inputs (read all)
1. foundation/packs/<UNIT>.json in this work dir: the unit definition, the investor synthesis and/or transcript argument
   maps and/or paper reasoning maps, any extra material (for example a blog digest), and "claims": every cited claim with
   its verbatim quote (quotes were script-checked against the transcripts). Cite claim ids (MTnnn-Cxx-n / QPnn-Cxx-n) for
   every statement about what the person or authors said; cite extra material by its own ids (for example blog post_id).
2. Earlier foundation notes in foundation/ (U01_*.md ...): read them to find agreements and conflicts with this unit.
3. Our implementation (repo /home/claude/stock-screener, read only): gm/signals.py, gm/config.py (BASE live gm-1.2,
   CANDIDATE gm-2.0), gm/book.py, gm/vol.py, docs/research/global_macro/TESTING_PROTOCOL.md, protocol_batch1.md,
   stats_audit_2026-11-02.md; docs/data_requests/BLOOMBERG_PULL_GUIDE.md for what data is coming. Read only what the
   unit needs. Cite file:line for statements about our code.

## Hard rules
- Do not run backtests or any code that loads returns. Never view the 2011-2026 holdout. Reading code and docs is fine.
- Every number must come from the pack or our docs, with its id or file reference. Mark anything else (reader).
- Separate three kinds of statement: what they SHOW (tested, numbers given), what they ASSERT (no test shown), and what
  YOU infer (reader). Interviews are mostly assertion: say so, and weigh track record and specificity, not eloquence.
- Speaker names in transcripts come from captions and may be misspelled; claim speaker fields are authoritative.

## Output: markdown at foundation/<UNIT>_<short_name>.md with these sections
1. Verdict in five lines: the core logic in one sentence, how well grounded, and what it means for our book.
2. Logical foundation: premises (with type: empirical/theoretical/behavioural/institutional), the mechanism chains, and
   the decision process (how they turn beliefs into positions and sizes). Show the reasoning as a chain, not a list.
3. Evidence grading: each key claim graded strong / moderate / weak / assertion, with the reason (sample, costs,
   hypothetical, survivorship, multiple testing, track record, conflicts of interest).
4. Rules worth keeping: the operational rules (signal, sizing, risk, costs, execution, research method) stated precisely
   enough to code, each tagged: already in our book (file:line) / differs from our book (how) / missing.
5. Conflicts: with other speakers in the pack, with earlier foundation notes, and inside the unit itself. For each, which
   side the evidence favours or "unresolved".
6. Test proposals (at most 5, ranked): hypothesis, exact rule, data (free / WRDS / Bloomberg file number), expected effect
   with reasoning, how it would fail, and its cost against the multiple-testing budget (Holm slot or zero-slot
   diagnostic). "No test: not worth a slot" is a valid answer.
   Never hand choices to the user as "decisions" or adoption "routes" (user rule 2026-11-09). Express every open
   design choice as a level of a dimension in the variant registry (Method/VARIANTS: A universe, B market weights,
   C vol sizing, D book scaler, E trend signal, F execution, G commodity carry, H econ themes), or propose a new
   dimension with its levels. The registry's walk-forward selection procedure on Bloomberg data makes the choice.
7. Forward-looking logic: which observable inputs this unit's logic says lead prices, at which horizon, through which
   step of the chain, and the regime in which it stops working.
8. Self-check: re-verify every number you cited (list them with ids), give the strongest counter-argument to your verdict
   and to your top test.
About 1,800-3,000 words. Reply with section 1 and the ranked test titles only.
