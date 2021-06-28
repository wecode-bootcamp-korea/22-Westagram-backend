import json

from django.http  import JsonResponse
from django.views import View
from django.db    import IntegrityError
from django.forms import ValidationError

from users.models    import User
from users.validator import check_email_validation, check_password_validation, check_phone_validation

class SigninView(View):
    def get(self, request):
        data = json.loads(request.body)

        try:
<<<<<<< HEAD
            if not check_email_validation(data['email']) or \
                    not check_password_validation(data['password']) or \
                    not check_phone_validation(data['phone']):
                        raise ValidationError("VALIDATION_ERROR")
||||||| 844ea14
            email    = check_email_validation(data['email'])
            password = check_password_validation(data['password'])
            phone    = check_phone_validation(data['phone'])
            nickname = data['nickname']
=======
            if "email" in data:
                user = User.objects.get(email=data['email'], password=data['password'])
            elif "phone" in data:
                user = User.objects.get(phone=data['phone'], password=data['password'])
            else:
                raise KeyError
>>>>>>> d60dd373289b8c266b150a1d081d723da391b2db

<<<<<<< HEAD
            User.objects.create(email=data['email'], password=data['password'], phone=data['phone'], nickname=data['nickname'])
            return JsonResponse({"message": "SUCCESS"}, status=201)
||||||| 844ea14
            User.objects.create(email=email, password=password, phone=phone, nickname=nickname)
            return JsonResponse({"message": "SUCCESS"}, status=201)
=======
            return JsonResponse({"message": "SUCCESS"}, status=200)
>>>>>>> d60dd373289b8c266b150a1d081d723da391b2db

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=401)
