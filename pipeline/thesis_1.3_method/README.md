# Thesis note 1.3c testing method (QP13, Stine): exact inputs and outputs, 2026-11-15
- BRIEF_FABLE.md + pack/ + tools/lookup.py = everything the Fable run (claude-fable-5-2, effort max, one run, ~0.46M tokens) was given.
  Pack: QP13.json (72 claims, verbatim quotes), QP13_slides_text.md (the slide text itself: the quotes of a slide deck are short
  fragments, so the slides are ground truth next to the quotes), TESTING_PROTOCOL.md, WORKFLOW_sections_1-6.md, CHARTER_DIGEST.md
  (charter sections 1, 5, 11; verdicts and diagnostics of notes 1.3a and 1.3b), BOOK_FACTS_design_era.md (repo result files,
  design months 1975-2010 only), BRIEF_V2_RULES.md.
- THESIS_1.3_method_fable_original.md = its output, untouched.
- BRIEF_OPUS.md = brief of the independent check (Opus 5.5, effort high, ~0.24M tokens), same pack and tools.
- check/CHECK_1.3_method.md = the check; check/apply_check.py applied its 22 corrections; check/recompute.py = the checker's arithmetic.
- Final text: repo docs/research/fable/THESIS_1.3_method.md (+ _check.md), vault Fable/.
