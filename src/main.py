from settings import *
from constants import *
import logger
import os
import sys
import subprocess
import qdarkstyle
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from typing import Dict
from copy import deepcopy
from instance import Instance
from widgets import *

os.environ['QT_API'] = 'pyside'

class MultiSiege:
    def __init__(self) -> None:
        self.app = qtw.QApplication(sys.argv)

        self.use_system_style = self.app.styleSheet()
        self.dark_style = qdarkstyle.load_stylesheet_pyside6()
        self.light_style = qdarkstyle.load_stylesheet(palette=qdarkstyle.LightPalette, qt_api='pyside6')

        self.global_settings = GlobalSettings()
        self.instances: list[Instance] = []

        self.setup_ui()
        self.setup_instances()

        #slot handling
        self.ui.pb_instance_folder.clicked.connect(self.open_instance_folder)
        self.ui.pb_siege_folder.clicked.connect(self.open_siege_folder)

        self.ui.global_settings_dialog.get_settings.connect(self.get_global_settings)
        self.ui.global_settings_dialog.set_settings.connect(self.set_global_settings)

        self.ui.new_instance_dialog.accepted.connect(self.add_instance)

        self.ui.pb_delete.clicked.connect(self.open_delete_window)
        self.ui.delete_dialog.delete_confirmed.connect(self.delete_instance)

        self.ui.pb_create_shortcut.clicked.connect(self.open_create_shortcut_window)
        self.ui.create_shortcut_dialog.accepted.connect(self.create_shortcut)

        self.ui.pb_instance_settings.clicked.connect(self.open_instance_settings_window)
        self.ui.instance_settings_dialog.set_settings.connect(self.set_instance_settings)

        self.ui.pb_download.clicked.connect(self.open_choose_account_window)
        self.ui.choose_account_dialog.account_selected.connect(self.handle_download)
        self.ui.choose_account_dialog.one_time_account_created.connect(self.handle_download_one_time_account)

        self.ui.pb_launch.clicked.connect(self.open_current_instance)

        self.ui.pb_folders.clicked.connect(self.open_multisiege_folder)

    #=============#
    #SETUP METHODS#
    #=============#
        
    def setup_instances(self):
        """
        Iterates through the set instances folder specified in `global_settings.json` and adds it as an `Instance` object to the list.
        """
        if not os.path.isdir(self.global_settings.features.instances_folder): os.mkdir(self.global_settings.features.instances_folder)

        self.refresh_instances()

    def setup_ui(self) -> None:
        """
        Initialises `PySide6` UI elements with the `MainWindow`. All other widgets are composed in `MainWindow`.
        """
        self.ui = MainWindow()
        self.set_mode()
        self.ui.show()

    def set_mode(self) -> None:
        """
        Sets the theme/mode the application is in.
        """
        if self.global_settings.features.mode == Mode.DARK:
            self.app.setStyleSheet(self.dark_style)
        elif self.global_settings.features.mode == Mode.LIGHT:
            self.app.setStyleSheet(self.light_style)
        elif self.global_settings.features.mode == Mode.USE_SYSTEM_SETTING:
            self.app.setStyleSheet(self.use_system_style)

    #=====#
    #SLOTS#
    #=====#
    
    @qtc.Slot()
    def open_instance_folder(self) -> None:
        current_instance = self.instances[self.ui.current_widget.index]
        current_instance.open_instance_folder()

    @qtc.Slot()
    def open_siege_folder(self) -> None:
        current_instance = self.instances[self.ui.current_widget.index]
        current_instance.open_siege_folder()

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

        #set settings
        self.set_mode()
        self.refresh_instances()

    @qtc.Slot()
    def add_instance(self) -> None:
        """
        Dumps relevant metadata and adds a new `Instance` object to the list.
        """
        instance_name, username, version = self.ui.new_instance_dialog.dump_metadata()

        instance_directory = os.path.join(self.global_settings.features.instances_folder, instance_name)

        #if we have clashing folder names keep on adding numbers until we have a unique folder name that won't override the old instance
        count = 1
        while os.path.isdir(instance_directory):
            instance_directory = os.path.join(self.global_settings.features.instances_folder, instance_name + str(count))
            count += 1

        new_instance = Instance(instance_directory,
                                False, 
                                instance_name=instance_name,
                                username=username,
                                version=version)
        
        self.instances.append(new_instance)
        self.sort_instances()

        self.ui.add_instance_widget(new_instance, True)

    @qtc.Slot()
    def open_delete_window(self) -> None:
        current_instance = self.instances[self.ui.current_widget.index]
        self.ui.delete_dialog.exec(current_instance.settings.instance_name)

    @qtc.Slot()
    def delete_instance(self) -> None:
        current_instance = self.instances[self.ui.current_widget.index]

        current_instance.delete()
        self.refresh_instances()

    @qtc.Slot()
    def open_create_shortcut_window(self) -> None:
        current_instance = self.instances[self.ui.current_widget.index]
        self.ui.create_shortcut_dialog.exec(current_instance.settings.instance_name)

    @qtc.Slot()
    def create_shortcut(self) -> None:
        current_instance = self.instances[self.ui.current_widget.index]

        shortcut_path = self.ui.create_shortcut_dialog.le_shortcut_path.text()

        if not shortcut_path.endswith(".lnk"):
            return logger.log("Attempted to create shortcut that doesn't end in .lnk", LogLevel.WARNING)
        
        try:
            current_instance.create_shortcut(self.ui.create_shortcut_dialog.le_shortcut_path.text())
        except Exception as e:
            print(e)
            logger.log("Could not create shortcut with path specified.", LogLevel.ERROR)
            self.throw_error("Could not create shortcut with path specified.")

    @qtc.Slot()
    def open_instance_settings_window(self) -> None:
        current_instance = self.instances[self.ui.current_widget.index]

        self.ui.instance_settings_dialog.exec(current_instance.settings)

    @qtc.Slot()
    def open_choose_account_window(self) -> None:
        self.ui.choose_account_dialog.exec(self.global_settings.accounts)

    @qtc.Slot(str, str, int)
    def set_instance_settings(self, instance_name: str, username: str, version_index: int) -> None:
        current_instance = self.instances[self.ui.current_widget.index]

        if instance_name != "":
            current_instance.settings.set_instance_name(instance_name)
        if username != "":
            current_instance.settings.set_username(username)

        current_instance.settings.set_version(list(SiegeVersions)[version_index])

        current_instance.settings.dump_settings()
        self.refresh_instances()

    @qtc.Slot(int, bool)
    def handle_download(self, account_index: int, sku_rus: bool) -> None:
        current_instance = self.instances[self.ui.current_widget.index]
        account = self.global_settings.accounts[account_index]

        current_instance.download(account.username, account.password, sku_rus)

    @qtc.Slot(str, str, bool)
    def handle_download_one_time_account(self, account_name: str, password: str, sku_rus: bool) -> None:
        current_instance = self.instances[self.ui.current_widget.index]

        current_instance.download(account_name, password, sku_rus)

    @qtc.Slot()
    def open_current_instance(self) -> None:
        current_instance = self.instances[self.ui.current_widget.index]

        if self.process_exists("RainbowSix.exe") or self.process_exists("RainbowSixGame.exe"):
            self.throw_error("RainbowSix or RainbowSixGame process is already running. If you don't have it open check background processes in Task Manager or expand the MultiSiege process.")
            return
        
        current_instance.launch()

    @qtc.Slot()
    def open_multisiege_folder(self) -> None:
        subprocess.call(f"explorer {os.path.abspath(os.getcwd())}")

    #==============#
    #HELPER METHODS#
    #==============#

    def sort_instances(self) -> None:
        self.instances.sort(key=lambda instance: instance.settings.instance_name.upper())# unicode char codes means that capitals go before lowercase letters

    def refresh_instances(self) -> None:
        """
        Forces a refresh of the instances, in case the instance directory gets changed.
        """
        if not os.path.isdir(self.global_settings.features.instances_folder): self.ui.clear_instance_widgets() # if the folder specified doesn't exist just show a blank screen.

        self.instances: list[Instance] = []

        for folder in os.listdir(self.global_settings.features.instances_folder):
            folder = os.path.join(self.global_settings.features.instances_folder, folder)
            if not os.path.isdir(folder):
                logger.log("File found in top level directory of instances folder.", LogLevel.WARNING)
            else:
                self.instances.append(Instance(folder, True))

        self.sort_instances()

        self.ui.clear_instance_widgets()        
        for instance in self.instances:
            self.ui.add_instance_widget(instance)

    def throw_error(self, error_message: str) -> None:
        """
        Throw an error to be displayed in the UI.
        """
        self.ui.error_dialog.exec(error_message)

    def process_exists(self, process_name):
        progs = str(subprocess.check_output('tasklist'))
        if process_name in progs:
            return True
        else:
            return False

if __name__ == "__main__":
    multi_siege = MultiSiege()

    sys.exit(multi_siege.app.exec())

