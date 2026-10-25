@echo off
title Alpenexperte Server (Port 3000)
cd /d "%~dp0"
echo ==========================================
echo  Alpenexperte.de - Entwicklungsserver
echo ==========================================
echo.
echo  Server laeuft unter: http://localhost:3000
echo.
echo  Druecke STRG+C zum Beenden
echo ==========================================
echo.
python -m http.server 3000
pause
