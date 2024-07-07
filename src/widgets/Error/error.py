import sys
import os
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from Error.UI.error_window import Ui_error_dialog

class ErrorWindow(qtw.QDialog, Ui_error_dialog):
    def __init__(self, parent: qtw.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.pb_close.clicked.connect(self.accept)

    def exec(self, error_message: str) -> int:
        """
        Override the `QDialog` exec method to display the error message.
        """
        self.lb_error.setText(error_message)
        return super().exec()