# Independent check of the step 3.4 registration draft, brief of 2026-11-23

You are an independent checker (quant and risk officer). Another agent drafted the registration that will become
section 7 of TESTING_PROTOCOL.md: reg_3.4/REGISTRATION_3.4.md (plus reg_3.4/SUMMARY_FOR_USER.md). It binds every
later run, so check it hard. You did not write it; do not defend it. "Cannot verify" is valid; a guess is not.

Work dir: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/reg_3.4. Write ONLY inside check/. Repo /home/claude/stock-screener
read-only. No backtests, no market data, never any 2011-2026 result, no web, do not spawn agents.

## Inputs
The draft and its brief (BRIEF_OPUS.md). Sources it must follow: docs/research/WORKFLOW.md,
docs/research/global_macro/TESTING_PROTOCOL.md, docs/research/THESIS_REGISTER_1.5.md, docs/research/specs/ (specs,
NOTES_3.1_agent_*, checks/CHECK_3.2_*), docs/research/power/POWER_3.3.md (+ csv/), docs/research/fable/
THESIS_1.3_method.md and the notes the specs cite, gm/CHANGES.md, gm/trials.csv, gm/config.py, gm/*.py.

## Check first: the three readings that drive the result
1. Rule 5: "documented before 2011 = a confirmed pre-2011 source states the RULE (what, which way, on what), even
   without a mechanism"; dating per pod/leg/version; which legs this makes Core-eligible (Trend, ranked currency carry,
   energy carry, equity value). Is this reading consistent with WORKFLOW rule 5 and section 6, with the register's
   dating classes and sources (column 8, section G), and with the notes' grades? Is it applied consistently to every
   leg (e.g. is equity value's source really pre-2011 for this rule form; is energy carry's)? What would the stricter
   reading (mechanism AND rule) change? Is the choice argued, not merely asserted?
2. "No new pod can be Core with today's data" and the Holm count over Core-eligible pods only (none today): does this
   follow from WORKFLOW s5-6 and the power check; does it change the batch error promise; is anything gamed?
3. Existing pods reach Core by placebo, double costs, tail and rebuild, with alpha only reported: is this consistent
   with WORKFLOW s5 ("decisive, all four") and with the fact that the design data were seen? Is the reason sound, and
   is the consequence (no decisive "adds to the book" test for the existing book) stated plainly?

## Then check everything else
- Every number against its source (specs, register, power csv). Every "settled" item: is the settlement inside what
  the sources allow, and argued? Every "blocked" item: is the unblock condition concrete?
- Precision: can a builder run each step without a choice? Look-ahead: any window, holding, diagnostic or test that
  reads past 2010-12 or uses data before release?
- The engine-change list (c): complete against specs/checks/NOTES; each a separate registered entry before code.
- Shop rules: no decision handed to the user; versions averaged, not picked; nothing claimed as run; no 2011+ number;
  the holdout consequences match WORKFLOW s6 exactly.
- The summary for the user: accurate, plain, no claim the draft does not make.

## Output: check/CHECK_3.4.md
1. Verdict: APPROVED / APPROVED WITH CORRECTIONS / REJECTED, with counts per check area, in five lines.
2. Findings: the three readings first (each: sound / sound with corrections / unsound, with reasons), then the rest.
3. Required corrections (heading exactly "## 3. Required corrections"). Sub-headings exactly "### REGISTRATION_3.4.md"
   and, if needed, "### SUMMARY_FOR_USER.md"; under each, numbered items: one line of description, then exactly:
   - Find: `<verbatim text from that file, one line, occurring exactly once, no backticks>`
   - Replace: `<replacement, one line, no backticks>`
   then a line "Reason:" with the source (file, section) and words. Run:
   python3 tools/apply_check.py check/CHECK_3.4.md . check/corrected   until ALL PAIRS APPLIED; read the changes once.
4. Open points that are not corrections (one line each).
5. What you could not verify.
Reply with section 1, the verdict on each of the three readings, and the number of corrections.
