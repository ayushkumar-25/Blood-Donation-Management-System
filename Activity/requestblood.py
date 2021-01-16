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
        self.requestbutton.clicked.connect(self.bloodRequest)

    def backtoHome(self):
        home = h.Home()
        m.widget.addWidget(home)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)

    def bloodRequest(self):
        bloodGroup = self.bloodGroup.currentText()
        location = self.location.currentText()
        users = m.db.child('Users').get()
        for user in users.each():
            if user.val()['Blood Group'] == bloodGroup and user.val()['Location'] == location:
                print(user.val())