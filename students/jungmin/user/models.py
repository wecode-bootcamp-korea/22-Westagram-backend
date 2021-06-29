from django.db import models

class User(models.Model):
    email    = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    phone    = models.CharField(max_length=20, blank=True, unique=True)
    nickname = models.CharField(max_length=20, blank=True, unique=True)

    class Meta:
        db_table = 'users'