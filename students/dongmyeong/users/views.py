import json
import bcrypt
import jwt

from django.http  import JsonResponse
from django.views import View
from django.db    import IntegrityError
from django.forms import ValidationError

from users.models    import User
from users.validator import check_email_validation, check_password_validation, check_phone_validation
import my_settings

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not check_email_validation(data['email']) or \
                    not check_password_validation(data['password']) or \
                    not check_phone_validation(data['phone']):
                        raise ValidationError("VALIDATION_ERROR")

            hashed_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            User.objects.create(
                    email    = data['email'],
                    password = hashed_pw.decode('utf-8'),
                    phone    = data['phone'],
                    nickname = data['nickname'],
                    )

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
            
            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            access_token = jwt.encode({"user_id": user.id}, my_settings.SECRET_KEY, my_settings.SECRET_ALGORITHM)

            return JsonResponse({"message": "SUCCESS", "access_token": access_token}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=401)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

