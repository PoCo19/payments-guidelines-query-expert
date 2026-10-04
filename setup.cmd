@echo off
setlocal
cd /d "%~dp0"
set "projectPython=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if not exist "%projectPython%" set "projectPython=python"
if exist ".venv\Scripts\python.exe" goto install
"%projectPython%" -m venv .venv
if errorlevel 1 exit /b 1
:install
".venv\Scripts\python.exe" -m pip install -r requirements-lock.txt
if errorlevel 1 exit /b 1
".venv\Scripts\python.exe" -X utf8 download_reranker.py
if errorlevel 1 exit /b 1
echo Setup complete. Open Ollama, run run.cmd embed, then run run.cmd.
