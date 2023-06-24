import sys
from PyQt5.QtWidgets import QComboBox, QVBoxLayout, QLineEdit, QLabel, QDialog, QDialogButtonBox

class NewOptionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Options")
        self.tab_name_edit = QLineEdit()
        self.tab_name_edit.setPlaceholderText("Enter tab name")
        self.dropdown = QComboBox()
        self.dropdown.addItems(["Light Mode", "Dark Mode", "Lemon Lime", "Lava Cakes"])
        self.dropdown.activated.connect(self.change_type)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Options Menu"))
        layout.addWidget(QLabel("Appearance:"))
        layout.addWidget(self.dropdown)
        layout.addWidget(button_box)
        self.setLayout(layout)
    
    def change_type(self):
        self.type = self.dropdown.currentIndex()