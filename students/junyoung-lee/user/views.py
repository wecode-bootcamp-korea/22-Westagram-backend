import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views import View

from user.models import User
from user.validators import validate_email

class UserView(View):
    # def post(self, request):
    #     email_vaildator = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    #     data = json.loads(request.body)
    #     if (not data['email']) or (not data['password']):
    #         return JsonResponse({'message':'KEY_ERROR'}, status = 400)
    #     if 
    def post(self, request):
        data = json.loads(request.body)
        try:
            if len(data['password']) < 8:
                return JsonResponse({'MESSAGE':'PASSWORD_LENGTH_ERROR'}, status=400)
            # validate_email(data['email'])
            user = User.objects.create(
                name = data['name'],
                nickname = data['nickname'],
                email = data['email'],
                phonenumber = data['phonenumber'],
                password = data['password']
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except ValidationError as e:
            return JsonResponse({'MESSAGE':f'{e}'}, status=400)
