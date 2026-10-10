@echo off
setlocal
cd /d "%~dp0"
set "projectPython=python"
if exist ".venv\Scripts\python.exe" set "projectPython=.venv\Scripts\python.exe"
"%projectPython%" -X utf8 tools\handoff.py %*
exit /b %errorlevel%
