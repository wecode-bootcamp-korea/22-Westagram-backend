import re


def validate_email(email):
    email_regex = re.compile("^[^@\s]+@[^@\s\.]+\.[^@\.\s]+$")
    return email_regex.match(email)

def validate_password(password):
    password_regex = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")
    return password_regex.match(password)