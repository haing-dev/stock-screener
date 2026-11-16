# Fable unit 1.3c: thesis note, testing method (WORKFLOW step 1.3), brief of 2026-11-15

You are the strategist of a small systematic-macro shop run as pods (read pack/WORKFLOW_sections_1-6.md first; step 1.3
lists three thesis notes; the first two, rates and value / momentum / carry, are done). This third note is not about a
pod. It is about how the shop judges evidence. One source: QP13, a deck of 45 teaching slides by Bob Stine (Wharton,
Department of Statistics): how to judge an investment record and decide how much to hold, given fat tails, dependence,
hidden volatility and many candidates. Write ONE note that
(a) separates what the slides SHOW from what they ASSERT about judging a record and about how much to hold;
(b) goes through each element of our test sheet and adoption protocol and says whether QP13 supports it, contradicts
    it, is silent on it, or adds a check we lack;
(c) turns every change you propose into exactly one of: a protocol item to be registered at step 3.4 (written as
    precisely as a rule), a zero-slot diagnostic with a gate fixed now, or "dropped" with a reason.
This is judgement on source logic only. Be meticulous and self-checking; "the slides do not establish this" is a valid
finding, and so is "our sheet already covers this".

## Inputs (read all of pack/; work dir: <work dir>)
1. pack/WORKFLOW_sections_1-6.md: the shop's rules, steps, test sheet (section 5), testing budget and holdout
   (section 6). Rule 2 (versions averaged), rule 3 (two questions, two tests), rule 4 (fixed budget), step 3.3 (power
   check), step 3.4 (registration), step 5.1 (book), steps Q and W5 (live record).
2. pack/TESTING_PROTOCOL.md: the registered adoption protocol for changes to the existing book (five tests, Holm,
   batches, the note on the holdout criteria). It cites "Stine 2009" for its tail test and names a "Foster-Stine
   value-add test": check both attributions against the slides.
3. pack/BRIEF_V2_RULES.md: binding, with one extension for this unit (see Hard rules).
4. pack/QP13.json: every claim with its VERBATIM "quote" plus machine summaries (claim, exact_rule, reported_result,
   mechanism: may be wrong) and a machine-written reasoning map. Read all 72 claims.
5. pack/QP13_slides_text.md: the text of the slides themselves. The quotes are short fragments of it, so read the
   slides too: formulas and several numbers are on a slide but not inside any quote.
6. pack/CHARTER_DIGEST.md: verdict, diagnostic pass and check summary of the systematic charter; verdicts and
   diagnostics of thesis notes 1.3a and 1.3b. Its numbers are not ground truth for this note.
7. pack/BOOK_FACTS_design_era.md: results already on record for the existing book, design months 1975-2010 only
   (protocol batches 0 and 1, diagnostics, the statistical audit with the power of the holdout criteria, engine change
   log extracts). Repo results, not ground truth about QP13.
8. Tool: <work dir>/tools/lookup.py (claim id -> quote; --slide Cnn; --grep "words"): use it to check every id,
   slide and quoted phrase you cite before you finish.
No code reading. No new backtests, no data, never 2011-2026 results.

## The elements to judge (each with where the pack defines it)
1. Paired stationary bootstrap of the Sharpe difference (TESTING_PROTOCOL section 2 test 1, section 4).
2. Holm correction inside a batch; the trial log; the selection-inflation figure; deflated Sharpe as a reported
   number (TESTING_PROTOCOL section 3; WORKFLOW rule 4, section 6, steps 4.2 and 7.1; BOOK_FACTS audit section 2).
3. Tail test (TESTING_PROTOCOL test 5; WORKFLOW section 5, decisive test 4).
4. Placebo (WORKFLOW section 5, decisive test 3).
5. Double costs (TESTING_PROTOCOL test 4; WORKFLOW section 5, decisive test 2).
6. Power check (WORKFLOW step 3.3).
7. Holdout criteria and their power (WORKFLOW section 6; TESTING_PROTOCOL section 6; BOOK_FACTS audit section 4).
8. Book sizing: Core pods at equal risk, a 10% volatility target, caps (WORKFLOW step 5.1; TESTING_PROTOCOL
   section 1; BOOK_FACTS header).
Also consider, and add a row only where the slides bear on it: "adds to the book" alpha against the Core book
(WORKFLOW section 5, decisive test 1) and the Newey-West alpha t-statistic reported in TESTING_PROTOCOL; the economic
size and per-era tests (TESTING_PROTOCOL tests 2 and 3); version averaging inside a pod (WORKFLOW rule 2); promotion
on the live record at registered checkpoints (WORKFLOW rule 6, steps W5 and Q).

## Hard rules
- Ground truth is the slide text and the claim quotes. Verify every statement and number you rely on against them and
  cite the claim id or the slide ([Cnn]). Label each statement SHOWN (the slides give a derivation, a constructed
  example or a result with numbers), SHOWN (words) (a result is reported, its numbers are not in the slide text),
  ASSERTED (no derivation, example or test), or reader (your inference). Give each number a status: "in quote",
  "on slide Cnn" (in the slide text but not inside a quote), or "summary only" (only in a machine field). Extension
  of v2 rule 2 for this unit: "on slide" counts as in the source; "summary only" still cannot support a SHOWN label,
  a grade above weak, or the premise of a proposal. Where the text layer makes a table ambiguous (cells as loose
  lines), say so and do not guess which number belongs to which row.
- Judge the source as a risk officer would: these are teaching slides with four hand-picked assets and constructed
  examples. Say what each kind of support can carry: a mathematical inequality holds under its stated assumptions; a
  constructed example shows that something can happen; four assets show nothing about frequency. State the
  assumptions each result needs and whether our book meets them.
- For any test or rule you take from the slides, state exactly what is assumed, what it controls and what it does not
  (false alarms against missed real effects), and every choice it leaves open when applied here: what plays the role
  of the market and of beta for a multi-asset long/short book or for a challenger-minus-incumbent return; the scale
  (leverage) at which returns are compounded; the data frequency; how any estimated quantity avoids look-ahead; the
  count used for multiplicity. Each open choice is closed by the slides (cite), closed by a rule you write with its
  reason, or reported as unanswered by the source. A proposal with an unclosed choice cannot be a protocol item.
- Arithmetic is allowed and welcome where it settles a question (for example what size of effect a test could detect
  over the design window). Use only formulas on the slides and numbers in the pack; show formula, inputs with their
  source, and result; label the result "(computed)". Do not import results from memory; anything from your own
  knowledge of the literature is marked "(author's knowledge)" and nothing is built on it.
- A new decisive test changes the pass chance of the whole sheet. For each protocol item say whether it is decisive
  or reported-only, why an existing test does not already cover it, and what step 3.3 (power check) must simulate
  for it. Prefer reported-only unless the slides give a reason the existing decisive tests cannot meet.
- No decisions or routes for the user. An open design choice becomes a registered rule with its reason, a zero-slot
  diagnostic with a gate fixed now (design months to 2010-12 only), or is dropped with a reason.
- Do not restate our protocol loosely: quote the pack's own words for the element you judge, and flag any place where
  WORKFLOW and TESTING_PROTOCOL disagree with each other.
- Dating: state what the pack shows about when the slides and the test they cite were written.
- Plain language, short sentences; explain any term a non-specialist would not know in a few words. Do not use
  backticks in the note.

## Output: write <work dir>/fable_work/THESIS_1.3_method.md (about 3,000-4,000 words)
1. Verdict in at most eight lines: what QP13 establishes about judging a record; which elements of our sheet it
   supports, which it contradicts, what it adds; the number of protocol items and diagnostics; the single weakest
   link in the source and the single weakest link in our sheet as the slides see it.
2. What the slides establish: one table, most important first (at most 18 rows): statement; label; claim ids or
   slide; the quoted words or numbers that carry it; limits (assumptions, constructed or real data, how many cases).
3. Element by element: one table. Element and its pack location with the pack's own words; what QP13 says about it
   (supports / contradicts / silent / adds a check) with the claim id or slide and the words that carry it;
   consequence (none / protocol item Pn / diagnostic Mn / dropped Dn).
4. The martingale test as a candidate check for this shop: assumptions; what it controls; what it leaves open and
   how each open choice is closed or cannot be; what size of effect it could detect on the design window, by
   arithmetic from the slides' own formulas and the pack's numbers; how it relates to the bootstrap test, the tail
   test and the placebo; the resulting status (decisive / reported-only / diagnostic / dropped).
5. How much to hold: what the slides show about long-run growth and the sizing rule and their own cautions; what
   that implies for the 10% volatility target, equal risk shares and caps, and for the registered holdout criteria
   (supports / contradicts / adds).
6. Protocol items for step 3.4: at most five, numbered P1.., none if none is justified. For each: the exact text as
   it would be written into TESTING_PROTOCOL.md and the section it goes to; decisive or reported-only; the reason
   with claim ids; the effect on the pass chance; what the power check must simulate.
7. Diagnostics: at most three zero-slot diagnostics on design months, numbered M1.. (question; computation in two
   sentences; data; the gate as a rule fixed now, free of hidden choices; what follows from pass and from fail).
   None if none is justified.
8. Dropped: every idea you considered and rejected, one line each with the reason.
9. Numbers used, each with claim id or slide and status (in quote / on slide / summary only / repo result /
   computed).
10. What the Opus check should look at first; what the slides leave unanswered.
11. Pack problems: contradictions inside the pack (summary against quote or slide, slide against slide, WORKFLOW
    against TESTING_PROTOCOL, a citation in our protocol that the slides do not support).
12. Self-check: the strongest argument against each proposal and against each rejection.
Write scratch files only inside <work dir>/fable_work. Do not spawn agents.
Reply with section 1, one line per protocol item and diagnostic, and the word count.
