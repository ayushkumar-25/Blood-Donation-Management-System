import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import home as h
import createacc as acc
import resetpass as req

firebaseConfig = {'apiKey': "AIzaSyD-UKONeVgyG4wmi7Rym-lZYIn9CDpLI3Y",
                  'authDomain': "fir-auth-ddfd6.firebaseapp.com",
                  'databaseURL': "https://fir-auth-ddfd6-default-rtdb.firebaseio.com/",
                  'projectId': "fir-auth-ddfd6",
                  'storageBucket': "fir-auth-ddfd6.appspot.com",
                  'messagingSenderId': "247106769958",
                  'appId': "1:247106769958:web:9df424102f1e67d92442e7",
                  'measurementId': "G-87VT2PCEEY"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi(r'..\Resource\login.ui', self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.forgetPassButton.clicked.connect(self.gotoReset)
        self.loginInvalidMessage.setVisible(False)
        self.loginMessage.setVisible(False)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        try:
            auth.sign_in_with_email_and_password(email, password)
            self.gotoHome()
            # self.loginInvalidMessage.setVisible(False)
            # self.loginMessage.setVisible(True)

        except:
            self.loginInvalidMessage.setVisible(True)
            self.loginMessage.setVisible(False)

    def gotocreate(self):
        createacc = acc.CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoHome(self):
        home = h.Home()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoReset(self):
        reset = req.ResetPass()
        widget.addWidget(reset)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)  # create pyqt5 app
mainwindow = Login()  # create the instance of our Window
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.setWindowTitle('Blood Bank')
widget.setWindowIcon(QtGui.QIcon(r'..\Resource\icon.jpg'))
widget.show()  # show all the widgets
sys.exit(app.exec_())  # start the app
#app.exec_()
