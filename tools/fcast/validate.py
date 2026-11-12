"""Check a coded forecast file against the spec. usage: validate.py <coded.jsonl> <input batch.jsonl>"""
import json, re, sys

CODES = set("""US_EQ US_TECH US_SMALL EU_EQ JP_EQ CN_EQ IN_EQ EM_EQ GLOBAL_EQ EQ_SECTOR EQ_SINGLE EQ_VALUE_VS_GROWTH
US_POLICY_RATE US_2Y US_10Y US_30Y US_CURVE US_REAL_YIELD US_TERM_PREMIUM EU_RATES JP_RATES UK_RATES OTHER_RATES
USD EURUSD USDJPY GBPUSD USDCNY EM_FX OTHER_FX GOLD SILVER OIL NATGAS COPPER URANIUM AGRI COMMODITIES OTHER_COMMODITY
CREDIT_SPREADS PRIVATE_CREDIT VIX RATES_VOL US_GROWTH US_RECESSION US_INFLATION US_JOBS US_DEFICIT_DEBT GLOBAL_GROWTH
CN_GROWTH EU_GROWTH JP_INFLATION LIQUIDITY BTC REAL_ESTATE TREND_FOLLOWING HEDGE_FUNDS POLICY_EVENT GEOPOLITICS OTHER""".split())
ENUM = {"date_precision": {"day", "month", "quarter", "year"},
        "kind": {"forecast", "conditional", "stance", "not_forecast"},
        "direction": {"up", "down", "flat", "range", "outperform", "underperform", "higher_vol", "lower_vol", "event_yes", "event_no", None},
        "confidence": {"high", "medium", "low", "unstated"},
        "call_type": {"direction", "relative", "macro", "event", "volatility", "structural", None},
        "resolvable": {"yes", "partly", "no"},
        "why_not": {"no_horizon", "vague_variable", "no_direction", "unobservable", "conditional_unmet_unknown", None}}
FIELDS = ["view_id", "row", "who", "made_date", "date_precision", "kind", "variable_code", "variable_text", "direction", "level",
          "horizon_months", "horizon_text", "condition", "probability", "confidence", "call_type", "resolvable", "why_not",
          "claim_ids", "note"]
inp = {}
for ln in open(sys.argv[2]):
    r = json.loads(ln)
    inp[r["view_id"]] = r
err, seen = [], {}
for i, ln in enumerate(open(sys.argv[1]), 1):
    if not ln.strip():
        continue
    try:
        r = json.loads(ln)
    except Exception as e:
        err.append("line %d: not JSON (%s)" % (i, e)); continue
    v = r.get("view_id")
    miss = [f for f in FIELDS if f not in r]
    extra = [f for f in r if f not in FIELDS]
    if miss or extra:
        err.append("line %d %s: missing %s extra %s" % (i, v, miss, extra))
    if v not in inp:
        err.append("line %d: unknown view_id %s" % (i, v)); continue
    seen.setdefault(v, []).append(r.get("row"))
    for f, ok in ENUM.items():
        if r.get(f) not in ok:
            err.append("line %d %s: %s=%r not allowed" % (i, v, f, r.get(f)))
    if not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", str(r.get("made_date") or "")):
        err.append("line %d %s: made_date %r" % (i, v, r.get("made_date")))
    if r.get("who") != inp[v]["speaker"]:
        err.append("line %d %s: who must equal input speaker" % (i, v))
    if r.get("kind") == "not_forecast":
        if r.get("resolvable") != "no":
            err.append("line %d %s: not_forecast must have resolvable=no" % (i, v))
    else:
        vc = str(r.get("variable_code") or "")
        parts = vc.split(">")
        if not all(p in CODES for p in parts) or len(parts) > 2:
            err.append("line %d %s: variable_code %r" % (i, v, vc))
        if r.get("direction") is None or r.get("call_type") is None:
            err.append("line %d %s: direction and call_type required" % (i, v))
        if r.get("resolvable") == "yes" and r.get("horizon_months") is None:
            err.append("line %d %s: resolvable=yes needs horizon_months" % (i, v))
        if r.get("resolvable") != "yes" and r.get("why_not") is None:
            err.append("line %d %s: why_not required" % (i, v))
    hm, pr = r.get("horizon_months"), r.get("probability")
    if hm is not None and not (isinstance(hm, (int, float)) and 0 < hm <= 600):
        err.append("line %d %s: horizon_months %r" % (i, v, hm))
    if pr is not None and not (isinstance(pr, (int, float)) and 0 <= pr <= 1):
        err.append("line %d %s: probability %r" % (i, v, pr))
for v, rows in seen.items():
    if sorted(rows) != list(range(1, len(rows) + 1)) or len(rows) > 3:
        err.append("%s: rows must be 1..n, at most 3 (got %s)" % (v, rows))
for v in inp:
    if v not in seen:
        err.append("%s: no row" % v)
if err:
    print("ERRORS %d (first 40)" % len(err))
    for e in err[:40]:
        print(" ", e)
    sys.exit(1)
print("OK | views %d | rows %d" % (len(seen), sum(len(x) for x in seen.values())))
