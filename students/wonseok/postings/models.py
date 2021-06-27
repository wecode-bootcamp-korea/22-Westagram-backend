from django.db import models

from user.models import User

class Post(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="own_post")
    liked_user  = models.ManyToManyField(User,through="PostLikeUser", related_name="liked_post")
    image_url   = models.URLField()
    content     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    class Meta():
        db_table = "posts"

class PostLikeUser(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    post        = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    class Meta():
        db_table = "posts_like_users"

class Comment(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    post        = models.ForeignKey(Post, on_delete=models.CASCADE)
    content     = models.TextField()
    liked_user  = models.ManyToManyField(User,through="CommentLikeUser", related_name="liked_comment")
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = "comments"

class CommentLikeUser(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    comment     = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    class Meta():
        db_table = "comments_like_users"