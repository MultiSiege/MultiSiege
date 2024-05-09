from settings import *
from constants import *
import logger
import os
from PySide6 import QtCore as qtc
from typing import Dict
from instance import Instance

class MultiSiege(qtc.QObject):
    def __init__(self) -> None:
        self.global_settings = GlobalSettings()
        self.instances: Dict[str, Instance] = {}

        self.setup_instances()

    #=============#
    #SETUP METHODS#
    #=============#
        
    def setup_instances(self):
        """
        Iterates through the set instances folder specified in `global_settings.json` and adds it as an `Instance` object to the dictionary for fast lookup.
        """
        for folder in os.listdir(self.global_settings.features.instances_folder):
            if not os.path.isdir(folder):
                os.remove(folder)
                logger.log("File found in top level directory of instances folder, deleting file.", LogLevel.WARNING)
            else:
                self.instances[os.path.basename(folder)] = Instance(folder, True)

        
        


