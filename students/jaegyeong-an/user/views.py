import json
import re

from django.views import View
from django.http  import JsonResponse
from django.db    import IntegrityError

from user.models  import User

class SignUpView(View):
    def post(self, request):
        REGEX_MAIL = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        try:
            data = json.loads(request.body)
            email = data['email']

            if REGEX_MAIL.match(email) == None:
                return JsonResponse({'error':'INVALID_EMAIL'}, status=400)
            if len(data['password']) < 8:
                return JsonResponse({'error':'INVALID_PASSWORD'}, status=400)
                
            User.objects.create(
            email        = data['email'],
            phone_number = data['phone_number'],
            name         = data['name'],
            nickname     = data['nickname'],
            password     = data['password']
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'error':'KEY_ERROR'}, status=400)
        except IntegrityError:
            return JsonResponse({'error':'DUPLICATE_ENTRY'}, status=400)