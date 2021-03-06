import json, re, bcrypt

from django.http            import JsonResponse, HttpResponse
from django.views           import View

from .models                import Account
from .utils                 import encoded_jwt

class SignInView(View):
    def post(self, request):
        data         = json.loads(request.body)
        
        try:
            email    = data['email']
            password = data['password'].encode('utf-8')
            if Account.objects.filter(email=email).exists():
                account_email    = Account.objects.get(email=email)
                account_password = account_email.password.encode('utf-8')
                if bcrypt.checkpw(password, account_password):
                    return JsonResponse({"message": "SUCCESS", "token":encoded_jwt(account_email.id)}, status=200) 
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=401)
            return JsonResponse({"message": "INVALID_USER"}, status=401)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

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
                password        = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                nickname        = data["nickname"],
                phone_number    = data["phone_number"]
            )
            return JsonResponse({"message":"SUCESS"}, status=201)
        except:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

