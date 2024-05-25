@echo off
echo Starting..

IF EXIST RainbowSixGame.exe (
    start "" RainbowSixGame.exe /belaunch
) ELSE (
    start "" RainbowSix.exe /belaunch
)
echo Press any button to close the game...
pause >nul
echo Killing...
TASKKILL.EXE /IM RainbowSix.exe /F
TASKKILL.EXE /IM RainbowSixGame.exe /F
pause
echo.