import re, jwt
from django.http import JsonResponse
from django.core.exceptions import ValidationError

from project_westagram.my_settings import ALGORITHM, SECRET_KEY
from user.models import User

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

def user_access(func):
    def wrapper_func(self, request, *args, **kwargs):
        try:
            access_token = request.headers['Authorization'] # None은모야
            payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
            request.user = User.objects.get(id=payload['user'])
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=400) # 400이뭐지
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper_func


