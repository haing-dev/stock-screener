---
tags: [fable, charter]
step: 1.2
inputs: _data/charter_1.2/
code_commit: 52a6a58
---
> Fable 5.2 max, one run; the 24 corrections of the independent check are applied. Full claim ids link to the verbatim quote in its source note; code refs link to GitHub at commit 52a6a58. Exact input pack, briefs and the original Fable text: `_data/charter_1.2/`. See also [[Charter 1.2 - Systematic charter]], [[Charter 1.2 - Independent check]], [[WORKFLOW]].
# Systematic charter (WORKFLOW step 1.2)

Fable 5.2, 2026-11-13. Inputs: every file in charter_1.2/pack and the repo, read only. No code was run, no return
or price was loaded, nothing from 2011-2026 was looked at.

Labels: SHOWN = the source gives a test with numbers ("described" = only told on air); ASSERTED = no test; reader =
my inference. Claim text = the pack's machine summary of a quote; a test known only through claim text or the blog
digest is "summary only" and is not labelled SHOWN (v2 rule 2). Claim ids are as the notes write them: a bare Cxx-n
takes the prefix of the id before it; U01's ids take the prefix [[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)|QP01]]; B01-B31 are the Carver blog digest. Repo line
numbers are today's (gm-1.2.1). Terms: a pod is one way of making money with its own rules and record; a version is
one variant of a pod's rule (versions are averaged, never picked); Sharpe = return per unit of risk; design data =
1975-2010; hygiene = a change for robustness, cost, risk or breadth, which must not hurt (Batch A); B1 and B2 = the
two batches of new pods; Core = a pod in the traded book; Incubator = a pod in shadow (forecasts logged, no
trades); spec = a pod's written rule sheet; net = after costs; BASE = the live paper book; CANDIDATE = the
incumbent that tests are measured against ([TESTING_PROTOCOL.md:8](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/TESTING_PROTOCOL.md#L8)).

> **Status (2026-11-13): PASS WITH CORRECTIONS.** Written by one Fable 5.2 run (effort max) from the seven foundation
> notes, then checked by an independent Opus 5.5 run against the verbatim quotes, the code, and two sources the author
> did not see (Eckhardt [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10|MT020]]; Fung and Hsieh 2001). The 24 corrections the check required are applied in this text;
> the check itself is `CHARTER_1.2_check.md`, its summary is section 11. The original Fable text, the exact input pack
> and both briefs are on the macro-vault branch, `pipeline/charter_1.2/`. Nothing here is registered or run: grids,
> diagnostics and items are registered at WORKFLOW step 3.4, before any run. Section 1 is the author's verdict as
> written; where the check changed a label (rows 1, 6, 7, 9 are no longer SHOWN), the tables below carry the change.

## 1. Verdict

The notes agree, mostly by assertion, on how to build trend: size by volatility, mix speeds, count price drivers
not markets, never time it. They do not establish why trends exist (four mechanisms conflict). Tests with numbers
come from one paper (U01), one blog (U02) and studies only described on air. Pods: Trend, Economic trend, Carry,
Value (existing book) and Curve carry (new, B1); the notes give no thesis for Carry or Value. Versions to average:
16, 2, 2, 1 and 2, each in four weekly tranches. The one pass has six diagnostics. It decides three Batch A items
(new commodity markets, a no-trade buffer, a faster book scaler) and four lines in pod specs, and adopts nothing;
the other 26 proposals are folded in or dropped. Largest unverified dependency: the one new pod rests on a seller's
unshown claims (U04). Rule 5 is open: no note dates a thesis before 2011; Economic trend's sources are 2017 and 2023.

## 2. Established vs asserted

Most important first. "Unverified" = not checked against quotes; "audit" = pack/AUDIT_1.1.md.

| # | Statement | Label | Sources | Agreement | Audit status |
|---|---|---|---|---|---|
| 1 | Sizing positions by current volatility gives a higher Sharpe than sizing fixed at entry, and gives up part of long moves. | ASSERTED for the Sharpe gain (summary only: U02 [[Carver blog digest#^B22|B22]]); the U03 described study (Quantica) gives long-volatility correlation and volatility ratios, not Sharpe | U03 [[MT195 - Trend Following in 2025- New Challenges, New Strategies! - Systematic Investor 326#^MT195-C07-4|MT195-C07-4]], C08-1, C08-2, C08-5; U02 [[Carver blog digest#^B22|B22]], [[Carver blog digest#^B31|B31]]; U04 [[MT009 - AI Can Build Your Portfolio—But Can You Trust It- - Systematic Investor - Ep.419#^MT009-C07-4|MT009-C07-4]]; U05 [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C15-1|MT192-C15-1]]; U06 [[MT158 - Taking the Trend Following Temperature - Systematic Investor 304#^MT158-C02-2|MT158-C02-2]] | U04-U06 quotes assert the practice, not a Sharpe gain; only U03 weighs the lost capture (static: '40% or higher' long-vol correlation, [[MT195 - Trend Following in 2025- New Challenges, New Strategies! - Systematic Investor 326#^MT195-C08-2|MT195-C08-2]]). Which estimator speed wins depends on the path (U03 [[MT042 - Diversification is more important than ever! - Systematic Investor - Ep.385#^MT042-C12-4|MT042-C12-4]], C12-5). | Substance confirmed, grade moderate; comparison corrected to [[Carver blog digest#^B22|B22]]'s 1.15 against 0.88 |
| 2 | Trend pays late: it loses or earns nothing at the start of an equity fall and pays only if the move lasts weeks to months. | SHOWN (described) | U03 [[MT194 - Trend Following during Trump Tariff Turmoil! - Systematic Investor 344#^MT194-C06-2|MT194-C06-2]], C06-4; U04 [[MT039 - Crowded Trades, Fluctuating Markets- Navigating the New Era of Investing - Systematic Inve#^MT039-C17-3|MT039-C17-3]], C17-4; U05 [[MT205 - Unpacking the Chaos- What Today’s Market Signals Really Mean - Systematic Investor 343#^MT205-C08-1|MT205-C08-1]]; U06 [[MT014 - Adapt or Perish- Why Systematic Investors Must Evolve in 2024 - Systematic Investor 325#^MT014-C06-5|MT014-C06-5]], C06-6 | Agree; "neutral" (U06) or "negative first" (U03; U05's [[MT205 - Unpacking the Chaos- What Today’s Market Signals Really Mean - Systematic Investor 343#^MT205-C08-1|MT205-C08-1]] says 'negative skew there', claim text: day to day) depends on prior positions | Unverified |
| 3 | No trend speed can be chosen in advance. Reversals hurt every speed, the middle most: 3-6 months (U04), 4-9 months (U03); the reversal link is [[MT042 - Diversification is more important than ever! - Systematic Investor - Ep.385#^MT042-C09-2|MT042-C09-2]] ('this extreme V-shaped move') (numbers in quote). | ASSERTED (desk tables described) | U03 [[MT042 - Diversification is more important than ever! - Systematic Investor - Ep.385#^MT042-C09-1|MT042-C09-1]], [[MT220 - Why Trend Following Never Looks the Same Twice - Systematic Investor - Ep.365#^MT220-C09-1|MT220-C09-1]]; U04 [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-1|MT200-C05-1]], [[MT099 - Major Market Moves for Trend Followers - Systematic Investor 308#^MT099-C10-3|MT099-C10-3]]; U06 [[MT014 - Adapt or Perish- Why Systematic Investors Must Evolve in 2024 - Systematic Investor 325#^MT014-C05-3|MT014-C05-3]]; U07 [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C10-1|MT177-C10-1]] | Agree on "cannot pick". Sources say slow has the higher Sharpe (U03 [[MT021 - Bonds Behaving Badly - Systematic Investor 309#^MT021-C04-2|MT021-C04-2]]; U06 [[MT014 - Adapt or Perish- Why Systematic Investors Must Evolve in 2024 - Systematic Investor 325#^MT014-C05-4|MT014-C05-4]]; U07 [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C08-2|MT177-C08-2]]); our design data say the fast blend ([CHANGES.md:113-116](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L113-L116)). | Unverified; mostly 2022-26 episodes |
| 4 | The form of the trend signal matters little. A stronger forecast says more about direction, but sizing by it adds little over a yes/no position ([[Carver blog digest#^B22|B22]]: 1.18 against 1.15, summary only). | ASSERTED by sources; SHOWN in our log | U04 [[MT131 - Redefining Trend Following - Systematic Investor - Ep.363#^MT131-C07-4|MT131-C07-4]], [[MT116 - Nick Baltas on Trend Following in 2026- Signals, Structure & Strategy - Systematic Investo#^MT116-C12-1|MT116-C12-1]], C12-2, C12-3; U05 [[MT223 - Why Trend Thrives When Inflation Returns - Systematic Investor - Ep.373#^MT223-C15-2|MT223-C15-2]]; U02 [[Carver blog digest#^B04|B04]], [[Carver blog digest#^B22|B22]]; [CHANGES.md:51-61](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L51-L61), 128-131 | Agree that form is second order. Sources prefer a graded signal; in our trial it lost ([CHANGES.md:51-52](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L51-L52)). | Audit: direction moderate, size weak |
| 5 | Diversification comes from independent price drivers, not the number of markets. | ASSERTED (sound as arithmetic; no test) | U05 [[MT205 - Unpacking the Chaos- What Today’s Market Signals Really Mean - Systematic Investor 343#^MT205-C12-2|MT205-C12-2]], C13-1, C13-2; U06 [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C08-2|MT083-C08-2]], [[MT111 - Navigating Market Chaos - Systematic Investor 336#^MT111-C06-1|MT111-C06-1]]; U07 [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-1|MT177-C13-1]]; U02 [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-1|MT026-C16-1]] | Agree. Do more markets still help? Yes: U02 [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-4|MT026-C17-4]] ('correlations ... probably understate the amount of diversification'), U06 [[MT158 - Taking the Trend Following Temperature - Systematic Investor 304#^MT158-C13-4|MT158-C13-4]]. No: U05 [[MT205 - Unpacking the Chaos- What Today’s Market Signals Really Mean - Systematic Investor 343#^MT205-C09-1|MT205-C09-1]]; the host in [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-1|MT026-C17-1]] ('there is no evidence, in my opinion, that'). Carver also: alternatives 'only buys you a little bit more diversification' ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-X1|MT026-C16-X1]]). | Unverified |
| 6 | Markets with local drivers ("alternative") gave a higher long-run trend Sharpe, 0.8-0.9 against 0.5-0.6 (unverified), and a weaker payoff in equity crises. | ASSERTED (numbers hedged: 'maybe 8.9 sharp something like that') | U06 [[MT158 - Taking the Trend Following Temperature - Systematic Investor 304#^MT158-C07-1|MT158-C07-1]], C07-2; [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C06-5|MT083-C06-5]], C07-2; [[MT111 - Navigating Market Chaos - Systematic Investor 336#^MT111-C06-2|MT111-C06-2]], C06-3; U04 [[MT130 - QIS & Trend Following in 2026 ft. Nick Baltas - Systematic Investor - Ep.401#^MT130-C12-2|MT130-C12-2]]; U07 [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-2|MT177-C13-2]] | Agree in direction; U06 gives counter-years ([[MT014 - Adapt or Perish- Why Systematic Investors Must Evolve in 2024 - Systematic Investor 325#^MT014-C16-2|MT014-C16-2]]; [[MT111 - Navigating Market Chaos - Systematic Investor 336#^MT111-C05-2|MT111-C05-2]]; [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-4|MT127-C05-4]]) | Unverified |
| 7 | A book of 12-month changes in five macro themes, signs fixed by theory, earned a Sharpe of 1.1 before costs over 1970-2022; price-built themes (0.77, 0.64, 0.63) beat forecast-built ones (0.26, 0.27) (all unverified). Its stated cause, slow reaction to economic news, is not tested. | Result summary only (Sharpe figures are chart reads in claim text; quotes: 'Hypothetical', 'gross of fees and transaction costs'); cause ASSERTED; U01 reads it as price momentum across assets (reader) | U01 C06-1, C07-2 (summary only), C03-9 (1970-2022), C04-2..C04-5, C06-6; C01-1, C02-3, C04-8 | U03 [[MT042 - Diversification is more important than ever! - Systematic Investor - Ep.385#^MT042-C07-3|MT042-C07-3]], U04 [[MT039 - Crowded Trades, Fluctuating Markets- Navigating the New Era of Investing - Systematic Inve#^MT039-C15-1|MT039-C15-1]]: a complement to trend. U07: a costly null on official data ([[MT070 - Harding Rewrites Winton's Quant Playbook in Search for Returns#^MT070-C04-2|MT070-C04-2]], C04-3). U02 expects high overlap with trend ([[MT144 - Should You Just Buy a CTA Index- - Systematic Investor 312#^MT144-C06-X1|MT144-C06-X1]], C06-2). | Unverified |
| 8 | Why price trends exist: slow recognition of macro change. | ASSERTED | U03 [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C15-1|MT083-C15-1]], [[MT086 - Interest Rates & Trend Following - Systematic Investor 318#^MT086-C04-5|MT086-C04-5]]; U04 [[MT116 - Nick Baltas on Trend Following in 2026- Signals, Structure & Strategy - Systematic Investo#^MT116-C02-1|MT116-C02-1]]; U06 [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C14-3|MT083-C14-3]]; U07 [[QP04 - The Numbers Man David Harding profile (Financial Times, Clive Cookson)#^QP04-C03-8|QP04-C03-8]] | Conflict, not blended: a risk premium (claim text of U02 [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C01-1|MT137-C01-1]]; quote: 'if anyone can do it then you haven't got an edge'); a 'sustained imbalance in the asset class' (U05 [[MT029 - CTAs- The Good, The Bad, & The Misunderstood - Top Traders Unplugged 148#^MT029-C08-1|MT029-C08-1]]), which gives autocorrelation, returns that follow their own past ([[MT024 - Building an Inflation-Proof Portfolio - Systematic Investor - Ep.384#^MT024-C14-2|MT024-C14-2]]: it 'is really important'); volatility clustering, no autocorrelation needed (U04 [[MT116 - Nick Baltas on Trend Following in 2026- Signals, Structure & Strategy - Systematic Investo#^MT116-C14-2|MT116-C14-2]], C15-1) | Unverified |
| 9 | Trend cannot be timed; a low-Sharpe strategy has long drawdowns without being broken. | ASSERTED (U06's 33% drawdown 'spent years in drawdown' is in quote; 'simulation' and its 0.6 Sharpe are claim text, [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C14-1|MT083-C14-1]]) | U06 [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C14-1|MT083-C14-1]], [[MT158 - Taking the Trend Following Temperature - Systematic Investor 304#^MT158-C08-1|MT158-C08-1]]; U02 [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C21-3|MT044-C21-3]]; U03 [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C09-2|MT045-C09-2]]; U04 [[MT087 - Investing in the Age of AI, Uncertainty, and Data Overload - Systematic Investor - Ep.352#^MT087-C14-1|MT087-C14-1]]; U05 [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C03-3|MT073-C03-3]]; U07 [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C06-3|MT177-C06-3]] | Agree; U03's "good years follow bad" ([[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-3|MT221-C11-3]]) conflicts with U02 | Audit: substance agreed; grade moderate or weak, quotes favour neither |
| 10 | Expect a trend Sharpe near 0.5 on liquid markets, about half the past ("nearly one for 30 years") (unverified). | ASSERTED (testimony) | U07 [[MT070 - Harding Rewrites Winton's Quant Playbook in Search for Returns#^MT070-C06-1|MT070-C06-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-1|MT177-C04-1]]; U06 [[MT158 - Taking the Trend Following Temperature - Systematic Investor 304#^MT158-C07-1|MT158-C07-1]]; U05 [[MT192 - Trend Following Still Works — So Why Do Allocators Ignore It- - Systematic Investor - Ep.3#^MT192-C11-3|MT192-C11-3]]; U02 [[Carver blog digest#^B25|B25]] | Agree on the level. Cause: crowding (U07 [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-1|MT177-C19-1]]), environment (U02 [[Carver blog digest#^B25|B25]]), cash rate and leverage (U07 [[MT070 - Harding Rewrites Winton's Quant Playbook in Search for Returns#^MT070-C02-4|MT070-C02-4]]), no rise in the return loading on slow or mid-frequency trend (U05 [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C10-3|MT073-C10-3]]) | Unverified; U02's "0.5-1" is claim text only (audit): not used |
| 11 | Carry beside trend: lowers the crisis payoff (U03 [[MT021 - Bonds Behaving Badly - Systematic Investor 309#^MT021-C13-2|MT021-C13-2]]; U07's quote says only that signals which 'smooth out those drawdowns' have 'Great Value', the crisis cost is claim text); helps if built neutral to the market (U04); has 'horrible left tails' in 'a full liquidity break, a dash for cash' (U06; 'only' and 'carry' are claim text). | ASSERTED | U03 [[MT021 - Bonds Behaving Badly - Systematic Investor 309#^MT021-C13-2|MT021-C13-2]]; U07 [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C05-2|MT177-C05-2]]; U04 [[MT131 - Redefining Trend Following - Systematic Investor - Ep.363#^MT131-C09-1|MT131-C09-1]], [[MT173 - The Negative Crisis Beta and CTA's Hidden Market Timing Skills - Systematic Investor 302#^MT173-C15-X2|MT173-C15-X2]]; U06 [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C05-1|MT083-C05-1]] | Conflict. Our log: carry adds ([CHANGES.md:66](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L66)) | Unverified |
| 12 | Far-dated against near-dated commodity futures earned a steady premium; it loses when a supply shock lifts the near contract. | ASSERTED (by a seller; no Sharpe or cost given) | U04 [[MT130 - QIS & Trend Following in 2026 ft. Nick Baltas - Systematic Investor - Ep.401#^MT130-C08-1|MT130-C08-1]], C10-4, C09-1; [[MT167 - The Hidden Cracks in Systematic Strategies - Systematic Investor - Ep. 392#^MT167-C02-X1|MT167-C02-X1]], C02-2 | U05: two legs double the cost; a quiet spread at constant risk needs high leverage ([[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C08-4|MT073-C08-4]], C05-1) | Unverified |
| 13 | Three blog results. A no-trade buffer cut turnover by about 5% for a fast rule and 31% for a slow one ([[Carver blog digest#^B27|B27]]). Trend forecasts are worth less when volatility is high ([[Carver blog digest#^B24|B24]]). Letting book risk fall when forecasts are weak beats forcing constant risk ([[Carver blog digest#^B03|B03]]). | ASSERTED (blog tests, summary only) | U02 [[Carver blog digest#^B27|B27]]; [[Carver blog digest#^B24|B24]], [[MT010 - AI Could Change Markets Forever - Systematic Investor - Ep.417#^MT010-C16-3|MT010-C16-3]]; [[Carver blog digest#^B03|B03]] | U04 asserts the opposite of [[Carver blog digest#^B24|B24]] ([[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-3|MT117-C11-3]]) and, against [[Carver blog digest#^B03|B03]], that total trend strength does not predict returns ([[MT087 - Investing in the Age of AI, Uncertainty, and Data Overload - Systematic Investor - Ep.352#^MT087-C09-3|MT087-C09-3]]) | [[Carver blog digest#^B27|B27]] corrected by the audit (note: 20-30%): 52.6 to 49.8; 10.16 to 7.04. [[Carver blog digest#^B24|B24]] corrected: "No mechanism was established", grade weak. [[Carver blog digest#^B03|B03]]: grade moderate or weak, quotes favour neither |

## 3. The systematic pods

The notes are one paper on economic trend (U01) and six practitioner units on price trend. They support two pods as
theses (Trend, Economic trend) and one thin new candidate (Curve carry). Carry and Value are in the book, but their
theses must come from step 1.3 ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)|QP15]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve|QP08]]), which also fills the other B1 and B2 places; short-rate futures
(U01-T4) go to its rates note.

**Trend** (existing book; grid tested in Batch A2)
- Chain: macro change → investors digest information slowly (U04 [[MT116 - Nick Baltas on Trend Following in 2026- Signals, Structure & Strategy - Systematic Investo#^MT116-C02-1|MT116-C02-1]] 'slow digestion of information'; [[MT216 - Why Smart Investors Are Switching to Trend Following - Systematic Investor 334#^MT216-C12-1|MT216-C12-1]] 'a journey that takes you from some valuation level to the new valuation level'); benchmark and career constraints are claim text of [[MT087 - Investing in the Age of AI, Uncertainty, and Data Overload - Systematic Investor - Ep.352#^MT087-C11-1|MT087-C11-1]] only → the move continues for weeks to months → we hold its direction on many markets. ASSERTED in four
  notes (row 8), tested in none.
- Other side: not established. Fragments: allocators who rebalance against moves (U04 [[MT216 - Why Smart Investors Are Switching to Trend Following - Systematic Investor 334#^MT216-C14-X2|MT216-C14-X2]]; U05
  [[MT073 - How Alpha Hides in Plain Sight - Systematic Investor - Ep.362#^MT073-C15-2|MT073-C15-2]], C15-3). U07: the payment shrinks as capital arrives ([[MT070 - Harding Rewrites Winton's Quant Playbook in Search for Returns#^MT070-C01-2|MT070-C01-2]]). The rival mechanisms in row 8
  imply other payers.
- Before 2011: not established in the notes (U07's dated early text, [[QP14 - Making Money from Mathematical Models (David Harding, Phil. Trans. R. Soc. Lond. A 1994)|QP14]] of 1994, is about method). Fung and
  Hsieh (2001) would settle it (reader); the Opus check reads it.
- Instruments: 62 ids (18 equity indexes, 15 bonds and notes, 13 currencies, 16 commodities; [panel.py:304-352](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L304-L352); 61 distinct; plus cm_aqr_ew, trend only, to 2000 ([panel.py:543-551](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L543-L551); [book.py:121-122](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L121-L122))).
- Rule: position = average over versions of a score of the past 1-, 3-, 6- or 12-month excess return, times 40%
  over market volatility, equal weight inside four equal-risk asset classes.
- Engine: BASE 30%, CANDIDATE 45%, as the sign of 1-, 3- and 12-month returns ([config.py:17](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L17), 20, 63;
  [book.py:60-76](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L60-L76)).
- Stops working: markets pinned by policy (U06 [[MT014 - Adapt or Perish- Why Systematic Investors Must Evolve in 2024 - Systematic Investor 325#^MT014-C16-1|MT014-C16-1]]); falls that reverse within days or stay shallow (U03
  [[MT194 - Trend Following during Trump Tariff Turmoil! - Systematic Investor 344#^MT194-C06-2|MT194-C06-2]], [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C12-2|MT045-C12-2]]).
- The notes add the version grid, the breadth item and the crisis profile.

**Economic trend** (existing book)
- Chain: macro news → investors update slowly (not named) → prices move late in the direction of the news → we
  hold each market in the direction of the 12-month change in four macro themes (U01 C01-1, C02-3, C04-8). Only the
  end result is SHOWN (row 7). Other side: not established.
- Before 2011: no, on the pack's evidence: the sources are from 2017 and 2023 (U01 C03-7). I know no earlier
  source for the combined rule (reader); the paper cites Eichenbaum and Evans for one sign (U01 C14-15b). Unless
  step 1.5 finds one, the verdict rule (WORKFLOW section 5) makes this an Incubator pod, run in shadow.
- Instruments and rule: the same 62 markets. Per market, the average over four themes (consumer prices,
  trade-weighted currency, 2-year yield, risk appetite) of the 12-month change over its 10-year volatility, signed
  by the paper's table ([signals.py:94-98](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/signals.py#L94-L98), 210-219, 223-231).
- Engine: BASE 30%, CANDIDATE 15%.
- Stops working: prices detached from fundamentals for long (U01 C03-6, C09-5); a weak 2010s (claim text of C06-3; its quote is the row label 'Jan. 2010 - Dec. 2019'; 'quiet macro data' is reader).
- The notes add U01's reading and U07's null (row 7). Overlap with Trend: section 8, item 8.

**Carry** (existing book)
- Chain, other side: not established; the notes treat carry only as a sleeve beside trend (row 11).
- Before 2011: not established; step 1.3 should date it. Candidates (reader): Brunnermeier, Nagel and Pedersen
  (2008) for currencies; Gorton and Rouwenhorst (2006) for commodities.
- Instruments and rule: bonds and notes, currencies, four energy futures; no equities ([signals.py:330-338](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/signals.py#L330-L338);
  [book.py:106](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L106)). Half the sign of carry, half its rank within the asset class ([book.py:131](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L131)). Carry = bond yield
  minus the 3-month rate, the rate gap to the dollar, or the slope between the first two energy contracts.
- Engine: BASE 20%, CANDIDATE 25%. Stops working: a funding break (U06 [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C05-1|MT083-C05-1]], ASSERTED).
- The notes add form ideas only (carry against its own history, neutral to the market: U04 [[MT173 - The Negative Crisis Beta and CTA's Hidden Market Timing Skills - Systematic Investor 302#^MT173-C15-3|MT173-C15-3]], C15-X2,
  [[MT173 - The Negative Crisis Beta and CTA's Hidden Market Timing Skills - Systematic Investor 302#^MT173-C17-2|MT173-C17-2]]), passed to step 1.3.

**Value** (existing book)
- Chain, other side, stop regime: not established. The notes say only that returns revert beyond about a year
  (U02 [[MT064 - Gold, Futures Pricing & Market Trends - Systematic Investor 335 REUPLOAD#^MT064-C20-2|MT064-C20-2]] 'anything longer than a year is is when mean reversion kicks in'; [[MT044 - Drawdowns, Diversification, and the Hidden Risks in Today’s Markets - Systematic Investor#^MT044-C07-2|MT044-C07-2]] 'In the very long run, it mean reverts') and that reversion belongs in its own engine (U04 [[MT116 - Nick Baltas on Trend Following in 2026- Signals, Structure & Strategy - Systematic Investo#^MT116-C13-2|MT116-C13-2]]) (claim text).
- Before 2011: not established; our protocol cites Asness, Moskowitz and Pedersen 2013 ([TESTING_PROTOCOL.md:61](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/TESTING_PROTOCOL.md#L61));
  step 1.3 should date it.
- Instruments and rule: rank within the asset class of equity indexes on dividend yield, long bonds on real
  yield, currencies on five-year real depreciation ([signals.py:352-384](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/signals.py#L352-L384)). Engine: 15% in both. The notes add nothing.

**Curve carry** (new; B1, or B2 if its history is not locked when B1 is registered)
- Chain: holders and hedgers of commodities trade the near contracts (reader) → near contracts lose more on each roll, the move to the next contract, than far ones (ASSERTED: 'doing it on the front has a negative roll yield', [[MT167 - The Hidden Cracks in Systematic Strategies - Systematic Investor - Ep. 392#^MT167-C03-X2|MT167-C03-X2]]) → the gap stays as pay for taking the other side (a premium 'shared between consumers and and and producers', [[MT167 - The Hidden Cracks in Systematic Strategies - Systematic Investor - Ep. 392#^MT167-C02-X1|MT167-C02-X1]]) → we hold the
  far contract against the near one ([[MT130 - QIS & Trend Following in 2026 ft. Nick Baltas - Systematic Investor - Ep.401#^MT130-C08-1|MT130-C08-1]]). ASSERTED by one seller. Other side: not established; U04 does
  not name who pays.
- Before 2011: not established. 'probably goes back 15 years' ([[MT130 - QIS & Trend Following in 2026 ft. Nick Baltas - Systematic Investor - Ep.401#^MT130-C08-X1|MT130-C08-X1]]) is in the quote, but it dates the QIS-format design to about 2011; it is not a live record and does not establish pre-2011 documentation. Erb and Harvey (2006) date roll
  yield as a return source (reader); a pre-2011 source for this spread must be found in step 1.5.
- Instruments and rule: per commodity with a contract about 12 months out: long that contract, short the front,
  equal face value, sized on the spread's current volatility with a cap on the face value of each leg (U05's
  warning, row 12). One version is flat in backwardation (front price above the 12-month price).
- Engine: not built; nearest code [bloomberg.py:128-142](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/bloomberg.py#L128-L142) and [panel.py:254-261](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L254-L261).
- Stops working: a supply shock that keeps the front above later contracts (U04 [[MT167 - The Hidden Cracks in Systematic Strategies - Systematic Investor - Ep. 392#^MT167-C02-2|MT167-C02-2]]).
- Cannot be Core today: no registered live source (section 6).

## 4. Version grids

Each version is run as its own pod; the pod is the equal-weight average of its versions' positions. A dimension is
listed only where the right choice is uncertain, never because a level is expected to earn more.

| Pod | Dimension | Levels | Why uncertain | n |
|---|---|---|---|---|
| Trend | lookback | 1, 3, 6, 12 months | No speed can be chosen in advance (row 3). Our 1/3/12 was picked among four sets on design data ([CHANGES.md:113-116](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L113-L116)); 6 months restores what that pick left out. | 4 |
| Trend | signal shape | sign; return over volatility, capped at 2 ([book.py:70-76](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L70-L76)) | Sources prefer the graded form; our trial preferred the sign (row 4). | 2 |
| Trend | volatility estimate | hybrid (70% fast estimate from daily returns, 30% ten-year, with a floor); 36-month ([vol.py:38-52](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/vol.py#L38-L52)) | The fast estimate may give up long moves (row 1) and was adopted on Sharpe alone ([CHANGES.md:128](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L128)). BASE runs one, CANDIDATE the other ([config.py:23](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L23), 64). | 2 |
| Economic trend | signal shape | a smooth capped function (tanh) of the scaled change ([signals.py:245](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/signals.py#L245)); its sign (not built) | The paper does not say how a signal becomes a position (U01 section 4). | 2 |
| Carry | form | sign of carry; rank within class | Sources split: directional (U03 [[MT021 - Bonds Behaving Badly - Systematic Investor 309#^MT021-C13-1|MT021-C13-1]]) or neutral to the market (U04 [[MT173 - The Negative Crisis Beta and CTA's Hidden Market Timing Skills - Systematic Investor 302#^MT173-C15-X2|MT173-C15-X2]]). This is today's half-and-half. | 2 |
| Value | none | rank within class | The notes give no reason. | 1 |
| Curve carry | backwardation switch | always on; flat in backwardation | The switch is the seller's rule, described in 2025-26 after losses (U04 [[MT130 - QIS & Trend Following in 2026 ft. Nick Baltas - Systematic Investor - Ep.401#^MT130-C10-4|MT130-C10-4]], C09-1): it may be hindsight. | 2 |

Totals: Trend 16 (4 x 2 x 2), Economic trend 2, Carry 2, Value 1, Curve carry 2.

Rebalance days: every pod runs in four weekly tranches (slices that decide one week apart; tranche 0 decides at
month end, as today), tested in the 1990-2010 weekly check, not in the monthly runs.

Fixed: sizing at 40% over volatility, equal weight in class, four classes at equal risk scaled over 36 months
([book.py:132](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L132), 138-139, 191; [config.py:26-27](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L26-L27)); the hybrid estimate outside Trend; costs ([book.py:46-57](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L46-L57)); the 12-month
change, four themes and sign table of Economic trend; the 12-month contract in Curve carry. Book: Core pods at
equal risk (WORKFLOW 5.1), 10% volatility target, 5x cap on total face value, per-market cap ([config.py:28-30](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L28-L30)).

Batch A, as it follows. A1: data swap, one block at a time (U07-T4's method), alternative-commodity columns off,
st_us_2y removed (bd_us_2y's series is a superset: the same DGS2 months plus any stooq months before DGS2, [panel.py:486-488](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L486-L488), 496); registered as a design change before the run. A2: the grids and tranches,
with Sharpe reported by tranche and asset class. Three more items enter only if D1-D3 open them.

Fate of every VARIANTS level:

| Level | Fate | Reason |
|---|---|---|
| A0, B0, D0, G0, H0 (current markets, class weights, book scaler, commodity carry, themes) | fixed | A0 minus the doubled US 2-year note |
| A1 + alternative commodities | Batch A breadth item, gated by D1 | breadth is hygiene (rule 3); markets enter on their drivers, never on their results |
| A2 + wider emerging currencies | dropped | no design-era history in hand (forwards from about 2010 on LSEG; Bloomberg on campus only); no live source |
| B1 weights by first-factor loading | dropped | needs a smoothing choice (shrinkage) no data can make (U05 section 8); the built cluster weights changed nothing ([CHANGES.md:54](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L54)) |
| C0 hybrid, C1 36-month | versions in Trend | |
| C2 slow only | dropped | already 30% of the hybrid and its floor ([vol.py:48-51](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/vol.py#L48-L51)) |
| C3 static at entry | dropped | not built; no design-era test in the notes |
| D1 6-month correlation x 1-month volatility | dropped as written | the audit found its source statement partly wrong; a faster scaler is a Batch A risk item gated by D3 |
| E0 sign 1/3/12 | versions in Trend, plus a 6-month lookback | rule 2 averages speeds; VARIANTS has no speed level |
| E1 continuous, average 10, cap 20 | version in Trend in the built form (cap 2) | Carver's scaling needs an estimated scalar and differs mainly in the cap (reader) |
| E2 volatility-regime attenuation | dropped | audit: no mechanism, grade weak; justified only by expected gain; U04 asserts the opposite |
| F0 monthly, day 1 | tranche 0 of four | |
| F1 day 3 | dropped as a level | the later tranches trade after the month-end turn |
| F2 weekly re-read | Batch A2 weekly tranches | a full weekly re-read is a speed change of unknown sign (U06-T3) |
| F3 no-trade buffer | Batch A cost item, gated by D2 | |
| G1 calendar spread | the Curve carry pod | |
| H1 forecast-based themes | dropped | no usable history and no live source for consensus forecasts |
| S0, S1, P0, P1 | dropped | nothing is selected; WORKFLOW section 6 fixes the holdout |
| Excluded list (carry tilt, geopolitical theme, spread trading) | dropped; spreads go to the step 1.3 rates note | section 5 |

## 5. The one diagnostic pass

One pass on design months (1975-2010) with the existing engine, run with Batch A2 and logged. It adopts nothing
and uses no place in a batch's error budget (Holm slot). "Item" = a Batch A hygiene item or a line in a pod spec.
Thresholds are reader choices fixed here: 20% and one half come from the notes (U02-T3, U06-T2), the rest are mine.

| Id | Question | Computation | Merges | Gate, fixed now | Premise ids |
|---|---|---|---|---|---|
| D1 | How many independent bets does Trend hold? Which candidates bring a new driver? | Trend profit and loss per market at equal risk ([book.py:60-76](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L60-L76), 132) on the 61 distinct markets (st_us_2y dropped). Principal components (common factors) of monthly excess returns in each trailing 60-month design window, on markets with all 60 months; report, averaged over windows, the first factor's share of variance, each class's mean loading, and pod Sharpe over mean market Sharpe. Per candidate with a locked history: in the same windows, the share of its variance explained by the held markets' first three factors, and its R-squared on the single held market with the highest absolute correlation, each averaged over windows. | U05-T1, U06-T1 | A candidate joins the breadth item only if both averaged shares are under one half, it has 120 months before 2011 ([TESTING_PROTOCOL.md:12](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/TESTING_PROTOCOL.md#L12)), and it is costed at the 8 bp charged for EM currencies (U06-T2). The item is registered with the markets that qualify, under the 30% cap ([book.py:140-148](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L140-L148)); if none, dropped. Candidate results are never read. | U05 [[MT205 - Unpacking the Chaos- What Today’s Market Signals Really Mean - Systematic Investor 343#^MT205-C12-2|MT205-C12-2]], C13-1; U06 [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C08-2|MT083-C08-2]], [[MT111 - Navigating Market Chaos - Systematic Investor 336#^MT111-C06-2|MT111-C06-2]], [[MT158 - Taking the Trend Following Temperature - Systematic Investor 304#^MT158-C13-1|MT158-C13-1]]; U07 [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-1|MT177-C13-1]], C14-1 |
| D2 | How much trading is not caused by signals? | Rebuild positions with volatilities and scalers (the multipliers that bring each block and the book to target risk) held at last month's values, then with scores held ([book.py:95-151](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L95-L151), 191, 198); turnover = sum of absolute position changes ([book.py:212-216](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L212-L216)). Cost drag per market (U02-T2 c) is reported. | U02-T2 (b, c) | If the non-signal share, 1 - (turnover with volatilities and all scalers held at last month's values) / (actual turnover), is at least 20% in both eras (1975-89, 1990-2010), a no-trade buffer is registered as a Batch A cost item (target: lower turnover, net Sharpe not lower); else dropped. Width: trade a market only if its target moves by more than 10% of its standard vol-adjusted position ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C08-2|MT026-C08-2]]: 'if it was less than 10%, I wouldn't bother trading'; 'standard position' is claim text), scaled by relative cost as in U02-T3 ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C11-1|MT026-C11-1]]: 'a wider buffer if an instrument's more expensive'); not [[Carver blog digest#^B13|B13]]'s 10% of target. | U02 [[MT137 - Rob Carver on Trend Following, Skew, and the Total Portfolio Shift - Systematic Investor -#^MT137-C14-1|MT137-C14-1]]; [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C08-1|MT026-C08-1]], C08-2; no number relied on |
| D3 | Is book risk understated in states we can name? | Realised volatility of book returns over the next 12 months against the 10% target ([book.py:197-199](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L197-L199); [config.py:28](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L28)), split by (a) the sign of the trailing 12-month correlation of US equity and 10-year bond returns, (b) the top tenth of mean absolute trend score ([book.py:72](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L72)). Resampling (bootstrap) as [stats.py:122-131](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/stats.py#L122-L131). | U03-T3, U04-T2 | If either split shows realised forward 12-month volatility at least 2 points higher in the named state than in the other months, with the one-sided 90% bootstrap bound of that difference above zero (stationary bootstrap, mean block 12 months, because the forward windows overlap; seed as stats.py), a faster book scaler (U03-T3's form: 70% 12-month EWMA + 30% 36-month book volatility, floor 0.75 x the 36-month value) is registered as a Batch A risk item (target: realised volatility nearer 10%, worst fall not deeper); else dropped. | U03 [[MT194 - Trend Following during Trump Tariff Turmoil! - Systematic Investor 344#^MT194-C16-3|MT194-C16-3]], C17-1, C17-2; [[MT021 - Bonds Behaving Badly - Systematic Investor 309#^MT021-C06-1|MT021-C06-1]]; U04 [[MT087 - Investing in the Age of AI, Uncertainty, and Data Overload - Systematic Investor - Ep.352#^MT087-C07-1|MT087-C07-1]] ('if your barometer is 90%. Then more likely than not you have a lot of directional exposures'), [[MT087 - Investing in the Age of AI, Uncertainty, and Data Overload - Systematic Investor - Ep.352#^MT087-C09-3|MT087-C09-3]] (performance only) |
| D4 | Does Trend lose early in equity falls and pay late? Does Carry lose in funding breaks? | Sort design months by the fall of the S&P 500 (eq_us_spx, compounded excess return; the source's base, [[MT194 - Trend Following during Trump Tariff Turmoil! - Systematic Investor 344#^MT194-C06-1|MT194-C06-1]]) from its 24-month high; report the same table for the four-market average of [protocol.py:200](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/protocol.py#L200) (under 5%, 5-15%, over 15%) and its age (up to 2 months, more). Mean return of each family per cell ([book.py:218-220](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L218-L220)) and in the six design-era stress windows ([config.py:68-70](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L68-L70)). | U03-T2 | If Trend's mean is negative in the young 5-15% cell and positive beyond 15%, its spec lists "young, shallow equity fall" as an expected-loss state; else no such line. If Carry loses in both the 1998 and 2008 windows, its spec lists "funding break" as its stop state; else dropped. A cell with fewer than 6 months is reported, not used. | U03 [[MT194 - Trend Following during Trump Tariff Turmoil! - Systematic Investor 344#^MT194-C06-2|MT194-C06-2]], C06-4; [[MT045 - Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356#^MT045-C05-3|MT045-C05-3]], C06-1; [[MT021 - Bonds Behaving Badly - Systematic Investor 309#^MT021-C13-2|MT021-C13-2]]; U06 [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C05-1|MT083-C05-1]] |
| D5 | Does the economic-trend edge fade when applied late? | Economic trend alone, net, positions applied 0, 1, 3, 6 and 12 months late ([config.py:17](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L17), 32; [book.py:208-209](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L208-L209)). | U01-T1 | If the Sharpe at 3 months' delay is under half the no-delay Sharpe, the spec claims slow reaction and names "no fading with delay" as what would prove it wrong; else it claims a lasting macro state. | U01 C01-1, C02-3, C04-8 |
| D6 | Is a weak trend year a year in which few markets moved? | Per design year and market: Sharpe of trend profit and loss at equal risk ([book.py:60-76](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L60-L76), 132) and of the market itself; regress the first on the absolute value of the second, by era (one regression per era on year-level cross-market means: mean trend Sharpe on mean |market Sharpe|; Newey-West slope standard error, 2 lags, extending [stats.py:165-182](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/stats.py#L165-L182), which returns only the intercept t). | U05-T2 | If the slope differs between eras by less than two standard errors, "trend return per unit of market move, against the design slope" is registered as Trend's breakdown check; else dropped. | U05 [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C07-1|MT221-C07-1]], C10-2; [[MT223 - Why Trend Thrives When Inflation Returns - Systematic Investor - Ep.373#^MT223-C12-1|MT223-C12-1]] |

Own-doc support for D3: realised 36-month volatility ran from 4.9% to 14.2% against 10%
([protocol_diagnostics.md:4](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/protocol_diagnostics.md#L4), 6). D4's 15% is U03's figure (unverified); 5% and 2 months are U03's reader choices.

Proposals dropped, deferred or folded elsewhere:

| Proposal | Fate | Reason |
|---|---|---|
| U01-T2 sign audit | dropped | signs are fixed by the source and may not change after results (WORKFLOW 3.1); pruning cells is selection |
| U01-T3 forecast themes; U02-T4 attenuation | dropped | with levels H1 and E2 |
| U01-T4 short-rate futures | deferred to the step 1.3 rates note | LSEG history pulled, not read; our synthetic 3-month market lost ([protocol_batch1.md:8](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/protocol_batch1.md#L8)) |
| U02-T1, U04-T4 forecast buckets | dropped | their only use was to decide on U02-T5, now a version |
| U02-T3 buffer; U06-T2 alternative commodities | Batch A items if D2, D1 open | U02-T3's premise was corrected by the audit (row 13); U06-T2's admission rule is kept |
| U02-T5 capped continuous trend; U04-T3 calendar spread | a version in Trend; the Curve carry pod | |
| U03-T1 volatility speed by shock | dropped | both estimators are averaged; Batch A2 reports each version in the stress windows |
| U03-T4 geopolitical risk | dropped | sources from 2024-26; the note itself expects a weak result |
| U04-T1, U06-T3 (and U02-T2 a) day-one loss, weekly re-read | folded into the Batch A2 tranche report | tranche 0 is the month-end trade; U04-T1's prediction is unclear in sign (section 8, item 7) |
| U05-T3 carry tilt of trend | dropped | justified only by expected gain, on evidence its source calls unproven; needs forwards not in hand |
| U05-T4 inflation split | dropped | gates nothing; its 4.5% boundary is claim text; the two eras already split high and low inflation (reader) |
| U05-T5 spread gate | recorded for the step 1.3 rates note and as the leg cap in Curve carry | the three built spreads are not traded ([panel.py:353](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L353); [signals.py:28](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/signals.py#L28)) |
| U07-T1 shape audit; U07-T3 frozen against continuing | dropped | dimensions S and P are gone; tail and fragility lines are in the test sheet |
| U07-T2 real against simulated trend | dropped | results by lookback and era come with the versions; the CTA index series are not in hand |
| U07-T4 data corrections | the method of Batch A1 | |
| No-test lists U01-T5, U03-T5, U04-T5, U06-T4, U07-T5 | stand, with three changes forced by rule 2 | the sign form of Economic trend (U01-T5) is now a version; trend speed (U03-T5, U07-T5) is averaged, not settled; U06-T4's planted-error test was done as audit 1.1 |

## 6. Data needs

| Pod | Input | History: source, start | Live: source, delay | Status |
|---|---|---|---|---|
| Trend | monthly excess returns, 62 markets | free panel, 1975 | free daily closes, 1 day | in engine |
| Trend | daily returns (fast volatility, tranches) | free: currencies 1971, US bonds 1962, energy 1983, other commodities 2000 ([daily.py:4-9](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/daily.py#L4-L9)) | free, 1 day | in engine; Bloomberg daily files (1990) usable; LSEG daily pulled, not read |
| Economic trend | consumer prices, trade-weighted currency, 2-year yield or 3-month rate, equity return, Baa spread ([signals.py:210-219](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/signals.py#L210-L219)) | free, 1975; latest revised values, not first releases | free; lag of 0-1 month | in engine; first-release history missing |
| Carry | bond yields, 3-month rates, first two energy contracts | free | free; rates a month late | in engine |
| Value | dividend yields, 10-year yields, consumer prices, spot currencies | free; dividend yields from a yearly file ([signals.py:317-327](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/signals.py#L317-L327)) | free; non-US dividend yield up to 12 months old | in engine; LSEG yields (1973) pulled, not read |
| Curve carry | front and 12-month commodity futures prices | LSEG: grains, softs, metals 1973; WTI 1983 (24 contracts only from 1995; when a 12-month contract starts is not on the sheet); Brent 1988; gas 1990. Bloomberg monthly curves: not usable | LSEG only; the free EIA files hold four energy contracts, no 12-month one ([panel.py:241-251](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L241-L251)) | pulled, not read; live source not registered |
| Trend, breadth item | excess returns of extra commodity markets | LSEG index returns by commodity, starting between 1970 and 1987; Bloomberg indexes: status not stated on the sheet (adapter built, [bloomberg.py:24-41](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/bloomberg.py#L24-L41)) | none free in the engine | pulled, not read; live missing |

Rule 7 flags. Curve carry cannot be Core: its live curves exist only on LSEG, which is not registered as a source,
and the pack does not say its licence allows trading use. A market added by the breadth item needs a live price
first. Value's non-US dividend yield is a weak live source. Economic trend passes rule 7, but its history uses
revised values, lagged to the release date, not the values first released.

## 7. Numbers not verified against quotes

Kept from the notes (unverified unless marked):

| Number | What it is | Note, claim id | Why it matters here |
|---|---|---|---|
| 1.1; 1970-2022 | Sharpe before costs of AQR's economic-trend book | U01 C06-1 (summary only); 1970-2022 in quote C03-9 | size of the Economic trend thesis |
| 0.77, 0.64, 0.63 against 0.26, 0.27 | Sharpe by theme, price-built against forecast-built | U01 C07-2 (summary only: chart reads) | U01's reading of the mechanism |
| 2017, 2023 | dates of the thesis in the pack | 2017 in quote C03-7; 2023 from [TESTING_PROTOCOL.md:55](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/TESTING_PROTOCOL.md#L55) (not a quote) | rule 5 for Economic trend |
| 1.15 against 0.88 | volatility-scaled against fixed sizing | U02 [[Carver blog digest#^B22|B22]] (audit-corrected; digest, summary only) | row 1 |
| 1.18 against 1.15 | graded against yes/no forecast | U02 [[Carver blog digest#^B22|B22]] (digest, summary only) | row 4 |
| 52.6 to 49.8; 10.16 to 7.04 | turnover without and with a buffer, fast and slow rule (about 5% and 31% less) | U02 [[Carver blog digest#^B27|B27]] (audit-corrected; digest, summary only) | row 13; not a premise of D2 |
| 15% | equity fall below which trend loses | U03 [[MT194 - Trend Following during Trump Tariff Turmoil! - Systematic Investor 344#^MT194-C06-2|MT194-C06-2]] | cell boundary in D4 |
| 3-6 months; 4-9 months | speeds hurt most by reversals | U04 [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-1|MT200-C05-1]]; U03 [[MT042 - Diversification is more important than ever! - Systematic Investor - Ep.385#^MT042-C09-1|MT042-C09-1]] | the 6-month lookback |
| 0.8-0.9 against 0.5-0.6 | trend Sharpe, alternative against liquid markets | U06 [[MT158 - Taking the Trend Following Temperature - Systematic Investor 304#^MT158-C07-2|MT158-C07-2]], C07-1 | prior for the breadth item |
| "nearly one for 30 years"; "around a half" | trend Sharpe, past and expected | U07 [[MT070 - Harding Rewrites Winton's Quant Playbook in Search for Returns#^MT070-C06-1|MT070-C06-1]]; [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-1|MT177-C04-1]] | row 10 |
| 15 years | age of the QIS-format design (in quote, not a live record) | U04 [[MT130 - QIS & Trend Following in 2026 ft. Nick Baltas - Systematic Investor - Ep.401#^MT130-C08-X1|MT130-C08-X1]] | rule 5 for Curve carry |
| about 12 months | the far contract in curve carry | about 12 months: U04-T3's choice; the quote says 'the back end of the curve' | the Curve carry rule |

Not used, because the audit found them wrong or summary-only: "within 1-2 bp", "20-30%", "0.5-1", "0.01",
"0.2-0.25", "50%", "10% of target", "1.18 against 0.88". Also not used: U05's 4.5% inflation boundary (claim text).

From our own code and docs (verified by reference): family shares 30/30/20/15/5 and 45/15/25/15 ([config.py:17](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L17),
63); lookbacks 1/3/12, cap 2 ([config.py:20](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L20)); hybrid weight 0.7 ([config.py:23](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L23)); 10% target, 5x cap
([config.py:28-29](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L28-L29)); 40% sizing ([book.py:132](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L132)); 30% cap ([book.py:147](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L147)); 36 months ([book.py:191](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L191), 198); 62 ids
([panel.py:304-352](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L304-L352)); 120 months ([TESTING_PROTOCOL.md:12](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/TESTING_PROTOCOL.md#L12)); selection inflation about 0.23 ([CHANGES.md:140](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L140)); trend
family 0.95 to 0.85 one day late, candidate 0.85 to 0.77 (timing_grid_2026-11-01.csv:3, 9); realised volatility
4.9% to 14.2% ([protocol_diagnostics.md:4](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/protocol_diagnostics.md#L4), 6).

## 8. Conflicts left open for the Opus check

Across notes:
1. Why trends exist (row 8). Does each quote state a cause, or does the claim text add it? U03's behavioural
   premise cites an unchecked reader claim ([[MT195 - Trend Following in 2025- New Challenges, New Strategies! - Systematic Investor 326#^MT195-C09-R1|MT195-C09-R1]]).
2. Speed and Sharpe (row 3). What sample is behind "slow has the higher Sharpe" ([[MT021 - Bonds Behaving Badly - Systematic Investor 309#^MT021-C04-2|MT021-C04-2]], [[MT014 - Adapt or Perish- Why Systematic Investors Must Evolve in 2024 - Systematic Investor 325#^MT014-C05-4|MT014-C05-4]],
   [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C08-2|MT177-C08-2]])? If after 2010, it is an outside prior and the grid rests on our own log.
3. Row 13. Which two columns do [[Carver blog digest#^B24|B24]] and [[Carver blog digest#^B03|B03]] compare? Does [[MT117 - Nick Baltas talks Signal Strength, Trend Following & Portfolio Strategies - Systematic Inv#^MT117-C11-3|MT117-C11-3]] speak of the level of volatility or of
   spikes ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C10-2|MT200-C10-2]])? What data are behind [[MT087 - Investing in the Age of AI, Uncertainty, and Data Overload - Systematic Investor - Ep.352#^MT087-C09-3|MT087-C09-3]], which excepts very high readings (they precede weak
   returns)?
4. Carry in crises (row 11): does [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C05-1|MT083-C05-1]] name episodes? More markets (row 5): [[MT205 - Unpacking the Chaos- What Today’s Market Signals Really Mean - Systematic Investor 343#^MT205-C09-1|MT205-C09-1]] against
   [[MT158 - Taking the Trend Following Temperature - Systematic Investor 304#^MT158-C13-4|MT158-C13-4]]. Cause of the lower Sharpe (row 10).
5. Speakers. U03 gives [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-3|MT221-C11-3]] to Kaminski; U05 gives [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381#^MT221-C11-1|MT221-C11-1]] and C11-X2 to Git and says the [[MT205 - Unpacking the Chaos- What Today’s Market Signals Really Mean - Systematic Investor 343|MT205]] and
   [[MT221 - Why Trend Following Still Works in Tough Markets - Systematic Investor - Ep.381|MT221]] attributions "rest on content and flow". Row 8 uses [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C15-1|MT083-C15-1]] (Kaminski) and [[MT083 - Inside Q1’s Chaos - Systematic Investor - Ep.394#^MT083-C14-3|MT083-C14-3]] (Moore).

Notes against code:
6. "0.10 a day" is BASE's trend family on markets with daily data, price moves only ([timing.py:5-6](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/timing.py#L5-L6)); the
   candidate's figure is 0.85 to 0.77 (timing_grid_2026-11-01.csv:3, 9). The notes quote only the first.
7. U04-T1 says month-end rebalancing makes first-day returns reverse the prior month. But a loss from trading
   with-trend one day late needs first-day returns to continue it. What do [[MT216 - Why Smart Investors Are Switching to Trend Following - Systematic Investor 334#^MT216-C14-1|MT216-C14-1]] and C14-X2 say about the
   timing and direction of the pressure?
8. Pod overlaps. For equities, half of Economic trend's risk theme is the country index's own 12-month return
   ([signals.py:215-219](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/signals.py#L215-L219)), which is Trend's signal. Trend's returns include carry ([book.py:64-68](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L64-L68)). Neither is
   removed here. Confirm both readings of the code.
9. Alternative commodities still enter the panel as soon as their file is present ([panel.py:569-574](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L569-L574)). Confirm,
   since Batch A1 needs them off.

Remaining trend sources:
10. Eckhardt (quotes as in the audit table). No volatility target for the portfolio ("we don't want to restrain it", [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-3|MT020-C06-3]], speaker Rob Santino of ETC) and resizing as a hidden reversion trade, "not always" ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-X1|MT020-C07-X1]], speaker Seibert), cut
    against row 1 and the 10% target. Volatility reverts, prices do not ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C07-2|MT020-C07-2]]): supports the slow part of
    the hybrid. Rules lost value "since" they were revealed ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C05-4|MT020-C05-4]]): supports U07 on decay. Robust statistics
    need 10 to 30 times more data ([[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C12-2|MT020-C12-2]]): bears on every gate here.
11. Fung and Hsieh (reader, from memory; not in the pack): trend funds' returns resemble an option that pays on
    large moves in either direction. Does this (a) date the Trend thesis before 2011; (b) support U04's "no
    autocorrelation needed" against the pod's working thesis; (c) contradict "no payoff in short shocks" at
    monthly frequency; (d) imply that sizing by current volatility gives the option-like payoff away?

## 9. Pack problems

1. Line numbers. The notes cite the repo before gm-1.2.1. Today config.py is +1 line, CHANGES.md +37, signals.py
   +1 after line 193 and +2 after line 345, panel.py a few lines after line 426.
2. Market count: 62 ([TESTING_PROTOCOL.md:25](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/TESTING_PROTOCOL.md#L25); the notes), 64 ([panel.py:1](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L1)), 65 (data sheet). By code reading, two of
   the 62 ids are one series: bd_us_2y and st_us_2y are both the 2-year par note from the same yield, less the
   same rate, wherever that yield exists ([panel.py:328](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L328), 332, 480, 502-503). So 61 distinct markets, and U06's
   "five points on the US curve" are four. Confirmed by the Opus check (code reading: [panel.py:477-480](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L477-L480), 496, 502-503; [daily.py:128-131](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/daily.py#L128-L131); [signals.py:36-39](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/signals.py#L36-L39)): identical in returns, volatility and every signal wherever DGS2 exists.
3. WORKFLOW rule 3 calls breadth, cost and risk changes hygiene; its section 6 lists Batch A as data swap,
   tranches and averaging only. The charter follows rule 3.
4. VARIANTS fixes family shares at 45/25/15/15; WORKFLOW 5.1 puts Core pods at equal risk. The charter follows
   WORKFLOW, which also supersedes U01's "keep econ at 15%".
5. VARIANTS has no speed dimension, though rule 2 names speeds first. Its D cites "U02 row 22" (a liquidity rule;
   the scaler is row 4, which the audit found partly wrong). Its E1 (average 10, cap 20) is not the built form
   ([book.py:73-76](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L73-L76)).
6. U02 against the audit: four errors (row 13; the cost and multiplier claims) and the mixed 1.18-0.88 comparison
   (row 1). U03, U04, U06 and U07 repeat U02's digest figures ([[Carver blog digest#^B03|B03]], [[Carver blog digest#^B17|B17]], [[Carver blog digest#^B22|B22]], [[Carver blog digest#^B24|B24]]) as if settled.
7. Data sheet against notes. U01-T3 assumes consensus forecasts with release dates (sheet: unconfirmed; none on
   LSEG). U04-T3 assumes Bloomberg curves from 1969 (sheet: not usable; LSEG from 1973, not read). U07-T2 assumes
   CTA indexes in the first pull (sheet: in today's visit set). U05-T3, U07-T4 and level A2 assume emerging-market
   forwards (sheet: from about 2010).
8. Data sheet against itself: the Economics sheet of file 1 is "usable now", yet first-release and consensus
   series are "unconfirmed" and also "not available from any source in hand".
9. WORKFLOW 4.1 runs the data swap on Bloomberg data; the sheet says Bloomberg's monthly rates and curves are not
   usable and proposes LSEG, which is not registered.
10. WORKFLOW does not name its "incumbent"; its 0.23 is CANDIDATE's figure ([CHANGES.md:140](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L140)). The brief names four
    families; BASE has a fifth (cross-sectional momentum, 5%, [config.py:17](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L17)), which no note discusses.
11. U01 and U03 do not say, number by number, whether a figure sits in a quote or in claim text; U04-U07 do.

## 10. Self-check

Against the pod list. All seven units are about trend, price or economic. Carry and Value get nothing from the
notes, and the one new pod rests on a seller's word. So the list is the old book plus one thin candidate; new
return sources still have to come from step 1.3. Economic trend may not be a second mechanism (U01 reads it as
price momentum across assets), and the verdict rule may send it to shadow with 15% of the candidate book.

Against the grids. Each added level comes from a variant that lost on design data (lookback sets with 6 months, the
graded shape, the 36-month estimate). Averaging them in lowers the design Sharpe by construction, and "must not
hurt, net of 0.23" then rests on one estimate of selection luck ([CHANGES.md:140](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L140)). The menu is still mine: equal
weight over levels I chose is a pick of its own, and Curve carry's "always on" version is mine, not the source's.
Most sources speak in 2024-26 about 2022-26, so hindsight can enter through the menu; hence each Trend level is
tied to our own design-era log, not to an episode.

Against one pass. It drops the two diagnostics their notes ranked first (U02-T1, U03-T1), so the shop averages
over signal shape and volatility speed without measuring whether either matters. Dropping U01-T2 leaves the sign
table untested, though its source never shows the check it claims (U01 C04-7). Five gate thresholds are reader
choices. Six looks at design data still shape three hygiene items: mild selection, logged, not free.

File:line citations, each re-read against the files on 2026-11-13: [config.py:17](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/config.py#L17), 20, 23, 26-27, 28, 28-29, 28-30,
32, 63, 64, 68-70; [book.py:46-57](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/book.py#L46-L57), 60-76, 64-68, 70-76, 72, 73-76, 95-151, 106, 131, 132, 138-139, 140-148, 147, 191,
197-199, 198, 208-209, 212-216, 218-220; [vol.py:38-52](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/vol.py#L38-L52), 48-51; [signals.py:28](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/signals.py#L28), 94-98, 210-219, 215-219, 223-231, 245,
317-327, 330-338, 352-384; [panel.py:1](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/panel.py#L1), 241-251, 254-261, 304-352, 328, 332, 353, 480, 502-503, 569-574;
[bloomberg.py:24-41](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/bloomberg.py#L24-L41), 128-142; [daily.py:4-9](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/daily.py#L4-L9); [timing.py:5-6](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/timing.py#L5-L6); [stats.py:122-131](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/stats.py#L122-L131), 165-182; [protocol.py:200](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/protocol.py#L200);
[TESTING_PROTOCOL.md:8](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/TESTING_PROTOCOL.md#L8), 12, 25, 61; [CHANGES.md:51-52](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L51-L52), 51-61, 54, 66, 113-116, 128, 128-131, 140;
[protocol_batch1.md:8](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/protocol_batch1.md#L8); [protocol_diagnostics.md:4](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/docs/research/global_macro/protocol_diagnostics.md#L4), 6; timing_grid_2026-11-01.csv:3, 9.

## 11. Independent check (Opus 5.5, 2026-11-13): summary

Full text: `CHARTER_1.2_check.md` (tables A-D per number, statement, premise and pre-2011 claim).

Verdict: PASS WITH CORRECTIONS. The pod list, the averaging logic and the accounting of the 34 proposals hold; no
error of the Carver note is carried.
- Numbers from sources (19): 11 are in the quote, 6 are summary only (U01's Sharpe figures are chart reads in claim
  text; the blog figures), 1 was misread ("15 years" is the age of a product design, not a live record), 1 has no
  claim id (2023, confirmed by our own doc). Numbers from our code and docs: 13 of 13 confirmed.
- Statements (27): 10 supported, 14 partly, 2 not supported (Value's reversion ids; the backwardation switch of Curve
  carry exists only in claim text), 1 contradicted (Curve carry "said to survive crowding": the quotes say the
  opposite). All corrected above.
- Diagnostic premises (6): D4 and D5 could be registered as written; D1, D2, D3 and D6 had hidden choices in their
  gates. The gates above are the corrected, fixed forms. D1's candidate-market part still waits for a locked history.
- Doubled market CONFIRMED by code reading: `bd_us_2y` and `st_us_2y` are the same series wherever the 2-year yield
  exists, in returns, daily volatility and every signal. The book has 61 distinct markets; the US 2-year note holds
  2/15 of each fixed-income block instead of 1/14 and can hold twice the per-market cap. Removing `st_us_2y` changes
  design numbers, so it needs a registered engine version (gm/CHANGES.md) before any run. Effect on Sharpe: unknown.

What the two unseen sources change (claim ids in the check, section 4):
1. Fung and Hsieh: trend pays like "bills and lookback straddles": strong positive skew, a mean that is not
   significant in the primitive strategy. Judged by Sharpe or linear alpha alone, a smoother rule that has given up
   that shape can win. A Trend pod should also be reported by equity state and against the published straddle factors.
2. Fung and Hsieh: trend funds earned in both equity tails (1987, 1990: in quote). Our engine lost in the 1987 crash
   from long equities ([CHANGES.md:134-135](https://github.com/haing-dev/stock-screener/blob/52a6a5818ccbe8eb3c169e9befeffd7602aa7bb3/gm/CHANGES.md#L134-L135)). The crisis payoff is a property of how the rule is run, not of "trend";
   commodities showed no such payoff in their sample. Their funds held the least capital in stock indexes.
3. Eckhardt's firm does not resize with volatility ("we don't want to restrain it", [[MT020 - Bill's Turtle Trading Journey, Modern Systematic Trading, and more! - Open Interest 10#^MT020-C06-3|MT020-C06-3]], speaker Santino) and
   calls resizing a hidden reversion trade (C07-X1, Seibert); Eckhardt says alternative markets are "in practice ...
   actually worse" (C11-1) and wants distribution-free statistics needing 10-30 times more data (C12-2). All ASSERTED.
   This cuts against row 1, the dropped static end of the volatility grid, the breadth item, and normal-theory gates.

Open judgement points (not corrections; none is a decision for the user). Each is closed at the named step under the
rules already written, before registration:
| # | Point | Closed at |
|---|---|---|
| 1 | A static or slow-only volatility version in Trend: three sources give stated model uncertainty there, which is this charter's own test for a version dimension | pod spec 3.1-3.2 |
| 2 | A zero-slot shape report per pod: the five-state equity table per pod, and Trend against the Fung-Hsieh factors 1994-2010 (report only) | registration 3.4 (diagnostic pass) |
| 3 | Whether the breadth item earns a Batch A place, given Eckhardt and the commodity result of Fung and Hsieh | registration 3.4 |
| 4 | One mechanism per pod: Trend's signal includes carry; Economic trend's risk theme includes equity momentum. Make each a version, or write the blend into the thesis | pod spec 3.1-3.2 |
| 5 | Curve carry: two versions, or only "always on" (the switch is summary only) | thesis note 1.3 + pod spec |
| 6 | Economic trend under rule 5 (sources 2017 and 2023): Incubator would take 15% (CANDIDATE) or 30% (BASE) out of the traded book untested; the reading of "2022 positive" is not pre-committed | thesis register 1.5; registration 3.4 |
| 7 | Class risk as a version dimension in Trend (equal risk to equities against where trend funds held capital) | pod spec 3.1-3.2 |
| 8 | D5 may not separate slow reaction from a lasting state (a 3-month delay keeps 9 of 12 months) | registration 3.4 |
| 9 | Rule 5 for Trend: Fung and Hsieh (2001) document the strategy and its payoff but "are not advocating that markets trend". Does a documented strategy without a documented cause count? | thesis register 1.5 |

Not verifiable in this check: the blog digest numbers (no post text), [[QP14 - Making Money from Mathematical Models (David Harding, Phil. Trans. R. Soc. Lond. A 1994)|QP14]], the size of the doubled-market effect
(needs a run), contract start dates of 12-month LSEG contracts, LSEG licence terms for trading use.

Usage: Fable 5.2 max, one run, about 0.67M tokens; Opus 5.5 high check, about 0.36M tokens.

