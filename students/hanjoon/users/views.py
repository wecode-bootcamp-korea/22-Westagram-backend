import json, re

from django.http import JsonResponse
from django.views import View

from users.models import User

class StargramView(View):
    def post(self, request):
       
        data = json.loads(request.body)
        email_reges = "p = re.compile(‘^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$’)"

        email              = data["email"]
        phone_number       = data["phone_number"]
        Phone_number_check = User.objects.filter(phone_number=phone_number).exists()

        if re.search(email_reges, data["email"]) != None:
            return JsonResponse({"MESSAGE":"이메일 중복"}, status=400)

        if Phone_number_check:
            return JsonResponse({"MESSAGE":"중복된 회원정보입니다"})

        # if "@" not in data["email"] or "." not in data["email"] and list["@", "."]:
        #     return JsonResponse ({"message":"email 주소 형식을 확인해주세요"})        

        if len(data['password']) < 8:
            return JsonResponse ({"message":"비밀번호는 최소 8자 이상입니다"})

        try:
            User.objects.create(
                name         = data["name"],
                password     = data["password"],
                email        = email,
                phone_number = data["phone_number"],
                nickname     = data["nickname"]
            )
            return JsonResponse({"message":"SUCCESS"}, status = 201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)

            
