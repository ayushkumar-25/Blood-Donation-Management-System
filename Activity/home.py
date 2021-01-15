import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import main as m
import myprofile as my


class Home(QDialog):
    def __init__(self):
        super(Home, self).__init__()
        loadUi(r'..\Resource\home.ui', self)
        self.signoutButton.clicked.connect(self.signoutfunction)
        self.myprofileButton.clicked.connect(self.gotoMyprofile)

    def gotoMyprofile(self):
        myprofile = my.MyProfile()
        m.widget.addWidget(myprofile)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)

    def signoutfunction(self):
        login = m.Login()
        m.widget.addWidget(login)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)
