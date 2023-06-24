from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class BudgetWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title = QLabel("50/30/20 Budget Calculator")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-weight: bold; font-size: 24px;")

        self.budget = QLineEdit()
        self.budget.setPlaceholderText("Budget ($)")
        self.budget.setAlignment(Qt.AlignCenter)

        self.submit = QPushButton("=")
        self.submit.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; padding: 8px 16px; border-radius: 4px;")
        self.submit.clicked.connect(self.calculate_budget)

        self.explain = QLabel("Your 50/30/20 Budget:")
        self.explain.setAlignment(Qt.AlignCenter)

        self.necessities = QLabel("Necessities (50):")
        self.necessities.setAlignment(Qt.AlignCenter)

        self.wants = QLabel("Wants (30):")
        self.wants.setAlignment(Qt.AlignCenter)

        self.savings = QLabel("Savings (20):")
        self.savings.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.budget)
        layout.addWidget(self.submit)
        layout.addWidget(self.explain)
        layout.addWidget(self.necessities)
        layout.addWidget(self.wants)
        layout.addWidget(self.savings)
        self.setLayout(layout)

    def calculate_budget(self):
        original_budget = float(self.budget.text())
        ness = original_budget * 0.5
        want = original_budget * 0.3
        sav = original_budget * 0.2
        self.necessities.setText("Necessities (50): $" + str(ness))
        self.wants.setText("Wants (30): $" + str(want))
        self.savings.setText("Savings (20): $" + str(sav))
