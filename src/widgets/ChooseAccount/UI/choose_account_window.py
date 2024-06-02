# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose_account_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QHeaderView, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTreeView,
    QWidget)
from . import icons_rc

class Ui_choose_account(object):
    def setupUi(self, choose_account):
        if not choose_account.objectName():
            choose_account.setObjectName(u"choose_account")
        choose_account.resize(702, 339)
        icon = QIcon()
        icon.addFile(u":/top_nav_bar/Steam_icon_logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        choose_account.setWindowIcon(icon)
        self.gridLayout = QGridLayout(choose_account)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 0, 1, 1)

        self.label = QLabel(choose_account)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.pb_accept = QPushButton(choose_account)
        self.pb_accept.setObjectName(u"pb_accept")

        self.gridLayout.addWidget(self.pb_accept, 6, 1, 1, 1)

        self.pb_reject = QPushButton(choose_account)
        self.pb_reject.setObjectName(u"pb_reject")

        self.gridLayout.addWidget(self.pb_reject, 6, 2, 1, 1)

        self.scrollArea = QScrollArea(choose_account)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 670, 286))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_SKU_RUS_countries = QLabel(self.scrollAreaWidgetContents)
        self.lb_SKU_RUS_countries.setObjectName(u"lb_SKU_RUS_countries")
        self.lb_SKU_RUS_countries.setTextFormat(Qt.TextFormat.RichText)

        self.gridLayout_3.addWidget(self.lb_SKU_RUS_countries, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 5, 0, 1, 3)

        self.line_2 = QFrame(choose_account)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 3)

        self.line = QFrame(choose_account)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.cb_SKU_RUS = QCheckBox(choose_account)
        self.cb_SKU_RUS.setObjectName(u"cb_SKU_RUS")

        self.gridLayout.addWidget(self.cb_SKU_RUS, 4, 0, 1, 3)

        self.frame_accounts = QFrame(choose_account)
        self.frame_accounts.setObjectName(u"frame_accounts")
        self.frame_accounts.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_accounts.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_accounts)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tv_accounts = QTreeView(self.frame_accounts)
        self.tv_accounts.setObjectName(u"tv_accounts")

        self.gridLayout_2.addWidget(self.tv_accounts, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_accounts, 2, 0, 1, 2)

        self.pb_one_time_account = QPushButton(choose_account)
        self.pb_one_time_account.setObjectName(u"pb_one_time_account")

        self.gridLayout.addWidget(self.pb_one_time_account, 2, 2, 1, 1)


        self.retranslateUi(choose_account)

        QMetaObject.connectSlotsByName(choose_account)
    # setupUi

    def retranslateUi(self, choose_account):
        choose_account.setWindowTitle(QCoreApplication.translate("choose_account", u"Choose account - MultiSiege", None))
        self.label.setText(QCoreApplication.translate("choose_account", u"Choose an account to download Rainbow Six Siege from Steam depots.", None))
        self.pb_accept.setText(QCoreApplication.translate("choose_account", u"OK", None))
        self.pb_reject.setText(QCoreApplication.translate("choose_account", u"Close", None))
        self.lb_SKU_RUS_countries.setText(QCoreApplication.translate("choose_account", u"<html><head/><body><p>\u2022 Armenia</p><p>\u2022 Azerbaijan</p><p>\u2022 Belarus</p><p>\u2022 Georgia</p><p>\u2022 Kazakhstan</p><p>\u2022 Republic of Moldova</p><p>\u2022 Russian Federation</p><p>\u2022 Tajikistan</p><p>\u2022 Ukraine</p><p>\u2022 Uzbekistan</p></body></html>", None))
        self.cb_SKU_RUS.setText(QCoreApplication.translate("choose_account", u"If your Steam account's store country is from any of the following countries, please select this checkbox.", None))
        self.pb_one_time_account.setText(QCoreApplication.translate("choose_account", u"One-time account", None))
    # retranslateUi

