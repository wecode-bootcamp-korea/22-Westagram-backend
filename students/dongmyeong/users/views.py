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
            if not check_email_validation(data['email']) and \
                    not check_password_validation(data['password']) and \
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

