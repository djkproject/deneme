import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
import datetime

cred = credentials.Certificate("path/to/serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)db = firestore.client()
firebase = firebase.FirebaseApplication('https://djkproject123-default-rtdb.firebaseio.com', None)


def create():
	    users_ref = ref.child('users')
	users_ref.set({
	    'alanisawesome': {
	        'date_of_birth': 'June 23, 1912',
	        'full_name': 'Alan Turing'
	    },
	    'gracehop': {
	        'date_of_birth': 'December 9, 1906',
	        'full_name': 'Grace Hopper'
	    }
	})
