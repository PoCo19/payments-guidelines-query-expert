@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv-eval\Scripts\python.exe" (
 echo Run setup-eval.cmd first.
 exit /b 1
)
set "RAGAS_DO_NOT_TRACK=true"
".venv-eval\Scripts\python.exe" -B -X utf8 evaluation\ragas_runner.py %*
exit /b %errorlevel%
