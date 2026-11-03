---
source_id: MT032
title: "China Open-Source, Compute Arms Race, Reordering Global Trade - BG2 w- Bill Gurley and Brad Gerstner"
date: 2025-07-31
channel: "Bg2 Pod"
url: https://www.youtube.com/watch?v=fTqINzeudJ4
words: 11742
claims: 71
added_by_opus: 6
corrections: 1
crosscheck: "opus cross-check"
speakers: ["Brad Gerstner (host, Altimeter Capital)", "Bill Gurley (co-host, investor)", "Sunny Madra (guest, COO of Groq)"]
tags: [source, layer0]
---
# China Open-Source, Compute Arms Race, Reordering Global Trade - BG2 w- Bill Gurley and Brad Gerstner

**Speakers:** Brad Gerstner (host, Altimeter Capital); Bill Gurley (co-host, investor); Sunny Madra (guest, COO of Groq)

**Summary:** BG2 episode on China's open-source AI lead, the compute arms race and AI funding/pricing, then tariffs. Gerstner argues the Bessent tariff path (about $300B) is working, markets are at highs, and a big China deal is coming.

**Approach:** AI industry structure, tariffs and trade policy, market sentiment, venture/private valuations

**Opus completeness estimate of first read:** 0.91 - first reader covered nearly all AI and tariff claims; missed Jevons demand effect, pricing-model shift, tariff pass-through caveat, the rate-cut flight path and the DeepSeek market reaction

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | tariff deals (EU, Japan), intro, guest, AI summit and crypto policy |
| C02 | 6 | US regulation, China open-source dominance, compounding and distillation |
| C03 | 3 | reasoning models with tools; China open source history |
| C04 | 3 | Chinese co-evolution, farmers analogy, AI Action Plan open source |
| C05 | 4 | price-performance of Chinese models, US open-source prediction, commoditization |
| C06 | 3 | US open-source entrants, brand and liability, OpenAI open model |
| C07 | 3 | Meta, values vs price, Chinese release speed, xAI open source |
| C08 | 5 | compute arms race, token growth, funding rounds |
| C09 | 5 | private vs public risk appetite, capex split, token demand |
| C10 | 5 | pricing below cost, price curve, cost optimization, open-source use by coding agents |
| C11 | 3 | subsidy strategy, capital market dependence, Google TPU |
| C12 | 4 | OpenAI lock-in, consumer battle, model commoditization |
| C13 | 4 | AI market structure; Liberation Day market reaction; consensus on tariffs |
| C14 | 3 | Bessent tariff theory, import prices, tariff revenue |
| C15 | 6 | tariff surplus, inflation watch, GDPNow, onshoring, adaptive policy |
| C16 | 4 | China deal view, trade data, rare earth retaliation |
| C17 | 3 | China deal, Gerstner positioning and market outlook, outro |

## Claims

### C01
- **Brad Gerstner** US tariff threats produced trade deals (EU 15% in, 0% out plus $750B energy purchases; Japan $550B investment) rather than retaliation, so consensus fears of trade war were too pessimistic.  #mech/policy_reaction _(time-bound view)_
  > Everybody said this was going to lead to retaliation to trade wars was going to be disastrous for the US and all we've seen so far is deals deals deals deals.
  indicator: tariff deals · asset: multi · horizon: months · conditions: mid-2025 · testable: partly - outcome observed over one half-year · confidence: high
  ^MT032-C01-1

### C02
- **Brad Gerstner** Excess US regulation of energy, model development and chip distribution was an unforced error that gave China momentum in AI.  #mech/policy_reaction _(time-bound view)_
  > excess regulation on everything from energy production to model development to semiconductor chip distribution.
  asset: equities · horizon: years · testable: no - qualitative · confidence: medium
  ^MT032-C02-1
- **Brad Gerstner** China leads global open-source AI models (six to seven high-quality providers; Qwen over 400M downloads) while Llama 4 is sputtering.  #mech/structural_shift _(time-bound view)_
  > they're dominating the global landscape for open-source models.
  indicator: open-source model downloads and rankings · asset: equities · horizon: months · testable: partly - download/leaderboard data · confidence: high
  ^MT032-C02-2
- **Sunny Madra** Open weights let Chinese labs build on, distill and remix each other's work, speeding progress without separate giant training clusters.  #mech/structural_shift
  > they're able to compound. So what you're seeing very quickly is both the open- source nature, the open weights nature, uh, allow them to basically compound on each other.
  indicator: open-weight model releases · asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT032-C02-3
- **Sunny Madra** Leading models are distilled to small, cheap models fast: a 30B-parameter Qwen matched GPT-4o performance.  #mech/structural_shift _(time-bound view)_
  > There was a a release today of a quen you know 30 billion parameter model which is performing as good as GPT40.
  indicator: model size vs benchmark performance · asset: equities · horizon: months · testable: yes - benchmark data · confidence: high
  ^MT032-C02-4
- **Sunny Madra** China's weaker IP and copyright stance lets its model makers train on copyrighted data freely, an advantage over US labs.  #mech/structural_shift
  > the Chinese just have been able to work around that because of, you know, their position on IP.
  asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C02-5
- **Brad Gerstner** Prediction that Chinese open-source models may pass the best US proprietary models by Q4 2025.  #mech/cycle_persistence _(time-bound view)_
  > this might allow them to pass the best proprietary models coming out of the US um yet this year, maybe by Q4 of this year.
  asset: equities · horizon: months · testable: partly - resolvable by leaderboard · confidence: low
  **Correction (Opus):** Wrong speaker: Gerstner is relaying Sunny Madra's tweet; the prediction is Madra's. → Sunny Madra (via Gerstner) suggested Chinese open-source models, by compounding on each other, may pass the best US proprietary models by Q4 2025.
  ^MT032-C02-6
- **Brad Gerstner** A Chinese AI efficiency breakthrough (DeepSeek) triggered a sharp sell-off in AI hardware leaders such as Nvidia, showing the sector's sensitivity to signs that frontier AI can be built cheaply.  #mech/overshoot _(added by Opus, time-bound view)_
  > we had this freakout moment earlier in the year with Deepseek that we all remember. [L60] Remember, Nvidia stock plummets.
  asset: equities · direction: AI hardware stocks down on cheap-AI news · horizon: days · testable: partly - event study on a single episode · confidence: medium
  ^MT032-C02-X1

### C03
- **Brad Gerstner** Models that use tools (web search) need not compress the whole internet, so reasoning models shift the open vs closed balance and cut the size and cost needed.  #mech/structural_shift
  > we've trained them to use tools like the internet, right? The they're true reasoning engines.
  asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT032-C03-1
- **Sunny Madra** Reasoning models coupled with tools perform better than benchmarks show because benchmarks do not allow tool use.  #mech/research_method
  > and once they're coupled with strong tools you start getting these really really incredible results that don't even just show up in benchmarks
  indicator: AI benchmarks · asset: equities · testable: partly · confidence: medium
  ^MT032-C03-2
- **Bill Gurley** China's long embrace of open source (Linux) and weaker IP protection made open-weights AI a natural strategy.  #mech/structural_shift
  > China got excited about open source about 20 years ago.
  asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C03-3

### C04
- **Bill Gurley** Seven or eight well-funded Chinese open-model labs co-evolve fast through distillation, producing quick progress unlike software competition.  #mech/structural_shift
  > when you have a competitive dynamic where every single player, and I think there may be seven or eight deep pocketed players with open models in China, they they all learn from each other extremely fast.
  asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT032-C04-1
- **Bill Gurley** Shared best practices (open source) give a community higher output and less chance of a breakout monopolist than closed competition.  #mech/structural_shift
  > the community where the best practices are shared across all farms is going to have a higher global output for the community than the one where you've just got proprietary ideas
  asset: equities · horizon: years · testable: no - analogy · confidence: medium
  ^MT032-C04-2
- **Brad Gerstner** The US AI Action Plan (July 2025) encourages open-source/open-weight US models; China responded with a call for a global AI cooperation organization.  #mech/policy_reaction _(time-bound view)_
  > had a section they did which which is about encouraging open-source and open weight models in the US
  asset: equities · horizon: months · testable: no · confidence: high
  ^MT032-C04-3

### C05
- **Sunny Madra** Leading Chinese open models offer about 90% of frontier intelligence at about a 90% lower price, driving demand from developers and enterprises.  #mech/structural_shift _(time-bound view)_
  > is 90% of the quality in terms of intelligence, but at a 90% price discount.
  indicator: intelligence vs price per million tokens · asset: equities · horizon: months · testable: yes - price/performance data · confidence: high
  ^MT032-C05-1
- **Sunny Madra** Enterprises want an accountable vendor for open-source software (Red Hat for Linux), so a US-domiciled open model company could win.  #mech/structural_shift
  > They want some accountability. And that's what you'll get. That's what you sort of got out of Linux and say Red Hat, right?
  asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C05-2
- **Sunny Madra** Prediction: by Q4 2025 or Q1 2026 a top-three model worldwide will be a US-based open source model (OpenAI open model, Meta).  #mech/cycle_persistence _(time-bound view)_
  > I'd be willing to say, you know, the a top three worldwide model will be a US-based open source model.
  asset: equities · horizon: months · testable: partly - resolvable · confidence: medium
  ^MT032-C05-3
- **Bill Gurley** Large tech firms that are not winning on offense fund open source to commoditize a rival (Facebook Open Compute; Alibaba funding Zhipu).  #mech/structural_shift
  > And so for any large tech company, commoditizing a a potential threat is is actually quite valuable.
  asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C05-4

### C06
- **Bill Gurley** Laggard big tech (Microsoft, Amazon, Apple) should fund open-source competitors instead of backing a proprietary lab.  #mech/structural_shift
  > if I'm at any of those companies, I'd be funding a open-source competitor
  asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C06-1
- **Bill Gurley** New US entrants can start from Chinese open models and reach near-frontier quality without frontier-lab spending, and regulatory capture fights may follow.  #mech/structural_shift _(time-bound view)_
  > if you start with access to those Chinese models it wouldn't take you long to move into a near place and you wouldn't have to spend the kind of money the foundational model companies have.
  asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C06-2
- **Sunny Madra** Enterprises pick a US-domiciled, liable provider when capability and price are equal, so a competitive US open model would win share back.  #mech/behavioral
  > two things that we see is brand and you know the US doiciled or you know someone that they can kind of point at that wins
  asset: equities · horizon: months · conditions: if price/performance equal · testable: no · confidence: medium
  ^MT032-C06-3

### C07
- **Bill Gurley** Meta is likely to stay open-source while adding a proprietary model.  #mech/policy_reaction _(time-bound view)_
  > My hunch is that they're going to stay very committed to open source, but they may complement it with a proprietary model.
  asset: equities · horizon: months · testable: no · confidence: low
  ^MT032-C07-1
- **Brad Gerstner** Global buyers choose cheap powerful models over values-aligned ones, but a model that is both would top the leaderboards.  #mech/behavioral
  > So it turns out if you deliver something really powerful and really cheap that's more important to these players than American values aligned.
  asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT032-C07-2
- **Brad Gerstner** Chinese open-source release cadence and quality now exceeds the US open-source ecosystem.  #mech/structural_shift _(time-bound view)_
  > the cycle time on the innovation in the open source community out of China. It's faster and better at the moment.
  indicator: model release cadence · asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT032-C07-3

### C08
- **Brad Gerstner** xAI's goal of 50 million H100-equivalents (about 4M GPUs, 11 GW) and OpenAI's 4.5 GW Abilene deal show planned compute is far larger than a year ago.  #mech/liquidity_flows _(time-bound view)_
  > If you look at this one out of Elon talking about the X.AI AI goal is 50 million in units of H100 equivalent.
  indicator: planned GPU capacity (H100 equivalents, GW) · asset: equities · horizon: years · testable: partly - announced vs built · confidence: medium
  ^MT032-C08-1
- **Brad Gerstner** Inference-time reasoning and agent-to-agent interaction raise compute demand, refuting the earlier overbuild (Cisco 2000) concern.  #mech/structural_shift _(time-bound view)_
  > So these compute clusters now that are being talked about being built over the next 5 years, these are massively bigger than what we were even talking about a year ago.
  indicator: compute demand · asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT032-C08-2
- **Sunny Madra** Google's monthly tokens grew from 5T to 480T and then above 1 quadrillion, about 200x in a little over a year.  #mech/structural_shift _(time-bound view)_
  > Google went from 5 trillion tokens a month to 480 trillion tokens a month.
  indicator: tokens per month · asset: equities · horizon: months · testable: yes - company disclosures · confidence: high
  ^MT032-C08-3
- **Sunny Madra** Groq inference capacity is fully consumed within hours of deployment, so demand outstrips supply.  #mech/structural_shift _(time-bound view)_
  > anywhere we lay infrastructure um we fire up a rack it becomes fully consumed within a few hours.
  indicator: inference utilization · asset: equities · horizon: months · testable: partly - anecdote · confidence: medium
  ^MT032-C08-4
- **Brad Gerstner** AI lab funding rounds (Anthropic about $170B on about $5B revenue, xAI $150-200B) are unprecedented in venture history, with option dilution debated.  #mech/crowding_positioning _(time-bound view)_
  > In the case of Anthropic, it's, you know, uh 170 billion on rumored $5 billion in revenue.
  indicator: private AI valuations / revenue · asset: equities · horizon: months · testable: yes - round data · confidence: medium
  ^MT032-C08-5
- **Sunny Madra** Search queries have turned into AI inference transactions, so ordinary search volume now feeds directly into compute demand.  #mech/structural_shift _(added by Opus)_
  > every single search query on the planet today is now an inference transaction. Correct.
  indicator: AI tokens processed per month · asset: equities · direction: compute demand up · horizon: years · testable: partly - token counts are disclosed sporadically · confidence: high
  ^MT032-C08-X1

### C09
- **Bill Gurley** Private labs can lose money (OpenAI about $7B a year) that public companies like Google would not allow, a new competitive advantage.  #mech/structural_shift
  > for the first time ever you saw private companies have a competitive advantage and that they can be more risk-seeking with capital than the public companies are allowed to be.
  indicator: cash burn · asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT032-C09-1
- **Bill Gurley** OpenAI, Meta and X form a cost-is-no-object spending group while Microsoft and Amazon hold back capex, leaving a split in AI investment intensity.  #mech/crowding_positioning _(time-bound view)_
  > the cost is no object the CNO group
  indicator: AI capex by company · asset: equities · horizon: months · testable: yes - capex data · confidence: medium
  ^MT032-C09-2
- **Bill Gurley** Nvidia, Dell and possibly SK Hynix are the winners of AI capex as suppliers.  #mech/structural_shift _(time-bound view)_
  > they're the winners um in a pick and shovel game that's got this amount of aggressiveness.
  indicator: Nvidia; Dell; SK Hynix · asset: equities · direction: long AI hardware suppliers · horizon: months · testable: partly · confidence: medium
  ^MT032-C09-3
- **Bill Gurley** Reasoning models consume 10-100x more tokens per query, a driver of token growth.  #mech/structural_shift
  > 10 to 100x more than the your very first AI search.
  indicator: tokens per query · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT032-C09-4
- **Sunny Madra** Anthropic throttling users shows demand exceeds supply and no evidence yet of oversupply.  #mech/liquidity_flows _(time-bound view)_
  > Anthropic had to put this uh you know, press release plus, you know, product change out saying
  asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT032-C09-5

### C10
- **Bill Gurley** AI model companies price below cost for market share, with rumors of negative gross margin, so a repricing would create a bump in supply and demand when it ends.  #mech/risk_management
  > And so everyone's pricing to share. That means they're pricing under cost.
  indicator: AI gross margins · asset: equities · horizon: months · conditions: funding available · testable: partly · confidence: medium
  ^MT032-C10-1
- **Bill Gurley** Compute scarcity could be solved by raising price, but vendors fear losing share, so shortage is partly artificial.  #mech/liquidity_flows
  > like the thing that throttles demand is price, but no one here is raising price.
  indicator: AI pricing · asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT032-C10-2
- **Brad Gerstner** Prices fall very steeply for older model generations, so users can switch to older or cheaper models to cut losses.  #mech/structural_shift
  > the steepness of that price curve on you know as you as it kind of becomes you know less less cutting edge is something I've never seen before.
  indicator: price per token by model age · asset: equities · horizon: months · testable: yes · confidence: high
  ^MT032-C10-3
- **Brad Gerstner** Analogy: startups first win at all cost, then optimize cost with open source; AI inference users are starting to optimize cost now.  #mech/cycle_persistence
  > in the internet age all the startups began with Oracle and Sun and eventually they all moved to Linux and MySQL.
  asset: equities · horizon: years · testable: no - analogy · confidence: medium
  ^MT032-C10-4
- **Sunny Madra** Coding-agent companies can distill open models under Apache licenses to replace expensive proprietary APIs for most use cases.  #mech/structural_shift
  > multiple folks are building their own models uh based off open source
  asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT032-C10-5
- **Sunny Madra** Jevons paradox: as AI capacity grows and intelligence gets cheaper, total token consumption rises rather than falls, so efficiency gains do not reduce compute demand.  #mech/structural_shift _(added by Opus)_
  > models right and you have the capacity for it it's one of those things people are consuming Jven's paradox or whatever.
  indicator: token consumption vs price per token · asset: equities · direction: compute demand up as unit cost falls · horizon: years · testable: partly - token volume and price series are partial · confidence: medium
  ^MT032-C10-X1

### C11
- **Brad Gerstner** OpenAI can use its high-margin consumer business to subsidize a cheap open model for price-sensitive coding workloads, as Amazon did with AWS.  #mech/structural_shift
  > Amazon had this monopoly retail business they could use to subsidize AWS gain share for a decade and then begin to take price.
  indicator: gross margin by segment · asset: equities · horizon: years · testable: no - strategy argument · confidence: medium
  ^MT032-C11-1
- **Bill Gurley** Share-seeking labs depend on capital markets and funding can disappear quickly, so labs without consumer products are vulnerable.  #mech/risk_management
  > they all exist at the beneficence of the capital markets and the capital markets are willing to provide an incredible amount of capital to these businesses today.
  indicator: funding conditions · asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C11-2
- **Bill Gurley** Google's TPU advantage depends on third-party use, as most TPU volume is internal.  #mech/structural_shift
  > how many non-G Google uh applications are running on the TPUs like how many third party customers are using
  indicator: third-party TPU customers · asset: equities · horizon: years · testable: partly - data not public · confidence: medium
  ^MT032-C11-3
- **Bill Gurley** AI pricing will rationalize from flat subscriptions toward consumption-based pricing with automatic routing to cheaper models, which improves lab economics (already happening in enterprise).  #mech/structural_shift _(added by Opus)_
  > I do think there'll be some rationalization where these models um kind of self-pick which one they're running based on what you need.
  asset: equities · horizon: years · testable: no - business-model forecast · confidence: medium
  ^MT032-C11-X1

### C12
- **Bill Gurley** User memory and history create switching costs and pricing power for ChatGPT even if models commoditize.  #mech/structural_shift
  > OpenAI's um most likely chance to long-term um success comes from switching cost and lock in more than it will come from staying on the edge of the of the model race
  asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C12-1
- **Brad Gerstner** Value accrues to whoever owns the consumer (as Google search did for 20 years), and ChatGPT is the first real threat.  #mech/structural_shift
  > the battle for the consumer is ultimately where the value occurs, Sunny, not who runs, you know, what hardware.
  asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C12-2
- **Brad Gerstner** Open-source distillation drives intelligence up and cost down, so model value shifts to applications.  #mech/structural_shift
  > the model layer is being increasingly commoditized and that there's not going to be a lot of intrinsic value in in in that intelligence layer
  asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C12-3
- **Brad Gerstner** ChatGPT may exceed one billion weekly users in 2025.  #mech/structural_shift _(time-bound view)_
  > I think chat GBT will cross a billion weeklys like maybe this year.
  indicator: ChatGPT weekly users · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT032-C12-4

### C13
- **Brad Gerstner** AI will be a heterogeneous market with many competitors and lower margins, yet a rising tide lets many do well; OpenAI plus Anthropic are worth over $500B.  #mech/structural_shift _(time-bound view)_
  > I think they're going to be lots of players that compete. I think the margins will be lower.
  indicator: AI enterprise values · asset: equities · horizon: years · testable: no · confidence: medium
  ^MT032-C13-1
- **Brad Gerstner** Markets sold off on Liberation Day because tariff outcomes ranged from about $300B (Bessent/Lutnick) to $2T (Navarro) and risk was unpriceable.  #mech/policy_reaction _(time-bound view)_
  > We all voted with our wallets and we said until the president tells us whether it's door one or door two, we're out.
  indicator: tariff policy uncertainty · asset: equities · direction: exit equities when policy range is wide · horizon: weeks · testable: partly · confidence: high
  ^MT032-C13-2
- **Brad Gerstner** The Nasdaq fell 21% at the April trough then rose over 30% in 60-70 days once the lower tariff path became clear.  #mech/overshoot _(time-bound view)_
  > The NASDAQ was down 21% right at its trough this year.
  indicator: Nasdaq · asset: equities · horizon: weeks · conditions: after policy uncertainty resolves · testable: yes · confidence: high
  ^MT032-C13-3
- **Brad Gerstner** Consensus (about 90% of economists) expected tariffs to be a tax paid by US consumers and cause inflation.  #mech/policy_reaction _(time-bound view)_
  > I think the consensus view of all economists, right, 90% of economists is that tariffs are going to be bad.
  indicator: consensus inflation forecast · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT032-C13-4

### C14
- **Brad Gerstner** Bessent/Hassett theory: because exporters depend on the US market (deficit about $1.2T in goods), modest tariffs are absorbed by foreign producers.  #mech/policy_reaction _(time-bound view)_
  > if we impose a 15% tariff on them they have to eat it the producers have to eat it because otherwise they're going end up laying off millions of people
  indicator: US trade deficit; tariff pass-through · asset: multi · horizon: months · conditions: tariff not draconian (about 15% not 70-80%) · testable: yes - import price pass-through can be measured · confidence: medium
  ^MT032-C14-1
- **Brad Gerstner** NEC analysis of core PCE shows import prices rising slower than domestic goods, with no pass-through of tariffs yet, though inflation could still come.  #mech/policy_reaction _(time-bound view)_
  > Import prices have been going up at a slower rate than domestically produced goods.
  indicator: core PCE; import prices vs domestic goods prices · asset: multi · horizon: months · conditions: as of July 2025, 'yet' caveat · testable: yes · confidence: medium
  ^MT032-C14-2
- **Brad Gerstner** Tariffs create about $300-350B a year in Treasury revenue, relevant to deficits.  #mech/fiscal_debt _(time-bound view)_
  > and the fact that we now have a 300 to a $350 billion recurring, you know, stream of revenues into Treasury in the form of these tariffs which are being paid.
  indicator: tariff revenue · asset: rates · horizon: years · testable: yes · confidence: medium
  ^MT032-C14-3

### C15
- **Brad Gerstner** June 2025 produced the first monthly US budget surplus since 2015 due to tariff revenue.  #mech/fiscal_debt _(time-bound view)_
  > the month of June we had our first surplus in the United States monthly surplus since 2015 right because of the tariff revenues that are coming in.
  indicator: monthly US budget balance · asset: rates · horizon: months · testable: yes · confidence: medium
  ^MT032-C15-1
- **Brad Gerstner** Core PCE bottomed in 2024 and is rising, so tariff pass-through risk requires monitoring.  #mech/policy_reaction _(time-bound view)_
  > core PCE h did bottom last year and it started to tick up and so we have to keep our eye on inflation.
  indicator: core PCE · asset: rates · horizon: months · testable: yes · confidence: medium
  ^MT032-C15-2
- **Brad Gerstner** The Atlanta Fed GDPNow rebounded to 3% after April's drop, supporting the view tariffs did not hurt activity.  #mech/cycle_persistence _(time-bound view)_
  > the Atlanta now Fed tracker which tracks real-time GDP has now ticked up back to 3%.
  indicator: Atlanta Fed GDPNow · asset: equities · horizon: weeks · testable: yes · confidence: high
  ^MT032-C15-3
- **Brad Gerstner** Market prices are a better read of tariff policy than economist warnings (Summers called it a disaster).  #mech/behavioral _(time-bound view)_
  > The voting machine is telling you that no retaliations, no trade wars, all these deals getting done um uh works for the US economy.
  indicator: equity index vs consensus · asset: equities · horizon: months · testable: no · confidence: medium
  ^MT032-C15-4
- **Brad Gerstner** Tariffs make US onshoring (rare earth magnets, chips, data centers, energy) investable.  #mech/structural_shift
  > these are now viable investments because of the tariffs and the resolve of the government to reonshore these critical supply chains.
  asset: equities · direction: long onshoring beneficiaries · horizon: years · testable: no · confidence: medium
  ^MT032-C15-5
- **Sunny Madra** The administration revised the tariff schedule six to eight times after supplier feedback, making policy adaptive and uncertainty decay.  #mech/policy_reaction _(time-bound view)_
  > we've seen you know our tariff schedule move around probably six to eight times since this all has started
  asset: multi · horizon: months · testable: no · confidence: medium
  ^MT032-C15-6
- **Brad Gerstner** Caveat: some tariffs will be passed through to US consumers on specific goods, and the schedule will need corrections, even if overall pass-through is small.  #mech/policy_reaction _(added by Opus, time-bound view)_
  > So, we're going to have some some goods and some products that, you know, consumers are US consumers are going to end up paying the taxes and we're going to have to go back and fix some of these things.
  indicator: goods-level import price inflation · asset: multi · direction: some consumer prices up · horizon: months · conditions: goods without quick substitutes · testable: yes - goods-level CPI/PCE vs tariff exposure · confidence: medium
  ^MT032-C15-X1

### C16
- **Brad Gerstner** View that a large US-China deal (rare earths, chips, trade rebalancing) is coming and consensus underestimates it.  #mech/policy_reaction _(time-bound view)_
  > I think this president wants to do the biggest deal ever done with China.
  indicator: US-China trade negotiation · asset: multi · horizon: months · testable: no · confidence: medium
  ^MT032-C16-1
- **Brad Gerstner** The EU and China each represent a roughly $300B US goods deficit, so they were the key targets.  #mech/structural_shift
  > we do, I think, $900 billion of trade with them a year. With China, it's about 600 billion, but we have about a $300 billion goods trade deficit with both Europe and China.
  indicator: US goods trade deficit by partner · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT032-C16-2
- **Brad Gerstner** China's rare earth ban and the US H20 chip cutoff show retaliation channels that create supply-chain risk.  #mech/policy_reaction _(time-bound view)_
  > the rare earth ban on Chinese magnets was devastating to US industry.
  indicator: rare earth exports · asset: multi · horizon: months · testable: partly · confidence: high
  ^MT032-C16-3
- **Brad Gerstner** Expected US tariff on China floor of 15% (the pre-Trump rate plus), with a more structured deal.  #mech/policy_reaction _(time-bound view)_
  > I don't think we're going below 15%.
  indicator: US tariff rate on China · asset: multi · horizon: months · testable: partly · confidence: low
  ^MT032-C16-4

### C17
- **Brad Gerstner** China must rebalance toward domestic consumption over years, and a large US-China deal before year-end would lift markets.  #mech/policy_reaction _(time-bound view)_
  > I think that there's going to be a big Chinese deal done before the year's out.
  indicator: US-China deal · asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT032-C17-1
- **Brad Gerstner** Altimeter went out of equities in March and back in May 2nd once the Bessent 300B tariff path won, getting the Nasdaq rebound.  #mech/behavioral _(time-bound view)_
  > On May 2nd, I said we're all we're all back in because the Bessant consensus has won.
  asset: equities · horizon: weeks · testable: no - single anecdote · confidence: medium
  ^MT032-C17-2
- **Brad Gerstner** With S&P and Nasdaq up about 10% YTD and a 15% year target, much of the 2025 return was already captured, though AI opportunities remain.  #mech/cycle_persistence _(time-bound view)_
  > I would have said the market can be up at least 15% for the year I think we've captured a lot of the return for the for the year
  asset: equities · horizon: months · testable: no · confidence: low
  ^MT032-C17-3
- **Brad Gerstner** Gerstner's 2025 flight path: tariffs landing near $300B with no inflation lets the Fed cut rates by year-end while growth accelerates near 3%, which is bullish for equities.  #mech/policy_reaction _(added by Opus, time-bound view)_
  > I said you can land the plane, no inflation, you get rate cuts and you know, and it's kind of off to the races.
  indicator: core PCE, Fed funds path, GDPNow · asset: multi · direction: long equities; rates lower · horizon: months · conditions: tariffs stay near $300B and inflation stays contained · testable: partly - scenario call, outcome checkable · confidence: high
  ^MT032-C17-X1

