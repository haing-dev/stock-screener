# Brief: held-out test (gate G5)

CARD.md is an investor card for Stanley Druckenmiller (Duquesne Family Office). heldout_claims.json holds the claims from
one more document (DRU2, 2022-06-10) that the card writer never saw: `rules` (verified rules) and
`other_claims` (principles, examples, views).

For EACH item in `rules`: does a rule on the card match it? Match = same part (buy, price, avoid, sell, size, process)
and same measure or idea; where both give a number, within 20%; where only one or neither does, the same direction.
Answer {id, match: yes/no, card_rule: R.. or "", why <= 20 words}.
Then check ALL items (rules and other_claims) for a contradiction with a card rule in the buy, price or sell part:
a claim that says the opposite of a card rule. For each, say whether the card already records it as a dated change of
view or a different scope (closed) or not (open). Answer {id, card_rule, status: open/closed, why}.

Write heldout_result.json in this folder: {"matches": [...], "contradictions": [...]}. Read and write only in this
folder. Reply with the match count (yes of total) and the open contradictions.
