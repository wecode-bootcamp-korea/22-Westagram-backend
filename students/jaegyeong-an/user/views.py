import json
import re

from django.views import View
from django.http  import JsonResponse
from django.db    import IntegrityError

from user.models  import User

class SignUpView(View):
    def post(self, request):
        REGEX = {
            'email'    : '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
            'password' : '[A-Za-z0-9@#$%^&+=]{8,}'
        }
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if not REGEX['email'].match(email):
                return JsonResponse({'error':'INVALID_EMAIL'}, status=400)
            if not REGEX['password'].match(password):
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
        data = json.loads(request.body)
        try:
            email    = data['email']
            password = data['password']

            if not User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'INVALID_USER'}, status=401)
            if User.objects.get(email=email).password == password:
                return JsonResponse({'message':'SUCCESS'}, status=200)
            return JsonResponse({'error': 'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'error': 'KEY_ERROR'}, status=400)