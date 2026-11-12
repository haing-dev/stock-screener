"""lseg_read_v1: read every saved LSEG workbook of a pull (L*.xlsx, P*.xlsx built by docs/data_requests/build_lseg_pull.py)
and report, per formula block, whether it returned data, how many numbers, the date range, spacing and day-of-month
kind, and any error text. Metadata only: no data value is printed.
Folder: env LSEG_DIR, else <Documents>\\WRDS results\\lseg\\pull_2026-11-12."""
import datetime as dt
import glob
import os
import re
import statistics
import sys
import time

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]
T0 = time.time()
print("=== lseg_read_v1 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
import openpyxl  # noqa: E402

D = os.environ.get("LSEG_DIR") or os.path.join(os.path.dirname(os.getcwd()), "lseg", "pull_2026-11-12")
files = sorted(f for f in glob.glob(os.path.join(D, "*.xlsx")) if not os.path.basename(f).startswith("~$"))
if not files:
    print("no workbook in", D)
    print("=== END ===")
    sys.exit(0)
ROW0 = 6
PID = re.compile(r"^[A-Z][A-Za-z0-9]*-\d+$|^P\d+$")
EPOCH = dt.date(1899, 12, 30)
ISO = re.compile(r"^\s*(\d{4})-(\d{2})-(\d{2})")
DMY = re.compile(r"^\s*(\d{1,2})[-/ ]([A-Za-z]{3}|\d{1,2})[-/ ](\d{4})")
MON = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}


def as_date(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    if isinstance(v, str):
        m = ISO.match(v)
        if m:
            try:
                return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            except ValueError:
                return None
        m = DMY.match(v)
        if m:
            mo = MON.get(m.group(2).lower()) if not m.group(2).isdigit() else int(m.group(2))
            try:
                return dt.date(int(m.group(3)), mo, int(m.group(1))) if mo else None
            except ValueError:
                return None
    return None


def num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


GRAND = {"DATA": 0, "TEXT": 0, "EXCEL ERROR": 0, "EMPTY": 0}


def read(path):
  print("##### file:", os.path.basename(path), "| saved", dt.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M"),
        "| %d bytes" % os.path.getsize(path))
  wbv = openpyxl.load_workbook(path, read_only=True, data_only=True)
  tot = {"DATA": 0, "TEXT": 0, "EXCEL ERROR": 0, "EMPTY": 0}
  for ws in wbv.worksheets:
      if ws.title == "Check":
          continue
      grid = [list(r) for r in ws.iter_rows(values_only=True)]
      ncol = max((len(r) for r in grid), default=0)
      print("--- sheet %s | rows read %d" % (ws.title, len(grid)))
      starts = [c for c in range(ncol) if len(grid) > 1 and c < len(grid[1]) and isinstance(grid[1][c], str) and PID.match(grid[1][c])]
      for q, c in enumerate(starts):
          pid = grid[1][c]
          W = (starts[q + 1] - c) if q + 1 < len(starts) else 8
          label = grid[2][c] if c < len(grid[2]) else ""
          ftxt = str(grid[3][c] if c < len(grid[3]) else "")[9:]
          cols = []
          for k in range(c, min(c + W - 1, ncol)):
              cols.append([grid[r][k] if k < len(grid[r]) else None for r in range(ROW0 - 1, len(grid))])
          first = cols[0][0] if cols and cols[0] else None
          texts, nnum, datecol, dates = [], 0, None, []
          for j, col in enumerate(cols):
              filled = [v for v in col if v is not None and v != ""]
              if not filled:
                  continue
              dd = [as_date(v) for v in filled]
              nd = sum(1 for d in dd if d)
              serial = [v for v in filled if num(v) and 15000 <= v <= 60000]
              if datecol is None and nd >= 0.8 * len(filled) and nd >= 3:
                  datecol, dates = j, [d for d in dd if d]
                  continue
              if datecol is None and len(serial) >= 0.8 * len(filled) and len(serial) >= 12:
                  steps = [b - a for a, b in zip(serial, serial[1:])]
                  if steps and (all(s >= 0 for s in steps) or all(s <= 0 for s in steps)) and any(steps):
                      datecol, dates = j, [EPOCH + dt.timedelta(days=int(v)) for v in serial]
                      continue
              nnum += sum(1 for v in filled if num(v))
              for v in filled[:3]:
                  if isinstance(v, str) and len(texts) < 6:
                      texts.append(v[:60])
          err = isinstance(first, str) and first.startswith("#")
          if nnum > 0:
              status = "DATA"
          elif err:
              status = "EXCEL ERROR"
          elif any(cols[j][i] not in (None, "") for j in range(len(cols)) for i in range(min(len(cols[j]), 50))):
              status = "TEXT"
          else:
              status = "EMPTY"
          tot[status] += 1
          line = "%s | %s | %s | %s" % (pid, status, label, ftxt[:110])
          if status == "DATA":
              if dates:
                  gaps = [abs((b - a).days) for a, b in zip(dates, dates[1:])]
                  order = "oldest first" if dates[0] <= dates[-1] else "newest first"
                  eom = sum(1 for d in dates if (d + dt.timedelta(days=1)).month != d.month)
                  line += " | numbers %d | dates %d: %s to %s (%s, typical gap %s days, calendar month-end %d%%)" % (
                      nnum, len(dates), min(dates), max(dates), order, int(statistics.median(gaps)) if gaps else "-",
                      round(100 * eom / len(dates)))
              else:
                  line += " | numbers %d | no date column recognised" % nnum
              if texts:
                  line += " | headers: " + "; ".join(texts[:4])
          else:
              shown = [str(first)[:90]] if isinstance(first, str) else []
              shown += [t for t in texts if t not in shown][:3]
              line += " | cell text: " + (" / ".join(shown) if shown else "(nothing)")
          print(line)
  print("TOTAL %s | " % os.path.basename(path) + " | ".join("%s %d" % kv for kv in tot.items()))
  for k in tot:
      GRAND[k] += tot[k]
  wbv.close()


for p in files:
    try:
        read(p)
    except Exception as e:
        print("FILE %s could not be read: %s %s" % (os.path.basename(p), type(e).__name__, str(e)[:120]))
print("GRAND TOTAL | " + " | ".join("%s %d" % kv for kv in GRAND.items()))
print("=== END === %.0fs" % (time.time() - T0))
