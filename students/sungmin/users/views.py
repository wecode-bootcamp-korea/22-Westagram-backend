import json, re, bcrypt, jwt
from django import views

from django.views   import View
from django.http    import JsonResponse

from my_settings    import SECRET_KEY
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

            
            
            hashed_password     = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            
           
            User.objects.create(
                email        = data['email'],
                password     = hashed_password.decode('utf-8'),
                phonenumber  = data['phonenumber'],
                nick_name    = data['nick_name'],               
                )
            return JsonResponse({"message": "SUCCESS!"}, status=200)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
       
        try:
            user = User.objects.get(email=data['email'])
              
            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            access_token = jwt.encode({"user_id": user.id},SECRET_KEY, algorithm='HS256')

            return JsonResponse({"message": "SUCCESS", "access_token": access_token}, status=200)


        except KeyError:
            return JsonResponse({'error': 'KEY_ERROR'}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({'error': 'INVALID_USER'}, status=401)                    
