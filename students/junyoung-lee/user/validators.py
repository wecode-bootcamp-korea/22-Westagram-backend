import re

def validate_email(email): 
    email_regex = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.search(email_regex, email)

def validate_password(password):
    password_regex = '[A-Za-z0-9@#$%^&+=]{8,}'
    return re.search(password_regex, password)

def validate_name(name):
    name_regex = '''^([A-Z][a-z]+([ ]?[a-z]?['-]?[A-Z][a-z]+)*)$|^[가-힣]'''
    return re.search(name_regex, name)

def validate_phone_number(phone_number):
    phone_number_regex = '^[0-9]{3}[-]+[0-9]{3,4}[-]+[0-9]{4}$|^[0-9]{10,11}$'
    return re.search(phone_number_regex, phone_number)