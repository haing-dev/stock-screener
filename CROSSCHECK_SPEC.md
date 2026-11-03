# Completeness cross-check spec v1 (Opus)

You check a first reader's extraction for COMPLETENESS and ACCURACY. Read EXTRACT_SPEC.md first (same claim schema).
For each assigned document:
1. Read the whole transcript file docs/MTnnn.txt (every chunk) AND the first reader's sonnet/MTnnn.json.
2. Go chunk by chunk. For every idea in the chunk that qualifies as a claim under EXTRACT_SPEC.md and is NOT already
   captured by a first-reader claim (same idea, any wording), add it. Pay special attention to: causal mechanisms and
   their reasoning steps, conditions/regimes, numbers and data series mentioned, methods (sizing, testing, costs),
   disagreements between speakers, and caveats.
3. Flag first-reader claims that misstate what was said (wrong meaning, wrong speaker, wrong direction, wrong number).
4. Write cross/MTnnn.json (UTF-8), exactly:
{
 "source_id": "MTnnn",
 "added_claims": [ same fields as EXTRACT_SPEC claims, claim_id "MTnnn-Cxx-Xk" ],
 "corrections": [ {"claim_id": "...", "issue": "what is wrong", "fix": "corrected claim text"} ],
 "chunks_checked": ["C01", ...],                       // every chunk
 "completeness_estimate": "share of the document's claim-worthy ideas the first reader caught, e.g. 0.85, with one line why"
}
Rules: quotes verbatim from the named chunk (a script checks them); do not duplicate first-reader claims; validate the
JSON with python before finishing. Process documents one at a time and write each file before starting the next.
