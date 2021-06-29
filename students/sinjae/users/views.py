import json
import re

from django.db.models.fields.json import JSONExact
from django.http                  import JsonResponse
from django.views                 import View

from users.models                 import User
from users.validation             import email_validation, password_validation, phone_validation

class SignUp(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)
            password            = data["password"]
            email               = data["email"]
            phone_number        = data["phone_number"]
            duplicate_user      = User.objects.filter(email=data["email"]).exists() or User.objects.filter(phone_number=data["phone_number"]).exists()
            
            if not email_validation(email):
                return JsonResponse({"message": "INAPPROPRIATE_EMAIL"}, status=400 )
            if not password_validation(password):
                return JsonResponse({"message": "INAPPROPRIATE_PASSWORD"}, status=400 )
            if not phone_validation(phone_number):
                return JsonResponse({"message": "INAPPROPRIATE_PHONE_NUMBER"}, status=400 )
            if duplicate_user:
                return JsonResponse({"message": "ALREADY_USER"}, status=400 )

            User.objects.create(
                nick_name       = data["nick_name"],
                name            = data["name"],
                password        = data["password"],
                email           = data["email"],
                phone_number    = data["phone_number"],
                gender          = data["gender"],
                birth_date      = data["birth_date"],
            )
            
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError as e:
            return JsonResponse({"message": e}, status=400 )
            
        
