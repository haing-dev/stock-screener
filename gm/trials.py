"""Trial runner and log. Every design-period variant goes through `trial(name, cfg)`: it runs the book, scores the
design periods only (gm/stats.py never reads the holdout), and appends one row to gm/trials.csv with the config
hash, so the deflated Sharpe can count every trial and any result can be rebuilt from its config.

python -m gm.trials            # prints the log and the deflated Sharpe of the best and of the candidate
"""
import datetime as dt
import json
import os
import pickle

import pandas as pd

from . import book as B
from . import config as CF
from . import panel as P
from . import stats as ST

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trials.csv")
COLS = ["when", "trial", "family", "hash", "sr_9010", "t_9010", "maxdd_9010", "sr_7589", "turnover", "note", "config"]


def _R():
    return pickle.load(open(os.path.join(P.OUT, "panel.pkl"), "rb"))["R"]


def log_row(row):
    df = pd.read_csv(LOG) if os.path.exists(LOG) else pd.DataFrame(columns=COLS)
    df = pd.concat([df, pd.DataFrame([row])[COLS]], ignore_index=True)
    df.to_csv(LOG, index=False)


def trial(name, cfg, family="book", note="", R=None, daily=None, log=True):
    R = _R() if R is None else R
    res = B.run(R, cfg=cfg, daily=daily)
    d, e = ST.summary(res["net"]), ST.summary(res["net"], *ST.EXTRA)
    row = {"when": dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M"), "trial": name, "family": family,
           "hash": CF.cfg_hash(cfg), "sr_9010": round(d["sr"], 3), "t_9010": round(d["t"], 2),
           "maxdd_9010": round(d["maxdd"], 3), "sr_7589": round(e["sr"], 3),
           "turnover": round(float(ST.cut(res["turnover"], *ST.DESIGN).mean() * 12), 1), "note": note,
           "config": json.dumps(cfg, sort_keys=True, default=list)}
    if log:
        log_row(row)
    return res, row


SEED = [  # book-level trials run before this log existed (gm/CHANGES.md), design 1990-2010 net SR
    ("v1.0", 1.50), ("v1.1", 1.55), ("v1.2", 1.47), ("ablate-trend", 1.25), ("ablate-econ", 1.57),
    ("ablate-carry", 1.27), ("ablate-value", 1.46), ("ablate-xsmom", 1.49), ("trend-3/6/12", 1.35),
    ("trend-6/12", 1.28), ("trend-12", 1.27), ("growth-pit", 1.47), ("scaler-credit", 1.48), ("scaler-corr", 1.45),
    ("scaler-ddbrake", 1.45)]


def seed():
    if os.path.exists(LOG):
        return
    for name, sr in SEED:
        log_row({"when": "2026-10-31", "trial": name, "family": "book", "hash": "", "sr_9010": sr, "t_9010": "",
                 "maxdd_9010": "", "sr_7589": "", "turnover": "", "note": "pre-log (CHANGES.md)", "config": ""})


def all_book_srs():
    df = pd.read_csv(LOG)
    return pd.to_numeric(df[df["family"] == "book"]["sr_9010"], errors="coerce").dropna().tolist()


def main():
    df = pd.read_csv(LOG)
    print(df[["trial", "family", "sr_9010", "t_9010", "maxdd_9010", "sr_7589", "turnover", "note"]].to_string())
    srs = all_book_srs()
    print("book-level trials:", len(srs))


if __name__ == "__main__":
    main()
