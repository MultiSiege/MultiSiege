import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
sys.path.append('src/widgets')
sys.path.append('src')
from InstanceSettings.UI.instance_settings_window import Ui_instance_settings
from settings import InstanceSettings
from constants import SiegeVersions

class InstanceSettingsWindow(qtw.QDialog, Ui_instance_settings):
    set_settings = qtc.Signal(str, str, int)
    def __init__(self, parent: qtw.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        for version in list(SiegeVersions):
            label = version.name

            label_list = label.split("_")

            new_label = ""

            for label in label_list:
                new_label += label[0].upper() + label[1:].lower() + " "

            self.cb_version.addItem("")
            self.cb_version.setItemText(self.cb_version.count() - 1, new_label[:-1])

        self.accepted.connect(lambda: self.set_settings.emit(self.le_instance_name.text(), self.le_username.text(), self.cb_version.currentIndex()))

    def exec(self, settings: InstanceSettings) -> int:
        self.le_instance_name.setText(settings.instance_name)
        self.le_username.setText(settings.username)
        self.cb_version.setCurrentIndex(list(SiegeVersions).index(settings.version))

        self.setWindowTitle(f" Instance settings for {settings.instance_name} - MultiSiege")
        self.setFocus()

        return super().exec()
        

