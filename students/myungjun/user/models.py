from django.db import models

class User(models.Model):
    name     = models.CharField(max_length=50, unique=True)
    email    = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    phone    = models.IntegerField(max_length=30, unique=True)
    nickname = models.CharField(max_length=50)

    class Meta:
        db_table = "users"