"""Markdown tables for POWER_3.3.md from the CSVs written by power_3_3.py (no simulation here)."""
import os

import numpy as np
import pandas as pd

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "docs", "research", "power")
RAW = os.path.join(OUT, "csv")


def md(df, fmt="%.2f"):
    cols = list(df.columns)
    L = ["| " + " | ".join(str(c) for c in cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if isinstance(v, (float, np.floating)):
                cells.append("" if np.isnan(v) else fmt % v)
            else:
                cells.append(str(v))
        L.append("| " + " | ".join(cells) + " |")
    return "\n".join(L)


def main():
    out = []
    c = pd.read_csv(os.path.join(RAW, "cells.csv"))
    order = ["no skill (gross 0)", "standalone S=0.0", "standalone S=0.2", "standalone S=0.4", "null alpha=0",
             "IR=0.2", "IR=0.4"]
    c["lab_i"] = c["label"].map({k: i for i, k in enumerate(order)})
    keep = ["shape", "label", "S", "true_IR", "true_dSR_held", "T1_alpha_025", "T1_dsr_05", "T2_alpha2x", "T3_pl05",
            "T4_tail", "ERA", "WF_025", "WF_05", "WF_025_era", "WF_dsr_025", "TP_05", "INCUB"]
    for SRb in (1.23, 0.5):
        for rho in (0.0, 0.3, 0.6):
            d = c[(c.SRb == SRb) & (c.rho == rho)].sort_values(["shape", "lab_i"])
            if len(d) == 0:
                continue
            out.append("\n### Cells: book SR %.2f, rho %.1f\n" % (SRb, rho))
            out.append(md(d[keep]))
    s = pd.read_csv(os.path.join(RAW, "special.csv"))
    for blk in s.block.unique():
        d = s[s.block == blk].dropna(axis=1, how="all")
        out.append("\n### Special: %s\n" % blk)
        out.append(md(d))
    b = pd.read_csv(os.path.join(RAW, "batch.csv"))
    out.append("\n### Batches\n")
    out.append(md(b))
    for f in ("hygiene", "holdout", "robust", "calibration"):
        p = os.path.join(RAW, f + ".csv")
        if os.path.exists(p):
            out.append("\n### %s\n" % f)
            out.append(md(pd.read_csv(p).dropna(axis=1, how="all"), fmt="%.3f"))
    open(os.path.join(HERE_OUT, "tables_all.md"), "w").write("\n".join(out) + "\n")
    print("written", os.path.join(HERE_OUT, "tables_all.md"))


HERE_OUT = os.path.join(OUT, "work")
if __name__ == "__main__":
    main()
