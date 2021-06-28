import json

from django.http  import JsonResponse
from django.views import View
from django.db    import IntegrityError
from django.forms import ValidationError

from users.models    import User
from users.validator import check_email_validation, check_password_validation, check_phone_validation

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not check_email_validation(data['email']) or \
                    not check_password_validation(data['password']) or \
                    not check_phone_validation(data['phone']):
                        raise ValidationError("VALIDATION_ERROR")

            User.objects.create(email=data['email'], password=data['password'], phone=data['phone'], nickname=data['nickname'])
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except ValidationError as err:
            return JsonResponse({"message": err.message}, status=400)

        except IntegrityError:
            return JsonResponse({"message": "DUPLICATE_ERROR"}, status=400)

class SigninView(View):
    def get(self, request):
        data = json.loads(request.body)

        try:
            user = User.objects.get(email=data['email'])

            if user.password != data['password']:
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            return JsonResponse({"message": "SUCCESS"}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=401)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
