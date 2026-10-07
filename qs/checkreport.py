"""Why companies land on 'Check manually': every CHECK note grouped by reason, per screen (markdown)."""
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
            if r["class"] != "CHECK":
                continue
            for n in r.get("check_notes") or []:
                key = _norm(n)
                reasons[key].append(ctxs[c]["ticker"])
                total[key.split(":")[0] if ":" in key else key] += 1
        for key, ts in sorted(reasons.items(), key=lambda kv: -len(kv[1]))[:25]:
            out.append(f"- **{len(ts)}** × {key}  (e.g. {', '.join(sorted(ts)[:examples])})")
        out.append("")
    return "\n".join(out)
