import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
import pyluhn
from pyluhn import verify

class Firstpage(QDialog):
    def __init__(self):
        super(Firstpage, self).__init__()
        loadUi("DapperCredit.ui",self)
        self.ValidateButton.clicked.connect(self.validate)

    def validate(self):
        UserInput = self.NumberBox.text()

        if len(UserInput) != 16:
            message = QMessageBox()
            message.setWindowTitle("ERROR")
            message.setText("Error, Your input is not == 16 characters")

            x = message.exec_()

        if UserInput.isnumeric() == False:
            message = QMessageBox()
            message.setWindowTitle("Error")
            message.setText("Your Card number must be integers only")


            x = message.exec_()

        if UserInput == "":
            message = QMessageBox()
            message.setWindowTitle("Error")
            message.setText("Input was empty")

            x = message.exec_()



        else:
            verification = verify(UserInput)
            if verification == True:
                message = QMessageBox()
                message.setWindowTitle("Success")
                message.setText("Card is Valid")

                x = message.exec_()
            else:
                message = QMessageBox()
                message.setWindowTitle("Error")
                message.setText("Card is Invalid")

                x = message.exec_()



app = QApplication(sys.argv)

window = Firstpage()
window.show()

app.exec()