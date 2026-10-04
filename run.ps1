param(
 [ValidateSet('serve','test','evaluate','embed')][string]$Action = 'serve',
 [int]$Port = 8765
)
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$bundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
if (Test-Path -LiteralPath (Join-Path $PSScriptRoot '.venv\Scripts\python.exe')) {
 $projectPython = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
} elseif (Test-Path -LiteralPath $bundledPython) {
 $projectPython = $bundledPython
} else {
 $projectPython = (Get-Command python -ErrorAction Stop).Source
}
if ($Action -eq 'test') {
 & $projectPython -B -X utf8 -m unittest discover -s tests -v
} else {
 & $projectPython -B -X utf8 app.py $Action --port $Port
}
exit $LASTEXITCODE
