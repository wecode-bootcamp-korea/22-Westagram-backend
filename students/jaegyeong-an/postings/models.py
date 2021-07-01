from typing_extensions import TypeGuard
from django.db   import models
from django.db.models.fields import CharField, TextField

from user.models import User

class Posting(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    image_url   = models.URLField()
    description = models.TextField()

    class Meta:
        db_table = 'postings'

class Comment(models.Model):
    posting         = models.ForeignKey(Posting, models.CASCADE)
    parents_comment = models.ForeignKey('self', related_name="parents", on_delete=models.CASCADE, null=True, blank=True)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    comment         = TextField()

    class Meta:
        db_table = 'comments'
