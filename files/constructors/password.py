from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit,QMainWindow
from PyQt5 import uic
import files.constructors.main as main
from files.resources.icons import icons
import sys
import os

print("loading...")

class PasswordWindow(QMainWindow):
    def __init__(self):
        super(PasswordWindow,self).__init__()
        uic.loadUi(f"files{os.sep}resources{os.sep}ui{os.sep}password.ui", self)  # Replace with your actual path to password.ui
        self.password_input= self.findChild(QLineEdit,"password_input")
        self.password_input.returnPressed.connect(self.submit_password)
        # self.show()

    def submit_password(self):
        # This method is called when Enter key is pressed in the password_input field
        self.destroy(destroySubWindows=True)
        with open("files/constructors/.temp", "w") as temp:
            temp.write(self.password_input.text())
        main.window.show()


#if __name__ == "__main__":
application = QApplication(sys.argv)
window = PasswordWindow()
window.show()
application.exec()