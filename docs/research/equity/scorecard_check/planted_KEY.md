# KEY to planted/excerpts.md (do not show to the checker)

| Excerpt | Status |
|---|---|
| E1 June peer groups (Peers._form) | planted |
| E2 Per-quarter aggregate SQL and its pull | clean |
| E3 Tier rule (section 7) | planted |
| E4 CUSIP-to-CRSP matching at the quarter-end | clean |
| E5 Entry month and buy-and-hold months | planted |
| E6 Fund share-class combination | planted |
| E7 Newey-West regression | clean |
| E8 Bridging a missed quarter and stopping | planted |
| E9 Rank shares and pools | clean |
| E10 What the report prints for an investor | planted |

Source: tools/equity/wrds/eq_scorecard.py, code sha256 a7792a0f4cd9... (module unchanged). Six planted, four clean; none of the six is among the registration's section 11 errors.

## E1 (June peer groups (Peers._form)): planted
- Changed line:
```python
        bps = np.percentile(cap[u], [20, 40, 60, 80])
```
- Original line:
```python
        bps = np.percentile(cap[ny], [20, 40, 60, 80])
```
- What goes wrong: Size breakpoints are computed on all stocks of the universe instead of NYSE stocks only (spec 4.3: NYSE breakpoints). Size fifths become equal-count over all stocks, so most NYSE firms land in the top groups and the 125 peer groups are wrong.

## E2 (Per-quarter aggregate SQL and its pull): clean (identical to the module)

## E3 (Tier rule (section 7)): planted
- Changed line:
```python
        if per.get(p["style"], 0) > STYLE_CAP:
```
- Original line:
```python
        if per.get(p["style"], 0) >= STYLE_CAP:
```
- What goes wrong: The style cap admits a ninth investor of the same primary style (spec 7.3: at most eight per primary style).

## E4 (CUSIP-to-CRSP matching at the quarter-end): clean (identical to the module)

## E5 (Entry month and buy-and-hold months): planted
- Changed line:
```python
    for k in range(int(h.max())):
```
- Original line:
```python
    for k in range(1, int(h.max()) + 1):
```
- What goes wrong: Holding months become em, em+1, em+2 instead of em+1..em+3: each quarter's holdings earn the return of the deadline month itself, before they enter at that month's close (one-month look-ahead; spec 3.4: the 31 March holdings are held June, July, August). The last month of each holding period is dropped too.

## E6 (Fund share-class combination): planted
- Changed line:
```python
    f["w"] = np.where((pf == f.crsp_fundno) & (pm == f.mi - 1), f.mtna, np.nan)
```
- Original line:
```python
    f["w"] = np.where((pf == f.crsp_fundno) & (pm == f.mi - 1), f.mtna.shift(1), np.nan)
```
- What goes wrong: Classes are weighted by assets at the END of the same month (which already include that month's return and flows) instead of the previous month-end (spec 5: assets at the start of the month). It favours the class that did better that month.

## E7 (Newey-West regression): clean (identical to the module)

## E8 (Bridging a missed quarter and stopping): planted
- Changed line:
```python
    f["H"] = np.where((nxt - f.q) >= 2, 6, 3).astype("int64")
```
- Original line:
```python
    f["H"] = np.where((nxt - f.q) == 2, 6, 3).astype("int64")
```
- What goes wrong: Any gap of two or more missed quarters is bridged for 3 extra months (stale portfolio held after the spell should have ended), instead of only a gap of exactly one missed quarter (spec 3.5: a longer gap ends the spell). With a long gap the filer also gets 3 months it never held.

## E9 (Rank shares and pools): clean (identical to the module)

## E10 (What the report prints for an investor): planted
- Changed line:
```python
            L.append(_wline(d["id"], w, s, full_rec or s.get("n", 0) >= MIN_RESULT))
```
- Original line:
```python
            L.append(_wline(d["id"], w, s, full_rec or s.get("n", 0) >= MIN_STATS))
```
- What goes wrong: Statistics are printed for a window with 36 to 59 months even when the whole record is under 60 months (spec 8: statistics only where the window has 60 months or the whole record has 60 months; otherwise rank shares only).
