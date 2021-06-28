import json, re

from django.views import View
from django.http  import JsonResponse

from user.models import Account

class SignUpView(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)    
            NAME_REGEX          = "^[가-힣]{2,4}$"
            NICKNAME_REGEX      = "^[a-zA-Z0-9._-]{2,16}\$"
            PHONE_NUMBER_REGEX  = "^\d{3}-\d{3,4}-\d{4}$"
            EMAIL_REGEX         = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            PASSWORD_REGEX      = "^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$"
            
            if not re.search(NAME_REGEX, data['name']):
                return JsonResponse({"MESSAGE": "2~4 글자의 한글을 입력해 주세요."}, status=400)
            
            if not re.search(NICKNAME_REGEX, data['nickname']):
                return JsonResponse({"MESSAGE" : "숫자, 영어, 언더스코어만 사용할 수 있습니다."}, status=400)

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
            
            Account.objects.create(
                name            = data['name'],
                email           = data['email'],
                phone_number    = data['phone_number'],
                password        = data['password'],
                nickname        = data['nickname']
            )
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if "email" in data:
                account = Account.objects.get(email=data['email'], password=data['password'])

            elif "phone_number" in data:
                account = Account.objects.get(phone_number=data['phone_number'], password=data['password'])

            elif "nickname" in data:
                account = Account.objects.get(nickname=data['nickname'], password=data['password'])
            else:
                return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=401)
                
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=200)

        except Account.DoesNotExist:
            return JsonResponse({"MESSAGE": "INVALID_USER"}, status=400)