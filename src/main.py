from settings import *
from constants import *
import logger
import os
import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from typing import Dict
from copy import deepcopy
from instance import Instance
from widgets import *

class MultiSiege:
    def __init__(self) -> None:
        self.global_settings = GlobalSettings()
        self.instances: Dict[str, Instance] = {}

        self.setup_instances()
        self.setup_ui()

        #slot handling
        self.ui.global_settings_dialog.get_settings.connect(self.get_global_settings)
        self.ui.global_settings_dialog.set_settings.connect(self.set_global_settings)

    #=============#
    #SETUP METHODS#
    #=============#
        
    def setup_instances(self):
        """
        Iterates through the set instances folder specified in `global_settings.json` and adds it as an `Instance` object to the dictionary for fast lookup.
        """
        if not os.path.isdir(self.global_settings.features.instances_folder): os.mkdir(self.global_settings.features.instances_folder)

        for folder in os.listdir(self.global_settings.features.instances_folder):
            if not os.path.isdir(folder):
                os.remove(folder)
                logger.log("File found in top level directory of instances folder, deleting file.", LogLevel.WARNING)
            else:
                self.instances[os.path.basename(folder)] = Instance(folder, True)

    def setup_ui(self) -> None:
        """
        Initialises `PySide6` UI elements with the `MainWindow`. All other widgets are composed in `MainWindow`.
        """
        self.ui = MainWindow()
        self.ui.show()

    #=====#
    #SLOTS#
    #=====#
    @qtc.Slot()
    def get_global_settings(self) -> None:
        """
        Sets the global settings object as an attribute of our global settings dialog.
        """
        #need to make a deepcopy otherwise will point to the same reference in memory, making it not an isolated sandbox
        self.ui.global_settings_dialog.settings = deepcopy(self.global_settings)

    @qtc.Slot()
    def set_global_settings(self) -> None:
        """
        Override the global_settings object with the one from our global settings dialog if the user has accepted the changes.
        """
        self.global_settings = self.ui.global_settings_dialog.settings
        self.global_settings.dump_settings()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    multi_siege = MultiSiege()

    sys.exit(app.exec())

