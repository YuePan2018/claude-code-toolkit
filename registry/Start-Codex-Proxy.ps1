$ErrorActionPreference = 'Stop'

$proxy = 'http://127.0.0.1:10808'

$env:HTTP_PROXY = $proxy
$env:HTTPS_PROXY = $proxy
$env:ALL_PROXY = $proxy
$env:NO_PROXY = 'localhost,127.0.0.1,::1'

$package = Get-AppxPackage -Name OpenAI.Codex -ErrorAction Stop
$codexExe = Join-Path $package.InstallLocation 'app\Codex.exe'

if (-not (Test-Path -LiteralPath $codexExe)) {
    throw "Codex executable was not found: $codexExe"
}

Start-Process -FilePath $codexExe -WorkingDirectory $PSScriptRoot
