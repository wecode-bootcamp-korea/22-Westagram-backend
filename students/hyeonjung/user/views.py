import json
import re
import bcrypt
import jwt

from django.http     import JsonResponse
from django.views    import View
from django.db       import IntegrityError 
from django.core.exceptions import MultipleObjectsReturned

from .models import User

class SignUpView(View):
    def post(self,request):
        try:
            data = json.loads(request.body) 
            
            REGEX_EMAIL        = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            REGEX_PASSWORD     = re.compile(r'^[a-zA-Z0-9]{8,20}$')
            REGEX_PHONE_NUMBER = re.compile(r'^[0-9]{10,20}')

            if not REGEX_PHONE_NUMBER.match(data['phone_number']):
                return JsonResponse({"message" : "Invalid_phone_number_foramt"} , status = 400)
            if not REGEX_PASSWORD.match(data['password']):
                return JsonResponse({"message" : "Invalid_password_foramt"} , status = 400)
            if not REGEX_EMAIL.match(data['email']):
                return JsonResponse({"message" : "Invald_email_format"} , status = 400) 
            
            if User.objects.filter(phone_number=data['phone_number']).exists(): 
                return JsonResponse({"message" : "phone_number_exist"} , status = 400) 
            if User.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({"message" : "nickname_exist"} , status = 400)
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message" : "email_exist"} , status = 400)

            hashed_password =bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt()) 

            user = User.objects.create(
                name         = data['name'], 
                nickname     = data['nickname'],
                email        = data['email'],
                password     = hashed_password.decode('utf-8'),
                phone_number = data['phone_number'],
            )
            return JsonResponse( {"message": "SUCCESS"} , status = 201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"} , status = 400)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user =  User.objects.get(email=data['email'])
            
            if bcrypt.checkpw(data['password'].encode('utf-8'),user.password.encode('utf-8')):
                token = jwt.encode({'id':user.id}, 'secret_key' , algorithm="HS256")
                return JsonResponse( {"message": "SUCCESS", "token": token} , status = 201) 
            
            return JsonResponse({"message" : "INVALID_USER"}, status = 401)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"} , status = 400)
        
        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status = 401)
        
        except IntegrityError:
            return JsonResponse({"message" : "INTEGERITY_ERROR"}, status = 400)
        
        except MultipleObjectsReturned:
            return JsonResponse({"message" : "MULTIPLE_OBJECT_RETURNED"}, status = 400)
            


