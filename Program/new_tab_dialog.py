from PyQt5.QtWidgets import QComboBox, QWidget, QVBoxLayout, QLineEdit, QLabel, QDialog, QDialogButtonBox
from calculator_widget import CalculatorWidget
from discount_widget import DiscountWidget
from budget_widget import BudgetWidget

class NewTabDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Tab Dialog")
        self.tab_name_edit = QLineEdit()
        self.tab_name_edit.setPlaceholderText("Enter tab name")
        self.dropdown = QComboBox()
        self.dropdown.addItems(["None", "Normal", "Discount", "50/30/20 Budget"])
        self.dropdown.activated.connect(self.change_type)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tab Name:"))
        layout.addWidget(self.tab_name_edit)
        layout.addWidget(QLabel("Presets:"))
        layout.addWidget(self.dropdown)
        layout.addWidget(button_box)
        self.setLayout(layout)
    
    def change_type(self):
        self.type = self.dropdown.currentIndex()

    def choose_preset(self):
        if self.type == 0:
            return QWidget()
        elif self.type == 1:
            return CalculatorWidget()
        elif self.type == 2:
            return DiscountWidget()
        elif self.type == 3:
            return BudgetWidget()

    def get_tab_creator(self):
        return [self.tab_name_edit.text(), self.choose_preset()]