---
source_id: MT075
title: "fIrlQDvcy_M"
date: 2025-09-02
channel: "Odds on Open"
url: https://www.youtube.com/watch?v=fIrlQDvcy_M
words: 915
claims: 9
added_by_opus: 0
corrections: 0
crosscheck: "pending"
speakers: ["Ernie Chan (founder, QTS hedge fund)", "Interviewer (Odds on Open, unnamed)"]
tags: [source, layer0]
---
# fIrlQDvcy_M

**Speakers:** Ernie Chan (founder, QTS hedge fund); Interviewer (Odds on Open, unnamed)

**Summary:** Short Odds on Open clip: Ernie Chan describes his fund's crisis strategy (option-like index futures payoff in market crashes) and why strategies decay. Asked how to handle regime shifts, he argues strategies fail only if regime variables are omitted, and proposes machine learning/AI that ingests broad context (rates, news, oil, GDP) and learns which matters.

**Approach:** crisis alpha, strategy decay, regime change, machine learning, index futures

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 7 | crisis strategy, strategy decay, regime change must be modeled, simple causal models vs AI context |
| C02 | 2 | regime definition, look at everything, let AI weight inputs; sign-off |

## Claims

### C01
- **Ernie Chan** Strategies often work for a while and then stop, e.g. an FX strategy that almost never lost for months then suddenly lost and its edge disappeared.  #mech/cycle_persistence
  > A lot of times strategy work well for a while and then they go away.
  asset: fx · horizon: months · testable: partly - decay is observable out-of-sample · confidence: high
  ^MT075-C01-1
- **Ernie Chan** A crisis strategy on index futures behaves like long options: it earns only when the market crashes.  #mech/risk_premium
  > that strategy is what we call crisis strategy. It's like buying options. You will only generate return when the market has a big crash.
  indicator: index futures crisis strategy · asset: equities · direction: long crash exposure · horizon: days · conditions: pays only in big crashes · testable: yes · confidence: high
  ^MT075-C01-2
- **Ernie Chan** Markets show a panic roughly every two years since 2011, each followed by recovery, which the crisis strategy exploits.  #mech/overshoot
  > market always have this turbulence every two years you go look back to 2011 essentially every two years there's a crisis of one sort another
  indicator: equity panics · asset: equities · direction: long volatility/crash exposure · horizon: days · conditions: crashes recover; panics last days · testable: partly - frequency countable · confidence: medium
  ^MT075-C01-3
- **Ernie Chan** The crisis strategy has kept generating alpha (captioned 'offer') for over ten years, unlike decaying strategies.  #mech/cycle_persistence
  > even though we have been running it for over 10 years is still generating offer is still generating particularly crisis hour
  indicator: crisis strategy track record · asset: equities · horizon: years · testable: partly - self-reported · confidence: medium
  ^MT075-C01-4
- **Ernie Chan** Regime shifts only hurt strategies that omit the regime variable (e.g. rates), so include such inputs rather than blaming the regime.  #mech/research_method
  > the idea of regime change is that it would only negatively affect your strategy if your strategy didn't take into account the regime.
  indicator: regime variables like interest rates · asset: multi · testable: yes - add variable and test · confidence: medium
  ^MT075-C01-5
- **Ernie Chan** Traditional quants build simple causal models (e.g. pair trading Google and Microsoft), which can fail when the underlying relation changes.  #mech/research_method
  > build a strategy they make it as simple as possible that makes sense you have a clear causal model
  indicator: pairs trading · asset: equities · conditions: when relative fundamentals diverge · testable: partly · confidence: medium
  ^MT075-C01-6
- **Ernie Chan** AI can read news and add context (e.g. Microsoft monetizing AI better than Google) as a subtle modifier of a short-term model, not its main signal.  #mech/new
  > AI can read the news and say oh Microsoft is generating getting much more revenue from from from from from you know AI
  indicator: news-derived context features · asset: equities · horizon: days · conditions: even for day trading models · testable: yes - add as feature and test · confidence: medium
  ^MT075-C01-7

### C02
- **Ernie Chan** Regime is hard to define, so feed the model all context (rates, news, GDP, presidential statements, oil) rather than choosing a few variables.  #mech/new
  > the short answer is you should look at everything that's the whole point of our AI is that you should be an allseeing eye to look at everything
  indicator: broad context inputs · asset: multi · testable: partly - overfitting risk · confidence: medium
  ^MT075-C02-1
- **Ernie Chan** The AI should learn which variables matter for a strategy instead of the researcher guessing, including oil even if its relevance is unknown ahead of time.  #mech/research_method
  > the AI is supposed to figure out oh maybe interest rates is important or maybe presidential treats are important
  indicator: feature selection by machine learning · asset: multi · testable: partly - depends on sample size and validation · confidence: medium
  ^MT075-C02-2

