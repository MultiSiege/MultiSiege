# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from . import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(639, 557)
        icon = QIcon()
        icon.addFile(u":/main_widget_logo/logo-TB.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)

        self.widget_topnav = QWidget(MainWindow)
        self.widget_topnav.setObjectName(u"widget_topnav")
        self.widget_topnav.setMaximumSize(QSize(16777215, 68))
        self.horizontalLayout = QHBoxLayout(self.widget_topnav)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_add_instance = QPushButton(self.widget_topnav)
        self.pb_add_instance.setObjectName(u"pb_add_instance")
        self.pb_add_instance.setMinimumSize(QSize(115, 50))
        icon1 = QIcon()
        icon1.addFile(u":/top_nav_bar/magic-wand-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_add_instance.setIcon(icon1)
        self.pb_add_instance.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pb_add_instance)

        self.line_4 = QFrame(self.widget_topnav)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.pb_folders = QPushButton(self.widget_topnav)
        self.pb_folders.setObjectName(u"pb_folders")
        self.pb_folders.setMinimumSize(QSize(100, 50))
        icon2 = QIcon()
        icon2.addFile(u":/top_nav_bar/285658_blue_folder_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_folders.setIcon(icon2)
        self.pb_folders.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pb_folders)

        self.pb_settings = QPushButton(self.widget_topnav)
        self.pb_settings.setObjectName(u"pb_settings")
        self.pb_settings.setMinimumSize(QSize(100, 50))
        icon3 = QIcon()
        icon3.addFile(u":/top_nav_bar/settings-cog.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_settings.setIcon(icon3)
        self.pb_settings.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pb_settings)

        self.pb_help = QPushButton(self.widget_topnav)
        self.pb_help.setObjectName(u"pb_help")
        self.pb_help.setMinimumSize(QSize(100, 50))
        icon4 = QIcon()
        icon4.addFile(u":/top_nav_bar/Blue_Question_Mark_clip_art.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_help.setIcon(icon4)
        self.pb_help.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pb_help)

        self.line_5 = QFrame(self.widget_topnav)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_accounts = QPushButton(self.widget_topnav)
        self.pb_accounts.setObjectName(u"pb_accounts")
        self.pb_accounts.setMinimumSize(QSize(100, 50))
        icon5 = QIcon()
        icon5.addFile(u":/top_nav_bar/Steam_icon_logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_accounts.setIcon(icon5)
        self.pb_accounts.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pb_accounts)


        self.gridLayout.addWidget(self.widget_topnav, 0, 0, 1, 3)

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
        self.label_instance_name.setWordWrap(False)

        self.verticalLayout.addWidget(self.label_instance_name)

        self.line = QFrame(self.widget_sidebar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.pb_launch = QPushButton(self.widget_sidebar)
        self.pb_launch.setObjectName(u"pb_launch")

        self.verticalLayout.addWidget(self.pb_launch)

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

        self.pb_export_instance = QPushButton(self.widget_sidebar)
        self.pb_export_instance.setObjectName(u"pb_export_instance")

        self.verticalLayout.addWidget(self.pb_export_instance)

        self.pb_delete = QPushButton(self.widget_sidebar)
        self.pb_delete.setObjectName(u"pb_delete")

        self.verticalLayout.addWidget(self.pb_delete)

        self.line_6 = QFrame(self.widget_sidebar)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_6)


        self.gridLayout.addWidget(self.widget_sidebar, 1, 2, 2, 1)

        self.frame_instances = QFrame(MainWindow)
        self.frame_instances.setObjectName(u"frame_instances")
        self.frame_instances.setMinimumSize(QSize(0, 0))
        self.frame_instances.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_instances.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_instances)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_instance_INSTANCE_NAME = QFrame(self.frame_instances)
        self.frame_instance_INSTANCE_NAME.setObjectName(u"frame_instance_INSTANCE_NAME")
        self.frame_instance_INSTANCE_NAME.setMaximumSize(QSize(113, 143))
        self.frame_instance_INSTANCE_NAME.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_instance_INSTANCE_NAME.setFrameShape(QFrame.Shape.Panel)
        self.frame_instance_INSTANCE_NAME.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_instance_INSTANCE_NAME.setLineWidth(2)
        self.verticalLayout_2 = QVBoxLayout(self.frame_instance_INSTANCE_NAME)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_icon_instance_INSTANCE_NAME = QLabel(self.frame_instance_INSTANCE_NAME)
        self.label_icon_instance_INSTANCE_NAME.setObjectName(u"label_icon_instance_INSTANCE_NAME")
        self.label_icon_instance_INSTANCE_NAME.setPixmap(QPixmap(u":/side_nav_bar/rainbow-six-siege-logo-logo-svg-vector.svg"))
        self.label_icon_instance_INSTANCE_NAME.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_icon_instance_INSTANCE_NAME)

        self.label_instance_INSTANCE_NAME = QLabel(self.frame_instance_INSTANCE_NAME)
        self.label_instance_INSTANCE_NAME.setObjectName(u"label_instance_INSTANCE_NAME")
        self.label_instance_INSTANCE_NAME.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_instance_INSTANCE_NAME)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame_instance_INSTANCE_NAME)


        self.gridLayout.addWidget(self.frame_instances, 1, 0, 3, 2)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MultiSiege - Main Window", None))
        self.pb_add_instance.setText(QCoreApplication.translate("MainWindow", u"Add instance", None))
        self.pb_folders.setText(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.pb_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pb_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.pb_accounts.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.label_instance_icon_sidebar.setText("")
        self.label_instance_name.setText(QCoreApplication.translate("MainWindow", u"INSTANCE_NAME", None))
        self.pb_launch.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.pb_instance_settings.setText(QCoreApplication.translate("MainWindow", u"Instance Settings", None))
        self.pb_instance_folder.setText(QCoreApplication.translate("MainWindow", u"Instance Folder", None))
        self.pb_siege_folder.setText(QCoreApplication.translate("MainWindow", u"Siege Folder", None))
        self.pb_create_shortcut.setText(QCoreApplication.translate("MainWindow", u"Create Shortcut", None))
        self.pb_export_instance.setText(QCoreApplication.translate("MainWindow", u"Export Instance", None))
        self.pb_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_icon_instance_INSTANCE_NAME.setText("")
        self.label_instance_INSTANCE_NAME.setText(QCoreApplication.translate("MainWindow", u"INSTANCE_NAME", None))
    # retranslateUi

