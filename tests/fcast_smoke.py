"""Smoke test for tools/fcast/score.py (forecast ledger scorer, SCORING_RULES v1) on hand-built forecasts and synthetic
series. No real data are read. Prints FCAST SMOKE OK."""
import math, os, sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "fcast"))
import score as S  # noqa: E402


def daily(rate, start="1985-01-01", end="2022-12-30", base=100.0):
    idx = pd.bdate_range(start, end)
    yrs = (idx - idx[0]).days / 365.25
    return S.Series(pd.Series(base * (1 + rate) ** yrs, index=idx), "D", "synthetic")


def monthly(rate, start="1980-01-31", end="2022-11-30", base=100.0):
    idx = pd.date_range(start, end, freq="ME")
    return S.Series(pd.Series(base * (1 + rate) ** (np.arange(len(idx)) / 12.0), index=idx), "M", "synthetic")


class Synth(S.Data):
    def __init__(self, series):
        self.cache, self._weo, self.raw, self.rd = dict(series), None, "", ""

    def get(self, name):
        if name.startswith("inv:"):
            b = self.cache.get(name[4:])
            return None if b is None else S.Series(1.0 / b.s, b.freq, name)
        return self.cache.get(name)


rec = pd.Series(0.0, index=pd.date_range("1985-01-31", "2023-06-30", freq="ME"))
rec[(rec.index >= "1990-08-01") & (rec.index <= "1991-03-31")] = 1
rec[(rec.index >= "2001-04-01") & (rec.index <= "2001-11-30")] = 1
rec[(rec.index >= "2008-01-01") & (rec.index <= "2009-06-30")] = 1
rec[(rec.index >= "2021-03-01") & (rec.index <= "2021-05-31")] = 1
D = Synth({"r/D__GSPC": daily(0.10), "r/D__N225": daily(0.03), "r/D_SPY": daily(0.10), "r/D_EWJ": daily(0.03),
           "r/CPIAUCNS": monthly(0.03), "USREC": S.Series(rec, "M", "USREC")})

ok = []


def row(fid, **kw):
    r = dict(forecast_id=fid, view_id=fid, row="1", source_id="SRC", who="Tester", made_date="2020-01-03",
             date_precision="day", kind="forecast", variable_code="US_EQ", variable_text="US stocks", direction="up",
             level="", horizon_months="12", horizon_text="", condition="", probability="", confidence="unstated",
             call_type="direction", resolvable="yes", why_not="", claim_ids="", note="")
    r.update(kw)
    return r


def check(name, cond):
    ok.append(cond)
    print(("PASS " if cond else "FAIL ") + name)


rows = [row("t_dates"), row("t_month", who="TM", made_date="2020-01", date_precision="month"),
        row("t_band_up", variable_code="JP_EQ", variable_text="Japan"),
        row("t_band_flat", variable_code="JP_EQ", variable_text="Japan", direction="flat", who="T2"),
        row("t_band_h3", variable_code="JP_EQ", variable_text="Japan", horizon_months="3", who="T3", direction="down"),
        row("t_def_vol", call_type="volatility", resolvable="partly", horizon_months="", direction="higher_vol",
            who="T4", why_not="no_horizon"),
        row("t_def_macro", call_type="macro", resolvable="partly", horizon_months="", who="T5", why_not="no_horizon",
            variable_code="US_INFLATION", variable_text="inflation", direction="flat", made_date="2020-03-10"),
        row("t_struct", call_type="structural", resolvable="partly", horizon_months="", who="T6", why_not="no_horizon"),
        row("t_dup1", who="D", made_date="2019-05-01"), row("t_dup2", who="D", made_date="2019-05-11"),
        row("t_dup3", who="D", made_date="2019-06-15"),
        row("t_open", who="O", made_date="2022-06-01"),
        row("t_maxh", who="M", horizon_months="72"),
        row("t_year", who="Y", made_date="2020", date_precision="year"),
        row("t_lev_hit", who="L1", level="above 3,000"), row("t_lev_miss", who="L2", level="above 3,500"),
        row("t_lev_guard", who="L3", level="50,000"),
        row("t_lev_move", who="L4", level="+15%"),
        row("t_rel", who="R", variable_code="US_EQ>JP_EQ", variable_text="US over Japan", direction="outperform",
            call_type="relative"),
        row("t_rec", who="E", variable_code="US_RECESSION", variable_text="recession", direction="event_yes",
            call_type="event", made_date="2020-06-15"),
        row("t_rec_no", who="E2", variable_code="US_RECESSION", variable_text="recession", direction="event_no",
            call_type="event", made_date="2022-03-15"),
        row("t_cond", kind="conditional", resolvable="no", why_not="conditional_unmet_unknown", who="C"),
        row("t_nf", kind="not_forecast", resolvable="no", why_not="no_direction", who="N"),
        row("t_prob", who="P", probability="0.8")]
out = {x["forecast_id"]: x for x in S.run(rows, D)}
g = lambda k: out[k]
for k, v in out.items():
    if v.get("status") not in ("resolved",):
        print("   (row %s: %s %s)" % (k, v.get("status"), v.get("reason")))

# start / end dates
check("day precision: start = first trading day after made date", g("t_dates")["start_date"] == "2020-01-06")
check("end = made + 12 months, last obs on or before", g("t_dates")["end_date"] == "2021-01-01")
check("month precision -> month end -> next trading day", g("t_month")["made_r"] == "2020-01-31"
      and g("t_month")["start_date"] == "2020-02-03")
# dead bands
check("12m band equity 4%", abs(g("t_band_up")["band"] - 0.04) < 1e-12)
check("+3% move inside 4% band: up call misses, sign-only hit", g("t_band_up")["hit"] is False
      and g("t_band_up")["sign_hit"] is True and g("t_band_up")["category"] == "flat")
check("flat call hits inside band", g("t_band_flat")["hit"] is True)
check("3m band = 4% x sqrt(3/12) = 2%", abs(g("t_band_h3")["band"] - 0.02) < 1e-12)
# default horizons and pools
check("default horizon volatility 6", g("t_def_vol")["h"] == 6.0 and g("t_def_vol")["h_source"] == "default"
      and g("t_def_vol")["pool"] == "B")
check("default horizon macro 12", g("t_def_macro")["h"] == 12.0)
check("structural pool E, 36 months", g("t_struct")["pool"] == "E" and g("t_struct")["h"] == 36.0)
check("conditional pool D (condition unknown)", g("t_cond")["pool"] == "D")
check("not_forecast not pooled", g("t_nf")["status"] == "not pooled")
# macro rule: start reading published before made date (lag 15), end reading <= end date
m = g("t_def_macro")
check("macro start reading Jan 2020, end Feb 2021", m.get("start_date") == "2020-01-31" and m.get("end_date") == "2021-02-28")
check("constant 3% inflation: flat call hits, base rate 1", m.get("hit") is True and m.get("base_p") == 1.0)
# duplicates
check("duplicate within 30 days", g("t_dup2")["status"] == "duplicate" and g("t_dup2")["duplicate_of"] == "t_dup1")
check("45 days later kept", g("t_dup3")["status"] == "resolved")
# open, max horizon, year precision
check("open row: end after data end, resolve date = end date", g("t_open")["status"] == "open"
      and g("t_open")["resolve_date"] == "2023-06-01")
check("horizon > 60 excluded", g("t_maxh")["status"] == "excluded")
check("year precision excluded", g("t_year")["status"] == "excluded")
# levels
check("threshold above 3,000 hit", g("t_lev_hit")["hit"] is True and "threshold" in g("t_lev_hit")["level_use"])
check("threshold above 3,500 miss", g("t_lev_miss")["hit"] is False)
check("unit-mismatch level ignored", "unit mismatch" in g("t_lev_guard")["level_use"])
check("move size +15% replaces band (10% move misses)", g("t_lev_move")["hit"] is False)
# baselines
check("base rate of up on a steady 10% series = 1", g("t_dates")["base_p"] == 1.0)
check("trend continuation = up, trend hit", g("t_dates")["trend_cat"] == "up" and g("t_dates")["trend_hit"] is True)
check("relative: 10% vs 3% outperform hit", g("t_rel")["hit"] is True and abs(g("t_rel")["change"] - 0.07) < 0.005)
check("recession event_yes resolves on first sign", g("t_rec")["status"] == "resolved" and g("t_rec")["hit"] is True
      and g("t_rec")["resolve_date"] == "2021-03-31")
bp = g("t_rec")["base_p"]
check("recession base rate in (0,1)", isinstance(bp, float) and 0 < bp < 1)
check("event_no waits 12 months after end (open)", g("t_rec_no")["status"] == "open")
check("probability carried for Brier", g("t_prob").get("probability") == 0.8)
# parse_level units
pl = S.parse_level
check("parse range 1.10 to 1.14", pl("1.10 to 1.14", "fx") == dict(kind="range", lo=1.10, hi=1.14))
check("parse signed bp move range", pl("-125 to -150bp", "policy") == dict(kind="moverange", lo=-1.5, hi=-1.25))
check("parse % on yields is a level", pl("about 4.25%", "yield") == dict(kind="threshold", T=4.25, side=None))
check("year after a month word dropped", pl("high in December 2027", "eq") is None)
# bootstrap helper used by the scorecard
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "fcast"))
import scorecard as SC  # noqa: E402
months = [str(pd.Period("2018-01", "M") + i) for i in range(40)]
lo, hi = SC.boot_ci(months, [1.0] * 40)
check("bootstrap of a constant = constant", abs(lo - 1) < 1e-12 and abs(hi - 1) < 1e-12)
lo2, _ = SC.boot_ci(["2020-%02d" % (i % 12 + 1) for i in range(40)], list(range(40)))
check("no interval when the cell spans <= 12 months", lo2 != lo2)

print("FCAST SMOKE OK" if all(ok) else "FCAST SMOKE FAILED (%d of %d)" % (ok.count(False), len(ok)))
sys.exit(0 if all(ok) else 1)
