import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import main as m
import home as h


class RequestBlood(QDialog):
    def __init__(self):
        super(RequestBlood, self).__init__()
        loadUi(r'..\Resource\requestblood.ui', self)
        self.backButton.clicked.connect(self.backtoHome)

    def backtoHome(self):
        home = h.Home()
        m.widget.addWidget(home)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)
