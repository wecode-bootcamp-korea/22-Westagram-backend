import re
import json

from django.core.exceptions import MultipleObjectsReturned
from django.views           import View
from django.http            import JsonResponse

from users.models           import User
from users.validators       import validate_email, validate_password

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not validate_email(data['email']):
                return JsonResponse({'MESSAGE': 'INVALID_EMAIL'}, status=400)

            if not validate_password(data['password']):
                return JsonResponse({'MESSEAGE': 'INVALID_PASSWORD'}, status=400)

            User.objects.create(
                phone_number =data['phone_number'],
                email        =data['email'],
                name         =data['name'],
                nickname     =data['nickname'],
                password     =data['password'],
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KeyError'}, status=404)

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            User.objects.get(email=data['email'], password=data['password'])
            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'messege': 'KeyError'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message': 'Invalid_User'}, status=401)

        except MultipleObjectsReturned:
            return JsonResponse({'message': 'Invalid_User'}, status=401)