import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from UI.new_instance_window import Ui_NewInstance

class SeasonsModel(qtg.QStandardItemModel):
    def __init__(self):
        super().__init__()

        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["Name", "Version", "Released", "Liberator Supported"])

        for i in range(0, 4):
            item = qtg.QStandardItem()
            item.setText("hello")
            self.setItem(0, i, item)

class NewInstance(qtw.QDialog, Ui_NewInstance):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = SeasonsModel()

        self.treeView_seasons.setModel(self.model)

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
    
