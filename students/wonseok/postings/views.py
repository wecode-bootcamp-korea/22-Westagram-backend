import json
from json.decoder import JSONDecodeError
from django.core.exceptions import ValidationError
from django.db.utils import Error

from django.http.response import JsonResponse
from django.views import View

from user.models import User
from postings.models import Post

class RegisterPostView(View):
    def post(self, request):
        try:
            data = json.loads(request.body) 
            if User.objects.filter(id=data["user_id"]):
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
            return JsonResponse({"message":"UNCAUGHT_ERROR"}, status=400)
        return JsonResponse({"message":"success"}, status=201)

class ShowPostView(View):
    def get(self, request):
        posts_queryset = Post.objects.all()
        all_posts = []
        for p in posts_queryset:
            user = {
                "nick_name":p.user.nick_name,
                "email":p.user.email,
                "phone_number":p.user.phone_number,
                "created_at":p.user.created_at,
            }
            post = {
                "user":user,
                "image_url":p.image_url,
                "content":p.content,
                "created_at":p.created_at
            }
            all_posts.append(post)
        return JsonResponse({"message":"success", "result":all_posts}, status=200)