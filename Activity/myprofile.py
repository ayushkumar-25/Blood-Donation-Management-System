import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

import main as m
import home as h


class MyProfile(QDialog):
    global datum

    def __init__(self):
        global datum
        super(MyProfile, self).__init__()
        loadUi(r'..\Resource\myprofile.ui', self)
        self.backButton.clicked.connect(self.backtoHome)
        user = m.db.child('Users').get()
        for users in user.each():
            if users.val()['id'] == m.id:
                datum = [users.val()]

        row = 0
        self.tableWidget.setRowCount(len(datum))
        for person in datum:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['Name']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Age']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Blood Group']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Location']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['Phone Number']))
            row = row + 1

    def backtoHome(self):
        home = h.Home()
        m.widget.addWidget(home)
        m.widget.setCurrentIndex(m.widget.currentIndex() + 1)
