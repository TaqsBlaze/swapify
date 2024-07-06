from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import os


class AboutWindow(QMainWindow):

    def __init__(self):
        super(AboutWindow,self).__init__()
        uic.loadUi(f"files{os.sep}resources{os.sep}ui{os.sep}about.ui",self)

