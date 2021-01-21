import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

firebaseConfig = {'apiKey': "AIzaSyD-UKONeVgyG4wmi7Rym-lZYIn9CDpLI3Y",
                  'authDomain': "fir-auth-ddfd6.firebaseapp.com",
                  'databaseURL': "https://fir-auth-ddfd6-default-rtdb.firebaseio.com/",
                  'projectId': "fir-auth-ddfd6",
                  'storageBucket': "fir-auth-ddfd6.appspot.com",
                  'messagingSenderId': "247106769958",
                  'appId': "1:247106769958:web:9df424102f1e67d92442e7",
                  'measurementId': "G-87VT2PCEEY"}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


class Table(QDialog):
    def __init__(self):
        super(Table, self).__init__()
        loadUi(r'table.ui', self)
        self.loadData()

    def loadData(self):
        # users = db.child('Users').child().get()
        # for user in users.each():
        #     if user.val()['Blood Group'] == 'A+' and user.val()['Location'] == 'Ranchi':
        #         data = (user.val())
        data = [{'Age': '22', 'Blood Group': 'A+', 'Location': 'Kolkata', 'Name': 'Rahul',
                 'Phone Number': '9708942540'},
                {'Age': '32', 'Blood Group': 'O+', 'Location': 'Ranchi', 'Name': 'Aman', 'Phone Number': '1234567890'}]
        row = 0
        self.tableWidget.setRowCount(len(data))
        for person in data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person['Name']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person['Age']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person['Blood Group']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person['Location']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person['Phone Number']))
            row = row + 1


app = QApplication(sys.argv)
mainwindow = Table()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
widget.show()
sys.exit(app.exec_())
