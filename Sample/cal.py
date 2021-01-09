import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Front(QDialog):
    def __init__(self):
        super(Front, self).__init__()
        loadUi('front.ui', self)
        self.pushButton.clicked.connect(self.add)

    def add(self):
        num1 = int(self.lineEdit_1.text())
        num2 = int(self.lineEdit_2.text())
        result = num1 + num2
        self.lcdNumber.display(result)


app = QApplication(sys.argv)
Front = Front()
widget = QtWidgets.QStackedWidget()
widget.addWidget(Front)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
