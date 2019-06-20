import pyrebase
# import firebase_admin
# from firebase_admin import credentials

config = {
    'apiKey': "AIzaSyC2CVMqiMtRfDceq2RepxToiSbAnQ1aNMM",
    'authDomain': "myapi-c7e3b.firebaseapp.com",
    'databaseURL': "https://myapi-c7e3b.firebaseio.com",
    'projectId': "myapi-c7e3b",
    'storageBucket': "myapi-c7e3b.appspot.com",
    'messagingSenderId': "935963960585",
    'appId': "1:935963960585:web:542b850bfa2140e4",
    'serviceAccount': "/home/mrunalini/Downloads/myapi-c7e3b-firebase-adminsdk-u4ibh-6bbb6fe678.json"
  }

# cred = credentials.Certificate("/home/mrunalini/Downloads/myapi-c7e3b-firebase-adminsdk-u4ibh-6bbb6fe678.json")
# firebase = firebase_admin.initialize_app(cred, config)
fb = pyrebase.initialize_app(config)

auth = fb.auth()
db = fb.database()

useremail = "123@abc.org"
userpass = "testing123"
myuser = auth.sign_in_with_email_and_password(useremail, userpass)
token = myuser['idToken']

def push(token, drive_obj, **user_obj):
    drive = {"user":drive_obj.user,
        "title":drive_obj.title,
        "file":drive_obj.file,
        "image":drive_obj.image}
    db.child("uploads").child(drive_obj.id).push(drive, token)
    print(drive)
    return drive

def get(token, **user_obj):
    all_data = db.child("uploads").get(token).val()
    print(all_data)
    return all_data

def update(token, changes, drive_obj, user_obj):
    db.child(user_obj.username).child(drive_obj.id).update(changes, token)
    changes = db.child(user_obj.username).child(drive_obj.id)
    print(changes)
    return changes

def delete(token, drive_obj, user_obj):
    db.child(user_obj.username).child(drive_obj.id).delete(token)
    print("Object deleted successfully")
