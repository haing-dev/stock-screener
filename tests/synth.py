"""Synthetic companyfacts subsets for probing the screener."""
import sys
from datetime import date
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__))))


def annual_entries(vals, kind="duration", fye_month=12, form="10-K"):
    out = []
    for y, v in vals.items():
        end = f"{y}-12-31" if fye_month == 12 else f"{y}-{fye_month:02d}-30"
        e = {"end": end, "val": v, "accn": f"0000000000-{y + 1 - 2000:02d}-000001", "fy": y + 1, "fp": "FY",
             "form": form, "filed": f"{y + 1}-02-15"}
        if kind == "duration":
            e["start"] = f"{y}-01-01"
        out.append(e)
    return out


def q_entries(vals):
    """vals: list of (start, end, val, filed)"""
    return [{"start": s, "end": e, "val": v, "accn": f"q-{e}", "fy": int(e[:4]), "fp": "Q", "form": "10-Q",
             "filed": f} for s, e, v, f in vals]


def build(spec, unit="USD", tax="us-gaap", extra=None):
    """spec: {tag: (kind, {year: val})}"""
    facts = {}
    for tag, (kind, vals) in spec.items():
        t = tax
        if ":" in tag:
            t, tag = tag.split(":")
        u = unit
        if tag.startswith("EarningsPerShare"):
            u = unit + "/shares"
        if tag.startswith("WeightedAverage"):
            u = "shares"
        facts.setdefault(t, {})[tag] = {u: annual_entries(vals, kind)}
    if extra:
        for t, tags in extra.items():
            for tag, units in tags.items():
                for u, ents in units.items():
                    facts.setdefault(t, {}).setdefault(tag, {}).setdefault(u, []).extend(ents)
    return {"subset_version": 4, "cik": 1, "entityName": "Synth Co", "facts": facts, "candidates": {}}


def yrs(a, b, f):
    return {y: f(y) for y in range(a, b + 1)}


def base_company(first=2007, last=2025, rev0=1e9, growth=0.10, om=0.20, ni_m=0.15, ocf_m=0.20, capex_m=0.03,
                 assets_x=0.8, extra_tags=None):
    rev = yrs(first, last, lambda y: rev0 * (1 + growth) ** (y - first))
    spec = {
        "Revenues": ("duration", rev),
        "OperatingIncomeLoss": ("duration", {y: v * om for y, v in rev.items()}),
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest":
            ("duration", {y: v * om * 0.98 for y, v in rev.items()}),
        "IncomeTaxExpenseBenefit": ("duration", {y: v * om * 0.98 * 0.21 for y, v in rev.items()}),
        "NetIncomeLoss": ("duration", {y: v * ni_m for y, v in rev.items()}),
        "NetCashProvidedByUsedInOperatingActivities": ("duration", {y: v * ocf_m for y, v in rev.items()}),
        "PaymentsToAcquirePropertyPlantAndEquipment": ("duration", {y: v * capex_m for y, v in rev.items()}),
        "DepreciationDepletionAndAmortization": ("duration", {y: v * 0.03 for y, v in rev.items()}),
        "Assets": ("instant", {y: v * assets_x for y, v in rev.items()}),
        "AssetsCurrent": ("instant", {y: v * 0.4 for y, v in rev.items()}),
        "LiabilitiesCurrent": ("instant", {y: v * 0.2 for y, v in rev.items()}),
        "CashAndCashEquivalentsAtCarryingValue": ("instant", {y: v * 0.1 for y, v in rev.items()}),
        "StockholdersEquity": ("instant", {y: v * 0.5 for y, v in rev.items()}),
        "PropertyPlantAndEquipmentNet": ("instant", {y: v * 0.2 for y, v in rev.items()}),
        "LongTermDebtNoncurrent": ("instant", {y: v * 0.1 for y, v in rev.items()}),
        "WeightedAverageNumberOfDilutedSharesOutstanding": ("duration", {y: 1e8 for y in rev}),
        "GrossProfit": ("duration", {y: v * 0.5 for y, v in rev.items()}),
    }
    if extra_tags:
        spec.update(extra_tags)
    return spec


def add_share_comparatives(d, tag="WeightedAverageNumberOfDilutedSharesOutstanding"):
    ents = d["facts"]["us-gaap"][tag]["shares"]
    extra = []
    for e in list(ents):
        y = int(e["end"][:4])
        extra.append(dict(e, start=f"{y - 1}-01-01", end=f"{y - 1}-12-31"))
    ents.extend(extra)
    return d
