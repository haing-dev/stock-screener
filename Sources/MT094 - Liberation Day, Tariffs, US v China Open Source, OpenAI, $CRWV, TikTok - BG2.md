---
source_id: MT094
title: "Liberation Day, Tariffs, US v China Open Source, OpenAI, $CRWV, TikTok - BG2"
date: 2025-04-04
channel: "Bg2 Pod"
url: https://www.youtube.com/watch?v=b0DO0tP06eQ
words: 13710
claims: 82
added_by_crosscheck: 17
corrections: 5
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Brad Gerstner (Altimeter Capital, host)", "Bill Gurley (Benchmark, investor)"]
tags: [source, layer0]
---
# Liberation Day, Tariffs, US v China Open Source, OpenAI, $CRWV, TikTok - BG2

**Speakers:** Brad Gerstner (Altimeter Capital, host); Bill Gurley (Benchmark, investor)

**Summary:** BG2 episode recorded on Liberation Day: tariffs and market reaction, China open source and DeepSeek vs OpenAI open weights, OpenAI valuation and unit economics, CoreWeave IPO and GPU depreciation, TikTok deal. Conclusions: tariffs will land lower than announced after negotiation, buy fear selectively, models commoditize and value moves to products.

**Approach:** tech investing, tariffs, AI, venture

**Cross-check completeness estimate of first read:** 0.82 - first reader (66 claims) caught the tariff, open-source, OpenAI valuation, GPU-depreciation and TikTok arguments; misses are mostly supporting facts, secondary reasoning links and several speaker attributions between the two hosts.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | sports banter; tariff doctrine view |
| C02 | 3 | agenda, market reaction to Liberation Day, non-tariff barriers |
| C03 | 3 | tariff structure, revenue math, exemptions |
| C04 | 5 | free-trade theory, reshoring, uncertainty and capex |
| C05 | 4 | cascading effects, Nasdaq drawdown, forecast tariffs, buying fear |
| C06 | 4 | clearing event, China open source |
| C07 | 4 | defensive open source, DeepSeek |
| C08 | 3 | OpenAI open-weight, Llama 4, DC policy |
| C09 | 3 | open source strategy, commoditization, consumerization |
| C10 | 2 | OpenAI round valuation multiples |
| C11 | 5 | mega-round promo, unit economics, losses, Uber analogy |
| C12 | 4 | ChatGPT metrics, compute demand, toy thesis |
| C13 | 3 | conversion, agent monetization, Google disruption |
| C14 | 3 | LTV math, MCP, critical window |
| C15 | 3 | CoreWeave customer mix, IPO timing, business model |
| C16 | 3 | IPO delays, GPU depreciation, CoreWeave economics |
| C17 | 4 | GPU lifetimes, depreciation pushback, Nvidia multiple, IPO price |
| C18 | 3 | IPO pricing, TikTok structure |
| C19 | 2 | TikTok valuation, ByteDance |
| C20 | 3 | TikTok risks, US-China outlook |

## Claims

### C01
- **Brad Gerstner** The administration's tariff push is a philosophical, doctrinal belief about fair trade rather than just a bargaining ploy; the debate is only how big, so conservative positioning was warranted.  #mech/policy_reaction _(time-bound view)_
  > You know this was doctrinal.
  asset: multi · direction: tariffs persist · horizon: months · testable: no: interpretation of intent · confidence: medium
  ^MT094-C01-1

### C02
- **Brad Gerstner** The pro-growth agenda (lower taxes, less regulation, M&A flywheel, AI super cycle) is the bullish side; the open question is how large tariffs land and how budget cuts offset.  #mech/policy_reaction _(time-bound view)_
  > pro business pro investment lower taxes less regulation pro M&A
  asset: equities · horizon: months · conditions: Bullish if tariffs land at the low end · testable: no: qualitative · confidence: medium
  ^MT094-C02-1
- **Brad Gerstner** Markets rose ~2.5% on a 10% across-the-board headline, then futures fell sharply when the reciprocal tariff table (China 54%) was shown; indices were already down 8-15% YTD.  #mech/overshoot _(time-bound view)_
  > They had a 600 basis point fall between where they initially jumped and where they ended up.
  indicator: S&P and Nasdaq futures on tariff headline · asset: equities · direction: equity down · horizon: days · conditions: Larger-than-expected tariffs · testable: yes: one event · confidence: high
  **Correction (cross-check):** Speaker appears wrong: the account of the market reaction (WSJ headline, +2.5%, then futures sinking when the 54% table appeared) follows 'You're right. We just listened to the president talk' and is Bill Gurley's, asking Brad for data; Brad answers in the next turn. → Bill Gurley: markets rose about 2.5% on the 10% across-the-board headline, then S&P and Nasdaq futures fell about 600bp from the high when the reciprocal table (China 54%) was shown; indices were already down 8-15% YTD.
  ^MT094-C02-2
- **Bill Gurley** Reciprocal tariffs are calculated from effective rates that include non-tariff barriers (currency manipulation, judicial actions), so the numbers can be set arbitrarily.  #mech/policy_reaction _(time-bound view)_
  > they call them non-tariff trade barriers. This is everything from what they call currency manipulation
  asset: fx · horizon: months · testable: no: policy formula · confidence: high
  **Correction (cross-check):** Speaker appears wrong: Bill Gurley raises the point that the administration computes an 'effective tariff'; it is Brad Gerstner who answers 'Correct. I mean, they call them non-tariff trade barriers' and says the numbers can be made whatever you want. → Brad Gerstner: the reciprocal numbers include non-tariff barriers (currency manipulation, judicial actions), so they can be set to whatever the administration wants (Bill Gurley raised the question).
  ^MT094-C02-3
- **Brad Gerstner** The market's key question before Liberation Day was where tariffs would land between the hawk camp (Navarro, Lutnik: $600bn to $1tn) and the lower-end camp (Bessent, Hassett); the landing point and the budget-cut glide path determine whether the pro-growth agenda dominates.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > were tariffs going to land closer to the $600 billion trillion dollar tariff level that Peter Navaro had been talking about
  indicator: US tariff revenue landing point · asset: equities · direction: equities down if tariffs land at the high end · horizon: weeks · conditions: Depends on tariff size and offsetting budget cuts · testable: partly - tariff revenue is measurable ex post · confidence: medium
  ^MT094-C02-X1

### C03
- **Brad Gerstner** Tariff structure: autos 25%, country-specific reciprocal rates, and a minimum 10% on all countries, with China a separate negotiation.  #mech/policy_reaction _(time-bound view)_
  > we're going to have a minimum tariff of 10% on all countries
  indicator: US tariff schedule · asset: multi · horizon: months · testable: yes: published schedule · confidence: high
  ^MT094-C03-1
- **Brad Gerstner** The announced tariff table is a starting point for ad hoc country-by-country negotiations (e.g. Vietnam) before April 9.  #mech/policy_reaction _(time-bound view)_
  > All these tariffs go into place. We'll put these charts up on April 9th country by country. And so we're going to hear all these ad hoc negotiations going on.
  asset: multi · direction: tariff rates down via deals · horizon: weeks · testable: yes: later outcomes observable · confidence: medium
  ^MT094-C03-2
- **Brad Gerstner** Tariff revenue would rise from about 77bn to 750bn, above Navarro's 600bn estimate, but pharma and semiconductor exemptions probably bring it to about 600bn.  #mech/policy_reaction _(time-bound view)_
  > we were at 77 billion last year and we end up at about 750 billion
  indicator: US tariff revenue · asset: multi · horizon: months · testable: yes: customs revenue · confidence: medium
  ^MT094-C03-3
- **Brad Gerstner** Tariffs are a delivered campaign promise to blue-collar and union voters (autos, UAW on stage), which gives the administration a political reason to keep them and shows how the parties have swapped trade positions.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > We won the state of Michigan because of this. This is what I campaigned on.
  indicator: auto tariffs 25% · asset: multi · direction: tariffs persist politically · horizon: years · conditions: Political benefit from union and manufacturing voters · testable: no - qualitative political reading · confidence: medium
  ^MT094-C03-X1
- **Brad Gerstner** The administration cites about $6 trillion of new US investment pledges (Nvidia, Apple, TSMC, SoftBank, OpenAI) as the payoff from tariffs, which is the administration's justification for the policy.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > He's also declared that there are $6 trillion of new investments right that people have committed to in the United States.
  indicator: announced US investment pledges · asset: equities · direction: onshoring investment up · horizon: years · conditions: Pledges may not translate into capex · testable: partly - compare pledges with realised capex · confidence: low
  ^MT094-C03-X2

### C04
- **Bill Gurley** Comparative advantage theory implies trade walls reduce efficiency in both countries in the long run.  #mech/structural_shift
  > there are very solid mathematical arguments why if you pull up the trade walls between multiple countries that you're going to hurt the efficiency of both of them um in the long run
  asset: multi · horizon: years · testable: no: theory · confidence: high
  ^MT094-C04-1
- **Bill Gurley** Reshoring a factory from Asia takes years and costs more because US labor is not globally competitive, so tariffs cannot quickly shift production.  #mech/structural_shift
  > if you start that process today, it might take three years
  asset: multi · direction: production costs up · horizon: years · testable: no: qualitative · confidence: medium
  ^MT094-C04-2
- **Bill Gurley** Policy ambiguity (not knowing what tariffs apply in 3, 6, 12 months) makes capex allocation very hard; business abhors uncertainty and needs predictability to forecast NPV.  #mech/behavioral _(time-bound view)_
  > which makes it very hard to allocate capex in any meaningful way whatsoever
  indicator: policy uncertainty and capex · asset: equities · direction: capex down · horizon: months · testable: partly: uncertainty indices vs capex · confidence: high
  ^MT094-C04-3
- **Brad Gerstner** About 100 CEOs reported a slowdown in February-March from tariff uncertainty, and the Fed cut GDP and raised inflation and unemployment forecasts, raising recession odds.  #mech/behavioral _(time-bound view)_
  > They said things are slowing down in February and March because nobody knows what to do.
  indicator: CEO survey / Fed projections · asset: multi · direction: growth down, recession odds up · horizon: months · testable: partly · confidence: medium
  ^MT094-C04-4
- **Brad Gerstner** Uncertainty cascades: firms pause hiring, which raises unemployment and eventually cuts consumer spending.  #mech/behavioral _(time-bound view)_
  > you're not going to hire a bunch of people, for example
  indicator: hiring, unemployment · asset: multi · direction: spending down · horizon: months · testable: partly · confidence: medium
  ^MT094-C04-5

### C05
- **Brad Gerstner** Retaliation effects: customers cancelling US vendors and China, Korea and Japan (and Europe) coordinating a response, shifting trade ties toward China.  #mech/structural_shift _(time-bound view)_
  > three European contracts canled and one Asian contract cancelled because the countries were so upset with America
  asset: multi · direction: US exporters hurt · horizon: months · testable: no: anecdote · confidence: low
  ^MT094-C05-1
- **Brad Gerstner** After hours the Nasdaq was down nearly 18% peak to trough with many names down 40-50%, so fear is entering prices.  #mech/overshoot _(time-bound view)_
  > NASDAQ down peak to trough post Trump at almost 18%
  indicator: Nasdaq drawdown · asset: equities · direction: equity down · horizon: days · testable: yes: price data · confidence: high
  ^MT094-C05-2
- **Brad Gerstner** Tariffs will settle closer to 300-400bn because the president wants deals and congressional Republicans, hearing from CEOs, constrain him (he cannot lose a vote on the reconciliation bill).  #mech/policy_reaction _(time-bound view)_
  > I think we're going to land the plane here closer to three or 400 billion in tariffs, not 6 or 700 and certainly not a trillion in tariffs
  indicator: tariff revenue · asset: multi · direction: tariffs lower · horizon: months · conditions: Needs Republican votes for reconciliation · testable: no: forecast · confidence: medium
  ^MT094-C05-3
- **Brad Gerstner** After the selloff, add to favorite companies as fear is priced in, while watching exemptions (semis, pharma), country renegotiations and China.  #mech/overshoot _(time-bound view)_
  > We're going to get a little bit more positive on the companies we like the best cuz we think some of this fear is now getting priced in.
  asset: equities · direction: buy quality equities · horizon: months · conditions: After a fear-driven drawdown · testable: no: discretionary · confidence: medium
  ^MT094-C05-4
- **Bill Gurley** Bill sees many negative ramifications of the tariff package (trading partners retaliating, realigning with China) and nothing in it that is good for markets or stocks, though he says macro is outside his usual world.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > I don't think that anything came out of it that's going to be good for the markets and good for good, you know, good for stocks
  asset: equities · direction: stocks down · horizon: months · testable: no - qualitative · confidence: medium
  ^MT094-C05-X1

### C06
- **Brad Gerstner** No clearing event for tariffs for at least 30-60 days, so the market remains in the fog of war.  #mech/policy_reaction _(time-bound view)_
  > I don't think I see any clearing event here um for at least uh another 30 to 60 days.
  asset: multi · direction: volatility remains · horizon: weeks · testable: no: forecast · confidence: medium
  ^MT094-C06-1
- **Brad Gerstner** The best purchase prices come when people are fearful, so one must take a leap of faith.  #mech/behavioral
  > the best opportunities to buy something are when people are a little fearful
  asset: equities · direction: buy during fear · horizon: months · testable: partly: contrarian sentiment studies · confidence: medium
  ^MT094-C06-2
- **Brad Gerstner** A US-China trade deal is imminent because tariffs of this size on China are too large to hold.  #mech/policy_reaction _(time-bound view)_
  > it's imminent that he and she are going to have to talk and get a big trade deal done
  indicator: US-China tariffs · asset: multi · direction: tariff de-escalation · horizon: months · testable: no: forecast · confidence: medium
  ^MT094-C06-3
- **Bill Gurley** Chinese support for open source is long-standing (not forced on DeepSeek), since open source removes IP-theft accusations.  #mech/structural_shift
  > China has been supportive of open source for well over a decade now
  asset: other · horizon: years · testable: no: history · confidence: high
  ^MT094-C06-4

### C07
- **Bill Gurley** Large companies use open source defensively when behind (Google/Kubernetes vs AWS, Android vs Apple, Meta/Llama), which commoditizes the leader's advantage.  #mech/structural_shift
  > if they get in a position where they feel like they're behind the eightball. So they're not in a leadership position, they will embrace open source as an attempt to level the playing field.
  asset: equities · horizon: years · conditions: When a firm is not the market leader · testable: partly: historical cases · confidence: high
  ^MT094-C07-1
- **Bill Gurley** Open source creates the most fluid competition and lowest consumer prices versus proprietary code.  #mech/structural_shift
  > Like it's just hyper competitive.
  asset: equities · direction: prices down · horizon: years · testable: no: theory · confidence: medium
  ^MT094-C07-2
- **Bill Gurley** DeepSeek is prolific in enterprise (hosted by AWS and Google, forked 1500+ times), so Washington may act to limit its use.  #mech/structural_shift _(time-bound view)_
  > it's been you know forked over 1500 times on their site
  indicator: DeepSeek adoption · asset: equities · horizon: months · testable: partly: fork count · confidence: medium
  ^MT094-C07-3
- **Bill Gurley** A short window exists for a US lab (Google or Meta; not Anthropic) to out-open DeepSeek, as an offensive or defensive move.  #mech/structural_shift _(time-bound view)_
  > you have a window in the US right now where someone might move to go left of deepseek in terms of openness on one of their models
  asset: equities · horizon: weeks · testable: no: speculative · confidence: medium
  ^MT094-C07-4

### C08
- **Brad Gerstner** OpenAI committed to an open-weight reasoning model without Llama's 700M-user licensing cap, putting pressure on Meta before LlamaCon.  #mech/structural_shift _(time-bound view)_
  > we're excited to release a powerful new openweight language model with reasoning in the coming months
  indicator: OpenAI open-weight release · asset: equities · horizon: months · testable: yes: release observable · confidence: high
  ^MT094-C08-1
- **Brad Gerstner** Llama 4 is rumored to be a 400bn-parameter mixture-of-experts with a 10-million context window, launching before LlamaCon.  #mech/structural_shift _(time-bound view)_
  > What I'm hearing Bill is that it'll be a 400 billion parameter model.
  indicator: Llama 4 specs · asset: equities · horizon: weeks · testable: yes · confidence: low
  ^MT094-C08-2
- **Brad Gerstner** Washington wants the world to run on US compute and models (Llama, OpenAI) rather than DeepSeek on Huawei chips, tying to AI diffusion restrictions.  #mech/policy_reaction _(time-bound view)_
  > they do not want to see a Huawei Deepseek Belt and Road either with chips or with open- source models
  asset: equities · direction: US AI exports favoured · horizon: years · testable: no: interpretation · confidence: medium
  ^MT094-C08-3

### C09
- **Bill Gurley** Open-sourcing a model protects the competitive flank like Google's Kubernetes move: others cannot make an API business, the model spreads globally, and compute is borne by users.  #mech/structural_shift
  > kind of wiping out the business opportunity for other models to play on the API side if you make yours open
  asset: equities · direction: API model revenues down · horizon: years · testable: no: strategic reasoning · confidence: medium
  ^MT094-C09-1
- **Brad Gerstner** Models are commoditizing; the contest is around products and services, with OpenAI focused on consumer (ChatGPT) and a leading enterprise business.  #mech/structural_shift
  > the battleground bill is really going to be fought around products and services
  asset: equities · direction: value to product layer · horizon: years · testable: no: strategy claim · confidence: medium
  ^MT094-C09-2
- **Brad Gerstner** ChatGPT's consumer base drives enterprise adoption (like iPhones displacing BlackBerry), with roughly 80-90% consumer share.  #mech/structural_shift _(time-bound view)_
  > Um because remember the consumerization of the enterprise. One of the fascinating things that's happening in the enterprise is these are all users of chat GPT.
  indicator: ChatGPT consumer share · asset: equities · horizon: years · testable: partly: share data · confidence: medium
  ^MT094-C09-3
- **Bill Gurley** Even if Washington restricts DeepSeek, a Western lab that wants to lead open source globally has to beat DeepSeek on openness and capability worldwide, not only be more open than other Western labs.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > they still have to compete with deepseek on a global on a global basis
  indicator: DeepSeek versus Western open-weight models · asset: equities · horizon: years · conditions: If DeepSeek usage is restricted in the US · testable: no - qualitative · confidence: medium
  ^MT094-C09-X1
- **Brad Gerstner** OpenAI's open-weight release serves three aims: bringing developers into its ecosystem, building products at scale, and acknowledging that models are commoditizing, so platform lock-in comes from products rather than the model.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > they want developers to develop on their platform and build applications for you know for open AI and so this brings them into the ecosystem
  indicator: open-weight model adoption · asset: equities · direction: value shifts to product and ecosystem · horizon: years · testable: no - strategy interpretation · confidence: medium
  ^MT094-C09-X2

### C10
- **Brad Gerstner** Market leaders never look cheap (Google 2005, Meta IPO, Microsoft's round); judge by multiples relative to peers.  #mech/risk_premium
  > market leaders never look cheap
  asset: equities · horizon: years · testable: no: heuristic · confidence: medium
  ^MT094-C10-1
- **Brad Gerstner** OpenAI's roughly $300bn post-money is about 20x forward run-rate revenue (13bn year, 15-18bn exit) versus Anthropic at 50x and X/xAI at 80x.  #mech/risk_premium _(time-bound view)_
  > So again you got OpenAI at 20 times, Anthropic at 50 times and then we had the merger of X and X.AI
  indicator: valuation / forward run-rate revenue · asset: equities · horizon: months · testable: yes: multiples · confidence: medium
  ^MT094-C10-2
- **Brad Gerstner** OpenAI's headline $40bn round led by SoftBank comes in two tranches (about $10bn then about $30bn), is larger than almost any IPO (a 'private IPO'), and values the company at about $260bn pre and $300bn post.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > the first trunch being closer to 10 billion. The second trunch being closer to 30 billion
  indicator: OpenAI funding round size and valuation · asset: equities · conditions: Second tranche conditional on later events · testable: yes - reported deal terms · confidence: high
  ^MT094-C10-X1

### C11
- **Bill Gurley** Mega-round headline numbers (Stargate, OpenAI) are bigger than the tranched reality and promotional, reflecting winner-take-all belief and a message to rivals.  #mech/behavioral _(time-bound view)_
  > the headline numbers bigger than you know the peace meal when you start to unpack it which you know for better for worse from my position smells of being promotional
  asset: equities · horizon: months · testable: no: judgement · confidence: medium
  ^MT094-C11-1
- **Bill Gurley** Capital-intensive winner-take-all competition postpones unit economics, requiring belief in power laws; Bill compares it to Uber/Lyft and a sport of kings.  #mech/structural_shift
  > unit economics get postponed. You have to believe in the power law and the network effect.
  asset: equities · horizon: years · testable: no: theory · confidence: medium
  ^MT094-C11-2
- **Bill Gurley** OpenAI expects 5-7bn of losses, with costs mostly compute rather than staff.  #mech/risk_premium _(time-bound view)_
  > they've said publicly they expect to lose, you know, five to seven billion this year
  indicator: OpenAI losses · asset: equities · horizon: months · testable: yes: reported · confidence: medium
  ^MT094-C11-3
- **Bill Gurley** Serving a free ChatGPT user costs roughly 15-20 dollars a year, which advertising or paid conversion may eventually cover.  #mech/structural_shift _(time-bound view)_
  > I ran some loose numbers and I come up around 15 or 20 bucks a year for a non-paid user
  indicator: cost per free user · asset: equities · horizon: years · testable: partly: estimate · confidence: low
  ^MT094-C11-4
- **Brad Gerstner** Uber was called unprofitable in 2020 yet now makes about 6bn FCF, so losses along the way do not disprove winner-take-most dynamics.  #mech/structural_shift
  > the winner does take all. The winner does take most.
  asset: equities · horizon: years · testable: no: analogy · confidence: medium
  ^MT094-C11-5
- **Bill Gurley** The OpenAI round carries contingencies on whether the nonprofit-to-for-profit conversion completes, so the headline funding is not fully secured.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > there there like are still contingencies on whether the full conversion from a nonprofit to a for-profit happens
  indicator: OpenAI structure conversion · asset: equities · conditions: Conversion approval · testable: yes - corporate filings · confidence: medium
  ^MT094-C11-X1
- **Bill Gurley** A challenger chasing ChatGPT must be prepared to fund the compute cost of free users itself, which makes the race a sport of kings and worrying for investors in smaller rivals such as Anthropic.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > if you're going to try and lay chase to them, um you got to be prepared to underwrite that cost yourself
  indicator: cost of serving free AI users · asset: equities · direction: funding burden on challengers · horizon: years · conditions: Scale economics favour the leader · testable: no - qualitative · confidence: medium
  ^MT094-C11-X2

### C12
- **Brad Gerstner** ChatGPT reached 20 million paid subscribers and 500 million weekly users, adding a million users in an hour.  #mech/structural_shift _(time-bound view)_
  > They crossed 500 million weekly average users of Chat GPT.
  indicator: ChatGPT users/subscribers · asset: equities · horizon: weeks · testable: yes: company data · confidence: high
  ^MT094-C12-1
- **Brad Gerstner** AI demand exceeds compute supply (rate limits, Sam asking for 100,000-GPU clusters), explaining the large raise and infrastructure build, and blocking product launches.  #mech/liquidity_flows _(time-bound view)_
  > America's leading AI companies are all reporting that demand is off the charts. so much so that they're being forced to impose rate limits.
  indicator: GPU demand / rate limiting · asset: equities · direction: compute buildout up · horizon: months · testable: partly · confidence: medium
  ^MT094-C12-2
- **Brad Gerstner** Viral demand for image generation (anime photos) is a sign of consumer pull: the next big thing often first appears as a toy.  #mech/structural_shift
  > the next big thing will first appear as a toy
  asset: equities · horizon: years · testable: no: heuristic · confidence: low
  ^MT094-C12-3
- **Brad Gerstner** ChatGPT's demand curves and cohort retention resemble early Google and Meta, so its consumer business will ultimately be valuable despite poor unit economics.  #mech/structural_shift
  > what I see out of chat GPT reminds me a lot of kind of those winner take all consumer applications
  indicator: demand curves, cohort retention · asset: equities · horizon: years · testable: partly: retention data · confidence: medium
  ^MT094-C12-4

### C13
- **Brad Gerstner** With more compute, upgraded models and pricing tiers would raise paid conversion above the roughly 4%, and a single smart model would replace the long model menu.  #mech/structural_shift _(time-bound view)_
  > I think most of Chat GPT users are using a model that's like a year old, right?
  indicator: paid conversion (20M/500M) · asset: equities · direction: conversion up · horizon: months · conditions: Once compute constraints ease · testable: no: speculation · confidence: low
  ^MT094-C13-1
- **Brad Gerstner** In an agent world (booking hotels) value to users or merchants creates mixed models of ads, tiers and commissions.  #mech/structural_shift _(time-bound view)_
  > either the user will pay or the end merchant will pay
  asset: equities · horizon: years · testable: no: speculation · confidence: low
  ^MT094-C13-2
- **Brad Gerstner** Google's maximized revenue per visitor makes it vulnerable, since agent partners cannot pay fees close to what advertisers pay Google.  #mech/structural_shift _(time-bound view)_
  > one of the reasons that Google is so susceptible to disruption is how they've maximized the revenue per visitor
  indicator: revenue per visitor · asset: equities · direction: Google ad pressure · horizon: years · conditions: Agent-based booking · testable: partly · confidence: medium
  ^MT094-C13-3
- **Brad Gerstner** ChatGPT has a big moat because network effects are kicking in: it is an order of magnitude bigger than rivals (even with Grok a strong model) and growing faster, so the consumer business will be valuable despite poor early unit economics.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > they really do have a big moat and I think the network effects are kicking in
  indicator: ChatGPT user base versus rivals · asset: equities · direction: leader share rises · horizon: years · conditions: Network effects persist · testable: partly - usage share is observable · confidence: medium
  ^MT094-C13-X1

### C14
- **Brad Gerstner** Travel advertisers like Booking pay Google about 50 per 100-dollar room using LTV math, while an agent-underlying service could share at most about 10, a big disruption advantage for OpenAI.  #mech/structural_shift _(time-bound view)_
  > they'll they'll pay 50 bucks instead of 20
  indicator: ad take rate per booking · asset: equities · direction: Google revenue down · horizon: years · testable: partly: unit economics example · confidence: medium
  ^MT094-C14-1
- **Bill Gurley** Open standards like MCP (started at Anthropic, now supported by OpenAI) let the most aggressive adopters define the agent ecosystem.  #mech/structural_shift _(time-bound view)_
  > there's this acronym people are starting to use, MCP, that is a way for you to represent your service.
  asset: equities · horizon: years · testable: no · confidence: low
  ^MT094-C14-2
- **Brad Gerstner** The next 3-6 months are a critical window, with executive shifts and anxiety at Google, Meta and Apple, ending 20 years of search paradigm dominance.  #mech/structural_shift _(time-bound view)_
  > I'm talking about like next 3 to 6 months could dictate who's standing on top of the hill 5 10 years from now
  asset: equities · horizon: months · testable: no · confidence: low
  **Correction (cross-check):** Speaker mixed: the anxiety at Google, Meta and Apple and the 3-6 month 'critical window' are Bill Gurley's (continuing after the MCP comment); the 'tectonic plates shifted for the first time in 20 years, search ruled 20 years' remark is Brad's. → Bill Gurley: anxiety is high at Google, Meta and Apple (executive shifts) and the next 3-6 months could decide who leads in 5-10 years. Brad Gerstner: this is the first tectonic shift in 20 years after two decades of search dominance.
  ^MT094-C14-3
- **Brad Gerstner** Google's share price falling from about 200 to about 150 shows the market already pricing disruption of search advertising by AI agents.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > Google's traded down from 200 to 150 in change and and you know, they see that disruption coming their way
  indicator: Alphabet share price · asset: equities · direction: Google down · horizon: months · conditions: AI agents replace paid search for travel · testable: yes - price series · confidence: medium
  ^MT094-C14-X1
- **Brad Gerstner** Antitrust action to break up Google's search monopoly arrives just as real competition from AI appears, so the market itself is correcting the monopoly and remedies are the last of Google's problems.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > finally in 2025, the first time we've actually had competition for Google, like very clear that competition is coming to all those categories
  indicator: Google search antitrust case · asset: equities · horizon: years · conditions: Competition from AI products · testable: no - qualitative · confidence: medium
  ^MT094-C14-X2

### C15
- **Brad Gerstner** CoreWeave diversified customers beyond Microsoft (Google deal on Nvidia Grace Blackwell), falling to about 37 around IPO then rising; it emerged as leading AI cloud.  #mech/structural_shift _(time-bound view)_
  > They have Microsoft, Meta, now Google, OpenAI, Nvidia, Coher, Mistral.
  indicator: CoreWeave customer mix · asset: equities · direction: long CoreWeave · horizon: months · testable: no: single-name view · confidence: medium
  ^MT094-C15-1
- **Bill Gurley** Do not wait for the market to be right before IPOing; IPO timing cannot be controlled.  #mech/behavioral
  > you can't control that thing. That's an external factor.
  asset: equities · testable: no: opinion · confidence: medium
  ^MT094-C15-2
- **Bill Gurley** CoreWeave's income statement is hard to read because capex precedes revenue and depreciation schedules are uncertain.  #mech/research_method
  > Their business model isn't fully unpacked because the capex is invested so far ahead of of the product.
  indicator: depreciation schedule, capex vs revenue · asset: equities · horizon: years · testable: yes: accounting · confidence: medium
  ^MT094-C15-3

### C16
- **Brad Gerstner** Large private companies are delaying IPOs because of massive private capital access, offsetting the push for more public listings.  #mech/liquidity_flows _(time-bound view)_
  > the stripes of the world and and data bricks and others are choosing to delay being public and have massive access to private capital
  indicator: IPO pipeline · asset: equities · direction: fewer IPOs · horizon: years · testable: partly: IPO counts · confidence: medium
  **Correction (cross-check):** Speaker likely wrong: the IPO-delay remark (Stripe, Databricks delaying; Klarna, Cerebras in the pipeline) continues Bill Gurley's IPO comments from C15; Brad's turn begins with 'Well, yeah. And somebody else I should mention is Morgan Stanley'. → Bill Gurley: large companies such as Stripe and Databricks are delaying IPOs because of abundant private capital, which offsets the push for more listings.
  ^MT094-C16-1
- **Brad Gerstner** GPUs keep value past the first two training years because they are reused for inference, so a two-year depreciation (implied by Jensen's 'chief revenue destroyer' remark) is too aggressive.  #mech/structural_shift
  > cutting edge GPUs are going to be used for cutting edge training for the, you know, frontier models in that first two-year period. But all these things are going to continue to get used for inference.
  indicator: GPU useful life · asset: equities · horizon: years · testable: partly: observe GPU lifecycles · confidence: medium
  ^MT094-C16-2
- **Brad Gerstner** CoreWeave contracts (four-year Microsoft, OpenAI, Google) repay capex, opex and GPUs in three years so year four is the margin; consensus EBIT around 25% gives no credit beyond contracts.  #mech/structural_shift _(time-bound view)_
  > They expect to pay back all the capex, opex, and GPUs in three years. And so, the fourth year, which is a four-year guaranteed contract, the fourth year is your profit margin, right?
  indicator: CoreWeave contract payback, EBIT margin · asset: equities · horizon: years · conditions: If contracts hold · testable: yes: modelable · confidence: medium
  ^MT094-C16-3

### C17
- **Brad Gerstner** Evidence of long GPU lives: A100s (2020) still widely used and V100s retired after seven years; CUDA software updates improve GPUs over time.  #mech/structural_shift
  > OpenAI had just retired the V100s. That was a 2017 GPU. So that's like a 7-year life cycle
  indicator: GPU lifecycle · asset: equities · direction: depreciation concern overstated · horizon: years · testable: yes: lifecycle data · confidence: medium
  ^MT094-C17-1
- **Bill Gurley** Depreciation should mirror the declining earning power of GPUs; six straight years is probably not the best fit (peers moved from four to six), the answer may lie in between.  #mech/research_method
  > what inevitably happens is the earning power of that product drops over time
  indicator: depreciation schedule · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT094-C17-2
- **Bill Gurley** Nvidia at 19x fully taxed earnings shows heavy skepticism about AI demand despite strong evidence.  #mech/risk_premium _(time-bound view)_
  > you have Nvidia trading at 19 times fully taxed earnings
  indicator: Nvidia P/E · asset: equities · horizon: months · testable: yes: multiple observable · confidence: medium
  **Correction (cross-check):** Speaker likely wrong: the Nvidia 19x remark closes Brad's CoreWeave answer (after 'the multiples that came public at were not overly taxing'); Bill's next turn is the IPO riddle. → Brad Gerstner: Nvidia trades at 19 times fully taxed earnings, showing broad scepticism about AI demand despite strong evidence.
  ^MT094-C17-3
- **Bill Gurley** Trading below IPO price is a poor quality signal; Salesforce, Netflix, Amazon, Facebook, Palo Alto and others all broke issue.  #mech/behavioral
  > when the talking heads on CNBC and others are critical of a company because they trade below their IPO price, it's just such a wrong way to look
  indicator: IPO price vs trading price · asset: equities · horizon: years · testable: yes: IPO history · confidence: medium
  ^MT094-C17-4
- **Brad Gerstner** CoreWeave is highly levered and must delever, which is the main risk against the cash-flow case from contracted GPU revenue.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > it's a highly levered business. They got to delever the business.
  indicator: CoreWeave leverage · asset: equities · horizon: years · conditions: Contract revenue must cover debt · testable: yes - balance sheet data · confidence: medium
  ^MT094-C17-X1
- **Brad Gerstner** At its IPO CoreWeave's valuation multiples were not overly demanding relative to contracted cash flows, even though sentiment on AI demand is sceptical (Nvidia at 19x).  #mech/risk_premium _(added by sonnet-xhigh cross-check, time-bound view)_
  > the multiples that came public at were not overly taxing from our perspective
  indicator: CoreWeave IPO multiples · asset: equities · conditions: Contract economics hold · testable: yes - compare multiples with peers · confidence: low
  ^MT094-C17-X2

### C18
- **Bill Gurley** High-quality IPOs are priced to perfection because strong founders negotiate hard, which also explains post-IPO dips.  #mech/behavioral
  > I think one of the reasons those highquality companies get priced to perfection is the founders are stronger minded and have more leverage
  asset: equities · testable: no · confidence: low
  ^MT094-C18-1
- **Bill Gurley** CoreWeave's series C put right at 38.75 likely influenced the IPO pricing at 40.  #mech/structural_shift _(time-bound view)_
  > the series C has a put right at like 3875. No doubt in my mind people wanted to make sure it priced above that
  asset: equities · horizon: days · testable: no: inference · confidence: low
  ^MT094-C18-2
- **Brad Gerstner** TikTok US rumored structure: new company with ByteDance under 20%, existing ByteDance shareholders (60% US investors) and about half new investors; the licence is to the algorithm.  #mech/policy_reaction _(time-bound view)_
  > they have to keep that owner ownership threshold under 20%
  indicator: TikTok US ownership · asset: equities · horizon: weeks · testable: no: rumor · confidence: low
  ^MT094-C18-3
- **Brad Gerstner** The TikTok sale, which needed extension by April 5, will be settled inside the broader US-China tariff negotiation rather than separately.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > I'm sure this will end up as part of a big trade negotiation as it pertains to China
  indicator: TikTok divestiture deadline · asset: multi · horizon: weeks · conditions: Tariff negotiations with China · testable: partly - observable on deal announcement · confidence: medium
  ^MT094-C18-X1

### C19
- **Brad Gerstner** ByteDance trades near $300bn secondary but many see $800bn-1tn, so a TikTok deal unlocks hundreds of billions of venture DPI as a condition to take ByteDance out; TikTok US is about 10% of value.  #mech/structural_shift _(time-bound view)_
  > although it only trades at let's call it 300 billion most people think the fair value of this is closer to a trillion dollars are certainly to 800 billion
  indicator: ByteDance valuation · asset: equities · horizon: years · testable: no: valuation view · confidence: low
  ^MT094-C19-1
- **Brad Gerstner** The TikTok US valuation may be low because Trump negotiates (sovereign wealth fund mention) and must clear Oracle audit of the algorithm.  #mech/policy_reaction _(time-bound view)_
  > I'm hearing that the valuation for Tik Tok US could be pretty low, which I would expect
  asset: equities · horizon: weeks · testable: no: rumor · confidence: low
  ^MT094-C19-2
- **Brad Gerstner** The reported breakthrough is that TikTok US licenses the same global algorithm, because ByteDance had said the algorithm cannot be split and would sooner shut down US TikTok than separate it.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > this idea that US Tik Tok um and global Tik Tok will continue to use the same algorithm and it's just a license to the US Tik Tok
  indicator: TikTok US license of ByteDance algorithm · asset: equities · direction: deal becomes feasible · conditions: Algorithm shared between US and rest of world · testable: no - negotiation detail · confidence: low
  ^MT094-C19-X1

### C20
- **Brad Gerstner** After 54% tariffs, China could block the TikTok deal, so an announced deal is not done.  #mech/policy_reaction _(time-bound view)_
  > and the Chinese government could probably block the deal
  asset: multi · horizon: weeks · testable: no: forecast · confidence: medium
  ^MT094-C20-1
- **Bill Gurley** 54% tariffs on China will not stay because cooperation is too important (Ukraine, Middle East) and the president likes dealmaking with Xi.  #mech/policy_reaction _(time-bound view)_
  > Um I don't believe we're going to have 54% tariffs against China.
  indicator: US tariff on China · asset: multi · direction: tariff de-escalation · horizon: months · testable: no: forecast · confidence: medium
  ^MT094-C20-2
- **Bill Gurley** US-China bilateral trade relations will dictate the direction of global and both countries' growth for the next few years.  #mech/structural_shift _(time-bound view)_
  > the most important thing that matters is USChina bilateral trade relations
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT094-C20-3
- **Brad Gerstner** For ByteDance shareholders the dilution from creating TikTok US is small relative to total company value (about 90% of value is outside TikTok US), so what matters is certainty of a deal.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > whatever the delilution is caused by this, it's nominal relative to the value of the total
  indicator: ByteDance shareholder dilution · asset: equities · conditions: Deal approved by China · testable: partly - depends on final ownership terms · confidence: medium
  ^MT094-C20-X1

