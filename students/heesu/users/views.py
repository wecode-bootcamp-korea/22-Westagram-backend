import json
import re


from django.views           import View
from django.http            import JsonResponse, request
from django.core.exceptions import ObjectDoesNotExist,ValidationError
from . models               import User

EXPRESSION = {"email":'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',"phone_number":"\d{3}-\d{3,4}-\d{4}"}

def vaild_check(input_data) :
    def expression(**kwargs):
        key = list(kwargs.keys())[0]
        value = list(kwargs.values())[0]
        pattern = EXPRESSION[key]
        pattern_test = re.compile(pattern).match(value)
        print(key,value,pattern,pattern_test)

        if pattern_test == None :
            raise ValidationError(key + "_ERROR")
        
    for i in range(0,len(input_data)) :
        key = (list(input_data.keys())[i])
        value = (list(input_data.values())[i])

        if key == "phone_number" :
            expression(phone_number = value)

        elif key == "email" :
            expression(email = value) 

        elif key == "password" :    
            if len(input_data[key]) < 8 :
                 raise ValidationError("PASSWORD_ERROR")
   
class UserView(View) :
    def post(self,request) :

        try :
            user_data = json.loads(request.body)  
            vaild_check(user_data)                 
            
            if  User.objects.filter(phone_number=user_data['phone_number']).exists() :
                return JsonResponse({'MESSAGE':'DUPLE_ERROR'}, status=400)

            elif User.objects.filter(email=user_data['email']).exists() :
                return JsonResponse({'MESSAGE':'DUPLE_ERROR'}, status=400)

            elif User.objects.filter(full_name=user_data['full_name']).exists() : 
                return JsonResponse({'MESSAGE':'DUPLE_ERROR'}, status=400)  
            
            else : 
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


