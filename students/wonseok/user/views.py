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
            data         = json.loads(request.body)
            email        = data["email"]
            password     = data["password"]
            nick_name    = data["nick_name"]
            name         = data["name"]
            phone_number = data["phone_number"]

            if not validate_email(email):
                raise ValidationError(message="EMAIL_VALIDATION_ERROR")
            
            if not validate_password(password):
                raise ValidationError(message="PASSWORD_VALIDATION_ERROR")
            
            hashed  = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(
                email        = email,
                password     = hashed.decode(),
                nick_name    = nick_name,
                name         = name,
                phone_number = phone_number,
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

