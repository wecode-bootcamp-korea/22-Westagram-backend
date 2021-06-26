import json

from django.views import View
from django.http  import JsonResponse
from django.utils import timezone

from postings.models import Posting
from users.models    import User

class PostingView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            user = User.objects.get(email=data['email'])

            Posting.objects.create(
                user       = user,
                created_at = timezone.localtime(),
                image_url  = data['image_url']
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)

    def get(self, request):
        postings = Posting.objects.all() 

        results = []
        for posting in postings:
            results.append({
                "nickname"   : posting.user.nickname,
                "image_url"  : posting.image_url,
                "created_at" : posting.created_at,
            })
        return JsonResponse({"results": results}, status=200)

