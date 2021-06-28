import json, re

from django.http  import JsonResponse
from django.views import View

from users.models import User

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        EMAIL_REGES        = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        PASSWORD_REGES     = '[A-Za-z0-9@#$%^&+=]{8,}'
        PHONE_NUMBER_REGES = '^[0-9]{3}[-]+[0-9]{3,4}[-]+[0-9]{4}$'

        if not re.search(EMAIL_REGES, data["email"]):
            return JsonResponse({"MESSAGE":"이메일 중복"}, status=400)

        if not re.search(PASSWORD_REGES, data["password"]):
            return JsonResponse ({"message":"비밀번호는 최소 8자 이상입니다"}, 400)

        if not re.search(PHONE_NUMBER_REGES, data["phone_number"]):
            return JsonResponse({"MESSAGE":"중복된 회원정보입니다"}, status = 400)

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

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        nickname       = data["nickname"]
        password       = data["password"]
        
        nickname_check = User.objects.filter(nickname=nickname).exists()
        password_check = User.objects.filter(password=password).exists()

        try:
            if nickname_check:
                if password_check:
                    return JsonResponse({"MESSAGE":"SUCCESS"}, status = 200)
                else:
                    return JsonResponse({"MESSAGE":"INVALID_PASSWORD"}, status = 400)
            else:
                return JsonResponse({"MESSAGE":"INVALID_NICKNAME"}, status = 400)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 401)
        except ValueError:
            return JsonResponse({"MESSAGE":"INVALID_NICKNAME"}, status = 401)