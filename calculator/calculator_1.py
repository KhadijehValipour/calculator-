from PySide6.QtWidgets import QApplication, QMainWindow , QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import *
from PySide6.QtGui import *
from functools import partial
from math import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.loader = QUiLoader()
        self.ui = self.loader.load("calculator-\calculator\calculator_1.ui")
        self.ui.show()
        self.temp_num = 0
        self.result = 0
        self.current_op = ''  #آخرین عملگر ریاضی را در خود ذخیره می کند تا در زمان استفاده از مساوی بداند باید چه عملی انجام دهد 
        self.display = QLineEdit()


        # operations
        self.ui.btn_sum.clicked.connect(partial(self.four_basic_operations, '+'))
        self.ui.btn_sub.clicked.connect(partial(self.four_basic_operations, '-'))
        self.ui.btn_div.clicked.connect(partial(self.four_basic_operations, '/'))
        self.ui.btn_multi.clicked.connect(partial(self.four_basic_operations, '*'))
        self.ui.equal.clicked.connect(self.Equal)
        self.ui.btn_percent.clicked.connect(self.Percent)
        self.ui.btn_clear.clicked.connect(self.ClearTxtBox)
        

        # numbers
        self.ui.btn_num_0.clicked.connect(partial(self.Write_num_txtbox, 0))
        self.ui.btn_num_1.clicked.connect(partial(self.Write_num_txtbox, 1))
        self.ui.btn_num_2.clicked.connect(partial(self.Write_num_txtbox, 2))
        self.ui.btn_num_3.clicked.connect(partial(self.Write_num_txtbox, 3))
        self.ui.btn_num_4.clicked.connect(partial(self.Write_num_txtbox, 4))
        self.ui.btn_num_5.clicked.connect(partial(self.Write_num_txtbox, 5))
        self.ui.btn_num_6.clicked.connect(partial(self.Write_num_txtbox, 6))
        self.ui.btn_num_7.clicked.connect(partial(self.Write_num_txtbox, 7))
        self.ui.btn_num_8.clicked.connect(partial(self.Write_num_txtbox, 8))
        self.ui.btn_num_9.clicked.connect(partial(self.Write_num_txtbox, 9))
        self.ui.btn_num_00.clicked.connect(partial(self.Write_num_txtbox, 0))
        self.ui.btn_decimal.clicked.connect(partial(self.Write_num_txtbox, '.'))




    
    def Write_num_txtbox(self, number):
        
        if self.ui.txtbox.text() != str(0):
            self.ui.txtbox.setText(self.ui.txtbox.text() + str(number)) 
  

        else:
            self.ui.txtbox.setText(str(number)) # نوع خروجی فرق میکن برای اینکه نمایش داده شود حتما باید استرینگ شود



    def ClearTxtBox(self):
        self.result = 0
        self.current_op = None
        self.temp_num = None
        self.ui.txtbox.setText("")



    def Percent(self):
        self.result = float(self.ui.txtbox.text())
        self.result /= 100
        self.ui.txtbox.setText(str(self.result))



    def Equal(self):
        self.temp_num = float(self.ui.txtbox.text())
        if self.current_op == '+':
            self.ui.txtbox.setText(str(self.result + self.temp_num))

        elif self.current_op == '-':
            self.ui.txtbox.setText(str(self.result - self.temp_num))

        elif self.current_op == '*':
            self.ui.txtbox.setText(str(self.result * self.temp_num))

        elif self.current_op == '/':
            self.ui.txtbox.setText(str(self.result / self.temp_num))
        
        self.result = 0
        self.temp_num = 0
        self.current_op =""







    def four_basic_operations(self, operation):
        try:
            if operation == "+":
                self.current_op = '+'
                self.result = float(self.ui.txtbox.text())

            elif operation == "-":
                self.current_op = "-"
                self.result = float(self.ui.txtbox.text())

            elif operation == "*":
                self.current_op = "*"
                self.result = float(self.ui.txtbox.text())

            elif operation == "/":
                self.current_op = "/"
                self.result = float(self.ui.txtbox.text())

            self.ui.txtbox.setText("") #  برای اینکه کادری که عدد در ان ولرد میکنیم پاک شده و آماده دریافت عدد بعدی باشه


        except:
            self.ui.txtbox.setText("Error")
            self.result = 0

app = QApplication()

main_window = MainWindow()
app.exec()
































