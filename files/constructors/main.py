from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QLineEdit
from PyQt5 import uic
from files.constructors import about
from files.resources.icons import icons
from subprocess import Popen, PIPE
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
        self.password = None
        
    
    def create_swap(self):
        if os.path.isfile("~/.safespace/swap"):
            print("Found old swap file")
            os.remove("~/.safespace/swap")
            print("Old swap file removed")
            
            commands = [
              f"fallocate -l {self.memorySlider.value()}GB ~/.safespace/swap",
              "chmod 600 ~/.safespace/swap",
              "mkswap ~/.safespace/swap",
              "swapon ~/.safespace/swap"
            ]
            
            message = ["[+] Creating swap file of {self.memorySlider.value()}GB","[+] Adding permisions...",
                     "[+] Converting file to swap memory...","[+] Activating swap memory..."]
            
            try:
                with open(f"files{os.sep}constructors{os.sep}.temp","r") as temp:
                    #Dont bite me for this.... I know theres a need for a more secure methode
                    #and I'm working on it Ok!..ok
                    temp_content = temp.read()
                    self.password = temp_content
                    print("Password:",self.password)
                    
                os.remove(f"files{os.sep}constructors{os.sep}.temp")
            
            except FileNotFoundError:
                #We want to do nothing and continue
                pass
            
            except Exception as error:
                os.remove(f"files{os.sep}constructors{os.sep}.temp")
                print("Error:", error)
                sys.exit(error)
         
          

          if os.path.exists("~/.safespace"):
            

            for command in commands:
              self.update_message(message[commands.index(command)]) #displaying message corresponding to current command

              p = Popen(['sudo','-S'] + command.split(), stdin = PIPE,
                        stderr = PIPE, universal_newlines = True)
              su = p.communicate(self.password + '\n')[1]

              print("SU:",su)
            # self.update_message()
            
            # self.update_message()
            # os.system()
            # self.update_message()
            # self.update_message(f"[+] Swap memory of {self.memorySlider.value()}GB was successfully added to your system!")
            # self.update_message("[+] Thank you for using swapify. Happy system performance")
          else:


            commands = [
              "mkdir ~/.safespace",
              f"fallocate -l {self.memorySlider.value()}GB ~/.safespace/swap",
              "chmod 600 ~/.safespace/swap",
              "mkswap ~/.safespace/swap",
              "swapon ~/.safespace/swap"
              ]
            message = ["[+] Creating safe space..","[+] Creating swap file of {self.memorySlider.value()}GB","[+] Adding permisions...",
                     "[+] Converting file to swap memory...","[+] Activating swap memory..."]
          
            for command in commands:
              self.update_message(message[commands.index(command)]) #displaying message corresponding to current command

              p = Popen(['sudo','-S'] + command.split(), stdin = PIPE,
                        stderr = PIPE, universal_newlines = True)
              su = p.communicate(self.password + '\n')[1]

              print("SU:",su)

            # self.update_message()
            # os.system()
            # self.update_message(f"[+] Creating swap file of {self.memorySlider.value()}GB")
            # os.system(f"fallocate -l {self.memorySlider.value()}GB ~/.safespace/swap")
            # self.update_message("[+] Adding permisions...")
            # os.system("sudo chmod 600 ~/.safespace/swap")
            # self.update_message("[+] Converting file to swap memory...")
            # os.system("mkswap ~/.safespace/swap")
            # self.update_message("[+] Activating swap memory...")
            # os.system("sudo swapon ~/.safespace/swap")
            # self.update_message(f"[+] Swap memory of {self.memorySlider.value()}GB was successfully added to your system!")
            # self.update_message("[+] Thank you for using swapify. Happy system performance")

    def update_message(self,message):
          self.updateScreen.append(message)
          #time.sleep(2)

    def current_memory_value(self):
          self.value_label.setText(str(self.memorySlider.value()))

    def show_about(self):
         about.ui.show()
         
        


def close():
    UI.destroy()
    application.exit()
    sys.exit(application.exec())
    
#if __name__ == '__main__':
application = QApplication(sys.argv)
window = UI()
#window.show()
#sys.exit(application.exec())
application.instance().aboutToQuit.connect(close)
