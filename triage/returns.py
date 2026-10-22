"""Monthly returns for the panel companies and the index ETFs: open of each month's entry day (first trading day
after the month-end) to the next month's, unadjusted prices plus splits and cash dividends (qs/backtest.run_returns;
a company that left the exchange is valued at its last daily close, else -30%).

Output: cache/tri/returns/<ym>.json.gz {cik: [return, how]}, cache/tri/returns/index.json.gz {ym: {SPY: r, IWM: r}}
"""
import os

from qs.backtest import run_returns
from qs.backtest_support import read_json, write_json
from qs.btprices import holding_return

from . import panel as PN
from . import paths as P

INDEX = ("SPY", "IWM")


def build(grid, btp, splits, divs, log=print, budget=300, priority=None):
    P.ensure(P.RETURNS)

    def companies(ym):
        p = PN.load(ym)
        return (p or {}).get("companies")
    spent = run_returns(grid, btp, splits, divs, log=log, last_close_budget=budget, priority=priority,
                        ret_dir=P.RETURNS, companies=companies)
    path = os.path.join(P.RETURNS, "index.json.gz")
    idx = read_json(path) or {}
    for g, nx in zip(grid, grid[1:]):
        if g["ym"] in idx:
            continue
        row = {}
        for s in INDEX:
            b0, b1 = (g.get("bars_e") or {}).get(s), (nx.get("bars_e") or {}).get(s)
            if b0 and b1 and b0[0] and b1[0]:
                row[s] = round(holding_return(b0[0], b1[0], splits.get(s) or [], divs.get(s) or [], g["e"], nx["e"]), 6)
        if row:
            idx[g["ym"]] = row
    write_json(path, idx)
    log(f"Returns: {len(idx)} index months; {spent} last-close lookups")
    return spent
