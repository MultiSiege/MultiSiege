import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
sys.path.append('src/widgets')
from Main.UI.main_window import Ui_MainWindow
from NewInstance.new_instance import NewInstance
from GlobalSettings.global_settings import GlobalSettingsWindow
from Help.help import HelpWindow

class MainWindow(qtw.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.new_instance_dialog = NewInstance(self)
        self.global_settings_dialog = GlobalSettingsWindow(self)
        self.help_dialog = HelpWindow(self)

        self.pb_add_instance.clicked.connect(self.open_new_instance_window)
        self.pb_settings.clicked.connect(lambda: self.open_global_settings_window(0))
        self.pb_accounts.clicked.connect(lambda: self.open_global_settings_window(1))
        self.pb_help.clicked.connect(self.open_help_window)

    @qtc.Slot()
    def open_new_instance_window(self) -> None:
        self.new_instance_dialog.exec()

    @qtc.Slot()
    def open_global_settings_window(self, page: int) -> None:
        self.global_settings_dialog.exec(index=page)

    @qtc.Slot()
    def open_help_window(self) -> None:
        self.help_dialog.exec()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())