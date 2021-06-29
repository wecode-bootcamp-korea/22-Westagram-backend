from django.db import models

# Create your models here.

class Post(models.Model): 
    user       = models.ForeignKey('users.User',on_delete=models.CASCADE)
    title      = models.CharField(max_length= 100)
    content    = models.CharField(max_length = 1000)
    image_url  = models.URLField(max_length = 200)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    class Meta: 
        db_table = 'posts'

class Comment(models.Model): 
    user       = models.ForeignKey('users.User',on_delete=models.CASCADE)
    post       = models.ForeignKey('Post', on_delete=models.CASCADE)
    content    = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        db_table = 'comments'


class Like(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'