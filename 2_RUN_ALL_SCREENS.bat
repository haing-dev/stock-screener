@echo off
setlocal
cd /d "%~dp0"
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set PY=
where py >nul 2>nul && set PY=py
if not defined PY where python >nul 2>nul && set PY=python
if not defined PY (
  echo.
  echo Python was not found. Install it from https://www.python.org/downloads/
  echo and TICK the box "Add python.exe to PATH" during installation. Then run this again.
  pause
  exit /b 1
)
echo Checking required packages (first time takes a minute)...
%PY% -m pip install --disable-pip-version-check -q -r requirements.txt
if errorlevel 1 (
  echo Package install failed - see the message above.
  pause
  exit /b 1
)
echo.
echo All six screens on every NYSE + Nasdaq company.
echo First run downloads the SEC filings again (new data format): about 30-50 minutes.
echo Then prices for the candidates from Twelve Data (on a free plan this can take two days -
echo just run this again tomorrow; everything already fetched is cached).
echo You can close the window any time - running it again continues where it stopped.
echo.
%PY% screener.py run
echo.
echo Finished. Opening the output folder - open the newest screen_results_*.xlsx
start "" "%~dp0output"
pause
