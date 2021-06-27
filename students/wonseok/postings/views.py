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

class DeletePostView(View):
    def post(self, request, post_id):
        try:
            data          = json.loads(request.body)
            post_instance = Post.objects.get(id=post_id)
            user_instance = User.objects.get(id=data["user_id"])
            if post_instance.user != user_instance:
                raise ValidationError(message="USER_NOT_MATCH")
            post_instance.delete()
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message":"JSON_DECODE_ERROR"}, status=400)
        except ValidationError as error:
            return JsonResponse({"message":error.message}, status=400)
        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status=400)
        except Post.DoesNotExist:
            return JsonResponse({"message":"POST_NOT_EXIST"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message":"USER_NOT_EXIST"}, status=400)
        except Exception as error:
            print(error.__class__)
            return JsonResponse({"message":"UNCAUGHT_ERROR"}, status=400)
        return JsonResponse({"message":"success"}, status=201)

class LikePostView(View):
    def post(self, request, post_id):
        try:
            data        = json.loads(request.body)
            post_object = Post.objects.get(id=post_id)
            user_object = User.objects.get(id=data["user_id"])
            if post_object.liked_user.filter(id=user_object.id).exists():
                user_object.liked_post.remove(post_object)
            else:
                user_object.liked_post.add(post_object)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message":"JSON_DECODE_ERROR"}, status=400)
        except Post.DoesNotExist:
            return JsonResponse({"message":"POST_NOT_EXIST"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message":"USER_NOT_EXIST"}, status=400)
        except Exception as error:
            print(error.__class__.__name__)
            return JsonResponse({"message":"UNCAUGHT_ERROR"}, status=400)
        return JsonResponse({"message":"success"}, status=201)

class CreateCommentView(View):
    def post(self, request, post_id):
        try:
            data    = json.loads(request.body)
            user    = User.objects.get(id=data["user_id"])
            post    = Post.objects.get(id=post_id)
            content = data["content"]
            Comment.objects.create(user=user, post=post, content=content)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message":"JSON_DECODE_ERROR"}, status=400)
        except Post.DoesNotExist:
            return JsonResponse({"message":"POST_NOT_EXIST"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message":"USER_NOT_EXIST"}, status=400)
        except Exception as error:
            print(error.__class__.__name__)
            return JsonResponse({"message":"UNCAUGHT_ERROR"}, status=400)
        return JsonResponse({"message":"success"}, status=201)

class ReadCommentView(View):
    def get(self, request, post_id):
        post              = Post.objects.get(id=post_id)
        comments_queryset = Comment.objects.filter(post=post)
        comments          = []
        for comment_object in comments_queryset:
            comment = {
                "user_nick_name" : comment_object.user.nick_name,
                "content" : comment_object.content,
                "created_at" : comment_object.created_at
            }
            comments.append(comment)
        return JsonResponse({"message":"success", "result":comments}, status=201)

class DeleteCommentView(View):
    def post(self, request, post_id):
        try:
            data             = json.loads(request.body)
            user_instance    = User.objects.get(id=data["user_id"])
            comment_instance = Comment.objects.get(id=data["comment_id"])
            print(comment_instance.user == user_instance)
            if comment_instance.user != user_instance:
                raise ValidationError(message="USER_NOT_MATCH")
            comment_instance.delete()
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message":"JSON_DECODE_ERROR"}, status=400)
        except ValidationError as error:
            return JsonResponse({"message":error.message}, status=400)
        except ValueError:
            return JsonResponse({"message": "VALUE_ERROR"}, status=400)
        except Comment.DoesNotExist:
            return JsonResponse({"message":"COMMENT_NOT_EXIST"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message":"USER_NOT_EXIST"}, status=400)
        except Exception as error:
            print(error.__class__)
            return JsonResponse({"message":"UNCAUGHT_ERROR"}, status=400)
        return JsonResponse({"message":"success"}, status=201)

class LikeCommentView(View):
    def post(self, request, post_id):
        try:
            data = json.loads(request.body)
            comment_object = Comment.objects.get(id=data["comment_id"])
            user = User.objects.get(id=data["user_id"])
            if comment_object.liked_user.filter(id=user.id):
                comment_object.liked_user.remove(user)
            else:
                comment_object.liked_user.add(user)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except JSONDecodeError:
            return JsonResponse({"message":"JSON_DECODE_ERROR"}, status=400)
        except Comment.DoesNotExist:
            return JsonResponse({"message":"COMMENT_NOT_EXIST"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message":"USER_NOT_EXIST"}, status=400)
        except Exception as error:
            print(error.__class__.__name__)
            return JsonResponse({"message":"UNCAUGHT_ERROR"}, status=400)
        return JsonResponse({"message":"success"}, status=201)
