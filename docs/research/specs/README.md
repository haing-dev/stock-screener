# Pod specs (WORKFLOW steps 3.1-3.2), 2026-11-23

APPROVED WITH CORRECTIONS at step 3.2 (all 11; none rejected). Step 3.1: three Opus 5.5 agents (effort high) wrote the
specs in parallel from docs/research/THESIS_REGISTER_1.5.md, the notes in docs/research/fable/ and the gm/ code (read
only), in the fixed 17-section form (macro-vault pipeline/spec_3.1/BRIEF_OPUS.md). Step 3.2: three fresh Opus agents
checked them (faithful? can it fail? hindsight right? fully specified and point in time? code, data, costs right?) and
listed Find/Replace corrections, applied by script (tools in pipeline/spec_3.1/tools) and re-verified. Ids and quotes
script-checked on every final spec. Nothing registered or run: registration is step 3.4 (after the 3.3 power check).

| Spec | Pod type | Written by (tokens) | Checked by (tokens) | Corrections |
|---|---|---|---|---|
| SPEC_Trend, SPEC_Economic_trend, SPEC_Carry, SPEC_Value | existing pods | agent A (~0.48M) | checker A (~0.39M) | 8, 8, 12, 3 |
| SPEC_Curve_carry, SPEC_Strip_reversion | new systematic pods | agent B (~0.42M) | checker B (~0.34M) | 14, 11 |
| SPEC_Card1..5 | discretionary pods (rule layer + shadow analyst) | agent C (~0.49M) | checker C (~0.40M) | 16, 5, 7, 4, 6 |

NOTES_3.1_agent_A/B/C.md = the writers' notes (items for 3.4; checker C corrects agent C's items 6 and 10).
checks/CHECK_3.2_A/B/C.md = the checks (section 4 = items for step 3.4; section 5 = not verifiable).
