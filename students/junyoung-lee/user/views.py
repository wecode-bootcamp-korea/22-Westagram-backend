import json

from django.http     import JsonResponse
from django.views    import View

from user.models     import User

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if 'email' in data:
                User.objects.get(email=data['email'], password=data['password'])
            
            elif 'phone_number' in data:
                User.objects.get(phone_number=data['phone_number'], password=data['password'])
            
            else:
                return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
                
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)