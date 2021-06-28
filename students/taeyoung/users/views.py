import json, re

from django.views   import View
from django.http    import JsonResponse

from users.models   import Account

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

    #      try:
    #          if not (data['email'] and data['password']):
    #              return JsonResponse({'message':'KEY_ERROR'}, status=401)
    #          if Account.objects.filter(email=data['email']).exists():
    #              email = Account.objects.get(email=data['email'])
    #              if email.password == data['password']:
    #                  return JsonResponse({'message': 'SUCCESS'}, status=200)
    #              else:
    #                  return JsonResponse({'message': 'INAVLID_PASSWORD'}, status=401)
    #          else:
    #              return JsonResponse({'message': 'INVALID_USER'}, status=401)
    #      except KeyError:
            #  return JsonResponse({'message': 'KEY_ERROR'}, status=401)

        try:
            if Account.objects.filter(email=data['email']).exists():
                email = Account.objects.get(email=data['email'])
                if email.password == data['password']:
                    return JsonResponse({'message': 'SUCCESS'}, status=200)
                else:
                    return JsonResponse({'message':'INVALID_PASSWORD'}, status=401)
            else:
                return JsonResponse({'message':'INAVLID_USER'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KeyError'}, status=400)

class AccountView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)
            email_regexr    = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            phone_regexr    = re.compile(r'^\d{3}-\d{3,4}-\d{4}')
            password_regexr = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$')

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
                password      = data['password'],
                nickname      = data['nickname'],
                phone_number  = data['phone_number']
            )
        
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'meesage': 'KEY_ERROR'}, status=400)
