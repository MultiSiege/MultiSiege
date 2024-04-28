import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from UI.new_instance_window import Ui_NewInstance

class NewInstance(qtw.QDialog, Ui_NewInstance):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        model = qtg.QStandardItemModel()
        model.setColumnCount(4)
        model.setVerticalHeaderLabels(["Name", "Version", "Released", "Liberator Supported"])
        parentItem = model.invisibleRootItem()
        for i in range(0, 4):
            item = qtg.QStandardItem()
            item.setText("hello")
            parentItem.appendColumn([item, item, item, item])

        self.treeView_seasons.setModel(model)

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
    
