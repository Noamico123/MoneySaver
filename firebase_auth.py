from typing import Dict

import pyrebase
import requests

from consts import INVALID_EMAIL, EMAIL_EXISTS, EMAIL_NOT_FOUND, INVALID_PASSWORD
from secret import firebase_config

firebase = pyrebase.initialize_app(firebase_config)

auth = firebase.auth()


def is_sign_up() -> bool:
    email = input('Enter email: ')
    password = input('Enter password: ')

    try:
        auth.create_user_with_email_and_password(email, password)
        print(f'Successfully created account to {email}')
        return True

    except requests.exceptions.HTTPError as exc:
        if INVALID_EMAIL in exc.strerror:
            print(INVALID_EMAIL)
        elif EMAIL_EXISTS in exc.strerror:
            print(EMAIL_EXISTS)

    except Exception as e:
        print('Could not create an account')

    return False


def is_logged_in() -> Dict:
    email = input('Enter email: ')
    password = input('Enter password: ')

    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print(f'Successfully logged in')

        return auth.get_account_info(login["idToken"])

    except requests.exceptions.HTTPError as exc:
        if INVALID_EMAIL in exc.strerror:
            print(INVALID_EMAIL)
        elif EMAIL_NOT_FOUND in exc.strerror:
            print(EMAIL_NOT_FOUND)
        elif INVALID_PASSWORD in exc.strerror:
            print(INVALID_PASSWORD)

    except Exception as e:
        print(f'Could not log in that account \n{e}')

    return {}
