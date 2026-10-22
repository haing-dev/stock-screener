# Archived: the v2.9 screener portal (stopped 2026-10-22)

The 14-screen portal was replaced by the triage site (`triage/`, workflow `.github/workflows/triage.yml`).
Nothing was deleted. The code under `qs/` is still used: the triage reuses its SEC extraction, metrics,
point-in-time backtest data, 13F and insider code.

What moved here:

| Archived | What it was |
|---|---|
| `site/` | Front end of the encrypted portal (Cloudflare Worker "stock-screener" served it from branch `site`) |
| `workflows/screen.yml` | Full screen, 1st and 16th of the month |
| `workflows/daily.yml` | Daily re-pricing |
| `workflows/background.yml` | Slow fills (histories, descriptions) |
| `workflows/report.yml` | Manual check report |
| `workflows/validate.yml` | Monthly validation of the frozen screens (validation/PROTOCOL.md) |

The last published portal build is kept on branch `site-archive-v2.9`. The triage workflow copies `site` there
before its first publish, and never overwrites it afterwards.

To restore: move the workflow files back to `.github/workflows/` and the folder `site/` back to the repository
root. Then point `qs/portal.py` SITE_DIR back to `site`, and do the same in `tests/demo_portal.py` and
`scripts/publish.sh`.
