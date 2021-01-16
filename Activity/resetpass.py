import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import main as m
import home as h

class ResetPass(QDialog):
    def __init__(self):
        super(ResetPass, self).__init__()
        loadUi(r'..\Resource\resetpass.ui', self)
        self.resetbutton.clicked.connect(self.sendMail)
        self.backButton.clicked.connect(self.backtoMain)
        self.sentMessage.setVisible(False)
        self.loginInvalidMessage.setVisible(False)

    def sendMail(self):
        email = self.email.text()
        try:
            m.auth.send_password_reset_email(email)
            self.sentMessage.setVisible(True)
            self.loginInvalidMessage.setVisible(False)
        except:
            self.loginInvalidMessage.setVisible(True)
            self.sentMessage.setVisible(False)

    def backtoMain(self):
        login = m.Login()
        m.widget.addWidget(login)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)

