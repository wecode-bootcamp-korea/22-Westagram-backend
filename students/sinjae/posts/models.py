from typing                     import Tuple
from django.db                  import models
from django.db.models.deletion  import CASCADE

from users.models               import User

class Post(models.Model):
    img             = models.URLField(max_length=400)
    content         = models.TextField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user            = models.ForeignKey('users.User', related_name="posts", on_delete=CASCADE)
    
    class Meta:
        db_table    = 'posts'