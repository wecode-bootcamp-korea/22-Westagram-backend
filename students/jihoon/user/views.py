import json, re

from json.decoder import JSONDecodeError
from django.views import View
from django.http  import JsonResponse

from user.models import Account


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        email_regas     = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        password_regex  = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        phone_number_regex = "\d{2}-\d{3}-\d{4}"

        if data['name']     == '':
            return JsonResponse({"MESSAGE": "필수 입력 사항입니다."})

        if (re.search(phone_number_regex, data['phone_number']) != None) == False:
            return JsonResponse({'MESSAGE':'필수 입력 사항입니다.'})

        if (re.search(email_regas, data['email']) != None) == False:
            return JsonResponse({"MESSAGE": "EMAIL VALIDATION"})

        if (re.search(password_regex, data['password']) != None) == False:
            return JsonResponse({'MESSAGE':'PASSWORD VALIDATION'})

        if len(data['password']) < 8:
            return JsonResponse({'MESSAGE':'PASSWORD ERROR'})

        try:
            Account.objects.create(
                name = data['name'],
                email = data['email'],
                phone_number = data['phone_number'],
                password = data['password'],
                nickname = data['nickname']
            )
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

