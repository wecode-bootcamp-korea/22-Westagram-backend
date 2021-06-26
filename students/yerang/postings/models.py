from django.db                 import models
from django.db.models.deletion import CASCADE

from user.models import User

class Post(models.Model):
    user       = models.ForeignKey(User, on_delete=CASCADE, null=False)
    created_at = models.DateTimeField()
    image_url  = models.URLField(max_length=200)

    class Meta:
        db_table = 'posts'

class Comment(models.Model):
    post       = models.ForeignKey(Post, on_delete=CASCADE, null=False)
    user       = models.ForeignKey(User, on_delete=CASCADE, null=False)
    created_at = models.DateTimeField()
    comment    = models.TextField(max_length=300, null=False)

    class Meta:
        db_table = 'comments'