@echo off
rem Global Macro Book - WRDS inventory. Double-click this file. Keep it in the same folder as gm_wrds_inventory.py.
cd /d "%~dp0"
set H=ttdlisa@wrds-cloud.wharton.upenn.edu
echo.
echo === 1 of 3: sending the script to WRDS. Type your WRDS password, then approve Duo (type 1 if asked).
scp gm_wrds_inventory.py %H%:~/
echo.
echo === 2 of 3: running it on WRDS. Password + Duo again. If asked "Create .pgpass file now", type y.
ssh -t %H% "qrsh -now no -pty y python3 $HOME/gm_wrds_inventory.py"
echo.
echo === 3 of 3: bringing the result back. Password + Duo one last time.
scp %H%:~/gm_inventory.txt .
echo.
if exist gm_inventory.txt (echo DONE. Attach gm_inventory.txt from this folder to the chat.) else (echo Something failed. Take a screenshot of this window and send it to Claude.)
pause
