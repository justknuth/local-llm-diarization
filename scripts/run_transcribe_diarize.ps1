# Set your project root (adjust as needed)
$projectRoot = "C:\Users\justin.knuth\pyprojects"
$inboundFolder = Join-Path $projectRoot "inbound"
$outboundFolder = Join-Path $projectRoot "outbound"
$pythonScript = Join-Path $PSScriptRoot "transcribe_diarize.py"
$venvActivate = Join-Path $projectRoot "venv\Scripts\Activate.ps1"

& $venvActivate

Write-Host "Looking for media files in: $inboundFolder"

$files = Get-ChildItem -Path $inboundFolder -File | Where-Object {
    $_.Extension.ToLower() -in '.mp3', '.wav', '.m4a', '.mp4'
}

Write-Host "Found $($files.Count) files."

foreach ($file in $files) {
    Write-Host "Processing $($file.Name)..."

    $inputFile = $file.FullName
    $fileName = $file.BaseName

    python $pythonScript --input "$inputFile" --output "$outboundFolder\$fileName.json"

    Write-Host "Output saved to $outboundFolder\$fileName.json"
}
