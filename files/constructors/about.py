from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from files.resources.icons import icons
import os
import sys


class AboutWindow(QMainWindow):

    def __init__(self):
        super(AboutWindow,self).__init__()
        uic.loadUi(f"files{os.sep}resources{os.sep}ui{os.sep}about.ui",self)





application = QApplication(sys.argv)
ui = AboutWindow()