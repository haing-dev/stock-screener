# Brief: blind tagging of investor claims (gate G3)

You are the second reader. Another reader picked these passages from five interviews with Dev Kantesaria (Valley
Forge Capital) and tagged them; you do NOT see those tags. Tag each item yourself from the quote and its context.

Input: verify_items.json in this folder (292 items: vid, doc, line, quote, context = the lines around the quote).
Tag definitions: CLAIM_SPEC_v1.1.md in this folder (fields kind, part, scope, computable, measure, value, direction,
strength). Use exactly those values. Rules 2-5 of the spec apply (tag what the quote says; example vs anecdote; a
number is a threshold as defined in "Definitions that decide tags"; when unsure choose the weaker value).
For `value`: every number in the quote that describes his own practice, copied exactly as stated; empty if none (see the spec).
Also give `speaker_ok`: yes if the quote is Kantesaria's own words, no if it is the host's or someone else's, unsure.

Output: tags.json in this folder, a list of {vid, kind, part, scope, computable, measure, value, direction, strength,
speaker_ok, note} for ALL items (note: at most 15 words, only when a tag is hard). Work only in this folder; do not
open any other file or folder. Reply with the counts by kind and the number of items with speaker_ok not yes.
