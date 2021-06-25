import json 

from django.core.validators  import validate_email
from django.core.exceptions  import ValidationError
from django.http             import JsonResponse
from django.views            import View 
from users.models            import User

class SignupsView(View)  : 
def   post(self, request): 
        data         = json.loads(request.body)
        email        = data['email']
        password     = data['password']
        phone_number = data['phone_number']
        name         = data['name']
        
        try: 
            validate_email(email)
            valid_email = True
            print(valid_email)
            print(is_valid)
        except ValidationError: 
            return JsonResponse({"message":"VALIDATION_ERROR"},status=400)

        signup = User.objects.create(
            email        = email,
            password     = password,
            phone_number = phone_number,
            name         = name
        )
        return JsonResponse({"message":"SUCCESS"},status = 201)