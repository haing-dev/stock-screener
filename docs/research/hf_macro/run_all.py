import lab
lab.COST = 0.002
import importlib, pandas as pd, harness
rows = []
for m in ["hyp_b12", "hyp_b34", "hyp_b56", "hyp_b7"]:
    mod = importlib.import_module(m)
    for h in mod.HYP:
        rows.append(harness.evaluate(h))
    print(m, len(mod.HYP), flush=True)
df = pd.DataFrame(rows)
df.to_csv("all_results.csv", index=False)
print("done", len(df), "errors", (df.error != "").sum())
