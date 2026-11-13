# Charter 1.2 (WORKFLOW step 1.2): exact inputs and outputs, 2026-11-13
- BRIEF_FABLE.md + pack/ = everything the Fable run (claude-fable-5-2, effort max, one run, ~0.67M tokens) was given.
- CHARTER_1.2_fable_original.md = its output, untouched.
- BRIEF_OPUS.md = brief of the independent check (Opus 5.5, effort high, ~0.36M tokens). Its quote sources were the
  existing foundation packs U02-U08 (pipeline/foundation packs, vault _data/foundation_packs) and papers/merged QP01, QP09.
- check/CHECK_1.2.md = the check; check/lookup.py = claim id -> quote lookup; check/apply_corrections.py = the script
  that applied the 24 required corrections to the original (whitespace-insensitive exact replacements).
- Final text: repo docs/research/fable/CHARTER_1.2.md (+ CHARTER_1.2_check.md), vault Fable/.
