# Bugs

* RainbowSixGame.exe doesn't launch? (not fully tested)
* Breaks in OneDrive folders (need OneDrive check)
* When you launch after you just played it doesn't work because RainbowSix background process is still running
* Windows 10 doesn't have Windows Terminal emulator on PATH (or at all), so downloader doesn't work for that OS

# Features

* Auto - updater
* Use Python / .NET interop with pythonnet to use DepotDownloader.dll for faster download speeds, better integration with the UI and compatability for Windows 10
* UI error messages
* Check for any RainbowSix or RainbowSixGame processes that are currently running
* Find better way to pack season metadata (a couple enums makes a lot of code redundant)