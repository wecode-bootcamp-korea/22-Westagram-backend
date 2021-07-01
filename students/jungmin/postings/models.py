from user.models import User
from django.db import models
from django.utils import timezone

class Posting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
    image_url = models.CharField(max_length=1000)
    text = models.TextField()

    class Meta:
        db_table = 'postings'

class Comment(models.Model):
    post = models.ForeignKey('Posting', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', blank=True, on_delete=models.CASCADE),
    created_at = models.DateTimeField(default=timezone.now, blank=True),
    text = models.TextField()

    class Meta:
        db_table = 'comments'

