# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shortcut_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
from . import icons_rc

class Ui_Create_Shortcut(object):
    def setupUi(self, Create_Shortcut):
        if not Create_Shortcut.objectName():
            Create_Shortcut.setObjectName(u"Create_Shortcut")
        Create_Shortcut.resize(400, 72)
        icon = QIcon()
        icon.addFile(u":/main_widget_logo/logo-TB.png", QSize(), QIcon.Normal, QIcon.Off)
        Create_Shortcut.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Create_Shortcut)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Create_Shortcut)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.le_shortcut_path = QLineEdit(Create_Shortcut)
        self.le_shortcut_path.setObjectName(u"le_shortcut_path")
        self.le_shortcut_path.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout.addWidget(self.le_shortcut_path, 0, 1, 1, 1)

        self.pb_shortcut_path_folder = QPushButton(Create_Shortcut)
        self.pb_shortcut_path_folder.setObjectName(u"pb_shortcut_path_folder")
        self.pb_shortcut_path_folder.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout.addWidget(self.pb_shortcut_path_folder, 0, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(Create_Shortcut)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 3)


        self.retranslateUi(Create_Shortcut)
        self.buttonBox.accepted.connect(Create_Shortcut.accept)
        self.buttonBox.rejected.connect(Create_Shortcut.reject)

        QMetaObject.connectSlotsByName(Create_Shortcut)
    # setupUi

    def retranslateUi(self, Create_Shortcut):
        Create_Shortcut.setWindowTitle(QCoreApplication.translate("Create_Shortcut", u"Create Shortcut - MultiSiege", None))
        self.label.setText(QCoreApplication.translate("Create_Shortcut", u"Shortcut Path:", None))
        self.pb_shortcut_path_folder.setText(QCoreApplication.translate("Create_Shortcut", u"...", None))
    # retranslateUi

