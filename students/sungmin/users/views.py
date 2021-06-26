import json, re

from django.views   import View
from django.http    import JsonResponse

from .models        import User


class SignUpView(View):
     def post(self, request):
        data                 = json.loads(request.body)
        email_regex          = re.compile(r'^[a-zA-Z0-9+-._]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        password_regex       = re.compile(r'[a-zA-Z0-9`~!@#$%^&*()_+-={};:",./<>?]{8,25}')

        try:
            if not email_regex.match(data['email']):
                return JsonResponse({"message":"Invald_email_format"}, status=400)
            if not password_regex.match(data['password']):
                return JsonResponse({"message":"Invalid_password"}, status=400)
            if User.objects.filter(phonenumber=data['phonenumber']).exists():
                return JsonResponse({"message":"Phonenumber_exist"}, status=400)
            if User.objects.filter(nick_name=data['nick_name']).exists():
                return JsonResponse({"message":"nick_name_exist"}, status=400)    
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message":"email_exist"}, status=400)

            User.objects.create(
                email        = data['email'],
                password     = data['password'],
                phonenumber  = data['phonenumber'],
                nick_name    = data['nick_name'],               
                )
            return JsonResponse({"message": "SUCCESS!"}, status=200)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)