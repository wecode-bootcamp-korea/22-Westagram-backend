import json, re

from django.http    import JsonResponse, HttpResponse
from django.views   import View

from .models        import Account

class SignUpView(View):
    def post(self, request):
        data                 = json.loads(request.body)
        email_regex          = re.compile(r'^[a-zA-Z0-9+-._]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        password_regex       = re.compile(r'[a-zA-Z0-9`~!@#$%^&*()_+-={};:",./<>?]{8,25}')
        phone_number_regex   = re.compile(r'^01[1|2|7|8|0|9]-?[0-9]{3,4}-?[0-9]{4}$')

        try:
            if not email_regex.match(data['email']):
                return JsonResponse({"message":"Invalid email address"}, status=401)
            if not password_regex.match(data['password']):
                return JsonResponse({"message":"Invalid password format"}, status=401)
            if not phone_number_regex.match(data['phone_number']):
                return JsonResponse({"message":"Invalid phone number format"}, status=401)

            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({"message":"Account is already taken"}, status=401)
            if Account.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({"message":"Phone number is already taken"}, status=401)
            if Account.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({"message":"nickname is already taken"}, status=401)
                
            Account.objects.create(
                email           = data["email"],
                password        = data["password"],
                nickname        = data["nickname"],
                phone_number    = data["phone_number"]
            )
            return JsonResponse({"message":"SUCESS"}, status=201)
        except:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
