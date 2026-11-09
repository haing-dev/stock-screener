---
tags: [method, spec]
file: INVESTOR_SYNTH_SPEC.md
---
# Investor synthesis spec v1 (2026-11-06)

Input: investors/packs/<slug>.json = every mapped appearance of ONE person (argument-map speaker block per transcript,
episode thesis, disagreements involving them; for David Harding also paper reasoning maps QPnn). Claim ids inside
(MTnnn-Cxx-n, QPnn-Cxx-n) point to verified, quote-checked claims. Read the WHOLE pack.

Goal: one coherent picture of how this person thinks about markets, built only from what they said, so a later
judgement model can compare investors and turn recurring ideas into testable strategies. Do not add outside knowledge
about the person; anything beyond the pack is your inference and goes only in fields marked (reader).

Output investors/<slug>.json:
{
 "name": "", "sources": ["MTnnn", ...], "period": "first as_of/date - last",
 "one_paragraph": "how this person sees markets and makes money, in plain words",
 "fingerprint": [{"tag": "from TRANSCRIPT_MAP_SPEC list", "count": n}],
 "core_beliefs": [{"belief": "", "times_stated": n, "sources": [], "claim_ids": [], "stable": "stable | evolved | contradicted - explain"}],
 "mechanisms": [{"name": "", "chain": ["step -> step -> step"], "fails_when": "", "sources": [], "claim_ids": []}],
 "playbook": [{"element": "signal | universe | sizing | risk | execution | research | portfolio | other", "rule": "as precise as stated", "why": "", "sources": [], "claim_ids": []}],
 "evidence_style": "",
 "views_timeline": [{"as_of": "", "view": "", "reasoning": "", "source": "", "claim_ids": []}],
 "how_views_changed": "what changed over time and the reason they gave (or 'not explained')",
 "disagreements": [{"with": "", "topic": "", "their_position": "", "other_position": "", "sources": []}],
 "internal_tensions": [{"issue": "where their own statements conflict", "claim_ids": []}],
 "testable_hypotheses": [{"hypothesis": "precise rule or prediction that data could test", "data_needed": "", "claim_ids": []}],
 "blind_spots": ["(reader) what they never address or assert without support"],
 "reader_inferences": ["(reader) ..."]
}
Rules: merge repeated ideas (count them) instead of listing each appearance; every belief, mechanism, playbook rule,
view and hypothesis cites claim_ids that appear in the pack; keep dates; keep their exact numbers; be complete but
compress (the output should be roughly 10-20% of the pack). Validate: JSON loads; every cited claim_id occurs in the
pack text; every source in "sources" is a source_id in the pack.
