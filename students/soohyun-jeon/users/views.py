import re
import json

from django.views     import View
from django.http      import JsonResponse

from users.models     import User
from users.validators import validate_email, validate_password

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not validate_email(data['email']):
                return JsonResponse({'MESSAGE': 'INVALID_EMAIL'}, status=400)

            if not validate_password(data['password']):
                return JsonResponse({'MESSEAGE': 'INVALID_PASSWORD'}, status=400)

            User.objects.create(
                phone_number = data['phone_number'],
                email        = data['email'],
                name         = data['name'],
                nickname     = data['nickname'],
                password     = data['password'],
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KeyError'}, status=404)
