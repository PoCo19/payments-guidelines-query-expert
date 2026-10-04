# Run after build_product_document.py. Uses installed Microsoft Word for PDF export.
# Creates its own hidden Word instance and opens only the generated handbook.
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent
$docInput = Join-Path $projectRoot 'output\docx\Circular_Intelligence_Core_Guide_v051.docx'
$pdfOutput = Join-Path $projectRoot 'output\pdf\Circular_Intelligence_Core_Guide_v051.pdf'
$wordRenderer = New-Object -ComObject Word.Application
$renderDocument = $null
$wordRenderer.Visible = $false
$wordRenderer.DisplayAlerts = 0
$wordRenderer.AutomationSecurity = 3
try {
    $renderDocument = $wordRenderer.Documents.Open($docInput, $false, $true, $false)
    $renderDocument.Repaginate()
    $renderDocument.ExportAsFixedFormat($pdfOutput, 17)
    Write-Output "Rendered pages: $($renderDocument.ComputeStatistics(2))"
    Write-Output $pdfOutput
} finally {
    if ($renderDocument) { $renderDocument.Close(0) }
    $wordRenderer.Quit()
}

