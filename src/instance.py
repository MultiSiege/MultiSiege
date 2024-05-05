from settings import *
from constants import *
from typing import Optional
from steamctl.commands.depot.gcmds import cmd_depot_download
import os
import logger
import subprocess
import shutil

class Instance:
    def __init__(self, instance_directory: str, load_from_file: bool, *, instance_name: Optional[str] = None, username: Optional[str] = None, version: Optional[SiegeVersions] = None) -> None:
        self.INSTANCE_DIRECTORY = instance_directory
        self.SIEGE_DIRECTORY = os.path.join(instance_directory, 'siege')
        self.SETTINGS_PATH = os.path.join(instance_directory, 'instance_settings.json')

        self.launched = False

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
        pass

    def download(self) -> None:
        pass

    def create_shortcut(self, shortcut_path: str) -> None:
        pass

    def export_instance(self) -> None:
        pass

    def delete(self) -> None:
        try:
            shutil.rmtree(self.INSTANCE_DIRECTORY)
            logger.log(f"Removed instance {self.settings.instance_name}", LogLevel.INFO)
        except:
            logger.log(f"Failed to remove instance {self.settings.instance_name}", LogLevel.ERROR)
            raise ValueError(f"Failed to remove instance {self.settings.instance_name}")
    
    def dump_codex(self) -> None:
        pass
