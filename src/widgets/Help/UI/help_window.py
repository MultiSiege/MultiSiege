# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
from . import icons_rc

class Ui_about_and_help_dialog(object):
    def setupUi(self, about_and_help_dialog):
        if not about_and_help_dialog.objectName():
            about_and_help_dialog.setObjectName(u"about_and_help_dialog")
        about_and_help_dialog.resize(525, 543)
        about_and_help_dialog.setMinimumSize(QSize(525, 543))
        icon = QIcon()
        icon.addFile(u":/top_nav_bar/Blue_Question_Mark_clip_art.svg", QSize(), QIcon.Normal, QIcon.Off)
        about_and_help_dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(about_and_help_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_close = QPushButton(about_and_help_dialog)
        self.pb_close.setObjectName(u"pb_close")
        self.pb_close.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.pb_close, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.tabWidget = QTabWidget(about_and_help_dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.verticalLayout = QVBoxLayout(self.about)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.about)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.link_multisiege_github = QLabel(self.about)
        self.link_multisiege_github.setObjectName(u"link_multisiege_github")
        self.link_multisiege_github.setTextFormat(Qt.TextFormat.RichText)
        self.link_multisiege_github.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.link_multisiege_github)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.about, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.link_guides_and_faqs = QLabel(self.tab_2)
        self.link_guides_and_faqs.setObjectName(u"link_guides_and_faqs")
        self.link_guides_and_faqs.setTextFormat(Qt.TextFormat.RichText)
        self.link_guides_and_faqs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.link_guides_and_faqs)

        self.link_discord_server = QLabel(self.tab_2)
        self.link_discord_server.setObjectName(u"link_discord_server")
        self.link_discord_server.setTextFormat(Qt.TextFormat.RichText)
        self.link_discord_server.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.link_discord_server)

        self.link_website = QLabel(self.tab_2)
        self.link_website.setObjectName(u"link_website")
        self.link_website.setTextFormat(Qt.TextFormat.RichText)
        self.link_website.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.link_website)

        self.line = QFrame(self.tab_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 2)

        self.label = QLabel(about_and_help_dialog)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/help_logo/logo_help.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_multisiege = QLabel(about_and_help_dialog)
        self.label_multisiege.setObjectName(u"label_multisiege")
        self.label_multisiege.setTextFormat(Qt.TextFormat.RichText)
        self.label_multisiege.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_multisiege, 1, 0, 1, 2)


        self.retranslateUi(about_and_help_dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(about_and_help_dialog)
    # setupUi

    def retranslateUi(self, about_and_help_dialog):
        about_and_help_dialog.setWindowTitle(QCoreApplication.translate("about_and_help_dialog", u"About MultiSiege", None))
        self.pb_close.setText(QCoreApplication.translate("about_and_help_dialog", u"Close", None))
        self.label_2.setText(QCoreApplication.translate("about_and_help_dialog", u"MultiSiege is an all in one, clean and efficient launcher and downloader for handling multiple isolated versions of Rainbow Six Siege, heavily inspired by MultiMC.", None))
        self.link_multisiege_github.setText(QCoreApplication.translate("about_and_help_dialog", u"<html><head/><body><p><a href=\"https://github.com/MultiSiege/MultiSiege\"><span style=\" text-decoration: underline; color:#55aaff;\">MultiSiege GitHub</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), QCoreApplication.translate("about_and_help_dialog", u"About", None))
        self.link_guides_and_faqs.setText(QCoreApplication.translate("about_and_help_dialog", u"<html><head/><body><p><a href=\"https://gitbook-throwback.gitbook.io/r6-operation-throwback-help-page\"><span style=\" text-decoration: underline; color:#55aaff;\">Guides and FAQs</span></a></p></body></html>", None))
        self.link_discord_server.setText(QCoreApplication.translate("about_and_help_dialog", u"<html><head/><body><p><a href=\"https://discord.gg/JGA9WPF4K8\"><span style=\" text-decoration: underline; color:#55aaff;\">R6 Throwback Discord Server</span></a></p></body></html>", None))
        self.link_website.setText(QCoreApplication.translate("about_and_help_dialog", u"<html><head/><body><p><a href=\"https://r6downloads.com/\"><span style=\" text-decoration: underline; color:#55aaff;\">R6 Downloads</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("about_and_help_dialog", u"Help", None))
        self.label.setText("")
        self.label_multisiege.setText(QCoreApplication.translate("about_and_help_dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">MultiSiege</span></p></body></html>", None))
    # retranslateUi

