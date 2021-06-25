import json
import re
from django.db.models.fields.json import JSONExact

from django.http    import JsonResponse
from django.views   import View

from users.models   import User

class UserSignUp(View):
    def post(self, request):
        data = json.loads(request.body)

        new_user = User.objects.create(
            full_name       = data["full_name"],
            user_name       = data["user_name"],
            password        = data["password"],
            user_website    = data["user_website"],
            user_bio        = data["user_bio"],
            email           = data["email"],
            phone_number    = data["phone_number"],
            gender          = data["gender"],
            birth_date      = data["birth_date"],
            create_date     = data["create_date"],
        )
        # email or password 가 전달 되지 않았을 경우
        if re.match():
            return JsonResponse({"message": "KEY_ERROR"}, status=400 )
        
        # eamil validation
        if re.match('[]', new_user.):
            return JsonResponse({"message": "INAPPROPRIATE_EMAIL"}, status=400 )
        
        # password validation
        if re.match('[!@#$?a-zA-Z0-9]{8:30}', new_user.password) is False:
            return JsonResponse({"message": "INAPPROPRIATE_PASSWORD"}, status=400 )

        # phone_number validation
        if re.match('[0-9]{7,8}', new_user.phone_number) is False:
            return JsonResponse({"message": "INAPPROPRIATE_PHONE_NUMBER"}, status=400 )

            

        # 중복 가입
        users = User.objects.all()
        users_email_data =  [new_user.email for user in users]
        users_password_data =  [new_user.password for user in users]
        
        if new_user.email in users_email_data or new_user.assword in users_password_data:
            return JsonResponse({"message": "ALREADY_USER"}, status=400 )

        else:
            return JsonResponse({"MESSAGE": "Success Sign Up"}, status=201)