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

# Tech S-curve screen: two branches with different gross-margin and working-capital rules
TECH_SOFTWARE = [(7370, 7379, "Software, internet & IT services")]
TECH_HARDWARE = [(3570, 3579, "Computers & storage"), (3661, 3669, "Communications equipment"),
                 (3670, 3679, "Semiconductors & electronic components"),
                 (3825, 3825, "Electronic test & measurement"), (3827, 3827, "Optical instruments & lenses")]

# Never screened: funds, blank checks, shells
NEVER = [(6722, 6726, "Funds & trusts"), (6770, 6770, "Blank checks / SPACs"), (6798, 6798, "REITs"),
         (9995, 9999, "Non-operating / shells")]
FINANCIALS = [(6000, 6799, "Financials")]


def group_rows():
    rows = []
    for name, lst in (("Healthcare", HEALTHCARE), ("Healthcare - clinical stage book", CLINICAL_STAGE),
                      ("Cyclicals", CYCLICAL), ("Hard assets & royalties", REAL_ASSETS),
                      ("Emerging - extra exclusions", EMERGING_EXTRA_EXCLUDE),
                      ("Tech S-curve - software branch", TECH_SOFTWARE), ("Tech S-curve - hardware branch", TECH_HARDWARE),
                      ("Never screened", NEVER)):
        for lo, hi, label in lst:
            rows.append({"screen": name, "sic_from": lo, "sic_to": hi, "label": label})
    return rows


# Excel 3-statement model templates (site/model.js buildModel): which lines and ratios fit the business
MODEL_TEMPLATES = [
    ((7370, 7379), "software"),
    ((6300, 6411), "insurer"),
    ((8000, 8099), "hc_services"), ((5047, 5047), "hc_services"), ((5122, 5122), "hc_services"),
    ((1520, 1531), "homebuilder"),
    ((100, 1499), "resources"), ((2400, 2411), "resources"), ((2911, 2911), "resources"),
    ((4610, 4619), "resources"), ((4922, 4925), "resources"), ((6792, 6792), "resources"), ((6795, 6795), "resources"),
    ((3570, 3579), "tech_hw"), ((3600, 3699), "tech_hw"), ((3825, 3825), "tech_hw"),
    ((4000, 4799), "transport"),
    ((2000, 2399), "consumer"), ((2840, 2844), "consumer"), ((3140, 3149), "consumer"), ((3940, 3949), "consumer"),
    ((5000, 5999), "consumer"), ((7000, 7299), "consumer"), ((7800, 7999), "consumer"),
]
HC_PRODUCTS = [(2833, 2836), (3826, 3826), (3841, 3845), (3851, 3851), (8731, 8731)]


def model_template(sic, revenue=None, rnd=None, operating_income=None):
    """Template id for the Excel model. Drug, device and research companies with little revenue (or spending more on
    R&D than half their sales while losing money) get the clinical-stage layout (cash, burn, runway)."""
    s = sic_int(sic)
    if s is None:
        return "industrial"
    if in_ranges(s, HC_PRODUCTS):
        early = revenue is None or revenue < 100e6 or (
            rnd is not None and revenue and rnd > 0.5 * revenue and (operating_income or 0) < 0)
        return "biotech" if early else "hc_products"
    for (lo, hi), t in MODEL_TEMPLATES:
        if lo <= s <= hi:
            return t
    return "industrial"
