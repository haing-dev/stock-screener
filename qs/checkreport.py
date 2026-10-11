"""What couldn't be verified: every note on a pass with an asterisk or a CHECK, grouped by reason, per screen (markdown)."""
import re
from collections import Counter, defaultdict

from .portal import evaluate_state
from .screens import BY_ID, SCREENS


def _norm(note):
    """Collapse numbers, dates, tickers and money so the same reason groups together."""
    s = re.sub(r"\d{4}-\d{2}-\d{2}", "<date>", note)
    s = re.sub(r"\$[\d,.]+[MBK]?", "$<x>", s)
    s = re.sub(r"[-+]?\d[\d,.]*%?x?", "<n>", s)
    return s[:180]


def build(state, cfg, examples=6):
    res = evaluate_state(state, cfg)
    ctxs = state["ctxs"]
    out = [f"# Check-manually report (screened {state.get('screened_on')}, priced {state.get('priced_on')})", ""]
    total = Counter()
    for s in SCREENS:
        rr = res.get(s.sid) or {}
        cls = Counter(r["class"] for r in rr.values())
        out.append(f"## {s.title}: " + ", ".join(f"{k} {cls.get(k, 0)}" for k in
                                                    ("PASS", "CHECK", "NEAR", "PRICE", "ONE", "FAIL")))
        reasons = defaultdict(list)
        for c, r in rr.items():
            if r["class"] != "CHECK" and not r.get("star"):
                continue
            for n in r.get("check_notes") or []:
                key = _norm(n)
                reasons[key].append(ctxs[c]["ticker"])
                total[key.split(":")[0] if ":" in key else key] += 1
        for key, ts in sorted(reasons.items(), key=lambda kv: -len(kv[1]))[:25]:
            out.append(f"- **{len(ts)}** × {key}  (e.g. {', '.join(sorted(ts)[:examples])})")
        out.append("")
    # companies that couldn't be screened at all, grouped by blocker
    from .portal import blocker
    gaps = defaultdict(list)
    for c, rec in (state.get("records") or {}).items():
        st = rec.get("stage") or ""
        if st == "screened" or (st.startswith("not screened: ") and "check by hand" not in st):
            continue
        if c in ctxs and not ctxs[c].get("events_only"):
            continue
        gaps[blocker(st)[0]].append(rec.get("ticker") or str(c))
    out.append(f"## Couldn't screen: {sum(len(v) for v in gaps.values())} companies")
    for b, ts in sorted(gaps.items(), key=lambda kv: -len(kv[1])):
        out.append(f"- **{len(ts)}** × {b}: {', '.join(sorted(ts))}")
    out.append("")
    return "\n".join(out)
