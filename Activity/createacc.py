import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import main as m
import home as h


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi(r'..\Resource\createacc.ui', self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.backButton.clicked.connect(self.backtoMain)
        self.invalid.setVisible(False)

    def backtoMain(self):
        login = m.Login()
        m.widget.addWidget(login)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)

    def createaccfunction(self):
        name = self.name.text()
        name = name.title()
        age = self.age.text()
        bloodGroup = self.bloodGroup.currentText()
        location = self.location.currentText()
        phoneNumber = self.phoneNo.text()
        email = self.email.text()
        if (len(name) != 0 and len(age) != 0):
            if self.password.text() == self.confirmpass.text():
                password = self.password.text()
                if len(password) >= 6:
                    if len(phoneNumber) == 10:
                        try:
                            m.auth.create_user_with_email_and_password(email, password)
                            data = {'Name': name, 'Age': age, 'Blood Group': bloodGroup, 'Location': location,
                                    'Phone Number': phoneNumber}
                            m.db.child('Users').child(name+password).set(data)
                            # m.auth.sign_in_with_email_and_password(email, password)
                            home = h.Home()
                            # login = m.Login()
                            m.widget.addWidget(home)
                            m.widget.setCurrentIndex(m.widget.currentIndex() + 1)
                        except:
                            self.invalid.setText('Please enter valid email.')
                            self.invalid.setVisible(True)
                    else:
                        self.invalid.setText('Please enter valid phone number.')
                        self.invalid.setVisible(True)
                else:
                    self.invalid.setText('Password must have min 6 letters.')
                    self.invalid.setVisible(True)
            else:
                self.invalid.setText('Password not Matching.')
                self.invalid.setVisible(True)
        else:
            self.invalid.setText('Please enter valid Name and Age.')
            self.invalid.setVisible(True)

