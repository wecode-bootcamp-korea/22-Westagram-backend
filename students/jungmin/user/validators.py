import re

from django.core.exceptions import ValidationError

def validate_email_regex(email):
    email_validation = re.compile('^[a-zA-Z0-9]+[a-zA-Z0-9+-_.]*@+[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not email_validation.match(email):
        raise ValidationError('ValidationError')

def validate_password(password):
    password_validation = re.compile('[a-zA-Z0-9]{8,45}')
    if not password_validation.match(password):
        raise ValidationError('ValidationError')

def validate_phone(phone):
    phone_validation = re.compile('[0-9]{11}')
    if not phone_validation.match(phone):
        raise ValidationError('ValidationError')
