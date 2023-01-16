from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Calculator.ui", self)

        # Define buttons functions
        self.btn_ac.clicked.connect(lambda: self.clear())
        self.btn_back.clicked.connect(lambda: self.backspace())
        self.btn_equal.clicked.connect(lambda: self.calculate())
        self.btn_dot.clicked.connect(lambda: self.add("."))
        self.btn_divide.clicked.connect(lambda: self.add("/"))
        self.btn_multiply.clicked.connect(lambda: self.add("*"))
        self.btn_subtract.clicked.connect(lambda: self.add("-"))
        self.btn_add.clicked.connect(lambda: self.add("+"))
        self.btn_1.clicked.connect(lambda: self.add("1"))
        self.btn_2.clicked.connect(lambda: self.add("2"))
        self.btn_3.clicked.connect(lambda: self.add("3"))
        self.btn_4.clicked.connect(lambda: self.add("4"))
        self.btn_5.clicked.connect(lambda: self.add("5"))
        self.btn_6.clicked.connect(lambda: self.add("6"))
        self.btn_7.clicked.connect(lambda: self.add("7"))
        self.btn_8.clicked.connect(lambda: self.add("8"))
        self.btn_9.clicked.connect(lambda: self.add("9"))
        self.btn_0.clicked.connect(lambda: self.add("0"))

    # App functions
    def add(self, text):
        expression = self.math_label.text()
        expression += text
        self.math_label.setText(expression)

    def clear(self):
        self.math_label.setText("")
        self.result_label.setText("0")

    def backspace(self):
        expression = self.math_label.text()
        expression = expression[:-1]
        self.math_label.setText(expression)

    def calculate(self):
        result = ""
        expression = self.math_label.text()
        if expression == "":
                return
        if expression != "":
                try:
                        result = eval(expression)
                        expression = str(result)
                except:
                        result = "Error"
                        self.result_label.setText(str(result))
                        return
        rounded_number = round(result, 2)
        self.result_label.setText(str(rounded_number))
        self.math_label.setText(str(rounded_number))


app = QApplication([])
window = UI()
window.show()
app.exec_()