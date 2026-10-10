@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Run setup.cmd first to prepare the project Python environment.
  exit /b 1
)
".venv\Scripts\python.exe" -B -X utf8 tools\document_pipeline.py %*
exit /b %errorlevel%
