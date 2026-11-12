"""Forecast ledger step 2.1c (script): merge the coded batches into one ledger and print counts.
usage: python3 tools/fcast/merge.py <macro-vault worktree>"""
import collections, csv, glob, json, os, sys

F = os.path.join(sys.argv[1], "pipeline", "forecasts")
raw = {json.loads(l)["view_id"]: json.loads(l) for l in open(os.path.join(F, "views_raw.jsonl"))}
rows = []
for p in sorted(glob.glob(os.path.join(F, "coded", "batch_*.jsonl"))):
    for l in open(p):
        if l.strip():
            rows.append(json.loads(l))
got = {r["view_id"] for r in rows}
cols = ["forecast_id", "view_id", "row", "source_id", "who", "made_date", "date_precision", "kind", "variable_code", "variable_text",
        "direction", "level", "horizon_months", "horizon_text", "condition", "probability", "confidence", "call_type",
        "resolvable", "why_not", "claim_ids", "note"]
with open(os.path.join(F, "ledger.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(cols)
    for r in rows:
        r = dict(r, forecast_id="%s-%d" % (r["view_id"], r["row"]), source_id=raw[r["view_id"]]["source_id"],
                 claim_ids=" ".join(r.get("claim_ids") or []))
        w.writerow([r.get(c) for c in cols])
c = collections.Counter
print("views coded %d of %d | rows %d | missing views %d" % (len(got), len(raw), len(rows), len(set(raw) - got)))
fr = [r for r in rows if r["kind"] != "not_forecast"]
print("kind:", dict(c(r["kind"] for r in rows)))
print("resolvable (forecast rows):", dict(c(r["resolvable"] for r in fr)))
print("why not:", dict(c(r["why_not"] for r in fr if r["resolvable"] != "yes")))
print("call type:", dict(c(r["call_type"] for r in fr)))
print("top variables:", c(r["variable_code"] for r in fr).most_common(25))
print("speakers with forecasts: %d | top: %s" % (len({r["who"] for r in fr}), c(r["who"] for r in fr).most_common(12)))
print("made year:", dict(sorted(c(str(r["made_date"])[:4] for r in fr).items())))
