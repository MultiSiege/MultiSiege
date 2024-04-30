# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_instance_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QFormLayout, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QTreeView, QWidget)
from . import icons_rc

class Ui_NewInstance(object):
    def setupUi(self, NewInstance):
        if not NewInstance.objectName():
            NewInstance.setObjectName(u"NewInstance")
        NewInstance.resize(635, 419)
        NewInstance.setMinimumSize(QSize(635, 419))
        icon = QIcon()
        icon.addFile(u":/top_nav_bar/magic-wand-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        NewInstance.setWindowIcon(icon)
        self.gridLayout = QGridLayout(NewInstance)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox_bottom = QDialogButtonBox(NewInstance)
        self.buttonBox_bottom.setObjectName(u"buttonBox_bottom")
        self.buttonBox_bottom.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox_bottom.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox_bottom, 3, 0, 1, 1)

        self.line = QFrame(NewInstance)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.frame = QFrame(NewInstance)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_instance_name = QLabel(self.frame)
        self.label_instance_name.setObjectName(u"label_instance_name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_instance_name)

        self.lineEdit_instance_name = QLineEdit(self.frame)
        self.lineEdit_instance_name.setObjectName(u"lineEdit_instance_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_instance_name)

        self.label_username = QLabel(self.frame)
        self.label_username.setObjectName(u"label_username")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_username)

        self.lineEdit_username = QLineEdit(self.frame)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_username)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(NewInstance)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.filter_year2 = QCheckBox(self.widget)
        self.filter_year2.setObjectName(u"filter_year2")

        self.gridLayout_3.addWidget(self.filter_year2, 5, 1, 1, 1)

        self.filter_year7 = QCheckBox(self.widget)
        self.filter_year7.setObjectName(u"filter_year7")

        self.gridLayout_3.addWidget(self.filter_year7, 10, 1, 1, 1)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 11, 1, 1, 1)

        self.label_filters = QLabel(self.widget)
        self.label_filters.setObjectName(u"label_filters")
        self.label_filters.setTextFormat(Qt.TextFormat.PlainText)
        self.label_filters.setScaledContents(False)
        self.label_filters.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_filters, 0, 1, 1, 2)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 3, 1, 1, 1)

        self.filter_year6 = QCheckBox(self.widget)
        self.filter_year6.setObjectName(u"filter_year6")

        self.gridLayout_3.addWidget(self.filter_year6, 9, 1, 1, 1)

        self.filter_year5 = QCheckBox(self.widget)
        self.filter_year5.setObjectName(u"filter_year5")

        self.gridLayout_3.addWidget(self.filter_year5, 8, 1, 1, 1)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 12, 1, 1, 1)

        self.filter_year4 = QCheckBox(self.widget)
        self.filter_year4.setObjectName(u"filter_year4")

        self.gridLayout_3.addWidget(self.filter_year4, 7, 1, 1, 1)

        self.filter_year3 = QCheckBox(self.widget)
        self.filter_year3.setObjectName(u"filter_year3")

        self.gridLayout_3.addWidget(self.filter_year3, 6, 1, 1, 1)

        self.filter_liberator = QCheckBox(self.widget)
        self.filter_liberator.setObjectName(u"filter_liberator")

        self.gridLayout_3.addWidget(self.filter_liberator, 2, 1, 1, 1)

        self.filter_year1 = QCheckBox(self.widget)
        self.filter_year1.setObjectName(u"filter_year1")

        self.gridLayout_3.addWidget(self.filter_year1, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)

        self.season_widget = QWidget(self.frame_2)
        self.season_widget.setObjectName(u"season_widget")
        self.gridLayout_4 = QGridLayout(self.season_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.treeView_seasons = QTreeView(self.season_widget)
        self.treeView_seasons.setObjectName(u"treeView_seasons")
        self.treeView_seasons.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.treeView_seasons.setAlternatingRowColors(True)
        self.treeView_seasons.setItemsExpandable(False)
        self.treeView_seasons.setWordWrap(False)
        self.treeView_seasons.header().setHighlightSections(True)
        self.treeView_seasons.header().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.treeView_seasons, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.season_widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)


        self.retranslateUi(NewInstance)
        self.buttonBox_bottom.accepted.connect(NewInstance.accept)
        self.buttonBox_bottom.rejected.connect(NewInstance.reject)

        QMetaObject.connectSlotsByName(NewInstance)
    # setupUi

    def retranslateUi(self, NewInstance):
        NewInstance.setWindowTitle(QCoreApplication.translate("NewInstance", u"New Instance - MultiSiege", None))
        self.label_instance_name.setText(QCoreApplication.translate("NewInstance", u"Instance name:", None))
        self.label_username.setText(QCoreApplication.translate("NewInstance", u"Username:", None))
        self.lineEdit_username.setText("")
        self.filter_year2.setText(QCoreApplication.translate("NewInstance", u"Year 2", None))
        self.filter_year7.setText(QCoreApplication.translate("NewInstance", u"Year 7", None))
        self.label_filters.setText(QCoreApplication.translate("NewInstance", u"Filters", None))
        self.filter_year6.setText(QCoreApplication.translate("NewInstance", u"Year 6", None))
        self.filter_year5.setText(QCoreApplication.translate("NewInstance", u"Year 5", None))
        self.filter_year4.setText(QCoreApplication.translate("NewInstance", u"Year 4", None))
        self.filter_year3.setText(QCoreApplication.translate("NewInstance", u"Year 3", None))
        self.filter_liberator.setText(QCoreApplication.translate("NewInstance", u"Liberator Supported", None))
        self.filter_year1.setText(QCoreApplication.translate("NewInstance", u"Year 1", None))
    # retranslateUi

