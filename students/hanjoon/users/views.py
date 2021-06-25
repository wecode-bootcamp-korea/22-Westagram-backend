import json

from django.http import JsonResponse
from django.views import View

from users.models import User

class StargramView(View):
    def post(self, request):
       
        data = json.loads(request.body)

        print('==============')
        print(data["email"])
        print('==============')

        email              = data["email"]
        phone_number       = data["phone_number"]
        email_check        = User.objects.filter(email=email).exists()
        Phone_number_check = User.objects.filter(phone_number=phone_number).exists()

        if email_check:
            return JsonResponse({"MESSAGE":"중복된 회원정보입니다"})

        if Phone_number_check:
            return JsonResponse({"MESSAGE":"중복된 회원정보입니다"})

        if "@" not in data["email"] or "." not in data["email"]:
            return JsonResponse ({"message":"email 주소 형식을 확인해주세요"})        

        if len(data['password']) < 8:
            return JsonResponse ({"message":"비밀번호는 최소 8자 이상입니다"})
        else:
            pass

        try:
            User.objects.create(
                name         = data["name"],
                password     = data["password"],
                email        = data["email"],
                phone_number = data["phone_number"],
                nickname     = data["nickname"]
            )
            return JsonResponse({"message":"SUCCESS"}, status = 201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)

            
