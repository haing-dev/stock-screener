"""Gates (pass/fail), pillar scores, flags and the industry-concentration proxy.

Each rule carries the manager insight it encodes so the Rules sheet is self-documenting.
"""
import pandas as pd

# ------------------------------------------------------------------ gates
# (id, name, metric, op, config key, insight)
GATES = [
    ("G1", "History", "years_with_data", ">=", "min_years_data",
     "Kantesaria: only own what you're confident stays dominant 10+ years. Hohn: 'good companies stay good' - "
     "you need a long record to see it."),
    ("G2", "Recent report", "years_since_latest_fy", "<=", "max_years_since_latest_fy",
     "Data must be current (latest annual report within ~1.5 years)."),
    ("G3", "Size", "latest_revenue_usd", ">=", "min_revenue_usd",
     "Dorsey: liquid enough to own; very small filers also have patchier XBRL data."),
    ("G4", "Consistent profits", "operating_loss_years", "<=", "gates.max_operating_loss_years",
     "Kantesaria: quality = growth AND predictability. At most one operating-loss year (allows a COVID-type shock)."),
    ("G5a", "High returns (median)", "roic_median", ">=", "gates.min_median_roic",
     "Dorsey's moat research: companies earning >15% return on invested capital for >15 years."),
    ("G5b", "High returns (consistency)", "roic_share_above_floor", ">=", "gates.min_share_of_years_above_floor",
     "Returns must be persistent, not one good stretch: ROIC above the floor in most years."),
    ("G6", "Growth", "revenue_cagr", ">=", "gates.min_revenue_cagr",
     "Kantesaria: predictable but slow (2-3%) businesses underperform; Dorsey: prefer a reinvestment runway."),
    ("G7", "Cash conversion", "fcf_conversion", ">=", "gates.min_fcf_conversion",
     "Kantesaria/Gaonkar: value is free cash flow; reported profits must turn into cash (sum FCF / sum net income)."),
    ("G8", "Balance sheet", "net_debt_to_ocf", "<=", "gates.max_net_debt_to_ocf",
     "Gaonkar: avoid over-levered companies/public LBOs (Altice). Singer: survive first. Net debt / 3-yr avg "
     "operating cash flow."),
]
NUMERIC_SENSITIVE = {"G5a", "G5b", "G6", "G7", "G8"}


def cfg_get(cfg, key):
    cur = cfg
    for k in key.split("."):
        cur = cur[k]
    return cur


def eval_gate(value, op, threshold):
    if value is None:
        return "FAIL", "no data"
    ok = value >= threshold if op == ">=" else value <= threshold
    return ("PASS" if ok else "FAIL"), ""


def scaled(op, threshold, s):
    """s > 0 = stricter, s < 0 = looser."""
    if op == ">=":
        return threshold * (1 + s) if threshold >= 0 else threshold * (1 - s)
    return threshold * (1 - s) if threshold >= 0 else threshold * (1 + s)


def run_gates(m, cfg, s=0.0):
    res = {}
    for gid, name, metric, op, key, _ in GATES:
        thr = cfg_get(cfg, key)
        if s and gid in NUMERIC_SENSITIVE:
            thr = scaled(op, thr, s)
            if gid == "G5b":
                thr = min(thr, 1.0)
        val = m.get(metric)
        if gid == "G8" and val is None and m.get("ocf_avg_3y") is not None and m["ocf_avg_3y"] <= 0:
            res[gid] = ("FAIL", "operating cash flow <= 0", val, thr)
            continue
        status, why = eval_gate(val, op, thr)
        if gid == "G7" and val is None and m.get("fcf_conversion_years", 0) >= 5:
            why = "cumulative net income <= 0"
        if gid == "G6" and val is None:
            why = "need >= 5 years of revenue, positive at both ends"
        if gid == "G3" and val is None:
            why = f"no FX rate for currency {m.get('currency')} in config.json fx_to_usd"
        res[gid] = (status, why, val, thr)
    return res


# ------------------------------------------------------------------ pillars
# metric, higher_is_better
PILLARS = {
    "predictability": [("revenue_growth_std", False), ("revenue_decline_years", False), ("operating_margin_std", False)],
    "pricing_power": [("gross_margin_median", True), ("gross_margin_std", False),
                      ("gross_margin_change_2021_2023", True), ("operating_margin_median", True),
                      ("operating_margin_trend", True)],
    "returns_moat_direction": [("roic_median", True), ("roic_trend", True), ("incremental_roic", True)],
    "growth_runway": [("revenue_cagr", True), ("nopat_cagr", True), ("fcf_per_share_cagr", True)],
    "capital_allocation": [("share_count_cagr", False), ("acquisitions_to_ocf", False),
                           ("sbc_to_revenue", False), ("goodwill_to_assets", False)],
    "balance_sheet": [("net_debt_to_ocf", False)],
}
PILLAR_SOURCES = {
    "predictability": "Kantesaria: growth x predictability; 'market closed for 10 years' test.",
    "pricing_power": "Hohn: price above inflation is the moat test; Kantesaria: pricing power is the hallmark; "
                     "2021-23 inflation is a natural experiment - did margins hold?",
    "returns_moat_direction": "Dorsey: moat AND its direction; Gaonkar: value = incremental ROIC x capital deployable.",
    "growth_runway": "Dorsey: narrower moat with runway beats widest moat with none; Kantesaria: compounding.",
    "capital_allocation": "Dorsey: capital allocation is rare; Kantesaria: avoid serial acquirers, prefer buybacks; "
                          "Gaonkar: expense stock-based pay.",
    "balance_sheet": "Gaonkar/Singer: avoid leverage that can force you out.",
}


def score(df, weights):
    """Percentile-rank each metric within df (the scored set), average into pillars (0-100)."""
    out = pd.DataFrame(index=df.index)
    for pillar, metrics in PILLARS.items():
        parts = []
        for metric, hib in metrics:
            if metric not in df:
                continue
            s = pd.to_numeric(df[metric], errors="coerce")
            if s.notna().sum() < 2:
                continue
            r = s.rank(pct=True, ascending=hib)
            parts.append(r)
        out[pillar] = (pd.concat(parts, axis=1).mean(axis=1) * 100).round(1) if parts else float("nan")
    wsum = pd.Series(0.0, index=df.index)
    acc = pd.Series(0.0, index=df.index)
    for pillar, w in weights.items():
        if pillar in out:
            v = out[pillar]
            acc += v.fillna(0) * w
            wsum += v.notna() * w
    out["composite"] = (acc / wsum.replace(0, float("nan"))).astype(float).round(1)
    return out


# ------------------------------------------------------------------ flags
def flags_for(m, cd_flags, sic_flag, info, cfg):
    f = list(sorted(cd_flags))
    fl = cfg["flags"]
    if m.get("acquisitions_to_ocf") is not None and m["acquisitions_to_ocf"] > fl["serial_acquirer_acq_to_ocf"]:
        f.append(f"serial acquirer? acquisitions = {m['acquisitions_to_ocf']:.0%} of operating cash flow (Kantesaria)")
    if m.get("goodwill_to_assets") is not None and m["goodwill_to_assets"] > fl["goodwill_to_assets"]:
        f.append(f"goodwill = {m['goodwill_to_assets']:.0%} of assets - growth may be bought")
    if m.get("sbc_to_revenue") is not None and m["sbc_to_revenue"] > fl["sbc_to_revenue"] and \
            (m.get("latest_revenue") or 0) >= 50e6:
        f.append(f"stock-based pay = {m['sbc_to_revenue']:.0%} of revenue (Gaonkar: expense it)")
    if m.get("latest_equity_negative"):
        f.append("negative equity (usually heavy buybacks) - ROIC uses operating capital, check debt")
    if m.get("any_negative_ic_year"):
        f.append("near-zero/negative invested capital in some year (ROIC capped at 100%)")
    if m.get("op_income_approx_years") and m["op_income_approx_years"] < (m.get("years_with_data") or 0):
        f.append(f"operating income not tagged in {m['op_income_approx_years']} year(s) - approximated as pretax "
                 "income + interest expense")
    if not m.get("debt_found"):
        f.append("no standard debt tag found - treated as debt-free; confirm on the balance sheet")
    if m.get("currency") and m["currency"] != "USD":
        f.append(f"reports in {m['currency']} (foreign filer: check tags in Evidence)")
    if m.get("restated_years"):
        f.append("restated figures in " + ", ".join(str(y) for y in sorted(set(m["restated_years"]))) + " (latest used)")
    if m.get("share_count_cagr") is None:
        f.append("share-count trend unavailable")
    if not m.get("acquisitions_tagged"):
        f.append("no acquisition-spend tag (assumed none)")
    if sic_flag:
        f.append(f"industry note: {sic_flag['label']} - {sic_flag['why']}")
    if info.get("entityType") and info["entityType"] != "operating":
        f.append(f"SEC entity type '{info['entityType']}'")
    return f


# ------------------------------------------------------------------ industry concentration proxy
def concentration(df):
    """Crude market-structure proxy: revenue share among SEC filers with the same 4-digit SIC code.

    Not real market share (ignores private and foreign non-SEC competitors), but a top-2 share
    near 100% in a SIC code is a hint of a duopoly worth checking qualitatively.
    """
    d = df[["sic", "latest_revenue_usd"]].copy()
    d = d[d["sic"].astype(str).str.len() > 0]
    d["latest_revenue_usd"] = pd.to_numeric(d["latest_revenue_usd"], errors="coerce")
    d = d.dropna()
    res = pd.DataFrame(index=df.index, columns=["sic_peer_count", "sic_revenue_share", "sic_rank",
                                                "sic_top2_share", "sic_hhi"])
    for sic, grp in d.groupby("sic"):
        tot = grp["latest_revenue_usd"].sum()
        if tot <= 0:
            continue
        shares = grp["latest_revenue_usd"] / tot
        top2 = shares.sort_values(ascending=False).head(2).sum()
        hhi = (shares ** 2).sum() * 10000
        ranks = grp["latest_revenue_usd"].rank(ascending=False, method="min")
        n = len(grp)
        for idx in grp.index:
            # with fewer than 3 SEC-filer peers a 'top-2 share' is trivially 100% - leave blank
            res.loc[idx] = [n, shares[idx], int(ranks[idx]), top2 if n >= 3 else None, round(hhi) if n >= 3 else None]
    return res
