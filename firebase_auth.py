import pyrebase

from auth_secret import firebase_config

firebase = pyrebase.initialize_app(firebase_config)

auth = firebase.auth()

