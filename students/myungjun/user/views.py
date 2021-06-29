import json

from django.http import JsonResponse
from django.views import View

from .models import User
from .validation import *

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not password_validate(data['password']):
               return JsonResponse({'message': 'INVALID_FORMAT'}, status=409)
            
            if not email_validate(data['email']):
              return JsonResponse({'message': 'INVALID_FORMAT'}, status=409)

            if not phone_validate(data['phone']):
                return JsonResponse({'message': 'INVALID_FORMAT'}, status=409)
             
            if User.objects.filter(name=data['name']).exists():
                return JsonResponse({'message': 'ALREADY_REGISTERED'}, status=409)
           
            if User.objects.filter(email=data['email']).exists():
               return JsonResponse({'message': 'ALREADY_REGISTERED'}, status=409)
           
            if User.objects.filter(phone=data['phone']).exists():
               return JsonResponse({'message': 'ALREADY_REGISTERED'}, status=409)
           
            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = data['password'],
                phone    = data['phone'],
                nickname = data['nickname']
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)    
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
