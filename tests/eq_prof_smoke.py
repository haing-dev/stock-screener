"""Smoke test for tools/equity/wrds/eq_prof.py on an invented conviction panel (no WRDS data).
Investor 1 (filer 13408): 10 equal positions, each held 8 quarters, then all replaced -> effective names 10,
top-5 weight 50%, median holding 8 quarters, 50% new per year. Investor 2 (filer 8350): 4 positions never sold ->
median holding not reached. python3 tests/eq_prof_smoke.py"""
import io
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools", "equity", "wrds"))
import eq_prof  # noqa: E402

qs = [y * 100 + m for y in range(2010, 2018) for m in (3, 6, 9, 12)]          # 32 quarters
rows = []
for k, q in enumerate(qs):
    block = k // 8
    for j in range(10):
        rows.append((13408, q, 1000 * (block + 1) + j, 0.1, j + 1, k % 8 == 0 and k > 0, False, False, False, k % 8 + 1))
    for j in range(4):
        rows.append((8350, q, 5000 + j, 0.25, j + 1, False, k == 5 and j == 0, False, False, k + 1))
store = {"eq_conv_panel": pd.DataFrame(rows, columns=["mgrno", "yyyymm", "permno", "w", "rank", "new", "add", "conv_a", "conv_b", "q_held"])}
saved, lines = {}, []


def load(n):
    buf = io.StringIO()
    store[n].to_csv(buf, index=False)
    buf.seek(0)
    return pd.read_csv(buf)


def save(n, df):
    saved[n] = df


def out(*a):
    lines.append(" ".join(str(x) for x in a))
    print(*a)


eq_prof.run(load, save, out)
T = saved["eq_prof_table"].set_index("name")
a = T.loc["Terry Smith"]
assert abs(a.eff_names - 10) < 1e-9 and abs(a.top5 - 0.5) < 1e-9 and a.names == 10, a
assert a.hold_med == 8, a.hold_med                       # blocks 2 and 3 are complete 8-quarter spells; block 4 still open
assert abs(a.new_per_year - 4 * 3 / 31) < 1e-9, a.new_per_year      # three full replacements over 31 quarters after the first
b = T.loc["Warren Buffett"]
assert b.spells == 0 and b.hold_med == -1, b              # positions held from the first filing: entry not observed
assert abs(b.add_share - 1.0) < 1e-9
print("\nSMOKE OK")
