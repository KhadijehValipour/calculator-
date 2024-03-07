from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def test():
    print("Connecting to the banking portal...")

def moshavere():
    print("To contact the consultant, call 02165488421")

def bime():
    my_window.lineEdit.setText("کجا میخوای بری؟")

my_app = QApplication([])


loader = QUiLoader()
my_window = loader.load("untitled.ui")
my_window.show()
my_window.pushButton.clicked.connect(test)
my_window.moshavere.clicked.connect(moshavere)
my_window.ahmad.clicked.connect(bime)


print(type(my_window))

my_app.exec()