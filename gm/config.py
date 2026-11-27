"""Global Macro Book: every rule in one place.

A config is a plain dict. `book.run(R, cfg=...)` reads only these keys, so a variant is a changed copy of a config
(`variant(BASE, trend={"kind": "cont"})`) and every trial is reproducible from its config (gm/trials.py logs it).

BASE = gm-1.2.3 (the live paper book; gm-1.2.0 with the registered input-layer look-ahead fixes C1-C4, gm/CHANGES.md
2026-11-11, without the doubled US 2-year market, 2026-11-22, and with the fix version E1-E5, 2026-11-24).
CANDIDATE = the gm-2.0.3 candidate (gm-2.0 + the same changes), frozen only after the Bloomberg data
and the decisions in docs/research/global_macro/gap_review_crosscheck_2026-10-31.md.
"""
import copy
import hashlib
import json

BASE = {
    "name": "gm-1.2.3",
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


CANDIDATE = variant(BASE, name="gm-2.0.3-candidate",
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

# E1 (gm-1.2.3, registered 2026-11-24, TESTING_PROTOCOL 7.4): Bloomberg switches, OFF by default. Each one is a
# registered flag; switching one on is a registered change (A1 data rule, charter D1 / A3), never a result of which
# tickers happen to load. The panel and the signals are shared by BASE and CANDIDATE, so the flags live here and not in
# the config dicts.
#   value_composite  Value: Bloomberg equity composite (forward E/P, B/P, D/P ranks) instead of the dividend yield
#   curve_carry      Carry: farthest-contract commodity curve carry from Bloomberg generic curves
#   alt_commodities  the alternative commodity columns (gm/bloomberg.py ALT_COMMOD) as markets
#   growth_surprise  Economic trend growth theme from Bloomberg data surprises (signals.GROWTH_SOURCE 'surprise')
BBG_SWITCHES = {"value_composite": False, "curve_carry": False, "alt_commodities": False, "growth_surprise": False}

# E4 (gm-1.2.3, registered 2026-11-24): Value's trailing 12-month dividend yield for the 7 non-US equity markets (Ken
# French country files) is the one ending at t - 12 (design and live alike); 0 = the lag-0 form, reported only.
VALUE_DY_LAG = 12

# E5 (gm-1.2.3, registered 2026-11-24, TESTING_PROTOCOL 7.3 item 5): seal and holding cut. In a design run no input
# dated after this close is used and no holding earns past it (gm/seal.py; gm.book.run seals by default).
SEAL_END = "2010-12-31"

# ---------------------------------------------------------------------------------------------------------------------
# gm-2.1.0 feature version (registered 2026-11-24, gm/CHANGES.md; TESTING_PROTOCOL 7.3, 7.4 E6-E11 and E14, 7.7).
# Nothing here changes BASE or CANDIDATE at k = 0: every new key below is absent from them.
ENGINE_VERSION = "gm-2.2.0"       # gm-2.2.0 (2026-11-27): E13 X1 seasonal adjustment flag; A1 data path (E15)

# E13 (gm-2.2.0, gm/CHANGES.md "X1 outcome", 2026-11-27): X1's gate opened for these energy markets (X1 run
# docs/research/batches/X1_2026-11-27.txt), so their carry is seasonally adjusted in both Carry versions
# (signals.x1_adjust) wherever a config holds the key "x1_seasonal". BASE (live paper book, 7.1 item 6) and CANDIDATE
# (the gm-2.0.3 reference) do not hold it, so neither changes at k = 0. The A1 runs and every later run of the
# programme use A1_INCUMBENT = CANDIDATE + the adjustment (TESTING_PROTOCOL 7.5 X1: "seasonally adjusted (E13)
# before A1").
X1_MARKETS = ("cm_natgas", "cm_gasoline")
A1_INCUMBENT = variant(CANDIDATE, name="gm-2.0.3-candidate-x1", x1_seasonal=X1_MARKETS)

# E7 version grids (approved specs, section 6). Trend versions: (lookback months, shape, volatility model).
TREND_GRID = tuple((h, shape, vm) for shape, vm in (("sign", "hybrid"), ("sign", "m36"), ("graded", "hybrid"),
                                                  ("graded", "m36")) for h in (1, 3, 6, 12))   # v1..v16, SPEC_Trend s6
ECON_GRID = ("tanh", "sign")       # SPEC_Economic_trend s6: v1 f(z) = tanh(z / 2), v2 f(z) = sign(z)
CARRY_GRID = ("dir", "cs")         # SPEC_Carry s6: v1 sign of carry, v2 rank in class
VALUE_GRID = (1, 2)                # SPEC_Value s6: v1 as coded, v2 (bonds 60-month yield change, FX real-rate deviation)
# gm-2.2.0: the A2 challenger is built on A1_INCUMBENT (SPEC_Carry s6: "X1 changes a market's signal in both versions")
A2_CHALLENGER = variant(A1_INCUMBENT, name="gm-2.2.0-a2-challenger",
                        grid={"trend": TREND_GRID, "econ": ECON_GRID, "carry": CARRY_GRID, "value": VALUE_GRID})

# E9 component masks: (pod, class, version); "*" = every class or every version. Versions are numbered as the grids
# (1-based); a config without a grid has one version per pod, except Carry, which is always split into v1 (sign) and
# v2 (rank) for masks. TESTING_PROTOCOL 7.2 item 5 and 7.6 step 6.
CORE_PARTS = {"trend": [("trend", "*", "*")],
              "carry": [("carry", "FX", 2), ("carry", "CM", 1), ("carry", "CM", 2)],
              "value": [("value", "EQ", "*")]}
SHADOW_PARTS = {"econ": [("econ", "*", "*")],
                "carry": [("carry", "FX", 1), ("carry", "FI", "*")],
                "value": [("value", "FI", "*"), ("value", "FX", "*")]}

# E11 spread pods: a 3-month contract counts at 0.25 / 1.9 of its notional in the gross cap (2-year equivalent,
# gm/variants.py us_3m_rate; SPEC_Strip_reversion s5, SPEC_Carry s5). Used through a config's "gross_weights".
STRIP_GROSS_WEIGHT = 0.25 / 1.9

# E10 registered test constants (TESTING_PROTOCOL 7.7)
TEST_SEED = 20261101
ALPHA_BOOT_N, ALPHA_BOOT_BLOCK = 10000, 6
PLACEBO_N, PLACEBO_BLOCK = 1000, 12
LAMBDA_COMBINED = 0.5
HOLM_LEVEL = 0.025
NI_MARGIN = -0.10
