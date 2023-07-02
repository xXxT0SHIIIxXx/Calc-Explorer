from PyQt5.QtWidgets import QComboBox, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class MGGramWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title = QLabel("Mg to Grams Converter")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-weight: bold; font-size: 24px;")

        self.digit1 = QLineEdit()
        self.digit1.setAlignment(Qt.AlignCenter)
        self.digit1.setPlaceholderText("Milligrams (mg)")
        self.digit1.installEventFilter(self)

        self.digit2 = QLineEdit()
        self.digit2.setAlignment(Qt.AlignCenter)
        self.digit2.setPlaceholderText("Grams (g)")
        self.digit2.installEventFilter(self)

        self.submit = QPushButton("Convert")
        self.submit.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; padding: 8px 16px; border-radius: 4px;")
        self.submit.clicked.connect(self.calculate_answer)

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.digit1)
        layout.addWidget(self.digit2)
        layout.addWidget(self.submit)
        self.setLayout(layout)

    def eventFilter(self, obj, event):
        if event.type() == event.FocusIn:
            self.digit2.clear()
            self.digit1.clear()
        return super().eventFilter(obj, event)

    def calculate_answer(self):
        mg = self.digit1.text()
        grams = self.digit2.text()

        if mg != "":
            mg = float(mg)
            grams_result = str(mg / 1000)
            self.digit2.setText(str(grams_result) + "g")
            self.digit1.setText(str(mg) + "mg")
        elif grams != "":
            grams = float(grams)
            mg_result = str(grams * 1000)
            self.digit1.setText(str(mg_result) + "mg")
            self.digit2.setText(str(grams) + "g")
