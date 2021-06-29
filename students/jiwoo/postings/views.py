import json 

from django.http             import JsonResponse
from django.views            import View 

from postings.models         import Post, Comment, Like
from users.models            import User


class CreatePostsView(View): 
    def  post(self, request): 
        try: 
            data = json.loads(request.body)
            user = User.objects.get(name=data['name'])
            Post.objects.create(
                user      = user,
                title     = data['title'],
                content   = data['content'],
                image_url = data['image_url']
            )            
            return JsonResponse({"message":"SUCCESS"},status =201)
        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status=400)

    def get(self, request): 
        results = [({"user" : user.name, "post" : [(post.title, post.content, post.created_at) for post in user.post_set.all()]}) for user in User.objects.all()]
        return JsonResponse({"results":results}, status = 200)


class CreateCommentsView(View): 
    def post(self, request): 
        try: 
            data = json.loads(request.body)
            user = User.objects.get(name=data['name'])
            post = Post.objects.get(title=data['title'])
            Comment.objects.create(
                user    = user,
                post    = post,
                content = data['content']
            )
            return JsonResponse({"message":"SUCCESS"}, status =201)        
        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status=400)

    def get(self, request):         
        results = [({"post": post.title, "comment": [(comment.content, comment.created_at, comment.user.name) for comment in post.comment_set.all()]}) for post in Post.objects.all()]
        return JsonResponse({"results":results}, status=200)

class CreateLikesView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(name=data['name'])
            post = Post.objects.get(title=data['title'])
            Like.objects.create(
                user = user,
                post = post
            )
            return JsonResponse({"message":"SUCCESS"},status=201)
        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status=400)

    def get(self, request):
        results = [({"user":user.name,"like": [(like.user.name, like.post.title) for like in user.like_set.all()]}) for user in User.objects.all()]
        return JsonResponse({"results":results},status =200)