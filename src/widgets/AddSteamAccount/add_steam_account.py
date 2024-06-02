import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
sys.path.append('src/widgets')
from AddSteamAccount.UI.add_steam_account_window import Ui_dialog_add_steam_account

class AddSteamAccountWindow(qtw.QDialog, Ui_dialog_add_steam_account):
    account_created = qtc.Signal(str, str, arguments=["account_name", "password"])
    def __init__(self, parent: qtw.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.pb_accept.clicked.connect(self.process_steam_account)
        self.pb_reject.clicked.connect(self.reject)
        self.le_account_name.textChanged.connect(self.handle_accept_button)
        self.le_password.textChanged.connect(self.handle_accept_button)

        self.pb_accept.setMinimumWidth(104)
        self.pb_reject.setMinimumWidth(104)

    @qtc.Slot()
    def handle_accept_button(self) -> None:
        if len(self.le_account_name.text()) >= 2 and len(self.le_password.text()) >= 8:
            self.pb_accept.setEnabled(True)
        else:
            self.pb_accept.setEnabled(False)

    @qtc.Slot()
    def process_steam_account(self) -> None:
        self.account_created.emit(self.le_account_name.text(), self.le_password.text())
        self.accept()

    def exec(self) -> int:
        """
        Overwrites the `exec` method to reset the window every time.
        """
        self.le_account_name.setText("")
        self.le_password.setText("")
        self.pb_accept.setEnabled(False)

        self.setFocus()
        
        return super().exec()