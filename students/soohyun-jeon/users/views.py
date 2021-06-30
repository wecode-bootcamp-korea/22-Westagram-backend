import re,json,bcrypt,jwt

from django.core.exceptions import MultipleObjectsReturned
from django.views           import View
from django.http            import JsonResponse

from users.models           import User
from users.validators       import validate_email, validate_password
from my_settings            import SECRET_KEY

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if not validate_email(data['email']):
                return JsonResponse({'MESSAGE': 'INVALID_EMAIL'}, status=400)

            if not validate_password(data['password']):
                return JsonResponse({'MESSEAGE': 'INVALID_PASSWORD'}, status=400)

            encoded_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            
            User.objects.create(
                phone_number =data['phone_number'],
                email        =data['email'],
                name         =data['name'],
                nickname     =data['nickname'],
                password     =encoded_password.decode('utf-8')
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KeyError'}, status=404)

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            user = User.objects.get(email=data['email'])
            if bcrypt.checkpw(data['password'].encode('utf-8'),user.password.encode('utf-8')):
                encoded_jwt = jwt.encode({'email':user.email}, SECRET_KEY, algorithm='HS256')
                return JsonResponse({'message': 'SUCCESS','TOKEN':encoded_jwt}, status=200)
            
            return JsonResponse({'messege':'INVALID_USER'},status=401)
        
        except KeyError:
            return JsonResponse({'messege': 'KeyError'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message': 'Invalid_User'}, status=401)

        except MultipleObjectsReturned:
            return JsonResponse({'message': 'Invalid_User'}, status=401)