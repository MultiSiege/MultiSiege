import sys
import os
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from CreateShortcut.UI.shortcut_window import Ui_Create_Shortcut

class CreateShortcutWindow(qtw.QDialog, Ui_Create_Shortcut):
    def __init__(self, parent: qtw.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.file_dialog = qtw.QFileDialog(self)
        self.file_dialog.setFileMode(qtw.QFileDialog.FileMode.AnyFile)
        self.file_dialog.setWindowTitle("Select shortcut path - MultiSiege")
        self.file_dialog.setDirectory(os.path.abspath(os.path.expanduser("~/Desktop")))

        self.pb_shortcut_path_folder.clicked.connect(self.handle_file_dialog)

    @qtc.Slot()
    def handle_file_dialog(self) -> None:
        self.file_dialog.selectFile(self.filename)

        if self.file_dialog.exec():
            file_path = os.path.abspath(self.file_dialog.selectedFiles()[0])

            if not os.path.exists(file_path):
                if not file_path.endswith(".lnk"):
                    self.le_shortcut_path.setText(file_path + ".lnk")
                else:
                    self.le_shortcut_path.setText(file_path)

    def exec(self, instance_name: str) -> int:
        self.le_shortcut_path.setText("")
        self.setFocus()
        self.filename = f"{instance_name} - MultiSiege.lnk"
        return super().exec()