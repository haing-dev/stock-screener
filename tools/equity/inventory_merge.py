"""Merge the coded inventory of step E0.1, check its form, measure agreement with the blind recode, and build the
investor table.

    python3 tools/equity/inventory_merge.py PACK_DIR CODED_DIR OUT_DIR

PACK_DIR: output of inventory_pack.py (docs.csv, recode_ids.json). CODED_DIR: pack_NN.jsonl files from the first
coder and recode.jsonl from the second. Writes OUT_DIR/inventory.csv (one row per document), investors.csv (one row
per person coded as investor or allocator who ran money) and agreement.md. Spec: E0.1_INVENTORY_SPEC.md."""
import collections
import csv
import glob
import json
import os
import re
import sys
import unicodedata

KIND = {"investor_talk", "secondary", "company", "expert", "other"}
SUBJ = {"stock_picking", "portfolio_and_risk", "macro_and_markets", "company_or_industry", "private_markets",
        "career_and_life", "other"}
STYLE = {"quality_compounders", "deep_value", "growth", "small_micro_cap", "special_situations", "long_short",
         "macro_multi_asset", "credit_distressed", "quant_systematic", "private_venture", "index_allocation",
         "sector_specialist", "none"}
REGION = {"us", "global", "europe", "asia", "emerging", "other", "unclear"}
TECH = {"valuation", "analysis_accounting", "screening_idea_sourcing", "portfolio_construction_sizing", "selling",
        "risk_management", "short_selling"}
ROLE = {"investor", "allocator", "executive", "expert", "host"}


def norm(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(sir|dr|prof|professor|mr|ms|mrs|jr|sr|ii|iii)\b\.?", " ", s)
    return re.sub(r"[^a-z ]", "", s).split()


ALIAS = {k: v for k, v in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                     "investor_aliases.json"), encoding="utf-8")).items()
         if not k.startswith("_")}


def key(name):
    w = norm(ALIAS.get(name.strip(), name))
    return (w[0] + " " + w[-1]) if len(w) >= 2 else " ".join(w)


def check(r, where):
    e = []
    if r.get("kind") not in KIND: e.append("kind")
    if r.get("subject") not in SUBJ: e.append("subject")
    if r.get("region") not in REGION: e.append("region")
    if not set(r.get("style") or []) <= STYLE or len(r.get("style") or []) > 2: e.append("style")
    if not set(r.get("technique") or []) <= TECH: e.append("technique")
    if r.get("explicit") not in (0, 1, 2, 3): e.append("explicit")
    if r.get("technique_depth") not in (0, 1, 2, 3): e.append("technique_depth")
    if r.get("short_side") not in ("yes", "no"): e.append("short_side")
    for p in r.get("people") or []:
        if p.get("role") not in ROLE or p.get("ran_money") not in ("yes", "no", "unclear") or not p.get("name"):
            e.append("people")
            break
    return ["%s doc %s: bad %s" % (where, r.get("doc"), x) for x in e]


def read(path):
    rows = []
    for ln in open(path, encoding="utf-8"):
        ln = ln.strip()
        if ln.startswith("{"):
            rows.append(json.loads(ln))
    return rows


def main(pack, coded, out):
    os.makedirs(out, exist_ok=True)
    files = dict((int(d), f) for d, f in list(csv.reader(open(os.path.join(pack, "docs.csv"), encoding="utf-8")))[1:])
    first, errs = {}, []
    for p in sorted(glob.glob(os.path.join(coded, "pack_*.jsonl"))):
        for r in read(p):
            errs += check(r, os.path.basename(p))
            if r.get("doc") in first:
                errs.append("doc %s coded twice" % r.get("doc"))
            first[r.get("doc")] = r
    miss = sorted(set(files) - set(first))
    extra = sorted(set(first) - set(files))
    second = {}
    rp = os.path.join(coded, "recode.jsonl")
    if os.path.exists(rp):
        for r in read(rp):
            errs += check(r, "recode")
            second[r.get("doc")] = r
    A = ["# E0.1 inventory: form check and agreement\n",
         "Documents coded: %d of %d. Missing: %d. Unknown doc numbers: %d. Form errors: %d.\n"
         % (len(set(first) & set(files)), len(files), len(miss), len(extra), len(errs))]
    A += ["- " + e for e in errs[:40]]
    if miss:
        A.append("- missing docs: " + ", ".join(map(str, miss[:60])))
    both = sorted(set(first) & set(second))
    if both:
        def rate(f):
            return 100.0 * sum(1 for d in both if f(first[d], second[d])) / len(both)
        inv = lambda r: {key(p["name"]) for p in r.get("people") or [] if p.get("role") in ("investor", "allocator")}
        n1 = sum(len(inv(first[d])) for d in both)
        nb = sum(len(inv(first[d]) & inv(second[d])) for d in both)
        n2 = sum(len(inv(second[d])) for d in both)
        rm = lambda r: {key(p["name"]): p.get("ran_money") for p in r.get("people") or []}
        same = tot = 0
        for d in both:
            a, b = rm(first[d]), rm(second[d])
            for k in set(a) & set(b):
                tot += 1
                same += a[k] == b[k]
        A += ["\n## Agreement on the blind recode (%d documents)\n" % len(both), "| Field | Agreement |", "|---|---|",
              "| kind | %.0f%% |" % rate(lambda a, b: a["kind"] == b["kind"]),
              "| subject | %.0f%% |" % rate(lambda a, b: a["subject"] == b["subject"]),
              "| region | %.0f%% |" % rate(lambda a, b: a["region"] == b["region"]),
              "| style (any overlap) | %.0f%% |" % rate(lambda a, b: bool(set(a["style"] or ["none"]) & set(b["style"] or ["none"]))),
              "| style (identical sets) | %.0f%% |" % rate(lambda a, b: set(a["style"] or ["none"]) == set(b["style"] or ["none"])),
              "| explicit (exact) | %.0f%% |" % rate(lambda a, b: a["explicit"] == b["explicit"]),
              "| explicit (within one step) | %.0f%% |" % rate(lambda a, b: abs(a["explicit"] - b["explicit"]) <= 1),
              "| technique_depth (exact) | %.0f%% |" % rate(lambda a, b: a["technique_depth"] == b["technique_depth"]),
              "| technique_depth (within one step) | %.0f%% |" % rate(lambda a, b: abs(a["technique_depth"] - b["technique_depth"]) <= 1),
              "| technique (any overlap or both empty) | %.0f%% |" % rate(lambda a, b: bool(set(a["technique"]) & set(b["technique"])) or not (a["technique"] or b["technique"])),
              "| short_side | %.0f%% |" % rate(lambda a, b: a["short_side"] == b["short_side"]),
              "| investor names: found by both / first coder / second coder | %d / %d / %d |" % (nb, n1, n2),
              "| ran_money, same answer for people named by both | %.0f%% (%d people) |" % (100.0 * same / max(tot, 1), tot)]
    open(os.path.join(out, "agreement.md"), "w", encoding="utf-8").write("\n".join(A) + "\n")
    w = csv.writer(open(os.path.join(out, "inventory.csv"), "w", newline="", encoding="utf-8"))
    w.writerow(["doc", "file", "kind", "subject", "style", "sector", "region", "explicit", "technique",
                "technique_depth", "short_side", "investors", "other_people", "absent"])
    P = collections.defaultdict(lambda: dict(names=collections.Counter(), firms=collections.Counter(), docs=[],
                                             styles=collections.Counter(), regions=collections.Counter(),
                                             roles=collections.Counter(), ran=collections.Counter(), explicit=[]))
    for d in sorted(set(first) & set(files)):
        r = first[d]
        inv = [p for p in r.get("people") or [] if p["role"] in ("investor", "allocator")]
        oth = [p for p in r.get("people") or [] if p["role"] not in ("investor", "allocator", "host")]
        w.writerow([d, files[d], r["kind"], r["subject"], ";".join(r["style"] or []), r.get("sector", ""), r["region"],
                    r["explicit"], ";".join(r["technique"] or []), r["technique_depth"], r["short_side"],
                    "; ".join("%s (%s)" % (p["name"], p.get("firm", "")) for p in inv),
                    "; ".join(p["name"] for p in oth), "; ".join(r.get("absent") or [])])
        for p in inv:
            x = P[key(p["name"])]
            x["names"][ALIAS.get(p["name"].strip(), p["name"])] += 1
            if p.get("firm"):
                x["firms"][p["firm"]] += 1
            x["docs"].append(d)
            x["roles"][p["role"]] += 1
            x["ran"][p["ran_money"]] += 1
            x["regions"][r["region"]] += 1
            x["explicit"].append(r["explicit"])
            for s in r["style"] or []:
                x["styles"][s] += 1
    w = csv.writer(open(os.path.join(out, "investors.csv"), "w", newline="", encoding="utf-8"))
    w.writerow(["id", "name", "other_spellings", "role", "ran_money", "firms", "documents", "doc_ids", "styles",
                "region", "explicit_max", "explicit_mean"])
    rows = sorted(P.items(), key=lambda kv: (-len(kv[1]["docs"]), kv[0]))
    for i, (k, x) in enumerate(rows, 1):
        nm = x["names"].most_common()
        w.writerow(["I%03d" % i, nm[0][0], "; ".join(n for n, _ in nm[1:]), x["roles"].most_common(1)[0][0],
                    x["ran"].most_common(1)[0][0], "; ".join("%s (%d)" % f for f in x["firms"].most_common()),
                    len(x["docs"]), " ".join(map(str, x["docs"])),
                    "; ".join("%s (%d)" % s for s in x["styles"].most_common()),
                    x["regions"].most_common(1)[0][0], max(x["explicit"]),
                    "%.2f" % (sum(x["explicit"]) / len(x["explicit"]))])
    print(A[1].strip(), "| investors:", len(rows), "| recoded:", len(both))


if __name__ == "__main__":
    main(*sys.argv[1:4])
