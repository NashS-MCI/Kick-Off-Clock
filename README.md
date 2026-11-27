# Kick-Off-Clock

MicroPython-Projekt für den **ESP32-S3-DevKitC-1-N8R8** (8 MB Flash, 8 MB Octal-PSRAM).

## Struktur

```
device/          → alles hier wird auf den ESP32 kopiert
  boot.py        → läuft beim Start zuerst (Grundsetup)
  main.py        → Einstiegspunkt, startet die Hauptschleife
  config.py      → Pins, WLAN-Daten (nicht in Git! Vorlage: config.example.py)
  lib/           → eigene Module (MicroPython sucht hier automatisch)
deploy.ps1       → lädt device/ auf den ESP32
requirements.txt → PC-Tools für die .venv
```

## Setup am PC

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item device\config.example.py device\config.py
```

## Firmware flashen (einmalig)

1. Firmware **ESP32_GENERIC_S3**, Variante **SPIRAM_OCT** (wegen Octal-PSRAM) von
   https://micropython.org/download/ESP32_GENERIC_S3/ herunterladen.
   Die Version sollte zu den Stubs in `requirements.txt` passen (aktuell 1.29).
2. Board über den USB-Port **„UART“** anschließen, COM-Port im Geräte-Manager nachsehen.
3. Flashen:
   ```powershell
   python -m esptool --chip esp32s3 --port COM3 erase_flash
   python -m esptool --chip esp32s3 --port COM3 write_flash -z 0 ESP32_GENERIC_S3-SPIRAM_OCT-xxx.bin
   ```
   Falls der Port nicht verbindet: **BOOT** gedrückt halten, **RST** kurz drücken, BOOT loslassen.

## Entwickeln

```powershell
.\deploy.ps1                       # device/ auf den ESP kopieren und neu starten
mpremote                           # REPL öffnen (Ctrl+] zum Beenden)
mpremote run device\main.py        # main.py testen, ohne sie zu kopieren (lib/ muss schon drauf sein)
mpremote mount device exec "import main"   # device/ direkt vom PC ausführen, ohne zu kopieren
mpremote ls                        # Dateien auf dem ESP anzeigen
```
