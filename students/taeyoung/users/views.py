import json, re, bcrypt, jwt

from django.views   import View
from django.http    import JsonResponse

from users.models   import Account
from my_settings import SECRET_KEY, ALGORITHM

class AccountView(View):
    def post(self, request):
        data            = json.loads(request.body)
        bcrypt_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        email_regexr    = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        phone_regexr    = re.compile(r'^\d{3}-?\d{3,4}-?\d{4}')
        password_regexr = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$')

        try: 
            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': '이미 존재하는 이메일입니다.'}, status=400)
            if Account.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({'message': '이미 존재하는 닉네임입니다.'}, status=400)
            if Account.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({'message': '이미 존재하는 번호입니다.'}, status=400)
            if not phone_regexr.match(data['phone_number']):
                return JsonResponse({'message': '잘못된 형식의 번호입니다.'}, status=400)
            if not email_regexr.match(data['email']):
                return JsonResponse({'message': '잘못된 형식의 이메일입니다.'}, status=400)
            if not password_regexr.match(data['password']): 
                return JsonResponse({'message': '잘못된 형식의 비밀번호입니다.'}, status=400)

            Account.objects.create(
                    name          = data['name'],
                    email         = data['email'],
                    password      = bcrypt_password,
                    nickname      = data['nickname'],
                    phone_number  = data['phone_number']
                    )

            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'meesage': 'KEY_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            email   = data['email']
            password = data['password'].encode('utf-8')
            
            if Account.objects.filter(email=email).exists():
                db_email    = Account.objects.get(email=email)
                db_password = db_email.password.encode('utf-8')
                if bcrypt.checkpw(password, db_password):
                    token = jwt.encode({'user_id': db_email.id}, SECRET_KEY, ALGORITHM)
                    return JsonResponse({'token': token, 'message': 'SUCCESS'}, status=200)
                return JsonResponse({'message':'INVALID_PASSWORD'}, status=401)
            return JsonResponse({'message':'INAVLID_USER'}, status=401)
        except KeyError:
             JsonResponse({'message': 'KEYERROR'}, status=400)
