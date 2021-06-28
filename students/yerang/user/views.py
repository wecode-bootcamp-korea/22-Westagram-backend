import json

from json.decoder import JSONDecodeError

from django.http  import JsonResponse
from django.views import View

from user.models     import User

class SignInView(View):
    def post(self, request):
        data     = json.loads(request.body)
       
        try:
            email    = data['email']
            password = data['password']
            user = User.objects.get(email=email)

            if user.password != password:
                return JsonResponse({'message': 'INVALID_USER'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)
        except ValueError:
            return JsonResponse({'message': 'VALUE_ERROR'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        return JsonResponse({'message': 'SUCCESS'}, status=200)