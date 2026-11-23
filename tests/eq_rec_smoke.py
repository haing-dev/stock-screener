"""Smoke test for tools/equity/wrds/eq_rec.py on invented data. python3 tests/eq_rec_smoke.py"""
import io, os, sys
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools", "equity", "wrds"))
import eq_rec  # noqa: E402

rng = np.random.default_rng(3)
ids = [int(m) for r in eq_rec.INV for m in r.get("mgrnos", [])] + [990001, 990002, 990003]
peers = list(range(500000, 500300))
store = {"eq_rec_names": pd.DataFrame({"mgrno": [990001, 990002, 990003] + peers,
                                       "mgrname": ["PECONIC PARTNERS LLC", "MANGROVE PARTNERS", "HUSSMAN ECONOMETRICS"] + ["P%d" % p for p in peers],
                                       "rdate2": "2025-12-31"})}
months = [y * 100 + m for y in range(2010, 2026) for m in range(1, 13) if y * 100 + m >= 201012]
store["eq_rec_spy"] = pd.DataFrame({"yyyymm": months, "mthret": 0.01})
fn = sorted({f for r in eq_rec.INV for f in r.get("fundnos", [])})
store["eq_rec_fund"] = pd.DataFrame([(f, pd.Timestamp(year=m // 100, month=m % 100, day=28), 100.0, 0.012) for f in fn for m in months],
                                    columns=["crsp_fundno", "caldt", "mtna", "mret"])
skill = {i: rng.normal(0, 0.01) for i in ids + peers}
skill[21801] = 0.03          # planted winner
skill[23050] = -0.02         # planted loser
for d in eq_rec.QW:
    rows = []
    for i in ids + peers:
        if i == 7142 and d < "2020-03-31":
            continue            # young fund
        rows.append((i, 20, 5e8, 20, 5e8, 0.0303 + skill[i] + rng.normal(0, 0.01), 1.0, 0.0303 + skill[i]))
    store["eq_rec_q_%s" % d[:7].replace("-", "")] = pd.DataFrame(rows, columns=["mgrno", "nall", "vall", "ncrsp", "vcrsp", "mw", "cov", "mw20"])


def load(n):
    b = io.StringIO(); store[n].to_csv(b, index=False); b.seek(0); return pd.read_csv(b)


lines = []
eq_rec.report(load, lambda *a: (lines.append(" ".join(map(str, a))), print(*a)))
txt = "\n".join(lines)
assert "Cliff Sosin | candidate" in txt and [l for l in lines if l.startswith("Cliff Sosin")][0].endswith("PASS")
assert [l for l in lines if l.startswith("Fred Martin")][0].endswith("FAIL")
assert "short record" in [l for l in lines if l.startswith("Val Zlatev")][0]
assert "William Harnisch | candidate | 13F 990001" in txt
print("\nSMOKE OK")

lines.clear()
eq_rec.scan(load, lambda *a: (lines.append(" ".join(map(str, a))), print(*a)))
assert any(l.startswith("21801 |") for l in lines), "planted winner not listed"
print("\nSCAN SMOKE OK")
