"""Verify that every quote cited by the moat reviewer appears word-for-word in the filing text."""
import json
import os
import re
import unicodedata

import pandas as pd

TRAITS = ["barriers_to_entry", "market_structure", "pricing_power", "essential_low_cost", "switching_costs",
          "disruption_risk", "regulatory_risk", "reinvestment_runway"]

_TRANS = str.maketrans({"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"', "\u2013": "-", "\u2014": "-",
                        "\u2011": "-", "\u00ad": "", "\u200b": "", "\u00a0": " "})


def norm(s):
    s = unicodedata.normalize("NFKC", s or "").translate(_TRANS).lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip(" .\"'")


def check_quote(quote, haystack_norm):
    q = norm(quote)
    if len(q) < 15:
        return False, "quote too short to verify"
    if q in haystack_norm:
        return True, ""
    if "..." in q or "\u2026" in q:
        pieces = [p.strip() for p in re.split(r"\.\.\.|\u2026", q) if len(p.strip()) >= 15]
        if pieces and all(p in haystack_norm for p in pieces):
            return True, "verified in pieces (ellipsis)"
    return False, "not found in filing text"


def verify(scores_path, pack_dir, out_dir=None):
    with open(scores_path, encoding="utf-8") as f:
        scores = json.load(f)
    if isinstance(scores, dict):
        scores = scores.get("companies") or list(scores.values())
    rows, summary = [], []
    for comp in scores:
        code = comp["company_code"]
        path = os.path.join(pack_dir, f"{code}_fulltext.txt")
        if not os.path.exists(path):
            summary.append({"company_code": code, "error": "fulltext file missing"})
            continue
        with open(path, encoding="utf-8") as f:
            hay = norm(f.read())
        n_ok = n_all = 0
        srow = {"company_code": code, "overall_moat": comp.get("overall_moat"),
                "moat_type": ", ".join(comp.get("moat_types") or [])}
        blocks = [(t, (comp.get("traits") or {}).get(t) or {}) for t in TRAITS] + [("bear_case", comp.get("bear_case") or {})]
        for trait, body in blocks:
            qs = body.get("quotes") or []
            ok = 0
            for q in qs:
                text = q.get("text") if isinstance(q, dict) else str(q)
                good, why = check_quote(text, hay)
                ok += good
                rows.append({"company_code": code, "trait": trait, "score": body.get("score"),
                             "quote": text, "section": q.get("section") if isinstance(q, dict) else None,
                             "verified": good, "note": why})
            n_ok += ok
            n_all += len(qs)
            if trait != "bear_case":
                srow[trait] = body.get("score")
                srow[f"{trait}_quotes_verified"] = f"{ok}/{len(qs)}"
                if qs and ok == 0:
                    srow[trait] = None  # score withdrawn: no verifiable evidence
        srow["quotes_verified"] = f"{n_ok}/{n_all}"
        srow["bear_case"] = (comp.get("bear_case") or {}).get("text")
        srow["unknowns"] = "; ".join(comp.get("unknowns") or [])
        summary.append(srow)
    out_dir = out_dir or pack_dir
    out = os.path.join(out_dir, "moat_scores_verified.xlsx")
    with pd.ExcelWriter(out, engine="openpyxl") as w:
        pd.DataFrame(summary).to_excel(w, sheet_name="Moat_Scores", index=False)
        pd.DataFrame(rows).to_excel(w, sheet_name="Quote_Checks", index=False)
    bad = sum(1 for r in rows if not r["verified"])
    print(f"Checked {len(rows)} quotes: {len(rows) - bad} verified, {bad} not found. Saved {out}")
    return out, summary, rows
