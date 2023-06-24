from PyQt5.QtWidgets import QComboBox, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class CalculatorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title = QLabel("Normal Calculator")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-weight: bold; font-size: 24px;")

        self.digit1 = QLineEdit()
        self.digit1.setAlignment(Qt.AlignCenter)
        self.digit1.setPlaceholderText("First Number")

        self.dropdown = QComboBox()
        self.dropdown.addItems(["None", "+", "-", "*", "/"])
        self.dropdown.activated.connect(self.change_type)

        self.digit2 = QLineEdit()
        self.digit2.setAlignment(Qt.AlignCenter)
        self.digit2.setPlaceholderText("Second Number")

        self.submit = QPushButton("=")
        self.submit.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; padding: 8px 16px; border-radius: 4px;")
        self.submit.clicked.connect(self.calculate_answer)

        self.answer_line = QLineEdit()
        self.answer_line.setReadOnly(True)
        self.answer_line.setAlignment(Qt.AlignCenter)
        self.answer_line.setPlaceholderText("Result")

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.digit1)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.digit2)
        layout.addWidget(self.submit)
        layout.addWidget(self.answer_line)
        self.setLayout(layout)

    def change_type(self):
        self.type = self.dropdown.currentIndex()

    def calculate_answer(self):
        d1 = float(self.digit1.text())
        d2 = float(self.digit2.text())
        sign = self.dropdown.currentIndex()

        if sign == 0:
            self.answer_line.setText("NONE")
        elif sign == 1:
            self.answer_line.setText(str(d1 + d2))
        elif sign == 2:
            self.answer_line.setText(str(d1 - d2))
        elif sign == 3:
            self.answer_line.setText(str(d1 * d2))
        elif sign == 4:
            self.answer_line.setText(str(d1 / d2))
