import re
from users.models                 import User

email_regex     = '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
phone_regex     = '[0-9]{10,12}'
password_regex  = '[a-zA-Z0-9\!\@\#\$\?]{8,}'

def email_validation(email):
    return re.match(email_regex, email)

def password_validation(password):
    return re.match(password_regex, password)

def phone_validation(phone_number):
    return re.match(phone_regex, phone_number)




# class Validation():
#     email_validation    = re.match('^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$', email)
#     phone_validation    = re.match('[0-9]{10,12}', phone_number)
#     password_validation = re.match('[a-zA-Z0-9\!\@\#\$\?]{8,}', password)
#     duplicate_user      = User.objects.filter(email=data["email"]).exists() or User.objects.filter(phone_number=data["phone_number"]).exists()


        # if email is False or password is False:
        #     return JsonResponse({"message": "KEY_ERROR"}, status=400 )
        
        # # eamil validation
        # elif re.match('^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$', email) is None:
        #     return JsonResponse({"message": "INAPPROPRIATE_EMAIL"}, status=400 )
        
        # # password validation
        # elif re.match('[a-zA-Z0-9\!\@\#\$\?]{8,}', password) is None:            
        #     return JsonResponse({"message": "INAPPROPRIATE_PASSWORD"}, status=400 )

        # # phone_number validation
        # elif re.match('[0-9]{10,12}', phone_number) is None:
        #     return JsonResponse({"message": "INAPPROPRIATE_PHONE_NUMBER"}, status=400 )
            
        # # 중복 가입
        # elif email in users_email_data or phone_number in users_password_data:
        #     return JsonResponse({"message": "ALREADY_USER"}, status=400 )