
# name        = models.CharField(max_length=100)
# password    = models.CharField(max_length=100) 
# email       = models.EmailField(unique=True)
# phone_number= models.CharField(max_length=100, unique=True)
# nick_name   = models.CharField(max_length=100, unique=True)


# 이메일이나 패스워드 키가 전달되지 않았을시, 키에러 코드 400 반환
# 이메일에 @, . 없으면 에러 반환
# 비밀번호 8자이상. 만족못하면 에러 반환
# 전화번호, 이름, 닉네임, 이메일 중복되면 X, 중복시 에러 반환


import json

from django.http import JsonResponse
from django.views import View
from users.models import User

class StargramView(View):
    def post(self, request):
        
        names = User.objects.all()
        email = User.objects.all()
        password = User.objects.all()
        phone_number = User.objects.all()

        result_users = [] 

        for name in names:
            if name == name:
                if email.name == email.name and phone_number.name == phone_number.name:
                    pass
                else:
                    return JsonResponse({"MESSAGE":"이미 회원정보가 존재합니다"})

        if "@" and "." not in email:
            return JsonResponse ({"message":"email 주소 형식을 확인해주세요"})
        else:
            pass
        
        if len(password) < 8:
            return JsonResponse ({"message":"비밀번호는 최소 8자 이상입니다"})
        else:
            pass
        
        try:
            data = json.loads(request.body)
            User.objects.create(
                name        = data["name"],
                password    = data["password"],
                email       = data["email"],
                phone_number= data["phone_number"],
                nick_name   = data["nick_name"]
            )
            return JsonResponse({"message":"SUCCESS"}, status = 201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status = 400)

            