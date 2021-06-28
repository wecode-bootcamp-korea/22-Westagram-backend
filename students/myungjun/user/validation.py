import re

def email_validate(email):
    regex_email = re.compile(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    )
    match = regex_email.match(email)
    return bool(match)

def password_validate(password):
    regex_password = re.compile(
        r'[a-zA-Z0-9`~!@#$%^&*()_+-={};:",./<>?]{8,25}'
    )
    match = regex_password.match(password)
    return bool(match)

def phone_validate(phone):
    regex_phone = re.compile(
        r'^01[1|2|7|8|0|9]-?[0-9]{3,4}-?[0-9]{4}$'
    )
    match = regex_phone.match(phone)
    return bool(match)