import json
import re

from django.http     import JsonResponse
from django.views    import View

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

            user = User.objects.create(
                name         = data['name'], 
                nickname     = data['nickname'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],
            )
            return JsonResponse( {"message": "SUCCESS"} , status = 201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"} , status = 400)
