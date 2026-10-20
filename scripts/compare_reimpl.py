"""Compare the independent re-implementation of Fortress (validation/reimpl/independent_fortress.csv, written by an
agent that saw only the written rules and the raw data) with the screener's own result on the same files and date.
Writes validation/reimplementation.md (PROTOCOL section 8: pass if Jaccard >= 0.9 with every difference explained).

    python scripts/compare_reimpl.py
"""
import csv
import glob
import gzip
import json
import os
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from qs.config import load_config  # noqa: E402
from qs.extract import CompanyData  # noqa: E402
from qs.pipeline import _CD, apply_industry_cycle, build_ctx, metrics_for  # noqa: E402
from qs.pit import facts_as_of  # noqa: E402
from qs.screens import BY_ID  # noqa: E402

AS_OF = date(2026, 10, 1)
REIMPL = os.path.join(ROOT, "validation", "reimpl", "independent_fortress.csv")
OUT = os.path.join(ROOT, "validation", "reimplementation.md")


def ours(cfg):
    s = BY_ID["fortress"]
    out = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "tests", "real_samples", "*companyfacts_subset.json.gz"))):
        name = os.path.basename(path)
        with gzip.open(path, "rt", encoding="utf-8") as f:
            fs = facts_as_of(json.load(f), AS_OF)
        cd = CompanyData(fs)
        if cd.currency is None:
            out[name] = {"class": "no data", "gates": {}}
            continue
        res, why = metrics_for(cd, "", {}, cfg, AS_OF)
        if res is None:
            out[name] = {"class": f"not screened ({why[:60]})", "gates": {}}
            continue
        m, _rows, compact = res
        tk = name.split("_")[0].upper()
        ctx = build_ctx({"cik": 0, "ticker": tk, "name": fs.get("entityName"), "exchange": "NYSE", "all_tickers": [tk]},
                        {"sic": ""}, m, compact, _CD(cd.flags, cd.candidates), cfg, {m["currency"]: (1.0, "x")}, AS_OF)
        apply_industry_cycle({0: ctx}, cfg)
        r = s.evaluate(ctx, cfg, priced=False)
        cls = "PASS*" if (r["class"] == "PASS" and r.get("star")) else r["class"]
        out[name] = {"class": cls, "gates": {g: st[0] for g, st in r["gates"].items()},
                     "vals": {"F7": ctx.get("operating_margin_std"), "F8": ctx.get("roic_median"),
                              "F10": ctx.get("interest_coverage")}}
    return out


def main():
    cfg = load_config()
    mine = ours(cfg)
    try:
        with open(REIMPL, encoding="utf-8") as f:
            theirs = {r["file"]: r for r in csv.DictReader(f)}
    except OSError:
        raise SystemExit(f"{REIMPL} not found - the independent re-implementation hasn't been run")
    files = sorted(set(mine) & set(theirs))
    pm = {f for f in files if mine[f]["class"].startswith("PASS")}
    pt = {f for f in files if theirs[f]["class"].strip().startswith("PASS")}
    jac = len(pm & pt) / len(pm | pt) if (pm | pt) else 1.0
    gate_agree = gate_total = 0
    diffs = []
    for f in files:
        for g, st in mine[f]["gates"].items():
            t = (theirs[f].get(g) or "").strip().upper()
            if not t:
                continue
            gate_total += 1
            if t == st:
                gate_agree += 1
            else:
                diffs.append((f, g, st, t))
    L = ["# Independent re-implementation: Fortress", "",
         "An agent that never saw the screener's code implemented the Fortress rules from their written text "
         "(validation/reimpl/fortress_rules.md) on the 38 real SEC samples, as of 2026-10-01. Its interpretation notes: "
         "validation/reimpl/independent_notes.md.", "",
         f"- Companies compared: {len(files)}",
         f"- Passing (PASS or PASS*): screener {len(pm)}, independent {len(pt)}, both {len(pm & pt)}",
         f"- **Jaccard of the pass lists: {jac:.2f}** (protocol: >= 0.9 with every difference explained)",
         f"- Rule outcomes agreeing: {gate_agree} of {gate_total} ({gate_agree / gate_total:.0%})" if gate_total else
         "- Rule outcomes agreeing: -", "",
         "## Companies classified differently", "", "| File | Screener | Independent |", "| --- | --- | --- |"]
    for f in files:
        a, b = mine[f]["class"], theirs[f]["class"].strip()
        if a.startswith("PASS") != b.startswith("PASS"):
            L.append(f"| {f} | {a} | {b} |")
    L += ["", "## Rule outcomes that differ", "", "| File | Rule | Screener | Independent |", "| --- | --- | --- | --- |"]
    by_rule = {}
    for f, g, a, b in diffs:
        by_rule[g] = by_rule.get(g, 0) + 1
        L.append(f"| {f} | {g} | {a} | {b} |")
    L += ["", "Differences per rule: " + ", ".join(f"{g} {n}" for g, n in sorted(by_rule.items(), key=lambda x: -x[1])),
          "", "Each difference must be explained (a different but defensible definition, a data issue, or a bug) before "
          "this check counts as passed; explanations go below.", "", "## Explanations", ""]
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"{OUT}: Jaccard {jac:.2f}, rule agreement {gate_agree}/{gate_total}")
    return jac


if __name__ == "__main__":
    main()
