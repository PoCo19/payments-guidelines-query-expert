@echo off
setlocal
cd /d "%~dp0"
set "evalPython=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if not exist "%evalPython%" set "evalPython=python"
if not exist ".venv-eval\Scripts\python.exe" "%evalPython%" -m venv .venv-eval
if errorlevel 1 exit /b 1
".venv-eval\Scripts\python.exe" -m pip install -r evaluation\requirements-ragas-lock.txt
if errorlevel 1 exit /b 1
".venv-eval\Scripts\python.exe" -m pip check
if errorlevel 1 exit /b 1
echo Evaluation environment ready. See evaluation\RAGAS_EVALUATION.md.
