## Quantitative & systematic strategies

The quants agree that skepticism matters more than cleverness. Every signal needs an economic story, you should diversify across many small, independent edges, and your capital base and risk control decide whether you survive long enough for the edge to pay.

| Strategy archetype | Horizon | Who | Core edge |
| --- | --- | --- | --- |
| Market making / HFT | Seconds–days | Lebron (Jane Street), ex-IMC trader | Seeing order flow; speed; plugging every exploitable hole |
| Trend, carry and risk-premia futures | Weeks–months | Carver, Gebhardt | Many rules across 200+ markets; harvesting risk premia |
| Multi-market diversified risk premia | Months–years | Quantedge | \~300 markets lets \~25% volatility run without ruin |
| Crisis alpha | Event-driven | Ernie Chan | Option-like payoff in crashes (roughly every 2 years) |
| Merger arbitrage | Deal life | Versor | Predicting deal bumps, not just failures |
| Alternative data / NLP equity | Days–months | Jha, Kantos | Data others don't have, trained on the right labels |
| Alpha capture (structured human opinion) | Days–weeks | Cedar (Two Sigma) | Trading *changes* in expert opinion |
| Power trading | Intraday–seasonal | Paddock | Obscure market rules plus paradigm-shift views |
| Niche relative-value multi-manager | Varies | Zach | Capacity-constrained PMs the big pods can't use |
| Event and catalyst arbitrage, hedged per idea | Event-driven | Gerber (Hudson Bay) | Each idea hedged for its own beta; limited loss, independent, slight edge |
| Global multi-manager platform | Varies | Tolkin (Schonfeld) | Scale pays for technology, data, overseas reach and talent |

### 1. Skepticism is the core skill

- "Nearly every error I've seen was overconfidence": trusting backtests, assuming clean data, lookahead bias (Carver). Backtests mostly convince yourself; investors believe only live records (Gebhardt).
- The worst danger is *implicit* fitting: swapping models after seeing the full backtest. Push model choice into an explicit, evidence-weighted process. "Better to fail than to overfit" (Carver).
- Repeated tweaking against out-of-sample data turns it in-sample: a Sharpe of 1.5 in backtest becomes 0.5 live. Use the deflated Sharpe ratio and try to falsify your hypothesis (Chan).
- Most "hockey-stick" backtests hide a flaw in transaction costs or distribution assumptions (Kantos). Overfitted 20-variable backtests are "a work of fiction" (Tom).
- Historical correlation isn't predictive. Only market and sector factors matter: the 21 smaller factors explain \~6% of moves, dangerous once levered (Gerber).

### 2. Every signal needs an economic story

- Never run a black box: if you can't explain a signal simply, it will probably decay. PMs must be able to explain each day's trades (Quantedge).
- Be "empirical market scientists": write the hypothesis and causal mechanism first, then find data. "Humans are incredibly good at finding patterns where they don't exist" (Versor).
- Start from a philosophy of how prices move. "Full flexibility finds amazing systems that don't last" (Gebhardt).
- Survivors run many signals, each with economic intuition, as an evolving process (Jha).

### 3. Diversify across many small, independent edges

- Information ratio ≈ skill × √(number of independent bets). Hundreds of markets lower idiosyncratic risk enough to run high volatility (Quantedge).
- Spread across many trading rules so that no single decaying rule hurts much (Carver). Keep thin or contradictory data as a running experiment with no obligation to trade (Versor).
- A multi-manager structure exists because no single PM has 100 clever twists (Zach).
- **The Gerber statistic** is a rank-order co-movement measure that ignores moves below a threshold as noise. Papers with Markowitz found "better performance with less risk" when it replaced historical covariance (Gerber).
- Be "the house": each idea has limited loss, is independent and carries a slight edge. Hedge each idea's beta on its own, not with an overlay (Gerber).

### 4. Crowding and alpha decay

- The 2007 Quant Quake happened because everyone bought the same data and built the same factors. A forced liquidation cost PDT \~$500M in 3 days while markets looked calm (Jha).
- Signals crowd more slowly than people expect: they either fade gradually into "table stakes" or die in a sudden liquidation (Jha).
- Decay speeds: high-frequency strategies lose their edge in 1–2 months, while slow ones decay over decades and look like noise (Carver).
- Arms race: companies now pre-test earnings calls against NLP models, and "Lazy Prices" is arbitraged away (Kantos). Earnings-day moves in insurance went from 2–3% to 15–20% intraday as data spread (Ying).
- An edge's value is inversely proportional to how many people know it (Lebron).
- Momentum and value work because everyone latches onto them, and fail in dislocations (Gerber). Technical analysis is "about 20% as effective" as it was (Druckenmiller).

### 5. Regime change

- The biggest power-trading edge is a view on a paradigm shift before it's priced. Historical data is a trap when the grid's topology changes. "If you want to trade an insight from 8 years ago, we're happy to take the other side" (Paddock).
- Regime change only hurts if the regime isn't a model input: if rising rates hurt you, why weren't rates an input? (Chan)
- Even systematic traders must judge whether today's regime is in-sample for their model (Lebron). In March 2020 quant models lost 5–10% because they had never seen a pandemic (Cedar). Regimes now shift every 2–3 years, so rigidity kills (Ying).
- Today's investors grew up in a paradigm that "got way accelerated the last 15 years": globalization, the US "security umbrella" and easy money. It is ending, so its history is a biased sample (Karniol-Tambour, May 2025).

### 6. Liquidity, capacity and the capital base

- Alpha in small, illiquid markets is "a mirage" unless you can trade size. Build real transaction costs into the optimizer (Versor).
- "Funds die from redemptions at the wrong time, not drawdowns." Quantedge introduced lock-ups, a move it estimates cost \~$20B of assets but aligned investors (Quantedge).
- In a crisis your capital base decides whether you can hold on: monthly-liquidity funds rode out the Quant Quake (Jha). Forced sellers create opportunity for those who aren't (Lebron).
- Small can be an edge: firms are viable above \~$100–200M and can trade less liquid names (Jha), and niche PMs are uncorrelated with the pods (Zach).

### 7. Humans remain inputs

- Alpha capture: survey analysts often, trade *deltas* not levels, fade experts who get even more extreme, and follow the first one who breaks from the crowd (Cedar).
- Quantamental: if a question can be answered without knowing which company it is, automate it; "how is this time different" stays human. Fundamental investors size badly and quants size well (Ying).
- Top PMs are \~90–95% conventional plus a clever twist. "Clever beats working harder" (Zach).

### 8. Measuring performance honestly

- No metric is perfect. Sharpe assumes symmetric returns, and LTCM's Sharpe was >3 *including* its blow-up. Use bootstrapped geometric returns at a conservative percentile (Carver).
- You never *know* you have edge, only statistical bounds, which pushes quants toward higher frequency. Judge discretionary edge on decision quality, the way a poker coach does (Lebron).
- Ignore your daily P&L, or view it in percentages, not "I lost a car today" (Carver). Judge process over outcome: 5–10 trades make most of a year (Paddock).
