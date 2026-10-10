"""The investment thesis shown at the top of each screen on the site (and in the IC/LP write-up).

Flow per screen: what it is -> what defines one (and why those traits exist) -> a typical example with sourced numbers.
No investor names (the site rule); companies are named. Figures were checked on 10 Oct 2026 against the pages in
"src"; 10-year returns are trailing to 8-9 Oct 2026, dividends reinvested unless marked price-only.
"""

THESIS = {
    "core": {
        "def": "Core Compounders are durable, predictable businesses that earn high returns on capital and can keep "
               "reinvesting at those returns for years, making them candidates for long-term buy-and-hold.",
        "traits": ["High returns on capital, held for a decade rather than one good stretch",
                   "Revenue still growing, so profits have room to compound",
                   "Profits that arrive as cash, after the cost of stock pay",
                   "Profitable through recessions, with little debt"],
        "cause": "These traits are the result of a resilient business with an entrenched competitive advantage, such "
                 "as a toll-like position, a network or a brand, that is unlikely to fade without a major disruption.",
        "ex": {"co": "S&P Global", "stat": "15%/yr", "stat_label": "earnings-per-share growth, 2015-2024",
               "text": "S&P Global is a typical Core Compounder. Bought during the 2008 crisis at about $17.50 a share, "
                       "it traded above $500 by late 2024, and earnings per share grew about 15% a year from 2015 to "
                       "2024. Its "
                       "moat is a toll on borrowing: almost every bond issuer needs a credit rating whatever the "
                       "cycle, and the business needs very little capital to grow.",
               "src": [["Earnings history (Sure Dividend)", "https://www.suredividend.com/wp-content/uploads/2025/11/SPGI-2025-11-17.pdf"],
                       ["10-year returns", "https://totalrealreturns.com/n/SPGI"]]},
    },
    "emerging": {
        "def": "Emerging Compounders are smaller, already-profitable companies that are growing fast and turning that "
               "growth into wider margins, making them candidates to become tomorrow's Core Compounders before the "
               "market prices them as such.",
        "traits": ["Already profitable: proven businesses, not cash burners that must dilute to survive",
                   "Revenue up at least 15% a year, and not fading in the latest year",
                   "Margins widening as the company scales",
                   "Little dilution, modest debt, and a price that works on profit growth alone"],
        "cause": "These traits are the result of a company that dominates a niche with a product customers value, run "
                 "by owner-minded management, at a size most large funds cannot buy.",
        "ex": {"co": "XPEL", "stat": "36%/yr", "stat_label": "revenue growth, 2015-2021",
               "text": "XPEL, a maker of automotive paint-protection film, grew revenue from $41 million in 2015 to "
                       "$259 million in 2021 while staying profitable. It dominates a niche that larger chemical "
                       "groups treat as a sideline, its software cuts the film to fit every car model, and its chief "
                       "executive keeps a large personal stake in the company.",
               "src": [["Revenue history (roic.ai)", "https://www.roic.ai/quote/XPEL/classic"]]},
    },
    "owners": {
        "def": "Owner-Operators are high-return companies run by people who own a large share of them, making them "
               "candidates for patient capital that wants management to think like shareholders.",
        "traits": ["Insiders own at least a fifth of the company",
                   "Consistent profits and returns on capital of at least 12%",
                   "Profits that arrive as cash, and little debt",
                   "A fair price: owner-run companies often trade cheaply"],
        "cause": "These traits are the result of owners who think in decades, avoid empire-building and allocate "
                 "capital as shareholders, while index funds, which weight by free float, systematically under-own "
                 "them.",
        "ex": {"co": "Interactive Brokers", "stat": "≈27%/yr", "stat_label": "total return, 10 years to Oct 2026",
               "text": "Interactive Brokers is still majority-owned by its founder: he and his affiliates hold about "
                       "74% of the operating company. Owning most of the business, he automated it rather than staffed "
                       "it, which gives pre-tax margins of 70-80%. The founder's stake sits in the operating company, "
                       "not the listed shares, so it is confirmed by hand rather than by the screen.",
               "src": [["FY2025 10-K", "https://www.sec.gov/Archives/edgar/data/1381197/000138119726000062/ibkr-20251231.htm"],
                       ["10-year returns", "https://chartrow.com/quote/ibkr/trailing-returns"]]},
    },
    "fortress": {
        "def": "Fortress companies are businesses whose earnings hold up when the economy does not, making them "
               "candidates for the defensive core of a portfolio.",
        "traits": ["Revenue and operating profit held up in both 2008-09 and 2020",
                   "No operating loss in ten years and free cash flow almost every year",
                   "Stable margins that held through the 2021-23 inflation",
                   "Low debt, comfortable interest cover and no refinancing wall"],
        "cause": "These traits are the result of essential, recurring demand and a cost or scale position that "
                 "competitors cannot match, so customers keep buying and the company keeps its pricing.",
        "ex": {"co": "Costco", "stat": "−1.5%", "stat_label": "revenue change in fiscal 2009",
               "text": "Costco's revenue slipped only 1.5% and its operating income 9.8% in fiscal 2009, the worst year "
                       "of the financial crisis, and its shares have returned about 22% a year over the last decade. "
                       "Its advantage is scale passed on to members as lower prices rather than taken as margin, which "
                       "keeps them renewing in good years and bad.",
               "src": [["FY2009 results", "https://www.globenewswire.com/news-release/2009/10/07/938202/0/en/Costco-Wholesale-Corporation-Reports-Fourth-Quarter-and-Fiscal-Year-2009-Operating-Results-and-September-Sales-Results.html?print=1"],
                       ["10-year returns", "https://chartrow.com/quote/cost/trailing-returns"]]},
    },
    "real_assets": {
        "def": "Hard Assets & Royalties companies own scarce land, minerals, royalties, water, timber or pipelines and "
               "collect income without working the asset themselves, making them candidates for long-term, "
               "inflation-resistant cash returns.",
        "traits": ["Almost no reinvestment: capital spending a small fraction of operating cash flow",
                   "Royalty-like operating margins of at least 30%",
                   "Profitable through commodity cycles, with little debt",
                   "A sensible price, since even a perfect royalty can be bought too dear"],
        "cause": "These traits are the result of owning the asset rather than operating it: others spend the capital "
                 "and the owner keeps a share of the revenue, and land or mineral rights cannot be made obsolete.",
        "ex": {"co": "Texas Pacific Land", "stat": "74%", "stat_label": "operating margin, 2025",
               "text": "Texas Pacific Land earned a 74% operating margin on $798 million of revenue in 2025 while "
                       "spending only $60 million on fixed assets, and its shares have returned about 30% a year over "
                       "the last decade. Shale drillers need its West Texas land, water and rights of way, so its "
                       "income grows with their activity without any reinvestment of its own.",
               "src": [["FY2025 results", "https://www.sec.gov/Archives/edgar/data/1811074/000181107426000016/exhibit991q42025earningsre.htm"],
                       ["10-year returns", "https://totalrealreturns.com/n/TPL"]]},
    },
    "cyclicals": {
        "def": "Capacity-cycle Cyclicals are good businesses in cyclical industries bought when their margins are "
               "depressed, making them candidates for buying low in the cycle and holding through the recovery.",
        "traits": ["Solid returns on capital in a typical year, and profitable in most years",
                   "Margins in the bottom half of their own ten-year range",
                   "Cheap against average earnings across the cycle, not this year's",
                   "Debt that a trough cannot break"],
        "cause": "These traits are the result of a sound business in an industry where low prices force weak capacity "
                 "out, which sets up the recovery, while investors extrapolate the trough.",
        "ex": {"co": "NVR", "stat": "≈11×", "stat_label": "from the 2009 low to end-2017",
               "text": "NVR, a homebuilder, fell to about $320 a share at the 2009 housing low. It closed 2012 at $920 "
                       "and 2017 at about $3,500. It options land rather than owning it and builds homes already sold, "
                       "so a housing slump dents its profits without causing losses, and the low was a cyclical price "
                       "for a durable business.",
               "src": [["Price history (Macrotrends)", "https://macrotrends.net/stocks/charts/NVR/nvr/stock-price-history"]]},
    },
    "trough_cash": {
        "def": "Trough Cyclical Cash companies are cyclical producers at depressed margins that still generate cash "
               "and are not adding capacity, making them candidates that pay shareholders to wait for the upturn.",
        "traits": ["Margins in the bottom half of their own ten-year range",
                   "Free cash flow positive in most years, troughs included",
                   "Capital spending close to depreciation: maintaining, not expanding",
                   "Average free cash flow of at least a tenth of the market value, with little debt"],
        "cause": "These traits are the result of an industry that has under-invested for years, so supply cannot "
                 "respond quickly when demand returns, while investors treat a trough year as the new normal.",
        "ex": {"co": "Solvay", "stat": "≈10%", "stat_label": "dividend yield at the 2024 trough",
               "text": "In April 2024, soda-ash producer Solvay was valued at €2.7 billion while expecting to generate "
                       "its whole market value in free cash flow over five years; the dividend alone yielded close to "
                       "10%. The dividend has been held since, but free cash flow (€350 million in 2025) has run below "
                       "that pace, which is why delivery is checked against the forecast.",
               "src": [["FY2025 results", "https://www.solvay.com/en/press-release/solvay-fourth-quarter-and-full-year-2025-results"]]},
    },
    "special": {
        "def": "Special Situations are spin-offs, companies emerging from bankruptcy and recent listings sold for "
               "reasons unrelated to value, making them candidates for buying good businesses from forced sellers.",
        "traits": ["A profitable business today",
                   "Moderate debt, since a spin-off is often loaded with it",
                   "A low price on operating profit"],
        "cause": "These traits are the result of selling driven by mandate, not value: index funds sell spin-offs that "
                 "don't fit, former creditors sell equity they never wanted, and few analysts cover the new company.",
        "ex": {"co": "NII Holdings", "stat": "2.8×", "stat_label": "EBITDA after bankruptcy, vs 6.7× for peers",
               "text": "NII Holdings came out of bankruptcy in 2002 at about $10 a share, valued at 2.8 times EBITDA "
                       "against 6.7 times for wireless peers, with its value hidden in the filings. The shares rose "
                       "to the equivalent of $240. It later re-borrowed and filed again in 2014, so the discipline is "
                       "to sell once the discount closes.",
               "src": [["2014 filing (Telecompaper)", "https://www.telecompaper.com/news/nii-holdings-files-for-chapter-11--1037143"]]},
    },
    "hidden": {
        "def": "Hidden Earnings companies are profitable businesses the market is looking past because of a feared or "
               "departing segment or a sharp sell-off, making them candidates for buying earnings the market cannot "
               "see yet.",
        "traits": ["A reason to be overlooked: a recent spin-off or sale, or a price at least 40% below its high",
                   "Still profitable and cash-generating today, with sales not in steady decline",
                   "Decent returns on capital over a decade, and moderate debt",
                   "A low price on operating profit"],
        "cause": "These traits are the result of coverage fixating on the noise: trailing figures still include a "
                 "business being exited, and sharp sell-offs leave forced sellers with no buyers.",
        "ex": {"co": "Zillow", "stat": "$23M", "stat_label": "net income in 2025, after a $112M loss in 2024",
               "text": "In late 2024 Zillow still looked unprofitable on trailing figures, because they included losses "
                       "from the home-flipping business it had exited; the core marketplace was profitable. In 2025 it "
                       "reported net income of $23 million against a $112 million loss a year earlier, on revenue up "
                       "16%.",
               "src": [["FY2025 results", "https://zillowgroup.mediaroom.com/2026-02-10-Zillow-Group-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results"]]},
    },
    "asset_floor": {
        "def": "Asset-Floor Value companies trade at or below their net cash or tangible book value and still generate "
               "cash, making them candidates for owning the operating business for little or nothing.",
        "traits": ["Market value no higher than net cash, or a price no higher than tangible book value",
                   "Tangible book per share not shrinking",
                   "Positive operating cash flow, and usually profitable",
                   "Little debt ranking ahead of shareholders"],
        "cause": "These traits are the result of neglect: such companies are usually small, unloved and dull, and "
                 "investors assume the cash will be wasted, while the assets protect the downside until a buyback, a "
                 "sale or an activist closes the gap.",
        "ex": {"co": "Meritage Homes", "stat": "0.8×", "stat_label": "price / tangible book, Oct 2026",
               "text": "Homebuilder Meritage traded at about 0.8 times tangible book in October 2026, while book value "
                       "per share grew 5% over the year and it bought back $100 million of stock in a single quarter. "
                       "A growing book makes the discount a floor rather than a trap.",
               "src": [["Q2 2026 results", "https://investors.meritagehomes.com/sec-filings/all-sec-filings/content/0000833079-26-000125/mth20260630earningsrelease.htm"],
                       ["Valuation (Stockopedia)", "https://www.stockopedia.com/share-prices/meritage-homes-NYQ:MTH"]]},
    },
    "hc_commercial": {
        "def": "Healthcare Commercial companies are profitable drug, device, tools, services and insurance businesses "
               "with durable returns, making them candidates for long-term ownership of franchises in one of the "
               "highest-return sectors.",
        "traits": ["Profitable in at least four of the last five years, or a new launcher growing 25%+ a year",
                   "Returns on capital of at least 12%",
                   "Gross margins of a proprietary product: 65%+ for drug makers, 50%+ for devices and tools",
                   "Growing revenue, cash conversion after stock pay, and moderate debt"],
        "cause": "These traits are the result of patents, regulatory approvals and scientific know-how that take "
                 "years and billions to replicate, while headline fears regularly price good franchises as if those "
                 "advantages were about to expire.",
        "ex": {"co": "Eli Lilly", "stat": "≈32%/yr", "stat_label": "total return, 10 years to Oct 2026",
               "text": "Eli Lilly has returned about 32% a year over the last decade. It takes a drug from first human "
                       "dose to approval in about 5.9 years, roughly half the industry's time, which leaves more of "
                       "each patent's life to sell the drug: a repeatable process rather than one lucky product.",
               "src": [["10-year returns", "https://totalrealreturns.com/n/LLY"]]},
    },
    "hc_clinical": {
        "def": "Healthcare Clinical companies are biotech and medtech developers valued near or below the cash they "
               "hold, with years of funding, making them candidates for owning the science for little or nothing.",
        "traits": ["At least two years of cash, or a funding gap one normal share sale can cover",
                   "Little debt ahead of shareholders",
                   "Enterprise value near or below cash",
                   "Market value covered by the cash left after another year of spending"],
        "cause": "These traits are the result of boom-and-bust biotech funding: in a bust, generalist investors sell "
                 "regardless of the science, and a company priced below its cash rarely goes to zero.",
        "ex": {"co": "MorphoSys", "stat": "5.8×", "stat_label": "takeover price vs the Dec 2022 low",
               "text": "In December 2022 MorphoSys held about €1 billion of cash and traded as low as €11.81 a share, "
                       "valuing its approved drug and late-stage pipeline at almost nothing. In February 2024 Novartis "
                       "agreed to buy it for €68 a share in cash.",
               "src": [["Dec 2022 low (4investors)", "https://www.4investors.de/nachrichten/boerse.php?ID=168395"],
                       ["Novartis offer", "https://www.accessnewswire.com/newsroom/en/biotechnology/morphosys-enters-into-business-combination-agreement-to-be-acquired-by-novartis-for-831278"]]},
    },
    "red_flags": {
        "def": "Red Flags are expensive companies whose business is already deteriorating, making them candidates to "
               "avoid, or to question if we already own them.",
        "traits": ["Priced at a high multiple of sales",
                   "At least two signs of breakage: fading growth or margins, losses, shrinking sales",
                   "Profits not backed by cash, recurring 'one-off' charges, growth bought with acquisitions or stock",
                   "Inventory piling up, or heavy capital spending while burning cash"],
        "cause": "These traits are the result of a price that still assumes the past: an expensive stock can stay "
                 "expensive until the business visibly weakens, and then the multiple and the earnings fall together.",
        "ex": {"co": "Semiconductors, 2000", "stat": "≈−80%", "stat_label": "chip index, Mar 2000 peak to Oct 2002",
               "text": "In early 2000, chip stocks traded at record multiples while inventories at the chipmakers and "
                       "their customers were also at record highs: demand had been pulled forward. The Philadelphia "
                       "Semiconductor Index then lost roughly four-fifths of its value by October 2002.",
               "src": [["Index levels (kabutore)", "https://www.kabutore.biz/shisu/sox.html"]]},
    },
}
