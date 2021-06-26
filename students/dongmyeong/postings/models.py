from django.db import models

class Posting(models.Model):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url  = models.URLField(max_length=2000)

    class Meta:
        db_table = 'postings'
    
    def __str__(self):
        return ', '.join([self.id, self.user, self.created_at, self.updated_at, self.image_url])

