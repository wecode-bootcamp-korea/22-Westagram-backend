import json
import re

from django.views           import View
from django.http            import JsonResponse
from django.db              import IntegrityError

from user.models            import User

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            email_pattern = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if email_pattern.match(email) == None:
                return JsonResponse({'error' : 'INVALID_EMAIL'}, status=400)
            if len(data['password']) < 8:
                return JsonResponse({'error' : 'INVALID_PASSWORD'}, status=400)
            else:
                User.objects.create(
                email = data['email'],
                phone_number = data['phone_number'],
                name = data['name'],
                nickname = data['nickname'],
                password = data['password']
                )
            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'error':'KEY_ERROR'}, status=400)
        except IntegrityError:
            return JsonResponse({'error':'DUPLICATE_ENTRY'}, status=400)


