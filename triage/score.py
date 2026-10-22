"""Cells, calls and outcomes for every event (rules: triage/rules.py; events: triage/episodes.py).

Each cell is [colour, text, note, bucket]: colour g (meets the thesis) / n (in between, or N/A) / r (against it),
the value shown, where it comes from (hover), and a filter bucket. Every number is as of the event's month-end.
"""
from bisect import bisect_left

from qs.backtest_support import write_json

from . import rules as R
from .episodes import CAP
from . import paths as P

NA = ["n", "N/A", "", "N/A"]


def money(v):
    a = abs(v or 0)
    s = f"${a / 1e9:.1f}B" if a >= 1e9 else f"${a / 1e6:.0f}M" if a >= 1e7 else f"${a / 1e6:.1f}M" if a >= 1e6 \
        else f"${a / 1e3:.0f}K" if a >= 1e3 else f"${a:.0f}"
    return s


def pct(v, d=0, sign=False):
    if v is None:
        return "N/A"
    s = f"{abs(v) * 100:.{d}f}%"
    return (("+" if v > 0 else "−" if v < 0 else "") if sign else ("−" if v < 0 else "")) + s


def pts(v):
    return f"{'+' if v >= 0 else '−'}{abs(v) * 100:.1f} pts"


def cell(kind, key, v, text, note, buckets):
    """Colour by the band, bucket by the colour (buckets: (green, neutral, red) labels)."""
    if v is None:
        return list(NA)
    c = R.band(kind, key, v)
    return [c, text, note, buckets[{"g": 0, "n": 1, "r": 2}[c]]]


# ------------------------------------------------------------------ thesis cells
def c_trend(kind, ev):
    now, then = ev["rec"].get("ebit"), ev.get("ebit_1y")
    if now is None or then is None:
        return list(NA)
    note = f"Operating income, last 12 months: {money(now)} vs {money(then)} a year earlier (as filed by each month-end)"
    if then > 0:
        g = now / then - 1
        return cell(kind, "trend", g, pct(g, 0, True), note, ("Up", "Down a little", "Down a lot"))
    if now > 0:
        return ["g", "Back to profit", note, "Up"]
    return ["r", "Loss both years", note, "Down a lot"]


def c_simple(kind, key, v, fmt, note, buckets):
    return cell(kind, key, v, fmt(v) if v is not None else "N/A", note, buckets)


def thesis_cells(kind, ev):
    r, info = ev["rec"], ev["info"]
    out = {}
    if kind == "hidden":
        out["trend"] = c_trend(kind, ev)
        fy = (r["fcf"] / r["mc"]) if (r.get("fcf") is not None and r.get("mc")) else None
        out["fcf"] = c_simple(kind, "fcf", fy, lambda v: pct(v, 1),
                              f"Free cash flow, last 12 months ({money(r.get('fcf'))}) ÷ market cap ({money(r.get('mc'))})",
                              ("6%+", "0–6%", "Negative"))
        ee = (r["ev"] / r["ebit"]) if (r.get("ev") and r.get("ebit") and r["ebit"] > 0) else None
        out["ev_ebit"] = c_simple(kind, "ev_ebit", ee, lambda v: f"{v:.1f}×",
                                  f"EV ({money(r.get('ev'))}: market cap + debt − cash) ÷ operating income, last 12 months",
                                  ("10× or less", "10–15×", "Over 15×"))
        out["roic"] = c_simple(kind, "roic", r.get("roic"), lambda v: pct(v),
                               "Median return on invested capital over up to 10 fiscal years", ("12%+", "8–12%", "Under 8%"))
        out["sales"] = c_simple(kind, "sales", r.get("rc3"), lambda v: pct(v, 0, True) + "/yr",
                                "Revenue growth per year over 3 fiscal years", ("Growing", "Down 0–5%/yr", "Down 5%+/yr"))
        return out
    yname = "EBITDA yield" if kind == "emerging" else "Earnings yield (EBIT / EV)"
    if info.get("p_own") is not None:
        out["own"] = cell(kind, "own", info["p_own"], f"Cheaper than {round(info['p_own'] * 100)}%",
                          f"{yname} {pct(info['y'], 1)} vs its median {pct(info.get('y_med'), 1)} over its last "
                          f"{info['n_own']} month-ends: cheaper than {round(info['p_own'] * 100)}% of them",
                          ("Cheapest fifth", "Cheaper than its median", "Dearer than its median"))
    else:
        out["own"] = ["n", "N/A", f"Needs {R.OWN_PAST_MIN}+ month-ends of its own history", "N/A"]
    if info.get("p_peer") is not None:
        out["peers"] = cell(kind, "peers", info["p_peer"], f"Cheaper than {round(info['p_peer'] * 100)}%",
                            f"{yname} {pct(info['y'], 1)}: cheaper than {round(info['p_peer'] * 100)}% of {info['n_peer']} companies of $100M+ with industry "
                            f"code {(r.get('sic') or '')[:info['peer_lvl']]} ({info['peer_lvl']}-digit) that month",
                            ("Cheapest fifth", "Cheaper than median", "Dearer than median"))
    else:
        out["peers"] = ["n", "N/A", f"Fewer than {R.PEER_MIN} industry peers with a yield", "N/A"]
    if kind == "emerging":
        out["growth"] = c_simple(kind, "growth", r.get("rc3"), lambda v: pct(v, 0, True) + "/yr",
                                 "Revenue growth per year over 3 fiscal years", ("15%+/yr", "5–15%/yr", "Under 5%/yr"))
        g, src = (r.get("ytdg"), "year-to-date vs the same months a year earlier") if r.get("ytdg") is not None else \
            (r.get("fyg"), "latest fiscal year (no year-to-date figure)")
        out["recent"] = c_simple(kind, "recent", g, lambda v: pct(v, 0, True), f"Revenue growth, {src}",
                                 ("8%+", "0–8%", "Shrinking"))
        m = r.get("em3") if r.get("em3") is not None else r.get("om3")
        s = r.get("sga3")
        if m is None and s is None:
            out["oplev"] = ["n", "N/A", "No margin or SG&A history", "N/A"]
        else:
            col = "g" if (m is not None and m >= 0) else "n" if (s is not None and s <= 0) else "r"
            txt = f"Margin {pts(m)}" if m is not None else f"SG&A {pts(s)}"
            out["oplev"] = [col, txt, "3-year change in EBITDA margin (operating margin if no EBITDA)"
                            + (f"; SG&A ÷ revenue {pts(s)}" if s is not None else ""),
                            {"g": "Margin up", "n": "Overheads down", "r": "Both worse"}[col]]
        if r.get("gm") is None and not r.get("gprep"):
            out["gm"] = ["n", "N/A", "No cost-of-sales line (service business)", "N/A"]
        else:
            out["gm"] = c_simple(kind, "gm", r.get("gm"), lambda v: pct(v), "Gross margin, last 12 months",
                                 ("35%+", "20–35%", "Under 20%"))
        out["dilution"] = c_simple(kind, "dilution", r.get("sh3"), lambda v: pct(v, 1, True) + "/yr",
                                   "Share count growth per year over 3 years", ("3%/yr or less", "3–8%/yr", "Over 8%/yr"))
    else:
        out["roic"] = c_simple(kind, "roic", r.get("roic"), lambda v: pct(v),
                               "Median return on invested capital over up to 10 fiscal years", ("15%+", "10–15%", "Under 10%"))
        out["persist"] = c_simple(kind, "persist", r.get("roics"), lambda v: pct(v) + " of years",
                                  "Share of fiscal years with return on invested capital of 10%+", ("80%+", "60–80%", "Under 60%"))
        out["growth"] = c_simple(kind, "growth", r.get("rc"), lambda v: pct(v, 0, True) + "/yr",
                                 "Revenue growth per year over up to 10 fiscal years", ("5%+/yr", "0–5%/yr", "Shrinking"))
        out["conversion"] = c_simple(kind, "conversion", r.get("fcfc"), lambda v: f"{v:.2f}×",
                                     "Free cash flow ÷ net income, summed over the fiscal years", ("0.8×+", "0.5–0.8×", "Under 0.5×"))
        out["trend"] = c_trend(kind, ev)
    return out


def hard_avoid(kind, r):
    if kind == "emerging":
        heavy = (r.get("das") or 0) >= 0.5
        a, b = (r.get("ebit"), r.get("fyebit")) if heavy or r.get("ebitda") is None else (r.get("ebitda"), r.get("fyebitda"))
        if (a is not None and a <= 0) or (b is not None and b <= 0):
            return [R.KINDS[kind]["hard"][0][1]]
        return []
    e = r.get("ebit")
    return [R.KINDS[kind]["hard"][0][1]] if (e is not None and e <= 0) else []


# ------------------------------------------------------------------ owners and insiders cells
def c_insider(ev):
    v = ev.get("ins")
    if v is None:
        return list(NA)
    if v["n"] == 0:
        return ["n", "None", "No open-market buys or discretionary sales in Form 4s filed in the 180 days to the "
                "month-end", "None"]
    big = v["largest"]
    note = (f"Open-market buys {money(v['buy'])}, discretionary sales {money(v['sell'])}"
            + (f", plan / option-exercise sales {money(v['plan'])} (not counted)" if v["plan"] else "")
            + f"; counts at {money(v['material'])}+ (the larger of $25K and 0.01% of market cap)")
    if big:
        note += f". Largest: {big[4]}{' (' + big[5] + ')' if big[5] else ''} {money(big[3])} on {big[0]}"
    if v["colour"] == "n":
        return ["n", "Small", note, "None"]
    return [v["colour"], f"{'Bought' if v['net'] > 0 else 'Sold'} {money(abs(v['net']))}", note,
            "Bought" if v["net"] > 0 else "Sold"]


def c_funds(ev):
    f = ev.get("fund")
    if f is None:
        return list(NA)
    n = len(f["list"])
    head = ("; ".join(f"{nm} {w * 100:.1f}%" for _, nm, w, _ in f["list"][:8]) + f" (end of {f['before']})") if n \
        else f"No high conviction owner held it at 3%+ of its portfolio at the end of {f['before']}"
    later = "; ".join(f"{nm} {w * 100:.1f}% (filed {d})" for _, nm, w, d in f["later"][:6])
    note = head + (f" · Later, for {f['after']}: {later}" if later else "")
    return ["g" if n >= 2 else "n", "None" if n == 0 else f"{n} fund{'s' if n > 1 else ''}", note,
            "None" if n == 0 else "1 fund" if n == 1 else "2+ funds"]


def c_top(ev):
    if ev.get("fund") is None:
        return list(NA)
    t, tl = ev.get("top") or [], ev.get("top_later") or []
    note = "; ".join([f"{n} (top {rk}: {h} of {k} plays beat similar stocks by 10+ points)" for n, rk, h, k in t] +
                     [f"{n} (top {rk}), 13F filed {d}" for n, rk, h, k, d in tl])
    if t:
        return ["g", "Yes", note, "Yes"]
    if tl:
        return ["n", f"Yes, {tl[0][4]}", note, "Yes"]
    return ["n", "No", note or "No top performer owner among its high conviction owners", "No"]


# ------------------------------------------------------------------ one event
def evaluate(kind, ev, ins_through, months_d, rets, index_sym):
    r = ev["rec"]
    cells = thesis_cells(kind, ev)
    cells["insider"] = c_insider(ev)
    cells["funds"] = c_funds(ev)
    cells["top"] = c_top(ev)
    order = [k for k, _, _ in R.KINDS[kind]["cells"]]
    cells = {k: cells.get(k, list(NA)) for k in order}
    colours = {k: (c[0] if c[1] != "N/A" else None) for k, c in cells.items()}
    hard = hard_avoid(kind, r)
    verdict, why, s = R.call(kind, colours, hard)
    pending = []
    if ev.get("fund") is None:
        pending.append("13F holdings for this date not loaded yet")
    if ev.get("ins") is None:
        pending.append("insider trades for this date not loaded yet")
    call_i, call_date, upgraded = ev["i"], ev["d"], None
    if verdict == "close" and ev.get("top_later"):
        fd = ev["top_later"][0][4]
        j = bisect_left(months_d, fd)                 # first month-end on or after the 13F filing
        if j < len(months_d):
            call_i, call_date = j, fd
            verdict, upgraded = "overdone", f"Watch until {fd}: a top performer owner's 13F filed then"
            why = [upgraded]
    if pending:
        verdict, why, call_i, call_date, upgraded = "tbu", pending, ev["i"], ev["d"], None
    out = {"id": ev["id"], "cik": ev["cik"], "name": r.get("nm") or "", "ticker": r.get("tk") or "",
           "date": ev["d"], "ym": ev["ym"], "sic": r.get("sic"), "verdict": verdict, "why": why, "score": s,
           "call_date": call_date, "upgraded": upgraded, "mcap": r.get("mc"), "price": r.get("px"),
           "factors": cells, "insider_net": (ev.get("ins") or {}).get("net"),
           "move": round(r["dd"] * 100, 1) if kind == "hidden" and r.get("dd") is not None else None,
           "p_own": ev["info"].get("p_own"), "p_peer": ev["info"].get("p_peer")}
    # outcome from the call's entry day
    sym = r.get("sym")
    own = rets.path(ev["cik"], sym, call_i)
    if own[0] is None:
        out["no_entry"] = True
        return out, None
    vals, complete, last_day, stopped = own
    out["entry_date"] = rets.e.get(rets.months[call_i]) if call_i < len(rets.months) else None
    out["path"] = [round(v * 100, 2) for v in vals]
    out["ret"], out["ret_to"], out["played"] = round(vals[-1] * 100, 1), last_day, complete
    if stopped:
        out["stopped"] = stopped
    sims = []
    for c in ev.get("sim") or []:
        p = rets.path(c, ev.get("sim_sym", {}).get(c), call_i)
        if p[0] is not None and len(p[0]) == len(vals):
            sims.append([min(v, CAP) for v in p[0]])
    if sims:
        cp = [sum(s_[k] for s_ in sims) / len(sims) for k in range(len(vals))]
        out["ctrl_path"] = [round(v * 100, 2) for v in cp]
        out["ctrl_ret"] = round(cp[-1] * 100, 1)
    ip = rets.path(index_sym, index_sym, call_i, index=True)
    if ip[0] is not None and len(ip[0]) == len(vals):
        out["idx_path"] = [round(v * 100, 2) for v in ip[0]]
        out["idx_ret"] = round(ip[0][-1] * 100, 1)
    if complete:
        out["outcome"] = R.outcome(vals[-1])
    learn = None
    if complete and sims and verdict != "tbu":
        learn = {"y": vals[-1] - cp[-1], "abs": vals[-1], "end": last_day}
    return out, learn


def write(kind, items):
    P.ensure(P.OUT)
    write_json(f"{P.OUT}/{kind}.json.gz", items)
