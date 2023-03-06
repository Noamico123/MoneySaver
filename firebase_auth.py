import pyrebase

from secrets import firebase_config

firebase = pyrebase.initialize_app(firebase_config)

auth = firebase.auth()

