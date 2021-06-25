import re
import json

from django.views import View
from django.http import JsonResponse

from users.models import User
from users.validators import validate_email, validate_password
# # 인스타그램에 회원가입 할 때에는 사용자 계정으로 이메일을 필수로 필요합니다.{"message": "KEY_ERROR"}, status code 400
# # 인스타그램에 회원가입 할 때에는 비밀번호도 필수로 필요합니다.{"message": "KEY_ERROR"}, status code 400
# # 회원가입 할 때 핸드폰 번호와 닉네임도 추가로 저장합니다.
# # 회원가입시 이메일을 사용할 경우, 이메일에는 @와 .이 필수로 포함되어야 합니다. 해당 조건이 만족되지 않을 시 적절한 에러를 반환해주세요. 이 과정을 email validation이라고 합니다.
# # 회원가입시 비밀번호는 8자리 이상이어야만 합니다. 해당 조건이 만족되지 않을 시, 적절한 에러를 반환해주세요. 이 과정을 password validation이라고 합니다.
# # 회원가입시 서로 다른 사람이 같은 전화번호나 사용자 이름, 이메일을 사용하지 않으므로 기존에 존재하는 자료와 중복되어서는 안됩니다. 적절한 에러를 반환해주세요.
# # 회원가입이 성공하면 {"message": "SUCCESS"}, status code 201을 반환합니다.
# # [추가 구현 사항] -> email validation 또는 password validation 과정에서 정규식을 사용해보세요.
class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not validate_email(data['email']):
                return JsonResponse({'MESSAGE': 'INVALID_EMAIL'}, status=400)
            if not validate_password(data['password']):
                return JsonResponse({'MESSEAGE': 'INVALID_PASSWORD'}, status=400)
            user = User.objects.create(
                phone_number  =data['phone_number'],
                email         =data['email'],
                name          =data['name'],
                nickname      =data['nickname'],
                password      =data['password'],
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KeyError'}, status=404)
