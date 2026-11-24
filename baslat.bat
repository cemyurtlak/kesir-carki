@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo   KESIR CARKI baslatiliyor...
echo.
where python >nul 2>nul
if %errorlevel%==0 (python sunucu.py) else (py sunucu.py)
pause
