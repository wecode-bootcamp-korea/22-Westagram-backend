import json

from django.http  import JsonResponse
from django.views import View
from django.utils import timezone

from postings.models import Post, Comment
from user.models     import User, Like

class PostView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            user       = User.objects.get(email=data['email'])
            created_at = timezone.now()
            image_url  = data['image_url']

            Post.objects.create(
                user       = user,
                created_at = created_at,
                image_url  = image_url,
            )
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)
        except Exception as e:
            return JsonResponse({'message': e})

        return JsonResponse({'message': 'SUCCESS'}, status=201)
    
    def get(self, request):
        results = []
        
        for post in Post.objects.all():
            results.append(
                {
                    'publisher' : f'Email: {post.user.email} / NickName: {post.user.nickname}',
                    'post_id'   : post.id,
                    'image_url' : post.image_url,
                    'created_at': post.created_at,
                }
            )
        
        return JsonResponse({'results': results}, status=200)

class CommentView(View):
    def post(self, request, post_id):
        data = json.loads(request.body)

        try:
            user       = User.objects.get(email=data['email'])
            post       = Post.objects.get(id=post_id)
            created_at = timezone.now()
            comment    = data['comment']

            Comment.objects.create(
                user       = user,
                post       = post,
                created_at = created_at,
                comment    = comment,
            )
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)
        except Exception as e:
            return JsonResponse({'message': e})

        return JsonResponse({'message': 'SUCCESS'}, status=201)

    def get(self, request, post_id):
        if not Post.objects.filter(id=post_id).exists():
            return JsonResponse({'message': 'POST_DOES_NOT_EXISTS'}, status=400)
            
        comments = Comment.objects.filter(post_id=post_id)
        results = [comment.comment for comment in comments]
        
        return JsonResponse({'results': results}, status=200)

class LikeView(View):
    def post(self, request, post_id, user_id):
        try:
            if not Post.objects.filter(id=post_id).exists():
                return JsonResponse({'message': 'POST_DOES_NOT_EXISTS'}, status=400)
                
            if not User.objects.filter(id=user_id).exists():
                return JsonResponse({'message': 'USER_DOES_NOT_EXISTS'}, status=400)

            Like.objects.create(
                post_id = post_id,
                user_id = user_id,
            )
        except Exception as e:
            return JsonResponse({'message': e})

        return JsonResponse({'message': 'SUCCESS'}, status=201)

    def get(self, request, post_id):
        if not Post.objects.filter(id=post_id).exists():
            return JsonResponse({'message': 'POST_DOES_NOT_EXISTS'}, status=400)
        
        results = []
        post = Post.objects.get(id=post_id)
        count = post.liked_users.count()

        for liked_user in post.liked_users.all():
            results.append(
                {
                    'NickName': liked_user.nickname,
                    'Email'   : liked_user.email,
                }
            )


        return JsonResponse({f'{count}명이 좋아합니다.': results}, status=200)