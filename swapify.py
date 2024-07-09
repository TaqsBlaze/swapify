from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame
from PyQt5 import uic
from about import AboutWindow
from password import PasswordWindow
import password
import sys
import os
import time






class UI(QMainWindow):

    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi(f"files{os.sep}resources{os.sep}ui{os.sep}swap.ui", self)
        self.actionAbout.triggered.connect(self.show_about)
        self.memorySlider.valueChanged.connect(self.current_memory_value)
        self.createButton.clicked.connect(self.create_swap)
        self.value_label.setText(str(self.memorySlider.value()))

    
    def create_swap(self):

          password_window = PasswordWindow()
          password = password_window.getPassword()
          print("password is", password)

          if os.path.exists("~/.safespace"):
                
                self.update_message(f"[+] Creating swap file of {self.memorySlider.value()}GB")
                os.system(f"fallocate -l {self.memorySlider.value()}GB ~/.safespace/swap")
                self.update_message("[+] Adding permisions...")
                os.system("sudo chmod 600 ~/.safespace/swap")
                self.update_message("[+] Converting file to swap memory...")
                os.system("mkswap ~/.safespace/swap")
                self.update_message("[+] Activating swap memory...")
                os.system("sudo swapon ~/.safespace/swap")
                self.update_message(f"[+] Swap memory of {self.memorySlider.value()}GB was successfully added to your system!")
                self.update_message("[+] Thank you for using swapify. Happy system performance")
          else:
            self.update_message("[+] Creating safe space..")
            os.system("mkdir ~/.safespace")
            self.update_message(f"[+] Creating swap file of {self.memorySlider.value()}GB")
            os.system(f"fallocate -l {self.memorySlider.value()}GB ~/.safespace/swap")
            self.update_message("[+] Adding permisions...")
            os.system("sudo chmod 600 ~/.safespace/swap")
            self.update_message("[+] Converting file to swap memory...")
            os.system("mkswap ~/.safespace/swap")
            self.update_message("[+] Activating swap memory...")
            os.system("sudo swapon ~/.safespace/swap")
            self.update_message(f"[+] Swap memory of {self.memorySlider.value()}GB was successfully added to your system!")
            self.update_message("[+] Thank you for using swapify. Happy system performance")

    def update_message(self,message):
          self.updateScreen.append(message)
          #time.sleep(2)

    def current_memory_value(self):
          self.value_label.setText(str(self.memorySlider.value()))

    def show_about(self):
         pass

if __name__ == '__main__':
	application = QApplication(sys.argv)
	window = UI()
	window.show()
	sys.exit(application.exec())
