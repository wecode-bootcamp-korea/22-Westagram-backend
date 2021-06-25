import re

from django.forms   import ValidationError

def check_email_validation(email):
    regex = r'^[a-z0-9]+[a-z0-9._-]*[a-z0-9]+[@][a-z0-9]+\.[a-z0-9]+[a-z0-9._-]*[a-z]$'
    
    if re.search(regex, email):
        return email
    else:
        raise ValidationError("EMAIL_ERROR")

def check_password_validation(password):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$'

    if re.search(regex, password):
        return password
    else:
        raise ValidationError("PASSWORD_ERROR")

def check_phone_validation(phone):
    regex = r'^(010)-?([\d]{4})-?([\d]{4})$'
    phone = re.search(regex, phone)

    if phone:
        return ''.join(phone.groups()) 
    else:
        raise ValidationError("PHONE_ERROR")

