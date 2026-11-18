"""Phase A2 of the scorecard (E0.4): build the frozen investor file from the matchers' output, the WRDS coverage
figures in the matching report and the E0.1 inventory. No return is read here or anywhere before this file exists.

    python3 tools/equity/freeze_investors.py MATCH_DIR MATCH_REPORT INVENTORY_DIR OUT_CSV [AGREEMENT_MD]

MATCH_DIR holds match_*.jsonl (first matcher, all investors) and optionally recheck.jsonl (blind second matcher,
a tenth). Grades, primary style, region and explicitness follow STAGE0_REGISTRATION.md section 6, by rule."""
import collections
import csv
import glob
import json
import os
import re
import sys

STYLES = ["quality_compounders", "deep_value", "growth", "small_micro_cap", "special_situations", "long_short",
          "macro_multi_asset", "credit_distressed", "quant_systematic", "private_venture", "index_allocation",
          "sector_specialist", "none"]
NOT_A = {"long_short", "macro_multi_asset", "credit_distressed", "quant_systematic", "private_venture",
         "index_allocation"}
F_RE = re.compile(r"^   F (\d+) \| (.*?) \| .*?(?:quarters (\d+) \((\d{4}-\d{2}) to (\d{4}-\d{2})\) \| positions median "
                  r"(\d+) \| value median \$(-?\d+)M|no holdings filed)")
M_RE = re.compile(r"^   M\*? fundno (\d+) \((\d+) classes\) \| (.*?) \| mgr (.*?) since (\S*) \| (.*?) \| obj (\S*) \| "
                  r"months since 2011: (\S+) \((\S*) to (\S*)\) \| mean assets \$(\S+?)M(.*)$")


def top(codes, order=None):
    c = collections.Counter(codes)
    if not c:
        return ""
    best = max(c.values())
    tie = [k for k, v in c.items() if v == best]
    return sorted(tie, key=lambda k: (order.index(k) if order and k in order else 99, k))[0]


def quarters_after_2010(n, first):
    """Quarter-ends from 2011-03 on, given the count since 2010-06 and the first quarter filed."""
    early = sum(1 for q in ("2010-06", "2010-09", "2010-12") if first <= q)
    return max(0, n - early)


def main(mdir, report, inv_dir, out, agree=None):
    F, M = collections.defaultdict(dict), collections.defaultdict(dict)
    cur = None
    for ln in open(report, encoding="utf-8", errors="replace"):
        ln = ln.rstrip("\n")
        if ln.startswith("## I"):
            cur = ln[3:7]
        m = F_RE.match(ln)
        if m and cur:
            F[cur][int(m.group(1))] = dict(name=m.group(2), nq=int(m.group(3) or 0), first=m.group(4) or "",
                                           last=m.group(5) or "", pos=int(m.group(6) or 0), val=int(m.group(7) or 0))
        m = M_RE.match(ln)
        if m and cur:
            M[cur][int(m.group(1))] = dict(fund=m.group(3), mgr=m.group(4), since=m.group(5), obj=m.group(7),
                                           months=0 if m.group(8) == "none" else int(m.group(8)), d0=m.group(9),
                                           tna=0 if m.group(11) == "?" else int(m.group(11)),
                                           index="| index" in m.group(12))
    first, errs = {}, []
    for p in sorted(glob.glob(os.path.join(mdir, "match_*.jsonl"))):
        for ln in open(p, encoding="utf-8"):
            if ln.strip().startswith("{"):
                r = json.loads(ln)
                if r["id"] in first:
                    errs.append("matched twice: " + r["id"])
                first[r["id"]] = r
    people = [p for p in csv.DictReader(open(os.path.join(inv_dir, "investors.csv"), encoding="utf-8"))]
    rows, grades = [], collections.Counter()
    for p in people:
        own_styles = p["own_styles"].split()
        style = top(own_styles, STYLES) or "none"
        region = top(p["own_regions"].split()) or "unclear"
        ex = [int(x) for x in p["own_explicit"].split()]
        r = first.get(p["id"], {})
        mg = [int(x) for x in r.get("mgrnos") or []]
        fn = [int(x) for x in r.get("fundnos") or []]
        bad = [x for x in mg if x not in F[p["id"]]] + [x for x in fn if x not in M[p["id"]]]
        if bad:
            errs.append("%s: ids not in its candidate block: %s" % (p["id"], bad))
            mg = [x for x in mg if x in F[p["id"]]]
            fn = [x for x in fn if x in M[p["id"]]]
        if p["ran_money"] == "yes" and p["id"] not in first:
            errs.append("no match line for " + p["id"])
        start = (r.get("start_ym") or "").strip()
        end = (r.get("end_ym") or "").strip()
        # fund record: an active US equity fund with 60 months under this investor after 2010
        fund_ok = []
        for x in fn:
            f = M[p["id"]][x]
            m0 = max(f["d0"] or "2011-01", start or "2011-01", "2011-01")
            m1 = min(end or "2025-12", "2025-12")
            months = (int(m1[:4]) - int(m0[:4])) * 12 + int(m1[5:7]) - int(m0[5:7]) + 1
            if f["obj"].startswith("ED") and not f["index"] and f["tna"] >= 15 and min(months, f["months"]) >= 60:
                fund_ok.append(x)
        q = sum(quarters_after_2010(F[p["id"]][x]["nq"], F[p["id"]][x]["first"]) for x in mg)
        main_f = max(mg, key=lambda x: F[p["id"]][x]["nq"]) if mg else None
        pos = F[p["id"]][main_f]["pos"] if mg else 0
        val = F[p["id"]][main_f]["val"] if mg else 0
        screen = bool(mg) and q >= 20 and 5 <= pos <= 150 and val >= 100
        if p["role"] != "investor" and (mg or fund_ok):
            kind, grade = ("13f" if mg else "none"), ("C" if mg else "N")     # allocators pick managers, not stocks
        elif fund_ok:
            kind, grade = "fund", "F"
        elif screen and style not in NOT_A and region in ("us", "global"):
            kind, grade = "13f", "A"
        elif screen and (style == "long_short" or region in ("europe", "asia", "emerging", "other")):
            kind, grade = "13f", "B"
        elif mg:
            kind, grade = "13f", "C"
        else:
            kind, grade = "none", "N"
        grades[grade] += 1
        rows.append([p["id"], p["name"], kind, " ".join(map(str, mg)) if kind == "13f" else "",
                     " ".join(map(str, fund_ok)) if kind == "fund" else "", start, end, grade, style, region,
                     max(ex) if ex else "", "%.2f" % (sum(ex) / len(ex)) if ex else "", p["own_docs"], p["ran_money"],
                     p["role"], q if mg else "", pos if mg else "", val if mg else "",
                     ("; ".join(M[p["id"]][x]["fund"][:60] for x in fund_ok) if kind == "fund" else
                      "; ".join(F[p["id"]][x]["name"][:40] for x in mg)),
                     (r.get("why") or "")[:160]])
    w = csv.writer(open(out, "w", newline="", encoding="utf-8"))
    w.writerow(["id", "name", "record_kind", "mgrnos", "fundnos", "start_ym", "end_ym", "grade", "primary_style",
                "region", "explicit_max", "explicit_mean", "own_docs", "ran_money", "role", "quarters_after_2010",
                "positions_median", "value_median_musd", "matched_name", "why"])
    w.writerows(rows)
    A = ["# E0.4 phase A2: matching check\n", "Investors: %d. Grades: %s. Form problems: %d.\n"
         % (len(rows), ", ".join("%s %d" % kv for kv in sorted(grades.items())), len(errs))] + ["- " + e for e in errs]
    rp = os.path.join(mdir, "recheck.jsonl")
    if os.path.exists(rp):
        sec = {}
        for ln in open(rp, encoding="utf-8"):
            if ln.strip().startswith("{"):
                r = json.loads(ln)
                sec[r["id"]] = r
        both = sorted(set(sec) & set(first))
        same_f = sum(set(first[i].get("mgrnos") or []) == set(sec[i].get("mgrnos") or []) for i in both)
        same_m = sum(set(first[i].get("fundnos") or []) == set(sec[i].get("fundnos") or []) for i in both)
        A += ["\n## Agreement with the blind second matcher (%d investors)\n" % len(both),
              "| Item | Same answer |", "|---|---|", "| 13F filer numbers | %d of %d |" % (same_f, len(both)),
              "| fund numbers | %d of %d |" % (same_m, len(both)), "\nDifferences:"]
        for i in both:
            a, b = first[i], sec[i]
            if set(a.get("mgrnos") or []) != set(b.get("mgrnos") or []) or set(a.get("fundnos") or []) != set(b.get("fundnos") or []):
                A.append("- %s: first %s / %s; second %s / %s" % (i, a.get("mgrnos"), a.get("fundnos"), b.get("mgrnos"), b.get("fundnos")))
    if agree:
        open(agree, "w", encoding="utf-8").write("\n".join(A) + "\n")
    print(A[1].strip())


if __name__ == "__main__":
    main(*sys.argv[1:6])
