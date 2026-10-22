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


def fix_haircuts(grid, btp, splits, divs, budget=100, log=print):
    """Companies that left the exchange during a period got -30% when their last close wasn't looked up within the
    run's request budget. Each run looks up more of them (one Massive request each, cached) and replaces the -30% with
    the real exit at the last close; event companies first. Returns (fixed, left)."""
    nxt = {g["ym"]: n["e"] for g, n in zip(grid, grid[1:])}
    e_of = {g["ym"]: g["e"] for g in grid}
    opens = {}
    todo = []
    for ym in sorted(nxt):
        r = read_json(os.path.join(P.RETURNS, f"{ym}.json.gz")) or {}
        for c, (v, how) in r.items():
            if how == "haircut":
                todo.append((ym, c))
    if not todo:
        return 0, 0
    pri = set()
    try:
        for kd in (read_json(os.path.join(P.OUT, "site.json.gz")) or {}).get("kinds", {}).values():
            pri.update(str(x["cik"]) for x in kd["items"])
    except Exception:  # noqa: BLE001 - order only
        pass
    todo.sort(key=lambda t: (t[1] not in pri, t[0]))
    fixed, spent, changed = 0, 0, {}
    for ym, c in todo:
        if spent >= budget:
            break
        rec = ((PN.load(ym) or {}).get("companies") or {}).get(c) or {}
        sym = rec.get("sym")
        g = next((x for x in grid if x["ym"] == ym), None)
        if not sym or not g:
            continue
        if ym not in opens:
            opens[ym] = g.get("bars_e") or {}
        b0 = opens[ym].get(sym)
        if not b0 or not b0[0]:
            continue
        lc = btp.last_close(sym, e_of[ym], nxt[ym])
        spent += 1
        if not lc:
            continue
        r = holding_return(b0[0], lc[1], splits.get(sym) or [], divs.get(sym) or [], e_of[ym], lc[0])
        if r is None:
            continue
        changed.setdefault(ym, {})[c] = [round(r, 6), "last close"]
        fixed += 1
    for ym, upd in changed.items():
        path = os.path.join(P.RETURNS, f"{ym}.json.gz")
        cur = read_json(path) or {}
        cur.update(upd)
        write_json(path, cur)
    left = len(todo) - fixed
    log(f"Exits: {fixed} replaced with the last close ({spent} lookups); {left} still at -30%")
    return fixed, left
