from PyQt5.QtWidgets import QMenu, QAction, QMainWindow, QTabWidget, QComboBox, QWidget, QVBoxLayout, QLineEdit, QLabel, QDialog, QDialogButtonBox
from new_tab_dialog import NewTabDialog
from new_option_dialog import NewOptionDialog

class TabbedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calc-Explorer v1.1")

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

    def add_tab(self, title, content):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(content)
        tab.setLayout(layout)

        self.tab_widget.addTab(tab, title)

    def remove_current_tab(self):
        current_index = self.tab_widget.currentIndex()
        self.tab_widget.removeTab(current_index)

    def mousePressEvent(self, event):
        if event.button() == 2:  # Right mouse button
            context_menu = QMenu(self)

            add_tab_action = QAction("Add New Tab", self)
            add_tab_action.triggered.connect(self.add_new_tab)
            context_menu.addAction(add_tab_action)

            close_tab_action = QAction("Close Current Tab", self)
            close_tab_action.triggered.connect(self.remove_current_tab)
            context_menu.addAction(close_tab_action)

            options_tab_action = QAction("Open Options", self)
            options_tab_action.triggered.connect(self.open_options_menu)
            context_menu.addAction(options_tab_action)

            context_menu.exec_(self.mapToGlobal(event.pos()))
        else:
            super().mousePressEvent(event)

    def add_new_tab(self):
        dialog = NewTabDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            tab_name = dialog.get_tab_creator()[0]
            tab_con = dialog.get_tab_creator()[1]
            if tab_name:
                self.add_tab(tab_name, tab_con)

    def open_options_menu(self):
        dialog = NewOptionDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            return
