"""Forecast ledger step 2.1d (script): agreement between the main coding and the independent blind recode (20% sample).
usage: python3 tools/fcast/agree.py <macro-vault worktree>"""
import collections, glob, json, os, sys

F = os.path.join(sys.argv[1], "pipeline", "forecasts")


def load(pat):
    d = collections.defaultdict(list)
    for p in sorted(glob.glob(os.path.join(F, pat))):
        for l in open(p):
            if l.strip():
                r = json.loads(l)
                d[r["view_id"]].append(r)
    return d


A, B = load("coded/batch_*.jsonl"), load("recode/coded_*.jsonl")
ids = sorted(set(A) & set(B))
print("views coded by both: %d (recode sample %d)" % (len(ids), len(B)))


def kappa(pairs):
    n = len(pairs)
    if not n:
        return float("nan")
    po = sum(a == b for a, b in pairs) / n
    ca, cb = collections.Counter(a for a, _ in pairs), collections.Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb.get(k, 0) for k in ca) / n / n
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def fam(code):
    code = (code or "").split(">")[0]
    for k, v in (("EQ", "equity"), ("RATE", "rates"), ("US_2Y", "rates"), ("US_10Y", "rates"), ("US_30Y", "rates"), ("CURVE", "rates"),
                 ("YIELD", "rates"), ("TERM", "rates"), ("USD", "fx"), ("FX", "fx"), ("JPY", "fx"), ("CNY", "fx"), ("GOLD", "commodity"),
                 ("SILVER", "commodity"), ("OIL", "commodity"), ("NATGAS", "commodity"), ("COPPER", "commodity"), ("URANIUM", "commodity"),
                 ("AGRI", "commodity"), ("COMMODIT", "commodity"), ("CREDIT", "credit"), ("VIX", "vol"), ("VOL", "vol"),
                 ("GROWTH", "macro"), ("RECESSION", "macro"), ("INFLATION", "macro"), ("JOBS", "macro"), ("DEFICIT", "macro"),
                 ("LIQUIDITY", "macro")):
        if k in code:
            return v
    return code.lower()


def hb(m):
    return "none" if m is None else "<=3m" if m <= 3 else "3-12m" if m <= 12 else "1-3y" if m <= 36 else ">3y"


isf = lambda rows: any(r["kind"] != "not_forecast" for r in rows)
pairs = [(isf(A[i]), isf(B[i])) for i in ids]
print("is a forecast (view level): agree %.1f%% | kappa %.2f | main yes %d | recode yes %d" % (
    100 * sum(a == b for a, b in pairs) / len(pairs), kappa(pairs), sum(a for a, _ in pairs), sum(b for _, b in pairs)))
print("rows per view: main %.2f | recode %.2f" % (sum(len(A[i]) for i in ids) / len(ids), sum(len(B[i]) for i in ids) / len(ids)))
both = [i for i in ids if isf(A[i]) and isf(B[i])]
fields = collections.defaultdict(list)
for i in both:
    ra = [r for r in A[i] if r["kind"] != "not_forecast"]
    rb = [r for r in B[i] if r["kind"] != "not_forecast"]
    # pair the two rows that agree best on the variable (exact code, else family), then on direction
    best = max(((a, b) for a in ra for b in rb), key=lambda ab: (ab[0]["variable_code"] == ab[1]["variable_code"],
                                                               fam(ab[0]["variable_code"]) == fam(ab[1]["variable_code"]),
                                                               ab[0]["direction"] == ab[1]["direction"]))
    a, b = best
    fields["variable_code (exact)"].append((a["variable_code"], b["variable_code"]))
    fields["variable family"].append((fam(a["variable_code"]), fam(b["variable_code"])))
    fields["direction"].append((a["direction"], b["direction"]))
    fields["kind"].append((a["kind"], b["kind"]))
    fields["call_type"].append((a["call_type"], b["call_type"]))
    fields["resolvable"].append((a["resolvable"], b["resolvable"]))
    fields["horizon bucket"].append((hb(a["horizon_months"]), hb(b["horizon_months"])))
    fields["made_date (month)"].append((str(a["made_date"])[:7], str(b["made_date"])[:7]))
    fields["confidence"].append((a["confidence"], b["confidence"]))
print("views both call a forecast: %d (best-matching row pair per view)" % len(both))
for k, p in fields.items():
    print("  %-24s agree %5.1f%% | kappa %.2f" % (k, 100 * sum(x == y for x, y in p) / len(p), kappa(p)))
p = fields["resolvable"]
print("resolvable table (main -> recode):", dict(collections.Counter(p)))
full = sum(1 for i in range(len(both)) if all(fields[k][i][0] == fields[k][i][1] for k in ("variable family", "direction", "resolvable")))
print("same variable family + direction + resolvable: %.1f%%" % (100 * full / len(both)))
