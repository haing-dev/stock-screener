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
set PACK=
for /f "delims=" %%d in ('dir /b /ad /o-d "output\ai_pack_*" 2^>nul') do (
  set "PACK=output\%%d"
  goto :found
)
:found
if not defined PACK (
  echo No ai_pack folder found in output. Run 3_MAKE_AI_PACK.bat first.
  pause
  exit /b 1
)
if not exist "%PACK%\moat_scores.json" (
  echo Put the moat_scores.json you got from Claude into %PACK% and run this again.
  pause
  exit /b 1
)
%PY% screener.py verify-quotes "%PACK%\moat_scores.json" "%PACK%"
start "" "%~dp0%PACK%"
pause
