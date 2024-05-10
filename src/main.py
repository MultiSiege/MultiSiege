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
from instance import Instance
from widgets import *

class MultiSiege(qtc.QObject):
    def __init__(self) -> None:
        self.global_settings = GlobalSettings()
        self.instances: Dict[str, Instance] = {}

        self.setup_instances()
        self.setup_ui()

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

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    multi_siege = MultiSiege()

    sys.exit(app.exec())

