import json

from django.http        import JsonResponse
from django.views       import View
from accounts.models    import Account

class SignInView(View):
    def post(self, request):
        data         = json.loads(request.body)
        
        try:
            if not (data['email'] and data['password']):
                return JsonResponse({"message": "KEY_ERROR1"}, status=400)

            if Account.objects.filter(email=data['email']).exists():
                email = Account.objects.get(email=data['email'])
                if email.password == data['password']:
                    return JsonResponse({"message": "SUCCESS"}, status=200)
                else: 
                    return JsonResponse({"message": "INVALID_PASSWORD"}, status=401)
            return JsonResponse({"message": "INVALID_USER"}, status=401)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR2"}, status=400)
            

