# Bugs

* RainbowSixGame.exe doesn't launch? (not fully tested)
* Breaks in OneDrive folders (need OneDrive check) - Fixed
* When you launch after you just played it doesn't work because RainbowSix background process is still running - Now has a check so they can kill process manually
* Windows 10 doesn't have Windows Terminal emulator on PATH (or at all), so downloader doesn't work for that OS - Fixed
* Shortcut path doesn't have /belaunch argument, so launches with BattlEye enabled - Fixed
* When launching from anywhere other than the EXE itself it fails because it doesn't know its current working directory. - Fixed
* We append the same modules (src and src/widgets) to PATH multiple times, need to call it once. - Fixed
* When setting instance settings it refreshes your instances so it might select a different instance once you click ok

# Features

* Auto - updater
* Use Python / .NET interop with pythonnet to use DepotDownloader.dll for faster download speeds, better integration with the UI and compatability for Windows 10 - scrapped
* UI error messages - Done
* Check for any RainbowSix or RainbowSixGame processes that are currently running - Done
* Find better way to pack season metadata (a couple enums makes a lot of code redundant)
* Custom icons for instances
* When running the program, check if there are MultiSiege processes already running and if so don't open a new window.
* Add a signal when different instance selected so we don't have to grab current instance variable every time we want to use it