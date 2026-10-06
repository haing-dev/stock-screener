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
echo Quick run of all six screens on ~45 well-known companies (5-10 minutes the first time)...
%PY% screener.py test
echo.
echo Finished. Opening the output folder - open test_results.xlsx
start "" "%~dp0output"
pause
