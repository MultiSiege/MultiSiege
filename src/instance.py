from settings import *
from constants import *
from typing import Optional
import os
import logger
import subprocess
import shutil
import tempfile

class Console:
    def __init__(self) -> None:
        self.logs = ""

    def log(self, message: str, logging_level: LogLevel) -> None:
        self.logs += f"[{logging_level.name}]: {message}\n"

    def display(self) -> str:
        return self.logs
    
    def clear(self) -> None:
        self.logs = ""

class Instance:
    def __init__(self, instance_directory: str, load_from_file: bool, *, instance_name: Optional[str] = None, username: Optional[str] = None, version: Optional[SiegeVersions] = None) -> None:
        self.INSTANCE_DIRECTORY = instance_directory
        self.SIEGE_DIRECTORY = os.path.join(instance_directory, 'siege')
        self.SETTINGS_PATH = os.path.join(instance_directory, 'instance_settings.json')

        self.console = Console()

        if not os.path.isdir(self.INSTANCE_DIRECTORY): os.mkdir(self.INSTANCE_DIRECTORY)
        if not os.path.isdir(self.SIEGE_DIRECTORY): os.mkdir(self.SIEGE_DIRECTORY)

        self.siege_process: subprocess.Popen[bytes] | None = None

        if load_from_file:
            try:
                self.settings = InstanceSettings(self.SETTINGS_PATH)
            except:
                logger.log("Invalid instance data, skipping instance.", LogLevel.WARNING)
                raise ValueError('Invalid instance data.')
        else:
            if instance_name is None or username is None or version is None:
                logger.log("Attempted to create a new instance with incomplete data.", LogLevel.ERROR)
                raise ValueError("Attempted to create a new instance with incomplete data.")
            else:
                try:
                    self.settings = InstanceSettings(
                        self.SETTINGS_PATH,
                        instance_name=instance_name,
                        username=username,
                        version=version
                    )
                except:
                    logger.log("Invalid instance data, skipping instance.", LogLevel.WARNING)
                    raise ValueError('Invalid instance data.')
                
    def launch(self) -> None:
        """
        Attempts to launch the instance through `RainbowSix.exe`.
        """
        try:
            self.siege_process = subprocess.Popen([os.path.join(self.SIEGE_DIRECTORY, "RainbowSix.exe")], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            self.console.log("Could not find RainbowSix.exe, try verifying files to recover lost data.", LogLevel.ERROR)
            self.siege_process = None
            return

        out, err = self.siege_process.communicate()

        if self.siege_process.returncode != 0:
            self.console.log(f"Siege process returned with error code {self.siege_process.returncode}. Check you have verified files correctly.", LogLevel.ERROR)
        else:
            self.console.log(f"Siege process successfully finished", LogLevel.INFO)

        self.siege_process = None

    def kill(self) -> None:
        """
        Kills the siege process if it is running.

        `WARNING`: Should only be used if the process is not communicating properly.
        """
        if self.siege_process is None: return logger.log("Attempted to kill instance process that is not currently running.", LogLevel.WARNING)

        self.siege_process.kill()
        self.siege_process = None

        self.console.log("Killed siege process that is currently running.", LogLevel.WARNING)

    def download(self, username: str, password: str) -> None:
        """
        Downloads the instance of siege using `steamctl`.
        Automatically applies the right crack for the respective season.

        Should only be used once when an instance is created, any other time use the `verify` method.
        """
        depot = SiegeDepots[self.settings.version.name]

        try:
            downloader_process = subprocess.run(["steamctl", "depot", "download", ])
        except:
            print("ez")

    def create_shortcut(self, name: str, shortcut_path: str) -> None:
        """
        Creates a shortcut for the RainbowSix.exe file with the `name` specified.

        Shortcuts are saved to `shortcut_path`.
        """
        siege_exe_path = os.path.join(self.SIEGE_DIRECTORY, "RainbowSix.exe")
        if not os.path.isfile(siege_exe_path): return self.console.log("Attempted to create shortcut with missing RainbowSix.exe", LogLevel.WARNING)

        with tempfile.TemporaryDirectory() as tmpdir:
            bat_file= os.path.join(tmpdir, "CreateShortcut.vbs")
            name_path = os.path.join(shortcut_path,f"{name.upper()}.lnk")
            with open(bat_file, "w") as fout:
                fout.write(SCIPTFILE.format(name=name_path, targetpath=siege_exe_path))
            try:
                subprocess.call(["cscript", bat_file], cwd=tmpdir)
            except Exception as ex:
                self.console.log("Error creating shoutcut", LogLevel.ERROR)
                self.console.log(ex, LogLevel.ERROR)
 
            self.console.log(f"Shortcut link created, check {shortcut_path}", LogLevel.INFO)

    def export_instance(self) -> None:
        pass

    def delete(self) -> None:
        """
        Deletes the entire instance folder.
        """
        try:
            shutil.rmtree(self.INSTANCE_DIRECTORY)
            logger.log(f"Removed instance {self.settings.instance_name}", LogLevel.INFO)
        except:
            logger.log(f"Failed to remove instance {self.settings.instance_name}", LogLevel.ERROR)
            raise ValueError(f"Failed to remove instance {self.settings.instance_name}")
    
    def dump_codex(self) -> None:
        """
        Dumps the relevant `GAMENAME` and `USERNAME` onto the `CODEX.ini` crack file.
        """
        try:
            with open(os.path.join(self.SIEGE_DIRECTORY, "CODEX.ini"), "r+") as f:
                pass

        except:
            self.console.log("Could not modify CODEX.ini crack file.")