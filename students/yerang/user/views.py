import json

from django.http  import JsonResponse
from django.views import View

from user.models     import User
from user.validation import email_validate, password_validate

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            if not (data['email'] and data['password']):
                return JsonResponse({'message': 'KEY_ERROR'}, status=400)

            if not email_validate(data['email']):
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)

            if not password_validate(data['password']):
                return JsonResponse({'message': 'PASSWORD_TOO_SHORT'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'EMAIL_ALREADY_EXISTS'}, status=400)
            
            if User.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({'message': 'PHONENUMBER_ALREADY_EXISTS'}, status=400)
            
            if User.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({'message': 'NICKNAME_ALREADY_EXISTS'}, status=400)
            
            User.objects.create(
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],
                nickname     = data['nickname'],
            )
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Exception as e:
            return JsonResponse({'message': e})

        return JsonResponse({'message': 'SUCCESS'}, status=201)