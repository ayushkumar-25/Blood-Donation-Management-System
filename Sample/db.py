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
l = ['A+', 'A-', 'O+', 'O-']
users = db.child('Users').child().get()
for user in users.each():
    #for i in l:
        if user.val()['Blood Group'] == 'A+' and user.val()['Location'] == 'Ranchi':
            print(user.val())


#
#
# n = int(input('Enter number of data entry: '))
# for i in range(n):
#     l1 = ['Name', 'Blood Group', 'Location']
#     l2 = input('Enter [Name, Blood Group, Location]: ').split(', ')
#     data = dict(zip(l1, l2))
#     db.child('Users').child().push(data)
# users = db.child('Users').get()
# for user in users.each():
#     if user.val()['Address'] == 'Ranchi' or user.val()['Age'] == '2':
#         print(user.val()['Name'])
# data = db.child('Users').child('Ayush Kumar').get()
# print(data.val())
#
# data = {'Name': 'Rohit Raj', 'Age': 21, 'Address': 'Ara'}
# #db.child("User").child('Ayush').update({'name': 'Ayush Kumar'})
# db.child("Users").child().push(data)
# data = {'Name': 'name', 'Age': 'age', 'Blood Group': 'bloodGroup', 'Location': 'location'}
# db.child('Users').child('email').push(data)
# user = db.child('User').get()
# for users in user.each():
#     if users.val()['Name'] == 'Ayush Kumar':
#         db.child('User').child(users.key()).update({'name': None})
#
# db.child('User').remove()

