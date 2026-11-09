---
tags: [method, spec]
file: TRANSCRIPT_MAP_SPEC.md
---
# Transcript argument map spec v1 (2026-11-05)

Goal: the speakers' REASONING, not isolated facts: what each main speaker believes about how markets work, how one
step leads to the next, how they turn beliefs into decisions, what evidence they offer, when they say it fails, and
where speakers disagree. Fable will later reason over these maps, so every element must point to verified claims.

Inputs for source MTnnn: docs/MTnnn.txt (the transcript, chunks [C01]..) and ledger/MTnnn.json (all verified claims of
this transcript: first read + cross-check additions; a claim may carry "correction" = a fix you must apply, e.g. the
right speaker). Read the WHOLE transcript and the WHOLE ledger. Do not read any other source's files.

Rules
- Cite claim_ids from ledger/MTnnn.json. If a reasoning step has no claim yet, add one in "added_claims" (same fields
  as ledger claims; id MTnnn-Cxx-Rk; quote copied character-for-character from that chunk, max 40 words).
- Host questions are context, not views, unless the host states a view. Map the main speakers (guests; the host too if
  he argues a position). Speaker attribution in captions is uncertain: if unsure, say so in "speaker_note".
- Anything the speakers did not say is your inference: only in fields marked (reader) or with "stated": "implicit".
- Market calls tied to the recording date go to current_views with as_of (recording date from the header if given).

Output maps/MTnnn.json:
{
 "source_id": "MTnnn",
 "episode_thesis": "2-3 sentences: the main argument(s) of the conversation",
 "speakers": [{
   "name": "", "role": "e.g. CTA founder, host, macro PM", "speaker_note": "",
   "fingerprint": ["3-8 tags from the list below"],
   "worldview_premises": [{"premise": "belief about how markets/economies behave", "type": "empirical | theoretical | behavioural | institutional | experience",
       "stated": "stated | implicit", "support": "how they justify it (data, track record, history, anecdote, none)", "claim_ids": []}],
   "mechanism_chains": [{"topic": "", "steps": [{"from": "", "to": "", "why": "", "claim_ids": []}],
       "evidence": "", "fails_when": "", "claim_ids": []}],
   "decision_process": [{"element": "signal | universe | sizing | risk | execution | research | portfolio | other",
       "practice": "the rule or habit as precisely as stated", "why": "", "claim_ids": []}],
   "evidence_style": "how this speaker establishes truth (backtests, track record, history, first principles, anecdote)",
   "current_views": [{"view": "", "as_of": "", "reasoning": "", "claim_ids": []}]
 }],
 "disagreements": [{"topic": "", "positions": [{"speaker": "", "position": "", "claim_ids": []}]}],
 "gaps_and_conflicts": [{"issue": "unsupported claim, internal contradiction, missing detail", "claim_ids": []}],
 "forward_looking_inputs": "(reader) observable inputs these speakers say lead future prices, horizon, and why",
 "reader_inferences": ["(reader) ..."],
 "added_claims": []
}

Fingerprint tags (use only these): trend_following, carry, value_mean_reversion, macro_fundamental_topdown,
bottom_up_fundamental, liquidity_flows, positioning_crowding, volatility_options, dealer_hedging_flows,
crisis_alpha_convexity, diversification_risk_parity, position_sizing_vol_target, kelly_or_conviction_sizing,
debt_cycle_long_term, policy_reaction_central_banks, fiscal_dominance, valuation_contrarian, behavioral_sentiment,
market_internals_leading, regime_detection, nowcasting_data, research_robustness_overfitting, costs_execution,
replication_indexing, portfolio_construction_stacking, short_term_systematic, relative_value_arbitrage,
commodity_fundamentals, geopolitics, structural_themes, manager_selection_allocation.

Validate before finishing: JSON loads; every cited claim_id exists in ledger/MTnnn.json or added_claims; every added
quote is found in its chunk (lowercase, whitespace-collapsed substring); fingerprint tags are from the list.
