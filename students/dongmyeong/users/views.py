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
            email    = check_email_validation(data['email'])
            password = check_password_validation(data['password'])
            phone    = check_phone_validation(data['phone'])
            nickname = data['nickname']

            User.objects.create(email=email, password=password, phone=phone, nickname=nickname)
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except ValidationError as err:
            return JsonResponse({"message": err.message}, status=400)

        except IntegrityError:
            return JsonResponse({"message": "DUPLICATE_ERROR"}, status=400)

