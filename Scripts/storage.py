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
storage = firebase.storage()
#filename = input("Enter file name: ")
#cloudFileName = input("Enter cloud file name: ")
#storage.child(cloudFileName).put(filename)
#print(storage.child('xyz.txt').get_url(None))
storage.child("xyz.txt").download( 'downloaded.txt')