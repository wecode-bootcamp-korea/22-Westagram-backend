from django.db                 import models
from django.db.models.deletion import CASCADE

class User(models.Model): 
    email        = models.EmailField(max_length=45, unique=True)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=45, unique=True)
    nickname     = models.CharField(max_length=45, unique=True)
    liked_posts  = models.ManyToManyField('postings.Post', related_name='liked_users', through='Like')

    class Meta:
        db_table = 'users'

class Like(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('postings.Post', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'