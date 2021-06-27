import json

from django.http  import JsonResponse
from django.views import View
from django.db    import IntegrityError
from django.forms import ValidationError

from users.models    import User, Follow
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

class SigninView(View):
    def get(self, request):
        data = json.loads(request.body)

        try:
            if "email" in data:
                user = User.objects.get(email=data['email'], password=data['password'])
            elif "phone" in data:
                user = User.objects.get(phone=data['phone'], password=data['password'])
            else:
                return JsonResponse({"message": "KEY_ERROR"}, status=401)

            return JsonResponse({"message": "SUCCESS"}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=401)

class FollowView(View):
    def post(self, request, followee_id):
        data = json.loads(request.body)

        try:
            follower = User.objects.get(id=data['user'])
            followee = User.objects.get(id=followee_id)

            Follow.objects.create(followee=followee, follower=follower)
            return JsonResponse({"messsage": "SUCCESS"}, status=201)
        
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=401)


    def delete(self, request, followee_id):
        data = json.loads(request.body)

        try:
            follower = User.objects.get(id=data['user'])
            followee = User.objects.get(id=followee_id)

            Follow.objects.get(followee=followee, follower=follower).delete()
            return JsonResponse({"messsage": "SUCCESS"}, status=201)
        
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)

        except Follow.DoesNotExist:
            return JsonResponse({"message": "INVALID_RELATION"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=401)

    def get(self, request):
        data = json.loads(request.body)

        try:
            user = User.objects.get(id=data['user'])

            results = [{
                "followees" : [followee.nickname for followee in user.following.all()],
                "followers" : [follower.nickname for follower in user.followed.all()],
                }]

            return JsonResponse({"results": results}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=401)

