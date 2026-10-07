"""SEC SIC-code groupings used by the screens.

SIC codes come from each company's SEC profile. They are coarse (a company has one code), so every screen
also shows the code and its description, and the Industry_Groups sheet lists the ranges used.
"""


def sic_int(sic):
    try:
        return int(str(sic)[:4])
    except (TypeError, ValueError):
        return None


def in_ranges(sic, ranges):
    s = sic_int(sic)
    if s is None:
        return None
    for r in ranges:
        lo, hi = r[0], r[1]
        if lo <= s <= hi:
            return r
    return None


# Healthcare (Healthcare screens). (from, to, label)
HEALTHCARE = [
    (2833, 2836, "Pharma, biotech & diagnostics"),
    (3826, 3826, "Lab & analytical instruments (life-science tools)"),
    (3841, 3845, "Medical devices & instruments"),
    (3851, 3851, "Ophthalmic goods"),
    (5047, 5047, "Medical equipment distribution"),
    (5122, 5122, "Drug distribution"),
    (6324, 6324, "Health insurers"),
    (8000, 8099, "Health services"),
    (8731, 8731, "Commercial biological research"),
]
# product businesses where a gross-margin test makes sense
HEALTHCARE_PRODUCT = [(2833, 2836), (3826, 3826), (3841, 3845), (3851, 3851)]
# where pre-revenue / clinical-stage companies sit
CLINICAL_STAGE = [(2833, 2836, "Pharma & biotech"), (8731, 8731, "Commercial biological research"),
                  (3841, 3845, "Medical devices")]

# Capacity-cycle groups (Cyclicals screen). Industry aggregates are computed per group label.
CYCLICAL = [
    (1000, 1099, "Metal mining"),
    (1220, 1241, "Coal"),
    (1311, 1311, "Oil & gas producers"),
    (1381, 1389, "Oilfield services & drilling"),
    (1400, 1499, "Aggregates & non-metal mining"),
    (1520, 1531, "Homebuilders"),
    (2400, 2499, "Wood & lumber"),
    (2600, 2699, "Paper & packaging"),
    (2800, 2829, "Chemicals"),
    (2850, 2899, "Chemicals"),
    (2911, 2911, "Refining"),
    (3200, 3299, "Building materials, glass & cement"),
    (3310, 3399, "Steel & metals"),
    (3510, 3569, "Machinery & equipment"),
    (3572, 3572, "Semiconductors & memory"),     # computer storage: SanDisk, Western Digital, Seagate
    (3674, 3674, "Semiconductors & memory"),
    (3711, 3716, "Autos, trucks & parts"),
    (4011, 4013, "Railroads"),
    (4210, 4231, "Trucking"),
    (4400, 4499, "Shipping"),
    (4512, 4513, "Airlines & air freight"),
]

# Hard Assets & Royalties screen: owners of land, minerals, water, timber and pipelines. Most of these codes are
# excluded from Core as price takers; the screen keeps only those that need little reinvestment (Stahl: a royalty
# is "a call option on everything"; "Being in energy or some other industry is not predictive. It's just descriptive").
REAL_ASSETS = [
    (800, 899, "Forestry & timberland"),
    (1000, 1099, "Metal mining & royalties"),
    (1311, 1389, "Oil & gas (incl. mineral & royalty owners)"),
    (1400, 1499, "Aggregates & non-metal mining"),
    (2400, 2411, "Timber"),
    (4610, 4619, "Pipelines"),
    (4922, 4925, "Gas transmission & storage"),
    (4941, 4941, "Water supply"),
    (6500, 6553, "Land & real-estate owners (not REITs)"),
    (6792, 6792, "Oil & gas royalty owners"),
    (6795, 6795, "Mineral royalty owners"),
]

# Extra exclusions for Emerging Compounders (Haley's study excluded energy, materials and financials;
# energy, metals, mining and financials are already in config exclude_sic).
EMERGING_EXTRA_EXCLUDE = [
    (2600, 2699, "Paper & packaging (materials)"),
    (2800, 2829, "Chemicals (materials)"),
    (2850, 2899, "Chemicals (materials)"),
    (3200, 3299, "Building materials (materials)"),
    (1400, 1499, "Non-metal mining (materials)"),
]

# Never screened: funds, blank checks, shells
NEVER = [(6722, 6726, "Funds & trusts"), (6770, 6770, "Blank checks / SPACs"), (6798, 6798, "REITs"),
         (9995, 9999, "Non-operating / shells")]
FINANCIALS = [(6000, 6799, "Financials")]


def group_rows():
    rows = []
    for name, lst in (("Healthcare", HEALTHCARE), ("Healthcare - clinical stage book", CLINICAL_STAGE),
                      ("Cyclicals", CYCLICAL), ("Hard assets & royalties", REAL_ASSETS),
                      ("Emerging - extra exclusions", EMERGING_EXTRA_EXCLUDE),
                      ("Never screened", NEVER)):
        for lo, hi, label in lst:
            rows.append({"screen": name, "sic_from": lo, "sic_to": hi, "label": label})
    return rows
