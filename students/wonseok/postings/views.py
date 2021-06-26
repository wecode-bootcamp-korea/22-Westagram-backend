import json

from django.views import View
from django.http.response import JsonResponse
from django.core.exceptions import ValidationError
from json.decoder import JSONDecodeError

from user.models import User
from postings.models import Comment, Post

class CreatePostView(View):
    def post(self, request):
        try:
            data = json.loads(request.body) 
            if User.objects.filter(id=data["user_id"]).exists():
                user = User.objects.get(id= data["user_id"])
            else:
                raise ValidationError(message="USER_DOESN'T EXIST")
            image_url = data["image_url"]
            content   = data["content"]
            Post.objects.create(user=user, image_url=image_url, content=content)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message":"JSON_DECODE_ERROR"}, status=400)
        except ValidationError as error:
            return JsonResponse({"message":error.message}, status=400)
        except Exception as error:
            print(error)
            return JsonResponse({"message":"UNCAUGHT_ERROR"}, status=400)
        return JsonResponse({"message":"success"}, status=201)

class ReadPostView(View):
    def get(self, request):
        posts_queryset = Post.objects.all()
        all_posts = []
        for post_object in posts_queryset:
            user = {
                "nick_name":post_object.user.nick_name,
                "email":post_object.user.email,
                "phone_number":post_object.user.phone_number,
                "created_at":post_object.user.created_at,
            }
            post = {
                "user":user,
                "image_url":post_object.image_url,
                "content":post_object.content,
                "created_at":post_object.created_at
            }
            all_posts.append(post)
        return JsonResponse({"message":"success", "result":all_posts}, status=200)

class CreateCommentView(View):
    def post(self, request):
        try:
            data    = json.loads(request.body)
            print(data)
            user    = User.objects.get(id=data["user_id"])
            post    = Post.objects.get(id=data["post_id"])
            content = data["content"]
            comment = Comment.objects.create(user=user, post=post, content=content)
            print(comment)
        except Exception as error:
            print(error)
            return JsonResponse({"message":"UNCAUGHT_ERROR"}, status=400)
        return JsonResponse({"message":"success"}, status=201)
