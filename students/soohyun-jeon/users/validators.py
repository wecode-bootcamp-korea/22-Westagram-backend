import re

def validate_email(email):
    email_regex = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.search(email_regex, email)

def validate_password(password):
    password_regex = '[a-zA-Z0-9!@##$%^&+=]{8,}'
    return re.search(password_regex, password)
