from django.db import models

from user.models import User

class Post(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url   = models.URLField()
    content     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = "posts"
