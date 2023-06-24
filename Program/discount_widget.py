from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class DiscountWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title = QLabel("Discount Calculator")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-weight: bold; font-size: 24px;")

        self.price_before = QLineEdit()
        self.price_before.setPlaceholderText("Price Before Discount")
        self.price_before.setAlignment(Qt.AlignCenter)

        self.discount = QLineEdit()
        self.discount.setPlaceholderText("Discount Percentage (%)")
        self.discount.setAlignment(Qt.AlignCenter)

        self.price_after = QLabel("Price After Discount:")
        self.price_after.setAlignment(Qt.AlignCenter)

        self.money_saved = QLabel("Money Saved:")
        self.money_saved.setAlignment(Qt.AlignCenter)

        self.submit = QPushButton("=")
        self.submit.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; padding: 8px 16px; border-radius: 4px;")
        self.submit.clicked.connect(self.calculate_discount)

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.price_before)
        layout.addWidget(self.discount)
        layout.addWidget(self.submit)
        layout.addWidget(self.price_after)
        layout.addWidget(self.money_saved)
        self.setLayout(layout)

    def calculate_discount(self):
        original_price = float(self.price_before.text())
        discount_percentage = float(self.discount.text())
        discounted_price = original_price - (original_price * (discount_percentage / 100))
        self.price_after.setText("Price After Discount: $" + str(discounted_price))
        self.money_saved.setText("Money Saved: $" + str(original_price - discounted_price))
