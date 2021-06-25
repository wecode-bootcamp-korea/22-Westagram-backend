import json, re

from django.views   import View
from django.http    import JsonResponse

from .models        import Account

class AccountView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)
            email_regexr    = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            phone_regexr    = re.compile(r'^\d{3}-\d{3,4}-\d{4}')
            
            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': '이미 존재하는 이메일입니다.'}, status=400)
            if not email_regexr.match(data['email']):
                return JsonResponse({'message': '잘못된 형식의 이메일입니다.'}, status=400)
            if len(data['password']) < 8:
                return JsonResponse({'message': '비밀번호는 8자리 이상이어야만 합니다.'}, status=400)
            if Account.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({'message': '이미 존재하는 닉네임입니다.'}, status=400)
            if Account.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({'message': '이미 존재하는 번호입니다.'}, status=400)
            if not phone_regexr.match(data['phone_number']):
                return JsonResponse({'message': '잘못된 형식의 번호입니다.'}, status=400)

            Account.objects.create(
                name          = data['name'],
                email         = data['email'],
                password      = data['password'],
                nickname      = data['nickname'],
                phone_number  = data['phone_number']
            )
        
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KEYERROR:
            return JsonResponse({'meesage': 'KEY_ERROR'}, status=400)
