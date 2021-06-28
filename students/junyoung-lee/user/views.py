import json

from django.db.utils import IntegrityError
from django.http     import JsonResponse
from django.views    import View

from user.models     import User
from user.validators import (
    validate_email, 
    validate_password, 
    validate_name, 
    validate_phone_number
)

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not validate_email(data['email']):
                return JsonResponse({'MESSAGE':'INVALID_EMAIL'}, status = 400)
            
            if not validate_password(data['password']):
                return JsonResponse({'MESSAGE':'INVALID_PASSWORD'}, status = 400)
            
            if not validate_name(data['name']):
                return JsonResponse({'MESSAGE':'INVALID_NAME'}, status = 400)
            
            if not validate_phone_number(data['phone_number']):
                return JsonResponse({'MESSAGE':'INVALID_PHONE_NUMBER'}, status = 400)
            
            User.objects.create(
                name         = data['name'],
                nickname     = data['nickname'],
                email        = data['email'],
                phone_number = data['phone_number'],
                password     = data['password'],
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

        except IntegrityError:
            return JsonResponse({'MESSAGE':'USER_ALREADY_EXISTS'}, status=400)

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if 'email' in data:
                User.objects.get(email=data['email'], password=data['password'])
            
            elif 'phone_number' in data:
                User.objects.get(phone_number=data['phone_number'], password=data['password'])

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)