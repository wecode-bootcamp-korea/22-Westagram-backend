import json
import re

from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ValidationError
from django.db.utils import DataError, IntegrityError

from user.models import User

email_regex = "^[^@\s]+@[^@\s\.]+\.[^@\.\s]+$"


# Create your views here.
class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        try:
            if not re.match(email_regex, data["email"]):
                raise ValidationError(message="EMAIL_VALIDATION_ERROR")
            if len(data["password"]) < 8:
                raise ValidationError(message="PASSWORD_VALIDATION_ERROR")
            new_user = User.objects.create(
                email=data["email"],
                password=data["password"],
                nick_name=data["nick_name"],
                phone_number=data["phone_number"],
            )
            print(new_user)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except ValidationError as error:
            return JsonResponse({"message": error.args[0]}, status=400)
        except IntegrityError as error:
            return JsonResponse(
                {"message": "INTEGRITY_ERROR", "content": error.args[1]}, status=400
            )
        except DataError:
            return JsonResponse({"message": "DATA_ERROR"}, status=400)
        except Exception:
            return JsonResponse({"message": "SUCCESS"}, status=201)

        return JsonResponse({"message": "SUCCESS"}, status=201)

