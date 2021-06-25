import json

from django.http     import JsonResponse
from django.views    import View

from .models import User

class UserView(View):
    def post(self,request):
        try:
            data = json.loads(request.body) 
            if len(data['phone_number']) < 11:
                return JsonResponse({"message" : "Invalid_phone_number_foramt"} , status = 400)
            if len(data['password']) < 8:
                return JsonResponse({"message" : "Invalid_password_foramt"} , status = 400)
            if '@' not in data['email'] or '.' not in data['email']: 
                return JsonResponse({"message" : "Invald_email_format"} , status = 400) 
            if User.objects.filter(phone_number=data['phone_number']).exists(): 
                return JsonResponse({"message" : "phone_number_exist"} , status = 400) 
            if User.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({"message" : "nickname_exist"} , status = 400)
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message" : "email_exist"} , status = 400)

            user = User.objects.create(
                name         = data['name'], 
                nickname     = data['nickname'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],
            )
            return JsonResponse( {"message": "SUCCESS"} , status = 201)
        
        except Exception as e:
            return JsonResponse ( {"message": f"KEY_ERROR : {e}"} , status = 400)    
