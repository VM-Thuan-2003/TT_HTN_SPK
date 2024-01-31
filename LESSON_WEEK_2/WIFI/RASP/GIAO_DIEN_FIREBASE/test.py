import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./tt-htn-3-con-bao-firebase-adminsdk-bkjw3-a06594cb50.json")

firebase_admin.initialize_app(cred,{
    "databaseURL":"https://tt-htn-3-con-bao-default-rtdb.firebaseio.com/"
})

# create and set items in firebase
ref = db.reference('users/')
users_ref = ref.child("ssid")
users_ref.set({
    "name": "John Doe",
    "age": 25,
    "city": "New York"
})