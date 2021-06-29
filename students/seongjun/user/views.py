import json
import bcrypt

from django.db import IntegrityError
from django.http import JsonResponse
from django.views import View

from user.models import Account
from user.validators import validate_email, validate_password, validate_phone_number


# Create your views here.
class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:

            if not validate_email(data['email']):
                return JsonResponse({"message": "이메일 형식을 맞추어주세요"}, status=400)
            if not validate_password(data['password']):
                return JsonResponse({'message': 'Password 8이상 작성해야합니다.'}, status=400)
            if not validate_phone_number(data['phone_number']):
                return JsonResponse({'message': '잘못된 형식의 번호입니다.'}, status=400)
            if len(data['nick_name']) < 4 or len(data['nick_name']) > 12:
                return JsonResponse({'message': '닉네임을 4자~8자까지 입력해주세요.'}, status=400)

            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            Account.objects.create(
                email       = data['email'],
                password    = hashed_password.decode('utf-8'),
                nick_name   = data['nick_name'],
                phone_number= data['phone_number']
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except IntegrityError:
            return JsonResponse({"message": "IntegrityError"}, status=400)


class LoginView(View):
    def post(self, request):
        data        = json.loads(request.body)
        email       = data['email']
        password    = data['password']

        try:
            if not validate_email(email):
                return JsonResponse({"message": "이메일 형식을 맞추어주세요"}, status=400)
            if not validate_password(password):
                return JsonResponse({'message': 'Password 8이상 작성해야합니다.'}, status=400)
            if not Account.objects.filter(email=email, password=password).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            return JsonResponse({"message": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
