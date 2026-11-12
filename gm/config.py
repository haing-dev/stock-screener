"""Global Macro Book: every rule in one place.

A config is a plain dict. `book.run(R, cfg=...)` reads only these keys, so a variant is a changed copy of a config
(`variant(BASE, trend={"kind": "cont"})`) and every trial is reproducible from its config (gm/trials.py logs it).

BASE = gm-1.2.1 (the live paper book; gm-1.2.0 with the registered input-layer look-ahead fixes C1-C4, gm/CHANGES.md
2026-11-11). CANDIDATE = the gm-2.0.1 candidate (gm-2.0 + the same fixes), frozen only after the Bloomberg data
and the decisions in docs/research/global_macro/gap_review_crosscheck_2026-10-31.md.
"""
import copy
import hashlib
import json

BASE = {
    "name": "gm-1.2.1",
    # family risk shares (sum 1)
    "family_w": {"trend": 0.30, "econ": 0.30, "carry": 0.20, "value": 0.15, "xsmom": 0.05},
    # price trend: 'sign' = mean of sign(n-month excess return); 'cont' = mean of clip(z_n, -cap, cap) / cap, where
    # z_n = n-month excess return / (annual vol x sqrt(n / 12)); 'spot' = use spot moves (no carry) for the signal
    "trend": {"kind": "sign", "horizons": (1, 3, 12), "cap": 2.0, "spot": False},
    # market volatility used to size positions: 'm36' = 36-month std of monthly returns; 'hybrid' = blend of a fast
    # estimate (daily EWMA where free daily data exist, else monthly EWMA) and a 10-year estimate, with a floor
    "vol": {"model": "m36", "hl_days": 35, "hl_months": 6, "fast_w": 0.7, "floor": 0.75},
    # weights inside an asset class: 'equal' or 'cluster' (1 / sum of positive correlations, 60 months, so a tight
    # cluster such as the US curve shares one weight)
    "within_class": "equal",
    "block_vol_months": 36,          # each family-class block scaled to unit ex-ante vol over this window
    "book_vol": 0.10,                # whole-book volatility target
    "gross_cap": 5.0,                # notional cap
    "market_risk_cap": 0.10,         # per-market risk cap (x 3 x book vol / market vol)
    "scenario_limit": None,          # e.g. 0.03: today's positions may lose at most 3% in any past stress window
    "delay_months": 0,               # trade-timing diagnostic: apply positions k months late
    "econ_themes": ("inflation", "trade", "monetary", "risk"),
}

# gm-2.0 candidate (2026-11-01), chosen by a fixed rule on the design periods: a component is adopted only if it
# raises the net Sharpe ratio in BOTH 1990-2010 and 1975-89 (trial log gm/trials.csv):
#   adopted : hybrid volatility (+0.10 / +0.13); expert family shares trend 45 / carry 25 / value 15 / econ 15
#             (+0.08 / +0.16; Winton 75/25 trend/other and distrust of macro data, Man AHL carry strongest, AQR keeps
#             economic trend, our marginal-alpha test: every family adds, econ t 2.8 at 15%)
#   rejected: continuous trend signal (-0.05 / -0.17), cluster weights (0 / +0.01), spot-only trend (-0.09 / -0.01),
#             slower trend 6/12 or 12 (-0.20 / -0.19; also worse at every trade delay), scenario limit (lower Sharpe;
#             drawdown per unit of risk only slightly better; kept as a diagnostic)
#   execution: trade on the first trading day after month end (the 1/3/12 trend loses ~0.05-0.1 Sharpe per day late)
CANDIDATE = None   # set below


def variant(cfg, **changes):
    out = copy.deepcopy(cfg)
    for k, v in changes.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k].update(v)
        else:
            out[k] = v
    return out


def cfg_hash(cfg):
    return hashlib.sha1(json.dumps(cfg, sort_keys=True, default=list).encode()).hexdigest()[:10]


CANDIDATE = variant(BASE, name="gm-2.0.1-candidate",
                    family_w={"trend": 0.45, "econ": 0.15, "carry": 0.25, "value": 0.15, "xsmom": 0.0},
                    vol={"model": "hybrid"})

# stress windows used by the scenario limit (only windows that ENDED before the decision month are used)
STRESS_WINDOWS = {
    "1987 crash": ("1987-10", "1987-11"), "1990 oil spike": ("1990-08", "1990-10"),
    "1994 bond rout": ("1994-02", "1994-11"), "1998 LTCM": ("1998-08", "1998-10"),
    "2007 quant / credit": ("2007-07", "2007-08"), "2008 Lehman": ("2008-09", "2008-12"),
    "2013 taper": ("2013-05", "2013-06"), "2018 Feb vol shock": ("2018-02", "2018-02"),
    "2020 Covid": ("2020-02", "2020-03"), "2022 rates shock": ("2022-01", "2022-10"),
    "2024 Aug yen carry": ("2024-07", "2024-08"), "2025 Apr tariffs": ("2025-03", "2025-04"),
}

# C4 (gm-1.2.1, registered 2026-11-11): fixed preference order between Bloomberg commodity excess-return indexes,
# decided by the index family in the ticker name only (no data needed): S&P GSCI ("SPGS...") first, then Bloomberg
# Commodity ("BCOM..."), the order of gm/bloomberg.py COMMOD_ER and of its docstring "GSCI, else BCOM".
BBG_ER_PREFERENCE = ("SPGS", "BCOM")
