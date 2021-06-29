import json, re, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View
from users.models import User
from my_settings import SECRET_KEY

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        EMAIL_REGES        = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        PASSWORD_REGES     = '[A-Za-z0-9@#$%^&+=]{8,}'
        PHONE_NUMBER_REGES = '^[0-9]{3}[-]+[0-9]{3,4}[-]+[0-9]{4}$|^[0-9]{10,11}$'

        if not re.search(EMAIL_REGES, data["email"]):
            return JsonResponse({"MESSAGE":"이메일 중복"}, status=400)

        if not re.search(PASSWORD_REGES, data["password"]):
            return JsonResponse ({"message":"비밀번호는 최소 8자 이상입니다"}, 400)

        if not re.search(PHONE_NUMBER_REGES, data["phone_number"]):
            return JsonResponse({"MESSAGE":"필수 입력 사항"}, status = 400)

        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode()

        try:
            User.objects.create(
                name         = data['name'],
                password     = hashed_password,
                email        = data['email'],
                phone_number = data['phone_number'],
                nickname     = data['nickname']
            )
            return JsonResponse({"message":"SUCCESS"}, status = 201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        user = User.objects.get(email=data["email"])

        try:
            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                
                access_token = jwt.encode({'user_id':user.pk}, SECRET_KEY, algorithm = 'HS256')
                return JsonResponse({"MESSAGE":"SUCCESS", "TOKEN":access_token}, status = 200)
            
            return JsonResponse({"MESSAGE":"INVALID_ERROR"}, status = 400)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 401)
        except ValueError:
            return JsonResponse({"MESSAGE":"INVALID_USER"}, status = 401)