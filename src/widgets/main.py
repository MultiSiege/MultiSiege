import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from Main.UI.main_window import Ui_MainWindow
from NewInstance.new_instance import NewInstance
from GlobalSettings.global_settings import GlobalSettingsWindow

sys.path.append('src')
from settings import GlobalSettings

class MainWindow(qtw.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_add_instance.clicked.connect(self.open_new_instance_window)
        self.pb_settings.clicked.connect(lambda: self.open_global_settings_window(GlobalSettings(), 0))
        self.pb_accounts.clicked.connect(lambda: self.open_global_settings_window(GlobalSettings(), 1))

    @qtc.Slot()
    def open_new_instance_window(self) -> None:
        self.new_instance_dialog = NewInstance()
        self.new_instance_dialog.show()

    @qtc.Slot()
    def open_global_settings_window(self, settings: GlobalSettings, index: int) -> None:
        self.global_settings_dialog = GlobalSettingsWindow(settings, index)
        self.global_settings_dialog.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())