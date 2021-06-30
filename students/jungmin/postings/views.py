import json
from django.http.response import JsonResponse

from django.views import View

from user.models import User
from postings.models import Posting

class PostingView(View):
    def post(self, request):
        data = json.loads(request.body)
        Posting.objects.create(
            user = User.objects.get(id=data['user']),
            image_url = data['image_url'],
            text = data['text']
        )

        return JsonResponse({'message': 'SUCCESS'}, status=201)

    def get(self, request):
        postings = Posting.objects.all()
        results = []
        for posting in postings:
            results.append(
                {
                    'user': posting.user.id,
                    'created_at': posting.created_at,
                    'updated_at': posting.updated_at,
                    'image_url': posting.image_url,
                    'text': posting.text
                }
            )

            return JsonResponse({'results': results}, status=200)