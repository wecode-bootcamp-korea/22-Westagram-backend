import re

def email_validate(value):
    email_validation = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    return email_validation.match(value)

def password_validate(value):
    password_validation = re.compile('[A-Za-z0-9!@#$%^&*()_+=-]{8,20}')

    return password_validation.match(value)