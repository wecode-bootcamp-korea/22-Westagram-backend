from django.db import models

class User(models.Model):
    email    = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    phone    = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)

    class Meta:
        db_table = 'users'