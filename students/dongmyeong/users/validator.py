import re

def check_email_validation(email):
    regex = r'^[a-z0-9]+[a-z0-9._-]*[a-z0-9]+[@][a-z0-9]+\.[a-z0-9]+[a-z0-9._-]*[a-z]$'
    
    return re.match(regex, email)

def check_password_validation(password):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$'

    return re.match(regex, password)

def check_phone_validation(phone):
    regex = r'^(010)-([\d]{4})-([\d]{4})$'

    return re.match(regex, phone)
