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

        self.add_steam_account_dialog = AddSteamAccountWindow(self)

        self.pb_accept.clicked.connect(self.accept)
        self.pb_reject.clicked.connect(self.reject)

        self.add_steam_account_dialog.account_created.connect(self.handle_one_time_account)
        self.accepted.connect(lambda: self.account_selected.emit(self.tv_accounts.currentIndex().row(), self.cb_SKU_RUS.isChecked()))

    @qtc.Slot(str, str)
    def handle_one_time_account(self, account_name: str, password: str) -> None:
        self.one_time_account_created.emit(account_name, password, self.cb_SKU_RUS.isChecked())
        self.accept()

    def exec(self, accounts: list[AccountModel]) -> int:
        self.accounts_model = AccountsModel(accounts)
        self.tv_accounts.setModel(self.accounts_model)

        return super().exec()

