import json, re, bcrypt, jwt

from django.views import View
from django.http  import JsonResponse

from my_settings import SECRET_KEY
from user.models import Account

class SignUpView(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)
            NAME_REGEX          = "^[가-힣]{2,4}$"
            PHONE_NUMBER_REGEX  = "^[0-9]{3}[-]+[0-9]{3,4}[-]+[0-9]{4}$|^[0-9]{10,11}$"
            EMAIL_REGEX         = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            PASSWORD_REGEX      = "^[A-Za-z0-9@#$%^&+=]{8,}"
            
            if not re.search(NAME_REGEX, data['name']):
                return JsonResponse({"MESSAGE": "2~4 글자의 한글을 입력해 주세요."}, status=400)

            if not re.search(PHONE_NUMBER_REGEX, data['phone_number']):
                return JsonResponse({"MESSAGE":"필수 입력 사항입니다."}, status=400)

            if not re.search(EMAIL_REGEX, data['email']):
                return JsonResponse({"MESSAGE": "EMAIL VALIDATION"}, status=400)

            if not re.search(PASSWORD_REGEX, data['password']):
                return JsonResponse({"MESSAGE":"PASSWORD VALIDATION"}, status=400)

            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({"MESSAGE": "이미 존재하는 이메일입니다."}, status=400)

            if Account.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({"MESSAGE": "이미 존재하는 번호입니다."}, status=400)

            if Account.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({"MESSAGE": "이미 존재하는 닉네임입니다."}, status=400)

            hashed_password     = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            
            Account.objects.create(
                name            = data['name'],
                email           = data['email'],
                phone_number    = data['phone_number'],
                password        = hashed_password.decode('utf-8'),
                nickname        = data['nickname']
            )
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        account = Account.objects.get(email=data['email'])

        try:
            if bcrypt.checkpw(data['password'].encode('utf-8'), account.password.encode('utf-8')):
                access_token = jwt.encode({'account_id':account.pk}, SECRET_KEY, algorithm = 'HS256')
                return JsonResponse({"MESSAGE": "SUCCESS", "TOKEN":access_token}, status=200)

            return JsonResponse({"MESSAGE":"INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)

        except Account.DoesNotExist:
            return JsonResponse({"MESSAGE":"INVALID_USER"}, status=400)