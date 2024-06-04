# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from . import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(748, 557)
        icon = QIcon()
        icon.addFile(u":/main_widget_logo/logo-TB.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 6, 1, 1)

        self.line_5 = QFrame(MainWindow)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_5, 0, 5, 1, 1)

        self.line_4 = QFrame(MainWindow)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 0, 1, 1, 1)

        self.pb_add_instance = QPushButton(MainWindow)
        self.pb_add_instance.setObjectName(u"pb_add_instance")
        self.pb_add_instance.setMinimumSize(QSize(115, 50))
        icon1 = QIcon()
        icon1.addFile(u":/top_nav_bar/magic-wand-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_add_instance.setIcon(icon1)
        self.pb_add_instance.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.pb_add_instance, 0, 0, 1, 1)

        self.pb_settings = QPushButton(MainWindow)
        self.pb_settings.setObjectName(u"pb_settings")
        self.pb_settings.setMinimumSize(QSize(100, 50))
        icon2 = QIcon()
        icon2.addFile(u":/top_nav_bar/settings-cog.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_settings.setIcon(icon2)
        self.pb_settings.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.pb_settings, 0, 3, 1, 1)

        self.widget_sidebar = QWidget(MainWindow)
        self.widget_sidebar.setObjectName(u"widget_sidebar")
        self.widget_sidebar.setMaximumSize(QSize(115, 406))
        self.verticalLayout = QVBoxLayout(self.widget_sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_instance_icon_sidebar = QLabel(self.widget_sidebar)
        self.label_instance_icon_sidebar.setObjectName(u"label_instance_icon_sidebar")
        self.label_instance_icon_sidebar.setPixmap(QPixmap(u":/side_nav_bar/rainbow-six-siege-logo-logo-svg-vector.svg"))
        self.label_instance_icon_sidebar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_instance_icon_sidebar)

        self.label_instance_name = QLabel(self.widget_sidebar)
        self.label_instance_name.setObjectName(u"label_instance_name")
        self.label_instance_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_instance_name.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_instance_name)

        self.line = QFrame(self.widget_sidebar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.pb_launch = QPushButton(self.widget_sidebar)
        self.pb_launch.setObjectName(u"pb_launch")

        self.verticalLayout.addWidget(self.pb_launch)

        self.pb_download = QPushButton(self.widget_sidebar)
        self.pb_download.setObjectName(u"pb_download")

        self.verticalLayout.addWidget(self.pb_download)

        self.line_3 = QFrame(self.widget_sidebar)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.pb_instance_settings = QPushButton(self.widget_sidebar)
        self.pb_instance_settings.setObjectName(u"pb_instance_settings")

        self.verticalLayout.addWidget(self.pb_instance_settings)

        self.pb_instance_folder = QPushButton(self.widget_sidebar)
        self.pb_instance_folder.setObjectName(u"pb_instance_folder")

        self.verticalLayout.addWidget(self.pb_instance_folder)

        self.pb_siege_folder = QPushButton(self.widget_sidebar)
        self.pb_siege_folder.setObjectName(u"pb_siege_folder")

        self.verticalLayout.addWidget(self.pb_siege_folder)

        self.line_2 = QFrame(self.widget_sidebar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.pb_create_shortcut = QPushButton(self.widget_sidebar)
        self.pb_create_shortcut.setObjectName(u"pb_create_shortcut")

        self.verticalLayout.addWidget(self.pb_create_shortcut)

        self.pb_delete = QPushButton(self.widget_sidebar)
        self.pb_delete.setObjectName(u"pb_delete")

        self.verticalLayout.addWidget(self.pb_delete)

        self.line_6 = QFrame(self.widget_sidebar)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_6)


        self.gridLayout.addWidget(self.widget_sidebar, 1, 9, 2, 1)

        self.pb_help = QPushButton(MainWindow)
        self.pb_help.setObjectName(u"pb_help")
        self.pb_help.setMinimumSize(QSize(100, 50))
        icon3 = QIcon()
        icon3.addFile(u":/top_nav_bar/Blue_Question_Mark_clip_art.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_help.setIcon(icon3)
        self.pb_help.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.pb_help, 0, 4, 1, 1)

        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 607, 481))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 3, 9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 9, 1, 1)

        self.pb_folders = QPushButton(MainWindow)
        self.pb_folders.setObjectName(u"pb_folders")
        self.pb_folders.setMinimumSize(QSize(100, 50))
        icon4 = QIcon()
        icon4.addFile(u":/top_nav_bar/285658_blue_folder_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_folders.setIcon(icon4)
        self.pb_folders.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.pb_folders, 0, 2, 1, 1)

        self.pb_accounts = QPushButton(MainWindow)
        self.pb_accounts.setObjectName(u"pb_accounts")
        self.pb_accounts.setMinimumSize(QSize(100, 50))
        icon5 = QIcon()
        icon5.addFile(u":/top_nav_bar/Steam_icon_logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_accounts.setIcon(icon5)
        self.pb_accounts.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.pb_accounts, 0, 9, 1, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MultiSiege - Main Window", None))
        self.pb_add_instance.setText(QCoreApplication.translate("MainWindow", u"Add instance", None))
        self.pb_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_instance_icon_sidebar.setText("")
        self.label_instance_name.setText(QCoreApplication.translate("MainWindow", u"INSTANCE_NAME", None))
        self.pb_launch.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.pb_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.pb_instance_settings.setText(QCoreApplication.translate("MainWindow", u"Instance Settings", None))
        self.pb_instance_folder.setText(QCoreApplication.translate("MainWindow", u"Instance Folder", None))
        self.pb_siege_folder.setText(QCoreApplication.translate("MainWindow", u"Siege Folder", None))
        self.pb_create_shortcut.setText(QCoreApplication.translate("MainWindow", u"Create Shortcut", None))
        self.pb_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pb_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.pb_folders.setText(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.pb_accounts.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
    # retranslateUi

