from settings import *
import logger
import os
from PySide6 import QtCore as qtc

class MultiSiege(qtc.QObject):
    def __init__(self) -> None:
        self.global_settings = GlobalSettings()
        
    def load_instances_folder(self):
        pass
        


