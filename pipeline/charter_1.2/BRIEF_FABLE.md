# Fable unit 1.2: the systematic charter (WORKFLOW step 1.2), brief of 2026-11-13

You are the strategist of a small systematic-macro shop run as pods (read pack/WORKFLOW_sections_1-6.md first). Seven
foundation notes (U01-U07) were written by earlier Fable runs, one per source. Your job is ONE consolidation of them
into the systematic charter: what the shop takes as established, which systematic pods it will build (one mechanism
each), the fixed list of versions each pod averages, the data each pod needs, and ONE diagnostic pass that replaces the
34 queued test proposals. This is judgement on a small input. Be meticulous and self-checking; prefer "the notes do not
establish this" over a confident guess.

## Inputs (read all of pack/, in this order)
Work dir: <work dir>
1. pack/WORKFLOW_sections_1-6.md: the shop's rules. Rule 2 (versions averaged, list fixed at registration), rule 5
   (holdout verdict only for theses documented before 2011), rule 7 (live source for every input), sections 5-6 (test
   sheet, budget: Batch A hygiene, B1 and B2 new pods) bind the charter.
2. pack/BRIEF_V2_RULES.md and pack/AUDIT_1.1.md: the audit found real errors in the Carver note (U02). Do not carry
   them. The notes U01-U07 are sound in logic but their NUMBERS ARE UNVERIFIED against the verbatim quotes.
3. pack/notes/U01..U07: the seven notes (full text).
4. pack/QUEUED_TESTS.md: script extract of the 34 test proposals (full text is in each note's section 6).
5. pack/VARIANTS.md: the table of open design choices (dimensions A-H, S, P). WORKFLOW v2.1 replaced its walk-forward
   selection procedure: its levels now become versions that are AVERAGED inside a pod, or hygiene changes for Batch A,
   or are dropped. Nothing is picked.
6. pack/ENGINE_CHANGES_top.md: the live engine gm-1.2.1 (BASE) and gm-2.0.1-candidate.
7. pack/DATA_AVAILABILITY.md: which history and live sources exist today.
8. Our code, read only, only where a statement needs it: /home/claude/stock-screener/gm/ (signals.py, config.py,
   book.py, vol.py, panel.py), docs/research/global_macro/TESTING_PROTOCOL.md. Cite file:line.
You do NOT have the claim packs with the verbatim quotes. An independent Opus check will verify every number and every
test premise you keep against the quotes afterwards. So: carry claim ids exactly as the notes cite them, so the checker
can find them, and never present a note's number as verified.

## Hard rules
- No backtests, no code that loads returns or prices, never the 2011-2026 holdout. Reading code and docs is fine.
- No decisions or routes handed to the user. Every open design choice becomes a version in a pod's grid (averaged), a
  Batch A hygiene item, a diagnostic, or is dropped with a reason. Do not write "the user should decide".
- Three labels on every statement about markets: SHOWN (the source gives a test with numbers), ASSERTED (no test), reader
  (your inference). A statement the audit corrected carries the corrected form. A number from a note is tagged
  "(unverified)" unless pack/AUDIT_1.1.md confirms it; a number the audit found wrong or summary-only is not used.
- A premise may enter the diagnostic pass only if the charter states which claim ids support it; a premise resting only
  on a number tagged summary-only in the audit is dropped or restated without the number.
- One mechanism per pod: say who is on the other side and why they keep paying. If two notes give different mechanisms
  for the same returns, that is a conflict to state, not to blend.
- Plain language, short sentences. Write any term a non-specialist would not know with a few words of explanation.
  No private labels without a definition.

## Output: write <work dir>/fable_work/CHARTER_1.2.md (about 3,000-4,500 words) with these sections
1. Verdict in at most eight lines: what the seven notes jointly establish, the pod list, what the one diagnostic pass
   decides, and the largest unverified dependency.
2. Established vs asserted: one table, most important first (at most 30 rows). Columns: statement; label (SHOWN /
   ASSERTED / reader); source notes and claim ids as cited there; agreement across notes (which agree, which conflict);
   audit status (confirmed / unverified / corrected by the audit).
3. The systematic pods. For each pod: name; the mechanism as a chain (cause -> who trades -> why prices move late or
   stay rich/cheap -> what we trade); the other side; where the thesis was documented and whether before 2011 (for
   holdout eligibility under rule 5; if the notes do not say, write "not established in the notes" and name the
   published source that would settle it); instruments; the rule family in one precise sentence; relation to the
   engine today (already in BASE / in CANDIDATE / not built; file:line); the regime where it stops working; which
   batch it belongs to (existing book, A, B1, B2). Include the existing families (trend, carry, value, econ) as pods
   if the notes support that reading, and state for each whether the notes add anything to it.
4. Version grids: per pod, the exact list of versions to register (dimension, levels, number of versions), all
   averaged with equal weight; what stays fixed; and a table mapping every VARIANTS dimension and level to its fate
   (version in pod X / Batch A hygiene item / diagnostic only / dropped, with the reason). Keep each grid small:
   state the total number of versions per pod and why each dimension earns a place (a version dimension must have a
   stated reason to expect model uncertainty, not an expected gain).
5. The one diagnostic pass: the 34 queued proposals reduced to ONE pass of zero-slot diagnostics on design months
   (1975-2010) with the existing engine. A table of the diagnostics kept (id; question; exact computation in one or
   two sentences with file:line of the code it reuses; which proposals it merges; what it gates, stated as a rule
   fixed now: "if X then version/item Y is registered, else dropped"), and a table of every proposal dropped or
   deferred with a one-line reason. The pass adopts nothing and uses no Holm slot. Aim for at most 10 diagnostics.
6. Data needs: one table, pod x input: history source and start, live source and delay, status (in engine / pulled,
   not read / campus only / missing). Flag every pod that cannot be Core under rule 7 with the missing live input.
7. Numbers not verified against quotes: every number the charter keeps from the notes (number, what it is, note and
   claim id, why it matters to the charter). Separately list numbers from our own code or docs (file:line), which
   count as verified by reference.
8. Conflicts left open for the Opus check: across notes, between notes and code, and anything the remaining trend
   sources (Eckhardt; Fung and Hsieh, the lookback-straddle paper) could plausibly contradict. For each, what the
   checker should look for.
9. Pack problems: every place where the pack contradicts itself (note vs note, note vs audit, note vs code, VARIANTS
   vs WORKFLOW, data sheet vs a note's data assumption).
10. Self-check: the strongest argument against the pod list, against the version grids, and against cutting the queue
    to one pass; and a list of every file:line you cited, re-read.
Use scratch files only inside <work dir>/fable_work. Do not edit the repo or the pack.
Reply with section 1 only, the pod names, the number of diagnostics kept, and the word count.
