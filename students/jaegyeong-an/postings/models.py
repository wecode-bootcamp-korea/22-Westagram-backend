from django.db   import models

from user.models import User

class Posting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField()
    description = models.TextField()

    class Meta:
        db_table = 'postings'