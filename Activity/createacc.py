import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import main as m


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi(r'..\Resource\createacc.ui', self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.backButton.clicked.connect(self.backtoHome)
        self.invalid.setVisible(False)

    def backtoHome(self):
        login = m.Login()
        m.widget.addWidget(login)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)

    def createaccfunction(self):
        name = self.name.text()
        age = self.age.text()
        bloodGroup = self.bloodGroup.currentText()
        location = self.location.currentText()
        phoneNumber = self.phoneNo.text()
        email = self.email.text()

        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            try:
                m.auth.create_user_with_email_and_password(email, password)
                data = {'Name': name, 'Age': age, 'Blood Group': bloodGroup, 'Location': location,
                        'Phone Number': phoneNumber}
                m.db.child('Users').child().push(data)
                login = m.Login()
                m.widget.addWidget(login)
                m.widget.setCurrentIndex(m.widget.currentIndex() + 1)
            except:
                self.invalid.setVisible(True)
        else:
            self.invalid.setVisible(True)
