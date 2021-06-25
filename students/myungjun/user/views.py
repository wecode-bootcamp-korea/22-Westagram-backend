import json

from django.http import JsonResponse
from django.views import View

from user.models import User


class UserView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            User.objects.create(
                name=data['name'],
                email=data['email'],
                password=data['password'],
                phone=data['phone'],
                nickname=data['nickname']
            )

        except Exception as e:
            return JsonResponse({"message": "Error"})
        return JsonResponse({'message': 'SUCCESS'}, status=201)
