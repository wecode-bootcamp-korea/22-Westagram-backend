import json

from django.views           import View
from django.http            import JsonResponse
from django.db              import IntegrityError
from django.core.exceptions import ValidationError

from user.models            import User
from user.validators        import validate_email_regex, validate_password, check_phone_number

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            # email validation (정규표현식)
            validate_email_regex(data['email'])

            # password validation
            validate_password(data['password'])

            # phone input check (입력값 중간 '-' 혹은 '.' 제거하기)
            phone_checked = check_phone_number(data['phone'])

            user = User.objects.create(
                email    = data['email'],
                password = data['password'],
                phone    = phone_checked,
                nickname = data['nickname']
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)

        # 필수 항목이 비어있는지 체크
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        # 계정 정보가 이미 등록되어 있는지 체크
        except IntegrityError:
            return JsonResponse({'message': 'IntegrityError: already in use'})

        # email, password validation 
        except ValidationError:
            return JsonResponse({'message': 'ValidationError'}, status=400)
