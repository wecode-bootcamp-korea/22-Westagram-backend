import json, bcrypt, jwt

from django.core.validators  import validate_email
from django.core.exceptions  import ValidationError
from django.http             import JsonResponse
from django.db               import IntegrityError
from django.views            import View 

from users.models            import User
from users.validations       import password_check, create_bcrypt, check_bcrypt, create_jwt
from my_settings             import SECRET_KEY


class SignupsView(View)  : 
    def post(self, request): 
        
        try: 
            data         = json.loads(request.body)
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            name         = data['name']

            validate_email(email)
            if not password_check(password): 
                return JsonResponse({"message":"INVALID_EMAIL_OR_PASSWORD"},status=400)
            hashed_password  = create_bcrypt(password)
            decoded_password = hashed_password.decode()

            User.objects.create(
                email        = email,
                password     = decoded_password,
                phone_number = phone_number,
                name         = name
            )
            return JsonResponse({"message":"SUCCESS"},status = 201)
        
        # exists()메소드 대신에 사용(models.py에 unique=True 설정)
        except IntegrityError: 
            return JsonResponse({"message":"INFORMATION_ALREAYD_EXISTS"},status=400)
        except KeyError: 
            return JsonResponse({"MESSAGE":"KEY_ERROR"},status=400)
        except ValidationError: 
            return JsonResponse({"message":"VALIDATION_ERROR"},status=400)
                

class SigninsView(View)  : 
    def post(self, request): 
        try                : 
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


