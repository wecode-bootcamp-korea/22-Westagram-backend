import json
import base64
import hashlib

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist,ValidationError

from . models               import User
from . validation           import expression
   
class UserView(View) :
    def post(self,request) :
        def encriptpassword(password) :
            return hashlib.sha256(base64.b64encode(password.encode("ascii"))).hexdigest()
            
        try :
            user_data = json.loads(request.body)  
            
            if not (expression.vaild_check("phone_number",user_data['phone_number'])) :
                raise ValidationError("phone_number")

            if not (expression.vaild_check("email",user_data['email'])) :
                raise ValidationError("email")

            if(len(user_data['password']) < 8) :
                raise ValidationError("password")

            if  User.objects.filter(phone_number=user_data['phone_number']).exists() :
                return JsonResponse({'MESSAGE':'DUPLE_ERROR'}, status=400)

            if User.objects.filter(email=user_data['email']).exists() :
                return JsonResponse({'MESSAGE':'DUPLE_ERROR'}, status=400)

            if User.objects.filter(full_name=user_data['full_name']).exists() : 
                return JsonResponse({'MESSAGE':'DUPLE_ERROR'}, status=400)  
            
            User.objects.create(
                phone_number    = user_data['phone_number'],
                email           = user_data['email'],
                full_name       = user_data['full_name'],
                password        = encriptpassword(user_data['password']),
                nick_name       = user_data['nick_name']
            )    

        except KeyError :
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

        except ValidationError as err:
            return JsonResponse({'MESSAGE':err.message}, status=400)
        
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)


