@echo off
setlocal
cd /d "%~dp0"
set "projectPython=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if exist "%~dp0.venv\Scripts\python.exe" set "projectPython=%~dp0.venv\Scripts\python.exe"
if exist "%projectPython%" goto ready
where python >nul 2>nul
if errorlevel 1 goto missingPython
set "projectPython=python"
:ready
if "%~1"=="" goto serve
if /I "%~1"=="serve" goto serve
if /I "%~1"=="launch" goto launch
if /I "%~1"=="test" goto test
if /I "%~1"=="evaluate" goto evaluate
if /I "%~1"=="embed" goto embed
if /I "%~1"=="validate" goto validate
if /I "%~1"=="live-check" goto livecheck
if /I "%~1"=="reranker" goto reranker
echo Usage: run.cmd [serve^|launch^|test^|evaluate^|embed^|validate^|live-check^|reranker]
exit /b 2
:serve
echo Keep this window open. Open http://127.0.0.1:8765 in your browser.
echo Ollama must be running for AI answers. Press Ctrl+C to stop the server.
"%projectPython%" -B -X utf8 app.py serve
exit /b %errorlevel%
:test
"%projectPython%" -B -X utf8 -m unittest discover -s tests -v
exit /b %errorlevel%
:launch
echo Open http://127.0.0.1:8766 in your browser. Keep this window open.
"%projectPython%" -B -X utf8 launch_app.py
exit /b %errorlevel%
:evaluate
"%projectPython%" -B -X utf8 app.py evaluate
exit /b %errorlevel%
:embed
"%projectPython%" -B -X utf8 -u app.py embed
exit /b %errorlevel%
:validate
"%projectPython%" -B -X utf8 -u evaluation/validate_v05.py
exit /b %errorlevel%
:livecheck
"%projectPython%" -B -X utf8 -u evaluation/live_v05.py
exit /b %errorlevel%
:reranker
"%projectPython%" -B -X utf8 download_reranker.py
exit /b %errorlevel%
:missingPython
echo Python was not found. Install Python 3.10 or later or restore the bundled runtime.
exit /b 1
