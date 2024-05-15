# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'global_settings_window.ui'
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
    QComboBox, QDialog, QDialogButtonBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTreeView,
    QWidget)
from . import icons_rc

class Ui_dialog_global_settings(object):
    def setupUi(self, dialog_global_settings):
        if not dialog_global_settings.objectName():
            dialog_global_settings.setObjectName(u"dialog_global_settings")
        dialog_global_settings.resize(501, 400)
        dialog_global_settings.setMinimumSize(QSize(500, 400))
        icon = QIcon()
        icon.addFile(u":/top_nav_bar/settings-cog.svg", QSize(), QIcon.Normal, QIcon.Off)
        dialog_global_settings.setWindowIcon(icon)
        self.gridLayout = QGridLayout(dialog_global_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(dialog_global_settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 3)

        self.listwidget_page_selector = QListWidget(dialog_global_settings)
        icon1 = QIcon()
        icon1.addFile(u":/main_widget_logo/logo-TB.png", QSize(), QIcon.Normal, QIcon.Off)
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(15)
        font.setBold(True)
        __qlistwidgetitem = QListWidgetItem(self.listwidget_page_selector)
        __qlistwidgetitem.setFont(font);
        __qlistwidgetitem.setIcon(icon1);
        icon2 = QIcon()
        icon2.addFile(u":/top_nav_bar/Steam_icon_logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listwidget_page_selector)
        __qlistwidgetitem1.setFont(font);
        __qlistwidgetitem1.setIcon(icon2);
        self.listwidget_page_selector.setObjectName(u"listwidget_page_selector")
        self.listwidget_page_selector.setMinimumSize(QSize(150, 0))
        self.listwidget_page_selector.setMaximumSize(QSize(100, 16777215))
        self.listwidget_page_selector.setViewMode(QListView.ViewMode.ListMode)

        self.gridLayout.addWidget(self.listwidget_page_selector, 0, 0, 3, 2)

        self.stackedWidget = QStackedWidget(dialog_global_settings)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.launcher = QWidget()
        self.launcher.setObjectName(u"launcher")
        self.gridLayout_3 = QGridLayout(self.launcher)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.launcher)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.label = QLabel(self.launcher)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.frame = QFrame(self.launcher)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(2)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cb_update_on_start = QCheckBox(self.frame)
        self.cb_update_on_start.setObjectName(u"cb_update_on_start")

        self.gridLayout_4.addWidget(self.cb_update_on_start, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.launcher)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(2)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pb_instances_file_dialog = QPushButton(self.frame_2)
        self.pb_instances_file_dialog.setObjectName(u"pb_instances_file_dialog")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_instances_file_dialog.sizePolicy().hasHeightForWidth())
        self.pb_instances_file_dialog.setSizePolicy(sizePolicy)
        self.pb_instances_file_dialog.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_5.addWidget(self.pb_instances_file_dialog, 0, 2, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.le_instances = QLineEdit(self.frame_2)
        self.le_instances.setObjectName(u"le_instances")

        self.gridLayout_5.addWidget(self.le_instances, 0, 1, 1, 1)

        self.le_mods = QLineEdit(self.frame_2)
        self.le_mods.setObjectName(u"le_mods")

        self.gridLayout_5.addWidget(self.le_mods, 1, 1, 1, 1)

        self.pb_mods_file_dialog = QPushButton(self.frame_2)
        self.pb_mods_file_dialog.setObjectName(u"pb_mods_file_dialog")
        self.pb_mods_file_dialog.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_5.addWidget(self.pb_mods_file_dialog, 1, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 4, 0, 1, 1)

        self.label_2 = QLabel(self.launcher)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.launcher)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.frame_3 = QFrame(self.launcher)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_3.setLineWidth(2)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.cb_mode = QComboBox(self.frame_3)
        self.cb_mode.addItem("")
        self.cb_mode.addItem("")
        self.cb_mode.addItem("")
        self.cb_mode.setObjectName(u"cb_mode")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_mode.sizePolicy().hasHeightForWidth())
        self.cb_mode.setSizePolicy(sizePolicy1)
        self.cb_mode.setMinimumSize(QSize(0, 0))

        self.gridLayout_6.addWidget(self.cb_mode, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 6, 0, 1, 1)

        self.stackedWidget.addWidget(self.launcher)
        self.accounts = QWidget()
        self.accounts.setObjectName(u"accounts")
        self.gridLayout_2 = QGridLayout(self.accounts)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_accounts_title = QLabel(self.accounts)
        self.label_accounts_title.setObjectName(u"label_accounts_title")
        self.label_accounts_title.setTextFormat(Qt.TextFormat.AutoText)
        self.label_accounts_title.setScaledContents(False)
        self.label_accounts_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_accounts_title, 0, 0, 1, 1)

        self.pb_add_account = QPushButton(self.accounts)
        self.pb_add_account.setObjectName(u"pb_add_account")

        self.gridLayout_2.addWidget(self.pb_add_account, 1, 1, 1, 1)

        self.pb_remove_account = QPushButton(self.accounts)
        self.pb_remove_account.setObjectName(u"pb_remove_account")
        self.pb_remove_account.setEnabled(True)
        self.pb_remove_account.setFlat(False)

        self.gridLayout_2.addWidget(self.pb_remove_account, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.treeView = QTreeView(self.accounts)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.gridLayout_2.addWidget(self.treeView, 1, 0, 3, 1)

        self.stackedWidget.addWidget(self.accounts)

        self.gridLayout.addWidget(self.stackedWidget, 0, 2, 3, 1)


        self.retranslateUi(dialog_global_settings)
        self.buttonBox.accepted.connect(dialog_global_settings.accept)
        self.buttonBox.rejected.connect(dialog_global_settings.reject)

        self.stackedWidget.setCurrentIndex(1)
        self.pb_remove_account.setDefault(False)


        QMetaObject.connectSlotsByName(dialog_global_settings)
    # setupUi

    def retranslateUi(self, dialog_global_settings):
        dialog_global_settings.setWindowTitle(QCoreApplication.translate("dialog_global_settings", u"Global Settings - MultiSiege", None))

        __sortingEnabled = self.listwidget_page_selector.isSortingEnabled()
        self.listwidget_page_selector.setSortingEnabled(False)
        ___qlistwidgetitem = self.listwidget_page_selector.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("dialog_global_settings", u"Features", None));
        ___qlistwidgetitem1 = self.listwidget_page_selector.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("dialog_global_settings", u"Accounts", None));
        self.listwidget_page_selector.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("dialog_global_settings", u"Folders", None))
        self.label.setText(QCoreApplication.translate("dialog_global_settings", u"Features", None))
        self.cb_update_on_start.setText(QCoreApplication.translate("dialog_global_settings", u"Check for update on start?", None))
        self.pb_instances_file_dialog.setText(QCoreApplication.translate("dialog_global_settings", u"...", None))
        self.label_5.setText(QCoreApplication.translate("dialog_global_settings", u"Mods:", None))
        self.label_4.setText(QCoreApplication.translate("dialog_global_settings", u"Instances:", None))
        self.pb_mods_file_dialog.setText(QCoreApplication.translate("dialog_global_settings", u"...", None))
        self.label_2.setText(QCoreApplication.translate("dialog_global_settings", u"Update Settings", None))
        self.label_6.setText(QCoreApplication.translate("dialog_global_settings", u"Theme", None))
        self.cb_mode.setItemText(0, QCoreApplication.translate("dialog_global_settings", u"Use system setting", None))
        self.cb_mode.setItemText(1, QCoreApplication.translate("dialog_global_settings", u"Light", None))
        self.cb_mode.setItemText(2, QCoreApplication.translate("dialog_global_settings", u"Dark", None))

        self.label_7.setText(QCoreApplication.translate("dialog_global_settings", u"Mode:", None))
        self.label_accounts_title.setText(QCoreApplication.translate("dialog_global_settings", u"Accounts", None))
        self.pb_add_account.setText(QCoreApplication.translate("dialog_global_settings", u"Add Account", None))
        self.pb_remove_account.setText(QCoreApplication.translate("dialog_global_settings", u"Remove", None))
    # retranslateUi

