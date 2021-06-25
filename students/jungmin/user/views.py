import json, re

from django.views   import View
from django.http    import JsonResponse
from django.core.exceptions import ValidationError
# from django.core.validators import validate_email

from user.models    import User

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            # # email validation (validate_email)
            # validate_email(data['email'])

            # email validation (정규표현식)
            email_validation = re.compile('^[a-zA-Z0-9+-_.]+@+[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if not email_validation.match(data['email']):
                return JsonResponse({'message': 'ValidationError'}, status=400)

            # password validation
            if len(data['password']) < 8:
                return JsonResponse({'ValidationError': "This password is too short."}, status=400)

            # integrity
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'IntegrityError': "Email already in use"}, status=400)
            if User.objects.filter(phone=data['phone']).exists():
                return JsonResponse({'IntegrityError': "Phone number already in use"}, status=400)
            if User.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({'IntegrityError': "Nickname already in use"}, status=400)

            user = User.objects.create(
                email    = data['email'],
                password = data['password'],
                phone    = data['phone'],
                nickname = data['nickname']
            )
            return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
            
        # except ValidationError:
        #     return JsonResponse({'MESSAGE': 'ValidationError'}, status=400)

    def get(self, request):
        users = User.objects.all()
        results = []
        for user in users:
            results.append(
                {
                    'email'   : user.email,
                    'password': user.password,
                    'phone'   : user.phone,
                    'nickname': user.nickname
                }
            )
        return JsonResponse({'results': results}, status=200)