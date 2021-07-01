import json
from django.http   import JsonResponse
from django.views  import View
from django.utils  import timezone

from .models       import User, Posting, Comment
from user.utils    import authorization

class WriteView(View):
    @authorization
    def post(self, request):
        try:
            data = json.loads(request.body)
            Posting.objects.create(
                user        = request.user,
                created_at  = timezone.localtime(),
                image_url   = data['image_url'],
                description = data['description'] 
                )
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'error':'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'error':'INVALID_USER'}, status=400)
    
    @authorization
    def put(self, request):
        try:
            data = json.loads(request.body)
            posting = Posting.objects.get(id = data['posting_id'])
            posting.description = data['description']
            posting.updated_at = timezone.localtime()
            posting.save()
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'error':'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'error':'INVALID_USER'}, status=400)

class PostingsView(View):
    @authorization
    def get(self, request):
        postings = Posting.objects.all()
        results = [{
            'user'        : posting.user.nickname,
            'created_at'  : posting.created_at,
            'image_url'   : posting.image_url,
            'description' : posting.description
        } for posting in postings]
        return JsonResponse({'results':results}, status=200)

class CommentsView(View):
    @authorization
    def post(self, request, posting_id):
        try:
            data = json.loads(request.body)
            posting = Posting.objects.get(id = posting_id)
            Comment.objects.create(
                user            = request.user,
                posting         = posting, 
                created_at      = timezone.localtime(),
                updated_at      = timezone.localtime(),
                parents_comment = data['parents_comment'],
                comment         = data['comment']
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'error':'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'error':'INVALID_USER'}, status=400)