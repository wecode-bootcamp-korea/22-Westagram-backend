import json
from django.http.response import JsonResponse

from django.views import View
from django.utils import timezone

from user.models import User
from postings.models import Posting, Comment, Like

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

    def delete(self, request, post_id):
        Posting.objects.filter(id=post_id).delete()

        return JsonResponse({'message': 'DELETED'}, status=200)

    def put(self, request, post_id):
        data = json.loads(request.body)
        post = Posting.objects.filter(id=post_id)
        updated_at = timezone.now()
        post.update(image_url=data['image_url'], text=data['text'], updated_at=updated_at)

        return JsonResponse({'message': 'UPDATED'}, status=200)

class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)

        Comment.objects.create(
            post = Posting.objects.get(id=data['post']),
            user = User.objects.get(id=data['user']),
            text = data['text']
        )

        return JsonResponse({'message': 'SUCCESS'}, status=201)

    def get(self, request):
        comments = Comment.objects.all()
        posts = Posting.objects.all()
        results = []
        for post in posts:
            comments = Comment.objects.filter(post=post.id)
            results.append(
                {
                    'post': post.id,
                    'user': post.user.id,
                    'comments': [{'user': comment.user.id, 'text': comment.text} for comment in comments]
                }
            )
        return JsonResponse({'results': results}, status=200)

    def delete(self, request, comment_id):
        Comment.objects.filter(id=comment_id).delete()

        return JsonResponse({'message': 'DELETED'}, status=200)

    def put(self, request, comment_id):
        data = json.loads(request.body)
        post = Posting.objects.filter(id=comment_id)
        post.update(text=data['text'])

        return JsonResponse({'message': 'UPDATED'}, status=200)
        
class LikeView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        # Like
        if not Like.objects.filter(post=data['post'], user=data['user']).exists():
            Like.objects.create(
                post = Posting.objects.get(id=data['post']),
                user = User.objects.get(id=data['user'])
            )
        
        #UnLike
        else:
            Like.objects.filter(post=data['post'], user=data['user']).delete()

        return JsonResponse({'message': 'SUCCESS'}, status=201)

    def get(self, request):
        posts = Posting.objects.all()
        results = []
        for post in posts:
            likers = Like.objects.filter(post=post.id)
            results.append(
                {
                    'post': post.id,
                    'likes_count': Like.objects.filter(post=post.id).count(),
                    'likers': [liker.user.id for liker in likers]
                }
            )
        return JsonResponse({'results': results}, status=200)
