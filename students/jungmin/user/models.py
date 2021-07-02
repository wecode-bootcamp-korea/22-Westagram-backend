from django.db import models

class User(models.Model):
    email    = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    phone    = models.CharField(max_length=20, blank=True, unique=True)
    nickname = models.CharField(max_length=20, blank=True, unique=True)
    follow   = models.ManyToManyField('self', blank=True, symmetrical=False)

    class Meta:
        db_table = 'users'

class Follow(models.Model):
    user_following = models.ForeignKey('User', on_delete=models.CASCADE, related_name='following')
    user_followed  = models.ForeignKey('User', on_delete=models.CASCADE, related_name='followed')

    class Meta:
        db_table = 'follows'