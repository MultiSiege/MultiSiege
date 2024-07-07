import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
from Help.UI.help_window import Ui_about_and_help_dialog

class HelpWindow(qtw.QDialog, Ui_about_and_help_dialog):
    def __init__(self, parent: qtc.QObject | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.link_multisiege_github.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.link_guides_and_faqs.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.link_discord_server.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.link_website.setTextInteractionFlags(qtc.Qt.TextInteractionFlag.TextBrowserInteraction)

        self.pb_close.setMinimumWidth(104)

        self.link_multisiege_github.setOpenExternalLinks(True)
        self.link_guides_and_faqs.setOpenExternalLinks(True)
        self.link_discord_server.setOpenExternalLinks(True)
        self.link_website.setOpenExternalLinks(True)

        self.pb_close.clicked.connect(self.accept)

    def exec(self) -> int:
        self.tabWidget.setCurrentIndex(0)

        return super().exec()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = HelpWindow()
    window.show()

    sys.exit(app.exec())