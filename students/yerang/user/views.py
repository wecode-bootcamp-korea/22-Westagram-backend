import json

from django.http  import JsonResponse
from django.views import View

from user.models import User

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        if (not data['email']) or (not data['password']):
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        if (not '@' in data['email']) or  (not '.' in data['email']):
            return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)

        if len(data['password']) < 8:
            return JsonResponse({'message': 'INVALID_PASSWORD'}, status=400)

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

        return JsonResponse({'message': 'SUCCESS'}, status=201)