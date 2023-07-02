from PyQt5.QtWidgets import QComboBox, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class SaleCommissionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title = QLabel("Sale Commission Calculator")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-weight: bold; font-size: 24px;")

        self.digit1 = QLineEdit()
        self.digit1.setAlignment(Qt.AlignCenter)
        self.digit1.setPlaceholderText("Sale Price ($)")

        self.digit2 = QLineEdit()
        self.digit2.setAlignment(Qt.AlignCenter)
        self.digit2.setPlaceholderText("Commission (%)")

        self.submit = QPushButton("Calculate Sale Commission")
        self.submit.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; padding: 8px 16px; border-radius: 4px;")
        self.submit.clicked.connect(self.calculate_answer)

        self.answer_line = QLineEdit()
        self.answer_line.setReadOnly(True)
        self.answer_line.setAlignment(Qt.AlignCenter)
        self.answer_line.setPlaceholderText("Commission Amount ($)")

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.digit1)
        layout.addWidget(self.digit2)
        layout.addWidget(self.submit)
        layout.addWidget(self.answer_line)
        self.setLayout(layout)

    def change_type(self):
        self.type = self.dropdown.currentIndex()

    def calculate_answer(self):
        price = float(self.digit1.text())
        commission = float(self.digit2.text())
        percent = commission / 100
        total = price * percent
        result = total
        self.answer_line.setText(str("{:.2f}".format(result)))
