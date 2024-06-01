# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instance_settings_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)
from . import icons_rc

class Ui_instance_settings(object):
    def setupUi(self, instance_settings):
        if not instance_settings.objectName():
            instance_settings.setObjectName(u"instance_settings")
        instance_settings.resize(400, 126)
        icon = QIcon()
        icon.addFile(u":/top_nav_bar/settings-cog.svg", QSize(), QIcon.Normal, QIcon.Off)
        instance_settings.setWindowIcon(icon)
        self.gridLayout = QGridLayout(instance_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_username = QLineEdit(instance_settings)
        self.le_username.setObjectName(u"le_username")
        self.le_username.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout.addWidget(self.le_username, 1, 1, 1, 1)

        self.label_2 = QLabel(instance_settings)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.le_instance_name = QLineEdit(instance_settings)
        self.le_instance_name.setObjectName(u"le_instance_name")
        self.le_instance_name.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout.addWidget(self.le_instance_name, 0, 1, 1, 1)

        self.label = QLabel(instance_settings)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(instance_settings)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(instance_settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.cb_version = QComboBox(instance_settings)
        self.cb_version.setObjectName(u"cb_version")

        self.gridLayout.addWidget(self.cb_version, 2, 1, 1, 1)


        self.retranslateUi(instance_settings)
        self.buttonBox.accepted.connect(instance_settings.accept)
        self.buttonBox.rejected.connect(instance_settings.reject)

        QMetaObject.connectSlotsByName(instance_settings)
    # setupUi

    def retranslateUi(self, instance_settings):
        instance_settings.setWindowTitle(QCoreApplication.translate("instance_settings", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("instance_settings", u"Username: ", None))
        self.label.setText(QCoreApplication.translate("instance_settings", u"Instance name:", None))
        self.label_3.setText(QCoreApplication.translate("instance_settings", u"Version:", None))
    # retranslateUi

