import json, bcrypt, jwt, my_settings

from json.decoder import JSONDecodeError

from django.http  import JsonResponse
from django.views import View

from user.models     import User
from user.validation import email_validate, password_validate

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
       
        try:
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email=email)

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):       
                access_token = jwt.encode({'id': user.id}, my_settings.SECRET_KEY, algorithm = "HS256")

                return JsonResponse({'message': 'SUCCESS', 'access_token': access_token}, status=200)
            
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)
        except ValueError:
            return JsonResponse({'message': 'VALUE_ERROR'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        
class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            if not email_validate(data['email']):
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)

            if not password_validate(data['password']):
                return JsonResponse({'message': 'PASSWORD_TOO_SHORT'}, status=400)

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'EMAIL_ALREADY_EXISTS'}, status=400)
            
            if User.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({'message': 'PHONENUMBER_ALREADY_EXISTS'}, status=400)
            
            if User.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse({'message': 'NICKNAME_ALREADY_EXISTS'}, status=400)

            hashed_password  = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            decoded_password = hashed_password.decode('utf-8')
            
            User.objects.create(
                email        = data['email'],
                password     = decoded_password,
                phone_number = data['phone_number'],
                nickname     = data['nickname'],
            )
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Exception as e:
            return JsonResponse({'message': e})

        return JsonResponse({'message': 'SUCCESS'}, status=201)