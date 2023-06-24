import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget
from calculator_widget import CalculatorWidget
from discount_widget import DiscountWidget
from budget_widget import BudgetWidget
from tabbed_interface import TabbedWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabbedWindow()

    # Example tabs
    tab1_content = CalculatorWidget()
    tab2_content = DiscountWidget()
    tab3_content = BudgetWidget()

    window.add_tab("Normal", tab1_content)
    window.add_tab("Discount", tab2_content)
    window.add_tab("Budget", tab3_content)

    window.show()
    sys.exit(app.exec_())
