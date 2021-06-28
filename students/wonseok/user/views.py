import json
import bcrypt

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError
from django.db.utils        import DataError, IntegrityError

from json.decoder import JSONDecodeError

from user.models     import User
from user.validation import validate_email, validate_password

class SignupView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data["email"]
            password = data["password"]
            if not validate_email(email):
                raise ValidationError(message="EMAIL_VALIDATION_ERROR")
            if not validate_password(password):
                raise ValidationError(message="PASSWORD_VALIDATION_ERROR")
            encoded = password.encode()
            hashed  = bcrypt.hashpw(encoded, bcrypt.gensalt())
            User.objects.create(
                email        = data["email"],
                password     = hashed.decode(),
                nick_name    = data["nick_name"],
                name         = data["name"],
                phone_number = data["phone_number"],
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except ValidationError as error:
            return JsonResponse({"message": error.args[0]}, status=400)
        except IntegrityError as error:
            return JsonResponse({"message": "INTEGRITY_ERROR","content":error.args[1] }, status=400)
        except DataError as error:
            return JsonResponse({"message": "DATA_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)

class LoginView(View):
    def post(self,request):
        try:
            data     = json.loads(request.body)
            email    = data["email"]
            password = data["password"]
            if not validate_email(email):
                raise ValidationError(message="INVALID_EMAIL")
            if not validate_password(password):
                raise ValidationError(message="INVALID_PASSWORD")
            user     = User.objects.get(email=email)
            encoded  = password.encode()
            original = user.password.encode()
            is_match = bcrypt.checkpw(encoded, original)
            if not is_match:
                raise ValidationError(message="INVALID_USER")
            current_time = datetime.datetime.now()
            five_hours = datetime.timedelta(hours=5)
            exp = current_time + five_hours
            access_token = jwt.encode({"id":user.id, "exp":exp}, my_settings.SECRET_KEY, my_settings.ALGORITHM)
            return JsonResponse({"message":"success", "access_token":access_token}, status=200)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except ValidationError as error:
            return JsonResponse({"message":error.message}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message":"USER_NOT_EXIST"}, status=400)