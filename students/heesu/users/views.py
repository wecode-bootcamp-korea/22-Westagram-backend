import json
import re


from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from . models                 import User

REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PHONE = '\d{3}-\d{3,4}-\d{4}'



def null_check(input_data) :
    for k,v in enumerate(input_data) :

        if v == None :
           return JsonResponse({'MESSAGE':'NULL_ERROR'}, status=400) 

        else :
            return input_data   

  



def vaild_check(input_data) :

    try :

        not_duple_data = []

        for k,v in enumerate(input_data) :

            if k == "email" :
                v = re.compile(REGEX_EMAIL).match

                if v == None :
                    return JsonResponse({'MESSAGE':'EMAIL_ERROR'}, status=400)
                User.objects.get(email = v)


            if k == "phone_number" :
                v = re.compile(REGEX_PHONE).match

                if v == None :
                    return JsonResponse({'MESSAGE':'PHOMENIMBER_ERROR'}, status=400)
                User.objects.get(phone_number = v)    

            if k == "pasword" :

                if len(v) < 8 :
                    return JsonResponse({'MESSAGE':'PASSWORD_LENTH_ERROR'}, status=400)

            if k == "full_name" :
                User.objects.get(phone_number = v)  

            return not_duple_data 

    except ObjectDoesNotExist :
        not_duple_data.append(v)


class UserView(View) :
    def post(self,request) :

        try :
            user_data = json.loads(request.body)  
            user_data = null_check(user_data)                    
            if len(vaild_check(user_data)) == 3 :           
                print(vaild_check(user_data))
                print(user_data)

        except KeyError :
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
