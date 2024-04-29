import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from UI.new_instance_window import Ui_NewInstance

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

class NewInstance(qtw.QDialog, Ui_NewInstance):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.base_model = SeasonsModel()
        self.treeView_seasons.setModel(self.base_model)

        self.filter_liberator.clicked.connect(self.apply_liberator_filter)

    #=======#
    #FILTERS#
    #=======#

    @qtc.Slot()
    def apply_liberator_filter(self):
        print("hi")
            

        

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = NewInstance()
    window.show()

    sys.exit(app.exec())
    
