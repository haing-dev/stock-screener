"""Build an offline replica of the SEC and Twelve Data endpoints the screener uses, with known 'true' numbers.

Run:  python tests/make_fixtures.py  -> writes tests/fixtures/...
Each company is a small model with exactly-known financials, designed to land in a specific list of a specific
screen, so the rules can be checked by hand. 'Today' for the tests is 2025-06-30; the latest fiscal year is
2024 and a 10-Q for the quarter to 2025-03-31 provides trailing-twelve-month figures.
"""
import json
import os
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
FX = os.path.join(HERE, "fixtures")
TODAY = date(2025, 6, 30)


def w(path, obj, raw=False):
    full = os.path.join(FX, *path.split("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(obj if raw else json.dumps(obj))


D = dict  # shorthand
COMPANIES = [
    # ---------------- Core (and Fortress) ----------------
    D(cik=1001, ticker="GOOD", name="Goodco Ratings Inc.", exchange="Nasdaq", sic="7320",
      sicd="Services-Consumer Credit Reporting, Collection Agencies", growth=0.10, gm=0.60, om=0.35,
      debt_x_rev=0.5, split_year=2020, rev_tag_switch=2018, restate_2019=1.01, buyback=0.02, price=180.0),
    D(cik=1011, ticker="RIVL", name="Rival Ratings Corp", exchange="NYSE", sic="7320",
      sicd="Services-Consumer Credit Reporting, Collection Agencies", growth=0.08, gm=0.55, om=0.30,
      debt_x_rev=0.6, base=600),
    D(cik=1002, ticker="SLOW", name="Slowco Beverages Inc", exchange="NYSE", sic="2080", sicd="Beverages",
      growth=0.02, gm=0.60, om=0.28, debt_x_rev=0.4),
    D(cik=1003, ticker="LEVR", name="Leverco Entertainment Inc", exchange="NYSE", sic="7990",
      sicd="Services-Misc Amusement & Recreation", growth=0.09, gm=0.50, om=0.30, debt_x_rev=3.5, q_no_debt=True),
    D(cik=1004, ticker="BANK", name="Bankco Financial Corp", exchange="NYSE", sic="6022",
      sicd="State Commercial Banks", growth=0.06, gm=None, om=0.35, debt_x_rev=2.0),
    D(cik=1005, ticker="LOSS", name="Lossco Software Inc", exchange="Nasdaq", sic="7372",
      sicd="Services-Prepackaged Software", growth=0.30, gm=0.75, om=-0.10, debt_x_rev=0.1, losses_until=2021),
    D(cik=1006, ticker="IFRS", name="Formosa Chip Manufacturing Co Ltd", exchange="NYSE", sic="3674",
      sicd="Semiconductors & Related Devices", growth=0.14, gm=0.52, om=0.40, debt_x_rev=0.3,
      ifrs=True, currency="TWD", base=900000, form="20-F", price=150.0),
    D(cik=1007, ticker="NEGQ", name="Negative Equity Burgers Inc", exchange="NYSE", sic="5812",
      sicd="Retail-Eating Places", growth=0.07, gm=None, om=0.40, debt_x_rev=1.5, neg_equity=True),
    D(cik=1008, ticker="OTCC", name="Otc Widgets Inc", exchange="OTC", sic="3490", sicd="Misc Fabricated Metal",
      growth=0.10, gm=0.4, om=0.2, debt_x_rev=0.2),
    D(cik=1009, ticker="NEAR", name="Nearmiss Medical Devices Inc", exchange="Nasdaq", sic="3841",
      sicd="Surgical & Medical Instruments & Apparatus", growth=0.08, gm=0.62, om=0.17, debt_x_rev=0.5,
      ic_x_rev=1.0),
    D(cik=1010, ticker="JANF", name="January Warehouse Clubs Corp", exchange="NYSE", sic="5331",
      sicd="Retail-Variety Stores", growth=0.09, gm=0.125, om=0.035, debt_x_rev=0.03, jan_fy=True, ic_x_rev=0.12),
    D(cik=1012, ticker="NCPX", name="Nocapex Payroll Services Inc", exchange="Nasdaq", sic="7374",
      sicd="Services-Computer Processing & Data Preparation", growth=0.07, gm=0.45, om=0.25, debt_x_rev=0.2,
      capex_tag=None),  # capex not tagged with any standard tag -> Core CHECK, not FAIL
    D(cik=1013, ticker="ALTX", name="Altcapex Logistics Inc", exchange="NYSE", sic="7389",
      sicd="Services-Business Services, NEC", growth=0.08, gm=0.40, om=0.22, debt_x_rev=0.3,
      capex_tag="PaymentsToAcquireNetPropertyPlantAndEquipmentAltTag"),  # found by the fallback pattern
    # ---------------- Fortress ----------------
    D(cik=1101, ticker="FORT", name="Fortress Waste Systems Inc", exchange="NYSE", sic="4953",
      sicd="Refuse Systems", growth=0.05, gm=0.40, om=0.20, debt_x_rev=0.4, ic_x_rev=1.2, start=2007,
      shocks={2009: (0.97, None), 2020: (0.98, None)}, price=90.0),
    D(cik=1102, ticker="SHOK", name="Shockco Travel Services Inc", exchange="NYSE", sic="7011",
      sicd="Hotels & Motels", growth=0.06, gm=0.45, om=0.22, debt_x_rev=0.6, start=2007,
      shocks={2009: (0.95, None), 2020: (0.70, 0.05)}),
    # ---------------- Emerging ----------------
    D(cik=1201, ticker="EMRG", name="Emergeco Software Inc", exchange="Nasdaq", sic="7372",
      sicd="Services-Prepackaged Software", growth=0.25, gm=0.60, om_path={2020: 0.06, 2021: 0.08, 2022: 0.10,
                                                                         2023: 0.12, 2024: 0.14},
      debt_x_rev=0.1, start=2020, base=150, buyback=-0.01, sga_path=True, price=18.0, dei_shares=60e6),
    D(cik=1202, ticker="DILU", name="Dilutive Growth Corp", exchange="Nasdaq", sic="7372",
      sicd="Services-Prepackaged Software", growth=0.30, gm=0.65, om_path={2020: 0.05, 2021: 0.07, 2022: 0.09,
                                                                          2023: 0.11, 2024: 0.13},
      debt_x_rev=0.0, start=2020, base=120, buyback=-0.08, price=20.0, dei_shares=70e6),
    D(cik=1203, ticker="PRCY", name="Pricey Growth Inc", exchange="Nasdaq", sic="7372",
      sicd="Services-Prepackaged Software", growth=0.25, gm=0.62, om_path={2020: 0.06, 2021: 0.08, 2022: 0.10,
                                                                          2023: 0.12, 2024: 0.14},
      debt_x_rev=0.0, start=2020, base=150, buyback=0.0, price=150.0, dei_shares=60e6),
    # ---------------- Special situations ----------------
    D(cik=1301, ticker="SPIN", name="Spinco Industrial Holdings Inc", exchange="NYSE", sic="3560",
      sicd="General Industrial Machinery & Equipment", growth=0.04, gm=0.35, om=0.15, debt_x_rev=0.8,
      start=2021, base=2000, events=[("10-12B", "2023-09-15", []), ("10-12B/A", "2023-12-01", [])],
      price=25.0, dei_shares=100e6),
    D(cik=1302, ticker="REOR", name="Reorg Retail Partners Inc", exchange="NYSE", sic="5940",
      sicd="Retail-Miscellaneous Shopping Goods Stores", growth=0.02, gm=0.40, om=0.08, debt_x_rev=0.3,
      events=[("8-K", "2023-02-10", ["1.03", "9.01"])], price=12.0, dei_shares=50e6),
    D(cik=1303, ticker="NIPO", name="Newipo Rockets Inc", exchange="Nasdaq", sic="3760",
      sicd="Guided Missiles & Space Vehicles & Parts", growth=0.40, gm=0.20, om=-0.20, debt_x_rev=0.0,
      start=2021, base=200, events=[("S-1", "2024-01-05", []), ("424B4", "2024-02-01", [])], new_company=True,
      price=10.0, dei_shares=100e6),
    # ---------------- Healthcare ----------------
    D(cik=1401, ticker="PHRM", name="Pharmaco Therapeutics Inc", exchange="NYSE", sic="2834",
      sicd="Pharmaceutical Preparations", growth=0.06, gm=0.82, om=0.30, debt_x_rev=0.8, rnd=0.18, price=70.0),
    D(cik=1402, ticker="BIOX", name="Bioxa Clinical Inc", exchange="Nasdaq", sic="2836",
      sicd="Biological Products, (No Diagnostic Substances)", clinical=dict(cash=500e6, burn=100e6, debt=0.0),
      start=2019, price=3.0, dei_shares=50e6, avg_volume=500000),
    D(cik=1404, ticker="NREV", name="Norevenue Gene Therapies Inc", exchange="Nasdaq", sic="2836",
      sicd="Biological Products, (No Diagnostic Substances)", clinical=dict(cash=400e6, burn=80e6, debt=0.0),
      start=2019, price=2.0, dei_shares=50e6, avg_volume=500000, no_revenue_tags=True),
    D(cik=1405, ticker="NEWS", name="Newspin Technologies Inc", exchange="NYSE", sic="3570",
      sicd="Computer & Office Equipment", events_only=True, events=[("10-12B", "2025-04-01", [])]),
    D(cik=1403, ticker="BURN", name="Burnrate Bio Inc", exchange="Nasdaq", sic="2834",
      sicd="Pharmaceutical Preparations", clinical=dict(cash=120e6, burn=110e6, debt=0.0),
      start=2019, price=2.0, dei_shares=50e6, avg_volume=500000),
    # ---------------- Cyclicals ----------------
    D(cik=1501, ticker="STEL", name="Steelworks Corp", exchange="NYSE", sic="3312",
      sicd="Steel Works, Blast Furnaces & Rolling Mills", growth=0.03, gm=0.20,
      om_path={2015: 0.06, 2016: 0.08, 2017: 0.12, 2018: 0.16, 2019: 0.10, 2020: 0.05, 2021: 0.20, 2022: 0.22,
               2023: 0.12, 2024: 0.07}, debt_x_rev=0.1, ic_x_rev=0.5, start=2012, base=3000, price=40.0,
      dei_shares=100e6),
    D(cik=1502, ticker="STL2", name="Second Steel Co", exchange="NYSE", sic="3312",
      sicd="Steel Works, Blast Furnaces & Rolling Mills", growth=0.03, gm=0.18,
      om_path={2015: 0.05, 2016: 0.07, 2017: 0.10, 2018: 0.14, 2019: 0.09, 2020: 0.04, 2021: 0.18, 2022: 0.20,
               2023: 0.10, 2024: 0.05}, debt_x_rev=0.5, ic_x_rev=0.7, start=2012, base=2000),
    D(cik=1503, ticker="STL3", name="Third Metals Inc", exchange="NYSE", sic="3350",
      sicd="Rolling Drawing & Extruding of Nonferrous Metals", growth=0.03, gm=0.18,
      om_path={2015: 0.04, 2016: 0.06, 2017: 0.09, 2018: 0.12, 2019: 0.08, 2020: 0.03, 2021: 0.16, 2022: 0.18,
               2023: 0.09, 2024: 0.04}, debt_x_rev=0.4, ic_x_rev=0.7, start=2012, base=1500),
    D(cik=1504, ticker="PEAK", name="Peakchem Corp", exchange="NYSE", sic="2821",
      sicd="Plastic Materials, Synth Resins & Nonvulcan Elastomers", growth=0.03, gm=0.30,
      om_path={2015: 0.08, 2016: 0.08, 2017: 0.09, 2018: 0.08, 2019: 0.08, 2020: 0.07, 2021: 0.09, 2022: 0.10,
               2023: 0.20, 2024: 0.24}, surge={2023: 1.4, 2024: 1.65}, debt_x_rev=0.2, ic_x_rev=0.5, start=2012,
      base=1000),
]

END_YEAR = 2024


def fy_end(c, y):
    if c.get("jan_fy"):
        d = date(y + 1, 1, 31)
        return d - timedelta(days=(d.weekday() + 1) % 7)
    return date(y, 12, 31)


def model(c):
    """Annual truth for each fiscal year, plus the Q1 2024 and Q1 2025 year-to-date figures."""
    start = c.get("start", 2012)
    years = list(range(start, END_YEAR + 1))
    out = {}
    base = c.get("base", 1000) * 1e6
    shares = 100e6
    rev = base
    for i, y in enumerate(years):
        if i:
            rev *= 1 + c.get("growth", 0.05)
        r = rev
        shock = (c.get("shocks") or {}).get(y)
        if shock:
            r = rev * shock[0]
        if (c.get("surge") or {}).get(y):
            r = rev * c["surge"][y]
        gm = c.get("gm")
        if gm is not None and y == 2022:
            gm -= 0.01
        if gm is not None and y >= 2023 and not c.get("om_path"):
            gm += 0.02
        om = c.get("om", 0.1)
        if c.get("om_path"):
            om = c["om_path"].get(y, sum(c["om_path"].values()) / len(c["om_path"]))
        if shock and shock[1] is not None:
            om = shock[1]
        if c.get("losses_until") and y <= c["losses_until"]:
            om = -0.10
        elif c.get("losses_until"):
            om = 0.05
        if c.get("clinical"):
            cl_ = c["clinical"]
            r = 1e6 * (1 if y >= 2023 else 0)
            op = -cl_["burn"]
            gm = None
        else:
            op = r * om
        da = abs(r) * 0.04
        interest = abs(r) * c.get("debt_x_rev", 0) * 0.04
        pretax = op - interest * 0.0
        tax = pretax * 0.21 if pretax > 0 else 0.0
        ni = pretax - tax
        if c.get("clinical"):
            ocf, capex = -c["clinical"]["burn"], 1e6
        else:
            ocf = ni * 1.15 + r * 0.02
            capex = r * 0.04
        ic = r * c.get("ic_x_rev", 0.6)
        cash = r * 0.10 if not c.get("clinical") else c["clinical"]["cash"]
        debt = r * c.get("debt_x_rev", 0) if not c.get("clinical") else c["clinical"]["debt"]
        cl = abs(r) * 0.25 if not c.get("clinical") else 20e6
        cur_debt = debt * 0.05
        assets = ic + cash + (cl - cur_debt) if not c.get("clinical") else cash + 50e6
        equity = assets - cl - (debt - cur_debt) - abs(r) * 0.05
        if c.get("neg_equity"):
            equity = -r * 0.3
        shares *= (1 - c.get("buyback", 0.01))
        sga = r * (0.30 - 0.02 * i) if c.get("sga_path") else r * 0.2
        ca = cl * 1.5 if not c.get("clinical") else cash + 5e6
        ppe = r * 0.3 if not c.get("clinical") else 10e6
        out[y] = dict(rev=r, gp=(r * gm if gm is not None else None), op=op, pretax=pretax, tax=tax, ni=ni,
                      ocf=ocf, capex=capex, cash=cash, debt=debt, cur_debt=cur_debt, cl=cl, assets=assets,
                      equity=equity, shares=shares, sbc=abs(r) * 0.02, acq=abs(r) * 0.03, goodwill=max(assets, 0) * 0.1,
                      buyback=abs(r) * 0.05, div=abs(r) * 0.04, da=da, interest=interest, sga=sga, ca=ca, ppe=ppe,
                      due1=debt * 0.05, due2=debt * 0.05)
    # quarterly: Q1 of year y = 25% of the annual figure, grown at the company's growth rate for 2025
    last = out[END_YEAR]
    g = c.get("growth", 0.05)
    q24 = {k: (v * 0.25 if isinstance(v, (int, float)) else v) for k, v in last.items()}
    q25 = {k: (v * 0.25 * (1 + g) if isinstance(v, (int, float)) else v) for k, v in last.items()}
    if c.get("clinical"):
        q25 = {k: (v * 0.25 if isinstance(v, (int, float)) else v) for k, v in last.items()}
    bs25 = {k: last[k] * (1 + g) ** 0.25 for k in ("cash", "debt", "cur_debt", "cl", "assets", "equity", "goodwill",
                                                   "ca", "ppe")}
    if c.get("clinical"):
        bs25 = dict(last)
        bs25["cash"] = last["cash"] - c["clinical"]["burn"] * 0.25
        bs25["assets"] = bs25["cash"] + 50e6
    return out, q24, q25, bs25


def build(c):
    if c.get("events_only"):   # a new spin-off: SEC profile with a Form 10, no XBRL financials yet
        recent = {k: [] for k in ("accessionNumber", "filingDate", "reportDate", "form", "primaryDocument", "items")}
        for i, (frm, dt, items) in enumerate(c["events"]):
            for k, v in (("accessionNumber", f"0000{c['cik']}-ev-{i:06d}"), ("filingDate", dt), ("reportDate", dt),
                         ("form", frm), ("primaryDocument", "form10.htm"), ("items", ",".join(items))):
                recent[k].append(v)
        w(f"data.sec.gov/submissions/CIK{c['cik']:010d}.json",
          {"cik": f"{c['cik']:010d}", "entityType": "operating", "sic": c["sic"], "sicDescription": c["sicd"],
           "name": c["name"], "tickers": [c["ticker"]], "exchanges": [c["exchange"]], "fiscalYearEnd": "1231",
           "filings": {"recent": recent, "files": []}})
        return
    ifrs = bool(c.get("ifrs"))
    tx = "ifrs-full" if ifrs else "us-gaap"
    cur = c.get("currency", "USD")
    form = c.get("form", "10-K")
    truth, q24, q25, bs25 = model(c)
    years = sorted(truth)
    facts = {}

    def add(tag, unit, entry, taxonomy=tx):
        facts.setdefault(taxonomy, {}).setdefault(tag, {"label": tag, "description": "", "units": {}})["units"]\
            .setdefault(unit, []).append(entry)

    tagmap = {
        "rev": ("Revenue" if ifrs else "Revenues"),
        "gp": "GrossProfit",
        "op": ("ProfitLossFromOperatingActivities" if ifrs else "OperatingIncomeLoss"),
        "pretax": ("ProfitLossBeforeTax" if ifrs else
                   "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"),
        "tax": ("IncomeTaxExpenseContinuingOperations" if ifrs else "IncomeTaxExpenseBenefit"),
        "ni": ("ProfitLossAttributableToOwnersOfParent" if ifrs else "NetIncomeLoss"),
        "ocf": ("CashFlowsFromUsedInOperatingActivities" if ifrs else "NetCashProvidedByUsedInOperatingActivities"),
        "capex": ("PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities" if ifrs
                  else (c["capex_tag"] if "capex_tag" in c else "PaymentsToAcquirePropertyPlantAndEquipment")),
        "sbc": ("AdjustmentsForSharebasedPayments" if ifrs else "ShareBasedCompensation"),
        "acq": ("CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities"
                if ifrs else "PaymentsToAcquireBusinessesNetOfCashAcquired"),
        "buyback": ("PaymentsToAcquireOrRedeemEntitysShares" if ifrs else "PaymentsForRepurchaseOfCommonStock"),
        "div": ("DividendsPaidClassifiedAsFinancingActivities" if ifrs else "PaymentsOfDividends"),
        "shares": ("AdjustedWeightedAverageShares" if ifrs else "WeightedAverageNumberOfDilutedSharesOutstanding"),
        "da": ("DepreciationAndAmortisationExpense" if ifrs else "DepreciationDepletionAndAmortization"),
        "interest": ("FinanceCosts" if ifrs else "InterestExpense"),
        "sga": ("SellingGeneralAndAdministrativeExpense"),
        "assets": "Assets",
        "cl": ("CurrentLiabilities" if ifrs else "LiabilitiesCurrent"),
        "ca": ("CurrentAssets" if ifrs else "AssetsCurrent"),
        "ppe": ("PropertyPlantAndEquipment" if ifrs else "PropertyPlantAndEquipmentNet"),
        "equity": ("EquityAttributableToOwnersOfParent" if ifrs else "StockholdersEquity"),
        "cash": ("CashAndCashEquivalents" if ifrs else "CashAndCashEquivalentsAtCarryingValue"),
        "debt_total": ("Borrowings" if ifrs else "LongTermDebt"),
        "cur_debt": ("CurrentPortionOfNoncurrentBorrowings" if ifrs else "LongTermDebtCurrent"),
        "goodwill": "Goodwill",
        "due1": "LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths",
        "due2": "LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo",
    }
    flow_keys = ("rev", "gp", "op", "pretax", "tax", "ni", "ocf", "capex", "sbc", "acq", "buyback", "div", "da",
                 "interest", "sga")
    inst_keys = ("assets", "cl", "ca", "ppe", "equity", "cash", "goodwill")
    filings = []
    n = 0
    for t in years[2:] if len(years) > 2 else years:
        n += 1
        end_t = fy_end(c, t)
        filed = (end_t + timedelta(days=55)).isoformat()
        accn = f"0000{c['cik']}-{str(t + 1)[2:]}-{n:06d}"
        filings.append((t, accn, filed, end_t, form))
        for y in (t, t - 1, t - 2):
            if y not in truth:
                continue
            v = truth[y]
            start = fy_end(c, y - 1) + timedelta(days=1)
            end = fy_end(c, y)
            base = {"start": start.isoformat(), "end": end.isoformat(), "accn": accn, "fy": t, "fp": "FY",
                    "form": form, "filed": filed}
            for key in flow_keys:
                val = v[key]
                if val is None:
                    continue
                tag = tagmap[key]
                if tag is None or (key in ("rev", "gp") and c.get("no_revenue_tags")):
                    continue
                if key == "rev" and c.get("rev_tag_switch") and not ifrs:
                    tag = "SalesRevenueNet" if y < c["rev_tag_switch"] else "RevenueFromContractWithCustomerExcludingAssessedTax"
                if key == "rev" and c.get("restate_2019") and y == 2019 and t == 2020:
                    val = val * c["restate_2019"]
                add(tag, cur, {**base, "val": round(val)})
            sh = v["shares"]
            if c.get("split_year") and t >= c["split_year"]:
                sh *= 2
            add(tagmap["shares"], "shares", {**base, "val": round(sh)})
        for y in (t, t - 1):
            if y not in truth:
                continue
            v = truth[y]
            base = {"end": fy_end(c, y).isoformat(), "accn": accn, "fy": t, "fp": "FY", "form": form, "filed": filed}
            for key in inst_keys:
                add(tagmap[key], cur, {**base, "val": round(v[key])})
            add(tagmap["debt_total"], cur, {**base, "val": round(v["debt"])})
            add(tagmap["cur_debt"], cur, {**base, "val": round(v["cur_debt"])})
            if not ifrs and v["debt"]:
                add(tagmap["due1"], cur, {**base, "val": round(v["due1"])})
                add(tagmap["due2"], cur, {**base, "val": round(v["due2"])})
    # 10-Q for Q1 2025 (with the Q1 2024 comparative), US filers only
    if form == "10-K" and not c.get("jan_fy"):
        qaccn = f"0000{c['cik']}-25-900001"
        qfiled = "2025-05-05"
        filings.append((2025, qaccn, qfiled, date(2025, 3, 31), "10-Q"))
        for period, vals in (((date(2025, 1, 1), date(2025, 3, 31)), q25), ((date(2024, 1, 1), date(2024, 3, 31)), q24)):
            base = {"start": period[0].isoformat(), "end": period[1].isoformat(), "accn": qaccn, "fy": 2025,
                    "fp": "Q1", "form": "10-Q", "filed": qfiled}
            for key in flow_keys:
                if vals.get(key) is None or tagmap[key] is None or (key in ("rev", "gp") and c.get("no_revenue_tags")):
                    continue
                tag = tagmap[key]
                if key == "rev" and c.get("rev_tag_switch"):
                    tag = "RevenueFromContractWithCustomerExcludingAssessedTax"
                add(tag, cur, {**base, "val": round(vals[key])})
            add(tagmap["shares"], "shares", {**base, "val": round(vals["shares"] / 0.25 *
                                                                  (2 if c.get("split_year") else 1))})
        base = {"end": "2025-03-31", "accn": qaccn, "fy": 2025, "fp": "Q1", "form": "10-Q", "filed": qfiled}
        for key in inst_keys:
            add(tagmap[key], cur, {**base, "val": round(bs25[key])})
        if not c.get("q_no_debt"):
            add(tagmap["debt_total"], cur, {**base, "val": round(bs25["debt"])})
            add(tagmap["cur_debt"], cur, {**base, "val": round(bs25["cur_debt"])})
    cf = {"cik": c["cik"], "entityName": c["name"], "facts": facts}
    last_shares = truth[years[-1]]["shares"] * (2 if c.get("split_year") else 1)
    dei_sh = c.get("dei_shares", last_shares)
    facts.setdefault("dei", {})["EntityCommonStockSharesOutstanding"] = {"units": {"shares": [
        {"end": "2025-04-25", "val": round(dei_sh), "accn": "x", "fy": 2025, "fp": "Q1", "form": "10-Q",
         "filed": "2025-05-05"}]}}
    if c.get("price") and not ifrs:
        facts["dei"]["EntityPublicFloat"] = {"units": {"USD": [
            {"end": "2024-06-30", "val": round(dei_sh * c["price"] * 0.9), "accn": "x", "fy": 2024, "fp": "FY",
             "form": "10-K", "filed": "2025-02-20"}]}}
    w(f"data.sec.gov/api/xbrl/companyfacts/CIK{c['cik']:010d}.json", cf)

    recent = {"accessionNumber": [], "filingDate": [], "reportDate": [], "form": [], "primaryDocument": [],
              "items": []}
    allf = [(f[1], f[2], f[3].isoformat(), f[4], "") for f in filings]
    for i, (frm, dt, items) in enumerate(c.get("events") or []):
        allf.append((f"0000{c['cik']}-ev-{i:06d}", dt, dt, frm, ",".join(items)))
    for accn, filed, rep, frm, items in sorted(allf, key=lambda x: x[1], reverse=True):
        doc = f"{c['ticker'].lower()}-{rep.replace('-', '')}.htm"
        for k, v in (("accessionNumber", accn), ("filingDate", filed), ("reportDate", rep), ("form", frm),
                     ("primaryDocument", doc), ("items", items)):
            recent[k].append(v)
    files = [] if c.get("new_company") or c.get("start", 2012) >= 2021 else [{"name": "CIK-submissions-001.json"}]
    sub = {"cik": f"{c['cik']:010d}", "entityType": "operating", "sic": c["sic"], "sicDescription": c["sicd"],
           "name": c["name"], "tickers": [c["ticker"]], "exchanges": [c["exchange"]],
           "fiscalYearEnd": fy_end(c, 2024).strftime("%m%d"), "category": "Large accelerated filer",
           "stateOfIncorporation": "DE", "filings": {"recent": recent, "files": files}}
    w(f"data.sec.gov/submissions/CIK{c['cik']:010d}.json", sub)
    t, accn, filed, end_t, frm = [f for f in filings if f[4] != "10-Q"][-1]
    doc = f"{c['ticker'].lower()}-{end_t.isoformat().replace('-', '')}.htm"
    w(f"www.sec.gov/Archives/edgar/data/{c['cik']}/{accn.replace('-', '')}/{doc}", tenk_html(c, form), raw=True)


def tenk_html(c, form):
    nm = c["name"]
    if form == "20-F":
        items = [("4", "Information on the Company"), ("3", "Key Information"), ("5", "Operating and Financial Review")]
    else:
        items = [("1", "Business"), ("1A", "Risk Factors"), ("7", "Management&#8217;s Discussion and Analysis")]
    body = ['<html><head><title>10-K</title></head><body>',
            '<div style="display:none"><ix:header><ix:hidden>HIDDEN XBRL STUFF 12345</ix:hidden></ix:header></div>',
            '<p><span>TABLE OF CONTENTS</span></p>']
    for k, title in items:
        body.append(f'<p><a href="#i{k}"><span>Item {k}.</span></a> <span>{title}</span></p>')
    para = ("<p><span>{nm}</span> <span style='font-weight:bold'>is the leading provider</span> of credit ratings, "
            "and our ratings are required by regulation for issuers seeking access to public debt markets. "
            "We have raised prices in each of the last five years while retention of customers remained above 95 percent. "
            "Our two largest competitors and we together account for the substantial majority of ratings issued, "
            "and switching providers would require issuers to obtain new ratings from scratch.</p>")
    filler = "<p>" + ("This sentence adds general descriptive content about operations, employees, and properties of the company. " * 6) + "</p>"
    for k, title in items:
        body.append(f'<p id="i{k}"><b>ITEM {k}.</b> <b>{title.upper()}</b></p>')
        body.append(para.format(nm=nm))
        body += [filler] * 10
        if k in ("1A", "3"):
            body.append("<p>Competition from new entrants using artificial intelligence could pressure our pricing and market share, "
                        "and regulators may seek to limit the fees we charge to issuers in certain jurisdictions over time.</p>")
        body.append('<table><tr><td>Revenue</td><td><ix:nonFraction name="us-gaap:Revenues">1,000</ix:nonFraction></td></tr></table>')
    body.append('<p><b>Item 8.</b> Financial Statements</p><p>Numbers here.</p></body></html>')
    return "\n".join(body)


def twelvedata():
    q = {}
    for c in COMPANIES:
        if not c.get("price"):
            continue
        ex = {"Nasdaq": "NASDAQ", "NYSE": "NYSE"}.get(c["exchange"], c["exchange"])
        q[c["ticker"]] = {"symbol": c["ticker"], "name": c["name"], "exchange": ex, "mic_code": "XNYS",
                          "currency": "USD", "datetime": "2025-06-27", "timestamp": 1751000000,
                          "open": str(c["price"]), "high": str(c["price"]), "low": str(c["price"]),
                          "close": str(c["price"]), "volume": "100000", "previous_close": str(c["price"]),
                          "change": "0", "percent_change": "0",
                          "average_volume": str(c.get("avg_volume", 2000000)), "is_market_open": False,
                          "fifty_two_week": {"low": str(c["price"] * 0.7), "high": str(c["price"] * 1.3)}}
    # a quote that comes back from the wrong market must be rejected
    if "GOOD" in q:
        pass
    w("twelvedata/quote.json", q)
    w("twelvedata/api_usage.json", {"timestamp": "2025-06-30 10:00:00", "current_usage": 0, "plan_limit": 120,
                                    "daily_usage": 0, "plan_daily_limit": 100000, "plan_category": "fixture"})
    w("twelvedata/exchange_rate.json", {"TWD/USD": {"symbol": "TWD/USD", "rate": 0.031, "timestamp": 1751000000}})
    # listing types: the foreign issuer trades as an ADR, everything else as common stock
    w("twelvedata/stocks.json", {"status": "ok", "data": [
        {"symbol": c["ticker"], "name": c["name"], "currency": "USD",
         "exchange": {"Nasdaq": "NASDAQ"}.get(c["exchange"], c["exchange"]),
         "type": "Depositary Receipt" if c.get("form") == "20-F" else "Common Stock"} for c in COMPANIES]})
    # closing prices on past dates (public-float date checks)
    w("twelvedata/time_series.json", {})


def main():
    rows = [[c["cik"], c["name"], c["ticker"], c["exchange"]] for c in COMPANIES]
    w("www.sec.gov/files/company_tickers_exchange.json", {"fields": ["cik", "name", "ticker", "exchange"], "data": rows})
    for c in COMPANIES:
        build(c)
    twelvedata()
    print("fixtures written to", FX)


if __name__ == "__main__":
    main()
