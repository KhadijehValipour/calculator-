from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def sub():
    global a
    a = int(calculator_window.txtbox.text())
    calculator_window.txtbox.setText("")


def result():
    b = int(calculator_window.txtbox.text())
    c = a - b
    calculator_window.txtbox.setText(str(c))


app = QApplication([])

loader = QUiLoader()

calculator_window = loader.load("calculator-\claculator\calculator_1.ui")
calculator_window.show()


calculator_window.btn_sub.clicked.connect(sub)
calculator_window.equal.clicked.connect(result)


app.exec()