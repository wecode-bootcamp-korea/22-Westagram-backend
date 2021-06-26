import json

from django.views import View
from django.http  import JsonResponse
from django.utils import timezone

from postings.models import Posting, Comment, Like
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

class CommentView(View):
    def post(self, request, posting_id):
        data = json.loads(request.body)

        try:
            posting = Posting.objects.get(id=posting_id)
            user    = User.objects.get(email=data['email'])

            Comment.objects.create(
                    posting    = posting,
                    user       = user,
                    created_at = timezone.localtime(),
                    contents   = data['contents']
                    )
            
            return JsonResponse({"message": "SUCCESS"}, status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except Posting.DoesNotExist:
            return JsonResponse({"message": "INVALID_POSTING"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)

    def get(self, request, posting_id):
        try:
            posting  = Posting.objects.get(id=posting_id)
            comments = posting.comment_set.all()

            results = []
            for comment in comments:
                results.append({
                    "user"       : comment.user.nickname,
                    "contents"   : comment.contents,
                    "created_at" : comment.created_at,
                    })  
            
            return JsonResponse({"results": results}, status=200)

        except Posting.DoesNotExist:
            return JsonResponse({"message": "INVALID_POSTING"}, status=400)

class LikeView(View):
    def post(self, request, posting_id, user_id):
        try:
            posting = Posting.objects.get(id=posting_id)
            user = User.objects.get(id=user_id)

            Like.objects.create(posting=posting, user=user)
            
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except Posting.DoesNotExist:
            return JsonResponse({"message": "INVALID_POSTING"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)

    def get(self, request, posting_id):
        try:
            posting = Posting.objects.get(id=posting_id)
            results = [user.nickname for user in posting.like_user.all()]
            
            return JsonResponse({"results": results}, status=200)
        
        except Posting.DoesNotExist:
            return JsonResponse({"message": "INVALID_POSTING"}, status=400)
