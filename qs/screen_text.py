"""Site text: one plain sentence per rule (RATIONALE) and per screen (PURPOSE). No investor names; the attributions
behind each rule live in docs/criteria/Screener_Criteria.xlsx. Kept apart from screens.py so rule logic stays short."""

_TRADE = "Big enough to trade."
_VOL = "Enough trading to build and exit a position."
_SIZE = "Big enough to own; small filers have patchier data."
RATIONALE = {
    "G1": "A long record shows the business has stayed good; good companies tend to stay good.",
    "G3": _SIZE,
    "G4": "Steady profits signal a predictable business.",
    "G5a": "High returns on capital sustained for a decade are the clearest sign of a moat.",
    "G5b": "Returns must hold year after year, not in one good stretch.",
    "G6": "A predictable but slow grower makes a poor compounder; growth needs a runway.",
    "G7": "Profits must turn into cash, after the cost of stock pay.",
    "G8": "Low debt leaves room to act when conditions turn.",
    "G9": "A true compounder stays profitable through downturns; a loss as sales fall points to a cyclical grower.",
    "G10": "Sales below their level 3 years ago need a reason: a cyclical dip or a structural decline.",
    "E1": "Three years is the minimum to measure growth and margin trends.",
    "E3": "Most big long-term winners were already profitable years earlier. For capital-heavy businesses depreciation "
          "is a real cost, so operating profit must be positive.",
    "E4": "Big winners typically grew revenue around 20% a year.",
    "E5": "Missing on revenue is how growth stocks blow up.",
    "E6": "A healthy gross margin leaves room for operating leverage.",
    "E7": "Margins should widen as revenue grows.",
    "E8": "Value per share is what counts; heavy dilution erodes it. Measured after any IPO or spin-off.",
    "E9": "A strong balance sheet protects the downside.",
    "E10": "Micro caps were the weakest group among small-cap winners.",
    "E11": "Room to grow; large caps belong in Core.",
    "E12": "Winners started at modest multiples; the case must work without the multiple rising. Capital-heavy "
           "businesses are valued on EBIT, since EBITDA flatters them.",
    "E13": _VOL,
    "S2": "Special situations work best in good businesses bought cheaply.",
    "S3": "Debt turns the equity into an option bet.",
    "S4": "Value on pre-tax operating earnings; about 10x EBIT matches a bond-like yield.",
    "S5": _TRADE, "S6": _VOL,
    "F1": "A long record, including 2020.",
    "F3": _SIZE,
    "F4": "Earnings that hold up in a recession protect the stock.",
    "F5": "The same test for 2008-09; an operating loss in a recession year fails.",
    "F6": "Fortress businesses don't post operating losses.",
    "F7": "Stable margins over 10 years signal a predictable business.",
    "F8": "Set below Core so asset-heavy toll collectors such as rail and waste qualify.",
    "F9": "Survive first: leverage that can't be refinanced breaks companies.",
    "F10": "Debt rolls over at today's rates; coverage must hold at them.",
    "F11": "Maturities larger than cash can cause a liquidity crisis.",
    "F12": "Positive free cash flow almost every year.",
    "F13": "Margins that held through 2021-23 inflation show pricing power.",
    "H1": "Enough history to judge durability.",
    "H3": _SIZE,
    "H4": "Commercial stage: profitable in at least 4 of the last 5 years. Not applied to a new launcher (profitable "
          "now, revenue up 25%+ a year), whose losses were the development years.",
    "H5": "Pharma and health care are persistently high-return sectors; demand returns to match. Not applied to a "
          "new launcher.",
    "H6": "Commercial drugs earn 80-90% gross margins, so drug makers need at least 65% (diversified groups with device arms run in the high 60s); devices and tools less.",
    "H7": "Profits must turn into cash, after the cost of stock pay.",
    "H8": "Avoid levered roll-ups.",
    "H9": "Shrinking sales are how patent cliffs show up.",
    "B1": "Cash burns fast, so the cash figure must be recent.",
    "B3": "Debt and converts ahead of equity erode the cash floor.",
    "B4": _TRADE, "B5": _VOL,
    "B2": "Cash-burning biotechs depend on financing; avoid forced raises at the bottom. Near miss when one normal "
          "equity raise (up to a fifth of market value) would cover the next two years.",
    "B6": "Below its cash, a biotech rarely goes to zero: the market charges almost nothing for the pipeline.",
    "B7": "The floor must survive the burn: market value against the cash left after another year of spending, net "
          "of debt.",
    "C1": "A full cycle is needed to normalize earnings.",
    "C3": _SIZE,
    "C4": "A good business in a cyclical industry still earns well on capital mid-cycle.",
    "C5": "Profitable in most years of the cycle.",
    "C6": "No leverage a trough can break.",
    "C7": "Buy when margins are depressed, not when the industry is expanding.",
    "C8": "Value on cycle-average operating earnings, not peak ones.",
    "O1": "Enough years to judge returns.",
    "O3": _SIZE,
    "O4": "Owners run the company as its largest shareholders; float-weighted indexes under-own them.",
    "O5": "A real business, not a lottery ticket.",
    "O6": "Owners compound only if the business earns well on capital.",
    "O7": "Profits must turn into cash, after the cost of stock pay.",
    "O8": "Owners who borrow heavily can lose the company in one bad year.",
    "O9": _TRADE, "O10": _VOL,
    "O11": "Owner-operated companies often trade cheaply; don't overpay anyway.",
    "R1": "Enough years to see a cycle.",
    "R3": _SIZE,
    "R4": "Royalty and land owners need almost no reinvestment; producers and builders fail here.",
    "R5": "Owning the asset rather than working it shows up as very high margins.",
    "R6": "Profitable through commodity cycles.",
    "R7": "No leverage a commodity slump can break.",
    "R8": _TRADE, "R9": _VOL,
    "R10": "Even a perfect royalty can be bought too dear.",
    "K1": "Enough years to see a record.",
    "K3": "The floor is measured on the latest balance sheet, so it must be recent.",
    "K4": "Buying below cash gets the operating business for free. A discount to tangible book counts only while book "
          "value per share is still growing; a shrinking book is usually a value trap.",
    "K5": "A floor the company is burning through isn't a floor.",
    "K6": "A cheap business that never earns is a value trap.",
    "K7": "Debt ahead of shareholders erodes the floor.",
    "K8": _TRADE, "K9": _VOL,
    "T1": "A full cycle is needed to judge.",
    "T3": _SIZE,
    "T4": "Buy at the trough, not at mid-cycle.",
    "T5": "A cash machine pays you to wait: free cash flow positive in most years, troughs included.",
    "T6": "Capex near depreciation means maintaining, not adding capacity.",
    "T7": "No leverage a trough can break.",
    "T8": "Cycle-average free cash flow should repay the price within a few years.",
    "T9": _TRADE, "T10": _VOL,
    "X1": "Enough years to know the business.",
    "X3": "Coverage often fixates on a feared or departing segment; what remains can look better once it's gone.",
    "X4": "The remaining business must be profitable now.",
    "X5": "Revenue mustn't be in steady decline.",
    "X6": "Free cash flow positive over the last 12 months.",
    "X7": "A good business behind the mess.",
    "X8": "Debt turns a messy situation into an option bet.",
    "X9": "Special situations work best bought cheaply.",
    "X10": _TRADE, "X11": _VOL,
    "W1": "Enough years to see a trend.",
    "W3": "Overvaluation is the first half of a short; high EV/Sales names de-rate even without misses.",
    "W4": "Overvaluation plus deterioration: fading growth, falling margins, losses, heavy dilution, shrinking sales, "
          "profits not backed by cash, recurring 'one-off' charges, growth bought through acquisitions, piling "
          "inventory, or capex far above depreciation while burning cash.",
    "W5": "Big enough to matter to a portfolio.", "W6": _VOL,
    "A1": "Four years is the minimum to see growth, margins and stock pay move together.",
    "A3": _SIZE,
    "A4": "In technology, growth is the single biggest input to value.",
    "A5": "Missing on revenue is how tech stocks blow up; models assume a slow fade, so a sharp one surprises.",
    "A6": "Growth plus free cash flow margin of 40% marks the strongest cohort; stock pay is counted as the cost "
          "it is.",
    "A7": "Software at 40-60% gross margin can never reach software-level operating margins. Hardware margins "
          "start lower, so they must be rising; the biggest earnings upgrades come from a low margin base.",
    "A8": "On an S-curve with rising margins, earnings grow exponentially rather than linearly.",
    "A9": "Few companies keep stock pay under a fifth of free cash flow; above that, the cash flow belongs partly to "
          "staff.",
    "A10": "When value per share is the goal, buybacks and low dilution turn business growth into a bigger share "
           "price gain.",
    "A11": "Unlike the dot-com build-out, today's leaders fund spending from their own cash flow, not from debt or "
           "new shares.",
    "A12": "Growth only creates value when new investment earns above its cost of capital.",
    "A13": "Receivable days slipping out and inventories piling up were the warning signs before past tech busts.",
    "A14": _TRADE, "A15": _VOL,
    "A16": "To earn a 10x sales multiple, a company must grow around 30-35% a year. Leaders rarely screen as the "
           "cheapest, so failing only this rule makes a 'wait for a better price' near miss.",
}
PURPOSE = {
    "core": "Durable, high-return, predictable businesses to hold for years. Price is not a rule; valuation is "
            "shown for timing.",
    "emerging": "Profitable small and mid caps growing fast, with widening margins and little dilution, at a "
                "sensible price.",
    "special": "Spin-offs, post-bankruptcy companies and recent IPOs that are profitable and cheap on operating "
               "earnings.",
    "fortress": "Recession-proof earnings, stable margins and strong balance sheets. Lower returns than Core; "
                "resilience is the point.",
    "hc_commercial": "Profitable pharma, medtech, tools, services and insurers with durable returns.",
    "hc_clinical": "Pre-revenue and early-commercial biotech and medtech valued near or below cash, with 2+ years "
                   "of runway.",
    "cyclicals": "Good businesses in cyclical industries, bought when margins are low in their cycle and the price is "
                 "low against cycle-average earnings.",
    "owners": "Profitable, high-return companies where insiders own at least 20%.",
    "real_assets": "Owners of land, minerals, royalties, water, timber and pipelines that barely reinvest and earn "
                   "very high margins.",
    "asset_floor": "Companies priced at or below net cash or tangible book that still generate cash.",
    "trough_cash": "Cyclical producers at depressed margins that still generate cash, aren't adding capacity and "
                   "trade at a high cycle-average cash yield.",
    "hidden": "Profitable, cash-generating businesses the market is looking past: parents of a recent spin-off or "
              "sale, and sound companies far below their 12-month high.",
    "red_flags": "Avoid list, not a buy list: companies priced for perfection where something is already "
                 "deteriorating.",
    "tech": "Software, internet, semiconductor and hardware companies riding a technology S-curve: fast growth with "
            "widening margins, funded from their own cash, with stock pay kept in check, at a price the growth "
            "justifies.",
}
