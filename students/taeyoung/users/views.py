import json

from django.views   import View
from django.http    import JsonResponse

from users.models import Account

class SignInView(View):
    def post(self, request):
        signin_data = json.loads(request.body)
        
        try:
            if Account.objects.filter(email=signin_data['email']).exists():
                email = Account.objects.get(email=signin_data['email'])
                if email.password == signin_data['password']:
                    return JsonResponse({'message': 'SUCCESS'}, status=200)
                else: 
                    return JsonResponse({'message': 'INAVLID_PASSWORD'}, status=401)
            else: 
                return JsonResponse({'message': 'INVALID_USER'}, status=401)

        except KEYERROR:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)
