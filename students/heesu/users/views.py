import json
import bcrypt

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist,ValidationError

from . models               import User
from . validation           import expression
   
class UserView(View) :
    def post(self,request) :
 
            
        try :
            user_data = json.loads(request.body)  
            user_password = user_data['password']

            if not (expression.vaild_check("phone_number",user_data['phone_number'])) :
                raise ValidationError("phone_number")

            if not (expression.vaild_check("email",user_data['email'])) :
                raise ValidationError("email")

            if(len(user_password) < 8) :
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
                password        = bcrypt.hashpw(user_password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8'),
                nick_name       = user_data['nick_name']
            )
                
        except KeyError :
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

        except ValidationError as err:
            return JsonResponse({'MESSAGE':err.message}, status=400)

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)


class SigninView(View) :
    def get(self,request) :

        try :
            user_data       = json.loads(request.body)  
            input_email     = user_data['email']
            password        = user_data['password']

            if not User.objects.filter(email=input_email).exists() :
                return JsonResponse({'message':'INVALID_USER'}, status=401)

            hashed_password = User.objects.get(email=input_email).password
                
            if (bcrypt.checkpw(password.encode('utf-8'),hashed_password.encode('utf-8')) == False) :
                return JsonResponse({'message':'INVALID_USER'}, status=401)

        except KeyError :
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

        except ValidationError as err:
            return JsonResponse({'MESSAGE':err.message}, status=400)

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)