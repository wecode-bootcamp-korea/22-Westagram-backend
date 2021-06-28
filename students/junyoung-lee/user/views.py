import json

from django.core.exceptions import MultipleObjectsReturned
from django.http     import JsonResponse
from django.views    import View

from user.models     import User

class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            User.objects.get(email=data['email'], password=data['password'])
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except MultipleObjectsReturned:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)