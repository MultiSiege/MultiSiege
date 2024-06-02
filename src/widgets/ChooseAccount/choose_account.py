import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
sys.path.append('src/widgets')
from ChooseAccount.UI.choose_account_window import Ui_choose_account
from AddSteamAccount.add_steam_account import AddSteamAccountWindow

from settings import *
from models import *

class AccountsModel(qtg.QStandardItemModel):
    def __init__(self, accounts: list[AccountModel]) -> None:
        super().__init__()

        self.setColumnCount(1)
        self.setHorizontalHeaderLabels(["Account name"])

        for account in accounts:
            self.add_account(account)

    def add_account(self, account: AccountModel) -> None:
        row = self.rowCount()

        item = qtg.QStandardItem()
        item.setText(account.username)
        self.setItem(row, 0, item)

class ChooseAccountWindow(qtw.QDialog, Ui_choose_account):
    account_selected = qtc.Signal(int, bool)
    one_time_account_created = qtc.Signal(str, str, bool)
    def __init__(self, parent: qtw.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.pb_accept.setEnabled(False)

        self.add_steam_account_dialog = AddSteamAccountWindow(self)
        self.pb_reject.clicked.connect(self.reject)

        self.pb_one_time_account.clicked.connect(self.add_steam_account_dialog.exec)
        self.tv_accounts.pressed.connect(self.handle_accept_button)

        self.add_steam_account_dialog.account_created.connect(self.handle_one_time_account)
        self.pb_accept.clicked.connect(self.handle_account)

    @qtc.Slot()
    def handle_account(self) -> None:
        self.account_selected.emit(self.tv_accounts.currentIndex().row(), self.cb_SKU_RUS.isChecked())
        self.accept()

    @qtc.Slot(str, str)
    def handle_one_time_account(self, account_name: str, password: str) -> None:
        self.one_time_account_created.emit(account_name, password, self.cb_SKU_RUS.isChecked())
        self.accept()

    @qtc.Slot()
    def handle_accept_button(self) -> None:
        if self.tv_accounts.currentIndex().row() != -1:
            self.pb_accept.setEnabled(True)

    def exec(self, accounts: list[AccountModel]) -> int:
        self.accounts_model = AccountsModel(accounts)
        self.tv_accounts.setModel(self.accounts_model)
        self.pb_accept.setEnabled(False)

        self.setFocus()

        return super().exec()

