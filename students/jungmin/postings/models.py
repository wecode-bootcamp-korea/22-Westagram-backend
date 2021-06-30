from user.models import User
from django.db import models
from django.db.models.fields.files import ImageField
from django.utils import timezone

class Posting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
    image_url = models.CharField(max_length=1000)
    text = models.TextField()

    class Meta:
        db_table = 'postings'


