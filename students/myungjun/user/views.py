import bcrypt
import json
import jwt

from django.http  import JsonResponse
from django.views import View

from .models     import User
from .validation import *
from my_settings import SECRET_KEY

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
           
            encoded_password = data['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

            User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = hashed_password.decode('utf-8'),
                phone    = data['phone'],
                nickname = data['nickname']
            )
            
            email = User.objects.get(email=data['email'])
            SECRET = SECRET_KEY
            token = jwt.encode({'id': email.id}, SECRET_KEY, algorithm='HS256')
            return JsonResponse({'message': 'SUCCESS', 'token': token}, status=201)    
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email            = User.objects.get(email = data['email'])
            encoded_password = data['password'].encode('utf-8')

            SECRET = SECRET_KEY
            token = jwt.encode({'id': email.id}, SECRET_KEY, algorithm='HS256')

            if bcrypt.checkpw(encoded_password, email.password.encode('utf-8')):
                return JsonResponse({'message': 'SUCCESS', 'token': token}, status=201)
            else:
                return JsonResponse({'message': 'INVALID_USER'}, status=401)
            
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)  

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)