from settings import *
from constants import *
from typing import Optional
import os
import logger
import subprocess
import shutil
from win32com.client import Dispatch
import configparser

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

        self.siege_process: subprocess.Popen[bytes] | None = None

        if not os.path.isdir(self.INSTANCE_DIRECTORY): os.mkdir(self.INSTANCE_DIRECTORY)
        if not os.path.isdir(self.SIEGE_DIRECTORY): os.mkdir(self.SIEGE_DIRECTORY)

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
                
    def launch(self) -> bool:
        """
        Attempts to launch the instance through `RainbowSix.bat`. If it cannot launch, it will paste in cracks again.

        Returns a `bool` for if the operation succeeded or not.
        """
        rainbowsix_exe = os.path.abspath(os.path.join(self.SIEGE_DIRECTORY, "RainbowSix.exe"))
        rainbowsixgame_exe = os.path.abspath(os.path.join(self.SIEGE_DIRECTORY, "RainbowSixGame.exe"))

        if os.path.isfile(rainbowsix_exe):
            file_path = rainbowsix_exe
        elif os.path.isfile(rainbowsixgame_exe):
            file_path = rainbowsixgame_exe
        else:
            self.console.log("Executable file does not exist!", LogLevel.ERROR)
            return False
        
        crack_type = SiegeVersions_CrackTypes[self.settings.version.name].value

        if crack_type == CrackType.Y1SX_Y6S2:
            crack = Y1SX_Y6S4_CRACKS
        elif crack_type == CrackType.Y6S3:
            crack = Y6S3_CRACK
        else:
            crack = Y6S4_Y8SX_CRACKS

        shutil.copytree(crack, self.SIEGE_DIRECTORY, dirs_exist_ok=True)#cba to deal with different hashes of files that may make the crack not work        
        self.dump_crack()

        try:
            self.siege_process = subprocess.Popen([file_path, "/belaunch"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            self.console.log("Could not find siege executable, try verifying files to recover lost data.", LogLevel.ERROR)
            self.siege_process = None

            return False
        return True

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
        subprocess.call(f"explorer {os.path.abspath(self.INSTANCE_DIRECTORY)}")
    
    def open_siege_folder(self) -> None:
        subprocess.call(f"explorer {os.path.abspath(self.SIEGE_DIRECTORY)}")

    def download(self, username: str, password: str, sku_rus: bool) -> None:
        """
        Downloads the instance of siege using `DepotDownloader`.
        """
        manifest_content = SiegeManifests_CONTENT[self.settings.version.name]
        manifest_sku_ww = SiegeManifests_SKU_WW[self.settings.version.name]
        manifest_sku_rus = SiegeManifests_SKU_RUS[self.settings.version.name]

        #download localisation files
        if sku_rus:
            command_loc = f'{DEPOT_DOWNLOADER} -app {SIEGE_APP_ID} -depot {SiegeDepots.SKU_RUS} -manifest {manifest_sku_rus} -username {username} -password {password} -dir "{os.path.abspath(self.SIEGE_DIRECTORY)}" -validate -max-servers 20 -max-downloads 20'
        else:
            command_loc = f'{DEPOT_DOWNLOADER} -app {SIEGE_APP_ID} -depot {SiegeDepots.SKU_WW} -manifest {manifest_sku_ww} -username {username} -password {password} -dir "{os.path.abspath(self.SIEGE_DIRECTORY)}" -validate -max-servers 20 -max-downloads 20'

        #download content
        command_content = f'{DEPOT_DOWNLOADER} -app {SIEGE_APP_ID} -depot {SiegeDepots.CONTENT} -manifest {manifest_content} -username {username} -password {password} -dir "{os.path.abspath(self.SIEGE_DIRECTORY)}" -validate -max-servers 20 -max-downloads 20'

        def format_season_label(label: str) -> str:
            label_list = label.split("_")

            new_label = ""

            for label in label_list:
                new_label += label[0].upper() + label[1:].lower() + " "

            return new_label[:-1]

        batch_file = """@echo off
        Title Downloading {version}...
        {command_loc}
        {command_content}
        Title Download Finished!
        echo Download Finished!
        pause
        exit
        """.format(version=format_season_label(self.settings.version.name), command_loc=command_loc, command_content=command_content)

        script_path = os.path.join(os.getcwd(), "assets", "DepotDownloader", "download.bat")

        with open(script_path, "w") as fp:
            fp.write(batch_file)

        subprocess.run(["start", "cmd", "/k", script_path], shell=True)
            
        logger.log(f"Download completed for {self.settings.instance_name}.", LogLevel.INFO)

    def create_shortcut(self, shortcut_path: str) -> None:
        """
        Creates a shortcut for the `RainbowSix` executable file with the `shortcut_path` specified.
        """
        rainbowsix_exe = os.path.abspath(os.path.join(self.SIEGE_DIRECTORY, "RainbowSix.exe"))
        rainbowsixgame_exe = os.path.abspath(os.path.join(self.SIEGE_DIRECTORY, "RainbowSixGame.exe"))

        if os.path.isfile(rainbowsix_exe):
            file_path = rainbowsix_exe
        elif os.path.isfile(rainbowsixgame_exe):
            file_path = rainbowsixgame_exe
        else:
            self.console.log("Executable file does not exist!")
            return

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = file_path
        shortcut.WorkingDirectory = self.SIEGE_DIRECTORY
        shortcut.IconLocation = file_path
        shortcut.Arguments = "/belaunch"
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
    
    def dump_crack(self) -> None:
        """
        Dumps the relevant `GAMENAME` and `USERNAME` onto the relevant crack file.
        """
        crack_type = SiegeVersions_CrackTypes[self.settings.version.name].value

        if crack_type == CrackType.Y1SX_Y6S2 or crack_type == CrackType.Y6S3:
            #codex dump
            codex = os.path.abspath(os.path.join(self.SIEGE_DIRECTORY, "CODEX.ini"))
            config = configparser.ConfigParser()
            config.read(codex)
            config['Settings']['GameName'] = f"{self.settings.version.value}_{self.settings.version.name}"
            with open(codex, "w") as config_file:
                config.write(config_file)

            #cplay dump
            cplay = os.path.abspath(os.path.join(self.SIEGE_DIRECTORY, "CPlay.ini"))
            config = configparser.ConfigParser()
            config.read(cplay)
            config['Uplay']['Username'] = self.settings.username
            with open(cplay, "w") as config_file:
                config.write(config_file)
        else:
            #uplay_r2 dump
            uplay_r2 = os.path.abspath(os.path.join(self.SIEGE_DIRECTORY, "uplay_r2.ini"))
            config = configparser.ConfigParser()
            config.read(uplay_r2)
            config['Settings']['Username'] = self.settings.username
            with open(uplay_r2, "w") as config_file:
                config.write(config_file)