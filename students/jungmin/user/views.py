import json, jwt, bcrypt

from django.views           import View
from django.http            import JsonResponse
from django.db              import IntegrityError
from django.core.exceptions import MultipleObjectsReturned, ValidationError

from user.models            import User
from user.validators        import validate_email_regex, validate_password, validate_phone
from project_westagram      import my_settings

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            validate_email_regex(data['email'])

            validate_password(data['password'])

            validate_phone(data['phone'])

            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            User.objects.create(
                email    = data['email'],
                password = hashed_password.decode('utf-8'),
                phone    = data['phone'],
                nickname = data['nickname']
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except IntegrityError:
            return JsonResponse({'message': 'IntegrityError: already in use'}, status=409)

        except ValidationError:
            return JsonResponse({'message': 'ValidationError'}, status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            user = User.objects.get(email=data['email'])

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message': 'INVALID_USER'}, status=401)

            encoded_jwt = jwt.encode({'user': user.id}, my_settings.SECRET_KEY, my_settings.ALGORITHM)

            return JsonResponse({'message': 'SUCCESS', 'token': encoded_jwt}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)
        
        except MultipleObjectsReturned:
            return JsonResponse({'message': 'MultipleObjectsReturned'}, status=400)
        

