from django.db import models

class User(models.Model):
    email    = models.CharField(max_length=320, unique=True)
    password = models.CharField(max_length=200)
    phone    = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    following = models.ManyToManyField(
            'self',
            through='Follow', 
            symmetrical=False, 
            related_name='followed'
            )

    class Meta:
        db_table = 'users'

class Follow(models.Model):
    follower = models.ForeignKey('User', on_delete=models.CASCADE, related_name='follower')
    followee = models.ForeignKey('User', on_delete=models.CASCADE, related_name='followee')

    class Meta:
        db_table = 'follows'

