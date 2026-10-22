"""The triage rules, written down before any backtest result was seen (pre-registered 2026-10-22).
Changing anything here is a rule change: log it in triage/CHANGES.md with the date and the reason.

Three triages share one method (the shape of the biotech crash/slide triage):

  1. Backend requirements decide which stocks are covered at all. They never move a call.
     US common stock (10-K filer, USD, NYSE / Nasdaq / NYSE American; no funds, REITs, banks or insurers),
     enough years of SEC data, a recent annual report, size, trading volume, leverage.
  2. An event dates the opportunity, from month-end data only:
       hidden    the month-end close is 40%+ below the highest of the previous 12 month-end closes
       emerging  the earnings yield (EBITDA / EV; EBIT / EV when depreciation is half of EBITDA or more) enters
       core      (EBIT / EV) the cheapest fifth of the company's own last 5 years of month-ends (24+ needed), or the
                 cheapest fifth of its industry peers that month
     The event is the first month the condition holds after a month it did not, at least 6 months after the
     company's previous event of the same triage.
  3. Cells score the event against the thesis: green +1, neutral or N/A 0, red -1, times the cell's weight.
     Score = sum / 100, from -1 to +1. Call:
       Avoid           a hard Avoid (below), or score <= AVOID_AT
       Buy candidate   no hard Avoid and score >= BUY_AT
       Watch           the rest. A Watch turns Buy candidate when a top performer owner's 13F for the event's quarter
                       (filed after the event, by the 45-day deadline) reports it at 3%+ of its portfolio; its return
                       then counts from the next entry day after that filing.
       TBU             13F or insider data for that date not loaded yet
  4. Outcome: total return from the entry (open of the first trading day after the month-end) to 12 months later,
     against the 10 most similar US stocks bought the same day and an index ETF.
"""

BUY_AT, AVOID_AT = 0.30, -0.10
COOLDOWN_MONTHS = 6
OWN_PAST_MONTHS, OWN_PAST_MIN = 60, 24
CHEAP_PCTL = 0.80                    # cheapest fifth: yield above 80% of the comparison values
PEER_MIN = 8                         # peers needed in a group (4-digit SIC, else 3-, else 2-digit)
PEER_MIN_MCAP = 100e6
HIDDEN_FALL = -0.40

# 13F: a high conviction owner is a 13F filer that is not an index fund, broker platform, fund house or quant fund
# (config portal.holders lists, or more than 1,000 stocks), with a reported stock portfolio of $100M+, holding the
# company at 3%+ of that portfolio
FUND_MIN_AUM, FUND_MIN_WEIGHT, FUND_MAX_POSITIONS = 100e6, 0.03, 1000
# top performer owners: ranked on past events of all three triages they held at 3%+ (walk-forward)
TOP_N, TOP_MIN_COMPANIES, TOP_PRIOR_PLAYS, TOP_WEIGHT_CAP, TOP_CONC_CAP, TOP_HIT = 20, 5, 5, 0.20, 2.0, 0.10
# insiders: open-market buys (P) minus discretionary sales (S, not under a 10b5-1 plan, not on an option-exercise day)
# filed in the 180 days up to the month-end; material = the larger of $25k and 0.01% of market cap
INSIDER_DAYS, INSIDER_MIN_USD, INSIDER_MIN_MCAP_SHARE = 180, 25_000, 0.0001

INDEX = {"hidden": ("SPY", "S&P 500 (SPY)"), "emerging": ("IWM", "Russell 2000 (IWM)"),
         "core": ("SPY", "S&P 500 (SPY)")}

KINDS = {
    "hidden": {
        "label": "Hidden Earnings",
        "thesis": "A profitable business whose share price has collapsed. If the business still earns and generates "
                  "cash, and is cheap, the fear should fade and the price recover.",
        "event": "the month-end close is 40%+ below the highest of the previous 12 month-end closes",
        "universe": "broad",
        "backend": {"min_years": 5, "min_mcap": 100e6, "max_mcap": None, "min_adv": 200e3, "max_lev": 3.0,
                    "min_revenue": None},
        "hard": [("ttm_loss", "operating loss over the last 12 months (the business isn't earning)")],
        "cells": [
            # key, label, weight
            ("trend", "Profit Trend", 20),
            ("fcf", "Cash Yield", 15),
            ("ev_ebit", "EV / EBIT", 15),
            ("roic", "Returns on Capital", 10),
            ("sales", "Sales Trend", 10),
            ("insider", "Insider Buy/Sell", 10),
            ("funds", "High Conviction Owners", 10),
            ("top", "Top Performer Owners", 10),
        ],
    },
    "emerging": {
        "label": "Emerging Compounders",
        "thesis": "A profitable small or mid-size company growing fast, getting more profitable as it grows and not "
                  "issuing many shares. Such companies rarely look cheap; this triage waits until it is cheap against "
                  "its own past or its industry.",
        "event": "its EBITDA yield (EBITDA / EV; EBIT / EV when depreciation is half of EBITDA or more) enters the "
                 "cheapest fifth of its own last 5 years of month-ends, or of its industry peers that month",
        "universe": "emerging",
        "backend": {"min_years": 4, "min_mcap": 150e6, "max_mcap": 10e9, "min_adv": 200e3, "max_lev": 2.5,
                    "min_revenue": None},
        "hard": [("not_profitable", "EBITDA not positive over the last 12 months and the last fiscal year")],
        "cells": [
            ("own", "Cheap vs Own Past", 12),
            ("peers", "Cheap vs Peers", 10),
            ("growth", "Sales Growth", 16),
            ("recent", "Growth Now", 12),
            ("oplev", "Operating Leverage", 10),
            ("gm", "Gross Margin", 6),
            ("dilution", "Share Count", 6),
            ("insider", "Insider Buy/Sell", 8),
            ("funds", "High Conviction Owners", 10),
            ("top", "Top Performer Owners", 10),
        ],
    },
    "core": {
        "label": "Core Compounders",
        "thesis": "A durable business with high, persistent returns on capital that converts profit into cash. "
                  "Such businesses rarely look cheap; this triage waits until it is cheap against its own past or "
                  "its industry, and checks that profits aren't falling.",
        "event": "its earnings yield (EBIT / EV) enters the cheapest fifth of its own last 5 years of month-ends, or "
                 "of its industry peers that month",
        "universe": "core",
        "backend": {"min_years": 8, "min_mcap": 300e6, "max_mcap": None, "min_adv": 1e6, "max_lev": 3.0,
                    "min_revenue": 200e6},
        "hard": [("ttm_loss", "operating loss over the last 12 months")],
        "cells": [
            ("own", "Cheap vs Own Past", 12),
            ("peers", "Cheap vs Peers", 8),
            ("roic", "Returns on Capital", 16),
            ("persist", "Returns That Persist", 10),
            ("growth", "Sales Growth", 8),
            ("conversion", "Cash Conversion", 8),
            ("trend", "Profit Trend", 12),
            ("insider", "Insider Buy/Sell", 8),
            ("funds", "High Conviction Owners", 8),
            ("top", "Top Performer Owners", 10),
        ],
    },
}

# green / red bands per cell (value -> 'g' | 'n' | 'r'); (green_at, red_below) for higher-is-better,
# ('low', green_at_most, red_above) for lower-is-better
BANDS = {
    "hidden": {"trend": (0.0, -0.25), "fcf": (0.06, 0.0), "ev_ebit": ("low", 10.0, 15.0), "roic": (0.12, 0.08),
               "sales": (0.0, -0.05)},
    "emerging": {"own": (0.80, 0.50), "peers": (0.80, 0.50), "growth": (0.15, 0.05), "recent": (0.08, 0.0),
                 "gm": (0.35, 0.20), "dilution": ("low", 0.03, 0.08)},
    "core": {"own": (0.80, 0.50), "peers": (0.80, 0.50), "roic": (0.15, 0.10), "persist": (0.80, 0.60),
             "growth": (0.05, 0.0), "conversion": (0.80, 0.50), "trend": (0.0, -0.15)},
}

OUTCOMES = (("Winner", 0.20), ("Gain", 0.0), ("Loss", None))     # 1-year return >= +20% / 0 to +20% / below 0


def band(kind, key, v):
    b = BANDS.get(kind, {}).get(key)
    if v is None or b is None:
        return "n"
    if b[0] == "low":
        return "g" if v <= b[1] else "r" if v > b[2] else "n"
    return "g" if v >= b[0] else "r" if v < b[1] else "n"


def weights(kind):
    return {k: w for k, _, w in KINDS[kind]["cells"]}


def score(kind, colours):
    """colours: {cell: 'g' | 'n' | 'r' | None} -> score in [-1, 1]."""
    pts = {"g": 1, "r": -1}
    return round(sum(w * pts.get(colours.get(k), 0) for k, w in weights(kind).items()) / 100.0, 4)


def call(kind, colours, hard):
    """(verdict, reasons): 'overdone' = Buy candidate, 'close' = Watch, 'justified' = Avoid (crash-triage codes)."""
    s = score(kind, colours)
    if hard:
        return "justified", hard, s
    if s <= AVOID_AT:
        return "justified", [f"score {s:+.2f} (Avoid at {AVOID_AT:+.2f} or lower)"], s
    if s >= BUY_AT:
        return "overdone", [], s
    return "close", [f"score {s:+.2f} (Buy candidate from {BUY_AT:+.2f})"], s


def outcome(r):
    for name, at in OUTCOMES:
        if at is None or r >= at:
            return name
    return OUTCOMES[-1][0]


assert all(sum(w for _, _, w in k["cells"]) == 100 for k in KINDS.values()), "weights must add up to 100"
