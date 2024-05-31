import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
sys.path.append('src/widgets')
from Delete.UI.delete_window import Ui_Dialog

class DeleteWindow(qtw.QDialog, Ui_Dialog):
    delete_confirmed = qtc.Signal()
    def __init__(self, parent: qtw.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.accepted.connect(self.delete_confirmed.emit)

    def exec(self, instance_name: str) -> int:
        self.label_warning.setText(self.label_warning.text().replace("INSTANCE_NAME", instance_name))
        return super().exec()

    