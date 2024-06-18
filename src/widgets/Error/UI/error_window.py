# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_window.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
from . import icons_rc

class Ui_error_dialog(object):
    def setupUi(self, error_dialog):
        if not error_dialog.objectName():
            error_dialog.setObjectName(u"error_dialog")
        error_dialog.resize(400, 84)
        icon = QIcon()
        icon.addFile(u":/error_logo/Cross_red_circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        error_dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(error_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(298, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.pb_close = QPushButton(error_dialog)
        self.pb_close.setObjectName(u"pb_close")

        self.gridLayout.addWidget(self.pb_close, 1, 1, 1, 1)

        self.frame_error = QFrame(error_dialog)
        self.frame_error.setObjectName(u"frame_error")
        self.frame_error.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_error)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_error = QLabel(self.frame_error)
        self.lb_error.setObjectName(u"lb_error")
        self.lb_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_error.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_error, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_error, 0, 0, 1, 2)


        self.retranslateUi(error_dialog)

        QMetaObject.connectSlotsByName(error_dialog)
    # setupUi

    def retranslateUi(self, error_dialog):
        error_dialog.setWindowTitle(QCoreApplication.translate("error_dialog", u"Error - MultiSiege", None))
        self.pb_close.setText(QCoreApplication.translate("error_dialog", u"Close", None))
        self.lb_error.setText(QCoreApplication.translate("error_dialog", u"ERROR_MESSAGE", None))
    # retranslateUi

