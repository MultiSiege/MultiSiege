import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from GlobalSettings.UI.global_settings_window import Ui_dialog_global_settings

sys.path.append('src')
from models import *
from settings import *

class AccountsModel(qtg.QStandardItemModel):
    def __init__(self, accounts: list[AccountModel]) -> None:
        super().__init__()

        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Account name", "Region"])

        for account in accounts:
            self.add_account(account)

    def add_account(self, account: AccountModel) -> None:
        row = self.rowCount()

        for column in range(2):
            item = qtg.QStandardItem()
            if column == 0:
                item.setText(account.username)
            else:
                item.setText(account.region)

            self.setItem(row, column, item)

class GlobalSettingsWindow(qtw.QDialog, Ui_dialog_global_settings):
    """
    Isolated sandbox for modifying settings, will only emit a signal for the updated settings once the user has pressed `OK`.

    Once the user has pressed `OK`, it will emit a callback signal with the new `GlobalSettings` object.
    """
    def __init__(self, settings: GlobalSettings, index: int) -> None:
        super().__init__()
        self.setupUi(self)

        self.settings = settings

        self.dialog = qtw.QFileDialog(self)
        self.dialog.setFileMode(qtw.QFileDialog.FileMode.Directory)

        self.setup_features()
        self.setup_accounts()

        #make sure the current index in the list is always selected as the inputted item
        self.stackedWidget.setCurrentIndex(index)
        self.listwidget_page_selector.setCurrentRow(index)

        #slot handling
        self.listwidget_page_selector.itemPressed.connect(self.set_page)

        self.treeView.pressed.connect(self.set_remove_enabled)
        self.pb_remove_account.clicked.connect(self.remove_selected_account)

        self.pb_instances_file_dialog.clicked.connect(lambda: self.handle_folder_dialog("Instances Folder", self.le_instances))
        self.pb_mods_file_dialog.clicked.connect(lambda: self.handle_folder_dialog("Mods Folder", self.le_mods))

    #=============#
    #SETUP METHODS#
    #=============#

    def setup_features(self) -> None:
        #check for update on start
        if self.settings.features.check_for_update_on_start:
            self.cb_update_on_start.setChecked(True)
        else:
            self.cb_update_on_start.setChecked(False)

        #folders
        self.le_instances.setText(os.path.relpath(self.settings.features.instances_folder))
        self.le_mods.setText(os.path.relpath(self.settings.features.mods_folder))

        #mode
        if self.settings.features.mode == Mode.USE_SYSTEM_SETTING: self.cb_mode.setCurrentIndex(0)
        elif self.settings.features.mode == Mode.LIGHT: self.cb_mode.setCurrentIndex(1)
        elif self.settings.features.mode == Mode.DARK: self.cb_mode.setCurrentIndex(2)

    def setup_accounts(self) -> None:
        self.accounts_model = AccountsModel(self.settings.accounts)
        self.treeView.setModel(self.accounts_model)

        #by default no account is selected, so we can't remove an account
        self.pb_remove_account.setEnabled(False)
        
    #=====#
    #SLOTS#
    #=====#

    @qtc.Slot()
    def set_page(self) -> None:
        if self.listwidget_page_selector.currentItem().text() == "Features":
            self.stackedWidget.setCurrentIndex(0)
        elif self.listwidget_page_selector.currentItem().text() == "Accounts":
            self.stackedWidget.setCurrentIndex(1)

    @qtc.Slot()
    def handle_folder_dialog(self, title: str, line_edit: qtw.QLineEdit) -> None:
        self.dialog.setWindowTitle(title)

        if os.path.isdir(line_edit.text()):
            self.dialog.setDirectory(os.path.abspath(line_edit.text()))
        else:
            self.dialog.setDirectory(os.getcwd())

        if self.dialog.exec():
            folder = os.path.relpath(self.dialog.selectedFiles()[0])
            if folder.startswith('.'):
                line_edit.setText(os.path.abspath(folder))
            else:
                line_edit.setText(folder)

    @qtc.Slot()
    def set_remove_enabled(self) -> None:
        if self.treeView.currentIndex().row() == -1:
            self.pb_remove_account.setEnabled(False)
        else:
            self.pb_remove_account.setEnabled(True)

    @qtc.Slot()
    def remove_selected_account(self) -> None:
        if self.treeView.currentIndex().row() != -1:
            self.treeView.model().removeRow(self.treeView.selectedIndexes()[0].row())

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    global_settings = GlobalSettings()
    global_settings.set_accounts([AccountModel(username="heeheeheehaw", password="no", region="UK")])
    global_settings.dump_settings()

    window = GlobalSettingsWindow(global_settings, 1)
    window.show()

    sys.exit(app.exec())