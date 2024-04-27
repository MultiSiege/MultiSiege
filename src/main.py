import sys

from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)

from windows.main_window import Ui_MainWindow

class MainWindow(qtw.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())