from typing                     import Tuple
from django.db                  import models
from django.db.models.deletion  import CASCADE
from django.db.models.fields import related

from users.models               import User

class Post(models.Model):
    img             = models.URLField(max_length=1000)
    content         = models.TextField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user            = models.ForeignKey('users.User', related_name="posts", on_delete=CASCADE)
    
    class Meta:
        db_table    = 'posts'

class Comment(models.Model):
    content         = models.TextField()
    post            = models.ForeignKey('Post', related_name='main_comments', on_delete=CASCADE)
    users           = models.ForeignKey('User', related_name='user_comments', on_delete=CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table    = 'comments'