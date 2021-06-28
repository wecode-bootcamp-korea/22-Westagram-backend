import json

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist,ValidationError

from . models               import User
from . validation           import expression
   
class UserView(View) :
    def post(self,request) :

        try :
            user_data = json.loads(request.body)  
            expression.vaild_check(user_data)                 
            
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
                password        = user_data['password'],
                nick_name       = user_data['nick_name']
            )    

        except KeyError :
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

        except ValidationError as err:
            return JsonResponse({'MESSAGE':err.message}, status=400)
        
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)


