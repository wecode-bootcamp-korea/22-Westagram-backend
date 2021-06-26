import json
from json.decoder import JSONDecodeError
import re

from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ValidationError
from django.db.utils import DataError, IntegrityError
from django.core.validators  import validate_email

from user.models import User

class UserView(View):
    def post(self, request):
        email_regex = re.compile("^[^@\s]+@[^@\s\.]+\.[^@\.\s]+$")
        password_regex = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")
        try:
            data = json.loads(request.body)
            if not email_regex.match(data["email"]):
                raise ValidationError(message="EMAIL_VALIDATION_ERROR")
            if not password_regex.match(data["password"]):
                raise ValidationError(message="PASSWORD_VALIDATION_ERROR")
            User.objects.create(
                email        = data["email"],
                password     = data["password"],
                nick_name    = data["nick_name"],
                phone_number = data["phone_number"],
            )
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except ValidationError as error:
            return JsonResponse({"message": error.args[0]}, status=400)
        except IntegrityError as error:
            return JsonResponse({"message": "INTEGRITY_ERROR","content":error.args[1] }, status=400)
        except DataError:
            return JsonResponse({"message": "DATA_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)
        except Exception:
            return JsonResponse({"message": "UNCATCHED_ERROR"}, status=400)
        return JsonResponse({"message": "SUCCESS"}, status=201)

