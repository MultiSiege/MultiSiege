import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from NewInstance.UI.new_instance_window import Ui_NewInstance

sys.path.append('src') #python can't usually find the constants module, so we have to manually append it to our path
from constants import *

class SeasonsModel(qtg.QStandardItemModel):
    def __init__(self):
        super().__init__()

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["Name", "Version", "Liberator Supported"])

        for row, version in enumerate(list(SiegeVersions)):
            for column in range(3):
                item = qtg.QStandardItem()

                if column == 0:
                    item.setText(self.format_season_label(version.name))
                elif column == 1:
                    item.setText(version.value)
                elif column == 2:
                    if int(version.value[1]) < 5: #arbitrary values that are gonna be used once, no need for constants (unless liberator gets updated, which is never happening)
                        item.setText("Yes")
                    else:
                        item.setText("No")
                
                self.setItem(row, column, item)

    def format_season_label(self, label: str) -> str:
        label_list = label.split("_")

        new_label = ""

        for label in label_list:
            new_label += label[0].upper() + label[1:].lower() + " "

        return new_label[:-1]
    
class YearFilterModel(qtc.QSortFilterProxyModel):
    def __init__(self, parent: qtc.QObject | None = ...) -> None:
        super().__init__(parent)

        self.regular_expression = []

    def dump_regex(self) -> str:
        """
        Dumps and returns the regex as a string.
        """
        if len(self.regular_expression) == 0: return ""

        regex = "Y("

        for index, reg in enumerate(self.regular_expression):
            if index == len(self.regular_expression) - 1:
                regex += reg

            else:
                regex += reg + "|"

        return regex + ")"

    def add_to_regex(self, regex: str) -> str:
        """
        Adds the given string to the regular expression to sort custom filtering and returns it.
        """
        self.regular_expression.append(regex)
        return self.dump_regex()
    
    def remove_from_regex(self, regex: str) -> str:
        """
        Removes the regular expression from the list and returns it
        """
        self.regular_expression.remove(regex)
        return self.dump_regex()
    
class NewInstance(qtw.QDialog, Ui_NewInstance):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #setting up the layered model for filtering
        self.base_model = SeasonsModel()
        self.year_model = YearFilterModel(self)
        self.year_model.setFilterKeyColumn(1)
        self.proxy_model = qtc.QSortFilterProxyModel(self)
        self.proxy_model.setFilterKeyColumn(2)
        self.year_model.setSourceModel(self.base_model)
        self.proxy_model.setSourceModel(self.year_model)
        self.treeView_seasons.setModel(self.proxy_model)

        #handling signals and calling slots
        self.filter_liberator.clicked.connect(self.apply_liberator_filter)
        self.filter_year1.clicked.connect(lambda: self.apply_year_filter(self.filter_year1, 1))
        self.filter_year2.clicked.connect(lambda: self.apply_year_filter(self.filter_year2, 2))
        self.filter_year3.clicked.connect(lambda: self.apply_year_filter(self.filter_year3, 3))
        self.filter_year4.clicked.connect(lambda: self.apply_year_filter(self.filter_year4, 4))
        self.filter_year5.clicked.connect(lambda: self.apply_year_filter(self.filter_year5, 5))
        self.filter_year6.clicked.connect(lambda: self.apply_year_filter(self.filter_year6, 6))

        #making sure that they cannot resize the sections
        self.treeView_seasons.header().setSectionResizeMode(0, qtw.QHeaderView.ResizeMode.Fixed)
        self.treeView_seasons.header().setSectionResizeMode(1, qtw.QHeaderView.ResizeMode.Fixed)
        self.treeView_seasons.header().setSectionResizeMode(2, qtw.QHeaderView.ResizeMode.Fixed)

    #=======#
    #FILTERS#
    #=======#

    @qtc.Slot()
    def apply_liberator_filter(self):
        if self.filter_liberator.isChecked():
            self.proxy_model.setFilterRegularExpression("Yes")
        else:
            self.proxy_model.setFilterRegularExpression("")

    @qtc.Slot()
    def apply_year_filter(self, year_checkbox: qtw.QCheckBox, year: int) -> None:
        if year_checkbox.isChecked():
            self.year_model.setFilterRegularExpression(self.year_model.add_to_regex(str(year)))
        else:
            self.year_model.setFilterRegularExpression(self.year_model.remove_from_regex(str(year)))

    #====================#
    #CREATING NEW INSTANCE
    #====================#
        

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = NewInstance()
    window.show()

    sys.exit(app.exec())
    
