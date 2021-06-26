import json

from django.http  import JsonResponse
from django.views import View
from django.utils import timezone

from postings.models import Post
from user.models     import User

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

        return JsonResponse({'message': 'SUCCESS'}, status=200)
    
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
        
        return JsonResponse({'results': results}, status=201)