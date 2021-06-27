import json

from django.db.models.fields.json import JSONExact
from django.http                  import JsonResponse
from django.views                 import View

from posts.models                 import Post

class PostView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        Post.objects.create(
            img     = data["img"],
            content = data["content"],
            user    = data["user_id"],
        )
        
    def get(self, request):
        posts = Post.objects.all()
        
        result = []

        for post in posts:
            result.append({
                "user": post.user.nick_name,
                "img": post.img,
                "content": post.content,
                "created_at": post.created_at,
            })

        return JsonResponse({"result" : result}, status=200)
