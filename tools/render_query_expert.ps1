$ErrorActionPreference='Stop'
$root=Split-Path $PSScriptRoot -Parent
$out=Join-Path $root 'output\midsem'
$render=Join-Path $root 'tmp\midsem\query-expert-render'
New-Item -ItemType Directory -Force $render | Out-Null
$wordApp=New-Object -ComObject Word.Application
$wordApp.Visible=$false
$wordApp.DisplayAlerts=0
$wordApp.AutomationSecurity=3
$reportDoc=$null
try {
 $reportDoc=$wordApp.Documents.Open((Join-Path $out 'Payments_Guidelines_Query_Expert_Report.docx'),$false,$true,$false)
 $reportDoc.Repaginate()
 $reportDoc.ExportAsFixedFormat((Join-Path $out 'Payments_Guidelines_Query_Expert_Report.pdf'),17)
 Write-Output "Report pages: $($reportDoc.ComputeStatistics(2))"
} finally {if($reportDoc){$reportDoc.Close(0)};$wordApp.Quit()}
$pptApp=New-Object -ComObject PowerPoint.Application
$pptApp.AutomationSecurity=3
$slideDeck=$null
try {
 $slideDeck=$pptApp.Presentations.Open((Join-Path $out 'Payments_Guidelines_Query_Expert_Slides.pptx'),-1,0,0)
 $slideDeck.Export((Join-Path $render 'slides'),'PNG',1600,900)
 $slideDeck.SaveAs((Join-Path $out 'Payments_Guidelines_Query_Expert_Slides.pdf'),32)
 Write-Output "Slides: $($slideDeck.Slides.Count)"
} finally {if($slideDeck){$slideDeck.Close()};$pptApp.Quit()}
$poppler='C:\Users\Admin\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe'
New-Item -ItemType Directory -Force (Join-Path $render 'report') | Out-Null
& $poppler -scale-to 1500 -png (Join-Path $out 'Payments_Guidelines_Query_Expert_Report.pdf') (Join-Path $render 'report\page')
