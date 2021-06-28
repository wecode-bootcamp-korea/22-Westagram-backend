import json

from django.views           import View
from django.http            import JsonResponse
from django.db              import IntegrityError
from django.core.exceptions import ValidationError

from user.models            import User
from user.validators        import validate_email_regex, validate_password, validate_phone

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            validate_email_regex(data['email'])

            validate_password(data['password'])

            validate_phone(data['phone'])

            User.objects.create(
                email    = data['email'],
                password = data['password'],
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

            if user.password != data['password']:
                return JsonResponse({'message': 'INVALID_USER'}, status=401)

            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)
