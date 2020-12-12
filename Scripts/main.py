import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi(r'..\Resource\login.ui', self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        print("Successfully logged in with email: ", email, "and password:", password)

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi(r'..\Resource\createacc.ui', self)
        self.signupbutton.clicked.connect(self.createaccfunction)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            print("Successfully created acc with email: ", email, "and password: ", password)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)



app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
