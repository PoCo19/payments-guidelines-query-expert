@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Run setup.cmd first to create the project Python environment.
  pause
  exit /b 1
)
echo Open http://127.0.0.1:8769 after the server is ready. Keep this window open.
".venv\Scripts\python.exe" -B -X utf8 tools\serve_graph_pilot.py
exit /b %errorlevel%
