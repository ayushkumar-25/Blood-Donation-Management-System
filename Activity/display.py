import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import requestblood as req
import main as m


class Display(QDialog):
    def __init__(self):
        super(Display, self).__init__()
        loadUi(r'..\Resource\display.ui', self)
        self.backButton.clicked.connect(self.backtoHome)

        # data = [{'Age': '22', 'Blood Group': 'A+', 'Location': 'Kolkata', 'Name': 'Rahul',
        #          'Phone Number': '9708942540'},
        #         {'Age': '32', 'Blood Group': 'O+', 'Location': 'Ranchi', 'Name': 'Aman', 'Phone Number': '1234567890'}]
        data = req.lis
        row = 0
        self.tableWidget.setRowCount(len(data))
        for person in data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['Name']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Age']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Blood Group']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Location']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['Phone Number']))
            row = row + 1

    def backtoHome(self):
        request = req.RequestBlood()
        m.widget.addWidget(request)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)
