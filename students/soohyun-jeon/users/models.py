from django.db import models

class User(models.Model):
    phone_number = models.CharField(max_length=30, unique=True)
    email        = models.EmailField(max_length=50, unique=True)
    name         = models.CharField(max_length=30)
    nickname     = models.CharField(max_length=30)
    password     = models.CharField(max_length=200)

    class Meta:
        db_table = 'users'
