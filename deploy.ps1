# Kopiert den Inhalt von device/ auf den ESP32 und startet ihn neu.
# Aufruf: .\deploy.ps1            (Port automatisch)
#         .\deploy.ps1 COM5       (Port explizit)
param([string]$Port = "auto")

Push-Location "$PSScriptRoot\device"
try {
    $files = Get-ChildItem -File -Filter *.py | Where-Object Name -ne "config.example.py" | ForEach-Object Name
    mpremote connect $Port cp @files : + cp -r lib : + reset
} finally {
    Pop-Location
}
