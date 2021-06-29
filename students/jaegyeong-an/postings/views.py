import json
from django.http   import JsonResponse
from django.views  import View
from django.utils  import timezone

from .models import User, Posting

class WriteView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(nickname = data['user'])
            Posting.objects.create(
                user        = user,
                created_at  = timezone.localtime(),
                image_url   = data['image_url'],
                description = data['description']
                )
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'error':'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'error':'INVALID_USER'}, status=400)

class PostingsView(View):
    def get(self, request):
        postings = Posting.objects.all()
        results = [{
            'user'        : posting.user.nickname,
            'created_at'  : posting.created_at,
            'image_url'   : posting.image_url,
            'description' : posting.description
        } for posting in postings]
        return JsonResponse({'results':results}, status=200)