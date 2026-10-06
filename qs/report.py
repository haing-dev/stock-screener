"""Excel + CSV + JSON output. Every number is traceable: the evidence CSV links each input to its SEC filing."""
import csv
import json
import os

import pandas as pd
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from .extract import CompanyData, _d
from .industry import CLINICAL_STAGE, group_rows, in_ranges
from .metrics import compute, evidence_rows
from .rules import PILLAR_SOURCES
from .screens import FAIL, PASS, SCREENS
from .sec import filing_index_url

SHEET = {"core": "1 Core", "emerging": "2 Emerging", "special": "3 Special sits", "fortress": "4 Fortress",
         "hc_commercial": "5a HC commercial", "hc_clinical": "5b HC clinical", "cyclicals": "6 Cyclicals"}

PCT = {"revenue_cagr", "roic_median", "roic_share_above_floor", "roic_trend", "incremental_roic",
       "gross_margin_median", "gross_margin_std", "gross_margin_change_2021_2023", "operating_margin_median",
       "operating_margin_std", "operating_margin_trend", "operating_margin_change_2021_2023", "fcf_conversion",
       "share_count_cagr", "acquisitions_to_ocf", "sbc_to_revenue", "goodwill_to_assets", "revenue_growth_std",
       "nopat_cagr", "fcf_cagr", "fcf_per_share_cagr", "fcf_margin_latest3", "rnd_to_revenue",
       "shareholder_returns_to_fcf", "sic_revenue_share", "sic_top2_share", "gross_margin", "operating_margin",
       "fcf_margin", "roic", "tax_rate_used", "cash_roic_median", "roc_tangible_median", "roc_tangible_latest",
       "reinvestment_rate", "recession_2020_revenue_change", "recession_2020_op_income_change",
       "recession_2009_revenue_change", "recession_2009_op_income_change", "earnings_yield", "fcf_yield",
       "revenue_cagr_3y", "ebitda_cagr_3y", "ytd_revenue_growth", "gross_margin_latest", "ttm_ebitda_margin",
       "ebitda_margin_change_3y", "sga_ratio_change_3y", "share_count_cagr_3y", "ttm_operating_margin",
       "operating_margin_latest", "op_margin_percentile_10y", "industry_margin_percentile",
       "industry_margin_latest", "share_count_change_latest", "revenue_growth_latest_fy", "ttm_gross_margin",
       "roic_latest", "cash_roic", "roc_tangible", "ebitda_margin", "sga_ratio", "gp_to_tangible_assets"}
MULT = {"net_debt_to_ocf", "net_debt_to_ebitda", "net_debt_to_norm_ebitda", "ev_ebit", "ev_ebitda", "ev_sales",
        "pe", "ev_normalized_ebit", "interest_coverage", "ev_to_liquid_assets", "debt_to_liquid_assets",
        "cash_runway_years", "industry_capex_to_da", "capex_to_da_3y", "mcap_to_public_float", "composite"}
MILLIONS = {"latest_revenue_usd", "market_cap_usd", "ev_usd", "adv_usd", "liquid_assets_usd", "ttm_revenue_usd"}
LOCAL_MILLIONS = {"ttm_revenue", "annual_cash_burn", "debt_due_2y_total", "bs_net_debt"}
HEADERS = {
    "composite": "Composite score (0-100)", "robust": "Robust (passes 20% stricter)",
    "latest_revenue_usd": "Revenue latest FY ($M)", "market_cap_usd": "Market cap ($M)", "ev_usd": "EV ($M)",
    "adv_usd": "Avg daily $ traded ($M)", "liquid_assets_usd": "Cash + investments ($M)",
    "ttm_revenue": "Revenue TTM (M, reporting ccy)", "annual_cash_burn": "Cash burn / yr (M, reporting ccy)",
    "debt_due_2y_total": "Debt due within 2y (M, reporting ccy)", "revenue_cagr": "Revenue CAGR (10y)",
    "roic_median": "ROIC median (10y)", "cash_roic_median": "Cash ROIC median (FCF / capital)",
    "roc_tangible_median": "Pre-tax return on tangible capital (median)", "reinvestment_rate": "Reinvestment rate (5y)",
    "gross_margin_median": "Gross margin median", "gross_margin_change_2021_2023": "Gross margin chg 2021->23",
    "operating_margin_median": "Operating margin median", "fcf_conversion": "FCF / net income (cum.)",
    "net_debt_to_ocf": "Net debt / OCF (x)", "share_count_cagr": "Share count CAGR (5y)",
    "recession_2020_revenue_change": "2020: revenue change", "recession_2020_op_income_change": "2020: op income change",
    "recession_2009_revenue_change": "2009: revenue change", "recession_2009_op_income_change": "2009: op income change",
    "acquisitions_to_ocf": "Acquisitions / OCF", "sbc_to_revenue": "Stock pay / revenue", "ev_ebit": "EV / EBIT (TTM)",
    "ev_ebitda": "EV / EBITDA (TTM)", "ev_sales": "EV / sales (TTM)", "pe": "P/E (TTM)",
    "earnings_yield": "Earnings yield (EBIT / EV)", "fcf_yield": "FCF yield", "revenue_cagr_3y": "Revenue CAGR (3y)",
    "ytd_revenue_growth": "Revenue growth, latest YTD", "ebitda_cagr_3y": "EBITDA CAGR (3y)",
    "gross_margin_latest": "Gross margin (latest FY)", "ttm_ebitda_margin": "EBITDA margin (TTM)",
    "ebitda_margin_change_3y": "EBITDA margin chg (3y)", "sga_ratio_change_3y": "SG&A / revenue chg (3y)",
    "gp_to_tangible_assets": "Gross profit / tangible assets", "share_count_cagr_3y": "Share count CAGR (3y)",
    "net_debt_to_ebitda": "Net debt / EBITDA (TTM)", "net_debt_to_norm_ebitda": "Net debt / avg EBITDA (cycle)",
    "interest_coverage": "Interest coverage (x)", "operating_margin_std": "Op margin volatility (10y)",
    "event_types": "Event", "event_date": "Event filing date", "months_since_event": "Months since event",
    "event_filing_url": "Event filing", "roc_tangible_latest": "Return on tangible capital (latest)",
    "ttm_operating_margin": "Operating margin (TTM)", "hc_segment": "Healthcare segment", "hc_stage": "Stage",
    "rnd_to_revenue": "R&D / revenue", "ev_to_liquid_assets": "EV / cash & investments",
    "cash_runway_years": "Cash runway (years; 99 = cash-generative)", "debt_to_liquid_assets": "Debt / cash & inv.",
    "share_count_change_latest": "Share count chg (latest FY)", "bs_date": "Balance sheet date",
    "cycle_group": "Cycle group", "industry_margin_percentile": "Industry margin percentile (10y)",
    "industry_capex_to_da": "Industry capex / D&A (3y)", "industry_trough_zone": "Industry in trough zone",
    "op_margin_percentile_10y": "Company margin percentile (10y)", "operating_margin_latest": "Op margin (latest FY)",
    "positive_ebit_years": "Profitable years (of 10)", "ev_normalized_ebit": "EV / avg EBIT (cycle)",
    "capex_to_da_3y": "Capex / D&A (3y)", "flags": "Flags (check by hand)", "latest_annual_url": "Latest annual report",
    "why": "Why it's here / what to check", "list": "List", "industry": "Industry (SEC SIC)",
    "val_issue": "Price / market cap note", "price": "Price ($)", "price_date": "Price date",
}
HEADER_FILL = PatternFill("solid", fgColor="1F3A5F")
HEADER_FONT = Font(color="FFFFFF", bold=True)
LEAD = ["ticker", "name", "industry"]
TAIL = ["flags", "price", "price_date", "val_issue", "latest_annual_url", "latest_fy", "ttm_end", "currency", "sic",
        "exchange", "cik"]


def _flags_str(v):
    if isinstance(v, (list, tuple)):
        return "; ".join(str(x) for x in v)
    return v if isinstance(v, str) else ""


def _prep(df, cols):
    d = df.copy()
    for c in cols:
        if c not in d:
            d[c] = None
    d = d[cols]
    for c in ("flags", "why", "event_types"):
        if c in d:
            d[c] = d[c].apply(_flags_str)
    for c in MILLIONS | LOCAL_MILLIONS:
        if c in d:
            d[c] = pd.to_numeric(d[c], errors="coerce") / 1e6
    return d


def _format_sheet(ws, df, link_cols=(), widths=None):
    ws.freeze_panes = "C2" if ws.max_column > 3 else "A2"
    for j, col in enumerate(df.columns, start=1):
        cell = ws.cell(row=1, column=j)
        cell.value = HEADERS.get(col, col)
        cell.fill, cell.font = HEADER_FILL, HEADER_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        letter = get_column_letter(j)
        w = (widths or {}).get(col)
        if w is None:
            w = 11 if col in PCT or col in MULT else min(40, max(10, len(str(cell.value)) * 0.8))
            if col in ("name", "industry"):
                w = 28
            if col in ("flags", "why"):
                w = 70
        ws.column_dimensions[letter].width = w
        fmt = "0.0%" if col in PCT else ("0.0" if col in MULT else ("#,##0.0" if col in MILLIONS | LOCAL_MILLIONS
                                                                  else None))
        for i in range(2, ws.max_row + 1):
            c = ws.cell(row=i, column=j)
            if fmt and isinstance(c.value, (int, float)):
                c.number_format = fmt
            if col in link_cols and isinstance(c.value, str) and c.value.startswith("http"):
                url = c.value
                c.value = f'=HYPERLINK("{url}","open")'
                c.font = Font(color="0563C1", underline="single")
            if col in ("flags", "why"):
                c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[1].height = 48
    ws.auto_filter.ref = ws.dimensions


def _kv_sheet(writer, name, rows, widths=(44, 120)):
    d = pd.DataFrame(rows, columns=["Item", "Detail"])
    d.to_excel(writer, sheet_name=name, index=False)
    ws = writer.sheets[name]
    ws.column_dimensions["A"].width, ws.column_dimensions["B"].width = widths
    for c in ws[1]:
        c.fill, c.font = HEADER_FILL, HEADER_FONT
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")


def _fmt_val(v, fmt):
    if v is None:
        return "n/a"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, tuple):
        return " / ".join(_fmt_val(x, fmt) for x in v)
    try:
        if fmt == "pct":
            return f"{v:.1%}"
        if fmt == "usd":
            return f"${v / 1e6:,.0f}M"
        if fmt in ("mult", "years"):
            return f"{v:.2f}"
        if fmt == "int":
            return f"{v:.0f}"
        return f"{v:.3g}" if isinstance(v, float) else str(v)
    except (TypeError, ValueError):
        return str(v)


WATCH = ("CHECK", "NEAR", "PRICE", "ONE")
LIST_LABEL = {"CHECK": "CHECK manually", "NEAR": "NEAR miss", "PRICE": "Price too high (rest passes)",
              "ONE": "Failed 1 rule"}


def class_cell(r):
    """'PASS', 'CHECK', or the class with the rules that failed, e.g. 'FAIL: G5a G8' (see the Rules sheet)."""
    if not r:
        return "-"
    name = {"ONE": "1 RULE"}.get(r["class"], r["class"])
    if r.get("failed") and r["class"] != PASS:
        return f"{name}: " + " ".join(r["failed"])
    return name


def why_text(screen, res):
    parts = []
    gmap = {g.gid: g for g in screen.gates}
    for gid in res.get("failed", []):
        st, val, thr, note = res["gates"][gid]
        g = gmap[gid]
        parts.append(f"FAILS {gid} {g.name}: {_fmt_val(val, g.fmt)} vs {g.op or ''} {_fmt_val(thr, g.fmt)}"
                     + (f" ({note})" if note else ""))
    parts += res.get("check_notes", [])
    return "; ".join(parts)


def gate_cell(st):
    s, val, thr, note = st
    return s


def rules_rows(cfg):
    rows = [("HOW TO READ",
             "Each screen has a universe (industries it looks at) and gates (rules). PASS = every gate passes and the "
             "data looked clean. CHECK = nothing fails but an input is missing or a data-quality check needs a human "
             "(these are potential candidates - never ignored). NEAR = failed exactly one numeric rule by less than "
             f"{cfg['sensitivity']:.0%}. 'Price too high (rest passes)' = every business rule passes, only the valuation "
             "rule fails (revisit when the price drops). 'Failed 1 rule' = exactly one business rule failed by a wider "
             "margin (e.g. more debt than allowed) and every other rule was verified - judge whether that rule matters. "
             "Quality warnings (margin collapse, shrinking revenue, 2008-09 loss with falling sales) turn a PASS into "
             "CHECK. All_Companies shows the failed rule codes (e.g. 'FAIL: G5a G8'). Passing companies are ranked by pillar scores (percentile within the screen's "
             "PASS + watch lists, 0-100). 'Robust' = still passes with every numeric threshold 20% stricter. Flags "
             "never remove a company; they tell you what to check.")]
    for s in SCREENS:
        rows.append((f"=== {SHEET[s.sid]}: {s.title}", f"{s.purpose}  Sources: {s.sources}"))
        for g in s.gates:
            rows.append((f"{s.sid} {g.gid} {g.name}" + (" (needs price)" if g.needs_price else ""),
                         f"{g.rule_text(cfg, s.sid)}.  Why: {g.insight}"))
        if s.pillars:
            for p, metrics in s.pillars.items():
                txt = ", ".join(f"{m} ({'higher' if hib else 'lower'} = better)" for m, hib in metrics)
                w = (s.weights or cfg.get("pillar_weights", {})).get(p)
                rows.append((f"{s.sid} pillar: {p} (weight {w})", txt + (f".  Why: {PILLAR_SOURCES[p]}"
                                                                        if p in PILLAR_SOURCES else "")))
        rows.append((f"{s.sid} AI review focus", s.rubric))
    rows += [
        ("Definitions", "ROIC = operating income x (1 - tax rate) / average invested capital (total assets - cash & "
                        "short-term investments - non-interest-bearing current liabilities). Cash ROIC = FCF / the same "
                        "capital. Return on tangible capital (Greenblatt) = EBIT / (net working capital ex cash + net "
                        "PP&E). FCF = operating cash flow - capex (PP&E + capitalised software)."),
        ("", "TTM = trailing twelve months: latest fiscal year + current year-to-date - prior-year year-to-date from "
             "10-Q filings, same XBRL tag. If no newer 10-Q (or a 20-F/40-F filer), TTM = latest fiscal year. Latest "
             "balance sheet = the most recent 10-K or 10-Q balance sheet; all its items are taken at the same date."),
        ("", "Market cap = Twelve Data price x SEC share count (cover page shares if < 9 months old and one share "
             "class; else weighted diluted shares). Checked against the public float the company reported (must be "
             "0.55x-8x) and the quote must be a US listing in USD, at most 7 days old. EV = market cap + debt + "
             "minority interest + preferred - cash & short-term investments."),
        ("", "Recession tests compare the fiscal years ending Mar-2020..Jun-2021 (and Sep-2008..Mar-2010) with the "
             "year before each; the worst year counts. Cycle tests: company margin percentile = where the latest "
             "operating margin sits in its own last-10-year range; industry percentile = same for the aggregate "
             "margin of all SEC filers in the cycle group."),
        ("Data-quality holds (move PASS -> CHECK)", "Revenue jumps where the XBRL tag changes; fiscal year-end "
                                                     "changed; several reporting currencies; a value taken from a "
                                                     "non-standard tag; debt seemingly missing; possible Chapter 11; "
                                                     "operating income tagged in earlier years but not the latest; "
                                                     "a filed annual report not yet in SEC's XBRL data; any price / "
                                                     "market-cap check failing."),
        ("Limitations", "1) Companies using company-specific XBRL tags can miss data - they land on 'Check manually' "
                        "with the reason, never silently dropped; see Data_Gaps. 2) ROIC flatters asset-light "
                        "software (Dorsey). 3) Only currently listed NYSE/Nasdaq SEC filers (survivorship; no "
                        "non-US-only listings). 4) SIC codes are coarse. 5) Moats, management, patents, pipelines "
                        "still need the AI + human review."),
    ]
    return rows


def _companies_rows(screen, results, ctxs, which):
    out = []
    for c, r in results.items():
        if r["class"] not in which:
            continue
        ctx = ctxs[c]
        row = {k: ctx.get(k) for k in set(LEAD + TAIL + screen.columns)}
        row.update({"list": r["class"], "why": why_text(screen, r), "robust": r.get("robust"),
                    "universe_note": r.get("universe_note")})
        for g in screen.gates:
            st = r["gates"].get(g.gid)
            if st:
                row[f"{g.gid}"] = st[0]
        out.append(row)
    return pd.DataFrame(out)


def write_outputs(path, cfg, run_info, screens, results, ctxs, records, cyc, today, write_latest=True):
    out_dir = os.path.dirname(path)
    summary_rows, latest = [], {"run_info": run_info, "screens": {}}
    listed = set()
    with pd.ExcelWriter(path, engine="openpyxl") as w:
        # placeholder first sheet; filled at the end via _kv_sheet ordering trick
        sheets = {}
        for s in screens:
            res = results[s.sid]
            counts = {k: sum(1 for r in res.values() if r["class"] == k) for k in (PASS, *WATCH, FAIL)}
            summary_rows.append((f"{SHEET[s.sid]} - {s.title}",
                                 f"in universe {len(res)} | PASS {counts[PASS]} | " +
                                 " | ".join(f"{LIST_LABEL[k]} {counts[k]}" for k in WATCH) + f" | fail {counts[FAIL]}"))
            p = _companies_rows(s, res, ctxs, {PASS})
            if len(p):
                sc = s.score(p, cfg)
                for col in sc.columns:
                    p[col] = sc[col]
                p = p.sort_values("composite", ascending=False)
                p.insert(0, "rank", range(1, len(p) + 1))
            pill = list(s.pillars.keys())
            cols = ["rank"] + LEAD + ["composite"] + pill + ["robust"] + s.columns + TAIL
            if s.sid == "core":
                cols = ["rank"] + LEAD + ["composite"] + pill + ["robust", "sic_top2_share", "sic_revenue_share"] + \
                       s.columns + TAIL
            pp = _prep(p, cols) if len(p) else pd.DataFrame(columns=cols)
            pp.to_excel(w, sheet_name=SHEET[s.sid], index=False)
            _format_sheet(w.sheets[SHEET[s.sid]], pp, link_cols={"latest_annual_url", "event_filing_url"})
            wch = _companies_rows(s, res, ctxs, set(WATCH))
            wcols = ["list"] + LEAD + ["why", "composite"] + [g.gid for g in s.gates] + s.columns + TAIL
            if len(wch):
                wsc = s.score(wch, cfg)
                wch["composite"] = wsc["composite"]
                wch["_o"] = wch["list"].map({k: i for i, k in enumerate(WATCH)})
                wch = wch.sort_values(["_o", "composite"], ascending=[True, False]).drop(columns="_o")
                wch["list"] = wch["list"].map(LIST_LABEL)
            ww = _prep(wch, wcols) if len(wch) else pd.DataFrame(columns=wcols)
            ww.to_excel(w, sheet_name=SHEET[s.sid] + " - watch", index=False)
            _format_sheet(w.sheets[SHEET[s.sid] + " - watch"], ww, link_cols={"latest_annual_url", "event_filing_url"})
            listed |= set(p["cik"]) if len(p) else set()
            listed |= set(wch["cik"]) if len(wch) else set()
            keep = ["rank", "ticker", "name", "cik", "industry", "sic", "composite", "list", "why", "flags"] + s.columns
            latest["screens"][s.sid] = {
                "title": s.title, "rubric": s.rubric,
                "pass": [{k: _jsonable(r.get(k)) for k in keep if k in r} for _, r in p.iterrows()] if len(p) else [],
                "watch": [{k: _jsonable(r.get(k)) for k in keep if k in r} for _, r in wch.iterrows()] if len(wch) else []}
            for item in latest["screens"][s.sid]["pass"] + latest["screens"][s.sid]["watch"]:
                ctx = ctxs.get(item["cik"]) or {}
                for k in ("latest_annual_form", "latest_annual_accn", "latest_annual_doc", "latest_annual_filed"):
                    item[k] = ctx.get(k)
            sheets[s.sid] = p

        # overlap
        ov = []
        allc = set()
        for s in screens:
            allc |= {c for c, r in results[s.sid].items() if r["class"] == PASS}
        for c in allc:
            ctx = ctxs[c]
            row = {"ticker": ctx["ticker"], "name": ctx["name"], "industry": ctx["industry"]}
            n = 0
            for s in screens:
                r = results[s.sid].get(c)
                row[SHEET[s.sid]] = class_cell(r)
                n += bool(r and r["class"] == PASS)
            row["screens_passed"] = n
            ov.append(row)
        ovd = pd.DataFrame(ov)
        if len(ovd):
            ovd = ovd.sort_values(["screens_passed", "ticker"], ascending=[False, True])
            ovd.to_excel(w, sheet_name="Overlap", index=False)
            _format_sheet(w.sheets["Overlap"], ovd)

        # events
        ev = []
        for c, ctx in ctxs.items():
            if ctx.get("event_types"):
                r = results.get("special", {}).get(c)
                ev.append({"ticker": ctx["ticker"], "name": ctx["name"], "industry": ctx["industry"],
                           "event_types": ctx["event_types"], "event_date": ctx.get("event_date"),
                           "months_since_event": ctx.get("months_since_event"),
                           "special_screen": r["class"] if r else "outside universe",
                           "why": why_text(next(s for s in screens if s.sid == "special"), r) if r and any(
                               s.sid == "special" for s in screens) else "",
                           "event_filing_url": ctx.get("event_filing_url"), "ttm_revenue": ctx.get("ttm_revenue"),
                           "ttm_operating_margin": ctx.get("ttm_operating_margin"), "ev_ebit": ctx.get("ev_ebit"),
                           "market_cap_usd": ctx.get("market_cap_usd"), "cik": c})
        for c, rec in records.items():  # events at companies without usable financials (new IPOs...)
            if c not in ctxs and rec.get("events") and not rec["stage"].startswith("not screened"):
                first = min(rec["events"].values(), key=lambda e: e["date"])
                ev.append({"ticker": rec["ticker"], "name": rec["name"], "industry": rec["industry"],
                           "event_types": ", ".join(sorted(rec["events"])), "event_date": first["date"],
                           "months_since_event": round((today - _d(first["date"])).days / 30.44, 1),
                           "special_screen": "not screened yet",
                           "why": "no financial statements in SEC XBRL yet (" + rec["stage"] + ")",
                           "event_filing_url": filing_index_url(c, first["accn"]) if first.get("accn") else None,
                           "cik": c})
        evd = pd.DataFrame(ev)
        if len(evd):
            evd = evd.sort_values("event_date", ascending=False)
            evd.to_excel(w, sheet_name="Events", index=False)
            _format_sheet(w.sheets["Events"], _prep(evd, list(evd.columns)), link_cols={"event_filing_url"})

        # industry cycle
        cy = pd.DataFrame(list(cyc.values()))
        if len(cy):
            cy = cy.sort_values("industry_margin_percentile") if "industry_margin_percentile" in cy else cy
            cy.to_excel(w, sheet_name="Industry_Cycle", index=False)
            _format_sheet(w.sheets["Industry_Cycle"], cy)

        # over-earners
        oe = [{"ticker": x["ticker"], "name": x["name"], "industry": x["industry"],
               "operating_margin_latest": x.get("operating_margin_latest"),
               "operating_margin_median": x.get("operating_margin_median"),
               "op_margin_vs_median": x.get("op_margin_vs_median"), "revenue_growth_2y": x.get("revenue_growth_2y"),
               "cycle_group": x.get("cycle_group"), "cik": c}
              for c, x in ctxs.items() if x.get("over_earning")]
        oed = pd.DataFrame(oe)
        if len(oed):
            oed.to_excel(w, sheet_name="Peak_Margins (check)", index=False)
            _format_sheet(w.sheets["Peak_Margins (check)"], oed)

        # data gaps for companies on any watch list
        gaps = []
        for s in screens:
            for c, r in results[s.sid].items():
                if r["class"] != "CHECK":
                    continue
                ctx = ctxs[c]
                cands = ctx.get("data_gap_candidates") or {}
                gaps.append({"screen": SHEET[s.sid], "ticker": ctx["ticker"], "name": ctx["name"],
                             "missing / to check": "; ".join(r["check_notes"]),
                             "candidate XBRL tags found in the filing": "; ".join(
                                 f"{k}: " + ", ".join(f"{x['tag']} ({x['latest_val']:,.0f} at {x['latest_end']})"
                                                      for x in v[:3]) for k, v in cands.items()),
                             "latest_annual_url": ctx.get("latest_annual_url")})
        # companies that couldn't be screened at all because a key figure wasn't found (never silently dropped)
        for c, rec in records.items():
            if c in ctxs or not (rec["stage"].startswith("revenue not found")
                                 or rec["stage"].startswith("no years with both")
                                 or rec["stage"].startswith("no annual revenue")):
                continue
            cands = rec.get("candidates") or {}
            gaps.append({"screen": "not screened", "ticker": rec["ticker"], "name": rec["name"],
                         "missing / to check": rec["stage"],
                         "candidate XBRL tags found in the filing": "; ".join(
                             f"{k}: " + ", ".join(f"{x['tag']} ({x['latest_val']:,.0f} at {x['latest_end']})"
                                                  for x in v[:3]) for k, v in cands.items()),
                         "latest_annual_url": None})
        gd = pd.DataFrame(gaps)
        if len(gd):
            gd.to_excel(w, sheet_name="Data_Gaps", index=False)
            _format_sheet(w.sheets["Data_Gaps"], gd, link_cols={"latest_annual_url"},
                          widths={"missing / to check": 80, "candidate XBRL tags found in the filing": 80})

        # all companies
        al = []
        for c, rec in records.items():
            row = {"ticker": rec["ticker"], "name": rec["name"], "industry": rec["industry"], "sic": rec["sic"],
                   "exchange": rec["exchange"], "stage": rec["stage"], "cik": c}
            for s in screens:
                r = results[s.sid].get(c)
                row[SHEET[s.sid]] = class_cell(r)
            ctx = ctxs.get(c)
            if ctx:
                row["latest_fy"] = ctx.get("latest_fy")
                row["latest_revenue_usd"] = ctx.get("latest_revenue_usd")
                row["flags"] = ctx.get("flags")
            al.append(row)
        ald = pd.DataFrame(al)
        if len(ald):
            ald = _prep(ald, list(ald.columns))
            ald.to_excel(w, sheet_name="All_Companies", index=False)
            _format_sheet(w.sheets["All_Companies"], ald)

        # annual data + evidence for listed companies
        annual, evid = [], []
        for c in sorted(listed):
            fs = _load_facts(c)
            if not fs:
                continue
            cd = CompanyData(fs)
            res, _ = compute(cd, cfg, today, allow_no_revenue=bool(in_ranges((ctxs.get(c) or {}).get("sic"),
                                                                             CLINICAL_STAGE)))
            if not res:
                continue
            m, rows = res
            t = ctxs[c]["ticker"]
            for r in rows[-12:]:
                annual.append({"ticker": t, **{k: v for k, v in r.items() if k != "neg_ic"}})
            for e in evidence_rows(cd, [r["fy"] for r in rows[-12:]]):
                e = {"ticker": t, **e}
                acc = (e.get("accession") or "").split(",")[0].strip()
                e["filing"] = filing_index_url(c, acc) if acc else None
                evid.append(e)
        an = pd.DataFrame(annual)
        if len(an):
            an.to_excel(w, sheet_name="Annual_Data", index=False)
            _format_sheet(w.sheets["Annual_Data"], an)

        _kv_sheet(w, "Rules", rules_rows(cfg), widths=(46, 140))
        gr = pd.DataFrame(group_rows() + [{"screen": "Core / Fortress / Emerging exclusions", "sic_from": r["from"],
                                           "sic_to": r["to"], "label": f"{r['label']} - {r.get('source', '')}"}
                                          for r in cfg["exclude_sic"]])
        gr.to_excel(w, sheet_name="Industry_Groups", index=False)
        _format_sheet(w.sheets["Industry_Groups"], gr, widths={"label": 60})

        info = [("What this is", "Six screens of NYSE + Nasdaq companies built on SEC filings (and Twelve Data "
                                 "prices). Each screen has a ranked PASS sheet and a '- watch' sheet (CHECK manually, "
                                 "NEAR misses, 'Price too high (rest passes)', 'Failed 1 rule'). Start with 'Overlap' for names passing several screens. Every input is "
                                 "in the evidence CSV with a link to its SEC filing.")]
        info += [(k.replace("_", " ").capitalize(), str(v)) for k, v in run_info.items()]
        info += [("", "")] + summary_rows
        stage_counts = pd.Series([r["stage"].split(":")[0] for r in records.values()]).value_counts()
        info += [("", "")] + [(f"Companies: {k}", str(v)) for k, v in stage_counts.items()]
        info += [("Evidence file", os.path.basename(path).replace(".xlsx", "_evidence.csv")),
                 ("Not financial advice", "A research filter to decide what to read next, not a buy list.")]
        _kv_sheet(w, "Read_Me", info)
        wb = w.book
        wb.move_sheet("Read_Me", offset=-(len(wb.sheetnames) - 1))
        if "Overlap" in wb.sheetnames:
            wb.move_sheet("Overlap", offset=-(wb.sheetnames.index("Overlap") - 1))

    ev_path = path.replace(".xlsx", "_evidence.csv")
    if evid:
        cols = ["ticker", "concept", "fy", "value", "unit", "taxonomy", "tag", "period_start", "period_end", "form",
                "filed", "accession", "first_reported_value", "first_reported_accession", "filing"]
        with open(ev_path, "w", newline="", encoding="utf-8-sig") as f:
            wr = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            wr.writeheader()
            for e in evid:
                wr.writerow(e)
    if write_latest:
        with open(os.path.join(out_dir, "latest_results.json"), "w", encoding="utf-8") as f:
            json.dump(latest, f, indent=1, default=str)


def _load_facts(cik):
    from .pipeline import load_cached_facts
    return load_cached_facts(cik)


def _jsonable(v):
    if isinstance(v, float) and v != v:
        return None
    if hasattr(v, "item"):
        try:
            return v.item()
        except (ValueError, AttributeError):
            return str(v)
    return v
