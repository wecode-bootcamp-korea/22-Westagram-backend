import json 

from django.core.validators  import validate_email
from django.core.exceptions  import ValidationError
from django.http             import JsonResponse
from django.db               import IntegrityError
from django.views            import View 

from users.models            import User
from users.validations       import password_check, email_check

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
            
            User.objects.create(
                email        = email,
                password     = password,
                phone_number = phone_number,
                name         = name
            )
            return JsonResponse({"message":"SUCCESS"},status = 201)
        

        except KeyError: 
            return JsonResponse({"MESSAGE":"KEY_ERROR"},status=400)
        except ValidationError: 
            return JsonResponse({"message":"VALIDATION_ERROR"},status=400)
                



