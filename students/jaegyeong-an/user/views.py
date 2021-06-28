import json
import re

from django.views import View
from django.http  import JsonResponse
from django.db    import IntegrityError

from user.models  import User

REGEX = {
    'email'    : '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    'password' : '[A-Za-z0-9@#$%^&+=]{8,}'
    }

class SignUpView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if not re.match(REGEX['email'], email):
                return JsonResponse({'error':'INVALID_EMAIL'}, status=400)
            if not re.match(REGEX['password'], password):
                return JsonResponse({'error':'INVALID_PASSWORD'}, status=400)
                
            User.objects.create(
            email        = email,
            phone_number = data['phone_number'],
            name         = data['name'],
            nickname     = data['nickname'],
            password     = password
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'error':'KEY_ERROR'}, status=400)
        except IntegrityError:
            return JsonResponse({'error':'DUPLICATE_ENTRY'}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            account  = data['account']
            password = data['password']

            if re.match(REGEX['email'], account):
                if not User.objects.filter(email=account).exists():
                    return JsonResponse({'error': 'INVALID_USER'}, status=401)
                if User.objects.get(email=account).password == password:
                    return JsonResponse({'message':'SUCCESS'}, status=200)
            else:
                if not User.objects.filter(phone_number=account).exists():
                    return JsonResponse({'error': 'INVALID_USER'}, status=401)
                if User.objects.get(phone_number=account).password == password:
                    return JsonResponse({'message':'SUCCESS'}, status=200)
            return JsonResponse({'error': 'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'error': 'KEY_ERROR'}, status=400)