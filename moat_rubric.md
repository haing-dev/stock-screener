# Moat review rubric (stage 2 of the screen)

Use this to score each `Cxx_evidence.txt` file in the AI review pack. Whoever scores (Claude, another LLM, or you) must follow these rules. Every score has to be checkable.

## Rules

1. **Evidence or nothing.** Every score must cite 1–3 verbatim quotes, each 15–60 words, copied exactly from the evidence file. If the text gives no evidence for a trait, set `score` to `null` and explain why in `note`. Never fill gaps from memory of the company.
2. **Blind.** Files are coded (C01, C02…). The company name is replaced with `[COMPANY]`. Don't try to identify the company, and don't use outside knowledge, prices or news. Score what the filing says.
3. **Bear case is mandatory.** Write the strongest argument *against* the moat, also with quotes. This follows Hohn's inherently bearish team members and the warnings about AI echo chambers.
4. **Discount promotional language.** "Leading", "best-in-class" and "unique" are claims, not evidence. A CEO praising their own company is not positive evidence (Kantos). Prefer facts: contract lengths, retention rates, share figures, price increases, number of competitors, regulation.
5. **Quotes get machine-checked.** `verify-quotes` checks every quote word-for-word against the full filing text. If none of a trait's quotes can be found, that trait's score is withdrawn.

## Traits (score 1–5; 5 = strongest moat, or LOWEST risk for the two risk traits)

| Trait | What a 5 looks like | What a 1 looks like | Source |
|---|---|---|---|
| `barriers_to_entry` | Several barriers stack up: irreplaceable assets, complex IP, regulation/licences, installed base, network effects. No credible new entrant in decades. | Easy to replicate; new entrants are common. | Hohn ("multiple barriers"), Dorsey |
| `market_structure` | Monopoly, or a duopoly or tight oligopoly with rational competitors; share stable or rising. | Fragmented, price wars, an irrational player. | Kantesaria (duopolies need rational competitors), Hohn |
| `pricing_power` | Regular price increases at or above inflation without losing volume; growth led by price. Value added keeps pace with price ("take 5, give 3"). | Price taker, discounting, margin pressure. | Hohn, Kantesaria, Dorsey |
| `essential_low_cost` | Essential to the customer, but a small share of the customer's costs. Spending can be deferred, not avoided. | Discretionary, or a large cost line customers attack. | Hohn (essential > discretionary), Kantesaria |
| `switching_costs` | Mission-critical and embedded in workflows; switching is risky or expensive; multi-year contracts and high renewal. | Customers switch easily. | Li Lu (Bloomberg), Hohn |
| `disruption_risk` *(5 = low risk)* | Technology (including AI) is unlikely to substitute; the product may benefit from AI. | AI or new technology could replace or commoditize it; fast-changing tech. | Hohn ("moats beaten down faster by AI"), Kantesaria |
| `regulatory_risk` *(5 = low risk)* | Regulation protects rather than threatens. | Returns so high that regulators or antitrust action are a live risk; price controls. | Hohn ("barriers too high invite regulators") |
| `reinvestment_runway` | Large, growing addressable market; capital can be reinvested at high returns for years. | Saturated market; nowhere to reinvest. | Dorsey ("narrower moat with runway"), Gaonkar |

Also give:
- `moat_types`: a list from [`irreplaceable_assets`, `complex_ip`, `installed_base_aftermarket`, `network_effects`, `switching_costs`, `scale_shared_with_customers`, `luxury_brand`, `regulatory_licence`, `toll_collector`, `cost_advantage`, `none_evident`].
- `overall_moat`: one of `wide`, `narrow`, `none`, `unclear`.
- `unknowns`: what you'd need to check outside the filing. Examples: real market share, competitor behavior, pricing history.

## Output format (one JSON object per company, all in one list)

```json
[
  {
    "company_code": "C01",
    "overall_moat": "wide",
    "moat_types": ["toll_collector", "regulatory_licence"],
    "traits": {
      "barriers_to_entry": {"score": 5, "note": "...", "quotes": [{"text": "exact words from the filing ...", "section": "Business"}]},
      "market_structure": {"score": 4, "note": "...", "quotes": [...]},
      "pricing_power": {"score": null, "note": "filing gives no pricing evidence", "quotes": []},
      "essential_low_cost": {...},
      "switching_costs": {...},
      "disruption_risk": {...},
      "regulatory_risk": {...},
      "reinvestment_runway": {...}
    },
    "bear_case": {"text": "strongest argument against the moat", "quotes": [{"text": "...", "section": "Risk factors"}]},
    "unknowns": ["...", "..."]
  }
]
```

Save it as `moat_scores.json` in the pack folder, then run `4_VERIFY_QUOTES.bat`.
