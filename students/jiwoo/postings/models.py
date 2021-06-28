from django.db import models

# Create your models here.

class Post(models.Model): 
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    content = models.CharField(max_length = 1000)
    image_url = models.URLField
    created_at = 
    updated_at = 

    class Meta: 
        db_table = 'posts'