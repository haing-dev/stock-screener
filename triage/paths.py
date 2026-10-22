"""Where the triage keeps its work (all under cache/, carried between runs by the workflow's cache)."""
import os

from qs.config import CACHE_DIR, ROOT

TRI = os.path.join(CACHE_DIR, "tri")
PANEL = os.path.join(TRI, "panel")          # <ym>.json.gz: one record per US company at each month-end
RETURNS = os.path.join(TRI, "returns")      # <ym>.json.gz: open-to-open return to the next month's entry day
OWNERS = os.path.join(TRI, "owners")        # 13F conviction holdings per data set
INSIDERS = os.path.join(TRI, "insiders")    # Form 4 open-market trades per quarter
OUT = os.path.join(TRI, "out")              # episodes, scores, stats (rebuilt every build)
MARK = os.path.join(TRI, "mark.json.gz")    # latest trading day's closes (daily mark-to-market)
SITE = os.path.join(ROOT, "triage_site")    # built site (published to branch 'site')
WEB = os.path.join(ROOT, "triage", "web")   # page code


def ensure(*dirs):
    for d in dirs:
        os.makedirs(d, exist_ok=True)
