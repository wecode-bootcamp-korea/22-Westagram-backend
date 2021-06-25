import json 

from django.core.validators  import validate_email
from django.core.exceptions  import ValidationError
from django.http             import JsonResponse
from django.views            import View 
from users.models            import User
from users.validations       import password_check
from django.db               import IntegrityError

class SignupsView(View)  : 
def   post(self, request): 
        
        try: 
            data         = json.loads(request.body)
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            name         = data['name']

            validate_email(email)
            if not password_check(password): 
                return JsonResponse({"message":"INVALID_EMAIL_OR_PASSWORD"})
            
            signup = User.objects.create(
                email        = email,
                password     = password,
                phone_number = phone_number,
                name         = name
            )
            return JsonResponse({"message":"SUCCESS"},status = 201)
        
        except IntegrityError: 
            return JsonResponse({"message":"INFORMATION_ALREAYD_EXISTS"},status=400)
        except KeyError: 
            return JsonResponse({"MESSAGE":"KEY_ERROR"},status=400)
        except ValidationError: 
            return JsonResponse({"message":"VALIDATION_ERROR"},status=400)
                
