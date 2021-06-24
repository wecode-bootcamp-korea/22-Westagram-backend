from django.db import models


class User(models.Model):
    name     = models.CharField(unique=True, max_length=30)
    email    = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    phone    = models.IntegerField(unique=True, max_length=11)
    nickname = models.CharField(max_length=30)

    class Meta:
        db_table = "users"