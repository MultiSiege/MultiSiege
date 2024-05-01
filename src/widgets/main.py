import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from Main.UI.main_window import Ui_MainWindow
from NewInstance.new_instance import NewInstance

class MainWindow(qtw.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_add_instance.clicked.connect(self.open_new_instance_window)

    @qtc.Slot()
    def open_new_instance_window(self) -> None:
        self.new_instance_dialog = NewInstance()
        self.new_instance_dialog.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())