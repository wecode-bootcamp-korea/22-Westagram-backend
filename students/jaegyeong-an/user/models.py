from django.db import models

class User(models.Model):
    email        = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=100, unique=True, blank=True)
    name         = models.CharField(max_length=100, blank=True)
    nickname     = models.CharField(max_length=100, unique=True, blank=True)
    password     = models.CharField(max_length=200)

    class Meta:
        db_table = 'users'