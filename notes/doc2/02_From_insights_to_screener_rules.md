## From insights to screener rules

The 63 new interviews, added in two batches of 39 and 24, mostly confirm the screener's core design: high cash returns on capital, sustained over many years, with room to reinvest, outside low-return industries. They also point to four gaps. The screen ignores price; it can't see investment that is expensed rather than capitalized; it doesn't test resilience to recessions and refinancing; and it treats healthcare as one bucket. The second batch adds checks on tax-flattered returns, owner-operators, spin-off parents, capex that buys no growth, and software and AI-infrastructure risk. Each change below is attributed, and effort assumes SEC financial-statement data unless marked.

### 1. Keep: what the new voices confirm

- **High returns persist, so a long record is informative.** High-ROE companies have clustered near \~20% since 1966, and no sector's ROIC switched ends (Terry Smith). Over long holds your return converges on the business's return on capital (Davis, Terry Smith via Munger). This supports gates G1 and G5.
- **The exclusion list matches the evidence.** Terry Smith's persistently low-ROIC sectors are utilities, telecoms, transport, energy, materials and retailing; Alta Fox's study screen also drops energy, materials and financials (Haley).
- **Cash, not reported profit.** Prefer free cash flow to earnings or EBITDA, which "can be easily manipulated" (Haley). Greenblatt and Terry Smith both measure returns in cash. This supports G7.
- **No momentum or volatility inputs.** Davis treats momentum buying as the opposite of investing, and Greenblatt calls beta and Sharpe ratios "garbage in garbage out". Price drawdowns aren't sell signals for a well-understood holding (Li Lu). With passive, quant and pod flows setting prices, short-term moves say even less (Sandler, Oct 2024).
- **Expect the obvious names and long dry spells.** Visible moats are "probably efficiently priced" (Dorsey), which is why a test run returns MSFT, V and MA. Good formulas also lag for 3–4 years at a stretch (Greenblatt).
- **Strong balance sheets are offense as well as defense.** Cash-rich companies keep investing through the AI shift, while those that "levered up to buy back stock or paid dividends" are "suffering" (Resnick, Jericho, Apr 2024). This supports the debt limits in Core and Fortress.
- **Fortress's recession limits are demanding enough.** A hard landing cuts profits "20 percent plus" (Druckenmiller, May 2023). Fortress lets operating income fall only 15% in 2020 and 25% in 2009.
- **Funded runway for clinical names.** In growth investing, lesson one is "don't run out of money" (Casdin, adapting Buffett). He over-capitalizes companies burning $100–150M every 12–24 months, which supports the clinical screen's 2-year runway rule.

### 2. Changes to the quality screen

| # | Change | What it catches | Who argues for it | Effort |
| --- | --- | --- | --- | --- |
| 1 | Add **cash ROCE** (free cash flow ÷ capital employed) next to NOPAT-based ROIC | Returns that don't turn into cash | Terry Smith (about 25% across his portfolio) | Easy |
| 2 | Add **pre-tax return on tangible capital**, EBIT ÷ (net working capital + net fixed assets); "good" starts above 20% | Fair comparison across tax rates and capital structures | Greenblatt | Easy |
| 3 | Add **reinvestment rate** (growth ÷ return on capital, or share of cash flow reinvested) to the returns pillar | A 20% business reinvesting 70% beats one reinvesting 30% | Dorsey, Goldstein, Terry Smith | Medium |
| 4 | Add an **asset-light route**: gross profit ÷ tangible assets for companies failing ROIC gates | Businesses whose investment is expensed, where ROIC is "frankly meaningless" | Haley, Dorsey | Easy |
| 5 | Score **recession resilience**: revenue and operating income in FY2020 (and FY2009 with a 15-year lookback) | Earnings that grow through a recession protect the stock | Druckenmiller, Davis | Easy |
| 6 | Test **peak-to-peak growth** across cycles, not only year-on-year steadiness | Secular growers with cyclical noise | Terry Smith | Medium |
| 7 | Flag **over-earning**: latest operating margin far above its 10-year median | COVID-style over-earners and cyclical peaks | Druckenmiller, Sundheim, Li Lu | Easy |
| 8 | Flag **per-share growth bought with debt**: falling share count while net debt rises, worse if R&D ÷ revenue is also falling | 2010–18 S&P EPS +60% vs corporate profits +27%; firms that "levered up to buy back stock" can't fund R&D | Druckenmiller, Resnick | Easy |
| 9 | Flag **refinancing risk**: debt due within 2 years vs cash, and interest coverage at today's rates | Leverage that breaks when long rates stay high | Druckenmiller, Gerber, Matt Mark | Medium |
| 10 | Flag **capex above operating cash flow** and equity-funded build-outs | Externally funded booms (dot-com capex ran \~200% of OCF) | Maverick, Sundheim | Easy |
| 11 | Flag **earnings far above operating cash flow** and capitalized costs growing faster than revenue | Aggressive capitalization (Sundheim's OCA fraud short) | Sundheim | Medium |
| 12 | Flag **customer concentration** (XBRL concentration-risk tags), e.g. one customer ≥ 50–70% | A 90% chance it's fine doesn't offset a 10% disaster | Haley | Medium |
| 13 | Flag **tax-flattered returns**: 3-year effective tax rate (income tax ÷ pretax income) 10+ points below its level 10 years earlier; also show ROIC at the 25% default rate (Core, Emerging, Fortress, Healthcare commercial) | Returns lifted by tax cuts that may reverse: Apple's rate fell from 30.2% to 14% and Microsoft's from 30% to 17.7% since 2007 | Stahl (Apr 2025), Karniol-Tambour (Jun 2022) | Easy |
| 14 | Score **affiliate ownership** from the cover page: 1 − public float ÷ market value on the float date; add it to the capital-allocation pillar (Core, Emerging) | Owner-operators, which float-weighted indexes underweight and so leave cheaper | Stahl; Haley (insiders ≥ \~5% in small caps) | Easy (EntityPublicFloat is already fetched) |
| 15 | Flag **capex that buys no growth**: 3-year capex ÷ revenue ≥ \~1.5x its 10-year median, or capex ÷ D&A well above 1, while growth doesn't speed up and the ROIC trend falls (Core, Fortress, Cyclicals) | Incumbents defending dominance with capex, which earns "a lower price earnings multiple"; resilience and decarbonization spend unlikely to lift profits | Stahl (Alphabet, Mar 2026), Sundheim (Feb 2026), Karniol-Tambour (Jun 2022) | Easy |
| 16 | **Special situations:** add **spin-off parents**, i.e. companies reporting discontinued operations within 36 months (XBRL discontinued-operations tags), not only the Form 10 spinco | Parents whose averages jump once the weak unit leaves ("It's just a different way of calculating"), and whose coverage fixates on one segment | Stahl (2015), Einhorn (Solvay, Apr 2024) | Medium |
| 17 | Add a **royalty and land exception** to the industry exclusions: in excluded commodity, real-estate and holding-company codes, screen anyway when capex is under \~10% of operating cash flow (Core) | Owners with no reinvestment need (Texas Pacific Land, Franco-Nevada) that the price-taker exclusion drops: "Being in energy or some other industry is not predictive. It's just descriptive" | Stahl | Easy |
| 18 | **Cyclicals:** add **5-year average free-cash-flow yield after capex** and dividend yield to the value pillar, and industry **buybacks + dividends ÷ capex** to Industry\_Cycle | Trough-priced producers that pay back their price in cash (Solvay: \~10% yield, 5-year post-capex FCF ≈ market cap), and industries where "higher prices aren't fueling new capacity instead they're fueling buybacks" | Einhorn (May 2022, Apr 2024) | Easy |
| 19 | Flag **software gross-margin erosion**: gross margin down three years in a row in SIC 7370–7379 (Core, Emerging) | AI adds "a real marginal cost to software this time around" | Nadella (Oct 2025) | Easy |
| 20 | Add a **home-country column** from SEC submissions (business address; state of incorporation is already extracted), flag companies based outside developed markets and count each PASS list by country (all screens) | Insider and local-rule risks that are "very very hard to compete with... sitting in New York", and lists that repeat US market-cap concentration | Einhorn, Sundheim; Karniol-Tambour, Citrone (May 2025) | Easy |

### 3. Healthcare: split the bucket

- **Keep commercial pharma, medtech, tools and services in the screen.** Pharma and health care are persistently high-ROIC sectors (Terry Smith), and healthcare was over-represented among Alta Fox's 2015–20 multibaggers (Haley).
- **Keep pre-revenue biotech out.** Its edge is whether a drug works, which numbers can't show (Chen, Kantesaria); gates G3 and G4 already remove it.
- **Add three healthcare flags.** Revenue near patent expiry is \~90–98% at risk (Johnson, Flynn). Medicare/Medicaid dependence needs a larger margin of safety (Greenblatt). Growth from price rises in old, crowded drug classes is a policy target (Flynn).
- **Benchmark margins by subsector:** drugs at 80–90% gross and toward \~50% operating (Chen); diagnostics and tools at \~70–80% gross (Casdin).
- **Clinical screen: flag a sharp 3-month run-up into a known readout.** In Casdin's factor data, high-impact events 1–3 months out were negatively correlated with returns. Readout dates need the AI review.
- **AI review: payers, scheduling and the team.** Does payer coverage lag the volume (Natera; Buckley, Duquesne)? Could drug scheduling be lifted (Rosen)? Are clinical, regulatory, finance and commercial seats filled (Casdin)?

### 4. Add a valuation stage after the quality screen

The screen deliberately ignores price, but almost every investor here separates a great business from a great investment. This needs share prices, which SEC filings don't provide.

- **Earnings-yield floor:** EBIT ÷ EV at least the higher of the 10-year bond yield and 6% (Greenblatt), or a starting P/E around 15x or below with no multiple expansion assumed (Davis).
- **Reverse DCF:** flag prices that need \~20%+ growth for 10 years at >50% margins, which only \~0.1% of companies have achieved (Davis).
- **Magic-formula cross-check:** rank on EBIT/EV plus EBIT/tangible capital, excluding financials (Greenblatt).
- **Forward lens for fast growers:** P/E on earnings 2–4 years out, because S-curve winners "may not screen as the cheapest" (Sacerdote, Shaulov). This needs analyst estimates.
- **Own-history multiple:** flag quality companies whose P/E sits near the bottom of its own long range while EPS has grown. J&J at \~12x in early 2011 had been seen about five times in 60 years (Watsa).
- **Net-cash and asset floors:** show market cap ÷ net cash on every screen, not only clinical. A price below cash is the extreme margin of safety (Watsa). For hard-asset owners, compare market cap with net PP&E plus net cash (Alfred).
- **Deceleration check:** flag high multiples where the latest year's growth is under half the 3-year CAGR (Cohen, May 2025). Exempt the most durable businesses, as Costco shows (Sundheim, May 2021).

### 5. Move to the AI review (Stage 2): what numbers can't show

Speakers repeatedly named things a financial screen can't capture. These belong in the moat rubric that Claude scores from the 10-K.

- **Moat durability and switching costs:** "you can't screen for switching costs" (Dorsey); durability is "a much more ... qualitative sort of a thing" (Thiel).
- **Management and alignment:** insider ownership ≥ \~5% in small caps (Haley), long-dated pay vesting (Davis), and stated hurdle rates for buybacks and M&A (Haley, Dorsey). Is it an owner-operator or an "agent-operator" paid "often independent of the long-term value of the shares" (Stahl)?
- **AI disruption exposure:** seat-based pricing, reliance on annual price rises and AI revenue ≤1–2% of sales (Sacerdote); enabler, user, insulated or "walking dead" (Davis). Early tells: high price with low usage (Nadella), slipping net retention (Bravo) and price rises without audience growth (Marques).
- **Temporary or permanent?** The key question for any cheap, troubled name (Greenblatt). For a cyclical, also ask trough or midcycle (Einhorn on Solvay, Apr 2024).
- **Why is this mispriced?** "The most important question in the investment process" (Haley). Pair it with Davis's pre-mortem: why would this holding "dramatically underperform" over five years?
- **Read the segment note.** Is the bear case about one segment? Solvay's sell side wrote about soda ash though \~70% of revenue came from other lines (Einhorn). Is a trailing loss from a business being exited, as at Zillow (Sandler)?
- **Hidden and dormant assets:** land carried at no value ("Property, no value assigned"), unexplored acreage and non-producing royalties. A royalty is "a call option on everything" (Stahl).
- **Macro and policy exposure:** does demand rely on lower-income consumers squeezed by fuel and food inflation, or on tariff-exposed supply chains? Do very low tax rates or dominant positions face tax rises and antitrust (Karniol-Tambour, Jun 2022, May 2025)?
- **Financing quality:** does revenue rely on customers the company finances or owns equity in? Vendor financing in "exotic forms" needs scrutiny (Nadella). Treat private-credit debt as equity-like risk (Karniol-Tambour, May 2025).
