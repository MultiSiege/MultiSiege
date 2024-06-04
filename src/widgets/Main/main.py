import sys
from PySide6 import (
    QtCore as qtc,
    QtWidgets as qtw,
    QtGui as qtg
)
sys.path.append('src\widgets')
from Main.UI.main_window import Ui_MainWindow
from NewInstance.new_instance import NewInstance
from GlobalSettings.global_settings import GlobalSettingsWindow
from Help.help import HelpWindow
from Delete.delete import DeleteWindow
from CreateShortcut.create_shortcut import CreateShortcutWindow
from InstanceSettings.instance_settings import InstanceSettingsWindow
from ChooseAccount.choose_account import ChooseAccountWindow

sys.path.append('src')
from instance import Instance

class InstanceWidget(qtw.QFrame):
    current_index_changed = qtc.Signal(int)
    def __init__(self, instance_name: str, index: int, parent: qtw.QWidget | None = None) -> None:
        super().__init__(parent)

        self.instance_name = instance_name
        self.index = index

        self.setObjectName(f"frame_instance_{index}")
        self.setMinimumSize(qtc.QSize(113, 143))
        self.setMaximumWidth(113)
        self.setCursor(qtg.QCursor(qtg.Qt.PointingHandCursor))
        self.setFrameShape(qtw.QFrame.Shape.Panel)
        self.setFrameShadow(qtw.QFrame.Shadow.Plain)
        self.setLineWidth(2)

        self.verticalLayout = qtw.QVBoxLayout(self)
        self.verticalLayout.setObjectName(f"verticalLayout_instance_{int}")
        self.label_icon = qtw.QLabel(self)
        self.label_icon.setObjectName(f"label_icon_instance_{instance_name}")
        self.label_icon.setPixmap(qtg.QPixmap(u":/side_nav_bar/rainbow-six-siege-logo-logo-svg-vector.svg"))
        self.label_icon.setAlignment(qtg.Qt.AlignmentFlag.AlignCenter)
        self.label_icon.setSizePolicy(qtw.QSizePolicy.Policy.MinimumExpanding, qtw.QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addWidget(self.label_icon)

        self.label_instance = qtw.QLabel(self)
        self.label_instance.setObjectName(f"label_instance_{index}")
        self.label_instance.setAlignment(qtg.Qt.AlignmentFlag.AlignCenter)
        self.label_instance.setWordWrap(True)
        self.label_instance.setText(instance_name)

        self.verticalLayout.addWidget(self.label_instance)

        self.default_colour = self.label_icon.styleSheet()
        self.selected_colour = "QLabel { color : black; }"

    def mousePressEvent(self, event: qtg.QMouseEvent) -> None:
        if event.button() == qtc.Qt.MouseButton.LeftButton:
            self.current_index_changed.emit(self.index)
        else:
            super().mousePressEvent(event)

class FlowLayout(qtw.QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

        if parent is not None:
            self.setContentsMargins(qtc.QMargins(0, 0, 0, 0))

        self._item_list: list[qtw.QLayoutItem] = []

    def sortInstances(self) -> None:
        self._item_list.sort(key=lambda layout_item: layout_item.widget().instance_name.upper())

        for index, item in enumerate(self._item_list):
            item.widget().index = index

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self._item_list.append(item)

    def count(self):
        return len(self._item_list)

    def itemAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list[index]

        return None

    def takeAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list.pop(index)

        return None

    def expandingDirections(self):
        return qtg.Qt.Orientation(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self._do_layout(qtc.QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self._do_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = qtc.QSize()

        for item in self._item_list:
            size = size.expandedTo(item.minimumSize())

        size += qtc.QSize(2 * self.contentsMargins().top(), 2 * self.contentsMargins().top())
        return size

    def _do_layout(self, rect, test_only):
        x = rect.x()
        y = rect.y()
        line_height = 0
        spacing = self.spacing()

        for item in self._item_list:
            style = item.widget().style()
            layout_spacing_x = style.layoutSpacing(
                qtw.QSizePolicy.PushButton, qtw.QSizePolicy.PushButton, qtg.Qt.Horizontal
            )
            layout_spacing_y = style.layoutSpacing(
                qtw.QSizePolicy.PushButton, qtw.QSizePolicy.PushButton, qtg.Qt.Vertical
            )
            space_x = spacing + layout_spacing_x
            space_y = spacing + layout_spacing_y
            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if not test_only:
                item.setGeometry(qtc.QRect(qtc.QPoint(x, y), item.sizeHint()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return y + line_height - rect.y()

class MainWindow(qtw.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.new_instance_dialog = NewInstance(self)
        self.global_settings_dialog = GlobalSettingsWindow(self)
        self.help_dialog = HelpWindow(self)
        self.delete_dialog = DeleteWindow(self)
        self.create_shortcut_dialog = CreateShortcutWindow(self)
        self.instance_settings_dialog = InstanceSettingsWindow(self)
        self.choose_account_dialog = ChooseAccountWindow(self)

        self.flow_layout_instances = FlowLayout(parent=self.scrollAreaWidgetContents)

        self.current_widget: InstanceWidget | None = None#by default set the current widget to None as there are no widgets currently
        self.set_instance_buttons_enabled(False)

        self.pb_add_instance.clicked.connect(self.open_new_instance_window)
        self.pb_settings.clicked.connect(lambda: self.open_global_settings_window(0))
        self.pb_accounts.clicked.connect(lambda: self.open_global_settings_window(1))
        self.pb_help.clicked.connect(self.open_help_window)

    @qtc.Slot()
    def open_new_instance_window(self) -> None:
        self.new_instance_dialog.exec()

    @qtc.Slot()
    def open_global_settings_window(self, page: int) -> None:
        self.global_settings_dialog.exec(index=page)

    @qtc.Slot()
    def open_help_window(self) -> None:
        self.help_dialog.exec()

    @qtc.Slot(int)
    def set_current_instance_widget(self, index: int) -> None:
        if self.current_widget is not None:
            self.current_widget.setStyleSheet(self.current_widget.default_colour)
        else:
            self.set_instance_buttons_enabled(True)

        new_instance_widget: InstanceWidget = self.flow_layout_instances.itemAt(index).widget()
        new_instance_widget.setStyleSheet(new_instance_widget.selected_colour)

        self.label_instance_name.setText(new_instance_widget.instance_name)

        self.current_widget = new_instance_widget

    def add_instance_widget(self, instance: Instance, select_instance: bool = False) -> None:
        """
        Adds a widget to display an `Instance` object in the main window. Automatically sorts by name.
        """
        instance_widget = InstanceWidget(instance.settings.instance_name, self.flow_layout_instances.count(), self.scrollAreaWidgetContents)
        instance_widget.current_index_changed.connect(self.set_current_instance_widget)

        self.flow_layout_instances.addWidget(instance_widget)
        self.flow_layout_instances.sortInstances()

        if len(self.flow_layout_instances._item_list) == 1 or select_instance:#if this is the first item then automatically set is as the selected instance
            instance_widget.current_index_changed.emit(instance_widget.index)

    def clear_instance_widgets(self) -> None:
        """
        Clears all widgets that are displayed currently in the layout.
        """
        item = self.flow_layout_instances.takeAt(0)

        while item is not None:
            item.widget().deleteLater()
            del item

            item = self.flow_layout_instances.takeAt(0)

        self.current_widget = None
        self.set_instance_buttons_enabled(False)
        self.label_instance_name.setText("you have no instances :(")

    def set_instance_buttons_enabled(self, enabled: bool) -> None:
        self.pb_launch.setEnabled(enabled)
        self.pb_download.setEnabled(enabled)
        self.pb_instance_settings.setEnabled(enabled)
        self.pb_instance_folder.setEnabled(enabled)
        self.pb_siege_folder.setEnabled(enabled)
        self.pb_create_shortcut.setEnabled(enabled)
        self.pb_delete.setEnabled(enabled)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())