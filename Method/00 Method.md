---
tags: [method, index]
---
# Method: how every note was made (traceability)

**From 2026-11-11 all new work follows [[WORKFLOW]] (pod shop workflow v2.1: steps, agent per step, tests, budget).**
Data: [[Bloomberg job runner]] (files stay on the PC, reports only), [[Bloomberg inventory 2026-11-10]], [[Bloomberg data lock v1]] (block 2; hashes in `_data/bbg_LOCK_v1.json`). [[Block 3 engine on the PC]] (reproduction pass, truncation causes C1-C4). Engine gm-1.2.1 / gm-2.0.1 (look-ahead fixed): [[Engine change log]].
Fable audit (step 1.1, gate passed; brief v2 rules): [[Fable audit 1.1]]. Systematic charter (step 1.2: pods, version grids, one diagnostic pass; checked by Opus): [[Charter 1.2 - Systematic charter]], [[Charter 1.2 - Independent check]]. Forecast ledger (steps 2.1-2.3): [[Forecast ledger spec]], [[Forecast coding agreement]], [[Forecast scoring rules]], [[Forecast scorecard 2026-11-12]].
The steps below describe how the existing notes were made.

1. **Transcripts** (originals in the Macro Transcripts folder) are split into ~700-word chunks [Cnn].
2. **Layer 0 extraction** (Sonnet, [[EXTRACT_SPEC]]) -> claims with verbatim quotes; **cross-check** by a second blind
   reader ([[CROSSCHECK_SPEC]]; routing in [[Cross-check routing]]); a script checks every quote against the chunk text
   (exact / other_chunk / near / not_found). Result: notes in `Sources/`, one block id per claim (^MTnnn-Cxx-n).
3. **Papers** (Quant folder, [[PAPER_SPEC]]): Sonnet extraction + Opus blind second read with reasoning map -> `Papers/`.
4. **Argument maps** per transcript (Sonnet, [[TRANSCRIPT_MAP_SPEC]], order in [[Transcript priority]]), rendered
   inside each Sources note under "Argument map"; every element cites claim ids.
5. **Investor syntheses** across appearances (Sonnet, [[INVESTOR_SYNTH_SPEC]]) -> `Investors/`; name variants in [[Speaker aliases]].
6. **Fable judgement** ([[F1_SPEC]], [[FOUNDATION_SPEC]]; units in [[Foundation units]]) -> `Fable/Foundation/`.
   Each note's exact input is saved in `_data/foundation_packs/<unit>.json`.

**Trace any statement:** Fable note -> claim id link -> claim block (quote + chunk) in the Sources/Papers note ->
chunk in the original transcript or PDF page. Code refs link to GitHub at a fixed commit.
**Raw data:** `_data/` (see its README). Same files are on the macro-vault branch of haing-dev/stock-screener.
