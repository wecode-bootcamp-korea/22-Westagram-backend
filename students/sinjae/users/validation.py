import re
from users.models                 import User

email_regex     = '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
phone_regex     = '[0-9]{10,12}'
password_regex  = '[a-zA-Z0-9\!\@\#\$\?]{8,}'

def email_validation(email):
    return re.match(email_regex, email)

def password_validation(password):
    return re.match(password_regex, password)

def phone_validation(phone_number):
    return re.match(phone_regex, phone_number)

