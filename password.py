from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit,QMainWindow
from PyQt5 import uic
import sys
import os


class PasswordWindow(QMainWindow):
    def __init__(self):
        super(PasswordWindow,self).__init__()
        uic.loadUi(f"files{os.sep}resources{os.sep}ui{os.sep}password.ui", self)  # Replace with your actual path to password.ui
        self.password_input= self.findChild(QLineEdit,"password_input")
        self.password_input.returnPressed.connect(self.submit_password)
        # self.show()

    def submit_password(self):
        # This method is called when Enter key is pressed in the password_input field
        self.destroy(destroySubWindows=True)  # Close the dialog with Accepted status

    def getPassword(self):
        self.show()
        return self.password_input.text()
    

app = QApplication(sys.argv)
passwordUI = PasswordWindow()