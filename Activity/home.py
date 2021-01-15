import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import main as m


class Home(QDialog):
    def __init__(self):
        super(Home, self).__init__()
        loadUi(r'..\Resource\home.ui', self)
        self.signoutButton.clicked.connect(self.signoutfunction)

    def signoutfunction(self):
        login = m.Login()
        m.widget.addWidget(login)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)
