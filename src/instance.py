from settings import *
from constants import *
from typing import Optional
import os
import logger
import subprocess
import shutil
from win32com.client import Dispatch

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
        Attempts to launch the instance through `RainbowSix.bat`. If it cannot launch, it will paste in cracks again.
        """
        try:
            self.siege_process = subprocess.Popen([os.path.join(self.SIEGE_DIRECTORY, "RainbowSix.bat")], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            self.console.log("Could not find RainbowSix.bat, try verifying files to recover lost data.", LogLevel.ERROR)
            self.siege_process = None

            crack_type = SiegeVersions_CrackTypes[self.settings.version.name].version

            #add crack files
            if crack_type == CrackType.Y1SX_Y6S2:
                shutil.copytree(Y1SX_Y6S4_CRACKS, self.SIEGE_DIRECTORY, dirs_exist_ok=True)
            elif crack_type == CrackType.Y6S3:
                shutil.copytree(Y6S3_CRACK, self.SIEGE_DIRECTORY, dirs_exist_ok=True)
            else:
                shutil.copytree(Y6S4_Y8SX_CRACKS, self.SIEGE_DIRECTORY, dirs_exist_ok=True)
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

    def open_instance_folder(self) -> None:
        subprocess.Popen(f"explorer {os.path.abspath(self.INSTANCE_DIRECTORY)}")
    
    def open_siege_folder(self) -> None:
        subprocess.Popen(f"explorer {os.path.abspath(self.SIEGE_DIRECTORY)}")

    def download(self, username: str, password: str, sku_rus: bool) -> None:
        """
        Downloads the instance of siege using `DepotDownloader`.
        Automatically applies the right crack for the respective season.
        """
        manifest_content = SiegeManifests_CONTENT[self.settings.version.name]
        manifest_sku_ww = SiegeManifests_SKU_WW[self.settings.version.name]
        manifest_sku_rus = SiegeManifests_SKU_RUS[self.settings.version.name]

        command = ""

        #download localisation files
        if sku_rus:
            command += f'wt cmd /c {DEPOT_DOWNLOADER} -app {SIEGE_APP_ID} -depot {SiegeDepots.SKU_RUS} -manifest {manifest_sku_rus} -username {username} -password {password} -dir "{os.path.abspath(self.SIEGE_DIRECTORY)}"'
        else:
            command += f'wt cmd /c {DEPOT_DOWNLOADER} -app {SIEGE_APP_ID} -depot {SiegeDepots.SKU_WW} -manifest {manifest_sku_ww} -username {username} -password {password} -dir "{os.path.abspath(self.SIEGE_DIRECTORY)}"'

        #download content
        command += f' & {DEPOT_DOWNLOADER} -app {SIEGE_APP_ID} -depot {SiegeDepots.CONTENT} -manifest {manifest_content} -username {username} -password {password} -dir "{os.path.abspath(self.SIEGE_DIRECTORY)}"'
        subprocess.run(command)

        logger.log(f"Download completed for {self.settings.instance_name}.", LogLevel.INFO)

    def create_shortcut(self, shortcut_path: str) -> None:
        """
        Creates a shortcut for the RainbowSix.bat file with the `shortcut_path` specified.
        """
        siege_bat_path = os.path.abspath(os.path.join(self.SIEGE_DIRECTORY, "RainbowSix.bat"))
        if not os.path.isfile(siege_bat_path): return self.console.log("Attempted to create shortcut with missing RainbowSix.bat", LogLevel.WARNING)

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = siege_bat_path
        shortcut.WorkingDirectory = self.SIEGE_DIRECTORY
        shortcut.save()

        logger.log(f"Shortcut successfully created for {self.settings.instance_name}", LogLevel.INFO)

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