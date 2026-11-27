# Brief: investor card (gate G4)

Investor: Dev Kantesaria (Valley Forge Capital). Input: verified claims of four documents (K065 2021-10-22, K105
2022-10-27, K189 2024-11-20, K290 2024-12-05), file `claims_for_card.json` in your folder (fields of CLAIM_SPEC_v1 +
`rule_status`: both = both readers call it a rule; third = they split and a third reader said rule; no = not a verified rule; `computable_final` = the weaker of the two readers' tags; `date_said`). One document is held out and is NOT
in your input; do not look for it.

Write `CARD.md` in your folder:
1. **One paragraph**: what he buys and why, in his terms, citing claim ids.
2. **Rules by part** (buy, price, avoid, sell, size, process). Each rule one line: `R<part><n>` | statement in plain
   words | measure (if computable) | number and direction as he states it, else "none stated" | strength | claim ids
   (at least one, verified both if possible) | dates said. Merge claims that say the same thing; keep the strongest
   quote's wording. A rule on the card needs at least one claim with rule_status both or third; principles, examples and
   views only support it.
3. **None stated**: for each part with no verified rule, write "none stated" (the recipe then uses the 13F or a
   convention, tagged).
4. **Changes of view and scope**: any two claims that disagree; say whether it is a dated change of view (later
   wins), a different scope (both stand), or open.
5. **Examples**: companies he names as fitting or failing the rules (id, company, which rule).
6. **Gaps**: what a screen would need that he does not state (e.g. a number he never gives).
Do not add anything from outside the claims (no general knowledge about him or Valley Forge). Every statement cites
claim ids. Reply with the number of rules per part and the open contradictions.
Work only in /tmp/claude-0/-home-claude/c6d39485-a0af-5a90-b220-a415744a715e/scratchpad/card1; read only claims_for_card.json and this brief.
