import json

from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ValidationError
from django.db.utils import DataError, IntegrityError
from json.decoder import JSONDecodeError

from user.models import User
from user.validation import validate_email, validate_password

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            if not validate_email(data["email"]):
                raise ValidationError(message="EMAIL_VALIDATION_ERROR")
            if not validate_password(data["password"]):
                raise ValidationError(message="PASSWORD_VALIDATION_ERROR")
            User.objects.create(
                email        = data["email"],
                password     = data["password"],
                nick_name    = data["nick_name"],
                name         = data["name"],
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

class LoginView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            if not validate_email(email=data["email"]):
                raise ValidationError(message="INVALID_USER")
            if not validate_password(password=data["password"]):
                raise ValidationError(message="INVALID_USER")
            if User.objects.filter(email=data["email"]).exists():
                user = User.objects.get(email=data["email"])
            else :
                raise ValidationError(message="INVALID_USER")
            if not validate_password(password= data["password"]) or user.password != data["password"]:
                raise ValidationError(message="INVALID_USER")
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except ValidationError as error:
            return JsonResponse({"message":error.message}, status=400)
        except Exception as error:
            return JsonResponse({"message":"NOT_CATCHED_ERROR"}, status=400)
        return JsonResponse({"message":"success"}, status=200)

class FollowView(View):
    def post(self, request, user_id):
        try:
            data = json.loads(request.body)
            user_instance = User.objects.get(id=user_id)
            follower_instance = User.objects.get(id=data["follower_id"])
            if user_instance == follower_instance:
                raise User.DoesNotExist
            if user_instance.follower.filter(id=data["follower_id"]).exists():
                user_instance.follower.remove(follower_instance)
            else:
                user_instance.follower.add(follower_instance)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message": "JSON_DECODE_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message": "USER_NOT_EXIST"}, status=400)
        except Exception as error:
            print(error.__class__)
            return JsonResponse({"message":"NOT_CATCHED_ERROR"}, status=400)
        return JsonResponse({"message":"success"}, status=200)
