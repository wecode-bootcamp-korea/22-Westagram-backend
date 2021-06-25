import json

from django.http  import JsonResponse
from django.views import View

from user.models import User

class SignInView(View):
    def post(self, request):
        data     = json.loads(request.body)
        email    = data['email']
        password = data['password']

        if not (email and password):
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        if not User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

        if User.objects.get(email=email).password != password:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

        return JsonResponse({'message': 'SUCCESS'}, status=200)