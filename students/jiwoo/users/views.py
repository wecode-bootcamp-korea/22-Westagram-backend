import json, bcrypt, jwt

from django.http             import JsonResponse
from django.views            import View 

from users.models            import User
from users.validations       import email_check, password_check, create_bcrypt, check_bcrypt, create_jwt
from my_settings             import SECRET_KEY


class SignupsView(View)  : 
    def post(self, request):         
        try: 
            data         = json.loads(request.body)
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            name         = data['name']

            if not email_check(email): 
                return JsonResponse({"message":"INVALID_EMAIL_OR_PASSWORD"},status=400)

            if not password_check(password): 
                return JsonResponse({"message":"INVALID_EMAIL_OR_PASSWORD"},status=400)

            if User.objects.filter(email=email).exists(): 
                return JsonResponse({"message":"EMAIL_ALREADY_EXISTS"},status=400)     

            if User.objects.filter(phone_number=phone_number).exists(): 
                return JsonResponse({"message":"PHONE_NUMBER_ALREADY_EXISTS"},status=400)

            if User.objects.filter(name=name).exists(): 
                return JsonResponse({"message":"NAME_ALREADY_EXISTS"},status=400)

            hashed_password  = create_bcrypt(password)
            decoded_password = hashed_password.decode()

            User.objects.create(
                email        = email,
                password     = decoded_password,
                phone_number = phone_number,
                name         = name
            )
            return JsonResponse({"message":"SUCCESS"},status = 201)      
        except KeyError: 
            return JsonResponse({"MESSAGE":"KEY_ERROR"},status=400)


class SigninsView(View)  : 
    def post(self, request): 
        try: 
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if not User.objects.filter(email=email).exists(): 
                return JsonResponse({"message":"INVALID_USER"},status=401)

            hashed_password = User.objects.get(email=email).password.encode('utf-8')
            if not check_bcrypt(password, hashed_password): 
                return JsonResponse({"message":"INVALID_USER"},status=401)

            num          = User.objects.get(email=email).id
            access_token = create_jwt(num)
            
            return JsonResponse({"message":"SUCCESS", "access_token": access_token},status= 200)
        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status = 400)