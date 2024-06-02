# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_steam_account_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
from . import icons_rc

class Ui_dialog_add_steam_account(object):
    def setupUi(self, dialog_add_steam_account):
        if not dialog_add_steam_account.objectName():
            dialog_add_steam_account.setObjectName(u"dialog_add_steam_account")
        dialog_add_steam_account.resize(410, 175)
        dialog_add_steam_account.setMinimumSize(QSize(410, 175))
        icon = QIcon()
        icon.addFile(u":/top_nav_bar/Steam_icon_logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        dialog_add_steam_account.setWindowIcon(icon)
        self.gridLayout = QGridLayout(dialog_add_steam_account)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.pb_accept = QPushButton(dialog_add_steam_account)
        self.pb_accept.setObjectName(u"pb_accept")

        self.gridLayout.addWidget(self.pb_accept, 1, 1, 1, 1)

        self.pb_reject = QPushButton(dialog_add_steam_account)
        self.pb_reject.setObjectName(u"pb_reject")

        self.gridLayout.addWidget(self.pb_reject, 1, 2, 1, 1)

        self.frame = QFrame(dialog_add_steam_account)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.le_account_name = QLineEdit(self.frame)
        self.le_account_name.setObjectName(u"le_account_name")
        self.le_account_name.setEchoMode(QLineEdit.EchoMode.Normal)

        self.gridLayout_2.addWidget(self.le_account_name, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.le_password = QLineEdit(self.frame)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_2.addWidget(self.le_password, 3, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)


        self.retranslateUi(dialog_add_steam_account)

        self.pb_accept.setDefault(True)


        QMetaObject.connectSlotsByName(dialog_add_steam_account)
    # setupUi

    def retranslateUi(self, dialog_add_steam_account):
        dialog_add_steam_account.setWindowTitle(QCoreApplication.translate("dialog_add_steam_account", u"Add Steam Account - MultiSiege", None))
        self.pb_accept.setText(QCoreApplication.translate("dialog_add_steam_account", u"OK", None))
        self.pb_reject.setText(QCoreApplication.translate("dialog_add_steam_account", u"Cancel", None))
        self.label_2.setText(QCoreApplication.translate("dialog_add_steam_account", u"Account name: ", None))
        self.le_account_name.setInputMask("")
        self.label_3.setText(QCoreApplication.translate("dialog_add_steam_account", u"Password:", None))
        self.label.setText(QCoreApplication.translate("dialog_add_steam_account", u"Enter your account name and password to add a new Steam account.", None))
        self.label_4.setText(QCoreApplication.translate("dialog_add_steam_account", u"Note: This does not verify Steam account credentials.", None))
    # retranslateUi

