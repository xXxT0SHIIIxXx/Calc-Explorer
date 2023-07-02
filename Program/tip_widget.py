from PyQt5.QtWidgets import QComboBox, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt

class TipWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):

        self.percents_array = [5,10,12,14,15,18,20,25,30,50]

        self.title = QLabel("Tip Calculator")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-weight: bold; font-size: 24px;")

        self.digit1 = QLineEdit()
        self.digit1.setAlignment(Qt.AlignCenter)
        self.digit1.setPlaceholderText("Price")

        self.submit = QPushButton("Calculate Hourly")
        self.submit.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; padding: 8px 16px; border-radius: 4px;")
        self.submit.clicked.connect(self.calculate_answer)

        self.answer_table = QTableWidget()
        self.answer_table.setRowCount(10)
        self.answer_table.setColumnCount(3)
        self.answer_table.setItem(0,0, QTableWidgetItem("5%"))
        self.answer_table.setItem(1,0, QTableWidgetItem("10%"))
        self.answer_table.setItem(2,0, QTableWidgetItem("12%"))
        self.answer_table.setItem(3,0, QTableWidgetItem("14%"))
        self.answer_table.setItem(4,0, QTableWidgetItem("15%"))
        self.answer_table.setItem(5,0, QTableWidgetItem("18%"))
        self.answer_table.setItem(6,0, QTableWidgetItem("20%"))
        self.answer_table.setItem(7,0, QTableWidgetItem("25%"))
        self.answer_table.setItem(8,0, QTableWidgetItem("30%"))
        self.answer_table.setItem(9,0, QTableWidgetItem("50%"))

        self.answer_table.setHorizontalHeaderLabels(['Tip %', 'Tip Amount', 'Total'])
        

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.digit1)
        layout.addWidget(self.submit)
        layout.addWidget(self.answer_table)
        self.setLayout(layout)

    def change_type(self):
        self.type = self.dropdown.currentIndex()

    def calculate_answer(self):
        xcount = 0
        ycount = 0
        price = float(self.digit1.text())
        for x in self.percents_array:
            percent = x / 100
            change = price * percent
            total = price + change
            changestr = str("{:.2f}".format(change))
            totalstr = str("{:.2f}".format(total))
            ycount = 1
            self.answer_table.setItem(xcount,ycount, QTableWidgetItem(changestr))
            ycount = 2
            self.answer_table.setItem(xcount,ycount, QTableWidgetItem(str(totalstr)))
            xcount = xcount + 1
