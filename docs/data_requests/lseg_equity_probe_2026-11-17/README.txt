LSEG equity probe (stocks) - what to do

1. Copy LSEG_equity_probe_v1.xlsx to Documents\WRDS results\lseg\ on your PC and open it in Excel.
2. Make sure LSEG Workspace is signed in (the Workspace and Datastream tabs are visible). If Excel asks, click
   "Enable Editing" and "Enable Content".
3. Wait until no cell on any sheet says "Retrieving" and the number in cell B4 of the Check sheet has not changed
   for two minutes. This can take 10 to 20 minutes: some formulas ask for very large lists on purpose.
4. Press Ctrl+S and keep the file name (if Excel asks about the format, keep .xlsx).
5. Tell Claude "saved". Claude's reader job runs on your PC and reports only what came back (counts, dates and
   error messages), never the numbers themselves.

Errors in many blocks are expected: about a third of the field names are guesses, and an error is the answer.
If Excel freezes on the Limits sheet, wait; if it stays frozen for more than 15 minutes, close Excel without
saving and tell Claude.
