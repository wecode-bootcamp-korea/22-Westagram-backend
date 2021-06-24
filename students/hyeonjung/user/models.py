from django.db import models
from django.db.models.deletion import CASCADE

class User(models.Model):
    name = models.CharField(max_length=30) 
    email = models.EmailField()
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'users'

