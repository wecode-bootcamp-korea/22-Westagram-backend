from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=30) 
    email        = models.EmailField(unique=True)
    password     = models.CharField(max_length=20)
    nickname     = models.CharField(max_length=20,unique=True)
    phone_number = models.CharField(max_length=20,unique=True)

    class Meta:
        db_table = 'users'

