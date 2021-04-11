import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import main as m
import home as h
import display as d


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
        display = d.Display()
        m.widget.addWidget(display)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)
        global g
        bloodGroup = self.bloodGroup.currentText()
        if bloodGroup == 'A+':
            g = ['A+', 'A-', 'O+', 'O-']
        if bloodGroup == 'O+':
            g = ['O+', 'O-']
        if bloodGroup == 'B+':
            g = ['B+', 'B-', 'O+', 'O-']
        if bloodGroup == 'AB+':
            g = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if bloodGroup == 'A-':
            g = ['A-', 'O-']
        if bloodGroup == 'O-':
            g = ['O-']
        if bloodGroup == 'B-':
            g = ['B-', 'O-']
        if bloodGroup == 'AB-':
            g = ['AB-', 'A-', 'O-', 'B-']
        location = self.location.currentText()
        users = m.db.child('Users').get()
        for user in users.each():
            for i in g:
                if user.val()['Blood Group'] == i and user.val()['Location'] == location:
                    print(user.val())