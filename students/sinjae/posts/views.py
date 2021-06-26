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
        
    