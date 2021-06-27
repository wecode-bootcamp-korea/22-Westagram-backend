import re

from django.core.exceptions import ValidationError
# from django.core.validators import validate_email

# # email validation (validate_email: 장고 모듈 함수)
# def validate_email_django(email):
#     try:
#         validate_email(email)
#     except ValidationError:
#         raise ValidationError

# email validation (정규표현식)
def validate_email_regex(email):
    email_validation = re.compile('^[a-zA-Z0-9]+[a-zA-Z0-9+-_.]*@+[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not email_validation.match(email):
        raise ValidationError

# password validation
def validate_password(password):
    password_validation = re.compile('[a-zA-Z0-9]{8,45}')
    if not password_validation.match(password):
        raise ValidationError

# phone number input check (입력값 중간 '-' 혹은 '.' 제거하기)
def check_phone_number(phone):
    phone_checked = re.sub('[-.]', '', phone)
    return phone_checked
    