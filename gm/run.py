"""Global Macro Book: monthly paper run (workflow .github/workflows/gm.yml).

python -m gm.run [OUT_DIR]
 1. build the panel, the signals and the book (gm.panel, gm.signals, gm.book);
 2. take positions at the last COMPLETE month end;
 3. write OUT_DIR/status.md (design-period record, current positions, family breakdown, placeholders) and
    OUT_DIR/positions.csv; append new months to OUT_DIR/ledger.csv (append-only paper record, branch gm-record).
The 2011-2026 holdout statistics are never printed; they are run once, after the rules are frozen.
"""
import io
import os
import pickle
import sys
from contextlib import redirect_stdout

import numpy as np
import pandas as pd

from . import book as B
from . import panel as P
from . import signals as G

VERSION = "gm-1.2.0"
NAMES = {"eq_": "equity", "bd_": "bond", "st_": "2-5y note", "fx_": "currency vs USD", "cm_": "commodity"}


def build_all():
    R, SRC, FLAG, rf = P.build()
    os.makedirs(P.OUT, exist_ok=True)
    pickle.dump({"grid": P.GRID, "R": R, "SRC": SRC, "FLAG": FLAG, "rf": rf}, open(os.path.join(P.OUT, "panel.pkl"), "wb"))
    buf = io.StringIO()
    with redirect_stdout(buf):
        G.main()
    return R, SRC, FLAG, buf.getvalue()


def main(out_dir="gm_out"):
    os.makedirs(out_dir, exist_ok=True)
    R, SRC, FLAG, sig_txt = build_all()
    res, x2 = B.run(R), B.run(R, cost_mult=2.0)
    as_of = pd.Period(pd.Timestamp.today(), "M") - 1
    pos = res["pos"].loc[as_of]
    vol = (R.rolling(36, min_periods=12).std() * np.sqrt(12)).loc[as_of]
    fam = pd.DataFrame({f: v.loc[as_of] for f, v in res["fam_pos"].items()})
    tab = pd.DataFrame({"position": pos, "vol": vol, "risk": pos * vol}).join(fam.mul(vol, axis=0).add_prefix("risk_"))
    tab = tab[tab["position"].abs() > 1e-6].sort_values("risk")
    tab.round(5).to_csv(os.path.join(out_dir, "positions.csv"), index_label="market")

    led_p = os.path.join(out_dir, "ledger.csv")
    led = pd.read_csv(led_p) if os.path.exists(led_p) else pd.DataFrame(columns=["as_of", "market", "position", "risk",
                                                                                  "version"])
    prev = led[led["as_of"].astype(str) == str(as_of)]
    restate = len(prev) and prev["market"].nunique() < len(tab)       # earlier run for this month had missing data
    if not len(prev) or restate:
        # append-only: a restatement adds rows (version tagged '-restated'); the earlier rows stay as they were
        new = pd.DataFrame({"as_of": str(as_of), "market": tab.index, "position": tab["position"].round(5).values,
                            "risk": tab["risk"].round(5).values, "version": VERSION + ("-restated" if restate else "")})
        led = pd.concat([led, new], ignore_index=True)
        led.to_csv(led_p, index=False)

    spx = R["eq_us_spx"]
    L = ["# Global Macro Book (paper) - %s" % VERSION,
         "", "Positions decided at the end of **%s**; built %s UTC. Paper research only, not investment advice." % (
             as_of, pd.Timestamp.utcnow().strftime("%Y-%m-%d %H:%M")),
         "", "## Backtest record (design and extra-check periods only; holdout 2011-2026 not run yet)", "```"]
    for a, b in (("1975-01", "1989-12"), ("1990-01", "2010-12")):
        L.append("%s..%s gross      %s" % (a[:4], b[:4], B.stats(res["gross"].loc[a:b], spx)))
        L.append("%s..%s net        %s" % (a[:4], b[:4], B.stats(res["net"].loc[a:b], spx)))
        L.append("%s..%s net 2xcost %s" % (a[:4], b[:4], B.stats(x2["net"].loc[a:b])))
    L += ["```", "", "## Current positions (risk = notional x annual vol; book targets 10%% vol; %d markets)" % len(tab),
          "", "| Market | Notional | Risk | Trend | Econ | Carry | Value | XS mom |", "|---|---|---|---|---|---|---|---|"]
    for k, r in tab.reindex(tab["risk"].abs().sort_values(ascending=False).index).iterrows():
        L.append("| %s | %+.2f | %+.2f%% | %+.2f%% | %+.2f%% | %+.2f%% | %+.2f%% | %+.2f%% |" % (
            k, r["position"], r["risk"] * 100, r.get("risk_trend", 0) * 100, r.get("risk_econ", 0) * 100,
            r.get("risk_carry", 0) * 100, r.get("risk_value", 0) * 100, r.get("risk_xsmom", 0) * 100))
    cls = {c: (pos[[k for k in pos.index if k.startswith(pre)]].abs().sum(),
               (pos * vol)[[k for k in pos.index if k.startswith(pre)]].sum()) for c, pre in G.CLASSES.items()}
    L += ["", "Gross notional and net risk by class: " + ", ".join("%s %.2fx / %+.1f%%" % (c, g, r * 100)
                                                                  for c, (g, r) in cls.items()),
          "", "## Family risk shares (fixed)", ", ".join("%s %d%%" % (f, w * 100) for f, w in B.FAMILY_W.items()),
          "", "## Placeholders (not yet in this version)"] + ["- " + p for p in B.PLACEHOLDERS]
    L += ["", "## Data flags", ""] + ["- %s: %s" % (k, "; ".join(v)) for k, v in FLAG.items() if v]
    L += ["", "## Signal families alone (design period)", "```", sig_txt.strip(), "```"]
    open(os.path.join(out_dir, "status.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L[:12]))
    print("positions as of %s: %d markets; ledger rows %d" % (as_of, len(tab), len(led)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "gm_out")
