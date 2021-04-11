import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import requestblood as req
import main as m


class Display(QDialog):
    def __init__(self):
        super(Display, self).__init__()
        loadUi(r'..\Resource\display.ui', self)
        self.backButton.clicked.connect(self.backtoHome)

    def backtoHome(self):
        request = req.RequestBlood()
        m.widget.addWidget(request)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)
