import json
import re

from django.db.models.fields.json import JSONExact
from django.http                  import JsonResponse
from django.views                 import View

from users.models                 import User

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)
        password            = data["password"]
        email               = data["email"]
        phone_number        = data["phone_number"]
        users               = User.objects.all()
        users_email_data    = [user.email for user in users]
        users_password_data = [user.password for user in users]

        # email or password 가 전달 되지 않았을 경우
        if email is False or password is False:
            return JsonResponse({"message": "KEY_ERROR"}, status=400 )
        
        # eamil validation
        elif re.match('^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$', email) is None:
            return JsonResponse({"message": "INAPPROPRIATE_EMAIL"}, status=400 )
        
        # password validation
        elif re.match('[a-zA-Z0-9\!\@\#\$\?]{8,}', password) is None:            
            return JsonResponse({"message": "INAPPROPRIATE_PASSWORD"}, status=400 )

        # phone_number validation
        elif re.match('[0-9]{10,12}', phone_number) is None:
            return JsonResponse({"message": "INAPPROPRIATE_PHONE_NUMBER"}, status=400 )
            
        # 중복 가입
        elif email in users_email_data or phone_number in users_password_data:
            return JsonResponse({"message": "ALREADY_USER"}, status=400 )

        else:
            User.objects.create(
            nick_name       = data["nick_name"],
            name            = data["name"],
            password        = data["password"],
            email           = data["email"],
            phone_number    = data["phone_number"],
            gender          = data["gender"],
            birth_date      = data["birth_date"],
        )

            return JsonResponse({"MESSAGE": "SUCESS"}, status=201)

class SignIn(View):
    def post(self, request):
        data          = json.loads(request.body)
        email         = data["email"]
        password      = data["password"]
        users         = User.objects.all()
        user_password = User.objects.get(email=email).password
        email_data    = [user.email for user in users]

        if email is False or password is False:
            return JsonResponse({"message": "KEY_ERROR"}, status=400 )

        elif email not in email_data or password != user_password:
            return JsonResponse({"message": "INVALID_USER"}, status=401)

        else:
            return JsonResponse({"message": "SUCCESS"}, status=200)
